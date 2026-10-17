"""Metadata-only freeze for the complete initially blind NJ-v2 R2 review.

No mathematical arithmetic, CAS, scan, certificate or constructor execution.
Run only once; all outputs use exclusive creation within this new prefix.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2024-B4/reviews/even-inner-next-jet-review-2-"
INPUT_PATH = PREFIX + "input-validation-v1.json"
MANIFEST_PATH = PREFIX + "manifest-v1.json"
NOW = datetime.now(timezone.utc).isoformat()


def safe_path(path):
    assert "even-inner-next-jet-review-1-" not in path, path
    assert "P2-next-jet-review-1-" not in path, path
    assert "P2-next-jet-review-2-" not in path, path
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
    "path": "problems/2024-B4/notes/coordinator-even-inner-next-jet-return-v2.md",
    "bytes": 12232,
    "sha256": "5197ab6841d0a97356484cf3a08a7163055449fa879bd8010886e28158532ef6",
})
target_freeze = verify({
    "path": "problems/2024-B4/notes/coordinator-even-inner-next-jet-manifest-v2.json",
    "bytes": 2368,
    "sha256": "7aec0a9fd4109910ea8d95e3b8e50860c4e8083bbe82249196617274d95b03a3",
})
constructor = read_json(target_freeze["path"])
assert len(constructor["records"]) == 9
assert constructor["whole_obligations"] == 10
constructor_records = [verify(row) for row in constructor["records"]]

full_body_paths = [
    "problems/2024-B4/proofs/reviewed-generalized-Kasami-v1.1.md",
    "problems/2024-B4/proofs/reviewed-composition-Kasami-v1.1.md",
    "problems/2024-B4/proofs/reviewed-P2-critical-jet-v1.1.md",
    "problems/2024-B4/statement.md",
    "problems/2024-B4/notes/reasoning-return-r3-sources-v1.json",
    "problems/2024-B4/notes/coordinator-generalized-Kasami-r1-sources-v1.md",
]
full_bodies = [fingerprint(path) for path in full_body_paths]
acceptance_records = []
acceptance_metadata = []
for name in ("generalized-Kasami", "composition-Kasami", "P2-critical-jet"):
    path = f"problems/2024-B4/reviews/{name}-acceptance.json"
    acceptance_records.append(fingerprint(path))
    acceptance_metadata.extend(metadata_rows(read_json(path)))

premise_metadata = []
premise_metadata_files = []
for path in (
    "problems/2024-B4/notes/coordinator-generalized-Kasami-r1-manifest-v1.json",
    "problems/2024-B4/notes/coordinator-generalized-Kasami-r1-input-validation-v1.json",
    "problems/2024-B4/notes/reasoning-return-r3-freeze-v1.json",
    "problems/2024-B4/notes/reasoning-return-r3-input-validation-v1.json",
    "problems/2024-B4/notes/coordinator-P2-critical-jet-manifest-v1.json",
):
    premise_metadata_files.append(fingerprint(path))
    premise_metadata.extend(metadata_rows(read_json(path)))

suffix_pairs = [
    ("problems/2024-B4/proofs/reviewed-generalized-Kasami-v1.1.md",
     "problems/2024-B4/notes/coordinator-generalized-Kasami-r1-candidate-v1.md"),
    ("problems/2024-B4/proofs/reviewed-composition-Kasami-v1.1.md",
     "problems/2024-B4/notes/reasoning-return-r3-candidate-v1.md"),
    ("problems/2024-B4/proofs/reviewed-P2-critical-jet-v1.1.md",
     "problems/2024-B4/notes/coordinator-P2-critical-jet-return-v1.md"),
]
suffix_records = []
for accepted, raw in suffix_pairs:
    assert safe_path(accepted).read_bytes().endswith(safe_path(raw).read_bytes())
    suffix_records.extend((fingerprint(accepted), fingerprint(raw)))

cache_records = [
    verify({"path": ".cache/official/2024-paper_b.pdf",
            "sha256": "1401f21218ad4c387c4d537ed8fd7de119b376cba52957ef788c772dc5ab4ddc"}),
    verify({"path": ".cache/literature/2024/cited-3e7f3cb84c20c6b1.pdf",
            "sha256": "bc9389858756658a7a2769a74ebb40b4df05523ddfe24a4639cd7d79ef31df16"}),
]

previous_manifest_record = verify({
    "path": "problems/2021-B4/reviews/reasoning-return-r7-review-2-manifest-v1.json",
    "bytes": 3119,
    "sha256": "de50c7ad01eca3ab2d4850122e2c3f1fe5371a9bb503a90bb4be1965535cb8ba",
})
previous_manifest = read_json(previous_manifest_record["path"])
previous_validation_record = verify({
    "path": "problems/2021-B4/reviews/reasoning-return-r7-review-2-input-validation-v1.json",
    "bytes": 576586,
    "sha256": "c1c168581ddd9247a377d361e1f7960e80b9aa84ae5da7ae1a9862058d11350f",
})
previous_validation = read_json(previous_validation_record["path"])
older_own = unique_records(previous_validation["older_own_records"]
                           + previous_manifest["records"]
                           + [previous_manifest_record])
assert len(older_own) == 253
previous_metadata = metadata_rows(previous_validation)
previous_metadata.extend(metadata_rows(previous_manifest))

new_main = safe_path(target_main["path"]).read_text()
last_obligations = new_main.split("## Ten required whole-audit obligations", 1)[1]
assert re.findall(r"^(\d+)\. ", last_obligations, re.MULTILINE) == [
    str(i) for i in range(1, 11)]
issues = safe_path(PREFIX + "issues-v1.md").read_text()
assert re.findall(r"^\|(NJR2-\d\d)\|", issues, re.MULTILINE) == [
    f"NJR2-{i:02d}" for i in range(1, 37)]

telemetry = {
    "at_utc": "2026-10-17T14:21:40+00:00",
    "source": "direct account-wide telemetry paired with UTC clock",
    "total_used_percent": 44, "window_duration_minutes": 10080,
    "resets_at_unix": 1792745187, "ordinary_usage_allowed": True,
    "total_used_ceiling_percent": 90, "integration_reserve": True,
}
all_inputs = ([protocol, target_main, target_freeze]
              + constructor_records + full_bodies + acceptance_records
              + acceptance_metadata + premise_metadata_files + premise_metadata
              + suffix_records + cache_records
              + [previous_manifest_record, previous_validation_record]
              + previous_metadata + older_own)
validation = {
    "checked_at_utc": NOW,
    "reviewer": "/root/review_2022_complexity_r2",
    "status": "complete initially blind WHOLE NJ-v2 R2; no substantive scoped defect found; not promotion",
    "metadata_only_not_mathematical_evidence": True,
    "new_NJ_peer_report_ledger_or_conclusions_read": False,
    "new_NJ_constructor_or_proof_contributor": False,
    "older_2024_GK_structural_divisor_necessary_valuation_review_roles_disclosed": True,
    "constructor_target_records": constructor_records,
    "full_accepted_bodies_and_new_source_records_read": full_bodies,
    "complete_acceptance_JSONs_read": acceptance_records,
    "acceptance_declared_metadata_rows_verified_not_historical_whole_review_reads": acceptance_metadata,
    "old_premise_metadata_files": premise_metadata_files,
    "old_premise_metadata_rows_verified_not_certificate_recertification": premise_metadata,
    "accepted_raw_suffixes_byte_identical": suffix_records,
    "existing_native_cache_fingerprints_not_live_byte_match": cache_records,
    "whole_v2_six_sections_limits_failedroutes_ten_obligations_read": True,
    "preserved_P2_only_v1_mathematical_body_read_or_assumed_correct": False,
    "DI_unverified_candidate_read_or_used": False,
    "complete_new_inference_checks": 36,
    "substantive_new_issues": 0,
    "repair_requested": False,
    "mathematical_program_scan_CAS_certificate_or_author_rerun": False,
    "primary_web_actual_read_scopes": [
        {"url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf",
         "scope": "Actual p2 B4 hypothesis and(b), coefficientwise/integer/nonconstant domains; no preliminary proof"},
        {"url": "https://arxiv.org/pdf/0903.2016v4",
         "scope": "Sections2.1-2.2 quotient definitions and complete Section2.3 Lemma3 coordinate proof; no APN/Weil/classification theorem imported",
         "whole_external_paper_proof_chain_claimed": False},
    ],
    "all_even_inner_r_and_all_target_s_and_extension_inseparable_H_reviewed": True,
    "critical_value_collisions_zero_K_higher_order_and_minimum_parameters_covered": True,
    "arbitrary_factors_odd_inner_full_annual_or_novelty_claim": False,
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
    "status": "COMPLETE initially blind nonconstructor WHOLE NJ-v2 R2; no substantive scoped issue; not promotion",
    "requested_model": "gpt-6.1-sol", "requested_reasoning_effort": "max",
    "independently_verified_effective_settings": None,
    "constructor_target_main": target_main,
    "constructor_target_freeze": target_freeze,
    "whole_claims_reviewed": ["NJ1-v2", "NJ2-v2", "exact accepted GK/CP bridges and CJ boundary"],
    "all10_constructor_obligations_covered": True,
    "complete_reviewer_inference_checks": 36,
    "substantive_issues_identified": 0,
    "author_repair_requested": False,
    "initial_frozen_before_any_new_peer_NJ_findings": True,
    "new_NJ_nonconstructor_independence": True,
    "older_review_roles_explicitly_disclosed": True,
    "source_hypotheses_actual_scopes_and_old_certificate_limits_recorded": True,
    "mathematical_program_scan_CAS_certificate_or_author_rerun": False,
    "all_factors_full_annual_or_novelty_claim": False,
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
