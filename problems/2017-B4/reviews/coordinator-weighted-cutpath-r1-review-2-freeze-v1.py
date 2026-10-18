#!/usr/bin/env python3
"""Byte/metadata/label checks ONLY; no rational/log/graph computation."""
import argparse
import datetime
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2017-B4/reviews/coordinator-weighted-cutpath-r1-review-2-"
C = "problems/2017-B4/notes/coordinator-weighted-cutpath-r1-"
TARGET_MAIN = {"path": C + "candidate-v1.md", "bytes": 12695,
               "sha256": "f77d09e57a7462faaf6d48077c6815b9d33ffa722470596a947b9f46c4205928"}
TARGET_FREEZE = {"path": C + "freeze-v1.json", "bytes": 2672,
                 "sha256": "2ff11ebea88c684a2d86be972ae6f937ec5aec95040904eb27fc5c392ad7b4d4"}
OWN_PARENT = {
    "path": "problems/2024-B4/reviews/cofactor-global-r2-review-2-manifest-v1.json",
    "bytes": 6399,
    "sha256": "e8a4dc472c78c4d47d59d63d97787ef2d3a7bb9234f53f220cbff4d6976e886d",
}
CONSTRUCTOR_NAMES = [
    "candidate-v1.md", "obligations-v1.md", "failures-worklog-v1.md",
    "source-audit-v1.md", "freeze-v1.py", "sources-v1.json",
    "baseline-v1.json", "metadata-v1.json", "input-validation-v1.json",
]
REVIEW_NAMES = [
    "initial-v1.md", "ledger-v1.md", "issues-v1.md", "source-checks-v1.md",
    "sources-v1.json", "worklog-v1.md", "freeze-v1.py", "baseline-v1.json",
    "input-validation-v1.json",
]
AUTHORITY = "problems/2017-B4/reviews/concavity-acceptance.json"


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def rec(path):
    assert "coordinator-weighted-cutpath-r1-review-1-" not in path
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def read(path):
    return json.loads((ROOT / path).read_text())


def check(row):
    actual = rec(row["path"])
    assert actual == row, (row, actual)
    return actual


