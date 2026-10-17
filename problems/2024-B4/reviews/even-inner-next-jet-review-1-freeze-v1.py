"""Administrative file fingerprints/JSON only; no mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2024-B4/reviews/even-inner-next-jet-review-1-"
TARGET = "problems/2024-B4/notes/coordinator-even-inner-next-jet-return-v2.md"
TARGET_SHA = "5197ab6841d0a97356484cf3a08a7163055449fa879bd8010886e28158532ef6"
AUTHOR = "problems/2024-B4/notes/coordinator-even-inner-next-jet-manifest-v2.json"
AUTHOR_SHA = "7aec0a9fd4109910ea8d95e3b8e50860c4e8083bbe82249196617274d95b03a3"


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
assert fp(TARGET)["bytes"] == 12232
assert fp(TARGET)["sha256"] == TARGET_SHA
assert fp(AUTHOR)["bytes"] == 2368
assert fp(AUTHOR)["sha256"] == AUTHOR_SHA
author_records = [checked(rec) for rec in read_json(AUTHOR)["records"]]
assert len(author_records) == 9
authority_paths = [
    "problems/2024-B4/reviews/generalized-Kasami-acceptance.json",
    "problems/2024-B4/reviews/composition-Kasami-acceptance.json",
    "problems/2024-B4/reviews/P2-critical-jet-acceptance.json",
]
authority_rows = [
    {"authority": fp(path),
     "declared_fingerprints_checked": [checked(rec) for rec in all_fps(read_json(path))]}
    for path in authority_paths
]
previous_input_path = "problems/2019-B4/notes/reasoning-return-r7-input-validation-v1.json"
previous_manifest_path = "problems/2019-B4/notes/reasoning-return-r7-freeze-v1.json"
assert fp(previous_manifest_path)["bytes"] == 3755
assert fp(previous_manifest_path)["sha256"] == "72ec54ed96255aaa17abe0eda98a98423e2e490f1ccd2c1b0a1c674f72238bf7"
previous_input = read_json(previous_input_path)
older = []
for item in previous_input["older_own_packets"]:
    older.append({"manifest": checked(item["manifest"]),
                  "checks": [checked(rec) for rec in item["checks"]]})
older.append({"manifest": fp(previous_manifest_path),
              "checks": [checked(rec) for rec in read_json(previous_manifest_path)["artifacts"]]})
assert len(older) == 52
gk_addendum = checked(previous_input["GK_separate_telemetry_addendum_preserved"])
ledger = read_json(PREFIX + "issues-v1.json")
assert len(ledger["checks"]) == 40
assert {row["id"] for row in ledger["checks"]} == {
    "NJR1-" + str(i).zfill(2) for i in range(1, 41)}
covered = {o for row in ledger["checks"] for o in row["obligations"]}
assert covered == set(range(1, 11))
assert ledger["substantive_objections"] == []
assert ledger["required_author_repairs"] == []
assert all(row["disposition"] == "clear" for row in ledger["checks"])
usage = {
    "at_utc": "2026-10-17 14:24:02 UTC (direct telemetry followed by UTC clock)",
    "total_used_percent": 44, "window_minutes": 10080,
    "reset_unix": 1792745187, "total_ceiling_percent": 90,
    "integration_reserve": True, "ordinary_usage_allowed": True,
}
validation = {
    "checked_at_utc": now,
    "metadata_only_no_mathematical_computation": True,
    "constructor_manifest": fp(AUTHOR),
    "constructor_nine_records": author_records,
    "accepted_complete_GK_CP_CJ_bodies_and_authorities_read": True,
    "accepted_authority_declared_fingerprints": authority_rows,
    "only_GK_recurrence_degrees_identity_and_CP1_whole_criterion_imported": True,
    "CJ_context_local_order_and_new_all_index_next_jet_rederived": True,
    "old_v1_body_assumed_as_theorem_or_local_extension_audit": False,
    "old_v1_bytes_hash_preserved_as_history": True,
    "unverified_DI_or_later_odd_period_root_material_used": False,
    "official_statement_complete_local_read": fp("problems/2024-B4/statement.md"),
    "official2024_B4b_primary_PDF_freshly_opened_and_domain_checked": True,
    "official_primary_url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf",
    "fresh_primary_binary_hash_or_cache_identity_claimed": False,
    "new_external_source_theorem_or_unseen_full_paper_proof_import": False,
    "applicable_protocol_read": fp("AGENTS.md"),
    "older_own_packets": older,
    "all_fifty_two_older_own_packets_unchanged": True,
    "GK_separate_telemetry_addendum_preserved": gk_addendum,
    "first_NJ_target_read_AFTER_complete2019R7_construction_freeze": True,
    "older_T1_T4_C7_C11_authorship_and_CP_GK_KC_CJ_DI_review_roles_disclosed": True,
    "new_NJ_construction_lead_extension_or_repair_contribution": False,
    "new_peer_NJ_findings_or_later_root_inspection_read_before_freeze": False,
    "queued2020_target_or_findings_read_before_complete_NJ_freeze": False,
    "complete_initially_blind_whole_NJ1_v2_NJ2_v2_reconstruction": True,
    "all_ten_end_obligations_reconstructed": True,
    "all_even_r_all_s_arbitrary_H_including_inseparable_and_zero_cases_checked": True,
    "finite_Frobenius_constants_not_variable_periodicity_checked": True,
    "exact_local_order_q_both_next_recurrence_summands_and_all_later_jets_checked": True,
    "whole_homogeneous_fixed_family_divisor_only_not_arbitrary_components": True,
    "odd_inner_other_factors_annual_full_solution_or_novelty_claim": False,
    "mathematical_program_CAS_scan_enumeration_certificate_replay_or_author_rerun": False,
    "only_current_assigned_prefix_written": True,
    "candidate_old_shared_cache_or_Git_mutation": False,
    "spawning_charge_contact_or_access_bypass": False,
}
save("input-validation-v1.json", validation)
output = {
    "checked_at_utc": now, "metadata_only_no_mathematical_computation": True,
    "candidate": fp(TARGET), "constructor_manifest": fp(AUTHOR),
    "constructor_records_checked": len(author_records),
    "accepted_authority_fingerprint_occurrences_checked": sum(
        len(item["declared_fingerprints_checked"]) for item in authority_rows),
    "whole_claims": ["NJ1-v2", "NJ2-v2"],
    "per_inference_ledger_rows": 40, "author_obligations_covered": len(covered),
    "older_own_packets_unchanged": len(older), "all_hash_checks_passed": True,
    "substantive_objections": 0, "required_author_repairs": 0,
    "new_peer_NJ_findings_or_later_root_inspection_read_before_freeze": False,
    "latest_authoritative_weekly_usage": usage,
    "command": "python3 problems/2024-B4/reviews/even-inner-next-jet-review-1-freeze-v1.py",
}
save("freeze-output-v1.json", output)
names = ["initial-v1.md", "issues-v1.json", "source-checks-v1.md",
         "freeze-v1.py", "input-validation-v1.json", "freeze-output-v1.json"]
manifest = {
    "frozen_at_utc": now,
    "status": "complete initially blind independent nonconstructor WHOLE NJ-v2 initial R1 audit",
    "reviewer": "/root/review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_sha256": TARGET_SHA, "constructor_manifest_sha256": AUTHOR_SHA,
    "whole_claims": ["NJ1-v2", "NJ2-v2"],
    "per_inference_ledger_rows": 40, "author_obligations_covered": 10,
    "substantive_objections": 0, "required_author_repairs": 0,
    "older_T1_T4_C7_C11_authorship_and_CP_GK_KC_CJ_DI_review_roles_disclosed": True,
    "new_NJ_constructor_or_contributor": False,
    "new_peer_NJ_findings_or_later_root_inspection_read_before_freeze": False,
    "findings_sent_before_complete_initial_freeze": False,
    "complete_v2_whole_reconstruction_not_partial_extension_check": True,
    "old_v1_proof_assumed": False,
    "both_claims_exact_quantifiers_boundaries_and_full_proofs_reconstructed": True,
    "odd_inner_other_factors_annual_full_solution_or_novelty_claim": False,
    "mathematical_program_CAS_scan_enumeration_author_rerun": False,
    "candidate_shared_old_files_cache_or_Git_mutation": False,
    "spawning_contact_charge_or_access_bypass": False,
    "coordinator_promotion_performed": False,
    "older_own_packets_unchanged": 52,
    "latest_authoritative_weekly_usage": usage,
    "command": output["command"],
    "records": [fp(PREFIX + name) for name in names],
}
save("manifest-v1.json", manifest)
print(json.dumps(dict(output, manifest=fp(PREFIX + "manifest-v1.json")), indent=2))
