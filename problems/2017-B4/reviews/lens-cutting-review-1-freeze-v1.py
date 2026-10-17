"""One-time metadata freeze of the initially blind whole CUT audit; no mathematics."""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/reviews/lens-cutting-review-1-"


def fingerprint(relative):
    data = (ROOT / relative).read_bytes()
    return {"path": relative, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def verify(expected):
    actual = fingerprint(expected["path"])
    actual["matches"] = all(actual[key] == expected[key] for key in ("bytes", "sha256"))
    assert actual["matches"], expected["path"]
    return actual


def create_json(relative, data):
    if not relative.startswith(PREFIX):
        raise RuntimeError("Write outside assigned CUT review prefix")
    with (ROOT / relative).open("x", encoding="utf-8") as stream:
        json.dump(data, stream, indent=2)
        stream.write("\n")


constructor_path = "problems/2017-B4/notes/coordinator-lens-cutting-freeze-v1.json"
constructor = json.loads((ROOT / constructor_path).read_text())
input_checks = [verify(expected) for expected in constructor["artifacts"]]
candidate = input_checks[0]
assert candidate["sha256"] == "1937c12d4cf9c9e2d7b4f713566a77e1b32e1a88ea0c55f09ae7e43870b8482f"
dg_path = "problems/2017-B4/proofs/reviewed-directed-geodesics-v1.1.md"
dg = fingerprint(dg_path)
assert dg["sha256"] == "061ae1749e938aad68f1824ab5f33583a3a1c58e556bd62649309c7cb12da9aa"
dg_acceptance_path = "problems/2017-B4/reviews/directed-geodesics-acceptance.json"
dg_acceptance = json.loads((ROOT / dg_acceptance_path).read_text())
assert dg_acceptance["accepted_exposition"]["path"] == dg_path
assert dg_acceptance["accepted_exposition"]["sha256"] == dg["sha256"]

older_paths = [
    "problems/2021-B4/reviews/reasoning-J15-review-2-manifest.json",
    "problems/2024-B4/notes/structural-reasoning-r2-manifest-v1.json",
    "problems/2017-B4/reviews/fixedD-structural-review-1-manifest-v1.json",
    "problems/2024-B4/notes/divisor-reasoning-r2-manifest-v1.json",
    "problems/2017-B4/reviews/directed-geodesics-review-2-manifest-v1.json",
    "problems/2017-B4/reviews/annulus-review-1-manifest-v1.json",
    "problems/2017-B4/reviews/fixedD-structural-review-1-reaudit-manifest-v1.1.json",
]
older_checks = []
for path in older_paths:
    manifest = json.loads((ROOT / path).read_text())
    older_checks.append({
        "manifest": fingerprint(path),
        "all_records_match": True,
        "checks": [verify(expected) for expected in manifest["records"]],
    })
assert older_checks[-1]["manifest"]["sha256"] == "ffef08f8b96909ddba3b8805d103917456e21c75c058712b2ed017e00dabbcfc"

now = datetime.now(timezone.utc).isoformat()
validation_path = PREFIX + "input-validation-v1.json"
create_json(validation_path, {
    "checked_at_utc": now,
    "constructor_manifest": fingerprint(constructor_path),
    "all_constructor_entries_match": True,
    "input_checks": input_checks,
    "accepted_dependencies": [dg],
    "local_dependency_fingerprints": [fingerprint(path) for path in (
        "AGENTS.md",
        "problems/2017-B4/reviews/directed-geodesics-acceptance.md",
        dg_acceptance_path,
    )],
    "DG_exposition_matches_acceptance": True,
    "older_own_packets": older_checks,
    "all_older_own_records_unchanged": True,
    "peer_CUT_contents_read": False,
    "metadata_only": True,
})
output_path = PREFIX + "freeze-output-v1.json"
create_json(output_path, {
    "frozen_at_utc": now,
    "initial_blind_whole_CUT1_CUT2_audit_complete": True,
    "substantive_objections": 0,
    "repair_requested": False,
    "no_peer_CUT_findings_read": True,
    "candidate_and_accepted_dependency_unchanged": True,
    "all_older_own_records_unchanged": True,
    "annulus_EAI_PR_H_or_full_solution_accepted": False,
    "mathematical_computation_or_CAS": False,
})
record_paths = [PREFIX + suffix for suffix in (
    "initial-v1.md", "issues-v1.json", "sources-v1.json",
    "freeze-v1.py", "input-validation-v1.json", "freeze-output-v1.json",
)]
manifest_path = PREFIX + "manifest-v1.json"
create_json(manifest_path, {
    "status": "initial blind whole CUT1/CUT2 audit complete; no substantive objection; no reviewer promotion",
    "frozen_at_utc": now,
    "reviewer": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_sha256": candidate["sha256"],
    "accepted_DG_exposition_sha256": dg["sha256"],
    "nonconstructor": True,
    "whole_reconstruction": True,
    "no_peer_CUT_findings_read_before_freeze": True,
    "substantive_objections": 0,
    "repair_requested": False,
    "all_older_records_unchanged": True,
    "no_annulus_EAI_PR_H_or_full_solution_acceptance": True,
    "mathematical_enumeration_or_CAS": False,
    "latest_weekly_total_used_percent": 20,
    "weekly_reset_unix": 1792745187,
    "command": ".venv/bin/python " + PREFIX + "freeze-v1.py",
    "records": [fingerprint(path) for path in record_paths],
})
print(json.dumps({
    "frozen_at_utc": now,
    "report": fingerprint(PREFIX + "initial-v1.md"),
    "manifest": fingerprint(manifest_path),
    "substantive_objections": 0,
    "all_older_records_unchanged": True,
}, indent=2))
