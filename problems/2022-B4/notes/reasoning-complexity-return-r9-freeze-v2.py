"""Metadata-only freeze for the unverified whole Q1--Q6 extension.

No mathematical orbit, residue enumeration, CAS or proof validation is run.
Writes only two NEW files in this worker's assigned versioned prefix.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
BASE = "problems/2022-B4/notes/reasoning-complexity-return-r9-"


def record(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def read_json(path):
    return json.loads((ROOT / path).read_text())


def fingerprint_occurrences(obj):
    result = []
    if isinstance(obj, dict):
        if all(k in obj for k in ("path", "bytes", "sha256")):
            result.append({k: obj[k] for k in ("path", "bytes", "sha256")})
        for value in obj.values():
            result.extend(fingerprint_occurrences(value))
    elif isinstance(obj, list):
        for value in obj:
            result.extend(fingerprint_occurrences(value))
    return result


def exclusive_json(path, obj):
    with (ROOT / path).open("x") as stream:
        stream.write(json.dumps(obj, indent=2) + "\n")


baseline_path = BASE + "baseline-v2.json"
validation_path = BASE + "input-validation-v2.json"
manifest_path = BASE + "freeze-v2.json"
assert not (ROOT / validation_path).exists()
assert not (ROOT / manifest_path).exists()
baseline = read_json(baseline_path)
occurrences = fingerprint_occurrences(baseline)
assert len(occurrences) == 25
unique = {}
for item in occurrences:
    if item["path"] in unique:
        assert unique[item["path"]] == item
    unique[item["path"]] = item
    assert record(item["path"]) == item, item["path"]
assert len(unique) == 23
assert baseline["older_own_paths_bound_transitively"] == 532
assert baseline["v1_mathematical_parent_is_unverified_pending_TWO_OTHER_audits"]

canonical = [unique[p] for p in sorted(unique)]
canonical_digest = hashlib.sha256(
    json.dumps(canonical, sort_keys=True, separators=(",", ":")).encode()
).hexdigest()

v1_main = (ROOT / (BASE + "candidate-v1.md")).read_bytes()
v2_main = (ROOT / (BASE + "candidate-v2.md")).read_bytes()
v1_obligations = (ROOT / (BASE + "obligations-v1.md")).read_bytes()
v2_obligations = (ROOT / (BASE + "obligations-v2.md")).read_bytes()
assert len(v1_main) == 16457
assert hashlib.sha256(v1_main).hexdigest() == (
    "2fdb1a495afa4f607b9fb63b7a1535e7ba6797ae5b699fd9d25124b503bfe211")
assert v2_main.endswith(v1_main)
assert v2_obligations.endswith(v1_obligations)
new_ids = re.findall(r"^\| (QV2\d\d) \|", v2_obligations.decode(), re.M)
old_ids = re.findall(r"^\| (QO\d\d) \|", v2_obligations.decode(), re.M)
assert new_ids == [f"QV2{i:02d}" for i in range(1, 33)]
assert old_ids == [f"QO{i:02d}" for i in range(1, 49)]
assert len(new_ids + old_ids) == 80

payload_suffixes = [
    "baseline-v2.json", "candidate-v2.md", "obligations-v2.md",
    "failed-routes-v2.md", "source-audit-v2.md", "sources-v2.json",
    "worklog-v2.md", "followup-draft-v2.md", "freeze-v2.py"
]
for suffix in payload_suffixes:
    assert (ROOT / (BASE + suffix)).is_file()
    if suffix.endswith(".json"):
        read_json(BASE + suffix)

checked_at = datetime.now(timezone.utc).isoformat()
validation = {
    "checked_utc": checked_at,
    "operation": "ONLY SHA/bytes/JSON/literal appendix/obligation-label integrity",
    "mathematical_validation_or_enumeration": False,
    "necessary_old_fingerprint_occurrences_verified": len(occurrences),
    "unique_paths_verified": len(unique),
    "canonical_deduplicated_summary_sha256": canonical_digest,
    "entire_v1_candidate_literal_suffix_unchanged": True,
    "entire_v1_48_obligation_literal_suffix_unchanged": True,
    "new_QV201_to_QV232_labels_once_in_order": True,
    "old_QO01_to_QO48_labels_once_in_order": True,
    "all80_labels_present_not_proof_validation": True,
    "no_NEW_A_C_peer2022R9_files_findings_or_metadata_read_or_hashed": True,
    "compact_own_parent": baseline["compact_own_parent"],
    "mathematical_parent_v1": baseline["mathematical_parent_v1"],
    "no_recursive_historical_inventory_recopy_or_rehash": True,
    "deduplicated_current_records": canonical,
    "errors": []
}
exclusive_json(validation_path, validation)
artifacts = [record(BASE + suffix) for suffix in payload_suffixes]
artifacts.append(record(validation_path))
manifest = {
    "frozen_utc": datetime.now(timezone.utc).isoformat(),
    "status": "candidate proof - unverified; COMPLETE whole Q1--Q6 v2 extension checkpoint",
    "constructor": "/root/review_2022_complexity_r2",
    "exact_new_whole_candidate": record(BASE + "candidate-v2.md"),
    "new_claims": [
        "Q5 one positive integer rank for central inverse and every critical double-input merger",
        "Q6 exact universal equivalence with unbounded singleton-next-output seeds plus B<=42 patch"
    ],
    "entire_Q1_Q4_mathematical_body_retained_as_literal_appendix": True,
    "Q1_Q4_parent_still_unverified_pending_TWO_OTHER_audits": True,
    "full_Q1_Q6_and_all80_obligations": True,
    "old48_plus_new32_obligations": True,
    "full_source_limits_failed_routes_worklog_and_draft_preserved": True,
    "actual_B36_rank_increase_and_B40_equality_preserved": True,
    "both_old_diagonal_and_outer_strip_inverse_counterexamples_preserved": True,
    "D2_RL_actual_one_step_hitting_subfamily_proved_by_hand": True,
    "no_all_residual_hitting_or_survivor_or_annual_solution_or_novelty_claim": True,
    "TWO_OTHER_fresh_initially_blind_WHOLE_v2_audits_required": True,
    "root_prompt_supplies_no_new_Q1_Q6_inference": True,
    "no_NEW_A_C_R9_findings_reports_ledgers_source_or_metadata_read_or_hashed": True,
    "old_authorship_and_review_roles_disclosed_no_self_certification": True,
    "mathematical_code_CAS_scan_author_rerun_or_finite_certificate": False,
    "metadata_checks_only_not_mathematical_validation": True,
    "old_shared_Git_cache_edit_spawn_charge_contact_or_bypass": False,
    "preliminary_a_proof_reproduced_or_investigated": False,
    "actual_fresh_primary_read_scopes_and_no_external_proof_import_recorded": True,
    "compact_own_parent": baseline["compact_own_parent"],
    "mathematical_parent_v1": baseline["mathematical_parent_v1"],
    "older_own_paths_bound_transitively": 532,
    "new_own_files_including_manifest": 11,
    "older_plus_new_own_paths_bound_transitively": 543,
    "fingerprint_occurrences_verified": len(occurrences),
    "unique_paths_verified": len(unique),
    "canonical_deduplicated_summary_sha256": canonical_digest,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
    "independently_verified_effective_settings": None,
    "authoritative_weekly_telemetry": {
        "at_utc": "2026-10-18 01:59:57 UTC",
        "method": "mcp__codex_app__get_usage_limits({}); codex.primary and legacy agree",
        "account_label": "029a8928...1334ac3a",
        "used_percent_TOTAL": 9,
        "window_minutes": 10080,
        "reset_unix": 1792874445,
        "ordinary_usage_allowed": True,
        "current_window_explicitly_user_authorized": True,
        "ceiling_TOTAL_percent": 90,
        "integration_reserve": True,
        "automatic_further_reset_spending": False
    },
    "artifacts": artifacts
}
exclusive_json(manifest_path, manifest)
for item in artifacts:
    assert record(item["path"]) == item
for item in occurrences:
    assert record(item["path"]) == item
assert read_json(manifest_path) == manifest
assert read_json(validation_path) == validation
print(json.dumps({
    "complete_unverified_checkpoint": True,
    "mathematical_validation": False,
    "main": record(BASE + "candidate-v2.md"),
    "manifest": record(manifest_path),
    "all80_obligation_labels": True,
    "old_occurrences_verified": len(occurrences),
    "old_unique_paths_verified": len(unique),
    "new_own_files_including_manifest": 11,
    "total_own_paths_bound_transitively": 543,
    "postfreeze_metadata_errors": 0
}, indent=2))
