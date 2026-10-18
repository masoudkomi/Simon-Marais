#!/usr/bin/env python3
"""R19 byte administration only; no mathematical proof computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2021-B4/notes/reasoning-center-return-r19-"
STATIC = [
    "candidate-v1.md", "obligations-v1.md", "checks-v1.md", "failures-v1.md",
    "sources-v1.md", "sources-v1.json", "worklog-v1.md", "code-log-v1.md",
    "admin-v1.py",
]
GENERATED = ["baseline-v1.json", "input-validation-v1.json", "metadata-v1.json"]
PARENTS = [
    "problems/2021-B4/reviews/reasoning-center-return-r18-acceptance.json",
    "problems/2021-B4/notes/reasoning-center-return-r18-freeze-v1.json",
    "problems/2021-B4/notes/reasoning-center-return-r18-baseline-v1.json",
    "problems/2021-B4/reviews/reasoning-center-return-r17-acceptance.json",
    "problems/2021-B4/reviews/reasoning-return-r8-acceptance.json",
    "problems/2021-B4/reviews/reasoning-return-r5-acceptance.json",
    "problems/2025-B4/reviews/reasoning-diagonal-return-r5-review-2-manifest-v1.json",
    "problems/2025-B4/reviews/reasoning-diagonal-return-r5-review-2-baseline-v1.json",
]
DIRECT = [
    "AGENTS.md", "problems/2021-B4/statement.md",
    "problems/2021-B4/proofs/reviewed-reasoning-center-return-r18-v1.1.md",
    "problems/2021-B4/reviews/reasoning-center-return-r18-acceptance.md",
    "problems/2021-B4/proofs/reviewed-reasoning-center-return-r17-v1.1.md",
    "problems/2021-B4/reviews/reasoning-center-return-r17-acceptance.md",
    "problems/2021-B4/proofs/reviewed-reasoning-return-r8-v1.1.md",
    "problems/2021-B4/reviews/reasoning-return-r8-acceptance.md",
    "problems/2021-B4/proofs/reviewed-reasoning-return-r5-v1.1.md",
    "problems/2021-B4/reviews/reasoning-return-r5-acceptance.md",
    "problems/2021-B4/notes/reasoning-center-return-r18-failures-v1.md",
    "problems/2021-B4/notes/reasoning-center-return-r18-sources-v1.md",
    "problems/2021-B4/notes/reasoning-center-return-r17-failures-v1.md",
    "problems/2021-B4/notes/reasoning-return-r8-failed-routes-v1.md",
] + PARENTS
EXPECTED = {
    "problems/2021-B4/proofs/reviewed-reasoning-center-return-r18-v1.1.md":
        (26067, "f26de3a17895354408e514d6a0b0066715a1c0f0234d494fd53485ea3feb8284"),
    "problems/2021-B4/proofs/reviewed-reasoning-center-return-r17-v1.1.md":
        (23107, "8c8daa274ea6dcf95e25249e215b09646c3473c4ccd6320302a364b0af5b7797"),
    "problems/2021-B4/proofs/reviewed-reasoning-return-r8-v1.1.md":
        (19921, "33b8713d402d09f711d0096cdc4e8c00f9e622a5335f8e3345eb4f82ba0d359d"),
    "problems/2021-B4/proofs/reviewed-reasoning-return-r5-v1.1.md":
        (23675, "f4f088adc133b0581520488cdbba30082c13b2402c96ae555142e5491ad4137d"),
    "problems/2025-B4/reviews/reasoning-diagonal-return-r5-review-2-manifest-v1.json":
        (3715, "744aae75d784d13433292a1656d8ce4935e70549f42b2f412a73766ab5f83e97"),
}
FORBIDDEN = [
    "problems/2019-B4/reviews/reasoning-cut-transfer-r5-review-1-",
    "problems/2019-B4/notes/reasoning-cut-transfer-r5-",
]


def utc():
    return datetime.now(timezone.utc).isoformat()


def fp(path):
    if any(str(path).startswith(q) for q in FORBIDDEN):
        raise ValueError("future BT packet access refused")
    p = ROOT / path
    raw = p.read_bytes()
    return {"path": str(path), "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest()}


def jread(path):
    return json.loads((ROOT / path).read_text())


def records(obj):
    """Declared exact local fingerprint occurrences; no file recursion."""
    out = []
    if isinstance(obj, dict):
        path, sha = obj.get("path"), obj.get("sha256")
        size = obj.get("bytes")
        if (isinstance(path, str) and not path.startswith(("https:", "http:"))
                and isinstance(sha, str) and re.fullmatch(r"[0-9a-f]{64}", sha)
                and isinstance(size, int)):
            out.append({"path": path, "bytes": size, "sha256": sha})
        for value in obj.values():
            out.extend(records(value))
    elif isinstance(obj, list):
        for value in obj:
            out.extend(records(value))
    return out


def checked(row):
    actual = fp(row["path"])
    if actual != row:
        raise ValueError({"declared": row, "actual": actual})
    return actual


def historical_mutable(path):
    """Coordinator status snapshots are not current mathematical premises."""
    return (bool(re.fullmatch(r"problems/\d{4}-B4/research\.md", path))
            or path == "README.md" or path.startswith(("progress/", "sources/")))


def canonical(rows):
    unique = {}
    for row in rows:
        if row["path"] in unique and unique[row["path"]] != row:
            raise ValueError("incompatible declared fingerprints: " + row["path"])
        unique[row["path"]] = row
    ordered = [unique[p] for p in sorted(unique)]
    raw = json.dumps(ordered, sort_keys=True, separators=(",", ":")).encode()
    return ordered, hashlib.sha256(raw).hexdigest()


def snapshot():
    direct = [fp(p) for p in DIRECT]
    for path, (size, sha) in EXPECTED.items():
        checked({"path": path, "bytes": size, "sha256": sha})
    occurrences = list(direct)
    parents = []
    observations = []
    for path in PARENTS:
        obj = jread(path)
        declared = records(obj)
        immutable = []
        mutable = []
        for row in declared:
            if historical_mutable(row["path"]):
                actual = fp(row["path"])
                mutable.append(row)
                observations.append({"parent": path, "declared": row,
                                     "observed_current": actual,
                                     "matches_historical_snapshot": actual == row,
                                     "not_a_current_proof_premise": True})
            else:
                checked(row)
                immutable.append(row)
        unique, digest = canonical(immutable)
        occurrences.extend(immutable)
        summary = {key: obj[key] for key in (
            "record_occurrences_verified", "unique_paths_verified",
            "protected_current_occurrences", "protected_current_unique_paths",
            "canonical_deduplicated_sha256") if key in obj}
        parents.append({
            "immutable_parent": fp(path),
            "parent_declared_occurrences": len(declared),
            "current_immutable_declared_occurrences_checked": len(immutable),
            "current_immutable_declared_unique_paths_checked": len(unique),
            "current_immutable_declared_canonical_sha256": digest,
            "historical_coordinator_mutable_declarations": mutable,
            "parent_historical_summary_not_fresh_recursive_model_read": summary,
        })
    unique, digest = canonical(occurrences)
    return direct, parents, len(occurrences), len(unique), digest, observations


def write_new(suffix, obj):
    path = ROOT / (PREFIX + suffix)
    with path.open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


def labels():
    text = (ROOT / (PREFIX + "obligations-v1.md")).read_text()
    ids = re.findall(r"(?m)^\|R19-(\d{2})\|", text)
    if ids != [f"{j:02d}" for j in range(1, 65)]:
        raise ValueError("exact64 obligation identifiers required")
    return len(ids)


def prepare():
    labels()
    for suffix in STATIC:
        fp(PREFIX + suffix)
    direct, parents, count, unique, digest, observations = snapshot()
    baseline = {
        "created_at_utc": utc(), "status": "candidate proof - unverified",
        "role": "NEW R19 constructor, excluded from its independent reviews",
        "direct_current_inputs": direct, "compact_parent_bindings": parents,
        "historical_mutable_observations_at_prepare": observations,
        "protected_current_occurrences": count,
        "protected_current_unique_paths": unique,
        "canonical_deduplicated_sha256": digest,
        "recipe": "Verify each immutable parent first, then its immutable path/bytes/sha256 records recursively within JSON objects, without recursively opening referenced historical metadata; combine with direct_current_inputs. Root-owned research/README/progress/source status snapshots are observed and retained separately, not asserted unchanged or used as current premises. Parent historical inventories stay in their immutable files.",
        "no_NEW_R19_peer_or_future_BT_author_peer_access": True,
        "fingerprint_validation_is_not_mathematical_model_reading": True,
    }
    write_new("baseline-v1.json", baseline)
    write_new("input-validation-v1.json", {
        "checked_at_utc": utc(), "result": "PASS",
        "declared_expected_fingerprints_match": True,
        "historical_mutable_observations": len(observations),
        "historical_mutable_mismatches_not_proof_inputs": sum(not x["matches_historical_snapshot"] for x in observations),
        "protected_current_occurrences": count,
        "protected_current_unique_paths": unique,
        "canonical_deduplicated_sha256": digest,
        "whole_obligation_identifiers": labels(),
        "all_inputs_read_only": True, "all_NEW_writes_assigned_prefix_only": True,
        "mathematical_program_CAS_scan_or_replay": False,
    })
    write_new("metadata-v1.json", {
        "created_at_utc": utc(), "status": "candidate proof - unverified",
        "constructor": "/root/review_2021_reasoning_j15_r2",
        "claims": ["R19A", "R19B", "R19C"], "whole_obligations": 64,
        "payload_files": 12, "ENTIRE_files_including_freeze": 13,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independently_verified_effective_settings": None,
        "root_supplied_new_proof_inference": False,
        "requires_TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits": True,
        "published_general_common_value_prohibition_attributed": True,
        "new_frame_I_entire_exclusion_proposed": True,
        "frame_II_III_or_degree20_annual_exclusion_claimed": False,
        "NEW_code_metadata_only": True,
        "protected_current_occurrences": count,
        "protected_current_unique_paths": unique,
        "canonical_deduplicated_sha256": digest,
        "weekly_authorized_window_only": {
            "observed_at_utc": "2026-10-18 13:19:40 UTC",
            "usedPercent_TOTAL": 37, "windowDurationMins": 10080,
            "resetsAt": 1792874445, "ordinaryUsageAllowed": True,
            "legacy_and_by_limit_agree": True,
            "account_id": "029a8928-15a9-456a-84f9-d2e61334ac3a",
            "ceiling_TOTAL": 90, "integration_reserve": True,
            "no_automatic_later_window": True,
        },
        "FULL_all_payload_model_readback_before_freeze_required": True,
        "FULL_freeze_model_readback_then_SEPARATE_readonly_verify_required": True,
        "no_future_BT_author_peer_packet_access": True,
    })
    print(json.dumps({"prepare": "PASS", "protected_occurrences": count,
                      "unique_paths": unique, "canonical_sha256": digest,
                      "NEW_payload_count": 12, "whole_obligations": 64}))


def validate_baseline():
    baseline = jread(PREFIX + "baseline-v1.json")
    for row in baseline["direct_current_inputs"]:
        checked(row)
    direct, parents, count, unique, digest, _observations = snapshot()
    if direct != baseline["direct_current_inputs"] or parents != baseline["compact_parent_bindings"]:
        raise ValueError("protected input or parent metadata changed")
    if (count, unique, digest) != (
            baseline["protected_current_occurrences"],
            baseline["protected_current_unique_paths"],
            baseline["canonical_deduplicated_sha256"]):
        raise ValueError("protected summary changed")
    return count, unique, digest


def freeze():
    count, unique, digest = validate_baseline()
    labels()
    payloads = [fp(PREFIX + suffix) for suffix in STATIC + GENERATED]
    for row in payloads:
        if row["path"].endswith(".json"):
            jread(row["path"])
    write_new("freeze-v1.json", {
        "frozen_at_utc": utc(), "status": "candidate proof - unverified",
        "constructor": "/root/review_2021_reasoning_j15_r2",
        "root_supplied_new_proof_inference": False,
        "requires_TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits": True,
        "whole_obligations": 64, "payload_files": len(payloads),
        "ENTIRE_files": len(payloads) + 1,
        "FULL_final_payload_model_readback_completed_before_freeze": True,
        "manifest_FULLreadback_and_SEPARATEverify_required_before_handoff": True,
        "compact_baseline": fp(PREFIX + "baseline-v1.json"),
        "immediate_own_parent": fp(PARENTS[6]),
        "accepted_R18_authority": fp(PARENTS[0]),
        "protected_current_occurrences": count,
        "protected_current_unique_paths": unique,
        "canonical_deduplicated_sha256": digest,
        "mathematical_program_CAS_scan_author_source_or_old_replay": False,
        "no_NEW_R19_peer_or_future_BT_author_peer_access": True,
        "payloads": payloads,
    })
    print(json.dumps({"freeze": fp(PREFIX + "freeze-v1.json")}))


def verify():
    manifest = jread(PREFIX + "freeze-v1.json")
    for row in manifest["payloads"]:
        checked(row)
    count, unique, digest = validate_baseline()
    if labels() != manifest["whole_obligations"]:
        raise ValueError("obligation count changed")
    if (count, unique, digest) != (
            manifest["protected_current_occurrences"],
            manifest["protected_current_unique_paths"],
            manifest["canonical_deduplicated_sha256"]):
        raise ValueError("manifest protection summary changed")
    print(json.dumps({"SEPARATE_readonly_verify": "PASS", "verified_at_utc": utc(),
                      "whole_obligations": 64, "payloads": len(manifest["payloads"]),
                      "ENTIRE_files": manifest["ENTIRE_files"],
                      "protected_occurrences": count, "unique_paths": unique,
                      "freeze": fp(PREFIX + "freeze-v1.json")}))


if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) == 2 else ""
    if action not in {"prepare", "freeze", "verify"}:
        raise SystemExit("usage: admin-v1.py prepare|freeze|verify")
    {"prepare": prepare, "freeze": freeze, "verify": verify}[action]()
