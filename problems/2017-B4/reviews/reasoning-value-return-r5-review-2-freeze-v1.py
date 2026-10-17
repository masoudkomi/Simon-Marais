"""CREATE-NEW administrative WHOLE-review freeze, no mathematical code.

Default is read-only preflight. --freeze creates only the assigned review
metadata. No constructor program, PL algorithm, scan or CAS is executed.
Compact frozen parents bind historical inventories without recopying them.
"""
from pathlib import Path
import datetime
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
OWN = "problems/2017-B4/reviews/reasoning-value-return-r5-review-2-"
AUTHOR = "problems/2017-B4/notes/reasoning-value-return-r5-"
PEER = "problems/2017-B4/reviews/reasoning-value-return-r5-review-1-"
STAMP = datetime.datetime.now(datetime.timezone.utc).isoformat()
OCCURRENCES = []
UNIQUE = {}


def guard(path):
    assert not path.startswith(PEER), "NEW root R5 review material forbidden"
    assert "coordinator-profile-closure-lead-v1" not in path, "Separate root lead forbidden"


def record(path):
    guard(path)
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def check(row, times=1):
    expected = {key: row[key] for key in ["path", "bytes", "sha256"]}
    actual = record(expected["path"])
    assert actual == expected, expected["path"]
    old = UNIQUE.setdefault(expected["path"], expected)
    assert old == expected
    for unused in range(times):
        OCCURRENCES.append(expected)
    return actual


def read_json(path):
    guard(path)
    return json.loads((ROOT / path).read_text())


def digest(rows):
    value = sorted(rows, key=lambda row: row["path"])
    data = json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":")).encode()
    return hashlib.sha256(data).hexdigest()


def declared(value):
    if isinstance(value, dict):
        if all(key in value for key in ["path", "bytes", "sha256"]):
            yield {key: value[key] for key in ["path", "bytes", "sha256"]}
        for child in value.values():
            yield from declared(child)
    elif isinstance(value, list):
        for child in value:
            yield from declared(child)


def write_new(suffix, value):
    path = OWN + suffix
    with (ROOT / path).open("x") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    return record(path)


constructor_row = check({
    "path": AUTHOR + "freeze-v1.json", "bytes": 3146,
    "sha256": "31b1789d41b1d492ef9f0d2235050025bb341ca70c8eb8d0c66765e63e43fed1"})
constructor = read_json(constructor_row["path"])
assert len(constructor["artifacts"]) == 9
assert constructor["whole_obligations"] == 40
assert constructor["artifacts"][0] == {
    "path": AUTHOR + "candidate-v1.md", "bytes": 30791,
    "sha256": "f0313ffa047c8c0ac7664192a01936f842b300f22168a9b929c8d4d39c41879e"}
for row in constructor["artifacts"]:
    check(row)

baseline_path = AUTHOR + "baseline-v1.json"
base = read_json(baseline_path)
assert base["record_occurrences"] == 33
assert base["deduplicated_paths"] == len(base["records"]) == 32
assert sum(row["occurrences"] for row in base["records"]) == 33
for row in base["records"]:
    check(row, row["occurrences"])
base_clean = [{key: row[key] for key in ["path", "bytes", "sha256"]}
              for row in base["records"]]
assert len({row["path"] for row in base_clean}) == 32
base_lookup = {row["path"]: row for row in base_clean}
author_validation = read_json(AUTHOR + "input-validation-v1.json")
assert author_validation["baseline"] == record(baseline_path)
assert author_validation["record_occurrences"] == 33
assert author_validation["deduplicated_paths"] == 32

parent_row = check(base["compact_immutable_parent"])
assert parent_row == constructor["compact_immutable_parent_manifest"]
parent_body = read_json(parent_row["path"])
assert len(parent_body["artifacts"]) == 9
for row in parent_body["artifacts"]:
    assert row == base_lookup[row["path"]]
    check(row)
assert base["all_earlier_own_paths_bound_compactly"] == 425

ec_path = "problems/2017-B4/reviews/reasoning-value-return-r4-acceptance.json"
ec_rows = list(declared(read_json(ec_path)))
assert len(ec_rows) == 9
for row in ec_rows:
    assert row == base_lookup[row["path"]]
    check(row)
assert read_json(ec_path)["upper_R_discharged"] is False

old_review_row = check({
    "path": "problems/2024-B4/reviews/reasoning-sector3-return-r1-review-2-manifest-v1.json",
    "bytes": 3633,
    "sha256": "d625576c8e3a317db01d2b823db2ed29f21948d05279151bc0d58de3094e0f3d"})
old_review = read_json(old_review_row["path"])
assert len(old_review["artifacts"]) == 8
for row in old_review["artifacts"]:
    check(row)

