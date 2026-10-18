"""Reviewer metadata only: bytes/SHA, JSON, authority pointers, ledger labels.

Commands: python3 THIS --baseline; python3 THIS --freeze; python3 THIS --verify.
No mathematical calculation, scan, CAS, source replay, or author-code run.
Only new assigned reasoning-Runge-return-r3-review-1-* files may be written.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2025-B4/reviews/reasoning-Runge-return-r3-review-1"
TARGET = "problems/2025-B4/notes/reasoning-Runge-return-r3"
PARENT = "problems/2024-B4/reviews/cofactor-cubic-r3-review-1-manifest-v1.json"
EXPECTED = {
    TARGET + "-candidate-v1.md": (23038, "5ccc04e72574187d1959efff22852dbbc5cca41e701afbaeebc9f97adbdf64a0"),
    TARGET + "-freeze-v1.json": (8661, "6a010ee19e90b4a07373f64dd375e9df7e6c8d4aee9ec7af001d8410e5bb461a"),
    PARENT: (4450, "c3d0be4190f076a273cfb2da3a1fb49f48ac3076f0e01bf5667ce39d825eec7d"),
}
AUTHORITIES = [
    "problems/2025-B4/reviews/reasoning-Runge-return-r2-acceptance.json",
    "problems/2025-B4/reviews/reasoning-return-r6-acceptance.json",
    "problems/2025-B4/reviews/reasoning-return-r9-runge-acceptance.json",
]
PAYLOAD_SUFFIXES = [
    "initial-v1.md", "ledger-v1.md", "issues-v1.md", "sources-v1.md",
    "sources-v1.json", "worklog-v1.md", "freeze-v1.py", "baseline-v1.json",
    "metadata-v1.json", "input-validation-v1.json",
]
TELEMETRY = {
    "method": "authoritative get_usage_limits and clock in same independent batch",
    "observed_utc": "2026-10-18 09:44:24 UTC",
    "used_percent_TOTAL": 22, "window_minutes": 10080,
    "reset_unix": 1792874445, "ordinary_usage_allowed": True,
    "legacy_by_limit_agree": True, "account_suffix": "1334ac3a",
    "human_authorized_current_window_only": True,
    "ceiling_TOTAL_percent": 90, "integration_reserve": True,
    "automatic_later_week_spending": False,
}


def now():
    return datetime.now(timezone.utc).isoformat()


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def record(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": sha(data)}


def load(path):
    return json.loads((ROOT / path).read_text())


def verify_record(rec):
    assert record(rec["path"]) == rec, rec["path"]


def put_new(path, obj):
    assert path.startswith(PREFIX + "-")
    with (ROOT / path).open("x") as out:
        json.dump(obj, out, ensure_ascii=False, indent=2)
        out.write("\n")


def parent_summary(path):
    rows = []

    def visit(obj):
        if isinstance(obj, dict):
            if isinstance(obj.get("path"), str) and isinstance(obj.get("bytes"), int) and isinstance(obj.get("sha256"), str):
                rows.append({key: obj[key] for key in ("path", "bytes", "sha256")})
            for value in obj.values():
                visit(value)
        elif isinstance(obj, list):
            for value in obj:
                visit(value)

    visit(load(path))
    dedup = sorted({canonical(rec) for rec in rows})
    return {
        "immutable_parent": record(path),
        "declared_fingerprint_occurrences": len(rows),
        "deduplicated_paths": len({rec["path"] for rec in rows}),
        "canonical_deduplicated_record_summary_sha256": sha(b"\n".join(dedup)),
        "historical_inventory_bound_not_recopied_or_recursively_reverified": True,
    }


def accepted_pointers():
    result = []
    for path in AUTHORITIES:
        obj = load(path)
        assert obj["status"] == "proved, independently reviewed scoped partial result"
        assert obj["unresolved_substantive_issues"] == 0
        verify_record(obj["accepted_copy"])
        result.append({"authority": record(path), "accepted_body": obj["accepted_copy"]})
    return result


def baseline():
    for path, (size, digest) in EXPECTED.items():
        rec = record(path)
        assert (rec["bytes"], rec["sha256"]) == (size, digest), path
    target = load(TARGET + "-freeze-v1.json")
    oldbase = load(TARGET + "-baseline-v1.json")
    parent = load(PARENT)
    records = [record(TARGET + "-freeze-v1.json")] + target["artifacts"] + oldbase["protected"]
    records += [record(PARENT)] + parent["artifacts"]
    for rec in records:
        verify_record(rec)
    by_path = {}
    for rec in records:
        assert rec["path"] not in by_path or by_path[rec["path"]] == rec
        by_path[rec["path"]] = rec
    guards = [by_path[key] for key in sorted(by_path)]
    obj = {
        "created_utc": now(), "status": "reviewer compact preservation baseline; metadata only",
        "prefix_unused_confirmed_by_exact_rg_exit1_before_first_write": True,
        "target_main": record(TARGET + "-candidate-v1.md"),
        "target_constructor_freeze": record(TARGET + "-freeze-v1.json"),
        "protected": guards, "current_occurrences": len(records),
        "current_unique_paths": len(guards), "canonical_current_summary_sha256": sha(canonical(guards)),
        "accepted_pointers": accepted_pointers(),
        "compact_immutable_parents": [parent_summary(path) for path in AUTHORITIES + [TARGET + "-freeze-v1.json", PARENT]],
        "own_immediate_parent": record(PARENT),
        "no_corresponding_C_NEW_R3_review_file_finding_hash_or_metadata_access": True,
        "no_math_program_CAS_scan_author_rerun_or_old_write": True,
        "authoritative_weekly_telemetry": TELEMETRY,
    }
    path = PREFIX + "-baseline-v1.json"
    put_new(path, obj)
    print(json.dumps({"baseline": record(path), "current_occurrences": len(records), "current_unique_paths": len(guards)}))


def freeze():
    base_path = PREFIX + "-baseline-v1.json"
    base = load(base_path)
    for rec in base["protected"]:
        verify_record(rec)
    pointers = accepted_pointers()
    ledger = (ROOT / (PREFIX + "-ledger-v1.md")).read_text()
    labels = re.findall(r"\| (R3O-\d{2}) \|", ledger)
    assert labels == [f"R3O-{i:02d}" for i in range(1, 61)]
    sources = load(PREFIX + "-sources-v1.json")
    assert sources["no_new_peer_review_access"] is True
    metadata = {
        "generated_utc": now(), "metadata_only_NOT_mathematical_evidence": True,
        "all60_manual_dispositions_present_once_in_order": True,
        "current_protected_occurrences": base["current_occurrences"],
        "current_protected_unique_paths": base["current_unique_paths"],
        "canonical_current_summary_sha256": base["canonical_current_summary_sha256"],
        "accepted_pointers": pointers,
        "whole_main_ALL60_failures_sources_log_code_and_constructor_metadata_read": True,
        "no_corresponding_C_NEW_R3_review_files_findings_hashes_or_metadata_read": True,
        "nonnegative_INTEGER_weight_scope_explicit": True,
        "mathematical_code_CAS_scan_author_freezer_source_rerun": False,
        "old_files_unchanged": True, "authoritative_weekly_telemetry": TELEMETRY,
    }
    put_new(PREFIX + "-metadata-v1.json", metadata)
    validation = {
        "verified_utc": now(), "metadata_only": True,
        "target_main_and_constructor_freeze_exact_assigned_bytes_SHA": True,
        "all_current_inputs_unchanged": True, "accepted_pointers_exact": len(pointers),
        "entire_ALL60_hand_ledger_complete": True,
        "source_JSON_parsed": True,
        "compact_parent_record_occurrences_and_dedup_summary_bound": True,
        "no_new_corresponding_peer_path_access_or_hash": True,
        "no_recursive_historical_inventory_or_math_executable": True,
    }
    put_new(PREFIX + "-input-validation-v1.json", validation)
    payloads = [record(PREFIX + "-" + suffix) for suffix in PAYLOAD_SUFFIXES]
    manifest = {
        "frozen_utc": now(), "status": "ENTIRE initially blind OTHER WHOLE R1 review recommendation; not promotion",
        "reviewer": "/root/review_2021_reasoning_j15_r2",
        "B_NEW_constructor_and_root_OLDER_quotient_contributor_excluded": True,
        "target_main": base["target_main"], "target_constructor_freeze": base["target_constructor_freeze"],
        "all60_obligations_reconstructed": True,
        "substantive_defects_found": 0, "required_author_repairs": 0,
        "closed_scope_notes": 8,
        "entire_report_ALL60_ledger_issues_sources_log_code_ALL_metadata_frozen": True,
        "no_corresponding_C_NEW_R3_review_finding_file_hash_or_metadata_access_through_ENTIRE_freeze": True,
        "findings_withheld_until_BOTH_entire_initials_confirmed": True,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independently_verified_effective_settings": None,
        "exact_scope": "BR1--BR5 signed actual prime diagonal p>=37, integer weights, scoped label/residual consequences only",
        "no_unrestricted_prime_bound_actual_existence_annual_or_novelty_claim": True,
        "baseline": record(base_path),
        "current_protected_occurrences": base["current_occurrences"],
        "current_protected_unique_paths": base["current_unique_paths"],
        "canonical_current_summary_sha256": base["canonical_current_summary_sha256"],
        "own_immediate_parent": base["own_immediate_parent"],
        "compact_parents": base["compact_immutable_parents"],
        "historical_inventories_not_recopied_or_recursively_reverified": True,
        "authoritative_weekly_telemetry": TELEMETRY,
        "mathematical_program_CAS_scan_author_source_or_freezer_rerun": False,
        "no_Git_shared_old_cache_write_spawn_contact_charge_or_bypass": True,
        "payloads": len(payloads), "files_including_manifest": len(payloads) + 1,
        "artifacts": payloads,
    }
    path = PREFIX + "-manifest-v1.json"
    put_new(path, manifest)
    verify()


def verify():
    path = PREFIX + "-manifest-v1.json"
    obj = load(path)
    for rec in obj["artifacts"]:
        verify_record(rec)
    base = load(PREFIX + "-baseline-v1.json")
    for rec in base["protected"]:
        verify_record(rec)
    accepted_pointers()
    print(json.dumps({"manifest": record(path), "initial": record(PREFIX + "-initial-v1.md"),
                      "whole_obligations": 60, "payloads": obj["payloads"],
                      "files_including_manifest": obj["files_including_manifest"],
                      "current_protected_occurrences": base["current_occurrences"],
                      "current_unique_paths": base["current_unique_paths"],
                      "postverification": "exact; no promotion; findings remain withheld"}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--baseline", action="store_true")
    group.add_argument("--freeze", action="store_true")
    group.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    baseline() if args.baseline else freeze() if args.freeze else verify()
