#!/usr/bin/env python3
"""R23 documentary preparation/seal/SEPARATE read-only verification.

No mathematical coefficients, polynomials, roots, valuations, searches,
CAS, tests or old/source/author programs are computed or executed.
All writes use exclusive creation in this NEW assigned prefix only.
"""
import datetime
import hashlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
PREFIX = "problems/2021-B4/notes/reasoning-negative-return-r23-"
BASE = PREFIX + "baseline-v1.json"
META = PREFIX + "metadata-v1.json"
FREEZE = PREFIX + "freeze-v1.json"
PAYLOADS = [
    PREFIX + "candidate-v1.md",
    PREFIX + "obligations-v1.md",
    PREFIX + "working-v1.md",
    PREFIX + "sources-v1.md",
    PREFIX + "sources-v1.json",
    PREFIX + "admin-v1.py",
    BASE,
    META,
]
PARENT = {
    "path": "problems/2025-B4/reviews/reasoning-compatible-return-r10-review-1-manifest-v1.json",
    "bytes": 2313,
    "sha256": "4e08aa7091de774ba78fb37ae7f6a13edd5142c60cf3f4eb716cc202cd3e6335",
}
MUTABLE_MAP = "problems/2025-B4/research.md"
DIRECT = ["AGENTS.md", "problems/2021-B4/statement.md"]
for _index in (18, 21, 22):
    DIRECT += [
        f"problems/2021-B4/proofs/reviewed-reasoning-center-return-r{_index}-v1.1.md",
        f"problems/2021-B4/reviews/reasoning-center-return-r{_index}-acceptance.md",
        f"problems/2021-B4/reviews/reasoning-center-return-r{_index}-acceptance.json",
    ]
DIRECT += [
    "problems/2021-B4/notes/reasoning-center-return-r21-failures-v1.md",
    "problems/2021-B4/notes/reasoning-center-return-r22-working-v1.md",
    "problems/2021-B4/notes/reasoning-center-return-r22-sources-v1.md",
]


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def read_json(path):
    return json.loads((ROOT / path).read_text())


def record(path):
    if not isinstance(path, str) or path.startswith("/") or ".." in pathlib.PurePosixPath(path).parts:
        raise ValueError("Expected exact repository-relative path")
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def verify_record(item):
    actual = record(item["path"])
    wanted = {key: item[key] for key in ("path", "bytes", "sha256")}
    if actual != wanted:
        raise RuntimeError("Immutable fingerprint changed: " + item["path"])
    return actual


def embedded_records(value):
    """Parse declared fingerprints only, never inventory directories."""
    if isinstance(value, dict):
        if all(key in value for key in ("path", "bytes", "sha256")):
            yield {key: value[key] for key in ("path", "bytes", "sha256")}
        for child in value.values():
            yield from embedded_records(child)
    elif isinstance(value, list):
        for child in value:
            yield from embedded_records(child)


def summary(items):
    distinct = {}
    for item in items:
        path = item["path"]
        if path in distinct and distinct[path] != item:
            raise RuntimeError("Conflicting immutable declarations: " + path)
        distinct[path] = item
    canonical = [distinct[key] for key in sorted(distinct)]
    raw = json.dumps(canonical, sort_keys=True, separators=(",", ":")).encode()
    return {
        "occurrences": len(items),
        "unique_paths": len(canonical),
        "canonical_deduplicated_sha256": hashlib.sha256(raw).hexdigest(),
    }


