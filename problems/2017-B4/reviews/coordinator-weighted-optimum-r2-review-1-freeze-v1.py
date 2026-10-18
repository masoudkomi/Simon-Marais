#!/usr/bin/env python3
"""NEW WO review1 preservation metadata only; not a mathematical program."""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2017-B4/reviews/coordinator-weighted-optimum-r2-review-1-"
AUTHOR = "problems/2017-B4/notes/coordinator-weighted-optimum-r2-"
AUTHOR_FREEZE = {
    "path": AUTHOR + "freeze-v1.json", "bytes": 2906,
    "sha256": "e8c60dd823a4e88c0b7d9cd5eb820f13c2791ca69b00317195c806faf51e30ec",
}
AUTHOR_MAIN = {
    "path": AUTHOR + "candidate-v1.md", "bytes": 14252,
    "sha256": "ca09c36677badac6649775d2ade78a4f5af90fcbdafd0648a6bf8541e835e533",
}
WC_AUTHORITY = "problems/2017-B4/reviews/coordinator-weighted-cutpath-r1-acceptance.json"
PARENT = {
    "path": "problems/2020-B4/notes/reasoning-arithmetic-return-r13-freeze-v1.json",
    "bytes": 6630,
    "sha256": "eba097f9c6bffc2549fef51ef74b99962b16affa86a7dcaf9679bab95ad8adbe",
}
FORBIDDEN = (
    "problems/2020-B4/reviews/reasoning-arithmetic-return-r13-",
    "problems/2025-B4/reviews/reasoning-branch-return-r4-",
)
PAYLOAD = (
    "initial-v1.md", "ledger-v1.md", "issues-v1.md",
    "source-checks-v1.md", "sources-v1.json", "worklog-v1.md",
    "freeze-v1.py", "baseline-v1.json", "input-validation-v1.json",
)


def now():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    assert isinstance(path, str) and not path.startswith("/")
    assert ".." not in Path(path).parts
    assert not any(path.startswith(x) for x in FORBIDDEN), path
    if path.startswith("problems/2017-B4/reviews/coordinator-weighted-optimum-r2-"):
        assert path.startswith(P), path
    return (ROOT / path).read_bytes()


def obj(path):
    return json.loads(raw(path))


def fp(path):
    value = raw(path)
    return {"path": path, "bytes": len(value), "sha256": hashlib.sha256(value).hexdigest()}


def check(record):
    value = {k: record[k] for k in ("path", "bytes", "sha256")}
    assert fp(record["path"]) == value, record["path"]
    return value


def digest(value):
    value = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(value.encode()).hexdigest()


