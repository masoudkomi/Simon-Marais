"""One-time administrative freeze of candidate G1/G2/C1/C2/W; no mathematics."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2021-B4/notes/reasoning-return-r3-"

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

sources_path = PREFIX + "sources-v1.json"
sources = json.loads((ROOT / sources_path).read_text())
input_checks = [verify(entry) for entry in sources["accepted_local_inputs"]]
cache_checks = []
for entry in sources["primary_sources"]:
    actual = fingerprint(entry["existing_ignored_cache"])
    assert actual["sha256"] == entry["existing_cache_sha256"]
    cache_checks.append(actual)

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
]
older_checks = []
for path in older_paths:
    manifest = json.loads((ROOT / path).read_text())
    older_checks.append({"manifest": fingerprint(path), "checks": [verify(entry) for entry in manifest["records"]]})
assert older_checks[-1]["manifest"]["sha256"] == "64a4b7273b493c64bd12c27f4486c30482fd821f5668b2975ab753968c842602"

now = datetime.now(timezone.utc).isoformat()
validation_path = PREFIX + "input-validation-v1.json"
create_json(validation_path, {
    "checked_at_utc": now,
    "accepted_inputs_and_scope_records": input_checks,
    "all_supplied_accepted_hashes_match": True,
    "existing_primary_caches": cache_checks,
    "fresh_web_viewer_cache_byte_identity_claimed": False,
    "older_own_packets": older_checks,
    "all_eleven_older_packets_unchanged": True,
    "no_J16_or_three_value_certificate_rerun": True,
    "metadata_only": True,
})
output_path = PREFIX + "freeze-output-v1.json"
create_json(output_path, {
    "frozen_at_utc": now,
    "status": "candidate proof - unverified",
    "claims": ["G1", "G2", "C1", "C2", "W"],
    "two_fresh_nonconstructor_whole_audits_required": True,
    "complete_J15_mask_or_degree20_excluded": False,
    "two_prime_exclusion_or_novelty_claimed": False,
    "mathematical_computation_enumeration_or_CAS": False,
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
    "claims": ["G1 global unrecycled factor barrier", "G2 global factor dichotomy",
        "C1 weighted-even collision criterion", "C2 sixth-witness square-class alternatives",
        "W higher fourth-rational-witness constraint"],
    "two_fresh_independent_nonconstructor_whole_audits_required": True,
    "no_complete_mask_degree20_annual_solution_or_novelty": True,
    "no_two_prime_exclusion": True,
    "mathematical_enumeration_Hensel_table_or_CAS": False,
    "accepted_inputs_primary_caches_and_eleven_older_own_packets_match": True,
    "latest_weekly_total_used_percent": 22,
    "weekly_reset_unix": 1792745187, "total_used_ceiling_percent": 90,
    "command": ".venv/bin/python " + PREFIX + "freeze-v1.py",
    "records": [fingerprint(path) for path in records],
})
print(json.dumps({"frozen_at_utc": now,
    "candidate": fingerprint(PREFIX + "candidate-v1.md"),
    "manifest": fingerprint(manifest_path),
    "status": "candidate proof - unverified",
    "two_fresh_nonconstructor_whole_audits_required": True,
    "all_older_records_unchanged": True}, indent=2))
