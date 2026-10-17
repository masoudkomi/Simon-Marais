"""Metadata-only initially blind WHOLE V1-V4 review2 freeze; no math code.

Creates only new assigned review outputs and refuses replacing any file.
Run: python3 problems/2017-B4/reviews/global-value-return-review-2-freeze-v1.py
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/reviews/global-value-return-review-2-"
AUTHOR = "problems/2017-B4/notes/global-value-return-r1-"
INPUT_PATH = PREFIX + "input-validation-v1.json"
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


for path in (INPUT_PATH, MANIFEST_PATH):
    assert not (ROOT / path).exists(), path

author_manifest_record = verify({
    "path": AUTHOR + "manifest-v1.json",
    "sha256": "61a261da6ae345a9255b8e9f5ea06cf697af2a1663c8bad4bc4f2010b5eeae53",
})
author_manifest = read_json(author_manifest_record["path"])
author_artifacts = [verify(row) for row in author_manifest["artifacts"]]
assert len(author_artifacts) == 8
verify({"path": AUTHOR + "candidate-v1.md", "bytes": 23428,
        "sha256": "d70cda1ce140e989d4d37d062c9c6c55e562db7044ba4302b6183ee91603c016"})
author_sources = read_json(AUTHOR + "sources-v1.json")
author_source_rows = metadata_rows(author_sources)
author_validation_rows = metadata_rows(read_json(AUTHOR + "input-validation-v1.json"))

full_context_records = [verify(row) for row in
                        author_sources["direct_full_logical_or_protocol_context_reads"]]
transitive_records = [verify(row) for row in author_sources[
    "global_ten_accepted_transitive_interfaces_checked_against_frozen_source_hashes"]]
assert len(transitive_records) == 10
cache_records = [verify(row) for row in author_sources["existing_cache_fingerprints"]]
verify({"path": "AGENTS.md", "bytes": 4707,
        "sha256": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"})
direct_full_read_paths = (
    "AGENTS.md", "problems/2017-B4/statement.md",
    "problems/2017-B4/references.md", "problems/2017-B4/research.md",
    "problems/2017-B4/proofs/reviewed-direction-coarsening-v1.1.md",
    "problems/2017-B4/proofs/reviewed-allD-global-v1.1.md",
    "problems/2017-B4/proofs/reviewed-concavity-v1.1.md",
    "problems/2017-B4/notes/allD-global-reasoning-r1-sources-v1.md",
    "problems/2017-B4/notes/coordinator-global-limit-literature-recheck-v1.md",
    "problems/2017-B4/reviews/allD-global-acceptance.md",
    "problems/2017-B4/reviews/coarsening-acceptance.md",
    "problems/2017-B4/reviews/concavity-acceptance.md",
)
direct_full_reads = [fingerprint(path) for path in direct_full_read_paths]

older_manifest_record = verify({
    "path": "problems/2021-B4/reviews/reasoning-return-r6-review-2-manifest-v1.json",
    "bytes": 2976,
    "sha256": "c20819e298135ae72f8e1ac53f682985c39b3ede4d338dba6b933886b23cd7f4",
})
older_manifest = read_json(older_manifest_record["path"])
older_validation = read_json(
    "problems/2021-B4/reviews/reasoning-return-r6-review-2-input-validation-v1.json")
older_own = unique_records(older_validation["older_own_records"]
                           + older_manifest["artifacts"]
                           + [older_manifest_record])
assert len(older_own) == 223

obligations = (ROOT / (AUTHOR + "obligations-v1.md")).read_text()
assert re.findall(r"^\| (GV-O\d\d) \|", obligations, re.MULTILINE) == [
    f"GV-O{i:02d}" for i in range(1, 41)]
ledger = (ROOT / (PREFIX + "issues-v1.md")).read_text()
assert re.findall(r"^\|(GVR2-C\d\d)\|", ledger, re.MULTILINE) == [
    f"GVR2-C{i:02d}" for i in range(1, 49)]

telemetry = {
    "at_utc": "2026-10-17T13:18:06+00:00",
    "source": "direct account-wide usage tool paired with UTC clock",
    "total_used_percent": 41, "window_duration_minutes": 10080,
    "resets_at_unix": 1792745187, "ordinary_usage_allowed": True,
    "total_used_cutoff_percent": 90, "integration_reserve": True,
}
primary_scopes = [
    {"url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-2_1.pdf",
     "actual_read_scope": "Live p2 B4 official domain/count/conclusion; no unrelated problem investigated",
     "new_binary_hash": None},
    {"url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-solutions-preliminary_1.pdf",
     "actual_read_scope": "Live p12 B4/comments and commutation-class identification; no preliminary proof investigated",
     "new_binary_hash": None},
    {"url": "https://arxiv.org/pdf/2502.20909v2",
     "actual_read_scope": "Abstract, printed pp1-2 introduction, simple/marked/orientation definition and dated scalar limit context",
     "old_full_bound_proof_or_certificate_rerun": False},
    {"url": "https://drops.dagstuhl.de/storage/00lipics/lipics-vol293-socg2024/LIPIcs.SoCG.2024.43/LIPIcs.SoCG.2024.43.pdf",
     "actual_read_scope": "Abstract/introduction printed43:1-43:3, marked definitions, scalar context, Theorem1/outline",
     "complete_computational_lower_proof_or_certificate_rerun": False},
    {"url": "https://annals.math.princeton.edu/wp-content/uploads/annals-v171-n3-p12-p.pdf",
     "actual_read_scope": "Abstract, Theorems1.1/1.3, Sections2.1-2.2 definitions, Theorem3.1 full proof,3.2 statement/factor-proof passage, full Lemma3.4/Cor3.5/Theorem1.3 proof through printed2021",
     "new_theorem_applied_to_L_or_ell_D": False,
     "full_paper_sections4_to9_or_binary_hash_claimed": False},
]
all_inputs = ([author_manifest_record] + author_artifacts + author_source_rows
              + author_validation_rows + full_context_records + transitive_records
              + cache_records + direct_full_reads + older_own)
input_output = {
    "checked_at_utc": NOW,
    "metadata_only_not_mathematical_evidence": True,
    "reviewer": "review_2022_complexity_r2",
    "new_constructor": "review_2017_coarsening_r1",
    "reviewer_constructed_or_contributed_to_NEW_V1_to_V4": False,
    "reviewer_older_allD_global_authorship_and_local_review_roles_disclosed": True,
    "older_G1_to_G3_is_separately_accepted_premise_not_new_self_audit": True,
    "requested_model": "gpt-6.1-sol",
    "requested_reasoning_effort": "max",
    "verified_effective_setting_readback": None,
    "initially_blind_to_new_V_peer_reports_and_findings": True,
    "author_manifest": author_manifest_record,
    "all_eight_author_artifacts_verified": author_artifacts,
    "author_source_metadata_rows_verified": author_source_rows,
    "author_input_validation_rows_verified_not_all_claimed_fresh_reads": author_validation_rows,
    "full_context_current_hashes_checked_against_author_records": full_context_records,
    "direct_full_mathematical_body_context_and_scope_reads": direct_full_reads,
    "ten_older_accepted_transitive_interfaces_current_hashes_checked": transitive_records,
    "existing_cache_hashes_verified_not_new_downloads": cache_records,
    "primary_actual_read_scopes": primary_scopes,
    "all40_author_obligations_and48_review_checks_present": True,
    "per_inference_checks": 48,
    "substantive_issues_identified": 0,
    "required_author_repairs": 0,
    "complete_finite_rank_code_and_effectiveness_abstract_sequence_reconstructed": True,
    "E_and_R_remain_explicit_extra_unproved_hypotheses": True,
    "V4_is_not_tiling_GE_or_SFT_counterexample": True,
    "old_finite_certificates_rerun_or_newly_recertified": False,
    "older_own_records": older_own,
    "older_own_unique_frozen_paths_preserved": len(older_own),
    "input_record_occurrences_verified": len(all_inputs),
    "input_unique_paths_verified": len({row["path"] for row in all_inputs}),
    "mathematical_program_scan_CAS_enumeration_certificate_or_author_rerun": False,
    "old_shared_Git_cache_other_owner_edits_spawning_contacts_charges_bypass": False,
    "actual_L_computability_noncomputability_numeric_value_or_full_annual_solution_claim": False,
    "novelty_or_coordinator_promotion_claim": False,
    "direct_weekly_telemetry": telemetry,
    "all_verified": True,
}
write_new(INPUT_PATH, input_output)
records = [fingerprint(PREFIX + suffix) for suffix in (
    "initial-v1.md", "issues-v1.md", "source-checks-v1.md",
    "freeze-v1.py", "input-validation-v1.json",
)]
manifest = {
    "frozen_at_utc": NOW,
    "status": "complete fresh initially blind nonconstructor WHOLE V1-V4 review2; no substantive defect identified in exact scopes",
    "reviewer": "review_2022_complexity_r2",
    "new_constructor": "review_2017_coarsening_r1",
    "reviewer_constructed_or_contributed_to_NEW_V1_to_V4": False,
    "older_global_authorship_and_local_review_roles_disclosed": True,
    "requested_model": "gpt-6.1-sol",
    "requested_reasoning_effort": "max",
    "verified_effective_setting_readback": None,
    "new_V_peer_findings_read_before_complete_initial_freeze": False,
    "full_main_source_log_and_all40_obligations_read": True,
    "whole_independent_mathematical_reconstruction": True,
    "per_inference_checks": 48,
    "substantive_issues_identified": 0,
    "required_author_repairs": 0,
    "E_and_R_remain_explicit_extra_unproved_hypotheses": True,
    "V4_is_abstract_not_actual_tiling_counterexample": True,
    "mathematical_program_scan_CAS_enumeration_certificate_or_author_rerun": False,
    "old_shared_Git_cache_other_owner_edits_spawning_contact_charge_or_bypass": False,
    "full_value_computability_noncomputability_novelty_or_coordinator_promotion_claim": False,
    "author_manifest": author_manifest_record,
    "author_artifacts_verified": len(author_artifacts),
    "input_record_occurrences_verified": len(all_inputs),
    "input_unique_paths_verified": len({row["path"] for row in all_inputs}),
    "older_own_unique_frozen_paths_preserved": len(older_own),
    "direct_weekly_telemetry": telemetry,
    "artifacts": records,
}
write_new(MANIFEST_PATH, manifest)
print(json.dumps({"manifest": fingerprint(MANIFEST_PATH), "artifacts": records,
                  "input_occurrences": len(all_inputs),
                  "unique_input_paths": len({row["path"] for row in all_inputs}),
                  "older_own_preserved": len(older_own), "all_verified": True},
                 indent=2, ensure_ascii=False))
