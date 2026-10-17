"""Metadata-only independent FS R2 freeze; no mathematical calculations."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2025-B4/reviews/reasoning-return-r4-review-2-"
TARGET = "problems/2025-B4/notes/reasoning-return-r4-candidate-v1.md"
EXPECTED = "29c98bf01d6336020a3720935fc571159db0bdd5159a75a75adf4a78ae038482"
CONSTRUCTOR_FREEZE = "problems/2025-B4/notes/reasoning-return-r4-freeze-v1.json"


def fp(path):
    data = (ROOT / path).read_bytes()
    return {"path": str(path), "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def check(rec):
    got = fp(rec["path"])
    if got["bytes"] != rec["bytes"] or got["sha256"] != rec["sha256"]:
        raise RuntimeError("Hash mismatch: " + rec["path"])
    return dict(got, matches=True)


def read_json(path):
    return json.loads((ROOT / path).read_text())


def all_fps(obj):
    if isinstance(obj, dict):
        if {"path", "bytes", "sha256"} <= obj.keys():
            yield obj
        for v in obj.values():
            yield from all_fps(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from all_fps(v)


def save(suffix, obj):
    path = ROOT / (PREFIX + suffix)
    if path.exists():
        raise RuntimeError("Refusing overwrite: " + str(path))
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


now = datetime.now(timezone.utc).isoformat()
candidate = fp(TARGET)
assert candidate["sha256"] == EXPECTED
submission = read_json(CONSTRUCTOR_FREEZE)
artifacts = [check(rec) for rec in submission["artifacts"]]
assert len(artifacts) == 8
source_path = "problems/2025-B4/notes/reasoning-return-r4-sources-v1.json"
constructor_input_path = "problems/2025-B4/notes/reasoning-return-r4-input-validation-v1.json"
source_checks = [check(rec) for rec in all_fps(read_json(source_path))]
constructor_input_checks = [check(rec) for rec in all_fps(read_json(constructor_input_path))]

previous_input_path = "problems/2021-B4/notes/reasoning-return-r6-input-validation-v1.json"
previous_freeze_path = "problems/2021-B4/notes/reasoning-return-r6-freeze-v1.json"
previous_input = read_json(previous_input_path)
previous_freeze = read_json(previous_freeze_path)
assert fp(previous_freeze_path)["sha256"] == "9c97c3b704fb2b53ce8108991ffca70e04a01760dcbadb8d2712ba339bc24538"
older = []
for item in previous_input["older_own_packets"]:
    older.append({"manifest": check(item["manifest"]),
                  "checks": [check(rec) for rec in item["checks"]]})
older.append({"manifest": fp(previous_freeze_path),
              "checks": [check(rec) for rec in previous_freeze["records"]]})
assert len(older) == 43
gk_addendum = check(previous_input["GK_separate_telemetry_addendum_preserved"])

accepted_bodies = [
    "problems/2025-B4/proofs/reviewed-partial-v1.1.md",
    "problems/2025-B4/proofs/reviewed-power-gap-return-v1.1.md",
    "problems/2025-B4/proofs/reviewed-diagonal-firstcase-v1.1.md",
    "problems/2025-B4/proofs/reviewed-diagonal-moment-v1.1.md",
]
acceptance_mds = [
    "problems/2025-B4/reviews/acceptance.md",
    "problems/2025-B4/reviews/power-gap-return-acceptance.md",
    "problems/2025-B4/reviews/diagonal-firstcase-acceptance.md",
    "problems/2025-B4/reviews/diagonal-moment-acceptance.md",
]
context = [
    "AGENTS.md",
    "problems/2025-B4/statement.md",
    "problems/2025-B4/proof.md",
    "problems/2025-B4/notes/reviewed-literature-supplement-v1.md",
    "problems/2025-B4/reviews/strongfc-acceptance.md",
    "problems/2025-B4/notes/coordinator-diagonal-appendix-inspection-v1.md",
    "problems/2025-B4/notes/coordinator-diagonal-moment-separation-v1.3.md",
    "problems/2025-B4/notes/coordinator-diagonal-moment-sources-v1.json",
]

ledger = read_json(PREFIX + "issues-v1.json")
assert len(ledger["checks"]) == 50
covered = {o for row in ledger["checks"] for o in row["obligations"]}
assert covered == {"FS%02d" % n for n in range(1, 41)}
assert ledger["substantive_objections"] == []
assert ledger["required_author_repairs"] == []

validation = {
    "checked_at_utc": now, "metadata_only": True,
    "constructor_freeze": fp(CONSTRUCTOR_FREEZE),
    "constructor_eight_artifact_submission": artifacts,
    "candidate": candidate,
    "constructor_declared_source_checks": source_checks,
    "constructor_declared_input_checks": constructor_input_checks,
    "complete_accepted_bodies_read": [fp(p) for p in accepted_bodies],
    "complete_acceptance_MD_records_read": [fp(p) for p in acceptance_mds],
    "actual_context_read_scopes_differentiated_in_source_MD": [fp(p) for p in context],
    "later_primary_cache": fp(".cache/literature/deep-literature-r1/2025-bartolome-mihailescu-binary-thue-v2.pdf"),
    "fresh_original_and_later_primary_definitions_hypotheses_weight_and_application_passages_read": True,
    "full_external_Diophantine_proof_reconstructed_or_endorsed": False,
    "old_finite_certificates_or_author_mathematical_code_rerun": False,
    "older_own_packets": older,
    "all_forty_three_older_own_packets_unchanged": True,
    "GK_separate_telemetry_addendum_preserved": gk_addendum,
    "complete_initially_blind_whole_reconstruction": True,
    "new_peer_FS_findings_read": False,
    "later_root_FS_inspection_read": False,
    "NEW_original_weight_packet_or_findings_read": False,
    "old_PG_CF1_review_and_unrelated_2021_author_roles_disclosed": True,
    "new_FS_constructor_strategy_or_repair_contributor": False,
    "higher_weight_equated_with_original_required_weight": False,
    "mathematical_program_CAS_enumeration_scan_or_author_rerun": False,
    "only_current_assigned_prefix_written": True,
    "candidate_shared_old_files_or_git_mutation": False,
}
save("input-validation-v1.json", validation)

source_occurrences = len(source_checks)
input_occurrences = len(constructor_input_checks)
all_constructor_paths = {r["path"] for r in source_checks + constructor_input_checks}
usage = {"at_utc": "2026-10-17 12:48:32 UTC (paired clock/telemetry check)",
         "total_used_percent": 39, "window_minutes": 10080,
         "reset_unix": 1792745187, "total_ceiling_percent": 90,
         "integration_reserve": True}
output = {
    "checked_at_utc": now,
    "metadata_only_no_mathematical_program": True,
    "candidate": candidate,
    "constructor_freeze": fp(CONSTRUCTOR_FREEZE),
    "constructor_artifacts": len(artifacts),
    "constructor_declared_source_fingerprint_occurrences": source_occurrences,
    "constructor_declared_input_fingerprint_occurrences": input_occurrences,
    "constructor_source_and_input_unique_paths": len(all_constructor_paths),
    "per_inference_ledger_rows": 50,
    "constructor_obligations_covered": len(covered),
    "older_own_packets_unchanged": len(older),
    "all_hash_checks_passed": True,
    "substantive_objections": 0,
    "required_author_repairs": 0,
    "peer_FS_or_NEW_OW_findings_read_before_freeze": False,
    "latest_authoritative_weekly_usage": usage,
    "command": "python3 problems/2025-B4/reviews/reasoning-return-r4-review-2-freeze-v1.py",
}
save("freeze-output-v1.json", output)

names = ["initial-v1.md", "issues-v1.json", "source-checks-v1.md",
         "freeze-v1.py", "input-validation-v1.json", "freeze-output-v1.json"]
manifest = {
    "frozen_at_utc": now,
    "status": "complete initially blind independent nonconstructor WHOLE initial FS1-FS3 audit",
    "reviewer": "/root/review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_sha256": EXPECTED,
    "constructor_freeze_sha256": fp(CONSTRUCTOR_FREEZE)["sha256"],
    "whole_claims": ["FS1", "FS2", "FS3"],
    "per_inference_ledger_rows": 50,
    "constructor_obligations_covered": 40,
    "substantive_objections": 0, "required_author_repairs": 0,
    "old_PG_CF1_review_and_unrelated_2021_authorship_roles_disclosed": True,
    "new_FS_constructor_strategy_or_repair_contributor": False,
    "peer_FS_findings_read_before_freeze": False,
    "later_root_FS_inspection_read_before_freeze": False,
    "NEW_original_weight_packet_or_findings_read_before_freeze": False,
    "findings_sent_before_complete_initial_freeze": False,
    "higher_weight_original_weight_reciprocal_Fourier_or_higher_jet_transfer": False,
    "new_Diophantine_exclusion_full_source_repair_full_annual_or_novelty_claim": False,
    "mathematical_code_CAS_scan_enumeration_author_rerun": False,
    "candidate_shared_old_files_or_git_mutation": False,
    "spawning_contact_charge_or_access_bypass": False,
    "coordinator_promotion_performed": False,
    "latest_authoritative_weekly_usage": usage,
    "command": output["command"],
    "records": [fp(PREFIX + name) for name in names],
}
save("manifest-v1.json", manifest)
print(json.dumps(dict(output, manifest=fp(PREFIX + "manifest-v1.json")), indent=2))
