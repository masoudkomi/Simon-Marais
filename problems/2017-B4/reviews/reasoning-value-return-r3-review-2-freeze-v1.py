"""Reviewer administrative integrity only: known-file SHA/JSON, no mathematics."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/reviews/reasoning-value-return-r3-review-2-"
TARGET = "problems/2017-B4/notes/reasoning-value-return-r3-"
FORBIDDEN = "problems/2017-B4/reviews/reasoning-value-return-r3-review-1-"
PREVIOUS = "problems/2020-B4/reviews/reasoning-return-r6-review-2-"


def fp(path):
    path = str(path)
    if path.startswith(FORBIDDEN):
        raise RuntimeError("Blindness guard: refusing new HC peer read/hash")
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


inventory = {}
occurrences = 0


def checked(rec):
    global occurrences
    actual = fp(rec["path"])
    if (actual["bytes"], actual["sha256"]) != (rec["bytes"], rec["sha256"]):
        raise RuntimeError("Fingerprint mismatch: " + rec["path"])
    occurrences += 1
    if actual["path"] in inventory and inventory[actual["path"]] != actual:
        raise RuntimeError("Conflicting immutable record")
    inventory[actual["path"]] = actual
    return actual


def bind(path):
    return checked(fp(path))


def read_json(path):
    if path.startswith(FORBIDDEN):
        raise RuntimeError("Blindness guard: refusing new HC peer JSON")
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
    path = ROOT / (PREFIX + suffix)
    with path.open("x") as handle:
        handle.write(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


now = datetime.now(timezone.utc).isoformat()
main_expected = {"path": TARGET + "candidate-v1.md", "bytes": 22915,
                 "sha256": "e76949699e6f6bfbcf58a4f0c8a8f7e3affa903a92dc5ec61b92887e4fe07bff"}
freeze_expected = {"path": TARGET + "freeze-v1.json", "bytes": 3565,
                   "sha256": "d638920197fdda4767a14d94072347361c3a53373c0c2e0242333199335152e5"}
checked(main_expected)
checked(freeze_expected)
manifest = read_json(freeze_expected["path"])
constructor_rows = [checked(rec) for rec in manifest["artifacts"]]
assert len(constructor_rows) == 9
source = read_json(TARGET + "sources-v1.json")
accepted_inputs = [checked(rec) for rec in source["exact_accepted_and_scope_inputs"]]
assert len(accepted_inputs) == 7

document_refs = []
for path in [TARGET + "sources-v1.json", TARGET + "input-validation-v1.json",
             TARGET + "freeze-output-v1.json"]:
    doc = read_json(path)
    count_before = occurrences
    for rec in rows(doc):
        checked(rec)
    document_refs.append({"source": bind(path),
                          "declared_fingerprint_occurrences_checked": occurrences - count_before - 1})

authority_rows = []
suffix_rows = []
for path in source["accepted_authority_paths"]:
    doc = read_json(path)
    declared = [checked(rec) for rec in rows(doc)]
    authority_rows.append({"source": bind(path),
                           "declared_fingerprint_occurrences_checked": len(declared)})
    if "accepted_copy" in doc:
        accepted_path = doc["accepted_copy"]["path"]
        raw_path = doc["candidate"]["path"]
        assert (ROOT / accepted_path).read_bytes().endswith((ROOT / raw_path).read_bytes())
        suffix_rows.append({"accepted": bind(accepted_path), "raw": bind(raw_path),
                            "entire_raw_submission_is_byte_identical_suffix": True})
assert [row["declared_fingerprint_occurrences_checked"] for row in authority_rows] == [7, 9, 9, 9, 7]
assert len(suffix_rows) == 3
context_rows = [bind(path) for path in source["complete_authority_md_and_context_read_paths"]]

previous_expected = {"path": PREVIOUS + "manifest-v1.json", "bytes": 3931,
                     "sha256": "c49b4b700bacce805a59e131d0f47ec0668fffaea4662a8b1b439ca120e1f841"}
previous_manifest_fp = checked(previous_expected)
previous_manifest = read_json(previous_expected["path"])
previous_validation_path = PREVIOUS + "input-validation-v1.json"
previous_validation_fp = bind(previous_validation_path)
previous_validation = read_json(previous_validation_path)
before = occurrences
for rec in rows(previous_validation):
    checked(rec)
previous_occurrences = occurrences - before
previous_records = [checked(rec) for rec in previous_manifest["records"]]
older = {}
for rec in previous_validation["older_own_records"] + previous_records + [previous_manifest_fp]:
    actual = checked(rec)
    older[actual["path"]] = actual
assert len(older) == 301

author_obligations = (ROOT / (TARGET + "obligations-v1.md")).read_text()
ledger = (ROOT / (PREFIX + "issues-v1.md")).read_text()
assert set(re.findall(r"R3-[0-9]{2}", author_obligations)) == {f"R3-{i:02d}" for i in range(1, 41)}
assert set(re.findall(r"R3-[0-9]{2}", ledger)) == {f"R3-{i:02d}" for i in range(1, 41)}
assert set(re.findall(r"HCR2-[0-9]{2}", ledger)) == {f"HCR2-{i:02d}" for i in range(1, 53)}
for suffix in ["initial-v1.md", "issues-v1.md", "source-checks-v1.md"]:
    assert (ROOT / (PREFIX + suffix)).read_text().strip()

usage = {"at_utc": "2026-10-17 16:21:41 UTC", "total_used_percent": 51,
         "window_minutes": 10080, "reset_unix": 1792745187,
         "ordinary_usage_allowed": True, "total_ceiling_percent": 90,
         "integration_reserve": True}
validation = {
    "checked_at_utc": now,
    "reviewer": "/root/review_2022_complexity_r2",
    "status": "complete initially blind whole R2; no substantive defect found; no promotion",
    "requested_model": "gpt-6.1-sol", "requested_reasoning_effort": "max",
    "independently_verified_effective_settings": None,
    "metadata_only_not_mathematical_evidence": True,
    "new_HC_peer_report_ledger_sources_manifest_or_findings_read": False,
    "new_HC_peer_prefix_explicitly_guarded_against_read_or_hash": FORBIDDEN,
    "unused_assigned_prefix_confirmed_before_first_write": True,
    "new_HC_constructor_or_proof_contributor": False,
    "older_G_authorship_and_V_OP_local_review_roles_disclosed": True,
    "accepted_G_is_premise_not_fresh_self_recertification": True,
    "constructor_old_strict_LOCAL_authorship_and_G_review_roles_disclosed": True,
    "complete_new_main_obligations_failed_routes_source_audit_worklog_JSON_freeze_read": True,
    "constructor_freezer_inspected_as_text_NOT_executed": True,
    "constructor_nine_artifacts_verified": constructor_rows,
    "exact_complete_accepted_bodies_and_scope_inputs_freshly_read": accepted_inputs,
    "complete_authority_MD_JSON_and_three_context_texts_read": context_rows,
    "complete_accepted_authorities_declared_records_checked": authority_rows,
    "accepted_G_V_OP_full_raw_suffix_comparisons": suffix_rows,
    "DC_U_bound_by_actual_accepted_expositions_not_false_suffix_claim": True,
    "constructor_saved_metadata_rows_revalidated_not_all_historical_math_reread": document_refs,
    "all_constructor_obligation_ids": [f"R3-{i:02d}" for i in range(1, 41)],
    "complete_reviewer_inference_check_ids": [f"HCR2-{i:02d}" for i in range(1, 53)],
    "substantive_issues_identified": 0, "author_repair_requested": False,
    "HC1_exact_actual_heap_two_directions_one_bundle_inverse_all_endpoints_reconstructed": True,
    "HC1_generic_Q_capacity_is_upper_code_not_equality_or_prefix_sufficiency": True,
    "HC2_all_actual_SUM_chains_strictness_balancing_sparse_recovery_reconstructed": True,
    "HC3_exact_parity_all_fixed_D_limits_binomial_error_strict_comparison_reconstructed": True,
    "retained_actual_general_Q_two_versus_three_counterexample_reconstructed_by_hand": True,
    "strict_finite_gain_not_promoted_to_quadratic_weighted_mass_gap": True,
    "effective_E_R_fixed_D_rate_value_annual_answer_or_novelty_claim": False,
    "primary_read_scope_record_is_separate_source_checks_not_full_external_proof_claim": True,
    "public_web_only_no_new_native_binary_identity_claim": True,
    "mathematical_program_scan_CAS_certificate_replay_source_algorithm_or_author_rerun": False,
    "previous_own_manifest": previous_manifest_fp,
    "previous_own_validation": previous_validation_fp,
    "previous_declared_metadata_occurrences_reverified": previous_occurrences,
    "all_source_document_fingerprint_occurrences_verified": occurrences,
    "input_unique_paths_verified": len(inventory),
    "deduplication_policy": "Every occurrence verified; complete unique inventory below; exact immutable parent metadata references retained",
    "deduplicated_all_verified_input_records": [inventory[p] for p in sorted(inventory)],
    "older_own_records": [older[p] for p in sorted(older)],
    "older_own_unique_frozen_paths_preserved": len(older),
    "old_shared_Git_cache_other_owner_edits_spawning_contact_charge_bypass": False,
    "direct_weekly_telemetry": usage, "all_verified": True,
}
save("input-validation-v1.json", validation)
names = ["initial-v1.md", "issues-v1.md", "source-checks-v1.md", "freeze-v1.py", "input-validation-v1.json"]
output_manifest = {
    "frozen_at_utc": now, "reviewer": validation["reviewer"],
    "status": validation["status"], "requested_model": "gpt-6.1-sol",
    "requested_reasoning_effort": "max", "independently_verified_effective_settings": None,
    "constructor_target_main": main_expected, "constructor_target_freeze": freeze_expected,
    "whole_claims_reviewed": [
        "HC1 actual finite heap capacity, exact B(1^m,a) inverse and generic invariant upper code",
        "HC2 weighted SUM hierarchy, parity-chain strictness, finite balancing and sparse full recovery",
        "HC3 exact fixed-D error g_D=h2(1/D)/2 and strict lower-order improvement over OP"
    ],
    "all40_constructor_obligations_covered": True,
    "complete_reviewer_inference_checks": 52,
    "substantive_issues_identified": 0, "author_repair_requested": False,
    "initial_frozen_before_any_new_peer_HC_findings": True,
    "new_HC_nonconstructor_independence": True,
    "old_G_authorship_not_fresh_self_recertification": True,
    "finite_strictness_general_Q_sufficiency_and_effective_rate_distinctions_preserved": True,
    "external_imports_classical_attributed_with_actual_read_limits": True,
    "exact_value_E_R_computability_full_annual_or_novelty_claim": False,
    "mathematical_program_scan_CAS_certificate_source_algorithm_or_author_rerun": False,
    "source_document_fingerprint_occurrences_verified": occurrences,
    "input_unique_paths_verified": len(inventory),
    "repeated_historical_rows_deduplicated_with_immutable_source_references": True,
    "older_own_unique_frozen_paths_preserved": len(older),
    "old_shared_Git_cache_other_owner_edits_spawning_contact_charge_bypass": False,
    "direct_weekly_telemetry": usage,
    "records": [fp(PREFIX + suffix) for suffix in names],
}
save("manifest-v1.json", output_manifest)
print(json.dumps({"frozen_at_utc": now, "manifest": fp(PREFIX + "manifest-v1.json"),
                  "records": output_manifest["records"],
                  "source_occurrences_verified": occurrences,
                  "input_unique_paths_verified": len(inventory),
                  "older_own_unique_frozen_paths_preserved": len(older),
                  "all40_obligations_52_checks_complete": True,
                  "substantive_issues_identified": 0}, indent=2))
