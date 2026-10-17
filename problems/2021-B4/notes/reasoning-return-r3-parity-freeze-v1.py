"""One-time parity-projection metadata freeze; no mathematical computation."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2021-B4/notes/reasoning-return-r3-parity-"
COLLISION = "problems/2021-B4/notes/reasoning-return-r3-collision-"

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

sources = json.loads((ROOT / (PREFIX + "sources-v1.json")).read_text())
input_checks = [verify(entry) for entry in sources["inputs"]]
collision_manifest_check = verify({
    "path": COLLISION + "manifest-v1.json",
    "sha256": "9810f2f82a9467f8d682204152e8893f7ba856827260b109b1031d6887c0a62d",
})
collision_manifest = json.loads((ROOT / collision_manifest_check["path"]).read_text())
collision_record_checks = [verify(entry) for entry in collision_manifest["records"]]
collision_validation = json.loads((ROOT / (COLLISION + "input-validation-v1.json")).read_text())
older_checks = []
for entry in collision_validation["older_own_packets"]:
    manifest_check = verify(entry["manifest"])
    manifest = json.loads((ROOT / entry["manifest"]["path"]).read_text())
    older_checks.append({
        "manifest": manifest_check,
        "checks": [verify(record) for record in manifest["records"]],
    })
older_checks.append({"manifest": collision_manifest_check, "checks": collision_record_checks})
assert len(older_checks) == 14
source_cache_checks = [verify({
    "path": entry["existing_ignored_cache"],
    "sha256": entry["existing_cache_sha256"],
}) for entry in sources["primary_sources"] if "existing_ignored_cache" in entry]
now = datetime.now(timezone.utc).isoformat()
create_json(PREFIX + "input-validation-v1.json", {
    "checked_at_utc": now, "accepted_inputs": input_checks,
    "older_own_packets": older_checks,
    "existing_ignored_source_cache_checks": source_cache_checks,
    "all_fourteen_older_own_packets_unchanged": True,
    "earlier_unreviewed_packets_are_proof_dependencies": False,
    "metadata_only": True,
})
create_json(PREFIX + "freeze-output-v1.json", {
    "frozen_at_utc": now, "status": "candidate proof - unverified",
    "claims": ["PP1 parity projection and SAME-support descent endpoint congruences",
               "PP2 repeated-ladder noncenter-H18 application"],
    "joint_nonvanishing_target_proved_or_asserted_true": False,
    "rational_lift_support_classification_mask_or_degree20_solution_claimed": False,
    "two_fresh_independent_nonconstructor_whole_audits_required": True,
    "mathematical_program_support_enumeration_CAS_or_digit_tree": False,
    "accepted_inputs_and_all_fourteen_older_own_packets_match": True,
})
records = [PREFIX + suffix for suffix in (
    "candidate-v1.md", "researchlog-v1.md", "sources-v1.json", "freeze-v1.py",
    "input-validation-v1.json", "freeze-output-v1.json",
)]
manifest_path = PREFIX + "manifest-v1.json"
create_json(manifest_path, {
    "frozen_at_utc": now, "status": "candidate proof - unverified",
    "constructor": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "claims": ["PP1", "PP2"],
    "two_fresh_independent_nonconstructor_whole_audits_required": True,
    "earlier_unreviewed_packets_are_proof_dependencies": False,
    "joint_nonvanishing_support_classification_rational_lift_or_degree20_not_claimed": True,
    "mathematical_program_support_enumeration_CAS_or_digit_tree": False,
    "accepted_inputs_and_fourteen_older_own_packets_match": True,
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
    "two_fresh_nonconstructor_whole_audits_required": True,
    "all_fourteen_older_packets_unchanged": True,
}, indent=2))

