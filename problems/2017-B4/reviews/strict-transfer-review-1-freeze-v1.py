"""One-time administrative review freeze; no mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/reviews/strict-transfer-review-1-"


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
known = [
    ("problems/2017-B4/notes/coordinator-strict-transfer-candidate-v1.md",
     "a19f8e66cb0fb810098eb209a47e73ecbb26e1d43316c13fa64bb5f743c8c3f1"),
    ("problems/2017-B4/notes/coordinator-strict-transfer-freeze-v1.json",
     "a1b47d24cd01e032e97d11cfc917d787518f53d1902b71ddbeece24be428410e"),
    ("problems/2017-B4/notes/annulus-reasoning-r1-candidate-v1.1.md",
     "c6da61f229ffa72dd830cd40132969717a395e3744b6d775cbe83a32bdd3747c"),
    ("problems/2017-B4/notes/coordinator-lens-cutting-candidate-v1.md",
     "1937c12d4cf9c9e2d7b4f713566a77e1b32e1a88ea0c55f09ae7e43870b8482f"),
    ("problems/2017-B4/proofs/reviewed-annulus-v1.2.md",
     "51c02b22a36705c736e4debefcfde0afbc1b2678a8d6092213d8ed00e6a75baf"),
    ("problems/2017-B4/proofs/reviewed-lens-cutting-v1.1.md",
     "81f175e2a0f10665e9228d18885180e91b4db6167001584182d9de4b9cb437fc"),
    ("problems/2017-B4/proofs/reviewed-directed-geodesics-v1.1.md",
     "061ae1749e938aad68f1824ab5f33583a3a1c58e556bd62649309c7cb12da9aa"),
    ("problems/2017-B4/proofs/reviewed-fixedD-structural-v1.2.md",
     "421dc271ed65831e3aa70057a0d74c4d999ba8249dfa2b99066dfdc298f86868"),
]
checks = [check({"path": path, "sha256": digest}) for path, digest in known]
scope_paths = [
    "AGENTS.md", "problems/2017-B4/statement.md",
    "problems/2017-B4/reviews/annulus-acceptance.md",
    "problems/2017-B4/reviews/annulus-acceptance.json",
    "problems/2017-B4/reviews/annulus-acceptance-integrity.json",
    "problems/2017-B4/reviews/lens-cutting-acceptance.md",
    "problems/2017-B4/reviews/lens-cutting-acceptance.json",
    "problems/2017-B4/reviews/lens-cutting-acceptance-integrity.json",
]
body_checks = []
for accepted, body in [
    ("problems/2017-B4/proofs/reviewed-annulus-v1.2.md",
     "problems/2017-B4/notes/annulus-reasoning-r1-candidate-v1.1.md"),
    ("problems/2017-B4/proofs/reviewed-lens-cutting-v1.1.md",
     "problems/2017-B4/notes/coordinator-lens-cutting-candidate-v1.md"),
]:
    assert (ROOT / accepted).read_bytes().endswith((ROOT / body).read_bytes())
    body_checks.append({"accepted": accepted, "frozen_body": body,
                        "accepted_ends_with_exact_frozen_body": True})

prior_path = "problems/2019-B4/reviews/moment-tail-review-1-manifest-v1.json"
prior_fp = check({"path": prior_path,
                  "sha256": "315713782cd82c0db0ebb46c623aad2714fd6ae60d1f1e7ec807d0300b3e0fda"})
prior = read_json(prior_path)
prior_checks = [check(row) for row in prior["records"]]
prior_validation = read_json("problems/2019-B4/reviews/moment-tail-review-1-input-validation-v1.json")
older = []
for packet in prior_validation["older_own_packets"]:
    older.append({"manifest": check(packet["manifest"]),
                  "checks": [check(row) for row in packet["checks"]]})
assert len(older) == 19
older.append({"manifest": prior_fp, "checks": prior_checks})

validation_path = create_json("input-validation-v1.json", {
    "checked_at_utc": now,
    "assigned_and_frozen_input_checks": checks,
    "acceptance_and_scope_records": [fingerprint(path) for path in scope_paths],
    "accepted_body_identity_checks": body_checks,
    "older_own_packets": older,
    "all_twenty_older_own_packets_unchanged": True,
    "new_peer_strict_transfer_review_or_findings_read": False,
    "rank_mesh_packet_read_before_this_freeze": False,
    "metadata_only": True,
})
output_path = create_json("freeze-output-v1.json", {
    "frozen_at_utc": now,
    "known_fingerprint_checks": len(checks),
    "additional_scope_fingerprints": len(scope_paths),
    "exact_accepted_body_checks": 2,
    "older_own_packets_checked": 20,
    "all_fingerprints_match": True,
    "mathematical_program_enumeration_or_CAS": False,
    "candidate_or_shared_mutation": False,
    "git_operations": False,
})
record_paths = [PREFIX + name for name in [
    "initial.md", "issues.md", "source-checks.md", "freeze-v1.py",
]] + [validation_path, output_path]
manifest_path = create_json("manifest-v1.json", {
    "frozen_at_utc": now,
    "status": "independent initially blind whole review; scoped recommendation only; no promotion",
    "reviewer": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_sha256": "a19f8e66cb0fb810098eb209a47e73ecbb26e1d43316c13fa64bb5f743c8c3f1",
    "whole_claims": ["ST1", "ST2", "ST3", "all accepted dependency interfaces"],
    "substantive_objections": 0,
    "repair_requested": False,
    "peer_findings_read_before_freeze": False,
    "no_H_PR_or_uniform_strata_claim": True,
    "mathematical_program_enumeration_or_CAS": False,
    "candidate_or_shared_changes": False,
    "git_operations": False,
    "spawned_agents": False,
    "latest_weekly_total_used_percent": 24,
    "weekly_window_minutes": 10080,
    "weekly_reset_unix": 1792745187,
    "total_used_ceiling_percent": 90,
    "command": "python3 problems/2017-B4/reviews/strict-transfer-review-1-freeze-v1.py",
    "records": [fingerprint(path) for path in record_paths],
})
print(json.dumps({"frozen_at_utc": now,
                  "manifest": fingerprint(manifest_path),
                  "records": len(record_paths),
                  "older_own_packets_checked": 20}, indent=2))
