"""One-time residual-barrier metadata freeze; no mathematical computation."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2021-B4/notes/reasoning-return-r3-parity-barrier-"
PREVIOUS = "problems/2021-B4/notes/reasoning-return-r3-sparse-descent-"

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

previous_manifest_check = verify({
    "path": PREVIOUS + "manifest-v1.json",
    "sha256": "6107660c9fadd8394b119cfa92c1fa9f027a163ad00a61ae58e6728d4ea643d5",
})
previous_manifest = json.loads((ROOT / previous_manifest_check["path"]).read_text())
previous_record_checks = [verify(entry) for entry in previous_manifest["records"]]
previous_validation = json.loads((ROOT / (PREVIOUS + "input-validation-v1.json")).read_text())
older_checks = []
for entry in previous_validation["older_own_packets"]:
    manifest_check = verify(entry["manifest"])
    manifest = json.loads((ROOT / entry["manifest"]["path"]).read_text())
    older_checks.append({
        "manifest": manifest_check,
        "checks": [verify(record) for record in manifest["records"]],
    })
older_checks.append({"manifest": previous_manifest_check, "checks": previous_record_checks})
assert len(older_checks) == 16
now = datetime.now(timezone.utc).isoformat()
create_json(PREFIX + "input-validation-v1.json", {
    "checked_at_utc": now, "older_own_packets": older_checks,
    "all_sixteen_older_own_packets_unchanged": True,
    "earlier_unreviewed_candidates_used_as_accepted_theorems": False,
    "finite_field_cover_verified_in_candidate_by_explicit_hand_equations": True,
    "metadata_only": True,
})
create_json(PREFIX + "freeze-output-v1.json", {
    "frozen_at_utc": now, "status": "candidate proof - unverified",
    "claim": "PB1 explicit CA17/F19 residual first-endpoint barrier, second endpoint fails",
    "original_degree20_model_rational_lift_or_counterexample_claimed": False,
    "two_fresh_independent_nonconstructor_audits_required": True,
    "mathematical_program_support_enumeration_CAS_or_digit_tree": False,
    "all_sixteen_older_own_packets_match": True,
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
    "claims": ["PB1"],
    "two_fresh_independent_nonconstructor_audits_required": True,
    "earlier_unreviewed_candidates_are_accepted_dependencies": False,
    "no_original_degree20_model_rational_lift_or_counterexample": True,
    "mathematical_program_support_enumeration_CAS_or_digit_tree": False,
    "all_sixteen_older_own_packets_match": True,
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
    "all_sixteen_older_packets_unchanged": True,
}, indent=2))

