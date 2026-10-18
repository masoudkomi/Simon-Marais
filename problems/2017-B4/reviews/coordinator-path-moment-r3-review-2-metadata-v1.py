#!/usr/bin/env python3
"""NEW PM9 R2 metadata only. No mathematical evaluation or old-code replay.

prepare: verify necessary immutable records; create NEW baseline/validation.
freeze: after FULL model readback, freeze the nine NEW payloads exclusively.
verify: separate read-only byte/JSON/label check of the entire ten-file freeze.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DIR = "problems/2017-B4/reviews/"
P = DIR + "coordinator-path-moment-r3-review-2-"
AUTHOR = "problems/2017-B4/notes/coordinator-path-moment-r3-"
PARENT = "problems/2020-B4/notes/reasoning-arithmetic-return-r14-"
AUTHOR_FREEZE = {
    "path": AUTHOR + "freeze-v2.json",
    "bytes": 4093,
    "sha256": "7210932f81b90afa8197fb40fe6c7cc3603fbfc85c39b58c67df4f36728b185d",
}
AUTHOR_MAIN = {
    "path": AUTHOR + "candidate-v1.md",
    "bytes": 12255,
    "sha256": "0af3e42df62385e086a53eec1d95461ba01ba26148a6f92bd34b1fb778924076",
}
PARENT_FREEZE = {
    "path": PARENT + "freeze-v1.json",
    "bytes": 7060,
    "sha256": "e10b1b5ed9b573e181846b4403d1dbda20515fab3ff39091ce1c8c51124919d5",
}
BASELINE = P + "baseline-v1.json"
VALIDATION = P + "input-validation-v1.json"
MANIFEST = P + "manifest-v1.json"
PROSE_AND_CODE = [
    P + "initial.md",
    P + "obligations-v1.md",
    P + "issues-v1.md",
    P + "sources-v1.md",
    P + "sources-v1.json",
    P + "worklog-v1.md",
    P + "metadata-v1.py",
]
PAYLOADS = PROSE_AND_CODE + [BASELINE, VALIDATION]
DENIED = (
    "problems/2017-B4/reviews/coordinator-path-moment-r3-review-1-",
    "problems/2019-B4/reviews/reasoning-cut-transfer-r5-review-",
    "problems/2021-B4/reviews/reasoning-center-return-r19-review-",
)
ACCEPTED = [
    {
        "name": "PM8A-PM8E exact current scope",
        "candidate": "problems/2017-B4/notes/reasoning-path-mass-return-r8-candidate-v1.md",
        "body": "problems/2017-B4/proofs/reviewed-reasoning-path-mass-return-r8-v1.1.md",
        "authority_md": "problems/2017-B4/reviews/reasoning-path-mass-return-r8-acceptance.md",
        "authority_json": "problems/2017-B4/reviews/reasoning-path-mass-return-r8-acceptance.json",
        "old_occurrences_bound_not_reexpanded": 174,
        "old_unique_paths_bound_not_reexpanded": 92,
    },
    {
        "name": "WC1-WC3 exact current scope",
        "candidate": "problems/2017-B4/notes/coordinator-weighted-cutpath-r1-candidate-v1.md",
        "body": "problems/2017-B4/proofs/reviewed-weighted-cutpath-r1-v1.1.md",
        "authority_md": "problems/2017-B4/reviews/coordinator-weighted-cutpath-r1-acceptance.md",
        "authority_json": "problems/2017-B4/reviews/coordinator-weighted-cutpath-r1-acceptance.json",
        "old_occurrences_bound_not_reexpanded": 102,
        "old_unique_paths_bound_not_reexpanded": 49,
    },
    {
        "name": "WO1-WO4 exact current accepted status",
        "candidate": "problems/2017-B4/notes/coordinator-weighted-optimum-r2-candidate-v1.md",
        "body": "problems/2017-B4/proofs/reviewed-weighted-optimum-r2-v1.1.md",
        "authority_md": "problems/2017-B4/reviews/coordinator-weighted-optimum-r2-acceptance.md",
        "authority_json": "problems/2017-B4/reviews/coordinator-weighted-optimum-r2-acceptance.json",
        "old_occurrences_bound_not_reexpanded": 122,
        "old_unique_paths_bound_not_reexpanded": 74,
    },
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
    return {
        "path": rel,
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
    }


def load(rel):
    return json.loads(path(rel).read_text(encoding="utf-8"))


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def check_rows(rows):
    for expected in rows:
        assert set(expected) >= {"path", "bytes", "sha256"}, expected
        actual = fp(expected["path"])
        assert actual == {k: expected[k] for k in actual}, (expected, actual)


def dedup(rows):
    result = {}
    for row in rows:
        reduced = {key: row[key] for key in ("path", "bytes", "sha256")}
        assert row["path"] not in result or result[row["path"]] == reduced
        result[row["path"]] = reduced
    return [result[key] for key in sorted(result)]


def write_new(rel, value):
    assert rel.startswith(P) and Path(rel).parent.as_posix() == DIR.rstrip("/")
    with path(rel).open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(value, handle, indent=2, ensure_ascii=False)
        handle.write("\n")


def guard():
    check_rows([AUTHOR_FREEZE, AUTHOR_MAIN, PARENT_FREEZE])
    author = load(AUTHOR_FREEZE["path"])
    assert author["ENTIRE_files_including_freeze"] == 16
    assert author["whole_obligations"] == 48
    assert author["main_mathematical_body_changed"] is False
    author_rows = author["payloads"] + [AUTHOR_FREEZE]
    assert len(author_rows) == 16
    check_rows(author_rows)

    old = load(author["old_freeze"]["path"])
    old_rows = old["payloads"] + [author["old_freeze"]]
    assert len(old_rows) == 12
    check_rows(old_rows)
    current_by_path = {row["path"]: row for row in author_rows}
    assert all(current_by_path[row["path"]] == row for row in old_rows)
    assert current_by_path[AUTHOR_MAIN["path"]] == AUTHOR_MAIN

    declared = load(AUTHOR + "baseline-v1.json")
    assert declared["protected_unique_paths"] == 21
    declared_rows = declared["fingerprints"]
    assert len(declared_rows) == 21
    check_rows(declared_rows)

    parent = load(PARENT_FREEZE["path"])
    parent_rows = parent["payloads"] + [PARENT_FREEZE]
    assert len(parent_rows) == 12
    assert parent["older_plus_new_own_paths_bound_transitively"] == 793
    check_rows(parent_rows)

    occurrences = author_rows + old_rows + declared_rows + parent_rows
    unique = dedup(occurrences)
    assert len(occurrences) == 61
    assert len(unique) == 49
    accepted = []
    protected_by_path = {row["path"]: row for row in unique}
    for binding in ACCEPTED:
        checked = dict(binding)
        for key in ("candidate", "body", "authority_md", "authority_json"):
            checked[key] = fp(binding[key])
            assert protected_by_path[binding[key]] == checked[key]
        assert path(binding["body"]).read_bytes().endswith(
            path(binding["candidate"]).read_bytes()
        )
        checked["unchanged_original_candidate_suffix"] = True
        checked["fresh_complete_body_and_MDJSON_read_by_model"] = True
        accepted.append(checked)
    return {
        "guard_occurrences": len(occurrences),
        "guard_unique_paths": len(unique),
        "guard_records": unique,
        "guard_canonical_sha256": hashlib.sha256(canonical(unique)).hexdigest(),
        "author_ENTIRE_files": 16,
        "old_v1_ENTIRE_files_preserved": 12,
        "author_declared_necessary_paths": 21,
        "own_parent_ENTIRE_files": 12,
        "compact_own_parent": PARENT_FREEZE,
        "older_own_paths_bound_transitively": 793,
        "accepted_bindings": accepted,
        "historical_inventory_reexpanded_or_old_math_reread_for_metadata": False,
        "corresponding_NEW_PM9_peer_or_pending_BT_R19_material_accessed": False,
    }


def check_own_labels():
    wanted = [f"PM9-{index:02d}" for index in range(1, 49)]
    author_text = path(AUTHOR + "obligations-v2.md").read_text(encoding="utf-8")
    review_text = path(P + "obligations-v1.md").read_text(encoding="utf-8")
    expression = r"(?m)^\| (PM9-\d{2}) \|"
    assert re.findall(expression, author_text) == wanted
    assert re.findall(expression, review_text) == wanted
    issue_text = path(P + "issues-v1.md").read_text(encoding="utf-8")
    assert re.findall(r"(?m)^\| PM9R2-N([1-8]) \|", issue_text) == list("12345678")
    sources = load(P + "sources-v1.json")
    assert sources["whole_obligations_reconstructed"] == 48
    assert sources["new_peer_PM9_material_accessed"] is False
    assert sources["NEW_PM9_contribution"] is False
    assert sources["new_math_executable_or_CAS_or_scan_or_optimizer"] is False
    return {
        "author_operative_obligation_labels": 48,
        "review_separate_hand_disposition_labels": 48,
        "closed_scope_note_labels": 8,
        "mathematical_assertions_evaluated_by_code": False,
    }


def prepare():
    existing = sorted(
        item.relative_to(ROOT).as_posix()
        for item in (ROOT / DIR).glob("coordinator-path-moment-r3-review-2-*")
    )
    assert existing == sorted(PROSE_AND_CODE), existing
    summary = guard()
    labels = check_own_labels()
    baseline = {
        "created_at_utc": now(),
        "purpose": "NEW reviewer necessary metadata only; not mathematical verification",
        "author_freeze": AUTHOR_FREEZE,
        "author_main": AUTHOR_MAIN,
        **summary,
        "requested": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independent_effective_readback": None,
        "exclusive_NEW_write_prefix": P,
        "no_Git_shared_old_cache_write_spawn_charge_contact_bypass": True,
    }
    write_new(BASELINE, baseline)
    validation = {
        "checked_at_utc": now(),
        "pass": True,
        "NEW_baseline": fp(BASELINE),
        "necessary_guard_occurrences": summary["guard_occurrences"],
        "necessary_guard_unique_paths": summary["guard_unique_paths"],
        "all_16_author_files_including_preserved_v1_bound": True,
        "all_21_author_declared_necessary_old_paths_unchanged": True,
        "all_12_immediate_own_parent_files_unchanged": True,
        "all_3_accepted_exact_candidate_suffixes_match": True,
        **labels,
        "author_source_or_old_code_replayed": False,
        "corresponding_NEW_peer_material_accessed": False,
    }
    write_new(VALIDATION, validation)
    print(json.dumps({"mode": "prepare", "at_utc": now(), "guard_occurrences": 61,
                      "guard_unique_paths": 49, "NEW_files_so_far": 9,
                      "reported_hand_obligation_labels": 48, "pass": True}))


def verify_pre_freeze():
    summary = guard()
    baseline = load(BASELINE)
    assert summary["guard_records"] == baseline["guard_records"]
    assert summary["guard_canonical_sha256"] == baseline["guard_canonical_sha256"]
    validation = load(VALIDATION)
    check_rows([validation["NEW_baseline"]])
    assert validation["pass"] is True
    labels = check_own_labels()
    assert len(PAYLOADS) == 9 and all(path(rel).is_file() for rel in PAYLOADS)
    return summary, labels


def freeze():
    summary, labels = verify_pre_freeze()
    assert not path(MANIFEST).exists()
    manifest = {
        "frozen_at_utc": now(),
        "status": "ENTIRE initially blind OTHER WHOLE review2 initial; not coordinator promotion",
        "reviewer": "/root/review_2022_complexity_r2",
        "root_sole_NEW_constructor_excluded": True,
        "reviewer_NEW_PM9_contribution": False,
        "old_WC_WO_PM8_review_roles_disclosed_not_self_recertified": True,
        "requested": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independent_effective_readback": None,
        "author_main": AUTHOR_MAIN,
        "operative_author_freeze": AUTHOR_FREEZE,
        "ENTIRE_author_files_read": 16,
        "whole_obligations": 48,
        "substantive_open_issues": 0,
        "required_author_repairs_identified": 0,
        "closed_scope_notes": 8,
        **labels,
        "ENTIRE_review_files_including_manifest": 10,
        "immediate_own_parent": PARENT_FREEZE,
        "older_own_paths_bound_transitively": 793,
        "older_plus_new_own_paths_bound_transitively": 803,
        "necessary_guard_occurrences": summary["guard_occurrences"],
        "necessary_guard_unique_paths": summary["guard_unique_paths"],
        "necessary_guard_canonical_sha256": summary["guard_canonical_sha256"],
        "FULL_final_model_readback_ALL9_payloads_code_generated_metadata_completed_before_freeze": True,
        "FULL_manifest_readback_then_SEPARATE_readonly_verify_required": True,
        "corresponding_NEW_C_PM9_findings_files_hashes_metadata_accessed": False,
        "pending_NEW_BT_R19_peer_material_accessed": False,
        "BOTH_entire_initials_explicit_confirmation_received_at_this_freeze": False,
        "findings_release_embargoed_until_explicit_BOTH_confirmation": True,
        "only_admin_identity_may_be_sent_before_BOTH": True,
        "no_mathematical_code_CAS_scan_optimizer_test_or_old_author_source_replay": True,
        "no_Git_shared_old_cache_mutation_spawn_charge_contact_bypass": True,
        "authoritative_weekly_telemetry": {
            "observed_at_utc": "2026-10-18 13:33:56 UTC",
            "method": "own direct clock/get_usage_limits same awaited batch",
            "TOTAL_used_percent": 38,
            "window_minutes": 10080,
            "reset_unix": 1792874445,
            "ordinary_usage_allowed": True,
            "legacy_by_limit_agree": True,
            "account_label": "029a8928...1334ac3a",
            "TOTAL_ceiling_percent": 90,
            "integration_reserve": True,
            "human_authorized_current_window_only": True,
            "automatic_later_window_spending": False,
        },
        "payloads": [fp(rel) for rel in PAYLOADS],
    }
    write_new(MANIFEST, manifest)
    print(json.dumps({"mode": "freeze", "manifest": fp(MANIFEST),
                      "ENTIRE_files": 10, "hand_obligations": 48,
                      "findings_embargoed": True}))


def verify():
    manifest = load(MANIFEST)
    check_rows(manifest["payloads"])
    summary, labels = verify_pre_freeze()
    assert manifest["whole_obligations"] == labels["review_separate_hand_disposition_labels"] == 48
    assert manifest["necessary_guard_canonical_sha256"] == summary["guard_canonical_sha256"]
    assert manifest["ENTIRE_review_files_including_manifest"] == 10
    existing = sorted(
        item.relative_to(ROOT).as_posix()
        for item in (ROOT / DIR).glob("coordinator-path-moment-r3-review-2-*")
    )
    assert existing == sorted(PAYLOADS + [MANIFEST]), existing
    print(json.dumps({"mode": "SEPARATE_readonly_verify", "at_utc": now(),
                      "pass": True, "ENTIRE_files": 10, "hand_obligation_labels": 48,
                      "necessary_guard_occurrences": 61, "necessary_guard_unique_paths": 49,
                      "manifest": fp(MANIFEST), "main_report": fp(P + "initial.md"),
                      "findings_release_still_requires_explicit_BOTH": True}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("prepare", "freeze", "verify"))
    mode = parser.parse_args().mode
    {"prepare": prepare, "freeze": freeze, "verify": verify}[mode]()
