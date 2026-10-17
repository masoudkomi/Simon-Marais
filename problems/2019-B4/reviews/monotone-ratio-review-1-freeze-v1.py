"""Complete MR1/conditional-MR2 initially blind WHOLE R1 metadata freeze.

No mathematical program, recurrence evaluation, scan, CAS, certificate
replay or constructor execution. Only the assigned NEW reviewer prefix
is written. Other NEW MR peer report/ledger/findings remain unread.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2019-B4/reviews/monotone-ratio-review-1-"
INPUT_PATH = PREFIX + "input-validation-v1.json"
MANIFEST_PATH = PREFIX + "manifest-v1.json"
NOW = datetime.now(timezone.utc).isoformat()


def safe_path(path):
    assert isinstance(path, str)
    assert not path.startswith(
        "problems/2019-B4/reviews/monotone-ratio-review-2-"), path
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


def legacy_artifact_rows(document):
    rows = []
    artifacts = document.get("artifacts")
    if isinstance(artifacts, dict):
        for path, digest in artifacts.items():
            if isinstance(digest, str) and re.fullmatch(r"[0-9a-f]{64}", digest):
                full_path = path if path.startswith("problems/") else "problems/2019-B4/" + path
                rows.append(verify({"path": full_path, "sha256": digest}))
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
    "path": "problems/2019-B4/notes/coordinator-monotone-ratio-return-v1.md",
    "bytes": 9239,
    "sha256": "67649f48ebd0f599461fa01cde4e5c37c8fdff0781b9decf4430705848396c29",
})
target_manifest = verify({
    "path": "problems/2019-B4/notes/coordinator-monotone-ratio-manifest-v1.json",
    "bytes": 1763,
    "sha256": "0af3087adb6814707b7c9257985256b882def1081f339a371b456af4f88dec8f",
})
constructor = read_json(target_manifest["path"])
assert constructor["constructor"] == "coordinator root"
assert constructor["whole_obligations"] == 12
assert len(constructor["records"]) == 1
assert len(constructor["accepted_inputs"]) == 5
constructor_records = [verify(row) for row in constructor["records"]]
declared_inputs = [verify(row) for row in constructor["accepted_inputs"]]

complete_new_and_accepted_texts = [fingerprint(path) for path in (
    "problems/2019-B4/statement.md",
    "problems/2019-B4/notes/secondpass-canonical-renewal.md",
    "problems/2019-B4/proofs/reviewed-secondpass-v1.1.md",
    "problems/2019-B4/proofs/reviewed-reasoning-return-r7-v1.1.md",
    "problems/2019-B4/proof.md",
    "problems/2019-B4/reviews/acceptance.md",
    "problems/2019-B4/reviews/secondpass-acceptance.md",
    "problems/2019-B4/notes/secondpass-checkpoint-2.md",
    "problems/2019-B4/notes/reasoning-return-r7-sources-v1.json",
)]
unverified_joining_context = fingerprint(
    "problems/2019-B4/notes/coordinator-short-joining-research-v1.md")
acceptance_records = []
acceptance_metadata = []
legacy_rows = []
for path in (
        "problems/2019-B4/reviews/acceptance.json",
        "problems/2019-B4/reviews/secondpass-acceptance.json",
        "problems/2019-B4/reviews/reasoning-return-r7-acceptance.json"):
    acceptance_records.append(fingerprint(path))
    document = read_json(path)
    acceptance_metadata.extend(metadata_rows(document))
    legacy_rows.extend(legacy_artifact_rows(document))
r7_source_metadata = metadata_rows(read_json(
    "problems/2019-B4/notes/reasoning-return-r7-sources-v1.json"))

accepted_r7_path = "problems/2019-B4/proofs/reviewed-reasoning-return-r7-v1.1.md"
raw_r7_path = "problems/2019-B4/notes/reasoning-return-r7-candidate-v1.md"
assert safe_path(accepted_r7_path).read_bytes().endswith(
    safe_path(raw_r7_path).read_bytes())
suffix_rows = [fingerprint(accepted_r7_path), fingerprint(raw_r7_path)]
suffix_comparison = {
    "accepted": suffix_rows[0], "raw": suffix_rows[1],
    "entire_frozen_raw_submission_is_byte_identical_suffix": True,
    "secondpass_accepted_register_is_NOT_mistaken_for_the_linked_renewal_body": True,
}

previous_manifest_record = verify({
    "path": "problems/2024-B4/reviews/Hermitian-all-index-review-1-manifest-v1.json",
    "bytes": 3610,
    "sha256": "84a0d744f4f6c4a418b227e96b522a8e3923af506ceb213feacf38d63e21799c",
})
previous_validation_record = verify({
    "path": "problems/2024-B4/reviews/Hermitian-all-index-review-1-input-validation-v1.json",
    "bytes": 1139896,
    "sha256": "02be412947f9893705087d03286b2b07e486cb2ee2f95a77e7ea5dc9d4388f18",
})
previous_manifest = read_json(previous_manifest_record["path"])
previous_validation = read_json(previous_validation_record["path"])
older_own = unique_records(previous_validation["older_own_records"]
                           + previous_manifest["records"]
                           + [previous_manifest_record])
assert len(older_own) == 277
previous_metadata = metadata_rows(previous_validation)
previous_metadata.extend(metadata_rows(previous_manifest))

main_text = safe_path(target_main["path"]).read_text()
inline_obligation_numbers = re.findall(r"^(\d+)\. ", main_text, re.MULTILINE)
assert inline_obligation_numbers == [str(i) for i in range(1, 13)]
ledger = safe_path(PREFIX + "issues-v1.md").read_text()
ledger_ids = re.findall(r"^\|(MRR1-\d\d)\|", ledger, re.MULTILINE)
assert ledger_ids == [f"MRR1-{i:02d}" for i in range(1, 33)]
assert {f"MR-O{i:02d}" for i in range(1, 13)} <= set(re.findall(r"MR-O\d\d", ledger))
for suffix in ("initial-v1.md", "issues-v1.md", "source-checks-v1.md"):
    assert safe_path(PREFIX + suffix).is_file()

telemetry = {
    "at_utc": "2026-10-17T15:11:09+00:00",
    "source": "direct authoritative account-wide telemetry paired with UTC clock",
    "total_used_percent": 47, "window_duration_minutes": 10080,
    "resets_at_unix": 1792745187, "ordinary_usage_allowed": True,
    "total_used_ceiling_percent": 90, "integration_reserve": True,
}
all_inputs = ([protocol, target_main, target_manifest] + constructor_records
              + declared_inputs + complete_new_and_accepted_texts
              + [unverified_joining_context] + acceptance_records
              + acceptance_metadata + legacy_rows + r7_source_metadata
              + suffix_rows + [previous_manifest_record, previous_validation_record]
              + previous_metadata + older_own)
validation = {
    "checked_at_utc": NOW,
    "reviewer": "/root/review_2022_complexity_r2",
    "status": "COMPLETE initially blind NONCONSTRUCTOR WHOLE MR1 and conditional MR2 R1; no substantive scoped issue; not promotion",
    "requested_model": "gpt-6.1-sol", "requested_reasoning_effort": "max",
    "independently_verified_effective_settings": None,
    "metadata_only_not_mathematical_evidence": True,
    "new_MR_peer_report_ledger_or_conclusions_read": False,
    "new_MR_constructor_or_proof_contributor": False,
    "root_is_constructor_excluded_from_independent_MR_audits": True,
    "older_moment_NR_LO_R7_review_roles_disclosed_not_fresh_recertification": True,
    "constructor_one_mathematical_record_verified": constructor_records,
    "constructor_five_declared_accepted_input_records_verified": declared_inputs,
    "complete_main_including_inline_sources_worklog_and12_obligations_read": True,
    "complete_actual_additional_mathematical_and_source_texts_read": complete_new_and_accepted_texts,
    "complete_acceptance_JSONs_read": acceptance_records,
    "acceptance_declared_metadata_only_not_new_old_peer_report_reads": acceptance_metadata,
    "legacy_relative_artifact_maps_verified": legacy_rows,
    "R7_source_declared_rows_verified_not_every_old_context_fresh_reread": r7_source_metadata,
    "accepted_R7_original_suffix_comparison": suffix_comparison,
    "short_joining_research_note_read_UNVERIFIED_not_premise": unverified_joining_context,
    "short_joining_J2_or_length8_diagnostic_recertified_or_rerun": False,
    "entire_a_sequence_positivity_and_all_recurrence_indices_checked": True,
    "MR1_strict_all_n_ge3_and_exact_equality_indices_reconstructed": True,
    "MR2_uniform_J_C_explicitly_UNPROVED": True,
    "MR2_variable_bridge_disjoint_union_empty_cases_and_fixed_C_limit_reconstructed": True,
    "R7_ratio_limit_unconditional_and_boundedness_equivalence_reconstructed": True,
    "inline_author_obligation_numbers": inline_obligation_numbers,
    "complete_new_reviewer_inference_checks": ledger_ids,
    "substantive_new_issues": 0,
    "author_repair_requested": False,
    "actual_positive_defect_or_J_C_claim": False,
    "new_external_theorem_imported": False,
    "primary_web_actual_read_scopes": [{
        "url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-paper-b_1.pdf",
        "scope": "Actual p2 B4(b), distinct-string rules and root-rate target; no preliminary proof investigation",
    }],
    "classical_EFP_actual_full_read_belongs_to_older_R7_audit_not_claimed_new_MR_read": True,
    "new_native_PDF_download_cache_identity_or_binary_hash_claim": False,
    "combined_read_truncation_resolved": {
        "affected_scope": "Short portion of R7 acceptance introductory paragraph in a combined tool output",
        "resolution": "Complete lines1-90 reread; all mathematical body and acceptance limitations actually read",
    },
    "mathematical_program_scan_CAS_certificate_or_constructor_rerun": False,
    "new_numeric_original_b_ratio_lower_root_monotonicity_annual_or_novelty_claim": False,
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
    "status": "COMPLETE initially blind NONCONSTRUCTOR WHOLE MR1 and conditional MR2 R1; no substantive scoped issue; not promotion",
    "requested_model": "gpt-6.1-sol", "requested_reasoning_effort": "max",
    "independently_verified_effective_settings": None,
    "constructor_target_main": target_main,
    "constructor_target_manifest": target_manifest,
    "whole_claims_reviewed": [
        "MR1 complete general positive signed-recurrence ratio induction",
        "MR1 exact initial values and strict every n>=3 log-concavity with unconditional R7 limiting upper endpoints",
        "MR2 CONDITIONALLY on UNPROVED one uniform J_C: variable bridge injection, fixed limit order, normalized bound and exact defect inequality",
        "complete accepted-language/source/diagnostic/role/official/annual boundaries",
    ],
    "all12_constructor_obligations_covered": True,
    "complete_reviewer_inference_checks": len(ledger_ids),
    "substantive_issues_identified": 0,
    "author_repair_requested": False,
    "initial_frozen_before_any_new_peer_MR_findings": True,
    "new_MR_nonconstructor_independence": True,
    "older_moment_NR_LO_R7_review_roles_explicitly_disclosed": True,
    "unproved_joining_not_promoted_and_diagnostic_excluded_from_premises": True,
    "actual_positive_defect_or_J_C_claim": False,
    "new_external_theorem_imported": False,
    "mathematical_program_scan_CAS_certificate_or_constructor_rerun": False,
    "new_numeric_original_b_ratio_lower_root_monotonicity_annual_or_novelty_claim": False,
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
