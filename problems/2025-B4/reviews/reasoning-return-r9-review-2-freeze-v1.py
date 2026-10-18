"""Administrative-only original-v1 R9 WHOLE R2 freeze.

Invocation: python3 problems/2025-B4/reviews/reasoning-return-r9-review-2-freeze-v1.py
Only creates NEW assigned-prefix validation/manifest. No mathematical
calculation, author program, historical inventory expansion or old edit.
"""
from pathlib import Path
import datetime
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PRE = "problems/2025-B4/reviews/reasoning-return-r9-review-2-"


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


def write_new(suffix, data):
    with (ROOT / (PRE + suffix)).open("x") as stream:
        json.dump(data, stream, indent=2)
        stream.write("\n")


assert not (ROOT / (PRE + "input-validation-v1.json")).exists()
assert not (ROOT / (PRE + "manifest-v1.json")).exists()
baseline_path = PRE + "baseline-v1.json"
assert fp(baseline_path)["sha256"] == "d8e15ad8bcdb84f4c36ae63d4a87e61c9caaa460d88035f34e5e5a437d12ecf4"
base = json.loads((ROOT / baseline_path).read_text())
records = [verify(record) for key in ("current_constructor_packet", "necessary_current_context_records", "immediately_previous_own_packet") for record in base[key]]
assert summary(records) == base["necessary_current_summary"]
assert len(records) == 48
target = "problems/2025-B4/notes/reasoning-return-r9-candidate-v1.md"
constructor_freeze = "problems/2025-B4/notes/reasoning-return-r9-freeze-v1.json"
assert fp(target) == {"path": target, "bytes": 22574, "sha256": "8fae8c0dd3e951fd4c847954f75186b8969f1dbdec9592b8cebcbda8394a9aa2"}
assert fp(constructor_freeze) == {"path": constructor_freeze, "bytes": 2790, "sha256": "93eed518f1584c8e4f1a7cbe4d6229c9532caae4269d18cf0393c1f0e934aa8f"}
ledger = (ROOT / (PRE + "ledger-v1.md")).read_text()
assert re.findall(r"^\|(\d{2})\|", ledger, re.MULTILINE) == [f"{i:02d}" for i in range(1, 49)]
issues = (ROOT / (PRE + "issues-v1.md")).read_text()
assert "## R9R2-01:" in issues
assert re.findall(r"^\|(R9R2-N\d+)\|", issues, re.MULTILINE) == [f"R9R2-N{i}" for i in range(1, 5)]
sources = json.loads((ROOT / (PRE + "sources-v1.json")).read_text())
assert len(sources["public_primary_source_records"]) == 5
assert sources["no_NEW_root_R9_files_findings_or_metadata_opened"] is True
assert sources["later_R9_constructor_versions_and_queued_R12_unopened"] is True
payload_suffixes = ["baseline-v1.json", "initial.md", "ledger-v1.md", "issues-v1.md", "source-checks-v1.md", "sources-v1.json", "freeze-v1.py"]
payload = [fp(PRE + suffix) for suffix in payload_suffixes]
assert all(record["bytes"] > 1000 for record in payload)
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
telemetry = sources["authoritative_weekly_telemetry"]
validation = {"checked_at_utc": now, "administrative_only_no_mathematical_evidence": True, "baseline": fp(baseline_path), "necessary_current_summary": summary(records), "all_eleven_original_v1_constructor_files_unchanged": True, "all28_selected_current_authority_context_records_unchanged": True, "all_nine_immediately_preceding_own_files_unchanged": True, "prior_own_history": base["prior_own_history"], "constructor_historical485_parent_bound_not_recopied": base["constructor_parent_history_bound_by_path_bytes_SHA_not_expanded"], "all48_obligation_rows_present_once": True, "whole_six_claims_reconstructed": True, "unresolved_auxiliary_boundary_issues": 1, "issue": "R9R2-01", "author_boundary_corrections_required": 1, "core_R9A_B_D_E_F_calculations_passed_in_exact_scopes": True, "intended_R9C_sqrtH_example_and_cofactor_proof_passed": True, "retained_scope_notes": 4, "no_linear_generator_exclusion_for_ideal_up_to_unit_certified": True, "NEW_root_R9_peer_files_findings_or_metadata_unopened_through_entire_initial": True, "coordinator_unsolicited_completion_identity_without_findings_received": True, "later_constructor_versions_and_queued_R12_unopened_through_entire_initial": True, "payload_records_before_validation": payload, "current_inputs_plus_payload_summary": summary(records + payload), "no_mathcode_CAS_scan_certificate_replay_or_author_rerun": True, "no_old_shared_Git_cache_edit_spawn_contact_charge_or_bypass": True, "authoritative_weekly_telemetry": telemetry}
write_new("input-validation-v1.json", validation)
artifacts = payload + [fp(PRE + "input-validation-v1.json")]
manifest = {"frozen_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "status": "COMPLETE original-v1 fresh initially blind NONCONSTRUCTOR WHOLE R2; localized auxiliary boundary correction R9R2-01 pending; not coordinator acceptance", "reviewer": "/root/review_2022_complexity_r2", "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"}, "independently_verified_effective_settings": None, "exact_target": fp(target), "exact_constructor_freeze": fp(constructor_freeze), "all48_obligations_and_all_six_R9A_F_claims_reconstructed": True, "unresolved_auxiliary_boundary_issues": 1, "issue": "R9R2-01", "exact_countercertificate": "H=2,d=17,R=1/2; integer cube contains only0 and cannot contain unit e16; equation16 and chosen sqrtH example remain valid", "author_boundary_corrections_required": 1, "versioned_author_correction_and_affected_review_required": True, "core_R9A_B_D_E_F_calculations_passed_in_exact_scopes": True, "intended_R9C_sqrtH_example_and_cofactor_proof_passed": True, "retained_scope_notes": 4, "chosen_generator_not_arbitrary_linear_ideal_generator_scope_retained": True, "C_NEW_constructor_excluded": True, "B_did_not_construct_NEW_R9": True, "old_B_R8_UW_authorship_and_R6_R7_reviews_disclosed_no_self_recertification": True, "root_generic_assignment_no_new_inference": True, "NEW_root_R9_peer_files_findings_or_metadata_unopened_through_entire_initial": True, "coordinator_completion_identity_received_without_findings": True, "another_OTHER_complete_initial_and_coordinator_reconciliation_required": True, "no_actual_solution_new_Diophantine_exclusion_source_final_theorem_refutation_or_annual_claim": True, "source_versions_and_precise_read_limits_recorded": True, "necessary_current_summary": summary(records), "compact_own_parent_manifest": base["prior_own_history"]["manifest"], "compact_own_parent_validation": base["prior_own_history"]["validation"], "older_own_paths_bound_transitively": 466, "new_own_files_including_manifest": 9, "older_plus_new_own_paths_bound_transitively": 475, "no_historical_inventory_recopied_or_recursively_rehashed": True, "no_mathcode_scan_CAS_native_mathematical_child_or_author_rerun": True, "no_old_shared_Git_cache_edit_spawn_contact_charge_or_bypass": True, "later_constructor_versions_and_queued_R12_unopened_before_current_entire_freeze": True, "authoritative_weekly_telemetry": telemetry, "artifacts": artifacts}
write_new("manifest-v1.json", manifest)
for suffix in ["initial.md", "ledger-v1.md", "issues-v1.md", "source-checks-v1.md", "sources-v1.json", "input-validation-v1.json", "manifest-v1.json"]:
    print(json.dumps(fp(PRE + suffix)))
