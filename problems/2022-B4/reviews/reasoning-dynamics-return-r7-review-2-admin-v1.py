#!/usr/bin/env python3
"""D7 whole-review byte/JSON/label administration only; no mathematical tests."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
PRE = "problems/2022-B4/reviews/reasoning-dynamics-return-r7-review-2-"
AUTHOR = "problems/2022-B4/notes/reasoning-dynamics-return-r7-"
FORBIDDEN = "problems/2022-B4/reviews/reasoning-dynamics-return-r7-review-1-"
STATIC = ["report-v1.md", "ledger-v1.md", "issues-v1.md", "sources-v1.md",
          "sources-v1.json", "worklog-v1.md", "admin-v1.py"]
GENERATED = ["baseline-v1.json", "input-validation-v1.json", "metadata-v1.json"]
PARENTS = [AUTHOR + "freeze-v1.json", AUTHOR + "baseline-v1.json",
    "problems/2021-B4/notes/reasoning-center-return-r19-freeze-v1.1.json",
    "problems/2022-B4/reviews/reasoning-dynamics-return-r6-acceptance.json",
    "problems/2022-B4/reviews/reasoning-fiber-return-r5-acceptance.json",
    "problems/2022-B4/reviews/reasoning-complexity-return-r9-v3-acceptance.json"]
DIRECT = ["AGENTS.md", "problems/2022-B4/statement.md"] + PARENTS
EXPECTED = {
    AUTHOR + "candidate-v1.md": (16504, "25ab177d6efebf1c4d5bb6e3c6bb97c4bfebed750ba782f022a4b3c94bb2d508"),
    AUTHOR + "freeze-v1.json": (3391, "305eb7fbd3a9c6282c34310e72c8ffd862c4ac5315996cf2cced945d503994b2"),
    "problems/2021-B4/notes/reasoning-center-return-r19-freeze-v1.1.json":
        (4753, "1b86a88b22a1cf755836900d314e26b7ac109f83e3031b03254a78a3d36f49fd"),
    "problems/2022-B4/proofs/reviewed-reasoning-dynamics-return-r6-v1.1.md":
        (25006, "a9f9e12a3c814a4c1098778acaec1bfd13eb631be0837b5550d767715d19b0c8"),
    "problems/2022-B4/proofs/reviewed-reasoning-fiber-return-r5-v1.1.md":
        (27422, "ab4158f60b3412ace615be689cd61d9384f753319c312e776831392f97a37ef8"),
    "problems/2022-B4/proofs/reviewed-reasoning-complexity-return-r9-v3.1.md":
        (49080, "18e681d69b29d3495fea0cc2a29dbcb8a9c34db60644b981b3f653d666bef4ad")}


def utc():
    return datetime.now(timezone.utc).isoformat()


def safe(path):
    path = str(path)
    if path.startswith(FORBIDDEN):
        raise ValueError("corresponding NEW root D7 material forbidden")
    if path.startswith("/") or ".." in Path(path).parts:
        raise ValueError("repository-relative path required")
    return path


def fp(path):
    path = safe(path)
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def obj(path):
    return json.loads((ROOT / safe(path)).read_text())


def records(value):
    rows = []
    if isinstance(value, dict):
        p, size, sha = value.get("path"), value.get("bytes"), value.get("sha256")
        if (isinstance(p, str) and not p.startswith(("http:", "https:"))
                and isinstance(size, int) and isinstance(sha, str)
                and re.fullmatch(r"[0-9a-f]{64}", sha)):
            rows.append({"path": p, "bytes": size, "sha256": sha})
        for item in value.values():
            rows.extend(records(item))
    elif isinstance(value, list):
        for item in value:
            rows.extend(records(item))
    return rows


def check(row):
    if fp(row["path"]) != row:
        raise ValueError("declared fingerprint differs: " + row["path"])


def historical_mutable(path):
    return (path == "README.md" or path.startswith(("progress/", "sources/"))
            or bool(re.fullmatch(r"problems/\d{4}-B4/research\.md", path)))


def canonical(rows):
    found = {}
    for row in rows:
        if row["path"] in found and found[row["path"]] != row:
            raise ValueError("inconsistent immutable declared fingerprints")
        found[row["path"]] = row
    values = [found[p] for p in sorted(found)]
    digest = hashlib.sha256(json.dumps(values, sort_keys=True,
        separators=(",", ":")).encode()).hexdigest()
    return len(values), digest


def snapshot():
    for path, (size, sha) in EXPECTED.items():
        check({"path": path, "bytes": size, "sha256": sha})
    direct = [fp(p) for p in DIRECT]
    all_rows = list(direct)
    parents = []
    for path in PARENTS:
        meta = obj(path)
        declared = records(meta)
        rows = [r for r in declared if not historical_mutable(r["path"])]
        for row in rows:
            check(row)
        unique, digest = canonical(rows)
        all_rows.extend(rows)
        parents.append({"immutable_parent": fp(path),
            "declared_occurrences": len(declared), "immutable_occurrences_checked": len(rows),
            "immutable_unique_paths_checked": unique, "immutable_canonical_sha256": digest,
            "historical_mutable_rows_not_current_proof_inputs": len(declared) - len(rows),
            "historical_counts_not_fresh_recursive_model_reads": {
                key: meta[key] for key in ("protected_current_occurrences", "protected_current_unique_paths",
                    "fingerprint_occurrences", "unique_paths", "record_occurrences_verified", "unique_paths_verified")
                if key in meta}})
    unique, digest = canonical(all_rows)
    return direct, parents, len(all_rows), unique, digest


def labels():
    ledger = (ROOT / (PRE + "ledger-v1.md")).read_text()
    ids = re.findall(r"(?m)^\|D7-(\d{2})\|PASS", ledger)
    if ids != [f"{n:02d}" for n in range(1, 49)]:
        raise ValueError("ALL48 independent dispositions required")
    author = (ROOT / (AUTHOR + "obligations-v1.md")).read_text()
    if re.findall(r"(?m)^\| D7-(\d{2}) \|", author) != ids:
        raise ValueError("author obligation labels differ")
    notes = (ROOT / (PRE + "issues-v1.md")).read_text()
    if re.findall(r"(?m)^\|D7R2-N(\d)\|CLOSED\|", notes) != list("12345678"):
        raise ValueError("eight scope notes required")
    return len(ids)


def put(suffix, value):
    with (ROOT / (PRE + suffix)).open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def prepare():
    labels()
    for suffix in STATIC:
        fp(PRE + suffix)
    direct, parents, count, unique, digest = snapshot()
    put("baseline-v1.json", {"created_at_utc": utc(),
        "direct_current_inputs": direct, "compact_immutable_parent_bindings": parents,
        "protected_occurrences": count, "protected_unique_paths": unique,
        "canonical_deduplicated_sha256": digest,
        "recipe": "Verify direct inputs/each immutable parent and every exact local fingerprint within that parent JSON; retain only compact per-parent counts/digest, without opening nested old metadata recursively or copying historical inventories. Exclude root-owned historical mutable status observations from immutable mathematical inputs.",
        "all_frozen_author_and_own_parent_payloads_unchanged": True,
        "byte_validation_NOT_fresh_historical_mathematical_model_reading": True,
        "corresponding_NEW_root_D7_accessed": False})
    put("input-validation-v1.json", {"validated_at_utc": utc(), "status": "PASS",
        "author_13_files_all_declared_records_verified": True,
        "current_operative_expected_bodies_match": True,
        "independent_ALL48_ledger_labels": labels(), "closed_scope_notes": 8,
        "protected_occurrences": count, "protected_unique_paths": unique,
        "canonical_deduplicated_sha256": digest, "no_mathematical_execution": True})
    put("metadata-v1.json", {"created_at_utc": utc(),
        "status": "initially blind ENTIRE WHOLE2 initial; findings embargoed",
        "reviewer": "/root/review_2021_reasoning_j15_r2", "constructor": "/root/review_2017_coarsening_r1",
        "constructor_excluded": True, "new_D7_construction_contribution": False,
        "older_D6_authorship_CF_Q_review_not_fresh_self_recertification": True,
        "requested_inherited": {"model": "gpt-6.1-sol", "reasoning": "max"},
        "independent_effective_readback": None,
        "whole_obligations": 48, "ALL_author_packet_files_read": 13,
        "payload_files": 10, "ENTIRE_review_files": 11,
        "substantive_issues": 0, "required_author_repairs": 0, "closed_scope_notes": 8,
        "annual_or_Omega_existence_emptiness_claim": False,
        "corresponding_NEW_root_D7_finding_file_hash_metadata_commentary_accessed": False,
        "BOTH_explicit_before_any_findings_release_required": True,
        "identity_only_initial_handoff": True,
        "mathematical_program_CAS_scan_test_author_source_old_replay": False,
        "Git_shared_old_cache_mutation_spawn_charge_contact_bypass": False,
        "authoritative_weekly_telemetry": {"at_utc": "2026-10-18 14:32:55 UTC", "TOTAL_used_percent": 43,
            "window_minutes": 10080, "resetsAt": 1792874445, "ordinary_usage_allowed": True,
            "legacy_by_limit_agree": True, "account_label": "029a8928...1334ac3a",
            "TOTAL_ceiling": 90, "integration_reserve": True, "no_automatic_later_week": True},
        "FULL_final_ALL10_payload_model_readback_before_freeze_required": True,
        "FULL_manifest_readback_then_SEPARATE_readonly_verify_required": True})
    print(json.dumps({"prepare": "PASS", "whole_obligations": 48,
        "protected_occurrences": count, "unique_paths": unique, "canonical_sha256": digest}))


def validate():
    direct, parents, count, unique, digest = snapshot()
    base = obj(PRE + "baseline-v1.json")
    if (direct != base["direct_current_inputs"] or parents != base["compact_immutable_parent_bindings"]
            or (count, unique, digest) != (base["protected_occurrences"], base["protected_unique_paths"],
                base["canonical_deduplicated_sha256"])):
        raise ValueError("immutable protection drift")
    labels()
    return count, unique, digest


def freeze():
    count, unique, digest = validate()
    payloads = [fp(PRE + s) for s in STATIC + GENERATED]
    for row in payloads:
        if row["path"].endswith(".json"):
            obj(row["path"])
    put("manifest-v1.json", {"frozen_at_utc": utc(),
        "status": "ENTIRE initially blind OTHER WHOLE2 initial; findings embargoed",
        "reviewer": "/root/review_2021_reasoning_j15_r2", "whole_obligations": 48,
        "constructor_excluded": True, "new_D7_construction_contribution": False,
        "payload_files": len(payloads), "ENTIRE_files": len(payloads) + 1,
        "corresponding_NEW_root_D7_finding_file_hash_metadata_commentary_accessed": False,
        "FULL_final_ALL10_payload_model_readback_completed": True,
        "FULL_manifest_readback_then_SEPARATE_readonly_verify_required_before_handoff": True,
        "findings_embargoed_until_BOTH_entire_explicit_confirmation": True,
        "author_main": fp(AUTHOR + "candidate-v1.md"), "author_freeze": fp(PARENTS[0]),
        "immediate_own_parent": fp(PARENTS[2]), "compact_baseline": fp(PRE + "baseline-v1.json"),
        "protected_occurrences": count, "protected_unique_paths": unique,
        "canonical_deduplicated_sha256": digest, "mathematical_execution": False,
        "payloads": payloads})
    print(json.dumps({"manifest": fp(PRE + "manifest-v1.json")}))


def verify():
    manifest = obj(PRE + "manifest-v1.json")
    for row in manifest["payloads"]:
        check(row)
    count, unique, digest = validate()
    if (manifest["whole_obligations"], manifest["payload_files"], manifest["ENTIRE_files"]) != (48, 10, 11):
        raise ValueError("whole packet count mismatch")
    if (count, unique, digest) != (manifest["protected_occurrences"], manifest["protected_unique_paths"],
            manifest["canonical_deduplicated_sha256"]):
        raise ValueError("manifest protection drift")
    print(json.dumps({"SEPARATE_readonly_verify": "PASS", "verified_at_utc": utc(),
        "whole_obligations": 48, "ENTIRE_files": 11,
        "protected_occurrences": count, "unique_paths": unique,
        "manifest": fp(PRE + "manifest-v1.json"), "report": fp(PRE + "report-v1.md")}))


if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) == 2 else ""
    if action not in {"prepare", "freeze", "verify"}:
        raise SystemExit("usage: admin-v1.py prepare|freeze|verify")
    {"prepare": prepare, "freeze": freeze, "verify": verify}[action]()
