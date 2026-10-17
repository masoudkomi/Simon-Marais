"""Administrative byte-integrity freeze only; no mathematical computation.

Never executes author code or opens the current R4 peer-review prefix.
Writes only new files in this assigned review prefix with exclusive create.
"""
from pathlib import Path
import datetime as dt
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2022-B4/reviews/reasoning-return-r4-review-1-"
AUTHOR = "problems/2022-B4/notes/reasoning-return-r4-"
PEER = "problems/2022-B4/reviews/reasoning-return-r4-review-2-"
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
    "path": AUTHOR + "freeze-v1.json", "bytes": 3530,
    "sha256": "f579d150c8b52450e5c20630fd36621ba8d36c3a6168c23235d352068c413f66"})
constructor = read_json(constructor_freeze["path"])
assert len(constructor["artifacts"]) == 8
submission = [checked(record) for record in constructor["artifacts"]]
candidate = checked({
    "path": AUTHOR + "candidate-v1.md", "bytes": 23750,
    "sha256": "cf3df09a2b38097bcbbe5c80c332a9bf1787f07a2114bf67b6108651240e2b2a"})
author_input = read_json(AUTHOR + "input-validation-v1.json")
declared_checks = [checked(record) for record in byte_records(author_input)]
assert len(author_input["earlier_unique_records_preserved"]) == 187
accepted = [checked(record) for record in
            author_input["all_four_complete_accepted_bodies"]]
assert len(accepted) == 4
context = [checked(record) for record in
           author_input["complete_deep_literature_and_acceptance_context"]]
assert len(context) == 9
scopes = [record for record in context if record["path"] in {
    "problems/2022-B4/reviews/acceptance.md",
    "problems/2022-B4/reviews/arithmetic-complexity-acceptance.md",
    "problems/2022-B4/reviews/return-r3-acceptance.md"}]
assert len(scopes) == 3
cached_sources = [checked(record) for record in
                  author_input["all_three_cached_primary_raw_sources"]]
assert len(cached_sources) == 3

old_R3_raws = []
for relative, expected_sha in [
    ("problems/2022-B4/notes/reasoning-return-r3-candidate-v1.md",
     "eb3d176680116595015069507f3904a0d048e44d3c2cde06965647010b82764e"),
    ("problems/2022-B4/notes/reasoning-return-r3-supplement-candidate-v1.md",
     "a0512f751dc5c648043025948a841fa4ecffb280785641c5e85f9fae5c99bca3")]:
    record = fp(relative)
    assert record["sha256"] == expected_sha, record
    old_R3_raws.append(record)
accepted_R3_blob = safe_path(
    "problems/2022-B4/proofs/reviewed-return-r3-v1.1.md").read_bytes()
assert safe_path(old_R3_raws[0]["path"]).read_bytes() in accepted_R3_blob
assert accepted_R3_blob.endswith(safe_path(old_R3_raws[1]["path"]).read_bytes())

prior_manifest = checked({
    "path": "problems/2017-B4/reviews/allD-global-review-1-manifest-v1.json",
    "bytes": 3194,
    "sha256": "366ab778386dedf1484a5ef7b0ad1ac3db6eb5687e101137a0987dcbad567e20"})
prior = read_json(prior_manifest["path"])
prior_checks = [checked(record) for record in prior["records"]]
assert len(prior_checks) == 6
old_input = read_json(
    "problems/2017-B4/reviews/allD-global-review-1-input-validation-v1.json")
assert len(old_input["older_own_packets"]) == 36
preserved = []
for packet in old_input["older_own_packets"]:
    preserved.append({
        "manifest": checked(packet["manifest"]),
        "checks": [checked(record) for record in packet["checks"]]})
preserved.append({"manifest": prior_manifest, "checks": prior_checks})
assert len(preserved) == 37
GK_addendum = checked(old_input["GK_separate_telemetry_addendum_preserved"])

