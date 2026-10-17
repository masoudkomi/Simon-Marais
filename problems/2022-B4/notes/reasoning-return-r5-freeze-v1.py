"""Metadata-only R5 construction freeze; no mathematical scans or tests.

Run from the repository root:
python3 problems/2022-B4/notes/reasoning-return-r5-freeze-v1.py

Only the assigned fresh prefix is written. Existing outputs are refused.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2022-B4/notes/reasoning-return-r5-"
INPUT_PATH = PREFIX + "input-validation-v1.json"
MANIFEST_PATH = PREFIX + "freeze-v1.json"
NOW = datetime.now(timezone.utc).isoformat()


def read_json(path):
    return json.loads((ROOT / path).read_text())


def fingerprint(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def verify(expected):
    actual = fingerprint(expected["path"])
    assert actual["sha256"] == expected["sha256"], (expected, actual)
    if "bytes" in expected:
        assert actual["bytes"] == expected["bytes"], (expected, actual)
    return actual


def unique_records(records):
    rows = {}
    for record in records:
        actual = verify(record)
        if actual["path"] in rows:
            assert rows[actual["path"]] == actual
        rows[actual["path"]] = actual
    return [rows[path] for path in sorted(rows)]


def metadata_rows(document):
    rows = []
    if isinstance(document, dict):
        if (isinstance(document.get("path"), str)
                and isinstance(document.get("sha256"), str)
                and re.fullmatch(r"[0-9a-f]{64}", document["sha256"])):
            rows.append(verify(document))
        for value in document.values():
            rows.extend(metadata_rows(value))
    elif isinstance(document, list):
        for value in document:
            rows.extend(metadata_rows(value))
    return rows


def write_new(path, document):
    assert path.startswith(PREFIX)
    with (ROOT / path).open("x") as stream:
        json.dump(document, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


for output in (INPUT_PATH, MANIFEST_PATH):
    assert not (ROOT / output).exists(), output

verify({"path": "AGENTS.md", "bytes": 4707,
        "sha256": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"})
sources = read_json(PREFIX + "sources-v1.json")
accepted_records = [verify(record) for record in
                    sources["complete_accepted_proof_bodies_read"]]
contributing_note = verify(sources[
    "unverified_contributing_note_fully_reconstructed_not_accepted_premise"])
cache_records = [verify({"path": source["cache_path"],
                         "bytes": source["bytes"],
                         "sha256": source["sha256"]})
                 for source in sources["primary_sources"]
                 if "cache_path" in source]
assert len(cache_records) == 3

direct_paths = [
    "AGENTS.md", "problems/2022-B4/statement.md",
    "problems/2022-B4/references.md",
    "problems/2022-B4/reviews/rational-base-shadow-return-acceptance.md",
    "problems/2022-B4/reviews/rational-base-shadow-return-acceptance.json",
    "problems/2022-B4/reviews/return-r3-acceptance.md",
    "problems/2022-B4/reviews/return-r3-acceptance.json",
    "problems/2022-B4/reviews/arithmetic-complexity-acceptance.md",
    "problems/2022-B4/reviews/arithmetic-complexity-acceptance.json",
    "problems/2022-B4/notes/arithmetic-reasoning-complexity-attribution-v1.md",
    "problems/2022-B4/notes/reasoning-return-r4-source-audit-v1.md",
    "problems/2022-B4/notes/reasoning-return-r4-sources-v1.json",
    "problems/2022-B4/notes/reasoning-return-r4-worklog-v1.md",
    "problems/2022-B4/notes/reasoning-return-r4-failed-routes-v1.md",
]
direct_records = [fingerprint(path) for path in direct_paths]
accepted_register_rows = []
for path in direct_paths:
    if path.endswith("acceptance.json"):
        accepted_register_rows.extend(metadata_rows(read_json(path)))

r4_manifest_path = "problems/2022-B4/notes/reasoning-return-r4-freeze-v1.json"
r4_manifest_record = verify({
    "path": r4_manifest_path, "bytes": 3530,
    "sha256": "f579d150c8b52450e5c20630fd36621ba8d36c3a6168c23235d352068c413f66",
})
r4_manifest = read_json(r4_manifest_path)
r4_artifacts = [verify(row) for row in r4_manifest["artifacts"]]
assert len(r4_artifacts) == 8
r4_validation_path = "problems/2022-B4/notes/reasoning-return-r4-input-validation-v1.json"
r4_validation_rows = metadata_rows(read_json(r4_validation_path))
r4_candidate_path = "problems/2022-B4/notes/reasoning-return-r4-candidate-v1.md"
assert (ROOT / accepted_records[0]["path"]).read_bytes().endswith(
    (ROOT / r4_candidate_path).read_bytes())

# Preserve the entire prior own chain; no peer findings are read here.
older_manifest_path = "problems/2019-B4/reviews/linear-output-return-r1-review-2-manifest-v1.json"
older_input_path = "problems/2019-B4/reviews/linear-output-return-r1-review-2-input-checks-v1.json"
older_manifest_record = verify({
    "path": older_manifest_path, "bytes": 3009,
    "sha256": "38dad4cbe24432e5714232a0c7a021a0277c689cb68dfbdea2f5040772dc879f",
})
older_manifest = read_json(older_manifest_path)
older_inputs = read_json(older_input_path)
older_own = unique_records(older_inputs["older_own_records"]
                           + older_manifest["records"]
                           + [older_manifest_record])
assert len(older_own) == 197

obligations = (ROOT / (PREFIX + "obligations-v1.md")).read_text()
assert re.findall(r"^\| (R5O\d\d) \|", obligations, re.MULTILINE) == [
    f"R5O{i:02d}" for i in range(1, 43)]
main = (ROOT / (PREFIX + "candidate-v1.md")).read_text()
assert main.startswith("**Candidate proof - unverified.**")
for claim in ("F5A", "F5B", "F5C", "F5D", "F5E"):
    assert claim in main

all_inputs = (accepted_records + [contributing_note] + cache_records
              + direct_records + accepted_register_rows
              + [r4_manifest_record] + r4_artifacts + r4_validation_rows
              + older_own)
telemetry = sources["direct_weekly_telemetry"]
assert telemetry["total_used_percent"] < telemetry["total_ceiling_percent"]
input_output = {
    "checked_at_utc": NOW,
    "metadata_only_not_mathematical_evidence": True,
    "constructor": "review_2022_complexity_r2",
    "root_bounded_carry_lead_contribution_disclosed": True,
    "requested_model": "gpt-6.1-sol",
    "requested_reasoning_effort": "max",
    "verified_effective_setting_readback": None,
    "complete_accepted_proof_bodies_read": accepted_records,
    "unverified_root_note_reconstructed_not_accepted_premise": contributing_note,
    "direct_scope_source_and_context_files": direct_records,
    "accepted_register_metadata_rows_verified_not_new_peer_report_reads": accepted_register_rows,
    "raw_source_cache_records_preserved_not_full_source_read_claim": cache_records,
    "r4_manifest": r4_manifest_record,
    "r4_eight_frozen_artifacts_preserved": r4_artifacts,
    "r4_input_validation_metadata_rows_preserved": r4_validation_rows,
    "r4_accepted_copy_preserves_entire_frozen_candidate_suffix": True,
    "older_own_records": older_own,
    "older_own_unique_frozen_paths_preserved": len(older_own),
    "input_record_occurrences_verified": len(all_inputs),
    "input_unique_paths_verified": len({row["path"] for row in all_inputs}),
    "all42_obligations_present": True,
    "all_five_claims_and_full_source_failure_worklog_records_present": True,
    "mathematical_program_scan_CAS_enumeration_or_certificate_replay": False,
    "administrative_operations_only": "known-file hashes, JSON metadata validation, exact accepted suffix comparison and obligation-label presence",
    "new_native_source_download_or_cached_pdf_mutation": False,
    "old_shared_Git_other_owner_file_edits_spawning_charges_contact_or_bypass": False,
    "no_new_peer_R5_findings_read_or_counted": True,
    "requires_two_OTHER_fresh_nonconstructor_whole_audits": True,
    "ordinary_infinite_lift_termination_full_annual_solution_or_novelty_claim": False,
    "direct_weekly_telemetry": telemetry,
    "all_verified": True,
}
write_new(INPUT_PATH, input_output)
records = [fingerprint(PREFIX + suffix) for suffix in (
    "candidate-v1.md", "obligations-v1.md", "failed-routes-v1.md",
    "source-audit-v1.md", "worklog-v1.md", "sources-v1.json",
    "freeze-v1.py", "input-validation-v1.json",
)]
manifest = {
    "frozen_at_utc": NOW,
    "status": "candidate proof - unverified; complete conceptual R5 construction checkpoint",
    "constructor": "review_2022_complexity_r2",
    "root_bounded_correction_contribution_and_old_roles_disclosed": True,
    "requested_model": "gpt-6.1-sol",
    "requested_reasoning_effort": "max",
    "verified_effective_setting_readback": None,
    "claims": ["F5A", "F5B", "F5C", "F5D", "F5E"],
    "whole_independent_audit_obligations": 42,
    "requires_two_OTHER_fresh_initially_blind_nonconstructor_whole_audits": True,
    "root_or_constructor_counted_as_independent_reviewer": False,
    "exact_nine_is_conditional_on_actual_ordinary_positive_AB_lift": True,
    "proposed_q_fiber_bound_still_permits_nine_at_11_over_10": True,
    "all_r_fold_fiber_equivalences_use_ordinary_positive_all_time_orbits": True,
    "common_global_radix_normalization_and_full_seed_recovery_proved_in_candidate": True,
    "real_binary_series_image_interval_not_identified_with_Z10_evaluation": True,
    "source_conjectures_or_singleton_theorem_promoted_to_two_or_three_residue_termination": False,
    "positive_infinite_lift_termination_no_ninefold_full_annual_or_novelty_claim": False,
    "mathematical_program_scan_CAS_enumeration_or_certificate_rerun": False,
    "old_shared_Git_other_owner_cache_edits_spawning_charges_contacts_bypass": False,
    "input_record_occurrences_verified": len(all_inputs),
    "input_unique_paths_verified": len({row["path"] for row in all_inputs}),
    "older_own_unique_frozen_paths_preserved": len(older_own),
    "direct_weekly_telemetry": telemetry,
    "artifacts": records,
}
write_new(MANIFEST_PATH, manifest)
print(json.dumps({"manifest": fingerprint(MANIFEST_PATH), "artifacts": records,
                  "input_occurrences": len(all_inputs),
                  "unique_input_paths": len({row["path"] for row in all_inputs}),
                  "older_own_preserved": len(older_own), "all_verified": True},
                 indent=2, ensure_ascii=False))
