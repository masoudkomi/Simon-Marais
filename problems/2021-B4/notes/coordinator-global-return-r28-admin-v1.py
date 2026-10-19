"""NEW R28 documentary bytes/JSON/literal labels only; no mathematics.
Never executes the finite mathematical certificate or any old helper.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,sys
ROOT=Path(__file__).resolve().parents[3]
P='problems/2021-B4/notes/coordinator-global-return-r28-'
PAYLOADS=[P+s for s in ['candidate-v1.md','sources-v1.json','certificate-v1.py','admin-v1.py','baseline-v1.json']]
MF=P+'freeze-v1.json'
PARENT='problems/2021-B4/notes/coordinator-contact-return-r27-freeze-v1.json'
GUARDS=['AGENTS.md','problems/2021-B4/statement.md',PARENT]
for name in ['reasoning-deep-return-r24','coordinator-dyadic-return-r26','coordinator-contact-return-r27']:
    GUARDS += ['problems/2021-B4/proofs/reviewed-'+name+'-v1.1.md']
    GUARDS += ['problems/2021-B4/reviews/'+name+'-acceptance'+s for s in ['.md','.json']]
def now():return datetime.now(timezone.utc).isoformat()
def fp(path):
    b=(ROOT/path).read_bytes();return dict(path=path,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def read(path):return json.loads((ROOT/path).read_text())
def check(row):assert fp(row['path'])==row,row['path']
def new(path,obj):
    assert path.startswith(P)
    with(ROOT/path).open('x')as f:json.dump(obj,f,indent=2);f.write('\n')
def labels():
    ids=re.findall(r'^\|O(\d{2})\|',(ROOT/PAYLOADS[0]).read_text(),re.M)
    assert ids==[f'{i:02}'for i in range(1,25)]
    return len(ids)
def prepare():
    assert len(GUARDS)==len(set(GUARDS))==12
    new(P+'baseline-v1.json',dict(created_UTC=now(),necessary_immutable_records=[fp(x)for x in GUARDS],ONE_compact_OWN_parent=fp(PARENT),recursive_inventory_expansion=False,mutable_map_guards=False,whole_obligations=labels(),requested=dict(model='gpt-6.1-sol',reasoning='max'),independent_effective_backend_readback=None))
    print(json.dumps(dict(prepared=True,necessary_paths=12,baseline=fp(P+'baseline-v1.json'))))
def freeze():
    assert '--FULL-final-ALL5-MODEL-readbacks-completed' in sys.argv
    base=read(P+'baseline-v1.json')
    for row in base['necessary_immutable_records']:check(row)
    read(P+'sources-v1.json');assert labels()==24
    new(MF,dict(frozen_UTC=now(),status='candidate proof - unverified',constructor='/root',constructor_excluded=True,claims=['R28A','R28B'],ENTIRE_files=6,whole_obligations=24,payloads=[fp(x)for x in PAYLOADS],necessary_paths=12,ONE_compact_OWN_parent=base['ONE_compact_OWN_parent'],FULL_final_ALL5_payload_MODEL_readbacks_completed=True,FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_REQUIRED=True,two_OTHER_initially_blind_ENTIRE_whole_audits_required=True,finite_mathematical_certificate_used=True,documentary_helper_checks_mathematical_truth=False,requested=dict(model='gpt-6.1-sol',reasoning='max'),independent_effective_backend_readback=None,quota=dict(usedPercent=86,observed_UTC='2026-10-19 03:56:09 UTC',resetsAt=1792874445,TOTAL_ceiling=90,reserve=True,automatic_later_window=False)))
    print(json.dumps(dict(frozen_UTC=read(MF)['frozen_UTC'],manifest=fp(MF))))
def verify():
    m=read(MF)
    for row in m['payloads']+read(P+'baseline-v1.json')['necessary_immutable_records']:check(row)
    assert m['ENTIRE_files']==len(m['payloads'])+1==6 and m['whole_obligations']==labels()==24
    print(json.dumps(dict(SEPARATE_readonly_verify_UTC=now(),status='PASS',ENTIRE_files=6,whole_obligations=24,manifest=fp(MF),candidate=fp(PAYLOADS[0]),writes=0,mathematical_truth_certified=False)))
if __name__=='__main__':{'prepare':prepare,'freeze':freeze,'verify':verify}[sys.argv[1]]()
