#!/usr/bin/env python3
"""Documentary DR7 administration only. No mathematical computation/replay."""
from pathlib import Path
import datetime
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
STEM = "problems/2025-B4/notes/reasoning-diagonal-return-r7-"
BASE = STEM + "baseline-v1.json"
VALID = STEM + "input-validation-v1.json"
META = STEM + "metadata-v1.json"
FREEZE = STEM + "freeze-v1.json"
PARENTS = [
    "problems/2019-B4/reviews/reasoning-cut-transfer-r6-review-2-manifest-v1.json",
    "problems/2025-B4/notes/reasoning-diagonal-return-r6-freeze-v1.json",
    "problems/2025-B4/reviews/reasoning-diagonal-return-r6-acceptance.json",
    "problems/2025-B4/reviews/reasoning-diagonal-return-r5-acceptance.json",
]
DIRECT = [
    "AGENTS.md",
    "problems/2025-B4/statement.md",
    "problems/2025-B4/proofs/reviewed-reasoning-diagonal-return-r6-v1.1.md",
    "problems/2025-B4/reviews/reasoning-diagonal-return-r6-acceptance.md",
    "problems/2025-B4/reviews/reasoning-diagonal-return-r6-acceptance.json",
    "problems/2025-B4/proofs/reviewed-reasoning-diagonal-return-r5-v1.1.md",
    "problems/2025-B4/reviews/reasoning-diagonal-return-r5-acceptance.md",
    "problems/2025-B4/reviews/reasoning-diagonal-return-r5-acceptance.json",
    "problems/2025-B4/notes/reasoning-diagonal-return-r6-failed-routes-v1.md",
    "problems/2025-B4/notes/reasoning-diagonal-return-r6-sources-v1.md",
    "problems/2025-B4/notes/reasoning-diagonal-return-r6-sources-v1.json",
    "problems/2025-B4/notes/coordinator-higher-trace-frontier-r6-v1.md",
]
OBSERVATIONS = [
    "problems/2025-B4/research.md",
    "problems/2025-B4/proof.md",
]
TEXT_SUFFIXES = [
    "candidate-v1.md", "obligations-v1.md", "checks-v1.md", "issues-v1.md",
    "failed-routes-v1.md", "sources-v1.md", "sources-v1.json",
    "worklog-v1.md", "code-record-v1.md", "admin-v1.py",
]
PAYLOADS = [STEM + suffix for suffix in TEXT_SUFFIXES] + [BASE, VALID, META]


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def guard(path):
    if "reasoning-center-return-r20-review-" in path:
        raise AssertionError("NEW R20 peer material is embargoed")
    if "reasoning-diagonal-return-r7-review-" in path:
        raise AssertionError("NEW DR7 peer material is forbidden")
    p = Path(path)
    if p.is_absolute() or ".." in p.parts:
        raise AssertionError("repository-relative immutable path required")
    return ROOT / p


