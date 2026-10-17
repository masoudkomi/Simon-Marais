"""Metadata-only freeze of FULL R4R2-01 author repair, not mathematical code.

Run: python3 problems/2020-B4/notes/reasoning-return-r4-freeze-v1.1.py
Only new versioned files are created; existing frozen outputs are refused.
"""

from datetime import datetime, timezone
import difflib
import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2020-B4/notes/reasoning-return-r4-"
INPUT_PATH = PREFIX + "input-validation-v1.1.json"
MANIFEST_PATH = PREFIX + "freeze-v1.1.json"
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


def unique_records(records):
    rows = {}
    for record in records:
        actual = verify(record)
        if actual["path"] in rows:
            assert rows[actual["path"]] == actual
        rows[actual["path"]] = actual
    return [rows[path] for path in sorted(rows)]


def write_new(path, document):
    assert path.startswith(PREFIX) and "v1.1" in path
    with (ROOT / path).open("x") as stream:
        json.dump(document, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


for output in (INPUT_PATH, MANIFEST_PATH):
    assert not (ROOT / output).exists(), output

original_manifest_record = verify({
    "path": PREFIX + "freeze-v1.json", "bytes": 3180,
    "sha256": "2e32adb6386d2ce110b22f78f57f29ebcf5016721c3e4025e75d6d6ff280d755",
})
original_manifest = read_json(original_manifest_record["path"])
original_artifacts = [verify(row) for row in original_manifest["artifacts"]]
assert len(original_artifacts) == 7
original_input_rows = metadata_rows(read_json(PREFIX + "input-validation-v1.json"))
original_sources = read_json(PREFIX + "sources-v1.json")
original_source_rows = metadata_rows(original_sources)
repair_sources = read_json(PREFIX + "sources-v1.1.json")
repair_read_rows = [verify(row) for row in repair_sources["full_repair_reads"]]
assert repair_sources["existing_related_native_cache_fingerprints"] == original_sources[
    "existing_related_native_cache_fingerprints"]
assert repair_sources["actual_primary_read_scopes"] == original_sources[
    "actual_primary_read_scopes"]
assert repair_sources["original_v1_direct_full_reads_preserved_unchanged"] == original_sources[
    "direct_full_local_document_or_register_reads"]

review_manifest_records = [
    verify({"path": "problems/2020-B4/reviews/reasoning-return-r4-review-1-manifest-v1.json",
            "bytes": 2630,
            "sha256": "ab2ce499628249f4a79853be15c247b9987c95734a995ad9dee92da9796f14d7"}),
    verify({"path": "problems/2020-B4/reviews/reasoning-return-r4-review-2-manifest-v1.json",
            "bytes": 3301,
            "sha256": "7353007da13f3f563ebb67684dd2c5fc6a2313b58388d4fc659570a6a8940a07"}),
]
review_artifact_rows = []
review_nested_rows = []
for manifest_record in review_manifest_records:
    review_manifest = read_json(manifest_record["path"])
    for expected in review_manifest["artifacts"]:
        row = verify(expected)
        review_artifact_rows.append(row)
        if row["path"].endswith("input-validation-v1.json"):
            review_nested_rows.extend(metadata_rows(read_json(row["path"])))
assert len(review_artifact_rows) == 9

# Preserve all own bytes through the immediately preceding COMPLETE R5.
older_manifest_record = verify({
    "path": "problems/2022-B4/notes/reasoning-return-r5-freeze-v1.json",
    "bytes": 3363,
    "sha256": "29a0ba60beda79572326525a2ab5fe20b23f0aff1c4129fc9645a86b83ff4601",
})
older_manifest = read_json(older_manifest_record["path"])
older_inputs = read_json("problems/2022-B4/notes/reasoning-return-r5-input-validation-v1.json")
older_own = unique_records(older_inputs["older_own_records"]
                           + older_manifest["artifacts"]
                           + [older_manifest_record])
assert len(older_own) == 206

old_main = (ROOT / (PREFIX + "candidate-v1.md")).read_text()
new_main = (ROOT / (PREFIX + "candidate-v1.1.md")).read_text()
old_core = old_main[old_main.index("## Exact domain and inputs"):
                    old_main.index("## R4E.")]
new_core = new_main[new_main.index("## Exact domain and inputs"):
                    new_main.index("## R4E.")]
assert old_core == new_core
later_start = r"When \(L>2\), the first interior congruence"
assert old_main[old_main.index(later_start):old_main.index("## What the packet")] == new_main[
    new_main.index(later_start):new_main.index("## What the packet")]
cursor = 0
old_formula_blocks = re.findall(r"\\\[.*?\\\]", old_main, re.DOTALL)
for block in old_formula_blocks:
    found = new_main.find(block, cursor)
    assert found >= 0
    cursor = found + len(block)
assert "The final equation is essential; the first congruences alone are" not in new_main
for suffix in ("source-checks", "worklog"):
    assert (ROOT / (PREFIX + suffix + "-v1.1.md")).read_bytes().endswith(
        (ROOT / (PREFIX + suffix + "-v1.md")).read_bytes())

new_obligations = (ROOT / (PREFIX + "obligations-v1.1.md")).read_text()
assert re.findall(r"^\|(R4-O\d\d)\|", new_obligations, re.MULTILINE) == [
    f"R4-O{i:02d}" for i in range(1, 37)]
assert re.findall(r"^\|(R4-R\d\d)\|", new_obligations, re.MULTILINE) == [
    f"R4-R{i:02d}" for i in range(1, 9)]

pairs = [(stem + "-v1" + ext, stem + "-v1.1" + ext)
         for stem, ext in (("candidate", ".md"), ("obligations", ".md"),
                           ("source-checks", ".md"), ("worklog", ".md"),
                           ("sources", ".json"))]
expected_diff = "".join("".join(difflib.unified_diff(
    (ROOT / (PREFIX + before)).read_text().splitlines(keepends=True),
    (ROOT / (PREFIX + after)).read_text().splitlines(keepends=True),
    fromfile=PREFIX + before, tofile=PREFIX + after))
    for before, after in pairs)
assert expected_diff == (ROOT / (PREFIX + "repair-v1.1.diff")).read_text()

all_inputs = ([original_manifest_record] + original_artifacts + original_input_rows
              + original_source_rows + repair_read_rows + review_manifest_records
              + review_artifact_rows + review_nested_rows + older_own)
input_output = {
    "checked_at_utc": NOW,
    "metadata_only_not_mathematical_evidence": True,
    "constructor": "review_2022_complexity_r2",
    "requested_model": "gpt-6.1-sol",
    "requested_reasoning_effort": "max",
    "verified_effective_setting_readback": None,
    "repair_issue": "R4R2-01",
    "complete_both_whole_initials_ledgers_and_sources_read_before_repair": True,
    "original_v1_manifest": original_manifest_record,
    "original_v1_seven_artifacts_preserved": original_artifacts,
    "original_input_validation_rows_verified": original_input_rows,
    "original_all_source_and_dependency_rows_verified": original_source_rows,
    "repair_full_reads": repair_read_rows,
    "both_initial_review_manifests_preserved": review_manifest_records,
    "both_initial_review_declared_artifacts_preserved": review_artifact_rows,
    "both_initial_review_nested_metadata_rows_verified": review_nested_rows,
    "older_own_records": older_own,
    "older_own_unique_frozen_paths_preserved": len(older_own),
    "entire_exact_domain_R4A_R4D_body_byte_identical": True,
    "E5_and_saturation_application_corollary_body_byte_identical": True,
    "all_original_displayed_formula_blocks_preserved_in_order": len(old_formula_blocks),
    "actual_q4_counterexample_and_common_individual_subgroup_distinction_preserved": True,
    "original_source_scope_cache_and_accepted_input_fingerprints_unchanged": True,
    "source_and_log_old_histories_preserved_as_explicit_historical_suffixes": True,
    "exact_five_file_unified_diff_verified": True,
    "original36_and_repair8_obligations_present": True,
    "author_acknowledges_v1_false_essential_insufficient_claim": True,
    "automatic_final_value_remains_minus_one": True,
    "full_E2_iff_retained_with_sufficient_interior_list_proof_added": True,
    "requires_BOTH_affected_independent_reaudits": True,
    "independent_resolution_or_coordinator_acceptance_claimed": False,
    "new_R6_peer_findings_read": False,
    "mathematical_program_scan_CAS_enumeration_certificate_or_old_author_rerun": False,
    "old_shared_Git_cache_other_owner_edits_spawning_charges_contacts_or_bypass": False,
    "input_record_occurrences_verified": len(all_inputs),
    "input_unique_paths_verified": len({row["path"] for row in all_inputs}),
    "direct_weekly_telemetry": repair_sources["direct_weekly_telemetry"],
    "all_verified": True,
}
write_new(INPUT_PATH, input_output)
records = [fingerprint(PREFIX + suffix) for suffix in (
    "candidate-v1.1.md", "obligations-v1.1.md", "source-checks-v1.1.md",
    "worklog-v1.1.md", "sources-v1.1.json", "repair-v1.1.md",
    "repair-v1.1.diff", "build-repair-v1.1.py", "freeze-v1.1.py",
    "input-validation-v1.1.json",
)]
manifest = {
    "frozen_at_utc": NOW,
    "status": "candidate proof - unverified; COMPLETE R4R2-01 author repair ready for BOTH affected re-audits",
    "constructor": "review_2022_complexity_r2",
    "requested_model": "gpt-6.1-sol",
    "requested_reasoning_effort": "max",
    "verified_effective_setting_readback": None,
    "repair_issue": "R4R2-01",
    "author_accepts_real_auxiliary_error": True,
    "root_initial_miss_C_initial_objection_and_original_v1_preserved": True,
    "full_replacement_candidate_not_summary_or_diff_only": True,
    "original_whole_obligations": 36,
    "additional_repair_obligations": 8,
    "entire_R4A_R4D_and_E5_application_core_unchanged": True,
    "full_E2_iff_unchanged_in_value_and_parameter_scope": True,
    "last_row_automatic_and_interior_list_sufficient_fully_proved_in_replacement": True,
    "final_row_minus_one_not_zero_and_L2_boundary_retained": True,
    "exact_diff_and_complete_source_log_obligation_records": True,
    "required_affected_reauditors": ["coordinator root", "review_2017_coarsening_r1"],
    "independent_repair_acceptance_or_coordinator_promotion": False,
    "new_external_theorem_full_classification_unbounded_system_solution_cutoff_or_novelty": False,
    "mathematical_program_scan_CAS_enumeration_certificate_or_old_author_rerun": False,
    "old_shared_Git_cache_other_owner_edits_spawning_charges_contacts_bypass": False,
    "input_record_occurrences_verified": len(all_inputs),
    "input_unique_paths_verified": len({row["path"] for row in all_inputs}),
    "older_own_unique_frozen_paths_preserved": len(older_own),
    "direct_weekly_telemetry": repair_sources["direct_weekly_telemetry"],
    "artifacts": records,
}
write_new(MANIFEST_PATH, manifest)
print(json.dumps({"manifest": fingerprint(MANIFEST_PATH), "artifacts": records,
                  "input_occurrences": len(all_inputs),
                  "unique_input_paths": len({row["path"] for row in all_inputs}),
                  "older_own_preserved": len(older_own), "all_verified": True},
                 indent=2, ensure_ascii=False))
