"""CREATE-NEW administrative review freeze; NO mathematical computation.

Verifies declared bytes, JSON/label structure and compact immutable parents.
Does not execute constructor code, traverse peer reviews, or alter old files.
Default: read-only preflight.  --freeze writes only this assigned review prefix.
"""
from pathlib import Path
import datetime
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
OWN = "problems/2024-B4/reviews/reasoning-sector3-return-r1-review-2-"
AUTHOR = "problems/2024-B4/notes/reasoning-sector3-return-r1-"
PEER = "problems/2024-B4/reviews/reasoning-sector3-return-r1-review-1-"
STAMP = datetime.datetime.now(datetime.timezone.utc).isoformat()
OCCURRENCES = []
UNIQUE = {}


def record(path):
    assert not path.startswith(PEER), "NEW peer sector3 material forbidden"
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def check(row):
    expected = {key: row[key] for key in ["path", "bytes", "sha256"]}
    actual = record(expected["path"])
    assert actual == expected, expected["path"]
    OCCURRENCES.append(expected)
    old = UNIQUE.setdefault(expected["path"], expected)
    assert old == expected, expected["path"]
    return actual


def read_json(path):
    assert not path.startswith(PEER)
    return json.loads((ROOT / path).read_text())


def digest(rows):
    value = sorted(rows, key=lambda row: row["path"])
    data = json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":")).encode()
    return hashlib.sha256(data).hexdigest()


def parent(path, size, sha, payload_key, count):
    row = check({"path": path, "bytes": size, "sha256": sha})
    body = read_json(path)
    payload = body[payload_key]
    assert len(payload) == count, path
    for item in payload:
        check(item)
    return {"metadata": row, "direct_payload_records_verified": count,
            "historical_inventory_bound_not_recopied": True}, body


