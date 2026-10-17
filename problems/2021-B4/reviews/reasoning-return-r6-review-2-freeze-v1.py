"""Metadata-only initially blind WHOLE R6 review2 freeze; no math code.

Run: python3 problems/2021-B4/reviews/reasoning-return-r6-review-2-freeze-v1.py
Only the assigned review prefix is created; existing outputs are refused.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2021-B4/reviews/reasoning-return-r6-review-2-"
AUTHOR = "problems/2021-B4/notes/reasoning-return-r6-"
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
    rows = {}
    for record in records:
        actual = verify(record)
        if actual["path"] in rows:
            assert rows[actual["path"]] == actual
        rows[actual["path"]] = actual
    return [rows[path] for path in sorted(rows)]


def write_new(path, document):
    assert path.startswith(PREFIX)
    with (ROOT / path).open("x") as stream:
        json.dump(document, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


for output in (INPUT_PATH, MANIFEST_PATH):
    assert not (ROOT / output).exists(), output

author_manifest_record = verify({
    "path": AUTHOR + "freeze-v1.json", "bytes": 2937,
    "sha256": "9c97c3b704fb2b53ce8108991ffca70e04a01760dcbadb8d2712ba339bc24538",
})
author_manifest = read_json(author_manifest_record["path"])
author_artifacts = [verify(row) for row in author_manifest["records"]]
assert len(author_artifacts) == 8
verify({"path": AUTHOR + "candidate-v1.md", "bytes": 17290,
        "sha256": "ad49ac369ce903131ad496b0e0f70fe2b966dca7507490860449bdde36eb7594"})
author_sources = read_json(AUTHOR + "sources-v1.json")
author_source_rows = metadata_rows(author_sources)
author_validation_rows = metadata_rows(read_json(AUTHOR + "input-validation-v1.json"))

full_body_records = [verify(row) for row in (
    author_sources["complete_accepted_bodies_and_registers"]
    + author_sources["relevant_complete_old_mathematical_bodies_reread"]
    + author_sources["complete_acceptance_MD_records_read"])]
linked_body_records = [fingerprint(path) for path in (
    "problems/2021-B4/notes/padic-rational-newton-obstructions-v1.md",
    "problems/2021-B4/notes/coordinator-three-rational-witnesses-v1.md",
)]
direct_context_records = [fingerprint(path) for path in (
    "AGENTS.md", "problems/2021-B4/statement.md",
    "problems/2021-B4/notes/reasoning-return-r5-source-audit-v1.md",
    "problems/2021-B4/notes/ghosh-source-reviewed-register-v1.1.md",
)]
verify({"path": "AGENTS.md", "bytes": 4707,
        "sha256": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"})
accepted_metadata_records = []
for path in (
    "problems/2021-B4/reviews/reasoning-return-r5-acceptance.json",
    "problems/2021-B4/reviews/return-r3-acceptance.json",
    "problems/2021-B4/reviews/reasoning-J15-acceptance.json",
    "problems/2021-B4/reviews/odd-support-exclusion-acceptance.json",
):
    accepted_metadata_records.append(fingerprint(path))
    accepted_metadata_records.extend(metadata_rows(read_json(path)))

# Preserve every earlier own artifact through the COMPLETE author repair.
older_manifest_record = verify({
    "path": "problems/2020-B4/notes/reasoning-return-r4-freeze-v1.1.json",
    "bytes": 3877,
    "sha256": "a76d1879815282839e87cf51b6a488279d213b11e1d5f00c8f216bbc44cc7b66",
})
older_manifest = read_json(older_manifest_record["path"])
older_inputs = read_json("problems/2020-B4/notes/reasoning-return-r4-input-validation-v1.1.json")
older_own = unique_records(older_inputs["older_own_records"]
                           + older_manifest["artifacts"]
                           + [older_manifest_record])
assert len(older_own) == 217

author_obligations = (ROOT / (AUTHOR + "obligations-v1.md")).read_text()
assert re.findall(r"^\| (R6-\d\d) \|", author_obligations, re.MULTILINE) == [
    f"R6-{i:02d}" for i in range(1, 37)]
review_ledger = (ROOT / (PREFIX + "issues-v1.md")).read_text()
assert re.findall(r"^\|(R6R2-C\d\d)\|", review_ledger, re.MULTILINE) == [
    f"R6R2-C{i:02d}" for i in range(1, 49)]

telemetry = {
    "at_utc": "2026-10-17T13:01:15+00:00",
    "source": "direct account-wide Codex usage tool paired with UTC clock",
    "total_used_percent": 40, "window_duration_minutes": 10080,
    "resets_at_unix": 1792745187, "ordinary_usage_allowed": True,
    "total_used_cutoff_percent": 90, "integration_reserve": True,
}
primary_scopes = [
    {"url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf",
     "actual_read_scope": "Live page2 B4 official hypothesis and(b); no preliminary proof investigated",
     "new_binary_hash": None},
    {"url": "https://arxiv.org/pdf/1208.5404",
     "actual_read_scope": "Live equation7,Section3.4 equations9-10/simple-center discussion, Lemma17/adjacent center context, Prop19 statement/proof passage and unramified-field remark",
     "full23_page_proof_or_old_computation_newly_reconstructed": False,
     "all_roots_rational_or_unramified_hypothesis_not_silently_assumed": True,
     "cache_and_live_viewer_byte_identity_claimed": False},
    {"url": "https://arxiv.org/html/2608.14726v1",
     "actual_read_scope": "Centered support definitions and full displayed TheoremB, coefficient nonvanishing and one-nonzero-recycled-root/multi-root boundary",
     "new_theorem_imported_for_R6": False,
     "full_external_proof_or_binary_hash_claimed": False},
]
all_inputs = ([author_manifest_record] + author_artifacts + author_source_rows
              + author_validation_rows + full_body_records + linked_body_records
              + direct_context_records + accepted_metadata_records + older_own)
input_output = {
    "checked_at_utc": NOW,
    "metadata_only_not_mathematical_evidence": True,
    "reviewer": "review_2022_complexity_r2",
    "new_constructor": "review_2021_reasoning_j15_r2",
    "reviewer_constructed_or_supplied_new_R6_lead": False,
    "old_R3_R5_and_single_center_review_roles_disclosed": True,
    "requested_model": "gpt-6.1-sol",
    "requested_reasoning_effort": "max",
    "verified_effective_setting_readback": None,
    "initially_blind_to_new_R6_peer_reports_and_findings": True,
    "author_manifest": author_manifest_record,
    "all_eight_author_artifacts_verified": author_artifacts,
    "author_source_metadata_rows_verified_not_all_claimed_fresh_report_reads": author_source_rows,
    "author_input_validation_rows_verified": author_validation_rows,
    "complete_accepted_bodies_relevant_immutable_texts_and_scope_MDs_read": full_body_records,
    "complete_linked_Newton_and_T1_mathematical_bodies_read": linked_body_records,
    "direct_full_context_reads": direct_context_records,
    "accepted_register_metadata_rows_verified": accepted_metadata_records,
    "primary_actual_read_scopes": primary_scopes,
    "all36_author_obligations_and48_review_checks_present": True,
    "per_inference_checks": 48,
    "substantive_issues_identified": 0,
    "required_author_repairs": 0,
    "exact_actual_double_J15_m2_soleH3_ladder_and_unit_hypotheses_reset": True,
    "finite_and_zero_displacement_and_nu1_checked": True,
    "nonzero_nonunit_essential_constant_not_trivial_unit_center_checked": True,
    "global_carrier_and_simple_center_full_gcd_refinement_checked": True,
    "independent_hand_rho_inverse_certificate_not_program": True,
    "old_finite_certificates_rerun_or_newly_recertified": False,
    "older_own_records": older_own,
    "older_own_unique_frozen_paths_preserved": len(older_own),
    "input_record_occurrences_verified": len(all_inputs),
    "input_unique_paths_verified": len({row["path"] for row in all_inputs}),
    "mathematical_program_scan_CAS_enumeration_certificate_or_author_rerun": False,
    "old_shared_Git_cache_other_owner_edits_spawning_contacts_charges_bypass": False,
    "full_degree20_annual_classification_novelty_or_coordinator_promotion_claim": False,
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
    "status": "complete fresh initially blind nonconstructor WHOLE R6A-R6C review2; no substantive defect identified in exact scope",
    "reviewer": "review_2022_complexity_r2",
    "new_constructor": "review_2021_reasoning_j15_r2",
    "reviewer_constructed_or_contributed_to_R6": False,
    "old_R3_R5_single_center_review_roles_disclosed": True,
    "requested_model": "gpt-6.1-sol",
    "requested_reasoning_effort": "max",
    "verified_effective_setting_readback": None,
    "new_R6_peer_findings_read_before_complete_initial_freeze": False,
    "full_main_source_log_and_all36_obligations_read": True,
    "whole_independent_mathematical_reconstruction": True,
    "per_inference_checks": 48,
    "substantive_issues_identified": 0,
    "required_author_repairs": 0,
    "independent_hand_five_case_certificate_and_all_actual_witness_cases": True,
    "accepted_old_certificate_reruns_or_new_recertification_claim": False,
    "mathematical_program_scan_CAS_enumeration_certificate_or_author_rerun": False,
    "old_shared_Git_cache_other_owner_edits_spawning_contact_charge_or_bypass": False,
    "complete_degree20_or_novelty_or_coordinator_promotion_claim": False,
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
