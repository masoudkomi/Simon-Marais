"""Administrative CCL review freeze: hashes and JSON only, no math code.

Never executes constructor code or opens the current CCL peer R1 prefix.
All writes exclusively create new files in the assigned R2 prefix.
"""
from pathlib import Path
import datetime as dt
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2019-B4/reviews/chronological-context-language-review-2-"
AUTHOR = "problems/2019-B4/notes/coordinator-chronological-context-language-"
PEER = "problems/2019-B4/reviews/chronological-context-language-review-1-"
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


constructor_manifest = fp(AUTHOR + "manifest-v1.json")
assert constructor_manifest["sha256"] == "38fb9ca9e5db47d97c18cbfc6fd5f52283b8896e0f8637dd802da4c532d56e8c"
constructor = read_json(constructor_manifest["path"])
assert len(constructor["records"]) == 3
submission = [checked(record) for record in constructor["records"]]
candidate = checked({
    "path": AUTHOR + "candidate-v1.md", "bytes": 6235,
    "sha256": "6d9446e4bb4fb81457eb8882b498c073353eaf93a546e8b56007a0adf0e613da"})
local_snapshots = [fp(relative) for relative in [
    "AGENTS.md", "problems/2019-B4/statement.md",
    "problems/2019-B4/references.md", "problems/2019-B4/proof.md",
    "problems/2019-B4/reviews/acceptance.md",
    "problems/2019-B4/reviews/nonregularity-return-acceptance.md",
    "problems/2019-B4/proofs/reviewed-nonregularity-return-v1.1.md",
    "problems/2019-B4/proofs/reviewed-secondpass-v1.1.md",
    "problems/2019-B4/notes/secondpass-canonical-renewal.md"]]
NR_raw = fp("problems/2019-B4/notes/reasoning-return-r3-candidate-v1.md")
assert safe_path(
    "problems/2019-B4/proofs/reviewed-nonregularity-return-v1.1.md").read_bytes().endswith(
        safe_path(NR_raw["path"]).read_bytes())

prior_manifest = checked({
    "path": "problems/2021-B4/reviews/reasoning-return-r5-review-1-manifest-v1.json",
    "bytes": 3651,
    "sha256": "86b14ce5a9a1a635c5275155885b60ba01bcc3348cd2adc7a3dc719f1e1536d3"})
prior = read_json(prior_manifest["path"])
prior_checks = [checked(record) for record in prior["records"]]
assert len(prior_checks) == 6
old_input = read_json(
    "problems/2021-B4/reviews/reasoning-return-r5-review-1-input-validation-v1.json")
assert len(old_input["older_own_packets"]) == 38
preserved = []
for packet in old_input["older_own_packets"]:
    preserved.append({
        "manifest": checked(packet["manifest"]),
        "checks": [checked(record) for record in packet["checks"]]})
preserved.append({"manifest": prior_manifest, "checks": prior_checks})
assert len(preserved) == 39
GK_addendum = checked(old_input["GK_separate_telemetry_addendum_preserved"])

ledger = read_json(PREFIX + "issues-v1.json")
rows = ledger["checks"]
assert len(rows) == 27 and len({row["id"] for row in rows}) == 27
assert all(row["status"] == "pass" for row in rows)
obligations = {item["id"] for item in
               read_json(AUTHOR + "obligations-v1.json")["obligations"]}
assert len(obligations) == 15
assert {item for row in rows for item in row["obligations"]} == obligations
assert ledger["issues"] == ledger["required_author_repairs"] == []

validation = {
    "checked_at_utc": NOW,
    "metadata_only": True,
    "constructor_manifest": constructor_manifest,
    "constructor_three_artifact_submission": submission,
    "candidate": candidate,
    "local_input_snapshots_actual_read_scope_in_source_MD": local_snapshots,
    "old_authored_NR_raw": NR_raw,
    "accepted_NR_contains_exact_complete_raw_suffix": True,
    "older_own_packets": preserved,
    "all_thirty_nine_older_own_packets_unchanged": True,
    "GK_separate_telemetry_addendum_preserved": GK_addendum,
    "complete_initially_blind_whole_reconstruction": True,
    "new_peer_CCL_findings_read": False,
    "later_root_CCL_inspection_read": False,
    "old_NR_authorship_and_moment_review_role_disclosed": True,
    "independent_reaudit_of_own_accepted_NR_theorem_claimed": False,
    "old_NR_conclusion_used_as_premise_for_new_CCL": False,
    "new_CCL_constructor_strategy_or_repair_contributor": False,
    "mathematical_program_CAS_enumeration_scan_or_author_rerun": False,
    "only_current_assigned_prefix_written": True,
    "candidate_shared_old_files_or_git_mutation": False
}
validation_fp = new_json("input-validation-v1.json", validation)
telemetry = {
    "total_used_percent": 35,
    "at_utc": "2026-10-17 11:56:48 UTC",
    "source": "authoritative account-wide get_usage_limits tool",
    "window_minutes": 10080,
    "reset_unix": 1792745187,
    "total_ceiling_percent": 90,
    "integration_reserve": True
}
output = {
    "frozen_at_utc": NOW,
    "metadata_only": True,
    "whole_CCL_reconstructed": True,
    "per_inference_ledger_rows": len(rows),
    "constructor_obligations_covered": len(obligations),
    "constructor_submission_artifacts": len(submission),
    "local_input_snapshots": len(local_snapshots),
    "old_NR_accepted_exact_complete_raw_suffix_verified": True,
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
    "status": "fresh initially blind nonconstructor WHOLE CCL review R2; no substantive defect found in exact separator-serialization scope",
    "reviewer": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_sha256": candidate["sha256"],
    "constructor_manifest_sha256": constructor_manifest["sha256"],
    "whole_claims": [
        "all-finite alternating chronological pairs and physical reversal boundary",
        "exact positive-even four-run regular slice with every final-pair branch",
        "all-decomposition finite-word CFL pumping contradiction",
        "regular-intersection closure and exact separator-serialization conclusion"],
    "per_inference_ledger_rows": len(rows),
    "constructor_obligations_covered": len(obligations),
    "substantive_objections": [],
    "required_author_repairs": [],
    "prior_NR_authorship_and_moment_review_role_disclosed": True,
    "new_CCL_constructor_strategy_or_repair_contributor": False,
    "peer_CCL_findings_read_before_freeze": False,
    "later_root_CCL_inspection_read_before_freeze": False,
    "findings_sent_before_complete_initial_freeze": False,
    "canonical_histories_original_outputs_all_encodings_or_series_conclusion": False,
    "exact_lambda_full_annual_or_novelty_claim": False,
    "mathematical_code_CAS_scan_enumeration_author_rerun": False,
    "candidate_shared_old_files_or_git_mutation": False,
    "spawning_contact_charge_or_access_bypass": False,
    "coordinator_promotion_performed": False,
    "latest_authoritative_weekly_usage": telemetry,
    "command": "python3 problems/2019-B4/reviews/chronological-context-language-review-2-freeze-v1.py",
    "records": records
}
manifest_fp = new_json("manifest-v1.json", manifest)
print(json.dumps({"manifest": manifest_fp, "output": output}, indent=2))