# Freshly read old acceptance text is additional scope context, not a new
# mathematical premise or an expanded historical inventory.
fd_scope_row = check(record("problems/2017-B4/reviews/fixedD-structural-acceptance.md"))
assert base_lookup["AGENTS.md"]["sha256"] == "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"

author_obs = re.findall(r"^\| GR-(\d\d) \|", (ROOT / (AUTHOR + "obligations-v1.md")).read_text(), re.M)
assert author_obs == [f"{i:02d}" for i in range(1,41)]
ledger = (ROOT / (OWN + "issues-v1.md")).read_text()
checks = re.findall(r"^\| R2-(\d\d) \|", ledger, re.M)
assert checks == [f"{i:02d}" for i in range(1,57)]
covered = set()
for line in ledger.splitlines():
    if line.startswith("| R2-"):
        covered.update(re.findall(r"GR-(\d\d)", line.split("|")[2]))
assert covered == set(author_obs)
assert "ENTIRE" in (ROOT / (OWN + "initial-v1.md")).read_text()
for suffix in ["sources-v1.json", "input-validation-v1.json", "freeze-output-v1.json", "manifest-v1.json"]:
    assert not (ROOT / (OWN + suffix)).exists(), "CREATE-NEW only: " + suffix

summary = {
    "declared_fingerprint_occurrences_verified": len(OCCURRENCES),
    "unique_paths_fingerprinted": len(UNIQUE),
    "canonical_deduplicated_summary_sha256": digest(list(UNIQUE.values())),
    "historical_inventories_bound_not_duplicated": True,
    "constructor_baseline_occurrences_verified": 33,
    "constructor_baseline_unique_paths_verified": 32,
}
if "--freeze" not in sys.argv:
    print(json.dumps({"preflight": "complete", "checks": len(checks),
                      "all_author_obligations": len(covered), "summary": summary}))
    raise SystemExit(0)

telemetry = {
    "at_utc": "2026-10-17 20:02:23 UTC", "total_used_percent": 62,
    "window_minutes": 10080, "reset_unix": 1792745187,
    "ordinary_usage_allowed": True, "total_ceiling_percent": 90,
    "integration_reserve": True,
}
sources_record = write_new("sources-v1.json", {
    "recorded_at_utc": STAMP,
    "actual_read_scope": "Complete source-checks-v1.md; not a claim of fresh whole audits of old own work",
    "primary_analytic": {
        "title": "Leon Simon, Introduction to Geometric Measure Theory,2017/2018",
        "url": "https://math.stanford.edu/~lms/ntu-gmt-text.pdf",
        "read_scope": "Chapter2 Theorems1.2,1.4,3.3 and relevant proofs,printed44--46,57--60",
        "application": "scalar extension/Rademacher; area formula on open planar domain for measurable zero-Jacobian set",
        "downloaded_byte_sha256": None,
    },
    "primary_context": [
        {"url": "https://lipn.fr/~fernique/info/hammingflip.pdf",
         "read_scope": "actual title and COMPLETEsection2,printed4--5; unit-generator edge-to-edge/ribbon definitions only",
         "full_later_proof_read": False, "downloaded_byte_sha256": None},
        {"url": "https://lipn.univ-paris13.fr/~fernique/qc/structure_3.pdf",
         "read_scope": "text PDFpages17--25,multigrid/pseudogrid context; no imported straightening or diagram theorem",
         "downloaded_byte_sha256": None},
    ],
    "official": [
        {"url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-2_1.pdf",
         "read_scope": "actual B4,PDFpage2", "existing_cache": base_lookup[".cache/official/2017-paper_b.pdf"]},
        {"url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-solutions-preliminary_1.pdf",
         "read_scope": "B4/comments,PDFpage12", "existing_cache": base_lookup[".cache/official/2017-solutions.pdf"]},
    ],
    "old_accepted_actual_read_scopes": [
        {"path": "problems/2017-B4/proofs/reviewed-fixedD-structural-v1.2.md", "scope": "FULLsections1--3,lines1--185; old necessary geometry/dictionary and actual convexity counterexample"},
        {"path": fd_scope_row["path"], "scope": "FULL acceptance text; FD2-01 preservation; later envelope unused", "fingerprint": fd_scope_row},
        {"path": "problems/2017-B4/proofs/reviewed-clean-strata-v1.1.md", "scope": "FULL accepted body FL1/CL1/OB1; no arbitrary-decoration inference"},
        {"path": "problems/2017-B4/proofs/reviewed-global-value-return-v1.1.md", "scope": "throughline52,accepted scope/setup only; not a fresh whole proof audit"},
        {"path": "problems/2017-B4/proofs/reviewed-global-value-return-r2-v1.1.md", "scope": "throughline70 and COMPLETEsmall fiber lines305--325"},
        {"path": "problems/2017-B4/proofs/reviewed-reasoning-value-return-r3-v1.1.md", "scope": "throughline60,accepted own HC scope/setup only"},
        {"path": "problems/2017-B4/proofs/reviewed-reasoning-value-return-r4-v1.1.md", "scope": "throughline54,accepted own EC scope/setup; FULL acceptance.md/json/integrity"},
    ],
    "old_roles": "A older strict-local/HC/EC constructor and local/global reviewer; no NEW R5 construction role",
    "no_new_root_R5_review_or_separate_closure_lead_opened": True,
    "no_new_download_render_cache_write_or_stalled_wait": True,
    "no_math_code_CAS_scan_author_rerun_or_proposed_algorithm_execution": True,
})
validation_record = write_new("input-validation-v1.json", {
    "checked_at_utc": STAMP, "administrative_only_not_mathematical_evidence": True,
    "constructor_metadata": constructor_row,
    "constructor_9_artifacts_verified": True,
    "constructor_baseline_metadata": record(baseline_path),
    "constructor_baseline_canonical_deduplicated_sha256": digest(base_clean),
    "constructor_current_declared_occurrences": 33,
    "constructor_current_unique_paths": 32,
    "constructor_immediate_parent_metadata": parent_row,
    "constructor_immediate_parent_9_artifacts_verified": True,
    "constructor_earlier_own_paths_bound_transitively": 425,
    "old_EC_acceptance_metadata": record(ec_path),
    "old_EC_9_declared_fingerprints_verified": True,
    "old_own_review_metadata": old_review_row,
    "old_own_review_8_payloads_verified": True,
    "old_own_review_compact_summary": old_review["compact_input_summary"],
    "all_56_ledger_checks": checks,
    "all_40_author_obligations": sorted(covered),
    "compact_input_summary": summary,
    "new_root_R5_peer_material_or_closure_lead_opened_even_for_metadata": False,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "independently_verified_effective_settings": None,
    "authoritative_account_weekly": telemetry,
    "source_metadata": sources_record,
})
report = record(OWN + "initial-v1.md")
output_record = write_new("freeze-output-v1.json", {
    "COMPLETE": True, "frozen_at_utc": STAMP,
    "manifest_path": OWN + "manifest-v1.json", "report": report,
    "checks": 56, "all_author_obligations": 40,
    "substantive_open_issues": 0, "required_author_repairs": 0,
    "compact_input_summary": summary, "mathematical_program": False,
})
suffixes = ["initial-v1.md", "issues-v1.md", "source-checks-v1.md", "worklog-v1.md",
            "freeze-v1.py", "sources-v1.json", "input-validation-v1.json", "freeze-output-v1.json"]
