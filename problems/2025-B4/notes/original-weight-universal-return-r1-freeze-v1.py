"""Metadata-only complete UW1-UW4 construction freeze; no math code.

Run: python3 problems/2025-B4/notes/original-weight-universal-return-r1-freeze-v1.py
Creates only NEW assigned-prefix JSON files and refuses replacing outputs.
Does not compute primes, moments, classes, certificates or Diophantine data.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2025-B4/notes/original-weight-universal-return-r1-"
SOURCE_PATH = PREFIX + "sources-v1.json"
INPUT_PATH = PREFIX + "input-validation-v1.json"
MANIFEST_PATH = PREFIX + "manifest-v1.json"
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
    {"path": "problems/2025-B4/proofs/reviewed-diagonal-moment-v1.1.md",
     "bytes": 10168,
     "sha256": "4e25e67e6459134cb5b6c618baef91c37f30bb1dae542d7426fb61450ce4a4f7"},
    {"path": "problems/2025-B4/proofs/reviewed-Fueter-selection-return-v1.1.md",
     "bytes": 20505,
     "sha256": "230dfe9da040e98506bc6fabd5c37c356fb756d5128f990eb9a4fe2ee7e3181a"},
    {"path": "problems/2025-B4/proofs/reviewed-original-weight-selection-v1.1.md",
     "bytes": 9301,
     "sha256": "06071958bafd1fa51d5ceba798b2dab18fb1e441c4a105f093595be78c96110f"},
]
accepted_records = [verify(row) for row in accepted_expected]
raw_expected = [
    {"path": "problems/2025-B4/notes/coordinator-diagonal-moment-candidate-v2.md",
     "bytes": 7096,
     "sha256": "dae1907e2c3afe744ede7ffc89321d560ebbfab326afd78786f30dac960fcb2f"},
    {"path": "problems/2025-B4/notes/reasoning-return-r4-candidate-v1.md",
     "bytes": 17661,
     "sha256": "29c98bf01d6336020a3720935fc571159db0bdd5159a75a75adf4a78ae038482"},
    {"path": "problems/2025-B4/notes/coordinator-original-weight-selection-candidate-v1.md",
     "bytes": 6934,
     "sha256": "ef41445567edb53e53980b9edfbba2739cb1879f048e19b9e64f48e2e684ad3e"},
]
raw_records = [verify(row) for row in raw_expected]
for accepted, raw in zip(accepted_records, raw_records):
    assert (ROOT / accepted["path"]).read_bytes().endswith(
        (ROOT / raw["path"]).read_bytes()), (accepted, raw)

acceptance_paths = [
    "problems/2025-B4/reviews/diagonal-moment-acceptance.json",
    "problems/2025-B4/reviews/Fueter-selection-return-acceptance.md",
    "problems/2025-B4/reviews/Fueter-selection-return-acceptance.json",
    "problems/2025-B4/reviews/original-weight-selection-acceptance.md",
    "problems/2025-B4/reviews/original-weight-selection-acceptance.json",
]
acceptance_records = [fingerprint(path) for path in acceptance_paths]
acceptance_metadata = []
for path in acceptance_paths:
    if path.endswith(".json"):
        acceptance_metadata.extend(metadata_rows(read_json(path)))

full_context_paths = [
    "AGENTS.md", "problems/2025-B4/statement.md",
    "problems/2025-B4/references.md",
    "problems/2025-B4/notes/coordinator-diagonal-appendix-inspection-v1.md",
    "problems/2025-B4/notes/reasoning-return-r4-source-audit-v1.md",
    "problems/2025-B4/notes/coordinator-diagonal-moment-separation-v1.3.md",
    "problems/2025-B4/notes/deep-literature-r1-sources-v1.json",
]
context_records = [fingerprint(path) for path in full_context_paths]
cache_expected = [
    {"path": ".cache/official/2025-paper_b.pdf",
     "sha256": "c6d1d0c47c84521da836e766201224c84cae7c481449f28c72df842caa8e2893"},
    {"path": ".cache/official/2025-solutions.pdf",
     "sha256": "46872f990326e1a0f484f02ce863b3341178a299622041768f4964a5cafd2e5e"},
    {"path": ".cache/literature/deep-literature-r1/2025-bartolome-mihailescu-binary-thue-v2.pdf",
     "bytes": 300321,
     "sha256": "7108b665ebed8b2364c5a6629951d21abd400c96d4e7d5f4f81028f12ed424aa"},
]
cache_records = [verify(row) for row in cache_expected]

older_manifest_record = verify({
    "path": "problems/2017-B4/reviews/global-value-return-review-2-manifest-v1.json",
    "bytes": 2979,
    "sha256": "39ad3d718964940c89f3499727133fee2af9f0abafbd454a336fd7e6ba66c25b",
})
older_manifest = read_json(older_manifest_record["path"])
older_validation = read_json(
    "problems/2017-B4/reviews/global-value-return-review-2-input-validation-v1.json")
older_own = unique_records(older_validation["older_own_records"]
                           + older_manifest["artifacts"]
                           + [older_manifest_record])
assert len(older_own) == 229

obligations = (ROOT / (PREFIX + "obligations-v1.md")).read_text()
assert re.findall(r"^\|(UW-O\d\d)\|", obligations, re.MULTILINE) == [
    f"UW-O{i:02d}" for i in range(1, 41)]
checks = (ROOT / (PREFIX + "constructor-checks-v1.md")).read_text()
assert re.findall(r"^\|(UW-I\d\d)\|", checks, re.MULTILINE) == [
    f"UW-I{i:02d}" for i in range(1, 7)]

telemetry = {
    "at_utc": "2026-10-17T13:27:37+00:00",
    "source": "direct account-wide usage tool paired with UTC clock",
    "total_used_percent": 41, "window_duration_minutes": 10080,
    "resets_at_unix": 1792745187, "ordinary_usage_allowed": True,
    "total_used_cutoff_percent": 90, "integration_reserve": True,
}
primary_scopes = [
    {"url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2025_paper_b.pdf",
     "actual_read_scope": "Official p2 B4(b) all-integer domain and degree/term indexing; no preliminary proof investigated",
     "new_binary_download_or_live_cache_identity_claim": False},
    {"url": "https://www.researchgate.net/publication/226863681_Class_Number_Conditions_for_the_Diagonal_Case_of_the_Equation_of_Nagell_and_Ljunggren",
     "title": "Mihailescu, Class Number Conditions for the Diagonal Case of the Equation of Nagell and Ljunggren",
     "doi": "10.1007/978-3-211-74280-8_15",
     "edition": "Published2008; actual author-uploaded version2.0 dated2007-09-17",
     "actual_read_scope": "Section2.3 equations14-18 and full Lemma3/proof; COMPLETE Section4.3 printed19-24 including full two-list weight-p-1 application and regular/singular alternatives",
     "full_chapter_Diophantine_proof_newly_reconstructed_or_imported": False,
     "new_binary_hash": None},
    {"url": "https://arxiv.org/pdf/1412.5798v2",
     "title": "Bartolome-Mihailescu, On the equation X^n-1=BZ^n",
     "edition": "arXivv2; cached internal version1.13 dated2021-11-02",
     "actual_read_scope": "COMPLETE cached PDF pp5-18 including definitions2.4-2.5, Lemmas2.4-2.10, selection application and full Appendices5.1,5.1.1,5.2; primary live viewer reopened",
     "Voronoi_hypotheses_retained": "Even2<=m<=p-1 and a unit; m6 matches the independently derived inverse fifth moment",
     "binary_Thue_theorem_or_appendix_repair_imported": False,
     "cache_record": cache_records[2],
     "live_cache_byte_identity_claimed": False},
]
source_document = {
    "recorded_at_utc": NOW,
    "status": "candidate proof - unverified; complete source/hypothesis checkpoint",
    "constructor": "review_2022_complexity_r2",
    "root_cubic_ratio_lead_is_contribution_not_theorem_premise": True,
    "two_OTHER_whole_nonconstructor_audits_required": True,
    "requested_model": "gpt-6.1-sol", "requested_reasoning_effort": "max",
    "verified_effective_setting_readback": None,
    "complete_accepted_mathematical_bodies_reread": accepted_records,
    "original_frozen_candidates_preserved_as_exact_suffixes": raw_records,
    "complete_scope_acceptance_records_read": acceptance_records,
    "complete_relevant_context_and_source_limit_reads": context_records,
    "existing_cache_records_verified": cache_records,
    "primary_actual_read_scopes": primary_scopes,
    "attribution_boundary": {
        "existing_mechanism": "Published positive two-Fueter translate pairing kills direct action; source Voronoi identity includes the fifth inverse moment",
        "root_contribution": "Exploratory normalized cubic pair invariant and unverified distribution lead",
        "new_proposed_completion": "Fifth ratio plus normalized linear identity, bounded fibers and common-ratio polynomial contradiction",
        "novelty_established": False,
        "odd_annihilator_basis_character_nonvanishing_or_decomposition_count_imported": False,
    },
    "source_specific_Diophantine_normalization_rank_cancellation_nonzero_delta_size_remaining": True,
    "mathematical_program_scan_CAS_certificate_or_author_rerun": False,
    "cache_PDF_extraction_only_not_mathematical_evidence": True,
    "direct_weekly_telemetry": telemetry,
}
write_new(SOURCE_PATH, source_document)

all_inputs = (accepted_records + raw_records + acceptance_records
              + acceptance_metadata + context_records + cache_records
              + [older_manifest_record] + older_own)
input_output = {
    "checked_at_utc": NOW,
    "metadata_only_not_mathematical_evidence": True,
    "status": "candidate proof - unverified; integrity of complete UW1-UW4 construction checkpoint",
    "constructor": "review_2022_complexity_r2",
    "root_is_contributor_not_independent_reviewer": True,
    "new_independent_whole_audits_complete": 0,
    "two_OTHER_initially_blind_whole_audits_required": True,
    "complete_accepted_bodies_read_and_verified": accepted_records,
    "exact_accepted_raw_suffixes_verified": raw_records,
    "scope_acceptance_records_verified": acceptance_records,
    "declared_acceptance_metadata_rows_verified_not_all_claimed_fresh_report_reads": acceptance_metadata,
    "context_and_existing_cache_records_verified": context_records + cache_records,
    "all40_author_obligations_and6_issue_rows_present": True,
    "all_mathematics_symbolic_no_test_cases": True,
    "proposed_theorem_prime_threshold": 37,
    "no_small_prime_scan_or_extension_claim": True,
    "ordinary_root_count_not_CAS_or_finite_certificate": True,
    "unconditional_u_image_distribution_not_claimed": True,
    "original_augmentation_p_minus1_retained": True,
    "source_odd_annihilator_basis_and_decomposition_counts_not_assumed": True,
    "older_own_records": older_own,
    "older_own_unique_frozen_paths_preserved": len(older_own),
    "input_record_occurrences_verified": len(all_inputs),
    "input_unique_paths_verified": len({row["path"] for row in all_inputs}),
    "mathematical_program_scan_CAS_enumeration_certificate_or_author_rerun": False,
    "old_shared_Git_cache_other_owner_edits_spawning_contacts_charges_bypass": False,
    "new_Diophantine_exclusion_full_annual_solution_novelty_or_promotion_claim": False,
    "direct_weekly_telemetry": telemetry,
    "all_verified": True,
}
write_new(INPUT_PATH, input_output)
records = [fingerprint(PREFIX + suffix) for suffix in (
    "candidate-v1.md", "obligations-v1.md", "constructor-checks-v1.md",
    "source-audit-v1.md", "worklog-v1.md", "freeze-v1.py",
    "sources-v1.json", "input-validation-v1.json",
)]
manifest = {
    "frozen_at_utc": NOW,
    "status": "candidate proof - unverified; COMPLETE UW1-UW4 mathematical/source/failure checkpoint awaiting two OTHER whole audits",
    "constructor": "review_2022_complexity_r2",
    "root_exploratory_cubic_lead_contributor": True,
    "constructor_or_root_counted_as_independent_reviewer": False,
    "requested_model": "gpt-6.1-sol", "requested_reasoning_effort": "max",
    "verified_effective_setting_readback": None,
    "scope": "2025 B4(b) algebraic original-weight selection partial result; no Diophantine exclusion",
    "proposed_claims": {
        "UW1": "For p>=11, first/cubic/fifth inverse Fueter moments, 7w5+800w3+4608=0 and at most six points per w3 fiber",
        "UW2": "Exact abstract two-ratio separation under nonconstant nonzero u, more than30 points and six-point fibers",
        "UW3": "Every prime p>=37 admits TWO nonconjugate free positive I_f elements, each augmentation p-1, complement2N, coefficients0/1/2 and nonzero inverse first moment",
        "UW4": "Two disjoint free Fourier orbits at original weight; no reciprocal cross-set or higher-series transfer",
    },
    "author_obligations": 40,
    "constructor_issue_rows": 6,
    "new_independent_whole_audits_complete": 0,
    "two_OTHER_initially_blind_whole_nonconstructor_audits_required": True,
    "root_and_constructor_cannot_supply_independent_reviews": True,
    "old_MS_FS_OW_accepted_suffixes_exactly_unchanged": True,
    "whole_original_Section4_3_and_later_selection_appendices_read": True,
    "ordinary_moment_and_root_count_algebra_not_mathematical_code": True,
    "input_record_occurrences_verified": len(all_inputs),
    "input_unique_paths_verified": len({row["path"] for row in all_inputs}),
    "older_own_unique_frozen_paths_preserved": len(older_own),
    "source_specific_Diophantine_gaps_preserved": True,
    "new_Diophantine_exclusion_full_annual_answer_or_novelty": False,
    "mathematical_program_scan_CAS_certificate_or_author_rerun": False,
    "old_shared_Git_cache_other_owner_edits_spawning_contact_charge_or_bypass": False,
    "direct_weekly_telemetry": telemetry,
    "artifacts": records,
}
write_new(MANIFEST_PATH, manifest)
print(json.dumps({"manifest": fingerprint(MANIFEST_PATH), "artifacts": records,
                  "input_occurrences": len(all_inputs),
                  "unique_input_paths": len({row["path"] for row in all_inputs}),
                  "older_own_preserved": len(older_own), "all_verified": True},
                 indent=2, ensure_ascii=False))
