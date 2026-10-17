"""CREATE-NEW administrative freeze. No mathematical evaluation or replay.

Only SHA/JSON/check labels and compact old metadata are validated.
Default: read-only preflight. --freeze writes the assigned review prefix.
"""
from pathlib import Path
import datetime
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
OWN = "problems/2019-B4/reviews/coordinator-retained-core-gap-r1-review-1-"
AUTHOR = "problems/2019-B4/notes/coordinator-retained-core-gap-r1-"
PEER = "problems/2019-B4/reviews/coordinator-retained-core-gap-r1-review-2-"
YEAR = "problems/2019-B4/"
STAMP = datetime.datetime.now(datetime.timezone.utc).isoformat()
OCCURRENCES = []
UNIQUE = {}


def record(path):
    assert not path.startswith(PEER), "NEW C retained-core peer material forbidden"
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def check(row):
    expected = {key: row[key] for key in ["path", "bytes", "sha256"]}
    actual = record(expected["path"])
    assert actual == expected, expected["path"]
    old = UNIQUE.setdefault(expected["path"], expected)
    assert old == expected
    OCCURRENCES.append(expected)
    return actual


def read_json(path):
    assert not path.startswith(PEER)
    return json.loads((ROOT / path).read_text())


def declared(value):
    if isinstance(value, dict):
        if all(key in value for key in ["path", "bytes", "sha256"]):
            yield {key: value[key] for key in ["path", "bytes", "sha256"]}
        for child in value.values():
            yield from declared(child)
    elif isinstance(value, list):
        for child in value:
            yield from declared(child)


def digest(rows):
    value = sorted(rows, key=lambda row: row["path"])
    data = json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":")).encode()
    return hashlib.sha256(data).hexdigest()


def write_new(suffix, value):
    path = OWN + suffix
    with (ROOT / path).open("x") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    return record(path)


constructor_row = check({
    "path": AUTHOR + "freeze-v1.json", "bytes": 1965,
    "sha256": "d2ea714f15cc653c044943a0485bfd0908fa0279b350c07a42a811ff9b4f0681"})
constructor = read_json(constructor_row["path"])
assert constructor["whole_author_obligations"] == 16
assert len(constructor["artifacts"]) == 5
assert constructor["artifacts"][0] == {
    "path": AUTHOR + "candidate-v1.md", "bytes": 6152,
    "sha256": "9bea48691719c0384e0a027131e6db1fad83ddd0572e8ae59578f72d71431b42"}
for row in constructor["artifacts"]:
    check(row)
inputs_path = AUTHOR + "inputs-v1.json"
inputs = read_json(inputs_path)
assert inputs["current_record_occurrences_verified"] == 19
assert inputs["current_unique_paths_verified"] == len(inputs["records"]) == 19
input_lookup = {row["path"]: row for row in inputs["records"]}
assert len(input_lookup) == 19
for row in inputs["records"]:
    check(row)

parent_row = check(inputs["immutable_parent_acceptance"])
assert parent_row == constructor["immutable_accepted_parent"]
assert parent_row == {
    "path": YEAR + "reviews/coordinator-cap-gap-r1-acceptance.json",
    "bytes": 3048,
    "sha256": "81e32cb11a1eb61330534c179097958f31701755eba0804624a5678ae08a569a"}
parent = read_json(parent_row["path"])
assert parent["status"] == "proved, independently reviewed scoped partial result"
parent_rows = list(declared(parent))
assert len(parent_rows) == 11
for row in parent_rows:
    assert row == input_lookup[row["path"]]
    check(row)

# Exact old accepted maps newly read as source authority: verify their
# declared hashes, but bind the inventories by metadata rather than copy them.
second_path = YEAR + "reviews/secondpass-acceptance.json"
second_row = check(record(second_path))
second = read_json(second_path)
assert second["initial_audits_blind"] and second["both_full_reconstructions"]
assert len(second["artifacts"]) == 14
for relative_path, old_sha in second["artifacts"].items():
    actual = record(YEAR + relative_path)
    check({"path": actual["path"], "bytes": actual["bytes"], "sha256": old_sha})
third_path = YEAR + "reviews/thirdpass-acceptance.json"
third_row = check(record(third_path))
third = read_json(third_path)
assert third["two_independent_nonconstructor_initially_blind_reviews"] is True
third_rows = list(declared(third))
assert len(third_rows) == 7
for row in third_rows:
    check(row)

