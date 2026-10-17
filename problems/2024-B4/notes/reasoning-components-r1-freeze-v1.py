"""Administrative known-file SHA/JSON integrity only. No mathematical code."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2024-B4/notes/reasoning-components-r1-"
BASE = "problems/2024-B4/"


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
    with path.open("x") as out:
        json.dump(obj, out, indent=2, ensure_ascii=False)
        out.write("\n")


now = datetime.now(timezone.utc).isoformat()
source = read_json(PREFIX + "sources-v1.json")
source_rows = [checked(rec) for rec in source["exact_accepted_and_scope_inputs"]]
assert len(source_rows) == 14
assert source_rows[0]["bytes"] == 4707
assert source_rows[0]["sha256"] == "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"

authority_rows = []
for path in source["accepted_authority_paths"]:
    authority = read_json(path)
    rows = [checked(rec) for rec in all_fps(authority)]
    legacy = []
    for relpath, expected in authority.get("artifacts", {}).items():
        if not isinstance(expected, str):
            raise RuntimeError("Unexpected legacy hash entry: " + path)
        actual = fp(BASE + relpath)
        if actual["sha256"] != expected:
            raise RuntimeError("Legacy authority mismatch: " + relpath)
        legacy.append(dict(actual, matches=True))
    authority_rows.append({"authority": fp(path),
                           "declared_fingerprints_checked": rows,
                           "legacy_path_hash_map_checked": legacy})
assert len(authority_rows) == 12
authority_md_rows = [fp(path) for path in source["complete_authority_md_read_paths"]]
assert len(authority_md_rows) == 12
context_rows = [fp(path) for path in source["complete_prior_context_read_paths"]]
assert len(context_rows) == 9

cache_rows = []
for rec in source["read_only_ignored_source_records"]:
    actual = checked(rec)
    if actual["sha256"] != rec["expected_sha256"]:
        raise RuntimeError("Old source baseline mismatch: " + rec["path"])
    cache_rows.append(actual)
assert len(cache_rows) == 2

previous_manifest_rec = source["previous_own_manifest"]
checked(previous_manifest_rec)
assert previous_manifest_rec["bytes"] == 3565
assert previous_manifest_rec["sha256"] == "d638920197fdda4767a14d94072347361c3a53373c0c2e0242333199335152e5"
previous_manifest = read_json(previous_manifest_rec["path"])
previous_input = read_json(source["previous_input_validation_path"])
older = []
for item in previous_input["older_own_packets"]:
    older.append({"manifest": checked(item["manifest"]),
                  "checks": [checked(rec) for rec in item["checks"]]})
assert len(older) == 59
older.append({"manifest": checked(previous_manifest_rec),
              "checks": [checked(rec) for rec in previous_manifest["artifacts"]]})
assert len(older) == 60
gk_addendum = checked(previous_input["GK_separate_telemetry_addendum_preserved"])

obligations = (ROOT / (PREFIX + "obligations-v1.md")).read_text()
assert set(re.findall(r"IC-[0-9]{2}", obligations)) == {"IC-" + str(i).zfill(2) for i in range(1, 49)}
main = (ROOT / (PREFIX + "candidate-v1.md")).read_text()
for label in ["**IC1", "**IC2", "**IC3", "**IC4"]:
    assert label in main
for name in ["candidate-v1.md", "obligations-v1.md", "failed-routes-v1.md",
             "source-audit-v1.md", "worklog-v1.md"]:
    assert (ROOT / (PREFIX + name)).read_text().strip()

usage = source["latest_authoritative_weekly_usage"]
validation = {
    "checked_at_utc": now,
    "metadata_only_not_mathematical_evidence": True,
    "exact_accepted_and_scope_fingerprints_checked": source_rows,
    "complete_accepted_authorities_declared_records_checked": authority_rows,
    "complete_accepted_authority_md_scopes_bound": authority_md_rows,
    "complete_prior_context_bound": context_rows,
    "existing_ignored_J_statement_and_image_read_only_fingerprints_checked": cache_rows,
    "older_own_packets": older,
    "all_sixty_older_own_packets_unchanged": True,
    "GK_separate_telemetry_addendum_preserved": gk_addendum,
    "assigned_new_prefix_confirmed_unused_before_first_write": True,
    "preceding_2017_value_r3_complete_constructor_checkpoint_frozen_before_new_assignment": True,
    "complete_official_and_all_twelve_accepted_bodies_and_MD_scopes_read": True,
    "all_forty_eight_whole_audit_obligations_present": True,
    "IC1_source_free_squarefreeness_and_all_boundary_contacts_proved": True,
    "IC1_cofactor_UNIT_and_EXACT_odd_contact_not_lower_bound_only": True,
    "IC2_individual_valuation_and_every_mixed_q_GK_target_including_t2_r1": True,
    "IC3_actual_coordinate_actions_scalar_and_exact_transitive_cases_reconstructed": True,
    "IC3_both_individual_divisor_directions_via_exact_accepted_KC_after_saturation": True,
    "IC4_two_q16_blocks_degrees_and_unresolved_proper_containment_explicit": True,
    "published_distinct_base_coprimality_attributed_not_claimed_new": True,
    "J_primary_coauthor_COMPLETE_statement_and_local_image_read": True,
    "J_original_1993_full_proof_read_or_reconstructed": False,
    "J_later_transversality_all_components_through_P_parity_APN_import": False,
    "IC2_IC3_IC4_applications_explicitly_import_attributed_published_J": True,
    "IC1_has_no_J_or_other_new_external_theorem_dependency": True,
    "old_roles_disclosed_no_independent_recertification_of_own_old_work": True,
    "root_broad_assignment_source_pointer_only_no_new_IC_proof_inference": True,
    "requires_two_OTHER_fresh_initially_blind_nonconstructor_whole_audits": True,
    "candidate_unverified_no_promotion": True,
    "new_qualifying_exponent_family_all_factors_annual_solution_or_novelty_claim": False,
    "mathematical_program_CAS_scan_sampler_or_author_certificate_rerun": False,
    "new_native_source_download_long_wait_cache_mutation_or_redistribution": False,
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
    "authority_legacy_path_hash_map_counts": [len(item["legacy_path_hash_map_checked"]) for item in authority_rows],
    "complete_authority_MD_scopes_bound": len(authority_md_rows),
    "complete_prior_context_bound": len(context_rows),
    "existing_ignored_read_only_source_records_checked": len(cache_rows),
    "whole_audit_obligations": 48,
    "older_own_packets_unchanged": len(older),
    "all_hash_checks_passed": True,
    "claims": ["IC1", "IC2", "IC3", "IC4"],
    "status": "candidate proof - unverified",
    "external_J_source_limit_explicit_original_1993_proof_not_read": True,
    "requires_two_OTHER_fresh_initially_blind_whole_audits": True,
    "latest_authoritative_weekly_usage": usage,
    "command": "python3 problems/2024-B4/notes/reasoning-components-r1-freeze-v1.py",
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
        "IC1 source-free global squarefreeness, smooth coordinate boundary and exact contact1/Q/Q+1",
        "IC2 individual Kasami component valuation necessity and arbitrary different-valuation/mixed-q coprimality using J",
        "IC3 actual symmetry saturation, exact transitive cases2/3/5 and unrestricted individual iff via accepted KC using J",
        "IC4 exact two-block q16 gcd obstruction with proper occurrences explicitly unresolved using J",
    ],
    "whole_audit_obligations": 48,
    "requires_two_OTHER_fresh_initially_blind_nonconstructor_whole_audits": True,
    "root_broad_assignment_source_pointer_only_no_new_IC_proof_inference_contribution": True,
    "old_author_and_reviewer_roles_disclosed": True,
    "J_primary_coauthor_statement_verified_original_1993_proof_not_read": True,
    "IC1_source_free_and_later_applications_external_J_dependency_explicit": True,
    "same_valuation_proper_blocks_non_base_components_annual_classification_or_novelty_resolved": False,
    "new_qualifying_exponent_family_claimed": False,
    "mathematical_program_CAS_scan_sampler_optimizer_or_author_rerun": False,
    "all_sixty_older_own_packets_unchanged": True,
    "Git_shared_old_byte_cache_edit_spawning_charge_contact_or_bypass": False,
    "latest_authoritative_weekly_usage": usage,
    "command": output["command"],
    "artifacts": [fp(PREFIX + name) for name in names],
}
save("freeze-v1.json", manifest)
print(json.dumps(dict(output, main=fp(PREFIX + "candidate-v1.md"),
                      manifest=fp(PREFIX + "freeze-v1.json")), indent=2))
