"""Freeze the COMPLETE initially blind HR whole R1: metadata only.

No mathematical evaluation, finite-field point scan, CAS, certificate or
constructor execution. No other NEW HR report/ledger/conclusions read.
Only NEW files in the explicitly assigned reviewer prefix are written.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2024-B4/reviews/Hermitian-all-index-review-1-"
INPUT_PATH = PREFIX + "input-validation-v1.json"
MANIFEST_PATH = PREFIX + "manifest-v1.json"
NOW = datetime.now(timezone.utc).isoformat()


def safe_path(path):
    assert isinstance(path, str)
    assert not path.startswith(
        "problems/2024-B4/reviews/Hermitian-all-index-review-2-"), path
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
    result = []
    if isinstance(document, dict):
        if (isinstance(document.get("path"), str)
                and isinstance(document.get("sha256"), str)
                and re.fullmatch(r"[0-9a-f]{64}", document["sha256"])):
            result.append(verify(document))
        for value in document.values():
            result.extend(metadata_rows(value))
    elif isinstance(document, list):
        for value in document:
            result.extend(metadata_rows(value))
    return result


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
    "path": "problems/2024-B4/notes/coordinator-Hermitian-all-index-return-v1.md",
    "bytes": 15281,
    "sha256": "296241f7538f7eb86315998ff760f4fa363d3a2d1c911988d6fa2b1a4f0287cc",
})
target_manifest = verify({
    "path": "problems/2024-B4/notes/coordinator-Hermitian-all-index-manifest-v1.json",
    "bytes": 3214,
    "sha256": "d93f76bb4aecc912bb9dc91a51714d41330d250ba333ca7a32061d39a36df0a3",
})
constructor = read_json(target_manifest["path"])
assert len(constructor["records"]) == 4
assert len(constructor["accepted_and_context_inputs"]) == 8
assert constructor["whole_obligations"] == 24
assert constructor["constructor"] == "coordinator root"
constructor_records = [verify(row) for row in constructor["records"]]
declared_inputs = [verify(row) for row in constructor["accepted_and_context_inputs"]]
statement = fingerprint("problems/2024-B4/statement.md")

accepted_full_bodies = [fingerprint(path) for path in (
    "problems/2024-B4/proofs/reviewed-generalized-Kasami-v1.1.md",
    "problems/2024-B4/proofs/reviewed-composition-Kasami-v1.1.md",
    "problems/2024-B4/proofs/reviewed-even-inner-next-jet-v2.1.md",
)]
historical_lead = fingerprint(
    "problems/2024-B4/notes/coordinator-odd-period-composition-lead-v1.md")
acceptance_records = []
acceptance_metadata = []
for path in (
        "problems/2024-B4/reviews/generalized-Kasami-acceptance.json",
        "problems/2024-B4/reviews/composition-Kasami-acceptance.json",
        "problems/2024-B4/reviews/even-inner-next-jet-acceptance.json"):
    acceptance_records.append(fingerprint(path))
    acceptance_metadata.extend(metadata_rows(read_json(path)))

suffix_comparisons = []
suffix_rows = []
for accepted, raw in (
        ("problems/2024-B4/proofs/reviewed-generalized-Kasami-v1.1.md",
         "problems/2024-B4/notes/coordinator-generalized-Kasami-r1-candidate-v1.md"),
        ("problems/2024-B4/proofs/reviewed-composition-Kasami-v1.1.md",
         "problems/2024-B4/notes/reasoning-return-r3-candidate-v1.md"),
        ("problems/2024-B4/proofs/reviewed-even-inner-next-jet-v2.1.md",
         "problems/2024-B4/notes/coordinator-even-inner-next-jet-return-v2.md")):
    assert safe_path(accepted).read_bytes().endswith(safe_path(raw).read_bytes())
    accepted_row, raw_row = fingerprint(accepted), fingerprint(raw)
    suffix_rows.extend((accepted_row, raw_row))
    suffix_comparisons.append({
        "accepted": accepted_row, "raw": raw_row,
        "entire_frozen_raw_submission_is_byte_identical_suffix": True,
    })

previous_manifest_record = verify({
    "path": "problems/2019-B4/reviews/reasoning-return-r7-review-2-manifest-v1.json",
    "bytes": 3120,
    "sha256": "d99d74f831a0138a50450579c71f3bc8ce0d990de27352a2d317594e9029a532",
})
previous_validation_record = verify({
    "path": "problems/2019-B4/reviews/reasoning-return-r7-review-2-input-validation-v1.json",
    "bytes": 1069619,
    "sha256": "fe0dadfced6b19e92d6b00ad3fec30031c0d4eec353c7fc774ef6081300677b8",
})
previous_manifest = read_json(previous_manifest_record["path"])
previous_validation = read_json(previous_validation_record["path"])
older_own = unique_records(previous_validation["older_own_records"]
                           + previous_manifest["records"]
                           + [previous_manifest_record])
assert len(older_own) == 271
previous_metadata = metadata_rows(previous_validation)
previous_metadata.extend(metadata_rows(previous_manifest))

obligation_text = safe_path(
    "problems/2024-B4/notes/coordinator-Hermitian-all-index-obligations-v1.md").read_text()
obligation_ids = re.findall(r"^\|(HR-O\d\d)\|", obligation_text, re.MULTILINE)
assert obligation_ids == [f"HR-O{i:02d}" for i in range(1, 25)]
ledger = safe_path(PREFIX + "issues-v1.md").read_text()
ledger_ids = re.findall(r"^\|(HRR1-\d\d)\|", ledger, re.MULTILINE)
assert ledger_ids == [f"HRR1-{i:02d}" for i in range(1, 49)]
assert set(obligation_ids) <= set(re.findall(r"HR-O\d\d", ledger))
for suffix in ("initial-v1.md", "issues-v1.md", "source-checks-v1.md"):
    assert safe_path(PREFIX + suffix).is_file()

telemetry = {
    "at_utc": "2026-10-17T15:02:19+00:00",
    "source": "direct authoritative account-wide telemetry paired with UTC clock",
    "total_used_percent": 46, "window_duration_minutes": 10080,
    "resets_at_unix": 1792745187, "ordinary_usage_allowed": True,
    "total_used_ceiling_percent": 90, "integration_reserve": True,
}
primary_reads = [
    {
        "url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf",
        "scope": "Actual page2 B4(b) official quantifiers/coefficientwise polynomial meaning; no preliminary proof investigation",
    },
    {
        "url": "https://arxiv.org/pdf/1509.00797",
        "edition": "Milne, arXiv1509.00797v1, September2015",
        "scope": "Complete curve-bound statement printed1-2 and complete modern geometric proof printed6-10 through final Frobenius application; not entire67pages or original Weil sources/foundational proof chains",
        "role": "Classical unconditional Hasse--Weil curve LOWER bound",
    },
    {
        "url": "https://stacks.math.columbia.edu/tag/0BYA",
        "scope": "Entire mathematical Section53.9 through Lemma53.9.4, complete53.9.1-.3 proofs and Fermat smoothness paragraph; infinite-field lemma not applied",
        "role": "Standard plane genus formula and smoothness hypothesis context",
    },
    {
        "url": "https://stacks.math.columbia.edu/tag/0B2N",
        "scope": "Complete Lemma33.34.3 statement/proof and supporting affine Lemma33.34.2; no claim to reprove full foundational dimension theory",
        "role": "Nonempty intersection of two projective plane curve components over algebraic closure",
    },
    {
        "url": "https://backend.orbit.dtu.dk/ws/portalfiles/portal/216803443/Complete_list_of_genera_Montanucci_Zini.pdf",
        "scope": "Deposit metadata, opening general Hermitian definition/genus discussion and Section2 displayed Fermat model; not full quotient-classification proof",
        "role": "Context only; restricted q=1mod4 quotient hypotheses fail for even q and are not imported",
    },
]
all_inputs = ([protocol, target_main, target_manifest] + constructor_records
              + declared_inputs + [statement] + accepted_full_bodies
              + [historical_lead] + acceptance_records + acceptance_metadata
              + suffix_rows + [previous_manifest_record, previous_validation_record]
              + previous_metadata + older_own)
validation = {
    "checked_at_utc": NOW,
    "reviewer": "/root/review_2022_complexity_r2",
    "status": "COMPLETE initially blind NONCONSTRUCTOR whole HR1/HR2 R1; no substantive scoped issue; not promotion",
    "requested_model": "gpt-6.1-sol", "requested_reasoning_effort": "max",
    "independently_verified_effective_settings": None,
    "metadata_only_not_mathematical_evidence": True,
    "new_HR_peer_report_ledger_or_conclusions_read": False,
    "new_HR_constructor_or_proof_contributor": False,
    "root_is_constructor_excluded_from_independent_HR_audits": True,
    "older_GK_and_NJ_whole_review_roles_disclosed_not_fresh_recertification": True,
    "old_CP_not_falsely_claimed_as_own_original_independent_audit": True,
    "constructor_four_records_verified": constructor_records,
    "constructor_eight_accepted_and_context_records_verified": declared_inputs,
    "complete_new_main_obligations_sources_worklog_read": True,
    "complete_accepted_mathematical_bodies_read": accepted_full_bodies,
    "complete_acceptance_JSONs_read": acceptance_records,
    "acceptance_declared_metadata_only_not_new_old_peer_report_reads": acceptance_metadata,
    "accepted_original_suffix_comparisons": suffix_comparisons,
    "official_statement_read": statement,
    "historical_odd_period_lead_read_NOT_theorem_premise": historical_lead,
    "complete_constructor_obligation_ids": obligation_ids,
    "complete_new_reviewer_inference_checks": ledger_ids,
    "substantive_new_issues": 0,
    "author_repair_requested": False,
    "all_index_r_ge2_not_extension_only_audit": True,
    "r2_endpoint_independently_reconstructed": True,
    "full_two_dimensional_every_shift_return_and_exact_order_q_reconstructed": True,
    "all_later_multiple_persistence_and_bottom_inverse_coefficient_checked": True,
    "both_fixed_family_whole_divisor_directions_and_exceptions_checked": True,
    "primary_web_actual_read_scopes": primary_reads,
    "new_native_PDF_download_cache_identity_or_binary_hash_claim": False,
    "mathematical_program_point_scan_CAS_certificate_or_author_rerun": False,
    "annual_other_component_mixed_q_arbitrary_inner_or_novelty_claim": False,
    "read_only_administrative_filename_correction": {
        "initial_attempts": [
            "cat problems/2019-B4/reviews/reasoning-return-r7-review-2-manifest.json",
            "sed -n '1,240p' problems/2019-B4/reviews/reasoning-return-r7-review-2-freeze.py",
        ],
        "outcome": "Both missing-v1 filename guesses exited1 without mutation; exact own names obtained via rg --files and read successfully",
        "mathematical_or_integrity_failure": False,
    },
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
    "status": "COMPLETE initially blind NONCONSTRUCTOR whole HR1/HR2 R1; no substantive scoped issue; not promotion",
    "requested_model": "gpt-6.1-sol", "requested_reasoning_effort": "max",
    "independently_verified_effective_settings": None,
    "constructor_target_main": target_main,
    "constructor_target_manifest": target_manifest,
    "whole_claims_reviewed": [
        "HR1 EVERY inner r>=2 and EVERY target s>=1 over arbitrary algebraically closed characteristic2 K",
        "HR2 BOTH fixed-q whole homogeneous divisor directions with r1 and equality exceptions",
        "degree reduction, smooth geometric curve/genus/Hasse--Weil LOWER bound and bad-point count",
        "full shifted two-dimensional return, exact local orderq and complete matrix perturbation persistence",
        "independent full r2 endpoint, arbitrary/inseparable outer and forbidden coefficient",
        "complete source/official/dependency/old-context/annual boundaries",
    ],
    "all24_constructor_obligations_covered": True,
    "complete_reviewer_inference_checks": len(ledger_ids),
    "substantive_issues_identified": 0,
    "author_repair_requested": False,
    "initial_frozen_before_any_new_peer_HR_findings": True,
    "new_HR_nonconstructor_independence": True,
    "older_GK_NJ_roles_and_CP_dependency_scope_explicitly_disclosed": True,
    "source_hypotheses_actual_scopes_and_classical_attribution_recorded": True,
    "mathematical_program_point_scan_CAS_certificate_or_author_rerun": False,
    "annual_other_component_mixed_q_arbitrary_inner_or_novelty_claim": False,
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
