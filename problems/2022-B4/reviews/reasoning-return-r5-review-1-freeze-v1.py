"""Administrative known-file fingerprints and JSON checks, never mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2022-B4/reviews/reasoning-return-r5-review-1-"
TARGET = "problems/2022-B4/notes/reasoning-return-r5-candidate-v1.md"
TARGET_SHA = "f08f3e579f9ddeec52746060ab81aec6055f1ecfce24fa2031608eadb7743bef"
AUTHOR_FREEZE = "problems/2022-B4/notes/reasoning-return-r5-freeze-v1.json"
AUTHOR_SHA = "29a0ba60beda79572326525a2ab5fe20b23f0aff1c4129fc9645a86b83ff4601"


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
assert fp(TARGET)["bytes"] == 26928
assert fp(TARGET)["sha256"] == TARGET_SHA
assert fp(AUTHOR_FREEZE)["sha256"] == AUTHOR_SHA
author = read_json(AUTHOR_FREEZE)
author_artifacts = [checked(rec) for rec in author["artifacts"]]
assert len(author_artifacts) == 8
author_input_path = "problems/2022-B4/notes/reasoning-return-r5-input-validation-v1.json"
author_input_rows = [checked(rec) for rec in all_fps(read_json(author_input_path))]
assert len(author_input_rows) == 450
assert len({row["path"] for row in author_input_rows}) == 410
source_json_path = "problems/2022-B4/notes/reasoning-return-r5-sources-v1.json"
declared_source_rows = [checked(rec) for rec in all_fps(read_json(source_json_path))]

previous_input_path = "problems/2025-B4/reviews/original-weight-selection-review-2-input-validation-v1.json"
previous_manifest_path = "problems/2025-B4/reviews/original-weight-selection-review-2-manifest-v1.json"
assert fp(previous_manifest_path)["sha256"] == "fe2d9a9b345cc57bf63140d9b7e61311bbc789c2ccd6359da2d422b02ffa837d"
previous_input = read_json(previous_input_path)
previous_manifest = read_json(previous_manifest_path)
older = []
for item in previous_input["older_own_packets"]:
    older.append({"manifest": checked(item["manifest"]),
                  "checks": [checked(rec) for rec in item["checks"]]})
older.append({"manifest": fp(previous_manifest_path),
              "checks": [checked(rec) for rec in previous_manifest["records"]]})
assert len(older) == 45
gk_addendum = checked(previous_input["GK_separate_telemetry_addendum_preserved"])

accepted_bodies = [
    "problems/2022-B4/proofs/reviewed-rational-base-shadow-return-v1.1.md",
    "problems/2022-B4/proofs/reviewed-return-r3-v1.1.md",
    "problems/2022-B4/proofs/reviewed-arithmetic-complexity-v1.1.md",
]
accepted_scope_paths = [
    "problems/2022-B4/reviews/rational-base-shadow-return-acceptance.md",
    "problems/2022-B4/reviews/return-r3-acceptance.md",
    "problems/2022-B4/reviews/arithmetic-complexity-acceptance.md",
]
accepted_authority_paths = [path[:-3] + ".json" for path in accepted_scope_paths]
authority_rows = [checked(rec) for path in accepted_authority_paths
                  for rec in all_fps(read_json(path))]
ledger = read_json(PREFIX + "issues-v1.json")
assert len(ledger["checks"]) == 60
assert {row["id"] for row in ledger["checks"]} == {
    "R5R1-" + str(i).zfill(2) for i in range(1, 61)
}
covered = {o for row in ledger["checks"] for o in row["obligations"]}
assert covered == set(range(1, 43))
assert ledger["substantive_objections"] == []
assert ledger["required_author_repairs"] == []
assert all(row["disposition"] == "clear" for row in ledger["checks"])

usage = {"at_utc": "2026-10-17 13:04:38 UTC (paired telemetry and clock)",
         "total_used_percent": 40, "window_minutes": 10080,
         "reset_unix": 1792745187, "total_ceiling_percent": 90,
         "integration_reserve": True, "ordinary_usage_allowed": True}
validation = {
    "checked_at_utc": now, "metadata_only_no_mathematical_computation": True,
    "constructor_freeze": fp(AUTHOR_FREEZE),
    "constructor_eight_artifacts": author_artifacts,
    "constructor_input_validation_declared_fingerprints": author_input_rows,
    "constructor_source_JSON_declared_fingerprints": declared_source_rows,
    "accepted_complete_bodies_read": [fp(path) for path in accepted_bodies],
    "accepted_complete_scope_texts_read": [fp(path) for path in accepted_scope_paths],
    "accepted_authority_JSON": [fp(path) for path in accepted_authority_paths],
    "accepted_authority_declared_fingerprints": authority_rows,
    "official_statement_read": fp("problems/2022-B4/statement.md"),
    "applicable_protocol_read": fp("AGENTS.md"),
    "unverified_root_carry_note_fully_rederived_not_accepted_premise": fp(
        "problems/2022-B4/notes/coordinator-AB-bounded-correction-rigidity-v1.md"),
    "raw_source_cache_fingerprints_are_preservation_not_new_binary_download_claims": True,
    "primary_named_passages_freshly_inspected_without_claim_of_entire_external_proof": True,
    "older_own_packets": older,
    "all_forty_five_older_own_packets_unchanged": True,
    "GK_separate_telemetry_addendum_preserved": gk_addendum,
    "old_R3_R4_whole_review_roles_disclosed": True,
    "new_R5_strategy_construction_or_repair_contribution": False,
    "new_peer_R5_findings_or_later_root_inspection_read_before_freeze": False,
    "complete_initially_blind_whole_reconstruction": True,
    "all_five_claims_and_42_obligations_reconstructed": True,
    "exact_nine_conditional_on_positive_ordinary_infinite_AB_lift": True,
    "bound_ten_still_permits_nine": True,
    "proper_set_endpoint_r2_full_residue_set_retained": True,
    "real_and_Z10_evaluations_never_identified": True,
    "source_conjecture_termination_no_ninefold_full_annual_or_novelty_claim": False,
    "mathematical_program_CAS_scan_enumeration_certificate_replay_or_author_rerun": False,
    "only_current_assigned_prefix_written": True,
    "candidate_old_shared_or_Git_mutation": False,
    "next_2024_CJ_packet_or_peer_findings_read_during_R5_audit": False,
}
save("input-validation-v1.json", validation)

output = {
    "checked_at_utc": now, "metadata_only_no_mathematical_computation": True,
    "candidate": fp(TARGET), "constructor_freeze": fp(AUTHOR_FREEZE),
    "constructor_artifacts_checked": len(author_artifacts),
    "constructor_input_record_occurrences_checked": len(author_input_rows),
    "constructor_input_unique_paths_checked": len({row["path"] for row in author_input_rows}),
    "constructor_source_declared_fingerprint_occurrences_checked": len(declared_source_rows),
    "accepted_authority_declared_fingerprint_occurrences_checked": len(authority_rows),
    "whole_claims": ["F5A", "F5B", "F5C", "F5D", "F5E"],
    "per_inference_ledger_rows": 60, "author_obligations_covered": len(covered),
    "older_own_packets_unchanged": len(older),
    "all_hash_checks_passed": True,
    "substantive_objections": 0, "required_author_repairs": 0,
    "new_peer_R5_findings_or_later_root_inspection_read_before_freeze": False,
    "latest_authoritative_weekly_usage": usage,
    "command": "python3 problems/2022-B4/reviews/reasoning-return-r5-review-1-freeze-v1.py",
}
save("freeze-output-v1.json", output)
names = ["initial-v1.md", "issues-v1.json", "source-checks-v1.md",
         "freeze-v1.py", "input-validation-v1.json", "freeze-output-v1.json"]
manifest = {
    "frozen_at_utc": now,
    "status": "complete initially blind independent nonconstructor WHOLE F5A-F5E initial R1 audit",
    "reviewer": "/root/review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_sha256": TARGET_SHA, "constructor_freeze_sha256": AUTHOR_SHA,
    "whole_claims": ["F5A", "F5B", "F5C", "F5D", "F5E"],
    "per_inference_ledger_rows": 60, "author_obligations_covered": 42,
    "substantive_objections": 0, "required_author_repairs": 0,
    "old_R3_R4_whole_review_roles_disclosed": True,
    "new_R5_construction_strategy_or_repair_contribution": False,
    "new_peer_R5_findings_or_later_root_inspection_read_before_freeze": False,
    "findings_sent_before_complete_initial_freeze": False,
    "full_annual_infinite_ordinary_lift_termination_no_ninefold_or_novelty_claim": False,
    "mathematical_program_CAS_scan_enumeration_author_rerun": False,
    "candidate_shared_old_files_or_git_mutation": False,
    "spawning_contact_charge_or_access_bypass": False,
    "coordinator_promotion_performed": False,
    "latest_authoritative_weekly_usage": usage,
    "command": output["command"],
    "records": [fp(PREFIX + name) for name in names],
}
save("manifest-v1.json", manifest)
print(json.dumps(dict(output, manifest=fp(PREFIX + "manifest-v1.json")), indent=2))
