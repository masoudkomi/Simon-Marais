#!/usr/bin/env python3
"""NEW independent administrative freezer only; no mathematical evaluation.

No constructor code is imported/run. No NEW corresponding peer file may
be read or hashed. All outputs are exclusive creations under REVIEW.
"""
import datetime
import hashlib
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[3]
REVIEW = "problems/2025-B4/reviews/reasoning-branch-return-r4-review-2-"
AUTHOR = "problems/2025-B4/notes/reasoning-branch-return-r4-"
PEER = "problems/2025-B4/reviews/reasoning-branch-return-r4-review-1-"
PARENT = "problems/2021-B4/notes/reasoning-center-return-r17-freeze-v1.json"
PARENT_EXPECTED = (3018, "5e9d1e9fe34d7e5041f645700d2315e6a5fce38279be9cd9423ade4c7df8ca5f")
AUTHOR_MAIN = (20313, "9535d35d72f559b1889f58966b30c8219eeeb90574625b2514e3cec028fa05ce")
AUTHOR_FREEZE = (7391, "0574b5b9231729c79db541fc26ae01e7ea33a578cd1379cfae71060aabcc3633")


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def raw(path):
    assert isinstance(path, str) and not path.startswith("/")
    assert ".." not in pathlib.Path(path).parts
    assert not path.startswith(PEER), path
    return (ROOT / path).read_bytes()


def obj(path):
    return json.loads(raw(path))


def fingerprint(path):
    data = raw(path)
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def check(record):
    assert fingerprint(record["path"]) == record, record["path"]


