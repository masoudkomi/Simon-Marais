"""Administrative byte-integrity freeze only; no mathematical computation.

Reads the exact assigned candidate and declared local fingerprints. Refuses
the current peer-global-review prefix. Never runs author scripts, writes an
old file, reads Git, or modifies a candidate/shared path.
"""
from pathlib import Path
import datetime as dt
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/reviews/allD-global-review-1-"
AUTHOR = "problems/2017-B4/notes/allD-global-reasoning-r1-"
PEER = "problems/2017-B4/reviews/allD-global-review-2-"
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
    assert actual["sha256"] == expected["sha256"], actual
    assert actual["bytes"] == expected["bytes"], actual
    return dict(actual, matches=True)


def read_json(relative):
    return json.loads(safe_path(relative).read_text())


def byte_records(value):
    if isinstance(value, dict):
        if (isinstance(value.get("path"), str)
                and isinstance(value.get("sha256"), str)
                and len(value["sha256"]) == 64
                and isinstance(value.get("bytes"), int)):
            yield value
        for nested in value.values():
            yield from byte_records(nested)
    elif isinstance(value, list):
        for nested in value:
            yield from byte_records(nested)


def new_json(suffix, value):
    target = PREFIX + suffix
    assert target.startswith(PREFIX) and not safe_path(target).exists(), target
    with safe_path(target).open("x") as out:
        json.dump(value, out, indent=2, ensure_ascii=False)
        out.write("\n")
    return fp(target)


constructor_manifest = checked({
    "path": AUTHOR + "manifest-v1.json", "bytes": 3810,
    "sha256": "64a2790adf232a9e43d532762e594c87d3f2190aeb15901b07d1bf186e8e68a3"})
constructor = read_json(constructor_manifest["path"])
assert len(constructor["records"]) == 8
submission = [checked(record) for record in constructor["records"]]
candidate = checked({
    "path": AUTHOR + "candidate-v1.md", "bytes": 46506,
    "sha256": "c16acc6b4785c114648ec8848311d5022284c894047bef9013e7313c34706428"})
declared_input = read_json(AUTHOR + "input-validation-v1.json")
declared_sources = read_json(AUTHOR + "sources-v1.json")
declared_checks = [checked(record) for record in byte_records(
    {"input": declared_input, "sources": declared_sources})]
declared_unique = len({record["path"] for record in declared_checks})

accepted = [checked(record) for record in declared_sources["logical_accepted_inputs"]]
scope_records = [checked(record) for record in
                 declared_sources["acceptance_scope_fingerprints"]]
assert len(accepted) == len(scope_records) == 10
strict = declared_sources["strict_status_chronology"]
strict_raw = checked(strict["raw"])
strict_accepted = checked(strict["accepted"])
assert safe_path(strict_accepted["path"]).read_bytes().endswith(
    safe_path(strict_raw["path"]).read_bytes())
strict_original = checked(declared_sources["strict_original_manifest"])
strict_submission = [checked(record) for record in
                     declared_sources["strict_original_submission_records"]]
assert len(strict_submission) == 8
assert len(read_json(strict_original["path"])["records"]) == 8

old_manifest = checked({
    "path": "problems/2024-B4/reviews/generalized-Kasami-review-1-manifest-v1.json",
    "bytes": 2812,
    "sha256": "37d7cfa85c26c38b2c95c06d09111a45c8d9aeb243453485177c9a0cbc8e3a04"})
old = read_json(old_manifest["path"])
old_checks = [checked(record) for record in old["records"]]
assert len(old_checks) == 6
older_input = read_json(
    "problems/2024-B4/reviews/generalized-Kasami-review-1-input-validation-v1.json")
preserved = []
assert len(older_input["older_own_packets"]) == 35
for packet in older_input["older_own_packets"]:
    old_manifest_check = checked(packet["manifest"])
    old_record_checks = [checked(record) for record in packet["checks"]]
    preserved.append({"manifest": old_manifest_check, "checks": old_record_checks})
preserved.append({"manifest": old_manifest, "checks": old_checks})
assert len(preserved) == 36
telemetry_addendum = checked({
    "path": "problems/2024-B4/reviews/generalized-Kasami-review-1-telemetry-addendum-v1.json",
    "bytes": 938,
    "sha256": "1a4998c93bcc7183680053c105c8fed6181b30205eb0dbfa2ede61a1c2e88632"})

ledger = read_json(PREFIX + "issues-v1.json")
rows = ledger["per_inference_checks"]
obligations = read_json(AUTHOR + "obligations-v1.json")[
    "new_inferences_for_complete_adversarial_review"]