artifacts = [record(OWN + suffix) for suffix in suffixes]
assert artifacts[-2] == validation_record and artifacts[-1] == output_record
for row in UNIQUE.values():
    assert record(row["path"]) == row, row["path"]
manifest_row = write_new("manifest-v1.json", {
    "frozen_at_utc": STAMP,
    "status": "COMPLETE initially blind NONCONSTRUCTOR WHOLE R2 initial; recommendation only",
    "reviewer": "/root/review_2021_reasoning_j15_r2",
    "new_constructor_excluded": "/root/review_2017_coarsening_r1",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "independently_verified_effective_settings": None,
    "whole_checks": 56, "all_author_obligations": 40,
    "recommendation": "No substantive defect found in exact geometric GR1--GR4; other whole review and root reconciliation required",
    "substantive_open_issues": 0, "required_author_repairs": 0, "advisories": [],
    "complete_initial_before_ANY_new_root_R5_report_ledger_source_manifest_or_finding_opened": True,
    "identity_only_peer_completion_notification_not_a_finding": True,
    "older_strict_local_HC_EC_authorship_and_other_reviews_disclosed": True,
    "new_R5_constructor_or_contributor": False,
    "root_separate_profile_closure_lead_unread_unused": True,
    "no_exponential_mass_entropy_upper_R_numeric_value_two_sided_computability_annual_or_novelty_claim": True,
    "no_math_code_CAS_scan_author_rerun_proposed_algorithm_execution_or_native_child": True,
    "no_old_shared_cache_Git_edits_spawn_contact_charge_bypass": True,
    "compact_input_summary": summary,
    "authoritative_account_weekly": telemetry,
    "administrative_command": ".venv/bin/python " + OWN + "freeze-v1.py --freeze",
    "artifacts": artifacts,
})
print(json.dumps({"COMPLETE": True, "manifest": manifest_row, "report": report,
                  "artifacts": len(artifacts), "summary": summary,
                  "mathematical_program": False}))
