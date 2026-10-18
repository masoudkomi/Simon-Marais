#!/usr/bin/env python3
"""Reviewer SHA/JSON preservation only; never executes mathematical code."""
from pathlib import Path
import argparse
import datetime as dt
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
BASE = "problems/2017-B4/reviews/reasoning-global-return-r7-review-2-"
CTOR = "problems/2017-B4/notes/reasoning-global-return-r7-"
FORBIDDEN = "problems/2017-B4/reviews/reasoning-global-return-r7-review-1-"
MAIN_SHA = "6bfa6327d4bb0c11dc014699bf41f1ad06102d3b1f0a5d40a2e7f4401347334f"
FREEZE_SHA = "545e1131036b4e298bfb2957584e2186e6b92a2f0c94ed3f2b4a4036653d9199"
OWN_PARENT = "problems/2025-B4/notes/reasoning-Runge-return-r2-freeze-v1.json"
OWN_PARENT_SHA = "34bf0623be5cc897f681e0bcaf81c0bd1fc2a57fecc460f4b11177aab29c2e34"
SUFFIXES = ["initial-v1.md", "ledger-v1.md", "issues-v1.md",
            "sources-v1.md", "sources-v1.json", "worklog-v1.md",
            "freeze-v1.py", "baseline-v1.json"]


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def data(rel):
    assert not rel.startswith(FORBIDDEN), rel
    return (ROOT / rel).read_bytes()


