"""Administrative hash/JSON integrity only; no mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2025-B4/reviews/original-weight-selection-review-2-"
TARGET = "problems/2025-B4/notes/coordinator-original-weight-selection-candidate-v1.md"
TARGET_SHA = "ef41445567edb53e53980b9edfbba2739cb1879f048e19b9e64f48e2e684ad3e"
AUTHOR_MANIFEST = "problems/2025-B4/notes/coordinator-original-weight-selection-manifest-v1.json"
AUTHOR_SHA = "f73e2c9152c196f1b39b360fa7c6fb4ba6d53dcf64a4abb7385c78ced8fc91a3"


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
assert fp(TARGET)["sha256"] == TARGET_SHA
assert fp(AUTHOR_MANIFEST)["sha256"] == AUTHOR_SHA
author = read_json(AUTHOR_MANIFEST)
author_artifacts = [checked(rec) for rec in author["artifacts"]]
author_inputs = [checked(rec) for rec in author["inputs"]]
assert len(author_artifacts) == 3 and len(author_inputs) == 5

previous_input_path = "problems/2025-B4/reviews/reasoning-return-r4-review-2-input-validation-v1.json"
previous_manifest_path = "problems/2025-B4/reviews/reasoning-return-r4-review-2-manifest-v1.json"
assert fp(previous_manifest_path)["sha256"] == "ee9e59780ebd28d429fbf0f2aa39a4920a9b770ce672af76c2a55e080a843ccb"
previous_input = read_json(previous_input_path)
previous_manifest = read_json(previous_manifest_path)
older = []
for item in previous_input["older_own_packets"]:
    older.append({"manifest": checked(item["manifest"]),
                  "checks": [checked(rec) for rec in item["checks"]]})
older.append({"manifest": fp(previous_manifest_path),
              "checks": [checked(rec) for rec in previous_manifest["records"]]})
assert len(older) == 44
gk_addendum = checked(previous_input["GK_separate_telemetry_addendum_preserved"])

ms_accept_path = "problems/2025-B4/reviews/diagonal-moment-acceptance.json"
ms_authority_checks = [checked(rec) for rec in all_fps(read_json(ms_accept_path))]
ledger = read_json(PREFIX + "issues-v1.json")
assert len(ledger["checks"]) == 30
covered = {o for row in ledger["checks"] for o in row["obligations"]}
assert covered == set(range(1, 19))
assert ledger["substantive_objections"] == []
assert ledger["required_author_repairs"] == []

usage = {"at_utc": "2026-10-17 12:53:52 UTC (paired clock/telemetry check)",
         "total_used_percent": 39, "window_minutes": 10080,
         "reset_unix": 1792745187, "total_ceiling_percent": 90,
         "integration_reserve": True}
validation = {
    "checked_at_utc": now, "metadata_only": True,
    "constructor_manifest": fp(AUTHOR_MANIFEST),
    "constructor_three_artifacts": author_artifacts,
    "constructor_five_declared_inputs": author_inputs,
    "accepted_MS_complete_body_and_scope_read": fp("problems/2025-B4/proofs/reviewed-diagonal-moment-v1.1.md"),
    "accepted_MS_authority": fp(ms_accept_path),
    "accepted_MS_authority_declared_fingerprints": ms_authority_checks,
    "primary_read_scopes_reused_from_immediately_preceding_FS_R2_continuous_session": True,
    "later_primary_existing_cache": fp(".cache/literature/deep-literature-r1/2025-bartolome-mihailescu-binary-thue-v2.pdf"),
    "no_invented_binary_hash_for_original_author_web_view": True,
    "older_own_packets": older,
    "all_forty_four_older_own_packets_unchanged": True,
    "GK_separate_telemetry_addendum_preserved": gk_addendum,
    "complete_initially_blind_whole_reconstruction": True,
    "OW_actual_target_first_read_AFTER_complete_FS_R2_initial_freeze": True,
    "new_peer_OW_findings_or_later_root_inspection_read": False,
    "root_FS_R1_read": False,
    "new_2022_R5_target_or_findings_read_during_this_audit": False,
    "new_OW_constructor_strategy_or_repair_contributor": False,
    "old_FS_PG_CF1_review_and_unrelated_2021_author_roles_disclosed": True,
    "universal_half_weight_kernel_or_sparse_zero_hypothesis_accepted": False,
    "full_external_proof_source_repair_or_Diophantine_exclusion_accepted": False,
    "mathematical_program_CAS_scan_enumeration_or_author_rerun": False,
    "only_current_assigned_prefix_written": True,
    "candidate_shared_old_or_Git_mutation": False,
}
save("input-validation-v1.json", validation)

output = {
    "checked_at_utc": now,
    "metadata_only_no_mathematical_computation": True,
    "candidate": fp(TARGET),
    "constructor_manifest": fp(AUTHOR_MANIFEST),
    "constructor_artifacts": len(author_artifacts),
    "constructor_inputs": len(author_inputs),
    "accepted_MS_authority_declared_records_checked": len(ms_authority_checks),
    "whole_claims": ["OW1", "OW2", "OW3"],
    "per_inference_ledger_rows": 30,
    "author_obligations_covered": len(covered),
    "older_own_packets_unchanged": len(older),
    "all_hash_checks_passed": True,
    "substantive_objections": 0,
    "required_author_repairs": 0,
    "peer_OW_findings_or_later_root_inspection_read_before_freeze": False,
    "latest_authoritative_weekly_usage": usage,
    "command": "python3 problems/2025-B4/reviews/original-weight-selection-review-2-freeze-v1.py",
}
save("freeze-output-v1.json", output)
names = ["initial-v1.md", "issues-v1.json", "source-checks-v1.md",
         "freeze-v1.py", "input-validation-v1.json", "freeze-output-v1.json"]
manifest = {
    "frozen_at_utc": now,
    "status": "complete initially blind independent nonconstructor WHOLE OW1-OW3 initial R2 audit",
    "reviewer": "/root/review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_sha256": TARGET_SHA,
    "constructor_manifest_sha256": AUTHOR_SHA,
    "whole_claims": ["OW1", "OW2", "OW3"],
    "per_inference_ledger_rows": 30,
    "author_obligations_covered": 18,
    "substantive_objections": 0, "required_author_repairs": 0,
    "OW_actual_target_first_read_AFTER_complete_FS_R2_initial_freeze": True,
    "old_review_and_author_roles_disclosed": True,
    "new_OW_constructor_strategy_or_repair_contributor": False,
    "peer_OW_findings_read_before_freeze": False,
    "later_root_OW_inspection_or_root_FS_R1_read_before_freeze": False,
    "findings_sent_before_complete_initial_freeze": False,
    "universal_selection_source_repair_Diophantine_annual_or_novelty_claim": False,
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
