"""Administrative integrity only. No mathematical construction is executed.

Run --baseline once, then --freeze once after the whole packet is written.
Writes only the assigned reasoning-value-return-r5-* prefix. Old metadata
is bound compactly; neither old proofs nor old computations are rerun.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/notes/reasoning-value-return-r5-"
PARENT = "problems/2024-B4/notes/reasoning-sector3-return-r1-freeze-v1.json"
PARENT_BYTES = 3893
PARENT_SHA = "2a3cf9ce9d04b92f42a03e0847a478c6b3402e4eadf7067cb2addf4f97055be2"


def now():
    return datetime.now(timezone.utc).isoformat()


def record(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def verify(expected):
    actual = record(expected["path"])
    for key in ("bytes", "sha256"):
        if key in expected and actual[key] != expected[key]:
            raise RuntimeError(f"fingerprint mismatch {expected['path']} {key}")
    return actual


def write_new(suffix, value):
    path = ROOT / (PREFIX + suffix)
    if path.exists():
        raise RuntimeError(f"refusing overwrite {path}")
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def declared(value):
    if isinstance(value, dict):
        if isinstance(value.get("path"), str) and isinstance(value.get("sha256"), str):
            yield value
        for child in value.values():
            yield from declared(child)
    elif isinstance(value, list):
        for child in value:
            yield from declared(child)


def baseline():
    parent_record = verify({"path": PARENT, "bytes": PARENT_BYTES, "sha256": PARENT_SHA})
    parent = json.loads((ROOT / PARENT).read_text(encoding="utf-8"))
    rows = [("immutable parent manifest", parent_record)]
    for expected in parent["artifacts"]:
        rows.append(("immediate immutable parent artifact", verify(expected)))

    direct = [
        "AGENTS.md",
        "problems/2017-B4/statement.md",
        "problems/2017-B4/references.md",
        "problems/2017-B4/proofs/reviewed-fixedD-structural-v1.2.md",
        "problems/2017-B4/proofs/reviewed-clean-strata-v1.1.md",
        "problems/2017-B4/proofs/reviewed-global-value-return-v1.1.md",
        "problems/2017-B4/proofs/reviewed-global-value-return-r2-v1.1.md",
        "problems/2017-B4/proofs/reviewed-reasoning-value-return-r3-v1.1.md",
        "problems/2017-B4/proofs/reviewed-reasoning-value-return-r4-v1.1.md",
        "problems/2017-B4/reviews/reasoning-value-return-r4-acceptance.md",
        "problems/2017-B4/reviews/reasoning-value-return-r4-acceptance.json",
        "problems/2017-B4/reviews/reasoning-value-return-r4-acceptance-integrity.json",
    ]
    rows.extend(("direct accepted input/scope", record(path)) for path in direct)
    ec_path = "problems/2017-B4/reviews/reasoning-value-return-r4-acceptance.json"
    ec = json.loads((ROOT / ec_path).read_text(encoding="utf-8"))
    ec_records = list(declared(ec))
    rows.extend(("declared EC acceptance fingerprint", verify(expected)) for expected in ec_records)
    official = [
        {"path": ".cache/official/2017-paper_b.pdf", "sha256": "69d7cf84128c2464d962136ed613808b6c7a7b07122cfba9c06b5adf775e2a68"},
        {"path": ".cache/official/2017-solutions.pdf", "sha256": "c272a72239ef4c2ccd54df0702140179e0a9b85f5a9028c87d485841eb1a2c12"},
    ]
    rows.extend(("old official source bytes; no fresh full PDF read", verify(expected)) for expected in official)

    by_path = {}
    for role, item in rows:
        if item["path"] not in by_path:
            by_path[item["path"]] = {**item, "occurrences": 0, "roles": []}
        target = by_path[item["path"]]
        if target["bytes"] != item["bytes"] or target["sha256"] != item["sha256"]:
            raise RuntimeError("inconsistent duplicate record")
        target["occurrences"] += 1
        if role not in target["roles"]:
            target["roles"].append(role)

    earlier = int(parent["earlier_own_paths_preserved_by_compact_reference"])
    parent_packet = len(parent["artifacts"]) + 1
    info = {
        "created_at_utc": now(),
        "administrative_only": True,
        "compact_immutable_parent": parent_record,
        "parent_artifacts_verified": len(parent["artifacts"]),
        "earlier_own_paths_bound_by_parent": earlier,
        "immediate_parent_packet_paths": parent_packet,
        "all_earlier_own_paths_bound_compactly": earlier + parent_packet,
        "older_transitive_inventory_freshly_expanded_or_math_reread": False,
        "EC_acceptance_declared_occurrences_verified": len(ec_records),
        "record_occurrences": len(rows),
        "deduplicated_paths": len(by_path),
        "records": [by_path[path] for path in sorted(by_path)],
    }
    write_new("baseline-v1.json", info)
    write_new("metadata-v1.json", {
        "status": "candidate proof - unverified",
        "constructor": "/root/review_2017_coarsening_r1",
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
        "independently_verified_effective_settings": None,
        "ownership": "only problems/2017-B4/notes/reasoning-value-return-r5-*",
        "new_mathematical_claims": ["GR1", "GR2", "GR3", "GR4"],
        "whole_obligations": 40,
        "two_OTHER_initially_blind_WHOLE_audits_required": True,
        "root_role": "broad target and scope cautions; no new proof inference used",
        "old_C_authorship": ["FD/profile/annulus/rank background", "V1-V4", "OP1-OP3"],
        "old_C_role_not_independent_recertification": True,
        "mathematical_code_CAS_scan_certificate_or_algorithm_execution": False,
        "new_native_child_or_pending_approval": False,
        "new_remote_PDF_byte_download_or_cache_hash_claim": False,
        "direct_weekly_telemetry": {
            "at_utc": "2026-10-17 19:47:17 UTC", "total_used_percent": 60,
            "window_minutes": 10080, "reset_unix": 1792745187,
            "ordinary_usage_allowed": True, "total_ceiling_percent": 90,
            "review_integration_reserve": True,
        },
        "proof_limits": {
            "exponential_count_mass": False, "effective_upper_R": False,
            "numerical_scalar_value": False, "two_sided_computability": False,
            "exact_arbitrary_decoration_preservation": False,
            "straightening_or_mixing": False, "novelty": False,
        },
        "compact_parent": parent_record,
        "earlier_own_path_count": earlier + parent_packet,
    })
    print(json.dumps({"phase": "baseline", "occurrences": len(rows), "unique_paths": len(by_path), "earlier_own_paths": earlier + parent_packet}))


def freeze():
    base = json.loads((ROOT / (PREFIX + "baseline-v1.json")).read_text(encoding="utf-8"))
    checked = [verify(expected) for expected in base["records"]]
    write_new("input-validation-v1.json", {
        "checked_at_utc": now(), "all_match": True,
        "baseline": record(PREFIX + "baseline-v1.json"),
        "record_occurrences": base["record_occurrences"],
        "deduplicated_paths": len(checked),
        "compact_parent": base["compact_immutable_parent"],
        "parent_artifacts_verified": base["parent_artifacts_verified"],
        "all_earlier_own_paths_bound_compactly": base["all_earlier_own_paths_bound_compactly"],
        "historical_inventory_not_recopied": True,
        "mathematical_program_rerun": False,
    })
    suffixes = [
        "candidate-v1.md", "obligations-v1.md", "source-audit-v1.md",
        "failed-routes-v1.md", "worklog-v1.md", "baseline-v1.json",
        "metadata-v1.json", "input-validation-v1.json", "freeze-v1.py",
    ]
    artifacts = [record(PREFIX + suffix) for suffix in suffixes]
    write_new("freeze-v1.json", {
        "frozen_at_utc": now(),
        "status": "candidate proof - unverified; COMPLETE GR1-GR4 mathematical checkpoint",
        "constructor": "/root/review_2017_coarsening_r1",
        "claims": [
            "fixed scalar cone and entire generic level graphs",
            "one simultaneous phase with once-only pair crossings",
            "every-p actual full-boundary tiling within (1+D^3)/p",
            "finite rational PL algorithm and exact uniform-profile characterization",
        ],
        "whole_obligations": 40,
        "two_OTHER_initially_blind_WHOLE_audits_required": True,
        "compact_immutable_parent_manifest": base["compact_immutable_parent"],
        "earlier_own_paths_preserved_by_compact_reference": base["all_earlier_own_paths_bound_compactly"],
        "record_occurrences_verified": base["record_occurrences"],
        "deduplicated_paths_verified": len(checked),
        "all_current_inputs_and_immediate_parent_files_reverified": True,
        "mathematical_code_or_algorithm_execution": False,
        "no_entropy_upper_R_count_mass_numerical_value_computability_or_novelty_claim": True,
        "administrative_command": "/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 " + PREFIX + "freeze-v1.py --freeze",
        "artifacts": artifacts,
    })
    print(json.dumps({"phase": "frozen", "artifacts": len(artifacts), "manifest": record(PREFIX + "freeze-v1.json")}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--baseline", action="store_true")
    group.add_argument("--freeze", action="store_true")
    args = parser.parse_args()
    if args.baseline:
        baseline()
    else:
        freeze()
