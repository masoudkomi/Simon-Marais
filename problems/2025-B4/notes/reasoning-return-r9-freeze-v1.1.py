"""ADMINISTRATIVE one-shot text/JSON/fingerprint freeze; no mathematics.

Does not execute any constructor/reviewer program, enumerate mathematical
objects, test a theorem, access the network, or write outside this prefix.
Refuses every existing output and preserves all immutable input bytes.
"""
from pathlib import Path
from datetime import datetime, timezone
import difflib
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
BASE = Path("problems/2025-B4/notes")
PREFIX = "reasoning-return-r9-"
VERSION = "v1.1"

def digest(data):
    return hashlib.sha256(data).hexdigest()

def record(path):
    data = (ROOT / path).read_bytes()
    return {"path": str(path), "bytes": len(data), "sha256": digest(data)}

def checked(expected):
    actual = record(expected["path"])
    assert actual == expected, ("IMMUTABLE INPUT MISMATCH", expected, actual)
    return actual

def output(name, data):
    path = ROOT / BASE / name
    assert not path.exists(), ("REFUSE overwrite", str(path))
    if isinstance(data, (dict, list)):
        data = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    path.write_text(data, encoding="utf-8")

declared = []

def manifest(path, size, sha):
    r = checked({"path": path, "bytes": size, "sha256": sha})
    declared.append(r)
    obj = json.loads((ROOT / path).read_text())
    for item in obj["artifacts"]:
        declared.append(checked(item))
    return obj

original = manifest(
    "problems/2025-B4/notes/reasoning-return-r9-freeze-v1.json", 2790,
    "93eed518f1584c8e4f1a7cbe4d6229c9532caae4269d18cf0393c1f0e934aa8f")
r1 = manifest(
    "problems/2025-B4/reviews/reasoning-return-r9-review-1-manifest-v1.json", 3352,
    "8d8370530a3eb92359e1f5d693c1f385e0622b99078e57d7a1674cd7a183397a")
r2 = manifest(
    "problems/2025-B4/reviews/reasoning-return-r9-review-2-manifest-v1.json", 5385,
    "f41cf698bbbed3ae0a2ceabdec53ae7ffcfc12ec74e35d2dc6d6bee42279d657")

parent_record = checked({
    "path": "problems/2017-B4/notes/reasoning-value-return-r6-freeze-v1.1.json",
    "bytes": 2987,
    "sha256": "bd8d7cfcd6d81dd09432e2c8c445bd401c864f3d640fc7214336f034e9effa02"})
declared.append(parent_record)
parent = json.loads((ROOT / parent_record["path"]).read_text())
assert parent["own_paths_after_this_packet"] == 517
for item in parent["artifacts"]:
    if item["path"].endswith(("metadata-v1.1.json", "input-validation-v1.1.json")):
        declared.append(checked(item))

for item in [
    {"path": "problems/2025-B4/proofs/reviewed-reasoning-return-r8-v1.1.md",
     "bytes": 28730,
     "sha256": "f00a2b2816f128df54060fd800cba83d726abf07303c1cc7c92688a61557ca15"},
    {"path": "problems/2025-B4/proofs/reviewed-reasoning-return-r6-v1.1.md",
     "bytes": 28748,
     "sha256": "4e157819789da12d6f26e89929d88ec886d52947405d836fe3957ab8ee727d3a"},
]:
    declared.append(checked(item))
declared.append(record("AGENTS.md"))
interlude_record = record(BASE / "reasoning-return-r9-positive-live-v1.md")
declared.append(interlude_record)

deduplicated = {}
for item in declared:
    if item["path"] in deduplicated:
        assert deduplicated[item["path"]] == item
    deduplicated[item["path"]] = item
canonical = json.dumps([deduplicated[k] for k in sorted(deduplicated)],
                       sort_keys=True, separators=(",", ":")).encode()
summary = digest(canonical)

def text_file(stem, version):
    return (ROOT / BASE / f"{PREFIX}{stem}-{version}.md").read_text()

old_main = text_file("candidate", "v1")
new_main = text_file("candidate", VERSION)

def segment(text, start, end=None):
    tail = text.split(start, 1)[1]
    return tail if end is None else tail.split(end, 1)[0]

unchanged = {
    "complete_sections1_to3": segment(old_main, "## 1.", "## 4.")
        == segment(new_main, "## 1.", "## 4."),
    "complete_sections5_to6": segment(old_main, "## 5.", "## 7.")
        == segment(new_main, "## 5.", "## 7."),
    "complete_section8": segment(old_main, "## 8.")
        == segment(new_main, "## 8."),
    "complete_cofactor_paragraph": segment(old_main, "A safe replacement is elementary.", "## 5.")
        == segment(new_main, "A safe replacement is elementary.", "## 5."),
}
assert all(unchanged.values()), unchanged
obligations = text_file("obligations", VERSION)
ids = [int(x) for x in re.findall(r"^\| (\d+) \|", obligations, re.M)]
assert ids == list(range(1, 57)), ids

patches = []
for stem in ["candidate", "obligations", "sources", "failed-routes", "worklog"]:
    old_path = BASE / f"{PREFIX}{stem}-v1.md"
    new_path = BASE / f"{PREFIX}{stem}-{VERSION}.md"
    patches.extend(difflib.unified_diff(
        (ROOT / old_path).read_text().splitlines(keepends=True),
        (ROOT / new_path).read_text().splitlines(keepends=True),
        fromfile=str(old_path), tofile=str(new_path)))
