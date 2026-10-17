"""Fresh reviewer metadata-only R7 whole-initial freeze.

Run: python3 problems/2021-B4/reviews/reasoning-return-r7-review-2-freeze-v1.py
No mathematical program, coefficient calculation, finite-certificate replay,
constructor execution or peer R7 report read. New prefix outputs only.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2021-B4/reviews/reasoning-return-r7-review-2-"
INPUT_PATH = PREFIX + "input-validation-v1.json"
MANIFEST_PATH = PREFIX + "manifest-v1.json"
NOW = datetime.now(timezone.utc).isoformat()


def fingerprint(path):
    assert "reasoning-return-r7-review-1-" not in path, path
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def verify(expected):
    actual = fingerprint(expected["path"])
    assert actual["sha256"] == expected["sha256"], (expected, actual)
    if "bytes" in expected:
        assert actual["bytes"] == expected["bytes"], (expected, actual)
    return actual


def read_json(path):
    assert "reasoning-return-r7-review-1-" not in path, path
    return json.loads((ROOT / path).read_text())


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
    for expected in records:
        actual = verify(expected)
        if actual["path"] in result:
            assert result[actual["path"]] == actual
        result[actual["path"]] = actual
    return [result[path] for path in sorted(result)]


def write_new(path, document):
    assert path.startswith(PREFIX)
    with (ROOT / path).open("x") as stream:
        json.dump(document, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


for path in (INPUT_PATH, MANIFEST_PATH):
    assert not (ROOT / path).exists(), path

protocol = verify({"path": "AGENTS.md", "bytes": 4707,
                   "sha256": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"})
target_main = verify({
    "path": "problems/2021-B4/notes/reasoning-return-r7-candidate-v1.md",
    "bytes": 17704,
    "sha256": "8f4d1f71930b82e029066c4f4d249489c34e70b731e80a11458c833223fc18a6",
})
target_freeze = verify({
    "path": "problems/2021-B4/notes/reasoning-return-r7-freeze-v1.json",
    "bytes": 3391,
    "sha256": "d29dc9823b24ae2df97ee1c506cb8fe8881a2ec2d82a206e2a7411566df7afa8",
})
constructor = read_json(target_freeze["path"])
assert len(constructor["artifacts"]) == 9
constructor_artifacts = [verify(row) for row in constructor["artifacts"]]
constructor_metadata = metadata_rows(constructor)
for suffix in ("sources-v1.json", "input-validation-v1.json", "freeze-output-v1.json"):
    constructor_metadata.extend(metadata_rows(read_json(
        "problems/2021-B4/notes/reasoning-return-r7-" + suffix)))

source_json = read_json("problems/2021-B4/notes/reasoning-return-r7-sources-v1.json")
accepted_records = [verify(row) for row in
                    source_json["complete_accepted_bodies_and_registers_read"]]
full_additional_paths = [
    "problems/2021-B4/statement.md",
    "problems/2021-B4/notes/padic-rational-newton-obstructions-v1.md",
    "problems/2021-B4/proofs/reviewed-odd-support-exclusion-v1.1.md",
    "problems/2021-B4/reviews/reasoning-return-r6-acceptance.md",
    "problems/2021-B4/reviews/reasoning-return-r5-acceptance.md",
    "problems/2021-B4/reviews/return-r3-acceptance.md",
]
full_additional_records = [fingerprint(path) for path in full_additional_paths]
partial_context = [
    {**fingerprint("problems/2021-B4/notes/reasoning-return-r3-candidate-v1.md"),
     "actual_read_scope": "Original lines1-114 assumptions and complete G1/G2, not a new whole seven-packet reread"},
    {**fingerprint("problems/2021-B4/notes/reasoning-return-r3-collision-candidate-v1.md"),
     "actual_read_scope": "Complete Section6 RC3 and subsequent source/remaining-boundary record"},
]

suffix_pairs = [
    ("problems/2021-B4/proofs/reviewed-reasoning-return-r6-v1.1.md",
     "problems/2021-B4/notes/reasoning-return-r6-candidate-v1.md"),
    ("problems/2021-B4/proofs/reviewed-reasoning-return-r5-v1.1.md",
     "problems/2021-B4/notes/reasoning-return-r5-candidate-v1.md"),
    ("problems/2021-B4/proofs/reviewed-reasoning-J15-v1.1.md",
     "problems/2021-B4/notes/reasoning-J15-double-root-candidate-v1.md"),
]
suffix_records = []
for accepted, raw in suffix_pairs:
    assert (ROOT / accepted).read_bytes().endswith((ROOT / raw).read_bytes())
    suffix_records.extend([fingerprint(accepted), fingerprint(raw)])

acceptance_metadata = []
acceptance_jsons = []
for name in ("reasoning-return-r6", "reasoning-return-r5", "return-r3"):
    path = f"problems/2021-B4/reviews/{name}-acceptance.json"
    acceptance_jsons.append(fingerprint(path))
    acceptance_metadata.extend(metadata_rows(read_json(path)))

cache_records = [
    verify({"path": ".cache/official/2021-paper_b.pdf", "bytes": 157688,
            "sha256": "2d507d593500f762e90b041d03a451e884ea33c8769f9a2132427e14d8f926d1"}),
    verify({"path": ".cache/literature/2021/cited-66c5af6a0f0239f5.pdf",
            "bytes": 281743,
            "sha256": "d818747102d32060f43ae5f015f27065aadf38699b272a2367749db8b33fedbf"}),
]

older_manifest_record = verify({
    "path": "problems/2020-B4/notes/reasoning-return-r5-freeze-v1.json",
    "bytes": 3920,
    "sha256": "bb654165037bef83a9c5105278775dda450268d0858937358cf54c0e3e7a3bfe",
})
older_manifest = read_json(older_manifest_record["path"])
older_validation = read_json(
    "problems/2020-B4/notes/reasoning-return-r5-input-validation-v1.json")
older_own = unique_records(older_validation["older_own_records"]
                           + older_manifest["artifacts"]
                           + [older_manifest_record])
assert len(older_own) == 247

obligations = (ROOT / "problems/2021-B4/notes/reasoning-return-r7-obligations-v1.md").read_text()
assert re.findall(r"^\|(R7O\d\d)\|", obligations, re.MULTILINE) == [
    f"R7O{i:02d}" for i in range(1, 37)]
issues = (ROOT / (PREFIX + "issues-v1.md")).read_text()
assert re.findall(r"^\|(R7R2-\d\d)\|", issues, re.MULTILINE) == [
    f"R7R2-{i:02d}" for i in range(1, 49)]

telemetry = {
    "at_utc": "2026-10-17T14:05:50+00:00",
    "source": "direct account-wide telemetry paired with UTC clock",
    "total_used_percent": 43, "window_duration_minutes": 10080,
    "resets_at_unix": 1792745187, "ordinary_usage_allowed": True,
    "total_used_ceiling_percent": 90, "integration_reserve": True,
}
all_inputs = ([protocol, target_main, target_freeze] + constructor_artifacts
              + constructor_metadata + accepted_records + full_additional_records
              + partial_context + suffix_records + acceptance_jsons
              + acceptance_metadata + cache_records + [older_manifest_record]
              + older_own)
validation = {
    "checked_at_utc": NOW,
    "reviewer": "/root/review_2022_complexity_r2",
    "status": "complete initially blind whole R7 R2 review, no substantive scoped defect found; not promotion",
    "metadata_only_not_mathematical_evidence": True,
    "new_peer_R7_report_ledger_or_conclusions_read": False,
    "new_R7_constructor_or_proof_contributor": False,
    "older_R3_R5_R6_single_center_review_roles_disclosed": True,
    "constructor_target_artifacts": constructor_artifacts,
    "constructor_declared_metadata_rows_verified": constructor_metadata,
    "full_accepted_bodies_and_registers_read": accepted_records,
    "additional_complete_bodies_and_acceptance_texts_read": full_additional_records,
    "older_context_precise_partial_read_scopes": partial_context,
    "accepted_raw_suffixes_byte_identical": suffix_records,
    "acceptance_jsons": acceptance_jsons,
    "acceptance_metadata_rows_verified_not_fresh_historical_review_reads": acceptance_metadata,
    "existing_native_cache_fingerprints_not_live_byte_match": cache_records,
    "whole_new_main_source_log_failedroutes_and36obligations_read": True,
    "complete_new_inference_checks": 48,
    "substantive_new_issues": 0,
    "repair_requested": False,
    "old_large_certificates_newly_regenerated_or_recertified": False,
    "mathematical_program_scan_CAS_certificate_or_author_rerun": False,
    "primary_web_actual_read_scopes": [
        {"url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf",
         "scope": "Actual p2 B4 hypothesis and(b), Qcoefficients/Qcommonwitnesses, d>=2; no preliminary proof investigated"},
        {"url": "https://arxiv.org/pdf/1208.5404",
         "scope": "Type/scenario/Hasse definitions, equation7, Section3.4 equations9-10 and full Lemma17 passage, Proposition19 proof and unramified qualification",
         "whole_external_paper_proof_chain_claimed": False},
        {"url": "https://arxiv.org/html/2608.14726v1",
         "scope": "Support definition, vacuity Theorem3.1/proof, complete TheoremB and t1/multi-root boundary, C/D statements",
         "whole_external_paper_or_multi_root_theorem_imported": False},
    ],
    "strict_tau_less_nu_and_cubic_boundary_retained": True,
    "zero_delta_and_arbitrarily_deep_finite_delta_covered": True,
    "deep_triple_and_nonunit_essential_center_not_excluded": True,
    "full_branch_degree20_annual_lift_or_novelty_claim": False,
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
    "status": "COMPLETE initially blind nonconstructor whole R7 R2 review; no substantive defect found within exact partial scope; not promotion",
    "requested_model": "gpt-6.1-sol", "requested_reasoning_effort": "max",
    "independently_verified_effective_settings": None,
    "constructor_target_main": target_main,
    "constructor_target_freeze": target_freeze,
    "whole_claims_reviewed": ["R7A", "R7B", "R7C", "R7D", "old cover consequence attribution", "cubic diagnostic and precise boundaries"],
    "all36_constructor_obligations_covered": True,
    "complete_reviewer_inference_checks": 48,
    "substantive_issues_identified": 0,
    "author_repair_requested": False,
    "initial_frozen_before_any_new_peer_R7_findings": True,
    "new_R7_nonconstructor_independence": True,
    "older_review_roles_explicitly_disclosed": True,
    "source_hypotheses_actual_scopes_and_old_certificate_limits_recorded": True,
    "mathematical_program_scan_CAS_certificate_or_author_rerun": False,
    "full_branch_degree20_annual_lift_or_novelty_claim": False,
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
