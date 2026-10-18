#!/usr/bin/env python3
"""PM8 metadata ONLY: read/hash bytes, inventory labels, exclusive own writes.

No arrangement, path, degree, probability, real constant, root, logarithm,
optimization, inequality, certificate or mathematical assertion is evaluated.
--verify is a separate read-only pass. This script never edits old inputs.
"""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/notes/reasoning-path-mass-return-r8-"
PARENT = "problems/2024-B4/notes/reasoning-cofactor-return-r6-freeze-v1.json"
CLAIMS = ["PM8A", "PM8B", "PM8C", "PM8D", "PM8E"]

def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def row(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}

def jread(path):
    return json.loads((ROOT / path).read_text())

def check(record):
    got = row(record["path"])
    for key in ("bytes", "sha256"):
        assert got[key] == record[key], (record["path"], key)
    return got

def exclusive(path, obj):
    assert path.startswith(PREFIX), path
    with (ROOT / path).open("x", encoding="utf-8") as stream:
        json.dump(obj, stream, indent=2, ensure_ascii=False)
        stream.write("\n")

def records(obj):
    if isinstance(obj, dict):
        if (isinstance(obj.get("path"), str)
                and isinstance(obj.get("bytes"), int)
                and isinstance(obj.get("sha256"), str)
                and re.fullmatch(r"[0-9a-f]{64}", obj["sha256"])):
            yield {k: obj[k] for k in ("path", "bytes", "sha256")}
        for value in obj.values():
            yield from records(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from records(value)

DIRECT = [
    "AGENTS.md",
    "problems/2017-B4/statement.md",
    "problems/2017-B4/proofs/reviewed-weighted-cutpath-r1-v1.1.md",
    "problems/2017-B4/proofs/reviewed-weighted-optimum-r2-v1.1.md",
    "problems/2017-B4/reviews/coordinator-weighted-cutpath-r1-acceptance.md",
    "problems/2017-B4/reviews/coordinator-weighted-cutpath-r1-acceptance.json",
    "problems/2017-B4/reviews/coordinator-weighted-optimum-r2-acceptance.md",
    "problems/2017-B4/reviews/coordinator-weighted-optimum-r2-acceptance.json",
    "problems/2017-B4/notes/coordinator-weighted-cutpath-r1-source-audit-v1.md",
    "problems/2017-B4/notes/coordinator-weighted-cutpath-r1-sources-v1.json",
    "problems/2017-B4/notes/coordinator-weighted-cutpath-r1-failures-worklog-v1.md",
    "problems/2017-B4/notes/coordinator-weighted-optimum-r2-sources-v1.md",
    "problems/2017-B4/notes/coordinator-weighted-optimum-r2-failed-routes-v1.md",
    PARENT,
]

KNOWN = [
    {"path": "AGENTS.md", "bytes": 4707,
     "sha256": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"},
    {"path": "problems/2017-B4/proofs/reviewed-weighted-cutpath-r1-v1.1.md",
     "bytes": 15914,
     "sha256": "93c08b0a43426c972bd6a0042c7e496cb08a106873c931f0231901e9f425f14b"},
    {"path": "problems/2017-B4/proofs/reviewed-weighted-optimum-r2-v1.1.md",
     "bytes": 18824,
     "sha256": "dcc12d2989e5ab657960498179e2585e62ad35ffb1989a4bca72fef8fb953f9a"},
    {"path": PARENT, "bytes": 3001,
     "sha256": "ea0a7c41741ca3655c36825a6a299c1859505855c786ea7494a9204995a0b8a9"},
]

def obligation_ids():
    text = (ROOT / (PREFIX + "obligations-v1.md")).read_text()
    ids = re.findall(r"^\| (PM8-[0-9]{2}) \|", text, re.MULTILINE)
    expected = [f"PM8-{i:02d}" for i in range(1, 65)]
    assert ids == expected, ids
    return ids

def verify():
    freeze = jread(PREFIX + "freeze-v1.json")
    for rec in freeze["artifacts"]:
        check(rec)
    baseline = jread(PREFIX + "baseline-v1.json")
    for rec in baseline["deduplicated_old_paths"]:
        check(rec)
    for rec in baseline["bound_metadata"]:
        check(rec)
    assert len(obligation_ids()) == freeze["whole_obligations"]
    for suffix in ("sources-v1.json", "input-validation-v1.json",
                   "metadata-v1.json", "baseline-v1.json"):
        jread(PREFIX + suffix)
    print(json.dumps({"status": "SEPARATE read-only postverification PASS",
                      "verified_at_utc": now(),
                      "freeze": row(PREFIX + "freeze-v1.json"),
                      "main": row(PREFIX + "candidate-v1.md"),
                      "whole_obligations": len(obligation_ids()),
                      "all_artifacts_including_freeze": len(freeze["artifacts"]) + 1,
                      "mathematical_code_executed": False}, indent=2))

def create():
    ids = obligation_ids()
    for rec in KNOWN:
        check(rec)
    bound_metadata_paths = [
        "problems/2017-B4/reviews/coordinator-weighted-cutpath-r1-acceptance.json",
        "problems/2017-B4/reviews/coordinator-weighted-optimum-r2-acceptance.json",
        PARENT,
    ]
    occurrences = []
    for path in bound_metadata_paths:
        # One declared-document pass only, never recursive historical traversal.
        occurrences.extend(records(jread(path)))
    occurrences.extend(KNOWN)
    occurrences.extend(row(path) for path in DIRECT)
    dedup = {}
    for rec in occurrences:
        got = check(rec)
        if got["path"] in dedup:
            assert got == dedup[got["path"]]
        dedup[got["path"]] = got
    bound_metadata = [row(path) for path in bound_metadata_paths]
    baseline = {
        "recorded_at_utc": now(),
        "status": "compact necessary-old-input preservation; no mathematical certificate",
        "immediate_own_parent": row(PARENT),
        "bound_metadata": bound_metadata,
        "fingerprint_occurrences_verified": len(occurrences),
        "deduplicated_old_paths": [dedup[path] for path in sorted(dedup)],
        "historical_rows_reexpanded_or_reproduced": False,
        "preserved_reproduction_reference": "immutable parent and authority metadata by path/bytes/SHA",
    }
    exclusive(PREFIX + "baseline-v1.json", baseline)
    exclusive(PREFIX + "input-validation-v1.json", {
        "validated_at_utc": now(),
        "all_necessary_declared_fingerprints_match": True,
        "fingerprint_occurrences": len(occurrences),
        "deduplicated_old_paths": len(dedup),
        "bound_metadata": bound_metadata,
        "whole_obligation_labels": ids,
        "validation_is_metadata_only_not_mathematical_verification": True,
    })
    exclusive(PREFIX + "metadata-v1.json", {
        "recorded_at_utc": now(),
        "status": "candidate proof - unverified",
        "constructor": "/root/review_2017_coarsening_r1",
        "constructor_excluded_from_TWO_OTHER_reviews": True,
        "root_contribution": "general target only; no NEW proof inference",
        "older_C_role": "OTHER WC/WO reviewer; not their constructor",
        "whole_claims": CLAIMS,
        "whole_obligations": len(ids),
        "TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits_required": True,
        "coordinator_reconciliation_required_before_promotion": True,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "verified_effective_readback": None,
        "authorized_weekly_reset": 1792874445,
        "latest_authoritative_root_total_used_percent": 35,
        "ceiling_total_used_percent": 90,
        "integration_reserve_required": True,
        "no_automatic_later_window_authorization": True,
        "mathematical_executable_CAS_optimizer_or_scan": False,
        "new_third_party_download_or_cache_write": False,
        "NEW_queued_D6_peer_content_hash_metadata_or_findings_accessed": False,
        "exact_value_effective_R_matching_lower_annual_or_priority_claim": False,
    })
    suffixes = [
        "candidate-v1.md", "obligations-v1.md", "constructor-checks-v1.md",
        "failures-worklog-v1.md", "source-audit-v1.md", "sources-v1.json",
        "freeze-v1.py", "baseline-v1.json", "input-validation-v1.json",
        "metadata-v1.json",
    ]
    exclusive(PREFIX + "freeze-v1.json", {
        "frozen_at_utc": now(),
        "status": "ENTIRE PM8A--PM8E constructor checkpoint; candidate proof - unverified",
        "constructor": "/root/review_2017_coarsening_r1",
        "whole_claims": CLAIMS,
        "whole_obligations": len(ids),
        "all_artifacts_including_freeze": len(suffixes) + 1,
        "immediate_own_parent": row(PARENT),
        "fingerprint_occurrences_verified": len(occurrences),
        "deduplicated_old_paths_verified": len(dedup),
        "TWO_OTHER_whole_audits_and_reconciliation_REQUIRED": True,
        "FULL_readback_and_SEPARATE_readonly_verify_follow_this_immutable_freeze": True,
        "mathematical_computation": False,
        "artifacts": [row(PREFIX + suffix) for suffix in suffixes],
    })
    print(json.dumps({"created": row(PREFIX + "freeze-v1.json"),
                      "main": row(PREFIX + "candidate-v1.md"),
                      "all_artifacts_including_freeze": len(suffixes) + 1,
                      "whole_obligations": len(ids),
                      "fingerprint_occurrences": len(occurrences),
                      "deduplicated_old_paths": len(dedup),
                      "next": "FULL readback ALL11 then SEPARATE --verify"}, indent=2))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    verify() if args.verify else create()
