"""Administrative exact-file fingerprints and JSON only; no mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2020-B4/reviews/reasoning-return-r5-review-2-"
TARGET = "problems/2020-B4/notes/reasoning-return-r5-candidate-v1.md"
TARGET_SHA = "26cb2d236722c41a67fc7d23bcc6af1da162cb39182d6e846286b19cb554c67a"
AUTHOR = "problems/2020-B4/notes/reasoning-return-r5-freeze-v1.json"
AUTHOR_SHA = "bb654165037bef83a9c5105278775dda450268d0858937358cf54c0e3e7a3bfe"


def fp(path):
    data = (ROOT / path).read_bytes()
    return {"path": str(path), "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def checked(rec):
    actual = fp(rec["path"])
    if actual["bytes"] != rec["bytes"] or actual["sha256"] != rec["sha256"]:
        raise RuntimeError("Fingerprint mismatch: " + rec["path"])
    return dict(actual, matches=True)


def read_json(path):
    return json.loads((ROOT / path).read_text())


def all_fps(obj):
    if isinstance(obj, dict):
        if {"path", "bytes", "sha256"} <= obj.keys():
            yield obj
        for value in obj.values():
            yield from all_fps(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from all_fps(value)


def save(suffix, obj):
    path = ROOT / (PREFIX + suffix)
    if path.exists():
        raise RuntimeError("Refusing to overwrite: " + str(path))
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


now = datetime.now(timezone.utc).isoformat()
assert fp(TARGET)["bytes"] == 23485
assert fp(TARGET)["sha256"] == TARGET_SHA
assert fp(AUTHOR)["bytes"] == 3920
assert fp(AUTHOR)["sha256"] == AUTHOR_SHA
author_records = [checked(rec) for rec in read_json(AUTHOR)["artifacts"]]
assert len(author_records) == 8
author_input_path = "problems/2020-B4/notes/reasoning-return-r5-input-validation-v1.json"
author_input_rows = [checked(rec) for rec in all_fps(read_json(author_input_path))]
source_path = "problems/2020-B4/notes/reasoning-return-r5-sources-v1.json"
source_rows = [checked(rec) for rec in all_fps(read_json(source_path))]
native_pdf_rows = [checked(rec) for rec in read_json(source_path)["public_native_PDF_downloads"]]
assert len(native_pdf_rows) == 6
assert all((ROOT / rec["path"]).read_bytes().startswith(b"%PDF-") for rec in native_pdf_rows)
r4_authority_path = "problems/2020-B4/reviews/reasoning-return-r4-acceptance.json"
r4_authority_rows = [checked(rec) for rec in all_fps(read_json(r4_authority_path))]
r4_accepted_path = "problems/2020-B4/proofs/reviewed-reasoning-return-r4-v1.2.md"
r4_raw_path = "problems/2020-B4/notes/reasoning-return-r4-candidate-v1.1.md"
assert (ROOT / r4_accepted_path).read_bytes().endswith((ROOT / r4_raw_path).read_bytes())
previous_input_path = "problems/2024-B4/reviews/even-inner-next-jet-review-1-input-validation-v1.json"
previous_manifest_path = "problems/2024-B4/reviews/even-inner-next-jet-review-1-manifest-v1.json"
assert fp(previous_manifest_path)["bytes"] == 3158
assert fp(previous_manifest_path)["sha256"] == "846164e683e61ed4adeac6152023b5a68ea8e25b87d4e5d5368ebe6a8995d756"
previous_input = read_json(previous_input_path)
older = []
for item in previous_input["older_own_packets"]:
    older.append({"manifest": checked(item["manifest"]),
                  "checks": [checked(rec) for rec in item["checks"]]})
older.append({"manifest": fp(previous_manifest_path),
              "checks": [checked(rec) for rec in read_json(previous_manifest_path)["records"]]})
assert len(older) == 53
gk_addendum = checked(previous_input["GK_separate_telemetry_addendum_preserved"])
ledger = read_json(PREFIX + "issues-v1.json")
assert len(ledger["checks"]) == 64
assert {row["id"] for row in ledger["checks"]} == {
    "R5R2-" + str(i).zfill(2) for i in range(1, 65)}
covered = {o for row in ledger["checks"] for o in row["obligations"]}
assert covered == set(range(1, 53))
assert ledger["substantive_objections"] == []
assert ledger["required_author_repairs"] == []
assert all(row["disposition"] == "clear" for row in ledger["checks"])
usage = {
    "at_utc": "2026-10-17 14:34:09 UTC (direct telemetry followed by UTC clock)",
    "total_used_percent": 45, "window_minutes": 10080,
    "reset_unix": 1792745187, "total_ceiling_percent": 90,
    "integration_reserve": True, "ordinary_usage_allowed": True,
}
validation = {
    "checked_at_utc": now,
    "metadata_only_no_mathematical_computation": True,
    "constructor_manifest": fp(AUTHOR),
    "constructor_eight_artifacts": author_records,
    "constructor_input_validation_declared_fingerprints_checked": author_input_rows,
    "constructor_source_declared_fingerprints_checked": source_rows,
    "six_existing_native_primary_PDF_cache_files_fingerprinted": native_pdf_rows,
    "native_PDF_magic_checked": True,
    "live_web_extraction_and_native_cache_byte_identity_claimed": False,
    "new_public_download_cache_edit_or_PDF_render": False,
    "accepted_R4_authority": fp(r4_authority_path),
    "accepted_R4_authority_declared_fingerprints_checked": r4_authority_rows,
    "complete_accepted_initial_header_and_linked_body_R4_header_and_repaired_body_read": True,
    "complete_accepted_initial_R4_scope_records_and_source_limits_read": True,
    "accepted_R4_copy_exact_raw_repaired_suffix_unchanged": True,
    "accepted_R4_copy": fp(r4_accepted_path),
    "accepted_R4_raw_suffix": fp(r4_raw_path),
    "official2020_B4b_primary_paper_and_printedp27_dictionary_discussion_read": True,
    "neighboring_preliminary_other_problem_excerpts_investigated_or_reproduced": False,
    "original_Kantor_A_B_statements_and_exception_scope_checked": True,
    "Thas_classical_collineation_statement_and_complete_Proposition2_1_proof_checked": True,
    "Huang_Schmidt_complete_Proposition5_proof_equivalence_scope_checked": True,
    "Xia2018_complete_Theorem5_1_statement_written_proof_index_nontriviality_checked": True,
    "Xia2023v7_complete_Proposition1_2_Theorem1_3_statements_and_Theorem3_7_scope_checked": True,
    "Sun2025v1_actual_definitions_Theorem5_2_Proposition5_17_complete_modified_subsection5_5_read": True,
    "full_CFSG_classical_synthetic_or_Groebner_certificate_proof_reconstructed": False,
    "published_imports_exact_hypotheses_and_read_limits_retained": True,
    "official_statement_local": fp("problems/2020-B4/statement.md"),
    "applicable_protocol_read": fp("AGENTS.md"),
    "older_own_packets": older,
    "all_fifty_three_older_own_packets_unchanged": True,
    "GK_separate_telemetry_addendum_preserved": gk_addendum,
    "first2020_R5_target_read_AFTER_complete_NJ_v2_whole_initial_freeze": True,
    "old_R3_whole_and_F4_repair_review_role_disclosed": True,
    "new_R4_R5_constructor_strategy_lead_or_repair_contribution": False,
    "new_peer_R5_findings_or_later_root_inspection_read_before_freeze": False,
    "complete_initially_blind_whole_R5A_R5E_reconstruction": True,
    "all_fifty_two_end_obligations_reconstructed": True,
    "exact_coset_polynomial_iff_both_directions_and_L2_endpoint_checked": True,
    "prime_point_classical_semilinear_normalizer_both_inclusions_and_scalar_checked": True,
    "all_pair_sums_repeats_zero_triples_and_actual_integer_counts_checked": True,
    "zero_orbit_adjoint_restriction_E00_Gram_diagonal_and_complete_spectra_checked": True,
    "even_flag_equivalence_exact_imports_and_odd_affine_two_orbits_checked": True,
    "extra_saturation_classical_hypothesis_and_necessary_only_matrix_preserved": True,
    "old_q4_q2435_and_R4_moment_repair_trails_preserved": True,
    "annual_full_solution_new_cutoff_or_novelty_claim": False,
    "mathematical_program_CAS_scan_enumeration_certificate_replay_or_author_rerun": False,
    "only_current_assigned_prefix_written": True,
    "candidate_old_shared_cache_or_Git_mutation": False,
    "spawning_charge_contact_or_access_bypass": False,
}
save("input-validation-v1.json", validation)
output = {
    "checked_at_utc": now, "metadata_only_no_mathematical_computation": True,
    "candidate": fp(TARGET), "constructor_manifest": fp(AUTHOR),
    "constructor_artifacts_checked": len(author_records),
    "constructor_input_fingerprint_occurrences_checked": len(author_input_rows),
    "constructor_source_fingerprint_occurrences_checked": len(source_rows),
    "accepted_R4_authority_fingerprint_occurrences_checked": len(r4_authority_rows),
    "native_primary_PDF_cache_files_checked_not_new_downloads": len(native_pdf_rows),
    "accepted_R4_exact_repaired_suffix_unchanged": True,
    "whole_claims": ["R5A", "R5B", "R5C", "R5D", "R5E"],
    "per_inference_ledger_rows": 64, "author_obligations_covered": len(covered),
    "older_own_packets_unchanged": len(older), "all_hash_checks_passed": True,
    "substantive_objections": 0, "required_author_repairs": 0,
    "new_peer_R5_findings_or_later_root_inspection_read_before_freeze": False,
    "latest_authoritative_weekly_usage": usage,
    "command": "python3 problems/2020-B4/reviews/reasoning-return-r5-review-2-freeze-v1.py",
}
save("freeze-output-v1.json", output)
names = ["initial-v1.md", "issues-v1.json", "source-checks-v1.md",
         "freeze-v1.py", "input-validation-v1.json", "freeze-output-v1.json"]
manifest = {
    "frozen_at_utc": now,
    "status": "complete initially blind independent nonconstructor WHOLE R5A-R5E initial R2 audit",
    "reviewer": "/root/review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_sha256": TARGET_SHA, "constructor_manifest_sha256": AUTHOR_SHA,
    "whole_claims": ["R5A", "R5B", "R5C", "R5D", "R5E"],
    "per_inference_ledger_rows": 64, "author_obligations_covered": 52,
    "substantive_objections": 0, "required_author_repairs": 0,
    "old_R3_whole_and_F4_repair_review_roles_disclosed": True,
    "new_R4_R5_construction_lead_or_repair_contribution": False,
    "new_peer_R5_findings_or_later_root_inspection_read_before_freeze": False,
    "findings_sent_before_complete_initial_freeze": False,
    "both_directions_exact_quantifiers_boundaries_and_full_written_deductions_reconstructed": True,
    "published_proof_imports_and_unreconstructed_chains_explicit": True,
    "extra_saturation_classical_hypothesis_and_necessary_only_matrix_preserved": True,
    "annual_full_solution_new_cutoff_or_novelty_claim": False,
    "mathematical_program_CAS_scan_enumeration_author_rerun": False,
    "candidate_shared_old_files_cache_or_Git_mutation": False,
    "spawning_contact_charge_or_access_bypass": False,
    "coordinator_promotion_performed": False,
    "older_own_packets_unchanged": 53,
    "latest_authoritative_weekly_usage": usage,
    "command": output["command"],
    "records": [fp(PREFIX + name) for name in names],
}
save("manifest-v1.json", manifest)
print(json.dumps(dict(output, manifest=fp(PREFIX + "manifest-v1.json")), indent=2))
