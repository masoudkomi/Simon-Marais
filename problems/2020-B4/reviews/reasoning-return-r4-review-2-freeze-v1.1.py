"""Administrative hashes, JSON and literal text comparison only."""
from pathlib import Path
import datetime
import difflib
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2020-B4/reviews/reasoning-return-r4-review-2-"
AUTHOR = "problems/2020-B4/notes/reasoning-return-r4-"


def record(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def read_json(path):
    return json.loads((ROOT / path).read_text())


def checked(expected):
    actual = record(expected["path"])
    for key in ("bytes", "sha256"):
        if key in expected:
            assert actual[key] == expected[key], (expected, actual)
    return actual


def unique_checked(records):
    output = {}
    for expected in records:
        actual = checked(expected)
        if actual["path"] in output:
            assert output[actual["path"]] == actual
        output[actual["path"]] = actual
    return list(output.values())


for suffix in ("input-validation-v1.1.json", "manifest-v1.1.json"):
    assert not (ROOT / (PREFIX + suffix)).exists(), "Never overwrite a frozen output"

target_path = AUTHOR + "candidate-v1.1.md"
checked({"path": target_path, "bytes": 22700,
         "sha256": "c8fc32fba5fb12a7af4e25b398b65cd9d148273c3bc6f055ea21394a66e01ce2"})
target_manifest_path = AUTHOR + "freeze-v1.1.json"
checked({"path": target_manifest_path,
         "sha256": "a76d1879815282839e87cf51b6a488279d213b11e1d5f00c8f216bbc44cc7b66"})
target_manifest = read_json(target_manifest_path)
assert len(target_manifest["artifacts"]) == 10
assert target_manifest["original_whole_obligations"] == 36
assert target_manifest["additional_repair_obligations"] == 8
target_records = unique_checked(target_manifest["artifacts"] + [record(target_manifest_path)])
old_manifest_path = AUTHOR + "freeze-v1.json"
old_manifest = read_json(old_manifest_path)
old_author = unique_checked(old_manifest["artifacts"] + [record(old_manifest_path)])
source = read_json(AUTHOR + "sources-v1.1.json")
old_source = read_json(AUTHOR + "sources-v1.json")
assert source["actual_primary_read_scopes"] == old_source["actual_primary_read_scopes"]
assert source["existing_related_native_cache_fingerprints"] == old_source["existing_related_native_cache_fingerprints"]
assert source["original_v1_direct_full_reads_preserved_unchanged"] == old_source["direct_full_local_document_or_register_reads"]
source_records = unique_checked(
    source["original_v1_direct_full_reads_preserved_unchanged"]
    + source["existing_related_native_cache_fingerprints"]
    + source["full_repair_reads"])

old_main = (ROOT / (AUTHOR + "candidate-v1.md")).read_text()
new_main = (ROOT / target_path).read_text()
def segment(text):
    return text.split("## R4A.", 1)[1].split("## R4E.", 1)[0]
assert segment(old_main) == segment(new_main)
def formulas(text):
    answer = {}
    for block in re.findall(r"\\\[(.*?)\\\]", text, re.S):
        tag = re.search(r"\\tag\{(E[1-5])\}", block)
        if tag:
            answer[tag.group(1)] = block
    return answer
assert set(formulas(old_main)) == {"E1", "E2", "E3", "E4", "E5"}
assert formulas(old_main) == formulas(new_main)
for stem in ("source-checks", "worklog"):
    assert (ROOT / (AUTHOR + stem + "-v1.1.md")).read_bytes().endswith(
        (ROOT / (AUTHOR + stem + "-v1.md")).read_bytes())

expected_diff = ""
for stem, extension in (("candidate", "md"), ("obligations", "md"),
                        ("source-checks", "md"), ("worklog", "md"),
                        ("sources", "json")):
    first = AUTHOR + stem + "-v1." + extension
    second = AUTHOR + stem + "-v1.1." + extension
    expected_diff += "".join(difflib.unified_diff(
        (ROOT / first).read_text().splitlines(keepends=True),
        (ROOT / second).read_text().splitlines(keepends=True),
        fromfile=first, tofile=second))
assert expected_diff == (ROOT / (AUTHOR + "repair-v1.1.diff")).read_text()

author_rows = (ROOT / (AUTHOR + "obligations-v1.1.md")).read_text()
review_rows = (ROOT / (PREFIX + "issues-v1.1.md")).read_text()
assert re.findall(r"^\|(R4-O\d{2})\|", author_rows, re.M) == [f"R4-O{i:02d}" for i in range(1, 37)]
assert re.findall(r"^\|(R4-R\d{2})\|", author_rows, re.M) == [f"R4-R{i:02d}" for i in range(1, 9)]
assert re.findall(r"^\| (R4-O\d{2}) \|", review_rows, re.M) == [f"R4-O{i:02d}" for i in range(1, 37)]
assert re.findall(r"^\| (R4-R\d{2}) \|", review_rows, re.M) == [f"R4-R{i:02d}" for i in range(1, 9)]

prior_path = "problems/2017-B4/notes/global-value-return-r1-manifest-v1.json"
checked({"path": prior_path, "bytes": 3534,
         "sha256": "61a261da6ae345a9255b8e9f5ea06cf697af2a1663c8bad4bc4f2010b5eeae53"})
prior = read_json(prior_path)
prior_validation = read_json("problems/2017-B4/notes/global-value-return-r1-input-validation-v1.json")
earlier = unique_checked(prior_validation["earlier_unique_records_preserved"]
                         + prior["artifacts"] + [record(prior_path)])
assert len(earlier) == 268

now = datetime.datetime.now(datetime.timezone.utc).isoformat()
validation = {
    "validated_at_utc": now, "administrative_integrity_only": True,
    "all_ten_author_artifacts_plus_freeze": target_records,
    "preserved_old_author_artifacts_and_freeze": old_author,
    "author_declared_source_and_full_repair_read_fingerprints": source_records,
    "all_36_original_and_8_repair_author_and_review_rows": True,
    "entire_R4A_R4D_segment_unchanged": True,
    "displayed_E1_E2_E3_E4_E5_formulas_identical": True,
    "exact_five_file_unified_diff_reconstructed_text_only": True,
    "historical_source_and_worklog_suffixes_unchanged": True,
    "earlier_unique_records_preserved": earlier,
    "earlier_unique_count": len(earlier),
    "new_targeted_peer_repair_findings_read_before_freeze": False,
    "older_repaired_R3_F1_F2_authorship_disclosed_not_independently_reaudited": True,
    "mathematical_code_CAS_scan_certificate_or_constructor_rerun": False,
    "shared_Git_spawning_contact_charge_bypass": False,
}
(ROOT / (PREFIX + "input-validation-v1.1.json")).write_text(json.dumps(validation, indent=2) + "\n")
artifacts = [record(PREFIX + suffix) for suffix in (
    "reaudit-v1.1.md", "issues-v1.1.md", "source-checks-v1.1.md",
    "freeze-v1.1.py", "input-validation-v1.1.json")]
manifest = {
    "frozen_at_utc": now,
    "status": "complete affected independent R2 reaudit; R4R2-01 resolved in v1.1; no remaining substantive objection in repaired scope; coordinator reconciliation pending",
    "reviewer": "/root/review_2017_coarsening_r1",
    "new_R4_or_repair_constructor": False,
    "old_repaired_R3_F1_F2_constructor": True,
    "not_new_independent_self_reaudit_of_old_input": True,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "target": record(target_path), "target_manifest": record(target_manifest_path),
    "issue": {"id": "R4R2-01", "disposition": "resolved in complete versioned replacement",
              "automatic_final_minus_one": True,
              "sufficient_interior_list_proved": True,
              "reduced_matrix_uses_known_actual_zero_count": True,
              "full_iff_and_unchanged_R4A_R4D_retained": True},
    "all_original_plus_repair_obligations_disposed": 44,
    "open_substantive_repair_issues": 0,
    "new_targeted_peer_repair_findings_read_before_freeze": False,
    "official_full_classification_unbounded_system_solution_cutoff_or_novelty": False,
    "earlier_unique_own_paths_verified_unchanged": len(earlier),
    "last_direct_weekly_telemetry": {
        "at_utc": "2026-10-17 12:58:40 UTC", "total_used_percent": 39,
        "window_minutes": 10080, "reset_unix": 1792745187,
        "total_ceiling_percent": 90, "integration_reserve": True},
    "administrative_command": "/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 " + PREFIX + "freeze-v1.1.py",
    "artifacts": artifacts,
}
manifest_path = PREFIX + "manifest-v1.1.json"
(ROOT / manifest_path).write_text(json.dumps(manifest, indent=2) + "\n")
print(json.dumps({"manifest": record(manifest_path), "artifacts": artifacts,
                  "author_records_checked": len(target_records),
                  "old_own_paths_unchanged": len(earlier),
                  "all_obligations": 44, "open_substantive_issues": 0}, indent=2))

