"""NEW fixed-path documentary SHA/JSON/literal-row helper; no mathematics.
No source/author/old replay, network, peer inventory, Git or subprocess.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2021-B4/reviews/coordinator-contact-return-r27-review-2-"
BASELINE = PREFIX + "baseline-v1.json"
MANIFEST = PREFIX + "manifest-v1.json"
PAYLOADS = [PREFIX+s for s in ["initial-v1.md","sources-v1.json","admin-v1.py","baseline-v1.json"]]
EXPECTED = [
 ("AGENTS.md",4707,"28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"),
 ("problems/2021-B4/statement.md",1745,"5cd9750a2458191370590120fb4ae7d547740784eb1de38ee9e2e7890a2fabed"),
 ("problems/2021-B4/notes/coordinator-contact-return-r27-candidate-v1.md",18009,"ef49a2b0a886f4e2c061e9bd381daa440992361800c015c32b4650a18a574984"),
 ("problems/2021-B4/notes/coordinator-contact-return-r27-sources-v1.json",2177,"49c3760c42b786aa08923248b6aca55bbe6694d0c394c6526eb7b3402bbf4f10"),
 ("problems/2021-B4/notes/coordinator-contact-return-r27-admin-v1.py",3560,"59b295cfc263329e346fa8f8b58a3917584dace6f97e6ffacd96e3e698d32413"),
 ("problems/2021-B4/notes/coordinator-contact-return-r27-baseline-v1.json",2822,"8361f75a73e50de4bec354661cc77c13b960994911cade8d177a517aab523f49"),
 ("problems/2021-B4/notes/coordinator-contact-return-r27-freeze-v1.json",1634,"8b0acf6aba3c262f2dff4810ade1625c5b3645e888eb9069ed8a3e509c6d5311"),
 ("problems/2021-B4/proofs/reviewed-reasoning-deep-return-r24-v1.1.md",27431,"a52fcb31da9b494659d29b1ea0b587baba3a096264688ac6989e3d98ed578946"),
 ("problems/2021-B4/reviews/reasoning-deep-return-r24-acceptance.md",5485,"c86814838459ce13a88137c389b5aa8715630b8ce3589fcf49810be9126f1050"),
 ("problems/2021-B4/reviews/reasoning-deep-return-r24-acceptance.json",3495,"8a41ba05fd3851890db2d2d94b946101de03905c08312b089d5346ef1f0e5296"),
 ("problems/2021-B4/proofs/reviewed-coordinator-dyadic-return-r26-v1.1.md",26334,"1e719102a7e202687e5ba65fb373d9dee4467f8b175a2ef94b60e73c948098c6"),
 ("problems/2021-B4/reviews/coordinator-dyadic-return-r26-acceptance.md",5781,"873e2f155fd303acd5c2f83d60f522116959f0300dcad1c7c113e1454cb7856f"),
 ("problems/2021-B4/reviews/coordinator-dyadic-return-r26-acceptance.json",3457,"b33ee6e5e1ed46f5ab88ebab723c760c13f91f53a4a674a518bb918f93f15cc8"),
 ("problems/2021-B4/notes/coordinator-contact-return-r27-exploration-unverified.md",6042,"e3eaba4ed52fdc5d7f04ac0dec1645fa1376c1eccda4f9d08289512aa8eb7449"),
 ("problems/2017-B4/reviews/reasoning-joint-mass-return-r16-review-1-manifest-v1.json",2286,"2a55c9f3d0e8d883a50ae40723ae603ed72592e5f679fe10e50b2476e31fbf39")
]

def now(): return datetime.now(timezone.utc).isoformat()
def fp(rel):
    b=(ROOT/rel).read_bytes()
    return dict(path=rel,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def read(rel): return json.loads((ROOT/rel).read_text())
def new(rel,value):
    assert rel in (BASELINE,MANIFEST)
    with (ROOT/rel).open("x") as out:
        out.write(json.dumps(value,indent=2,ensure_ascii=False)+"\n")
def guards():
    records=[]
    for rel,size,sha in EXPECTED:
        record=fp(rel)
        assert record["bytes"]==size and record["sha256"]==sha,record
        records.append(record)
    assert len(records)==len({r["path"] for r in records})==15
    return records
def labels():
    text=(ROOT/PAYLOADS[0]).read_text()
    for i in range(1,33): assert text.count(f"|R27-{i:02d}|")==1
    assert read(PAYLOADS[1])["ALL_obligations"]==32
    return 32
def prepare():
    records=guards()
    new(BASELINE,dict(captured_UTC=now(),necessary_immutable_records=records,
        guard_occurrences=15,guard_unique_paths=15,ONE_exact_OWN_parent=records[-1],
        recursive_inventory_expansion=False,living_map_guards=False,
        corresponding_NEW_R27_peer_access=False,NEW_R28_access=False,
        mathematical_truth_checked_by_code=False))
    print(json.dumps(dict(baseline=fp(BASELINE),guards=15)))
def check_base():
    b=read(BASELINE)
    assert b["necessary_immutable_records"]==guards()
    return b
def freeze():
    assert "--FULL-final-ALL4-MODEL-readbacks-completed" in sys.argv
    b=check_base();count=labels()
    value=dict(frozen_UTC=now(),status="sealed OTHER independent WHOLE2 initial; not promotion",
        reviewer="/root/review_2022_complexity_r2",constructor="/root",constructor_excluded=True,
        claims=["R27A","R27B"],ENTIRE_files=5,ALL_obligations=count,
        payloads=[fp(p) for p in PAYLOADS],guard_occurrences=15,guard_unique_paths=15,
        ONE_exact_OWN_parent=b["ONE_exact_OWN_parent"],
        FULL_final_ALL4_payload_MODEL_readbacks_completed=True,
        FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_REQUIRED=True,
        findings_sealed_until_explicit_BOTH=True,corresponding_NEW_peer_access=False,
        NEW_R28_access=False,no_mathematical_executable_or_old_replay=True,
        requested=dict(model="gpt-6.1-sol",reasoning="max",inherited=True),
        independent_effective_backend_readback=None,
        quota=dict(usedPercent=83,observed_UTC="2026-10-19 02:45:56 UTC",
                   resetsAt=1792874445,TOTAL_ceiling=90,reserve=True,automatic_later_window=False))
    new(MANIFEST,value)
    print(json.dumps(dict(manifest=fp(MANIFEST),frozen_UTC=value["frozen_UTC"])))
def verify():
    before=fp(MANIFEST);f=read(MANIFEST);check_base()
    assert f["payloads"]==[fp(p) for p in PAYLOADS]
    assert f["ALL_obligations"]==labels()==32 and f["ENTIRE_files"]==5
    assert before==fp(MANIFEST)
    print(json.dumps(dict(SEPARATE_readonly_verify_UTC=now(),status="PASS",
        ENTIRE_files=5,literal_obligations=32,necessary_immutable_paths=15,
        manifest=before,writes=0,mathematics_certified=False)))
if __name__=="__main__":
    assert len(sys.argv)>1 and sys.argv[1] in ("prepare","freeze","verify")
    {"prepare":prepare,"freeze":freeze,"verify":verify}[sys.argv[1]]()
