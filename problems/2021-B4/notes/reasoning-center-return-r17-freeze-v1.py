#!/usr/bin/env python3
"""ADMINISTRATIVE ONLY: fingerprints, labels and immutable provenance.

No mathematical evaluation, finite-field calculation, scan, test or author
certificate is performed. Run once from repository root. Every output uses
exclusive creation; this cannot overwrite a frozen or unrelated artifact.
"""
import datetime
import hashlib
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[3]
STEM = "problems/2021-B4/notes/reasoning-center-return-r17-"
PREFIX = ROOT / STEM
PARENT = "problems/2019-B4/reviews/reasoning-cut-number-r3-review-2-manifest-v1.json"
PARENT_EXPECTED = (2937, "120fd2a3b25544c536a5e3258f5a5d7e014daa96a6d94d9f9140549a67393a30")
INPUTS = [
    ("reasoning-return-r5", 23675, "f4f088adc133b0581520488cdbba30082c13b2402c96ae555142e5491ad4137d"),
    ("reasoning-return-r8", 19921, "33b8713d402d09f711d0096cdc4e8c00f9e622a5335f8e3345eb4f82ba0d359d"),
    ("reasoning-return-r12", 20521, "bfc4a3549b9357600fdadf79a826d203e2226a1a4fd8d7c183412f8abc18e3ef"),
    ("reasoning-return-r13", 19299, "a29ecdb8002f3cbb4250e93f94c65ed83a67b086331fb3497d48ad740959ab6b"),
    ("reasoning-return-r14", 23801, "c574096c94bc4deaab81b54c5dd0599f3089e7122165312d9089ea28d2a9f880"),
    ("reasoning-unit-return-r15", 21263, "7ba8dd9cb3ce9818e46e9c7d13d64bba7257489842f6d5706eb29a33604ccdc0"),
    ("reasoning-early-return-r16", 22642, "6d66df441f414e97e09944fffe83fb6346b4f46631121ff84d5668d68c6af210"),
]


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def fingerprint(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def verify(record):
    assert fingerprint(record["path"]) == record, record["path"]


def dump(suffix, value):
    path = ROOT / (STEM + suffix)
    with path.open("x", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
    return fingerprint(STEM + suffix)


protected_occurrences = []


def protect(record):
    verify(record)
    protected_occurrences.append(record)


parent_record = fingerprint(PARENT)
assert (parent_record["bytes"], parent_record["sha256"]) == PARENT_EXPECTED
protect(parent_record)
parent = json.loads((ROOT / PARENT).read_text())
assert parent["whole_obligations"] == 48
assert parent["review_file_count"] == 10
assert parent["ENTIRE_report_ALL48_ledger_issues_sources_log_code_ALL_metadata_frozen"] is True
for record in parent["artifacts"]:
    protect(record)
assert len(parent["artifacts"]) == 9
# Bind the declared immediate older constructor freeze without expanding its
# historical descendants. Its exact fingerprint is necessary parent metadata.
protect(parent["immediate_own_parent"])
parent_baseline_path = "problems/2019-B4/reviews/reasoning-cut-number-r3-review-2-baseline-v1.json"
parent_baseline = json.loads((ROOT / parent_baseline_path).read_text())
parent_summary = {
    "manifest": parent_record,
    "payload_records_verified": len(parent["artifacts"]),
    "older_constructor_freeze_bound_without_inventory_expansion": parent["immediate_own_parent"],
    "baseline": fingerprint(parent_baseline_path),
    "historical_protected_fingerprint_occurrences": parent_baseline["protected_fingerprint_occurrences"],
    "historical_protected_unique_paths": parent_baseline["protected_unique_paths"],
    "historical_canonical_summary_sha256": parent_baseline["canonical_protected_summary_sha256"],
    "historical_inventory_rehashed_or_copied_again": False,
}

accepted_inputs = []
for stem, expected_bytes, expected_sha in INPUTS:
    json_path = f"problems/2021-B4/reviews/{stem}-acceptance.json"
    md_path = f"problems/2021-B4/reviews/{stem}-acceptance.md"
    authority = json.loads((ROOT / json_path).read_text())
    assert authority["status"] == "proved, independently reviewed scoped partial result"
    assert authority["unresolved_substantive_issues"] == 0
    assert authority["repair_required"] is False
    accepted = authority["accepted_copy"]
    candidate = authority["candidate"]
    assert (accepted["bytes"], accepted["sha256"]) == (expected_bytes, expected_sha)
    assert (ROOT / accepted["path"]).read_bytes().endswith((ROOT / candidate["path"]).read_bytes())
    json_record, md_record = fingerprint(json_path), fingerprint(md_path)
    for record in [accepted, candidate, json_record, md_record]:
        protect(record)
    accepted_inputs.append({
        "id": stem,
        "accepted_copy": accepted,
        "literal_immutable_candidate_suffix": candidate,
        "MD_authority": md_record,
        "JSON_authority": json_record,
        "accepted_status_and_no_unresolved_issues_verified": True,
        "complete_operative_body_and_authorities_read": True,
        "older_mathematical_certificates_rerun": False,
    })

for path in ["AGENTS.md", "problems/2021-B4/statement.md", "problems/2021-B4/research.md", "problems/2021-B4/references.md"]:
    protect(fingerprint(path))
assert fingerprint("AGENTS.md")["sha256"] == "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"

dedup = {}
for record in protected_occurrences:
    prior = dedup.setdefault(record["path"], record)
    assert prior == record
protected = [dedup[key] for key in sorted(dedup)]
canonical = json.dumps(protected, sort_keys=True, separators=(",", ":")).encode()
baseline = {
    "created_utc": now(),
    "purpose": "Compact administrative preservation, not mathematical evidence",
    "assigned_prefix_confirmed_unused_before_first_write": True,
    "protected_fingerprint_occurrences": len(protected_occurrences),
    "protected_unique_paths": len(protected),
    "canonical_protected_summary_sha256": hashlib.sha256(canonical).hexdigest(),
    "protected": protected,
    "immediate_own_parent_compact_summary": parent_summary,
    "accepted_inputs": accepted_inputs,
    "no_historical_inventory_proliferation": True,
    "no_Git_old_shared_cache_mutation": True,
}
baseline_record = dump("baseline-v1.json", baseline)

ledger = (ROOT / (STEM + "obligations-v1.md")).read_text()
labels = re.findall(r"^\|(R17-\d{2})\|", ledger, flags=re.MULTILINE)
assert labels == [f"R17-{index:02d}" for index in range(1, 61)]
main = (ROOT / (STEM + "candidate-v1.md")).read_text()
assert "Candidate proof - unverified" in main
for claim in ["R17A", "R17B", "R17C", "R17D"]:
    assert claim in main

metadata = {
    "created_utc": now(),
    "status": "candidate proof - unverified; constructor checkpoint only",
    "constructor": "C /root/review_2017_coarsening_r1",
    "root_broad_assignment_NO_NEW_proof_inference": True,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
    "verified_effective_setting_readback": None,
    "two_OTHER_fresh_initially_blind_ENTIRE_WHOLE_audits_required": True,
    "constructor_eligible_as_required_auditor": False,
    "whole_obligations": 60,
    "proposed_claims": ["R17A", "R17B", "R17C", "R17D"],
    "mathematical_code_CAS_scan_source_author_rerun": False,
    "proof_critical_hand_certificate": "16+32 affine zeros and two actual-H7 products; all derivations exposed",
    "source_read_limits": "sources-v1.md, full operative accepted bodies; no invented full-paper read or cache hash",
    "old_roles_disclosed_not_independent_recertification": True,
    "same_current_weekly_window_only": {"reset": 1792874445, "latest_parent_total_used_percent": 26, "latest_parent_telemetry_utc": "2026-10-18T10:40:59Z", "ceiling_total_percent": 90, "integration_reserve_required": True},
    "full_degree20_annual_lift_height_priority_or_external_validation_claim": False,
    "pending_tool_approval_job_or_unreaped_child": False,
    "immediate_own_parent": parent_record,
    "baseline": baseline_record,
}
metadata_record = dump("metadata-v1.json", metadata)

for record in protected:
    verify(record)
validation = {
    "checked_utc": now(),
    "administrative_only_not_mathematical_evidence": True,
    "all_protected_fingerprints_exact": True,
    "protected_occurrences": len(protected_occurrences),
    "protected_unique_paths": len(protected),
    "immediate_parent_entire_payload_records_exact": True,
    "seven_accepted_statuses_and_literal_candidate_suffixes_exact": True,
    "ALL60_obligation_labels_exact_once_in_order": True,
    "all_four_proposed_claims_and_unverified_label_present": True,
    "historical_unrelated_mathematical_inventories_replayed": False,
    "no_corresponding_NEW_R17_peer_files_findings_or_metadata_accessed": True,
    "separate_full_readback_and_postverification_still_required_before_handoff": True,
}
validation_record = dump("input-validation-v1.json", validation)
payload_suffixes = [
    "interim-v1.md", "candidate-v1.md", "obligations-v1.md", "checks-v1.md",
    "failures-v1.md", "sources-v1.md", "worklog-v1.md", "freeze-v1.py",
    "baseline-v1.json", "metadata-v1.json", "input-validation-v1.json",
]
payloads = [fingerprint(STEM + suffix) for suffix in payload_suffixes]
freeze = {
    "frozen_utc": now(),
    "status": "ENTIRE R17 constructor checkpoint; candidate proof - unverified",
    "whole_obligations": 60,
    "artifact_count_including_this_freeze": 12,
    "ENTIRE_main_ALL60_checks_failures_sources_log_code_ALL_metadata_frozen": True,
    "immediate_own_parent": parent_record,
    "proposed_claims": ["R17A", "R17B", "R17C", "R17D"],
    "two_OTHER_ENTIRE_WHOLE_audits_and_root_reconciliation_required": True,
    "mathematical_program_scan_CAS_or_author_rerun": False,
    "no_full_degree20_annual_lift_height_or_priority_claim": True,
    "artifacts": payloads,
}
freeze_record = dump("freeze-v1.json", freeze)
print(json.dumps({
    "freeze": freeze_record,
    "main": fingerprint(STEM + "candidate-v1.md"),
    "whole_obligations": 60,
    "artifact_count": 12,
    "protected_occurrences": len(protected_occurrences),
    "protected_unique_paths": len(protected),
    "readback_and_separate_postverify_required_before_handoff": True,
}, indent=2))
