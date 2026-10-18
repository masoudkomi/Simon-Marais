"""Review metadata ONLY. No mathematical computation or author rerun.

Writes exclusively unused cofactor-cubic-r3-review-2-* outputs.
Use --baseline once, then --freeze once. Old inventories stay compact.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2024-B4/reviews/cofactor-cubic-r3-review-2"
TARGET = "problems/2024-B4/notes/cofactor-cubic-r3-candidate-v1.md"
TARGET_FREEZE = "problems/2024-B4/notes/cofactor-cubic-r3-freeze-v1.json"
TARGET_BASE = "problems/2024-B4/notes/cofactor-cubic-r3-baseline-v1.json"
AUTHORITY = "problems/2024-B4/reviews/cofactor-global-r2-acceptance.json"
PARENT = "problems/2025-B4/notes/reasoning-Runge-return-r3-freeze-v1.json"
OLD_OWN_CG = "problems/2024-B4/reviews/cofactor-global-r2-review-2-manifest-v1.json"
EXPECTED = {
    TARGET: (9112, "153cbc7a070eb1bffdb62f351c64a79353d8dd41a3e5db03c051b4ed8041f0c4"),
    TARGET_FREEZE: (2786, "fcb6f42f7aa824110a5bb60178b2f9db9dc80e37a5827dbc03895484957be263"),
    PARENT: (8661, "6a010ee19e90b4a07373f64dd375e9df7e6c8d4aee9ec7af001d8410e5bb461a"),
    OLD_OWN_CG: (6399, "e8a4dc472c78c4d47d59d63d97787ef2d3a7bb9234f53f220cbff4d6976e886d"),
}
SUFFIXES = [
    "initial-v1.md", "ledger-v1.md", "issues-v1.md",
    "source-checks-v1.md", "sources-v1.json", "worklog-v1.md",
    "freeze-v1.py", "baseline-v1.json", "input-validation-v1.json",
]
TELEMETRY = {
    "observed_at_utc": "2026-10-18 09:40:27 UTC",
    "method": "get_usage_limits and clock in same independent batch",
    "used_percent_TOTAL": 22, "window_minutes": 10080,
    "reset_unix": 1792874445, "ordinary_usage_allowed": True,
    "legacy_by_limit_agree": True, "account_label": "029a8928...1334ac3a",
    "human_authorized_current_window_ONLY": True,
    "ceiling_TOTAL_percent": 90, "integration_reserve": True,
    "automatic_later_reset_spending": False,
}


def now():
    return datetime.now(timezone.utc).isoformat()


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()


def record(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": digest(data)}


def read_json(path):
    return json.loads((ROOT / path).read_text())


def verify(rec):
    assert record(rec["path"]) == {key: rec[key] for key in ("path", "bytes", "sha256")}, rec["path"]


def put_new(path, obj):
    assert path.startswith(PREFIX + "-")
    with (ROOT / path).open("x") as out:
        json.dump(obj, out, indent=2, ensure_ascii=False)
        out.write("\n")


def declared_summary(path):
    rows = []

    def visit(obj):
        if isinstance(obj, dict):
            if isinstance(obj.get("path"), str) and isinstance(obj.get("bytes"), int) and isinstance(obj.get("sha256"), str):
                rows.append({key: obj[key] for key in ("path", "bytes", "sha256")})
            for value in obj.values():
                visit(value)
        elif isinstance(obj, list):
            for value in obj:
                visit(value)

    visit(read_json(path))
    return {
        "immutable_parent": record(path),
        "declared_fingerprint_occurrences": len(rows),
        "deduplicated_paths": len({row["path"] for row in rows}),
        "canonical_deduplicated_summary_sha256": digest(b"\n".join(sorted({canonical(row) for row in rows}))),
        "historical_rows_not_copied_or_recursively_reverified": True,
    }


def accepted_check():
    obj = read_json(AUTHORITY)
    assert obj["unresolved_substantive_issues"] == 0
    assert obj["repair_required"] is False
    assert obj["proposed_claims_accepted"] == ["CG1", "CG2", "CG3"]
    assert obj["constructor_excluded"] is True
    verify(obj["accepted_copy"])
    verify(obj["candidate"])
    assert obj["accepted_copy"]["sha256"] == "fd110d1615e730d754063b157cc1906b418702f510b2640bfd1b5c63e898548d"
    assert (ROOT / obj["accepted_copy"]["path"]).read_bytes().endswith((ROOT / obj["candidate"]["path"]).read_bytes())
    return {"authority": record(AUTHORITY), "accepted_body": obj["accepted_copy"], "candidate_suffix": obj["candidate"], "operative_new_premises": ["CG1", "CG2 strong intermediate section6 eq9"], "old_CG3_NOT_a_new_premise": True}


def baseline():
    for path, (size, sha) in EXPECTED.items():
        rec = record(path)
        assert (rec["bytes"], rec["sha256"]) == (size, sha), path
    target = read_json(TARGET_FREEZE)
    assert len(target["artifacts"]) == 9
    for rec in target["artifacts"]:
        verify(rec)
    base = read_json(TARGET_BASE)
    assert len(base["protected"]) == 10
    for rec in base["protected"]:
        verify(rec)
    verify(target["exact_accepted_CG_authority"])
    paths = [TARGET_FREEZE] + [rec["path"] for rec in target["artifacts"]] + [rec["path"] for rec in base["protected"]] + [PARENT, OLD_OWN_CG]
    guards = [record(path) for path in sorted(set(paths))]
    assert len(guards) == 22
    assert read_json(PARENT)["older_plus_new_own_paths_bound_transitively"] == 646
    obj = {
        "created_utc": now(), "status": "ENTIRE initially blind review2 metadata baseline",
        "prefix_confirmed_unused_before_first_write": True,
        "target_ten_files_exact_and_entire_read": True,
        "constructor_ten_old_guards_verified_without_historical_replay": True,
        "protected": guards, "protected_unique_paths": len(guards),
        "canonical_protected_summary_sha256": digest(canonical(guards)),
        "accepted_pointer_and_suffix_check": accepted_check(),
        "compact_immutable_parent_summaries": [declared_summary(path) for path in (TARGET_FREEZE, TARGET_BASE, AUTHORITY, PARENT, OLD_OWN_CG)],
        "immediate_own_parent": record(PARENT),
        "older_own_paths_bound_transitively": 646,
        "no_corresponding_A_NEW_cubic_review_finding_file_hash_or_metadata_access": True,
        "no_math_code_source_author_rerun_or_old_edit": True,
    }
    path = PREFIX + "-baseline-v1.json"
    put_new(path, obj)
    print(json.dumps({"baseline": record(path), "protected": len(guards), "accepted_pointer_exact": True}))


def freeze():
    base_path = PREFIX + "-baseline-v1.json"
    base = read_json(base_path)
    for rec in base["protected"]:
        verify(rec)
    pointer = accepted_check()
    original = (ROOT / "problems/2024-B4/notes/cofactor-cubic-r3-obligations-v1.md").read_text()
    labels = re.findall(r"\| CC-(\d{2}) \|", original)
    assert labels == [f"{i:02d}" for i in range(1, 21)]
    own = (ROOT / (PREFIX + "-ledger-v1.md")).read_text()
    labels = re.findall(r"\| CCR2-(\d{2}) \|", own)
    assert labels == [f"{i:02d}" for i in range(1, 21)]
    read_json(PREFIX + "-sources-v1.json")
    val_path = PREFIX + "-input-validation-v1.json"
    put_new(val_path, {
        "verified_utc": now(), "metadata_only_NOT_mathematical_evidence": True,
        "all22_protected_unchanged": True,
        "constructor_ten_file_records_exact": True,
        "accepted_CG_pointer_and_unchanged_candidate_suffix_exact": True,
        "all20_constructor_and_all20_independent_reviewer_labels_exact": True,
        "no_historical_inventory_recopy_or_recursive_replay": True,
        "no_corresponding_A_NEW_cubic_material_access": True,
        "no_math_code_scan_CAS_optimizer_or_author_rerun": True,
        "authoritative_weekly_telemetry": TELEMETRY,
    })
    artifacts = [record(PREFIX + "-" + suffix) for suffix in SUFFIXES]
    man_path = PREFIX + "-manifest-v1.json"
    put_new(man_path, {
        "frozen_utc": now(), "status": "ENTIRE initially blind OTHER WHOLE R3A-R3B review2 initial frozen",
        "reviewer": "/root/review_2022_complexity_r2", "constructor": "/root",
        "constructor_excluded": True, "reviewer_NEW_constructive_contribution": False,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independently_verified_effective_settings": None,
        "target_main": record(TARGET), "target_freeze": record(TARGET_FREEZE),
        "entire_ten_file_target_and_all20_whole_obligations_read_reconstructed": True,
        "substantive_proof_defects_found": 0, "required_mathematical_repairs": 0,
        "unresolved_proof_objections": 0, "closed_scope_dependency_notes": 4,
        "no_corresponding_A_NEW_cubic_finding_file_hash_or_metadata_before_entire_freeze": True,
        "identity_only_handoff_until_BOTH_entire_initials_confirmed": True,
        "accepted_operative_dependency": pointer,
        "compact_necessary_baseline": record(base_path),
        "protected_unique_paths": 22,
        "canonical_protected_summary_sha256": base["canonical_protected_summary_sha256"],
        "compact_immutable_parent_summaries": base["compact_immutable_parent_summaries"],
        "immediate_own_parent": base["immediate_own_parent"],
        "older_own_paths_bound_transitively": 646,
        "new_review_files_including_manifest": 10,
        "older_plus_new_own_paths_bound_transitively": 656,
        "no_historical_inventory_recopy_or_recursive_replay": True,
        "no_math_code_CAS_scan_optimizer_tests_certificate_or_author_rerun": True,
        "no_old_shared_Git_cache_edit_spawn_contact_charge_or_bypass": True,
        "coordinator_promotion_full_annual_or_priority_claim": False,
        "authoritative_weekly_telemetry": TELEMETRY,
        "artifacts": artifacts,
    })
    for rec in artifacts + base["protected"]:
        verify(rec)
    print(json.dumps({
        "complete_review_files": 10, "whole_obligations": 20,
        "protected_unchanged": 22,
        "initial": record(PREFIX + "-initial-v1.md"),
        "manifest": record(man_path),
        "postverification": "all exact; completion IDENTITY ONLY",
    }))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--baseline", action="store_true")
    group.add_argument("--freeze", action="store_true")
    args = parser.parse_args()
    baseline() if args.baseline else freeze()
