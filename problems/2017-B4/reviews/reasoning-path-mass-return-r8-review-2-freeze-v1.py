#!/usr/bin/env python3
"""NEW independent review metadata only; no mathematical or author-code replay."""
from pathlib import Path
import datetime
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
BASE = "problems/2017-B4/reviews/reasoning-path-mass-return-r8-review-2-"
AUTHOR = "problems/2017-B4/notes/reasoning-path-mass-return-r8-"
FORBIDDEN = "problems/2017-B4/reviews/reasoning-path-mass-return-r8-review-1-"
MAIN = {"path": AUTHOR + "candidate-v1.md", "bytes": 22876,
        "sha256": "5bac467356c5f13bf5c93ad696d6325788e64a44b6d87eb5b9b2c97de847626e"}
AUTHOR_FREEZE = {"path": AUTHOR + "freeze-v1.json", "bytes": 2910,
                 "sha256": "83c9efd6a2e47e0a169a8415256d40ee1d154c142cd37dee28e344ec67b248e3"}
OWN_PARENT = {
    "path": "problems/2019-B4/notes/reasoning-cut-transfer-r5-freeze-v1.json",
    "bytes": 8902,
    "sha256": "52f8a794c3d82d3803a6b9700496cac2dff4b81a84e3f6c935b1bb9fbe107896",
}
PAYLOADS = ["initial.md", "ledger-v1.md", "issues-v1.md",
            "source-checks-v1.md", "sources-v1.json", "worklog-v1.md",
            "freeze-v1.py", "baseline-v1.json", "input-validation-v1.json"]
OLD_NAMES = ["coordinator-weighted-cutpath-r1", "coordinator-weighted-optimum-r2"]


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def read(path):
    p = Path(path)
    assert not p.is_absolute() and ".." not in p.parts and ".git" not in p.parts
    assert not path.startswith(FORBIDDEN), "NEW peer material forbidden"
    return (ROOT / p).read_bytes()


def obj(path):
    return json.loads(read(path))


def fp(path):
    data = read(path)
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def match(record):
    got = fp(record["path"])
    for key in ("bytes", "sha256"):
        assert got[key] == record[key], (record["path"], key)
    return got


def digest(records):
    return hashlib.sha256(json.dumps(records, sort_keys=True,
                                    separators=(",", ":")).encode()).hexdigest()


def write_new(path, data):
    assert path.startswith(BASE)
    with (ROOT / path).open("x", encoding="utf-8") as out:
        json.dump(data, out, indent=2, ensure_ascii=False)
        out.write("\n")


def label_checks():
    own = re.findall(r"^\| PM8R2-(\d{2}) \|",
                     read(BASE + "ledger-v1.md").decode(), re.MULTILINE)
    author = re.findall(r"^\| PM8-(\d{2}) \|",
                        read(AUTHOR + "obligations-v1.md").decode(), re.MULTILINE)
    expected = [f"{i:02d}" for i in range(1, 65)]
    assert own == expected and author == expected
    return 64


