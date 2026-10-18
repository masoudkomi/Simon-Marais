#!/usr/bin/env python3
"""PM9 R1 administrative byte/JSON/label checks only; no mathematics."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
PRE = "problems/2017-B4/reviews/coordinator-path-moment-r3-review-1-"
AUTHOR = "problems/2017-B4/notes/coordinator-path-moment-r3-freeze-v2.json"
AUTHOR_EXPECT = (4093, "7210932f81b90afa8197fb40fe6c7cc3603fbfc85c39b58c67df4f36728b185d")
MAIN = "problems/2017-B4/notes/coordinator-path-moment-r3-candidate-v1.md"
MAIN_EXPECT = (12255, "0af3e42df62385e086a53eec1d95461ba01ba26148a6f92bd34b1fb778924076")
PARENT = "problems/2024-B4/notes/reasoning-cofactor-return-r7-freeze-v1.json"
PARENT_EXPECT = (3129, "18d2a87ffb4f0f7ca2140659a0883f697974620ba507453fdfda01b8cff49cd1")

def now():
    return datetime.now(timezone.utc).isoformat()

def raw(path):
    assert not path.startswith("/") and ".." not in Path(path).parts
    return (ROOT / path).read_bytes()

def fp(path):
    b = raw(path)
    return {"path": path, "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}

def check(row):
    value = {key: row[key] for key in ("path", "bytes", "sha256")}
    assert fp(row["path"]) == value, row["path"]
    return value

def obj(path):
    return json.loads(raw(path))

def put(suffix, value):
    assert suffix in ("baseline-v1.json", "input-validation-v1.json", "metadata-v1.json", "manifest-v1.json")
    with (ROOT / (PRE + suffix)).open("x") as f:
        json.dump(value, f, indent=2, ensure_ascii=False)
        f.write("\n")

def pinned(path, expected):
    actual = fp(path)
    assert (actual["bytes"], actual["sha256"]) == expected, path
    return actual

def inputs():
    a = pinned(AUTHOR, AUTHOR_EXPECT)
    pinned(MAIN, MAIN_EXPECT)
    v = obj(AUTHOR)
    assert v["whole_obligations"] == 48 and len(v["payloads"]) == 15
    author_rows = [check(row) for row in v["payloads"]] + [a]
    baseline = obj("problems/2017-B4/notes/coordinator-path-moment-r3-baseline-v1.json")
    old_rows = [check(row) for row in baseline["fingerprints"]]
    assert len(old_rows) == 21
    old_v1 = obj("problems/2017-B4/notes/coordinator-path-moment-r3-freeze-v1.json")
    assert len(old_v1["payloads"]) == 11
    for row in old_v1["payloads"]:
        check(row)
    p = pinned(PARENT, PARENT_EXPECT)
    parent = obj(PARENT)
    parent_rows = [check(row) for row in parent["artifacts"]] + [p]
    assert len(parent_rows) == 13
    return author_rows, old_rows, parent_rows

def labels():
    expected = [f"{j:02d}" for j in range(1, 49)]
    ids = re.findall(r"(?m)^\| PM9-(\d{2}) \|", raw(PRE + "ledger-v1.md").decode())
    assert ids == expected
    author_ids = re.findall(r"(?m)^\| PM9-(\d{2}) \|", raw("problems/2017-B4/notes/coordinator-path-moment-r3-obligations-v2.md").decode())
    assert author_ids == expected
    source = obj(PRE + "sources-v1.json")
    assert source["whole_obligations"] == 48 and not source["new_peer_review_files_findings_hash_metadata_accessed"]

def freeze():
    author_rows, old_rows, parent_rows = inputs()
    labels()
    all_rows = author_rows + old_rows + parent_rows
    unique = {row["path"]: row for row in all_rows}
    put("baseline-v1.json", {
        "created_at_utc": now(), "author_ENTIRE16": author_rows,
        "accepted_input_records": old_rows,
        "immediate_own_parent_records": parent_rows,
        "fingerprint_occurrences_checked": len(all_rows) + 11,
        "deduplicated_unique_paths": len(unique),
        "preserved_v1_payload_occurrences_additionally_checked": 11,
        "compact_parent_not_recursive_history_recopy": True,
        "corresponding_NEW_peer_material_accessed": False,
    })
    put("input-validation-v1.json", {
        "validated_at_utc": now(), "status": "PASS administrative only",
        "author16_and_old_v1_11_payloads_checked": True,
        "accepted_inputs21_and_parent13_unchanged": True,
        "all48_labels_match_operative_v2": True,
        "baseline": fp(PRE + "baseline-v1.json"),
        "author_or_old_freezer_rerun": False,
        "mathematical_program_executed": False,
    })
    put("metadata-v1.json", {
        "created_at_utc": now(), "status": "ENTIRE initially blind OTHER WHOLE PM9 R1, not promotion",
        "reviewer": "/root/review_2017_coarsening_r1", "new_constructor": "/root",
        "whole_obligations": 48, "all_files_including_manifest": 11,
        "old_PM8_constructor_role_disclosed_not_self_recertification": True,
        "corresponding_NEW_peer_content_hash_metadata_accessed": False,
        "findings_EMBARGOED_until_explicit_BOTH_entire_confirmation": True,
        "FULL_final_model_readback_and_SEPARATE_readonly_verify_REQUIRED_after_freeze": True,
        "requested_model": "gpt-6.1-sol", "requested_reasoning": "max", "effective_readback": "unavailable",
        "authorized_weekly_reset": 1792874445, "total_weekly_ceiling_percent": 90,
        "latest_root_context_percent": 38, "integration_reserve": True,
        "no_math_program_scan_CAS_optimizer_test_or_old_replay": True,
    })
    files = sorted((ROOT / Path(PRE).parent).glob(Path(PRE).name + "*"))
    assert len(files) == 10, [str(path) for path in files]
    for path in files:
        if path.suffix == ".json":
            json.loads(path.read_text())
    put("manifest-v1.json", {
        "frozen_at_utc": now(), "status": "ENTIRE initially blind OTHER WHOLE PM9 R1 checkpoint; findings embargoed",
        "reviewer": "/root/review_2017_coarsening_r1", "whole_obligations": 48,
        "all_files_including_manifest": 11, "author_freeze": fp(AUTHOR),
        "immediate_own_parent": fp(PARENT),
        "corresponding_NEW_peer_accessed": False,
        "BOTH_explicit_confirmation_required_before_findings_release": True,
        "FULL_final_model_readback_ALL11_then_SEPARATE_verify_REQUIRED": True,
        "artifacts": [fp(str(path.relative_to(ROOT))) for path in files],
    })
    print(json.dumps({"manifest": fp(PRE + "manifest-v1.json"), "initial": fp(PRE + "initial-v1.md"), "ENTIRE_files": 11, "whole_obligations": 48}, indent=2))

def verify():
    inputs()
    labels()
    baseline = obj(PRE + "baseline-v1.json")
    for key in ("author_ENTIRE16", "accepted_input_records", "immediate_own_parent_records"):
        for row in baseline[key]:
            check(row)
    manifest = obj(PRE + "manifest-v1.json")
    assert len(manifest["artifacts"]) == 10
    for row in manifest["artifacts"]:
        check(row)
        if row["path"].endswith(".json"):
            obj(row["path"])
    print(json.dumps({"separate_readonly_verify_at_utc": now(), "status": "PASS", "ALL11_and_inputs_unchanged": True, "ALL48": True, "manifest": fp(PRE + "manifest-v1.json"), "initial": fp(PRE + "initial-v1.md"), "mathematics_executed": False}, indent=2))

if __name__ == "__main__":
    if sys.argv[1:] == ["verify"]:
        verify()
    elif not sys.argv[1:]:
        freeze()
    else:
        raise SystemExit("usage: admin-v1.py [verify]")
