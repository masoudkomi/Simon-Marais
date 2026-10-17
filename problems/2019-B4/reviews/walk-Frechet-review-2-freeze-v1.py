"""Administrative SHA/JSON integrity only; no mathematical program or test."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2019-B4/reviews/walk-Frechet-review-2-"
AUTHOR_MANIFEST = "problems/2019-B4/notes/coordinator-walk-Frechet-manifest-v1.json"


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
assert fp(AUTHOR_MANIFEST)["bytes"] == 2046
assert fp(AUTHOR_MANIFEST)["sha256"] == "bd895bb6d18dee9a66fa337cce0b5f7330aa1a76c34a0bc8f692022611c5012d"
author = read_json(AUTHOR_MANIFEST)
author_rows = [checked(rec) for rec in author["records"] + author["accepted_and_scope_inputs"]]
assert len(author_rows) == 8
assert author_rows[0]["bytes"] == 15923
assert author_rows[0]["sha256"] == "a62416fe466f21265b6f6572ce5333f7bbe75744cb17c293ef963288b73bf8f2"
source = read_json(PREFIX + "sources-v1.json")
source_rows = [checked(rec) for rec in all_fps(source)]
assert len(source_rows) == 7

map_authorities = []
for path in ["problems/2019-B4/reviews/acceptance.json",
             "problems/2019-B4/reviews/secondpass-acceptance.json"]:
    authority = read_json(path)
    rows = []
    for rel, sha in authority["artifacts"].items():
        row = fp("problems/2019-B4/" + rel)
        assert row["sha256"] == sha, rel
        rows.append(dict(row, matches=True))
    map_authorities.append({"authority": fp(path), "actual_path_to_sha_map_checked": rows})
assert [len(item["actual_path_to_sha_map_checked"]) for item in map_authorities] == [7, 14]
r7_authority_path = "problems/2019-B4/reviews/reasoning-return-r7-acceptance.json"
r7_rows = [checked(rec) for rec in all_fps(read_json(r7_authority_path))]
assert len(r7_rows) == 9
accepted_r7 = "problems/2019-B4/proofs/reviewed-reasoning-return-r7-v1.1.md"
raw_r7 = "problems/2019-B4/notes/reasoning-return-r7-candidate-v1.md"
assert (ROOT / accepted_r7).read_bytes().endswith((ROOT / raw_r7).read_bytes())

previous_manifest_path = "problems/2021-B4/notes/reasoning-return-r8-freeze-v1.json"
previous_input_path = "problems/2021-B4/notes/reasoning-return-r8-input-validation-v1.json"
assert fp(previous_manifest_path)["bytes"] == 3602
assert fp(previous_manifest_path)["sha256"] == "9d366b0c0eee1a56dae269a2aeb197627516d00f2d87d17a4d6c93304b1919b8"
previous_input = read_json(previous_input_path)
older = []
for item in previous_input["older_own_packets"]:
    older.append({"manifest": checked(item["manifest"]),
                  "checks": [checked(rec) for rec in item["checks"]]})
older.append({"manifest": fp(previous_manifest_path),
              "checks": [checked(rec) for rec in read_json(previous_manifest_path)["artifacts"]]})
assert len(older) == 58
gk_addendum = checked(previous_input["GK_separate_telemetry_addendum_preserved"])

main_text = (ROOT / author["records"][0]["path"]).read_text()
obligation_text = main_text.split("## Complete WHOLE-audit obligations", 1)[1]
assert set(re.findall(r"(?m)^([0-9]+)\.", obligation_text)) == {str(i) for i in range(1, 13)}
ledger = (ROOT / (PREFIX + "issues-v1.md")).read_text()
assert set(re.findall(r"DG2-R[0-9]{2}", ledger)) == {"DG2-R" + str(i).zfill(2) for i in range(1, 44)}
covered = set()
for group in re.findall(r"\|DG2-R[0-9]{2}\|([0-9,]+)\|", ledger):
    covered.update(group.split(","))
assert covered == {str(i) for i in range(1, 13)}

usage = {"at_utc": "2026-10-17 15:47:23 UTC (direct telemetry and UTC clock)",
         "total_used_percent": 49, "window_minutes": 10080,
         "reset_unix": 1792745187, "total_ceiling_percent": 90,
         "integration_reserve": True, "ordinary_usage_allowed": True}
validation = {
    "checked_at_utc": now,
    "metadata_only_not_mathematical_evidence": True,
    "author_manifest": fp(AUTHOR_MANIFEST),
    "author_direct_records_checked": author_rows,
    "source_declared_fingerprints_checked": source_rows,
    "accepted_old_authorities_and_actual_maps_checked": map_authorities,
    "secondpass_register_not_incorrectly_treated_as_raw_suffix": True,
    "accepted_R7_authority": fp(r7_authority_path),
    "accepted_R7_authority_declared_fingerprints_checked": r7_rows,
    "accepted_R7_exact_raw_suffix": {"accepted": fp(accepted_r7), "raw": fp(raw_r7), "matches": True},
    "complete_accepted_relevant_bodies_and_scope_authorities_read": True,
    "older_own_packets": older,
    "all_fifty_eight_older_own_packets_unchanged": True,
    "GK_separate_telemetry_addendum_preserved": gk_addendum,
    "assigned_prefix_confirmed_unused_before_first_write": True,
    "complete_main_all_twelve_obligations_and_postfreeze_context_read": True,
    "forty_three_inference_checks_cover_all_twelve_obligations": True,
    "DG1_full_sign_offset_phase_diagonal_and_empty_argument_reconstructed": True,
    "DG2_full_global_incoming_intervals_closed_pinches_and_grid_vertex_reconstruction": True,
    "classical_polygonal_minimum_attainment_explicitly_justified_in_report": True,
    "DG3_fixed_bidegree_square_injection_all_m_limit_and_supremum_reconstructed": True,
    "DG4_exact_uniform_pair_count_probability_and_log_rate_reconstructed": True,
    "old_R7_authorship_and_other_roles_disclosed_not_self_recertification": True,
    "new_DG_construction_contribution_by_reviewer": False,
    "root_constructor_excluded_from_independent_review_count": True,
    "new_DG_peer_report_findings_or_later_root_inspection_read_before_complete_initial_freeze": False,
    "no_substantive_defect_or_required_repair_found": True,
    "exact_lambda_actual_defect_original_b_ratio_full_annual_or_novelty_claim": False,
    "mathematical_program_CAS_scan_sampler_or_author_rerun": False,
    "new_external_counting_theorem_import": False,
    "postfreeze_ECCC_addendum_context_only_not_new_DG_premise": True,
    "new_native_retrieval_cache_mutation_download_or_source_wait": False,
    "Git_shared_old_byte_edit_spawning_charge_contact_or_bypass": False,
    "only_assigned_current_review_prefix_written": True,
    "recommendation_only_not_coordinator_promotion": True,
    "operational_notes": [
        "Initial rg --files restricted to own walk-Frechet-review-2-* prefix returned no files, exit 1; prefix unused.",
        "A read-only lookup used older own filename monotone-ratio-review-2-freezer-v1.py, which did not exist; rg located the actual freeze-v1.py; no file mutation.",
        "One own-draft apply_patch context did not match and was rejected atomically; corrected patch completed before this initial freeze.",
        "Only administrative fingerprints/JSON/obligation-label coverage were programmed. All mathematical reconstruction was by hand."
    ],
    "latest_authoritative_weekly_usage": usage,
}
save("input-validation-v1.json", validation)
output = {
    "frozen_at_utc": now,
    "metadata_only_not_mathematical_evidence": True,
    "author_direct_fingerprints_checked": len(author_rows),
    "source_declared_fingerprints_checked": len(source_rows),
    "old_acceptance_authority_map_counts": [7, 14],
    "R7_authority_fingerprint_occurrences_checked": len(r7_rows),
    "accepted_R7_raw_suffix_unchanged": True,
    "whole_inference_checks": 43,
    "all_author_obligations": 12,
    "older_own_packets_unchanged": len(older),
    "all_hash_checks_passed": True,
    "no_substantive_defect_or_required_repair_found": True,
    "initial_whole_review_blind_before_peer_findings": True,
    "postfreeze_literature_context_not_new_premise": True,
    "recommendation_only_not_promotion": True,
    "latest_authoritative_weekly_usage": usage,
    "command": "python3 problems/2019-B4/reviews/walk-Frechet-review-2-freeze-v1.py",
}
save("freeze-output-v1.json", output)
names = ["initial-v1.md", "issues-v1.md", "source-checks-v1.md", "sources-v1.json",
         "freeze-v1.py", "input-validation-v1.json", "freeze-output-v1.json"]
manifest = {
    "frozen_at_utc": now,
    "status": "complete initially blind WHOLE review recommendation; no promotion",
    "reviewer": "/root/review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "target_manifest": fp(AUTHOR_MANIFEST),
    "target_main": author_rows[0],
    "postfreeze_context_addendum": source_rows[0],
    "claims_reviewed": ["DG1", "DG2", "DG3", "DG4"],
    "whole_inference_checks": 43,
    "all_author_obligations": 12,
    "new_DG_peer_findings_unread_before_complete_initial_freeze": True,
    "new_DG_nonconstructor_whole_reconstruction": True,
    "older_R7_authorship_and_other_roles_disclosed": True,
    "independent_recertification_of_own_R7": False,
    "root_DG_constructor_excluded_from_independent_review_count": True,
    "no_substantive_defect_or_required_repair_found": True,
    "exact_lambda_actual_defect_original_b_ratio_annual_or_novelty_claim": False,
    "postfreeze_addendum_not_new_DG_premise": True,
    "all_fifty_eight_older_own_packets_unchanged": True,
    "mathematical_program_scan_CAS_sampler_or_author_rerun": False,
    "Git_shared_old_byte_cache_mutation_spawning_charge_contact_or_bypass": False,
    "latest_authoritative_weekly_usage": usage,
    "command": output["command"],
    "records": [fp(PREFIX + name) for name in names],
}
save("manifest-v1.json", manifest)
print(json.dumps(dict(output, manifest=fp(PREFIX + "manifest-v1.json")), indent=2))
