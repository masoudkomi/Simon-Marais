"""Administrative known-file fingerprints and JSON only; no mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2024-B4/reviews/P2-critical-jet-review-1-"
TARGET = "problems/2024-B4/notes/coordinator-P2-critical-jet-return-v1.md"
TARGET_SHA = "fa5b79ce59303a06a61da18ee902235bc299add309aa0725846bbfd3a7716f26"
AUTHOR_MANIFEST = "problems/2024-B4/notes/coordinator-P2-critical-jet-manifest-v1.json"
AUTHOR_SHA = "d1926b3e81b4952ad29c46dcda57b932365d8b36728b228a31d169dfda67cec3"


def fp(path):
    data = (ROOT / path).read_bytes()
    return {"path": str(path), "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def checked(rec):
    actual = fp(rec["path"])
    if actual["bytes"] != rec["bytes"] or actual["sha256"] != rec["sha256"]:
        raise RuntimeError("Fingerprint mismatch: " + rec["path"])
    return dict(actual, matches=True)


def read_json(path):
    return json.loads((ROOT / path).read_text())


def all_fps(obj):
    if isinstance(obj, dict):
        if {"path", "bytes", "sha256"} <= obj.keys():
            yield obj
        for value in obj.values():
            yield from all_fps(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from all_fps(value)


def save(suffix, obj):
    path = ROOT / (PREFIX + suffix)
    if path.exists():
        raise RuntimeError("Refusing to overwrite: " + str(path))
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


now = datetime.now(timezone.utc).isoformat()
assert fp(TARGET)["bytes"] == 6774
assert fp(TARGET)["sha256"] == TARGET_SHA
assert fp(AUTHOR_MANIFEST)["bytes"] == 1089
assert fp(AUTHOR_MANIFEST)["sha256"] == AUTHOR_SHA
author = read_json(AUTHOR_MANIFEST)
author_records = [checked(rec) for rec in author["records"]]
assert len(author_records) == 3

gk_accept_path = "problems/2024-B4/reviews/generalized-Kasami-acceptance.json"
gk_authority_rows = [checked(rec) for rec in all_fps(read_json(gk_accept_path))]
gk_manifest_path = "problems/2024-B4/notes/coordinator-generalized-Kasami-r1-manifest-v1.json"
assert fp(gk_manifest_path)["sha256"] == "50c3269d28a49327e28e216a857fdb711dae8875cab127645bc4081f2ac9ec65"
gk_records = [checked(rec) for rec in read_json(gk_manifest_path)["records"]]
assert len(gk_records) == 6
gk_input_path = "problems/2024-B4/notes/coordinator-generalized-Kasami-r1-input-validation-v1.json"
gk_input = read_json(gk_input_path)
gk_input_rows = [checked(rec) for rec in gk_input["records"]]
assert len(gk_input_rows) == 417
assert len({rec["path"] for rec in gk_input_rows}) == 214
gk_old_motivation_cache = checked(gk_input["motivation_cache_only_not_new_theorem_premise"])

previous_input_path = "problems/2022-B4/reviews/reasoning-return-r5-review-1-input-validation-v1.json"
previous_manifest_path = "problems/2022-B4/reviews/reasoning-return-r5-review-1-manifest-v1.json"
assert fp(previous_manifest_path)["sha256"] == "e047f54566a6b63e74a7885a937932e34fe34d08b269377d8f8b6b09871f5c96"
previous_input = read_json(previous_input_path)
previous_manifest = read_json(previous_manifest_path)
older = []
for item in previous_input["older_own_packets"]:
    older.append({"manifest": checked(item["manifest"]),
                  "checks": [checked(rec) for rec in item["checks"]]})
older.append({"manifest": fp(previous_manifest_path),
              "checks": [checked(rec) for rec in previous_manifest["records"]]})
assert len(older) == 46
gk_addendum = checked(previous_input["GK_separate_telemetry_addendum_preserved"])

context_paths = [
    "problems/2024-B4/notes/coordinator-P2-critical-fixed-return-v1.md",
    "problems/2024-B4/notes/coordinator-higher-family-composition-return-v1.md",
]
context_expected = [
    "d309653d612d8cf18a542b6c9c89cbd310c577e369bc13898a0863d6a00bc300",
    "00e573d6f9794e84bcc6bbe92a979dfdce0d2ba4df1b4fba91bbaa051740b9a0",
]
for path, expected in zip(context_paths, context_expected):
    assert fp(path)["sha256"] == expected
ledger = read_json(PREFIX + "issues-v1.json")
assert len(ledger["checks"]) == 30
assert {row["id"] for row in ledger["checks"]} == {
    "CJR1-" + str(i).zfill(2) for i in range(1, 31)
}
covered = {o for row in ledger["checks"] for o in row["obligations"]}
assert covered == set(range(1, 7))
assert ledger["substantive_objections"] == []
assert ledger["required_author_repairs"] == []
assert all(row["disposition"] == "clear" for row in ledger["checks"])

usage = {"at_utc": "2026-10-17 13:12:26 UTC (paired telemetry and clock)",
         "total_used_percent": 40, "window_minutes": 10080,
         "reset_unix": 1792745187, "total_ceiling_percent": 90,
         "integration_reserve": True, "ordinary_usage_allowed": True}
validation = {
    "checked_at_utc": now, "metadata_only_no_mathematical_computation": True,
    "constructor_manifest": fp(AUTHOR_MANIFEST),
    "constructor_three_records": author_records,
    "accepted_GK_complete_body_read": fp("problems/2024-B4/proofs/reviewed-generalized-Kasami-v1.1.md"),
    "accepted_GK_complete_scope_text_read": fp("problems/2024-B4/reviews/generalized-Kasami-acceptance.md"),
    "accepted_GK_authority_JSON": fp(gk_accept_path),
    "accepted_GK_authority_declared_fingerprints": gk_authority_rows,
    "GK_frozen_constructor_manifest": fp(gk_manifest_path),
    "GK_six_artifacts": gk_records,
    "GK_old_input_declared_fingerprints": gk_input_rows,
    "GK_old_motivation_cache_preserved_not_new_premise": gk_old_motivation_cache,
    "older_unverified_context_read_not_accepted_premise": [fp(path) for path in context_paths],
    "official_statement_read": fp("problems/2024-B4/statement.md"),
    "applicable_protocol_read": fp("AGENTS.md"),
    "fresh_official_web_read_no_new_binary_hash_claim": True,
    "older_own_packets": older,
    "all_forty_six_older_own_packets_unchanged": True,
    "GK_separate_telemetry_addendum_preserved": gk_addendum,
    "old_T1_T4_C7_C11_authorship_and_CP_GK_KC_whole_review_roles_disclosed": True,
    "new_CJ_strategy_construction_or_repair_contribution": False,
    "new_peer_CJ_findings_or_later_root_inspection_read_before_freeze": False,
    "first_CJ_target_read_AFTER_complete_2022_R5_R1_freeze": True,
    "complete_initially_blind_whole_reconstruction": True,
    "all_six_end_obligations_reconstructed": True,
    "local_order_exactly_q_and_q5_jet_reconstructed": True,
    "zero_K_and_inseparable_H_included": True,
    "polynomial_not_finite_field_function_divisibility": True,
    "necessary_not_sufficient_composition_condition": True,
    "mathematical_program_CAS_scan_enumeration_certificate_replay_or_author_rerun": False,
    "only_current_assigned_prefix_written": True,
    "candidate_old_shared_or_Git_mutation": False,
    "full_composition_factorization_annual_or_novelty_claim": False,
    "administrative_patch_syntax_rejection_before_any_write_corrected_before_freeze": True,
}
save("input-validation-v1.json", validation)

output = {
    "checked_at_utc": now, "metadata_only_no_mathematical_computation": True,
    "candidate": fp(TARGET), "constructor_manifest": fp(AUTHOR_MANIFEST),
    "constructor_records_checked": len(author_records),
    "accepted_GK_authority_fingerprint_occurrences_checked": len(gk_authority_rows),
    "accepted_GK_frozen_artifacts_checked": len(gk_records),
    "accepted_GK_old_input_occurrences_checked": len(gk_input_rows),
    "accepted_GK_old_input_unique_paths_checked": len({row["path"] for row in gk_input_rows}),
    "whole_claims": ["CJ1"], "per_inference_ledger_rows": 30,
    "author_obligations_covered": len(covered),
    "older_own_packets_unchanged": len(older),
    "all_hash_checks_passed": True,
    "substantive_objections": 0, "required_author_repairs": 0,
    "new_peer_CJ_findings_or_later_root_inspection_read_before_freeze": False,
    "latest_authoritative_weekly_usage": usage,
    "command": "python3 problems/2024-B4/reviews/P2-critical-jet-review-1-freeze-v1.py",
}
save("freeze-output-v1.json", output)
names = ["initial-v1.md", "issues-v1.json", "source-checks-v1.md",
         "freeze-v1.py", "input-validation-v1.json", "freeze-output-v1.json"]
manifest = {
    "frozen_at_utc": now,
    "status": "complete initially blind independent nonconstructor WHOLE CJ1 initial R1 audit",
    "reviewer": "/root/review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_sha256": TARGET_SHA, "constructor_manifest_sha256": AUTHOR_SHA,
    "whole_claims": ["CJ1"], "per_inference_ledger_rows": 30,
    "author_obligations_covered": 6,
    "substantive_objections": 0, "required_author_repairs": 0,
    "old_authorship_and_CP_GK_KC_whole_review_roles_disclosed": True,
    "new_CJ_construction_strategy_or_repair_contribution": False,
    "new_peer_CJ_findings_or_later_root_inspection_read_before_freeze": False,
    "findings_sent_before_complete_initial_freeze": False,
    "full_composition_factorization_annual_or_novelty_claim": False,
    "mathematical_program_CAS_scan_enumeration_author_rerun": False,
    "candidate_shared_old_files_or_git_mutation": False,
    "spawning_contact_charge_or_access_bypass": False,
    "coordinator_promotion_performed": False,
    "latest_authoritative_weekly_usage": usage,
    "command": output["command"],
    "records": [fp(PREFIX + name) for name in names],
}
save("manifest-v1.json", manifest)
print(json.dumps(dict(output, manifest=fp(PREFIX + "manifest-v1.json")), indent=2))
