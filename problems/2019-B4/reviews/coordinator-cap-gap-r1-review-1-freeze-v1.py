"""One-time administrative blind-review freezer; no mathematical execution."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2019-B4/reviews/coordinator-cap-gap-r1-review-1-"
T = "problems/2019-B4/notes/coordinator-cap-gap-r1-"
PARENT = "problems/2017-B4/notes/reasoning-value-return-r5-freeze-v1.json"


def stamp():
    return datetime.now(timezone.utc).isoformat()


def fp(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def check(expected):
    actual = fp(expected["path"])
    for key in ("bytes", "sha256"):
        if key in expected and actual[key] != expected[key]:
            raise RuntimeError(f"mismatch {expected['path']} {key}")
    return actual


def declared(x):
    if isinstance(x, dict):
        if isinstance(x.get("path"), str) and isinstance(x.get("sha256"), str):
            yield x
        for y in x.values():
            yield from declared(y)
    elif isinstance(x, list):
        for y in x:
            yield from declared(y)


def save(suffix, value):
    path = ROOT / (P + suffix)
    if path.exists():
        raise RuntimeError(f"refuse overwrite {path}")
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


if (ROOT / (P + "manifest-v1.json")).exists():
    raise RuntimeError("already frozen")

rows = []
target = check({"path": T + "freeze-v1.json", "bytes": 3669,
                "sha256": "9b3751764cb2ba0177f3b8ff9e5f90721acf134f3e92c42cf4be67e5179d3d49"})
rows.append(("target freeze", target))
check({"path": T + "candidate-v1.md", "bytes": 11796,
       "sha256": "0e8afb24ec9e58004ee9464de327b309d834058b277eae4a2608d0d7afde5f33"})
manifest = json.loads((ROOT / target["path"]).read_text())
rows.extend(("constructor declared artifact", check(r)) for r in declared(manifest))
inputs = json.loads((ROOT / (T + "input-validation-v1.json")).read_text())
rows.extend(("constructor declared accepted input", check(r)) for r in declared(inputs))
sources = json.loads((ROOT / (T + "sources-v1.json")).read_text())
rows.extend(("constructor compact source parent", check(r)) for r in declared(sources))

old_acceptance = json.loads((ROOT / "problems/2019-B4/reviews/secondpass-acceptance.json").read_text())
for rel in ("notes/secondpass-canonical-renewal.md", "notes/secondpass-rigidity-obstructions.md"):
    rows.append(("operative accepted second-pass body", check({
        "path": "problems/2019-B4/" + rel,
        "sha256": old_acceptance["artifacts"][rel],
    })))

parent_fp = check({"path": PARENT, "bytes": 3146,
                   "sha256": "31b1789d41b1d492ef9f0d2235050025bb341ca70c8eb8d0c66765e63e43fed1"})
parent = json.loads((ROOT / PARENT).read_text())
rows.append(("immutable own parent freeze", parent_fp))
rows.extend(("immediate immutable own parent artifact", check(r)) for r in parent["artifacts"])
earlier = parent["earlier_own_paths_preserved_by_compact_reference"] + len(parent["artifacts"]) + 1

unique = {}
for role, r in rows:
    if r["path"] not in unique:
        unique[r["path"]] = {**r, "occurrences": 0, "roles": []}
    item = unique[r["path"]]
    if item["sha256"] != r["sha256"] or item["bytes"] != r["bytes"]:
        raise RuntimeError("inconsistent duplicates")
    item["occurrences"] += 1
    if role not in item["roles"]:
        item["roles"].append(role)

save("baseline-v1.json", {
    "at_utc": stamp(), "record_occurrences": len(rows), "deduplicated_paths": len(unique),
    "target": target, "compact_own_parent": parent_fp,
    "earlier_own_paths_bound_compactly": earlier,
    "records": [unique[k] for k in sorted(unique)],
    "all_expected_fingerprints_match": True,
    "constructor_or_old_mathematical_program_executed": False,
    "new_peer_report_or_findings_read": False,
})
save("metadata-v1.json", {
    "reviewer": "/root/review_2017_coarsening_r1",
    "review_kind": "fresh initially blind WHOLE nonconstructor R1",
    "target_constructor": "/root", "new_constructor_role": False,
    "older_roles": ["SS1-SS3 whole audit", "separate original-output linear-language research"],
    "older_roles_not_independent_recertification": True,
    "all_constructor_obligations": 24,
    "all_main_and_12_constructor_artifacts_inspected": True,
    "peer_R2_new_reports_findings_read_before_entire_initial_freeze": False,
    "all_new_inferences_reconstructed": True,
    "required_repairs_found": 0, "substantive_issues_found": 0,
    "independent_numerical_check": "hand rational power bounds; no program or author rerun",
    "old_11662_matrix_rows_freshly_rerun": False,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
    "verified_effective_readback": None,
    "last_direct_weekly_telemetry": {"at_utc": "2026-10-17 19:47:17 UTC",
        "total_used_percent": 60, "window_minutes": 10080, "reset_unix": 1792745187,
        "ordinary_usage_allowed": True, "total_ceiling": 90, "reserve": True},
    "compact_own_parent": parent_fp, "earlier_own_paths": earlier,
    "worker_Git_shared_old_cache_mutations_spawning_or_charges": False,
})

for r in unique.values():
    check(r)
save("input-validation-v1.json", {
    "at_utc": stamp(), "all_unchanged": True,
    "record_occurrences_verified": len(rows), "deduplicated_paths_verified": len(unique),
    "baseline": fp(P + "baseline-v1.json"), "compact_own_parent": parent_fp,
    "earlier_own_paths_bound_compactly": earlier,
    "no_historical_inventory_expansion_or_mathematical_rerun": True,
})
suffixes = ["initial-v1.md", "issues-v1.md", "ledger-v1.md", "sources-v1.md",
            "worklog-v1.md", "baseline-v1.json", "metadata-v1.json",
            "input-validation-v1.json", "freeze-v1.py"]
save("manifest-v1.json", {
    "frozen_at_utc": stamp(), "status": "COMPLETE initially blind WHOLE R1 audit",
    "reviewer": "/root/review_2017_coarsening_r1", "target": target,
    "target_main": fp(T + "candidate-v1.md"), "whole_obligations": 24,
    "initial_blind_until_entire_packet_frozen": True,
    "all_constructor_artifacts_and_accepted_input_scopes_covered": True,
    "record_occurrences_verified": len(rows), "deduplicated_paths_verified": len(unique),
    "compact_immutable_parent": parent_fp, "earlier_own_paths_preserved": earlier,
    "mathematical_code_CAS_scan_or_author_certificate_replay": False,
    "verdict": "no substantive defect in exact CG1-CG4 scope relative to accepted inputs",
    "coordinator_promotion_or_second_review": False,
    "artifacts": [fp(P + s) for s in suffixes],
})
print(json.dumps({"manifest": fp(P + "manifest-v1.json"), "artifacts": len(suffixes),
                  "record_occurrences": len(rows), "unique_paths": len(unique), "old_own_paths": earlier}))