ledger = read_json(PREFIX + "issues-v1.json")
rows = ledger["checks"]
assert len(rows) == 40 and len({row["id"] for row in rows}) == 40
assert all(row["status"] == "pass" for row in rows)
obligations = set(re.findall(
    r"^\|(R4-O[0-9]{2})\|", safe_path(AUTHOR + "obligations-v1.md").read_text(), re.M))
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
    "constructor_declared_fingerprint_occurrences": len(declared_checks),
    "constructor_declared_unique_paths": len({item["path"] for item in declared_checks}),
    "all_four_complete_accepted_bodies": accepted,
    "all_nine_pre_review_context_records": context,
    "all_three_complete_acceptance_scope_MDs": scopes,
    "all_three_primary_cache_bytes_checked_not_whole_read_claim": cached_sources,
    "accepted_R3_contains_exact_original_base_and_complete_supplement_suffix": True,
    "R3_original_raw_fingerprints": old_R3_raws,
    "older_own_packets": preserved,
    "all_thirty_seven_older_own_packets_unchanged": True,
    "GK_separate_telemetry_addendum_preserved": GK_addendum,
    "complete_initially_blind_whole_reconstruction": True,
    "new_peer_R4_findings_read": False,
    "later_root_R4_inspection_read": False,
    "prior_R3_whole_R1_role_disclosed": True,
    "new_R4_constructor_or_strategy_contributor": False,
    "mathematical_program_CAS_enumeration_scan_or_author_rerun": False,
    "read_only_pypdf_named_pages_not_math_computation": True,
    "only_current_assigned_prefix_written": True,
    "candidate_shared_old_files_or_git_mutation": False
}
validation_fp = new_json("input-validation-v1.json", validation)
telemetry = {
    "total_used_percent": 34,
    "at_utc": "2026-10-17 11:30:04 UTC",
    "source": "authoritative account-wide get_usage_limits tool",
    "window_minutes": 10080,
    "reset_unix": 1792745187,
    "total_ceiling_percent": 90,
    "integration_reserve": True
}
output = {
    "frozen_at_utc": NOW,
    "metadata_only": True,
    "whole_E1_E2_V1_V4_reconstructed": True,
    "per_inference_ledger_rows": len(rows),
    "constructor_obligations_covered": len(obligations),
    "constructor_submission_artifacts": len(submission),
    "constructor_declared_fingerprint_occurrences": len(declared_checks),
    "constructor_declared_unique_paths": len({item["path"] for item in declared_checks}),
    "complete_accepted_bodies_checked": len(accepted),
    "complete_acceptance_scope_MDs_checked": len(scopes),
    "old_R3_accepted_exact_original_base_and_supplement_verified": True,
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
    "status": "fresh initially blind nonconstructor WHOLE R4 review R1; no substantive defect found in stated E1/E2/V1-V4 partial claims",
    "reviewer": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_sha256": candidate["sha256"],
    "constructor_freeze_sha256": constructor_freeze["sha256"],
    "whole_claims": [
        "E1 constant-translate admissible expansion lemma with one common radix normalization",
        "E2 positive ordinary AB lift forces at least nine full-alphabet expansions; no-ninefold remains a hypothesis",
        "V1 exact two-prime valuation balance and every-step accelerated ordinary return",
        "V2 signed fixedpoint and exact first/second-B power100 shadow criteria",
        "V3 two-prime isometry and arbitrary finite post-B shadow continuation",
        "V4 compatible finite positive preimages do not imply nonnegative ordinary surjectivity"],
    "per_inference_ledger_rows": len(rows),
    "constructor_obligations_covered": len(obligations),
    "substantive_objections": [],
    "required_author_repairs": [],
    "prior_R3_whole_R1_role_disclosed": True,
    "new_R4_constructor_or_strategy_contributor": False,
    "peer_R4_findings_read_before_freeze": False,
    "later_root_R4_inspection_read_before_freeze": False,
    "findings_sent_before_complete_initial_freeze": False,
    "full_digit10_ninth_path_retained": True,
    "no_ninefold_bridge_marked_unproved": True,
    "inverse_limit_not_ordinary_surjectivity_preserved": True,
    "unconditional_termination_infinite_positive_lift_full_solution_or_novelty_claim": False,
    "mathematical_code_CAS_scan_enumeration_author_rerun": False,
    "candidate_shared_old_files_or_git_mutation": False,
    "spawning_contact_charge_or_access_bypass": False,
    "coordinator_promotion_performed": False,
    "latest_authoritative_weekly_usage": telemetry,
    "command": "python3 " + PREFIX + "freeze-v1.py",
    "records": records
}
manifest_fp = new_json("manifest-v1.json", manifest)
print(json.dumps({"manifest": manifest_fp, "summary": output}, indent=2))
