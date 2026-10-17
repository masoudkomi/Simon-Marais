"""Administrative fingerprints and JSON only; no mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2024-B4/reviews/P2-indecomposable-review-1-"
TARGET = "problems/2024-B4/notes/coordinator-P2-indecomposable-return-v1.md"
TARGET_SHA = "44a91d25943bb3d25f3c4a9c7fc2c2b7f498692889bf82b7dabbdb610b57c957"
AUTHOR_MANIFEST = "problems/2024-B4/notes/coordinator-P2-indecomposable-manifest-v1.json"
AUTHOR_SHA = "ab71ed21157e434de2d487628fae2c72748e6582e2f0e16fc7ed6e37005fc17b"


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
assert fp(TARGET)["bytes"] == 8550
assert fp(TARGET)["sha256"] == TARGET_SHA
assert fp(AUTHOR_MANIFEST)["bytes"] == 1108
assert fp(AUTHOR_MANIFEST)["sha256"] == AUTHOR_SHA
author_records = [checked(rec) for rec in read_json(AUTHOR_MANIFEST)["records"]]
assert len(author_records) == 3
gk_accept_path = "problems/2024-B4/reviews/generalized-Kasami-acceptance.json"
gk_authority_rows = [checked(rec) for rec in all_fps(read_json(gk_accept_path))]
gk_manifest_path = "problems/2024-B4/notes/coordinator-generalized-Kasami-r1-manifest-v1.json"
assert fp(gk_manifest_path)["sha256"] == "50c3269d28a49327e28e216a857fdb711dae8875cab127645bc4081f2ac9ec65"
gk_records = [checked(rec) for rec in read_json(gk_manifest_path)["records"]]
assert len(gk_records) == 6
gk_input_path = "problems/2024-B4/notes/coordinator-generalized-Kasami-r1-input-validation-v1.json"
gk_input = read_json(gk_input_path)
gk_input_rows = [checked(rec) for rec in gk_input["records"]]
assert len(gk_input_rows) == 417
assert len({rec["path"] for rec in gk_input_rows}) == 214
gk_old_motivation = checked(gk_input["motivation_cache_only_not_new_theorem_premise"])

previous_input_path = "problems/2021-B4/notes/reasoning-return-r7-input-validation-v1.json"
previous_manifest_path = "problems/2021-B4/notes/reasoning-return-r7-freeze-v1.json"
assert fp(previous_manifest_path)["sha256"] == "d29dc9823b24ae2df97ee1c506cb8fe8881a2ec2d82a206e2a7411566df7afa8"
previous_input = read_json(previous_input_path)
older = []
for item in previous_input["older_own_packets"]:
    older.append({"manifest": checked(item["manifest"]),
                  "checks": [checked(rec) for rec in item["checks"]]})
older.append({"manifest": fp(previous_manifest_path),
              "checks": [checked(rec) for rec in read_json(previous_manifest_path)["artifacts"]]})
assert len(older) == 48
gk_addendum = checked(previous_input["GK_separate_telemetry_addendum_preserved"])
ledger = read_json(PREFIX + "issues-v1.json")
assert len(ledger["checks"]) == 32
assert {row["id"] for row in ledger["checks"]} == {
    "DIR1-" + str(i).zfill(2) for i in range(1, 33)}
covered = {o for row in ledger["checks"] for o in row["obligations"]}
assert covered == set(range(1, 9))
assert ledger["substantive_objections"] == []
assert ledger["required_author_repairs"] == []
assert all(row["disposition"] == "clear" for row in ledger["checks"])
usage = {"at_utc": "2026-10-17 13:48:08 UTC (paired direct telemetry and clock)",
         "total_used_percent": 42, "window_minutes": 10080,
         "reset_unix": 1792745187, "total_ceiling_percent": 90,
         "integration_reserve": True, "ordinary_usage_allowed": True}
validation = {
    "checked_at_utc": now, "metadata_only_no_mathematical_computation": True,
    "constructor_manifest": fp(AUTHOR_MANIFEST),
    "constructor_three_records": author_records,
    "accepted_GK_complete_body_read": fp("problems/2024-B4/proofs/reviewed-generalized-Kasami-v1.1.md"),
    "accepted_GK_complete_scope_text_read": fp("problems/2024-B4/reviews/generalized-Kasami-acceptance.md"),
    "accepted_GK_authority_JSON_read": fp(gk_accept_path),
    "accepted_GK_authority_declared_fingerprints": gk_authority_rows,
    "GK_frozen_constructor_manifest": fp(gk_manifest_path),
    "GK_six_artifacts": gk_records,
    "GK_old_input_declared_fingerprints": gk_input_rows,
    "GK_old_motivation_cache_preserved_not_new_premise": gk_old_motivation,
    "official_statement_read_in_continuous_session": fp("problems/2024-B4/statement.md"),
    "applicable_protocol_read": fp("AGENTS.md"),
    "primary_Kreso_complete_section2_text_read_no_binary_hash_claim": True,
    "primary_PDF_overbar_visual_inspection_not_claimed": True,
    "older_own_packets": older,
    "all_forty_eight_older_own_packets_unchanged": True,
    "GK_separate_telemetry_addendum_preserved": gk_addendum,
    "old_T1_T4_C7_C11_authorship_and_CP_GK_KC_CJ_whole_review_roles_disclosed": True,
    "new_DI_strategy_construction_or_repair_contribution": False,
    "new_peer_DI_findings_or_later_root_inspection_read_before_freeze": False,
    "first_DI_target_read_AFTER_complete_2021_R7_freeze": True,
    "complete_initially_blind_whole_DI1_DI2_reconstruction": True,
    "all_eight_end_obligations_reconstructed": True,
    "exact_inner_fiber_and_exact_local_order_product_reconstructed": True,
    "all_critical_points_and_values_and_exact_order_q_reconstructed": True,
    "arbitrary_coefficient_extensions_and_composite_degrees_included": True,
    "composition_not_multiplication_and_not_higher_inner_use_exclusion": True,
    "queued_UW_or_RK_target_or_new_peer_findings_read": False,
    "mathematical_program_CAS_scan_enumeration_certificate_replay_or_author_rerun": False,
    "only_current_assigned_prefix_written": True,
    "candidate_old_shared_cache_or_Git_mutation": False,
    "full_composition_factorization_annual_or_novelty_claim": False,
}
save("input-validation-v1.json", validation)
output = {
    "checked_at_utc": now, "metadata_only_no_mathematical_computation": True,
    "candidate": fp(TARGET), "constructor_manifest": fp(AUTHOR_MANIFEST),
    "constructor_records_checked": len(author_records),
    "accepted_GK_authority_fingerprint_occurrences_checked": len(gk_authority_rows),
    "accepted_GK_frozen_artifacts_checked": len(gk_records),
    "accepted_GK_old_input_occurrences_checked": len(gk_input_rows),
    "accepted_GK_old_input_unique_paths_checked": len({row["path"] for row in gk_input_rows}),
    "whole_claims": ["DI1", "DI2"], "per_inference_ledger_rows": 32,
    "author_obligations_covered": len(covered),
    "older_own_packets_unchanged": len(older), "all_hash_checks_passed": True,
    "substantive_objections": 0, "required_author_repairs": 0,
    "new_peer_DI_findings_or_later_root_inspection_read_before_freeze": False,
    "latest_authoritative_weekly_usage": usage,
    "command": "python3 problems/2024-B4/reviews/P2-indecomposable-review-1-freeze-v1.py",
}
save("freeze-output-v1.json", output)
names = ["initial-v1.md", "issues-v1.json", "source-checks-v1.md",
         "freeze-v1.py", "input-validation-v1.json", "freeze-output-v1.json"]
manifest = {
    "frozen_at_utc": now,
    "status": "complete initially blind independent nonconstructor WHOLE DI1-DI2 initial R1 audit",
    "reviewer": "/root/review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_sha256": TARGET_SHA, "constructor_manifest_sha256": AUTHOR_SHA,
    "whole_claims": ["DI1", "DI2"], "per_inference_ledger_rows": 32,
    "author_obligations_covered": 8, "substantive_objections": 0,
    "required_author_repairs": 0,
    "old_authorship_and_CP_GK_KC_CJ_whole_review_roles_disclosed": True,
    "new_DI_construction_strategy_or_repair_contribution": False,
    "new_peer_DI_findings_or_later_root_inspection_read_before_freeze": False,
    "findings_sent_before_complete_initial_freeze": False,
    "full_composition_factorization_annual_or_novelty_claim": False,
    "mathematical_program_CAS_scan_enumeration_author_rerun": False,
    "candidate_shared_old_files_cache_or_git_mutation": False,
    "spawning_contact_charge_or_access_bypass": False,
    "coordinator_promotion_performed": False,
    "latest_authoritative_weekly_usage": usage,
    "command": output["command"],
    "records": [fp(PREFIX + name) for name in names],
}
save("manifest-v1.json", manifest)
print(json.dumps(dict(output, manifest=fp(PREFIX + "manifest-v1.json")), indent=2))
