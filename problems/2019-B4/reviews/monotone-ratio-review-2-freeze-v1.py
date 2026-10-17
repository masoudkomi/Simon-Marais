"""Administrative SHA/JSON known-file integrity only; no mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2019-B4/reviews/monotone-ratio-review-2-"
AUTHOR_MANIFEST = "problems/2019-B4/notes/coordinator-monotone-ratio-manifest-v1.json"


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
assert fp(AUTHOR_MANIFEST)["bytes"] == 1763
assert fp(AUTHOR_MANIFEST)["sha256"] == "0af3087adb6814707b7c9257985256b882def1081f339a371b456af4f88dec8f"
author = read_json(AUTHOR_MANIFEST)
author_rows = [checked(rec) for rec in author["records"] + author["accepted_inputs"]]
assert len(author_rows) == 6
assert author_rows[0]["bytes"] == 9239
assert author_rows[0]["sha256"] == "67649f48ebd0f599461fa01cde4e5c37c8fdff0781b9decf4430705848396c29"
source = read_json(PREFIX + "sources-v1.json")
source_rows = [checked(rec) for rec in all_fps(source)]
assert len(source_rows) == 5

secondpass_path = "problems/2019-B4/reviews/secondpass-acceptance.json"
secondpass = read_json(secondpass_path)
secondpass_rows = []
for rel, sha in secondpass["artifacts"].items():
    row = fp("problems/2019-B4/" + rel)
    assert row["sha256"] == sha, rel
    secondpass_rows.append(dict(row, matches=True))
r7_authority_path = "problems/2019-B4/reviews/reasoning-return-r7-acceptance.json"
r7_authority_rows = [checked(rec) for rec in all_fps(read_json(r7_authority_path))]
accepted_r7 = "problems/2019-B4/proofs/reviewed-reasoning-return-r7-v1.1.md"
raw_r7 = "problems/2019-B4/notes/reasoning-return-r7-candidate-v1.md"
assert (ROOT / accepted_r7).read_bytes().endswith((ROOT / raw_r7).read_bytes())
context_paths = [
    "AGENTS.md", "problems/2019-B4/statement.md",
    "problems/2019-B4/reviews/secondpass-acceptance.md",
    "problems/2019-B4/reviews/reasoning-return-r7-acceptance.md",
    "problems/2019-B4/notes/reasoning-return-r7-source-audit-v1.md",
]

previous_manifest_path = "problems/2024-B4/reviews/Hermitian-all-index-review-2-manifest-v1.json"
previous_input_path = "problems/2024-B4/reviews/Hermitian-all-index-review-2-input-validation-v1.json"
assert fp(previous_manifest_path)["bytes"] == 3377
assert fp(previous_manifest_path)["sha256"] == "dd2aa253163896a117d7ee17a2c756b6def8971a03d79b8ea4bca689c509ae01"
previous_input = read_json(previous_input_path)
older = []
for item in previous_input["older_own_packets"]:
    older.append({"manifest": checked(item["manifest"]),
                  "checks": [checked(rec) for rec in item["checks"]]})
older.append({"manifest": fp(previous_manifest_path),
              "checks": [checked(rec) for rec in read_json(previous_manifest_path)["records"]]})
assert len(older) == 56
gk_addendum = checked(previous_input["GK_separate_telemetry_addendum_preserved"])
main_text = (ROOT / author["records"][0]["path"]).read_text()
obligation_text = main_text.split("## Twelve complete WHOLE-audit obligations", 1)[1]
assert set(re.findall(r"(?m)^([0-9]+)\.", obligation_text)) == {str(i) for i in range(1, 13)}
ledger = (ROOT / (PREFIX + "issues-v1.md")).read_text()
assert set(re.findall(r"MR2-R[0-9]{2}", ledger)) == {"MR2-R" + str(i).zfill(2) for i in range(1, 29)}
covered = set()
for group in re.findall(r"\|MR2-R[0-9]{2}\|([0-9,]+)\|", ledger):
    covered.update(group.split(","))
assert covered == {str(i) for i in range(1, 13)}

usage = {"at_utc": "2026-10-17 15:15:27 UTC (direct telemetry and UTC clock)",
         "total_used_percent": 47, "window_minutes": 10080,
         "reset_unix": 1792745187, "total_ceiling_percent": 90,
         "integration_reserve": True, "ordinary_usage_allowed": True}
validation = {
    "checked_at_utc": now,
    "metadata_only_not_mathematical_evidence": True,
    "author_manifest": fp(AUTHOR_MANIFEST),
    "author_direct_records_checked": author_rows,
    "source_declared_fingerprints_checked": source_rows,
    "accepted_secondpass_authority": fp(secondpass_path),
    "secondpass_actual_path_to_sha_map_checked": secondpass_rows,
    "secondpass_register_correctly_not_treated_as_raw_suffix": True,
    "accepted_R7_authority": fp(r7_authority_path),
    "accepted_R7_authority_declared_fingerprints_checked": r7_authority_rows,
    "accepted_R7_exact_raw_suffix": {"accepted": fp(accepted_r7), "raw": fp(raw_r7), "matches": True},
    "full_relevant_scope_and_source_records_read": [fp(path) for path in context_paths],
    "older_own_packets": older,
    "all_fifty_six_older_own_packets_unchanged": True,
    "GK_separate_telemetry_addendum_preserved": gk_addendum,
    "assigned_prefix_confirmed_unused_before_first_write": True,
    "complete_main_all_twelve_obligations_and_accepted_bodies_read": True,
    "twenty_eight_inference_checks_cover_all_twelve_obligations": True,
    "MR1_full_generic_and_strict_inductions_reconstructed": True,
    "MR2_full_conditional_injection_limit_order_and_defect_bound_reconstructed": True,
    "old_R7_authorship_and_other_roles_disclosed_not_self_recertification": True,
    "new_MR_construction_contribution_by_reviewer": False,
    "root_constructor_excluded_from_independent_review_count": True,
    "new_MR_peer_findings_report_or_later_root_inspection_read_before_complete_initial_freeze": False,
    "no_substantive_defect_or_required_repair_found": True,
    "actual_J_C_C3_positive_defect_exact_lambda_b_ratio_or_annual_claim": False,
    "finite_diagnostic_or_mathematical_program_CAS_scan_or_author_rerun": False,
    "new_external_mathematical_theorem_import": False,
    "new_native_retrieval_cache_mutation_or_source_wait": False,
    "Git_shared_old_byte_edit_spawning_charge_contact_or_bypass": False,
    "only_assigned_current_review_prefix_written": True,
    "recommendation_only_not_coordinator_promotion": True,
    "latest_authoritative_weekly_usage": usage,
}
save("input-validation-v1.json", validation)
output = {
    "frozen_at_utc": now,
    "metadata_only_not_mathematical_evidence": True,
    "author_direct_fingerprints_checked": len(author_rows),
    "source_declared_fingerprints_checked": len(source_rows),
    "secondpass_authority_map_records_checked": len(secondpass_rows),
    "R7_authority_declared_fingerprint_occurrences_checked": len(r7_authority_rows),
    "accepted_R7_raw_suffix_unchanged": True,
    "whole_inference_checks": 28,
    "all_author_obligations": 12,
    "older_own_packets_unchanged": len(older),
    "all_hash_checks_passed": True,
    "no_substantive_defect_or_required_repair_found": True,
    "MR2_J_C_hypothesis_remains_unproved": True,
    "initial_whole_review_blind_before_peer_findings": True,
    "recommendation_only_not_promotion": True,
    "latest_authoritative_weekly_usage": usage,
    "command": "python3 problems/2019-B4/reviews/monotone-ratio-review-2-freeze-v1.py",
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
    "claims_reviewed": ["MR1", "MR2 CONDITIONAL on unproved J_C"],
    "whole_inference_checks": 28,
    "all_author_obligations": 12,
    "new_MR_peer_findings_unread_before_complete_initial_freeze": True,
    "new_MR_nonconstructor_whole_reconstruction": True,
    "older_R7_authorship_and_other_roles_disclosed": True,
    "independent_recertification_of_own_R7": False,
    "root_MR_constructor_excluded_from_independent_review_count": True,
    "no_substantive_defect_or_required_repair_found": True,
    "actual_J_C_C3_defect_regime_lambda_b_ratio_annual_or_novelty_claim": False,
    "all_fifty_six_older_own_packets_unchanged": True,
    "mathematical_program_scan_CAS_or_author_rerun": False,
    "Git_shared_old_byte_cache_mutation_spawning_charge_contact_or_bypass": False,
    "latest_authoritative_weekly_usage": usage,
    "command": output["command"],
    "records": [fp(PREFIX + name) for name in names],
}
save("manifest-v1.json", manifest)
print(json.dumps(dict(output, manifest=fp(PREFIX + "manifest-v1.json")), indent=2))