def inputs():
    match(MAIN)
    match(AUTHOR_FREEZE)
    match(OWN_PARENT)
    declared = obj(AUTHOR_FREEZE["path"])
    assert declared["whole_obligations"] == 64
    assert declared["all_artifacts_including_freeze"] == 11
    assert len(declared["artifacts"]) == 10
    paths = ["AGENTS.md", "problems/2017-B4/statement.md", AUTHOR_FREEZE["path"]]
    for rec in declared["artifacts"]:
        match(rec)
        paths.append(rec["path"])
    author_baseline = obj(AUTHOR + "baseline-v1.json")
    old_records = [match(rec) for rec in author_baseline["deduplicated_old_paths"]]
    assert len(old_records) == 51
    assert author_baseline["fingerprint_occurrences_verified"] == 60
    for rec in author_baseline["bound_metadata"]:
        match(rec)
    bindings = []
    for name in OLD_NAMES:
        authority = "problems/2017-B4/reviews/" + name + "-acceptance.json"
        a = obj(authority)
        assert a["status"].startswith("proved, independently reviewed")
        assert a["unresolved_substantive_issues"] == 0
        assert a["repair_required"] is False
        match(a["candidate"])
        match(a["accepted_copy"])
        assert read(a["accepted_copy"]["path"]).endswith(read(a["candidate"]["path"]))
        paths += [authority, authority[:-5] + ".md",
                  a["candidate"]["path"], a["accepted_copy"]["path"]]
        bindings.append({
            "authority": fp(authority),
            "accepted_body": a["accepted_copy"],
            "unchanged_candidate_suffix": a["candidate"],
            "historical_occurrences_bound_not_reexpanded": a["record_occurrences_verified"],
            "historical_unique_paths_bound_not_reexpanded": a["unique_paths_verified"],
        })
    paths += [
        "problems/2017-B4/notes/coordinator-weighted-cutpath-r1-source-audit-v1.md",
        "problems/2017-B4/notes/coordinator-weighted-cutpath-r1-sources-v1.json",
        "problems/2017-B4/notes/coordinator-weighted-cutpath-r1-failures-worklog-v1.md",
        "problems/2017-B4/notes/coordinator-weighted-optimum-r2-sources-v1.md",
        "problems/2017-B4/notes/coordinator-weighted-optimum-r2-failed-routes-v1.md",
        OWN_PARENT["path"],
    ]
    parent = obj(OWN_PARENT["path"])
    assert parent["older_plus_new_own_paths_bound_transitively"] == 771
    assert parent["ENTIRE_files_including_freeze"] == 11
    for rec in parent["payloads"]:
        match(rec)
        paths.append(rec["path"])
    assert fp("AGENTS.md")["sha256"] == "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"
    direct = [fp(path) for path in sorted(set(paths))]
    combined = {}
    for rec in direct + old_records:
        prior = combined.get(rec["path"])
        assert prior is None or prior == rec
        combined[rec["path"]] = rec
    all_unique = [combined[path] for path in sorted(combined)]
    assert label_checks() == 64
    summary = {
        "author_freeze": AUTHOR_FREEZE,
        "author_baseline": fp(AUTHOR + "baseline-v1.json"),
        "author_reports_original_occurrences": 60,
        "author_declared_deduplicated_paths_readonly_verified": len(old_records),
        "author_declared_rows_canonical_sha256": digest(old_records),
        "direct_guard_occurrences": len(paths),
        "direct_guard_unique_paths": len(direct),
        "combined_direct_plus_author_record_occurrences": len(paths) + len(old_records),
        "combined_unique_paths": len(all_unique),
        "combined_unique_canonical_sha256": digest(all_unique),
    }
    return direct, bindings, summary


def prepare():
    direct, bindings, summary = inputs()
    baseline = {
        "created_at_utc": utc(),
        "status": "necessary compact fingerprint preservation; NOT mathematical proof",
        "main": MAIN, "constructor_freeze": AUTHOR_FREEZE,
        "direct_guard_records": direct,
        "direct_guard_canonical_sha256": digest(direct),
        "accepted_bindings": bindings,
        "declared_metadata_summary": summary,
        "reproduction_reference": AUTHOR + "baseline-v1.json",
        "immediate_own_parent": OWN_PARENT,
        "older_own_paths_bound_transitively": 771,
        "no_historical_inventory_recopy_or_recursive_replay": True,
        "NEW_root_PM8_peer_content_hash_metadata_access": False,
    }
    write_new(BASE + "baseline-v1.json", baseline)
    validation = {
        "validated_at_utc": utc(),
        "status": "PASS necessary readonly fingerprints and ALL64 label correspondence; NOT proof",
        "whole_obligations": 64,
        "ENTIRE_constructor_files": 11,
        "direct_guard_canonical_sha256": digest(direct),
        "declared_metadata_summary": summary,
        "mathematical_program_CAS_scan_test_optimizer_or_replay": False,
        "NEW_peer_PM8_findings_files_hash_metadata_access": False,
    }
    write_new(BASE + "input-validation-v1.json", validation)
    print(json.dumps({"mode": "prepare", "UTC": utc(), "whole_obligations": 64,
                      "summary": summary}))


