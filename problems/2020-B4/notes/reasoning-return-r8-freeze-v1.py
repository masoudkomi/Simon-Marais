#!/usr/bin/env python3
"""Administrative-only freeze for R8; no mathematical computation or scan."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2020-B4/notes/reasoning-return-r8-"
TELEMETRY = {"at_utc": "2026-10-17 20:17:23 UTC", "total_used_percent": 63,
             "window_minutes": 10080, "reset_unix": 1792745187,
             "ordinary_usage_allowed": True, "total_ceiling_percent": 90,
             "review_integration_reserve": True}


def record(path):
    data = (ROOT / path).read_bytes()
    return {"path": str(path), "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def verify(row):
    expected = {key: row[key] for key in ("path", "bytes", "sha256")}
    actual = record(row["path"])
    if actual != expected:
        raise RuntimeError(("Unexpected fingerprint", expected, actual))
    return actual


def read_json(path):
    return json.loads((ROOT / path).read_text())


def write_new(suffix, value):
    path = PREFIX + suffix
    with (ROOT / path).open("x") as handle:
        json.dump(value, handle, indent=2)
        handle.write("\n")
    return record(path)


def summary(rows):
    unique = {}
    for row in rows:
        old = unique.setdefault(row["path"], row)
        if old != row:
            raise RuntimeError(("Conflicting fingerprint", old, row))
    encoded = json.dumps([unique[key] for key in sorted(unique)],
                         sort_keys=True, separators=(",", ":")).encode()
    return {"occurrences": len(rows), "unique_paths": len(unique),
            "canonical_deduplicated_summary_sha256": hashlib.sha256(encoded).hexdigest(),
            "canonical_encoding": "UTF8 JSON sorted unique path/bytes/sha256, sorted keys, compact separators"}


def main():
    for suffix in ("sources-v1.json", "input-validation-v1.json",
                   "freeze-output-v1.json", "freeze-v1.json"):
        if (ROOT / (PREFIX + suffix)).exists():
            raise RuntimeError("Refuse any overwrite of an existing output")
    baseline_row = record(PREFIX + "baseline-v1.json")
    assert baseline_row["bytes"] == 13188
    assert baseline_row["sha256"] == \
        "866f7e18fc46ed38713aa76e496848e098191e3260cb7263b1fae6a6aee825e9"
    baseline = read_json(baseline_row["path"])
    direct = [verify(row) for row in baseline["direct_scope_context_and_failed_route_records"]]
    authority = [verify(row) for row in baseline["R7_accepted_authority_declared_records"]]
    parents = [{"metadata": verify(row["metadata"]),
                "declared_prior_occurrences": row["declared_prior_occurrences"]}
               for row in baseline["R7_immutable_metadata_parents"]]
    r7_packet = [verify(row) for row in baseline["R7_declared_frozen_artifacts_unchanged"]]
    own_rows = [verify(row) for row in baseline["own_parent_new_records"]]
    own_manifest = verify(baseline["compact_own_parent_manifest"])
    own_validation = verify(baseline["compact_own_parent_validation"])
    old_rows = direct + authority + [row["metadata"] for row in parents] + \
        r7_packet + own_rows + [own_validation]
    old_summary = summary(old_rows)
    assert old_summary["occurrences"] == baseline["necessary_current_fingerprint_occurrences"] == 54
    assert old_summary["unique_paths"] == baseline["necessary_current_unique_paths"] == 40
    assert old_summary["canonical_deduplicated_summary_sha256"] == \
        baseline["canonical_deduplicated_summary_sha256"]
    assert baseline["older_own_paths_bound_transitively"] == 409
    assert len(own_rows) == 9 and len(r7_packet) == 10 and len(parents) == 7
    accepted_r7 = verify(baseline["exact_accepted_R7"])
    r7_candidate = next(row for row in authority if row["path"].endswith("reasoning-return-r7-candidate-v1.md"))
    assert (ROOT / accepted_r7["path"]).read_bytes().endswith((ROOT / r7_candidate["path"]).read_bytes())
    assert (ROOT / "problems/2020-B4/proofs/reviewed-reasoning-return-r5-v1.1.md").read_bytes().endswith(
        (ROOT / "problems/2020-B4/notes/reasoning-return-r5-candidate-v1.md").read_bytes())
    accepted_integrity = read_json("problems/2020-B4/reviews/reasoning-return-r7-acceptance-integrity.json")
    assert baseline["R7_acceptance_declared_historical_summary_bound_not_replayed"] == {
        "occurrences": accepted_integrity["record_occurrences"],
        "unique_paths": accepted_integrity["unique_paths"]}

    prose_suffixes = ["candidate-v1.md", "obligations-v1.md", "failed-routes-v1.md",
                      "constructor-checks-v1.md", "source-audit-v1.md", "worklog-v1.md"]
    prose = [record(PREFIX + suffix) for suffix in prose_suffixes]
    main_text = (ROOT / prose[0]["path"]).read_text()
    obligations = (ROOT / prose[1]["path"]).read_text()
    ids = re.findall(r"^\|(R8-\d{2})\|(.+)\|$", obligations, re.MULTILINE)
    assert [row[0] for row in ids] == ["R8-%02d" % index for index in range(1, 55)]
    assert all(len(row[1]) > 50 for row in ids)
    assert all("**R8" + letter + ".**" in main_text for letter in "ABCDEF")
    assert "candidate proof - unverified" in main_text.lower()
    assert "For a fixed a with o(a)=0" in main_text

    sources = {
        "recorded_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "candidate proof - unverified; COMPLETE meaningful constructor source checkpoint",
        "constructor": "/root/review_2022_complexity_r2",
        "requested_settings": baseline["requested_settings"],
        "independently_verified_effective_settings": None,
        "exact_accepted_R7": accepted_r7,
        "R7_full_body_header_acceptance_md_json_integrity_freshly_read": True,
        "R4_full_repaired_and_R6_full_accepted_bodies_freshly_read": True,
        "R5_complete_math_plus_accepted_header_and_exact_suffix_read_verified": True,
        "R3_actual_read_scope": "complete repair ledger; candidate SectionsF3,F3a,B1/final scope only, not entire current body",
        "prior_R3_R4_misses_R5_R6_R7_failures_and_deep_source_limits_preserved": True,
        "primary_sources": [
            {"title": "Official SMMC2020 Paper B",
             "url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2020-paper-b_1.pdf",
             "actual_read_scope": "page2 B4 full hypothesis and(b); no preliminary construction or unrelated problem investigation",
             "fresh_native_PDF_sha256": None},
            {"title": "Kedlaya, Class Field Theory, Theorem7.2.10",
             "url": "https://kskedlaya.org/cft/sec_ideles-cohom2.html",
             "actual_read_scope": "complete Hasse norm theorem statement/short proof and noncyclic warning, returned lines618-643; nearby context",
             "import": "classical cyclic number-field all-place norm theorem; underlying deep theory attributed, not re-proved",
             "fresh_native_PDF_sha256": None},
            {"title": "Milne, Class Field Theory4.03,6August2020, VIII Theorem3.1",
             "url": "https://jmilne.org/math/CourseNotes/CFT.pdf",
             "actual_read_scope": "title/version, complete Hasse theorem/short proof and Remark3.2, printed234-235/PDF242-243; not all296pages",
             "fresh_native_PDF_sha256": None},
            {"title": "Kedlaya, Class Field Theory, Propositions4.2.4-4.2.5",
             "url": "https://kskedlaya.org/cft/sec_localcomp.html",
             "actual_read_scope": "complete finite residue norm and unramified-unit norm statements/proofs, returned lines449-478, nearby context",
             "import": "classical unit norm argument reconstructed including residue characteristic2",
             "fresh_native_PDF_sha256": None},
            {"title": "Lemmermeyer, The Ambiguous Class Number Formula Revisited, arXiv1309.1071v1",
             "url": "https://arxiv.org/pdf/1309.1071",
             "actual_read_scope": "COMPLETE six-page original author preprint/all353 extracted lines, especially Proposition1 complete exact sequence/proof",
             "use": "classical ambiguous/strongly ambiguous norm-unit obstruction; full quadratic proof reconstructed in main",
             "fresh_native_PDF_sha256": None},
            {"title": "Lemmermeyer, Ideal Class Groups of Cyclotomic Number Fields I, arXiv1202.5777v1",
             "url": "https://arxiv.org/pdf/1202.5777",
             "actual_read_scope": "CM/ideal/unit notation, Proposition1 and applicable proof passages, essential ramification definition, Theorem1 and applicable proof, Example1 and nearby context, PDF0-4; not entire11pages",
             "use": "Hasse prime-conductor unit-index/capitulation attribution; exact specialized proof supplied independently in main",
             "fresh_native_PDF_sha256": None}
        ],
        "limited_or_failed_source_leads": [
            {"title": "Folk, When are global units norms of units?, Acta Arith.76(1996),145-147",
             "url": "https://matwbn.icm.edu.pl/ksiazki/aa/aa76/aa7624.pdf",
             "actual_scope": "journal metadata and indexed first-page introduction/Theorem1 statement only; full PDF403/publisher redirect failed; no full proof read/import"},
            {"title": "Schmidt, Cyclotomic Integers of Prescribed Absolute Value and the Class Group",
             "url": "https://personal.ntu.edu.sg/bernhard/Publications/pub/class.pdf",
             "actual_scope": "unreadable PDF encoding; screenshot calls returned no pixels to worker; publisher abstract/publication list only; no precise theorem import"},
            {"title": "Zhu, Algebraic Number Theory II",
             "url": "https://yhzhumath.github.io/ANT2.pdf",
             "actual_scope": "discovery corroboration: Remark1.21.4 and Hasse theorem2.7.6 statement/start only; no additional proof premise or full83page read"}
        ],
        "ordinary_class_groups_not_narrow": True,
        "root_broad_assignment_no_new_R8_proof_contribution": True,
        "old_R4_R5_R7_authorship_and_R6_review_disclosed_no_self_recertification": True,
        "two_OTHER_fresh_initially_blind_WHOLE_nonconstructor_audits_required": True,
        "no_new_taut_or_excluded_order_unrestricted_classification_cutoff_or_novelty": True,
        "no_mathematical_code_CAS_scan_class_table_certificate_or_author_rerun": True,
        "no_new_PDF_cache_write_old_shared_Git_edit_spawn_contact_charge_or_bypass": True,
        "immutable_historical_summary_bound_not_recursively_replayed": baseline["R7_acceptance_declared_historical_summary_bound_not_replayed"],
        "necessary_current_fingerprints_reverified": old_summary,
        "compact_own_parent_manifest": own_manifest,
        "compact_own_parent_validation": own_validation,
        "older_own_paths_bound_transitively": 409,
        "direct_weekly_telemetry": TELEMETRY}
    sources_row = write_new("sources-v1.json", sources)
    freezer_row = record(PREFIX + "freeze-v1.py")
    current = prose + [baseline_row, freezer_row, sources_row]
    validation = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "administrative_only_not_mathematical_evidence": True,
        "baseline": baseline_row,
        "all_necessary_baseline_fingerprints_unchanged": True,
        "exact_accepted_R7": accepted_r7,
        "R7_accepted_math_is_exact_frozen_candidate_suffix": True,
        "R5_accepted_math_is_exact_freshly_read_candidate_suffix": True,
        "necessary_old_records": old_summary,
        "R7_acceptance_historical_summary_bound_not_replayed": baseline["R7_acceptance_declared_historical_summary_bound_not_replayed"],
        "immutable_R7_verification_parent_count": len(parents),
        "old_R7_frozen_artifact_count_unchanged": len(r7_packet),
        "compact_own_parent_manifest": own_manifest,
        "compact_own_parent_validation": own_validation,
        "older_own_paths_bound_transitively": 409,
        "historical_inventory_not_recopied_or_claimed_freshly_reread": True,
        "new_constructor_records": current,
        "all_current_input_and_new_record_summary": summary(old_rows + current),
        "all54_whole_obligation_rows_present_once": True,
        "whole_claims": ["R8A", "R8B", "R8C", "R8D", "R8E", "R8F"],
        "independent_review_count_for_NEW_R8": 0,
        "two_OTHER_whole_reviews_still_required": True,
        "no_mathematical_program_CAS_scan_or_author_rerun": True,
        "no_old_shared_Git_cache_edit_spawn_contact_charge_or_bypass": True,
        "source_record": sources_row,
        "direct_weekly_telemetry": TELEMETRY}
    validation_row = write_new("input-validation-v1.json", validation)
    output_row = write_new("freeze-output-v1.json", {
        "finished_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "candidate proof - unverified; COMPLETE meaningful mathematical constructor checkpoint",
        "whole_claims": ["R8A", "R8B", "R8C", "R8D", "R8E", "R8F"],
        "all54_obligations_present": True,
        "two_OTHER_whole_audits_outstanding": True,
        "necessary_old_occurrences_reverified": 54,
        "necessary_old_unique_paths": 40,
        "older_own_paths_bound_transitively": 409,
        "all_current_record_summary": validation["all_current_input_and_new_record_summary"],
        "main": prose[0], "input_validation": validation_row,
        "no_math_code_or_class_group_computation": True})
    artifacts = prose + [baseline_row, freezer_row, sources_row, validation_row, output_row]
    freeze = {
        "frozen_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "candidate proof - unverified; COMPLETE meaningful constructor checkpoint",
        "constructor": "/root/review_2022_complexity_r2",
        "requested_settings": baseline["requested_settings"],
        "independently_verified_effective_settings": None,
        "whole_claims": ["R8A", "R8B", "R8C", "R8D", "R8E", "R8F"],
        "all_whole_obligations": 54,
        "extra_prime_modulus_and_odd_T_containing_every_prime_divisor_retained": True,
        "odd_hF_unit_correction_is_conditional_sufficiency_for_actual_positive_sets": True,
        "principality_not_asserted_automatic": True,
        "Gamma_even_class_number_cases_not_universally_discharged": True,
        "full_multiplier_stabilizer_is_exact_ideal_not_ideal_class": True,
        "classical_Hasse_and_ambiguous_class_theory_attributed": True,
        "exact_accepted_R7": accepted_r7,
        "independent_NEW_R8_whole_audits_completed": 0,
        "two_OTHER_fresh_initially_blind_WHOLE_nonconstructor_reviews_required": True,
        "root_broad_assignment_only_no_new_proof_inference": True,
        "old_author_review_roles_disclosed_no_fresh_self_recertification": True,
        "no_new_unconditional_taut_excluded_order_full_classification_cutoff_or_novelty": True,
        "no_preliminary_construction_or_other_problem_investigation": True,
        "no_mathematical_executable_CAS_scan_class_table_certificate_or_author_rerun": True,
        "no_old_shared_Git_cache_edit_spawn_contact_charge_or_bypass": True,
        "no_new_2024_packet_or_peer_findings_read": True,
        "necessary_old_fingerprint_occurrences_reverified": 54,
        "necessary_old_unique_paths": 40,
        "current_inputs_and_new_records": validation["all_current_input_and_new_record_summary"],
        "R7_historical_acceptance_summary_bound_not_replayed": baseline["R7_acceptance_declared_historical_summary_bound_not_replayed"],
        "compact_own_parent_manifest": own_manifest,
        "compact_own_parent_validation": own_validation,
        "older_own_paths_bound_transitively": 409,
        "historical_inventory_not_copied": True,
        "direct_weekly_telemetry": TELEMETRY,
        "administrative_command": "python3 " + PREFIX + "freeze-v1.py",
        "artifacts": artifacts}
    freeze_row = write_new("freeze-v1.json", freeze)
    for row in old_rows + artifacts + [freeze_row]:
        verify(row)
    print(json.dumps({"freeze": freeze_row, "main": prose[0],
                      "obligations": prose[1], "source_audit": prose[4],
                      "failures": prose[2], "input_validation": validation_row,
                      "all54_obligations": True, "candidate_unverified": True,
                      "two_OTHER_whole_audits_required": True,
                      "artifacts_plus_freeze": len(artifacts) + 1,
                      "old_bytes_preserved": True}, indent=2))


if __name__ == "__main__":
    main()
