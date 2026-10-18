"""Administrative-only affected R6 v1.1 whole-reaudit freeze; never runs author code."""
from pathlib import Path
from datetime import datetime, timezone
import difflib
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2017-B4/reviews/reasoning-value-return-r6-review-1-reaudit-v1.1-"
T = "problems/2017-B4/notes/reasoning-value-return-r6-"
rows = []
groups = []


def data(path):
    assert not Path(path).is_absolute() and ".." not in Path(path).parts
    assert not Path(path).name.startswith("reasoning-value-return-r6-review-2-reaudit")
    return (ROOT / path).read_bytes()


def fp(path):
    b = data(path)
    return {"path": path, "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}


def record(path, size, sha):
    return {"path": path, "bytes": size, "sha256": sha}


def check(item, origin):
    core = {k: item[k] for k in ("path", "bytes", "sha256")}
    assert fp(core["path"]) == core, (origin, core["path"])
    rows.append({"origin": origin, **core})
    return core


def canonical(items):
    unique = {}
    for item in items:
        core = {k: item[k] for k in ("path", "bytes", "sha256")}
        if core["path"] in unique:
            assert unique[core["path"]] == core
        unique[core["path"]] = core
    ordered = [unique[path] for path in sorted(unique)]
    digest = hashlib.sha256(json.dumps(ordered, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return {"occurrences": len(items), "unique_paths": len(unique),
            "canonical_deduplicated_summary_sha256": digest}


def group(name, start, metadata, selector, extra=None):
    value = {"group": name, "metadata": fp(metadata), "reproduce_by_selector": selector,
             "verified_current_summary": canonical(rows[start:])}
    if extra:
        value.update(extra)
    groups.append(value)


def save(suffix, value):
    with (ROOT / (P + suffix)).open("x", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")
    return fp(P + suffix)


start = len(rows)
manifest_path = T + "freeze-v1.1.json"
check(record(manifest_path, 2987,
             "bd8d7cfcd6d81dd09432e2c8c445bd401c864f3d640fc7214336f034e9effa02"),
      "exact assigned full repair freeze")
target = json.loads(data(manifest_path))
assert target["full_obligations"] == 60 and len(target["artifacts"]) == 11
for item in target["artifacts"]:
    check(item, "full repair frozen payload")
assert fp(T + "candidate-v1.1.md") == record(T + "candidate-v1.1.md", 38143,
    "44f327ce61046b8226ff62d699ed0fa004ceb11e7900779636c583b27a2745db")
group("complete repair packet", start, manifest_path, "self plus artifacts[0:11]")

start = len(rows)
baseline_path = T + "baseline-v1.1.json"
baseline = json.loads(data(baseline_path))
assert len(baseline["records"]) == 38
for item in baseline["records"]:
    check(item, "repair compact preservation/current input declaration")
index = {item["path"]: {k: item[k] for k in ("path", "bytes", "sha256")}
         for item in baseline["records"]}
for old_manifest in [baseline["original_constructor_manifest"],
                     *baseline["both_original_whole_initial_manifests"],
                     baseline["immutable_own_parent"]]:
    assert index[old_manifest["path"]] == old_manifest
    old = json.loads(data(old_manifest["path"]))
    for item in old["artifacts"]:
        assert index[item["path"]] == {k: item[k] for k in ("path", "bytes", "sha256")}
group("original v1, BOTH complete initial sets, author parent and DC/US bodies", start,
      baseline_path, "records[0:38]", {
          "both_original_whole_initial_manifests": baseline["both_original_whole_initial_manifests"],
          "all_original_artifact_sets_crossmatched": True,
          "historical_author_paths_bound_not_recopied": baseline["historical_own_paths_bound"],
      })

start = len(rows)
original_baseline_path = T + "baseline-v1.json"
original_baseline = json.loads(data(original_baseline_path))
authorities = original_baseline["authoritative_acceptance_metadata"]
assert len(authorities) == 6
for item in [*authorities, *original_baseline["explicit_inputs"]]:
    check(item, "original authority metadata/protocol/domain compact declaration")
group("old accepted scopes, current AGENTS/domain and immutable context", start,
      original_baseline_path, "authoritative_acceptance_metadata plus explicit_inputs", {
          "no_recursive_old_inventory_copy_or_unrelated_mathematical_reread": True})

start = len(rows)
selectors = []
for authority_record in authorities:
    authority = json.loads(data(authority_record["path"]))
    selected = []
    for key, value in authority.items():
        if isinstance(value, dict) and all(k in value for k in ("path", "bytes", "sha256")):
            check(value, "accepted authority top-level " + key + " declaration")
            selected.append(key)
    selectors.append({"metadata": authority_record, "top_level_keys": selected})
groups.append({"group": "accepted candidate/copy/direct integrity declarations",
               "selectors": selectors, "verified_current_summary": canonical(rows[start:]),
               "deeper_historical_inventories_bound_only": True})

start = len(rows)
parent_path = "problems/2025-B4/reviews/reasoning-return-r9-runge-review-2-manifest-v1.json"
check(record(parent_path, 3792,
             "d123d5a2b91f6846ee61a702de890d61f4e7c2b3bc568f1f7773331ea51b95d5"),
      "immediate own immutable whole-review parent, NOT mathematical premise")
parent = json.loads(data(parent_path))
assert len(parent["artifacts"]) == 7
for item in parent["artifacts"]:
    check(item, "direct own immutable parent payload, NOT premise")
group("immediate own preservation parent", start, parent_path, "self plus artifacts[0:7]", {
    "own_parent_compact_input_summary_bound": parent["compact_input_summary"]})

old_main = data(T + "candidate-v1.md").decode()
new_main = data(T + "candidate-v1.1.md").decode()
unchanged = {
    "PM1_sections1_to3_exact_text_equal": old_main[old_main.index("## 1."):old_main.index("## 4.")]
        == new_main[new_main.index("## 1."):new_main.index("## 4.")],
    "PM4_section6_to_end_exact_text_equal": old_main[old_main.index("## 6."):]
        == new_main[new_main.index("## 6."):],
    "PM1_summary_exact_text_equal": old_main[old_main.index("**PM1,"):old_main.index("**PM2,")]
        == new_main[new_main.index("**PM1,"):new_main.index("**PM2,")],
    "PM4_summary_and_old_roles_exact_text_equal": old_main[old_main.index("**PM4,"):old_main.index("## 1.")]
        == new_main[new_main.index("**PM4,"):new_main.index("## 1.")],
}
assert all(unchanged.values()), unchanged
diff = []
for stem in ("candidate", "obligations", "sources", "failures", "worklog"):
    before, after = T + stem + "-v1.md", T + stem + "-v1.1.md"
    diff.extend(difflib.unified_diff(data(before).decode().splitlines(keepends=True),
                                   data(after).decode().splitlines(keepends=True),
                                   fromfile=before, tofile=after))
assert "".join(diff).encode() == data(T + "diff-v1-to-v1.1.patch")
unchanged["complete_five_file_diff_exactly_reproduced_without_author_execution"] = True

ledger = data(P + "issues.md").decode()
ids = re.findall(r"^\| ((?:PM|FC)-\d\d) \|", ledger, flags=re.MULTILINE)
expected_ids = [f"PM-{n:02d}" for n in range(1, 49)] + [f"FC-{n:02d}" for n in range(1, 13)]
assert ids == expected_ids, ids
assert len(re.findall(r"\| Closed[^|\n]* \|$", ledger, flags=re.MULTILINE)) == 60
assert "zero new" in ledger and "PMR2-01: resolved" in ledger

summary = canonical(rows)
summary.update({"encoding": "UTF8 JSON sorted unique path/bytes/sha256; sorted keys; compact separators",
                "parent_inventory_rows_reproduced_from_bound_metadata_not_recopied": True})
payloads = [P + suffix for suffix in (
    "initial.md", "issues.md", "source-checks.md", "worklog.md", "freeze.py")]
assert all((ROOT / path).is_file() for path in payloads)
for suffix in ("input-validation.json", "freeze-output.json", "manifest.json"):
    assert not (ROOT / (P + suffix)).exists(), suffix

save("input-validation.json", {
    "status": "all necessary current declarations verified; exact parent metadata bound compactly",
    "summary": summary, "groups": groups, "text_preservation_checks": unchanged,
    "all_60_ledger_IDs_exact_and_closed": True,
    "NEW_B_affected_reaudit_material_read_or_hashed": False,
    "both_ORIGINAL_frozen_whole_reports_ledgers_sources_comparison_authorized": True,
    "old_original_dispositions_preserved_not_rewritten": True,
    "browser_sources_have_URLs_read_limits_no_invented_native_byte_hash": True,
})
payloads.append(P + "input-validation.json")
unique = {}
for item in rows:
    unique[item["path"]] = {k: item[k] for k in ("path", "bytes", "sha256")}
for item in unique.values():
    assert fp(item["path"]) == item
output = {
    "status": "ENTIRE affected WHOLE R1 reaudit v1.1 complete and frozen",
    "all_obligations": 60, "closed": 60, "PMR2_01": "resolved by author v1.1",
    "new_substantive_issues": 0, "open_issues": 0, "required_author_repairs": 0,
    "compact_current_summary": summary, "text_preservation_checks": unchanged,
    "all_current_input_rows_rechecked": True,
    "no_author_or_mathematical_program_executed": True,
}
save("freeze-output.json", output)
payloads.append(P + "freeze-output.json")
manifest = {
    "frozen_at_utc": datetime.now(timezone.utc).isoformat(),
    "status": output["status"], "reviewer": "/root/review_2021_reasoning_j15_r2",
    "target": fp(T + "candidate-v1.1.md"), "constructor_freeze": fp(manifest_path),
    "scope": "FULL PM2/PM3 affected proof, unchanged PM1/PM4 preservation, ALL48+12 obligations",
    "whole_obligations": 60, "closed": 60,
    "PMR2_01": "resolved for author version1.1 in literal source domain",
    "new_substantive_issues": 0, "open_issues": 0, "required_author_repairs": 0,
    "recommendation": "scoped PM1-PM4 acceptance after BOTH affected whole reaudits and coordinator reconciliation",
    "coordinator_promotion": False,
    "original_R1_closed_N1_and_R2_PMR2_01_bytes_dispositions_preserved": True,
    "root_C_contributors_excluded": True,
    "old_S_D_HC_EC_authorship_G_GR_review_roles_disclosed_not_self_recertified": True,
    "NEW_B_reaudit_reports_ledgers_sources_manifests_metadata_findings_read_or_hashed_before_ENTIRE_freeze": False,
    "compact_current_summary": summary, "immutable_input_groups": len(groups),
    "no_historical_inventory_recopy_or_unrelated_old_mathematical_reread": True,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
    "independently_verified_effective_settings": None,
    "mathematical_program_scan_CAS_author_rerun_old_certificate_replay": False,
    "old_shared_cache_Git_write_spawn_contact_charge_bypass": False,
    "authoritative_weekly_snapshot": {
        "tool": "mcp__codex_app__get_usage_limits", "at_utc": "2026-10-18 01:03:44 UTC",
        "total_used_percent": 6, "window_minutes": 10080, "reset_unix": 1792874445,
        "ordinary_usage_allowed": True, "legacy_by_limit_agree": True,
        "new_window_explicitly_user_authorized": True, "ceiling_total_percent": 90,
        "integration_reserve_retained": True, "automatic_further_reset_authorized": False,
    },
    "administrative_command": "python3 " + P + "freeze.py",
    "artifacts": [fp(path) for path in payloads],
}
assert len(manifest["artifacts"]) == 7
result = save("manifest.json", manifest)
print(json.dumps({"manifest": result, **output}, indent=2))
