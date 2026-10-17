"""One-time blind-review integrity freeze; no mathematical calculation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2021-B4/reviews/odd-support-exclusion-review-1-"


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
constructor_path = "problems/2021-B4/notes/coordinator-odd-support-exclusion-freeze-v1.json"
constructor_fp = check({"path": constructor_path,
                        "sha256": "337a43225bd6637d666bc992738a49afab8e7b569f526281add45564ab17b592"})
constructor = read_json(constructor_path)
constructor_checks = [check(row) for row in constructor["files"]]
assert len(constructor_checks) == 13

prior_path = "problems/2025-B4/reviews/power-gap-return-review-1-manifest-v1.json"
prior_fp = check({"path": prior_path,
                  "sha256": "dc12f0e8b0a8caef4ccf546e80206d18605996abe2b56cd282db342905aa9487"})
prior = read_json(prior_path)
prior_checks = [check(row) for row in prior["records"]]
prior_validation = read_json("problems/2025-B4/reviews/power-gap-return-review-1-input-validation-v1.json")
older = []
for packet in prior_validation["older_own_packets"]:
    older.append({"manifest": check(packet["manifest"]),
                  "checks": [check(row) for row in packet["checks"]]})
assert len(older) == 22
older.append({"manifest": prior_fp, "checks": prior_checks})

validation_path = create_json("input-validation-v1.json", {
    "checked_at_utc": now,
    "constructor_manifest": constructor_fp,
    "constructor_and_input_records": constructor_checks,
    "all_thirteen_constructor_and_input_records_unchanged": True,
    "additional_inputs": [fingerprint(path) for path in [
        "AGENTS.md", "problems/2021-B4/statement.md",
        "problems/2021-B4/notes/reasoning-return-r3-parity-sources-v1.json",
    ]],
    "older_own_packets": older,
    "all_twenty_three_older_own_packets_unchanged": True,
    "new_peer_PN_review_or_findings_read": False,
    "accepted_dependency_authorship": "Reviewer constructed accepted PP1/PP2 and PB1; this review does not count as their independent audit",
    "new_PN_packet_construction_contribution": False,
    "constructor_arithmetic_program_or_output_read_for_proof": False,
    "constructor_program_executed": False,
    "mathematical_program_or_CAS": False,
    "finite_certificate": "all64 residues reconstructed by hand via prefix coefficient matrix and independent eight-column simplification",
    "public_primary_read": [
        "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf",
        "https://arxiv.org/pdf/1710.11033v2",
        "https://arxiv.org/pdf/2608.14726",
    ],
    "independent_binary_retrieval_hash_claimed": False,
})
output_path = create_json("freeze-output-v1.json", {
    "frozen_at_utc": now,
    "constructor_records_checked": 13,
    "older_own_packets_checked": 23,
    "all_fingerprints_match": True,
    "open_substantive_issues": [],
    "whole_initial_review_complete_before_disclosure": True,
    "PN1": "all64 cases and reduced coefficient vector pass",
    "PN2": "derivative and mod361 endpoint pass",
    "PN3_PN4": "pass in exact accepted PP1/PP2 scope",
    "candidate_or_shared_mutation": False,
    "git_operations": False,
})
record_paths = [PREFIX + name for name in [
    "initial.md", "issues.md", "source-checks.md", "freeze-v1.py",
]] + [validation_path, output_path]
manifest_path = create_json("manifest-v1.json", {
    "frozen_at_utc": now,
    "status": "initially blind whole review; no substantive defect found; no promotion",
    "reviewer": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_sha256": "a7845441df7725edc5d30e28f7b8f28c529b0b710168ad4b068d279582c1857c",
    "whole_claims": ["PN1", "PN2", "PN3", "PN4"],
    "per_inference_ledger_rows": 26,
    "substantive_objections": [],
    "required_author_repairs": [],
    "reviewer_constructed_accepted_dependencies": ["PP1", "PP2", "PB1"],
    "reviewer_constructed_new_PN_packet": False,
    "new_claim_finite_certificate_reconstructed": "all64 cases by hand",
    "peer_findings_read_before_freeze": False,
    "mathematical_program_or_CAS": False,
    "candidate_or_shared_changes": False,
    "git_operations": False,
    "spawned_agents": False,
    "latest_weekly_total_used_percent": 26,
    "weekly_window_minutes": 10080,
    "weekly_reset_unix": 1792745187,
    "total_used_ceiling_percent": 90,
    "command": "python3 problems/2021-B4/reviews/odd-support-exclusion-review-1-freeze-v1.py",
    "records": [fingerprint(path) for path in record_paths],
})
print(json.dumps({"frozen_at_utc": now,
                  "manifest": fingerprint(manifest_path),
                  "records": len(record_paths),
                  "constructor_records_checked": 13,
                  "older_own_packets_checked": 23}, indent=2))
