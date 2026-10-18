"""NEW R22 whole2 documentary freeze only; no mathematical code or old replay."""
from pathlib import Path
import datetime, hashlib, json, sys

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
STEM = "reasoning-center-return-r22-review-2-"
MANIFEST = HERE / (STEM + "manifest-v1.json")
PAYLOADS = [HERE / (STEM + name) for name in
            ("report-v1.md", "sources-v1.json", "admin-v1.py")]
AUTHOR = ROOT / "problems/2021-B4/notes/reasoning-center-return-r22-freeze-v1.json"

def fp(path):
    data = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)), "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}

def check(row):
    assert fp(ROOT / row["path"]) == row, row["path"]

def inputs():
    author = json.loads(AUTHOR.read_text())
    for row in author["payloads"]:
        check(row)
    paths = [AUTHOR] + [ROOT / row["path"] for row in author["payloads"]]
    paths += [ROOT / "AGENTS.md", ROOT / "problems/2021-B4/statement.md"]
    for version in (18, 20, 21):
        base = ROOT / "problems/2021-B4"
        paths.append(base / f"proofs/reviewed-reasoning-center-return-r{version}-v1.1.md")
        for ext in ("md", "json"):
            paths.append(base / f"reviews/reasoning-center-return-r{version}-acceptance.{ext}")
    return [fp(path) for path in paths]

if sys.argv[1:] == ["freeze"]:
    assert not MANIFEST.exists(), "preserve prior manifest"
    source = json.loads(PAYLOADS[1].read_text())
    assert source["peer_NEW_findings_files_actual_inventory_hash_metadata_accessed_before_BOTH"] is False
    record = {"frozen_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "reviewer": "/root", "role": "OTHER initially blind WHOLE2",
              "whole_obligations": 48, "ENTIRE_files": 4,
              "payloads": [fp(path) for path in PAYLOADS], "inputs": inputs(),
              "FULL_final_ALL3_payload_model_readback_completed": True,
              "FULL_manifest_model_readback_then_SEPARATE_verify_required": True,
              "NEW_peer_findings_files_actual_inventory_hash_metadata_accessed": False,
              "substantive_defects_repair_required": False,
              "all_48_issues_sources_log_code_metadata_complete": True,
              "mathematical_program_CAS_scan_test_old_replay": False}
    MANIFEST.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps(fp(MANIFEST)))
elif sys.argv[1:] == ["verify"]:
    record = json.loads(MANIFEST.read_text())
    for row in record["payloads"] + record["inputs"]:
        check(row)
    assert inputs() == record["inputs"]
    print(json.dumps({"separate_verify_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                      "status": "PASS", "ENTIRE_files": 4, "whole_obligations": 48,
                      "manifest": fp(MANIFEST)}))
else:
    raise SystemExit("freeze or verify only; documentary checks")
