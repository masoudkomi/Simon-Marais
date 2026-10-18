#!/usr/bin/env python3
"""NEW independent BT review metadata only; no mathematical evaluation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
BASE = "problems/2019-B4/reviews/reasoning-cut-transfer-r5-review-2-"
AUTHOR = "problems/2019-B4/notes/reasoning-cut-transfer-r5-freeze-v1.json"
AUTHOR_BASELINE = "problems/2019-B4/notes/reasoning-cut-transfer-r5-baseline-v1.json"
PARENT = "problems/2021-B4/notes/reasoning-center-return-r19-freeze-v1.json"
FORBIDDEN = "problems/2019-B4/reviews/reasoning-cut-transfer-r5-review-1-"
NAMES = ["reasoning-cut-transfer-r4", "reasoning-critical-return-r2",
         "reasoning-return-r7", "reasoning-cut-number-r3", "reasoning-growth-return-r1"]
PARENTS = [AUTHOR, AUTHOR_BASELINE, PARENT] + [
    "problems/2019-B4/reviews/" + name + "-acceptance.json" for name in NAMES
] + ["problems/2019-B4/reviews/reasoning-cut-transfer-r4-presentation-erratum-v1.json"]
BODIES = [
    "problems/2019-B4/proofs/reviewed-reasoning-cut-transfer-r4-v1.2.md",
    "problems/2019-B4/proofs/reviewed-reasoning-critical-return-r2-v1.1.md",
    "problems/2019-B4/proofs/reviewed-reasoning-return-r7-v1.1.md",
    "problems/2019-B4/proofs/reviewed-reasoning-cut-number-r3-v1.1.md",
    "problems/2019-B4/proofs/reviewed-reasoning-growth-return-r1-v1.1.md",
]
DIRECT = ["AGENTS.md", "problems/2019-B4/statement.md"] + BODIES + [
    "problems/2019-B4/reviews/" + name + "-acceptance.md" for name in NAMES
] + ["problems/2019-B4/reviews/reasoning-cut-transfer-r4-presentation-erratum-v1.md"] + PARENTS
STATIC = ["initial-v1.md", "ledger-v1.md", "issues-v1.md", "source-checks-v1.md",
          "sources-v1.json", "worklog-v1.md", "admin-v1.py"]
GENERATED = ["baseline-v1.json", "input-validation-v1.json", "metadata-v1.json"]
EXPECTED = [
    {"path": AUTHOR, "bytes": 8902,
     "sha256": "52f8a794c3d82d3803a6b9700496cac2dff4b81a84e3f6c935b1bb9fbe107896"},
    {"path": "problems/2019-B4/notes/reasoning-cut-transfer-r5-candidate-v1.md", "bytes": 21608,
     "sha256": "649e94c8a6f4a19a008b39af1d27b5badbf78ba1052bc6d31b181d6afa26b435"},
    {"path": PARENT, "bytes": 3893,
     "sha256": "dfe7b6b4f372b44a2806fc96ce41613bfc2fb7e8f5469fc2d10552aa83b835d3"},
]


def utc():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    assert not str(path).startswith(FORBIDDEN), "corresponding NEW peer access refused"
    p = Path(path)
    assert not p.is_absolute() and ".." not in p.parts and ".git" not in p.parts
    return (ROOT / p).read_bytes()


def fp(path):
    data = raw(path)
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def jread(path):
    return json.loads(raw(path))


def match(row):
    actual = fp(row["path"])
    assert actual == row, {"declared": row, "actual": actual}


def declared(obj):
    out = []
    if isinstance(obj, dict):
        path, size, sha = obj.get("path"), obj.get("bytes"), obj.get("sha256")
        if (isinstance(path, str) and not path.startswith(("http:", "https:"))
                and isinstance(size, int) and isinstance(sha, str)
                and re.fullmatch(r"[0-9a-f]{64}", sha)):
            out.append({"path": path, "bytes": size, "sha256": sha})
        for value in obj.values():
            out.extend(declared(value))
    elif isinstance(obj, list):
        for value in obj:
            out.extend(declared(value))
    return out


def canonical(rows):
    unique = {}
    for row in rows:
        assert row["path"] not in unique or unique[row["path"]] == row
        unique[row["path"]] = row
    ordered = [unique[path] for path in sorted(unique)]
    data = json.dumps(ordered, sort_keys=True, separators=(",", ":")).encode()
    return len(ordered), hashlib.sha256(data).hexdigest()


def snapshot():
    direct = [fp(path) for path in DIRECT]
    for row in EXPECTED:
        match(row)
    occurrences = list(direct)
    bindings = []
    for path in PARENTS:
        parent = jread(path)
        rows = declared(parent)
        for row in rows:
            match(row)
        unique, digest = canonical(rows)
        occurrences.extend(rows)
        old_summary = {key: parent[key] for key in [
            "record_occurrences_verified", "unique_paths_verified",
            "current_guard_occurrences", "current_guard_unique_paths",
            "protected_current_occurrences", "protected_current_unique_paths",
            "canonical_guard_summary_sha256", "canonical_deduplicated_sha256",
        ] if key in parent}
        bindings.append({"immutable_parent": fp(path),
                         "current_declared_occurrences_checked": len(rows),
                         "current_declared_unique_paths_checked": unique,
                         "current_declared_canonical_sha256": digest,
                         "historical_summary_bound_not_recursive_model_read_or_replay": old_summary})
    for name in NAMES:
        authority = jread("problems/2019-B4/reviews/" + name + "-acceptance.json")
        assert authority["status"].startswith("proved, independently reviewed")
        assert authority["unresolved_substantive_issues"] == 0
        assert raw(authority["accepted_copy"]["path"]).endswith(raw(authority["candidate"]["path"]))
    e = jread(PARENTS[-1])
    old = raw(e["old_accepted_copy"]["path"])
    new = raw(e["operative_accepted_copy"]["path"])
    assert old.count(b"t0=010") == 1
    assert old.replace(b"t0=010", b"t0=10", 1) == new
    assert new.endswith(raw(e["unchanged_candidate_suffix"]["path"]))
    unique, digest = canonical(occurrences)
    return direct, bindings, len(occurrences), unique, digest


def write_new(suffix, obj):
    path = ROOT / (BASE + suffix)
    with path.open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


def labels():
    text = raw(BASE + "ledger-v1.md").decode()
    found = re.findall(r"^\|BT-(\d{2})\|", text, re.MULTILINE)
    assert found == [f"{j:02d}" for j in range(1, 57)], found
    return len(found)


def prepare():
    assert labels() == 56
    for suffix in STATIC:
        fp(BASE + suffix)
    direct, bindings, count, unique, digest = snapshot()
    write_new("baseline-v1.json", {
        "created_at_utc": utc(), "role": "OTHER initially blind ENTIRE WHOLE BT review2",
        "direct_inputs": direct, "compact_immutable_parent_bindings": bindings,
        "protected_current_occurrences": count, "protected_current_unique_paths": unique,
        "canonical_deduplicated_sha256": digest,
        "recipe": "First verify each immutable bound JSON, then its exact path/bytes/sha256 occurrences recursively within objects, without recursively opening referenced older metadata. Combine with direct_inputs. Historical inventories and model-read claims are not recopied or relabelled current reading.",
        "no_NEW_corresponding_root_BT_finding_file_hash_metadata_or_thread_access": True,
        "parent_R19_is_administrative_not_BT_mathematical_premise": True,
    })
    write_new("input-validation-v1.json", {
        "checked_at_utc": utc(), "result": "PASS necessary immutable fingerprints/suffixes/current CT byte correction; NOT mathematical proof",
        "whole_obligation_identifiers": 56, "accepted_bodies": 5,
        "protected_current_occurrences": count, "protected_current_unique_paths": unique,
        "canonical_deduplicated_sha256": digest,
        "author_source_or_old_freezer_executed": False,
        "NEW_peer_access": False,
    })
    write_new("metadata-v1.json", {
        "created_at_utc": utc(), "reviewer": "/root/review_2021_reasoning_j15_r2",
        "role": "OTHER initially blind ENTIRE WHOLE BT review2",
        "whole_obligations": 56, "payload_files": 10, "ENTIRE_files": 11,
        "substantive_defects": 0, "required_repairs": 0, "closed_scope_notes": 7,
        "recommendation_only_no_promotion": True,
        "no_NEW_corresponding_root_BT_finding_file_hash_metadata_or_thread_access": True,
        "root_times_counts_only_messages_received": True,
        "identity_only_until_explicit_BOTH_ENTIRE_confirmation": True,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independently_verified_effective_settings": None,
        "NEW_code_metadata_only_no_math_scan_or_replay": True,
        "protected_current_occurrences": count, "protected_current_unique_paths": unique,
        "canonical_deduplicated_sha256": digest,
        "weekly_authorized_window_only": {"observed_at_utc": "2026-10-18 13:35:57 UTC", "TOTAL_used_percent": 38,
            "window_minutes": 10080, "reset_unix": 1792874445, "ordinary_usage_allowed": True,
            "legacy_and_by_limit_agree": True, "account_label": "029a8928...1334ac3a",
            "TOTAL_ceiling": 90, "integration_reserve": True, "no_automatic_later_window": True},
        "FULL_all_payload_model_readback_before_manifest_required": True,
        "FULL_manifest_model_readback_then_SEPARATE_readonly_verify_required": True,
    })
    print(json.dumps({"prepare": "PASS", "whole_obligations": 56,
                      "protected_occurrences": count, "unique_paths": unique,
                      "canonical_sha256": digest, "payload_count": 10}))


def check_baseline():
    baseline = jread(BASE + "baseline-v1.json")
    for row in baseline["direct_inputs"]:
        match(row)
    direct, bindings, count, unique, digest = snapshot()
    assert direct == baseline["direct_inputs"]
    assert bindings == baseline["compact_immutable_parent_bindings"]
    assert (count, unique, digest) == (baseline["protected_current_occurrences"],
            baseline["protected_current_unique_paths"], baseline["canonical_deduplicated_sha256"])
    assert labels() == 56
    return count, unique, digest


def freeze():
    count, unique, digest = check_baseline()
    payloads = [fp(BASE + suffix) for suffix in STATIC + GENERATED]
    for row in payloads:
        if row["path"].endswith(".json"):
            jread(row["path"])
    write_new("manifest-v1.json", {
        "frozen_at_utc": utc(), "role": "OTHER initially blind ENTIRE WHOLE BT review2",
        "whole_obligations": 56, "payload_files": 10, "ENTIRE_files": 11,
        "substantive_defects": 0, "required_repairs": 0, "closed_scope_notes": 7,
        "recommendation_only_no_promotion": True,
        "FULL_all_final_payload_model_readback_completed_before_manifest": True,
        "FULL_manifest_model_readback_then_SEPARATEverify_required_before_handoff": True,
        "author_ENTIRE_freeze": fp(AUTHOR), "immediate_own_parent": fp(PARENT),
        "compact_baseline": fp(BASE + "baseline-v1.json"),
        "protected_current_occurrences": count, "protected_current_unique_paths": unique,
        "canonical_deduplicated_sha256": digest,
        "no_NEW_corresponding_root_BT_finding_file_hash_metadata_or_thread_access": True,
        "identity_only_until_explicit_BOTH_ENTIRE_confirmation": True,
        "mathematical_program_CAS_scan_author_source_or_old_replay": False,
        "payloads": payloads,
    })
    print(json.dumps({"manifest": fp(BASE + "manifest-v1.json")}))


def verify():
    manifest = jread(BASE + "manifest-v1.json")
    for row in manifest["payloads"]:
        match(row)
    count, unique, digest = check_baseline()
    assert len(manifest["payloads"]) == 10 and manifest["ENTIRE_files"] == 11
    assert manifest["whole_obligations"] == 56
    assert (count, unique, digest) == (manifest["protected_current_occurrences"],
            manifest["protected_current_unique_paths"], manifest["canonical_deduplicated_sha256"])
    print(json.dumps({"SEPARATE_readonly_verify": "PASS", "verified_at_utc": utc(),
                      "whole_obligations": 56, "ENTIRE_files": 11,
                      "protected_occurrences": count, "unique_paths": unique,
                      "manifest": fp(BASE + "manifest-v1.json")}))


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) == 2 else ""
    if mode not in {"prepare", "freeze", "verify"}:
        raise SystemExit("usage: admin-v1.py prepare|freeze|verify")
    {"prepare": prepare, "freeze": freeze, "verify": verify}[mode]()
