#!/usr/bin/env python3
"""R11 R2 administrative fingerprints/JSON/labels only; no mathematics executes."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2020-B4/reviews/reasoning-arithmetic-return-r11-review-2-"
TARGET = "problems/2020-B4/notes/reasoning-arithmetic-return-r11-"
PARENT = "problems/2025-B4/reviews/reasoning-Runge-return-r2-review-1-manifest-v1.json"
TARGET_SHA = "f93bc9f57db3ff196db2b32380cd0aadd122bff5ea0bfbbf09b7a9a6868f0ead"
FREEZE_SHA = "0c53f7526ba90e3a8a5e419562f593f79923810aa63127cbe1bf053af5361906"
PARENT_SHA = "8613747639aa2d2c10243d83931d58bbae0e20f32cab0feefe4e3b229eaf845c"
STEMS = ["reasoning-return-r7", "reasoning-return-r8", "reasoning-arithmetic-return-r9", "reasoning-arithmetic-return-r10"]
PAYLOADS = ["initial-v1.md", "issues-v1.md", "sources-v1.md", "worklog-v1.md", "freeze-v1.py", "baseline-v1.json", "metadata-v1.json", "input-validation-v1.json"]


def now():
    return datetime.now(timezone.utc).isoformat()


def load(path):
    return json.loads((ROOT / path).read_text())


def fp(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def checked(row):
    assert fp(row["path"]) == row, row["path"]
    return row


def canonical(rows):
    return hashlib.sha256(json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def create(suffix, value):
    path = PREFIX + suffix
    assert path.startswith(PREFIX)
    with (ROOT / path).open("x", encoding="utf-8") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2)
        stream.write("\n")


def baseline():
    main = fp(TARGET + "candidate-v1.md")
    constructor_freeze = fp(TARGET + "freeze-v1.json")
    assert (main["bytes"], main["sha256"]) == (19167, TARGET_SHA)
    assert (constructor_freeze["bytes"], constructor_freeze["sha256"]) == (6719, FREEZE_SHA)
    submission = load(constructor_freeze["path"])
    rows = [checked(row) for row in submission["artifacts"]] + [constructor_freeze]
    assert len(rows) == 11
    protected = load(TARGET + "baseline-v1.json")
    assert len(protected["protected"]) == 26
    assert canonical(protected["protected"]) == protected["canonical_protected_summary_sha256"]
    rows += [checked(row) for row in protected["protected"]]
    authorities = []
    for stem in STEMS:
        authority_path = f"problems/2020-B4/reviews/{stem}-acceptance.json"
        authority = load(authority_path)
        proof = checked(authority["accepted_copy"])
        candidate = checked(authority["candidate"])
        assert (ROOT / proof["path"]).read_bytes().endswith((ROOT / candidate["path"]).read_bytes())
        rows.append(candidate)
        authorities.append({
            "authority": fp(authority_path), "accepted_copy": proof,
            "candidate_exact_suffix_verified": candidate,
            "historical_occurrences_bound_not_replayed": authority["record_occurrences_verified"],
            "historical_paths_bound_not_replayed": authority["unique_paths_verified"],
        })
    parent = fp(PARENT)
    assert (parent["bytes"], parent["sha256"]) == (2798, PARENT_SHA)
    parent_record = load(PARENT)
    rows.append(parent)
    rows += [checked(row) for row in parent_record["artifacts"]]
    rows.append(fp("problems/2020-B4/notes/reasoning-return-r7-sources-v1.json"))
    unique = {}
    for row in rows:
        assert row["path"] not in unique or unique[row["path"]] == row
        unique[row["path"]] = row
    record = {
        "recorded_at_utc": now(),
        "purpose": "current necessary fingerprints and compact immutable parents, no historical recursion",
        "target_main": main, "constructor_freeze": constructor_freeze,
        "entire_constructor_artifacts_including_freeze": 11,
        "constructor_declared_protected_inputs_checked": 26,
        "accepted_authorities": authorities,
        "immediate_own_parent": parent,
        "own_parent_payloads_checked": len(parent_record["artifacts"]),
        "own_parent_historical_summary_bound_not_replayed": parent_record["current_input_summary"],
        "fingerprint_occurrences": len(rows), "unique_paths": len(unique),
        "rows": rows, "deduplicated_rows": list(unique.values()),
        "deduplicated_summary_sha256": canonical(list(unique.values())),
        "NEW_prefix_unused_before_first_write": True,
        "corresponding_NEW_root_R11_contents_or_hashes_accessed": False,
        "incidental_inventory_filenames_only": "Initial overly broad filename inventory also listed root review-1-baseline-v1.json and review-1-freeze-v1.py; neither was opened or hashed. Subsequent queries were exact own prefix.",
        "no_mathematics_executed": True,
    }
    create("baseline-v1.json", record)
    print(json.dumps({"baseline": fp(PREFIX + "baseline-v1.json"), "occurrences": len(rows), "paths": len(unique)}))


def validate_inputs():
    record = load(PREFIX + "baseline-v1.json")
    for row in record["deduplicated_rows"]:
        checked(row)
    assert canonical(record["deduplicated_rows"]) == record["deduplicated_summary_sha256"]
    return record


def freeze():
    record = validate_inputs()
    expected = [f"R11-{i:02d}" for i in range(1, 61)]
    obligations = (ROOT / (TARGET + "obligations-v1.md")).read_text()
    author_checks = (ROOT / (TARGET + "constructor-checks-v1.md")).read_text()
    ledger = (ROOT / (PREFIX + "issues-v1.md")).read_text()
    assert re.findall(r"^\| (R11-\d\d) \|", obligations, re.M) == expected
    assert re.findall(r"^\| (R11-\d\d) \|", author_checks, re.M) == expected
    assert re.findall(r"^\| (R11-\d\d) \|", ledger, re.M) == expected
    assert len(re.findall(r"^\| R11-\d\d \| closed \|", ledger, re.M)) == 60
    metadata = {
        "reviewer": "/root/review_2021_reasoning_j15_r2", "review": "OTHER fresh initially blind ENTIRE WHOLE R2",
        "claims_wholly_reconstructed": ["A11A", "A11B", "A11C", "A11D", "A11E"],
        "all_obligations": 60, "closed": 60, "substantive_defects": 0, "required_author_repairs": 0,
        "closed_scope_notes": 7, "promotion_by_reviewer": False,
        "full_constructor_packet_read": True,
        "accepted_inputs_full_actual_bodies_read": ["R7", "R8", "A9", "M10"],
        "old_review_roles_not_self_recertified": ["R3 and repair", "R5", "R8", "R10"],
        "NEW_R11_construction_contribution": False,
        "NEW_corresponding_peer_file_contents_findings_or_hash_computations_before_entire_freeze": False,
        "root_provided_completion_identity_only_received": True,
        "incidental_root_filenames_only_disclosed": True,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independently_verified_effective_settings": None,
        "latest_authoritative_telemetry": {
            "observed_utc": "2026-10-18 08:18:39 UTC", "method": "direct mcp__codex_app__get_usage_limits and clock in the same awaited batch",
            "TOTAL_used_percent": 17, "window_minutes": 10080, "reset_unix": 1792874445,
            "ordinary_usage_allowed": True, "both_views_agree": True,
            "account_label": "029a8928...1334ac3a", "current_window_explicitly_authorized": True,
            "ceiling_TOTAL_percent": 90, "integration_reserve": True, "automatic_later_week_spending": False,
        },
        "source_binary_hashes": None, "browser_only_no_native_source_download_or_cache_write": True,
        "mathcode_CAS_scan_author_or_source_rerun": False,
        "Git_shared_old_cache_write_spawn_contact_charge_or_bypass": False,
    }
    create("metadata-v1.json", metadata)
    create("input-validation-v1.json", {
        "verified_at_utc": now(), "all_current_inputs_unchanged": True,
        "occurrences_verified": record["fingerprint_occurrences"], "unique_paths_verified": record["unique_paths"],
        "deduplicated_summary_sha256": record["deduplicated_summary_sha256"],
        "all11_constructor_fingerprints_checked": True, "all26_current_declared_protected_fingerprints_checked": True,
        "four_accepted_bodies_exact_candidate_suffixes_verified": True,
        "immediate_own_parent_and_eight_payloads_unchanged": True,
        "all60_labels_exact_once_in_order_in_obligations_author_checks_and_independent_ledger": True,
        "label_checks_are_text_structure_only_not_proof": True,
        "historical_inventory_recursively_replayed": False,
        "NEW_peer_R11_file_access_or_hash": False,
    })
    artifacts = [fp(PREFIX + suffix) for suffix in PAYLOADS]
    create("manifest-v1.json", {
        "frozen_at_utc": now(),
        "status": "ENTIRE initially blind WHOLE A11A-E R2 frozen; no promotion",
        "reviewer": "/root/review_2021_reasoning_j15_r2",
        "entire_constructor": record["constructor_freeze"],
        "all_whole_obligations": 60, "complete_main_ledger_issues_source_worklog_code_ALL_metadata": True,
        "NEW_corresponding_peer_R11_file_contents_findings_or_hash_computations_before_entire_freeze": False,
        "root_provided_completion_identity_only_received": True,
        "incidental_filename_inventory_only_disclosed": True,
        "compact_own_parent": record["immediate_own_parent"],
        "current_input_summary": {"occurrences": record["fingerprint_occurrences"], "unique_paths": record["unique_paths"], "sha256": record["deduplicated_summary_sha256"]},
        "initial_completion_identity_only_until_both_freeze_release": True,
        "artifacts": artifacts,
    })
    verify()


def verify():
    record = validate_inputs()
    manifest = load(PREFIX + "manifest-v1.json")
    for row in manifest["artifacts"]:
        checked(row)
    print(json.dumps({"postverified": True, "manifest": fp(PREFIX + "manifest-v1.json"), "payloads": len(manifest["artifacts"]), "whole_obligations": 60, "input_occurrences": record["fingerprint_occurrences"], "input_paths": record["unique_paths"]}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", choices=["baseline", "freeze", "verify"])
    args = parser.parse_args()
    {"baseline": baseline, "freeze": freeze, "verify": verify}[args.operation]()