additional_scope_paths = [
    YEAR + "proof.md",
    YEAR + "reviews/thirdpass-acceptance.md",
    YEAR + "reviews/moment-tail-acceptance.md",
    YEAR + "notes/reasoning-return-r7-candidate-v1.md",
]
additional_scope_rows = [check(record(path)) for path in additional_scope_paths]
old_review_row = check({
    "path": "problems/2017-B4/reviews/reasoning-value-return-r5-review-2-manifest-v1.json",
    "bytes": 3805,
    "sha256": "11741a6e3049d5dafa6403ec18d109b711bef40996662eb78932db6877842f79"})
old_review = read_json(old_review_row["path"])
assert len(old_review["artifacts"]) == 8
for row in old_review["artifacts"]:
    check(row)
assert input_lookup["AGENTS.md"]["sha256"] == "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"

author_obs = re.findall(r"^\|RC-(\d\d)\|", (ROOT / (AUTHOR + "obligations-v1.md")).read_text(), re.M)
assert author_obs == [f"{i:02d}" for i in range(1,17)]
ledger = (ROOT / (OWN + "issues-v1.md")).read_text()
checks = re.findall(r"^\| R1-(\d\d) \|", ledger, re.M)
assert checks == [f"{i:02d}" for i in range(1,29)]
covered = set()
for line in ledger.splitlines():
    if line.startswith("| R1-"):
        covered.update(re.findall(r"RC-(\d\d)", line.split("|")[2]))
assert covered == set(author_obs)
for suffix in ["sources-v1.json", "input-validation-v1.json", "freeze-output-v1.json", "manifest-v1.json"]:
    assert not (ROOT / (OWN + suffix)).exists(), "CREATE-NEW only: " + suffix

summary = {
    "declared_fingerprint_occurrences_verified": len(OCCURRENCES),
    "unique_paths_fingerprinted": len(UNIQUE),
    "canonical_deduplicated_summary_sha256": digest(list(UNIQUE.values())),
    "historical_inventories_bound_not_duplicated": True,
    "constructor_current19_records_verified": True,
}
if "--freeze" not in sys.argv:
    print(json.dumps({"preflight": "complete", "checks": len(checks),
                      "all_author_obligations": len(covered), "summary": summary}))
    raise SystemExit(0)

