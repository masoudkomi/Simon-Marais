"""Administrative fingerprints/JSON only; no mathematical computation or source rerun."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2025-B4/reviews/original-weight-universal-review-1-"
AUTHOR_PREFIX = "problems/2025-B4/notes/original-weight-universal-return-r1-"
TARGET = AUTHOR_PREFIX + "candidate-v1.md"
TARGET_SHA = "89fb03923c61b7785dbcd2b4ff6e6b6f08e17b7fc1653be6ea72f004831040ed"
AUTHOR_MANIFEST = AUTHOR_PREFIX + "manifest-v1.json"
AUTHOR_SHA = "96ea49d93cec3b08514c1d5d67704f72163332bdbe7feb354c86b821ee90c1a7"


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
assert fp(TARGET)["bytes"] == 19429
assert fp(TARGET)["sha256"] == TARGET_SHA
assert fp(AUTHOR_MANIFEST)["bytes"] == 4060
assert fp(AUTHOR_MANIFEST)["sha256"] == AUTHOR_SHA
author_records = [checked(rec) for rec in read_json(AUTHOR_MANIFEST)["artifacts"]]
assert len(author_records) == 8
author_source_path = AUTHOR_PREFIX + "sources-v1.json"
author_source_rows = [checked(rec) for rec in all_fps(read_json(author_source_path))]
author_input_path = AUTHOR_PREFIX + "input-validation-v1.json"
author_input_rows = [checked(rec) for rec in all_fps(read_json(author_input_path))]
acceptance_paths = [
    "problems/2025-B4/reviews/diagonal-moment-acceptance.json",
    "problems/2025-B4/reviews/Fueter-selection-return-acceptance.json",
    "problems/2025-B4/reviews/original-weight-selection-acceptance.json",
]
authority_rows = [checked(rec) for path in acceptance_paths
                  for rec in all_fps(read_json(path))]
source = read_json(author_source_path)
suffix_rows = []
for body, raw in zip(source["complete_accepted_mathematical_bodies_reread"],
                     source["original_frozen_candidates_preserved_as_exact_suffixes"]):
    checked(body)
    checked(raw)
    assert (ROOT / body["path"]).read_bytes().endswith((ROOT / raw["path"]).read_bytes())
    suffix_rows.append({"accepted": fp(body["path"]), "raw": fp(raw["path"]),
                        "exact_suffix": True})

previous_input_path = "problems/2024-B4/reviews/P2-indecomposable-review-1-input-validation-v1.json"
previous_manifest_path = "problems/2024-B4/reviews/P2-indecomposable-review-1-manifest-v1.json"
assert fp(previous_manifest_path)["sha256"] == "d994367b05c01864231e37d00c667a1664c2a7827c566d6738caaa2aa6d396c8"
previous_input = read_json(previous_input_path)
older = []
for item in previous_input["older_own_packets"]:
    older.append({"manifest": checked(item["manifest"]),
                  "checks": [checked(rec) for rec in item["checks"]]})
older.append({"manifest": fp(previous_manifest_path),
              "checks": [checked(rec) for rec in read_json(previous_manifest_path)["records"]]})
assert len(older) == 49
gk_addendum = checked(previous_input["GK_separate_telemetry_addendum_preserved"])
ledger = read_json(PREFIX + "issues-v1.json")
assert len(ledger["checks"]) == 56
assert {row["id"] for row in ledger["checks"]} == {
    "UWR1-" + str(i).zfill(2) for i in range(1, 57)}
covered = {o for row in ledger["checks"] for o in row["obligations"]}
assert covered == set(range(1, 41))
assert ledger["substantive_objections"] == []
assert ledger["required_author_repairs"] == []
assert all(row["disposition"] == "clear" for row in ledger["checks"])
usage = {"at_utc": "2026-10-17 13:54:38 UTC (paired direct telemetry and clock)",
         "total_used_percent": 42, "window_minutes": 10080,
         "reset_unix": 1792745187, "total_ceiling_percent": 90,
         "integration_reserve": True, "ordinary_usage_allowed": True}
validation = {
    "checked_at_utc": now, "metadata_only_no_mathematical_computation": True,
    "constructor_manifest": fp(AUTHOR_MANIFEST),
    "constructor_eight_artifacts": author_records,
    "constructor_complete_source_record": fp(author_source_path),
    "constructor_source_declared_fingerprints": author_source_rows,
    "constructor_input_validation": fp(author_input_path),
    "constructor_old_input_declared_fingerprints": author_input_rows,
    "complete_accepted_MS_FS_OW_authority_JSON_read": [fp(path) for path in acceptance_paths],
    "accepted_authority_declared_fingerprints": authority_rows,
    "complete_accepted_mathematical_bodies_read": source["complete_accepted_mathematical_bodies_reread"],
    "exact_accepted_suffixes": suffix_rows,
    "complete_acceptance_scope_texts_read": [
        fp("problems/2025-B4/reviews/Fueter-selection-return-acceptance.md"),
        fp("problems/2025-B4/reviews/original-weight-selection-acceptance.md")],
    "official_statement_read": fp("problems/2025-B4/statement.md"),
    "applicable_protocol_read": fp("AGENTS.md"),
    "fresh_primary_original_complete_section2_3_Lemma3_and_section4_3_read": True,
    "fresh_primary_later_complete_PDF_pages5_8_and15_18_read": True,
    "new_primary_binary_download_or_cache_mutation": False,
    "system_Python_pypdf_unavailable_then_bundled_runtime_used_for_read_only_extraction": True,
    "older_own_packets": older, "all_forty_nine_older_own_packets_unchanged": True,
    "GK_separate_telemetry_addendum_preserved": gk_addendum,
    "old_FS_OW_PG_CF1_whole_review_roles_disclosed": True,
    "new_UW_strategy_construction_lead_or_repair_contribution": False,
    "new_peer_UW_findings_or_later_root_inspection_read_before_freeze": False,
    "first_UW_target_read_AFTER_complete_DI_R1_freeze": True,
    "queued_reciprocal_kernel_target_or_new_peer_findings_read": False,
    "complete_initially_blind_whole_UW1_UW4_reconstruction": True,
    "all_forty_obligations_reconstructed": True,
    "all_three_moments_signs_denominators_and_exact_six_fiber_bound_reconstructed": True,
    "conditional_u_fiber_descent_and_both_polynomial_root_contradictions_reconstructed": True,
    "both_branches_give_actual_positive_integer_vectors_at_original_weight": True,
    "Fourier_and_reciprocal_or_higher_jet_application_scopes_separate": True,
    "mathematical_program_CAS_scan_enumeration_certificate_replay_or_author_rerun": False,
    "only_current_assigned_prefix_written": True,
    "candidate_old_shared_cache_or_Git_mutation": False,
    "source_proof_repair_Diophantine_annual_or_novelty_claim": False,
}
save("input-validation-v1.json", validation)
output = {
    "checked_at_utc": now, "metadata_only_no_mathematical_computation": True,
    "candidate": fp(TARGET), "constructor_manifest": fp(AUTHOR_MANIFEST),
    "constructor_artifacts_checked": len(author_records),
    "constructor_source_declared_fingerprint_occurrences_checked": len(author_source_rows),
    "constructor_input_declared_fingerprint_occurrences_checked": len(author_input_rows),
    "constructor_input_unique_paths_checked": len({row["path"] for row in author_input_rows}),
    "accepted_authority_fingerprint_occurrences_checked": len(authority_rows),
    "accepted_exact_suffixes_checked": len(suffix_rows),
    "whole_claims": ["UW1", "UW2", "UW3", "UW4"],
    "per_inference_ledger_rows": 56, "author_obligations_covered": len(covered),
    "older_own_packets_unchanged": len(older), "all_hash_checks_passed": True,
    "substantive_objections": 0, "required_author_repairs": 0,
    "new_peer_UW_findings_or_later_root_inspection_read_before_freeze": False,
    "queued_RK_target_or_findings_read": False,
    "latest_authoritative_weekly_usage": usage,
    "command": "python3 problems/2025-B4/reviews/original-weight-universal-review-1-freeze-v1.py",
}
save("freeze-output-v1.json", output)
names = ["initial-v1.md", "issues-v1.json", "source-checks-v1.md",
         "freeze-v1.py", "input-validation-v1.json", "freeze-output-v1.json"]
manifest = {
    "frozen_at_utc": now,
    "status": "complete initially blind independent nonconstructor WHOLE UW1-UW4 initial R1 audit",
    "reviewer": "/root/review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_sha256": TARGET_SHA, "constructor_manifest_sha256": AUTHOR_SHA,
    "whole_claims": ["UW1", "UW2", "UW3", "UW4"],
    "per_inference_ledger_rows": 56, "author_obligations_covered": 40,
    "substantive_objections": 0, "required_author_repairs": 0,
    "old_FS_OW_PG_CF1_whole_review_roles_disclosed": True,
    "new_UW_construction_strategy_lead_or_repair_contribution": False,
    "new_peer_UW_findings_or_later_root_inspection_read_before_freeze": False,
    "findings_sent_before_complete_initial_freeze": False,
    "queued_RK_packet_read_before_complete_UW_freeze": False,
    "source_proof_repair_Diophantine_annual_or_novelty_claim": False,
    "mathematical_program_CAS_scan_enumeration_author_rerun": False,
    "candidate_shared_old_files_cache_or_git_mutation": False,
    "spawning_contact_charge_or_access_bypass": False,
    "coordinator_promotion_performed": False,
    "latest_authoritative_weekly_usage": usage,
    "command": output["command"], "records": [fp(PREFIX + name) for name in names],
}
save("manifest-v1.json", manifest)
print(json.dumps(dict(output, manifest=fp(PREFIX + "manifest-v1.json")), indent=2))
