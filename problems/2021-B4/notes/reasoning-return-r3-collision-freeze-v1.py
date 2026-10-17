"""Administrative one-time collision-depth freeze; no mathematical computation."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2021-B4/notes/reasoning-return-r3-collision-"

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
previous_candidate_checks = [verify(entry) for entry in sources["earlier_unreviewed_packets_preserved"]]
source_cache_checks = [verify({
    "path": entry["existing_ignored_cache"],
    "sha256": entry["existing_cache_sha256"],
}) for entry in sources["primary_sources"] if "existing_ignored_cache" in entry]
older_paths = [
    "problems/2021-B4/reviews/reasoning-J15-review-2-manifest.json",
    "problems/2024-B4/notes/structural-reasoning-r2-manifest-v1.json",
    "problems/2017-B4/reviews/fixedD-structural-review-1-manifest-v1.json",
    "problems/2024-B4/notes/divisor-reasoning-r2-manifest-v1.json",
    "problems/2017-B4/reviews/directed-geodesics-review-2-manifest-v1.json",
    "problems/2017-B4/reviews/annulus-review-1-manifest-v1.json",
    "problems/2017-B4/reviews/fixedD-structural-review-1-reaudit-manifest-v1.1.json",
    "problems/2017-B4/reviews/lens-cutting-review-1-manifest-v1.json",
    "problems/2017-B4/reviews/annulus-review-1-reaudit-manifest-v1.1.json",
    "problems/2017-B4/reviews/clean-strata-review-1-manifest-v1.json",
    "problems/2017-B4/reviews/remainder-padding-review-1-manifest-v1.json",
    "problems/2021-B4/notes/reasoning-return-r3-manifest-v1.json",
    "problems/2021-B4/notes/reasoning-return-r3-mirror-manifest-v1.json",
]
older_checks = []
for path in older_paths:
    manifest = json.loads((ROOT / path).read_text())
    older_checks.append({
        "manifest": fingerprint(path),
        "checks": [verify(entry) for entry in manifest["records"]],
    })
assert older_checks[-2]["manifest"]["sha256"] == "a8f7aab114b19f3d317280cfcefac89ca9dc9ab7df6a51e58433b0f7451bb10e"
assert older_checks[-1]["manifest"]["sha256"] == "f3afbca0be5445f44cdc0946db3c3af897368e54ef9ece6c0cad4b9b9ef6edad"
now = datetime.now(timezone.utc).isoformat()
validation_path = PREFIX + "input-validation-v1.json"
create_json(validation_path, {
    "checked_at_utc": now, "accepted_inputs": input_checks,
    "older_own_packets": older_checks,
    "previous_candidate_checks": previous_candidate_checks,
    "existing_ignored_source_cache_checks": source_cache_checks,
    "all_thirteen_older_packets_unchanged": True,
    "earlier_unreviewed_candidates_used_as_theorems": False,
    "metadata_only": True,
})
output_path = PREFIX + "freeze-output-v1.json"
create_json(output_path, {
    "frozen_at_utc": now,
    "status": "candidate proof - unverified",
    "claims": ["RC1 Euler reflection displacement",
               "RC2 long-even-ladder repeated root forces nu1 and depth15or16; H18 notcenter",
               "RC3 two indispensable rational witnesses and exact coefficient zero"],
    "two_fresh_independent_nonconstructor_whole_audits_required": True,
    "complete_mask_repeated_branch_degree20_annual_solution_or_novelty_claimed": False,
    "mathematical_program_enumeration_CAS_or_digit_tree": False,
    "all_accepted_and_older_packets_unchanged": True,
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
    "claims": ["RC1", "RC2", "RC3"],
    "two_fresh_independent_nonconstructor_whole_audits_required": True,
    "earlier_unreviewed_packets_are_proof_dependencies": False,
    "no_complete_mask_repeated_branch_degree20_annual_solution_or_novelty": True,
    "mathematical_program_enumeration_CAS_or_digit_tree": False,
    "accepted_inputs_and_thirteen_older_own_packets_match": True,
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
    "all_older_records_unchanged": True,
}, indent=2))