telemetry = {
    "at_utc": "2026-10-17 20:09:51 UTC", "total_used_percent": 62,
    "window_minutes": 10080, "reset_unix": 1792745187,
    "ordinary_usage_allowed": True, "total_ceiling_percent": 90,
    "integration_reserve": True,
}
sources_record = write_new("sources-v1.json", {
    "recorded_at_utc": STAMP,
    "read_scope": "COMPLETE source-checks-v1.md; old accepted authority distinct from NEW C retained-core peer material",
    "official": {
        "url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-paper-b_1.pdf",
        "actual_read_scope": "B4 definitions and(b),PDFpage2; no preliminary proof research",
        "browser_text_only_no_downloaded_byte_sha256": None,
    },
    "complete_accepted_bodies_read": [
        YEAR + "proofs/reviewed-cap-gap-v1.1.md",
        YEAR + "proofs/reviewed-thirdpass-v1.1.md",
        YEAR + "proofs/reviewed-moment-tail-v1.1.md",
        YEAR + "proofs/reviewed-secondpass-v1.1.md",
        YEAR + "notes/secondpass-canonical-renewal.md",
    ],
    "other_exact_reads": [
        {"path": YEAR + "proof.md", "scope": "lines1--84,actual marked/original common-root bridge"},
        {"path": YEAR + "reviews/coordinator-cap-gap-r1-review-1-initial-v1.md", "scope": "FULLsection5,lines208--254,attributed OLD hand method; AFTER independent new arithmetic"},
        {"path": YEAR + "notes/reasoning-return-r7-candidate-v1.md", "scope": "header/setup lines1--54,solely old authorship-role clarification; not RC premise"},
    ],
    "operative_acceptance_scopes_read": [
        YEAR + "reviews/coordinator-cap-gap-r1-acceptance.md",
        YEAR + "reviews/coordinator-cap-gap-r1-acceptance.json",
        YEAR + "reviews/coordinator-cap-gap-r1-acceptance-integrity.json",
        YEAR + "reviews/thirdpass-acceptance.md",
        YEAR + "reviews/thirdpass-acceptance.json",
        YEAR + "reviews/moment-tail-acceptance.md",
        YEAR + "reviews/secondpass-acceptance.json",
    ],
    "old_cap_rows_lower_and_sign_certificates_not_rerun_or_falsely_reaudited": True,
    "new_rational_sign_reconstructed_entirely_by_hand": True,
    "new_external_theorem_or_unread_program_as_premise": False,
    "old_A_2019_R7_authorship_and_other_reviews_disclosed": True,
    "new_RC_construction_contribution": False,
    "new_C_RC_peer_material_read_before_ENTIREfreeze": False,
    "no_new_download_cache_mutation_stalled_wait_contact_charge_or_bypass": True,
})
validation_record = write_new("input-validation-v1.json", {
    "checked_at_utc": STAMP, "administrative_only_not_mathematical_evidence": True,
    "constructor_metadata": constructor_row,
    "constructor_5_artifacts_verified": True,
    "constructor_inputs_metadata": record(inputs_path),
    "constructor19_current_records_verified": True,
    "constructor_current_canonical_sha256": digest(inputs["records"]),
    "accepted_CG_parent_metadata": parent_row,
    "accepted_CG11_direct_declared_fingerprints_verified": True,
    "accepted_CG_historical_summary_bound_not_freshly_expanded": {
        "occurrences": parent["record_occurrences_verified"],
        "unique_paths": parent["unique_paths_verified"],
    },
    "old_secondpass_acceptance_metadata": second_row,
    "old_secondpass14_declared_hashes_verified": True,
    "old_thirdpass_acceptance_metadata": third_row,
    "old_thirdpass7_declared_fingerprints_verified": True,
    "additional_accepted_scope_fingerprints": additional_scope_rows,
    "previous_own_review_metadata": old_review_row,
    "previous_own_review8_payloads_verified": True,
    "previous_own_review_compact_summary": old_review["compact_input_summary"],
    "all28_ledger_checks": checks, "all16_author_obligations": sorted(covered),
    "compact_input_summary": summary,
    "new_C_RC_peer_material_read_even_for_metadata": False,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "independently_verified_effective_settings": None,
    "authoritative_account_weekly": telemetry, "source_metadata": sources_record,
})
report = record(OWN + "initial-v1.md")
output_record = write_new("freeze-output-v1.json", {
    "COMPLETE": True, "frozen_at_utc": STAMP,
    "manifest_path": OWN + "manifest-v1.json", "report": report,
    "checks": 28, "all_author_obligations": 16,
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
    "status": "COMPLETE initially blind NONCONSTRUCTOR WHOLE R1 initial; recommendation only",
    "reviewer": "/root/review_2021_reasoning_j15_r2",
    "new_constructor_excluded": "/root",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "independently_verified_effective_settings": None,
    "whole_checks": 28, "all_author_obligations": 16,
    "recommendation": "No substantive defect found in exact retained-core gap and proposed strict lambda<1.834843; other whole review/root reconciliation required",
    "substantive_open_issues": 0, "required_author_repairs": 0, "advisories": [],
    "complete_initial_before_ANY_new_C_RC_report_ledger_source_manifest_or_finding": True,
    "old_A_2019_R7_authorship_and_other_reviews_disclosed": True,
    "new_RC_constructor_or_contributor": False,
    "old_accepted_CG_hand_method_read_after_independent_new_arithmetic": True,
    "all_state_cap_bound_not_merely_canonical_rate_bound": True,
    "no_exact_rate_renewal_regime_matching_scale_annual_or_novelty_claim": True,
    "no_math_code_CAS_scan_sign_child_author_rerun_or_certificate_replay": True,
    "no_old_shared_cache_Git_edits_spawn_contact_charge_bypass": True,
    "compact_input_summary": summary,
    "authoritative_account_weekly": telemetry,
    "administrative_command": ".venv/bin/python " + OWN + "freeze-v1.py --freeze",
    "artifacts": artifacts,
})
print(json.dumps({"COMPLETE": True, "manifest": manifest_row, "report": report,
                  "artifacts": len(artifacts), "summary": summary,
                  "mathematical_program": False}))
