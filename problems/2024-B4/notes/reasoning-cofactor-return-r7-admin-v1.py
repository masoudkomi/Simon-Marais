#!/usr/bin/env python3
"""R7 administrative preservation only; no mathematics, scans, or old reruns."""
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BASE = Path("problems/2024-B4/notes")
PREFIX = "reasoning-cofactor-return-r7-"
PARENT = "problems/2022-B4/reviews/reasoning-dynamics-return-r6-review-1-manifest-v1.json"
PARENT_EXPECTED = (3020, "f02e07762a7434b3c5292604733f3c50ad5abb51474290e07725e298156ff308")

EXPECTED = {
    "AGENTS.md": (4707, "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"),
    "problems/2024-B4/proofs/reviewed-structural-v1.1.md": (17079, "082dc054ce2cdaea80eee009f4c97c877c6968afb54b5a8f3141b7354031dd3f"),
    "problems/2024-B4/proofs/reviewed-reasoning-cofactor-return-r6-v1.1.md": (20658, "fb988a13187b5765619532ad14077ae2f32a948e04704252e3d8981e10d65d98"),
    "problems/2024-B4/proofs/reviewed-cofactor-dominant-r4-v1.1.md": (18793, "14c47b6db082bee1d60bcf297c289fe949fdec9384cc8a159b199c56ba265838"),
    "problems/2024-B4/proofs/reviewed-cofactor-Frobenius-r5-v2.1.md": (17704, "aa7c3edba910270594302ede19cce7a8f530e21f3c5b17e4c64ddd387762bcf3"),
    "problems/2024-B4/proofs/reviewed-coordinator-three-bit-sector-r2-v1.1.md": (20916, "52e107759f513006a93f141add6130ca31b2d14220c9980ef596e9bebf5d2dab"),
}
AUTHORITIES = [
    ("structural-acceptance", "reviewed-structural-v1.1.md"),
    ("reasoning-cofactor-return-r6-acceptance", "reviewed-reasoning-cofactor-return-r6-v1.1.md"),
    ("cofactor-dominant-r4-acceptance", "reviewed-cofactor-dominant-r4-v1.1.md"),
    ("cofactor-Frobenius-r5-acceptance", "reviewed-cofactor-Frobenius-r5-v2.1.md"),
    ("coordinator-three-bit-sector-r2-acceptance", "reviewed-coordinator-three-bit-sector-r2-v1.1.md"),
]
OTHER_INPUTS = [
    "problems/2024-B4/statement.md",
    "problems/2024-B4/proofs/reviewed-generalized-Kasami-v1.1.md",
    "problems/2024-B4/notes/cofactor-dominant-r4-sources-v1.md",
    "problems/2024-B4/notes/cofactor-dominant-r4-failures-worklog-v1.md",
    "problems/2024-B4/notes/cofactor-Frobenius-r5-sources-v1.md",
    "problems/2024-B4/notes/cofactor-Frobenius-r5-failures-worklog-v2.md",
]

def now():
    return datetime.now(timezone.utc).isoformat()

