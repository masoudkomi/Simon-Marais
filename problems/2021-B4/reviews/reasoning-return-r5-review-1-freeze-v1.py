"""Administrative byte-integrity freeze only; no mathematical computation.

Never executes author code or opens the current R5 peer-review prefix.
Writes only new files in the assigned review prefix with exclusive create.
"""
from pathlib import Path
import datetime as dt
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2021-B4/reviews/reasoning-return-r5-review-1-"
AUTHOR = "problems/2021-B4/notes/reasoning-return-r5-"
PEER = "problems/2021-B4/reviews/reasoning-return-r5-review-2-"
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
    "path": AUTHOR + "freeze-v1.json", "bytes": 3592,
    "sha256": "1626fa3981c78eb04f7fe41fc5a725b2500de0cf1647e7324941c6a5f3671533"})
constructor = read_json(constructor_freeze["path"])
assert len(constructor["artifacts"]) == 8
submission = [checked(record) for record in constructor["artifacts"]]
candidate = checked({
    "path": AUTHOR + "candidate-v1.md", "bytes": 20083,
    "sha256": "0d546265a3f9b1f83c05fce46e5a97acb6cad5d8841518d891ffed91717166f6"})
author_input = read_json(AUTHOR + "input-validation-v1.json")
author_sources = read_json(AUTHOR + "sources-v1.json")
declared_checks = [checked(record) for record in byte_records(author_input)]
source_checks = [checked(record) for record in byte_records(author_sources)]
assert len(author_input["earlier_unique_records_preserved"]) == 202
accepted = [checked(record) for record in
            author_input["complete_accepted_registers_and_bodies"]]
assert len(accepted) == 12
old_returns = [checked(record) for record in
               author_input["seven_accepted_return_texts_hash_checked"]]
assert len(old_returns) == 7

acceptance_MDs = [fp("problems/2021-B4/reviews/" + suffix) for suffix in [
    "witness-acceptance.md", "newton-acceptance.md",
    "three-witness-acceptance.md", "reasoning-J15-acceptance.md",
    "single-center-acceptance.md", "return-r3-acceptance.md",
    "odd-support-exclusion-acceptance.md"]]
PN_raw = fp("problems/2021-B4/notes/coordinator-odd-support-exclusion-candidate-v1.md")
assert PN_raw["sha256"] == "a7845441df7725edc5d30e28f7b8f28c529b0b710168ad4b068d279582c1857c"
PN_accepted = safe_path(
    "problems/2021-B4/proofs/reviewed-odd-support-exclusion-v1.1.md").read_bytes()
assert PN_accepted.endswith(safe_path(PN_raw["path"]).read_bytes())

prior_manifest = checked({
    "path": "problems/2022-B4/reviews/reasoning-return-r4-review-1-manifest-v1.json",
    "bytes": 3637,
    "sha256": "4c07c73aa65392f643a99a93742a335e2d1d3b2163129fe70e6d622610b44e10"})
prior = read_json(prior_manifest["path"])
prior_checks = [checked(record) for record in prior["records"]]
assert len(prior_checks) == 6
old_input = read_json(
    "problems/2022-B4/reviews/reasoning-return-r4-review-1-input-validation-v1.json")
assert len(old_input["older_own_packets"]) == 37
preserved = []
for packet in old_input["older_own_packets"]:
    preserved.append({
        "manifest": checked(packet["manifest"]),
        "checks": [checked(record) for record in packet["checks"]]})
preserved.append({"manifest": prior_manifest, "checks": prior_checks})
assert len(preserved) == 38
GK_addendum = checked(old_input["GK_separate_telemetry_addendum_preserved"])

ledger = read_json(PREFIX + "issues-v1.json")
rows = ledger["checks"]
assert len(rows) == 42 and len({row["id"] for row in rows}) == 42
assert all(row["status"] == "pass" for row in rows)
obligations = set(re.findall(
    r"^\|\s*(R5-[0-9]{2})\s*\|",
    safe_path(AUTHOR + "obligations-v1.md").read_text(), re.M))