def write(suffix, value):
    path = REVIEW + suffix
    with (ROOT / path).open("x", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    return fingerprint(path)


def records_in(value):
    result = []
    if isinstance(value, dict):
        if all(key in value for key in ("path", "bytes", "sha256")):
            result.append({key: value[key] for key in ("path", "bytes", "sha256")})
        for child in value.values():
            result.extend(records_in(child))
    elif isinstance(value, list):
        for child in value:
            result.extend(records_in(child))
    return result


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


target_main = fingerprint(AUTHOR + "candidate-v1.md")
target_freeze = fingerprint(AUTHOR + "freeze-v1.json")
assert (target_main["bytes"], target_main["sha256"]) == AUTHOR_MAIN
assert (target_freeze["bytes"], target_freeze["sha256"]) == AUTHOR_FREEZE
author = obj(target_freeze["path"])
assert author["whole_obligations"] == 64
assert author["new_constructor_files_including_freeze"] == 11
assert len(author["artifacts"]) == 10
for record in author["artifacts"]:
    assert record["path"].startswith(AUTHOR)
    check(record)

author_json_paths = [AUTHOR + suffix for suffix in (
    "freeze-v1.json", "baseline-v1.json", "sources-v1.json", "input-validation-v1.json")]
direct_occurrences = []
for path in author_json_paths:
    direct_occurrences.extend(records_in(obj(path)))
assert len(direct_occurrences) == 58
direct_by_path = {}
for record in direct_occurrences:
    check(record)
    previous = direct_by_path.setdefault(record["path"], record)
    assert previous == record
assert len(direct_by_path) == 50
author_baseline = obj(AUTHOR + "baseline-v1.json")
assert len(author_baseline["protected_fingerprints"]) == 38
assert canonical(author_baseline["protected_fingerprints"]) == author_baseline["canonical_protected_summary_sha256"]
mutable = author_baseline["mutable_landscape_context_snapshots_not_immutable_premises"]
mutable_paths = {record["path"] for record in mutable}
# These two landscape records were also verified above, but are explicitly
# snapshots rather than immutable logical premises; do not guard future
# coordinator-authorized map edits as if they were proof mutations.
assert len(mutable_paths) == 2
protected_occurrences = [r for r in direct_occurrences if r["path"] not in mutable_paths]
protected_occurrences.append(target_freeze)

parent_record = fingerprint(PARENT)
assert (parent_record["bytes"], parent_record["sha256"]) == PARENT_EXPECTED
parent = obj(PARENT)
assert parent["whole_obligations"] == 60
assert parent["artifact_count_including_this_freeze"] == 12
assert len(parent["artifacts"]) == 11
protected_occurrences.append(parent_record)
for record in parent["artifacts"]:
    assert record["path"].startswith("problems/2021-B4/notes/reasoning-center-return-r17-")
    check(record)
    protected_occurrences.append(record)

accepted_inputs = []
for binding in author_baseline["accepted_bindings"]:
    authority = obj(binding["authority_json"])
    assert authority["status"] == "proved, independently reviewed scoped partial result"
    assert authority["unresolved_substantive_issues"] == 0
    assert authority["repair_required"] is False
    accepted, candidate = authority["accepted_copy"], authority["candidate"]
    check(accepted)
    check(candidate)
    assert raw(accepted["path"]).endswith(raw(candidate["path"]))
    assert accepted["path"] == binding["accepted_body"]
    assert candidate["path"] == binding["exact_candidate_suffix"]
    accepted_inputs.append({
        "accepted_copy": accepted,
        "literal_candidate_suffix": candidate,
        "MD_authority": fingerprint(binding["authority_md"]),
        "JSON_authority": fingerprint(binding["authority_json"]),
        "operative": binding["operative"],
        "complete_body_and_authorities_read": True,
        "accepted_and_no_unresolved_issue_status_checked": True,
        "historical_fingerprint_occurrences_bound_not_recopied": authority["record_occurrences_verified"],
        "historical_unique_paths_bound_not_recopied": authority["unique_paths_verified"],
        "old_mathematical_certificates_or_sources_rerun": False,
    })
assert len(accepted_inputs) == 5
assert fingerprint("AGENTS.md")["sha256"] == "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"

dedup = {}
for record in protected_occurrences:
    check(record)
    previous = dedup.setdefault(record["path"], record)
    assert previous == record
protected = [dedup[path] for path in sorted(dedup)]
assert len(protected_occurrences) == 69
assert len(protected) == 61
baseline = {
    "created_utc": now(),
    "purpose": "Independent compact administrative preservation, not mathematical evidence",
    "assigned_review2_prefix_confirmed_unused_before_first_write": True,
    "target_main": target_main,
    "target_freeze": target_freeze,
    "all_eleven_constructor_files_read_and_fingerprints_exact": True,
    "direct_constructor_JSON_record_occurrences_verified": len(direct_occurrences),
    "direct_constructor_JSON_unique_paths_verified": len(direct_by_path),
    "two_mutable_context_snapshots_also_verified_at_freeze_not_immutable_premises": mutable,
    "protected_fingerprint_occurrences": len(protected_occurrences),
    "protected_unique_paths": len(protected),
    "canonical_protected_summary_sha256": canonical(protected),
    "protected": protected,
    "complete_accepted_inputs": accepted_inputs,
    "immediate_own_parent": parent_record,
    "immediate_own_parent_plus_eleven_payloads_verified": True,
    "author_older_parent_and_ancestry_bound_without_recursive_replay": author["immediate_own_parent"],
    "author_older_own_paths_bound_transitively_not_recopied": author["older_own_paths_bound_transitively"],
    "no_new_corresponding_root_BD_R1_finding_file_hash_metadata_accessed": True,
    "no_Git_shared_old_cache_mutation": True,
}
baseline_record = write("baseline-v1.json", baseline)

for suffix in ["obligations-v1.md", "constructor-checks-v1.md"]:
    labels = [int(x) for x in re.findall(r"(?m)^(\d+)\. ", raw(AUTHOR + suffix).decode())]
    assert labels == list(range(1, 65))
ledger_labels = re.findall(r"(?m)^\|(BDR2-\d{2})\|", raw(REVIEW + "ledger-v1.md").decode())
assert ledger_labels == [f"BDR2-{i:02d}" for i in range(1, 65)]
assert "Initially blind nonconstructor audit" in raw(REVIEW + "initial-v1.md").decode()

metadata = {
    "created_utc": now(),
    "status": "ENTIRE initially blind OTHER WHOLE BD R2; not promotion",
    "reviewer": "C /root/review_2017_coarsening_r1",
    "NEW_BD_constructor": "B /root/review_2022_complexity_r2",
    "reviewer_did_not_construct_NEW_BD": True,
    "old_C_R6_R9_RG_FS_authorship_and_RS_BR_UW_review_roles_disclosed": True,
    "not_independent_fresh_recertification_of_own_older_inputs": True,
    "root_old_RS_contribution_is_old_input_not_NEW_BD_construction": True,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
    "verified_effective_setting_readback": None,
    "whole_obligations": 64,
    "complete_new_constructor_files_read": 11,
    "complete_current_accepted_bodies_and_MD_JSON_read": 5,
    "complete_primary_operative_Jacobi_section_and_Hadamard_context_read": True,
    "full_source_Theorems3_4_or_class_number_foundations_newly_certified": False,
    "mathematical_program_CAS_scan_test_author_certificate_or_freezer_rerun": False,
    "corresponding_NEW_root_BD_R1_file_finding_hash_metadata_accessed": False,
    "identity_only_completion_until_explicit_BOTH_entire_confirmation": True,
    "latest_parent_authoritative_TOTAL_percent": 28,
    "latest_parent_telemetry_utc": "2026-10-18T10:59:28Z",
    "only_current_authorized_reset": 1792874445,
    "TOTAL_ceiling_percent": 90,
    "integration_reserve_and_no_automatic_later_window": True,
    "pending_tool_approval_child_or_stall": False,
    "immediate_own_parent": parent_record,
    "baseline": baseline_record,
}
metadata_record = write("metadata-v1.json", metadata)
for record in protected:
    check(record)
validation = {
    "checked_utc": now(),
    "administrative_only_not_a_mathematical_test_or_proof": True,
    "target_main_freeze_and_all_eleven_constructor_files_exact": True,
    "direct_author_JSON_occurrences_verified": 58,
    "direct_author_JSON_unique_paths_verified": 50,
    "protected_occurrences_verified": 69,
    "protected_unique_paths_verified": 61,
    "five_current_accepted_statuses_and_literal_suffixes_exact": True,
    "ALL64_author_obligations_and_dispositions_labels_exact": True,
    "ALL64_independent_review_ledger_labels_exact_once_in_order": True,
    "NEW_root_BD_R1_material_read_or_hashed": False,
    "constructor_or_old_mathematical_code_executed": False,
    "complete_generated_metadata_full_readback_and_SEPARATE_postverify_required_before_handoff": True,
}
validation_record = write("input-validation-v1.json", validation)
suffixes = [
    "initial-v1.md", "ledger-v1.md", "issues-v1.md", "sources-v1.md",
    "worklog-v1.md", "freeze-v1.py", "baseline-v1.json", "metadata-v1.json",
    "input-validation-v1.json",
]
artifacts = [fingerprint(REVIEW + suffix) for suffix in suffixes]
manifest = {
    "frozen_utc": now(),
    "status": "ENTIRE initially blind OTHER WHOLE BD R2 frozen; not promotion",
    "whole_obligations": 64,
    "review_file_count": 10,
    "ENTIRE_report_ALL64_ledger_issues_source_log_code_ALLmetadata_frozen": True,
    "no_corresponding_NEW_root_BD_R1_finding_file_hash_metadata_accessed": True,
    "identity_only_completion_until_explicit_BOTH_entire_confirmation": True,
    "target_main": target_main,
    "target_freeze": target_freeze,
    "immediate_own_parent": parent_record,
    "artifacts": artifacts,
}
manifest_record = write("manifest-v1.json", manifest)
print(json.dumps({
    "ENTIRE_initial_freeze_identity_only": True,
    "manifest": manifest_record,
    "initial": fingerprint(REVIEW + "initial-v1.md"),
    "whole_obligations": 64,
    "review_files": 10,
    "all_metadata_readback_and_SEPARATE_postverify_still_required": True,
}, indent=2))
