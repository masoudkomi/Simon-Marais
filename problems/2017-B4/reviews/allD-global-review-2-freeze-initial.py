"""Exclusive blind whole-review metadata freeze; no mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/reviews/allD-global-review-2-"
TARGET_PREFIX = "problems/2017-B4/notes/allD-global-reasoning-r1-"


def read_json(path):
    return json.loads((ROOT / path).read_text())


def row(path):
    payload = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(payload),
            "sha256": hashlib.sha256(payload).hexdigest()}


checked = {}


def check(expected):
    actual = row(expected["path"])
    assert actual["sha256"] == expected["sha256"], actual
    if "bytes" in expected:
        assert actual["bytes"] == expected["bytes"], actual
    if actual["path"] in checked:
        assert checked[actual["path"]] == actual
    checked[actual["path"]] = actual
    return actual


def create_json(suffix, payload):
    path = PREFIX + suffix
    assert path.startswith(PREFIX)
    with (ROOT / path).open("x", encoding="utf-8") as stream:
        json.dump(payload, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    return row(path)


now = datetime.now(timezone.utc).isoformat()
target = check({
    "path": TARGET_PREFIX + "candidate-v1.md", "bytes": 46506,
    "sha256": "c16acc6b4785c114648ec8848311d5022284c894047bef9013e7313c34706428",
})
target_manifest = check({
    "path": TARGET_PREFIX + "manifest-v1.json", "bytes": 3810,
    "sha256": "64a2790adf232a9e43d532762e594c87d3f2190aeb15901b07d1bf186e8e68a3",
})
manifest = read_json(target_manifest["path"])
target_rows = [check(expected) for expected in manifest["records"]]
assert len(target_rows) == 8
assert manifest["candidate"] == target

sources = read_json(TARGET_PREFIX + "sources-v1.json")
accepted_bodies = [check(expected) for expected in sources["logical_accepted_inputs"]]
acceptance_records = [check(expected) for expected in sources["acceptance_scope_fingerprints"]]
assert len(accepted_bodies) == len(acceptance_records) == 10
strict_raw = check(sources["strict_status_chronology"]["raw"])
strict_accepted = check(sources["strict_status_chronology"]["accepted"])
assert (ROOT / strict_accepted["path"]).read_bytes().endswith(
    (ROOT / strict_raw["path"]).read_bytes())
strict_manifest = check(sources["strict_original_manifest"])
strict_rows = [check(expected) for expected in
               read_json(strict_manifest["path"])["records"]]
assert len(strict_rows) == 8

constructor_validation = read_json(TARGET_PREFIX + "input-validation-v1.json")
declared_inputs = [check(expected) for expected in
                   constructor_validation["exact_input_records"]]
constructor_old = [check(expected) for expected in
                   constructor_validation["earlier_own_records"]]
assert len(declared_inputs) == constructor_validation["unique_input_paths_verified"] == 37
assert len(constructor_old) == constructor_validation["earlier_own_paths_verified_unchanged"] == 138
assert {x["path"] for x in accepted_bodies + acceptance_records}.issubset(
    {x["path"] for x in declared_inputs})

obligations = read_json(TARGET_PREFIX + "obligations-v1.json")
ids = [x["id"] for x in obligations["new_inferences_for_complete_adversarial_review"]]
assert ids == [f"AG-{i:02d}" for i in range(1, 41)]
ledger = (ROOT / (PREFIX + "issues-initial.md")).read_text()
for inference_id in ids:
    assert "| " + inference_id + " |" in ledger
assert "Substantive issues found:0" in ledger

prior_path = "problems/2022-B4/notes/reasoning-return-r4-freeze-v1.json"
prior_manifest = check({
    "path": prior_path, "bytes": 3530,
    "sha256": "f579d150c8b52450e5c20630fd36621ba8d36c3a6168c23235d352068c413f66",
})
earlier = {prior_manifest["path"]: prior_manifest}
for expected in read_json(prior_path)["artifacts"]:
    actual = check(expected)
    earlier[actual["path"]] = actual
prior_validation = read_json(
    "problems/2022-B4/notes/reasoning-return-r4-input-validation-v1.json")
for expected in prior_validation["earlier_unique_records_preserved"]:
    actual = check(expected)
    if actual["path"] in earlier:
        assert earlier[actual["path"]] == actual
    earlier[actual["path"]] = actual
assert len(earlier) == 196

validation = create_json("input-validation.json", {
    "validated_at_utc": now,
    "metadata_only_not_mathematical_evidence": True,
    "target_candidate": target,
    "target_manifest": target_manifest,
    "all_eight_target_artifacts": target_rows,
    "all_ten_complete_accepted_bodies_read": accepted_bodies,
    "all_ten_complete_acceptance_scopes_read": acceptance_records,
    "strict_raw_body": strict_raw,
    "strict_accepted_body": strict_accepted,
    "strict_complete_exact_suffix_verified": True,
    "strict_original_manifest": strict_manifest,
    "all_eight_strict_manifest_rows": strict_rows,
    "declared_exact_input_rows": declared_inputs,
    "constructor_earlier_immutable_rows_metadata_only": constructor_old,
    "forty_inference_ids_checked": ids,
    "substantive_issue_count": 0,
    "editorial_repairs_required": 0,
    "earlier_unique_records_preserved": sorted(earlier.values(), key=lambda x: x["path"]),
    "earlier_unique_count": len(earlier),
    "unique_external_or_earlier_paths_verified": len(checked),
    "fresh_peer_global_R1_findings_or_root_later_inspection_read": False,
    "older_own_structural_annulus_rank_D4_background_authorship_disclosed": True,
    "independent_review_of_own_old_background_claimed": False,
    "new_global_constructor_or_co_constructor": False,
    "mathematical_computation_CAS_scan_or_author_rerun": False,
    "only_new_assigned_review_prefix_written": True,
})

artifacts = [row(PREFIX + suffix) for suffix in [
    "initial.md", "issues-initial.md", "source-checks-initial.md", "freeze-initial.py",
]] + [validation]
assert len(artifacts) == 5
review_manifest = create_json("manifest-initial.json", {
    "frozen_at_utc": now,
    "status": "fresh initially blind WHOLE independent R2 audit complete; no substantive objection found on exact scope; coordinator reconciliation pending",
    "reviewer": "/root/review_2017_coarsening_r1",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate": target,
    "candidate_manifest": target_manifest,
    "whole_inferences_reconstructed": 40,
    "substantive_issues_found": 0,
    "editorial_repairs_required": 0,
    "complete_main_source_log_obligations_and_ten_inputs_scopes_read": True,
    "peer_global_findings_read_before_initial_freeze": False,
    "coordinator_later_inspection_read_before_initial_freeze": False,
    "older_own_local_background_authorship_disclosed": True,
    "fresh_independent_review_of_own_old_local_inputs_claimed": False,
    "numerical_value_full_annual_solution_PR_or_novelty_claim": False,
    "mathematical_program_CAS_enumeration_or_scan": False,
    "author_certificate_rerun": False,
    "git_shared_edits_spawning_contacts_charges_or_bypass": False,
    "earlier_unique_own_paths_verified_unchanged": len(earlier),
    "unique_external_or_earlier_paths_verified": len(checked),
    "last_direct_weekly_telemetry": {
        "total_used_percent": 32, "window_minutes": 10080,
        "reset_unix": 1792745187, "total_ceiling_percent": 90,
        "ordinary_usage_allowed": True, "integration_reserve": True,
        "read_during_this_review": True,
    },
    "command": "python3 problems/2017-B4/reviews/allD-global-review-2-freeze-initial.py",
    "artifacts": artifacts,
})
for expected in artifacts:
    check(expected)
print(json.dumps({
    "manifest": review_manifest, "artifacts": artifacts,
    "whole_inferences": 40, "substantive_issues": 0,
    "target_artifacts_verified": len(target_rows),
    "declared_inputs_verified": len(declared_inputs),
    "constructor_earlier_rows_verified": len(constructor_old),
    "earlier_unique_own_records_preserved": len(earlier),
    "unique_external_or_earlier_paths_verified": len(checked) - len(artifacts),
}, indent=2))
