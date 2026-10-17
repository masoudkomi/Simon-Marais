"""Administrative exact-file integrity/freezing only; no mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2024-B4/reviews/Hermitian-all-index-review-2-"
AUTHOR_MANIFEST = "problems/2024-B4/notes/coordinator-Hermitian-all-index-manifest-v1.json"


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
assert fp(AUTHOR_MANIFEST)["bytes"] == 3214
assert fp(AUTHOR_MANIFEST)["sha256"] == "d93f76bb4aecc912bb9dc91a51714d41330d250ba333ca7a32061d39a36df0a3"
author = read_json(AUTHOR_MANIFEST)
author_rows = [checked(rec) for rec in author["records"] + author["accepted_and_context_inputs"]]
assert len(author_rows) == 12
assert author_rows[0]["bytes"] == 15281
assert author_rows[0]["sha256"] == "296241f7538f7eb86315998ff760f4fa363d3a2d1c911988d6fa2b1a4f0287cc"
source_path = PREFIX + "sources-v1.json"
source = read_json(source_path)
source_rows = [checked(rec) for rec in all_fps(source)]
assert len(source_rows) == 4

authority_paths = [
    "problems/2024-B4/reviews/generalized-Kasami-acceptance.json",
    "problems/2024-B4/reviews/composition-Kasami-acceptance.json",
    "problems/2024-B4/reviews/even-inner-next-jet-acceptance.json",
]
authority = []
for path in authority_paths:
    authority.append({"authority": fp(path),
                      "declared_fingerprints_checked": [checked(rec) for rec in all_fps(read_json(path))]})
suffix_pairs = [
    ("problems/2024-B4/proofs/reviewed-generalized-Kasami-v1.1.md",
     "problems/2024-B4/notes/coordinator-generalized-Kasami-r1-candidate-v1.md"),
    ("problems/2024-B4/proofs/reviewed-composition-Kasami-v1.1.md",
     "problems/2024-B4/notes/reasoning-return-r3-candidate-v1.md"),
    ("problems/2024-B4/proofs/reviewed-even-inner-next-jet-v2.1.md",
     "problems/2024-B4/notes/coordinator-even-inner-next-jet-return-v2.md"),
]
suffix_rows = []
for accepted, raw in suffix_pairs:
    assert (ROOT / accepted).read_bytes().endswith((ROOT / raw).read_bytes())
    suffix_rows.append({"accepted": fp(accepted), "raw": fp(raw), "exact_suffix": True})
context_paths = [
    "AGENTS.md", "problems/2024-B4/statement.md",
    "problems/2024-B4/reviews/generalized-Kasami-acceptance.md",
    "problems/2024-B4/reviews/composition-Kasami-acceptance.md",
    "problems/2024-B4/reviews/even-inner-next-jet-acceptance.md",
]

previous_manifest_path = "problems/2022-B4/notes/reasoning-return-r6-freeze-v1.json"
previous_input_path = "problems/2022-B4/notes/reasoning-return-r6-input-validation-v1.json"
assert fp(previous_manifest_path)["bytes"] == 3784
assert fp(previous_manifest_path)["sha256"] == "44415c8ddcd197c8593e3738bc70ba52d07b408ee4302e0db7beb80408f39fee"
previous_input = read_json(previous_input_path)
older = []
for item in previous_input["older_own_packets"]:
    older.append({"manifest": checked(item["manifest"]),
                  "checks": [checked(rec) for rec in item["checks"]]})
older.append({"manifest": fp(previous_manifest_path),
              "checks": [checked(rec) for rec in read_json(previous_manifest_path)["artifacts"]]})
assert len(older) == 55
gk_addendum = checked(previous_input["GK_separate_telemetry_addendum_preserved"])
obligation_text = (ROOT / author["records"][1]["path"]).read_text()
assert set(re.findall(r"HR-O[0-9]{2}", obligation_text)) == {"HR-O" + str(i).zfill(2) for i in range(1, 25)}
ledger_text = (ROOT / (PREFIX + "issues-v1.md")).read_text()
assert set(re.findall(r"HR2-R[0-9]{2}", ledger_text)) == {"HR2-R" + str(i).zfill(2) for i in range(1, 49)}
assert set(re.findall(r"\bO[0-9]{2}\b", ledger_text)) == {"O" + str(i).zfill(2) for i in range(1, 25)}

usage = {"at_utc": "2026-10-17 15:03:00 UTC (direct telemetry and UTC clock)",
         "total_used_percent": 46, "window_minutes": 10080,
         "reset_unix": 1792745187, "total_ceiling_percent": 90,
         "integration_reserve": True, "ordinary_usage_allowed": True}
validation = {
    "checked_at_utc": now,
    "metadata_only_not_mathematical_evidence": True,
    "author_manifest": fp(AUTHOR_MANIFEST),
    "complete_author_and_context_direct_records_checked": author_rows,
    "own_source_declared_fingerprints_checked": source_rows,
    "exact_accepted_authorities_and_declared_fingerprints_checked": authority,
    "accepted_bodies_exact_submitted_suffixes_checked": suffix_rows,
    "full_relevant_acceptance_scopes_and_context_read": [fp(path) for path in context_paths],
    "older_own_packets": older,
    "all_fifty_five_older_own_packets_unchanged": True,
    "GK_separate_telemetry_addendum_preserved": gk_addendum,
    "preceding_R6_constructor_packet_complete_before_HR_target_opened": True,
    "assigned_review_prefix_confirmed_unused_before_first_write": True,
    "full_four_artifact_author_submission_and_all_twenty_four_obligations_read": True,
    "complete_accepted_GK_CP_NJ_bodies_and_acceptances_read": True,
    "old_unverified_odd_period_lead_read_as_history_not_premise": True,
    "all_forty_eight_inference_labels_and_twenty_four_obligation_labels_present": True,
    "whole_argument_independently_reconstructed_not_extension_only": True,
    "actual_Hasse_Weil_and_plane_genus_hypotheses_checked": True,
    "full_shifted_two_dimensional_return_and_separate_derivative_initial_checked": True,
    "exact_local_order_and_first_perturbation_bottom_inverse_and_persistence_checked": True,
    "complete_r2_and_both_homogeneous_divisor_directions_checked": True,
    "nonconstructor_prior_local_author_and_whole_review_roles_disclosed": True,
    "new_HR_peer_report_findings_or_root_later_inspection_read_before_complete_initial_freeze": False,
    "new_HR_proof_contribution_or_author_repair_by_reviewer": False,
    "no_substantive_defect_or_required_repair_found": True,
    "coordinator_acceptance_annual_or_novelty_claim": False,
    "new_mathematical_program_CAS_scan_or_author_rerun": False,
    "new_native_download_cache_write_source_timeout_or_running_job": False,
    "Git_shared_old_byte_mutation_spawning_charge_contact_or_bypass": False,
    "only_current_assigned_review_prefix_written": True,
    "latest_authoritative_weekly_usage": usage,
}
save("input-validation-v1.json", validation)
output = {
    "frozen_at_utc": now,
    "metadata_only_not_mathematical_evidence": True,
    "author_direct_fingerprints_checked": len(author_rows),
    "source_declared_fingerprints_checked": len(source_rows),
    "accepted_authority_declared_fingerprint_occurrences_checked": sum(len(item["declared_fingerprints_checked"]) for item in authority),
    "accepted_exact_suffix_checks": len(suffix_rows),
    "whole_inference_checks": 48,
    "all_author_obligations": 24,
    "older_own_packets_unchanged": len(older),
    "all_hash_checks_passed": True,
    "no_substantive_defect_or_required_repair_found": True,
    "whole_initial_blind_before_peer_findings": True,
    "recommendation_only_not_promotion": True,
    "latest_authoritative_weekly_usage": usage,
    "command": "python3 problems/2024-B4/reviews/Hermitian-all-index-review-2-freeze-v1.py",
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
    "target_main": dict(author_rows[0]),
    "claims_reviewed": ["HR1", "HR2"],
    "whole_inference_checks": 48,
    "all_author_obligations": 24,
    "new_HR_peer_findings_unread_before_complete_initial_freeze": True,
    "nonconstructor_whole_reconstruction": True,
    "older_T1_T4_C7_C11_authorship_and_CP_GK_CJ_DI_NJ_review_roles_disclosed": True,
    "root_constructor_excluded_from_independent_audit_count": True,
    "no_substantive_defect_or_required_repair_found": True,
    "recommendation_requires_coordinator_full_reconciliation": True,
    "ordinary_irreducibility_full_annual_or_novelty_claim": False,
    "all_fifty_five_older_own_packets_unchanged": True,
    "mathematical_program_CAS_scan_author_rerun": False,
    "Git_shared_old_byte_cache_mutation_spawning_charge_contact_or_bypass": False,
    "latest_authoritative_weekly_usage": usage,
    "command": output["command"],
    "records": [fp(PREFIX + name) for name in names],
}
save("manifest-v1.json", manifest)
print(json.dumps(dict(output, manifest=fp(PREFIX + "manifest-v1.json")), indent=2))
