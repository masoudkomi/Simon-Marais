"""Metadata only. No mathematical calculation, scan, CAS or author rerun.
Use --baseline, --freeze, --verify. Only new assigned review-prefix writes.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2024-B4/reviews/cofactor-dominant-r4-review-1"
T = "problems/2024-B4/notes/cofactor-dominant-r4"
AUTH = "problems/2024-B4/reviews/cofactor-global-r2-acceptance.json"
PARENT = "problems/2025-B4/reviews/reasoning-Runge-return-r3-review-1-manifest-v1.json"
EXPECTED = {
    T + "-candidate-v1.md": (14524, "b6c454eba513c0ebb364f4b53393741c8737239c5b03c75fc2a0ac000871e365"),
    T + "-freeze-v1.json": (3054, "1d0c4e90c0b75a2417539401d4350e13dd29c9d3030fc06074f4cff18358371b"),
    PARENT: (7609, "fc0c00b693a08c601f66954c96aa1c39d0fe3b340e26a616fad17e8495789e7a"),
}
SUFFIXES = ["initial-v1.md", "ledger-v1.md", "issues-v1.md", "sources-v1.md",
            "sources-v1.json", "worklog-v1.md", "freeze-v1.py", "baseline-v1.json",
            "metadata-v1.json", "input-validation-v1.json"]
TELEMETRY = {
    "observed_utc": "2026-10-18 09:54:22 UTC",
    "method": "authoritative get_usage_limits and clock in same independent batch",
    "used_percent_TOTAL": 23, "window_minutes": 10080, "reset_unix": 1792874445,
    "ordinary_usage_allowed": True, "legacy_by_limit_agree": True,
    "account_suffix": "1334ac3a", "ceiling_TOTAL_percent": 90,
    "integration_reserve": True, "human_authorized_current_window_only": True,
    "automatic_later_week_spending": False,
}


def now():
    return datetime.now(timezone.utc).isoformat()


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()


def digest(data):
    return hashlib.sha256(data).hexdigest()


def rec(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": digest(data)}


def load(path):
    return json.loads((ROOT / path).read_text())


def check(row):
    assert rec(row["path"]) == {key: row[key] for key in ("path", "bytes", "sha256")}, row["path"]


def put(suffix, obj):
    path = P + "-" + suffix
    with (ROOT / path).open("x") as out:
        json.dump(obj, out, indent=2, ensure_ascii=False)
        out.write("\n")
    return rec(path)


def compact(path):
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
    return {"immutable_parent": rec(path), "declared_fingerprint_occurrences": len(rows),
            "deduplicated_paths": len({row["path"] for row in rows}),
            "canonical_deduplicated_record_summary_sha256": digest(b"\n".join(sorted({canonical(row) for row in rows}))),
            "historical_inventory_bound_not_recopied_or_recursively_reverified": True}


def authority():
    obj = load(AUTH)
    assert obj["status"] == "proved, independently reviewed scoped partial result"
    assert obj["unresolved_substantive_issues"] == 0 and not obj["repair_required"]
    check(obj["accepted_copy"])
    check(obj["candidate"])
    assert (ROOT / obj["accepted_copy"]["path"]).read_bytes().endswith((ROOT / obj["candidate"]["path"]).read_bytes())
    return {"authority": rec(AUTH), "accepted_body": obj["accepted_copy"],
            "operative_claims": ["CG1", "CG2"], "complete_accepted_body_read": True,
            "historical_occurrences_bound_not_replayed": obj["record_occurrences_verified"],
            "historical_paths_bound_not_replayed": obj["unique_paths_verified"],
            "CG3_cubic_R3_and_Frobenius_lead_not_premises": True}


def baseline():
    for path, expected in EXPECTED.items():
        row = rec(path)
        assert (row["bytes"], row["sha256"]) == expected, path
    target = load(T + "-freeze-v1.json")
    base = load(T + "-baseline-v1.json")
    oldparent = load(target["own_parent"]["path"])
    own = load(PARENT)
    rows = [rec(T + "-freeze-v1.json")] + target["artifacts"] + base["protected"]
    rows += oldparent["artifacts"] + [rec(PARENT)] + own["artifacts"]
    for row in rows:
        check(row)
    by_path = {}
    for row in rows:
        assert row["path"] not in by_path or by_path[row["path"]] == row
        by_path[row["path"]] = row
    guards = [by_path[key] for key in sorted(by_path)]
    obj = {"created_utc": now(), "metadata_only": True,
           "prefix_unused_confirmed_by_exact_rg_exit1_before_first_write": True,
           "target_main": rec(T + "-candidate-v1.md"),
           "target_constructor_freeze": rec(T + "-freeze-v1.json"),
           "protected": guards, "current_occurrences": len(rows), "unique_paths": len(guards),
           "canonical_current_summary_sha256": digest(canonical(guards)),
           "accepted_input": authority(), "own_immediate_parent": rec(PARENT),
           "compact_parents": [compact(AUTH), compact(T + "-freeze-v1.json"), compact(target["own_parent"]["path"]), compact(PARENT)],
           "no_corresponding_C_NEW_R4_review_file_finding_hash_or_metadata_access": True,
           "no_math_program_CAS_scan_author_rerun_or_old_write": True,
           "authoritative_weekly_telemetry": TELEMETRY}
    print(json.dumps({"baseline": put("baseline-v1.json", obj), "current_occurrences": len(rows), "unique_paths": len(guards)}))


def freeze():
    base = load(P + "-baseline-v1.json")
    for row in base["protected"]:
        check(row)
    accepted = authority()
    labels = re.findall(r"\| (DC-\d{2}) \|", (ROOT / (P + "-ledger-v1.md")).read_text())
    assert labels == [f"DC-{i:02d}" for i in range(1, 49)]
    assert load(P + "-sources-v1.json")["no_new_peer_review_access"] is True
    put("metadata-v1.json", {"generated_utc": now(), "metadata_only": True,
        "all48_hand_dispositions_present_once_in_order": True,
        "whole_main_ALL48_companions_source_code_and_constructor_metadata_read": True,
        "current_occurrences": base["current_occurrences"], "unique_paths": base["unique_paths"],
        "canonical_current_summary_sha256": base["canonical_current_summary_sha256"],
        "accepted_input": accepted,
        "no_corresponding_C_NEW_R4_finding_file_hash_or_metadata_access": True,
        "no_math_scan_CAS_or_author_source_freezer_rerun": True,
        "authoritative_weekly_telemetry": TELEMETRY})
    put("input-validation-v1.json", {"verified_utc": now(), "metadata_only": True,
        "all_current_protected_records_unchanged": True,
        "target_main_freeze_exact_assigned_bytes_SHA": True,
        "accepted_CG_pointer_and_candidate_suffix_exact": True,
        "entire_ALL48_hand_ledger_complete": True, "sources_JSON_parsed": True,
        "compact_parent_occurrences_and_dedup_summary_bound": True,
        "no_corresponding_NEW_peer_path_access_or_hash": True})
    artifacts = [rec(P + "-" + suffix) for suffix in SUFFIXES]
    obj = {"frozen_utc": now(), "status": "ENTIRE initially blind OTHER WHOLE R1 recommendation; not promotion",
        "reviewer": "/root/review_2021_reasoning_j15_r2", "root_sole_NEW_constructor_excluded": True,
        "target_main": base["target_main"], "target_constructor_freeze": base["target_constructor_freeze"],
        "all48_reconstructed": True, "substantive_defects_found": 0, "required_author_repairs": 0,
        "closed_scope_notes": 7,
        "entire_report_ALL48_ledger_issues_sources_log_code_ALL_metadata_frozen": True,
        "no_corresponding_C_NEW_R4_finding_file_hash_or_metadata_access_through_ENTIRE_freeze": True,
        "findings_withheld_until_BOTH_entire_initials_confirmed": True,
        "exact_scope": "R4A--E stated size hypotheses; bounded cofactor, F2/S4 descent, 4|D, threshold and Q16 k>=2 only",
        "no_general_s5plus_k2_full_annual_external_validation_or_novelty_claim": True,
        "accepted_input": accepted, "baseline": rec(P + "-baseline-v1.json"),
        "current_occurrences": base["current_occurrences"], "unique_paths": base["unique_paths"],
        "canonical_current_summary_sha256": base["canonical_current_summary_sha256"],
        "own_immediate_parent": base["own_immediate_parent"], "compact_parents": base["compact_parents"],
        "historical_inventories_not_recopied_or_recursively_reverified": True,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independently_verified_effective_settings": None,
        "authoritative_weekly_telemetry": TELEMETRY,
        "no_math_code_CAS_scan_optimizer_author_source_or_freezer_rerun": True,
        "no_Git_shared_old_cache_write_spawn_contact_charge_or_bypass": True,
        "payloads": len(artifacts), "files_including_manifest": len(artifacts) + 1,
        "artifacts": artifacts}
    put("manifest-v1.json", obj)
    verify()


def verify():
    obj = load(P + "-manifest-v1.json")
    for row in obj["artifacts"]:
        check(row)
    base = load(P + "-baseline-v1.json")
    for row in base["protected"]:
        check(row)
    authority()
    print(json.dumps({"manifest": rec(P + "-manifest-v1.json"), "initial": rec(P + "-initial-v1.md"),
        "whole_obligations": 48, "payloads": obj["payloads"], "files_including_manifest": obj["files_including_manifest"],
        "current_occurrences": base["current_occurrences"], "unique_paths": base["unique_paths"],
        "postverification": "all exact; findings withheld; no promotion"}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--baseline", action="store_true")
    group.add_argument("--freeze", action="store_true")
    group.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    baseline() if args.baseline else freeze() if args.freeze else verify()
