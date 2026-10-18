"""Administrative-only whole review freeze; no mathematical evaluation.

Checks direct immutable fingerprints, JSON, source-copy suffixes and
obligation labels. Never executes an author program or a field formula.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2021-B4/reviews/reasoning-return-r14-review-2-"
T = "problems/2021-B4/notes/reasoning-return-r14-"


def read(path):
    assert not path.startswith("problems/2021-B4/reviews/reasoning-return-r14-review-1-")
    assert not path.startswith("problems/2024-B4/notes/coordinator-F8-pencil-r1-")
    assert not path.startswith("problems/2024-B4/reviews/coordinator-F8-pencil-r1-")
    return (ROOT / path).read_bytes()


def rec(path):
    b = read(path)
    return {"path": path, "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}


def readj(path):
    return json.loads(read(path))


def occurrences(obj):
    rows = []
    if isinstance(obj, dict):
        if {"path", "bytes", "sha256"} <= obj.keys():
            rows.append({k: obj[k] for k in ("path", "bytes", "sha256")})
        for value in obj.values():
            rows.extend(occurrences(value))
    elif isinstance(obj, list):
        for value in obj:
            rows.extend(occurrences(value))
    return rows


def newj(path, obj):
    with (ROOT / path).open("x") as stream:
        stream.write(json.dumps(obj, indent=2) + "\n")


for suffix in ("metadata-v1.json", "input-validation-v1.json", "manifest-v1.json"):
    assert not (ROOT / (P + suffix)).exists()
baseline = readj(P + "baseline-v1.json")
rows = occurrences(baseline)
unique = {}
for row in rows:
    assert rec(row["path"]) == row, row["path"]
    if row["path"] in unique:
        assert unique[row["path"]] == row
    unique[row["path"]] = row
    if row["path"].endswith(".json"):
        readj(row["path"])
assert len(rows) == len(unique) == 27
assert baseline["historical_own_paths_bound"] == 581
assert readj(baseline["immutable_own_parent"]["path"])["own_paths_after_this_packet"] == 581
canonical = [unique[path] for path in sorted(unique)]
digest = hashlib.sha256(json.dumps(
    canonical, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
for path in baseline["accepted_authority_paths"]:
    a = readj(path)
    assert a["unresolved_substantive_issues"] == 0
    assert a["repair_required"] is False
    for key in ("candidate", "accepted_copy"):
        assert rec(a[key]["path"]) == a[key]
    assert read(a["accepted_copy"]["path"]).endswith(read(a["candidate"]["path"]))
author_ids = re.findall(r"^\|(R14O\d\d)\|", read(T + "obligations-v1.md").decode(), re.M)
review_ids = re.findall(r"^\|(R14O\d\d)\|", read(P + "ledger-v1.md").decode(), re.M)
expected = [f"R14O{i:02d}" for i in range(1, 57)]
assert author_ids == review_ids == expected
assert rec(T + "candidate-v1.md")["sha256"] == (
    "18b13277fb58aced493db2b4ed2b6bfb92a3778c50e661bf5bc858a59f0c2e7f")

now = datetime.now(timezone.utc).isoformat()
validation = {
    "verified_utc": now,
    "administrative_only_not_mathematical_validation": True,
    "operation": "direct bytes/SHA/JSON/accepted-copy-suffix/56-label checks",
    "declared_occurrences_verified": len(rows),
    "deduplicated_paths_verified": len(unique),
    "canonical_deduplicated_summary_sha256": digest,
    "all_current_target_payloads_preserved": True,
    "accepted_R8_R12_R13_exact_direct_authorities_and_copy_suffixes_verified": True,
    "current_R13_acceptance_separate_from_historical_R14_conditional_wording": True,
    "all56_author_and_reviewer_IDs_once_in_order": True,
    "immutable_own_parent": baseline["immutable_own_parent"],
    "no_NEW_B_R14_review_file_finding_source_code_or_metadata_accessed": True,
    "queued_FP_target_and_peer_files_not_opened_before_entire_freeze": True,
    "no_recursive_historical_inventory_copy_or_rehash": True,
    "errors": []
}
newj(P + "input-validation-v1.json", validation)
metadata = {
    "reviewer": "/root/review_2017_coarsening_r1",
    "scope": "ENTIRE OTHER initially blind WHOLE R14A--D and all56 obligations",
    "whole_initial_before_ANY_NEW_peer_R14_material": True,
    "old_R5_G1_constructor_and_other_review_roles_disclosed": True,
    "no_fresh_independent_recertification_of_own_old_input": True,
    "substantive_defects_identified": 0,
    "required_repairs": 0,
    "advisories": 0,
    "R14D_as_submitted_explicit_conditional_valid": True,
    "current_separate_accepted_R13C_matches_exact_conditional_premise": True,
    "no_all_m5_m3m4_J15_degree20_annual_lift_height_or_novelty_conclusion": True,
    "all48_low_assignments_and_ten_exceptional_tuples_recomputed_by_hand": True,
    "mathematical_program_CAS_scan_table_generator_author_or_certificate_rerun": False,
    "no_old_shared_cache_Git_write_spawn_contact_charge_or_bypass": True,
    "preliminary_proof_investigated_or_reproduced": False,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
    "independently_verified_effective_settings": None,
    "authoritative_weekly_telemetry": {
        "at_utc": "2026-10-18 06:37:31 UTC",
        "method": "mcp__codex_app__get_usage_limits; legacy/by-limit primary agree",
        "used_percent_TOTAL": 12,
        "window_minutes": 10080,
        "reset_unix": 1792874445,
        "ordinary_usage_allowed": True,
        "current_window_explicitly_user_authorized_through_TOTAL_percent": 90,
        "integration_reserve_retained": True,
        "automatic_further_reset_spending": False
    },
    "historical_own_paths_bound": 581,
    "new_packet_paths_including_manifest": 10,
    "own_paths_after_this_packet": 591,
    "compact_own_parent": baseline["immutable_own_parent"],
    "direct_input_summary_sha256": digest
}
newj(P + "metadata-v1.json", metadata)
suffixes = ["initial-v1.md", "ledger-v1.md", "issues-v1.md", "source-checks-v1.md",
            "worklog-v1.md", "freeze-v1.py", "baseline-v1.json",
            "metadata-v1.json", "input-validation-v1.json"]
artifacts = [rec(P + suffix) for suffix in suffixes]
manifest = {
    "frozen_utc": datetime.now(timezone.utc).isoformat(),
    "status": "ENTIRE OTHER initially blind WHOLE R14 R2 frozen before NEW peer material",
    "target_main": rec(T + "candidate-v1.md"),
    "target_freeze": rec(T + "freeze-v1.json"),
    "all56_obligations": True,
    "substantive_issues": 0,
    "required_repairs": 0,
    "advisories": 0,
    "no_NEW_B_R14_report_findings_source_code_metadata_read_or_hashed": True,
    "findings_withheld_until_OTHER_entire_initial_confirmation": True,
    "R14D_conditional_and_current_separate_accepted_premise_distinguished": True,
    "old_roles_disclosed_no_self_recertification": True,
    "no_mathematical_program_CAS_scan_author_or_certificate_rerun": True,
    "immutable_own_parent": baseline["immutable_own_parent"],
    "historical_own_paths_bound": 581,
    "new_packet_paths_including_manifest": 10,
    "own_paths_after_this_packet": 591,
    "declared_occurrences_verified": len(rows),
    "deduplicated_paths_verified": len(unique),
    "no_coordinator_promotion_or_annual_claim": True,
    "artifacts": artifacts
}
newj(P + "manifest-v1.json", manifest)
for row in rows + artifacts:
    assert rec(row["path"]) == row
assert readj(P + "input-validation-v1.json") == validation
assert readj(P + "metadata-v1.json") == metadata
assert readj(P + "manifest-v1.json") == manifest
print(json.dumps({
    "ENTIRE_whole_initial_frozen": True,
    "manifest": rec(P + "manifest-v1.json"),
    "whole_report": rec(P + "initial-v1.md"),
    "all56_obligations": True,
    "fingerprint_occurrences": len(rows),
    "deduplicated_paths": len(unique),
    "new_packet_files_including_manifest": 10,
    "own_paths_after_this_packet": 591,
    "postfreeze_errors": 0,
    "mathematical_validation_by_code": False
}, indent=2))
