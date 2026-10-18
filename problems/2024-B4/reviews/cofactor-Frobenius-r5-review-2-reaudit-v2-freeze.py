#!/usr/bin/env python3
"""NEW affected-review metadata only; no mathematics or author-code execution."""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2024-B4/reviews/cofactor-Frobenius-r5-review-2-reaudit-v2-"
AUTHOR = "problems/2024-B4/notes/cofactor-Frobenius-r5-"
REPAIR = AUTHOR + "repair-freeze-v2.json"
PARENT = "problems/2025-B4/notes/reasoning-branch-return-r4-freeze-v1.json"
ORIGINAL_OWN = "problems/2024-B4/reviews/cofactor-Frobenius-r5-review-2-manifest-v1.json"
EXPECTED_REPAIR = {
    "path": REPAIR, "bytes": 8397,
    "sha256": "aaa1da5e9143787046b0286dc7de75f04107d8ec209deadda65d53b5e1cc9885",
}
EXPECTED_PARENT = {
    "path": PARENT, "bytes": 7391,
    "sha256": "0574b5b9231729c79db541fc26ae01e7ea33a578cd1379cfae71060aabcc3633",
}
HEADER = """> Author repair v2, 18 October2026 UTC: candidate proof - unverified
> pending BOTH affected reaudits. Corrects the odd-s residue from2 to1
> modulo3, and assigns the s3 failure to the off-diagonal coprimality
> step; its diagonal exclusion still holds. R1 N1/N2 and R2 N1 supplied
> these corrective observations after BOTH entire blind audits froze.
> No theorem/domain/threshold is strengthened. All original bytes remain.

"""
MAIN_REPLACEMENTS = [
    ["Since s is odd,2^s-1 is2 modulo3. The order3 cannot divide Q-1;",
     "Since s is odd,2^s is2 modulo3, so2^s-1 is1 modulo3. The order3 cannot divide Q-1;"],
    ["need not have length1 or s; for s3 a permutation can have order3\nand the diagonal cube-root obstruction changes. No such case is\nsilently included.",
     "need not have length1 or s; for s3 a permutation can have order3\nand the off-diagonal coprimality step fails. The diagonal cube-root\nexclusion still holds at s3, since3 does not divide7. No such case is\nsilently included."],
]
LOG_REPLACEMENT = [
    "   permutation argument and diagonal cube-root obstruction change.",
    "   permutation argument fails; the diagonal cube-root exclusion still holds.",
]
PAYLOAD_SUFFIXES = (
    "report.md", "ledger.md", "issues.md", "source-checks.md", "sources.json",
    "worklog.md", "freeze.py", "baseline.json", "input-validation.json",
)
BASELINE = PREFIX + "baseline.json"
VALIDATION = PREFIX + "input-validation.json"
MANIFEST = PREFIX + "manifest.json"


def now():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    assert isinstance(path, str) and not path.startswith("/")
    assert ".." not in Path(path).parts
    assert not path.startswith("problems/2024-B4/reviews/cofactor-Frobenius-r5-review-1-reaudit-"), path
    assert not path.startswith("problems/2020-B4/reviews/reasoning-Todd-return-r12-"), path
    assert not path.startswith("problems/2025-B4/reviews/reasoning-branch-return-r4-"), path
    return (ROOT / path).read_bytes()


def obj(path):
    return json.loads(raw(path))


def fp(path):
    data = raw(path)
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def check(record):
    expected = {k: record[k] for k in ("path", "bytes", "sha256")}
    assert fp(record["path"]) == expected, record["path"]
    return expected


def canonical_sha(value):
    data = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(data.encode()).hexdigest()


def put(path, data):
    assert path in (BASELINE, VALIDATION, MANIFEST)
    assert path.startswith(PREFIX)
    with (ROOT / path).open("x", encoding="utf-8") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def exact_diff():
    expected = raw(AUTHOR + "candidate-v1.md").decode()
    for old, new in MAIN_REPLACEMENTS:
        assert expected.count(old) == 1
        expected = expected.replace(old, new)
    assert raw(AUTHOR + "candidate-v2.md").decode() == HEADER + expected
    expected = raw(AUTHOR + "failures-worklog-v1.md").decode()
    old, new = LOG_REPLACEMENT
    assert expected.count(old) == 1
    assert raw(AUTHOR + "failures-worklog-v2.md").decode() == HEADER + expected.replace(old, new)
    repair = obj(REPAIR)
    assert repair["exact_replacements"] == {"main": MAIN_REPLACEMENTS, "log": LOG_REPLACEMENT}


