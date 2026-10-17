"""Administrative KC review freeze: hashes and JSON only, no math code.

Never executes constructor code or opens the current KC peer R2 prefix.
All writes exclusively create new files in the assigned R1 prefix.
"""
from pathlib import Path
import datetime as dt
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2024-B4/reviews/Kasami-whole-criterion-review-1-"
AUTHOR = "problems/2024-B4/notes/coordinator-Kasami-whole-criterion-"
PEER = "problems/2024-B4/reviews/Kasami-whole-criterion-review-2-"
NOW = dt.datetime.now(dt.timezone.utc).isoformat()


def safe_path(relative):
    assert isinstance(relative, str) and not relative.startswith(PEER), relative
    result = (ROOT / relative).resolve()
    assert result.is_relative_to(ROOT), relative
    return result


def fp(relative):
    blob = safe_path(relative).read_bytes()
    return {"path": relative, "bytes": len(blob),
            "sha256": hashlib.sha256(blob).hexdigest()}


def checked(expected):
    actual = fp(expected["path"])
    assert actual["bytes"] == expected["bytes"], actual
    assert actual["sha256"] == expected["sha256"], actual
    return dict(actual, matches=True)


def read_json(relative):
    return json.loads(safe_path(relative).read_text())


def new_json(suffix, value):
    relative = PREFIX + suffix
    assert relative.startswith(PREFIX) and not safe_path(relative).exists(), relative
    with safe_path(relative).open("x") as out:
        json.dump(value, out, indent=2, ensure_ascii=False)
        out.write("\n")
    return fp(relative)


constructor_manifest = checked({
    "path": AUTHOR + "manifest-v1.json", "bytes": 1202,
    "sha256": "f08044ef0a1a9d8fa38e26f50e2b261d46ef761e68604060f918c5119816a3f3"})
constructor = read_json(constructor_manifest["path"])
assert len(constructor["records"]) == 4
submission = [checked(record) for record in constructor["records"]]
candidate = checked({
    "path": AUTHOR + "candidate-v1.md", "bytes": 7192,
    "sha256": "390d795343eb32a9496aa9a64c054b4809bd400c37c8195264053d343ba180bf"})
declared_sources = [checked(record) for record in
                    read_json(AUTHOR + "sources-v1.json")["fingerprints"]]
assert len(declared_sources) == 8
local_snapshots = [fp(relative) for relative in [
    "problems/2024-B4/reviews/composition-Kasami-acceptance.md",
    "problems/2024-B4/reviews/generalized-Kasami-acceptance.md",
    "problems/2024-B4/notes/zero-automaton-criterion-reviewed-v1.1.md",
    "problems/2024-B4/reviews/criterion-acceptance.md",
    "problems/2024-B4/reviews/necessary-valuation-acceptance.md"]]
raws = []
for raw_relative, accepted_relative, expected_sha in [
    ("problems/2024-B4/notes/reasoning-return-r3-candidate-v1.md",
     "problems/2024-B4/proofs/reviewed-composition-Kasami-v1.1.md",
     "cff70e9b104a48613712d0f2920157f29a5c20b56fb26055de829984e11fb021"),
    ("problems/2024-B4/notes/coordinator-generalized-Kasami-r1-candidate-v1.md",
     "problems/2024-B4/proofs/reviewed-generalized-Kasami-v1.1.md",
     "f99bae5f5d3877e556a30347a38616daf6b54fde300ae60543f849893a7dc4b8")]:
    raw = fp(raw_relative)
    assert raw["sha256"] == expected_sha, raw
    assert safe_path(accepted_relative).read_bytes().endswith(
        safe_path(raw_relative).read_bytes())
    raws.append(raw)

prior_manifest = checked({
    "path": "problems/2019-B4/reviews/chronological-context-language-review-2-manifest-v1.json",
    "bytes": 3402,
    "sha256": "858740ac58ca88adf90f1216c3714f8ccb1c1035e48cc771cba519377b34b805"})
prior = read_json(prior_manifest["path"])
prior_checks = [checked(record) for record in prior["records"]]
assert len(prior_checks) == 6
old_input = read_json(
    "problems/2019-B4/reviews/chronological-context-language-review-2-input-validation-v1.json")
assert len(old_input["older_own_packets"]) == 39
preserved = []
for packet in old_input["older_own_packets"]:
    preserved.append({
        "manifest": checked(packet["manifest"]),
        "checks": [checked(record) for record in packet["checks"]]})
preserved.append({"manifest": prior_manifest, "checks": prior_checks})
assert len(preserved) == 40
GK_addendum = checked(old_input["GK_separate_telemetry_addendum_preserved"])

ledger = read_json(PREFIX + "issues-v1.json")
rows = ledger["checks"]
assert len(rows) == 40 and len({row["id"] for row in rows}) == 40
assert all(row["status"] == "pass" for row in rows)
obligations = {item["id"] for item in
               read_json(AUTHOR + "obligations-v1.json")["obligations"]}
