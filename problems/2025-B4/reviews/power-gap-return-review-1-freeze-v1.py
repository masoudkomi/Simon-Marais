"""One-time blind-review integrity freeze; no mathematical calculation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2025-B4/reviews/power-gap-return-review-1-"


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
constructor_path = "problems/2025-B4/notes/coordinator-power-gap-return-freeze-v1.json"
constructor_fp = check({"path": constructor_path,
                        "sha256": "b6612a8286379c12340df3686421c52b3aedb1a6926bd5fa0c9d0a09d88cd9d3"})
constructor = read_json(constructor_path)
constructor_checks = [check(row) for row in constructor["files"]]
assert len(constructor_checks) == 10

prior_path = "problems/2017-B4/reviews/rank-mesh-review-1-manifest-v1.json"
prior_fp = check({"path": prior_path,
                  "sha256": "e76dde7938e9e5a7e48ba6b8eea6cee6e4fa695cf898dcc44973df3d25aeb328"})
prior = read_json(prior_path)
prior_checks = [check(row) for row in prior["records"]]
prior_validation = read_json("problems/2017-B4/reviews/rank-mesh-review-1-input-validation-v1.json")
older = []
for packet in prior_validation["older_own_packets"]:
    older.append({"manifest": check(packet["manifest"]),
                  "checks": [check(row) for row in packet["checks"]]})
assert len(older) == 21
older.append({"manifest": prior_fp, "checks": prior_checks})

validation_path = create_json("input-validation-v1.json", {
    "checked_at_utc": now,
    "constructor_manifest": constructor_fp,
    "constructor_and_input_records": constructor_checks,
    "all_ten_constructor_and_input_records_unchanged": True,
    "older_own_packets": older,
    "all_twenty_two_older_own_packets_unchanged": True,
    "new_peer_PG_review_or_findings_read": False,
    "mathematical_computation_enumeration_or_CAS": False,
    "python_other_than_freeze": "read-only source-text extraction from primary cached PDF",
    "public_primary_read": {
        "bennett_levin_url": "https://personal.math.ubc.ca/~bennett/BeLe-Mona-2015.pdf",
        "bennett_levin_scope": "full Equation1, Proposition1, Theorem1 and qualifications printedpages15-17; not entire external proof reconstruction",
        "bugeaud_mihailescu_scope": "complete seven-page cached primary PDF text independently extracted with bundled pypdf",
        "independent_binary_retrieval_hash_claimed": False,
    },
})
output_path = create_json("freeze-output-v1.json", {
    "frozen_at_utc": now,
    "constructor_records_checked": 10,
    "older_own_packets_checked": 22,
    "all_fingerprints_match": True,
    "open_substantive_issues": [],
    "whole_initial_review_complete_before_disclosure": True,
    "PG1_PG2_PG3_elementary_reconstruction": "pass",
    "PG4_attributed_published_input_corollary": "pass with explicit external-theorem boundary",
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
    "candidate_sha256": "233e00fec364f6f865179c6e3f810173d92b2cd0f5e8a59279e63b605a5d05fb",
    "source_note_sha256": "ae388dc3e6030dcc01b61fe000ff5398b6f3958df252fd9188759e90a1078f60",
    "whole_claims": ["PG1", "PG2", "PG3", "PG4 with attributed full published theorem inputs"],
    "per_inference_ledger_rows": 28,
    "substantive_objections": [],
    "required_author_repairs": [],
    "external_theorem_full_proof_reconstructed": False,
    "peer_findings_read_before_freeze": False,
    "mathematical_program_enumeration_or_CAS": False,
    "candidate_or_shared_changes": False,
    "git_operations": False,
    "spawned_agents": False,
    "latest_weekly_total_used_percent": 25,
    "weekly_window_minutes": 10080,
    "weekly_reset_unix": 1792745187,
    "total_used_ceiling_percent": 90,
    "command": "python3 problems/2025-B4/reviews/power-gap-return-review-1-freeze-v1.py",
    "records": [fingerprint(path) for path in record_paths],
})
print(json.dumps({"frozen_at_utc": now,
                  "manifest": fingerprint(manifest_path),
                  "records": len(record_paths),
                  "constructor_records_checked": 10,
                  "older_own_packets_checked": 22}, indent=2))