def fp(path):
    data = guard(path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def read_json(path):
    return json.loads(guard(path).read_text())


def write_new(path, value):
    if not path.startswith(STEM):
        raise AssertionError("write outside owned prefix")
    with guard(path).open("x", encoding="utf-8") as out:
        json.dump(value, out, ensure_ascii=False, indent=2)
        out.write("\n")


def declared_rows(value):
    out = []
    if isinstance(value, dict):
        if (isinstance(value.get("path"), str)
                and isinstance(value.get("bytes"), int)
                and isinstance(value.get("sha256"), str)
                and re.fullmatch(r"[0-9a-f]{64}", value["sha256"])):
            out.append({key: value[key] for key in ("path", "bytes", "sha256")})
        for item in value.values():
            out.extend(declared_rows(item))
    elif isinstance(value, list):
        for item in value:
            out.extend(declared_rows(item))
    return out


def is_mutable_observation(path):
    return path.endswith("/research.md")


def canonical_summary(rows):
    by_path = {}
    for row in rows:
        previous = by_path.setdefault(row["path"], row)
        if previous != row:
            raise AssertionError("inconsistent declared frozen identity: " + row["path"])
    unique = [by_path[path] for path in sorted(by_path)]
    encoded = json.dumps(unique, sort_keys=True, separators=(",", ":")).encode()
    return {"occurrences": len(rows), "unique_paths": len(unique),
            "canonical_deduplicated_sha256": hashlib.sha256(encoded).hexdigest()}, unique


def verify_rows(rows):
    _, unique = canonical_summary(rows)
    for row in unique:
        if fp(row["path"]) != row:
            raise AssertionError("frozen identity mismatch: " + row["path"])


def label_check():
    expected = {"DR7-" + str(i).zfill(2) for i in range(1, 49)}
    result = {}
    for name in ("obligations-v1.md", "checks-v1.md"):
        labels = re.findall(r"^\| (DR7-[0-9]{2}) \|", guard(STEM + name).read_text(), re.M)
        if len(labels) != 48 or set(labels) != expected:
            raise AssertionError("ALL48 exact label coverage failed: " + name)
        result[name] = len(labels)
    return result


def parent_material():
    bindings = [fp(path) for path in PARENTS]
    inherited = []
    historical_mutable = []
    descriptions = []
    for binding in bindings:
        data = read_json(binding["path"])
        rows = declared_rows(data)
        fixed = [row for row in rows if not is_mutable_observation(row["path"])]
        historical_mutable.extend(row for row in rows if is_mutable_observation(row["path"]))
        inherited.extend(fixed)
        descriptions.append({
            "binding": binding,
            "direct_declared_frozen_summary": canonical_summary(fixed)[0],
            "historical_parent_occurrences_reported_not_recursively_reverified":
                data.get("record_occurrences_verified", data.get("protected_occurrences")),
            "historical_parent_paths_reported_not_recursively_reverified":
                data.get("unique_paths_verified", data.get("protected_unique_paths")),
            "recursion_limit": "Validate immediate declared records; bind their immutable metadata bytes without recopying all historical inventories",
        })
    return bindings, inherited, historical_mutable, descriptions


def current_protection():
    bindings, inherited, historical_mutable, descriptions = parent_material()
    direct = [fp(path) for path in DIRECT]
    rows = direct + bindings + inherited
    verify_rows(rows)
    return rows, direct, bindings, historical_mutable, descriptions


def verify_baseline():
    base = read_json(BASE)
    verify_rows(base["direct_current_frozen_inputs"])
    verify_rows([item["binding"] for item in base["immutable_parent_bindings"]])
    rows, _, _, historical_mutable, _ = current_protection()
    summary, _ = canonical_summary(rows)
    if summary != base["protected_current_summary"]:
        raise AssertionError("compact protected summary changed")
    if historical_mutable != base["historical_mutable_observations_not_protected_as_current"]:
        raise AssertionError("bound parent metadata was not preserved")
    return summary


def prepare():
    for path in (BASE, VALID, META, FREEZE):
        if guard(path).exists():
            raise AssertionError("prepare would overwrite existing new artifact")
    for suffix in TEXT_SUFFIXES:
        if not guard(STEM + suffix).is_file():
            raise AssertionError("missing new payload: " + suffix)
    rows, direct, bindings, historical_mutable, descriptions = current_protection()
    summary, _ = canonical_summary(rows)
    labels = label_check()
    baseline = {
        "prepared_at_utc": now(),
        "status": "candidate proof - unverified",
        "scope": "DR7 new ordinary signed cofactor construction; no old mathematical recertification",
        "direct_current_frozen_inputs": direct,
        "immutable_parent_bindings": descriptions,
        "protected_current_summary": summary,
        "parent_expansion": "Only immediate declared frozen records; no giant historical list copied",
        "historical_mutable_observations_not_protected_as_current": historical_mutable,
        "current_mutable_landscape_observations_not_frozen_inputs": [fp(path) for path in OBSERVATIONS],
        "mutable_status_policy": "Preserve old metadata bytes and its historical observations; do not assert old mutable map snapshots equal current coordinator maps",
        "NEW_R20_peer_material_accessed": False,
        "NEW_DR7_peer_material_accessed": False,
        "no_Git_shared_old_or_cache_writes": True,
    }
    write_new(BASE, baseline)
    write_new(VALID, {
        "validated_at_utc": now(), "result": "PASS",
        "protected_current_summary": summary,
        "all48_label_coverage": labels,
        "new_mathematical_computation": False,
        "parents_compactly_bound_not_historically_recopied": len(bindings),
        "mutable_landscape_excluded_from_frozen_current_guard": True,
    })
    write_new(META, {
        "status": "candidate proof - unverified",
        "claims": ["DR7A", "DR7B", "DR7C", "DR7D"],
        "constructor": "/root/review_2021_reasoning_j15_r2",
        "constructor_excluded_from_two_independent_whole_audits": True,
        "requested_model": "gpt-6.1-sol", "requested_reasoning": "max",
        "verified_effective_settings": None,
        "whole_obligations": 48,
        "new_external_theorem_or_Jacobi_premise": False,
        "operative_hypotheses": "p>=37 prime, X,Y ordinary integers, abs(X)>=2, Phi_p(X)=Y^p, p divides X(X+1)",
        "older_roles": "A authored accepted DR6 and audited RD/BR/RS and earlier2025 packets; no independent self-recertification",
        "root_NEW_proof_inference_supplied": False,
        "mathematical_program_scan_CAS_or_old_source_replay": False,
        "TWO_OTHER_ENTIRE_initially_blind_WHOLE_audits_required": True,
        "annual_upper_height_or_priority_claim": False,
        "unbounded_actual_order_p_part_remains_open": True,
        "code_scope": "Documentary hashing, JSON and exact obligation labels only",
        "protected_current_summary": summary,
        "baseline": fp(BASE), "input_validation": fp(VALID),
        "author_payload_files": 13, "ENTIRE_files_including_freeze": 14,
        "FULL_final_ALLfile_model_readback_then_SEPARATE_readonly_verify_required": True,
        "weekly_usage": {"method": "mcp__codex_app__get_usage_limits",
            "observed_at_utc": "2026-10-18 15:43:44 UTC", "total_used_percent": 48,
            "window_minutes": 10080, "resets_at": 1792874445,
            "ordinaryUsageAllowed": True, "ceiling_total_percent": 90,
            "integration_reserve": True, "automatic_future_window_spending": False},
    })
    print(json.dumps({"action": "prepare", "result": "PASS", **summary, "labels": labels}))


def freeze():
    if guard(FREEZE).exists():
        raise AssertionError("freeze already immutable")
    summary = verify_baseline()
    labels = label_check()
    rows = [fp(path) for path in PAYLOADS]
    write_new(FREEZE, {
        "frozen_at_utc": now(), "status": "candidate proof - unverified",
        "constructor": "/root/review_2021_reasoning_j15_r2",
        "claims": ["DR7A", "DR7B", "DR7C", "DR7D"],
        "whole_obligations": 48, "constructor_hand_checks": labels,
        "payload_files": len(rows), "ENTIRE_files": len(rows) + 1,
        "TWO_OTHER_ENTIRE_initially_blind_WHOLE_audits_required": True,
        "protected_current_summary": summary, "compact_baseline": fp(BASE),
        "no_math_executable_scan_CAS_or_old_source_replay": True,
        "FULL_final_ALLfile_model_readback_then_SEPARATE_readonly_verify_REQUIRED_before_handoff": True,
        "artifacts": rows,
    })
    print(json.dumps({"action": "freeze", "identity": fp(FREEZE),
                      "ENTIRE_files": len(rows) + 1, "whole_obligations": 48, **summary}))


def verify():
    summary = verify_baseline()
    manifest = read_json(FREEZE)
    verify_rows(manifest["artifacts"])
    labels = label_check()
    if manifest["protected_current_summary"] != summary:
        raise AssertionError("freeze protection summary mismatch")
    if len(manifest["artifacts"]) != 13 or manifest["ENTIRE_files"] != 14:
        raise AssertionError("ENTIRE payload count mismatch")
    print(json.dumps({"action": "SEPARATE_readonly_verify", "verified_at_utc": now(),
        "result": "PASS", "identity": fp(FREEZE), "main": fp(STEM + "candidate-v1.md"),
        "ENTIRE_files": 14, "ALL_obligations": 48, "labels": labels, **summary,
        "no_file_written": True}))


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ("prepare", "freeze", "verify"):
        raise SystemExit("usage: administrative-script prepare|freeze|verify")
    {"prepare": prepare, "freeze": freeze, "verify": verify}[sys.argv[1]]()