def rec(path):
    data = (ROOT / path).read_bytes()
    return {"path": str(path), "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}

def validate(row):
    actual = rec(row["path"])
    assert actual == {k: row[k] for k in ("path", "bytes", "sha256")}, (actual, row)
    return actual

def records(value):
    if isinstance(value, dict):
        if all(k in value for k in ("path", "bytes", "sha256")):
            yield {k: value[k] for k in ("path", "bytes", "sha256")}
        for child in value.values():
            yield from records(child)
    elif isinstance(value, list):
        for child in value:
            yield from records(child)

def own(name):
    return BASE / (PREFIX + name)

def write(name, data):
    path = ROOT / own(name)
    assert not path.exists(), f"refuse overwrite {path}"
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")

def verify():
    manifest = json.loads((ROOT / own("freeze-v1.json")).read_text())
    for row in manifest["artifacts"]:
        validate(row)
        if row["path"].endswith(".json"):
            json.loads((ROOT / row["path"]).read_text())
    baseline = json.loads((ROOT / own("baseline-v1.json")).read_text())
    for row in baseline["input_records"] + baseline["immediate_parent_records"]:
        validate(row)
    ledger = (ROOT / own("obligations-v1.md")).read_text()
    ids = re.findall(r"^\| (R7-\d{2}) \|", ledger, flags=re.M)
    assert len(ids) == 64 and len(set(ids)) == 64
    assert ids == [f"R7-{j:02d}" for j in range(1, 65)]
    assert len(manifest["artifacts"]) == 12
    print(json.dumps({"separate_read_only_verify_at_utc": now(), "all13_files_and_inputs": "PASS", "whole_obligations": 64, "manifest": rec(own("freeze-v1.json")), "main": rec(own("candidate-v1.md")), "no_mathematics_run": True}, indent=2))

def freeze():
    assert rec(PARENT)["bytes"] == PARENT_EXPECTED[0]
    assert rec(PARENT)["sha256"] == PARENT_EXPECTED[1]
    parent = json.loads((ROOT / PARENT).read_text())
    parent_rows = list(records(parent))
    parent_dedup = {row["path"]: validate(row) for row in parent_rows}
    parent_dedup[PARENT] = rec(PARENT)
    input_rows = []
    for path, expected in EXPECTED.items():
        actual = rec(path)
        assert (actual["bytes"], actual["sha256"]) == expected, actual
        input_rows.append(actual)
    authority_checks = []
    for stem, body_name in AUTHORITIES:
        md = f"problems/2024-B4/reviews/{stem}.md"
        js = f"problems/2024-B4/reviews/{stem}.json"
        input_rows.extend([rec(md), rec(js)])
        value = json.loads((ROOT / js).read_text())
        body_path = "problems/2024-B4/proofs/" + body_name
        declared = [row for row in records(value) if row["path"] == body_path]
        assert declared, (js, body_path)
        for row in declared:
            validate(row)
        authority_checks.append({"authority": js, "accepted_body": body_path, "declared_occurrences_verified": len(declared)})
    input_rows.extend(rec(path) for path in OTHER_INPUTS)
    unique_inputs = {row["path"]: row for row in input_rows}
    ids = re.findall(r"^\| (R7-\d{2}) \|", (ROOT / own("obligations-v1.md")).read_text(), flags=re.M)
    assert ids == [f"R7-{j:02d}" for j in range(1, 65)]
    baseline = {
        "created_at_utc": now(),
        "compact_parent_binding_not_historical_inventory_copy": True,
        "immediate_parent_manifest": rec(PARENT),
        "parent_fingerprint_occurrences_verified": len(parent_rows),
        "parent_unique_paths_including_manifest": len(parent_dedup),
        "immediate_parent_records": list(parent_dedup.values()),
        "input_records": list(unique_inputs.values()),
        "authority_body_checks": authority_checks,
        "NEW_peer_material_read": False,
        "source_binaries_downloaded_or_cache_written": False,
    }
    write("baseline-v1.json", baseline)
    write("input-validation-v1.json", {
        "validated_at_utc": now(), "status": "PASS administrative input checks only",
        "baseline": rec(own("baseline-v1.json")),
        "parent_occurrences": len(parent_rows), "parent_unique_paths_including_manifest": len(parent_dedup),
        "current_input_unique_paths": len(unique_inputs),
        "authorities_current_body_matches": len(authority_checks),
        "no_old_source_author_freezer_program_rerun": True,
        "no_new_math_computation": True,
    })
    write("metadata-v1.json", {
        "created_at_utc": now(), "status": "candidate proof - unverified",
        "constructor": "/root/review_2017_coarsening_r1", "constructor_excluded": True,
        "root_generic_target_no_NEW_inference": True,
        "claims": ["R7A", "R7B", "R7C", "R7D"], "whole_obligations": 64,
        "TWO_OTHER_ENTIRE_initially_blind_WHOLE_audits_required": True,
        "requested_model": "gpt-6.1-sol", "requested_reasoning": "max", "effective_readback": "unavailable",
        "authorized_weekly_reset": 1792874445, "stop_total_used_percent": 90,
        "current_root_meter_context_percent": 37, "integration_reserve_required": True,
        "old_C_R6_and_sector3_roles_disclosed_not_self_recertification": True,
        "proof_is_hand_no_math_executable": True,
        "Férard2017_operative_body_unread_priority_unestablished": True,
        "annual_classification_or_novel_method_claim": False,
        "FULL_final_readback_and_SEPARATE_readonly_verify_follow_freeze": True,
    })
    files = sorted(path for path in (ROOT / BASE).glob(PREFIX + "*") if path.is_file())
    assert len(files) == 12, [str(path) for path in files]
    for path in files:
        if path.suffix == ".json":
            json.loads(path.read_text())
    write("freeze-v1.json", {
        "frozen_at_utc": now(), "status": "ENTIRE R7 constructor checkpoint, candidate proof - unverified",
        "constructor": "/root/review_2017_coarsening_r1", "whole_obligations": 64,
        "all_files_including_freeze": 13, "immediate_own_parent": rec(PARENT),
        "TWO_OTHER_ENTIRE_initially_blind_WHOLE_audits_pending": True,
        "no_NEW_peer_material_or_math_computation": True,
        "FULL_final_readback_and_SEPARATE_verify_REQUIRED_after_freeze": True,
        "artifacts": [rec(path.relative_to(ROOT)) for path in files],
    })
    print(json.dumps({"freeze": rec(own("freeze-v1.json")), "main": rec(own("candidate-v1.md")), "all_files": 13, "whole_obligations": 64}, indent=2))

if __name__ == "__main__":
    if sys.argv[1:] == ["verify"]:
        verify()
    elif not sys.argv[1:]:
        freeze()
    else:
        raise SystemExit("usage: admin-v1.py [verify]")
