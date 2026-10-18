#!/usr/bin/env python3
"""R14 R2 administrative file/JSON/label preservation only; no mathematics."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
PRE = "problems/2020-B4/reviews/reasoning-arithmetic-return-r14-review-2-"
AUTHOR = "problems/2020-B4/notes/reasoning-arithmetic-return-r14-freeze-v1.json"
AUTHOR_EXPECT = (7060, "e10b1b5ed9b573e181846b4403d1dbda20515fab3ff39091ce1c8c51124919d5")
MAIN = "problems/2020-B4/notes/reasoning-arithmetic-return-r14-candidate-v1.md"
MAIN_EXPECT = (16951, "673bcde7cadb391baf6a8362295bc4ba833e40a69dd4836725b5b3de2015df7f")
PARENT = "problems/2017-B4/reviews/coordinator-path-moment-r3-review-1-manifest-v1.json"
PARENT_EXPECT = (3001, "ec794d052263e2118eb49d5a61b08520439feba102b7addf08c9bc4216a56cd6")


def now():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    assert not path.startswith("/") and ".." not in Path(path).parts
    return (ROOT / path).read_bytes()


def fp(path):
    value = raw(path)
    return {"path": path, "bytes": len(value), "sha256": hashlib.sha256(value).hexdigest()}


def obj(path):
    return json.loads(raw(path))


def check(row):
    expected = {key: row[key] for key in ("path", "bytes", "sha256")}
    assert fp(row["path"]) == expected, row["path"]
    return expected


def pinned(path, expected):
    actual = fp(path)
    assert (actual["bytes"], actual["sha256"]) == expected, path
    return actual


def put(suffix, value):
    assert suffix in ("baseline-v1.json", "input-validation-v1.json", "metadata-v1.json", "manifest-v1.json")
    with (ROOT / (PRE + suffix)).open("x") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


def inputs():
    author = pinned(AUTHOR, AUTHOR_EXPECT)
    pinned(MAIN, MAIN_EXPECT)
    manifest = obj(AUTHOR)
    assert manifest["whole_obligations"] == 64
    assert manifest["ENTIRE_files_including_freeze"] == 12
    assert len(manifest["payloads"]) == 11
    author_rows = [check(row) for row in manifest["payloads"]] + [author]
    baseline = obj("problems/2020-B4/notes/reasoning-arithmetic-return-r14-baseline-v1.json")
    guard_rows = [check(row) for row in baseline["guard_records"]]
    assert len(guard_rows) == baseline["guard_occurrences"] == 30
    assert len({row["path"] for row in guard_rows}) == baseline["guard_unique_paths"] == 30
    for binding in manifest["accepted_bindings"]:
        for key in ("authority", "accepted_body", "unchanged_candidate_suffix"):
            check(binding[key])
        body = raw(binding["accepted_body"]["path"])
        candidate = raw(binding["unchanged_candidate_suffix"]["path"])
        assert body.endswith(candidate), binding["accepted_body"]["path"]
    parent = pinned(PARENT, PARENT_EXPECT)
    own_parent = obj(PARENT)
    parent_rows = [check(row) for row in own_parent["artifacts"]] + [parent]
    assert len(parent_rows) == 11
    return author_rows, guard_rows, parent_rows


def labels():
    expected = [f"{j:02d}" for j in range(1, 65)]
    actual = re.findall(r"(?m)^\| SQ14-(\d{2}) \| PASS \|", raw(PRE + "ledger-v1.md").decode())
    assert actual == expected
    author = re.findall(r"(?m)^\| SQ14-(\d{2}) \|", raw("problems/2020-B4/notes/reasoning-arithmetic-return-r14-obligations-v1.md").decode())
    assert author == expected
    source = obj(PRE + "sources-v1.json")
    assert source["whole_obligations"] == 64
    assert not source["new_peer_review_files_findings_hash_metadata_accessed"]
    notes = re.findall(r"(?m)^\| R14R2-N(\d) \| CLOSED \|", raw(PRE + "issues-v1.md").decode())
    assert notes == list("12345678")


def freeze():
    author_rows, guard_rows, parent_rows = inputs()
    labels()
    rows = author_rows + guard_rows + parent_rows
    unique = {row["path"]: row for row in rows}
    put("baseline-v1.json", {
        "created_at_utc": now(),
        "status": "Compact immutable preservation; not mathematical proof",
        "author_ENTIRE12": author_rows,
        "necessary_old_guard_records": guard_rows,
        "immediate_own_parent_records": parent_rows,
        "fingerprint_occurrences_checked": len(rows),
        "deduplicated_unique_paths": len(unique),
        "author_older_own_paths_bound_transitively_not_reexpanded": 781,
        "accepted_parent_metadata_occurrences_not_reexpanded": 725,
        "accepted_parent_unique_counts_per_binding": [110, 136, 62],
        "current_accepted_body_candidate_suffixes_verified": True,
        "corresponding_NEW_root_R14_peer_accessed": False,
        "no_recursive_historical_inventory_recopy_or_replay": True,
    })
    put("input-validation-v1.json", {
        "validated_at_utc": now(),
        "status": "PASS administrative only",
        "author12_oldguards30_ownparent11_checked": True,
        "all64_own_and_author_labels_match": True,
        "closed_scope_notes": 8,
        "baseline": fp(PRE + "baseline-v1.json"),
        "accepted_current_bodies_end_with_pinned_candidate_suffixes": True,
        "author_or_old_freezer_replayed": False,
        "mathematical_program_executed": False,
    })
    put("metadata-v1.json", {
        "created_at_utc": now(),
        "status": "ENTIRE OTHER initially blind WHOLE R14 R2; not promotion",
        "reviewer": "/root/review_2017_coarsening_r1",
        "constructor": "/root/review_2022_complexity_r2",
        "whole_obligations": 64,
        "all_files_including_manifest": 11,
        "old_A9_M10_authorship_disclosed_not_self_recertification": True,
        "NEW_R14_construction_contribution": False,
        "corresponding_NEW_peer_content_file_hash_metadata_accessed": False,
        "findings_EMBARGOED_until_explicit_BOTH_entire_confirmation": True,
        "FULL_final_model_readback_ALL11_and_SEPARATE_readonly_verify_required_after_freeze": True,
        "requested_model": "gpt-6.1-sol",
        "requested_reasoning": "max",
        "effective_readback": "unavailable",
        "authorized_weekly_reset": 1792874445,
        "total_weekly_ceiling_percent": 90,
        "latest_authoritative_root_context_percent": 38,
        "integration_reserve": True,
        "no_math_program_scan_CAS_test_source_author_old_replay": True,
        "no_Git_shared_old_cache_change_spawn_charge_contact_bypass": True,
    })
    files = sorted((ROOT / Path(PRE).parent).glob(Path(PRE).name + "*"))
    assert len(files) == 10, [str(path) for path in files]
    for path in files:
        if path.suffix == ".json":
            json.loads(path.read_text())
    put("manifest-v1.json", {
        "frozen_at_utc": now(),
        "status": "ENTIRE initially blind OTHER WHOLE R14 R2 checkpoint; findings embargoed",
        "reviewer": "/root/review_2017_coarsening_r1",
        "whole_obligations": 64,
        "all_files_including_manifest": 11,
        "author_freeze": fp(AUTHOR),
        "immediate_own_parent": fp(PARENT),
        "corresponding_NEW_peer_accessed": False,
        "BOTH_explicit_confirmation_required_before_findings_release": True,
        "FULL_final_model_readback_ALL11_then_SEPARATE_verify_REQUIRED": True,
        "artifacts": [fp(str(path.relative_to(ROOT))) for path in files],
    })
    print(json.dumps({"manifest": fp(PRE + "manifest-v1.json"), "initial": fp(PRE + "initial-v1.md"), "ENTIRE_files": 11, "whole_obligations": 64}, indent=2))


def verify():
    inputs()
    labels()
    baseline = obj(PRE + "baseline-v1.json")
    for key in ("author_ENTIRE12", "necessary_old_guard_records", "immediate_own_parent_records"):
        for row in baseline[key]:
            check(row)
    manifest = obj(PRE + "manifest-v1.json")
    assert len(manifest["artifacts"]) == 10
    for row in manifest["artifacts"]:
        check(row)
        if row["path"].endswith(".json"):
            obj(row["path"])
    print(json.dumps({
        "separate_readonly_verify_at_utc": now(),
        "status": "PASS",
        "ALL11_and_inputs_unchanged": True,
        "ALL64_labels": True,
        "manifest": fp(PRE + "manifest-v1.json"),
        "initial": fp(PRE + "initial-v1.md"),
        "mathematics_executed": False,
    }, indent=2))


if __name__ == "__main__":
    if sys.argv[1:] == ["verify"]:
        verify()
    elif not sys.argv[1:]:
        freeze()
    else:
        raise SystemExit("usage: admin-v1.py [verify]")
