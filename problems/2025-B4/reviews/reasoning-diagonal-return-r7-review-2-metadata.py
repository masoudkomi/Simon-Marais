#!/usr/bin/env python3
"""Fresh reviewer metadata only. Never executes mathematical/source/old code.

Only this NEW review2 prefix may be written, using exclusive-create. No
inventory, mathematical enumeration, coefficient/prime/valuation evaluation,
network, cache, subprocess or old freezer import is present. verify is read-only.
"""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2025-B4/reviews/reasoning-diagonal-return-r7-review-2-"
AUTHOR_STEM = "problems/2025-B4/notes/reasoning-diagonal-return-r7-"
AUTHOR_FREEZE = {
    "path": AUTHOR_STEM + "freeze-v1.json", "bytes": 3663,
    "sha256": "5a029bb837c9fc8232f3364262d4d9ca66370e10d60e1dd545d5c5441798c412",
}
AUTHOR_MAIN = {
    "path": AUTHOR_STEM + "candidate-v1.md", "bytes": 14119,
    "sha256": "854f1f690ce2c49d62c2011db462ce53f97b44e442fe271042662832314b0885",
}
OWN_PARENT = {
    "path": "problems/2017-B4/notes/reasoning-path-mass-return-r10-freeze-v1.json",
    "bytes": 4859,
    "sha256": "8eaf21309963d0c7d6b12aa3be03e957989d598bb13dd1fea6d4979ab33d5441",
}
ACCEPTANCES = [
    "problems/2025-B4/reviews/reasoning-diagonal-return-r6-acceptance.json",
    "problems/2025-B4/reviews/reasoning-diagonal-return-r5-acceptance.json",
]
PAYLOAD_SUFFIXES = [
    "report.md", "ledger.md", "issues.md", "sources.md", "sources.json",
    "worklog.md", "metadata.py", "baseline.json", "input-validation.json",
]


def now():
    return datetime.now(timezone.utc).isoformat()


def path(rel):
    # Deny the corresponding NEW peer before touching its bytes or metadata.
    assert "reasoning-diagonal-return-r7-review-1-" not in rel
    assert "sq15" not in rel.lower()
    p = Path(rel)
    assert not p.is_absolute() and ".." not in p.parts
    full = ROOT / p
    assert full.resolve().is_relative_to(ROOT)
    return full


