"""Complete initially blind 2025 R6 WHOLE R2 metadata-only freeze.

No mathematical computation, scan, CAS, certificate replay, source proof
execution or constructor script. Only the assigned NEW reviewer prefix
is written. NEW R6 reviewer1 findings remain unread.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2025-B4/reviews/reasoning-return-r6-review-2-"
INPUT_PATH = PREFIX + "input-validation-v1.json"
MANIFEST_PATH = PREFIX + "manifest-v1.json"
NOW = datetime.now(timezone.utc).isoformat()


def safe_path(path):
    assert isinstance(path, str)
    assert not path.startswith(
        "problems/2025-B4/reviews/reasoning-return-r6-review-1-"), path
    assert not Path(path).is_absolute() and ".." not in Path(path).parts
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

protocol = verify({
    "path": "AGENTS.md", "bytes": 4707,
    "sha256": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff",
})
target_main = verify({
    "path": "problems/2025-B4/notes/reasoning-return-r6-candidate-v1.md",
    "bytes": 25588,
    "sha256": "bdf566f44dcabb5b7bbfb96778b1dd58b7375bf46fcd697c3579564e5e9da627",
})
target_freeze = verify({
    "path": "problems/2025-B4/notes/reasoning-return-r6-freeze-v1.json",
    "bytes": 3350,
    "sha256": "72885d683855f2bf61f5aeb225f7d17ccecc2dc1e8898c7aae88161b549a26f0",
})
constructor = read_json(target_freeze["path"])
assert constructor["constructor"] == "/root/review_2017_coarsening_r1"
assert constructor["whole_obligations"] == 50
assert len(constructor["artifacts"]) == 8
constructor_records = [verify(row) for row in constructor["artifacts"]]
source_data = read_json("problems/2025-B4/notes/reasoning-return-r6-sources-v1.json")
declared_accepted = [verify(row) for row in source_data["accepted_context_records"]]
assert len(declared_accepted) == 8
constructor_metadata = metadata_rows(read_json(
    "problems/2025-B4/notes/reasoning-return-r6-input-validation-v1.json"))
source_metadata = metadata_rows(source_data)

complete_accepted_bodies = [fingerprint(path) for path in (
    "problems/2025-B4/proofs/reviewed-partial-v1.1.md",
    "problems/2025-B4/proof.md",
    "problems/2025-B4/proofs/reviewed-diagonal-moment-v1.1.md",
    "problems/2025-B4/proofs/reviewed-Fueter-selection-return-v1.1.md",
    "problems/2025-B4/proofs/reviewed-original-weight-selection-v1.1.md",
    "problems/2025-B4/proofs/reviewed-original-weight-universal-v1.1.md",
    "problems/2025-B4/proofs/reviewed-reciprocal-kernel-v1.1.md",
    "problems/2025-B4/proofs/reviewed-power-gap-return-v1.1.md",
    "problems/2025-B4/proofs/reviewed-diagonal-firstcase-v1.1.md",
)]
additional_texts = [fingerprint(path) for path in (
    "problems/2025-B4/statement.md",
    "problems/2025-B4/notes/coordinator-diagonal-appendix-inspection-v1.md",
)]
acceptance_records = []
acceptance_metadata = []
suffix_comparisons = []
suffix_rows = []
for path in (
        "problems/2025-B4/reviews/diagonal-moment-acceptance.json",
        "problems/2025-B4/reviews/Fueter-selection-return-acceptance.json",
        "problems/2025-B4/reviews/original-weight-selection-acceptance.json",
        "problems/2025-B4/reviews/original-weight-universal-acceptance.json",
        "problems/2025-B4/reviews/reciprocal-kernel-acceptance.json"):
    document = read_json(path)
    acceptance_records.append(fingerprint(path))
    acceptance_metadata.extend(metadata_rows(document))
    accepted = document["accepted_copy"]["path"]
    raw = document["candidate"]["path"]
    assert safe_path(accepted).read_bytes().endswith(safe_path(raw).read_bytes())
    accepted_row, raw_row = verify(document["accepted_copy"]), verify(document["candidate"])
    suffix_rows.extend((accepted_row, raw_row))
    suffix_comparisons.append({
        "accepted": accepted_row, "raw": raw_row,
        "entire_frozen_raw_submission_is_byte_identical_suffix": True,
    })

previous_manifest_record = verify({
    "path": "problems/2019-B4/reviews/monotone-ratio-review-1-manifest-v1.json",
    "bytes": 3533,
    "sha256": "a853b05da6f1e376b958d02b017406901cbd2b3882946ddc15b22cb8fb4049ae",
})
previous_validation_record = verify({
    "path": "problems/2019-B4/reviews/monotone-ratio-review-1-input-validation-v1.json",
    "bytes": 1209508,
    "sha256": "6e966ee075651146c91523337e86bf14bac70e01edd14a3f4b974e983b2ed777",
})
previous_manifest = read_json(previous_manifest_record["path"])
previous_validation = read_json(previous_validation_record["path"])
older_own = unique_records(previous_validation["older_own_records"]
                           + previous_manifest["records"]
                           + [previous_manifest_record])
assert len(older_own) == 283
previous_metadata = metadata_rows(previous_validation)
previous_metadata.extend(metadata_rows(previous_manifest))

obligations = safe_path(
    "problems/2025-B4/notes/reasoning-return-r6-obligations-v1.md").read_text()
obligation_ids = re.findall(r"^\| (R6-\d\d) \|", obligations, re.MULTILINE)
assert obligation_ids == [f"R6-{i:02d}" for i in range(1, 51)]
ledger = safe_path(PREFIX + "issues-v1.md").read_text()
ledger_ids = re.findall(r"^\|(R6R2-\d\d)\|", ledger, re.MULTILINE)
assert ledger_ids == [f"R6R2-{i:02d}" for i in range(1, 61)]
assert set(obligation_ids) <= set(re.findall(r"R6-\d\d", ledger))
for line in ledger.splitlines():
    if line.startswith("|R6R2-"):
        assert line.count("|") == 4, line
for suffix in ("initial-v1.md", "issues-v1.md", "source-checks-v1.md"):
    assert safe_path(PREFIX + suffix).is_file()

telemetry = {
    "at_utc": "2026-10-17T15:30:59+00:00",
    "source": "direct authoritative account-wide telemetry paired with UTC clock",
    "total_used_percent": 48, "window_duration_minutes": 10080,
    "resets_at_unix": 1792745187, "ordinary_usage_allowed": True,
    "total_used_ceiling_percent": 90, "integration_reserve": True,
}
primary_reads = [
    {
        "url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2025_paper_b.pdf",
        "scope": "Actual p2 B4(b), integer signed domain and degree/exponent quantifiers; no preliminary proof investigation",
    },
    {
        "url": "https://www.researchgate.net/publication/226863681_Class_Number_Conditions_for_the_Diagonal_Case_of_the_Equation_of_Nagell_and_Ljunggren",
        "edition": "Mihailescu2008 chapter, actual author-uploaded internalVersion2.0 September17 2007",
        "scope": "Section2.1 operative conventions; COMPLETE2.2 and2.3 including Lemmas2/3; COMPLETE4.3 including both systems, singular/zero-delta and second-case ending; Theorem3 actual statement. Not entire external Theorems3/4/background proof reconstruction",
        "import": "Classical matched-prime Jacobi ideal formula equation11 and nontrivial Gauss absolute-value identity; standard cyclotomic arithmetic explicitly attributed",
        "source_basis_cardinality_Iwasawa_proof_or_generalized_e1_assumed": False,
    },
    {
        "url": "https://arxiv.org/pdf/1412.5798v2",
        "edition": "Actual arXivv2 label30June2015; internalVersion1.13 November2 2021",
        "scope": "Operative moment/group-ring/reciprocal definitions and Lemmas2.5-2.7; COMPLETE2.8-2.10 including proof; COMPLETEAppendices5.1,5.1.1,5.2. Not entire binary-Thue proof or allpages5-18 freshly claimed",
        "role": "Method attribution and exact N<p-1/read-scope check; new all-k recurrence and weaker kernel/norm proof independently reconstructed",
        "binary_Thue_class_number_or_stronger_all_but_one_target_imported": False,
    },
]
all_inputs = ([protocol, target_main, target_freeze] + constructor_records
              + declared_accepted + constructor_metadata + source_metadata
              + complete_accepted_bodies + additional_texts
              + acceptance_records + acceptance_metadata + suffix_rows
              + [previous_manifest_record, previous_validation_record]
              + previous_metadata + older_own)
validation = {
    "checked_at_utc": NOW,
    "reviewer": "/root/review_2022_complexity_r2",
    "status": "COMPLETE initially blind NONCONSTRUCTOR WHOLE2025R6 R2; no substantive scoped issue; not promotion",
    "requested_model": "gpt-6.1-sol", "requested_reasoning_effort": "max",
    "independently_verified_effective_settings": None,
    "metadata_only_not_mathematical_evidence": True,
    "new_2025_R6_peer_report_ledger_or_conclusions_read": False,
    "new_R6_constructor_or_proof_contributor": False,
    "older_own_UW_authorship_and_root_contribution_disclosed": True,
    "older_UW_accepted_by_TWO_OTHER_reviewers_not_fresh_self_recertification": True,
    "older_MS_PG_CF1_review_roles_and_constructor_old_FS_authorship_disclosed": True,
    "constructor_eight_artifacts_verified": constructor_records,
    "constructor_eight_accepted_context_records_verified": declared_accepted,
    "constructor_saved_metadata_rows_verified_NOT_constructor_execution": constructor_metadata,
    "constructor_source_metadata_rows_verified": source_metadata,
    "complete_new_main50_obligations_source_audit_JSON_constructor_check_worklog_read": True,
    "complete_accepted_mathematical_bodies_read": complete_accepted_bodies,
    "additional_complete_texts_read": additional_texts,
    "complete_five_acceptance_JSONs_read": acceptance_records,
    "acceptance_declared_metadata_not_fresh_old_peer_report_reads": acceptance_metadata,
    "accepted_raw_suffix_comparisons": suffix_comparisons,
    "complete_constructor_obligation_ids": obligation_ids,
    "complete_new_reviewer_inference_checks": ledger_ids,
    "substantive_new_issues": 0,
    "author_repair_requested": False,
    "J1_all_k_and_J2_exact_p_minus1_endpoint_reconstructed": True,
    "P1_complex_real_semilinearity_and_formal_admissibility_firewall_reconstructed": True,
    "A1_actual_signed_e0_lift_generation_fraction_integrality_normalization_reconstructed": True,
    "H1_actual_full_constant_kernel_and_one_nonzero_real_jet_reconstructed": True,
    "H2_BOTH_delta_evaluation_branches_and_uniform_constants_reconstructed": True,
    "formal_bad_pattern_claimed_arithmetically_realized": False,
    "full_phase_rank_or_all_but_one_elementary_target_claim": False,
    "new_Diophantine_exclusion_full_annual_source_refutation_or_novelty_claim": False,
    "primary_web_actual_read_scopes": primary_reads,
    "existing_cached_primary_verified_as_metadata_only_new_read_used_web": source_metadata,
    "new_native_PDF_download_cache_mutation_or_invented_author_viewer_hash": False,
    "source_viewer_failure_and_resolution": {
        "failed": "Original Section4.3 initial web open at line1969 returned internal error",
        "resolved": "Same public primary URL reopened successfully at same line; bounded opens covered full section",
        "access_bypass_or_unread_source_proof_claim": False,
    },
    "combined_local_read_truncation_resolved": "Explicit UW ending and FS earlier/middle bounded reads completed every accepted mathematical body",
    "pre_freeze_ledger_table_formatting_corrected_without_math_change": True,
    "mathematical_program_scan_CAS_certificate_or_constructor_rerun": False,
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
    "status": "COMPLETE initially blind NONCONSTRUCTOR WHOLE2025R6 R2; no substantive scoped issue; not promotion",
    "requested_model": "gpt-6.1-sol", "requested_reasoning_effort": "max",
    "independently_verified_effective_settings": None,
    "constructor_target_main": target_main,
    "constructor_target_freeze": target_freeze,
    "whole_claims_reviewed": [
        "J1 all-order integral reciprocal normalization and congruence",
        "J2 chosen-half p-1 ordinary jet Vandermonde endpoint",
        "P1 complete complex/real actual semilinearity and formal zero-phase firewall",
        "A1 actual signed e0 normalized Jacobi lift from attributed classical ideal theorem",
        "H1 actual EVERY-conjugate constant kernel and one nonzero first coefficient",
        "H2 BOTH delta branches and uniform weak height bound",
        "complete source/dependency/role/official/remaining-gap limits",
    ],
    "all50_constructor_obligations_covered": True,
    "complete_reviewer_inference_checks": len(ledger_ids),
    "substantive_issues_identified": 0,
    "author_repair_requested": False,
    "initial_frozen_before_any_new_peer_2025_R6_findings": True,
    "new_R6_nonconstructor_independence": True,
    "older_own_UW_authorship_and_other_UW_auditors_explicitly_disclosed": True,
    "classical_Jacobi_ideal_input_attributed_not_fully_reproved": True,
    "formal_bad_pattern_claimed_arithmetically_realized": False,
    "full_phase_rank_or_all_but_one_elementary_target_claim": False,
    "new_Diophantine_exclusion_full_annual_source_refutation_or_novelty_claim": False,
    "mathematical_program_scan_CAS_certificate_or_constructor_rerun": False,
    "input_record_occurrences_verified": len(all_inputs),
    "input_unique_paths_verified": len({row["path"] for row in all_inputs}),
    "older_own_unique_frozen_paths_preserved": len(older_own),
    "old_shared_Git_cache_other_owner_edits_spawning_contact_charge_bypass": False,
    "direct_weekly_telemetry": telemetry,
    "records": records,
}
write_new(MANIFEST_PATH, manifest)
print(json.dumps({
    "manifest": fingerprint(MANIFEST_PATH), "records": records,
    "input_occurrences": len(all_inputs),
    "unique_input_paths": len({row["path"] for row in all_inputs}),
    "older_own_preserved": len(older_own), "all_verified": True,
}, indent=2, ensure_ascii=False))
