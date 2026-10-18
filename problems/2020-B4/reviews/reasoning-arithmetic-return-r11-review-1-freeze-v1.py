#!/usr/bin/env python3
"""Root R11 OTHER WHOLE initial: byte preservation only, no mathematical program."""
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PRE = "problems/2020-B4/reviews/reasoning-arithmetic-return-r11-review-1-"
TARGET = "problems/2020-B4/notes/reasoning-arithmetic-return-r11-"
PARENT = "problems/2017-B4/reviews/reasoning-global-return-r7-review-1-manifest-v1.json"

def now():
    return datetime.now(timezone.utc).isoformat()

def fp(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}

def read(path):
    return json.loads((ROOT / path).read_text())

def save(path, data):
    assert path.startswith(PRE)
    with (ROOT / path).open("x") as stream:
        json.dump(data, stream, indent=2)
        stream.write("\n")

def verify_rows(rows):
    for row in rows:
        assert fp(row["path"]) == row, row["path"]

def baseline():
    constructor = read(TARGET + "freeze-v1.json")
    old = read(TARGET + "baseline-v1.json")
    verify_rows(constructor["artifacts"])
    verify_rows(old["protected"])
    paths = [r["path"] for r in constructor["artifacts"]]
    paths += [TARGET + "freeze-v1.json"] + [r["path"] for r in old["protected"]]
    paths += [PARENT]
    rows = [fp(p) for p in dict.fromkeys(paths)]
    save(PRE + "baseline-v1.json", {
        "recorded_utc": now(),
        "baseline_created_after_constructor_and_source_reads_before_ANY_new_R11_peer_access": True,
        "records": rows,
        "occurrences": len(paths), "unique_paths": len(rows),
        "compact_own_parent": fp(PARENT),
        "historical_inventories_bound_not_recursively_replayed": True,
        "mathematical_code": False,
    })
    print(json.dumps({"baseline": fp(PRE + "baseline-v1.json"), "paths": len(rows)}))

def freeze():
    base = read(PRE + "baseline-v1.json")
    verify_rows(base["records"])
    ledger = (ROOT / (PRE + "ledger-v1.md")).read_text()
    assert re.findall(r"^\| (R11-\d\d) \|", ledger, re.M) == [f"R11-{i:02}" for i in range(1, 61)]
    metadata = {
        "reviewer": "/root", "constructor": "/root/review_2022_complexity_r2",
        "constructor_excluded": True, "root_NEW_constructor_contribution": False,
        "ENTIRE_whole_initial_all60_complete": True,
        "ANY_new_corresponding_peer_findings_files_hashes_metadata_access_before_entire_freeze": False,
        "substantive_issues": 0, "required_repairs": 0, "closed_scope_notes": 5,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "verified_effective_settings": None,
        "mathematical_code_CAS_scan_source_rerun": False,
        "accepted_old_input_roles_not_new_self_certification": True,
        "new_q_verified_full_annual_solution_novelty": False,
        "latest_direct_weekly": {"utc": "2026-10-18 08:06:51 UTC", "total_percent": 16,
                                "reset_unix": 1792874445, "minutes": 10080,
                                "ordinary_allowed": True, "ceiling_total_percent": 90,
                                "automatic_later_window": False},
    }
    save(PRE + "metadata-v1.json", metadata)
    save(PRE + "input-validation-v1.json", {
        "verified_utc": now(), "protected_records_verified": len(base["records"]),
        "whole_ledger_60_labels_once_in_order": True,
        "metadata_only_not_proof": True, "old_and_constructor_bytes_unchanged": True,
    })
    suffixes = ["initial-v1.md", "ledger-v1.md", "issues-v1.md", "source-checks-v1.md",
                "worklog-v1.md", "freeze-v1.py", "baseline-v1.json", "metadata-v1.json",
                "input-validation-v1.json"]
    save(PRE + "manifest-v1.json", {
        "frozen_at_utc": now(), "status": "ENTIRE initially blind OTHER WHOLE R11 R1",
        "reviewer": "/root", "constructor": "/root/review_2022_complexity_r2",
        "all60_obligations": True, "substantive_issues": 0, "required_repairs": 0,
        "closed_scope_notes": 5,
        "exact_target": fp(TARGET + "candidate-v1.md"),
        "constructor_freeze": fp(TARGET + "freeze-v1.json"),
        "compact_own_parent": fp(PARENT),
        "no_NEW_R11_peer_material_read_or_hashed": True,
        "entire_report_ledger_sources_worklog_code_ALL_metadata_frozen": True,
        "artifacts": [fp(PRE + s) for s in suffixes], "promotion": False,
    })
    verify()

def verify():
    verify_rows(read(PRE + "baseline-v1.json")["records"])
    verify_rows(read(PRE + "manifest-v1.json")["artifacts"])
    print(json.dumps({"postverified": True, "manifest": fp(PRE + "manifest-v1.json")}))

if __name__ == "__main__":
    {"baseline": baseline, "freeze": freeze, "verify": verify}[sys.argv[1]]()
