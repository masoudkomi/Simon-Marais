"""One-time initially blind whole-review integrity freeze; no mathematical calculation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/reviews/chart-window-review-1-"


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
constructor_path = "problems/2017-B4/notes/coordinator-chart-window-freeze-v1.json"
constructor_fp = check({"path": constructor_path,
                        "sha256": "f9708bcba4de2c877420e162336a8a8775c3a72e30c98eb2b03fef7e540e6a19"})
constructor_checks = [check(row) for row in read_json(constructor_path)["files"]]
assert len(constructor_checks) == 5

prior_path = "problems/2020-B4/reviews/reasoning-return-r3-review-2-reaudit-manifest-v1.1.json"
prior_fp = check({"path": prior_path,
                  "sha256": "93ab0bdd891fdb6c94a60413af1d0a1d1b021828f9c7650948493ca4c53fa55d"})
prior_checks = [check(row) for row in read_json(prior_path)["records"]]
prior_validation = read_json("problems/2020-B4/reviews/reasoning-return-r3-review-2-reaudit-input-validation-v1.1.json")
older = []
for packet in prior_validation["older_own_packets"]:
    older.append({"manifest": check(packet["manifest"]),
                  "checks": [check(row) for row in packet["checks"]]})
assert len(older) == 29
older.append({"manifest": prior_fp, "checks": prior_checks})

validation_path = create_json("input-validation-v1.json", {
    "checked_at_utc": now,
    "constructor_manifest": constructor_fp,
    "constructor_records": constructor_checks,
    "all_five_constructor_records_unchanged": True,
    "older_own_packets": older,
    "all_thirty_older_own_packets_unchanged": True,
    "new_peer_CW_review_or_findings_read": False,
    "accepted_OC_read_in_full_with_scope": True,
    "own_strict_construction_or_other_unproved_packet_used": False,
    "mathematical_program_enumeration_or_CAS": False,
})
output_path = create_json("freeze-output-v1.json", {
    "frozen_at_utc": now,
    "constructor_records_checked": 5,
    "older_own_packets_checked": 30,
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
    "status": "initially blind whole review; no substantive defect found; exact geometric/coding scope",
    "reviewer": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_sha256": "c272eabf4d5efcd2d0f8075d68b010ec00a48e824bdec81e563f6402a7568e0b",
    "whole_claims": ["CW0", "CW1", "CW2", "CW3", "CW4"],
    "per_inference_ledger_rows": 24,
    "substantive_objections": [],
    "required_author_repairs": [],
    "new_external_theorem_imported": False,
    "entropy_or_UR4_H_PR_claim": False,
    "peer_findings_read_before_freeze": False,
    "mathematical_program_enumeration_or_CAS": False,
    "candidate_or_shared_changes": False,
    "git_operations": False,
    "spawned_agents": False,
    "latest_weekly_total_used_percent": 28,
    "weekly_window_minutes": 10080,
    "weekly_reset_unix": 1792745187,
    "total_used_ceiling_percent": 90,
    "command": "python3 problems/2017-B4/reviews/chart-window-review-1-freeze-v1.py",
    "records": [fingerprint(path) for path in record_paths],
})
print(json.dumps({"frozen_at_utc": now,
                  "manifest": fingerprint(manifest_path),
                  "records": len(record_paths),
                  "constructor_records_checked": 5,
                  "older_own_packets_checked": 30}, indent=2))