def author_records():
    check(EXPECTED_REPAIR)
    repair = obj(REPAIR)
    assert len(repair["old_current_guards"]) == repair["old_guard_paths"] == 30
    assert len(repair["artifacts"]) == 4
    records = [EXPECTED_REPAIR] + repair["old_current_guards"] + repair["artifacts"]
    for record in records:
        check(record)
    assert len({r["path"] for r in records}) == 35
    assert fp(AUTHOR + "candidate-v2.md") == {
        "path": AUTHOR + "candidate-v2.md", "bytes": 13006,
        "sha256": "329b975a7f8fe7456f9794a2170dc443396fb1a2b0143cc61ac9ddd027beb47e"}
    exact_diff()
    return records


def accepted_records():
    old = obj(ORIGINAL_OWN)
    old_baseline = obj(old["compact_necessary_baseline"]["path"])
    check(old["compact_necessary_baseline"])
    old_fps = {r["path"]: r for r in old_baseline["protected_rows"]}
    records, bindings = [], []
    for binding in old["accepted_operative_bindings"]:
        for key in ("authority", "accepted_body", "exact_candidate_suffix"):
            check(binding[key])
            records.append({k: binding[key][k] for k in ("path", "bytes", "sha256")})
        authority_path = binding["authority"]["path"]
        authority_md = authority_path[:-5] + ".md"
        records.append(check(old_fps[authority_md]))
        current = obj(authority_path)
        assert current["status"].startswith("proved, independently reviewed")
        assert current["accepted_copy"] == binding["accepted_body"]
        assert current["candidate"] == binding["exact_candidate_suffix"]
        assert raw(current["accepted_copy"]["path"]).endswith(raw(current["candidate"]["path"]))
        bindings.append({
            "authority_json": authority_path, "authority_md": authority_md,
            "accepted_body": current["accepted_copy"]["path"],
            "exact_candidate_suffix": current["candidate"]["path"],
            "historical_occurrences_bound_not_replayed": binding["historical_occurrences_bound_not_recopied_or_replayed"],
            "historical_paths_bound_not_replayed": binding["historical_paths_bound_not_recopied_or_replayed"],
        })
    assert len(records) == 8
    return records, bindings


def parent_records():
    check(EXPECTED_PARENT)
    parent = obj(PARENT)
    assert parent["older_plus_new_own_paths_bound_transitively"] == 698
    assert len(parent["artifacts"]) == 10
    for record in parent["artifacts"]:
        check(record)
    return [EXPECTED_PARENT] + parent["artifacts"]


def current_records():
    records = author_records() + parent_records()
    accepted, bindings = accepted_records()
    records += accepted + [fp("AGENTS.md"), fp("problems/2024-B4/statement.md")]
    assert len(records) == len({r["path"] for r in records}) == 56
    return sorted(records, key=lambda r: r["path"]), bindings


def baseline():
    records, bindings = current_records()
    value = {
        "created_at_utc": now(),
        "purpose": "NEW metadata-only affected-review preservation and exact-diff baseline",
        "snapshot_stage": "after complete affected hand reconstruction, before immutable whole freeze",
        "protected_fingerprint_occurrences": 56,
        "protected_unique_paths": 56,
        "canonical_protected_summary_sha256": canonical_sha(records),
        "protected_fingerprints": records,
        "five_file_author_repair_including_30_original_guards_checked": True,
        "exact_main_header_two_sentences_and_log_header_one_sentence_checked": True,
        "accepted_operative_bindings": bindings,
        "immediate_own_parent": EXPECTED_PARENT,
        "older_own_paths_bound_transitively": 698,
        "no_historical_inventory_recopy_or_recursive_replay": True,
        "no_NEW_peer_affected_report_findings_hashes_or_metadata_accessed": True,
    }
    put(BASELINE, value)
    print(json.dumps({"baseline": fp(BASELINE), "protected_paths": 56}))


def check_baseline():
    data = obj(BASELINE)
    records, bindings = current_records()
    assert records == data["protected_fingerprints"]
    assert canonical_sha(records) == data["canonical_protected_summary_sha256"]
    assert bindings == data["accepted_operative_bindings"]
    return data


def label_checks():
    original = raw(AUTHOR + "obligations-v1.md").decode()
    assert re.findall(r"(?m)^\| (CF-\d+) \|", original) == [f"CF-{i:02d}" for i in range(1, 33)]
    ledger = raw(PREFIX + "ledger.md").decode()
    assert re.findall(r"(?m)^\| (CF-\d+) \|", ledger) == [f"CF-{i:02d}" for i in range(1, 33)]
    assert re.findall(r"(?m)^\| (AR-\d+) \|", ledger) == [f"AR-{i:02d}" for i in range(1, 9)]
    source = obj(PREFIX + "sources.json")
    assert source["original_obligations_checked"] == 32
    assert source["additional_affected_checks"] == 8
    assert source["total_hand_ledger_rows"] == 40
    assert source["new_peer_repair_findings_files_hashes_or_metadata_accessed"] is False
    assert source["requested_settings"] == {
        "model": "gpt-6.1-sol", "reasoning": "max", "inherited": True}
    assert source["independently_verified_effective_settings"] is None
    meter = source["authoritative_weekly_telemetry"]
    assert meter["reset_unix"] == 1792874445
    assert meter["used_percent_TOTAL"] < meter["ceiling_TOTAL_percent"] == 90
    return source