assert len(obligations) == 30, obligations
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
    "all_twelve_complete_accepted_registers_and_bodies": accepted,
    "all_seven_complete_old_return_mathematical_texts": old_returns,
    "all_seven_complete_acceptance_scope_MDs": acceptance_MDs,
    "complete_reading_not_claimed_for_all_extra_context_or_older_certificates": True,
    "PN_raw": PN_raw,
    "accepted_PN_contains_exact_complete_raw_suffix": True,
    "older_own_packets": preserved,
    "all_thirty_eight_older_own_packets_unchanged": True,
    "GK_separate_telemetry_addendum_preserved": GK_addendum,
    "complete_initially_blind_whole_reconstruction": True,
    "new_peer_R5_findings_read": False,
    "later_root_R5_inspection_read": False,
    "old_seven_return_texts_authorship_and_prior_J15_PN_review_roles_disclosed": True,
    "independent_reaudit_of_own_accepted_old_theorems_claimed": False,
    "new_R5_constructor_strategy_or_clarification_contributor": False,
    "mathematical_program_CAS_enumeration_scan_or_author_rerun": False,
    "only_current_assigned_prefix_written": True,
    "candidate_shared_old_files_or_git_mutation": False
}
validation_fp = new_json("input-validation-v1.json", validation)
telemetry = {
    "total_used_percent": 35,
    "clock_read_at_current_stage_utc": "2026-10-17 11:49:53 UTC",
    "source": "authoritative account-wide get_usage_limits tool",
    "window_minutes": 10080,
    "reset_unix": 1792745187,
    "total_ceiling_percent": 90,
    "integration_reserve": True
}
output = {
    "frozen_at_utc": NOW,
    "metadata_only": True,
    "whole_R5A_R5E_reconstructed": True,
    "per_inference_ledger_rows": len(rows),
    "constructor_obligations_covered": len(obligations),
    "constructor_submission_artifacts": len(submission),
    "constructor_input_fingerprint_occurrences": len(declared_checks),
    "constructor_source_fingerprint_occurrences": len(source_checks),
    "constructor_input_and_source_unique_paths": len({
        item["path"] for item in declared_checks + source_checks}),
    "complete_accepted_registers_and_bodies_checked": len(accepted),
    "complete_old_return_mathematical_texts_checked": len(old_returns),
    "complete_acceptance_scope_MDs_checked": len(acceptance_MDs),
    "PN_accepted_exact_complete_raw_suffix_verified": True,
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
    "status": "fresh initially blind nonconstructor WHOLE R5 review R1; no substantive defect found in exact R5A-R5E partial scopes",
    "reviewer": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_sha256": candidate["sha256"],
    "constructor_freeze_sha256": constructor_freeze["sha256"],
    "whole_claims": [
        "R5A arbitrary exact center selector, nonzero signed descent count and p-adic divisibility",
        "R5B disjoint-triple bound on minimum selected rational-witness valuation; degree20 minimum at most10",
        "R5C symbolic p+1 global long-cluster carrier is coprime to every derivative",
        "R5D exact repeated2R complete five-equation ladder subfamily excluded by RC2 plus PN4",
        "R5E five odd units imply a higher even derivative with full monic gcd X-1, with no a3 hypothesis"],
    "per_inference_ledger_rows": len(rows),
    "constructor_obligations_covered": len(obligations),
    "substantive_objections": [],
    "required_author_repairs": [],
    "old_seven_return_texts_authorship_and_J15_PN_review_roles_disclosed": True,
    "independent_reaudit_of_own_accepted_old_theorems_claimed": False,
    "new_R5_constructor_strategy_or_clarification_contributor": False,
    "peer_R5_findings_read_before_freeze": False,
    "later_root_R5_inspection_read_before_freeze": False,
    "findings_sent_before_complete_initial_freeze": False,
    "all_root_depth_height_or_unused_witness_bound_claimed": False,
    "residual_quotient_claimed_Casas_Alvero": False,
    "full_J15_degree20_mask_annual_or_novelty_claim": False,
    "mathematical_code_CAS_scan_enumeration_author_rerun": False,
    "candidate_shared_old_files_or_git_mutation": False,
    "spawning_contact_charge_or_access_bypass": False,
    "coordinator_promotion_performed": False,
    "latest_authoritative_weekly_usage": telemetry,
    "command": "python3 problems/2021-B4/reviews/reasoning-return-r5-review-1-freeze-v1.py",
    "records": records
}
manifest_fp = new_json("manifest-v1.json", manifest)
print(json.dumps({"manifest": manifest_fp, "output": output}, indent=2))