assert len(obligations) == 26
assert {item for row in rows for item in row["obligations"]} == obligations
assert ledger["issues"] == ledger["required_author_repairs"] == []

validation = {
    "checked_at_utc": NOW,
    "metadata_only": True,
    "constructor_manifest": constructor_manifest,
    "constructor_four_artifact_submission": submission,
    "candidate": candidate,
    "all_eight_declared_source_fingerprints": declared_sources,
    "additional_actual_read_scope_local_snapshots": local_snapshots,
    "CP_and_GK_original_raw_candidates": raws,
    "accepted_CP_and_GK_contain_exact_complete_original_suffixes": True,
    "full_accepted_CP_and_GK_mathematical_bodies_read": True,
    "old_phi13_certificate_rerun_or_newly_independently_recertified": False,
    "external_context_or_unverified_MCM_bridge_used_as_premise": False,
    "older_own_packets": preserved,
    "all_forty_older_own_packets_unchanged": True,
    "GK_separate_telemetry_addendum_preserved": GK_addendum,
    "complete_initially_blind_whole_reconstruction": True,
    "new_peer_KC_findings_read": False,
    "later_root_KC_inspection_read": False,
    "older_T1_T4_C7_C11_authorship_and_CP_R2_GK_R1_roles_disclosed": True,
    "new_KC_constructor_strategy_clarification_or_repair_contributor": False,
    "mathematical_program_CAS_enumeration_scan_or_author_rerun": False,
    "only_current_assigned_prefix_written": True,
    "candidate_shared_old_files_or_git_mutation": False
}
validation_fp = new_json("input-validation-v1.json", validation)
telemetry = {
    "total_used_percent": 36,
    "at_utc": "2026-10-17 12:05:31 UTC",
    "source": "authoritative account-wide get_usage_limits tool",
    "window_minutes": 10080,
    "reset_unix": 1792745187,
    "total_ceiling_percent": 90,
    "integration_reserve": True
}
output = {
    "frozen_at_utc": NOW,
    "metadata_only": True,
    "whole_KC_iff_reconstructed": True,
    "per_inference_ledger_rows": len(rows),
    "constructor_obligations_covered": len(obligations),
    "constructor_submission_artifacts": len(submission),
    "declared_source_fingerprints_checked": len(declared_sources),
    "additional_actual_read_scope_local_snapshots": len(local_snapshots),
    "full_CP_and_GK_bodies_and_exact_original_suffixes_checked": True,
    "older_own_packets_preserved": len(preserved),
    "separate_GK_telemetry_addendum_preserved": True,
    "substantive_objections": [],
    "required_author_repairs": [],
    "whole_initial_blind_freeze": True,
    "latest_authoritative_weekly_usage": telemetry
}
output_fp = new_json("freeze-output-v1.json", output)
records = [fp(PREFIX + suffix) for suffix in [
    "initial-v1.md", "issues-v1.json", "source-checks-v1.md", "freeze-v1.py"]]
records.extend([validation_fp, output_fp])
manifest = {
    "frozen_at_utc": NOW,
    "status": "fresh initially blind nonconstructor WHOLE KC review R1; no substantive defect found in exact all-k whole Kasami divisor iff",
    "reviewer": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_sha256": candidate["sha256"],
    "constructor_manifest_sha256": constructor_manifest["sha256"],
    "whole_claims": [
        "exact accepted F2 composition interface and equality only on F1",
        "explicit all-entry-nonzero constant matrix preserving F and C",
        "homogeneous difference and infinite-field polynomial extension",
        "adjacent binary mixed coefficients force weight2",
        "integer congruence gives precisely odd Frobenius-index progression",
        "all-index accepted GK converse, actual factors, integer lifts and all endpoints"],
    "per_inference_ledger_rows": len(rows),
    "constructor_obligations_covered": len(obligations),
    "substantive_objections": [],
    "required_author_repairs": [],
    "older_T1_T4_C7_C11_authorship_and_CP_R2_GK_R1_roles_disclosed": True,
    "new_KC_constructor_strategy_clarification_or_repair_contributor": False,
    "peer_KC_findings_read_before_freeze": False,
    "later_root_KC_inspection_read_before_freeze": False,
    "findings_sent_before_complete_initial_freeze": False,
    "external_MCM_group_absolute_factor_theorem_used": False,
    "all_reducibility_individual_components_full_annual_or_novelty_claim": False,
    "mathematical_code_CAS_scan_enumeration_author_rerun": False,
    "candidate_shared_old_files_or_git_mutation": False,
    "spawning_contact_charge_or_access_bypass": False,
    "coordinator_promotion_performed": False,
    "latest_authoritative_weekly_usage": telemetry,
    "command": "python3 problems/2024-B4/reviews/Kasami-whole-criterion-review-1-freeze-v1.py",
    "records": records
}
manifest_fp = new_json("manifest-v1.json", manifest)
print(json.dumps({"manifest": manifest_fp, "output": output}, indent=2))
