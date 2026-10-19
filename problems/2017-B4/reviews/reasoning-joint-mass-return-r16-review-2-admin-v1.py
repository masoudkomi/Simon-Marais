#!/usr/bin/env python3
"""NEW JM16 WHOLE2 documentary byte/JSON/literal-label binding only.

No geometry, path, probability, count or asymptotic computation. No old
or author/source helper is executed. Exclusive NEW review writes only.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import re

ROOT=Path('/Users/uqmkamga/Documents/ChatGPT/Website')
P='problems/2017-B4/reviews/reasoning-joint-mass-return-r16-review-2-'
A='problems/2017-B4/notes/reasoning-joint-mass-return-r16-'
PARENT='problems/2020-B4/reviews/reasoning-global-return-r20-review-2-manifest-v1.json'
DIRECT=[
 ('problems/2017-B4/proofs/reviewed-'+name+'-v1.1.md','problems/2017-B4/reviews/'+name+'-acceptance')
 for name in ['reasoning-pressure-return-r11','reasoning-concentration-return-r12','reasoning-lower-return-r14','reasoning-joint-return-r15']
]
FILES=[P+s for s in ['initial-v1.md','sources-v1.json','admin-v1.py','baseline-v1.json']]
MF=P+'manifest-v1.json'
EXPECTED={
 A+'candidate-v1.md':(22236,'f202e568a7f48810bfe0d3b567338477c91f09023267eb1e15b356722737b886'),
 A+'freeze-v1.json':(2455,'487d92acc4bb6fe433b656473e487f88bcf17cf6341d9a15364ed6f9be3571ef'),
 PARENT:(2824,'e8e7c2c42711ba47036f0569bf92bc993ee1bf13f1f8d664e62683b21da46b4d')
}
def now():return datetime.now(timezone.utc).isoformat()
def read(rel):return json.loads((ROOT/rel).read_text())
def fp(rel):
 data=(ROOT/rel).read_bytes()
 return {'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
def check(rec):assert fp(rec['path'])==rec,rec['path']
def new(rel,obj):
 assert rel.startswith(P)
 with (ROOT/rel).open('x') as f:f.write(json.dumps(obj,indent=2)+'\n')
def digest(rows):return hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def labels():
 ids=re.findall(r'^\|JM16-O(\d{2})\|',(ROOT/FILES[0]).read_text(),re.M)
 assert ids==[f'{i:02}' for i in range(1,33)],'ALL32 literal outcomes'
 return len(ids)
def prepare():
 author=read(A+'freeze-v1.json');ab=read(A+'baseline-v1.json');parent=read(PARENT)
 occurrences=[fp(A+'freeze-v1.json')]+author['payloads']+ab['necessary_guards_ONCE']
 unique={}
 for rec in occurrences:
  old=unique.setdefault(rec['path'],rec);assert old==rec,rec['path']
 for body,authority in DIRECT:
  assert read(authority+'.json')['accepted_copy']==fp(body),body
  for path in [body,authority+'.md',authority+'.json']:
   assert path in unique and unique[path]==fp(path),path
 occurrences += [fp(PARENT)]+parent['payloads']
 for rec in [fp(PARENT)]+parent['payloads']:
  old=unique.setdefault(rec['path'],rec);assert old==rec,rec['path']
 for rec in unique.values():check(rec)
 for path,(size,sha) in EXPECTED.items():
  assert unique[path]['bytes']==size and unique[path]['sha256']==sha,path
 assert author['ALL_obligations']==labels()==32
 assert author['ENTIRE_files']==len(author['payloads'])+1==5
 assert parent['ENTIRE_files']==len(parent['payloads'])+1==5
 read(FILES[1]);rows=[unique[k] for k in sorted(unique)]
 new(P+'baseline-v1.json',{
  'created_UTC':now(),'status':'Necessary immutable guards ONCE, ONE exact OWN parent, no recursive ET12/CM16 or historical inventory',
  'immutable_records':rows,'declared_occurrences':len(occurrences),'unique_paths':len(rows),
  'canonical_deduplicated_sha256':digest(rows),'compact_OWN_parent':fp(PARENT),
  'OWN_parent_guard_summary_NOT_expanded':parent['guard_summary'],
  'mutable_map_guards':False,
  'NEW_JM16_peer_finding_file_actual_inventory_hash_metadata_commentary_access':False,
  'R20_BOTH_release_received_during_audit':True,'R20_peer_file_access':False,'root_R27_access':False,
  'mathematical_computation_or_old_author_helper_replay':False
 })
 print(json.dumps({'prepared':True,'baseline':fp(P+'baseline-v1.json'),
                   'declared_occurrences':len(occurrences),'unique_paths':len(rows)}))
def freeze():
 b=read(P+'baseline-v1.json')
 for rec in b['immutable_records']:check(rec)
 assert digest(b['immutable_records'])==b['canonical_deduplicated_sha256']
 read(FILES[1]);n=labels()
 new(MF,{
  'frozen_UTC':now(),'status':'Immutable initially blind independent OTHER WHOLE2; coordinator reconciliation pending',
  'reviewer':'/root/review_2021_reasoning_j15_r2','constructor':'C /root/review_2017_coarsening_r1',
  'constructor_excluded':True,'NEW_construction_contribution':False,
  'claims':['JM16A','JM16B','JM16C'],'whole_obligations':n,'ENTIRE_files':5,
  'payloads':[fp(x) for x in FILES],
  'guard_summary':{'occurrences':b['declared_occurrences'],'unique_paths':b['unique_paths'],
                  'canonical_deduplicated_sha256':b['canonical_deduplicated_sha256']},
  'compact_OWN_parent':b['compact_OWN_parent'],
  'all32_reconstructed_by_hand':True,'unresolved_substantive_defects':0,'required_author_repairs':0,
  'closed_scope_notes':10,'FULL_final_ALL4_payload_MODEL_readbacks_completed':True,
  'FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_REQUIRED':True,
  'NEW_JM16_peer_finding_file_actual_inventory_hash_metadata_commentary_access':False,
  'R20_BOTH_release_received_during_audit':True,'R20_peer_file_access':False,'root_R27_access':False,
  'findings_require_explicit_BOTH_release':True,
  'requested':{'model':'gpt-6.1-sol','reasoning':'max','inherited':True},
  'independent_effective_backend_readback':None,
  'quota':{'usedPercent':82,'observed_UTC':'2026-10-19 02:38:13 UTC','windowDurationMins':10080,
   'resetsAt':1792874445,'ordinaryUsageAllowed':True,'TOTAL_ceiling':90,'reserve':True,'automatic_later_window':False},
  'mathematical_truth_checked_by_code':False,'old_author_source_helper_freezer_replay':False,
  'Git_shared_old_cache_configuration_mutation':False
 })
 print(json.dumps({'frozen_UTC':read(MF)['frozen_UTC'],'manifest':fp(MF)}))
def verify():
 m=read(MF);b=read(P+'baseline-v1.json')
 for rec in m['payloads']+b['immutable_records']:check(rec)
 assert m['whole_obligations']==labels()==32
 assert m['ENTIRE_files']==len(m['payloads'])+1==5
 assert digest(b['immutable_records'])==b['canonical_deduplicated_sha256']
 assert m['guard_summary']['canonical_deduplicated_sha256']==b['canonical_deduplicated_sha256']
 print(json.dumps({'SEPARATE_readonly_verify_UTC':now(),'result':'PASS','ENTIRE_files':5,'whole_obligations':32,
  'manifest':fp(MF),'initial':fp(FILES[0]),'guard_summary':m['guard_summary'],
  'writes':0,'mathematical_truth_checked_by_code':False}))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['prepare','freeze','verify'])
 args=ap.parse_args();{'prepare':prepare,'freeze':freeze,'verify':verify}[args.mode]()
