"""Administrative LO review freeze: hashes and JSON only, no math code.

Never executes constructor code or opens the current LO peer R2 prefix.
All writes exclusively create new files in the assigned R1 prefix.
"""
from pathlib import Path
import datetime as dt
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2019-B4/reviews/linear-output-return-r1-review-1-"
AUTHOR = "problems/2019-B4/notes/linear-output-return-r1-"
PEER = "problems/2019-B4/reviews/linear-output-return-r1-review-2-"
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


def byte_records(value):
    if isinstance(value, dict):
        if (isinstance(value.get("path"), str)
                and isinstance(value.get("bytes"), int)
                and isinstance(value.get("sha256"), str)
                and len(value["sha256"]) == 64):
            yield value
        for nested in value.values():
            yield from byte_records(nested)
    elif isinstance(value, list):
        for nested in value:
            yield from byte_records(nested)


def new_json(suffix, value):
    relative = PREFIX + suffix
    assert relative.startswith(PREFIX) and not safe_path(relative).exists(), relative
    with safe_path(relative).open("x") as out:
        json.dump(value, out, indent=2, ensure_ascii=False)
        out.write("\n")
    return fp(relative)


constructor_freeze = checked({
    "path": AUTHOR + "freeze-v1.json", "bytes": 3511,
    "sha256": "b1728d67d1101e3c9207fc935919c0cc4bf7c148f3af3220344729e5554b2deb"})
constructor = read_json(constructor_freeze["path"])
assert len(constructor["artifacts"]) == 8
submission = [checked(record) for record in constructor["artifacts"]]
candidate = checked({
    "path": AUTHOR + "candidate-v1.md", "bytes": 17270,
    "sha256": "b1bec632971326a661a4188135ce23d40f0fdcc6a121197aefe10d2237f6e1fa"})
author_input = read_json(AUTHOR + "input-validation-v1.json")
author_sources = read_json(AUTHOR + "sources-v1.json")
declared_checks = [checked(record) for record in byte_records(author_input)]
source_checks = [checked(record) for record in byte_records(author_sources)]
assert len(author_input["earlier_unique_records_preserved"]) == 229
accepted_existence = checked(author_input["accepted_existence_and_strict_bound_full_body_read"])
assert accepted_existence["path"] == "problems/2019-B4/proof.md"
assert len(author_sources["input_fingerprints"]) == 8
acceptance_MD = fp("problems/2019-B4/reviews/acceptance.md")

prior_manifest = checked({
    "path": "problems/2024-B4/reviews/Kasami-whole-criterion-review-1-manifest-v1.json",
    "bytes": 3491,
    "sha256": "6b4c430f9b1ad0c91b1da3651b67d9b26ea8dca8712c89e7f47ea2d3bf373cda"})
prior = read_json(prior_manifest["path"])
prior_checks = [checked(record) for record in prior["records"]]
assert len(prior_checks) == 6
old_input = read_json(
    "problems/2024-B4/reviews/Kasami-whole-criterion-review-1-input-validation-v1.json")
assert len(old_input["older_own_packets"]) == 40
preserved = []
for packet in old_input["older_own_packets"]:
    preserved.append({
        "manifest": checked(packet["manifest"]),
        "checks": [checked(record) for record in packet["checks"]]})
preserved.append({"manifest": prior_manifest, "checks": prior_checks})
assert len(preserved) == 41
GK_addendum = checked(old_input["GK_separate_telemetry_addendum_preserved"])

ledger = read_json(PREFIX + "issues-v1.json")
rows = ledger["checks"]
assert len(rows) == 44 and len({row["id"] for row in rows}) == 44
assert all(row["status"] == "pass" for row in rows)
obligations = set(re.findall(
    r"^\|\s*(LO[0-9]{2})\s*\|",
    safe_path(AUTHOR + "obligations-v1.md").read_text(), re.M))
assert len(obligations) == 28
assert {item for row in rows for item in row["obligations"]} == obligations
assert ledger["issues"] == ledger["required_author_repairs"] == []

