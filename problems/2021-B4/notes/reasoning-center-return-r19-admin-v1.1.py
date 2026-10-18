#!/usr/bin/env python3
"""R19 v1.1 compact byte administration, no mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2021-B4/notes/reasoning-center-return-r19-"
STATIC = [
    "candidate-v1.1.md", "obligations-v1.1.md", "checks-v1.1.md",
    "failures-v1.1.md", "sources-v1.1.md", "sources-v1.1.json",
    "worklog-v1.1.md", "code-log-v1.1.md", "repair-ledger-v1.1.md",
    "diff-v1-to-v1.1.patch", "build-v1.1.py", "admin-v1.1.py",
]
GENERATED = ["baseline-v1.1.json", "input-validation-v1.1.json", "metadata-v1.1.json"]
PARENTS = [
    PREFIX + "freeze-v1.json", PREFIX + "baseline-v1.json",
    "problems/2021-B4/reviews/reasoning-center-return-r19-review-1-manifest-v1.json",
    "problems/2021-B4/reviews/reasoning-center-return-r19-review-2-manifest-v1.json",
    "problems/2021-B4/reviews/reasoning-center-return-r19-coordinator-reconciliation-v1.json",
    "problems/2025-B4/notes/reasoning-diagonal-return-r6-freeze-v1.json",
]
DIRECT = ["AGENTS.md", "problems/2021-B4/statement.md"] + PARENTS
EXPECTED = {
    PREFIX + "candidate-v1.md": (17591, "589eddbf5f305b3380ee2c499d774aff8bb1b4499aa46c15c3dbffcf1bd56462"),
    PREFIX + "freeze-v1.json": (3893, "dfe7b6b4f372b44a2806fc96ce41613bfc2fb7e8f5469fc2d10552aa83b835d3"),
    "problems/2021-B4/reviews/reasoning-center-return-r19-review-1-manifest-v1.json":
        (2677, "4dbb9d1f2c775c2198fb990bd23a40ed5400f9d054042c796fe84a4c9eb0653d"),
    "problems/2021-B4/reviews/reasoning-center-return-r19-review-2-manifest-v1.json":
        (5195, "2cdc76363c43865d1ca20347670ba0878e6c90cf0ad4b2acb2af04b26212754e"),
    "problems/2025-B4/notes/reasoning-diagonal-return-r6-freeze-v1.json":
        (3623, "a9edb267e1b417beedcfbe57dec293b9d494fe878f2758ccbdc4f5c300188b8d"),
    "problems/2021-B4/proofs/reviewed-reasoning-center-return-r18-v1.1.md":
        (26067, "f26de3a17895354408e514d6a0b0066715a1c0f0234d494fd53485ea3feb8284"),
    "problems/2021-B4/proofs/reviewed-reasoning-center-return-r17-v1.1.md":
        (23107, "8c8daa274ea6dcf95e25249e215b09646c3473c4ccd6320302a364b0af5b7797"),
    "problems/2021-B4/proofs/reviewed-reasoning-return-r8-v1.1.md":
        (19921, "33b8713d402d09f711d0096cdc4e8c00f9e622a5335f8e3345eb4f82ba0d359d"),
    "problems/2021-B4/proofs/reviewed-reasoning-return-r5-v1.1.md":
        (23675, "f4f088adc133b0581520488cdbba30082c13b2402c96ae555142e5491ad4137d"),
}


def utc():
    return datetime.now(timezone.utc).isoformat()


def fp(path):
    path = str(path)
    if "reasoning-center-return-r19-review-" in path and (
            "reaudit" in path or "v1.1" in path):
        raise ValueError("future affected peer material not accessible")
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def jread(path):
    return json.loads((ROOT / path).read_text())


def records(obj):
    found = []
    if isinstance(obj, dict):
        path, size, sha = obj.get("path"), obj.get("bytes"), obj.get("sha256")
        if (isinstance(path, str) and not path.startswith(("http:", "https:"))
                and isinstance(size, int) and isinstance(sha, str)
                and re.fullmatch(r"[0-9a-f]{64}", sha)):
            found.append({"path": path, "bytes": size, "sha256": sha})
        for value in obj.values():
            found.extend(records(value))
    elif isinstance(obj, list):
        for value in obj:
            found.extend(records(value))
    return found


def check(row):
    actual = fp(row["path"])
    if actual != row:
        raise ValueError({"declared": row, "actual": actual})


def mutable(path):
    return (bool(re.fullmatch(r"problems/\d{4}-B4/research\.md", path))
            or path == "README.md" or path.startswith(("progress/", "sources/")))


def canonical(rows):
    unique = {}
    for row in rows:
        if row["path"] in unique and unique[row["path"]] != row:
            raise ValueError("conflicting immutable declaration")
        unique[row["path"]] = row
    ordered = [unique[p] for p in sorted(unique)]
    digest = hashlib.sha256(json.dumps(ordered, sort_keys=True,
        separators=(",", ":")).encode()).hexdigest()
    return len(ordered), digest


def snapshot():
    for path, (size, sha) in EXPECTED.items():
        check({"path": path, "bytes": size, "sha256": sha})
    direct = [fp(p) for p in DIRECT]
    all_rows = list(direct)
    summaries = []
    for path in PARENTS:
        obj = jread(path)
        declared = records(obj)
        immutable = [r for r in declared if not mutable(r["path"])]
        historical = [r for r in declared if mutable(r["path"])]
        for row in immutable:
            check(row)
        unique, digest = canonical(immutable)
        all_rows.extend(immutable)
        summaries.append({"parent": fp(path),
            "declared_fingerprint_occurrences": len(declared),
            "immutable_occurrences_verified": len(immutable),
            "immutable_unique_paths_verified": unique,
            "immutable_canonical_sha256": digest,
            "historical_mutable_occurrences_NOT_current_math_inputs": len(historical),
            "historical_mutable_rows_preserved_in_immutable_parent_only": True,
            "parent_historical_counts_NOT_fresh_recursive_model_reads": {
                key: obj[key] for key in (
                    "protected_current_occurrences", "protected_current_unique_paths",
                    "necessary_guard_occurrences", "necessary_guard_unique_paths")
                if key in obj}})
    unique, digest = canonical(all_rows)
    return direct, summaries, len(all_rows), unique, digest


def labels():
    text = (ROOT / (PREFIX + "obligations-v1.1.md")).read_text()
    old_ids = re.findall(r"(?m)^\|R19-(\d{2})\|", text)
    repair_ids = re.findall(r"(?m)^\|R19-FC(\d{2})\|", text)
    if old_ids != [f"{n:02d}" for n in range(1, 65)]:
        raise ValueError("original64 exact IDs required")
    if repair_ids != [f"{n:02d}" for n in range(1, 13)]:
        raise ValueError("repair12 exact IDs required")
    return len(old_ids) + len(repair_ids)


def write_new(suffix, obj):
    with (ROOT / (PREFIX + suffix)).open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


def prepare():
    labels()
    for suffix in STATIC:
        fp(PREFIX + suffix)
    direct, parents, count, unique, digest = snapshot()
    write_new("baseline-v1.1.json", {"created_at_utc": utc(),
        "status": "candidate proof - unverified; required author correction",
        "direct_current_inputs": direct, "compact_immutable_parent_bindings": parents,
        "protected_current_occurrences": count, "protected_current_unique_paths": unique,
        "canonical_deduplicated_sha256": digest,
        "recipe": "Check direct paths and each immutable parent identity, recursively collect exact path/bytes/sha256 objects within each parent JSON without opening nested historical metadata; verify immutable records and summarize duplicate occurrences. Historical mutable status snapshots are retained only in original immutable parents, never asserted current or used as mathematical premises.",
        "all_original_author13_and_original_peer21_preserved": True,
        "fingerprints_NOT_fresh_historical_mathematical_model_reads": True,
        "no_future_affected_peer_material_access": True})
    write_new("input-validation-v1.1.json", {"checked_at_utc": utc(),
        "result": "PASS", "original64_plus_repair12_identifiers": labels(),
        "all_expected_exact_fingerprints_match": True,
        "protected_current_occurrences": count, "protected_current_unique_paths": unique,
        "canonical_deduplicated_sha256": digest,
        "original_author_and_review_payloads_unchanged": True,
        "mathematical_program_CAS_scan_replay": False})
    write_new("metadata-v1.1.json", {"created_at_utc": utc(),
        "status": "candidate proof - unverified; affected reaudits pending",
        "version": "1.1", "issue": "R19R2-01", "constructor": "/root/review_2021_reasoning_j15_r2",
        "requested_inherited": {"model": "gpt-6.1-sol", "reasoning": "max"},
        "verified_effective_settings": None,
        "original64_plus_repair12_whole_obligations": 76,
        "payload_files": 15, "ENTIRE_files_including_freeze": 16,
        "original_BOTH_WHOLE_initials_complete_and_explicitly_released_before_author_peer_read": True,
        "reviewer_B_scaling_objection_and_counterexample_attributed": True,
        "root_relay_and_original_initial_miss_disclosed": True,
        "withdrawn_unscaled_integral_Eisenstein_claim": True,
        "normalized_Eisenstein_and_original_quadratic_field_root_distances_retained": True,
        "BOTH_OTHER_affected_ENTIRE_WHOLE_reaudits_required": True,
        "frameII_III_annual_exclusion_or_global_Q_factor_claim": False,
        "mathematical_program_CAS_scan_replay": False,
        "protected_current_occurrences": count, "protected_current_unique_paths": unique,
        "canonical_deduplicated_sha256": digest,
        "weekly_authoritative_current_window": {"at_utc": "2026-10-18 14:22:59 UTC",
            "TOTAL_used_percent": 42, "window_minutes": 10080, "resetsAt": 1792874445,
            "ordinary_usage_allowed": True, "legacy_by_limit_agree": True,
            "account_label": "029a8928...1334ac3a", "ceiling_TOTAL": 90,
            "integration_reserve": True, "no_automatic_later_week": True},
        "FULL_final_ALL_payload_model_readback_before_freeze_required": True,
        "FULL_freeze_manifest_model_readback_then_SEPARATE_verify_required": True,
        "no_future_affected_peer_finding_file_hash_metadata_access": True})
    print(json.dumps({"prepare": "PASS", "whole_obligations": 76,
        "protected_occurrences": count, "unique_paths": unique, "canonical_sha256": digest}))


def validate():
    base = jread(PREFIX + "baseline-v1.1.json")
    direct, parents, count, unique, digest = snapshot()
    if (direct != base["direct_current_inputs"]
            or parents != base["compact_immutable_parent_bindings"]
            or (count, unique, digest) != (base["protected_current_occurrences"],
                base["protected_current_unique_paths"], base["canonical_deduplicated_sha256"])):
        raise ValueError("immutable input fingerprint drift")
    if labels() != 76:
        raise ValueError("obligation drift")
    return count, unique, digest


def freeze():
    count, unique, digest = validate()
    payloads = [fp(PREFIX + suffix) for suffix in STATIC + GENERATED]
    for row in payloads:
        if row["path"].endswith(".json"):
            jread(row["path"])
    write_new("freeze-v1.1.json", {"frozen_at_utc": utc(),
        "status": "candidate proof - unverified; BOTH affected whole reaudits required",
        "version": "1.1", "issue": "R19R2-01", "constructor_excluded": True,
        "whole_obligations": 76, "original_whole": 64, "repair_additional": 12,
        "payload_files": len(payloads), "ENTIRE_files": len(payloads) + 1,
        "FULL_final_ALL15_payload_model_readback_completed": True,
        "manifest_FULL_readback_and_SEPARATE_verify_required_before_handoff": True,
        "compact_baseline": fp(PREFIX + "baseline-v1.1.json"),
        "original_immutable_author_manifest": fp(PARENTS[0]),
        "original_peer_manifests": [fp(PARENTS[2]), fp(PARENTS[3])],
        "protected_current_occurrences": count, "protected_current_unique_paths": unique,
        "canonical_deduplicated_sha256": digest,
        "mathematical_program_CAS_scan_replay": False,
        "no_future_affected_peer_finding_file_hash_metadata_access": True,
        "payloads": payloads})
    print(json.dumps({"freeze": fp(PREFIX + "freeze-v1.1.json")}))


def verify():
    manifest = jread(PREFIX + "freeze-v1.1.json")
    for row in manifest["payloads"]:
        check(row)
    count, unique, digest = validate()
    if (manifest["whole_obligations"], manifest["payload_files"], manifest["ENTIRE_files"]) != (76, 15, 16):
        raise ValueError("packet count mismatch")
    if (count, unique, digest) != (manifest["protected_current_occurrences"],
            manifest["protected_current_unique_paths"], manifest["canonical_deduplicated_sha256"]):
        raise ValueError("manifest guard mismatch")
    print(json.dumps({"SEPARATE_readonly_verify": "PASS", "verified_at_utc": utc(),
        "ALL_obligations": 76, "ENTIRE_files": 16,
        "protected_occurrences": count, "unique_paths": unique,
        "main": fp(PREFIX + "candidate-v1.1.md"),
        "freeze": fp(PREFIX + "freeze-v1.1.json")}))


if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) == 2 else ""
    if action not in {"prepare", "freeze", "verify"}:
        raise SystemExit("usage: admin-v1.1.py prepare|freeze|verify")
    {"prepare": prepare, "freeze": freeze, "verify": verify}[action]()
