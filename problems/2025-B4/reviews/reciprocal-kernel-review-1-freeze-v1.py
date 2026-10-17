"""Administrative known-file fingerprints and JSON only; no mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2025-B4/reviews/reciprocal-kernel-review-1-"
TARGET = "problems/2025-B4/notes/coordinator-reciprocal-kernel-return-v1.md"
TARGET_SHA = "4c752f3ca4699ea0c184dbb79d79f9f192182cc91aeac7fd8a459b7b8bea49b8"
AUTHOR_MANIFEST = "problems/2025-B4/notes/coordinator-reciprocal-kernel-manifest-v1.json"
AUTHOR_SHA = "6ba9a9c094b36a530e383e33e65961f1032ffe72fee601699dd135a88223aa86"


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
assert fp(TARGET)["bytes"] == 9541
assert fp(TARGET)["sha256"] == TARGET_SHA
assert fp(AUTHOR_MANIFEST)["bytes"] == 1319
assert fp(AUTHOR_MANIFEST)["sha256"] == AUTHOR_SHA
author_records = [checked(rec) for rec in read_json(AUTHOR_MANIFEST)["records"]]
assert len(author_records) == 4
ms_accept_path = "problems/2025-B4/reviews/diagonal-moment-acceptance.json"
ms_authority_rows = [checked(rec) for rec in all_fps(read_json(ms_accept_path))]
ms_source_path = "problems/2025-B4/notes/coordinator-diagonal-moment-sources-v1.json"
ms_source_rows = [checked(rec) for rec in all_fps(read_json(ms_source_path))]
images = [
    {"path": "/private/tmp/smmc-hasse-1.png", "bytes": 138397,
     "sha256": "58d7747f7a1d5c4c28fa86b03d685f0fd63dfa8381dfea91bbbbded245d96af6"},
    {"path": "/private/tmp/smmc-hasse-2.png", "bytes": 142584,
     "sha256": "7aea97dab952c50ffdb11c08dc17dfbe1e5bb8c15407e8020c264467e8836243"},
    {"path": "/private/tmp/smmc-hasse-3.png", "bytes": 165556,
     "sha256": "63d27f2ba18a51c32ca94677c9469790bf59299c270c6313c48c24892137cfc1"},
    {"path": "/private/tmp/smmc-hasse-4.png", "bytes": 118646,
     "sha256": "0d0f18bd0eb01256f72f4913d81a8623dc28657e72cf5afe68ad391a07fba3f7"},
]
image_rows = [checked(rec) for rec in images]
previous_input_path = "problems/2025-B4/reviews/original-weight-universal-review-1-input-validation-v1.json"
previous_manifest_path = "problems/2025-B4/reviews/original-weight-universal-review-1-manifest-v1.json"
assert fp(previous_manifest_path)["sha256"] == "cd8f4db3a4d5ff6926e36d41e4d37d6ab5ab4f78278e261b2efe11578f93f1c3"
previous_input = read_json(previous_input_path)
older = []
for item in previous_input["older_own_packets"]:
    older.append({"manifest": checked(item["manifest"]),
                  "checks": [checked(rec) for rec in item["checks"]]})
older.append({"manifest": fp(previous_manifest_path),
              "checks": [checked(rec) for rec in read_json(previous_manifest_path)["records"]]})
assert len(older) == 50
gk_addendum = checked(previous_input["GK_separate_telemetry_addendum_preserved"])
uw_target = checked({"path": "problems/2025-B4/notes/original-weight-universal-return-r1-candidate-v1.md",
                     "bytes": 19429,
                     "sha256": "89fb03923c61b7785dbcd2b4ff6e6b6f08e17b7fc1653be6ea72f004831040ed"})
ledger = read_json(PREFIX + "issues-v1.json")
assert len(ledger["checks"]) == 32
assert {row["id"] for row in ledger["checks"]} == {
    "RKR1-" + str(i).zfill(2) for i in range(1, 33)}
covered = {o for row in ledger["checks"] for o in row["obligations"]}
assert covered == set(range(1, 9))
assert ledger["substantive_objections"] == []
assert ledger["required_author_repairs"] == []
assert all(row["disposition"] == "clear" for row in ledger["checks"])
usage = {"at_utc": "2026-10-17 13:59:28 UTC (direct telemetry followed by UTC clock)",
         "total_used_percent": 43, "window_minutes": 10080,
         "reset_unix": 1792745187, "total_ceiling_percent": 90,
         "integration_reserve": True, "ordinary_usage_allowed": True}
validation = {
    "checked_at_utc": now, "metadata_only_no_mathematical_computation": True,
    "constructor_manifest": fp(AUTHOR_MANIFEST),
    "constructor_four_records": author_records,
    "accepted_MS_complete_body_read": fp("problems/2025-B4/proofs/reviewed-diagonal-moment-v1.1.md"),
    "accepted_MS_complete_authority_read": fp(ms_accept_path),
    "accepted_MS_authority_declared_fingerprints": ms_authority_rows,
    "accepted_MS_old_source_record": fp(ms_source_path),
    "accepted_MS_old_source_declared_fingerprints": ms_source_rows,
    "primary_Hasse_all_printed_pages275_280_visually_read": True,
    "primary_Hasse_four_two_page_spreads_inspected_at_original_resolution": image_rows,
    "adjacent_pages274_281_not_part_of_Hasse_paper": True,
    "primary_general_cotangent_and_special_elementary_scopes_distinguished": True,
    "full_classical_analytic_or_unseen_reference_proof_reconstructed": False,
    "primary_Hamahata_introduction_Theorem1_1_complete_Theorem2_1_and_displayed_proof_read": True,
    "publisher_details_click_failed_issue_metadata_and_complete_cached_scan_available": True,
    "PDF_skill_read_and_used_for_read_only_visual_source_inspection": True,
    "new_source_download_cache_PDF_image_edit_or_render": False,
    "official_statement_read_in_continuous_session": fp("problems/2025-B4/statement.md"),
    "applicable_protocol_read": fp("AGENTS.md"),
    "older_own_packets": older, "all_fifty_older_own_packets_unchanged": True,
    "GK_separate_telemetry_addendum_preserved": gk_addendum,
    "separate_UW_target_read_only_AFTER_its_complete_whole_initial_freeze": False,
    "separate_UW_target_was_read_within_prior_completed_UW_audit": uw_target,
    "first_RK_target_read_AFTER_complete_UW_whole_R1_freeze": True,
    "separate_UW_existence_imported_as_accepted_by_this_review": False,
    "old_FS_OW_PG_CF1_and_prior_UW_whole_review_roles_disclosed": True,
    "new_RK_strategy_construction_lead_or_repair_contribution": False,
    "new_peer_RK_findings_or_later_root_inspection_read_before_freeze": False,
    "complete_initially_blind_whole_RK1_RK3_reconstruction": True,
    "all_eight_end_obligations_reconstructed": True,
    "entire_rational_kernel_both_inclusions_and_p3_endpoint_reconstructed": True,
    "fixed_C_affine_injectivity_arbitrary_coordinates_and_Galois_prefactor_checked": True,
    "actual_pair_positive_integral_RK3_remains_conditional": True,
    "mathematical_program_CAS_scan_enumeration_certificate_replay_or_author_rerun": False,
    "only_current_assigned_prefix_written": True,
    "candidate_old_shared_cache_or_Git_mutation": False,
    "source_proof_repair_higher_jet_Diophantine_annual_or_novelty_claim": False,
}
save("input-validation-v1.json", validation)
output = {
    "checked_at_utc": now, "metadata_only_no_mathematical_computation": True,
    "candidate": fp(TARGET), "constructor_manifest": fp(AUTHOR_MANIFEST),
    "constructor_records_checked": len(author_records),
    "accepted_MS_authority_fingerprint_occurrences_checked": len(ms_authority_rows),
    "accepted_MS_source_fingerprint_occurrences_checked": len(ms_source_rows),
    "actual_primary_scanned_spreads_visually_read_and_fingerprinted": len(image_rows),
    "whole_claims": ["RK1", "RK2", "RK3"],
    "per_inference_ledger_rows": 32, "author_obligations_covered": len(covered),
    "older_own_packets_unchanged": len(older), "all_hash_checks_passed": True,
    "substantive_objections": 0, "required_author_repairs": 0,
    "new_peer_RK_findings_or_later_root_inspection_read_before_freeze": False,
    "separate_UW_existence_and_RK3_universal_corollary_remain_conditional": True,
    "latest_authoritative_weekly_usage": usage,
    "command": "python3 problems/2025-B4/reviews/reciprocal-kernel-review-1-freeze-v1.py",
}
save("freeze-output-v1.json", output)
names = ["initial-v1.md", "issues-v1.json", "source-checks-v1.md",
         "freeze-v1.py", "input-validation-v1.json", "freeze-output-v1.json"]
manifest = {
    "frozen_at_utc": now,
    "status": "complete initially blind independent nonconstructor WHOLE RK1-RK3 initial R1 audit",
    "reviewer": "/root/review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_sha256": TARGET_SHA, "constructor_manifest_sha256": AUTHOR_SHA,
    "whole_claims": ["RK1", "RK2", "RK3"],
    "per_inference_ledger_rows": 32, "author_obligations_covered": 8,
    "substantive_objections": 0, "required_author_repairs": 0,
    "old_FS_OW_PG_CF1_and_prior_UW_whole_review_roles_disclosed": True,
    "new_RK_construction_strategy_lead_or_repair_contribution": False,
    "new_peer_RK_findings_or_later_root_inspection_read_before_freeze": False,
    "findings_sent_before_complete_initial_freeze": False,
    "separate_UW_existence_and_RK3_universal_corollary_remain_conditional": True,
    "full_classical_analytic_proof_reconstructed": False,
    "source_proof_repair_higher_jet_Diophantine_annual_or_novelty_claim": False,
    "mathematical_program_CAS_scan_enumeration_author_rerun": False,
    "candidate_shared_old_files_cache_or_git_mutation": False,
    "spawning_contact_charge_or_access_bypass": False,
    "coordinator_promotion_performed": False,
    "latest_authoritative_weekly_usage": usage,
    "command": output["command"], "records": [fp(PREFIX + name) for name in names],
}
save("manifest-v1.json", manifest)
print(json.dumps(dict(output, manifest=fp(PREFIX + "manifest-v1.json")), indent=2))