def fp(rel):
    data = path(rel).read_bytes()
    return {"path": rel, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def check(row):
    expected = {k: row[k] for k in ("path", "bytes", "sha256")}
    assert fp(expected["path"]) == expected, expected["path"]
    return expected


def read_json(rel):
    return json.loads(path(rel).read_text())


def declared(value):
    result = []
    if isinstance(value, dict):
        if (isinstance(value.get("path"), str) and isinstance(value.get("bytes"), int)
                and isinstance(value.get("sha256"), str)
                and re.fullmatch("[0-9a-f]{64}", value["sha256"])):
            result.append({k: value[k] for k in ("path", "bytes", "sha256")})
        for v in value.values():
            result.extend(declared(v))
    elif isinstance(value, list):
        for v in value:
            result.extend(declared(v))
    return result


def summary(rows):
    unique = {}
    for row in rows:
        previous = unique.setdefault(row["path"], row)
        assert previous == row
    ordered = [unique[p] for p in sorted(unique)]
    encoded = json.dumps(ordered, sort_keys=True, separators=(",", ":")).encode()
    return {"occurrences": len(rows), "unique_paths": len(ordered),
            "canonical_deduplicated_sha256": hashlib.sha256(encoded).hexdigest()}


def write_new(suffix, value):
    rel = PREFIX + suffix
    assert rel.startswith(PREFIX)
    with path(rel).open("x", encoding="utf-8") as out:
        out.write(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def labels():
    expected = ["DR7-" + str(i).zfill(2) for i in range(1, 49)]
    for rel in (AUTHOR_STEM + "obligations-v1.md", AUTHOR_STEM + "checks-v1.md", PREFIX + "ledger.md"):
        actual = re.findall(r"^\| (DR7-[0-9]{2}) \|", path(rel).read_text(), re.M)
        assert actual == expected, rel
    return {"whole_obligations": 48, "separate_reviewer_hand_dispositions": 48}


def gather():
    rows = [check(AUTHOR_FREEZE), check(AUTHOR_MAIN)]
    author = read_json(AUTHOR_FREEZE["path"])
    assert len(author["artifacts"]) == 13 and author["ENTIRE_files"] == 14
    assert author["whole_obligations"] == 48
    rows.extend(check(r) for r in author["artifacts"])
    baseline = read_json(AUTHOR_STEM + "baseline-v1.json")
    direct = [check(r) for r in baseline["direct_current_frozen_inputs"]]
    rows.extend(direct)
    author_declared = list(direct)
    binding_count = 0
    for item in baseline["immutable_parent_bindings"]:
        binding = check(item["binding"])
        rows.append(binding)
        binding_count += 1
        immediate = declared(read_json(binding["path"]))
        immediate = [r for r in immediate if not r["path"].endswith("/research.md")]
        assert summary(immediate) == item["direct_declared_frozen_summary"]
        for r in immediate:
            check(r)
        author_declared.extend([binding] + immediate)
    assert summary(author_declared) == baseline["protected_current_summary"]
    assert baseline["protected_current_summary"] == author["protected_current_summary"]
    # Historical parent rows are verified above but not copied into this new
    # baseline; immutable bindings+canonical summary preserve exact reproduction.
    accepted_suffixes = []
    for authority_path in ACCEPTANCES:
        authority = read_json(authority_path)
        candidate = check(authority["candidate"])
        accepted = check(authority["accepted_copy"])
        rows.extend((candidate, accepted))
        assert path(accepted["path"]).read_bytes().endswith(path(candidate["path"]).read_bytes())
        assert authority["unresolved_substantive_issues"] == 0
        accepted_suffixes.append(accepted["path"])
    rows.append(check(OWN_PARENT))
    parent = read_json(OWN_PARENT["path"])
    assert len(parent["payloads"]) == 10
    rows.extend(check(r) for r in parent["payloads"])
    assert parent["older_plus_new_own_paths_bound_transitively"] == 865
    detail = {
        "necessary_guard_summary": summary(rows),
        "author_ENTIRE14_fingerprints_verified": True,
        "author_compact_protected_summary_reconstructed_and_verified": summary(author_declared),
        "author_direct_current_records": len(direct),
        "author_immediate_immutable_bindings": binding_count,
        "historical_mutable_map_observations_not_protected_as_current": True,
        "accepted_context_suffixes_verified": accepted_suffixes,
        "own_immediate_parent_payloads_verified": 10,
        "older_own_paths_bound_transitively": 865,
        "mathematical_assertions_evaluated_by_code": False,
    }
    return rows, detail


def prepare():
    rows, detail = gather()
    coverage = labels()
    write_new("baseline.json", {"at_utc": now(),
        "kind": "compact necessary immutable inputs and parent metadata; no giant history recopy",
        "author_freeze": AUTHOR_FREEZE, "own_parent": OWN_PARENT,
        "guard_detail": detail, "records": rows})
    write_new("input-validation.json", {"at_utc": now(), "result": "PASS",
        **coverage, "guard_detail": detail,
        "only_assigned_NEW_prefix_written": True,
        "corresponding_NEW_root_DR7_material_accessed": False,
        "mathematical_execution": False})
    print(json.dumps({"mode": "prepare", "result": "PASS", **coverage, **detail}))


def verify_inputs():
    baseline = read_json(PREFIX + "baseline.json")
    for r in baseline["records"]:
        check(r)
    rows, detail = gather()
    assert detail == baseline["guard_detail"]
    assert summary(rows) == summary(baseline["records"])
    return detail


def freeze(attested):
    assert attested, "FULL final model readback ALL9 payloads required"
    detail = verify_inputs()
    coverage = labels()
    write_new("manifest.json", {
        "frozen_at_utc": now(),
        "status": "ENTIRE initially blind OTHER WHOLE2 initial; findings EMBARGOED; not promotion",
        "reviewer": "/root/review_2022_complexity_r2",
        "A_sole_NEW_constructor_excluded": True,
        "reviewer_NEW_DR7_contribution": False,
        "older_RD_UW_RS_BR_BD_authorship_disclosed_not_self_recertification": True,
        "requested": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independent_effective_readback": None,
        **coverage,
        "author_ENTIRE_files_FULLread": 14,
        "substantive_defects_or_required_repairs_found": 0,
        "closed_notes": 8,
        "ENTIRE_review_files_including_manifest": 10,
        "immediate_own_parent": OWN_PARENT,
        "older_own_paths_bound_transitively": 865,
        "older_plus_new_own_paths_bound_transitively": 875,
        "guard_detail": detail,
        "no_corresponding_NEW_root_DR7_filename_inventory_findings_files_hashes_meta_commentary_accessed": True,
        "no_SQ15_peer_access": True,
        "FULL_final_model_readback_ALL9_payloads_code_generated_metadata_attested": True,
        "FULL_manifest_model_readback_then_SEPARATE_readonly_verify_required": True,
        "findings_EMBARGOED_until_explicit_BOTH_confirmation": True,
        "no_mathematical_program_scan_CAS_test_optimizer_author_source_old_replay": True,
        "no_Git_shared_old_cache_mutation_spawn_charge_contact_bypass": True,
        "authoritative_weekly_telemetry": {
            "at_utc": "2026-10-18 15:58:29 UTC",
            "method": "own same-awaited clock/get_usage_limits",
            "TOTAL_used_percent": 49, "window_minutes": 10080,
            "resetsAt": 1792874445, "ordinary_usage_allowed": True,
            "legacy_by_limit_agree": True, "account_label": "029a8928...1334ac3a",
            "TOTAL_ceiling_percent": 90, "integration_reserve": True,
            "human_authorized_current_window_only": True,
            "automatic_later_window_spending": False},
        "payloads": [fp(PREFIX + suffix) for suffix in PAYLOAD_SUFFIXES],
    })
    print(json.dumps({"mode": "freeze", "result": "PASS", "manifest": fp(PREFIX + "manifest.json")}))


def verify():
    manifest = read_json(PREFIX + "manifest.json")
    assert len(manifest["payloads"]) == 9
    for r in manifest["payloads"]:
        check(r)
    detail = verify_inputs()
    coverage = labels()
    print(json.dumps({"at_utc": now(), "mode": "SEPARATE read-only verify", "result": "PASS",
        **coverage, "ENTIRE_review_files": 10, "guard_detail": detail,
        "manifest": fp(PREFIX + "manifest.json"), "report": fp(PREFIX + "report.md")}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("prepare", "freeze", "verify"))
    parser.add_argument("--attest-final-model-readback", action="store_true")
    args = parser.parse_args()
    {"prepare": prepare, "freeze": lambda: freeze(args.attest_final_model_readback), "verify": verify}[args.mode]()
