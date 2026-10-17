"""Administrative input verification and immutable initial audit freeze."""
from pathlib import Path
import datetime
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/reviews/uniform-strict-review-1-"


def row(path):
    raw = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}


def check(expected):
    actual = row(expected["path"])
    assert actual["sha256"] == expected["sha256"], actual
    if "bytes" in expected:
        assert actual["bytes"] == expected["bytes"], actual
    return actual


def read(path):
    return json.loads((ROOT / path).read_text())


def write(suffix, obj):
    path = PREFIX + suffix
    with (ROOT / path).open("x", encoding="utf-8") as out:
        json.dump(obj, out, indent=2, ensure_ascii=False)
        out.write("\n")
    return row(path)


target_prefix = "problems/2017-B4/notes/uniform-strict-reasoning-r1-"
target_manifest = check({"path": target_prefix + "manifest-v1.json",
                         "sha256": "902b8ad01e994b03204673f55f647c2e03db80e8ac2b917faf514bc0ca249bbc"})
target_rows = [check(expected) for expected in read(target_manifest["path"])["records"]]
candidate = check({"path": target_prefix + "candidate-v1.md",
                   "sha256": "643d0906e3eebee91dd91f53e5e1b241de35c3b7912d5010d2e651e830258c9d"})
validation = read(target_prefix + "input-validation-v1.json")
dependencies = [check(expected) for expected in validation["accepted_dependencies_and_unproved_inspiration"]]
protocol = [check(expected) for expected in validation["additional_inputs"]]
extra = [row(path) for path in [
    "problems/2017-B4/proofs/reviewed-fixedD-structural-v1.2.md",
    "problems/2017-B4/reviews/annulus-acceptance.json",
    "problems/2017-B4/reviews/lens-cutting-acceptance.json",
    "problems/2017-B4/reviews/directed-geodesics-acceptance.json",
    "problems/2017-B4/reviews/strict-transfer-acceptance.json",
    ".cache/official/2017-paper_b.pdf",
]]
assert validation["program_is_a_theorem_premise"] is False
assert validation["rank_mesh_is_a_theorem_premise"] is False

old_manifest_path = "problems/2020-B4/notes/reasoning-return-r3-freeze-v1.1.json"
old_manifest = check({"path": old_manifest_path,
                      "sha256": "807827ddb14ace9a98f0c9f8bf7f63244129414d0a85cfcde4889ff84d7aa806"})
preserved = {old_manifest_path: old_manifest}
for expected in read(old_manifest_path)["artifacts"]:
    actual = check(expected)
    preserved[actual["path"]] = actual
old_validation = read("problems/2020-B4/notes/reasoning-return-r3-input-validation-v1.1.json")
for expected in old_validation["all_earlier_unique_frozen_records_preserved"]:
    actual = check(expected)
    if actual["path"] in preserved:
        assert preserved[actual["path"]] == actual
    preserved[actual["path"]] = actual
assert len(preserved) == 153

input_row = write("input-validation.json", {
    "validated_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "candidate": candidate,
    "candidate_manifest": target_manifest,
    "all_six_constructor_records": target_rows,
    "accepted_dependencies_and_nonpremise_program": dependencies,
    "protocol_official_statement": protocol,
    "additional_source_and_acceptance_records": extra,
    "earlier_unique_records_preserved": sorted(preserved.values(), key=lambda x: x["path"]),
    "earlier_unique_count": len(preserved),
    "no_peer_uniform_strict_review_read": True,
    "whole_US1_US2_US3_exact_reasoning": True,
    "mathematical_program_CAS_or_author_rerun": False,
})
artifacts = [row(PREFIX + suffix) for suffix in [
    "initial.md", "issues.md", "source-checks.md", "freeze.py"
]] + [input_row]
manifest = write("manifest-initial.json", {
    "frozen_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "status": "initially blind whole independent nonconstructor review; no substantive defect found; no promotion",
    "reviewer": "review_2017_coarsening_r1",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate": candidate,
    "candidate_manifest": target_manifest,
    "claims_wholly_reconstructed": ["US1", "US2", "US3"],
    "substantive_issues": [],
    "inference_ledger_rows": 30,
    "peer_US_findings_read_before_freeze": False,
    "constructed_US_argument": False,
    "prior_annulus_and_structural_dependency_authorship_disclosed": True,
    "artifacts": artifacts,
    "constructor_records_verified": len(target_rows),
    "earlier_unique_frozen_records_preserved": len(preserved),
    "whole_buffer_common_offset_actual_reference_and_compact_strict_D4_retained": True,
    "q_independent_tolerance_and_q_dependent_scale_only_checked": True,
    "every_m_supremum_upper_and_fixed_original_domain_M_limit_checked": True,
    "new_mathematical_program_CAS_or_author_rerun": False,
    "reviewer_promotion": False,
    "H_PR_all_D_boundary_stratum_or_official_limit_claim": False,
    "only_assigned_review_prefix_written": True,
    "git_shared_edits_spawning_contacts_charges_or_bypass": False,
    "weekly_total_used_percent": 28,
    "telemetry_at_utc": "2026-10-17 07:00:53 UTC",
    "weekly_reset_unix": 1792745187,
    "total_used_ceiling_percent": 90,
})
print(json.dumps({"manifest": manifest, "artifacts": artifacts,
                  "constructor_records_verified": len(target_rows),
                  "earlier_unique_frozen_records_preserved": len(preserved)}, indent=2))
