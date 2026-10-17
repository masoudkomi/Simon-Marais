"""One-time blind whole-review integrity freeze; no mathematical calculation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/reviews/single-pair-allD-review-1-"


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
constructor_path = "problems/2017-B4/notes/coordinator-single-pair-allD-freeze-v1.json"
constructor_fp = check({"path": constructor_path,
                        "sha256": "2714227e14b516d260a1c9d1c8cdef5ae7b9071ea8b9b9c7140b65b6ead520db"})
constructor = read_json(constructor_path)
constructor_checks = [check(row) for row in constructor["files"]]
assert len(constructor_checks) == 6
program_check = check({
    "path": "problems/2017-B4/notes/coordinator-dimension-induction-program-v1.md",
    "sha256": "b499899787f8d8607ba030ec21173451267ea0b1dd6d419481a548a103c2f291",
})

prior_path = "problems/2025-B4/reviews/diagonal-firstcase-review-1-manifest-v1.json"
prior_fp = check({"path": prior_path,
                  "sha256": "5814bbb9ad233b0384ab7be74549f6b5333bb5b76950833515029a7c0478853f"})
prior = read_json(prior_path)
prior_checks = [check(row) for row in prior["records"]]
prior_validation = read_json("problems/2025-B4/reviews/diagonal-firstcase-review-1-input-validation-v1.json")
older = []
for packet in prior_validation["older_own_packets"]:
    older.append({"manifest": check(packet["manifest"]),
                  "checks": [check(row) for row in packet["checks"]]})
assert len(older) == 27
older.append({"manifest": prior_fp, "checks": prior_checks})

validation_path = create_json("input-validation-v1.json", {
    "checked_at_utc": now,
    "constructor_manifest": constructor_fp,
    "constructor_records": constructor_checks,
    "all_six_constructor_records_unchanged": True,
    "GE_program_read_as_definition_not_theorem": program_check,
    "older_own_packets": older,
    "all_twenty_eight_older_own_packets_unchanged": True,
    "new_peer_SP_review_or_findings_read": False,
    "RM1_used_as_exact_conditional_dependency": True,
    "auxiliary_arbitrary_window_bound_used": False,
    "UR_D_or_H_imported": False,
    "own_uniform_strict_construction_used": False,
    "mathematical_program_enumeration_or_CAS": False,
})
output_path = create_json("freeze-output-v1.json", {
    "frozen_at_utc": now,
    "constructor_records_checked": 6,
    "additional_GE_definition_checked": 1,
    "older_own_packets_checked": 28,
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
    "status": "initially blind whole review; no substantive defect found; exact conditional RM1 scope",
    "reviewer": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_sha256": "c0d51d61f110cf5a190344403d346940b06b95a6d1880c6c725d241c92c397b4",
    "whole_claims": ["SP1", "SP2", "SP3"],
    "per_inference_ledger_rows": 25,
    "substantive_objections": [],
    "required_author_repairs": [],
    "RM1_used_as_exact_conditional_dependency": True,
    "UR_D_or_H_claim": False,
    "peer_findings_read_before_freeze": False,
    "mathematical_program_enumeration_or_CAS": False,
    "candidate_or_shared_changes": False,
    "git_operations": False,
    "spawned_agents": False,
    "latest_weekly_total_used_percent": 28,
    "weekly_window_minutes": 10080,
    "weekly_reset_unix": 1792745187,
    "total_used_ceiling_percent": 90,
    "command": "python3 problems/2017-B4/reviews/single-pair-allD-review-1-freeze-v1.py",
    "records": [fingerprint(path) for path in record_paths],
})
print(json.dumps({"frozen_at_utc": now,
                  "manifest": fingerprint(manifest_path),
                  "records": len(record_paths),
                  "constructor_records_checked": 6,
                  "older_own_packets_checked": 28}, indent=2))
