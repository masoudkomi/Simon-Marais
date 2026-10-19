#!/usr/bin/env python3
"""NEW R25 whole1 documentary helper; bytes/JSON/labels ONLY, no mathematics.

No source, constructor, old helper or freezer is replayed. No corresponding
NEW peer prefix or unrelated R26 exploration is inventoried/opened/hashed.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import re

ROOT=Path('/Users/uqmkamga/Documents/ChatGPT/Website')
P='problems/2021-B4/reviews/coordinator-dyadic-depth-return-r25-review-1-'
A='problems/2021-B4/notes/coordinator-dyadic-depth-return-r25-'
PARENT='problems/2022-B4/reviews/reasoning-itinerary-return-r12-review-2-manifest-v1.json'
FILES=[P+s for s in ['initial-v1.md','sources-v1.json','admin-v1.py','baseline-v1.json']]
MF=P+'manifest-v1.json'
EXPECTED={
 A+'candidate-v1.md':'4ebcb8df634d91edc5b380effc883f795ce817dbdd992c5182da1f659eb203cc',
 A+'freeze-v1.json':'fa65dcb84789d0db25218940ff5957e234d10cf30a699973d255c9b3c55ab5b6',
 PARENT:'abb6eac674211a556b13b48842c6e5af8b8903b2ec14047ebdf978831e24a36b'
}
def now(): return datetime.now(timezone.utc).isoformat()
def read(rel): return json.loads((ROOT/rel).read_text())
def fp(rel):
 b=(ROOT/rel).read_bytes()
 return {'path':rel,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def check(rec): assert fp(rec['path'])==rec,rec['path']
def new(rel,value):
 assert rel.startswith(P)
 with (ROOT/rel).open('x') as f:f.write(json.dumps(value,indent=2)+'\n')
def labels():
 found=re.findall(r'^\|O(\d{2})\|',(ROOT/FILES[0]).read_text(),re.M)
 assert found==[f'{i:02}' for i in range(1,29)],'Literal ALL28 labels'
 return len(found)
def prepare():
 af=read(A+'freeze-v1.json');ab=read(A+'baseline-v1.json');parent=read(PARENT)
 occurrences=[fp(A+'freeze-v1.json')]+af['payloads']+ab['necessary_immutable_records']
 occurrences+=[fp(PARENT)]+parent['payloads']
 unique={}
 for rec in occurrences:
  check(rec)
  old=unique.setdefault(rec['path'],rec)
  assert old==rec,rec['path']
 for rel,sha in EXPECTED.items():assert unique[rel]['sha256']==sha,rel
 assert af['whole_obligations']==labels()==28
 read(FILES[1])
 rows=[unique[k] for k in sorted(unique)]
 new(P+'baseline-v1.json',{
  'created_UTC':now(),'status':'Exact necessary inputs and compact OWN parent binding',
  'immutable_records':rows,'declared_occurrences':len(occurrences),'unique_paths':len(rows),
  'guard_digest_sha256':hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
  'immediate_OWN_parent':fp(PARENT),'historical_parent_inventory_expanded':False,
  'NEW_R25_peer_actual_inventory_content_hash_metadata_access':False,
  'unrelated_root_R26_exploration_access':False,'mathematical_computation_or_old_replay':False
 })
 print(json.dumps({'prepared':True,'baseline':fp(P+'baseline-v1.json'),
                   'declared_occurrences':len(occurrences),'unique_paths':len(rows)}))
def freeze():
 b=read(P+'baseline-v1.json')
 for rec in b['immutable_records']:check(rec)
 read(FILES[1]);n=labels()
 new(MF,{
  'frozen_UTC':now(),'status':'OTHER initially blind ENTIRE WHOLE1; findings SEALED until explicit BOTH',
  'reviewer':'/root/review_2017_coarsening_r1','NEW_constructor':False,'whole_obligations':n,
  'ENTIRE_files':5,'payloads':[fp(rel) for rel in FILES],
  'guard_occurrences':b['declared_occurrences'],'guard_unique_paths':b['unique_paths'],
  'guard_digest_sha256':b['guard_digest_sha256'],'immediate_OWN_parent':b['immediate_OWN_parent'],
  'FULL_final_ALL4_payload_MODEL_readbacks_completed':True,
  'FULL_manifest_MODEL_readback_then_SEPARATE_readonly_verify_REQUIRED':True,
  'NEW_R25_peer_actual_inventory_content_hash_metadata_access':False,
  'unrelated_root_R26_exploration_access':False,
  'requested':{'model':'gpt-6.1-sol','reasoning':'max','inherited':True},
  'independent_effective_backend_readback':None,
  'quota':{'usedPercent':78,'observed_UTC':'2026-10-19 01:40:30 UTC',
           'windowDurationMins':10080,'resetsAt':1792874445,'ordinaryUsageAllowed':True,
           'TOTAL_ceiling':90,'reserve':True,'automatic_later_window_spending':False},
  'mathematical_program_CAS_scan_test_old_replay':False,'Git_shared_old_cache_mutation':False
 })
 print(json.dumps({'frozen':True,'manifest':fp(MF)}))
def verify():
 m=read(MF);b=read(P+'baseline-v1.json')
 for rec in m['payloads']+b['immutable_records']:check(rec)
 assert m['whole_obligations']==labels()==28
 assert m['ENTIRE_files']==len(m['payloads'])+1==5
 assert m['guard_digest_sha256']==b['guard_digest_sha256']
 print(json.dumps({'SEPARATE_readonly_verify_UTC':now(),'result':'PASS',
  'ENTIRE_files':5,'literal_obligations':28,'guard_occurrences':b['declared_occurrences'],
  'guard_unique_paths':b['unique_paths'],'manifest':fp(MF),'mathematical_verification_claimed':False}))
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('mode',choices=['prepare','freeze','verify'])
 args=parser.parse_args();{'prepare':prepare,'freeze':freeze,'verify':verify}[args.mode]()
