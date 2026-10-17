"""Administrative initial-review freeze only; no mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2024-B4/reviews/generalized-Kasami-review-2-"
AUTHOR = "problems/2024-B4/notes/coordinator-generalized-Kasami-r1-"


def record(rel):
    data = (ROOT / rel).read_bytes()
    return {"path": rel, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def verify(expected):
    actual = record(expected["path"])
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
author_manifest_record = record(author_manifest_path)
assert author_manifest_record["bytes"] == 2042
assert author_manifest_record["sha256"] == "50c3269d28a49327e28e216a857fdb711dae8875cab127645bc4081f2ac9ec65"
author_manifest = read_json(author_manifest_path)
assert len(author_manifest["records"]) == 6
author_artifacts = [verify(item) for item in author_manifest["records"]]
assert author_artifacts[0]["sha256"] == "f99bae5f5d3877e556a30347a38616daf6b54fde300ae60543f849893a7dc4b8"

author_validation = read_json(AUTHOR + "input-validation-v1.json")
author_core = [verify(item) for item in author_validation["records"]]
assert len(author_core) == author_validation["record_occurrences"] == 417
assert len({item["path"] for item in author_core}) == author_validation["unique_paths"] == 214
motivation_cache = verify(author_validation["motivation_cache_only_not_new_theorem_premise"])

direct_paths = [
    "AGENTS.md",
    "problems/2024-B4/statement.md",
    "problems/2024-B4/proofs/reviewed-composition-Kasami-v1.1.md",
    "problems/2024-B4/reviews/composition-Kasami-acceptance.md",
    "problems/2024-B4/reviews/composition-Kasami-acceptance.json",
    "problems/2024-B4/notes/zero-automaton-criterion-reviewed-v1.1.md",
    "problems/2024-B4/reviews/criterion-acceptance.md",
    "problems/2024-B4/reviews/criterion-acceptance.json",
]
direct_inputs = [record(rel) for rel in direct_paths]
assert direct_inputs[2]["sha256"] == "f1e82d443b5ac997889c7a7f7f340437f8401516cccf9516eac132558df220c5"
assert direct_inputs[5]["sha256"] == "362f2541b2bb1ab1e22ba768b41d55e7282f08631b0ad39522682244d213f226"

cp_acceptance_records = [verify(item) for item in embedded_records(read_json(direct_paths[4]))]
assert len(cp_acceptance_records) == 9
phi13_acceptance = read_json(direct_paths[7])
phi13_acceptance_records = []
for suffix, digest in phi13_acceptance["artifacts"].items():
    item = record("problems/2024-B4/" + suffix)
    assert item["sha256"] == digest
    phi13_acceptance_records.append(item)
assert len(phi13_acceptance_records) == 10

older_global_validation = read_json("problems/2017-B4/notes/allD-global-reasoning-r1-input-validation-v1.json")
older_manifest_path = "problems/2017-B4/notes/allD-global-reasoning-r1-manifest-v1.json"
older_manifest = read_json(older_manifest_path)
older_expected = older_global_validation["earlier_own_records"] + older_manifest["records"] + [record(older_manifest_path)]
older_by_path = {}
for item in older_expected:
    actual = verify(item)
    if actual["path"] in older_by_path:
        assert older_by_path[actual["path"]] == actual
    older_by_path[actual["path"]] = actual
assert len(older_by_path) == 147
older_own = [older_by_path[key] for key in sorted(older_by_path)]

all_input_records = [author_manifest_record] + author_artifacts + author_core + [motivation_cache] + direct_inputs + cp_acceptance_records + phi13_acceptance_records
now = datetime.now(timezone.utc).isoformat()
validation_path = PREFIX + "input-checks-v1.json"
validation = {
    "checked_at_utc": now,
    "metadata_only_not_mathematical_evidence": True,
    "reviewer": "review_2022_complexity_r2",
    "requested_model": "gpt-6.1-sol",
    "requested_reasoning_effort": "max",
    "verified_effective_setting_readback": None,
    "initial_whole_review_blind_to_GK_peer_findings_and_root_later_inspection": True,
    "new_candidate_constructed_by_reviewer": False,
    "earlier_context": "Previously audited T1-T4 and C7/C11; did not construct those packets, CP, or GK; not a CP reviewer.",
    "author_manifest": author_manifest_record,
    "author_artifact_records": author_artifacts,
    "author_core_input_occurrences_verified": len(author_core),
    "author_core_unique_paths_verified": len({item["path"] for item in author_core}),
    "author_core_input_records": author_core,
    "motivation_only_cache_record": motivation_cache,
    "direct_read_input_records": direct_inputs,
    "CP_acceptance_embedded_records_verified": cp_acceptance_records,
    "phi13_acceptance_artifact_map_records_verified": phi13_acceptance_records,
    "all_input_record_occurrences_in_this_validation": len(all_input_records),
    "all_input_unique_paths_in_this_validation": len({item["path"] for item in all_input_records}),
    "older_own_paths_verified_unchanged": len(older_own),
    "older_own_records": older_own,
    "mathematical_computation_enumeration_CAS_or_certificate_rerun": False,
    "writes_only_new_assigned_review_prefix": True,
    "old_candidate_shared_source_Git_or_other_review_edits": False,
    "public_primary_source_read": {
        "url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf",
        "read_at_utc_approximately": "2026-10-17T10:57:00+00:00",
        "scope": "Page2 B4(b) and associated congruence definitions; PDF text, no new visual audit.",
    },
    "direct_weekly_telemetry": {
        "at_utc": "2026-10-17T10:58:57+00:00",
        "total_used_percent": 31,
        "window_duration_minutes": 10080,
        "resets_at_unix": 1792745187,
        "ordinary_usage_allowed": True,
        "total_used_cutoff_percent": 90,
        "reserve_for_review_integration_commit_push": True,
    },
    "administrative_freeze_command": "python3 problems/2024-B4/reviews/generalized-Kasami-review-2-freeze-v1.py",
    "all_verified": True,
}
write_exclusive(validation_path, validation)

review_files = [PREFIX + suffix for suffix in [
    "initial.md", "issues.md", "source-checks.md", "freeze-v1.py", "input-checks-v1.json"
]]
manifest_path = PREFIX + "manifest-v1.json"
manifest = {
    "frozen_at_utc": now,
    "status": "Independent initially blind WHOLE R2 audit frozen; no substantive objection found; root alone may accept.",
    "reviewer": "review_2022_complexity_r2",
    "constructor": "coordinator root",
    "reviewer_constructed_target": False,
    "requested_model": "gpt-6.1-sol",
    "requested_reasoning_effort": "max",
    "verified_effective_setting_readback": None,
    "claims_audited": ["GK1", "GK2", "GK3"],
    "whole_main_sources_log_and_all_16_author_obligations_read": True,
    "complete_inference_checks": 36,
    "unresolved_substantive_issues": 0,
    "repairs_requested": 0,
    "blind_before_any_new_GK_peer_findings": True,
    "exact_accepted_CP1_and_phi13_scopes_checked": True,
    "accepted_phi13_finite_certificate_rerun": False,
    "author_manifest": author_manifest_record,
    "author_artifact_records_verified": 6,
    "author_core_input_occurrences_verified": len(author_core),
    "author_core_unique_paths_verified": len({item["path"] for item in author_core}),
    "separate_motivation_cache_hash_verified": True,
    "CP_acceptance_embedded_records_verified": len(cp_acceptance_records),
    "phi13_acceptance_artifact_map_entries_verified": len(phi13_acceptance_records),
    "all_input_record_occurrences_in_this_validation": len(all_input_records),
    "all_input_unique_paths_in_this_validation": len({item["path"] for item in all_input_records}),
    "older_own_paths_verified_unchanged": len(older_own),
    "mathematical_computation_enumeration_CAS_or_certificate_rerun": False,
    "candidate_shared_Git_or_old_artifact_edits": False,
    "no_full_annual_solution_classification_or_novelty_claim": True,
    "weekly_total_used_percent": 31,
    "weekly_resets_at_unix": 1792745187,
    "weekly_total_used_cutoff_percent": 90,
    "records": [record(rel) for rel in review_files],
}
write_exclusive(manifest_path, manifest)
print(json.dumps({"manifest": record(manifest_path), "records": manifest["records"], "older_own_paths_preserved": len(older_own), "all_input_occurrences": len(all_input_records), "all_input_unique_paths": len({item["path"] for item in all_input_records})}, indent=2))
