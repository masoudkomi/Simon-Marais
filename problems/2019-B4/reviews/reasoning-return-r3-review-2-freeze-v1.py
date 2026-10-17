"""Administrative whole initial-review freeze; no mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2019-B4/reviews/reasoning-return-r3-review-2-"
AUTHOR = "problems/2019-B4/notes/reasoning-return-r3-"


def fingerprint(rel):
    data = (ROOT / rel).read_bytes()
    return {"path": rel, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def verify(expected):
    actual = fingerprint(expected["path"])
    assert all(actual[key] == expected[key] for key in ("path", "bytes", "sha256")), (expected, actual)
    return actual


def embedded_records(value):
    if isinstance(value, dict):
        if isinstance(value.get("path"), str) and isinstance(value.get("bytes"), int) and isinstance(value.get("sha256"), str):
            yield value
        for child in value.values():
            yield from embedded_records(child)
    elif isinstance(value, list):
        for child in value:
            yield from embedded_records(child)


def read_json(rel):
    return json.loads((ROOT / rel).read_text())


def write_exclusive(rel, value):
    with (ROOT / rel).open("x") as stream:
        json.dump(value, stream, indent=2)
        stream.write("\n")


author_manifest_path = AUTHOR + "manifest-v1.json"
author_manifest_record = fingerprint(author_manifest_path)
assert author_manifest_record["bytes"] == 3091
assert author_manifest_record["sha256"] == "6e9dd78603daa564999d083f4234f2e83d6aa063d738c6936704eaca3f33b9cb"
author_manifest = read_json(author_manifest_path)
assert len(author_manifest["records"]) == 8
author_artifacts = [verify(item) for item in author_manifest["records"]]
assert author_artifacts[0]["bytes"] == 20957
assert author_artifacts[0]["sha256"] == "6530949cc16310fabb68a3405266ab5f376a9d153a930bafda0d969ba493f296"
assert len(read_json(AUTHOR + "obligations-v1.json")["obligations"]) == 20

source_records = [verify(item) for item in embedded_records(read_json(AUTHOR + "sources-v1.json"))]
constructor_input_records = [verify(item) for item in embedded_records(read_json(AUTHOR + "input-validation-v1.json"))]
assert len(source_records) == 26
assert len(constructor_input_records) == 276
assert len({item["path"] for item in constructor_input_records}) == 276

read_body_paths = [
    "AGENTS.md",
    "problems/2019-B4/statement.md",
    "problems/2019-B4/proof.md",
    "problems/2019-B4/proofs/reviewed-secondpass-v1.1.md",
    "problems/2019-B4/notes/secondpass-canonical-renewal.md",
    "problems/2019-B4/notes/secondpass-rigidity-obstructions.md",
    "problems/2019-B4/notes/secondpass-staircases-and-pumping.md",
    "problems/2019-B4/proofs/reviewed-thirdpass-v1.1.md",
    "problems/2019-B4/proofs/reviewed-moment-tail-v1.1.md",
    "problems/2019-B4/notes/thirdpass-literature.md",
    "problems/2019-B4/notes/thirdpass-literature-sources.json",
    "problems/2019-B4/notes/coordinator-two-tape-directions.md",
]
acceptance_paths = ["problems/2019-B4/reviews/" + name + ".json" for name in [
    "acceptance", "secondpass-acceptance", "thirdpass-acceptance", "moment-tail-acceptance"
]]
for rel in acceptance_paths:
    read_body_paths += [rel[:-5] + ".md", rel]
assert len(read_body_paths) == 20
direct_read_records = [fingerprint(rel) for rel in read_body_paths]

acceptance_checks = []
for rel, expected_count in zip(acceptance_paths, [7, 14, 7, 6]):
    payload = read_json(rel)
    rows = [verify(item) for item in embedded_records(payload)]
    for suffix, digest in payload.get("artifacts", {}).items():
        item = fingerprint("problems/2019-B4/" + suffix)
        assert item["sha256"] == digest
        rows.append(item)
    assert len(rows) == expected_count
    acceptance_checks.append({"acceptance": rel, "entries_verified": len(rows), "records": rows})
assert sum(item["entries_verified"] for item in acceptance_checks) == 34

older_manifest_path = "problems/2024-B4/reviews/generalized-Kasami-review-2-manifest-v1.json"
older_manifest_record = fingerprint(older_manifest_path)
assert older_manifest_record["sha256"] == "a15b2790e601d62fb08d57d33c9bec31916ce4fc0e95a4841c427c07ab513cd7"
older_manifest = read_json(older_manifest_path)
older_validation = read_json("problems/2024-B4/reviews/generalized-Kasami-review-2-input-checks-v1.json")
older_expected = older_validation["older_own_records"] + older_manifest["records"] + [older_manifest_record]
older_by_path = {}
for item in older_expected:
    actual = verify(item)
    if actual["path"] in older_by_path:
        assert older_by_path[actual["path"]] == actual
    older_by_path[actual["path"]] = actual
assert len(older_by_path) == 153
older_own = [older_by_path[key] for key in sorted(older_by_path)]

all_inputs = [author_manifest_record] + author_artifacts + source_records + constructor_input_records + direct_read_records
for group in acceptance_checks:
    all_inputs += group["records"]
now = datetime.now(timezone.utc).isoformat()
telemetry = {
    "at_utc": "2026-10-17T11:11:31+00:00",
    "source": "direct account-wide Codex usage tool",
    "total_used_percent": 32,
    "window_duration_minutes": 10080,
    "resets_at_unix": 1792745187,
    "ordinary_usage_allowed": True,
    "total_used_cutoff_percent": 90,
    "integration_review_commit_push_reserve": True,
}
validation_path = PREFIX + "input-checks-v1.json"
write_exclusive(validation_path, {
    "checked_at_utc": now,
    "metadata_only_not_mathematical_evidence": True,
    "reviewer": "review_2022_complexity_r2",
    "constructor": "review_2021_reasoning_j15_r2",
    "requested_model": "gpt-6.1-sol",
    "requested_reasoning_effort": "max",
    "verified_effective_settings": None,
    "initial_whole_review_blind_to_new_NR_peer_reports_findings_and_reconciliation": True,
    "prior_role_disclosed": "Independent reviewer of the older root-constructed moment/tail M1-M3; no construction role in new NR1-NR4.",
    "author_manifest": author_manifest_record,
    "eight_author_artifact_records": author_artifacts,
    "author_source_records": source_records,
    "constructor_validation_records": constructor_input_records,
    "direct_read_body_and_scope_records": direct_read_records,
    "accepted_artifact_hash_checks": acceptance_checks,
    "input_record_occurrences_verified": len(all_inputs),
    "input_unique_paths_verified": len({item["path"] for item in all_inputs}),
    "older_own_paths_verified_unchanged": len(older_own),
    "older_own_records": older_own,
    "primary_read_scopes": [
        {"url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-paper-b_1.pdf", "scope": "Page2 B4(b), exact definition/domain, PDF text, about11:04UTC"},
        {"url": "https://cs.nyu.edu/~mohri/pub/edit.pdf", "scope": "Section4.3 Definition9/Lemmas1-2 and nearby residual synchronization context, about11:05UTC; no theorem imported"},
        {"url": "https://eiche.theoinf.tu-ilmenau.de/kuske/Publications/HusKZ14.pdf", "scope": "Section3 definition, Theorem4.1 normal-form context, Section8 product embedding context, about11:05UTC; no equivalence transfer"},
    ],
    "fresh_direct_weekly_telemetry": telemetry,
    "mathematical_computation_CAS_history_or_cap_enumeration_or_certificate_replay": False,
    "candidate_shared_old_source_review_or_Git_mutation": False,
    "only_assigned_new_review_prefix_written": True,
    "spawning_contact_charge_or_access_bypass": False,
    "administrative_freeze_command": "python3 problems/2019-B4/reviews/reasoning-return-r3-review-2-freeze-v1.py",
    "all_verified": True,
})

review_paths = [PREFIX + suffix for suffix in [
    "initial.md", "issues.md", "source-checks.md", "freeze-v1.py", "input-checks-v1.json"
]]
manifest_path = PREFIX + "manifest-v1.json"
manifest = {
    "frozen_at_utc": now,
    "status": "Initially blind independent WHOLE R2 frozen; no substantive objection found, no repair requested; root alone may accept.",
    "reviewer": "review_2022_complexity_r2",
    "constructor": "review_2021_reasoning_j15_r2",
    "reviewer_constructed_target": False,
    "requested_model": "gpt-6.1-sol",
    "requested_reasoning_effort": "max",
    "verified_effective_settings": None,
    "claims_audited": ["NR1", "NR2", "NR3", "NR4"],
    "whole_main_log_sources_all_twenty_obligations_accepted_bodies_and_scopes_read": True,
    "complete_per_inference_checks": 45,
    "unresolved_substantive_objections": 0,
    "author_repairs_requested": 0,
    "no_new_NR_peer_findings_read_before_initial_freeze": True,
    "prior_moment_tail_audit_disclosed": True,
    "author_manifest": author_manifest_record,
    "author_artifacts_verified": 8,
    "author_source_records_verified": len(source_records),
    "constructor_validation_record_occurrences_verified": len(constructor_input_records),
    "acceptance_hash_entries_verified": 34,
    "input_record_occurrences_verified": len(all_inputs),
    "input_unique_paths_verified": len({item["path"] for item in all_inputs}),
    "earlier_own_paths_preserved_unchanged": len(older_own),
    "mathematical_computation_enumeration_CAS_or_certificate_rerun": False,
    "candidate_shared_old_artifact_Git_or_other_worker_edits": False,
    "exact_lambda_full_annual_solution_series_nonalgebraicity_or_novelty_claim": False,
    "fresh_direct_weekly_telemetry": telemetry,
    "records": [fingerprint(rel) for rel in review_paths],
}
write_exclusive(manifest_path, manifest)
print(json.dumps({"manifest": fingerprint(manifest_path), "records": manifest["records"], "input_occurrences": len(all_inputs), "input_unique_paths": len({item["path"] for item in all_inputs}), "earlier_own_paths_preserved": len(older_own)}, indent=2))
