"""One-time blind-review integrity freeze; no mathematical calculation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2020-B4/reviews/reasoning-return-r3-review-2-"


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
constructor_path = "problems/2020-B4/notes/reasoning-return-r3-freeze-v1.json"
constructor_fp = check({"path": constructor_path,
                        "sha256": "413351e9d6d6b9e8c463ba6b3ad230f2d4440c5042711df882f879a7b82a02ed"})
constructor = read_json(constructor_path)
constructor_checks = [check(row) for row in constructor["artifacts"]]
assert len(constructor_checks) == 7
author_validation = read_json("problems/2020-B4/notes/reasoning-return-r3-input-validation-v1.json")
unique = {}
for row in hash_rows(author_validation):
    old = unique.setdefault(row["path"], row)
    assert old["sha256"] == row["sha256"]
author_input_checks = [check(row) for row in unique.values()]

prior_path = "problems/2017-B4/notes/uniform-strict-reasoning-r1-manifest-v1.json"
prior_fp = check({"path": prior_path,
                  "sha256": "902b8ad01e994b03204673f55f647c2e03db80e8ac2b917faf514bc0ca249bbc"})
prior = read_json(prior_path)
prior_checks = [check(row) for row in prior["records"]]
prior_validation = read_json("problems/2017-B4/notes/uniform-strict-reasoning-r1-input-validation-v1.json")
older = []
for packet in prior_validation["older_own_packets"]:
    older.append({"manifest": check(packet["manifest"]),
                  "checks": [check(row) for row in packet["checks"]]})
assert len(older) == 24
older.append({"manifest": prior_fp, "checks": prior_checks})

validation_path = create_json("input-validation-v1.json", {
    "checked_at_utc": now,
    "constructor_manifest": constructor_fp,
    "constructor_artifacts": constructor_checks,
    "constructor_declared_unique_input_checks": author_input_checks,
    "constructor_declared_unique_input_count": len(author_input_checks),
    "older_own_packets": older,
    "all_twenty_five_older_own_packets_unchanged": True,
    "new_peer_2020_return_review_or_findings_read": False,
    "mathematical_program_scan_or_CAS": False,
    "hand_counterexample": "q4 normalized difference set21; all10 undirected separations supplied",
    "primary_source": "https://aeb.win.tue.nl/preprints/hermitian1.pdf",
    "source_read_scope": "complete applicable Section2 setup and Lemmas1-2 with proofs pp1-2",
    "primary_raw_byte_hash_claimed": False,
})
output_path = create_json("freeze-output-v1.json", {
    "frozen_at_utc": now,
    "constructor_artifacts_checked": 7,
    "constructor_unique_input_rows_checked": len(author_input_checks),
    "older_own_packets_checked": 25,
    "all_fingerprints_match": True,
    "open_substantive_issues": ["2020R2-01 F4 requires t-fixed rather than arbitrary common T-fixed subgroup"],
    "whole_initial_review_complete_before_disclosure": True,
    "candidate_or_shared_mutation": False,
    "git_operations": False,
})
record_paths = [PREFIX + name for name in [
    "initial-v1.md", "issues-v1.json", "source-checks-v1.md", "freeze-v1.py",
]] + [validation_path, output_path]
manifest_path = create_json("manifest-v1.json", {
    "frozen_at_utc": now,
    "status": "initially blind whole review; one scoped statement repair required; no promotion",
    "reviewer": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_sha256": "2cb5803b20cdcc96961956773f02a3fe2e00f0ae9a4bee8df56af0ec2cd86796",
    "whole_claims": ["F1", "F1a", "F2", "F2a", "F3", "F3a", "B1"],
    "per_inference_ledger_rows": 28,
    "substantive_objections": ["2020R2-01"],
    "author_full_versioned_repair_and_both_affected_reaudits_required": True,
    "peer_findings_read_before_freeze": False,
    "mathematical_program_scan_or_CAS": False,
    "candidate_or_shared_changes": False,
    "git_operations": False,
    "spawned_agents": False,
    "latest_weekly_total_used_percent": 27,
    "weekly_window_minutes": 10080,
    "weekly_reset_unix": 1792745187,
    "total_used_ceiling_percent": 90,
    "command": "python3 problems/2020-B4/reviews/reasoning-return-r3-review-2-freeze-v1.py",
    "records": [fingerprint(path) for path in record_paths],
})
print(json.dumps({"frozen_at_utc": now,
                  "manifest": fingerprint(manifest_path),
                  "records": len(record_paths),
                  "constructor_unique_inputs_checked": len(author_input_checks),
                  "older_own_packets_checked": 25}, indent=2))
