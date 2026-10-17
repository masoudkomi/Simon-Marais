"""Reviewer known-file JSON/SHA integrity only; no mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2019-B4/reviews/auxiliary-presentation-r1-review-1-"
TARGET = "problems/2019-B4/notes/auxiliary-presentation-r1-"
PREVIOUS = "problems/2017-B4/reviews/reasoning-value-return-r3-review-2-"
FORBIDDEN = "problems/2019-B4/reviews/auxiliary-presentation-r1-review-2-"


def fp(path):
    path = str(path)
    if path.startswith(FORBIDDEN):
        raise RuntimeError("Blindness guard: no new AF peer read/hash")
    b = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}


inventory = {}
occurrences = 0


def checked(rec):
    global occurrences
    actual = fp(rec["path"])
    if actual["bytes"] != rec["bytes"] or actual["sha256"] != rec["sha256"]:
        raise RuntimeError("Fingerprint mismatch: " + rec["path"])
    occurrences += 1
    if actual["path"] in inventory:
        assert inventory[actual["path"]] == actual
    inventory[actual["path"]] = actual
    return actual


def bind(path):
    return checked(fp(path))


def read_json(path):
    if path.startswith(FORBIDDEN):
        raise RuntimeError("Blindness guard: no new AF peer JSON")
    return json.loads((ROOT / path).read_text())


def rows(obj):
    if isinstance(obj, dict):
        if {"path", "bytes", "sha256"} <= obj.keys():
            yield obj
        for value in obj.values():
            yield from rows(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from rows(value)


def save(suffix, obj):
    with (ROOT / (PREFIX + suffix)).open("x") as f:
        f.write(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


now = datetime.now(timezone.utc).isoformat()
main_expected = {"path": TARGET + "candidate-v1.md", "bytes": 8849,
                 "sha256": "a0cc010860ee21155239421bef44e95e3ce2cec84be6796a9e067b39afcf4372"}
freeze_expected = {"path": TARGET + "freeze-v1.json", "bytes": 1705,
                   "sha256": "114dabe97999c84e37687c3e88b7e8f65080f93ac3477ab708e99712d0ffcbb5"}
checked(main_expected)
checked(freeze_expected)
constructor_manifest = read_json(freeze_expected["path"])
constructor_records = [checked(r) for r in constructor_manifest["records"]]
assert len(constructor_records) == 5
constructor_integrity = read_json(TARGET + "integrity-v1.json")
constructor_input_records = [checked(r) for r in rows(constructor_integrity)]
assert len(constructor_input_records) == 20
authority_path = "problems/2019-B4/reviews/secondpass-acceptance.json"
authority_fp = bind(authority_path)
authority = read_json(authority_path)
authority_rows = []
for relative_path, digest in authority["artifacts"].items():
    actual = fp("problems/2019-B4/" + relative_path)
    assert actual["sha256"] == digest
    authority_rows.append(checked(actual))
assert len(authority_rows) == 14
read_scopes = [bind(p) for p in [
    "AGENTS.md", "problems/2019-B4/statement.md",
    "problems/2019-B4/notes/secondpass-rigidity-obstructions.md",
    "problems/2019-B4/notes/secondpass-canonical-renewal.md",
    "problems/2019-B4/notes/secondpass-staircases-and-pumping.md",
    "problems/2019-B4/notes/secondpass-checkpoint-2.md",
    "problems/2019-B4/proofs/reviewed-secondpass-v1.1.md",
    "problems/2019-B4/reviews/secondpass-acceptance.md",
    "problems/2019-B4/reviews/secondpass-acceptance.json",
    "problems/2019-B4/reviews/secondpass-acceptance-issues-snapshot.md",
]]

previous_expected = {"path": PREVIOUS + "manifest-v1.json", "bytes": 3394,
                     "sha256": "f286838bef70e2b2b67848c150d13d5e57ac8f94ba247dc0e2e3a4bf7d4d8e30"}
previous_manifest_fp = checked(previous_expected)
previous_manifest = read_json(previous_expected["path"])
previous_validation_fp = bind(PREVIOUS + "input-validation-v1.json")
previous_validation = read_json(previous_validation_fp["path"])
before = occurrences
for rec in rows(previous_validation):
    checked(rec)
previous_occurrences = occurrences - before
previous_records = [checked(rec) for rec in previous_manifest["records"]]
older = {}
for rec in previous_validation["older_own_records"] + previous_records + [previous_manifest_fp]:
    actual = checked(rec)
    older[actual["path"]] = actual
assert len(older) == 307

author_obligations = (ROOT / (TARGET + "obligations-v1.md")).read_text()
ledger = (ROOT / (PREFIX + "issues-v1.md")).read_text()
assert set(re.findall(r"AF-[0-9]{2}", author_obligations)) == {f"AF-{i:02d}" for i in range(1, 11)}
assert set(re.findall(r"AF-[0-9]{2}", ledger)) == {f"AF-{i:02d}" for i in range(1, 11)}
assert set(re.findall(r"AFR1-[0-9]{2}", ledger)) == {f"AFR1-{i:02d}" for i in range(1, 25)}
for suffix in ["initial-v1.md", "issues-v1.md", "source-checks-v1.md"]:
    assert (ROOT / (PREFIX + suffix)).read_text().strip()

usage = {"at_utc": "2026-10-17 16:29:42 UTC", "total_used_percent": 51,
         "window_minutes": 10080, "reset_unix": 1792745187,
         "ordinary_usage_allowed": True, "total_ceiling_percent": 90,
         "integration_reserve": True}
validation = {
    "checked_at_utc": now,
    "reviewer": "/root/review_2022_complexity_r2",
    "status": "complete initially blind whole R1; no substantive defect found; no promotion",
    "requested_model": "gpt-6.1-sol", "requested_reasoning_effort": "max",
    "independently_verified_effective_settings": None,
    "metadata_only_not_mathematical_evidence": True,
    "new_AF_peer_report_ledger_source_manifest_or_findings_read": False,
    "new_AF_peer_prefix_explicitly_guarded_against_read_or_hash": FORBIDDEN,
    "assigned_unused_prefix_confirmed_before_first_write": True,
    "new_AF_constructor_or_proof_contributor": False,
    "root_constructor_excluded_from_independent_review_count": True,
    "older_2019_whole_review_roles_disclosed_not_fresh_self_recertification": True,
    "complete_new_main10_obligations_source_failures_worklog_integrity_and_freeze_read": True,
    "constructor_five_records_plus_freeze_six_files_verified": constructor_records,
    "constructor_integrity_all20_declared_records_verified": constructor_input_records,
    "accepted_secondpass_authority": authority_fp,
    "accepted_old_schema_relative_path_SHA_dictionary14_entries_verified": authority_rows,
    "complete_accepted_linked_bodies_register_and_scope_texts_freshly_read": read_scopes,
    "all_constructor_obligation_ids": [f"AF-{i:02d}" for i in range(1, 11)],
    "complete_reviewer_inference_check_ids": [f"AFR1-{i:02d}" for i in range(1, 25)],
    "substantive_issues_identified": 0, "author_repair_requested": False,
    "AF1_typed_maps_both_inclusions_all_contexts_inverse_steps_and_empty_words_reconstructed": True,
    "AF2_actual_rigid_branches_proper_factor_first_change_and_every_finite_alphabet_reconstructed": True,
    "finite_rewriting_trace_consequences_same_monoid_scope_reconstructed": True,
    "ambient_product_finite_presentation_and_finite_two_tape_loop_scope_counterchecks_by_hand": True,
    "odd_phase_unmarked_output_relations_not_conflated_with_even_M0": True,
    "primary_actual_read_scopes": [
        {"url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-paper-b_1.pdf",
         "scope": "Actual page2 B4 definition and (b); no preliminary proof or other problem investigated"},
        {"url": "https://www.researchgate.net/publication/45896849_Decision_problems_for_finite_and_infinite_presentations_of_groups_and_monoids",
         "scope": "Author text sections1/9 specified in source checks; not full survey or external proof"},
        {"url": "https://arxiv.org/pdf/1001.3981",
         "scope": "Definitions1.1-1.4,1.7-1.10/Remark1.3;9.1-9.3/Proposition9.2 finite discussion;Remark9.5 generator substitution passage. Not full39pages or cited outside proof"},
    ],
    "classical_Tietze_attribution_direct_proof_no_algorithmic_or_group_only_import": True,
    "old_fixed_generator_obstruction_not_new_discovery": True,
    "full_annual_value_defect_growth_rationality_cross_section_or_novelty_claim": False,
    "native_source_binary_hash_or_download_claim": False,
    "mathematical_program_scan_CAS_certificate_source_algorithm_or_author_rerun": False,
    "previous_own_manifest": previous_manifest_fp,
    "previous_own_validation": previous_validation_fp,
    "previous_declared_metadata_occurrences_reverified": previous_occurrences,
    "all_source_document_fingerprint_occurrences_verified": occurrences,
    "input_unique_paths_verified": len(inventory),
    "deduplication_policy": "Every occurrence checked; complete unique inventory and immutable source references retained",
    "deduplicated_all_verified_input_records": [inventory[p] for p in sorted(inventory)],
    "older_own_records": [older[p] for p in sorted(older)],
    "older_own_unique_frozen_paths_preserved": len(older),
    "old_shared_Git_cache_other_owner_edits_spawning_contact_charge_bypass": False,
    "direct_weekly_telemetry": usage, "all_verified": True,
}
save("input-validation-v1.json", validation)
names = ["initial-v1.md", "issues-v1.md", "source-checks-v1.md", "freeze-v1.py", "input-validation-v1.json"]
manifest = {
    "frozen_at_utc": now, "reviewer": validation["reviewer"], "status": validation["status"],
    "requested_model": "gpt-6.1-sol", "requested_reasoning_effort": "max",
    "independently_verified_effective_settings": None,
    "constructor_target_main": main_expected, "constructor_target_freeze": freeze_expected,
    "whole_claims_reviewed": ["AF1 finite-generator transport for arbitrary finite monoid presentation", "AF2 no finite presentation of actual even M0 on any finite alphabet and precise rewriting/trace consequences"],
    "all10_constructor_obligations_covered": True, "complete_reviewer_inference_checks": 24,
    "substantive_issues_identified": 0, "author_repair_requested": False,
    "initial_frozen_before_any_new_AF_peer_findings": True,
    "new_AF_nonconstructor_independence_and_old_roles_disclosed": True,
    "actual_even_homomorphism_identity_and_odd_phase_firewall_preserved": True,
    "accepted_fixed_generator_result_not_rediscovered_or_repaired": True,
    "external_classical_attribution_actual_bounded_read_scopes_preserved": True,
    "embedding_transducer_regular_cross_section_growth_value_or_novelty_exclusion_claim": False,
    "mathematical_program_scan_CAS_certificate_source_algorithm_or_author_rerun": False,
    "source_document_fingerprint_occurrences_verified": occurrences,
    "input_unique_paths_verified": len(inventory),
    "repeated_historical_rows_deduplicated_with_immutable_source_references": True,
    "older_own_unique_frozen_paths_preserved": len(older),
    "old_shared_Git_cache_other_owner_edits_spawning_contact_charge_bypass": False,
    "direct_weekly_telemetry": usage,
    "records": [fp(PREFIX + suffix) for suffix in names],
}
save("manifest-v1.json", manifest)
print(json.dumps({"frozen_at_utc": now, "manifest": fp(PREFIX + "manifest-v1.json"),
                  "records": manifest["records"], "all10_obligations_24_checks_complete": True,
                  "source_occurrences_verified": occurrences, "input_unique_paths_verified": len(inventory),
                  "older_own_unique_frozen_paths_preserved": len(older),
                  "substantive_issues_identified": 0}, indent=2))
