"""Administrative-only ENTIRE initially blind FP review freeze.

Direct immutable bytes/SHA, JSON, exact accepted-copy suffix and obligation
labels only. No mathematical formula, source experiment or author program
is evaluated. No NEW peer FP file is read or hashed.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2024-B4/reviews/coordinator-F8-pencil-r1-review-2-"
T = "problems/2024-B4/notes/coordinator-F8-pencil-r1-"
FORBIDDEN = "problems/2024-B4/reviews/coordinator-F8-pencil-r1-review-1-"


def read(path):
    assert not path.startswith(FORBIDDEN), "NEW peer FP material prohibited"
    return (ROOT / path).read_bytes()


def rec(path):
    value = read(path)
    return {"path": path, "bytes": len(value),
            "sha256": hashlib.sha256(value).hexdigest()}


def readj(path):
    return json.loads(read(path))


def occurrences(obj):
    result = []
    if isinstance(obj, dict):
        if {"path", "bytes", "sha256"} <= obj.keys():
            result.append({key: obj[key] for key in ("path", "bytes", "sha256")})
        for value in obj.values():
            result.extend(occurrences(value))
    elif isinstance(obj, list):
        for value in obj:
            result.extend(occurrences(value))
    return result


def newj(path, obj):
    with (ROOT / path).open("x") as output:
        output.write(json.dumps(obj, indent=2) + "\n")


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
assert len(rows) == len(unique) == 22
assert baseline["historical_own_paths_bound"] == 591
assert readj(baseline["immutable_own_parent"]["path"])["own_paths_after_this_packet"] == 591
canonical = [unique[path] for path in sorted(unique)]
digest = hashlib.sha256(json.dumps(
    canonical, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

target = readj(T + "freeze-v1.json")
assert target["all_obligations"] == 36
assert target["constructor"] == "/root"
assert len(target["artifacts"]) == 8
for row in target["artifacts"]:
    assert unique[row["path"]] == row
assert rec(T + "candidate-v1.md")["sha256"] == (
    "68accf09323d692e4d4d6850e8c2c04d735d667e1ddaa56cbb73c451fb6402ef")
assert rec(T + "freeze-v1.json")["sha256"] == (
    "3bab98755fd2df8b13ca531e408f1f543762bad9f4289230a9d9668135d45d28")

nf = readj("problems/2024-B4/reviews/coordinator-neighbor-Frobenius-r1-acceptance.json")
assert nf["unresolved_substantive_issues"] == 0
assert nf["repair_required"] is False
for key in ("candidate", "accepted_copy"):
    assert unique[nf[key]["path"]] == nf[key]
    assert rec(nf[key]["path"]) == nf[key]
assert read(nf["accepted_copy"]["path"]).endswith(read(nf["candidate"]["path"]))

author_ids = re.findall(r"^\|(\d{2})\|", read(T + "obligations-v1.md").decode(), re.M)
review_ids = re.findall(r"^\|(\d{2})\|", read(P + "ledger-v1.md").decode(), re.M)
expected = [f"{index:02d}" for index in range(1, 37)]
assert author_ids == review_ids == expected

validation = {
    "verified_utc": datetime.now(timezone.utc).isoformat(),
    "administrative_only_not_mathematical_validation": True,
    "operation": "direct bytes/SHA/JSON/NF-copy-suffix/36-label checks",
    "fingerprint_occurrences_verified": len(rows),
    "deduplicated_paths_verified": len(unique),
    "canonical_direct_input_summary_sha256": digest,
    "entire_nine_file_target_unchanged": True,
    "accepted_NF_exact_candidate_suffix_and_direct_authority_verified": True,
    "all36_author_and_reviewer_IDs_once_in_order": True,
    "no_NEW_A_FP_review_findings_source_code_or_metadata_accessed_or_hashed": True,
    "no_recursive_historical_inventory_rehash_or_copy": True,
    "immutable_own_parent": baseline["immutable_own_parent"],
    "errors": []
}
newj(P + "input-validation-v1.json", validation)

metadata = {
    "reviewer": "/root/review_2017_coarsening_r1",
    "scope": "ENTIRE OTHER initially blind WHOLE FP0--FP2; all36 obligations",
    "whole_initial_before_ANY_NEW_A_FP_material": True,
    "new_FP_constructor": "/root",
    "reviewer_did_not_construct_NEW_FP": True,
    "old_CP1_S3_construction_and_KC_threebit_review_roles_disclosed": True,
    "no_fresh_independent_recertification_of_own_old_input": True,
    "substantive_defects_identified": 0,
    "required_repairs": 0,
    "advisories": 0,
    "conclusion_only_pencil_constraint_degree_gap_unique_large_F2_component": True,
    "possibly_nonconstant_small_F2_cofactor_still_unresolved": True,
    "no_whole_irreducibility_official_membership_annual_or_priority_claim": True,
    "mathematical_program_CAS_scan_factor_table_certificate_or_author_rerun": False,
    "all_local_cones_incidence_contacts_quadratic_bounds_grouping_hand_checked": True,
    "no_old_shared_cache_Git_write_spawn_contact_charge_or_bypass": True,
    "preliminary_proof_investigated_or_reproduced": False,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
    "independently_verified_effective_settings": None,
    "authoritative_weekly_telemetry": {
        "at_utc": "2026-10-18 06:48:39 UTC",
        "method": "mcp__codex_app__get_usage_limits; legacy/by-limit primary agree",
        "used_percent_TOTAL": 12,
        "window_minutes": 10080,
        "reset_unix": 1792874445,
        "ordinary_usage_allowed": True,
        "current_window_explicitly_user_authorized_through_TOTAL_percent": 90,
        "integration_reserve_retained": True,
        "automatic_further_reset_spending": False
    },
    "historical_own_paths_bound": 591,
    "new_packet_paths_including_manifest": 10,
    "own_paths_after_this_packet": 601,
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
    "status": "ENTIRE OTHER initially blind WHOLE FP R2 frozen before NEW peer material",
    "target_main": rec(T + "candidate-v1.md"),
    "target_freeze": rec(T + "freeze-v1.json"),
    "all36_obligations": True,
    "substantive_issues": 0,
    "required_repairs": 0,
    "advisories": 0,
    "no_NEW_A_FP_report_findings_source_code_or_metadata_read_or_hashed": True,
    "both_whole_initials_required_before_coordinator_promotion": True,
    "findings_withheld_until_OTHER_entire_initial_confirmation": True,
    "old_roles_disclosed_no_self_recertification": True,
    "no_mathematical_program_CAS_scan_author_or_certificate_rerun": True,
    "no_whole_irreducibility_official_membership_annual_or_priority_claim": True,
    "immutable_own_parent": baseline["immutable_own_parent"],
    "historical_own_paths_bound": 591,
    "new_packet_paths_including_manifest": 10,
    "own_paths_after_this_packet": 601,
    "fingerprint_occurrences_verified": len(rows),
    "deduplicated_paths_verified": len(unique),
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
    "all36_obligations": True,
    "fingerprint_occurrences": len(rows),
    "deduplicated_paths": len(unique),
    "new_packet_files_including_manifest": 10,
    "own_paths_after_this_packet": 601,
    "postfreeze_errors": 0,
    "mathematical_validation_by_code": False
}, indent=2))