def rec(rel):
    raw = data(rel)
    return {"path": rel, "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest()}


def readj(rel):
    return json.loads(data(rel))


def canonical(rows):
    return hashlib.sha256(json.dumps(sorted(rows, key=lambda r: r["path"]),
        sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def fingerprints(obj):
    rows = []
    if isinstance(obj, dict):
        if {"path", "bytes", "sha256"} <= obj.keys():
            rows.append({k: obj[k] for k in ("path", "bytes", "sha256")})
        for value in obj.values():
            rows.extend(fingerprints(value))
    elif isinstance(obj, list):
        for value in obj:
            rows.extend(fingerprints(value))
    return rows


def save_new(rel, value):
    assert rel.startswith(BASE), rel
    with (ROOT / rel).open("x", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, ensure_ascii=False)
        handle.write("\n")


def check_inputs():
    main = rec(CTOR + "candidate-v1.md")
    freeze = rec(CTOR + "freeze-v1.json")
    assert (main["bytes"], main["sha256"]) == (27776, MAIN_SHA)
    assert (freeze["bytes"], freeze["sha256"]) == (3015, FREEZE_SHA)
    manifest = readj(freeze["path"])
    targets = manifest["artifacts"] + [freeze]
    assert len(targets) == 11
    for row in targets:
        assert rec(row["path"]) == row, row["path"]
    old_bundle = readj(CTOR + "baseline-v1.json")
    old_rows = fingerprints(old_bundle)
    assert len(old_rows) == len({r["path"] for r in old_rows}) == 26
    for row in old_rows:
        assert rec(row["path"]) == row, row["path"]
    for rel in old_bundle["accepted_authority_paths"]:
        authority = readj(rel)
        assert authority["unresolved_substantive_issues"] == 0
        assert authority["repair_required"] is False
        assert data(authority["accepted_copy"]["path"]).endswith(
            data(authority["candidate"]["path"]))
    parent = rec(OWN_PARENT)
    assert (parent["bytes"], parent["sha256"]) == (4617, OWN_PARENT_SHA)
    assert readj(OWN_PARENT)["older_plus_new_own_paths_bound_transitively"] == 584
    all_rows = targets + old_rows + [parent]
    assert len(all_rows) == len({r["path"] for r in all_rows}) == 38
    return {
        "constructor_packet_binding": {"main": main, "freeze": freeze,
            "target_files": 11, "canonical_target_summary_sha256": canonical(targets)},
        "constructor_declared_old_input_binding": {
            "baseline": rec(CTOR + "baseline-v1.json"),
            "occurrences": 26, "unique_paths": 26,
            "canonical_input_summary_sha256": canonical(old_rows)},
        "compact_immediate_own_parent": parent,
        "necessary_live_fingerprint_checks": 38,
        "necessary_unique_paths": 38,
        "canonical_combined_summary_sha256": canonical(all_rows),
    }


def baseline():
    binding = check_inputs()
    save_new(BASE + "baseline-v1.json", {
        "observed_utc": now(),
        "purpose": "compact necessary metadata only; no historical inventory recopy",
        **binding,
        "older_own_paths_bound_transitively": 584,
        "only_four_direct_parent_target_bindings_copied": True,
        "constructor_own_FP_parent_is_hashed_NOT_recursively_read": True,
        "NEW_root_R7_prefix_not_opened_or_hashed": True,
        "old_shared_Git_cache_mutation": False,
    })
    print(json.dumps({"baseline": rec(BASE + "baseline-v1.json"),
                      "live_checks": 38}))


def finish():
    before = readj(BASE + "baseline-v1.json")
    binding = check_inputs()
    assert all(before[key] == value for key, value in binding.items())
    own_ledger = data(BASE + "ledger-v1.md").decode()
    own_labels = re.findall(r"^\| (R7O\d{2}) \|", own_ledger, re.M)
    ctor_labels = re.findall(r"^\|(R7O\d{2})\|",
                            data(CTOR + "obligations-v1.md").decode(), re.M)
    expected = [f"R7O{i:02d}" for i in range(1, 61)]
    assert own_labels == ctor_labels == expected
    sourcej = readj(BASE + "sources-v1.json")
    assert sourcej["ALL_author_obligations_reconstructed"] == 60
    assert not sourcej["NEW_root_R7_findings_files_metadata_read_or_hashed"]
    payloads = [rec(BASE + suffix) for suffix in SUFFIXES]
    save_new(BASE + "input-validation-v1.json", {
        "verified_utc": now(),
        "operation": "metadata-only SHA/JSON/copy-suffix/label checks; NOT math tests",
        "constructor_target_files_verified": 11,
        "constructor_direct_input_occurrences_verified": 26,
        "total_necessary_live_fingerprint_checks": 38,
        "total_necessary_unique_paths": 38,
        "four_accepted_copy_suffixes_match_exact_candidates": True,
        "own_and_constructor_ALL60_labels_once_in_order": True,
        "compact_own_parent_584_paths_bound_not_recopied": True,
        "all_protected_old_fingerprints_unchanged": True,
        "NEW_root_R7_material_opened_or_hashed": False,
        "no_author_code_or_mathematical_program_executed": True,
        "payloads_before_validation": payloads,
        "errors": [],
    })
    artifacts = payloads + [rec(BASE + "input-validation-v1.json")]
    save_new(BASE + "manifest-v1.json", {
        "frozen_utc": now(),
        "status": "ENTIRE initially blind NONCONSTRUCTOR WHOLE R2 original-v1 audit frozen",
        "reviewer": "/root/review_2022_complexity_r2",
        "NEW_constructor": "/root/review_2017_coarsening_r1",
        "whole_R7A_through_R7F_and_ALL60_obligations": True,
        "complete_source_failures_worklog_code_ALL_metadata_read": True,
        "substantive_defects_found": 0,
        "required_author_repairs": 0,
        "closed_scope_notes": ["R7R2-N1", "R7R2-N2", "R7R2-N3", "R7R2-N4"],
        "coordinator_promotion": False,
        "old_B_G_authorship_PM_review_roles_disclosed_not_self_recertified": True,
        "NEW_root_R7_findings_files_metadata_opened_or_hashed_before_entire_freeze": False,
        "completion_IDENTITY_ONLY_until_root_entire_initial_confirmed": True,
        "no_math_program_CAS_scan_count_compiler_source_or_author_rerun": True,
        "no_Git_shared_old_cache_write_spawn_contact_charge_or_bypass": True,
        **binding,
        "reviewer_baseline": rec(BASE + "baseline-v1.json"),
        "older_own_paths_bound_transitively": 584,
        "new_own_files_including_manifest": 10,
        "older_plus_new_own_paths_bound_transitively": 594,
        "no_recursive_historical_inventory_copy_or_reverify": True,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independently_verified_effective_settings": None,
        "authoritative_weekly_telemetry": {
            "observed_at_utc": "2026-10-18 07:34:10 UTC",
            "method": "mcp__codex_app__get_usage_limits; clock same batch",
            "account_label": "029a8928...1334ac3a",
            "used_percent_TOTAL": 14,
            "window_minutes": 10080,
            "reset_unix": 1792874445,
            "ordinary_usage_allowed": True,
            "current_window_explicitly_user_authorized": True,
            "ceiling_TOTAL_percent": 90,
            "integration_reserve": True,
            "automatic_further_reset_spending": False,
        },
        "artifacts": artifacts,
    })
    verify()


def verify():
    manifest = readj(BASE + "manifest-v1.json")
    binding = check_inputs()
    assert all(manifest[key] == value for key, value in binding.items())
    assert len(manifest["artifacts"]) == 9
    for row in manifest["artifacts"]:
        assert rec(row["path"]) == row, row["path"]
    print(json.dumps({"ENTIRE_initial_frozen_and_postverified": True,
        "report": rec(BASE + "initial-v1.md"),
        "manifest": rec(BASE + "manifest-v1.json"),
        "review_files_including_manifest": 10,
        "all60_obligations_present": True,
        "necessary_live_fingerprint_checks": 38,
        "own_paths_bound_transitively": 594,
        "mathematical_findings_withheld_until_both_entire_initials_frozen": True}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("baseline", "finish", "verify"))
    mode = parser.parse_args().mode
    {"baseline": baseline, "finish": finish, "verify": verify}[mode]()
