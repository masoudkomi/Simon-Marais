"""AF R2 administrative identity freeze, not mathematical computation."""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2019-B4/reviews/auxiliary-presentation-r1-review-2-"
TARGET = "problems/2019-B4/notes/auxiliary-presentation-r1-"
PREVIOUS = "problems/2022-B4/notes/reasoning-return-r7-"


def fingerprint(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def verify(record):
    actual = fingerprint(record["path"])
    assert actual == {key: record[key] for key in actual}, record["path"]
    return actual


def write_new(suffix, value):
    with (ROOT / (PREFIX + suffix)).open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(value, indent=2, ensure_ascii=False) + "\n")
    return fingerprint(PREFIX + suffix)


def rows_in(value):
    if isinstance(value, dict):
        if {"path", "bytes", "sha256"} <= set(value):
            yield value
        for child in value.values():
            yield from rows_in(child)
    elif isinstance(value, list):
        for child in value:
            yield from rows_in(child)


assert not (ROOT / (PREFIX + "input-validation-v1.json")).exists()
assert not (ROOT / (PREFIX + "manifest-v1.json")).exists()
target_main = verify({"path": TARGET + "candidate-v1.md", "bytes": 8849,
    "sha256": "a0cc010860ee21155239421bef44e95e3ce2cec84be6796a9e067b39afcf4372"})
target_freeze = verify({"path": TARGET + "freeze-v1.json", "bytes": 1705,
    "sha256": "114dabe97999c84e37687c3e88b7e8f65080f93ac3477ab708e99712d0ffcbb5"})
target_manifest = json.loads((ROOT / target_freeze["path"]).read_text())
target_records = [verify(record) for record in target_manifest["records"]]
assert len(target_records) == 5
target_integrity = json.loads((ROOT / (TARGET + "integrity-v1.json")).read_text())
declared = [verify(record) for obj in [target_manifest, target_integrity]
            for record in rows_in(obj)]
declared_unique = {record["path"]: record for record in declared}
assert len(declared) == 25

accepted_json_path = "problems/2019-B4/reviews/secondpass-acceptance.json"
accepted_json = json.loads((ROOT / accepted_json_path).read_text())
old_accepted = []
for relative, expected_hash in accepted_json["artifacts"].items():
    record = fingerprint("problems/2019-B4/" + relative)
    assert record["sha256"] == expected_hash, record["path"]
    old_accepted.append(record)
assert len(old_accepted) == 14

previous_freeze = verify({"path": PREVIOUS + "freeze-v1.json", "bytes": 3683,
    "sha256": "f1894610350eb829c7be4c93329cc9054420ac111f5f28c3d0c709099529df69"})
previous_manifest = json.loads((ROOT / previous_freeze["path"]).read_text())
previous_validation_path = PREVIOUS + "input-validation-v1.json"
verify(next(record for record in previous_manifest["artifacts"]
            if record["path"] == previous_validation_path))
previous_validation = json.loads((ROOT / previous_validation_path).read_text())
prior = {}
for record in (previous_validation["earlier_unique_records_preserved"]
               + previous_manifest["artifacts"] + [previous_freeze]):
    actual = verify(record)
    if actual["path"] in prior:
        assert prior[actual["path"]] == actual
    prior[actual["path"]] = actual
assert len(prior) == 361

ledger = (ROOT / (PREFIX + "issues-v1.md")).read_text()
ids = re.findall(r"^\|AFR2-(\d\d)\|", ledger, re.MULTILINE)
assert ids == [f"{i:02}" for i in range(1, 17)]
obligations = (ROOT / (TARGET + "obligations-v1.md")).read_text()
author_ids = re.findall(r"^AF-(\d\d):", obligations, re.MULTILINE)
assert author_ids == [f"{i:02}" for i in range(1, 11)]

