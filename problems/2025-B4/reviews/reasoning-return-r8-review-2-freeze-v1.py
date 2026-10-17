"""Administrative-only WHOLE R8 R2 freezer; executes no mathematics."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2025-B4/reviews/reasoning-return-r8-review-2-"
T = "problems/2025-B4/notes/reasoning-return-r8-"
OWN_PARENT = "problems/2019-B4/reviews/coordinator-cap-gap-r1-review-1-manifest-v1.json"


def now():
    return datetime.now(timezone.utc).isoformat()


def fp(path):
    if path.startswith("problems/2025-B4/reviews/reasoning-return-r8-") and not path.startswith(P):
        raise RuntimeError("new R8 peer files forbidden before complete initial freeze")
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def verify(expected):
    actual = fp(expected["path"])
    for key in ("bytes", "sha256"):
        if key in expected and actual[key] != expected[key]:
            raise RuntimeError(f"immutable mismatch {expected['path']} {key}")
    return actual


def records(x):
    if isinstance(x, dict):
        if isinstance(x.get("path"), str) and isinstance(x.get("sha256"), str):
            yield x
        for y in x.values():
            yield from records(y)
    elif isinstance(x, list):
        for y in x:
            yield from records(y)


def save(suffix, value):
    path = ROOT / (P + suffix)
    if path.exists():
        raise RuntimeError(f"refuse overwrite {path}")
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


if (ROOT / (P + "manifest-v1.json")).exists():
    raise RuntimeError("initial already frozen")

rows = []
target_fp = verify({"path": T + "freeze-v1.json", "bytes": 4298,
                    "sha256": "a68ae37d1d5b9f0b209629e6d2027da1ad0fe8d8e6d889b6e261bc0f5a8cff04"})
main_fp = verify({"path": T + "candidate-v1.md", "bytes": 25033,
                  "sha256": "2688587a44e9c161c7bb2bcdc6eecfb474c231ab9542572aaec5e9ed557a9b8d"})
rows.append(("exact target freeze", target_fp))
for suffix in ("freeze-v1.json", "sources-v1.json", "input-validation-v1.json"):
    doc = json.loads((ROOT / (T + suffix)).read_text())
    rows.extend(("explicit constructor " + suffix + " declaration", verify(r)) for r in records(doc))

authority_summary = []
for name in ("original-weight-universal", "reasoning-return-r6", "reasoning-return-r7"):
    path = "problems/2025-B4/reviews/" + name + "-acceptance.json"
    doc = json.loads((ROOT / path).read_text())
    declared = list(records(doc))
    rows.extend(("necessary accepted " + name + " declaration", verify(r)) for r in declared)
    authority_summary.append({"acceptance": fp(path), "explicit_occurrences_checked": len(declared)})

parent_fp = verify({"path": OWN_PARENT, "bytes": 3126,
                    "sha256": "c482bb0b681d7ff110ecfc4eea97370fbf1dac041e8f84196f0758d8638df400"})
parent = json.loads((ROOT / OWN_PARENT).read_text())
rows.append(("compact immutable own parent", parent_fp))
rows.extend(("immediate immutable own parent artifact", verify(r)) for r in parent["artifacts"])
old_own = parent["earlier_own_paths_preserved"] + len(parent["artifacts"]) + 1

unique = {}
for role, r in rows:
    if r["path"] not in unique:
        unique[r["path"]] = {**r, "occurrences": 0, "roles": []}
    item = unique[r["path"]]
    if item["bytes"] != r["bytes"] or item["sha256"] != r["sha256"]:
        raise RuntimeError("inconsistent duplicate")
    item["occurrences"] += 1
    if role not in item["roles"]:
        item["roles"].append(role)

save("baseline-v1.json", {
    "at_utc": now(), "target": target_fp, "target_main": main_fp,
    "record_occurrences": len(rows), "deduplicated_paths": len(unique),
    "records": [unique[k] for k in sorted(unique)],
    "accepted_authority_occurrence_summaries": authority_summary,
    "compact_own_parent": parent_fp, "earlier_own_paths_bound_compactly": old_own,
    "constructor_historical_438_occurrence_400_path_inventory_reexpanded": False,
    "old_transitive_inventory_bound_by_immutable_wrappers": True,
    "new_peer_R8_files_or_findings_read": False,
    "mathematical_program_CAS_or_author_rerun": False,
})
save("metadata-v1.json", {
    "reviewer": "/root/review_2017_coarsening_r1",
    "kind": "fresh initially blind WHOLE nonconstructor R2",
    "new_R8_constructor": "/root/review_2022_complexity_r2",
    "reviewer_new_R8_contribution": False,
    "old_roles": ["FS/R6/R7 constructor", "UW/OW/RK/MS whole review roles"],
    "not_independent_recertification_of_own_old_inputs": True,
    "complete_new_main_and_all_ten_constructor_artifacts_inspected": True,
    "all_author_obligations_covered": 48,
    "initial_blind_until_ENTIRE_packet_frozen": True,
    "root_peer_new_R8_reports_or_findings_read": False,
    "substantive_issues_found": 0, "required_repairs": 0,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
    "effective_setting_readback": None,
    "mathematical_code_scan_CAS_rank_test_certificate_or_author_rerun": False,
    "new_native_mathematical_child_or_pending_approval": False,
    "last_direct_weekly_telemetry": {"at_utc": "2026-10-17 20:00:34 UTC",
        "total_used_percent": 62, "window_minutes": 10080, "reset_unix": 1792745187,
        "ordinary_usage_allowed": True, "total_ceiling_percent": 90, "reserve": True},
    "compact_own_parent": parent_fp, "earlier_own_paths": old_own,
    "annual_exclusion_useful_unconditional_height_improvement_or_novelty_promoted": False,
    "worker_Git_shared_old_cache_mutations_spawning_contact_or_charges": False,
})

for item in unique.values():
    verify(item)
save("input-validation-v1.json", {
    "at_utc": now(), "all_unchanged": True,
    "baseline": fp(P + "baseline-v1.json"),
    "record_occurrences_verified": len(rows), "deduplicated_paths_verified": len(unique),
    "compact_own_parent": parent_fp, "earlier_own_paths_bound_compactly": old_own,
    "full_historical_inventory_freshly_reexpanded_or_math_reread": False,
    "mathematical_program_execution": False,
})

suffixes = ["initial-v1.md", "issues-v1.md", "ledger-v1.md", "sources-v1.md",
            "worklog-v1.md", "baseline-v1.json", "metadata-v1.json",
            "input-validation-v1.json", "freeze-v1.py"]
save("manifest-v1.json", {
    "frozen_at_utc": now(), "status": "COMPLETE initially blind WHOLE R8 R2 initial",
    "reviewer": "/root/review_2017_coarsening_r1", "new_constructor": "/root/review_2022_complexity_r2",
    "target_main": main_fp, "target_freeze": target_fp, "whole_obligations": 48,
    "all_ten_constructor_artifacts_and_exact_accepted_input_scopes_covered": True,
    "new_root_peer_R8_findings_unread_until_entire_initial_frozen": True,
    "old_constructor_roles_disclosed_no_independent_self_recertification": True,
    "verdict": "no substantive defect in exact R8A-R8D scope relative to accepted inputs",
    "substantive_issues": 0, "required_repairs": 0,
    "record_occurrences_verified": len(rows), "deduplicated_paths_verified": len(unique),
    "compact_immutable_own_parent": parent_fp, "earlier_own_paths_preserved": old_own,
    "mathematical_code_CAS_scan_rank_test_or_author_rerun": False,
    "no_evaluated_nonvanishing_annual_exclusion_useful_global_height_or_novelty_claim": True,
    "artifacts": [fp(P + suffix) for suffix in suffixes],
})
print(json.dumps({"manifest": fp(P + "manifest-v1.json"), "artifacts": len(suffixes),
                  "record_occurrences": len(rows), "unique_paths": len(unique), "old_own_paths": old_own}))
