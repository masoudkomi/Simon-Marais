"""NEW R30 review documentary byte/JSON/label code ONLY. No mathematics."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2021-B4/reviews/reasoning-coverage-synthesis-r30-review-2-"
AUTHOR = "problems/2021-B4/notes/reasoning-coverage-synthesis-r30-"
PARENT = "problems/2021-B4/reviews/coordinator-original-roots-r29-review-2-manifest-v1.json"
PAYLOADS = [PREFIX+s for s in ("initial.md", "sources-v1.json", "docadmin-v1.py", "baseline-v1.json")]

def now():
    return datetime.now(timezone.utc).isoformat()

def read(path):
    return json.loads((ROOT/path).read_text())

def row(path):
    data=(ROOT/path).read_bytes()
    return {"path":path,"bytes":len(data),"sha256":hashlib.sha256(data).hexdigest()}

def new(path,value):
    assert path.startswith(PREFIX)
    with (ROOT/path).open("x") as out:
        out.write(json.dumps(value,indent=2)+"\n")

def prepare():
    frozen=row(AUTHOR+"freeze-v1.json")
    assert frozen["bytes"]==2394 and frozen["sha256"]=="39ce9a61b63f77c40e3d83d2e229cccf9a10f1e75d5eb35151ec2327fdc05b8a"
    author=read(AUTHOR+"freeze-v1.json")
    for declared in author["payloads"]:
        assert row(declared["path"])==declared
    # These are the thirty-five immediate necessary files, not historical
    # verification inventories. Exclude the constructor's unrelated OWN note.
    necessary=read(AUTHOR+"baseline-v1.json")["guards"][:-1]
    assert len(necessary)==35
    for declared in necessary:
        assert row(declared["path"])==declared
    parent=row(PARENT)
    assert parent["bytes"]==2225 and parent["sha256"]=="d5836303ae27c88dde3beb5f8735940a11a885f71a1f0a5c6dd559a91528572e"
    guards=necessary+[frozen]+author["payloads"]+[parent]
    assert len(guards)==len({r["path"] for r in guards})==41
    new(PREFIX+"baseline-v1.json",{"captured_UTC":now(),"necessary_guards":guards,
        "occurrences":41,"unique_paths":41,"ONE_compact_OWN_parent":parent,
        "recursive_inventory":False,"mutable_map_guards":False,"mathematical_truth_check":False})
    print(json.dumps({"prepared_UTC":now(),"baseline":row(PREFIX+"baseline-v1.json")},indent=2))

def freeze():
    text=(ROOT/PAYLOADS[0]).read_text()
    assert all("|R30R2-"+str(i).zfill(2)+"|" in text for i in range(1,13))
    for declared in read(PREFIX+"baseline-v1.json")["necessary_guards"]:
        assert row(declared["path"])==declared
    new(PREFIX+"manifest-v1.json",{"frozen_UTC":now(),
        "reviewer":"/root/review_2022_complexity_r2","role":"OTHER initially blind WHOLE2",
        "ENTIRE_files":5,"ALL_obligations":12,"payloads":[row(p) for p in PAYLOADS],
        "ONE_compact_OWN_parent":row(PARENT),"guard_occurrences":41,"guard_unique_paths":41,
        "FULL_final_ALL4_payload_MODEL_readbacks_completed":True,
        "FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_REQUIRED":True,
        "corresponding_NEW_peer_findings_files_actual_inventory_hash_metadata_access":False,
        "findings_sealed_until_explicit_BOTH_release":True,
        "requested":{"model":"gpt-6.1-sol","reasoning":"max","inherited":True},
        "independent_effective_backend_readback":None,
        "quota":{"start_usedPercent":88,"usedPercent":89,"observed_UTC":"2026-10-19 05:48:47 UTC","resetsAt":1792874445,
                 "TOTAL_ceiling":90,"checkpoint_notify_at":89,"integration_reserve":True,"automatic_later_window":False}})
    print(json.dumps(row(PREFIX+"manifest-v1.json"),indent=2))

def verify():
    manifest=read(PREFIX+"manifest-v1.json")
    for declared in manifest["payloads"]:
        assert row(declared["path"])==declared
    baseline=read(PREFIX+"baseline-v1.json")
    for declared in baseline["necessary_guards"]:
        assert row(declared["path"])==declared
    assert baseline["ONE_compact_OWN_parent"]==manifest["ONE_compact_OWN_parent"]
    assert manifest["ENTIRE_files"]==5 and manifest["ALL_obligations"]==12
    print(json.dumps({"verified_UTC":now(),"SEPARATE_readonly_documentary_verify":"PASS",
        "ENTIRE_files":5,"ALL_obligations":12,"necessary_paths":41,
        "mathematical_computation_or_replay":False,"manifest":row(PREFIX+"manifest-v1.json")},indent=2))

if __name__=="__main__":
    {"prepare":prepare,"freeze":freeze,"verify":verify}[sys.argv[1]]()