output("reasoning-return-r9-diff-v1-to-v1.1.patch", "".join(patches))

now = datetime.now(timezone.utc).isoformat()
baseline = {
    "recorded_at_utc": now,
    "purpose": "Compact necessary immutable inputs for FULL R9 v1.1 author repair",
    "records": declared,
    "declared_occurrences": len(declared),
    "deduplicated_paths": len(deduplicated),
    "canonical_deduplicated_summary_sha256": summary,
    "historical_own_parent": parent_record,
    "historical_own_paths_bound_transitively": 517,
    "all517_historical_paths_recopied_or_rehashed": False,
    "both_review_manifests_and_ALL_their_artifact_bytes_verified": True,
    "all_original_constructor_artifact_bytes_verified": True,
    "separate_positive_interlude_NOT_a_repair_premise": interlude_record,
}
output(f"{PREFIX}baseline-{VERSION}.json", baseline)
metadata = {
    "status": "candidate proof - unverified, COMPLETE FULL version1.1 author repair",
    "constructor": "/root/review_2017_coarsening_r1",
    "requested_model": "gpt-6.1-sol",
    "requested_reasoning": "max",
    "independently_verified_effective_setting_readback": None,
    "shared_required_issue": ["R9R1-01", "R9R2-01"],
    "scope_note_made_explicit": "R9R2-N3:chosen generator only; no ideal-level all-generator exclusion",
    "original_whole_obligations": 48,
    "additional_affected_checks": 8,
    "full_obligations": 56,
    "unchanged_complete_mathematical_text_blocks": unchanged,
    "both_original_whole_initials_complete_before_B_findings_read": True,
    "both_complete_reports_all96_ledger_rows_issues_sources_read": True,
    "both_OTHER_affected_reaudits_required": True,
    "all_old_bytes_preserved_no_constructor_promotion": True,
    "separate_Runge_and_positive_interlude_NOT_premises": True,
    "no_mathcode_CAS_scan_native_child_download_or_new_primary_import": True,
    "no_new_Diophantine_exclusion_useful_unconditional_height_or_annual_claim": True,
    "latest_direct_budget": {
        "at_utc": "2026-10-18 00:48:00 UTC", "used_percent_TOTAL": 4,
        "reset": 1792874445, "ordinary_allowed": True,
        "explicit_new_window_user_authorization": True,
        "ceiling_TOTAL_with_reserve": 90, "automatic_further_reset_spending": False},
}
output(f"{PREFIX}metadata-{VERSION}.json", metadata)
for item in declared:
    checked(item)
output(f"{PREFIX}input-validation-{VERSION}.json", {
    "validated_at_utc": now,
    "declared_occurrences_verified": len(declared),
    "deduplicated_paths_verified": len(deduplicated),
    "canonical_deduplicated_summary_sha256": summary,
    "all_immutable_records_match_before_and_after_new_writes": True,
    "all56_obligation_IDs_present_in_order": True,
    "unchanged_mathematical_text_blocks": unchanged,
    "administrative_only_not_mathematical_testing": True,
})

artifact_names = [
    f"{PREFIX}candidate-{VERSION}.md", f"{PREFIX}obligations-{VERSION}.md",
    f"{PREFIX}sources-{VERSION}.md", f"{PREFIX}failed-routes-{VERSION}.md",
    f"{PREFIX}worklog-{VERSION}.md", f"{PREFIX}repair-ledger-{VERSION}.md",
    "reasoning-return-r9-diff-v1-to-v1.1.patch", f"{PREFIX}freeze-{VERSION}.py",
    f"{PREFIX}baseline-{VERSION}.json", f"{PREFIX}metadata-{VERSION}.json",
    f"{PREFIX}input-validation-{VERSION}.json",
]
artifacts = [record(BASE / name) for name in artifact_names]
freeze_name = f"{PREFIX}freeze-{VERSION}.json"
freeze = {
    "frozen_at_utc": now,
    "status": "COMPLETE FULL R9 v1.1 author repair - candidate proof unverified",
    "required_issues_addressed": ["R9R1-01", "R9R2-01"],
    "scope_note_explicit": "R9R2-N3 chosen-number nonlinearity only",
    "full_obligations": 56,
    "all_original_v1_and_both_whole_initials_preserved": True,
    "both_OTHER_affected_reaudits_required_before_coordinator_promotion": True,
    "immutable_own_parent": parent_record,
    "historical_own_paths_bound": 517,
    "separate_new_positive_interlude_paths": 1,
    "own_paths_after_interlude_and_this_packet": 530,
    "declared_occurrences_verified": len(declared),
    "deduplicated_paths_verified": len(deduplicated),
    "no_Diophantine_exclusion_annual_or_source_final_theorem_refutation_claim": True,
    "artifacts": artifacts,
}
output(freeze_name, freeze)
print(json.dumps({"main": artifacts[0], "freeze": record(BASE / freeze_name),
                  "whole_obligations": 56, "new_packet_files_including_freeze": 12,
                  "verified_occurrences": len(declared),
                  "verified_paths": len(deduplicated),
                  "historical_own_paths_after": 530}, indent=2))