def put(suffix, value):
    assert suffix in ("baseline-v1.json", "input-validation-v1.json", "manifest-v1.json")
    with (ROOT / (P + suffix)).open("x", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def records():
    check(AUTHOR_FREEZE)
    author = obj(AUTHOR_FREEZE["path"])
    assert author["whole_obligations"] == 48
    assert author["constructor_files_including_freeze"] == 11
    assert len(author["artifacts"]) == 10
    assert author["artifacts"][0] == AUTHOR_MAIN
    rows = [AUTHOR_FREEZE] + [check(r) for r in author["artifacts"]]

    wc = obj(WC_AUTHORITY)
    assert wc["status"] == "proved, independently reviewed scoped partial result"
    assert wc["proposed_claims_accepted"] == ["WC1", "WC2", "WC3"]
    assert not wc["repair_required"] and wc["unresolved_substantive_issues"] == 0
    body, candidate = check(wc["accepted_copy"]), check(wc["candidate"])
    assert body["bytes"] == 15914
    assert body["sha256"] == "93c08b0a43426c972bd6a0042c7e496cb08a106873c931f0231901e9f425f14b"
    assert raw(body["path"]).endswith(raw(candidate["path"]))
    assert wc["record_occurrences_verified"] == 102 and wc["unique_paths_verified"] == 49
    wc_rows = [fp(WC_AUTHORITY), fp(WC_AUTHORITY[:-5] + ".md"), body, candidate]
    wc_rows += [fp(path) for path in (
        "problems/2017-B4/notes/coordinator-weighted-cutpath-r1-source-audit-v1.md",
        "problems/2017-B4/notes/coordinator-weighted-cutpath-r1-sources-v1.json",
        "problems/2017-B4/notes/coordinator-weighted-cutpath-r1-freeze-v1.json",
        "AGENTS.md", "problems/2017-B4/statement.md",
    )]
    assert len(wc_rows) == 9
    assert fp("AGENTS.md") == {
        "path": "AGENTS.md", "bytes": 4707,
        "sha256": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"}
    assert fp("problems/2017-B4/statement.md") == {
        "path": "problems/2017-B4/statement.md", "bytes": 2140,
        "sha256": "e459750064b4e25e3eaa71f25f236c046548147e415b06d8bd097839020228f3"}
    rows += wc_rows

    # Validate the author's DECLARED compact summary, without reopening
    # unrelated root R17 review payloads as fresh mathematical premises.
    declared = obj(AUTHOR + "baseline-v1.json")
    assert declared["occurrences"] == declared["unique_paths"] == 20
    assert digest(declared["protected_rows"]) == declared["canonical_summary_sha256"]
    declared_by_path = {r["path"]: r for r in declared["protected_rows"]}
    assert len(declared_by_path) == 20
    for record in wc_rows:
        assert declared_by_path[record["path"]] == record
    assert declared["immediate_own_parent"] == author["immediate_own_parent"]

    check(PARENT)
    own = obj(PARENT["path"])
    assert own["older_plus_new_own_paths_bound_transitively"] == 719
    assert own["new_constructor_files_including_freeze"] == 11
    assert len(own["artifacts"]) == 10
    rows += [PARENT] + [check(r) for r in own["artifacts"]]
    assert len(rows) == len({r["path"] for r in rows}) == 31
    return sorted(rows, key=lambda r: r["path"]), declared["canonical_summary_sha256"]


def baseline():
    rows, author_summary = records()
    put("baseline-v1.json", {
        "captured_at_utc": now(),
        "purpose": "NEW compact preservation metadata only, not mathematical evidence or another review",
        "snapshot_stage": "after ENTIRE author read and hand reconstruction, before whole review freeze",
        "assigned_prefix_confirmed_unused_before_first_write": True,
        "protected_fingerprint_occurrences": 31, "protected_unique_paths": 31,
        "canonical_protected_summary_sha256": digest(rows),
        "protected_fingerprints": rows,
        "author_packet_files": 11, "author_whole_obligations": 48,
        "author_declared_20_path_summary_bound_without_unrelated_ancestry_replay": author_summary,
        "accepted_WC_occurrences_bound_not_replayed": 102,
        "accepted_WC_paths_bound_not_replayed": 49,
        "current_WC_MD_JSON_body_candidate_suffix_exact": True,
        "immediate_own_parent": PARENT,
        "older_own_paths_bound_transitively": 719,
        "no_historical_inventory_recopy_or_recursive_replay": True,
        "no_corresponding_NEW_peer_material_read_or_hashed": True,
        "mathematical_program_or_constructor_freezer_executed": False,
    })
    print(json.dumps({"baseline": fp(P + "baseline-v1.json"), "protected_paths": 31}))


def check_baseline():
    data = obj(P + "baseline-v1.json")
    rows, author_summary = records()
    assert rows == data["protected_fingerprints"]
    assert digest(rows) == data["canonical_protected_summary_sha256"]
    assert author_summary == data["author_declared_20_path_summary_bound_without_unrelated_ancestry_replay"]
    return data


def label_checks():
    ledger = raw(P + "ledger-v1.md").decode()
    labels = re.findall(r"(?m)^\|(WO-\d{2})\|PASS\.", ledger)
    assert labels == [f"WO-{i:02d}" for i in range(1, 49)]
    issues = raw(P + "issues-v1.md").decode()
    assert re.findall(r"(?m)^\|(WOR1-N\d)\|", issues) == [f"WOR1-N{i}" for i in range(1, 7)]
    main = raw(P + "initial-v1.md").decode()
    assert all(x in main for x in ("WO1", "WO2", "WO3", "WO4", "candidate proof -"))
    source = obj(P + "sources-v1.json")
    assert source["whole_obligations"] == 48
    assert source["substantive_defects"] == source["required_author_repairs"] == source["unresolved_mathematical_issues"] == 0
    assert source["closed_scope_notes"] == 6
    assert source["reviewer_constructed_or_supplied_NEW_proof_inference"] is False
    assert source["corresponding_NEW_peer_report_findings_files_hash_or_metadata_accessed"] is False
    assert source["requested_settings"] == {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True}
    assert source["independently_verified_effective_readback"] is None
    meter = source["authoritative_weekly_telemetry"]
    assert meter["reset_unix"] == 1792874445 and meter["used_percent_TOTAL"] < meter["TOTAL_ceiling"] == 90
    assert meter["automatic_later_reset_spending"] is False
    return source


def freeze():
    data = check_baseline()
    source = label_checks()
    for suffix in PAYLOAD:
        if suffix != "input-validation-v1.json":
            assert raw(P + suffix)
    put("input-validation-v1.json", {
        "verified_at_utc": now(),
        "metadata_ONLY_NOT_mathematical_test_or_independent_review": True,
        "all31_necessary_protected_fingerprints_unchanged": True,
        "ENTIRE_eleven_file_constructor_packet_exact": True,
        "WC_current_authority_body_literal_candidate_suffix_exact": True,
        "ALL48_PASS_ledger_labels_once_in_order": True,
        "six_closed_scope_note_labels_once_in_order": True,
        "unrelated_historical_inventory_replayed": False,
        "immediate_own_parent_and_ten_payloads_unchanged": True,
        "ENTIRE_generated_metadata_full_readback_and_SEPARATE_verify_required_before_handoff": True,
    })
    artifacts = [fp(P + suffix) for suffix in PAYLOAD]
    put("manifest-v1.json", {
        "frozen_at_utc": now(),
        "status": "ENTIRE initially blind OTHER WHOLE review1; not coordinator acceptance",
        "reviewer": "/root/review_2022_complexity_r2",
        "whole_obligations": 48,
        "ENTIRE_main_ALL48_ledger_issues_sources_log_code_ALLmetadata_frozen": True,
        "requested_settings": source["requested_settings"],
        "independently_verified_effective_readback": None,
        "reviewer_constructed_or_supplied_NEW_proof_inference": False,
        "root_sole_constructor_excluded": True,
        "corresponding_NEW_peer_report_findings_files_hash_or_metadata_accessed": False,
        "initial_handoff_IDENTITY_ONLY_until_BOTH_ENTIRE_freezes_confirmed": True,
        "review_finding": {"substantive_defects": 0, "required_author_repairs": 0, "unresolved_mathematical_issues": 0, "closed_scope_notes": 6},
        "WO4_low_cost_hypothesis_remains_unproved_and_conditional": True,
        "author_main": AUTHOR_MAIN, "author_freeze": AUTHOR_FREEZE,
        "accepted_WC_occurrences_paths_bound_not_replayed": [102, 49],
        "compact_necessary_baseline": fp(P + "baseline-v1.json"),
        "protected_fingerprint_occurrences": 31, "protected_unique_paths": 31,
        "canonical_protected_summary_sha256": data["canonical_protected_summary_sha256"],
        "immediate_own_parent": PARENT,
        "older_own_paths_bound_transitively": 719,
        "new_review_files_including_manifest": 10,
        "older_plus_new_own_paths_bound_transitively": 729,
        "no_historical_inventory_recopy_or_recursive_replay": True,
        "no_mathematical_code_scan_test_optimizer_CAS_source_author_or_old_freezer_replay": True,
        "no_old_shared_Git_cache_edit_spawn_download_charge_contact_or_bypass": True,
        "authoritative_weekly_telemetry": source["authoritative_weekly_telemetry"],
        "artifacts": artifacts,
    })
    print(json.dumps({"manifest": fp(P + "manifest-v1.json"), "report": artifacts[0], "new_files": 10}))


def verify():
    data = check_baseline()
    label_checks()
    manifest = obj(P + "manifest-v1.json")
    assert manifest["whole_obligations"] == 48
    assert manifest["compact_necessary_baseline"] == fp(P + "baseline-v1.json")
    assert manifest["canonical_protected_summary_sha256"] == data["canonical_protected_summary_sha256"]
    assert [r["path"] for r in manifest["artifacts"]] == [P + s for s in PAYLOAD]
    for record in manifest["artifacts"]:
        check(record)
    print(json.dumps({
        "separate_postfreeze_metadata_verification": "pass",
        "manifest": fp(P + "manifest-v1.json"),
        "report": manifest["artifacts"][0],
        "whole_obligations": 48, "new_files": 10,
        "necessary_old_paths_unchanged": 31,
        "own_paths_bound_transitively": 729,
        "mathematical_test_certificate_or_another_independent_review": False,
        "corresponding_NEW_peer_material_read_or_hashed": False,
    }))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("baseline", "freeze", "verify"))
    {"baseline": baseline, "freeze": freeze, "verify": verify}[parser.parse_args().mode]()
