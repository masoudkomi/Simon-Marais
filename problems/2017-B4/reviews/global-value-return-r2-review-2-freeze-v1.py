"""Metadata-only complete OP1-OP3 initially blind whole R2 freeze.

No mathematical program, enumeration, certificate/CAS or author rerun.
All new outputs are exclusively created within this review prefix.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/reviews/global-value-return-r2-review-2-"
INPUT_PATH = PREFIX + "input-validation-v1.json"
MANIFEST_PATH = PREFIX + "manifest-v1.json"
NOW = datetime.now(timezone.utc).isoformat()


def safe_path(path):
    assert "global-value-return-r2-review-1-" not in path, path
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

protocol = verify({"path": "AGENTS.md", "bytes": 4707,
                   "sha256": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"})
target_main = verify({
    "path": "problems/2017-B4/notes/global-value-return-r2-candidate-v1.md",
    "bytes": 22228,
    "sha256": "49045e601d8934cbeb282b78162a34652b3a50772df66987b3c21280936befdc",
})
target_freeze = verify({
    "path": "problems/2017-B4/notes/global-value-return-r2-manifest-v1.json",
    "bytes": 3351,
    "sha256": "05b38b4c3af797def7910863d731b72e6d747b1fd945a4167a6e994270d892e6",
})
constructor = read_json(target_freeze["path"])
assert len(constructor["artifacts"]) == 8
assert constructor["author_obligations"] == 48
constructor_records = [verify(row) for row in constructor["artifacts"]]
source_path = "problems/2017-B4/notes/global-value-return-r2-sources-v1.json"
source_data = read_json(source_path)
accepted_bodies = [verify(row) for row in source_data["direct_accepted_logical_input_records"]]
assert len(accepted_bodies) == 4
transitive_interfaces = [verify(row) for row in
                         source_data["transitive_ten_accepted_global_interface_identities"]]
assert len(transitive_interfaces) == 10
source_metadata = metadata_rows(source_data)
constructor_validation_path = "problems/2017-B4/notes/global-value-return-r2-input-validation-v1.json"
constructor_metadata = metadata_rows(read_json(constructor_validation_path))
additional_full_texts = [fingerprint(path) for path in (
    "problems/2017-B4/statement.md",
    "problems/2017-B4/reviews/allD-global-acceptance.md",
    "problems/2017-B4/reviews/global-value-return-acceptance.md",
    "problems/2017-B4/reviews/concavity-acceptance.md",
)]

acceptance_records = []
acceptance_metadata = []
for name in ("coarsening", "allD-global", "global-value-return", "concavity"):
    path = f"problems/2017-B4/reviews/{name}-acceptance.json"
    acceptance_records.append(fingerprint(path))
    acceptance_metadata.extend(metadata_rows(read_json(path)))

suffix_pairs = [
    ("problems/2017-B4/proofs/reviewed-allD-global-v1.1.md",
     "problems/2017-B4/notes/allD-global-reasoning-r1-candidate-v1.md"),
    ("problems/2017-B4/proofs/reviewed-global-value-return-v1.1.md",
     "problems/2017-B4/notes/global-value-return-r1-candidate-v1.md"),
]
suffix_records = []
for accepted, raw in suffix_pairs:
    assert safe_path(accepted).read_bytes().endswith(safe_path(raw).read_bytes())
    suffix_records.extend((fingerprint(accepted), fingerprint(raw)))

cache_records = [verify(row) for row in source_data["existing_cache_records_revalidated"]]
retrieval_absence_record = {
    "path": ".cache/literature/2017/global-value-return-r2-felsner-valtr-2011.pdf",
    "exists_at_current_review_freeze": safe_path(
        ".cache/literature/2017/global-value-return-r2-felsner-valtr-2011.pdf").exists(),
    "new_native_retrieval_or_process_cleanup_performed": False,
    "binary_hash_or_PID_reap_inferred": False,
}

previous_manifest_record = verify({
    "path": "problems/2024-B4/reviews/even-inner-next-jet-review-2-manifest-v1.json",
    "bytes": 3051,
    "sha256": "5e598a025fbdcd59d8127618892ba665321dfbe93cf1b81cccea9d215ae9a992",
})
previous_manifest = read_json(previous_manifest_record["path"])
previous_validation_record = verify({
    "path": "problems/2024-B4/reviews/even-inner-next-jet-review-2-input-validation-v1.json",
    "bytes": 763419,
    "sha256": "13a752a93d6fdd64cb2174ca5e724363b8225454a9e6843170b33099d65e7ca1",
})
previous_validation = read_json(previous_validation_record["path"])
older_own = unique_records(previous_validation["older_own_records"]
                           + previous_manifest["records"]
                           + [previous_manifest_record])
assert len(older_own) == 259
previous_metadata = metadata_rows(previous_validation)
previous_metadata.extend(metadata_rows(previous_manifest))

obligations = safe_path("problems/2017-B4/notes/global-value-return-r2-obligations-v1.md").read_text()
assert re.findall(r"^\|\s*(OP-\d\d)\s*\|", obligations, re.MULTILINE) == [
    f"OP-{i:02d}" for i in range(1, 49)]
issues = safe_path(PREFIX + "issues-v1.md").read_text()
assert re.findall(r"^\|(OPR2-\d\d)\|", issues, re.MULTILINE) == [
    f"OPR2-{i:02d}" for i in range(1, 53)]

telemetry = {
    "at_utc": "2026-10-17T14:30:35+00:00",
    "source": "direct account-wide telemetry paired with UTC clock",
    "total_used_percent": 44, "window_duration_minutes": 10080,
    "resets_at_unix": 1792745187, "ordinary_usage_allowed": True,
    "total_used_ceiling_percent": 90, "integration_reserve": True,
}
all_inputs = ([protocol, target_main, target_freeze] + constructor_records
              + accepted_bodies + transitive_interfaces + source_metadata
              + constructor_metadata + additional_full_texts
              + acceptance_records + acceptance_metadata + suffix_records
              + cache_records + [previous_manifest_record, previous_validation_record]
              + previous_metadata + older_own)
validation = {
    "checked_at_utc": NOW,
    "reviewer": "/root/review_2022_complexity_r2",
    "status": "COMPLETE initially blind whole OP1-OP3 R2; no substantive scoped issue; not promotion",
    "metadata_only_not_mathematical_evidence": True,
    "new_OP_peer_report_ledger_or_conclusions_read": False,
    "new_OP_constructor_or_proof_contributor": False,
    "older_G_construction_and_V_whole_review_roles_disclosed": True,
    "constructor_eight_records_verified": constructor_records,
    "complete_accepted_bodies_reread": accepted_bodies,
    "ten_transitive_global_interfaces_hashed_at_existing_scopes_not_new_self_audit": transitive_interfaces,
    "source_declared_metadata_rows_verified": source_metadata,
    "constructor_declared_metadata_rows_verified_not_author_execution": constructor_metadata,
    "additional_complete_texts_read": additional_full_texts,
    "complete_acceptance_JSONs_read": acceptance_records,
    "acceptance_declared_metadata_not_fresh_old_peer_report_reads": acceptance_metadata,
    "G_V_accepted_raw_suffixes_byte_identical": suffix_records,
    "existing_native_cache_fingerprints_not_live_byte_match": cache_records,
    "constructor_interrupted_retrieval_current_absence_check": retrieval_absence_record,
    "whole_main_log_checks_sources_and48_obligations_read": True,
    "complete_new_inference_checks": 52,
    "substantive_new_issues": 0,
    "repair_requested": False,
    "mathematical_program_scan_CAS_certificate_or_author_rerun": False,
    "primary_web_actual_read_scopes": [
        {"url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-2_1.pdf",
         "scope": "Actual p2 B4 all-n domain and normalization"},
        {"url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-solutions-preliminary_1.pdf",
         "scope": "Actual p12 B4 comments/count convention/commutation dictionary; other problems not investigated"},
        {"url": "https://page.math.tu-berlin.de/~felsner/Paper/new-pla.pdf",
         "scope": "Complete introduction and Section2 through Theorem1, marked definitions/local lists/wiring/zonogon/coding context",
         "whole_external_later_section_proof_claimed": False},
        {"url": "https://arxiv.org/pdf/2502.20909v2",
         "scope": "Introduction/marked conventions and Section2 Lemmas3-7/zone tuple and entropy hypotheses; no LP/certificate rerun or new theorem import",
         "whole_external_proof_chain_claimed": False},
    ],
    "one_sided_class_injection_and_all_finite_endpoints_reconstructed": True,
    "common_prefix_conditions_asserted_sufficient": False,
    "fixed_D_before_n_and_leading_half_coefficient_reconstructed": True,
    "auxiliary_brickwall_actual_class_but_not_weighted_mass_exponent": True,
    "numerical_value_effective_E_R_actual_computability_annual_or_novelty_claim": False,
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
    "status": "COMPLETE initially blind nonconstructor WHOLE OP1-OP3 R2; no substantive scoped issue; not promotion",
    "requested_model": "gpt-6.1-sol", "requested_reasoning_effort": "max",
    "independently_verified_effective_settings": None,
    "constructor_target_main": target_main,
    "constructor_target_freeze": target_freeze,
    "whole_claims_reviewed": ["OP1", "OP2a/b/c", "Q-dependent refinement and exact small fiber", "OP3a/b/c", "auxiliary actual brickwall per-class obstruction"],
    "all48_constructor_obligations_covered": True,
    "complete_reviewer_inference_checks": 52,
    "substantive_issues_identified": 0,
    "author_repair_requested": False,
    "initial_frozen_before_any_new_peer_OP_findings": True,
    "new_OP_nonconstructor_independence": True,
    "older_G_author_and_V_review_roles_explicitly_disclosed": True,
    "source_hypotheses_actual_scopes_and_old_certificate_limits_recorded": True,
    "mathematical_program_scan_CAS_certificate_or_author_rerun": False,
    "numerical_value_effective_E_R_actual_computability_annual_or_novelty_claim": False,
    "input_record_occurrences_verified": len(all_inputs),
    "input_unique_paths_verified": len({row["path"] for row in all_inputs}),
    "older_own_unique_frozen_paths_preserved": len(older_own),
    "old_shared_Git_cache_other_owner_edits_spawning_contact_charge_bypass": False,
    "direct_weekly_telemetry": telemetry,
    "records": records,
}
write_new(MANIFEST_PATH, manifest)
print(json.dumps({"manifest": fingerprint(MANIFEST_PATH), "records": records,
                  "input_occurrences": len(all_inputs),
                  "unique_input_paths": len({row["path"] for row in all_inputs}),
                  "older_own_preserved": len(older_own), "all_verified": True},
                 indent=2, ensure_ascii=False))
