"""One-time affected-repair integrity freeze; no mathematical calculation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/reviews/rank-mesh-review-1-reaudit-"


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


def hash_rows(value):
    found = []
    if isinstance(value, dict):
        if isinstance(value.get("path"), str) and isinstance(value.get("sha256"), str) and len(value["sha256"]) == 64:
            found.append(value)
        for nested in value.values():
            found.extend(hash_rows(nested))
    elif isinstance(value, list):
        for nested in value:
            found.extend(hash_rows(nested))
    return found


now = datetime.now(timezone.utc).isoformat()
repair_path = "problems/2017-B4/notes/rank-mesh-reasoning-r1-freeze-v1.1.json"
repair_fp = check({"path": repair_path,
                   "sha256": "0273dd67122b549dbf7b9cf6dab57f6671aab52ed793e942524c1bd69718bb14"})
repair = read_json(repair_path)
repair_checks = [check(row) for row in repair["artifacts"]]
assert len(repair_checks) == 8
original_main = check(repair["original_main"])
analytic = check(repair["unchanged_analytic_supplement"])
author_validation = read_json("problems/2017-B4/notes/rank-mesh-reasoning-r1-input-validation-v1.1.json")
unique = {}
for row in hash_rows(author_validation):
    old = unique.setdefault(row["path"], row)
    assert old["sha256"] == row["sha256"]
author_checks = [check(row) for row in unique.values()]

initials = []
for path, digest in [
    ("problems/2017-B4/reviews/rank-mesh-review-1-manifest-v1.json",
     "e76dde7938e9e5a7e48ba6b8eea6cee6e4fa695cf898dcc44973df3d25aeb328"),
    ("problems/2017-B4/reviews/rank-mesh-review-2-manifest-v1.json",
     "7f591a955988bc30e867b8928d530b6e22926ecd8170987b1a6e3e13fa522dcb"),
]:
    fp = check({"path": path, "sha256": digest})
    initials.append({"manifest": fp,
                     "checks": [check(row) for row in read_json(path)["records"]]})

prior_path = "problems/2020-B4/reviews/reasoning-return-r3-review-2-manifest-v1.json"
prior_fp = check({"path": prior_path,
                  "sha256": "bbda561c3d8379666e92308ae851de4f46c042548f4d4e3bf6bcdc0ba01b07b6"})
prior = read_json(prior_path)
prior_checks = [check(row) for row in prior["records"]]
prior_validation = read_json("problems/2020-B4/reviews/reasoning-return-r3-review-2-input-validation-v1.json")
older = []
for packet in prior_validation["older_own_packets"]:
    older.append({"manifest": check(packet["manifest"]),
                  "checks": [check(row) for row in packet["checks"]]})
assert len(older) == 25
older.append({"manifest": prior_fp, "checks": prior_checks})

validation_path = create_json("input-validation-v1.1.json", {
    "checked_at_utc": now,
    "repair_manifest": repair_fp,
    "repair_artifacts": repair_checks,
    "original_main": original_main,
    "unchanged_analytic_supplement": analytic,
    "author_declared_unique_input_checks": author_checks,
    "author_declared_unique_input_count": len(author_checks),
    "both_original_initial_packets": initials,
    "older_own_packets": older,
    "all_twenty_six_older_own_packets_unchanged": True,
    "both_original_reports_read_after_both_initial_freezes": True,
    "new_peer_targeted_findings_read": False,
    "unrelated_uniform_strict_candidate_is_a_premise": False,
    "mathematical_program_enumeration_or_CAS": False,
})
output_path = create_json("freeze-output-v1.1.json", {
    "frozen_at_utc": now,
    "repair_artifacts_checked": 8,
    "author_unique_input_rows_checked": len(author_checks),
    "older_own_packets_checked": 26,
    "both_original_initials_unchanged": True,
    "all_fingerprints_match": True,
    "recommended_resolved": ["RMR1-01", "RM2-01", "N1"],
    "open_substantive_issues": [],
    "complete_targeted_report_before_disclosure": True,
    "candidate_shared_or_Git_mutation": False,
})
record_paths = [PREFIX + name for name in [
    "initial-v1.1.md", "issues-v1.1.json", "source-checks-v1.1.md", "freeze-v1.1.py",
]] + [validation_path, output_path]
manifest_path = create_json("manifest-v1.1.json", {
    "frozen_at_utc": now,
    "status": "complete targeted reaudit; recommend resolving repair issues; no promotion",
    "reviewer": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "main_v1_1_sha256": "f6c1681ae288b37d2e845e31ca1ef4503d659c9669ec6801266f3564de771ee3",
    "repair_sha256": "f9d637f76ee320d022dd481b836b04b584cf392bc5acf130106326701c94767d",
    "UR3_sha256": "40ad9b252b6c34f5dee5c8cd3eedea8e8feeabb0cec1497b224bf5c32ba58aab",
    "recommended_resolved": ["RMR1-01", "RM2-01", "N1"],
    "targeted_ledger_rows": 12,
    "substantive_objections": [],
    "both_targeted_audits_and_root_reconciliation_required": True,
    "original_initial_reports_preserved": True,
    "new_peer_targeted_findings_read_before_freeze": False,
    "mathematical_program_enumeration_or_CAS": False,
    "candidate_or_shared_changes": False,
    "git_operations": False,
    "spawned_agents": False,
    "latest_weekly_total_used_percent": 27,
    "weekly_window_minutes": 10080,
    "weekly_reset_unix": 1792745187,
    "total_used_ceiling_percent": 90,
    "command": "python3 problems/2017-B4/reviews/rank-mesh-review-1-reaudit-freeze-v1.1.py",
    "records": [fingerprint(path) for path in record_paths],
})
print(json.dumps({"frozen_at_utc": now,
                  "manifest": fingerprint(manifest_path),
                  "records": len(record_paths),
                  "author_unique_inputs_checked": len(author_checks),
                  "older_own_packets_checked": 26}, indent=2))