def freeze():
    assert not (ROOT / MANIFEST).exists()
    assert not (ROOT / VALIDATION).exists()
    data = check_baseline()
    source = label_checks()
    for suffix in PAYLOAD_SUFFIXES:
        if suffix != "input-validation.json":
            assert raw(PREFIX + suffix)
    put(VALIDATION, {
        "verified_at_utc": now(),
        "metadata_only_NOT_mathematical_certificate": True,
        "necessary_current_protected_paths_unchanged": 56,
        "all_five_author_repair_files_and_30_original_guards_checked": True,
        "exact_full_main_and_log_diff_checked_without_author_execution": True,
        "accepted_CG_R4_body_authority_suffix_bindings_unchanged": True,
        "original32_and_additional8_ledger_labels_present_ordered": True,
        "immediate_own_parent_and_ten_payloads_unchanged": True,
        "historical_inventory_recopied_or_recursively_replayed": False,
        "author_or_mathematical_code_executed": False,
        "ENTIRE_generated_metadata_readback_separate_postverify_required_before_handoff": True,
    })
    artifacts = [fp(PREFIX + suffix) for suffix in PAYLOAD_SUFFIXES]
    put(MANIFEST, {
        "frozen_at_utc": now(),
        "status": "ENTIRE affected independent R5 v2 review2 frozen, not promotion",
        "reviewer": "/root/review_2022_complexity_r2",
        "constructor": "/root", "constructor_excluded": True,
        "requested_settings": source["requested_settings"],
        "independently_verified_effective_settings": None,
        "original_obligations_checked": 32, "additional_affected_checks": 8,
        "total_hand_ledger_rows": 40,
        "whole_affected_report_ledger_issues_sources_log_code_ALLmetadata_complete": True,
        "whole_disposition": source["disposition"],
        "substantive_defects": 0, "further_required_repairs": 0,
        "unresolved_mathematical_objections": 0,
        "both_literal_corrections_and_log_consistency_checked": True,
        "original_closing_sentence_audit_omission_acknowledged": True,
        "all_downstream_orbits_divisibility_threshold_and_original_domain_reconstructed": True,
        "no_NEW_peer_affected_findings_files_hashes_or_metadata_accessed": True,
        "completion_identity_ONLY_until_BOTH_affected_entire_freezes": True,
        "no_math_program_CAS_scan_test_author_source_or_old_certificate_freezer_replay": True,
        "no_old_shared_Git_cache_write_spawn_download_charge_contact_or_bypass": True,
        "exact_author_repair_freeze": EXPECTED_REPAIR,
        "compact_necessary_baseline": fp(BASELINE),
        "protected_fingerprint_occurrences": 56, "protected_unique_paths": 56,
        "canonical_protected_summary_sha256": data["canonical_protected_summary_sha256"],
        "accepted_operative_bindings": data["accepted_operative_bindings"],
        "immediate_own_parent": EXPECTED_PARENT,
        "older_own_paths_bound_transitively": 698,
        "new_review_files_including_manifest": 10,
        "older_plus_new_own_paths_bound_transitively": 708,
        "no_historical_inventory_recopy_or_recursive_replay": True,
        "authoritative_weekly_telemetry": source["authoritative_weekly_telemetry"],
        "artifacts": artifacts,
    })
    print(json.dumps({"manifest": fp(MANIFEST), "report": artifacts[0], "files": 10}))


def verify():
    baseline_data = check_baseline()
    label_checks()
    data = obj(MANIFEST)
    assert data["compact_necessary_baseline"] == fp(BASELINE)
    assert data["canonical_protected_summary_sha256"] == baseline_data["canonical_protected_summary_sha256"]
    assert [r["path"] for r in data["artifacts"]] == [PREFIX + s for s in PAYLOAD_SUFFIXES]
    for record in data["artifacts"]:
        check(record)
    print(json.dumps({
        "separate_postfreeze_metadata_verification": "pass",
        "manifest": fp(MANIFEST), "report": data["artifacts"][0],
        "new_files": 10, "protected_paths_unchanged": 56,
        "own_paths_bound_transitively": 708,
        "no_NEW_peer_affected_material_accessed": True,
        "mathematical_certificate_or_promotion": False,
    }))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("baseline", "freeze", "verify"))
    mode = parser.parse_args().mode
    {"baseline": baseline, "freeze": freeze, "verify": verify}[mode]()
