"""Complete initially blind 2019 R7 whole R2 metadata-only freeze.

No mathematical program, root evaluation, history/automaton scan, CAS,
certificate regeneration, constructor execution or peer R7 conclusion read.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2019-B4/reviews/reasoning-return-r7-review-2-"
INPUT_PATH = PREFIX + "input-validation-v1.json"
MANIFEST_PATH = PREFIX + "manifest-v1.json"
NOW = datetime.now(timezone.utc).isoformat()


def safe_path(path):
    assert not path.startswith(
        "problems/2019-B4/reviews/reasoning-return-r7-review-1-"), path
    return ROOT / path


def fingerprint(path):
    data = safe_path(path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def verify(expected):
    actual = fingerprint(expected["path"])
    assert actual["sha256"] == expected["sha256"], (expected, actual)
    if "bytes" in expected:
        assert actual["bytes"] == expected["bytes"], (expected, actual)
    return actual


def read_json(path):
    return json.loads(safe_path(path).read_text())


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


def legacy_artifact_map(document):
    result = []
    artifacts = document.get("artifacts")
    if isinstance(artifacts, dict):
        for path, digest in artifacts.items():
            if isinstance(digest, str) and re.fullmatch(r"[0-9a-f]{64}", digest):
                full_path = path if path.startswith("problems/") else "problems/2019-B4/" + path
                result.append(verify({"path": full_path, "sha256": digest}))
    return result


def unique_records(rows):
    result = {}
    for expected in rows:
        actual = verify(expected)
        if actual["path"] in result:
            assert result[actual["path"]] == actual
        result[actual["path"]] = actual
    return [result[path] for path in sorted(result)]


def write_new(path, document):
    assert path.startswith(PREFIX)
    with safe_path(path).open("x") as stream:
        json.dump(document, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


for path in (INPUT_PATH, MANIFEST_PATH):
    assert not safe_path(path).exists(), path

protocol = verify({"path": "AGENTS.md", "bytes": 4707,
                   "sha256": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"})
target_main = verify({
    "path": "problems/2019-B4/notes/reasoning-return-r7-candidate-v1.md",
    "bytes": 14206,
    "sha256": "22ab005f7f66f90f194b79cf79520b77983a67716a53f04f1c401bfed646d96f",
})
target_freeze = verify({
    "path": "problems/2019-B4/notes/reasoning-return-r7-freeze-v1.json",
    "bytes": 3755,
    "sha256": "72ec54ed96255aaa17abe0eda98a98423e2e490f1ccd2c1b0a1c674f72238bf7",
})
constructor = read_json(target_freeze["path"])
assert len(constructor["artifacts"]) == 9
assert constructor["whole_independent_audit_obligations"] == 40
constructor_records = [verify(row) for row in constructor["artifacts"]]
source_path = "problems/2019-B4/notes/reasoning-return-r7-sources-v1.json"
source_data = read_json(source_path)
full_prerequisite_records = [verify(row) for row in
    source_data["complete_mathematical_prerequisite_bodies_and_scopes_read"]]
constructor_context_rows = [verify(row) for row in
    source_data["complete_context_and_exact_language_boundaries_read_not_new_premises"]]
constructor_metadata = []
for suffix in ("sources-v1.json", "input-validation-v1.json", "freeze-output-v1.json"):
    constructor_metadata.extend(metadata_rows(read_json(
        "problems/2019-B4/notes/reasoning-return-r7-" + suffix)))

additional_full_texts = [fingerprint(path) for path in (
    "problems/2019-B4/statement.md",
    "problems/2019-B4/reviews/thirdpass-acceptance.md",
    "problems/2019-B4/proofs/reviewed-chronological-context-language-v1.1.md",
    "problems/2019-B4/notes/coordinator-unmarked-greedy-failure-v1.md",
    "problems/2019-B4/notes/coordinator-relational-normal-form-followup-v1.md",
)]
partial_context = [
    {**fingerprint("problems/2019-B4/proofs/reviewed-nonregularity-return-v1.1.md"),
     "actual_read_scope": "Accepted header/complete claim statements/limiting scope; not a fresh whole symbol-budget/Perron proof review"},
    {**fingerprint("problems/2019-B4/proofs/reviewed-linear-output-return-v1.1.md"),
     "actual_read_scope": "Lines1-100 accepted header/statements,187-310 complete ambiguity and Sections3-4 overlaps/counterexample; not new whole weighted-pattern proof read"},
]
acceptance_records = []
acceptance_metadata = []
legacy_map_records = []
for name in ("acceptance", "secondpass-acceptance", "thirdpass-acceptance",
             "moment-tail-acceptance", "nonregularity-return-acceptance",
             "linear-output-return-acceptance", "chronological-context-language-acceptance"):
    path = f"problems/2019-B4/reviews/{name}.json"
    acceptance_records.append(fingerprint(path))
    document = read_json(path)
    acceptance_metadata.extend(metadata_rows(document))
    legacy_map_records.extend(legacy_artifact_map(document))

suffix_pairs = [
    ("problems/2019-B4/proofs/reviewed-moment-tail-v1.1.md",
     "problems/2019-B4/notes/coordinator-moment-regular-tail-candidate-v1.md"),
    ("problems/2019-B4/proofs/reviewed-nonregularity-return-v1.1.md",
     "problems/2019-B4/notes/reasoning-return-r3-candidate-v1.md"),
    ("problems/2019-B4/proofs/reviewed-linear-output-return-v1.1.md",
     "problems/2019-B4/notes/linear-output-return-r1-candidate-v1.md"),
    ("problems/2019-B4/proofs/reviewed-chronological-context-language-v1.1.md",
     "problems/2019-B4/notes/coordinator-chronological-context-language-candidate-v1.md"),
]
suffix_records = []
for accepted, raw in suffix_pairs:
    assert safe_path(accepted).read_bytes().endswith(safe_path(raw).read_bytes())
    suffix_records.extend((fingerprint(accepted), fingerprint(raw)))

third_accepted = "problems/2019-B4/proofs/reviewed-thirdpass-v1.1.md"
third_raw = "problems/2019-B4/notes/thirdpass-bounded-separation-v1.md"
third_marker = b"## 1. Inputs, scope and proposed conclusions"
third_accepted_bytes = safe_path(third_accepted).read_bytes()
third_raw_bytes = safe_path(third_raw).read_bytes()
assert not third_accepted_bytes.endswith(third_raw_bytes)
assert third_accepted_bytes.split(third_marker, 1)[1] == third_raw_bytes.split(third_marker, 1)[1]
third_status_comparison = {
    "accepted": fingerprint(third_accepted),
    "raw": fingerprint(third_raw),
    "literal_entire_raw_suffix": False,
    "mathematical_body_from_marker_byte_identical": True,
    "marker": third_marker.decode(),
    "introductory_acceptance_status_is_changed": True,
}

previous_manifest_record = verify({
    "path": "problems/2017-B4/reviews/global-value-return-r2-review-2-manifest-v1.json",
    "bytes": 3174,
    "sha256": "c48258f6b6f14bdbf6b9fcbdc38e82bdd747ff25956292d4663ffe2329bfffd1",
})
previous_manifest = read_json(previous_manifest_record["path"])
previous_validation_record = verify({
    "path": "problems/2017-B4/reviews/global-value-return-r2-review-2-input-validation-v1.json",
    "bytes": 897284,
    "sha256": "8dc04b7e305b8aa85ae15da1e9ef17562c15beb00a84a3cad39c962377b55e7f",
})
previous_validation = read_json(previous_validation_record["path"])
older_own = unique_records(previous_validation["older_own_records"]
                           + previous_manifest["records"]
                           + [previous_manifest_record])
assert len(older_own) == 265
previous_metadata = metadata_rows(previous_validation)
previous_metadata.extend(metadata_rows(previous_manifest))

obligations = safe_path("problems/2019-B4/notes/reasoning-return-r7-obligations-v1.md").read_text()
assert re.findall(r"^\|(R7-O\d\d)\|", obligations, re.MULTILINE) == [
    f"R7-O{i:02d}" for i in range(1, 41)]
issues = safe_path(PREFIX + "issues-v1.md").read_text()
assert re.findall(r"^\|(R7R2-\d\d)\|", issues, re.MULTILINE) == [
    f"R7R2-{i:02d}" for i in range(1, 47)]

telemetry = {
    "at_utc": "2026-10-17T14:38:06+00:00",
    "source": "direct account-wide telemetry paired with UTC clock",
    "total_used_percent": 45, "window_duration_minutes": 10080,
    "resets_at_unix": 1792745187, "ordinary_usage_allowed": True,
    "total_used_ceiling_percent": 90, "integration_reserve": True,
}
all_inputs = ([protocol, target_main, target_freeze] + constructor_records
              + full_prerequisite_records + constructor_context_rows
              + constructor_metadata + additional_full_texts + partial_context
              + acceptance_records + acceptance_metadata + legacy_map_records
              + suffix_records + [third_status_comparison["accepted"], third_status_comparison["raw"]]
              + [previous_manifest_record, previous_validation_record]
              + previous_metadata + older_own)
validation = {
    "checked_at_utc": NOW,
    "reviewer": "/root/review_2022_complexity_r2",
    "status": "COMPLETE initially blind whole 2019 R7 R2; no substantive scoped issue; not promotion",
    "metadata_only_not_mathematical_evidence": True,
    "new_2019_R7_peer_report_ledger_or_conclusions_read": False,
    "new_R7_constructor_or_proof_contributor": False,
    "older_moment_NR_LO_review_roles_disclosed_and_CCL_not_claimed_as_own_audit": True,
    "constructor_nine_records_verified": constructor_records,
    "complete_actual_mathematical_prerequisites_and_acceptance_scopes_reread": full_prerequisite_records,
    "constructor_context_declared_records_integrity_only_not_claimed_full_new_read": constructor_context_rows,
    "constructor_declared_metadata_rows_verified_not_author_execution": constructor_metadata,
    "additional_complete_texts_read": additional_full_texts,
    "context_precise_partial_read_scopes": partial_context,
    "complete_acceptance_JSONs_read": acceptance_records,
    "acceptance_declared_metadata_not_fresh_old_peer_report_reads": acceptance_metadata,
    "old_relative_artifact_hash_maps_verified": legacy_map_records,
    "accepted_raw_suffixes_byte_identical": suffix_records,
    "thirdpass_mathematical_body_identical_with_status_intro_change": third_status_comparison,
    "initial_metadata_attempt_failure": {
        "command": "python3 problems/2019-B4/reviews/reasoning-return-r7-review-2-freeze-v1.py",
        "reason": "Overbroad literal-suffix assertion for thirdpass accepted status introduction; stopped before either output was created",
        "corrected_by": "Compare every mathematical section from the exact Section1 marker; record intro distinction instead of asserting whole raw suffix",
        "mathematical_certificate_or_candidate_change": False,
    },
    "whole_main_log_sources_failures_and40_obligations_read": True,
    "complete_new_inference_checks": 46,
    "substantive_new_issues": 0,
    "repair_requested": False,
    "mathematical_program_scan_CAS_certificate_or_author_rerun": False,
    "primary_web_actual_read_scopes": [
        {"url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-paper-b_1.pdf",
         "scope": "Actual p2 B4(b), distinct outputs, alternating operations and root-rate target; no preliminary proof"},
        {"url": "https://users.renyi.hu/~p_erdos/1949-01.pdf",
         "scope": "COMPLETE original EFP four-page article, proper-law/aperiodicity theorem and both proof routes including infinite mean; adjacent Brunk not investigated",
         "generic_local_theorem_needed_by_new_proof": False},
        {"url": "https://arxiv.org/pdf/2402.17953",
         "scope": "Abstract, complete Theorem1.1, Section2 definitions/Lemma2.2 and displayed Section3 mean discussion, not full seven-page later proof",
         "new_external_theorem_imported": False},
    ],
    "new_native_PDF_download_cache_identity_or_binary_hash_claim": False,
    "all_three_actual_moment_alternatives_retained": True,
    "canonical_consecutive_ratio_and_strict_adjacent_count_enclosures_reconstructed": True,
    "raw_ratio_monotonicity_or_original_b_ratio_convergence_inferred": False,
    "all_parity_n0_seed_one_fibers_and_conditional_2_over_mu_scale_checked": True,
    "numerical_improvement_exact_lambda_algebraicity_annual_or_novelty_claim": False,
    "previous_own_manifest": previous_manifest_record,
    "previous_own_validation": previous_validation_record,
    "previous_declared_input_rows_reverified_without_math_reruns": previous_metadata,
    "older_own_records": older_own,
    "older_own_unique_paths_preserved": len(older_own),
    "input_record_occurrences_verified": len(all_inputs),
    "input_unique_paths_verified": len({row["path"] for row in all_inputs}),
    "old_shared_Git_cache_other_owner_edits_spawning_contact_charge_bypass": False,
    "direct_weekly_telemetry": telemetry,
    "all_verified": True,
}
write_new(INPUT_PATH, validation)
records = [fingerprint(PREFIX + suffix) for suffix in (
    "initial-v1.md", "issues-v1.md", "source-checks-v1.md",
    "freeze-v1.py", "input-validation-v1.json",
)]
manifest = {
    "frozen_at_utc": NOW,
    "reviewer": "/root/review_2022_complexity_r2",
    "status": "COMPLETE initially blind nonconstructor WHOLE 2019 R7 R2; no substantive scoped issue; not promotion",
    "requested_model": "gpt-6.1-sol", "requested_reasoning_effort": "max",
    "independently_verified_effective_settings": None,
    "constructor_target_main": target_main,
    "constructor_target_freeze": target_freeze,
    "whole_claims_reviewed": ["R7A", "R7B", "R7C", "R7D", "both abstract diagnostics", "source/language/failure boundaries"],
    "all40_constructor_obligations_covered": True,
    "complete_reviewer_inference_checks": 46,
    "substantive_issues_identified": 0,
    "author_repair_requested": False,
    "initial_frozen_before_any_new_peer_2019_R7_findings": True,
    "new_R7_nonconstructor_independence": True,
    "older_moment_NR_LO_review_roles_explicitly_disclosed": True,
    "source_hypotheses_actual_scopes_and_old_certificate_limits_recorded": True,
    "mathematical_program_scan_CAS_certificate_or_author_rerun": False,
    "numerical_improvement_exact_lambda_algebraicity_annual_or_novelty_claim": False,
    "input_record_occurrences_verified": len(all_inputs),
    "input_unique_paths_verified": len({row["path"] for row in all_inputs}),
    "older_own_unique_frozen_paths_preserved": len(older_own),
    "old_shared_Git_cache_other_owner_edits_spawning_contact_charge_bypass": False,
    "direct_weekly_telemetry": telemetry,
    "records": records,
}
write_new(MANIFEST_PATH, manifest)
print(json.dumps({"manifest": fingerprint(MANIFEST_PATH), "records": records,
                  "input_occurrences": len(all_inputs),
                  "unique_input_paths": len({row["path"] for row in all_inputs}),
                  "older_own_preserved": len(older_own), "all_verified": True},
                 indent=2, ensure_ascii=False))
