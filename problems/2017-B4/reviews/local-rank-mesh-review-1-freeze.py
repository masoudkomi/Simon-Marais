"""Administrative byte integrity and one-time initially blind audit freeze."""
from pathlib import Path
import datetime
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/reviews/local-rank-mesh-review-1-"


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


candidate = check({
    "path": "problems/2017-B4/notes/coordinator-local-rank-mesh-candidate-v1.md",
    "sha256": "09c206718f1acecb9f23ae9bdb54122a4e9a9420b4549326413a664cb44230c5"})
target_manifest = check({
    "path": "problems/2017-B4/notes/coordinator-local-rank-mesh-freeze-v1.json",
    "sha256": "a3e76f8d6dcb6a2db900e810aa75c076b4b479235e95e6bbe021a85799fdc781"})
inputs = [check(expected) for expected in read(target_manifest["path"])["files"]]
protocol = [check(expected) for expected in [
    {"path": "AGENTS.md", "sha256": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"},
    {"path": "problems/2017-B4/statement.md", "sha256": "e459750064b4e25e3eaa71f25f236c046548147e415b06d8bd097839020228f3"},
]]

old_path = "problems/2017-B4/reviews/uniform-strict-review-1-manifest-initial.json"
old_manifest = check({"path": old_path,
                      "sha256": "bf4502a10fcab5fa45724a745e66aeaae35a0e9e6a72d6503555e47f07d35366"})
preserved = {old_path: old_manifest}
for expected in read(old_path)["artifacts"]:
    actual = check(expected)
    preserved[actual["path"]] = actual
previous_validation = read("problems/2017-B4/reviews/uniform-strict-review-1-input-validation.json")
for expected in previous_validation["earlier_unique_records_preserved"]:
    actual = check(expected)
    if actual["path"] in preserved:
        assert preserved[actual["path"]] == actual
    preserved[actual["path"]] = actual
assert len(preserved) == 159
official = next(check(expected) for expected in previous_validation["additional_source_and_acceptance_records"]
                if expected["path"] == ".cache/official/2017-paper_b.pdf")

validation = write("input-validation.json", {
    "validated_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "candidate": candidate,
    "candidate_manifest": target_manifest,
    "all_six_declared_candidate_inputs": inputs,
    "protocol_and_official_statement": protocol,
    "cached_official_pdf": official,
    "earlier_unique_records_preserved": sorted(preserved.values(), key=lambda r: r["path"]),
    "earlier_unique_count": len(preserved),
    "exact_RM1_is_explicit_conditional_premise_not_author_promotion": True,
    "no_peer_LW_or_fresh_RM1_audit_findings_read": True,
    "mathematical_program_CAS_finite_certificate_or_author_rerun": False,
})
artifacts = [row(PREFIX + suffix) for suffix in [
    "initial.md", "issues.md", "source-checks.md", "freeze.py"
]] + [validation]
manifest = write("manifest-initial.json", {
    "frozen_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "status": "initially blind whole independent nonconstructor audit; no substantive defect found in conditional LW1; no promotion",
    "reviewer": "review_2017_coarsening_r1",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate": candidate,
    "candidate_manifest": target_manifest,
    "whole_claims_reconstructed": ["LW1"],
    "inference_ledger_rows": 28,
    "substantive_issues": [],
    "exact_RM1_disk_port_diameter_conclusions_remain_conditional": True,
    "prior_general_RM1_authorship_disclosed_not_counted_as_independent_RM1_audit": True,
    "constructed_new_LW_local_code": False,
    "peer_LW_findings_read_before_freeze": False,
    "artifacts": artifacts,
    "declared_candidate_inputs_verified": len(inputs),
    "earlier_unique_frozen_records_preserved": len(preserved),
    "global_N_required_O_L": False,
    "one_log_R_anchor_and_no_outside_exit_permutation_checked": True,
    "actual_global_faces_complete_fine_boundaries_and_same_exterior_checked": True,
    "rare_absence_after_replacement_only_with_zero_flux_qualification": True,
    "reviewer_promotion": False,
    "H_PR_UR4_lower_direction_entropy_or_official_limit_claim": False,
    "new_mathematical_program_CAS_certificate_or_author_rerun": False,
    "only_assigned_review_prefix_written": True,
    "git_shared_edits_spawning_contacts_charges_or_bypass": False,
    "weekly_total_used_percent": 28,
    "telemetry_at_utc": "2026-10-17 07:00:53 UTC",
    "weekly_reset_unix": 1792745187,
    "total_used_ceiling_percent": 90,
})
print(json.dumps({"manifest": manifest, "artifacts": artifacts,
                  "declared_candidate_inputs_verified": len(inputs),
                  "earlier_unique_frozen_records_preserved": len(preserved)}, indent=2))
