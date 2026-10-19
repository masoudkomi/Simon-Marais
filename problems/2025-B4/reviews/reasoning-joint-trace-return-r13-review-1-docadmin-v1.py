#!/usr/bin/env python3
"""NEW documentary JT13 whole1 helper. No mathematical execution.
Author/old helpers are NEVER imported or executed. No peer inventory.
prepare; FULL final ALL4 MODEL reads; freeze; FULL manifest MODEL read;
SEPARATE read-only verify. Writes only this NEW exclusive prefix.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,sys

ROOT=Path('/Users/uqmkamga/Documents/ChatGPT/Website')
P='problems/2025-B4/reviews/reasoning-joint-trace-return-r13-review-1-'
BASE=P+'baseline-v1.json'
MAN=P+'manifest-v1.json'
PAYLOADS=[P+x for x in ['initial-v1.md','sources-v1.json','docadmin-v1.py','baseline-v1.json']]
AP='problems/2025-B4/notes/reasoning-joint-trace-return-r13-'
AUTHOR=[(AP+'candidate-v1.md',17562,'0a66da03cea5cde313db07f4c4c48bd3047276a1d56449cf2ca3272db4fda79f'),(AP+'sources-v1.json',3421,'e7976ded20465664c0eb3b54cee19c66fd716f3152e6250fb95622e0a466edcf'),(AP+'admin-v1.py',3916,'414e592a393fe772017dbc0a12c2e03b39f60eb5b47ab1d688d4ab5dd5956c6e'),(AP+'baseline-v1.json',2900,'138f37421858eb962cf25dc03d67f499d68823813b5f1a48c65d2d550b8e1dd5'),(AP+'freeze-v1.json',2115,'c797b85ac45ac25e2c8155a62c2d768f721538650d97c925dcd1210502a22075')]
STEMS=['reasoning-exception-return-r12','reasoning-compatible-return-r10','reasoning-global-return-r11']
PARENT='problems/2022-B4/notes/reasoning-physical-return-r13-freeze-v1.json'

def now():return datetime.now(timezone.utc).isoformat()
def load(p):return json.loads((ROOT/p).read_text())
def fp(p):
    b=(ROOT/p).read_bytes()
    return {'path':p,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def digest(rows):
    b=json.dumps(sorted(rows,key=lambda x:x['path']),sort_keys=True,separators=(',',':')).encode()
    return hashlib.sha256(b).hexdigest()
def new(p,data):
    assert p in [BASE,MAN]
    with (ROOT/p).open('x')as out:out.write(json.dumps(data,indent=2)+'\n')
def labels():
    txt=(ROOT/PAYLOADS[0]).read_text()
    found=re.findall(r'^\|(JT13-\d{2})\|',txt,re.M)
    assert found==['JT13-%02d'%i for i in range(1,33)]
    return len(found)
def guards():
    paths=['AGENTS.md','problems/2025-B4/statement.md']
    for p,n,h in AUTHOR:
        assert fp(p)=={'path':p,'bytes':n,'sha256':h}
        paths.append(p)
    for s in STEMS:
        a='problems/2025-B4/reviews/'+s+'-acceptance.json'
        value=load(a)
        assert value['status']=='proved, independently reviewed scoped partial result'
        assert fp(value['accepted_copy']['path'])==value['accepted_copy']
        paths.extend([value['accepted_copy']['path'],a[:-4]+'md',a])
    assert fp(PARENT)=={'path':PARENT,'bytes':2526,'sha256':'256bedd300fa0ce8ebe1ee1f69d47e1246a7c5c2c50f802e6d3d2d2ce5e6c1c6'}
    paths.append(PARENT)
    assert len(paths)==len(set(paths))==17
    return [fp(p)for p in paths]

mode=sys.argv[1]if len(sys.argv)>1 else''
if mode=='prepare':
    rows=guards();parent=load(PARENT)
    new(BASE,{'captured_UTC':now(),'necessary_immutable_records':rows,'occurrences':17,'unique_paths':17,'canonical_deduplicated_sha256':digest(rows),'ONE_OWN_parent_manifest':fp(PARENT),'parent_declared_summary':{'ENTIRE_files':parent['ENTIRE_files'],'ALL_obligations':parent['ALL_obligations'],'guard_occurrences':parent['guard_summary']['occurrences'],'guard_unique_paths':parent['guard_summary']['unique_paths']},'recursive_inventory_expansion':False,'mutable_map_guards':False,'NEW_JT13_peer_access':False,'NEW_PH13_peer_or_root_R26_access':False,'mathematical_truth_checked_by_code':False})
    print(json.dumps({'baseline':fp(BASE),'literal_obligations':labels(),'necessary_guards':17}))
elif mode=='freeze':
    assert '--FULL-final-ALL4-MODEL-readbacks-completed'in sys.argv
    rows=guards();assert load(BASE)['necessary_immutable_records']==rows
    new(MAN,{'frozen_UTC':now(),'status':'sealed initially blind whole1; explicit BOTH release required','reviewer':'C /root/review_2017_coarsening_r1','ENTIRE_files':5,'ALL_obligations':labels(),'payloads':[fp(p)for p in PAYLOADS],'guard_summary':{'occurrences':17,'unique_paths':17,'canonical_deduplicated_sha256':digest(rows)},'ONE_OWN_parent_manifest':fp(PARENT),'FULL_final_ALL4_payload_MODEL_readbacks_completed':True,'FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_REQUIRED':True,'NEW_JT13_peer_access_before_entire_freeze':False,'NEW_PH13_peer_or_root_R26_access':False,'requested':{'model':'gpt-6.1-sol','reasoning':'max','inherited':True},'independent_effective_backend_readback':None,'start_quota':{'usedPercent':85,'observed_UTC':'2026-10-19 03:46:14 UTC','resetsAt':1792874445,'TOTAL_ceiling':90,'reserve':True,'automatic_later_window':False},'no_mathematical_executable_or_old_replay':True,'author_documentary_code_executed':False,'Git_shared_old_cache_mutation':False})
    print(json.dumps({'manifest':fp(MAN)}))
elif mode=='verify':
    before=fp(MAN);m=load(MAN)
    for r in m['payloads']:assert fp(r['path'])==r
    rows=guards();assert load(BASE)['necessary_immutable_records']==rows
    assert m['guard_summary']['canonical_deduplicated_sha256']==digest(rows)
    assert m['ALL_obligations']==labels()==32 and m['ENTIRE_files']==5
    assert fp(MAN)==before
    print(json.dumps({'SEPARATE_readonly_verify_UTC':now(),'PASS':True,'ENTIRE_files':5,'ALL_obligations':32,'necessary_guards':17,'manifest':before,'writes':0,'mathematics_certified':False}))
else:raise SystemExit('prepare/freeze/verify: documentary operations only')
