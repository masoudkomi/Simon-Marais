"""Metadata-only whole-audit freeze. No mathematical scans/CAS/reruns.

Run from repository root:
python3 problems/2019-B4/reviews/linear-output-return-r1-review-2-freeze-v1.py

Only new assigned review files are created, and existing outputs refused.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2019-B4/reviews/linear-output-return-r1-review-2-"
AUTHOR_PREFIX = "problems/2019-B4/notes/linear-output-return-r1-"
INPUT_PATH = PREFIX + "input-checks-v1.json"
MANIFEST_PATH = PREFIX + "manifest-v1.json"
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
    result = {}
    for record in records:
        actual = verify(record)
        if actual["path"] in result:
            assert result[actual["path"]] == actual
        result[actual["path"]] = actual
    return [result[path] for path in sorted(result)]


def write_new(path, value):
    assert path.startswith(PREFIX)
    with (ROOT / path).open("x") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


for output in (INPUT_PATH, MANIFEST_PATH):
    assert not (ROOT / output).exists(), output

author_manifest_path = AUTHOR_PREFIX + "freeze-v1.json"
author_manifest_record = verify({
    "path": author_manifest_path, "bytes": 3511,
    "sha256": "b1728d67d1101e3c9207fc935919c0cc4bf7c148f3af3220344729e5554b2deb",
})
author_manifest = read_json(author_manifest_path)
author_records = [verify(record) for record in author_manifest["artifacts"]]
assert len(author_records) == 8
verify({"path": AUTHOR_PREFIX + "candidate-v1.md", "bytes": 17270,
        "sha256": "b1bec632971326a661a4188135ce23d40f0fdcc6a121197aefe10d2237f6e1fa"})

author_sources = read_json(AUTHOR_PREFIX + "sources-v1.json")
author_validation = read_json(AUTHOR_PREFIX + "input-validation-v1.json")
author_source_rows = [verify(record) for record in author_sources["input_fingerprints"]]
author_validation_context = [verify(record) for record in author_validation["source_context_fingerprints"]]
author_earlier_rows = [verify(record) for record in author_validation["earlier_unique_records_preserved"]]
author_CCL_rows = [verify(record) for record in author_validation["prior_blind_CCL_submission_unchanged_but_not_a_proof_premise"]]
assert len(author_earlier_rows) == 229
assert len(author_source_rows) == len(author_validation_context) == 8
assert len(author_CCL_rows) == 4

# Verify presence of all author obligations and all reviewer inference rows.
author_obligations = (ROOT / (AUTHOR_PREFIX + "obligations-v1.md")).read_text()
assert re.findall(r"^\| (LO\d\d) \|", author_obligations, re.MULTILINE) == [
    f"LO{i:02d}" for i in range(1, 29)
]
review_ledger = (ROOT / (PREFIX + "issues.md")).read_text()
assert re.findall(r"^\|(LOR2-C\d\d)\|", review_ledger, re.MULTILINE) == [
    f"LOR2-C{i:02d}" for i in range(1, 51)
]

direct_paths = [
    "AGENTS.md", "problems/2019-B4/statement.md",
    "problems/2019-B4/proof.md",
    "problems/2019-B4/reviews/acceptance.md",
    "problems/2019-B4/reviews/acceptance.json",
    "problems/2019-B4/proofs/reviewed-secondpass-v1.1.md",
    "problems/2019-B4/reviews/secondpass-acceptance.md",
    "problems/2019-B4/reviews/secondpass-acceptance.json",
    "problems/2019-B4/proofs/reviewed-thirdpass-v1.1.md",
    "problems/2019-B4/reviews/thirdpass-acceptance.md",
    "problems/2019-B4/reviews/nonregularity-return-acceptance.md",
    "problems/2019-B4/references.md",
    "problems/2019-B4/notes/thirdpass-literature.md",
]
direct_records = [fingerprint(path) for path in direct_paths]
context_records = [fingerprint("problems/2019-B4/proofs/reviewed-nonregularity-return-v1.1.md")]
verify({"path": "AGENTS.md", "bytes": 4707,
        "sha256": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"})
verify({"path": "problems/2019-B4/proof.md", "bytes": 10500,
        "sha256": "58f140f1fe9c64aa77d04a9c80a76f13411264d09d5f9e908f8e0997dc6985e2"})

accepted_metadata = []
for acceptance_path in (
    "problems/2019-B4/reviews/acceptance.json",
    "problems/2019-B4/reviews/secondpass-acceptance.json",
):
    for path, digest in read_json(acceptance_path)["artifacts"].items():
        accepted_metadata.append(verify({"path": "problems/2019-B4/" + path,
                                         "sha256": digest}))

# Preserve every earlier own frozen artifact, including the separate 2020 r4.
older_manifest_path = "problems/2020-B4/notes/reasoning-return-r4-freeze-v1.json"
older_input_path = "problems/2020-B4/notes/reasoning-return-r4-input-validation-v1.json"
older_manifest_record = verify({
    "path": older_manifest_path, "bytes": 3180,
    "sha256": "2e32adb6386d2ce110b22f78f57f29ebcf5016721c3e4025e75d6d6ff280d755",
})
older_manifest = read_json(older_manifest_path)
older_inputs = read_json(older_input_path)
older_own = unique_records(older_inputs["older_own_records"]
                           + older_manifest["artifacts"] + [older_manifest_record])
assert len(older_own) == 191

telemetry = {
    "at_utc": "2026-10-17T12:19:01+00:00",
    "source": "direct account-wide Codex usage tool, paired with UTC clock",
    "total_used_percent": 37,
    "window_duration_minutes": 10080,
    "resets_at_unix": 1792745187,
    "ordinary_usage_allowed": True,
    "total_used_cutoff_percent": 90,
    "integration_reserve": True,
}
primary_scopes = [
    {
        "url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-paper-b_1.pdf",
        "scope": "Actual page2 B4 definition/(b) reopened; no preliminary proof investigated",
        "new_binary_sha256": None,
    },
    {
        "url": "https://scispace.com/pdf/growth-and-ergodicity-of-context-free-languages-ii-the-4xfrjcv85s.pdf",
        "doi": "10.1090/S0002-9947-06-03958-4",
        "scope": "Actual title/definitions, Theorems1.2/1.5, Proposition2.1, proof endpp613-614, section5pp615-616 and displayed appendix excerpt",
        "full_external_proof_newly_reconstructed": False,
        "unweighted_unambiguity_and_extra_occurrence_checked": True,
        "rightmost_derivation_weights_and_cumulative_length_convention_checked": True,
        "new_binary_sha256": None,
    },
    {
        "url": "https://www.sciencedirect.com/author/6603366451/tullio-g-ceccherini-silberstein",
        "doi": "10.1016/j.aam.2005.01.002",
        "scope": "Primary publisher-indexed abstract, confirmed by2007p615 discussion; direct publisher opens returned internal errors",
        "full2005_body_read_or_imported": False,
        "new_binary_sha256": None,
    },
]
all_inputs = (
    [author_manifest_record] + author_records + author_source_rows
    + author_validation_context + author_earlier_rows + author_CCL_rows
    + direct_records + context_records + accepted_metadata + older_own
)
input_output = {
    "checked_at_utc": NOW,
    "metadata_only_not_mathematical_evidence": True,
    "reviewer": "review_2022_complexity_r2",
    "constructor": "review_2017_coarsening_r1",
    "reviewer_constructed_new_linear_output_packet": False,
    "root_grammar_and_source_lead_contribution_disclosed": True,
    "earlier_2019_moment_and_NR_review_roles_disclosed": True,
    "requested_model": "gpt-6.1-sol",
    "requested_reasoning_effort": "max",
    "verified_effective_setting_readback": None,
    "initial_whole_review_blind_to_new_peer_linear_output_findings": True,
    "author_manifest": author_manifest_record,
    "author_eight_artifacts_verified": author_records,
    "constructor_source_fingerprint_rows_verified": author_source_rows,
    "constructor_validation_context_rows_verified": author_validation_context,
    "constructor_earlier_preservation_rows_verified": author_earlier_rows,
    "constructor_prior_CCL_metadata_not_a_proof_premise": author_CCL_rows,
    "direct_full_document_or_register_reads": direct_records,
    "context_header_and_model_reads_not_claimed_fresh_full_body": context_records,
    "accepted_register_metadata_rows_not_all_fresh_full_linked_proof_reads": accepted_metadata,
    "complete_accepted_existence_and_strict_bound_body_reread": True,
    "all28_author_obligations_and50_reviewer_checks_present": True,
    "per_inference_checks": 50,
    "unresolved_substantive_issues": 0,
    "author_repairs_requested": 0,
    "primary_actual_read_scopes": primary_scopes,
    "new_external_growth_theorem_imported_for_unmarked_counts": False,
    "formal_single_start_vs_parity_union_checked": True,
    "J0_one_and_both_recoverable_shift_indices_checked": True,
    "complete_six_pairwise_and_all_triple_intersections_checked": True,
    "exact_alternating_ambiguity_and01110_counterexample_reconstructed_by_hand": True,
    "weighted_bound_not_transferred_to_generic_strict_comparison_with_lambda": True,
    "older_own_records": older_own,
    "older_own_unique_paths_preserved_unchanged": len(older_own),
    "input_record_occurrences_verified": len(all_inputs),
    "input_unique_paths_verified": len({r["path"] for r in all_inputs}),
    "mathematical_program_scan_CAS_enumeration_certificate_or_author_rerun": False,
    "new_native_downloads_or_external_processes": False,
    "old_candidate_shared_Git_cache_or_other_review_edits": False,
    "spawning_contacts_charges_or_access_bypass": False,
    "only_new_assigned_prefix_written": True,
    "direct_weekly_telemetry": telemetry,
    "administrative_freeze_command": "python3 problems/2019-B4/reviews/linear-output-return-r1-review-2-freeze-v1.py",
    "all_verified": True,
}
write_new(INPUT_PATH, input_output)
records = [fingerprint(PREFIX + suffix) for suffix in (
    "initial.md", "issues.md", "source-checks.md", "freeze-v1.py",
    "input-checks-v1.json",
)]
manifest = {
    "frozen_at_utc": NOW,
    "status": "Initially blind nonconstructor WHOLE LO1-LO6 and conditional rational-series R2 frozen; no substantive objection found",
    "reviewer": "review_2022_complexity_r2",
    "constructor": "review_2017_coarsening_r1",
    "reviewer_constructed_target": False,
    "root_lead_contribution_and_earlier_review_roles_disclosed": True,
    "requested_model": "gpt-6.1-sol",
    "requested_reasoning_effort": "max",
    "verified_effective_setting_readback": None,
    "blind_to_new_peer_linear_output_findings_before_complete_freeze": True,
    "complete_main_source_log_selfcheck_and28_obligations_read": True,
    "complete_accepted_asymptotic_input_body_reread": True,
    "actual_primary_hypotheses_and_weighted_definitions_checked": True,
    "per_inference_checks": 50,
    "unresolved_substantive_issues": 0,
    "author_repairs_requested": 0,
    "no_ordinary_growth_sensitivity_full_value_inherent_ambiguity_or_novelty_claim": True,
    "mathematical_computation_scan_CAS_certificate_or_author_rerun": False,
    "old_shared_Git_cache_other_review_edits_spawning_charges_contacts_bypass": False,
    "author_manifest": author_manifest_record,
    "author_artifact_records_verified": len(author_records),
    "constructor_source_rows_verified": len(author_source_rows),
    "constructor_validation_rows_verified": len(author_validation_context) + len(author_earlier_rows) + len(author_CCL_rows),
    "input_record_occurrences_verified": len(all_inputs),
    "input_unique_paths_verified": len({r["path"] for r in all_inputs}),
    "older_own_frozen_paths_preserved": len(older_own),
    "direct_weekly_telemetry": telemetry,
    "records": records,
}
write_new(MANIFEST_PATH, manifest)
print(json.dumps({"manifest": fingerprint(MANIFEST_PATH), "records": records,
                  "input_occurrences": len(all_inputs),
                  "unique_input_paths": len({r["path"] for r in all_inputs}),
                  "older_own_preserved": len(older_own), "all_verified": True},
                 indent=2, ensure_ascii=False))
