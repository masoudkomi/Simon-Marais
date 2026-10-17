"""Administrative known-file SHA/JSON freezing only; no mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2022-B4/notes/reasoning-return-r6-"


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
source_path = PREFIX + "sources-v1.json"
source = read_json(source_path)
source_fps = [checked(rec) for rec in all_fps(source)]
assert len(source_fps) == 8
f5_authority_path = "problems/2022-B4/reviews/reasoning-return-r5-acceptance.json"
f5_authority_rows = [checked(rec) for rec in all_fps(read_json(f5_authority_path))]
f5_body_path = "problems/2022-B4/proofs/reviewed-reasoning-return-r5-v1.1.md"
f5_raw_path = "problems/2022-B4/notes/reasoning-return-r5-candidate-v1.md"
assert (ROOT / f5_body_path).read_bytes().endswith((ROOT / f5_raw_path).read_bytes())
context_paths = [
    "AGENTS.md", "problems/2022-B4/statement.md", "problems/2022-B4/references.md",
    "problems/2022-B4/reviews/reasoning-return-r5-acceptance.md",
    "problems/2022-B4/notes/reasoning-return-r5-source-audit-v1.md",
    "problems/2022-B4/notes/reasoning-return-r5-failed-routes-v1.md",
    "problems/2022-B4/notes/reasoning-return-r4-failed-routes-v1.md",
    "problems/2022-B4/notes/deep-literature-coordinator-v1.md",
]
context_rows = [fp(path) for path in context_paths]
previous_input_path = "problems/2020-B4/reviews/reasoning-return-r5-review-2-input-validation-v1.json"
previous_manifest_path = "problems/2020-B4/reviews/reasoning-return-r5-review-2-manifest-v1.json"
assert fp(previous_manifest_path)["bytes"] == 3238
assert fp(previous_manifest_path)["sha256"] == "db799db3b9f84db7b722107135b5547631bbde3db0411a207489986abcf0c05c"
previous_input = read_json(previous_input_path)
older = []
for item in previous_input["older_own_packets"]:
    older.append({"manifest": checked(item["manifest"]),
                  "checks": [checked(rec) for rec in item["checks"]]})
older.append({"manifest": fp(previous_manifest_path),
              "checks": [checked(rec) for rec in read_json(previous_manifest_path)["records"]]})
assert len(older) == 54
gk_addendum = checked(previous_input["GK_separate_telemetry_addendum_preserved"])
obligation_text = (ROOT / (PREFIX + "obligations-v1.md")).read_text()
labels = set(re.findall(r"R6-O[0-9]{2}", obligation_text))
assert labels == {"R6-O" + str(i).zfill(2) for i in range(1, 41)}
usage = {
    "at_utc": "2026-10-17 14:51:25 UTC (direct telemetry followed by UTC clock)",
    "total_used_percent": 46, "window_minutes": 10080,
    "reset_unix": 1792745187, "total_ceiling_percent": 90,
    "integration_reserve": True, "ordinary_usage_allowed": True,
}
validation = {
    "checked_at_utc": now,
    "metadata_only_not_mathematical_evidence": True,
    "exact_current_source_declared_fingerprints_checked": source_fps,
    "exact_accepted_F5_authority": fp(f5_authority_path),
    "accepted_F5_authority_declared_fingerprints_checked": f5_authority_rows,
    "complete_accepted_F5_body_and_acceptance_scopes_read": True,
    "accepted_F5_body_exact_raw_suffix_unchanged": True,
    "context_records_actual_read_limits_in_source_audit": context_rows,
    "older_own_packets": older,
    "all_fifty_four_older_own_packets_unchanged": True,
    "GK_separate_telemetry_addendum_preserved": gk_addendum,
    "assigned_R6_prefix_confirmed_unused_before_first_write": True,
    "all_forty_whole_obligation_labels_present": True,
    "new_R6A_R6B_R6C_full_proofs_and_actual_contest_scope_written": True,
    "arbitrary_finite_prime_set_with_explicit3_and7_cancellation": True,
    "every_cycle_phase_avoids_finite_rational_zero_pole_set": True,
    "fixed_cycle_before_arbitrary_finite_repetition_count": True,
    "both2_and5_precision_losses_prove_ordinary_integrality": True,
    "added_prime_function_and_residue_features_repeat_at_every_phase": True,
    "ordinary_start_changes_with_depth_no_infinite_lift_inferred": True,
    "bounded_error_arbitrary_feature_score_and_positive_log_height_exact_scope": True,
    "all_selected_primes_not_ALL_primes_for_one_fixed_cycle": True,
    "root_generic_assignment_only_no_new_proof_inference_contribution": True,
    "old_R3_R4_F5_whole_review_roles_disclosed": True,
    "candidate_status_unverified_and_two_OTHER_whole_audits_required": True,
    "new_external_theorem_import_or_unseen_full_paper_proof_claim": False,
    "actual_primary_read_scopes_and_web_timeout_disclosed": True,
    "native_source_wait_or_unreaped_process": False,
    "new_source_download_PDF_cache_edit_or_render": False,
    "positive_ordinary_infinite_lift_termination_or_annual_solution_claim": False,
    "priority_novelty_or_new_numerical_bound_claim": False,
    "queued2024_HR_target_or_new_peer_findings_read_before_complete_constructor_freeze": False,
    "only_current_assigned_prefix_written": True,
    "old_candidate_review_shared_cache_or_Git_mutation": False,
    "mathematical_program_CAS_scan_enumeration_certificate_replay_or_author_rerun": False,
    "spawning_charge_contact_or_access_bypass": False,
}
save("input-validation-v1.json", validation)
output = {
    "frozen_at_utc": now,
    "metadata_only_not_mathematical_evidence": True,
    "candidate": fp(PREFIX + "candidate-v1.md"),
    "source_declared_fingerprints_checked": len(source_fps),
    "accepted_F5_authority_fingerprint_occurrences_checked": len(f5_authority_rows),
    "context_files_bound_actual_read_limits_preserved": len(context_rows),
    "all_forty_obligation_labels_present": True,
    "older_own_packets_unchanged": len(older),
    "all_hash_checks_passed": True,
    "positive_ordinary_infinite_lift_termination_or_full_annual_claim": False,
    "candidate_requires_two_OTHER_fresh_whole_audits": True,
    "latest_authoritative_weekly_usage": usage,
    "command": "python3 problems/2022-B4/notes/reasoning-return-r6-freeze-v1.py",
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
    "whole_independent_audit_obligations": 40,
    "requires_two_OTHER_fresh_initially_blind_nonconstructor_whole_audits": True,
    "root_generic_assignment_only_no_new_cycle_feature_or_no_go_proof_contribution": True,
    "old_R3_R4_F5_whole_review_roles_disclosed": True,
    "standard_CRT_and_p_adic_techniques_claimed_novel": False,
    "arbitrary_finite_prime_and_rational_function_feature_obstruction_full_scope": True,
    "varying_start_not_one_positive_ordinary_infinite_lift": True,
    "termination_all_controller_or_full_annual_solution_claim": False,
    "new_numerical_or_novelty_claim": False,
    "mathematical_program_CAS_scan_enumeration_certificate_or_author_rerun": False,
    "old_shared_Git_cache_mutation_spawning_charge_contact_or_bypass": False,
    "queued2024_HR_target_or_new_peer_findings_read_before_complete_constructor_freeze": False,
    "older_own_packets_unchanged": 54,
    "latest_authoritative_weekly_usage": usage,
    "command": output["command"],
    "artifacts": [fp(PREFIX + name) for name in names],
}
save("freeze-v1.json", manifest)
print(json.dumps(dict(output, manifest=fp(PREFIX + "freeze-v1.json")), indent=2))
