"""One-time sparse-descent metadata freeze; no mathematical computation."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2021-B4/notes/reasoning-return-r3-sparse-descent-"
PARITY = "problems/2021-B4/notes/reasoning-return-r3-parity-"

def fingerprint(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}

def verify(expected):
    actual = fingerprint(expected["path"])
    for key in ("bytes", "sha256"):
        if key in expected:
            assert actual[key] == expected[key], expected["path"]
    return dict(actual, matches=True)

def create_json(path, data):
    assert path.startswith(PREFIX)
    with (ROOT / path).open("x", encoding="utf-8") as stream:
        json.dump(data, stream, indent=2)
        stream.write("\n")

parity_manifest_check = verify({
    "path": PARITY + "manifest-v1.json",
    "sha256": "bae5a876437f34347232c7e66f0360166748b3d15a7a93073cc3d76646642d3c",
})
parity_manifest = json.loads((ROOT / parity_manifest_check["path"]).read_text())
parity_record_checks = [verify(entry) for entry in parity_manifest["records"]]
parity_validation = json.loads((ROOT / (PARITY + "input-validation-v1.json")).read_text())
older_checks = []
for entry in parity_validation["older_own_packets"]:
    manifest_check = verify(entry["manifest"])
    manifest = json.loads((ROOT / entry["manifest"]["path"]).read_text())
    older_checks.append({
        "manifest": manifest_check,
        "checks": [verify(record) for record in manifest["records"]],
    })
older_checks.append({"manifest": parity_manifest_check, "checks": parity_record_checks})
assert len(older_checks) == 15
now = datetime.now(timezone.utc).isoformat()
create_json(PREFIX + "input-validation-v1.json", {
    "checked_at_utc": now, "older_own_packets": older_checks,
    "all_fifteen_older_own_packets_unchanged": True,
    "parity_PP1_used_as_accepted_theorem": False,
    "arithmetic_hypotheses_explicit_in_SD1": True,
    "metadata_only": True,
})
create_json(PREFIX + "freeze-output-v1.json", {
    "frozen_at_utc": now, "status": "candidate proof - unverified",
    "claim": "SD1 joint odd-support descent endpoint equations require at least four support indices",
    "larger_support_joint_nonvanishing_or_2021_branch_exclusion_claimed": False,
    "two_fresh_independent_nonconstructor_audits_required": True,
    "mathematical_program_support_enumeration_CAS_or_digit_tree": False,
    "all_fifteen_older_own_packets_match": True,
})
records = [PREFIX + suffix for suffix in (
    "candidate-v1.md", "sources-log-v1.md", "freeze-v1.py",
    "input-validation-v1.json", "freeze-output-v1.json",
)]
manifest_path = PREFIX + "manifest-v1.json"
create_json(manifest_path, {
    "frozen_at_utc": now, "status": "candidate proof - unverified",
    "constructor": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "claims": ["SD1"],
    "two_fresh_independent_nonconstructor_audits_required": True,
    "parity_PP1_is_an_accepted_dependency": False,
    "no_larger_support_classification_or_degree20_solution": True,
    "mathematical_program_support_enumeration_CAS_or_digit_tree": False,
    "all_fifteen_older_own_packets_match": True,
    "latest_weekly_total_used_percent": 23,
    "weekly_reset_unix": 1792745187, "total_used_ceiling_percent": 90,
    "command": ".venv/bin/python " + PREFIX + "freeze-v1.py",
    "records": [fingerprint(path) for path in records],
})
print(json.dumps({
    "frozen_at_utc": now,
    "candidate": fingerprint(PREFIX + "candidate-v1.md"),
    "manifest": fingerprint(manifest_path),
    "status": "candidate proof - unverified",
    "two_fresh_nonconstructor_audits_required": True,
    "all_fifteen_older_packets_unchanged": True,
}, indent=2))

