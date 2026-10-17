"""Administrative fingerprints, read-scope records and JSON; no mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2019-B4/notes/reasoning-return-r7-"


def fp(path):
    data = (ROOT / path).read_bytes()
    return {"path": str(path), "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def checked(rec):
    actual = fp(rec["path"])
    if actual["bytes"] != rec["bytes"] or actual["sha256"] != rec["sha256"]:
        raise RuntimeError("Fingerprint mismatch: " + rec["path"])
    return dict(actual, matches=True)


def read_json(path):
    return json.loads((ROOT / path).read_text())


def all_fps(obj):
    if isinstance(obj, dict):
        if {"path", "bytes", "sha256"} <= obj.keys():
            yield obj
        for value in obj.values():
            yield from all_fps(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from all_fps(value)


def save(suffix, obj):
    path = ROOT / (PREFIX + suffix)
    if path.exists():
        raise RuntimeError("Refusing to overwrite: " + str(path))
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


for suffix in ["sources-v1.json", "input-validation-v1.json", "freeze-output-v1.json", "freeze-v1.json"]:
    assert not (ROOT / (PREFIX + suffix)).exists()
now = datetime.now(timezone.utc).isoformat()
base = "problems/2019-B4/"
accepted_paths = [
    base + "proof.md", base + "reviews/acceptance.md", base + "reviews/acceptance.json",
    base + "proofs/reviewed-secondpass-v1.1.md",
    base + "notes/secondpass-canonical-renewal.md",
    base + "reviews/secondpass-acceptance.md", base + "reviews/secondpass-acceptance.json",
    base + "proofs/reviewed-thirdpass-v1.1.md",
    base + "proofs/reviewed-moment-tail-v1.1.md",
    base + "reviews/moment-tail-acceptance.json",
]
context_paths = [
    "AGENTS.md", base + "statement.md",
    base + "proofs/reviewed-linear-output-return-v1.1.md",
    base + "proofs/reviewed-nonregularity-return-v1.1.md",
    base + "proofs/reviewed-chronological-context-language-v1.1.md",
    base + "reviews/linear-output-return-acceptance.json",
    base + "reviews/nonregularity-return-acceptance.json",
    base + "reviews/chronological-context-language-acceptance.json",
    base + "notes/coordinator-unmarked-greedy-failure-v1.md",
    base + "notes/coordinator-relational-normal-form-followup-v1.md",
    base + "notes/thirdpass-literature.md",
    base + "notes/thirdpass-literature-sources.json",
    base + "notes/reasoning-return-r3-source-audit-v1.md",
]
secondpass_authority = read_json(base + "reviews/secondpass-acceptance.json")
secondpass_rows = []
for relative, expected in secondpass_authority["artifacts"].items():
    row = fp(base + relative)
    assert row["sha256"] == expected
    secondpass_rows.append(dict(row, matches=True))
authority_paths = [
    base + "reviews/moment-tail-acceptance.json",
    base + "reviews/linear-output-return-acceptance.json",
    base + "reviews/nonregularity-return-acceptance.json",
    base + "reviews/chronological-context-language-acceptance.json",
]
authority_rows = [checked(rec) for path in authority_paths
                  for rec in all_fps(read_json(path))]
literature_source_rows = [checked(rec) for rec in all_fps(
    read_json(base + "notes/thirdpass-literature-sources.json"))]

previous_input_path = "problems/2025-B4/reviews/reciprocal-kernel-review-1-input-validation-v1.json"
previous_manifest_path = "problems/2025-B4/reviews/reciprocal-kernel-review-1-manifest-v1.json"
assert fp(previous_manifest_path)["sha256"] == "9acbcc65b0b41d5bc24a1681c698bca95d17e179ebc8353b5f971b48a42a2698"
previous_input = read_json(previous_input_path)
older = []
for item in previous_input["older_own_packets"]:
    older.append({"manifest": checked(item["manifest"]),
                  "checks": [checked(rec) for rec in item["checks"]]})
older.append({"manifest": fp(previous_manifest_path),
              "checks": [checked(rec) for rec in read_json(previous_manifest_path)["records"]]})
assert len(older) == 51
gk_addendum = checked(previous_input["GK_separate_telemetry_addendum_preserved"])
obligations = (ROOT / (PREFIX + "obligations-v1.md")).read_text()
assert set(re.findall(r"\|R7-O(\d\d)\|", obligations)) == {
    str(i).zfill(2) for i in range(1, 41)}
candidate = (ROOT / (PREFIX + "candidate-v1.md")).read_text()
for label in ["R7A", "R7B", "R7C", "R7D"]:
    assert label in candidate
usage = {"at_utc": "2026-10-17 14:17:21 UTC (direct telemetry followed by UTC clock)",
         "total_used_percent": 44, "window_minutes": 10080,
         "reset_unix": 1792745187, "total_ceiling_percent": 90,
         "integration_reserve": True, "ordinary_usage_allowed": True}
sources = {
    "recorded_at_utc": now, "status": "candidate proof - unverified",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "complete_mathematical_prerequisite_bodies_and_scopes_read": [fp(path) for path in accepted_paths],
    "complete_context_and_exact_language_boundaries_read_not_new_premises": [fp(path) for path in context_paths],
    "primary_actual_reads": [
        {"url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-paper-b_1.pdf",
         "scope": "Official p2 B4(b), distinct-string operations and root-rate target; no preliminary proof"},
        {"url": "https://users.renyi.hu/~p_erdos/1949-01.pdf",
         "title": "Erdos-Feller-Pollard, A property of power series with positive coefficients",
         "publication": "Bull. Amer. Math. Soc.55(1949),201-204",
         "doi": "10.1090/S0002-9904-1949-09203-0",
         "scope": "COMPLETE original four-page article, both printed proof routes and finite/infinite mean distinction; adjacent Brunk article not a premise",
         "hypotheses": "Proper nonnegative law and support not periodic; would match critical Q because q0=0, total1 and q1>0",
         "generic_local_renewal_theorem_imported_as_needed_premise": False,
         "new_binary_hash_or_cache_identity_claim": None},
        {"url": "https://arxiv.org/pdf/2402.17953",
         "title": "Koga, A Proof of Basic Limit Theorem of Renewal Theory",
         "edition": "arXiv2402.17953v2,2024-03-28",
         "scope": "Abstract, complete Theorem1.1, section2 convolution identities and displayed section3 finite/infinite-mean discussion; not full seven-page proof",
         "new_theorem_imported": False, "new_binary_hash": None},
        {"url": "https://air.unimi.it/handle/2434/4919",
         "title": "Goldwurm-Wich, Unambiguous Turn Position and Rational Trace Languages",
         "scope": "Primary repository metadata and indexed snippets only; full newklaus.pdf403, theorem/proof unread and unused",
         "new_theorem_imported": False},
    ],
    "failed_retrievals": [
        "Goldwurm-Wich full repository file403; no bypass",
        "Combinatorica EFP URL502 gateway; independent public Renyi author archive succeeded",
        "AMS EFP web viewer route unsupported; no full file obtained there",
        "Guessed local deep-literature-r2-report-v1 filename absent; actual thirdpass-literature located and read",
    ],
    "primary_full_PDF_download_cache_mutation_or_redistribution": False,
    "classical_renewal_theory_attributed_and_novelty_unestablished": True,
    "new_generic_renewal_theorem_or_complete_language_classification_claim": False,
}
save("sources-v1.json", sources)
validation = {
    "checked_at_utc": now, "metadata_only_not_mathematical_evidence": True,
    "accepted_current_inputs": [fp(path) for path in accepted_paths],
    "context_current_inputs": [fp(path) for path in context_paths],
    "secondpass_authority_declared_SHA_records": secondpass_rows,
    "other_accepted_authority_declared_fingerprints": authority_rows,
    "older_literature_cache_fingerprints_preserved_not_all_fresh_paper_reads": literature_source_rows,
    "older_own_packets": older, "all_fifty_one_older_own_packets_unchanged": True,
    "GK_separate_telemetry_addendum_preserved": gk_addendum,
    "assigned_prefix_confirmed_unused_before_first_write": True,
    "all40_obligation_labels_present": True,
    "candidate_status_unverified_and_two_OTHER_whole_audits_required": True,
    "old_NR_authorship_and_moment_CCL_LO_whole_review_roles_disclosed": True,
    "root_generic_research_assignment_not_new_normalization_ratio_or_trichotomy_contribution": True,
    "actual_F_not_finite_cap_and_unknown_true_R_retained": True,
    "positive_tail_mass_gap_zero_and_infinite_second_moment_all_retained": True,
    "raw_consecutive_ratios_not_claimed_monotone": True,
    "original_b_consecutive_ratio_limit_not_inferred_from_marked_fibers": True,
    "no_evaluated_lambda_new_numeric_enclosure_or_algebraicity_claim": True,
    "queued_2024_NJ_v1_or_v2_and_2020_return_targets_or_new_peer_findings_read": False,
    "only_current_assigned_prefix_written": True,
    "old_candidate_review_shared_cache_or_Git_mutation": False,
    "mathematical_program_CAS_scan_enumeration_certificate_replay_or_author_rerun": False,
    "spawning_charge_contact_or_access_bypass": False,
}
save("input-validation-v1.json", validation)
output = {
    "checked_at_utc": now, "metadata_only_not_mathematical_evidence": True,
    "claims": ["R7A", "R7B", "R7C", "R7D"], "whole_obligations": 40,
    "accepted_current_input_records": len(accepted_paths),
    "context_current_input_records": len(context_paths),
    "secondpass_authority_records_checked": len(secondpass_rows),
    "other_authority_fingerprint_occurrences_checked": len(authority_rows),
    "older_literature_cache_fingerprint_occurrences_checked": len(literature_source_rows),
    "older_own_packets_unchanged": len(older), "all_hash_checks_passed": True,
    "status": "candidate proof - unverified; complete mathematical/source/failure checkpoint",
    "exact_growth_value_selected_regime_new_numeric_or_novelty": False,
    "two_OTHER_fresh_whole_nonconstructor_audits_required": True,
    "latest_authoritative_weekly_usage": usage,
    "command": "python3 problems/2019-B4/notes/reasoning-return-r7-freeze-v1.py",
}
save("freeze-output-v1.json", output)
names = ["candidate-v1.md", "obligations-v1.md", "failed-routes-v1.md",
         "researchlog-v1.md", "source-audit-v1.md", "sources-v1.json",
         "freeze-v1.py", "input-validation-v1.json", "freeze-output-v1.json"]
manifest = {
    "frozen_at_utc": now, "status": "candidate proof - unverified",
    "constructor": "/root/review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "claims": ["R7A positive tail-kernel normalization and bounded increments",
               "R7B strict consecutive canonical-ratio limit/infimum and adjacent-count algebraic enclosures",
               "R7C complete defect/critical finite-mean/critical infinite-mean normalized-count alternatives",
               "R7D all-parity seed-one fiber refinement and conditional critical original lower prefactor"],
    "whole_independent_audit_obligations": 40,
    "requires_two_OTHER_fresh_initially_blind_nonconstructor_whole_audits": True,
    "root_supplied_new_normalization_ratio_or_moment_regime_proof": False,
    "classical_renewal_theory_attributed_not_claimed_new": True,
    "generic_local_renewal_theorem_needed_as_new_external_premise": False,
    "actual_delta_zero_positive_and_F_second_moment_alternatives_retained": True,
    "raw_c_ratio_monotonicity_or_original_b_ratio_convergence_claim": False,
    "evaluated_lambda_complete_F_or_ordinary_unambiguous_grammar_claim": False,
    "new_numeric_full_annual_algebraicity_or_novelty_claim": False,
    "mathematical_program_CAS_scan_enumeration_certificate_or_author_rerun": False,
    "old_shared_Git_cache_mutation_spawning_charge_contact_or_bypass": False,
    "queued_2024_and2020_targets_or_new_peer_findings_read_before_freeze": False,
    "older_own_packets_unchanged": len(older), "latest_authoritative_weekly_usage": usage,
    "command": output["command"], "artifacts": [fp(PREFIX + name) for name in names],
}
save("freeze-v1.json", manifest)
print(json.dumps(dict(output, candidate=fp(PREFIX + "candidate-v1.md"),
                      manifest=fp(PREFIX + "freeze-v1.json")), indent=2))