def check():
    baseline = obj(BASE + "baseline-v1.json")
    for rec in baseline["direct_guard_records"]:
        match(rec)
    direct, bindings, summary = inputs()
    assert direct == baseline["direct_guard_records"]
    assert digest(direct) == baseline["direct_guard_canonical_sha256"]
    assert bindings == baseline["accepted_bindings"]
    assert summary == baseline["declared_metadata_summary"]
    validation = obj(BASE + "input-validation-v1.json")
    assert validation["declared_metadata_summary"] == summary
    return baseline


def freeze():
    baseline = check()
    source = obj(BASE + "sources-v1.json")
    payloads = [fp(BASE + suffix) for suffix in PAYLOADS]
    manifest = {
        "frozen_at_utc": utc(),
        "status": "ENTIRE initially blind OTHER WHOLE review2; no coordinator promotion",
        "claims_reviewed": ["PM8A", "PM8B", "PM8C", "PM8D", "PM8E"],
        "whole_obligations": 64,
        "constructor": "/root/review_2017_coarsening_r1",
        "constructor_excluded": True,
        "reviewer": "/root/review_2022_complexity_r2",
        "reviewer_did_not_construct_NEW_PM8": True,
        "NEW_corresponding_root_PM8_review_findings_files_hash_metadata_access": False,
        "all64_initial_dispositions": "PASS within exact scope",
        "substantive_defects": 0, "required_repairs": 0,
        "unresolved_substantive_issues": 0, "closed_scope_notes": 7,
        "FULL_final_readback_ALLpayload_code_generatedmetadata_required": True,
        "SEPARATE_readonly_postverification_required": True,
        "identity_ONLY_handoff_until_BOTH_ENTIRE_confirmed": True,
        "requested_settings": source["requested_settings"],
        "independent_effective_readback": None,
        "authoritative_weekly_telemetry": source["authoritative_weekly_telemetry"],
        "main_review": payloads[0],
        "target_main": MAIN, "target_freeze": AUTHOR_FREEZE,
        "baseline": fp(BASE + "baseline-v1.json"),
        "declared_metadata_summary": baseline["declared_metadata_summary"],
        "accepted_bindings": baseline["accepted_bindings"],
        "immediate_own_parent": OWN_PARENT,
        "older_own_paths_bound_transitively": 771,
        "ENTIRE_review_files_including_manifest": 10,
        "older_plus_new_own_paths_bound_transitively": 781,
        "no_mathematical_code_CAS_scan_test_optimizer_source_author_or_old_freezer_replay": True,
        "no_Git_shared_old_cache_write_spawn_charge_contact_bypass": True,
        "payloads": payloads,
    }
    path = BASE + "manifest-v1.json"
    write_new(path, manifest)
    print(json.dumps({"mode": "freeze", "UTC": utc(), "manifest": fp(path),
                      "report": payloads[0], "ENTIRE_files": 10,
                      "whole_obligations": 64}))


def verify():
    baseline = check()
    path = BASE + "manifest-v1.json"
    manifest = obj(path)
    assert manifest["whole_obligations"] == 64
    assert manifest["ENTIRE_review_files_including_manifest"] == 10
    assert len(manifest["payloads"]) == 9
    for rec in manifest["payloads"]:
        match(rec)
    match(manifest["baseline"])
    assert manifest["declared_metadata_summary"] == baseline["declared_metadata_summary"]
    print(json.dumps({"mode": "verify", "verified_at_utc": utc(),
                      "status": "PASS SEPARATE read-only metadata verification; NOT mathematical proof",
                      "ENTIRE_files": 10, "whole_obligations": 64,
                      "combined_unique_paths": baseline["declared_metadata_summary"]["combined_unique_paths"],
                      "own_paths_bound_transitively": 781,
                      "manifest": fp(path), "report": manifest["main_review"]}))


if __name__ == "__main__":
    assert len(sys.argv) == 2
    mode = sys.argv[1]
    assert mode in {"prepare", "freeze", "verify"}
    {"prepare": prepare, "freeze": freeze, "verify": verify}[mode]()