now = datetime.now(timezone.utc).isoformat()
primary_reads = [
    {"url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-paper-b_1.pdf",
     "read": "Actual complete B4 definition and(b), distinct strings and both exponential limits; no preliminary proof research"},
    {"url": "https://www.researchgate.net/publication/45896849_Decision_problems_for_finite_and_infinite_presentations_of_groups_and_monoids",
     "read": "Section1 monoid congruence/finite contextual derivations/presentation definitions; Section9 Definitions9.1--9.3, Proposition9.2/finite transformation context, Remark9.5 generator-elimination argument",
     "limit": "No full survey or outside Tietze equivalence proof audit; AF1 reconstructed directly instead"},
]
validation = write_new("input-validation-v1.json", {
    "validated_at_utc": now, "administrative_metadata_only_not_mathematical_proof": True,
    "complete_six_record_submission": target_records + [target_freeze],
    "declared_author_fingerprint_occurrences_verified": len(declared),
    "declared_author_unique_paths_verified": [declared_unique[path] for path in sorted(declared_unique)],
    "old_acceptance_dictionary_fourteen_records_verified": old_accepted,
    "accepted_dictionary_schema_respected_no_nonexistent_integrity_path": True,
    "earlier_unique_records_preserved": [prior[path] for path in sorted(prior)],
    "earlier_unique_record_count": len(prior),
    "whole_author_obligations": author_ids, "whole_inference_rows": ids,
    "reviewer_NEW_AF_constructor_or_contributor": False,
    "OLD_linear_output_authorship_CCL_review_roles_disclosed": True,
    "new_AF_peer_report_ledger_manifest_or_findings_read_before_initial_freeze": False,
    "blind_guard_prefix": "problems/2019-B4/reviews/auxiliary-presentation-r1-review-1-",
    "primary_reads_and_limits": primary_reads,
    "mathematical_program_CAS_scan_source_certificate_or_author_rerun": False,
    "native_download_hash_or_live_text_cache_identity_claim": False,
    "old_shared_Git_cache_mutation_or_spawning_contact_charge_bypass": False,
})
artifacts = [fingerprint(PREFIX + suffix) for suffix in [
    "initial-v1.md", "issues-v1.md", "source-checks-v1.md", "freeze-v1.py"]] + [validation]
manifest = write_new("manifest-v1.json", {
    "frozen_at_utc": now,
    "status": "COMPLETE initially blind WHOLE AF R2; no substantive scoped defect or required repair; coordinator reconciliation pending",
    "reviewer": "/root/review_2017_coarsening_r1",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "target": target_main, "target_manifest": target_freeze,
    "whole_author_obligations": len(author_ids), "independent_inference_rows": len(ids),
    "open_substantive_issues": 0, "required_author_repairs": 0,
    "reviewer_NEW_AF_constructor_or_contributor": False,
    "OLD_linear_output_authorship_CCL_review_roles_disclosed": True,
    "complete_maps_two_congruence_inclusions_rigidity_application_and_consequences_reconstructed": True,
    "empty_identity_generators_both_rewrite_directions_arbitrary_contexts_and_lengths_checked": True,
    "no_annual_growth_value_regularity_algebraicity_embedding_or_novelty_claim": True,
    "new_AF_peer_findings_read_before_initial_freeze": False,
    "declared_author_fingerprint_occurrences_verified": len(declared),
    "declared_author_unique_paths_verified": len(declared_unique),
    "old_acceptance_dictionary_records_verified": len(old_accepted),
    "earlier_frozen_context_records_verified_unchanged": len(prior),
    "mathematical_program_CAS_scan_source_certificate_or_author_rerun": False,
    "last_direct_weekly_telemetry": {"at_utc": "2026-10-17 about16:25--16:26UTC",
        "total_used_percent": 51, "window_minutes": 10080, "reset_unix": 1792745187,
        "total_ceiling_percent": 90, "review_integration_reserve": True},
    "administrative_command": "/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 " + PREFIX + "freeze-v1.py",
    "artifacts": artifacts,
})
print(json.dumps({"manifest": manifest, "main": artifacts[0],
    "whole_author_obligations": len(author_ids), "whole_inference_rows": len(ids),
    "open_substantive_issues": 0, "required_author_repairs": 0,
    "six_target_records_and_declared_identity_occurrences": [6, len(declared)],
    "old_acceptance_dictionary_records_verified": len(old_accepted),
    "earlier_unique_records_preserved": len(prior)}, indent=2))
