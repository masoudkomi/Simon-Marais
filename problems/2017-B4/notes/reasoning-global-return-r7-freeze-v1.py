"""Administrative-only R7 constructor freeze.

This program evaluates no mathematical algorithm, count, period bound,
geometry compiler, rule array or source theorem. It verifies direct
immutable fingerprints, JSON, accepted-copy suffixes and60 label strings.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2017-B4/notes/reasoning-global-return-r7-"


def read(path):
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


def newj(path, value):
    with (ROOT / path).open("x") as stream:
        stream.write(json.dumps(value, indent=2) + "\n")


for suffix in ("metadata-v1.json", "input-validation-v1.json", "freeze-v1.json"):
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
assert len(rows) == len(unique) == 26
assert baseline["historical_own_paths_bound"] == 601
assert readj(baseline["immutable_own_parent"]["path"])["own_paths_after_this_packet"] == 601

for path in baseline["accepted_authority_paths"]:
    authority = readj(path)
    assert authority["unresolved_substantive_issues"] == 0
    assert authority["repair_required"] is False
    for key in ("candidate", "accepted_copy"):
        assert unique[authority[key]["path"]] == authority[key]
        assert rec(authority[key]["path"]) == authority[key]
    assert read(authority["accepted_copy"]["path"]).endswith(
        read(authority["candidate"]["path"]))

labels = re.findall(r"^\|(R7O\d{2})\|", read(P + "obligations-v1.md").decode(), re.M)
assert labels == [f"R7O{number:02d}" for number in range(1, 61)]
main = read(P + "candidate-v1.md").decode()
assert "Candidate proof - unverified" in main
assert all(f"R7{letter}" in main for letter in "ABCDEF")
canonical = [unique[path] for path in sorted(unique)]
digest = hashlib.sha256(json.dumps(
    canonical, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

validation = {
    "verified_utc": datetime.now(timezone.utc).isoformat(),
    "administrative_only_not_mathematical_validation": True,
    "operation": "direct bytes/SHA/JSON/accepted-copy suffixes/60-label strings",
    "fingerprint_occurrences_verified": len(rows),
    "deduplicated_paths_verified": len(unique),
    "canonical_direct_input_summary_sha256": digest,
    "all_declared_old_direct_bytes_preserved": True,
    "four_direct_accepted_candidate_suffixes_verified": True,
    "all60_obligation_labels_once_in_order": True,
    "immutable_own_parent": baseline["immutable_own_parent"],
    "no_recursive_historical_inventory_rehash_or_copy": True,
    "mathematical_period_count_model_or_algorithm_evaluated": False,
    "errors": []
}
newj(P + "input-validation-v1.json", validation)

metadata = {
    "constructor": "/root/review_2017_coarsening_r1",
    "status": "candidate proof - unverified",
    "claims_proposed": ["R7A", "R7B", "R7C", "R7D", "R7E"],
    "R7F_exact_remaining_upper_limit_gap": True,
    "all_obligations": 60,
    "TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits_required": True,
    "constructor_excluded_from_independent_audits": True,
    "root_supplied_broad_target_no_NEW_mathematical_inference": True,
    "old_PM_GR_OP_construction_and_old_review_roles_disclosed": True,
    "published_geometric_periodization_attributed_not_claimed_new": True,
    "actual_whole_boundary_fibre_count_not_formal_decoration": True,
    "full_boundary_pinned_mass_not_free_or_average_composition_entropy": True,
    "bounded_period_language_recognition_not_entropy_density_preservation": True,
    "no_upper_R_numeric_value_two_sided_computability_or_annual_claim": True,
    "no_mathematical_program_CAS_scan_count_certificate_or_author_rerun": True,
    "no_new_source_binary_download_cache_or_Git_shared_old_write": True,
    "no_spawn_contact_fee_separate_API_or_bypass": True,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
    "independently_verified_effective_settings": None,
    "authoritative_weekly_telemetry": {
        "at_utc": "2026-10-18 07:13:30 UTC",
        "method": "mcp__codex_app__get_usage_limits; legacy/by-limit primary agree",
        "used_percent_TOTAL": 13,
        "window_minutes": 10080,
        "reset_unix": 1792874445,
        "ordinary_usage_allowed": True,
        "current_window_explicitly_user_authorized_through_TOTAL_percent": 90,
        "integration_reserve_retained": True,
        "automatic_further_reset_spending": False
    },
    "immutable_own_parent": baseline["immutable_own_parent"],
    "historical_own_paths_bound": 601,
    "new_packet_paths_including_freeze": 11,
    "own_paths_after_this_packet": 612,
    "direct_input_summary_sha256": digest
}
newj(P + "metadata-v1.json", metadata)

suffixes = ["candidate-v1.md", "obligations-v1.md", "source-checks-v1.md",
            "failed-routes-v1.md", "worklog-v1.md", "interim-v0.md",
            "freeze-v1.py", "baseline-v1.json", "metadata-v1.json",
            "input-validation-v1.json"]
artifacts = [rec(P + suffix) for suffix in suffixes]
manifest = {
    "frozen_utc": datetime.now(timezone.utc).isoformat(),
    "status": "ENTIRE R7 constructor packet - candidate proof unverified",
    "constructor": "/root/review_2017_coarsening_r1",
    "TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits_required": True,
    "all60_obligations": True,
    "main_sources_failures_worklog_interim_code_ALL_metadata_frozen": True,
    "mathematical_algorithm_rule_compiler_period_count_or_scan_executed": False,
    "no_upper_R_value_two_sided_computability_or_annual_promotion": True,
    "published_periodization_and_old_roles_disclosed": True,
    "immutable_own_parent": baseline["immutable_own_parent"],
    "historical_own_paths_bound": 601,
    "new_packet_paths_including_freeze": 11,
    "own_paths_after_this_packet": 612,
    "fingerprint_occurrences_verified": len(rows),
    "deduplicated_paths_verified": len(unique),
    "artifacts": artifacts
}
newj(P + "freeze-v1.json", manifest)

for row in rows + artifacts:
    assert rec(row["path"]) == row
assert readj(P + "input-validation-v1.json") == validation
assert readj(P + "metadata-v1.json") == metadata
assert readj(P + "freeze-v1.json") == manifest
print(json.dumps({
    "ENTIRE_constructor_packet_frozen": True,
    "main": rec(P + "candidate-v1.md"),
    "freeze": rec(P + "freeze-v1.json"),
    "all60_obligations": True,
    "fingerprint_occurrences": len(rows),
    "deduplicated_paths": len(unique),
    "packet_files_including_freeze": 11,
    "own_paths_after_this_packet": 612,
    "postfreeze_errors": 0,
    "mathematical_validation_by_code": False
}, indent=2))
