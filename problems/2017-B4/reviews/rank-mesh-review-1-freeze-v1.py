"""One-time blind-review integrity freeze; no mathematical calculation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/reviews/rank-mesh-review-1-"


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
constructor_path = "problems/2017-B4/notes/rank-mesh-reasoning-r1-freeze-v1.json"
constructor_fp = check({"path": constructor_path,
                        "sha256": "7173ee9db5d7990af60ca0731a301d9017691e42f9c741efce1e81a7d90de747"})
constructor = read_json(constructor_path)
constructor_checks = [check(row) for row in constructor["artifacts"] + constructor["inputs"]]
assert len(constructor_checks) == 13

prior_path = "problems/2017-B4/reviews/strict-transfer-review-1-manifest-v1.json"
prior_fp = check({"path": prior_path,
                  "sha256": "70b2efcb2a9a34244b5f01ce3eb75357c002f92ccc0820462dc3ca15154fa0cd"})
prior = read_json(prior_path)
prior_checks = [check(row) for row in prior["records"]]
prior_validation = read_json("problems/2017-B4/reviews/strict-transfer-review-1-input-validation-v1.json")
older = []
for packet in prior_validation["older_own_packets"]:
    older.append({"manifest": check(packet["manifest"]),
                  "checks": [check(row) for row in packet["checks"]]})
assert len(older) == 20
older.append({"manifest": prior_fp, "checks": prior_checks})

validation_path = create_json("input-validation-v1.json", {
    "checked_at_utc": now,
    "constructor_manifest": constructor_fp,
    "constructor_and_input_records": constructor_checks,
    "all_thirteen_constructor_and_input_records_unchanged": True,
    "older_own_packets": older,
    "all_twenty_one_older_own_packets_unchanged": True,
    "new_peer_rank_mesh_or_UR3_review_or_findings_read": False,
    "mathematical_computation_enumeration_or_CAS": False,
    "counterexample_method": "hand-constructed D2 grid with many small window holes; no computation",
    "public_primary_read": {
        "url": "https://arxiv.org/pdf/math/0008220v3",
        "read_scope": "Section1.6 metric; relevant Section2 and3; complete Section4 theorem/proofs; printedpage13 lozenges",
        "independent_binary_retrieval_hash_claimed": False,
    },
})
output_path = create_json("freeze-output-v1.json", {
    "frozen_at_utc": now,
    "constructor_records_checked": 13,
    "older_own_packets_checked": 21,
    "all_fingerprints_match": True,
    "open_substantive_issue": "RMR1-01 rectifiable-window boundary components",
    "no_separate_substantive_LC3_or_UR3_GE_issue_found": True,
    "whole_initial_review_complete_before_disclosure": True,
    "candidate_or_shared_mutation": False,
    "git_operations": False,
})
record_paths = [PREFIX + name for name in [
    "initial.md", "issues.md", "source-checks.md", "freeze-v1.py",
]] + [validation_path, output_path]
manifest_path = create_json("manifest-v1.json", {
    "frozen_at_utc": now,
    "status": "initially blind whole review; one standalone domain repair requested; no promotion",
    "reviewer": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_sha256": "e0f2e55e62aabe5547120f4fc72c506c3f680844a90aa98ece7147d404178d27",
    "UR3_sha256": "40ad9b252b6c34f5dee5c8cd3eedea8e8feeabb0cec1497b224bf5c32ba58aab",
    "whole_claims": ["RM1", "RM1a", "scoped RM2", "RM2a", "RM3", "LC3", "UR3-GE"],
    "substantive_objections": ["RMR1-01 missing boundary-component/Jordan condition in mainlines173-178"],
    "editorial_notes": ["N1 general-D alphabet has binom(D,2) types"],
    "author_full_versioned_repair_and_two_affected_reaudits_required": True,
    "no_separate_substantive_LC3_or_UR3_GE_issue_found": True,
    "peer_findings_read_before_freeze": False,
    "mathematical_program_enumeration_or_CAS": False,
    "candidate_or_shared_changes": False,
    "git_operations": False,
    "spawned_agents": False,
    "latest_weekly_total_used_percent": 25,
    "weekly_window_minutes": 10080,
    "weekly_reset_unix": 1792745187,
    "total_used_ceiling_percent": 90,
    "command": "python3 problems/2017-B4/reviews/rank-mesh-review-1-freeze-v1.py",
    "records": [fingerprint(path) for path in record_paths],
})
print(json.dumps({"frozen_at_utc": now,
                  "manifest": fingerprint(manifest_path),
                  "records": len(record_paths),
                  "constructor_records_checked": 13,
                  "older_own_packets_checked": 21}, indent=2))
