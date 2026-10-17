"""Initially blind COMPLETE 2020 R6 WHOLE R2, metadata-only freeze.

No mathematical computation, parameter scan, CAS, certificate replay,
source algorithm or author program. All source-document fingerprint
occurrences are verified; repeated historical rows are stored once in
the deduplicated inventory, with exact immutable source references.
Only the unused assigned NEW reviewer prefix is written.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2020-B4/reviews/reasoning-return-r6-review-2-"
INPUT_PATH = PREFIX + "input-validation-v1.json"
MANIFEST_PATH = PREFIX + "manifest-v1.json"
NOW = datetime.now(timezone.utc).isoformat()


def safe_path(path):
    assert isinstance(path, str)
    assert not path.startswith(
        "problems/2020-B4/reviews/reasoning-return-r6-review-1-"), path
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
    "path": "problems/2020-B4/notes/reasoning-return-r6-candidate-v1.md",
    "bytes": 19423,
    "sha256": "1c71e9225a8e7881a4a640cd420c4cac55d86ddd09f8538fabe7cb630099f24c",
})
target_freeze = verify({
    "path": "problems/2020-B4/notes/reasoning-return-r6-freeze-v1.json",
    "bytes": 3821,
    "sha256": "d0f3c1f2697af5198971034696c77cac542d3553bc429aab31c1ce7428605f29",
})
constructor = read_json(target_freeze["path"])
assert constructor["constructor"] == "/root/review_2017_coarsening_r1"
assert constructor["whole_obligations"] == 54
assert len(constructor["artifacts"]) == 9
assert constructor["two_OTHER_initially_blind_whole_audits_required"]
assert not constructor["new_proof_contribution_from_another_agent_used"]
constructor_artifacts = [verify(row) for row in constructor["artifacts"]]
assert constructor_artifacts[0] == target_main
source_path = "problems/2020-B4/notes/reasoning-return-r6-sources-v1.json"
source_data = read_json(source_path)
constructor_source_metadata = metadata_rows(source_data)
accepted_math = [verify(row) for row in source_data["complete_accepted_bodies_read"]]
assert len(accepted_math) == 5
constructor_validation_path = "problems/2020-B4/notes/reasoning-return-r6-input-validation-v1.json"
constructor_validation = read_json(constructor_validation_path)
constructor_saved_metadata = metadata_rows(constructor_validation)
assert constructor_validation["administrative_integrity_only"]
assert len(constructor_validation["earlier_unique_records_preserved"]) == 334
cache_records = [verify(row) for row in source_data[
    "existing_native_cache_records_PDF_magic_verified"]]
assert len(cache_records) == 5
assert all(safe_path(row["path"]).read_bytes().startswith(b"%PDF-")
           for row in cache_records)

complete_scope_paths = (
    "problems/2020-B4/statement.md",
    "problems/2020-B4/reviews/acceptance.md",
    "problems/2020-B4/notes/reviewed-source-clarifications-v1.md",
    "problems/2020-B4/reviews/return-r3-acceptance.md",
    "problems/2020-B4/reviews/return-r3-acceptance.json",
    "problems/2020-B4/reviews/reasoning-return-r4-acceptance.md",
    "problems/2020-B4/reviews/reasoning-return-r4-acceptance.json",
    "problems/2020-B4/reviews/reasoning-return-r5-acceptance.md",
    "problems/2020-B4/reviews/reasoning-return-r5-acceptance.json",
    "problems/2020-B4/notes/reasoning-return-r3-sources-v1.json",
    "problems/2020-B4/notes/reasoning-return-r4-source-checks-v1.1.md",
    "problems/2020-B4/notes/reasoning-return-r5-source-audit-v1.md",
    "problems/2020-B4/notes/reasoning-return-r5-sources-v1.json",
    "problems/2020-B4/notes/reasoning-return-r5-obligations-v1.md",
)
complete_scope_records = [fingerprint(path) for path in complete_scope_paths]
scope_metadata = []
suffix_comparisons = []
for path in (
        "problems/2020-B4/reviews/return-r3-acceptance.json",
        "problems/2020-B4/reviews/reasoning-return-r4-acceptance.json",
        "problems/2020-B4/reviews/reasoning-return-r5-acceptance.json"):
    document = read_json(path)
    scope_metadata.extend(metadata_rows(document))
    accepted_row, raw_row = verify(document["accepted_copy"]), verify(document["candidate"])
    assert safe_path(accepted_row["path"]).read_bytes().endswith(
        safe_path(raw_row["path"]).read_bytes())
    suffix_comparisons.append({
        "accepted": accepted_row, "raw": raw_row,
        "entire_raw_submission_is_byte_identical_accepted_suffix": True,
    })
old_source_metadata = metadata_rows(read_json(
    "problems/2020-B4/notes/reasoning-return-r5-sources-v1.json"))

previous_manifest_record = verify({
    "path": "problems/2019-B4/reviews/walk-Frechet-review-1-manifest-v1.json",
    "bytes": 3563,
    "sha256": "f7fa4e56563288050aeec137eedb54ee8d43635a648302b76b02f93b02b851d7",
})
previous_validation_record = verify({
    "path": "problems/2019-B4/reviews/walk-Frechet-review-1-input-validation-v1.json",
    "bytes": 1423030,
    "sha256": "20790471fdff874d06e92e3089f0b44537901aa26de47b08d4d5c98b4e2f548b",
})
previous_manifest = read_json(previous_manifest_record["path"])
previous_validation = read_json(previous_validation_record["path"])
older_own = unique_records(previous_validation["older_own_records"]
                           + previous_manifest["records"]
                           + [previous_manifest_record])
assert len(older_own) == 295
previous_metadata = metadata_rows(previous_validation)
previous_metadata.extend(metadata_rows(previous_manifest))

obligations = safe_path(
    "problems/2020-B4/notes/reasoning-return-r6-obligations-v1.md").read_text()
obligation_ids = re.findall(r"^\| (O\d\d) \|", obligations, re.MULTILINE)
assert obligation_ids == [f"O{i:02d}" for i in range(1, 55)]
ledger = safe_path(PREFIX + "issues-v1.md").read_text()
ledger_ids = re.findall(r"^\|(R6R2-\d\d)\|", ledger, re.MULTILINE)
assert ledger_ids == [f"R6R2-{i:02d}" for i in range(1, 66)]
assert set(obligation_ids) <= set(re.findall(r"\bO\d\d\b", ledger))
for line in ledger.splitlines():
    if line.startswith("|R6R2-"):
        assert line.count("|") == 4, line
for suffix in ("initial-v1.md", "issues-v1.md", "source-checks-v1.md"):
    assert safe_path(PREFIX + suffix).is_file()
assert ",+and" not in safe_path(PREFIX + "initial-v1.md").read_text()

telemetry = {
    "at_utc": "2026-10-17T16:07:09+00:00",
    "source": "direct authoritative account-wide telemetry paired with UTC clock",
    "total_used_percent": 50, "window_duration_minutes": 10080,
    "resets_at_unix": 1792745187, "ordinary_usage_allowed": True,
    "total_used_ceiling_percent": 90, "integration_reserve": True,
    "target_start_at_utc": "2026-10-17T15:54:02+00:00",
    "target_start_total_used_percent": 49,
}
primary_reads = [
    {
        "url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2020-paper-b_1.pdf",
        "discussion": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2020-solutions_1.pdf",
        "scope": "Actual p2 B4(b) during preparation; actual printedp27 discussion during whole audit. Known Singer existence attribution only; preliminary proof and other competition problems not investigated/reproduced",
    },
    {
        "url": "https://www.researchgate.net/publication/220077727_Generators_in_cyclic_difference_sets",
        "edition": "Cohen1989 JCTA51,227-236 actual author-uploaded original text",
        "scope": "Definition, Theorem1, two literal exceptions, translation warning, order21 discussion with nearby sieve context",
        "nontriviality_hypothesis": "1<k<v-1; smaller r2 order-one case handled separately",
        "full_sieve_and_exceptional_parameter_proof_newly_reconstructed": False,
        "native_web_viewer_binary_hash_invented": False,
    },
    {
        "url": "https://www.combinatorics.org/ojs/index.php/eljc/article/download/v1i1r6/pdf/",
        "edition": "Gordon1994 EJC1 R6",
        "scope": "Operative Section2 printedpp2-3 multiplier definitions, Theorems2-5 and relevant collision/involution conditions; not full original imported proof chains or computation replay",
    },
    {
        "url": "https://arxiv.org/pdf/2007.07292v1",
        "edition": "Actual arXivv1 label14July2020; theorem numbering distinguished from publisher",
        "scope": "Introduction, COMPLETE applicable Section2 Lemma2/Theorem3, Theorems4/5 including complete written Theorem5 proof; Section3 collision/table context",
        "Theorem3_required_hypotheses": "G=Z_p x H,p prime,gcd(p,abs(H))=1,specified multiplier power fixes H",
        "Arasu_attribution_retained": True,
        "direct_product_theorem_imported_for_general_coinvariant_overlap": False,
        "finite_search_replayed_or_used_as_unrestricted_classification": False,
    },
    {
        "url": "https://aeb.win.tue.nl/preprints/hermitian1.pdf",
        "edition": "BBB author version7March1990, publication1991",
        "scope": "Applicable Section2 normalized abelian setting, involution argument, Lemmas1/2 and written proofs; no later unital/code theorem import",
        "generic_applicable_passage_requires_prime_power": False,
        "historical_missing_native_hash_retried_or_declared_resolved": False,
        "native_binary_hash": None,
    },
    {
        "url": "https://personal.ntu.edu.sg/bernhard/Publications/pub/Singer.pdf",
        "edition": "Huang-Schmidt author version15January2008",
        "scope": "Introduction printedpp1-3 definitions, known Singer existence and separate classicality conjecture. No new uniqueness/conjugacy/algorithm proof import or preliminary construction",
        "known_actual_examples": ["q5 universal-saturation counterexample", "q16 faithfulness endpoint", "reviewer q128 overlap diagnostic"],
    },
    {
        "url": "https://arxiv.org/pdf/1707.05486v7",
        "edition": "Xia activev7,11January2023",
        "scope": "During preparation: definitions, Conjecture1.1, COMPLETE Proposition1.2/Theorem1.3 statements including necessary systems; accepted R5 boundary only",
        "actual_non_Desarguesian_FLAG_transitive_hypotheses_retained": True,
        "CFSG_or_system_nonsolvability_or_elimination_certificate_imported": False,
    },
]
extra_context_reads = [
    {"url": "https://ems.press/content/serial-article-files/31619?nt=1",
     "scope": "Actual classical automorphism/flag statements and Remark1.2 in preparation; not a full new external proof audit"},
    {"url": "https://pages.uoregon.edu/kantor/PAPERS/odddegree_planes.pdf",
     "scope": "ORIGINAL TheoremsA/B printedpp15-16 and following exception warning; no full CFSG proof read/import"},
    {"url": "https://arxiv.org/pdf/1501.03275v3",
     "scope": "Notation and actual Theorem5.1 with written proof/computation provenance, even INDEX<=22 only; no certificate rerun"},
    {"url": "https://arxiv.org/pdf/2511.13613v1",
     "scope": "Actual PREPRINT complete Section5.5 modified criterion/Gram formulas; no matrix-realizability converse"},
]
all_occurrences = ([protocol, target_main, target_freeze] + constructor_artifacts
                   + constructor_source_metadata + constructor_saved_metadata
                   + accepted_math + cache_records + complete_scope_records
                   + scope_metadata + old_source_metadata
                   + [previous_manifest_record, previous_validation_record]
                   + previous_metadata + older_own)
all_unique = unique_records(all_occurrences)
validation = {
    "checked_at_utc": NOW,
    "reviewer": "/root/review_2022_complexity_r2",
    "status": "COMPLETE initially blind NONCONSTRUCTOR WHOLE2020R6 R2; no substantive scoped issue; not promotion",
    "requested_model": "gpt-6.1-sol", "requested_reasoning_effort": "max",
    "independently_verified_effective_settings": None,
    "metadata_only_not_mathematical_evidence": True,
    "new_2020_R6_peer_report_ledger_source_or_conclusions_read": False,
    "root_noticed_R1_manifest_and_companions_left_unopened": True,
    "new_R6_constructor_or_proof_contributor": False,
    "old_R4_R5_authorship_and_R4_repair_not_counted_as_self_recertification": True,
    "constructor_old_R3_authorship_and_R4_R5_review_roles_disclosed": True,
    "preparation_did_not_open_inflight_R6_notes": True,
    "complete_new_main54_obligations_checks_failed_routes_source_audit_JSON_worklog_read": True,
    "constructor_freezer_read_as_text_NOT_executed": True,
    "constructor_nine_artifacts_verified": constructor_artifacts,
    "complete_accepted_mathematical_bodies_freshly_read": accepted_math,
    "complete_acceptance_scope_and_old_source_texts_read": complete_scope_records,
    "accepted_full_raw_suffix_comparisons": suffix_comparisons,
    "constructor_saved_validation_schema_and_full_metadata_records_inspected": True,
    "constructor_saved_prior_record_count": 334,
    "constructor_context_hashes_do_not_imply_every_old_linked_math_proof_was_read": True,
    "unverified_quadratic_character_matrix_lead_imported_or_read_as_theorem": False,
    "complete_constructor_obligation_ids": obligation_ids,
    "complete_reviewer_inference_check_ids": ledger_ids,
    "substantive_issues_identified": 0,
    "author_repair_requested": False,
    "R6A_exact_c_cross_term_general_minimum_prime_equality_defect_reconstructed": True,
    "R6B_every_individual_fixed_group_equality_before_free_action_reconstructed": True,
    "R6C_actual_residual_plane_image_reset_r2_r5_Cohen_stabilizers_reconstructed": True,
    "R6C_inequality_directions_all_denominators_large_small_r_faithful_product_gap_reconstructed": True,
    "R6C_actual_q16_sharp_faithfulness_endpoint_reconstructed": True,
    "R6D_both_fixed_group_containments_actual_pair_class_and_DFT_bound_reconstructed": True,
    "extra_hand_challenges_no_mathematical_code": [
        "known actual q128,v16513=49*337,U=<8> prime order7; h7,b2359,c7 and E size3 exhibit actual c>1 and ell dividing v",
        "retained actual q4,U=<2> order6 has nonfixed orbits2/3; energy20 contradicts false-free lower25",
        "abstract C3xC3 faithful action degree6/order9 refutes false s<=r",
    ],
    "classical_q5_actual_example_not_nonexistent_parameter_used_against_universal_S0": True,
    "unrestricted_saturation_primepower_annual_cutoff_realization_or_novelty_claim": False,
    "primary_actual_read_scopes": primary_reads,
    "additional_preparation_context_NOT_new_R6_premises": extra_context_reads,
    "source_full_sieve_CFSG_uniqueness_or_large_computation_newly_certified": False,
    "combined_preparation_output_truncation_resolved_by_bounded_R5_and_scope_reads": True,
    "Cohen_word_find_no_match_resolved_by_bounded_original_text_read": True,
    "new_native_PDF_download_cache_mutation_or_viewer_binary_identity_claim": False,
    "mathematical_program_scan_CAS_certificate_source_algorithm_or_author_rerun": False,
    "previous_own_manifest": previous_manifest_record,
    "previous_own_validation": previous_validation_record,
    "previous_declared_metadata_occurrences_reverified": len(previous_metadata),
    "all_source_document_fingerprint_occurrences_verified": len(all_occurrences),
    "input_unique_paths_verified": len(all_unique),
    "deduplication_policy": "Every source-document occurrence verified; inventory stores each exact immutable path/hash once, with original source JSON references retained above. This is metadata compression only, not mathematical omission",
    "deduplicated_all_verified_input_records": all_unique,
    "older_own_records": older_own,
    "older_own_unique_frozen_paths_preserved": len(older_own),
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
    "status": "COMPLETE initially blind NONCONSTRUCTOR WHOLE2020R6 R2; no substantive scoped issue; not promotion",
    "requested_model": "gpt-6.1-sol", "requested_reasoning_effort": "max",
    "independently_verified_effective_settings": None,
    "constructor_target_main": target_main,
    "constructor_target_freeze": target_freeze,
    "whole_claims_reviewed": [
        "R6A exact arbitrary cyclic coinvariant fiber energy, actual overlap c, general orbit bound and prime-order defect/equality",
        "R6B numerical common Baer pointwise stabilizer via individual fixed-group equality and justified freeness",
        "R6C actual residual-kernel plane, full relative image reset/exceptions and exact r<=5,s<=12 restriction",
        "R6C faithful abelian product/logarithmic gap and actual q16 sharp faithfulness endpoint",
        "R6D nonsquare q1mod3 actual fixed-pair/quotient character multiplier bound",
        "actual q5 saturation counterexample, source/realization/domain/nonclosure/old-role limits",
    ],
    "all54_constructor_obligations_covered": True,
    "complete_reviewer_inference_checks": len(ledger_ids),
    "substantive_issues_identified": 0,
    "author_repair_requested": False,
    "initial_frozen_before_any_new_peer_2020_R6_findings": True,
    "new_R6_nonconstructor_independence": True,
    "old_R4_R5_authorship_not_fresh_self_recertification": True,
    "actual_overlap_and_rejected_freeness_shortcuts_challenged_by_hand": True,
    "external_imports_attributed_with_actual_read_limits": True,
    "unrestricted_saturation_annual_primepower_cutoff_realization_novelty_claim": False,
    "mathematical_program_scan_CAS_certificate_source_algorithm_or_author_rerun": False,
    "source_document_fingerprint_occurrences_verified": len(all_occurrences),
    "input_unique_paths_verified": len(all_unique),
    "repeated_historical_rows_deduplicated_in_validation_with_immutable_source_references": True,
    "older_own_unique_frozen_paths_preserved": len(older_own),
    "old_shared_Git_cache_other_owner_edits_spawning_contact_charge_bypass": False,
    "direct_weekly_telemetry": telemetry,
    "records": records,
}
write_new(MANIFEST_PATH, manifest)
print(json.dumps({
    "manifest": fingerprint(MANIFEST_PATH), "records": records,
    "source_fingerprint_occurrences_verified": len(all_occurrences),
    "unique_input_paths": len(all_unique),
    "older_own_preserved": len(older_own),
    "all_verified": True,
}, indent=2, ensure_ascii=False))
