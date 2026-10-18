"""Administrative-only whole R6 R2 freeze; no mathematical computation.

Invocation: python3 problems/2017-B4/reviews/reasoning-value-return-r6-review-2-freeze-v1.py
Writes only this assigned prefix's NEW validation and manifest, once.
Never runs a constructor program or expands historical inventories recursively.
"""
from pathlib import Path
import datetime
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PRE = "problems/2017-B4/reviews/reasoning-value-return-r6-review-2-"


def fp(path):
    raw = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}


def verify(record):
    actual = fp(record["path"])
    assert actual == record, (record, actual)
    return actual


def summary(records):
    unique = {}
    for record in records:
        if record["path"] in unique:
            assert unique[record["path"]] == record
        unique[record["path"]] = record
    rows = [unique[path] for path in sorted(unique)]
    digest = hashlib.sha256(json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return {"occurrences": len(records), "unique_paths": len(rows), "canonical_deduplicated_summary_sha256": digest}


def declarations(value):
    if isinstance(value, dict):
        if all(key in value for key in ("path", "bytes", "sha256")):
            yield {key: value[key] for key in ("path", "bytes", "sha256")}
        for child in value.values():
            yield from declarations(child)
    elif isinstance(value, list):
        for child in value:
            yield from declarations(child)


def write_new(suffix, data):
    with (ROOT / (PRE + suffix)).open("x") as stream:
        json.dump(data, stream, indent=2)
        stream.write("\n")


assert not (ROOT / (PRE + "input-validation-v1.json")).exists()
assert not (ROOT / (PRE + "manifest-v1.json")).exists()
baseline_path = PRE + "baseline-v1.json"
assert fp(baseline_path)["sha256"] == "d0b00575aad90c1c448706204c881ae813fa41d475bc8217f18eda75ccb369ac"
base = json.loads((ROOT / baseline_path).read_text())
records = [verify(record) for key in ("current_constructor_packet", "necessary_current_inputs", "immediately_previous_own_packet") for record in base[key]]
assert summary(records) == base["necessary_current_summary"]
assert len(records) == 41
constructor_base = json.loads((ROOT / base["constructor_selected_one_level_80_declarations"]["exact_baseline"]["path"]).read_text())
selected = []
for record in [constructor_base["immutable_parent"]] + constructor_base["authoritative_acceptance_metadata"]:
    selected.append(verify(record))
    selected.extend(verify(child) for child in declarations(json.loads((ROOT / record["path"]).read_text())))
selected.extend(verify(record) for record in constructor_base["explicit_inputs"])
assert summary(selected) == base["constructor_selected_one_level_80_declarations"]["verified_summary"]
target = "problems/2017-B4/notes/reasoning-value-return-r6-candidate-v1.md"
freeze = "problems/2017-B4/notes/reasoning-value-return-r6-freeze-v1.json"
assert fp(target)["sha256"] == "dbb4232858154bbbae385e16ef0444101e02c50cddbe0dbc82402166cd2869af"
assert fp(freeze)["sha256"] == "aba8108ec5191eb5c6d2702944d74c340c06ff949938bbe0bcd197b34998e9d4"
ledger = (ROOT / (PRE + "ledger-v1.md")).read_text()
assert re.findall(r"^\|(PM-\d{2})\|", ledger, re.MULTILINE) == [f"PM-{i:02d}" for i in range(1, 49)]
issue = (ROOT / (PRE + "issues-v1.md")).read_text()
assert "## PMR2-01:" in issue
assert re.findall(r"^\|(PMR2-N\d+)\|", issue, re.MULTILINE) == [f"PMR2-N{i}" for i in range(1, 5)]
sources = json.loads((ROOT / (PRE + "sources-v1.json")).read_text())
assert len(sources["public_primary_sources"]) == 6
assert sources["new_A_R6_peer_material_read"] is False
assert sources["source_use_issue"] == "PMR2-01"
payload_suffixes = ["baseline-v1.json", "initial.md", "ledger-v1.md", "issues-v1.md", "source-checks-v1.md", "sources-v1.json", "freeze-v1.py"]
payload = [fp(PRE + suffix) for suffix in payload_suffixes]
assert all(record["bytes"] > 1000 for record in payload)
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
telemetry = {"at_utc": "2026-10-18 00:23:55 UTC", "method": "mcp__codex_app__get_usage_limits({}); rateLimitsByLimitId.codex.primary and legacy agree; rechecked at freeze preparation", "account_label": "029a8928…1334ac3a", "used_percent_total": 3, "window_minutes": 10080, "reset_unix": 1792874445, "ordinary_usage_allowed": True, "new_window_explicitly_user_authorized_via_coordinator": True, "total_ceiling_percent": 90, "integration_reserve": True, "automatic_further_reset_spending": False}
validation = {"checked_at_utc": now, "administrative_only_no_mathematical_evidence": True, "baseline": fp(baseline_path), "necessary_current_summary": summary(records), "all10_constructor_files_unchanged": True, "all22_selected_current_authority_input_records_unchanged": True, "all_nine_immediately_previous_own_files_unchanged": True, "constructor_selected_one_level_80_declarations": base["constructor_selected_one_level_80_declarations"], "constructor_selected_80_declarations_independently_reverified": summary(selected), "prior_own_history": base["prior_own_history"], "all48_obligation_rows_present_once": True, "substantive_issues": 1, "required_author_resolutions": 1, "retained_scope_notes": 4, "source_use_issue": "PMR2-01", "affected_claims": ["PM2", "PM3"], "PM1_PM4_whole_reconstruction_passed": True, "downstream_conditional_arguments_reconstructed_not_source_gap_repair": True, "new_A_R6_findings_files_or_metadata_unread_through_entire_initial": True, "queued_NF_R9_packets_and_peer_material_unopened_through_entire_initial": True, "one_unfrozen_own_patch_context_mismatch_changed_no_file_corrected_own_patch_succeeded": True, "payload_records_before_validation": payload, "current_inputs_plus_payload_summary": summary(records + payload), "no_mathcode_scan_CAS_certificate_replay_or_author_rerun": True, "no_old_shared_Git_cache_edit_spawn_contact_charge_or_bypass": True, "authoritative_weekly_telemetry": telemetry}
write_new("input-validation-v1.json", validation)
artifacts = payload + [fp(PRE + "input-validation-v1.json")]
manifest = {"frozen_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "status": "COMPLETE fresh initially blind NONCONSTRUCTOR WHOLE R2; PMR2-01 unresolved source-use gap; no promotion", "reviewer": "/root/review_2022_complexity_r2", "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"}, "independently_verified_effective_settings": None, "exact_target": fp(target), "exact_constructor_freeze": fp(freeze), "all48_obligations_and_whole_PM1_PM4_reconstructed": True, "substantive_issues": 1, "required_author_resolutions": 1, "retained_scope_notes": 4, "source_use_issue": "PMR2-01", "affected_claims": ["PM2", "PM3"], "PM1_PM4_whole_reconstruction_passed": True, "countercertificate": "Two-color actual plane grid: a fixed color1 track crosses infinitely many distinctly perturbed color2 tracks, giving infinitely many crossing angles, outside de Tiliere's standing finite-angle domain", "not_a_counterexample_to_PM2_conclusion_or_source_theorem": True, "complete_versioned_author_response_and_both_affected_reaudits_required": True, "no_reviewer_repair_or_unverified_source_extension_imported": True, "new_A_R6_findings_files_or_metadata_unread_through_entire_initial": True, "reviewer_did_not_construct_NEW_PM_packet": True, "root_C_contributors_excluded": True, "old_B_global_authorship_and_local_US_HC_EC_review_roles_disclosed": True, "no_self_recertification_of_accepted_premises": True, "no_upper_R_mass_value_annual_or_novelty_claim": True, "necessary_current_summary": summary(records), "constructor_selected_one_level80_summary": summary(selected), "compact_own_parent_manifest": base["prior_own_history"]["manifest"], "compact_own_parent_validation": base["prior_own_history"]["validation"], "older_own_paths_bound_transitively": 448, "new_own_files_including_manifest": 9, "older_plus_new_own_paths_bound_transitively": 457, "no_historical_inventory_recopied_or_recursively_rehashed": True, "no_mathcode_scan_CAS_native_mathematical_child_or_author_rerun": True, "no_old_shared_Git_cache_edit_spawn_contact_charge_or_bypass": True, "queued_NF_R9_unopened_before_current_entire_freeze": True, "authoritative_weekly_telemetry": telemetry, "artifacts": artifacts}
write_new("manifest-v1.json", manifest)
for suffix in ["initial.md", "ledger-v1.md", "issues-v1.md", "source-checks-v1.md", "input-validation-v1.json", "manifest-v1.json"]:
    print(json.dumps(fp(PRE + suffix)))
