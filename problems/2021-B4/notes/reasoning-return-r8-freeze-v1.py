"""Administrative SHA/JSON/label freezing only; no mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2021-B4/notes/reasoning-return-r8-"


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
source = read_json(PREFIX + "sources-v1.json")
source_rows = [checked(rec) for rec in all_fps(source)]
assert len(source_rows) == 3
authority = []
suffix_rows = []
for return_id in ["r5", "r6", "r7"]:
    path = "problems/2021-B4/reviews/reasoning-return-" + return_id + "-acceptance.json"
    record = read_json(path)
    rows = [checked(rec) for rec in all_fps(record)]
    authority.append({"authority": fp(path), "declared_fingerprints_checked": rows})
    accepted, raw = record["accepted_copy"]["path"], record["candidate"]["path"]
    assert (ROOT / accepted).read_bytes().endswith((ROOT / raw).read_bytes())
    suffix_rows.append({"accepted": fp(accepted), "raw": fp(raw), "exact_suffix": True})
context_paths = ["AGENTS.md", "problems/2021-B4/statement.md"]
context_paths += source["freshly_read_context_paths"]
context_paths += ["problems/2021-B4/reviews/reasoning-return-" + r + "-acceptance.md" for r in ["r5", "r6", "r7"]]

previous_manifest_path = "problems/2019-B4/reviews/monotone-ratio-review-2-manifest-v1.json"
previous_input_path = "problems/2019-B4/reviews/monotone-ratio-review-2-input-validation-v1.json"
assert fp(previous_manifest_path)["bytes"] == 3339
assert fp(previous_manifest_path)["sha256"] == "adbda3dc6667bdcc47980a76df7d0c895aa6c20154c18091d016b35457b95068"
previous_input = read_json(previous_input_path)
older = []
for item in previous_input["older_own_packets"]:
    older.append({"manifest": checked(item["manifest"]),
                  "checks": [checked(rec) for rec in item["checks"]]})
older.append({"manifest": fp(previous_manifest_path),
              "checks": [checked(rec) for rec in read_json(previous_manifest_path)["records"]]})
assert len(older) == 57
gk_addendum = checked(previous_input["GK_separate_telemetry_addendum_preserved"])
obligations = (ROOT / (PREFIX + "obligations-v1.md")).read_text()
assert set(re.findall(r"R8-O[0-9]{2}", obligations)) == {"R8-O" + str(i).zfill(2) for i in range(1, 41)}

usage = {"at_utc": "2026-10-17 15:35:23 UTC (direct telemetry and UTC clock)",
         "total_used_percent": 48, "window_minutes": 10080,
         "reset_unix": 1792745187, "total_ceiling_percent": 90,
         "integration_reserve": True, "ordinary_usage_allowed": True}
validation = {
    "checked_at_utc": now,
    "metadata_only_not_mathematical_evidence": True,
    "exact_accepted_source_fingerprints_checked": source_rows,
    "complete_accepted_authorities_and_declared_fingerprints_checked": authority,
    "accepted_bodies_exact_raw_suffixes_checked": suffix_rows,
    "context_records_actual_read_scopes_in_source_audit": [fp(path) for path in context_paths],
    "older_own_packets": older,
    "all_fifty_seven_older_own_packets_unchanged": True,
    "GK_separate_telemetry_addendum_preserved": gk_addendum,
    "assigned_R8_prefix_confirmed_unused_before_first_write": True,
    "preceding_MR_whole_review_complete_and_frozen_before_R8_construction": True,
    "complete_R8A_R8B_R8C_R8D_mathematical_proofs_supplied": True,
    "all_forty_whole_audit_obligation_labels_present": True,
    "full_actual_double_root_rational_witness_and_global_carrier_hypotheses_retained": True,
    "both_quadratic_strict_inequalities_and_all_nonunit_integrality_checked_by_hand": True,
    "complete_symbolic_nine_pair_cubic_identity_and_four_actual_node_rows_by_hand": True,
    "arbitrary_nu_sigma_and_zero_coefficients_and_separate_delta0_retained": True,
    "four_depth_and_cubic_alternatives_not_eliminated_or_claimed_lifts": True,
    "two_frame_invariance_and_exact_negative_reflection_supplied": True,
    "old_roles_and_no_new_root_proof_inference_contribution_disclosed": True,
    "candidate_unverified_and_two_OTHER_fresh_whole_audits_required": True,
    "actual_primary_read_limits_and_old_source_objections_preserved": True,
    "new_external_mathematical_theorem_import": False,
    "mathematical_program_CAS_scan_Hensel_table_certificate_replay_or_author_rerun": False,
    "queued2019_walk_Frechet_target_or_new_peer_findings_read_before_complete_constructor_freeze": False,
    "positive_rational_Q19_lift_branch_degree20_or_full_annual_or_novelty_claim": False,
    "new_native_retrieval_wait_download_cache_edit_or_render": False,
    "Git_shared_old_byte_edit_spawning_charge_contact_or_bypass": False,
    "only_current_assigned_R8_prefix_written": True,
    "latest_authoritative_weekly_usage": usage,
}
save("input-validation-v1.json", validation)
output = {
    "frozen_at_utc": now,
    "metadata_only_not_mathematical_evidence": True,
    "candidate": fp(PREFIX + "candidate-v1.md"),
    "accepted_source_fingerprints_checked": len(source_rows),
    "accepted_authority_declared_fingerprint_occurrences_checked": sum(len(a["declared_fingerprints_checked"]) for a in authority),
    "accepted_exact_raw_suffixes_checked": len(suffix_rows),
    "all_forty_obligation_labels_present": True,
    "older_own_packets_unchanged": len(older),
    "all_hash_checks_passed": True,
    "whole_actual_double_branch_degree20_annual_or_novelty_claim": False,
    "requires_two_OTHER_fresh_initially_blind_whole_audits": True,
    "latest_authoritative_weekly_usage": usage,
    "command": "python3 problems/2021-B4/notes/reasoning-return-r8-freeze-v1.py",
}
save("freeze-output-v1.json", output)
names = ["candidate-v1.md", "obligations-v1.md", "failed-routes-v1.md",
         "source-audit-v1.md", "worklog-v1.md", "sources-v1.json",
         "freeze-v1.py", "input-validation-v1.json", "freeze-output-v1.json"]
manifest = {
    "frozen_at_utc": now,
    "status": "candidate proof - unverified",
    "constructor": "/root/review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "claims": source["claims"],
    "whole_obligations": 40,
    "requires_two_OTHER_fresh_initially_blind_nonconstructor_whole_audits": True,
    "root_generic_assignment_only_no_new_R8_proof_inference_contribution": True,
    "old_author_and_reviewer_roles_disclosed": True,
    "actual_double_branch_rational_witnesses_and_global_carrier_required": True,
    "neither_remaining_depth_cubic_nor_essential_center_alternative_excluded": True,
    "ordinary_rational_or_Q19_lift_degree20_annual_or_novelty_claim": False,
    "mathematical_program_CAS_scan_Hensel_table_certificate_or_author_rerun": False,
    "all_fifty_seven_older_own_packets_unchanged": True,
    "queued2019_walk_Frechet_target_or_new_peer_findings_read_before_complete_constructor_freeze": False,
    "Git_shared_old_byte_cache_edit_spawning_charge_contact_or_bypass": False,
    "latest_authoritative_weekly_usage": usage,
    "command": output["command"],
    "artifacts": [fp(PREFIX + name) for name in names],
}
save("freeze-v1.json", manifest)
print(json.dumps(dict(output, manifest=fp(PREFIX + "freeze-v1.json")), indent=2))