def save(suffix, value):
    path = P + suffix
    with (ROOT / path).open("x") as handle:
        json.dump(value, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
    return rec(path)


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def authority():
    value = read(AUTHORITY)
    check(value["accepted_proof"])
    assert value["unresolved_substantive_objections"] == 0
    assert value["substantive_author_repair_required"] is False
    return {"authority": rec(AUTHORITY), "accepted_body": value["accepted_proof"],
            "historical_integrity_parent": value["integrity_record"],
            "historical_inventory_recursively_replayed": False}


def labels(path, pattern):
    found = re.findall(pattern, (ROOT / path).read_text(), re.M)
    assert found == [f"{i:02d}" for i in range(1, 41)], (path, found)
    return len(found)


def baseline():
    check(TARGET_MAIN)
    check(TARGET_FREEZE)
    target = read(TARGET_FREEZE["path"])
    assert [r["path"] for r in target["artifacts"]] == [C + n for n in CONSTRUCTOR_NAMES]
    packet = [check(row) for row in target["artifacts"]] + [TARGET_FREEZE]
    ctorbase = read(C + "baseline-v1.json")
    assert len(ctorbase["protected_direct_records"]) == 8
    guards = packet + [check(row) for row in ctorbase["protected_direct_records"]]
    check(OWN_PARENT)
    assert read(OWN_PARENT["path"])["older_plus_new_own_paths_bound_transitively"] == 626
    guards.append(OWN_PARENT)
    assert len(guards) == len({r["path"] for r in guards}) == 19
    output = {
        "captured_utc": now(),
        "actual_baseline_after_hand_review_before_entire_freeze": True,
        "target_main": TARGET_MAIN, "target_freeze": TARGET_FREEZE,
        "constructor_packet_files_verified": 10,
        "constructor_prior_direct_guards_verified": 8,
        "protected_occurrences": 19, "protected_unique_paths": 19,
        "protected": guards, "canonical_protected_summary_sha256": digest(guards),
        "accepted_concavity_authority": authority(),
        "constructor_historical_parent_artifacts_declared": ctorbase["own_parent_all_artifacts_checked"],
        "constructor_historical_parent_inventory_replayed_by_reviewer": False,
        "unrelated_parent_fingerprints_only_not_review_findings_read": True,
        "immediate_own_parent": OWN_PARENT,
        "older_own_paths_bound_transitively": 626,
        "no_growing_historical_inventory_copy_or_recursive_rehash": True,
        "no_corresponding_C_NEW_WC_finding_file_hash_or_metadata_access": True,
        "mathematical_test_or_author_program_execution": False,
    }
    baseline_rec = save("baseline-v1.json", output)
    print(json.dumps({"baseline": baseline_rec, "constructor_files": 10,
                      "constructor_prior_guards": 8, "total_unique_guards": 19}))


def freeze():
    base = read(P + "baseline-v1.json")
    for row in base["protected"]:
        check(row)
    assert digest(base["protected"]) == base["canonical_protected_summary_sha256"]
    assert authority() == base["accepted_concavity_authority"]
    n_ctor = labels(C + "obligations-v1.md", r"^\|WC-O(\d\d)\|")
    n_reviewer = labels(P + "ledger-v1.md", r"^\|WCR2-(\d\d)\|")
    src = read(P + "sources-v1.json")
    assert src["NEW_corresponding_C_WC_finding_file_or_metadata_accessed"] is False
    assert src["mathematical_program_CAS_scan_author_rerun"] is False
    validation = {
        "postverified_utc": now(), "all_protected_records_unchanged": True,
        "protected_occurrences": 19, "protected_unique_paths": 19,
        "constructor_files": 10, "constructor_prior_direct_guards": 8,
        "accepted_copy_pointer_verified": True,
        "constructor_labels_in_order": n_ctor, "independent_ledger_labels_in_order": n_reviewer,
        "scope": "fixed-file fingerprint and document completeness ONLY; no mathematical validation",
        "full_report_issues_sources_log_code_and_ALLmetadata_present": True,
        "no_corresponding_C_NEW_WC_material_accessed": True,
        "old626_paths_bound_by_exact_parent_without_recursive_replay": True,
    }
    validation_rec = save("input-validation-v1.json", validation)
    artifacts = [rec(P + n) for n in REVIEW_NAMES]
    final = {
        "frozen_utc": now(),
        "status": "ENTIRE initially blind OTHER WHOLE WC1–WC3 review2 initial frozen",
        "reviewer": "/root/review_2022_complexity_r2", "constructor": "/root",
        "constructor_excluded": True, "reviewer_NEW_constructive_contribution": False,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independently_verified_effective_settings": None,
        "target_main": TARGET_MAIN, "target_freeze": TARGET_FREEZE,
        "entire_ten_file_constructor_packet_read": True,
        "all40_whole_obligations_and_independent_hand_reconstructions_complete": True,
        "substantive_proof_defects_found": 0, "required_mathematical_author_repairs": 0,
        "unresolved_proof_objections": 0, "closed_scope_source_notes": 5,
        "no_corresponding_C_NEW_WC_finding_file_hash_or_metadata_before_entire_freeze": True,
        "identity_only_handoff_until_BOTH_entire_initials_confirmed": True,
        "mathematical_program_CAS_scan_optimization_certificate_or_author_rerun": False,
        "new_protected_occurrences": 19, "new_protected_unique_paths": 19,
        "canonical_protected_summary_sha256": base["canonical_protected_summary_sha256"],
        "accepted_concavity_authority": base["accepted_concavity_authority"],
        "immediate_own_parent": OWN_PARENT,
        "older_own_paths_bound_transitively": 626,
        "new_review_files_including_manifest": 10,
        "older_plus_new_own_paths_bound_transitively": 636,
        "no_historical_inventory_copy_or_recursive_reverify": True,
        "authoritative_weekly_telemetry": {
            "observed_at_utc": "2026-10-18 09:05:22 UTC",
            "method": "get_usage_limits and clock same batch",
            "used_percent_TOTAL": 20, "window_minutes": 10080,
            "reset_unix": 1792874445, "ordinary_usage_allowed": True,
            "account_label": "029a8928...1334ac3a", "legacy_by_limit_agree": True,
            "human_authorized_current_window_ONLY": True,
            "ceiling_TOTAL_percent": 90, "integration_reserve": True,
            "automatic_later_reset_spending": False,
        },
        "no_old_shared_Git_cache_edit_spawn_contact_charge_or_bypass": True,
        "coordinator_acceptance_external_validation_annual_or_priority_claim": False,
        "artifacts": artifacts,
    }
    manifest = save("manifest-v1.json", final)
    for row in artifacts:
        check(row)
    for row in base["protected"]:
        check(row)
    check(manifest)
    print(json.dumps({"complete_review_files": 10, "all_obligations": 40,
                      "protected_unchanged": 19, "initial": artifacts[0],
                      "validation": validation_rec, "manifest": manifest,
                      "postverification": "all exact; completion IDENTITY ONLY"}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--baseline", action="store_true")
    group.add_argument("--freeze", action="store_true")
    args = parser.parse_args()
    baseline() if args.baseline else freeze()
