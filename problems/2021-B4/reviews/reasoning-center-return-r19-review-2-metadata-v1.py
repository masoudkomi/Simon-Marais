#!/usr/bin/env python3
"""NEW R19 R2 metadata only: no mathematics and no author/old-code replay.

prepare verifies necessary immutable records and creates new baseline/validation.
freeze is run only after FULL model readback of all nine final payloads.
verify is a SEPARATE read-only check after FULL manifest model readback.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DIR = "problems/2021-B4/reviews/"
P = DIR + "reasoning-center-return-r19-review-2-"
A = "problems/2021-B4/notes/reasoning-center-return-r19-"
AUTHOR_MAIN = {
    "path": A + "candidate-v1.md", "bytes": 17591,
    "sha256": "589eddbf5f305b3380ee2c499d774aff8bb1b4499aa46c15c3dbffcf1bd56462",
}
AUTHOR_FREEZE = {
    "path": A + "freeze-v1.json", "bytes": 3893,
    "sha256": "dfe7b6b4f372b44a2806fc96ce41613bfc2fb7e8f5469fc2d10552aa83b835d3",
}
OWN_PARENT = {
    "path": "problems/2017-B4/reviews/coordinator-path-moment-r3-review-2-manifest-v1.json",
    "bytes": 4918,
    "sha256": "8aeb3ac85ffceb69c8eff363e6fcdfe9f7995540fad3428d8295ae05656155a1",
}
BASELINE, VALIDATION, MANIFEST = (
    P + "baseline-v1.json", P + "input-validation-v1.json", P + "manifest-v1.json"
)
STATIC = [
    P + "initial.md", P + "obligations-v1.md", P + "issues-v1.md",
    P + "sources-v1.md", P + "sources-v1.json", P + "worklog-v1.md",
    P + "metadata-v1.py",
]
PAYLOADS = STATIC + [BASELINE, VALIDATION]
DENIED = (
    "problems/2021-B4/reviews/reasoning-center-return-r19-review-1-",
    "problems/2019-B4/reviews/reasoning-cut-transfer-r5-review-",
)
AUTHORITIES = [
    "problems/2021-B4/reviews/reasoning-center-return-r18-acceptance.json",
    "problems/2021-B4/reviews/reasoning-center-return-r17-acceptance.json",
    "problems/2021-B4/reviews/reasoning-return-r8-acceptance.json",
    "problems/2021-B4/reviews/reasoning-return-r5-acceptance.json",
]


def now():
    return datetime.now(timezone.utc).isoformat()


def path(rel):
    assert isinstance(rel, str) and not rel.startswith("/"), rel
    assert not any(rel.startswith(prefix) for prefix in DENIED), rel
    resolved = (ROOT / rel).resolve()
    assert resolved.is_relative_to(ROOT), rel
    return resolved


def fp(rel):
    data = path(rel).read_bytes()
    return {"path": rel, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def load(rel):
    return json.loads(path(rel).read_text(encoding="utf-8"))


def exact(row):
    reduced = {key: row[key] for key in ("path", "bytes", "sha256")}
    actual = fp(row["path"])
    assert actual == reduced, (reduced, actual)
    return reduced


def records(obj):
    """JSON-object traversal only, never recursive opening of referenced files."""
    out = []
    if isinstance(obj, dict):
        rel, size, digest = obj.get("path"), obj.get("bytes"), obj.get("sha256")
        if (isinstance(rel, str) and not rel.startswith(("http:", "https:"))
                and isinstance(size, int) and isinstance(digest, str)
                and re.fullmatch(r"[0-9a-f]{64}", digest)):
            out.append({"path": rel, "bytes": size, "sha256": digest})
        for value in obj.values():
            out.extend(records(value))
    elif isinstance(obj, list):
        for value in obj:
            out.extend(records(value))
    return out


def historical_mutable(rel):
    return (bool(re.fullmatch(r"problems/\d{4}-B4/research\.md", rel))
            or rel == "README.md" or rel.startswith(("progress/", "sources/")))


def canonical(rows):
    unique = {}
    for row in rows:
        reduced = {key: row[key] for key in ("path", "bytes", "sha256")}
        assert row["path"] not in unique or unique[row["path"]] == reduced
        unique[row["path"]] = reduced
    ordered = [unique[key] for key in sorted(unique)]
    raw = json.dumps(ordered, sort_keys=True, separators=(",", ":")).encode()
    return ordered, hashlib.sha256(raw).hexdigest()


def write_new(rel, obj):
    assert rel.startswith(P) and Path(rel).parent.as_posix() == DIR.rstrip("/")
    with path(rel).open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(obj, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


def guard():
    exact(AUTHOR_MAIN)
    exact(AUTHOR_FREEZE)
    author = load(AUTHOR_FREEZE["path"])
    assert author["ENTIRE_files"] == 13 and author["whole_obligations"] == 64
    author_rows = author["payloads"] + [AUTHOR_FREEZE]
    assert len(author_rows) == 13
    for row in author_rows:
        exact(row)

    old = load(A + "baseline-v1.json")
    direct = old["direct_current_inputs"]
    assert len(direct) == 22
    for row in direct:
        exact(row)
    accepted_rows = list(direct)
    compact = []
    skipped_historical = []
    for binding in old["compact_parent_bindings"]:
        parent_row = exact(binding["immutable_parent"])
        declared = records(load(parent_row["path"]))
        assert len(declared) == binding["parent_declared_occurrences"]
        immutable = [row for row in declared if not historical_mutable(row["path"])]
        mutable = [row for row in declared if historical_mutable(row["path"])]
        # Do not read current mutable research/progress/source-index status.
        # The preserved historical declaration is not a current proof premise.
        assert mutable == binding["historical_coordinator_mutable_declarations"]
        skipped_historical.extend(mutable)
        for row in immutable:
            exact(row)
        unique, digest = canonical(immutable)
        assert len(immutable) == binding["current_immutable_declared_occurrences_checked"]
        assert len(unique) == binding["current_immutable_declared_unique_paths_checked"]
        assert digest == binding["current_immutable_declared_canonical_sha256"]
        accepted_rows.extend(immutable)
        compact.append({
            "immutable_parent": parent_row,
            "declared_occurrences": len(declared),
            "immutable_occurrences_verified": len(immutable),
            "immutable_unique_paths_verified": len(unique),
            "immutable_canonical_sha256": digest,
            "historical_mutable_declarations_skipped_not_current_premises": mutable,
            "historical_parent_summary_not_reexpanded": binding[
                "parent_historical_summary_not_fresh_recursive_model_read"],
        })
    assert len(compact) == 8
    accepted_unique, accepted_digest = canonical(accepted_rows)
    assert len(accepted_rows) == old["protected_current_occurrences"] == 205
    assert len(accepted_unique) == old["protected_current_unique_paths"] == 131
    assert accepted_digest == old["canonical_deduplicated_sha256"]
    assert accepted_digest == "783e7de0f846c6f0fd91a3f3bfb0b7f3a564968f805efb6a244ad6805e9bad34"

    exact(OWN_PARENT)
    own = load(OWN_PARENT["path"])
    own_rows = own["payloads"] + [OWN_PARENT]
    assert len(own_rows) == 10
    assert own["older_plus_new_own_paths_bound_transitively"] == 803
    for row in own_rows:
        exact(row)

    total = author_rows + accepted_rows + own_rows
    unique, digest = canonical(total)
    assert len(total) == 228 and len(unique) == 154
    direct_unique, _ = canonical(author_rows + direct + own_rows)
    assert len(direct_unique) == 45
    by_path = {row["path"]: row for row in unique}
    suffixes = []
    for rel in AUTHORITIES:
        authority = load(rel)
        assert "proved" in authority["status"] and "independently" in authority["status"]
        body, candidate = authority["accepted_copy"], authority["candidate"]
        assert exact(body) == by_path[body["path"]]
        assert exact(candidate) == by_path[candidate["path"]]
        assert path(body["path"]).read_bytes().endswith(path(candidate["path"]).read_bytes())
        md = rel[:-5] + ".md"
        suffixes.append({
            "authority_json": exact(by_path[rel]),
            "authority_md": exact(by_path[md]),
            "accepted_body": body,
            "unchanged_original_candidate_suffix": candidate,
            "suffix_matches": True,
            "old_occurrences_bound_not_reexpanded": authority["record_occurrences_verified"],
            "old_unique_paths_bound_not_reexpanded": authority["unique_paths_verified"],
            "COMPLETE_current_body_and_MDJSON_model_read": True,
        })
    return {
        "necessary_guard_occurrences": len(total),
        "necessary_guard_unique_paths": len(unique),
        "necessary_guard_canonical_sha256": digest,
        "direct_guard_records": direct_unique,
        "compact_declared_parent_bindings": compact,
        "constructor_necessary_immutable_summary": {
            "occurrences": 205, "unique_paths": 131, "canonical_sha256": accepted_digest},
        "historical_mutable_declarations_not_currently_read_or_asserted_unchanged": skipped_historical,
        "accepted_candidate_suffix_bindings": suffixes,
        "immediate_own_parent": OWN_PARENT,
        "older_own_paths_bound_transitively": 803,
        "author_ENTIRE_files": 13,
        "own_parent_ENTIRE_files": 10,
        "historical_inventory_copied_or_recursively_opened": False,
        "NEW_corresponding_root_R19_or_pending_BT_peer_material_accessed": False,
    }


def labels():
    wanted = [f"{number:02d}" for number in range(1, 65)]
    expression = r"(?m)^\|R19-(\d{2})\|"
    assert re.findall(expression, path(A + "obligations-v1.md").read_text()) == wanted
    assert re.findall(expression, path(P + "obligations-v1.md").read_text()) == wanted
    issue = path(P + "issues-v1.md").read_text()
    assert re.findall(r"(?m)^## (R19R2-\d{2}) —", issue) == ["R19R2-01"]
    assert re.findall(r"(?m)^\|R19R2-N([1-6])\|", issue) == list("123456")
    sources = load(P + "sources-v1.json")
    assert sources["whole_hand_obligations"] == 64
    assert sources["NEW_root_R19_peer_material_accessed"] is False
    assert sources["NEW_R19_contribution"] is False
    assert sources["prototype_is_actual_degree20_counterexample"] is False
    return {"author_obligation_labels": 64, "review_separate_hand_dispositions": 64,
            "required_issue_labels": 1, "closed_note_labels": 6,
            "mathematical_assertions_evaluated_by_code": False}


def prepare():
    existing = sorted(p.relative_to(ROOT).as_posix()
                      for p in (ROOT / DIR).glob("reasoning-center-return-r19-review-2-*"))
    assert existing == sorted(STATIC), existing
    summary = guard()
    label_counts = labels()
    write_new(BASELINE, {"created_at_utc": now(),
                        "purpose": "NEW compact reviewer metadata; not mathematical verification",
                        "author_main": AUTHOR_MAIN, "author_freeze": AUTHOR_FREEZE,
                        **summary})
    write_new(VALIDATION, {
        "checked_at_utc": now(), "pass": True, "baseline": fp(BASELINE),
        "necessary_guard_occurrences": summary["necessary_guard_occurrences"],
        "necessary_guard_unique_paths": summary["necessary_guard_unique_paths"],
        "all_13_author_files_readonly_and_unchanged": True,
        "all_4_current_accepted_exact_candidate_suffixes_match": True,
        "all_10_own_parent_files_unchanged": True,
        "mutable_historical_status_not_a_current_proof_input": True,
        **label_counts,
        "corresponding_NEW_root_R19_peer_material_accessed": False,
        "mathematical_program_CAS_scan_or_author_source_old_replay": False,
    })
    print(json.dumps({"mode": "prepare", "at_utc": now(), "pass": True,
                      "ENTIRE_files_so_far": 9, "hand_disposition_labels": 64,
                      "necessary_guard_occurrences": 228, "necessary_guard_unique_paths": 154}))


def prefreeze():
    summary = guard()
    baseline = load(BASELINE)
    for key, value in summary.items():
        assert baseline[key] == value, key
    validation = load(VALIDATION)
    exact(validation["baseline"])
    assert validation["pass"] is True
    count = labels()
    assert len(PAYLOADS) == 9 and all(path(rel).is_file() for rel in PAYLOADS)
    return summary, count


def freeze():
    summary, count = prefreeze()
    assert not path(MANIFEST).exists()
    write_new(MANIFEST, {
        "frozen_at_utc": now(),
        "status": "ENTIRE initially blind OTHER WHOLE review2 initial; author correction required, not promotion",
        "reviewer": "/root/review_2022_complexity_r2",
        "A_sole_NEW_constructor_excluded": True,
        "reviewer_NEW_R19_contribution": False,
        "older_roles_disclosed_not_fresh_self_recertification": True,
        "requested": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independent_effective_readback": None,
        "author_main": AUTHOR_MAIN, "author_freeze": AUTHOR_FREEZE,
        "ENTIRE_author_files_read": 13,
        "whole_obligations": 64, **count,
        "core_normalized_R19A_R19B_R19C_proof_defect_identified": False,
        "required_author_explanatory_scope_corrections": ["R19R2-01"],
        "formal_normalized_carrier_theorem_not_refuted": True,
        "counterexample_is_to_omitted_scaling_inference_not_actual_degree20": True,
        "versioned_author_response_and_BOTH_affected_reaudits_required": True,
        "ENTIRE_review_files_including_manifest": 10,
        "immediate_own_parent": OWN_PARENT,
        "older_own_paths_bound_transitively": 803,
        "older_plus_new_own_paths_bound_transitively": 813,
        "necessary_guard_occurrences": summary["necessary_guard_occurrences"],
        "necessary_guard_unique_paths": summary["necessary_guard_unique_paths"],
        "necessary_guard_canonical_sha256": summary["necessary_guard_canonical_sha256"],
        "FULL_final_model_readback_ALL9_payloads_code_generated_metadata_completed_before_freeze": True,
        "FULL_manifest_model_readback_then_SEPARATE_readonly_verify_required": True,
        "NEW_corresponding_root_R19_findings_files_hashes_metadata_accessed": False,
        "pending_NEW_BT_peer_material_accessed": False,
        "BOTH_entire_initials_explicit_confirmation_received_at_freeze": False,
        "findings_release_embargoed_until_explicit_BOTH_confirmation": True,
        "only_admin_completion_identity_may_be_sent_before_BOTH": True,
        "no_mathematical_program_CAS_scan_test_or_author_source_old_replay": True,
        "no_Git_shared_old_cache_mutation_spawn_charge_contact_bypass": True,
        "authoritative_weekly_telemetry": {
            "observed_at_utc": "2026-10-18 13:58:35 UTC",
            "method": "own direct clock/get_usage_limits same awaited batch",
            "TOTAL_used_percent": 40, "window_minutes": 10080,
            "reset_unix": 1792874445, "ordinary_usage_allowed": True,
            "legacy_by_limit_agree": True, "account_label": "029a8928...1334ac3a",
            "TOTAL_ceiling_percent": 90, "integration_reserve": True,
            "human_authorized_current_window_only": True,
            "automatic_later_window_spending": False,
        },
        "payloads": [fp(rel) for rel in PAYLOADS],
    })
    print(json.dumps({"mode": "freeze", "manifest": fp(MANIFEST),
                      "ENTIRE_files": 10, "hand_obligations": 64, "findings_embargoed": True}))


def verify():
    manifest = load(MANIFEST)
    for row in manifest["payloads"]:
        exact(row)
    summary, count = prefreeze()
    assert manifest["whole_obligations"] == count["review_separate_hand_dispositions"] == 64
    assert manifest["necessary_guard_canonical_sha256"] == summary["necessary_guard_canonical_sha256"]
    existing = sorted(p.relative_to(ROOT).as_posix()
                      for p in (ROOT / DIR).glob("reasoning-center-return-r19-review-2-*"))
    assert existing == sorted(PAYLOADS + [MANIFEST]), existing
    print(json.dumps({"mode": "SEPARATE_readonly_verify", "verified_at_utc": now(),
                      "pass": True, "ENTIRE_files": 10, "hand_obligations": 64,
                      "necessary_guard_occurrences": 228, "necessary_guard_unique_paths": 154,
                      "manifest": fp(MANIFEST), "main_report": fp(P + "initial.md"),
                      "findings_release_still_requires_explicit_BOTH": True}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("prepare", "freeze", "verify"))
    mode = parser.parse_args().mode
    {"prepare": prepare, "freeze": freeze, "verify": verify}[mode]()
