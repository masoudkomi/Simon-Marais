"""One-time metadata freeze of the blind fixed-D review; no mathematics."""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/reviews/fixedD-structural-review-1-"


def fingerprint(relative):
    data = (ROOT / relative).read_bytes()
    return {
        "path": relative,
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
    }


def write_new(relative, value):
    if not relative.startswith(PREFIX):
        raise RuntimeError("Attempt to write outside assigned review prefix")
    with (ROOT / relative).open("x", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


expected = {
    "problems/2017-B4/notes/fixedD-reasoning-r1-structural-candidate-v1.md":
        "c776e81d0fd44c0e8042ddc00a0d949966cdc106ba9b7e67486dc4d14a1b7d87",
    "problems/2017-B4/notes/fixedD-reasoning-r1-profile-reduction-v1.md":
        "973e8d7da034082b4416100d51650798ec3eb90e75cfd44106b5810dd9ec7e8d",
    "problems/2017-B4/notes/fixedD-reasoning-r1-sources-v1.json":
        "e33ef844964e5cdfa0420696c2ee08ab90600ac766b9d7aa3667e8776c7ac3c0",
}
input_records = []
for relative, wanted in expected.items():
    record = fingerprint(relative)
    record["expected_sha256"] = wanted
    record["matches"] = record["sha256"] == wanted
    if not record["matches"]:
        raise RuntimeError(f"Frozen candidate changed: {relative}")
    input_records.append(record)

constructor_manifest_path = "problems/2017-B4/notes/fixedD-reasoning-r1-freeze-v1.json"
constructor_manifest = json.loads((ROOT / constructor_manifest_path).read_text())
constructor_entries = []
for expected_entry in constructor_manifest["artifacts"]:
    actual = fingerprint(expected_entry["path"])
    actual["matches"] = all(
        actual[field] == expected_entry[field] for field in ("bytes", "sha256")
    )
    if not actual["matches"]:
        raise RuntimeError("Constructor manifest entry changed")
    constructor_entries.append(actual)

preserved_manifests = [
    "problems/2021-B4/reviews/reasoning-J15-review-2-manifest.json",
    "problems/2024-B4/notes/structural-reasoning-r2-manifest-v1.json",
]
preserved_checks = []
for relative in preserved_manifests:
    old_manifest = json.loads((ROOT / relative).read_text())
    checks = []
    for old_entry in old_manifest["records"]:
        actual = fingerprint(old_entry["path"])
        actual["matches"] = all(
            actual[field] == old_entry[field] for field in ("bytes", "sha256")
        )
        if not actual["matches"]:
            raise RuntimeError(f"Older frozen packet changed: {old_entry['path']}")
        checks.append(actual)
    preserved_checks.append({
        "manifest": fingerprint(relative),
        "all_records_unchanged": True,
        "checks": checks,
    })

dependency_paths = [
    "AGENTS.md",
    "problems/2017-B4/statement.md",
    "problems/2017-B4/reviews/coarsening-acceptance.md",
    "problems/2017-B4/proofs/reviewed-direction-coarsening-v1.1.md",
    constructor_manifest_path,
]
source_dependency = fingerprint("problems/2017-B4/reviews/coarsening-review-1-sources.json")
source_dependency["declared_sha256_matches"] = (
    source_dependency["sha256"] ==
    "5fec609c63f708dd1ca01d892803166b765e154e29fc821f2d13f967f08a1518"
)
if not source_dependency["declared_sha256_matches"]:
    raise RuntimeError("Constructor's prior source-record fingerprint changed")

now = datetime.now(timezone.utc).isoformat()
validation_path = PREFIX + "input-validation-v1.json"
write_new(validation_path, {
    "checked_at_utc": now,
    "candidate_input_records": input_records,
    "constructor_manifest_all_entries_match": True,
    "constructor_manifest_checks": constructor_entries,
    "dependency_records": [fingerprint(path) for path in dependency_paths],
    "constructor_prior_source_record_hash_only": source_dependency,
    "older_frozen_packets": preserved_checks,
    "metadata_only": True,
    "mathematical_enumeration_or_CAS": False,
})

output_path = PREFIX + "freeze-output-v1.json"
write_new(output_path, {
    "frozen_at_utc": now,
    "candidate_inputs_unchanged": True,
    "older_J15_and_2024_packets_unchanged": True,
    "blind_initial_report_complete": True,
    "peer_new_fixedD_reviews_read": False,
    "unresolved_substantive_objections_to_partial_claims": 0,
    "EAI_D_and_all_scale_recovery_remain_open": True,
    "H_proved": False,
    "mathematical_enumeration_or_CAS": False,
})

review_paths = [
    PREFIX + "initial-v1.md",
    PREFIX + "issues-v1.json",
    PREFIX + "sources-v1.json",
    PREFIX + "freeze-v1.py",
    validation_path,
    output_path,
]
manifest = {
    "status": "initial blind whole mathematical audit complete; no reviewer promotion",
    "frozen_at_utc": now,
    "reviewer": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "independence": {
        "did_not_construct_packet": True,
        "no_peer_new_fixedD_review_or_conclusion_read": True,
        "initial_report_issues_sources_frozen_together": True,
        "accepted_coarsening_dependency_read": True,
    },
    "candidate_inputs_unchanged": True,
    "older_J15_and_2024_packets_unchanged": True,
    "unresolved_substantive_objections_to_claimed_partials": 0,
    "open_research_obligations": ["precise phase-compatible EAI_D", "all-scale profile recovery"],
    "H_proved": False,
    "full_2017_solution": False,
    "new_mathematical_computation_or_CAS": False,
    "second_fresh_independent_audit_still_required": True,
    "promotion_authority": "coordinator only",
    "command": ".venv/bin/python " + PREFIX + "freeze-v1.py",
    "records": [fingerprint(path) for path in review_paths],
}
write_new(PREFIX + "manifest-v1.json", manifest)
print(json.dumps({
    "frozen_at_utc": now,
    "report": fingerprint(PREFIX + "initial-v1.md"),
    "manifest": fingerprint(PREFIX + "manifest-v1.json"),
    "all_inputs_and_older_packets_match": True,
    "unresolved_substantive_objections_to_partial_claims": 0,
    "H_proved": False,
}, indent=2))