validation = {
    "checked_at_utc": NOW,
    "metadata_only": True,
    "constructor_freeze": constructor_freeze,
    "constructor_eight_artifact_submission": submission,
    "candidate": candidate,
    "constructor_declared_input_checks": declared_checks,
    "constructor_declared_source_checks": source_checks,
    "constructor_input_fingerprint_occurrences": len(declared_checks),
    "constructor_source_fingerprint_occurrences": len(source_checks),
    "constructor_input_and_source_unique_paths": len({
        item["path"] for item in declared_checks + source_checks}),
    "complete_accepted_existence_and_strict_bound_body": accepted_existence,
    "complete_acceptance_MD": acceptance_MD,
    "actual_context_read_scopes_differentiated_in_source_MD": True,
    "full_2007_primary_text_and_all_used_hypotheses_freshly_read": True,
    "full_external_proof_independently_reconstructed_claim": False,
    "full_2005_text_or_unread_theorem_imported": False,
    "old_finite_certificates_rerun_or_newly_independently_recertified": False,
    "older_own_packets": preserved,
    "all_forty_one_older_own_packets_unchanged": True,
    "GK_separate_telemetry_addendum_preserved": GK_addendum,
    "complete_initially_blind_whole_reconstruction": True,
    "new_peer_LO_findings_read": False,
    "later_root_LO_inspection_read": False,
    "old_NR_authorship_moment_review_and_CCL_R2_roles_disclosed": True,
    "old_NR_or_CCL_conclusions_used_as_LO_premises": False,
    "new_LO_constructor_strategy_or_repair_contributor": False,
    "mathematical_program_CAS_enumeration_scan_or_author_rerun": False,
    "only_current_assigned_prefix_written": True,
    "candidate_shared_old_files_or_git_mutation": False
}
validation_fp = new_json("input-validation-v1.json", validation)
telemetry = {
    "total_used_percent": 36,
    "at_utc": "2026-10-17 12:12:14 UTC",
    "source": "authoritative account-wide get_usage_limits tool",
    "window_minutes": 10080,
    "reset_unix": 1792745187,
    "total_ceiling_percent": 90,
    "integration_reserve": True
}
output = {
    "frozen_at_utc": NOW,
    "metadata_only": True,
    "whole_LO1_LO6_and_conditional_reconstructed": True,
    "per_inference_ledger_rows": len(rows),
    "constructor_obligations_covered": len(obligations),
    "constructor_submission_artifacts": len(submission),
    "constructor_input_fingerprint_occurrences": len(declared_checks),
    "constructor_source_fingerprint_occurrences": len(source_checks),
    "constructor_input_and_source_unique_paths": len({
        item["path"] for item in declared_checks + source_checks}),
    "full_existence_body_and_acceptance_MD_checked": True,
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
    "status": "fresh initially blind nonconstructor WHOLE LO review R1; no substantive defect found in scoped LO1-LO6 and conditional rational-series claims",
    "reviewer": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_sha256": candidate["sha256"],
    "constructor_freeze_sha256": constructor_freeze["sha256"],
    "whole_claims": [
        "LO1 exact original-output parity linear grammar",
        "LO2 original-output nonregularity and proper nonterminal occurrence condition",
        "LO3 exact derivation totals and exponential alternating/mean ambiguity",
        "LO4 complete distinct-word intersections and recurrences including J0",
        "LO5 recoverable injections, single-word overlap entropy, generating identities and failed closure",
        "LO6 uniform internal forcing block and weighted avoidance comparison below2 only",
        "finite proper unambiguous linear presentation conditionally gives a rational distinct-word series"],
    "per_inference_ledger_rows": len(rows),
    "constructor_obligations_covered": len(obligations),
    "substantive_objections": [],
    "required_author_repairs": [],
    "old_NR_authorship_moment_review_and_CCL_R2_roles_disclosed": True,
    "new_LO_constructor_strategy_or_repair_contributor": False,
    "peer_LO_findings_read_before_freeze": False,
    "later_root_LO_inspection_read_before_freeze": False,
    "findings_sent_before_complete_initial_freeze": False,
    "ordinary_growth_sensitivity_or_weighted_to_unweighted_entropy_transfer": False,
    "inherent_ambiguity_nonrationality_exact_lambda_new_bound_full_annual_or_novelty_claim": False,
    "mathematical_code_CAS_scan_enumeration_author_rerun": False,
    "candidate_shared_old_files_or_git_mutation": False,
    "spawning_contact_charge_or_access_bypass": False,
    "coordinator_promotion_performed": False,
    "latest_authoritative_weekly_usage": telemetry,
    "command": "python3 problems/2019-B4/reviews/linear-output-return-r1-review-1-freeze-v1.py",
    "records": records
}
manifest_fp = new_json("manifest-v1.json", manifest)
print(json.dumps({"manifest": manifest_fp, "output": output}, indent=2))
