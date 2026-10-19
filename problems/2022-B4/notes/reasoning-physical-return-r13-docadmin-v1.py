#!/usr/bin/env python3
"""NEW documentary PH13 admin only: hashes, JSON and literal labels.
No mathematical executable, source/author helper import, or old replay.
init -> final ALL4 MODEL reads -> freeze -> FULL manifest MODEL read ->
SEPARATE read-only verify. Exclusive new prefix; refuse overwrite.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

ROOT=Path('/Users/uqmkamga/Documents/ChatGPT/Website')
P='problems/2022-B4/notes/reasoning-physical-return-r13-'
PAYLOAD=['candidate-v1.md','sources-v1.json','docadmin-v1.py','baseline-v1.json']
BASE=ROOT/(P+'baseline-v1.json')
FREEZE=ROOT/(P+'freeze-v1.json')
PARENT='problems/2020-B4/reviews/reasoning-global-return-r20-review-1-manifest-v1.json'
AUTHORITIES=[
 'problems/2022-B4/reviews/reasoning-itinerary-return-r12-acceptance',
 'problems/2022-B4/reviews/reasoning-dynamics-return-r9-acceptance',
 'problems/2022-B4/reviews/reasoning-fiber-return-r5-acceptance'
]
BODY=[
 'problems/2022-B4/proofs/reviewed-reasoning-itinerary-return-r12-v1.1.md',
 'problems/2022-B4/proofs/reviewed-reasoning-dynamics-return-r9-v1.1.md',
 'problems/2022-B4/proofs/reviewed-reasoning-fiber-return-r5-v1.1.md'
]
PATHS=['AGENTS.md','problems/2022-B4/statement.md']+BODY+[a+e for a in AUTHORITIES for e in ['.md','.json']]+[PARENT]

def now(): return datetime.now(timezone.utc).isoformat()
def rec(path):
    b=(ROOT/path).read_bytes()
    return {'path':path,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def digest(rows):
    b=json.dumps(sorted(rows,key=lambda x:x['path']),sort_keys=True,separators=(',',':')).encode()
    return hashlib.sha256(b).hexdigest()
def labels():
    txt=(ROOT/(P+'candidate-v1.md')).read_text()
    ids=re.findall(r'^\|(PH13-\d{2})\|',txt,re.M)
    assert ids==['PH13-%02d'%n for n in range(1,33)]
    return len(ids)
def guarded():
    rows=[rec(p) for p in PATHS]
    assert len(rows)==len({r['path'] for r in rows})==12
    for a,b in zip(AUTHORITIES,BODY):
        assert json.loads((ROOT/(a+'.json')).read_text())['accepted_copy']==rec(b)
    assert rec(PARENT)=={'path':PARENT,'bytes':2361,'sha256':'8583427bbff1d07c8e95506d46badb2babb7a825196ed5073be5219912b8fbf9'}
    return rows

mode=sys.argv[1] if len(sys.argv)>1 else ''
if mode=='init':
    assert not BASE.exists() and not FREEZE.exists()
    rows=guarded()
    parent=json.loads((ROOT/PARENT).read_text())
    data={'schema':'PH13-compact-baseline-v1','created_UTC':now(),'immutable_guards':rows,'occurrences':12,'unique_paths':12,'canonical_deduplicated_sha256':digest(rows),'ONE_OWN_immediate_parent_manifest':rec(PARENT),'parent_declared_summary':{'ENTIRE_files':parent['ENTIRE_files'],'ALL_obligations':parent['ALL_obligations'],'guard_occurrences':parent['guard_summary']['occurrences'],'guard_unique_paths':parent['guard_summary']['unique_paths']},'recursive_parent_expansion':False,'mutable_maps_added_as_guards':False,'corresponding_NEW_JM16_peer_access':False,'root_R26_exploration_access':False,'mathematical_executable_or_old_replay':False}
    BASE.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'initialized':str(BASE.relative_to(ROOT)),'guards':12,'literal_obligations':labels()}))
elif mode=='freeze':
    assert BASE.exists() and not FREEZE.exists()
    rows=guarded()
    assert json.loads(BASE.read_text())['immutable_guards']==rows
    data={'schema':'PH13-entire-author-freeze-v1','frozen_UTC':now(),'status':'candidate proof - unverified','constructor':'C /root/review_2017_coarsening_r1','constructor_excluded':True,'TWO_OTHER_initially_blind_ENTIRE_whole_audits_required':True,'claims':['PH13A','PH13B','PH13C','PH13D'],'ALL_obligations':labels(),'ENTIRE_files':5,'payloads':[rec(P+n) for n in PAYLOAD],'guard_summary':{'occurrences':12,'unique_paths':12,'canonical_deduplicated_sha256':digest(rows)},'ONE_OWN_parent_manifest':rec(PARENT),'FULL_final_ALL4_payload_MODEL_readbacks_completed_before_manifest':True,'FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_required':True,'requested':{'model':'gpt-6.1-sol','reasoning':'max','inherited':True},'independent_effective_backend_readback':None,'quota':{'own_direct_usedPercent':84,'observed_UTC':'2026-10-19 02:50:53 UTC','windowDurationMins':10080,'ordinaryUsageAllowed':True,'legacy_by_limit_agree':True,'resetsAt':1792874445,'TOTAL_ceiling':90,'review_integration_reserve':True,'automatic_later_window_spending':False},'root_NEW_inference_contribution':False,'corresponding_NEW_JM16_peer_access':False,'root_R26_exploration_access':False,'mathematical_program_scan_CAS_test_or_old_replay':False,'Git_shared_old_cache_mutation':False}
    FREEZE.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(rec(P+'freeze-v1.json')))
elif mode=='verify':
    data=json.loads(FREEZE.read_text())
    assert data['ALL_obligations']==labels()==32 and data['ENTIRE_files']==5
    for row in data['payloads']: assert rec(row['path'])==row
    rows=guarded()
    assert json.loads(BASE.read_text())['immutable_guards']==rows
    assert data['guard_summary']['canonical_deduplicated_sha256']==digest(rows)
    assert data['ONE_OWN_parent_manifest']==rec(PARENT)
    print(json.dumps({'SEPARATE_readonly_verify_UTC':now(),'PASS':True,'ENTIRE_files':5,'ALL_obligations':32,'immutable_guards':12,'freeze':rec(P+'freeze-v1.json')}))
else:
    raise SystemExit('Use init, freeze, verify: documentary operations only.')
