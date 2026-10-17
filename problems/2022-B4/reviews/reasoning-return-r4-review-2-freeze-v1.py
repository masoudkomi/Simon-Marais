"""Administrative initial-review freeze. No mathematical tests or searches."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2022-B4/reviews/reasoning-return-r4-review-2-"
AUTHOR = "problems/2022-B4/notes/reasoning-return-r4-"


def record(rel):
    data = (ROOT / rel).read_bytes()
    return {"path": rel, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def verify(expected):
    actual = record(expected["path"])
    assert all(actual[key] == expected[key] for key in ("path", "bytes", "sha256")), (expected, actual)
    return actual


def embedded(value):
    if isinstance(value, dict):
        if isinstance(value.get("path"), str) and isinstance(value.get("bytes"), int) and isinstance(value.get("sha256"), str):
            yield value
        for child in value.values():
            yield from embedded(child)
    elif isinstance(value, list):
        for child in value:
            yield from embedded(child)


def load(rel):
    return json.loads((ROOT / rel).read_text())


def dump_exclusive(rel, payload):
    with (ROOT / rel).open("x") as stream:
        json.dump(payload, stream, indent=2)
        stream.write("\n")


author_freeze_path = AUTHOR + "freeze-v1.json"
author_freeze_record = record(author_freeze_path)
assert author_freeze_record["bytes"] == 3530
assert author_freeze_record["sha256"] == "f579d150c8b52450e5c20630fd36621ba8d36c3a6168c23235d352068c413f66"
author_freeze = load(author_freeze_path)
author_artifacts = [verify(item) for item in author_freeze["artifacts"]]
assert len(author_artifacts) == 8
assert author_artifacts[0]["bytes"] == 23750
assert author_artifacts[0]["sha256"] == "cf3df09a2b38097bcbbe5c80c332a9bf1787f07a2114bf67b6108651240e2b2a"
obligation_ids = re.findall(r"^\|R4-O(\d{2})\|", (ROOT / (AUTHOR + "obligations-v1.md")).read_text(), re.M)
assert obligation_ids == [f"{index:02d}" for index in range(1, 29)]
review_ids = re.findall(r"^\| R4R2-(\d{2}) \|", (ROOT / (PREFIX + "issues.md")).read_text(), re.M)
assert review_ids == [f"{index:02d}" for index in range(1, 59)]

constructor_validation = [verify(item) for item in embedded(load(AUTHOR + "input-validation-v1.json"))]
assert len(constructor_validation) == 205
assert len({item["path"] for item in constructor_validation}) == 204
cache_records = []
for source in load(AUTHOR + "sources-v1.json")["primary_sources"]:
    if "cache_path" in source:
        cache_records.append(verify({"path": source["cache_path"], "bytes": source["bytes"], "sha256": source["sha256"]}))
assert len(cache_records) == 3

direct_read_paths = [
    "AGENTS.md",
    "problems/2022-B4/statement.md",
    "problems/2022-B4/proofs/reviewed-partials-v1.md",
    "problems/2022-B4/proofs/reviewed-density-v3.md",
    "problems/2022-B4/proofs/reviewed-arithmetic-complexity-v1.1.md",
    "problems/2022-B4/proofs/reviewed-return-r3-v1.1.md",
    "problems/2022-B4/notes/deep-literature-coordinator-v1.md",
    "problems/2022-B4/notes/rational-base-lead-v1.md",
    "problems/2022-B4/notes/reasoning-return-r3-sources-v1.json",
]
acceptance_paths = ["problems/2022-B4/reviews/" + name + ".json" for name in [
    "acceptance", "arithmetic-complexity-acceptance", "return-r3-acceptance"
]]
for rel in acceptance_paths:
    direct_read_paths += [rel[:-5] + ".md", rel]
direct_read_records = [record(rel) for rel in direct_read_paths]
assert len(direct_read_records) == 15
assert direct_read_records[5]["sha256"] == "c4b734830e9706fa5553e21fcadfa2b15c912b909ec15511066ccd5e8672c6be"

acceptance_groups = []
for rel, expected in zip(acceptance_paths, [10, 8, 1]):
    payload = load(rel)
    rows = [verify(item) for item in embedded(payload)]
    for suffix, digest in payload.get("artifacts", {}).items():
        item = record("problems/2022-B4/" + suffix)
        assert item["sha256"] == digest
        rows.append(item)
    assert len(rows) == expected
    acceptance_groups.append({"acceptance": rel, "hash_entries_verified": len(rows), "records": rows})

older_manifest_path = "problems/2019-B4/reviews/reasoning-return-r3-review-2-manifest-v1.json"
older_manifest_record = record(older_manifest_path)
assert older_manifest_record["sha256"] == "29597e68ed1a17cb5a3ab8c28fd9127730590656e5522a9429333c670b5a3e41"
older_manifest = load(older_manifest_path)
older_validation = load("problems/2019-B4/reviews/reasoning-return-r3-review-2-input-checks-v1.json")
older_expected = older_validation["older_own_records"] + older_manifest["records"] + [older_manifest_record]
older_by_path = {}
for item in older_expected:
    actual = verify(item)
    if actual["path"] in older_by_path:
        assert older_by_path[actual["path"]] == actual
    older_by_path[actual["path"]] = actual
assert len(older_by_path) == 159
older_own = [older_by_path[key] for key in sorted(older_by_path)]

all_inputs = [author_freeze_record] + author_artifacts + constructor_validation + cache_records + direct_read_records
for group in acceptance_groups:
    all_inputs += group["records"]
now = datetime.now(timezone.utc).isoformat()
telemetry = {
    "at_utc": "2026-10-17T11:20:47+00:00",
    "source": "direct account-wide Codex usage tool",
    "total_used_percent": 33,
    "window_duration_minutes": 10080,
    "resets_at_unix": 1792745187,
    "ordinary_usage_allowed": True,
    "total_used_cutoff_percent": 90,
    "integration_review_commit_push_reserve": True,
}
validation_path = PREFIX + "input-checks-v1.json"
dump_exclusive(validation_path, {
    "checked_at_utc": now,
    "metadata_only_not_mathematical_evidence": True,
    "reviewer": "review_2022_complexity_r2",
    "constructor": "review_2017_coarsening_r1",
    "requested_model": "gpt-6.1-sol",
    "requested_reasoning_effort": "max",
    "verified_effective_setting_readback": None,
    "new_R4_initial_whole_audit_blind_to_new_peer_findings": True,
    "prior_role_disclosed": "Authored old accepted R0-R3/S1-S2, audited old complexity; did not construct new R4 E1-E2/V1-V4 or supply root's power100 lead.",
    "author_freeze": author_freeze_record,
    "author_eight_artifact_records": author_artifacts,
    "constructor_validation_record_occurrences_verified": len(constructor_validation),
    "constructor_validation_unique_paths_verified": len({item["path"] for item in constructor_validation}),
    "constructor_validation_records": constructor_validation,
    "three_cached_primary_records": cache_records,
    "complete_direct_read_body_and_scope_records": direct_read_records,
    "accepted_artifact_hash_checks": acceptance_groups,
    "input_record_occurrences_verified": len(all_inputs),
    "input_unique_paths_verified": len({item["path"] for item in all_inputs}),
    "older_own_paths_verified_unchanged": len(older_own),
    "older_own_records": older_own,
    "actual_primary_read_scopes": [
        {"url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2022-paper-b.pdf", "scope": "Page2 B4(b), original domains; PDF text only, no preliminary proof"},
        {"url": "https://perso.telecom-paristech.fr/jsaka/PUB/Files/RBNS-rev.pdf", "scope": "MD/uniqueness; Lemma18/Proposition22; evaluation/prefix language; complete Proposition37/Corollary38 context. Existing cached PDF pages6,7,14,15,21,22 also extracted read-only."},
        {"url": "https://arxiv.org/html/2510.11723v2", "scope": "Expansion definition and complete relevant Section3.3 Conjecture3.9, Proposition3.10 proof, Question3.12 and Proposition3.13 proof; no unproved hypothesis imported"},
        {"url": "https://www.researchgate.net/publication/220576840_Lower_bounds_for_Z-numbers", "scope": "Public author-uploaded original body Section1, Proposition3.1 hypotheses and complete Proposition3.2 singleton proof/context; not generated abstract; web-only no binary hash"},
    ],
    "AFS_PDF_read": {"zero_based_pages": [6, 7, 14, 15, 21, 22], "exit_code": 0, "elapsed_seconds": 0.098387875, "mathematical_job": False},
    "direct_weekly_telemetry": telemetry,
    "mathematical_program_scan_CAS_enumeration_certificate_or_author_rerun": False,
    "old_candidate_source_review_shared_or_Git_edits": False,
    "only_new_assigned_review_prefix_written": True,
    "spawning_charge_contact_or_access_bypass": False,
    "administrative_freeze_command": "python3 problems/2022-B4/reviews/reasoning-return-r4-review-2-freeze-v1.py",
    "all_verified": True,
})

review_paths = [PREFIX + suffix for suffix in [
    "initial.md", "issues.md", "source-checks.md", "freeze-v1.py", "input-checks-v1.json"
]]
manifest_path = PREFIX + "manifest-v1.json"
manifest = {
    "frozen_at_utc": now,
    "status": "Fresh initially blind nonconstructor WHOLE R4 R2 frozen; no substantive objection found, no repair requested; root alone may accept.",
    "reviewer": "review_2022_complexity_r2",
    "constructor": "review_2017_coarsening_r1",
    "reviewer_constructed_new_R4": False,
    "prior_R0_R3_S1_S2_authorship_explicitly_disclosed": True,
    "requested_model": "gpt-6.1-sol",
    "requested_reasoning_effort": "max",
    "verified_effective_setting_readback": None,
    "claims_audited": ["E1", "E2", "V1", "V2", "V3", "V4"],
    "whole_main_sources_log_failed_routes_28_obligations_and_accepted_bodies_read": True,
    "per_inference_checks": len(review_ids),
    "unresolved_substantive_objections": 0,
    "author_repairs_requested": 0,
    "blind_to_new_R4_peer_findings_before_freeze": True,
    "actual_primary_definitions_and_hypotheses_checked": True,
    "no_ninefold_remains_unproved": True,
    "AFS_at_most_two_range_fails_at_11_over_10": True,
    "ninth_expansion_retains_digit10_and_is_not_a_ninth_ceiling_ray": True,
    "Phi_residue_bijections_not_ordinary_surjectivity": True,
    "author_freeze": author_freeze_record,
    "author_artifact_records_verified": 8,
    "constructor_validation_occurrences_verified": len(constructor_validation),
    "constructor_validation_unique_paths_verified": len({item["path"] for item in constructor_validation}),
    "cached_primary_hashes_verified": 3,
    "acceptance_hash_entries_verified": 19,
    "input_record_occurrences_verified": len(all_inputs),
    "input_unique_paths_verified": len({item["path"] for item in all_inputs}),
    "earlier_own_paths_preserved_unchanged": len(older_own),
    "mathematical_computation_scan_CAS_enumeration_or_author_rerun": False,
    "old_candidate_shared_Git_source_or_other_review_edits": False,
    "unconditional_termination_positive_infinite_lift_full_solution_or_novelty_claim": False,
    "direct_weekly_telemetry": telemetry,
    "records": [record(rel) for rel in review_paths],
}
dump_exclusive(manifest_path, manifest)
print(json.dumps({"manifest": record(manifest_path), "records": manifest["records"], "input_occurrences": len(all_inputs), "input_unique_paths": len({item["path"] for item in all_inputs}), "earlier_own_paths_preserved": len(older_own)}, indent=2))
