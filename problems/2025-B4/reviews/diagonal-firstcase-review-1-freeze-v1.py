"""One-time blind-review integrity freeze; no mathematical calculation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2025-B4/reviews/diagonal-firstcase-review-1-"


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
constructor_path = "problems/2025-B4/notes/coordinator-diagonal-firstcase-freeze-v1.json"
constructor_fp = check({"path": constructor_path,
                        "sha256": "59ad3e5d858d4b809195f55453f2af4c09ef519580eca5d5c448a1a0db3c3250"})
constructor = read_json(constructor_path)
constructor_checks = [check(row) for row in constructor["files"]]
assert len(constructor_checks) == 8

prior_path = "problems/2017-B4/reviews/rank-mesh-review-1-reaudit-manifest-v1.1.json"
prior_fp = check({"path": prior_path,
                  "sha256": "eccf665f8d9b6b61ee48479c09d9e3faabafaa3f943d25d6f74c2d29950c3ea3"})
prior = read_json(prior_path)
prior_checks = [check(row) for row in prior["records"]]
prior_validation = read_json("problems/2017-B4/reviews/rank-mesh-review-1-reaudit-input-validation-v1.1.json")
older = []
for packet in prior_validation["older_own_packets"]:
    older.append({"manifest": check(packet["manifest"]),
                  "checks": [check(row) for row in packet["checks"]]})
assert len(older) == 26
older.append({"manifest": prior_fp, "checks": prior_checks})

validation_path = create_json("input-validation-v1.json", {
    "checked_at_utc": now,
    "constructor_manifest": constructor_fp,
    "constructor_records": constructor_checks,
    "all_eight_constructor_records_unchanged": True,
    "older_own_packets": older,
    "all_twenty_seven_older_own_packets_unchanged": True,
    "new_peer_CF1_review_or_findings_read": False,
    "primary_read_scope": {
        "mihailescu": "full Theorem1 and Section3 first-case explanation, author version2.0",
        "HHO": "full Introduction items1-3 and complete Table2, arXivv1",
    },
    "Theorem4_appendix_binary_Thue_used": False,
    "external_source_proofs_reconstructed_in_full": False,
    "published_computation_rerun": False,
    "mathematical_program_enumeration_or_CAS": False,
    "new_primary_raw_binary_hash_claimed": False,
})
output_path = create_json("freeze-output-v1.json", {
    "frozen_at_utc": now,
    "constructor_records_checked": 8,
    "older_own_packets_checked": 27,
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
    "status": "initially blind whole review; no substantive defect found; attributed finite-range corollary only",
    "reviewer": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_sha256": "3a6c0bc793d7e5cf77d440fdb27b3ec139d3a5c61fe773b03310e9b8184a1a03",
    "whole_claims": ["CF1 including signed substitution, LTE, relative rank, HHO finite input and exact scope"],
    "per_inference_ledger_rows": 15,
    "substantive_objections": [],
    "required_author_repairs": [],
    "external_theorem_full_proof_reconstructed": False,
    "published_computation_rerun": False,
    "peer_findings_read_before_freeze": False,
    "mathematical_program_enumeration_or_CAS": False,
    "candidate_or_shared_changes": False,
    "git_operations": False,
    "spawned_agents": False,
    "latest_weekly_total_used_percent": 27,
    "weekly_window_minutes": 10080,
    "weekly_reset_unix": 1792745187,
    "total_used_ceiling_percent": 90,
    "command": "python3 problems/2025-B4/reviews/diagonal-firstcase-review-1-freeze-v1.py",
    "records": [fingerprint(path) for path in record_paths],
})
print(json.dumps({"frozen_at_utc": now,
                  "manifest": fingerprint(manifest_path),
                  "records": len(record_paths),
                  "constructor_records_checked": 8,
                  "older_own_packets_checked": 27}, indent=2))
