"""One-time initially blind whole-review freeze; hashes/suffix checks only."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/reviews/UR4-assembly-review-1-"


def fingerprint(path):
    payload = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(payload),
            "sha256": hashlib.sha256(payload).hexdigest()}


def check(expected):
    actual = fingerprint(expected["path"])
    assert actual["sha256"] == expected["sha256"], actual
    if "bytes" in expected:
        assert actual["bytes"] == expected["bytes"], actual
    return dict(actual, matches=True)


def read_json(path):
    return json.loads((ROOT / path).read_text())


def create_json(suffix, payload):
    path = PREFIX + suffix
    with (ROOT / path).open("x") as stream:
        json.dump(payload, stream, indent=2)
        stream.write("\n")
    return path


now = datetime.now(timezone.utc).isoformat()
constructor_path = "problems/2017-B4/notes/coordinator-UR4-assembly-freeze-v1.json"
constructor_fp = check({"path": constructor_path,
                        "sha256": "20c10f07ba8cc7977628e218e4339976428e552f65d0efa1ec5764db33a03a0f"})
constructor_checks = [check(row) for row in read_json(constructor_path)["files"]]
assert len(constructor_checks) == 14
assert constructor_checks[0]["sha256"] == "fa0bd05d345dee884335e3a5cd0e601ce08e8212da3d812227750f04c5113d0f"

accepted_checks = []
suffix_checks = []
nested_constructor_checks = []
for tag, sha in [
    ("local-rank-mesh", "67d6821f64c0be2a64bb49ccd595dd80105ca7ed913b2fd6be342b81cf756a10"),
    ("chart-window", "f89e784c407f3c780d2ca9a95ea4f58e0cd71841f2855ffa7225465f9dd9abc1"),
]:
    accepted_path = f"problems/2017-B4/proofs/reviewed-{tag}-v1.1.md"
    old_path = f"problems/2017-B4/notes/coordinator-{tag}-candidate-v1.md"
    accepted_checks.append(check({"path": accepted_path, "sha256": sha}))
    accepted_checks.append(fingerprint(f"problems/2017-B4/reviews/{tag}-acceptance.md"))
    assert (ROOT / accepted_path).read_bytes().endswith((ROOT / old_path).read_bytes())
    suffix_checks.append({"accepted_path": accepted_path, "original_path": old_path,
                          "complete_original_is_exact_byte_suffix": True})
    nested_path = f"problems/2017-B4/notes/coordinator-{tag}-freeze-v1.json"
    nested = read_json(nested_path)
    nested_constructor_checks.append({"manifest": fingerprint(nested_path),
                                      "records": [check(row) for row in nested["files"]]})

prior_path = "problems/2017-B4/notes/allD-uniform-strict-reasoning-r1-manifest-v1.json"
prior_fp = check({"path": prior_path,
                  "sha256": "126fd14f143d6ab619c7aba5d57be968471080d7f07bb081805f6706434b1f18"})
prior_checks = [check(row) for row in read_json(prior_path)["records"]]
prior_validation = read_json("problems/2017-B4/notes/allD-uniform-strict-reasoning-r1-input-validation-v1.json")
older = []
for packet in prior_validation["older_own_packets"]:
    older.append({"manifest": check(packet["manifest"]),
                  "checks": [check(row) for row in packet["checks"]]})
assert len(older) == 31
older.append({"manifest": prior_fp, "checks": prior_checks})
ledger = read_json(PREFIX + "issues-v1.json")
assert len(ledger["checks"]) == 42
assert ledger["open_substantive_issues"] == []

validation_path = create_json("input-validation-v1.json", {
    "checked_at_utc": now,
    "constructor_manifest": constructor_fp,
    "constructor_records": constructor_checks,
    "all_fourteen_constructor_records_unchanged": True,
    "newly_accepted_LW_CW_records": accepted_checks,
    "accepted_suffix_checks": suffix_checks,
    "nested_LW_CW_constructor_records": nested_constructor_checks,
    "older_own_packets": older,
    "all_thirty_two_older_own_packets_unchanged": True,
    "new_peer_G4_review_or_findings_read": False,
    "own_accepted_D4_US_dependency_authorship_disclosed": True,
    "new_allD_strict_candidate_used_as_premise": False,
    "old_G4_draft_used_to_fill_candidate_gap": False,
    "mathematical_program_enumeration_or_CAS": False,
})
output_path = create_json("freeze-output-v1.json", {
    "frozen_at_utc": now,
    "constructor_records_checked": 14,
    "additional_accepted_LW_CW_records": 4,
    "older_own_packets_checked": 32,
    "all_fingerprints_match": True,
    "open_substantive_issues": [],
    "whole_initial_review_complete_before_disclosure": True,
    "candidate_or_shared_mutation": False,
    "git_operations": False,
})
record_paths = [PREFIX + name for name in [
    "initial-v1.md", "issues-v1.json", "source-checks-v1.md", "freeze-v1.py",
]] + [validation_path, output_path]
manifest_path = create_json("manifest-v1.json", {
    "frozen_at_utc": now,
    "status": "initially blind whole review; no substantive defect found in complete scoped G4 implication",
    "reviewer": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_sha256": "fa0bd05d345dee884335e3a5cd0e601ce08e8212da3d812227750f04c5113d0f",
    "whole_claims": ["G4 uniform GE4 deficit", "fixed-D4 balanced limit existence"],
    "per_inference_ledger_rows": 42,
    "substantive_objections": [],
    "required_author_repairs": [],
    "own_accepted_D4_US_authorship_boundary_disclosed": True,
    "newly_accepted_exact_LW_CW_bodies_checked": True,
    "allD_growing_D_PR_numerical_or_novelty_conclusion": False,
    "peer_findings_read_before_freeze": False,
    "mathematical_program_enumeration_or_CAS": False,
    "candidate_or_shared_changes": False,
    "git_operations": False,
    "spawned_agents": False,
    "latest_weekly_total_used_percent": 30,
    "weekly_window_minutes": 10080,
    "weekly_reset_unix": 1792745187,
    "total_used_ceiling_percent": 90,
    "command": "python3 problems/2017-B4/reviews/UR4-assembly-review-1-freeze-v1.py",
    "records": [fingerprint(path) for path in record_paths],
})
print(json.dumps({"frozen_at_utc": now,
                  "manifest": fingerprint(manifest_path),
                  "records": len(record_paths),
                  "constructor_records_checked": 14,
                  "older_own_packets_checked": 32}, indent=2))