assert len(rows) == 46 and len(obligations) == 40
assert len({row["id"] for row in rows}) == 46
assert all(row["status"] == "pass" for row in rows)
assert {item for row in rows for item in row["obligations"]} == {
    item["id"] for item in obligations}
assert ledger["issues"] == ledger["required_author_repairs"] == []

input_validation = {
    "checked_at_utc": NOW,
    "metadata_only": True,
    "constructor_manifest": constructor_manifest,
    "constructor_eight_artifact_submission": submission,
    "candidate": candidate,
    "constructor_declared_input_checks": declared_checks,
    "constructor_declared_fingerprint_occurrences": len(declared_checks),
    "constructor_declared_unique_paths": declared_unique,
    "accepted_local_bodies_all_read_completely": accepted,
    "acceptance_scope_MDs_all_read_completely": scope_records,
    "strict_original_submission": strict_submission,
    "strict_original_manifest": strict_original,
    "strict_accepted_has_exact_complete_raw_suffix": True,
    "older_own_packets": preserved,
    "all_thirty_six_older_own_packets_unchanged": True,
    "GK_separate_telemetry_addendum_preserved": telemetry_addendum,
    "initially_blind_complete_global_reconstruction": True,
    "peer_global_report_or_findings_read": False,
    "prior_strict_LOCAL_authorship_and_G4_R1_disclosed": True,
    "new_global_constructor_or_contributor": False,
    "G4_UR3_CKP_dimension_outline_as_premise": False,
    "mathematical_code_CAS_enumeration_or_author_rerun": False,
    "only_current_assigned_prefix_written": True,
    "candidate_shared_old_files_or_git_mutation": False
}
input_fp = new_json("input-validation-v1.json", input_validation)
telemetry = {
    "used_percent": 33,
    "at_utc": "2026-10-17 11:17:26 UTC",
    "source": "authoritative account-wide get_usage_limits tool",
    "window_minutes": 10080,
    "reset_unix": 1792745187,
    "ceiling_total_used_percent": 90,
    "integration_reserve": True
}
output = {
    "frozen_at_utc": NOW,
    "metadata_only": True,
    "per_inference_ledger_rows": len(rows),
    "constructor_obligations_covered": len(obligations),
    "constructor_submission_artifacts": len(submission),
    "constructor_declared_fingerprint_occurrences": len(declared_checks),
    "constructor_declared_unique_paths": declared_unique,
    "exact_accepted_bodies_checked": len(accepted),
    "complete_acceptance_scope_MDs_checked": len(scope_records),
    "strict_accepted_exact_raw_suffix": True,
    "older_own_packets_preserved": len(preserved),
    "separate_GK_telemetry_addendum_preserved": True,
    "substantive_objections": [],
    "required_author_repairs": [],
    "whole_initial_blind_freeze": True,
    "latest_authoritative_weekly_usage": telemetry
}
output_fp = new_json("freeze-output-v1.json", output)
records = [fp(PREFIX + name) for name in [
    "initial-v1.md", "issues-v1.json", "source-checks-v1.md", "freeze-v1.py"]]
records.extend([input_fp, output_fp])
manifest = {
    "frozen_at_utc": NOW,
    "status": "initially blind independent WHOLE review; no substantive defect found in the complete stated all-D global induction and scalar-only consequence",
    "reviewer": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_sha256": candidate["sha256"],
    "constructor_manifest_sha256": constructor_manifest["sha256"],
    "whole_claims": [
        "UR_D on exact GE_(D,C)(r), every fixed D>=2 and every fixed C",
        "full balanced H_D at all integer sizes for each fixed D",
        "official scalar liminf equals limsup and ell_D converges to that value only"],
    "per_inference_ledger_rows": len(rows),
    "constructor_obligations_covered": len(obligations),
    "substantive_objections": [],
    "required_author_repairs": [],
    "prior_strict_LOCAL_S_D_authorship_and_G4_R1_role_disclosed": True,
    "new_global_constructor_or_contributor": False,
    "independent_reaudit_of_own_old_local_theorem_claimed": False,
    "peer_global_findings_read_before_freeze": False,
    "findings_sent_before_complete_initial_freeze": False,
    "G4_UR3_CKP_or_dimension_outline_as_premise": False,
    "mathematical_code_CAS_scan_enumeration_author_rerun": False,
    "common_numerical_value_full_annual_answer_PR_or_novelty_claim": False,
    "candidate_shared_old_files_or_git_mutation": False,
    "spawning_contact_charge_or_access_bypass": False,
    "latest_authoritative_weekly_usage": telemetry,
    "coordinator_promotion_performed": False,
    "command": "python3 " + PREFIX + "freeze-v1.py",
    "records": records
}
manifest_fp = new_json("manifest-v1.json", manifest)
print(json.dumps({"manifest": manifest_fp, "summary": output}, indent=2))
