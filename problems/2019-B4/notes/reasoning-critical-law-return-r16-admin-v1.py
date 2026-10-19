#!/usr/bin/env python3
"""NEW CM16 documentary helper: exact bytes/JSON/literal labels only.

No obstruction count, moment, inequality, word, orbit, or source/old helper
is evaluated. Every write stays in the exclusive NEW CM16 namespace.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import re

ROOT=Path('/Users/uqmkamga/Documents/ChatGPT/Website')
P='problems/2019-B4/notes/reasoning-critical-law-return-r16-'
PARENT='problems/2021-B4/reviews/coordinator-dyadic-depth-return-r25-review-1-manifest-v1.json'
DIRECT=[
 ('problems/2019-B4/proofs/reviewed-reasoning-return-r7-v1.1.md','problems/2019-B4/reviews/reasoning-return-r7-acceptance','accepted_copy'),
 ('problems/2019-B4/proofs/reviewed-reasoning-cut-transfer-r6-v1.1.md','problems/2019-B4/reviews/reasoning-cut-transfer-r6-acceptance','accepted_copy'),
 ('problems/2019-B4/proofs/reviewed-moment-tail-v1.1.md','problems/2019-B4/reviews/moment-tail-acceptance','proof_register'),
 ('problems/2019-B4/proofs/reviewed-reasoning-full-law-return-r15-v1.1.md','problems/2019-B4/reviews/reasoning-full-law-return-r15-acceptance','accepted_copy')
]
COMPARISON=[
 'problems/2019-B4/reviews/reasoning-occupation-return-r1-acceptance',
 'problems/2019-B4/reviews/reasoning-area-return-r2-acceptance'
]
FILES=[P+s for s in ['candidate-v1.md','sources-v1.json','admin-v1.py','baseline-v1.json']]
MF=P+'freeze-v1.json'
EXPECTED={
 PARENT:'be2abbb9eff0536a97580726d0d0e9133ac10599ba3f652324900777d9b144a9',
 DIRECT[0][0]:'4fe222b8b1d89b6b3d66bb16c6a1985390d537eee55bb42bfefdb2d4821e351a',
 DIRECT[1][0]:'f43bd14fbec8b827dadbdbc33161e34aad3082f946a858bbf8d78880d0024ff8',
 DIRECT[2][0]:'b9d934da65eedf4514ef7883e29dda98ee846982e89c8e3ee677f2c96bff2ee8',
 DIRECT[3][0]:'50c41a30e785a51c7cfe51cfeb56a8f301a53b214c91d9cfa1cbd0d0bf526e31',
 'AGENTS.md':'28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff'
}
def now():return datetime.now(timezone.utc).isoformat()
def read(rel):return json.loads((ROOT/rel).read_text())
def fp(rel):
 data=(ROOT/rel).read_bytes()
 return {'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
def check(rec):assert fp(rec['path'])==rec,rec['path']
def new(rel,value):
 assert rel.startswith(P)
 with (ROOT/rel).open('x') as f:f.write(json.dumps(value,indent=2)+'\n')
def labels():
 found=re.findall(r'^\|CM16-(\d{2})\|',(ROOT/FILES[0]).read_text(),re.M)
 assert found==[f'{k:02}' for k in range(1,33)],'Literal ALL32 labels'
 return len(found)
def prepare():
 paths=['AGENTS.md','problems/2019-B4/statement.md']
 for body,authority,key in DIRECT:
  paths += [body,authority+'.md',authority+'.json']
  assert read(authority+'.json')[key]==fp(body),body
 for authority in COMPARISON:paths += [authority+'.md',authority+'.json']
 parent=read(PARENT)
 occurrences=[fp(rel) for rel in paths]+[fp(PARENT)]+parent['payloads']
 unique={}
 for rec in occurrences:
  check(rec);old=unique.setdefault(rec['path'],rec);assert old==rec,rec['path']
 for rel,sha in EXPECTED.items():assert unique[rel]['sha256']==sha,rel
 assert labels()==32;read(FILES[1])
 rows=[unique[key] for key in sorted(unique)]
 new(P+'baseline-v1.json',{
  'created_UTC':now(),'status':'Minimal direct guards; exact compact OWN parent binding, no historical expansion',
  'immutable_records':rows,'declared_occurrences':len(occurrences),'unique_paths':len(rows),
  'guard_digest_sha256':hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
  'immediate_OWN_parent':fp(PARENT),'historical_parent_inventory_expanded':False,
  'mutable_context_NOT_immutable_guard':fp('problems/2019-B4/research.md'),
  'NEW_R25_peer_access':False,'unrelated_root_R26_access':False,
  'mathematical_computation_or_old_replay':False
 })
 print(json.dumps({'prepared':True,'baseline':fp(P+'baseline-v1.json'),
                   'declared_occurrences':len(occurrences),'unique_paths':len(rows)}))
def freeze():
 b=read(P+'baseline-v1.json')
 for rec in b['immutable_records']:check(rec)
 read(FILES[1]);n=labels()
 new(MF,{
  'frozen_UTC':now(),'status':'candidate proof - unverified',
  'constructor':'/root/review_2017_coarsening_r1','constructor_excluded':True,
  'TWO_OTHER_initially_blind_ENTIRE_whole_audits_required':True,
  'claims':['CM16A critical residual moment restriction','CM16B actual full mean/count prefactors','CM16C actual full uniform mass bound'],
  'ENTIRE_files':5,'whole_obligations':n,'payloads':[fp(rel) for rel in FILES],
  'guard_occurrences':b['declared_occurrences'],'guard_unique_paths':b['unique_paths'],
  'guard_digest_sha256':b['guard_digest_sha256'],'immediate_OWN_parent':b['immediate_OWN_parent'],
  'FULL_final_ALL4_payload_MODEL_readbacks_completed':True,
  'FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_REQUIRED':True,
  'requested':{'model':'gpt-6.1-sol','reasoning':'max','inherited':True},
  'independent_effective_backend_readback':None,
  'quota':{'usedPercent':79,'observed_UTC':'2026-10-19 02:01:16 UTC',
           'windowDurationMins':10080,'resetsAt':1792874445,'ordinaryUsageAllowed':True,
           'TOTAL_ceiling':90,'reserve':True,'automatic_later_window_spending':False},
  'NEW_R25_peer_access':False,'unrelated_root_R26_access':False,
  'mathematical_program_CAS_scan_test_old_replay':False,'Git_shared_old_cache_mutation':False
 })
 print(json.dumps({'frozen':True,'manifest':fp(MF)}))
def verify():
 m=read(MF);b=read(P+'baseline-v1.json')
 for rec in m['payloads']+b['immutable_records']:check(rec)
 assert m['ENTIRE_files']==len(m['payloads'])+1==5
 assert m['whole_obligations']==labels()==32
 assert m['guard_digest_sha256']==b['guard_digest_sha256']
 print(json.dumps({'SEPARATE_readonly_verify_UTC':now(),'result':'PASS',
  'ENTIRE_files':5,'literal_obligations':32,'guard_occurrences':b['declared_occurrences'],
  'guard_unique_paths':b['unique_paths'],'manifest':fp(MF),'mathematical_verification_claimed':False}))
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('mode',choices=['prepare','freeze','verify'])
 args=parser.parse_args();{'prepare':prepare,'freeze':freeze,'verify':verify}[args.mode]()
