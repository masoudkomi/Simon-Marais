#!/usr/bin/env python3
"""Fixed-file integrity and label completeness ONLY; no mathematical executable."""
import argparse
import datetime
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2024-B4/reviews/cofactor-global-r2-review-2-"
C = "problems/2024-B4/notes/cofactor-global-r2-"
TARGET_MAIN = {
    "path": C + "candidate-v1.md", "bytes": 15586,
    "sha256": "9dac8137a3b47637e25ee66a5c2bf5ff00146e9d1d54ba55764002111d5376f9",
}
TARGET_FREEZE = {
    "path": C + "freeze-v1.json", "bytes": 2322,
    "sha256": "3e63984333d64dcfe8bb32395d28e948ab1023ce8f4ab367e0ea374d51dfeaef",
}
OWN_PARENT = {
    "path": "problems/2019-B4/notes/reasoning-critical-return-r2-freeze-v1.json",
    "bytes": 6949,
    "sha256": "295feae2d5671960ad9d9ae3456abcd94850a2c2faec0ce42e024eb5d05b18c9",
}
CONSTRUCTOR_NAMES = [
    "candidate-v1.md", "obligations-v1.md", "source-audit-v1.md",
    "failures-worklog-v1.md", "freeze-v1.py", "baseline-v1.json",
    "metadata-v1.json", "input-validation-v1.json",
]
REVIEW_NAMES = [
    "initial-v1.md", "ledger-v1.md", "issues-v1.md", "source-checks-v1.md",
    "sources-v1.json", "worklog-v1.md", "freeze-v1.py", "baseline-v1.json",
    "input-validation-v1.json",
]
AUTHORITY_KEYS = [
    ("structural", "accepted_proof"),
    ("coordinator-F8-pencil-r1", "accepted_copy"),
    ("cofactor-symmetry-r1", "accepted_copy"),
]


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def rec(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def read(path):
    return json.loads((ROOT / path).read_text())


def check(record):
    actual = rec(record["path"])
    assert actual == record, (record, actual)
    return actual


def save(suffix, value):
    path = P + suffix
    with (ROOT / path).open("x") as handle:
        json.dump(value, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
    return rec(path)


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def authorities():
    summaries = []
    for stem, key in AUTHORITY_KEYS:
        path = f"problems/2024-B4/reviews/{stem}-acceptance.json"
        value = read(path)
        check(value[key])
        summaries.append({
            "authority": rec(path), "accepted_body": value[key],
            "declared_historical_occurrences": value.get("record_occurrences_verified"),
            "declared_historical_unique_paths": value.get("unique_paths_verified"),
            "old_inventory_recursively_replayed": False,
        })
    return summaries


def labels(path, pattern):
    found = re.findall(pattern, (ROOT / path).read_text(), re.M)
    assert found == [f"{i:02d}" for i in range(1, 57)], (path, found)
    return len(found)


def baseline():
    check(TARGET_MAIN)
    check(TARGET_FREEZE)
    frozen = read(TARGET_FREEZE["path"])
    assert [r["path"] for r in frozen["artifacts"]] == [C + name for name in CONSTRUCTOR_NAMES]
    packet = [check(r) for r in frozen["artifacts"]] + [TARGET_FREEZE]
    base = read(C + "baseline-v1.json")
    assert len(base["protected"]) == 16
    prior = [check(r) for r in base["protected"]]
    assert not any("cofactor-global-r2-review-1-" in r["path"] for r in prior)
    check(OWN_PARENT)
    assert read(OWN_PARENT["path"])["older_plus_new_own_paths_bound_transitively"] == 616
    guards = packet + prior + [OWN_PARENT]
    assert len(guards) == len({r["path"] for r in guards}) == 26
    result = {
        "recorded_utc": now(),
        "actual_baseline_after_hand_reconstruction_before_entire_review_freeze": True,
        "target_main": TARGET_MAIN, "target_freeze": TARGET_FREEZE,
        "constructor_packet_files_verified": 9,
        "constructor_prior_guard_records_verified": 16,
        "protected_occurrences": 26, "protected_unique_paths": 26,
        "protected": guards, "canonical_protected_summary_sha256": digest(guards),
        "accepted_authority_summaries": authorities(),
        "immediate_own_parent": OWN_PARENT,
        "older_own_paths_bound_transitively": 616,
        "old_ancestry_recopied_or_recursively_rehashed": False,
        "unrelated_constructor_own_parent_fingerprint_only_not_report_read": True,
        "NEW_corresponding_C_CG_findings_files_or_metadata_accessed": False,
        "mathematical_test_or_author_rerun": False,
    }
    output = save("baseline-v1.json", result)
    print(json.dumps({"baseline": output, "protected_paths": 26, "target_packet_files": 9, "constructor_prior_guards": 16, "accepted_copy_pointers": 3}))


def freeze():
    base = read(P + "baseline-v1.json")
    for record in base["protected"]:
        check(record)
    assert digest(base["protected"]) == base["canonical_protected_summary_sha256"]
    assert authorities() == base["accepted_authority_summaries"]
    n_constructor = labels(C + "obligations-v1.md", r"^\| CG-(\d\d) \|")
    n_reviewer = labels(P + "ledger-v1.md", r"^\| CG2R2-(\d\d) \|")
    review = (ROOT / (P + "initial-v1.md")).read_text()
    assert "ENTIRE WHOLE" in review and "no substantive" in review
    sources = read(P + "sources-v1.json")
    assert sources["NEW_corresponding_C_CG_finding_file_or_metadata_accessed"] is False
    assert sources["mathematical_code_CAS_scan_or_author_program_executed"] is False
    validation = {
        "postverified_utc": now(), "protected_occurrences": 26,
        "protected_unique_paths": 26, "all_protected_records_unchanged": True,
        "constructor_packet_files": 9, "constructor_prior_guards": 16,
        "accepted_copy_pointers_verified": 3,
        "constructor_obligations_in_exact_order": n_constructor,
        "independent_ledger_dispositions_in_exact_order": n_reviewer,
        "full_source_log_code_and_compact_metadata_present": True,
        "scope": "fixed-byte and label completeness only, NOT proof validation",
        "no_NEW_corresponding_C_CG_material_read_or_hashed": True,
        "immediate_own_parent_binds616_prior_paths_without_recursive_replay": True,
    }
    validation_rec = save("input-validation-v1.json", validation)
    artifacts = [rec(P + name) for name in REVIEW_NAMES]
    result = {
        "frozen_utc": now(),
        "status": "ENTIRE initially blind OTHER WHOLE CG1–CG3 review2 initial frozen",
        "reviewer": "/root/review_2022_complexity_r2",
        "constructor": "/root", "constructor_excluded": True,
        "reviewer_NEW_construction_contribution": False,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independently_verified_effective_settings": None,
        "target_main": TARGET_MAIN, "target_freeze": TARGET_FREEZE,
        "entire_nine_file_packet_read": True,
        "all56_obligations_and_full_independent_derivations_complete": True,
        "substantive_proof_defects_found": 0,
        "required_mathematical_author_repairs": 0,
        "unresolved_proof_objections": 0,
        "closed_scope_source_notes": 5,
        "source_note_proper_divisor_condition_retained": True,
        "no_NEW_corresponding_C_CG_finding_file_hash_or_metadata_before_entire_freeze": True,
        "handoff_identity_only_until_BOTH_entire_initials_confirmed": True,
        "mathematical_code_CAS_scan_factor_table_author_or_certificate_rerun": False,
        "new_guard_occurrences": 26, "new_guard_unique_paths": 26,
        "canonical_protected_summary_sha256": base["canonical_protected_summary_sha256"],
        "accepted_authority_summaries": base["accepted_authority_summaries"],
        "immediate_own_parent": OWN_PARENT,
        "older_own_paths_bound_transitively": 616,
        "new_review_files_including_manifest": 10,
        "older_plus_new_own_paths_bound_transitively": 626,
        "no_large_historical_inventory_copy_or_recursive_reverify": True,
        "authoritative_weekly_telemetry": {
            "observed_at_utc": "2026-10-18 08:56:03 UTC",
            "method": "get_usage_limits and clock same batch",
            "used_percent_TOTAL": 19, "window_minutes": 10080,
            "reset_unix": 1792874445, "ordinary_usage_allowed": True,
            "account_label": "029a8928...1334ac3a", "legacy_by_limit_agree": True,
            "human_authorized_current_window_ONLY": True,
            "ceiling_TOTAL_percent": 90, "integration_reserve": True,
            "automatic_later_reset_spending": False,
        },
        "no_Git_shared_old_cache_mutation_spawn_contact_charge_or_bypass": True,
        "queued_WC_candidate_or_peer_material_opened": False,
        "coordinator_acceptance_annual_answer_or_external_validation": False,
        "artifacts": artifacts,
    }
    final = save("manifest-v1.json", result)
    for record in artifacts:
        check(record)
    for record in base["protected"]:
        check(record)
    check(final)
    print(json.dumps({"complete_review_files": 10, "all_obligations": n_reviewer,
                      "input_guards_unchanged": 26, "initial": artifacts[0],
                      "validation": validation_rec, "manifest": final,
                      "postverification": "all exact; IDENTITY-ONLY handoff"}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--baseline", action="store_true")
    group.add_argument("--freeze", action="store_true")
    args = parser.parse_args()
    baseline() if args.baseline else freeze()