def create_json(path, data):
    if not path.startswith(PREFIX):
        raise RuntimeError("Write outside assigned NEW prefix")
    with (ROOT / path).open("x") as stream:
        json.dump(data, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


def current_guards():
    parent_record = verify_record(PARENT)
    parent = read_json(PARENT["path"])
    parent_payloads = [verify_record(item) for item in parent["payloads"]]
    parent_baseline = read_json(
        "problems/2025-B4/reviews/reasoning-compatible-return-r10-review-1-baseline-v1.json"
    )
    parent_immutable = []
    mutable_observations = []
    for item in parent_baseline["direct_records"]:
        if item["path"] == MUTABLE_MAP:
            current = record(MUTABLE_MAP)
            mutable_observations.append({
                "historical_parent_record": item,
                "current_observation": current,
                "observed_UTC": now(),
                "historical_is_frozen_observation_not_current_identity": True,
                "current_map_is_not_a_R23_premise": True,
                "changed_since_parent_snapshot": current != item,
            })
        else:
            parent_immutable.append(verify_record(item))
    direct = [record(path) for path in DIRECT]
    authority_declared = []
    for index in (18, 21, 22):
        authority = read_json(
            f"problems/2021-B4/reviews/reasoning-center-return-r{index}-acceptance.json"
        )
        for item in embedded_records(authority):
            if item["path"] == MUTABLE_MAP:
                raise RuntimeError("Unexpected mutable map in operative authority")
            authority_declared.append(verify_record(item))
    effective = [parent_record] + parent_payloads + parent_immutable + direct + authority_declared
    return {
        "direct_records": direct,
        "current_direct_summary": summary(direct),
        "compact_parent_binding": {
            "immediate_own_parent": parent_record,
            "parent_all_payloads_verified": len(parent_payloads),
            "parent_direct_immutable_guard_occurrences_verified": len(parent_immutable),
            "parent_historical_effective_summary_bound_NOT_reverified_recursively": parent["effective_fresh_guard_summary"],
            "historical_mutable_and_current_observations_separate": mutable_observations,
        },
        "current_authority_declared_summary": summary(authority_declared),
        "effective_current_immutable_summary": summary(effective),
        "effective_records_internal_only": effective,
    }


def literal_obligations():
    text = (ROOT / (PREFIX + "obligations-v1.md")).read_text()
    labels = re.findall(r"^\|R23-O(\d\d)\|", text, re.M)
    if labels != [f"{index:02}" for index in range(1, 49)]:
        raise RuntimeError("Expected exactly48 distinct ordered literal obligation labels")
    return len(labels)


def prepare():
    if (ROOT / BASE).exists() or (ROOT / META).exists() or (ROOT / FREEZE).exists():
        raise RuntimeError("Already prepared/frozen: preserve old bytes")
    guards = current_guards()
    guards.pop("effective_records_internal_only")
    create_json(BASE, {
        "created_UTC": now(),
        "scope": "Necessary current operative guards and compact immutable parent binding",
        **guards,
        "old_mathematical_read_scope_not_inferred_from_hashing": True,
        "NEW_queued_2024_R13_target_or_peer_material_access": False,
        "root_NEW_R23_constructive_inference": False,
        "new_mathematical_program_CAS_scan_test_source_author_old_replay": False,
        "Git_shared_old_cache_writes": False,
    })
    create_json(META, {
        "prepared_UTC": now(),
        "status": "candidate proof - unverified",
        "constructor": "/root/review_2021_reasoning_j15_r2",
        "claims": ["R23A", "R23B", "R23C", "R23D"],
        "whole_obligations": literal_obligations(),
        "two_OTHER_initially_blind_ENTIRE_WHOLE_audits_required": True,
        "constructor_excluded": True,
        "root_NEW_constructive_inference": False,
        "requested": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independent_effective_setting_readback": None,
        "weekly": {
            "usedPercent": 68,
            "observed_UTC": "2026-10-18 22:59:16 UTC",
            "windowDurationMins": 10080,
            "resetsAt": 1792874445,
            "ordinaryUsageAllowed": True,
            "TOTAL_ceiling": 90,
            "integration_reserve": True,
            "automatic_later_window": False,
        },
        "mathematical_program_CAS_scan_test_optimizer_source_author_old_replay": False,
        "metadata_code_only": True,
        "NEW_queued_2024_R13_target_opened_or_constructed": False,
        "negative_d1_and_both_nonzero_actual_D5_forks_proposed_excluded": True,
        "deeper_d_ge2_A5_zero_frameIII_or_annual_solved": False,
        "FULL_final_payload_model_readback_then_seal_manifest_readback_and_SEPARATE_verify_required": True,
    })
    print(json.dumps({"prepare": "PASS", "baseline": record(BASE), "metadata": record(META), "guards": guards["effective_current_immutable_summary"]}, indent=2))


def check_baseline():
    baseline = read_json(BASE)
    for item in baseline["direct_records"]:
        verify_record(item)
    current = current_guards()
    if current["effective_current_immutable_summary"] != baseline["effective_current_immutable_summary"]:
        raise RuntimeError("Necessary immutable guard summary changed")
    return baseline, current


def seal():
    if (ROOT / FREEZE).exists():
        raise RuntimeError("Already frozen: preserve every byte")
    baseline, current = check_baseline()
    count = literal_obligations()
    if "Candidate proof - unverified" not in (ROOT / PAYLOADS[0]).read_text():
        raise RuntimeError("Missing unverified status")
    payloads = [record(path) for path in PAYLOADS]
    create_json(FREEZE, {
        "frozen_UTC": now(),
        "status": "candidate proof - unverified",
        "constructor": "/root/review_2021_reasoning_j15_r2",
        "claims": ["R23A", "R23B", "R23C", "R23D"],
        "whole_obligations": count,
        "payload_count": len(payloads),
        "ENTIRE_files": len(payloads) + 1,
        "payloads": payloads,
        "effective_current_immutable_guard_summary": baseline["effective_current_immutable_summary"],
        "current_direct_summary": baseline["current_direct_summary"],
        "compact_parent_historical_summary_bound_NOT_recopied": baseline["compact_parent_binding"]["parent_historical_effective_summary_bound_NOT_reverified_recursively"],
        "FULL_final_ALL8_payload_model_readback_completed_before_seal": True,
        "FULL_final_manifest_model_readback_then_SEPARATE_readonly_verify_REQUIRED": True,
        "two_OTHER_initially_blind_ENTIRE_WHOLE_audits_required": True,
        "constructor_excluded": True,
        "root_NEW_R23_constructive_inference": False,
        "NEW_queued_2024_R13_target_or_peer_material_access": False,
        "requested": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independent_effective_setting_readback": None,
        "mathematical_program_CAS_scan_test_source_author_old_replay": False,
        "remaining_deeper_actual_frameIII_or_annual_solved": False,
    })
    print(json.dumps({"seal": "PASS", "manifest": record(FREEZE)}, indent=2))


def verify():
    manifest = read_json(FREEZE)
    for item in manifest["payloads"]:
        verify_record(item)
    baseline, current = check_baseline()
    if literal_obligations() != manifest["whole_obligations"]:
        raise RuntimeError("Obligation labels changed")
    protected = current["effective_records_internal_only"] + manifest["payloads"] + [record(FREEZE)]
    print(json.dumps({
        "SEPARATE_readonly_verify": "PASS",
        "verified_UTC": now(),
        "manifest": record(FREEZE),
        "ENTIRE_files": manifest["ENTIRE_files"],
        "whole_obligations": manifest["whole_obligations"],
        "protected_summary": summary(protected),
        "current_mutable_map_observation_is_NOT_immutable_guard": current["compact_parent_binding"]["historical_mutable_and_current_observations_separate"],
        "writes_performed": False,
        "mathematical_program_or_old_replay": False,
    }, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ("prepare", "seal", "verify"):
        raise SystemExit("Usage: NEW-own-admin prepare|seal|verify")
    {"prepare": prepare, "seal": seal, "verify": verify}[sys.argv[1]]()
