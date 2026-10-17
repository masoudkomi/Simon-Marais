"""Independent R7 reviewer metadata only: known-file SHA/JSON; no mathematics."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2022-B4/reviews/reasoning-return-r7-review-2-"
TARGET = "problems/2022-B4/notes/reasoning-return-r7-"
FORBIDDEN = "problems/2022-B4/reviews/reasoning-return-r7-review-1-"
PREVIOUS = "problems/2019-B4/reviews/auxiliary-presentation-r1-review-1-"


def fp(path):
    path = str(path)
    if path.startswith(FORBIDDEN):
        raise RuntimeError("Blindness guard: refusing new R7 peer content/hash")
    b = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}


inventory = {}
occurrences = 0


def checked(rec):
    global occurrences
    actual = fp(rec["path"])
    if actual["bytes"] != rec["bytes"] or actual["sha256"] != rec["sha256"]:
        raise RuntimeError("Fingerprint mismatch: " + rec["path"])
    occurrences += 1
    if actual["path"] in inventory:
        assert inventory[actual["path"]] == actual
    inventory[actual["path"]] = actual
    return actual


def bind(path):
    return checked(fp(path))


def read_json(path):
    if path.startswith(FORBIDDEN):
        raise RuntimeError("Blindness guard: refusing new R7 peer JSON")
    return json.loads((ROOT / path).read_text())


def rows(obj):
    if isinstance(obj, dict):
        if {"path", "bytes", "sha256"} <= obj.keys():
            yield obj
        for value in obj.values():
            yield from rows(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from rows(value)


def save(suffix, obj):
    with (ROOT / (PREFIX + suffix)).open("x") as f:
        f.write(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


now = datetime.now(timezone.utc).isoformat()
main_expected = {"path": TARGET + "candidate-v1.md", "bytes": 20450,
                 "sha256": "874e30f4fef000510edc0e67541161a735d5e11654e430ff283f4610047abd1e"}
freeze_expected = {"path": TARGET + "freeze-v1.json", "bytes": 3683,
                   "sha256": "f1894610350eb829c7be4c93329cc9054420ac111f5f28c3d0c709099529df69"}
checked(main_expected)
checked(freeze_expected)
constructor_manifest = read_json(freeze_expected["path"])
constructor_records = [checked(rec) for rec in constructor_manifest["artifacts"]]
assert len(constructor_records) == 10
metadata_refs = []
for path in [TARGET + "sources-v1.json", TARGET + "input-validation-v1.json", TARGET + "freeze-output-v1.json"]:
    doc = read_json(path)
    before = occurrences
    for rec in rows(doc):
        checked(rec)
    count = occurrences - before
    metadata_refs.append({"source": bind(path), "declared_fingerprint_occurrences_checked": count})
constructor_validation = read_json(TARGET + "input-validation-v1.json")
assert len(constructor_validation["earlier_unique_records_preserved"]) == 350
assert len(constructor_validation["accepted_context_fingerprints"]) == 7

authority_rows = []
suffix_rows = []
for tag in ["reasoning-return-r5", "reasoning-return-r6"]:
    path = "problems/2022-B4/reviews/" + tag + "-acceptance.json"
    doc = read_json(path)
    declared = [checked(rec) for rec in rows(doc)]
    authority_rows.append({"source": bind(path), "declared_fingerprint_occurrences_checked": len(declared)})
    accepted_path, raw_path = doc["accepted_copy"]["path"], doc["candidate"]["path"]
    assert (ROOT / accepted_path).read_bytes().endswith((ROOT / raw_path).read_bytes())
    suffix_rows.append({"accepted": bind(accepted_path), "raw": bind(raw_path),
                        "entire_raw_submission_is_byte_identical_suffix": True})
assert [r["declared_fingerprint_occurrences_checked"] for r in authority_rows] == [9, 8]
fresh_complete_inputs = [bind(path) for path in [
    "AGENTS.md", "problems/2022-B4/statement.md",
    "problems/2022-B4/proofs/reviewed-reasoning-return-r5-v1.1.md",
    "problems/2022-B4/proofs/reviewed-reasoning-return-r6-v1.1.md",
    "problems/2022-B4/reviews/reasoning-return-r5-acceptance.md",
    "problems/2022-B4/reviews/reasoning-return-r5-acceptance.json",
    "problems/2022-B4/reviews/reasoning-return-r6-acceptance.md",
    "problems/2022-B4/reviews/reasoning-return-r6-acceptance.json",
]]
bounded_context_inputs = [bind(path) for path in [
    "problems/2022-B4/proofs/reviewed-return-r3-v1.1.md",
    "problems/2022-B4/proofs/reviewed-rational-base-shadow-return-v1.1.md",
]]

previous_expected = {"path": PREVIOUS + "manifest-v1.json", "bytes": 3352,
                     "sha256": "db33ac733a1bb5321ab6fc059357e48d8162d19165d4bf40dbd14f26379230c4"}
previous_manifest_fp = checked(previous_expected)
previous_manifest = read_json(previous_expected["path"])
previous_validation_fp = bind(PREVIOUS + "input-validation-v1.json")
previous_validation = read_json(previous_validation_fp["path"])
before = occurrences
for rec in rows(previous_validation):
    checked(rec)
previous_occurrences = occurrences - before
previous_records = [checked(rec) for rec in previous_manifest["records"]]
older = {}
for rec in previous_validation["older_own_records"] + previous_records + [previous_manifest_fp]:
    actual = checked(rec)
    older[actual["path"]] = actual
assert len(older) == 313

author_obligations = (ROOT / (TARGET + "obligations-v1.md")).read_text()
ledger = (ROOT / (PREFIX + "issues-v1.md")).read_text()
assert set(re.findall(r"R7-O[0-9]{2}", author_obligations)) == {f"R7-O{i:02d}" for i in range(1, 47)}
assert set(re.findall(r"R7-O[0-9]{2}", ledger)) == {f"R7-O{i:02d}" for i in range(1, 47)}
assert set(re.findall(r"R7R2-[0-9]{2}", ledger)) == {f"R7R2-{i:02d}" for i in range(1, 59)}
for suffix in ["initial-v1.md", "issues-v1.md", "source-checks-v1.md"]:
    assert (ROOT / (PREFIX + suffix)).read_text().strip()

usage = {"at_utc": "2026-10-17 16:38:15 UTC", "total_used_percent": 52,
         "window_minutes": 10080, "reset_unix": 1792745187,
         "ordinary_usage_allowed": True, "total_ceiling_percent": 90,
         "integration_reserve": True}
validation = {
    "checked_at_utc": now, "reviewer": "/root/review_2022_complexity_r2",
    "status": "complete initially blind whole R2; no substantive defect found; old-scope advisory N1; no promotion",
    "requested_model": "gpt-6.1-sol", "requested_reasoning_effort": "max",
    "independently_verified_effective_settings": None,
    "metadata_only_not_mathematical_evidence": True,
    "new_R7_peer_report_ledger_sources_manifest_or_findings_read": False,
    "new_R7_peer_prefix_guarded_against_content_and_hash": FORBIDDEN,
    "unused_assigned_prefix_confirmed_before_first_write": True,
    "new_R7_constructor_or_proof_contributor": False,
    "root_generic_assignment_supplied_no_new_R7_inference": True,
    "older_R0_R3_S1_S2_F5_authorship_root_F5_carry_contribution_R4_review_disclosed": True,
    "old_authored_input_not_fresh_independent_self_recertification": True,
    "constructor_old_R4_authorship_and_F5_R6_review_roles_disclosed": True,
    "complete_current_main46_obligations_failures_constructor_checks_sources_worklog_freeze_read": True,
    "constructor_freezer_inspected_as_TEXT_not_executed": True,
    "constructor_ten_artifact_records_verified": constructor_records,
    "constructor_saved_metadata_rows_reverified": metadata_refs,
    "constructor350_prior_paths_preserved": True,
    "complete_accepted_bodies_and_scope_records_freshly_read": fresh_complete_inputs,
    "bounded_R3_R4_interface_reads_not_fresh_full_unrelated_section_read": bounded_context_inputs,
    "accepted_authorities_and_declared_record_counts": authority_rows,
    "accepted_F5_R6_complete_raw_suffix_preservation": suffix_rows,
    "truncated_combined_output_resolved_by_bounded_F5_and_companion_reads": True,
    "all_constructor_obligation_ids": [f"R7-O{i:02d}" for i in range(1, 47)],
    "complete_reviewer_inference_check_ids": [f"R7R2-{i:02d}" for i in range(1, 59)],
    "substantive_issues_identified": 0, "author_repair_requested": False,
    "advisories": [{"id": "N1", "scope": "Old F5 explanatory no-tenfold warning must be limited to old argument; new10C consequence makes global reading too broad", "R7_explicitly_flags_and_qualifies": True, "old_bytes_edited": False, "coordinator_reconciliation_pending": True}],
    "R7A_both_directions_all_integer_ranges_strict_endpoints_official_states_reconstructed": True,
    "R7B_binary_potential_scaling_positive_integer_inverse_even_phase_bijection_reconstructed": True,
    "R7C_all_ten_full_expansions_arbitrary_fiber_one_radix_seed_and_carry_reconstructed": True,
    "R7C_eventual9_9_8_tails_and_entire_nine_positive_ceiling_seeds_reconstructed": True,
    "R7D_uniqueness_spacing_actual_predecessors_well_ordering_and_UNPROVED_bridge_reconstructed": True,
    "C_vs10C_not_integer_multiplication_fiber_invariance": True,
    "source_interval_union_and_residue_hypotheses_checked_at_actual_primary_texts": True,
    "primary_actual_read_scopes_recorded_in_complete_source_checks": True,
    "AEV_printed_question_proper_subset_qualification_checked_against_original_DM": True,
    "ordinary_infinite_path_no_tenfold_future_to_past_termination_annual_or_novelty_claim": False,
    "mathematical_program_scan_CAS_certificate_source_algorithm_or_author_rerun": False,
    "new_native_PDF_download_cache_mutation_or_live_binary_identity_claim": False,
    "previous_own_manifest": previous_manifest_fp, "previous_own_validation": previous_validation_fp,
    "previous_declared_metadata_occurrences_reverified": previous_occurrences,
    "all_source_document_fingerprint_occurrences_verified": occurrences,
    "input_unique_paths_verified": len(inventory),
    "deduplication_policy": "Every occurrence checked; complete unique inventory and exact immutable parent references retained",
    "deduplicated_all_verified_input_records": [inventory[p] for p in sorted(inventory)],
    "older_own_records": [older[p] for p in sorted(older)],
    "older_own_unique_frozen_paths_preserved": len(older),
    "old_shared_Git_cache_other_owner_edits_spawning_contact_charge_bypass": False,
    "direct_weekly_telemetry": usage, "all_verified": True,
}
save("input-validation-v1.json", validation)
names = ["initial-v1.md", "issues-v1.md", "source-checks-v1.md", "freeze-v1.py", "input-validation-v1.json"]
manifest = {
    "frozen_at_utc": now, "reviewer": validation["reviewer"], "status": validation["status"],
    "requested_model": "gpt-6.1-sol", "requested_reasoning_effort": "max",
    "independently_verified_effective_settings": None,
    "constructor_target_main": main_expected, "constructor_target_freeze": freeze_expected,
    "whole_claims_reviewed": ["R7A exact phased real iff and ordinary all-time converse", "R7B scaled phase-aligned ceiling bijection", "R7C conditional full10/ordinary9 complete fibers at10C", "R7D discrete feasible growth and exact ordinary predecessor scope"],
    "all46_constructor_obligations_covered": True, "complete_reviewer_inference_checks": 58,
    "substantive_issues_identified": 0, "author_repair_requested": False,
    "old_F5_explanatory_scope_advisory_N1": True,
    "N1_not_formal_F5_lemma_refutation_or_new_R7_defect": True,
    "initial_frozen_before_any_new_R7_peer_findings": True,
    "new_R7_nonconstructor_independence_and_older_roles_disclosed": True,
    "one_ordinary_start_one_C_one_radix_and_full_fiber_recovery_preserved": True,
    "external_imports_classical_attributed_with_actual_primary_read_limits": True,
    "ordinary_infinite_path_termination_no_tenfold_annual_or_novelty_claim": False,
    "mathematical_program_scan_CAS_certificate_source_algorithm_or_author_rerun": False,
    "source_document_fingerprint_occurrences_verified": occurrences,
    "input_unique_paths_verified": len(inventory),
    "repeated_historical_rows_deduplicated_with_immutable_source_references": True,
    "older_own_unique_frozen_paths_preserved": len(older),
    "old_shared_Git_cache_other_owner_edits_spawning_contact_charge_bypass": False,
    "direct_weekly_telemetry": usage, "records": [fp(PREFIX + suffix) for suffix in names],
}
save("manifest-v1.json", manifest)
print(json.dumps({"frozen_at_utc": now, "manifest": fp(PREFIX + "manifest-v1.json"),
                  "records": manifest["records"], "all46_obligations_58_checks_complete": True,
                  "source_occurrences_verified": occurrences, "input_unique_paths_verified": len(inventory),
                  "older_own_unique_frozen_paths_preserved": len(older),
                  "substantive_issues_identified": 0, "old_scope_advisory_N1": True}, indent=2))
