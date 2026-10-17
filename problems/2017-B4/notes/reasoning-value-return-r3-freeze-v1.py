"""Administrative SHA/JSON known-file integrity only; no mathematical code."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/notes/reasoning-value-return-r3-"


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
source = read_json(PREFIX + "sources-v1.json")
source_rows = [checked(rec) for rec in source["exact_accepted_and_scope_inputs"]]
assert len(source_rows) == 7
authority_rows = []
suffix_rows = []
for path in source["accepted_authority_paths"]:
    authority = read_json(path)
    rows = [checked(rec) for rec in all_fps(authority)]
    authority_rows.append({"authority": fp(path), "declared_fingerprints_checked": rows})
    if "accepted_copy" in authority:
        accepted = authority["accepted_copy"]["path"]
        raw = authority["candidate"]["path"]
        assert (ROOT / accepted).read_bytes().endswith((ROOT / raw).read_bytes())
        suffix_rows.append({"accepted": fp(accepted), "raw": fp(raw), "matches": True})
assert [len(item["declared_fingerprints_checked"]) for item in authority_rows] == [7, 9, 9, 9, 7]
assert len(suffix_rows) == 3
context_rows = [fp(path) for path in source["complete_authority_md_and_context_read_paths"]]
assert len(context_rows) == 8

previous_manifest_path = "problems/2019-B4/reviews/walk-Frechet-review-2-manifest-v1.json"
previous_input_path = "problems/2019-B4/reviews/walk-Frechet-review-2-input-validation-v1.json"
assert fp(previous_manifest_path)["bytes"] == 3618
assert fp(previous_manifest_path)["sha256"] == "9f4434b026751155da4794e24e98a40ef0940c42f4bd077464333fe4cee75223"
previous_input = read_json(previous_input_path)
older = []
for item in previous_input["older_own_packets"]:
    older.append({"manifest": checked(item["manifest"]),
                  "checks": [checked(rec) for rec in item["checks"]]})
older.append({"manifest": fp(previous_manifest_path),
              "checks": [checked(rec) for rec in read_json(previous_manifest_path)["records"]]})
assert len(older) == 59
gk_addendum = checked(previous_input["GK_separate_telemetry_addendum_preserved"])

obligations = (ROOT / (PREFIX + "obligations-v1.md")).read_text()
assert set(re.findall(r"R3-[0-9]{2}", obligations)) == {"R3-" + str(i).zfill(2) for i in range(1, 41)}
main = (ROOT / (PREFIX + "candidate-v1.md")).read_text()
for label in ["**HC1", "**HC2", "**HC3"]:
    assert label in main
for name in ["candidate-v1.md", "obligations-v1.md", "failed-routes-v1.md",
             "source-audit-v1.md", "worklog-v1.md"]:
    assert (ROOT / (PREFIX + name)).read_text().strip()

usage = {"at_utc": "2026-10-17 16:11:29 UTC (direct telemetry and UTC clock)",
         "total_used_percent": 50, "window_minutes": 10080,
         "reset_unix": 1792745187, "total_ceiling_percent": 90,
         "integration_reserve": True, "ordinary_usage_allowed": True}
validation = {
    "checked_at_utc": now,
    "metadata_only_not_mathematical_evidence": True,
    "exact_accepted_and_scope_fingerprints_checked": source_rows,
    "complete_accepted_authorities_and_declared_fingerprints_checked": authority_rows,
    "accepted_G_V_OP_complete_raw_suffixes_checked": suffix_rows,
    "DC_and_U_bound_by_actual_exposition_authorities_not_false_raw_suffix": True,
    "complete_context_read_scopes_in_source_audit": context_rows,
    "older_own_packets": older,
    "all_fifty_nine_older_own_packets_unchanged": True,
    "GK_separate_telemetry_addendum_preserved": gk_addendum,
    "assigned_new_prefix_confirmed_unused_before_first_write": True,
    "preceding_DG_whole_review_complete_and_frozen_before_new_construction": True,
    "complete_official_and_accepted_G_V_OP_DC_U_bodies_scopes_read": True,
    "all_forty_whole_audit_obligations_present": True,
    "HC1_finite_actual_heap_capacity_and_full_class_invariant_code_supplied": True,
    "HC1_both_directions_and_exact_staged_parallel_bundle_realization_supplied": True,
    "HC2_actual_class_weighted_SUM_disjoint_chain_cover_and_strict_scopes_supplied": True,
    "HC2_full_sparse_partner_and_mixed_neighbor_order_recovery_supplied": True,
    "HC3_exact_parity_identity_fixed_D_normalization_and_new_error_supplied": True,
    "source_frameworks_classical_attributed_and_all_needed_hypotheses_proved": True,
    "source_binary_hashes_deliberately_null_no_download_claim": True,
    "a0_a1_m1_m2_m3_D1_S0_all_singletons_and_auxiliary_n1_checked_by_hand": True,
    "general_Q_prefix_counterexample_and_missing_quadratic_mass_gap_preserved": True,
    "genuine_failed_bridges_and_effective_E_R_gap_recorded": True,
    "root_broad_assignment_only_no_new_HC_proof_inference_contribution": True,
    "old_roles_disclosed_not_independent_self_recertification": True,
    "requires_two_OTHER_fresh_initially_blind_nonconstructor_whole_audits": True,
    "candidate_unverified_no_promotion": True,
    "leading_logarithmic_direction_error_not_claimed_halved_again": True,
    "exact_value_effective_side_length_rate_actual_computability_annual_or_novelty_claim": False,
    "mathematical_program_CAS_scan_sampler_optimizer_or_certificate_replay": False,
    "new_native_download_source_wait_cache_mutation_or_third_party_redistribution": False,
    "Git_shared_old_byte_edit_spawning_charge_contact_or_bypass": False,
    "only_current_assigned_new_prefix_written": True,
    "latest_authoritative_weekly_usage": usage,
}
save("input-validation-v1.json", validation)
output = {
    "frozen_at_utc": now,
    "metadata_only_not_mathematical_evidence": True,
    "exact_accepted_and_scope_records_checked": len(source_rows),
    "authority_declared_fingerprint_counts": [len(item["declared_fingerprints_checked"]) for item in authority_rows],
    "accepted_G_V_OP_raw_suffixes_unchanged": len(suffix_rows),
    "complete_context_records_bound": len(context_rows),
    "whole_audit_obligations": 40,
    "older_own_packets_unchanged": len(older),
    "all_hash_checks_passed": True,
    "claims": ["HC1", "HC2", "HC3"],
    "status": "candidate proof - unverified",
    "requires_two_OTHER_fresh_initially_blind_whole_audits": True,
    "latest_authoritative_weekly_usage": usage,
    "command": "python3 problems/2017-B4/notes/reasoning-value-return-r3-freeze-v1.py",
}
save("freeze-output-v1.json", output)
names = ["candidate-v1.md", "obligations-v1.md", "failed-routes-v1.md",
         "source-audit-v1.md", "worklog-v1.md", "sources-v1.json", "freeze-v1.py",
         "input-validation-v1.json", "freeze-output-v1.json"]
manifest = {
    "frozen_at_utc": now,
    "status": "candidate proof - unverified",
    "constructor": "/root/review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "claims": [
        "HC1 exact finite commutation-heap capacity H_m(a)=B(1^m,a) and invariant coarsening upper code",
        "HC2 actual-class weighted SUM hierarchy, alternating-chain record and smaller finite gap count",
        "HC3 all fixed D new scalar error g_D=(1/2)h2(1/D), with strict improvement over OP"
    ],
    "whole_audit_obligations": 40,
    "requires_two_OTHER_fresh_initially_blind_nonconstructor_whole_audits": True,
    "root_broad_assignment_only_no_new_HC_proof_inference_contribution": True,
    "old_author_and_reviewer_roles_disclosed": True,
    "actual_tilings_commutation_quotient_weighted_SUM_and_orders_preserved": True,
    "general_Q_realization_and_quadratic_mass_gain_not_assumed": True,
    "leading_logarithmic_error_not_claimed_halved_again": True,
    "exact_value_E_R_effective_rate_computability_full_annual_or_novelty_claim": False,
    "mathematical_program_CAS_scan_sampler_optimizer_or_author_rerun": False,
    "all_fifty_nine_older_own_packets_unchanged": True,
    "Git_shared_old_byte_cache_edit_spawning_charge_contact_or_bypass": False,
    "latest_authoritative_weekly_usage": usage,
    "command": output["command"],
    "artifacts": [fp(PREFIX + name) for name in names],
}
save("freeze-v1.json", manifest)
print(json.dumps(dict(output, manifest=fp(PREFIX + "freeze-v1.json")), indent=2))
