"""Administrative metadata only. No mathematical programs, scans or CAS."""
from pathlib import Path
import datetime
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2019-B4/notes/linear-output-return-r1-"


def read_json(path):
    return json.loads((ROOT / path).read_text())


def record(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def checked(expected):
    actual = record(expected["path"])
    assert all(actual[key] == value for key, value in expected.items()), (expected, actual)
    return actual


def unique_checked(records):
    result = {}
    for expected in records:
        actual = checked(expected)
        if actual["path"] in result:
            assert result[actual["path"]] == actual
        result[actual["path"]] = actual
    return list(result.values())


old_manifest_path = "problems/2019-B4/reviews/chronological-context-language-review-1-manifest-v1.json"
checked({"path": old_manifest_path, "bytes": 2942,
         "sha256": "6bc8f88023b8105a8656baebfd01a26012c994a3760bffa5ed4cb4f46a4c6f36"})
old_manifest = read_json(old_manifest_path)
old_validation = read_json("problems/2019-B4/reviews/chronological-context-language-review-1-input-validation-v1.json")
earlier = unique_checked(old_validation["earlier_unique_records_preserved"]
                         + old_manifest["artifacts"] + [record(old_manifest_path)])
assert len(earlier) == 229
prior_CCL_submission = unique_checked(old_validation["exact_target_and_all_three_declared_records"])
obligation_text = (ROOT / (PREFIX + "obligations-v1.md")).read_text()
assert re.findall(r"^\| (LO\d\d) \|", obligation_text, re.MULTILINE) == [f"LO{i:02d}" for i in range(1, 29)]

now = datetime.datetime.now(datetime.timezone.utc).isoformat()
context_paths = (
    "AGENTS.md", "problems/2019-B4/statement.md", "problems/2019-B4/proof.md",
    "problems/2019-B4/proofs/reviewed-secondpass-v1.1.md",
    "problems/2019-B4/proofs/reviewed-thirdpass-v1.1.md",
    "problems/2019-B4/proofs/reviewed-nonregularity-return-v1.1.md",
    "problems/2019-B4/references.md", "problems/2019-B4/notes/thirdpass-literature.md")
context = [record(path) for path in context_paths]
sources = {
    "recorded_at_utc": now,
    "candidate_status": "candidate proof - unverified",
    "new_external_growth_theorem_is_proof_premise": False,
    "coordinator_supplied_grammar_and_literature_leads": True,
    "primary_sources": [
        {"title": "Official2019 Paper B, B4(b)",
         "url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-paper-b_1.pdf",
         "read_scope": "Part(b) and exact insertion definition, page2; no preliminary proof",
         "binary_sha256": None, "viewer_hash_not_invented": True},
        {"author": "Tullio Ceccherini-Silberstein, sole author",
         "title": "Growth and ergodicity of context-free languages II: the linear case",
         "publication": "Transactions AMS359(2)(2007),605-618; electronic2006",
         "doi": "10.1090/S0002-9947-06-03958-4",
         "official_url": "https://www.ams.org/journals/tran/2007-359-02/S0002-9947-06-03958-4/S0002-9947-06-03958-4.pdf",
         "actual_full_published_text_viewed_at": "https://scispace.com/pdf/growth-and-ergodicity-of-context-free-languages-ii-the-4xfrjcv85s.pdf",
         "read_scope": "Complete published text through bounded overlapping viewer ranges; exact unweighted unambiguity hypothesis and section5 derivation weighting checked",
         "binary_sha256": None, "binary_download_succeeded": False,
         "external_full_theorem_imported_for_unmarked_word_counts": False},
        {"author": "Tullio Ceccherini-Silberstein",
         "title": "On the growth of linear languages",
         "publication": "Advances in Applied Mathematics35(3)(2005),243-253",
         "doi": "10.1016/j.aam.2005.01.002",
         "url": "https://www.sciencedirect.com/science/article/pii/S0196885805000321",
         "read_scope": "Primary publisher-indexed abstract only; full text not obtained",
         "unread_full_theorem_imported": False,
         "binary_sha256": None}
    ],
    "bounded_public_download_attempts": [
        {"source": "AMS publishedPDF", "curl_exit": 56, "http_status": 403,
         "max_time_seconds": 30, "bypass": False},
        {"source": "Citeseer parent lead", "curl_exit": 56, "http_status": 404,
         "max_time_seconds": 30, "exec_session": 82838, "completed_and_reaped": True,
         "bypass": False},
        {"source": "Public publishedPDF copy", "curl_exit": 56, "http_status": 403,
         "max_time_seconds": 30, "bypass": False}
    ],
    "successful_new_binary_cache_records": [],
    "input_fingerprints": context,
    "mathematical_program_CAS_scan_or_certificate_rerun": False,
}
sources_path = PREFIX + "sources-v1.json"
(ROOT / sources_path).write_text(json.dumps(sources, indent=2) + "\n")
validation = {
    "validated_at_utc": now,
    "metadata_not_mathematical_evidence": True,
    "accepted_existence_and_strict_bound_full_body_read": record("problems/2019-B4/proof.md"),
    "source_context_fingerprints": context,
    "earlier_unique_records_preserved": earlier,
    "earlier_unique_count": len(earlier),
    "prior_blind_CCL_submission_unchanged_but_not_a_proof_premise": prior_CCL_submission,
    "twenty_eight_obligations_present": True,
    "constructor_self_check_is_independent_audit": False,
    "ordinary_distinct_count_lambda_evaluated": False,
    "new_numerical_enclosure": False,
    "inherent_ambiguity_or_nonrationality_claimed": False,
    "weighted_bound_transferred_to_strict_comparison_with_lambda": False,
    "new_math_program_CAS_scan_or_author_rerun": False,
    "only_new_assigned_linear_output_notes_prefix_written": True,
    "shared_Git_spawning_contact_charge_or_bypass": False,
}
validation_path = PREFIX + "input-validation-v1.json"
(ROOT / validation_path).write_text(json.dumps(validation, indent=2) + "\n")
artifacts = [record(PREFIX + suffix) for suffix in (
    "candidate-v1.md", "obligations-v1.md", "source-audit-v1.md", "worklog-v1.md",
    "constructor-self-check-v1.md", "freeze-v1.py", "sources-v1.json", "input-validation-v1.json")]
manifest = {
    "frozen_at_utc": now,
    "status": "candidate proof - unverified; COMPLETE meaningful linear-output checkpoint requiring two other fresh initially blind whole audits",
    "constructor": "/root/review_2017_coarsening_r1",
    "coordinator_grammar_and_primary_literature_leads_acknowledged": True,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "claims": ["LO1 exact unmarked parity linear grammar", "LO2 original-output nonregularity and sentential occurrence condition",
               "LO3 exact derivation totals and exponential alternating-word ambiguity", "LO4 exact distinct overlap recurrence includingJ0",
               "LO5 recoverable overlap injections, same entropy and analytic normalization; failed Jclosure",
               "LO6 explicit weighted factor-avoidance bound only", "conditional finite proper unambiguous linear grammar gives rational word series"],
    "whole_audit_obligations": 28,
    "exact_lambda_full_annual_inherent_ambiguity_or_novelty_claim": False,
    "ordinary_growth_sensitivity_or_new_numerical_enclosure": False,
    "weighted_to_unweighted_entropy_transfer": False,
    "full_2005_source_import": False,
    "constructor_self_check_counted_as_other_independent_review": False,
    "earlier_unique_own_paths_verified_unchanged": len(earlier),
    "mathematical_program_CAS_scan_or_certificate_rerun": False,
    "old_frozen_texts_or_scopes_overwritten": False,
    "last_direct_weekly_telemetry": {"at_utc": "2026-10-17 11:59:03 UTC",
                                      "total_used_percent": 36, "window_minutes": 10080,
                                      "reset_unix": 1792745187, "total_ceiling_percent": 90,
                                      "integration_reserve": True},
    "administrative_command": "/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 " + PREFIX + "freeze-v1.py",
    "artifacts": artifacts,
}
manifest_path = PREFIX + "freeze-v1.json"
(ROOT / manifest_path).write_text(json.dumps(manifest, indent=2) + "\n")
print(json.dumps({"freeze": record(manifest_path), "artifacts": artifacts,
                  "earlier_unchanged": len(earlier), "whole_obligations": 28}, indent=2))
