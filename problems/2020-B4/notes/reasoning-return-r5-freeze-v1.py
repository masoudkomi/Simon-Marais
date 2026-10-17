"""Metadata-only complete 2020 R5 construction freeze; NO mathematical code.

Run: python3 problems/2020-B4/notes/reasoning-return-r5-freeze-v1.py
Creates only new assigned-prefix JSON outputs, refusing replacements.
No primes, subgroup elements, moments, matrices, eigenvalues or certificates
are generated or tested. Existing bytes are read and SHA256 checked only.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2020-B4/notes/reasoning-return-r5-"
SOURCE_PATH = PREFIX + "sources-v1.json"
INPUT_PATH = PREFIX + "input-validation-v1.json"
MANIFEST_PATH = PREFIX + "freeze-v1.json"
NOW = datetime.now(timezone.utc).isoformat()


def fingerprint(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def read_json(path):
    return json.loads((ROOT / path).read_text())


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
    result = {}
    for record in records:
        actual = verify(record)
        if actual["path"] in result:
            assert actual == result[actual["path"]]
        result[actual["path"]] = actual
    return [result[path] for path in sorted(result)]


def write_new(path, document):
    assert path.startswith(PREFIX)
    with (ROOT / path).open("x") as stream:
        json.dump(document, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


for path in (SOURCE_PATH, INPUT_PATH, MANIFEST_PATH):
    assert not (ROOT / path).exists(), path

verify({"path": "AGENTS.md", "bytes": 4707,
        "sha256": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"})
accepted_expected = [
    {"path": "problems/2020-B4/proofs/reviewed-partial-v1.1.md",
     "bytes": 2207,
     "sha256": "3fcdd2d50c4545b2e466b8a24f5a958fb69f2b0f10cccf19fa4b628ed02a690f"},
    {"path": "problems/2020-B4/proofs/partial-v1.md",
     "bytes": 8703,
     "sha256": "f53945e49bd626847e52a61f7e39e96defd2ae44900f9d235c2c14e720f41525"},
    {"path": "problems/2020-B4/proofs/reviewed-reasoning-return-r4-v1.2.md",
     "bytes": 26219,
     "sha256": "6e1c29498cb3c61f84da80785a2697dc0511718c745098c3624e8a1eb7207493"},
]
accepted_records = [verify(row) for row in accepted_expected]
raw_record = verify({
    "path": "problems/2020-B4/notes/reasoning-return-r4-candidate-v1.1.md",
    "bytes": 22700,
    "sha256": "c8fc32fba5fb12a7af4e25b398b65cd9d148273c3bc6f055ea21394a66e01ce2",
})
assert (ROOT / accepted_records[2]["path"]).read_bytes().endswith(
    (ROOT / raw_record["path"]).read_bytes())

acceptance_paths = [
    "problems/2020-B4/reviews/acceptance.md",
    "problems/2020-B4/notes/reviewed-source-clarifications-v1.md",
    "problems/2020-B4/reviews/reasoning-return-r4-acceptance.md",
    "problems/2020-B4/reviews/reasoning-return-r4-acceptance.json",
]
acceptance_records = [fingerprint(path) for path in acceptance_paths]
acceptance_metadata = metadata_rows(read_json(acceptance_paths[3]))
context_paths = [
    "AGENTS.md", ".gitignore", "problems/2020-B4/statement.md",
    "problems/2020-B4/references.md",
    "problems/2020-B4/notes/reasoning-return-r4-source-checks-v1.1.md",
    "problems/2020-B4/notes/deep-literature-r1-report-v1.md",
    "problems/2020-B4/notes/deep-literature-r1-sources-v1.json",
    ".cache/official/2020-paper_b.pdf", ".cache/official/2020-solutions.pdf",
]
context_records = [fingerprint(path) for path in context_paths]
assert ".cache/" in (ROOT / ".gitignore").read_text().splitlines()

cache_specs = [
    ("Kantor1987.pdf", 1715166,
     "28b4bf0808e4f92ceba1d4cbf93b1981dfa6a6dd1bd320ff39dae37b7c1afcf3"),
    ("ThasZagier2008.pdf", 171081,
     "a8c2d922863e7f459eeb024dedbe965d7b0572a8941744e09f36b3db9b038592"),
    ("HuangSchmidt2008.pdf", 178716,
     "01e1606d116c69a2541e7be4b4e67d30574111907b9367bc1ba96f15bebf381b"),
    ("Xia2018v3.pdf", 276257,
     "e48723f71b74a53eae4613028ebe5a52f3ccf995ccbc53c3364915fd1f2443b7"),
    ("Xia2023v7.pdf", 202492,
     "dbb9cbf51d43223d87a4de9a96a94a50e4a860022c86057c9a9c62cb3ff3228a"),
    ("Sun2025v1.pdf", 319374,
     "769b10daaa6490c18e9cb030118e012c7a72608ae2881e738ec4f82de9976b06"),
]
cache_records = []
for name, size, digest in cache_specs:
    path = ".cache/literature/2020/reasoning-return-r5/" + name
    cache_records.append(verify({"path": path, "bytes": size, "sha256": digest}))
    assert (ROOT / path).read_bytes().startswith(b"%PDF")

older_manifest_record = verify({
    "path": "problems/2025-B4/notes/original-weight-universal-return-r1-manifest-v1.json",
    "bytes": 4060,
    "sha256": "96ea49d93cec3b08514c1d5d67704f72163332bdbe7feb354c86b821ee90c1a7",
})
older_manifest = read_json(older_manifest_record["path"])
older_validation = read_json(
    "problems/2025-B4/notes/original-weight-universal-return-r1-input-validation-v1.json")
older_own = unique_records(older_validation["older_own_records"]
                           + older_manifest["artifacts"]
                           + [older_manifest_record])
assert len(older_own) == 238

obligations = (ROOT / (PREFIX + "obligations-v1.md")).read_text()
assert re.findall(r"^\|(R5-O\d\d)\|", obligations, re.MULTILINE) == [
    f"R5-O{i:02d}" for i in range(1, 53)]
checks = (ROOT / (PREFIX + "constructor-checks-v1.md")).read_text()
assert re.findall(r"^\|(R5-I\d\d)\|", checks, re.MULTILINE) == [
    f"R5-I{i:02d}" for i in range(1, 11)]

telemetry = {
    "at_utc": "2026-10-17T13:52:54+00:00",
    "source": "direct account-wide usage tool paired with UTC clock",
    "total_used_percent": 42, "window_duration_minutes": 10080,
    "resets_at_unix": 1792745187, "ordinary_usage_allowed": True,
    "total_used_cutoff_percent": 90, "integration_reserve": True,
}
primary_scopes = [
    {"title": "Official2020 PaperB and solution discussion",
     "urls": ["https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2020-paper-b_1.pdf",
              "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2020-solutions_1.pdf"],
     "actual_read_scope": "p2 B4(b) and printedp27 discussion; neighboring preliminary excerpts returned but no preliminary proof investigated/reproduced",
     "individual_setter_credit_verified": False,
     "live_extraction_existing_cache_byte_identity_claimed": False},
    {"title": "Kantor1987 Primitive Permutation Groups of Odd Degree",
     "url": "https://pages.uoregon.edu/kantor/PAPERS/odddegree_planes.pdf",
     "doi": "10.1016/0021-8693(87)90019-6",
     "actual_read_scope": "Original printedpp15-16, TheoremsA/B and following arithmetic-exception warning",
     "full_CFSG_proof_reconstructed_or_imported": False,
     "original_TheoremB_has_even_order_clause_in_exception": False,
     "later_stronger_formulation_used_to_eliminate_odd_row": False,
     "cache_record": cache_records[0]},
    {"title": "Thas-Zagier2008 Finite projective planes, Fermat curves, and Gaussian periods",
     "url": "https://ems.press/content/serial-article-files/31619?nt=1",
     "doi": "10.4171/JEMS/107",
     "actual_read_scope": "pp173-177 definitions, classical P-Gamma-L automorphism statement, Theorems1.1/1.3, Remark1.2, COMPLETE Proposition2.1 proof and Theorem2.4",
     "classical_collineation_theorem_standard_attributed_input": True,
     "full_synthetic_or_external_classification_proof_reconstructed": False,
     "odd_branch_exclusion_from_Theorem1_3_imported": False,
     "cache_record": cache_records[1]},
    {"title": "Huang-Schmidt2008 Uniqueness of Some Cyclic Projective Planes",
     "url": "https://personal.ntu.edu.sg/bernhard/Publications/pub/Singer.pdf",
     "edition": "author version2008-01-15",
     "actual_read_scope": "Definitions and COMPLETE Proposition5 proof, pp1-5",
     "Ellers_Karzel_or_general_Singer_conjugacy_theorem_imported": False,
     "cache_record": cache_records[2]},
    {"title": "Xia2018 Cyclotomic difference sets in finite fields",
     "url": "https://arxiv.org/pdf/1501.03275v3",
     "doi": "10.1090/mcom/3311",
     "edition": "arXivv3 dated2017-07-04; published MathComp87(2018)",
     "actual_read_scope": "Introduction/Notation1.1, Lemmas2.2-2.5, Theorem4.1 domain, Section5.1 computation explanation/Table9, COMPLETE Theorem5.1 statement/written proof, Conjectures5.2/5.3, Proposition5.4",
     "attributed_import": "Theorem5.1 even cyclotomic INDEX<=22 other than2/4/8, both ordinary/modified",
     "finite_Groebner_data_independently_certified_or_rerun": False,
     "general_classification_conjecture_imported": False,
     "cache_record": cache_records[3]},
    {"title": "Xia2023 New necessary conditions for finite non-Desarguesian flag-transitive projective planes",
     "url": "https://arxiv.org/pdf/1707.05486v7",
     "edition": "activev7 dated2023-01-11",
     "actual_read_scope": "Introduction/definitions; COMPLETE Proposition1.2 and Theorem1.3 statements; Theorem3.4 context; Corollary3.6 and Theorem3.7 computation paragraph; Section4 through Lemma4.1 and q8mod24 deduction",
     "attributed_imports": ["Proposition1.2 exact nonclassical FLAG-transitive reverse reduction", "Theorem1.3 congruence within its exact hypotheses", "Theorem3.7 ordinary indices26/32 in primefields"],
     "full_prior_classification_or_Groebner_certificates_newly_audited": False,
     "necessary_char3_systems_treated_as_nonsolvability": False,
     "cache_record": cache_records[4]},
    {"title": "Sun2025 Cyclotomic Matrices and Power Difference Sets",
     "url": "https://arxiv.org/pdf/2511.13613v1",
     "edition": "PREPRINTv1 dated2025-11-17",
     "actual_read_scope": "Introduction/TheoremsA-C, Section2 definitions/Lemma2.1 complete proof, Section5.1 Lehmer parity/Theorem5.2 proof, Section5.3 Proposition5.17 proof, Section5.4 shifted matrices/spectral discussion, COMPLETE Section5.5, Section6 unresolved questions",
     "known_mechanism_attributed": "Modified Gram identity Proposition5.23, ordinary lambda-one0-or2 row, shifted symmetric matrices",
     "R5_proofs": "Own full coset-count, pair-sum and convolution/zero-orbit derivations; modified lambda-one normalizedT/diagonal/spectrum complete",
     "general_characterization_or_open_problem_solution_imported": False,
     "cache_record": cache_records[5]},
]
source_document = {
    "recorded_at_utc": NOW,
    "status": "candidate proof - unverified; complete R5 mathematical/source/failure checkpoint",
    "constructor": "review_2022_complexity_r2",
    "constructor_of_accepted_R4_and_its_repair_disclosed": True,
    "new_R5_proof_contribution_from_another_agent_received": False,
    "two_OTHER_fresh_whole_audits_required": True,
    "requested_model": "gpt-6.1-sol", "requested_reasoning_effort": "max",
    "verified_effective_setting_readback": None,
    "complete_accepted_bodies_read_and_verified": accepted_records,
    "accepted_R4_raw_suffix_verified": raw_record,
    "complete_scope_acceptance_records_read": acceptance_records,
    "context_metadata_not_all_external_proofs_newly_read": context_records,
    "public_native_PDF_downloads": cache_records,
    "PDF_magic_verified": True,
    "full_PDFs_only_in_ignored_cache": True,
    "redistribution_licence_verified_or_full_papers_tracked": False,
    "native_download_and_web_extraction_byte_identity_claimed": False,
    "pdftotext_and_shell_python_pypdf_available": False,
    "all_curl_downloads_completed_exit0": True,
    "initial_pending_sessions_reaped": [10823, 34283, 29745],
    "primary_actual_read_scopes": primary_scopes,
    "theorem_attribution_and_open_gaps": {
        "classical_normalizer_reconstruction_not_global_classification": True,
        "cyclotomic_count_and_Gram_mechanisms_attributed": True,
        "Xia_imports_retain_all_additional_hypotheses": True,
        "modified_T_condition_necessary_only": True,
        "nonsaturated_branch_unresolved": True,
        "old_R4_last_moment_automatic_and_interior_sufficient": True,
        "novelty_or_improved_cutoff_established": False,
    },
    "mathematical_program_scan_CAS_certificate_or_author_rerun": False,
    "direct_weekly_telemetry": telemetry,
}
write_new(SOURCE_PATH, source_document)

all_inputs = (accepted_records + [raw_record] + acceptance_records
              + acceptance_metadata + context_records + cache_records
              + [older_manifest_record] + older_own)
validation = {
    "checked_at_utc": NOW,
    "metadata_only_not_mathematical_evidence": True,
    "status": "candidate proof - unverified; complete R5 integrity/preservation checkpoint",
    "accepted_records_verified": accepted_records,
    "exact_accepted_R4_raw_suffix_verified": raw_record,
    "scope_acceptance_records_verified": acceptance_records,
    "declared_acceptance_metadata_verified_not_fresh_historical_math_audit": acceptance_metadata,
    "context_and_native_cache_records_verified": context_records + cache_records,
    "all52_obligation_rows_and10_author_issue_rows_present": True,
    "all_mathematics_symbolic_no_test_cases": True,
    "classical_hypothesis_kept_for_normalizer": True,
    "actual_zero_and_full_adjoint_blocks_kept_for_Gram": True,
    "matrix_condition_necessary_only": True,
    "extra_saturation_not_claimed_for_all_taut_orders": True,
    "old_R4_last_moment_automatic_and_interior_sufficient": True,
    "older_own_records": older_own,
    "older_own_unique_frozen_paths_preserved": len(older_own),
    "input_record_occurrences_verified": len(all_inputs),
    "input_unique_paths_verified": len({row["path"] for row in all_inputs}),
    "new_independent_whole_audits_complete": 0,
    "two_OTHER_whole_initials_required_before_promotion": True,
    "mathematical_program_scan_CAS_enumeration_certificate_or_author_rerun": False,
    "old_shared_Git_other_owner_edits_spawning_contact_charge_or_bypass": False,
    "new_public_ignored_cache_downloads_authorized": True,
    "full_annual_solution_new_cutoff_novelty_or_promotion_claim": False,
    "direct_weekly_telemetry": telemetry,
    "all_verified": True,
}
write_new(INPUT_PATH, validation)
records = [fingerprint(PREFIX + suffix) for suffix in (
    "candidate-v1.md", "obligations-v1.md", "constructor-checks-v1.md",
    "source-audit-v1.md", "worklog-v1.md", "freeze-v1.py",
    "sources-v1.json", "input-validation-v1.json",
)]
manifest = {
    "frozen_at_utc": NOW,
    "status": "candidate proof - unverified; COMPLETE R5A-R5E structural/literature checkpoint awaiting two OTHER whole audits",
    "constructor": "review_2022_complexity_r2",
    "old_R4_authorship_and_repair_role_disclosed": True,
    "requested_model": "gpt-6.1-sol", "requested_reasoning_effort": "max",
    "verified_effective_setting_readback": None,
    "scope": "2020 B4(b) EXTRA saturated subgroup branch only; no preliminary proof or full taut classification",
    "proposed_claims": {
        "R5A": "Exact coset/image-polynomial iff and product reconstruction of3-divisibility, odd subgrouporder includingL2",
        "R5B": "PrimePhi3 perfect-power restriction; exact classical prime-degree multiplier normalizer; saturatedDesarguesian orders only2/3/8",
        "R5C": "Pair sums including repeats, exact0/1/2 row; modifiedsumfree subgroup and cube-rootzero-triple classification",
        "R5D": "Actual modified oddbranch yields symmetricintegerT with rowzero,T²=qI-J,entries>=-1,exactdiagonal and spectrum; NECESSARY ONLY",
        "R5E": "Attributed exact evenresidual flag-transitive equivalence and restrictedindex sourceapplications; nooddbranchmisapplication",
    },
    "author_obligations": 52,
    "constructor_issue_rows": 10,
    "new_independent_whole_audits_complete": 0,
    "two_OTHER_initially_blind_whole_nonconstructor_audits_required": True,
    "old_R4_accepted_suffix_exactly_unchanged": True,
    "old_last_moment_automatic_and_interior_sufficient_preserved": True,
    "full_primary_source_scope_and_failed_inferences_recorded": True,
    "input_record_occurrences_verified": len(all_inputs),
    "input_unique_paths_verified": len({row["path"] for row in all_inputs}),
    "older_own_unique_frozen_paths_preserved": len(older_own),
    "mathematical_program_scan_CAS_certificate_or_author_rerun": False,
    "old_shared_Git_other_owner_edits_spawning_contact_charge_or_bypass": False,
    "public_PDFs_only_ignored_cache": True,
    "full_annual_answer_novelty_or_improved_published_cutoff": False,
    "direct_weekly_telemetry": telemetry,
    "artifacts": records,
}
write_new(MANIFEST_PATH, manifest)
print(json.dumps({"manifest": fingerprint(MANIFEST_PATH), "artifacts": records,
                  "input_occurrences": len(all_inputs),
                  "unique_input_paths": len({row["path"] for row in all_inputs}),
                  "older_own_preserved": len(older_own), "all_verified": True},
                 indent=2, ensure_ascii=False))