def write_new(suffix, body):
    path = OWN + suffix
    with (ROOT / path).open("x") as stream:
        json.dump(body, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    return record(path)


constructor, main_freeze = parent(
    AUTHOR + "freeze-v1.json", 3893,
    "2a3cf9ce9d04b92f42a03e0847a478c6b3402e4eadf7067cb2addf4f97055be2",
    "artifacts", 9)
assert main_freeze["whole_obligations"] == 36
assert main_freeze["contributors"] == ["C", "root"]
assert main_freeze["artifacts"][0] == {
    "path": AUTHOR + "candidate-v1.md", "bytes": 17157,
    "sha256": "e8ca03cd139df7dcbe7508ad4c701e66d220a177c58ea01f8fac23a1788edd6a"}

baseline = read_json(AUTHOR + "baseline-v1.json")
base_rows = baseline["direct_inputs_and_occupied_prefix_and_source_bytes"]
assert len(base_rows) == 44
assert digest(base_rows) == baseline["canonical_record_array_sha256"]
assert baseline["unused_fresh_prefix_confirmed"] is True
assert baseline["old_R3_prefix_occupied_files"] == 16
validation = read_json(AUTHOR + "input-validation-v1.json")
extras = validation["additional_source_records"]
assert len(extras) == 3
current_rows = base_rows + extras
assert len(current_rows) == len({row["path"] for row in current_rows}) == 47
assert digest(current_rows) == validation["canonical_sorted_record_array_sha256"]
for row in current_rows:
    check(row)
assert validation["all_record_occurrences"] == 47

author_parent_row = baseline["immutable_parent_manifest"]
assert author_parent_row == validation["compact_immutable_parent_manifest"]
author_parent, author_parent_body = parent(
    author_parent_row["path"], author_parent_row["bytes"], author_parent_row["sha256"],
    "artifacts", 8)

previous_review, previous_review_body = parent(
    "problems/2022-B4/reviews/reasoning-return-r8-review-2-manifest-v1.json", 3548,
    "5f5a596e0f4d6a1d637fb91aafb4bb0ac46cba56dacc4b9a8b1f60bb2142a40e",
    "artifacts", 8)
previous_construction, previous_construction_body = parent(
    "problems/2021-B4/notes/reasoning-return-r10-freeze-v1.json", 3884,
    "ff20fd17e080ce3fb5d3c0f4f3f7c1f58624741b0fadc1be4a0fee26fc73f2bd",
    "artifacts", 10)
# The old own CP manifest was opened only for role provenance. Bind its
# current immutable metadata and all six declared payload records, without
# claiming a new independent audit of old mathematics or copying its inventory.
old_role_path = "problems/2024-B4/reviews/reasoning-return-r3-review-2-manifest-v1.json"
old_role_row = record(old_role_path)
check(old_role_row)
old_role_body = read_json(old_role_path)
assert old_role_body["peer_findings_read_before_freeze"] is False
assert len(old_role_body["records"]) == 6
for row in old_role_body["records"]:
    check(row)
old_role = {"metadata": old_role_row, "direct_payload_records_verified": 6,
            "historical_inventory_bound_not_recopied": True,
            "current_read_role_only_not_new_math_recertification": True}

check({"path": "AGENTS.md", "bytes": 4707,
       "sha256": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"})

author_sources = read_json(AUTHOR + "sources-v1.json")
thesis_source = author_sources["source_records"][0]
assert thesis_source["visual_pages_read_this_task"] == [7,12,13,14,15,18,20,21,22,23,24,25]
for row in thesis_source["read_only_source_images"]:
    check(row)
check(thesis_source["existing_cache"])
images = thesis_source["read_only_source_images"]
assert len(images) == 12

author_obs = re.findall(r"^\| (\d\d) \|", (ROOT / (AUTHOR + "obligations-v1.md")).read_text(), re.M)
assert author_obs == [f"{i:02d}" for i in range(1,37)]
ledger = (ROOT / (OWN + "issues-v1.md")).read_text()
check_ids = re.findall(r"^\| R2-(\d\d) \|", ledger, re.M)
assert check_ids == [f"{i:02d}" for i in range(1,45)]
covered = set()
for line in ledger.splitlines():
    if line.startswith("| R2-"):
        covered.update(re.findall(r"\d\d", line.split("|")[2]))
assert covered == set(author_obs)
for suffix in ["initial-v1.md", "issues-v1.md", "source-checks-v1.md", "worklog-v1.md"]:
    assert (ROOT / (OWN + suffix)).is_file()
for suffix in ["sources-v1.json", "input-validation-v1.json", "freeze-output-v1.json", "manifest-v1.json"]:
    assert not (ROOT / (OWN + suffix)).exists(), "CREATE-NEW only: " + suffix

summary = {
    "declared_fingerprint_occurrences_verified": len(OCCURRENCES),
    "unique_paths_fingerprinted": len(UNIQUE),
    "canonical_deduplicated_summary_sha256": digest(list(UNIQUE.values())),
    "historical_inventories_bound_not_duplicated": True,
    "constructor_47_current_records_verified": True,
}
if "--freeze" not in sys.argv:
    print(json.dumps({"preflight": "complete", "checks": len(check_ids),
                      "all_author_obligations": len(covered), "summary": summary}))
    raise SystemExit(0)

telemetry = {
    "at_utc": "2026-10-17 19:49:12 UTC", "total_used_percent": 61,
    "window_minutes": 10080, "reset_unix": 1792745187,
    "ordinary_usage_allowed": True, "total_ceiling_percent": 90,
    "integration_reserve": True,
}
sources_record = write_new("sources-v1.json", {
    "recorded_at_utc": STAMP,
    "actual_full_read_scope": "See COMPLETE source-checks-v1.md; no peer sector3 record opened",
    "official": {
        "url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf",
        "read_scope": "actual B4(b), PDFpage2, coefficientwise and nonconstant definitions",
        "existing_cache": [row for row in extras if row["path"] == ".cache/official/2024-paper_b.pdf"][0],
        "no_preliminary_solution_investigation": True,
    },
    "primary_operative_source": {
        "title": "McGuire, On Certain Exponential Sums and Cyclic Codes,1995 thesis",
        "url": "https://thesis.caltech.edu/4053/01/McGuire_gm_1995.pdf",
        "record_url": "https://thesis.caltech.edu/4053/", "doi": "10.7907/1CZ2-6S05",
        "existing_cache": thesis_source["existing_cache"],
        "visual_pages_read": [7,12,13,14,15,18,20,21,22,23,24,25],
        "printed_pages": "2,7--10,13,15--20",
        "complete_operative_Theorem2_1prime_and_PropositionA_proofs_read": True,
        "projective_Bezout_actual_statement_read": True,
        "source_images": images,
        "journal_full_pdf_read": False,
        "source_infinity_defect_claim": False,
    },
    "contextual_primary_reads": [
        {"url": "https://arxiv.org/pdf/0903.2016v4",
         "actual_read_scope": "definitions/conjectures, exact conditional Theorems15/16, selected local setup, t205 counterexample assertion/references",
         "entire_long_proof_freshly_reconstructed": False,
         "general_whole_irreducibility_import": False,
         "downloaded_byte_sha256": None},
        {"url": "https://arxiv.org/pdf/1207.5528v1",
         "actual_read_scope": "matching definitions, Lemma1 statement/proof and selected context/diagonal identity",
         "arbitrary_target_gcd_import": False, "downloaded_byte_sha256": None},
    ],
    "older_accepted_read_scopes": [
        {"path": "problems/2024-B4/proofs/reviewed-divisor-criteria-v1.1.md", "read_scope": "FULL; old authored C7/C11 only, no certificate rerun"},
        {"path": "problems/2024-B4/proofs/reviewed-structural-v1.1.md", "read_scope": "throughline130, exact accepted scope/setup; not fresh whole recertification"},
        {"path": "problems/2024-B4/proofs/reviewed-reasoning-components-r1-v1.1.md", "read_scope": "throughline125, exact accepted scope/setup; old authored IC context, not diagonal premise"},
    ],
    "PDF_skill_read_only": "/Users/uqmkamga/.codex/plugins/cache/openai-primary-runtime/pdf/26.1013.11914/skills/pdf/SKILL.md",
    "no_new_download_render_cache_mutation_or_escalated_wait": True,
    "no_math_code_CAS_scan_author_rerun_or_certificate": True,
})
validation_record = write_new("input-validation-v1.json", {
    "checked_at_utc": STAMP, "administrative_only_not_mathematical_evidence": True,
    "constructor_packet": constructor,
    "constructor_baseline_metadata": record(AUTHOR + "baseline-v1.json"),
    "constructor_input_validation_metadata": record(AUTHOR + "input-validation-v1.json"),
    "constructor_declared_current_record_occurrences": 47,
    "constructor_declared_current_unique_paths": 47,
    "constructor_current_canonical_sha256": digest(current_rows),
    "constructor_immutable_parent": author_parent,
    "constructor_earlier_own_paths_bound_transitively": 415,
    "own_previous_review": previous_review,
    "own_previous_review_old_summary": previous_review_body["compact_input_summary"],
    "own_previous_construction": previous_construction,
    "own_previous_construction_old_summary": previous_construction_body["compact_old_inputs"],
    "old_own_CP_role_metadata": old_role,
    "all_44_ledger_checks": check_ids,
    "all_36_author_obligations": sorted(covered),
    "compact_input_summary": summary,
    "new_peer_sector3_paths_read_even_for_metadata": False,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "independently_verified_effective_settings": None,
    "authoritative_account_weekly": telemetry,
    "source_metadata": sources_record,
})

report = record(OWN + "initial-v1.md")
output_record = write_new("freeze-output-v1.json", {
    "COMPLETE": True, "frozen_at_utc": STAMP,
    "manifest_path": OWN + "manifest-v1.json", "report": report,
    "checks": 44, "all_author_obligations": 36,
    "substantive_open_issues": 0, "required_author_repairs": 0,
    "compact_input_summary": summary, "mathematical_program": False,
})
suffixes = ["initial-v1.md", "issues-v1.md", "source-checks-v1.md", "worklog-v1.md",
            "freeze-v1.py", "sources-v1.json", "input-validation-v1.json", "freeze-output-v1.json"]
artifacts = [record(OWN + suffix) for suffix in suffixes]
assert artifacts[-2] == validation_record and artifacts[-1] == output_record
for row in UNIQUE.values():
    assert record(row["path"]) == row, row["path"]
manifest_record = write_new("manifest-v1.json", {
    "frozen_at_utc": STAMP,
    "status": "COMPLETE initially blind NONCONSTRUCTOR WHOLE R2 initial; recommendation only",
    "reviewer": "/root/review_2021_reasoning_j15_r2",
    "new_contributors_excluded": ["C", "root"],
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "independently_verified_effective_settings": None,
    "whole_checks": 44, "all_author_obligations": 36,
    "recommendation": "No substantive defect found in exact S3A--S3D; root reconciliation and other whole audit required",
    "substantive_open_issues": 0, "required_author_repairs": 0, "advisories": [],
    "complete_initial_before_ANY_new_peer_sector3_report_ledger_source_manifest_or_finding": True,
    "older_T1_T4_C7_C11_IC_authorship_and_reviews_disclosed": True,
    "new_sector3_constructor_or_contributor": False,
    "original_author_full_operative_proof_read_journal_full_pdf_unread": True,
    "no_annual_classification_new_qualifying_family_or_novelty_claim": True,
    "no_math_program_CAS_scan_author_rerun_or_certificate": True,
    "no_old_shared_cache_Git_edits_spawn_contact_charge_bypass": True,
    "compact_input_summary": summary,
    "authoritative_account_weekly": telemetry,
    "administrative_command": ".venv/bin/python " + OWN + "freeze-v1.py --freeze",
    "artifacts": artifacts,
})
print(json.dumps({"COMPLETE": True, "manifest": manifest_record,
                  "report": report, "artifacts": len(artifacts),
                  "summary": summary, "mathematical_program": False}))
