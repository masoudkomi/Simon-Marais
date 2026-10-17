"""Complete initially blind DG1-DG4 WHOLE R1 metadata-only freeze.

No mathematical program, enumeration, sample, CAS, certificate replay,
source algorithm or author rerun. Only the assigned NEW reviewer prefix
is written. Other NEW DG findings remain unread through this freeze.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2019-B4/reviews/walk-Frechet-review-1-"
INPUT_PATH = PREFIX + "input-validation-v1.json"
MANIFEST_PATH = PREFIX + "manifest-v1.json"
NOW = datetime.now(timezone.utc).isoformat()


def safe_path(path):
    assert isinstance(path, str)
    assert not path.startswith(
        "problems/2019-B4/reviews/walk-Frechet-review-2-"), path
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
    "path": "problems/2019-B4/notes/coordinator-walk-Frechet-return-v1.md",
    "bytes": 15923,
    "sha256": "a62416fe466f21265b6f6572ce5333f7bbe75744cb17c293ef963288b73bf8f2",
})
target_freeze = verify({
    "path": "problems/2019-B4/notes/coordinator-walk-Frechet-manifest-v1.json",
    "bytes": 2046,
    "sha256": "bd895bb6d18dee9a66fa337cce0b5f7330aa1a76c34a0bc8f692022611c5012d",
})
constructor = read_json(target_freeze["path"])
assert constructor["constructor"] == "root"
assert constructor["whole_obligations"] == 12
assert len(constructor["records"]) == 1
assert len(constructor["accepted_and_scope_inputs"]) == 7
constructor_records = [verify(row) for row in constructor["records"]]
accepted_scope = [verify(row) for row in constructor["accepted_and_scope_inputs"]]
assert constructor_records == [target_main]
assert constructor["two_OTHER_initially_blind_whole_audits_required"]
assert not constructor["mathematical_program_CAS_scan_or_sample"]

initial_acceptance_path = "problems/2019-B4/reviews/acceptance.json"
initial_acceptance = read_json(initial_acceptance_path)
legacy_acceptance_rows = [verify({
    "path": "problems/2019-B4/" + relative,
    "sha256": digest,
}) for relative, digest in initial_acceptance["artifacts"].items()]
r7_acceptance_path = "problems/2019-B4/reviews/reasoning-return-r7-acceptance.json"
r7_acceptance = read_json(r7_acceptance_path)
r7_acceptance_metadata = metadata_rows(r7_acceptance)
r7_accepted = verify(r7_acceptance["accepted_copy"])
r7_raw = verify(r7_acceptance["candidate"])
assert safe_path(r7_accepted["path"]).read_bytes().endswith(
    safe_path(r7_raw["path"]).read_bytes())
assert r7_acceptance["unresolved_substantive_issues"] == 0
assert r7_acceptance["root_read_full_candidate_both_reports_all_ledgers_sources"]
accepted_math = [fingerprint(path) for path in (
    "problems/2019-B4/proof.md",
    "problems/2019-B4/notes/secondpass-canonical-renewal.md",
    "problems/2019-B4/proofs/reviewed-reasoning-return-r7-v1.1.md",
)]
context_addendum = fingerprint(
    "problems/2019-B4/notes/coordinator-walk-literature-addendum-v1.md")
assert context_addendum["bytes"] == 5322

previous_manifest_record = verify({
    "path": "problems/2025-B4/reviews/reasoning-return-r6-review-2-manifest-v1.json",
    "bytes": 3670,
    "sha256": "15bc55817d068fa6dd81ea393d95c0b2fe6213c8827f89543da54c3ca8052579",
})
previous_validation_record = verify({
    "path": "problems/2025-B4/reviews/reasoning-return-r6-review-2-input-validation-v1.json",
    "bytes": 1357865,
    "sha256": "0249ff1de6aced191c2b1230764b3482adeb3ab87a65cdcef20365a393c30293",
})
previous_manifest = read_json(previous_manifest_record["path"])
previous_validation = read_json(previous_validation_record["path"])
older_own = unique_records(previous_validation["older_own_records"]
                           + previous_manifest["records"]
                           + [previous_manifest_record])
assert len(older_own) == 289
previous_metadata = metadata_rows(previous_validation)
previous_metadata.extend(metadata_rows(previous_manifest))

main_text = safe_path(target_main["path"]).read_text()
numbered_obligations = re.findall(r"^(\d+)\. ", main_text, re.MULTILINE)
assert numbered_obligations == [str(i) for i in range(1, 13)]
obligation_ids = [f"DG-O{i:02d}" for i in range(1, 13)]
ledger = safe_path(PREFIX + "issues-v1.md").read_text()
ledger_ids = re.findall(r"^\|(DGR1-\d\d)\|", ledger, re.MULTILINE)
assert ledger_ids == [f"DGR1-{i:02d}" for i in range(1, 41)]
assert set(obligation_ids) <= set(re.findall(r"DG-O\d\d", ledger))
for line in ledger.splitlines():
    if line.startswith("|DGR1-"):
        assert line.count("|") == 4, line
for suffix in ("initial-v1.md", "issues-v1.md", "source-checks-v1.md"):
    assert safe_path(PREFIX + suffix).is_file()

telemetry = {
    "at_utc": "2026-10-17T15:43:36+00:00",
    "source": "direct authoritative account-wide telemetry paired with UTC clock",
    "total_used_percent": 48, "window_duration_minutes": 10080,
    "resets_at_unix": 1792745187, "ordinary_usage_allowed": True,
    "total_used_ceiling_percent": 90, "integration_reserve": True,
}
primary_reads = [
    {
        "url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-paper-b_1.pdf",
        "scope": "Actual p2 B4(b) read immediately preceding MR audit; unchanged distinct-string root-growth domain retained. No preliminary proof investigation",
    },
    {
        "url": "https://www.researchgate.net/publication/228723178_Computing_Discrete_Frechet_Distance",
        "edition": "Eiter-Mannila CD-TR94/64 April25 1994, actual author-uploaded report",
        "scope": "COMPLETE mathematical Sections1-5 printedpp1-7 through references",
        "operative_use": "Indexed axis/diagonal coupling and monotone continuous-surjection definitions; ordinary continuous<=discrete comparison, independently proved here",
        "general_additive_edge_bound_used_for_exact_converse": False,
        "incidental_metric_stuttering_assertion_or_source_algorithm_imported": False,
    },
    {
        "url": "https://research-portal.uu.nl/ws/portalfiles/portal/275020035/9-faster-frechet.pdf",
        "edition": "van der Horst-van Kreveld-Ophelders-Speckmann JoCG16(2)265-298 2025 DOI10.20382/jocg.v16i2a9, publisher-version deposit",
        "scope": "Opening metadata/introduction/outline, COMPLETE Section2 definitions/free-space setup, Section4 beginning through strict long-edge condition/setup printed265-272; not full35page proof",
        "actual_required_long_edge_condition": "edge length STRICTLY greater than2delta",
        "our_edge_length": 1, "our_delta": 0.5,
        "generic_long_edge_hypothesis_satisfied_or_imported": False,
        "one_dimensional_Linfinity_is_absolute_value": True,
    },
    {
        "url": "https://eccc.weizmann.ac.il/report/2026/001/",
        "fulltext": "https://eccc.weizmann.ac.il/report/2026/001/download",
        "edition": "Fabris-Limaye-Srinivasan-Yehudayoff ECCC TR26-001 January1 2026",
        "role": "Postfreeze context ONLY, no new DG premise",
        "scope": "Actual record title/authors/date; COMPLETE Definition4.1; Lemmas4.2/4.3 and Theorem4.4 statements; portions interval proof; complete Lemma4.7 hypothesis/statement with nearby proof portions. Not complete Section4/external probability foundations",
        "source_discrete_definition": "axis-only moves and both walks start0",
        "Lemma4_3_hypotheses": "d=n^(1/4-epsilon),0<epsilon<1/4,d>=(2/3)lnn,sufficiently large n",
        "Lemma4_7_hypothesis": "Delta>=2logn",
        "fixed_half_or_one_threshold_direct_substitution_valid": False,
        "constructor_broader_read_converted_to_reviewer_full_read": False,
        "ECCC_probability_theorem_imported_or_exact_rate_evaluated": False,
    },
]
all_inputs = ([protocol, target_main, target_freeze] + constructor_records
              + accepted_scope + accepted_math + legacy_acceptance_rows
              + r7_acceptance_metadata + [r7_accepted, r7_raw, context_addendum]
              + [previous_manifest_record, previous_validation_record]
              + previous_metadata + older_own)
validation = {
    "checked_at_utc": NOW,
    "reviewer": "/root/review_2022_complexity_r2",
    "status": "COMPLETE initially blind NONCONSTRUCTOR WHOLE2019DG R1; no substantive scoped issue; not promotion",
    "requested_model": "gpt-6.1-sol", "requested_reasoning_effort": "max",
    "independently_verified_effective_settings": None,
    "metadata_only_not_mathematical_evidence": True,
    "new_DG_peer_report_ledger_or_conclusions_read": False,
    "new_DG_constructor_or_proof_contributor": False,
    "root_is_new_DG_constructor_and_excluded_as_independent_auditor": True,
    "older_moment_NR_linear_output_R7_and_MR_review_roles_disclosed": True,
    "unaccepted_MR_joining_or_finite_diagnostic_used_as_premise": False,
    "unrelated_critical_code_note_read_as_part_of_DG": False,
    "constructor_main_record_verified": constructor_records,
    "constructor_seven_accepted_scope_records_verified": accepted_scope,
    "accepted_math_bodies_full_read_during_immediately_prior_MR_with_operative_DG_rereads": accepted_math,
    "current_operative_rereads": [
        "canonical renewal chronological-model/growth prefix",
        "initial proof sections through marked/context injection",
        "accepted R7 status/domain header",
        "both acceptance JSONs complete",
    ],
    "old_R7_fresh_whole_recertification_claim": False,
    "legacy_initial_acceptance_hash_map_verified_not_old_peer_math_reread": legacy_acceptance_rows,
    "R7_acceptance_declared_metadata_verified_not_old_peer_math_reread": r7_acceptance_metadata,
    "R7_entire_raw_is_byte_identical_suffix_of_accepted_copy": {
        "accepted": r7_accepted, "raw": r7_raw, "verified": True,
    },
    "postfreeze_context_addendum_entire_text_read_NOT_new_premise": context_addendum,
    "complete_new_main_inline_sources_worklog12_obligations_and_manifest_read": True,
    "complete_constructor_numbered_obligations": numbered_obligations,
    "reviewer_assigned_obligation_ids": obligation_ids,
    "complete_new_reviewer_inference_checks": ledger_ids,
    "substantive_new_issues": 0,
    "author_repair_requested": False,
    "DG1_all_finite_words_signs_diagonal_refinement_empty_cases_reconstructed": True,
    "DG2_closed_threshold_attainment_incoming_intervals_and_grid_induction_reconstructed": True,
    "DG3_fixed_bidegree_independent_square_ALLm_limit_and_supremum_reconstructed": True,
    "DG4_distinct_pair_probability_exact4_to_m_and_log_rate_reconstructed": True,
    "rejected_naive_rounding_counterexample": "u=v=0 cell difference -1/2+s+t has free interior points but forbidden upper-right corner; candidate does not use rounding",
    "primary_web_actual_read_scopes": primary_reads,
    "truncated_source_front_matter_resolved_by_bounded_primary_opens": True,
    "new_native_PDF_download_cache_mutation_or_invented_viewer_binary_hash": False,
    "mathematical_program_scan_sample_CAS_certificate_or_constructor_rerun": False,
    "exact_lambda_positive_defect_grammar_annual_novelty_or_generic_equivalence_claim": False,
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
    "status": "COMPLETE initially blind NONCONSTRUCTOR WHOLE2019DG R1; no substantive scoped issue; not promotion",
    "requested_model": "gpt-6.1-sol", "requested_reasoning_effort": "max",
    "independently_verified_effective_settings": None,
    "constructor_target_main": target_main,
    "constructor_target_freeze": target_freeze,
    "whole_claims_reviewed": [
        "DG1 exact all-finite-tape discrete height-strip equivalence",
        "DG2 exact special closed continuous threshold equivalence with full interval/grid induction",
        "DG3 independent fixed-bidegree square, ALLm balanced root rate and supremum",
        "DG4 exact independent walk-pair probability and logarithmic rate",
        "complete source conventions/long-edge firewall/postfreeze-context/dependency/domain limits",
    ],
    "all12_constructor_obligations_covered": True,
    "complete_reviewer_inference_checks": len(ledger_ids),
    "substantive_issues_identified": 0,
    "author_repair_requested": False,
    "initial_frozen_before_any_new_peer_DG_findings": True,
    "new_DG_nonconstructor_independence": True,
    "root_new_DG_constructor_excluded_from_independent_audit": True,
    "older_review_roles_disclosed_without_self_recertification": True,
    "unaccepted_MR_joining_finite_diagnostic_or_ECCC_result_imported": False,
    "postfreeze_ECCC_context_only_actual_partial_reviewer_scope_disclosed": True,
    "exact_lambda_positive_defect_annual_generic_equivalence_or_novelty_claim": False,
    "mathematical_program_scan_sample_CAS_certificate_or_constructor_rerun": False,
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
