"""One-time metadata freeze of the blind DG1/DG2 review; no mathematics."""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/reviews/directed-geodesics-review-2-"


def fingerprint(relative):
    data = (ROOT / relative).read_bytes()
    return {"path": relative, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def create_json(relative, data):
    if not relative.startswith(PREFIX):
        raise RuntimeError("Write outside assigned review prefix")
    with (ROOT / relative).open("x", encoding="utf-8") as stream:
        json.dump(data, stream, indent=2)
        stream.write("\n")


candidate_path = "problems/2017-B4/notes/coordinator-directed-geodesics-candidate-v1.md"
candidate = fingerprint(candidate_path)
assert candidate["sha256"] == "0fe9e72b07d12d7a5e417e14a56fec06191ea7f76a9f8787ea533cdd9824bcb6"
constructor_manifest_path = "problems/2017-B4/notes/coordinator-directed-geodesics-freeze-v1.json"
constructor_manifest = json.loads((ROOT / constructor_manifest_path).read_text())
input_checks = []
for expected in constructor_manifest["artifacts"]:
    actual = fingerprint(expected["path"])
    actual["matches"] = all(actual[key] == expected[key] for key in ("bytes", "sha256"))
    assert actual["matches"]
    input_checks.append(actual)

old_manifest_paths = [
    "problems/2021-B4/reviews/reasoning-J15-review-2-manifest.json",
    "problems/2024-B4/notes/structural-reasoning-r2-manifest-v1.json",
    "problems/2017-B4/reviews/fixedD-structural-review-1-manifest-v1.json",
    "problems/2024-B4/notes/divisor-reasoning-r2-manifest-v1.json",
]
old_checks = []
for path in old_manifest_paths:
    manifest = json.loads((ROOT / path).read_text())
    checks = []
    for expected in manifest["records"]:
        actual = fingerprint(expected["path"])
        actual["matches"] = all(actual[key] == expected[key] for key in ("bytes", "sha256"))
        assert actual["matches"], expected["path"]
        checks.append(actual)
    old_checks.append({"manifest": fingerprint(path), "all_records_match": True, "checks": checks})
assert old_checks[-1]["manifest"]["sha256"] == "76143ab6f93a41f0fe5c3db8088e184f41c0159c8d61b089e0bdb66c3477b971"

now = datetime.now(timezone.utc).isoformat()
validation_path = PREFIX + "input-validation-v1.json"
create_json(validation_path, {
    "checked_at_utc": now,
    "candidate": candidate,
    "constructor_manifest": fingerprint(constructor_manifest_path),
    "constructor_manifest_all_entries_match": True,
    "input_checks": input_checks,
    "local_dependency_fingerprints": [fingerprint(path) for path in (
        "AGENTS.md",
        "problems/2017-B4/proofs/reviewed-direction-coarsening-v1.1.md",
    )],
    "older_frozen_packets": old_checks,
    "older_frozen_packets_unchanged": True,
    "metadata_only": True,
})

output_path = PREFIX + "freeze-output-v1.json"
create_json(output_path, {
    "frozen_at_utc": now,
    "initial_blind_whole_audit_complete": True,
    "peer_DG_findings_read": False,
    "substantive_objections": 0,
    "repair_requested": False,
    "candidate_unchanged": True,
    "older_frozen_packets_unchanged": True,
    "H_or_annulus_claim_audited": False,
    "mathematical_computation_or_CAS": False,
})

record_paths = [PREFIX + suffix for suffix in (
    "initial-v1.md", "issues-v1.json", "sources-v1.json",
    "freeze-v1.py", "input-validation-v1.json", "freeze-output-v1.json",
)]
manifest = {
    "status": "initial blind whole DG1/DG2 audit complete; no reviewer promotion",
    "frozen_at_utc": now,
    "reviewer": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_sha256": candidate["sha256"],
    "nonconstructor": True,
    "disk_adaptation_contribution": False,
    "no_peer_DG_review_or_findings_read_before_freeze": True,
    "whole_reconstruction": True,
    "primary_Lemma_2_2_definition_and_complete_proof_read": True,
    "substantive_objections": 0,
    "repair_requested": False,
    "no_closed_annulus_or_H_acceptance": True,
    "candidate_and_older_packets_unchanged": True,
    "mathematical_enumeration_or_CAS": False,
    "latest_weekly_total_used_percent": 20,
    "weekly_reset_unix": 1792745187,
    "command": ".venv/bin/python " + PREFIX + "freeze-v1.py",
    "records": [fingerprint(path) for path in record_paths],
}
manifest_path = PREFIX + "manifest-v1.json"
create_json(manifest_path, manifest)
print(json.dumps({
    "frozen_at_utc": now,
    "report": fingerprint(PREFIX + "initial-v1.md"),
    "manifest": fingerprint(manifest_path),
    "substantive_objections": 0,
    "candidate_and_older_packets_unchanged": True,
}, indent=2))
