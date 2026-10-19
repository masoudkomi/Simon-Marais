#!/usr/bin/env python3
"""NEW ET12 WHOLE2 documentary bytes/JSON/labels only; no mathematics.

No author/source/old helper is run. Writes only this exclusive NEW prefix.
Historical mutable research maps are excluded from immutable guards.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import re

ROOT=Path('/Users/uqmkamga/Documents/ChatGPT/Website')
P='problems/2025-B4/reviews/reasoning-exception-return-r12-review-2-'
A='problems/2025-B4/notes/reasoning-exception-return-r12-'
PARENT='problems/2019-B4/reviews/reasoning-critical-law-return-r16-review-1-manifest-v1.json'
DIRECT=[
 ('problems/2025-B4/proofs/reviewed-reasoning-compatible-return-r10-v1.1.md','problems/2025-B4/reviews/reasoning-compatible-return-r10-acceptance'),
 ('problems/2025-B4/proofs/reviewed-reasoning-global-return-r11-v1.1.md','problems/2025-B4/reviews/reasoning-global-return-r11-acceptance')
]
FILES=[P+s for s in ['initial-v1.md','sources-v1.json','admin-v1.py','baseline-v1.json']]
MF=P+'manifest-v1.json'
EXPECTED={
 A+'candidate-v1.md':(25536,'de6c6478d45115aa559d00070c7ed469ab9b146d07398219b99b1a0553057c87'),
 A+'freeze-v1.json':(2517,'79e7c6bd6746a38b1cceb44a773f7b267795560ed7439a88564994ec93e3d68b'),
 PARENT:(2726,'f57069968d4ab1ac690084207dfc0d1330937b919b7ada0dc81a6dc2f57db2dd')
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
 ids=re.findall(r'^\|ET12-O(\d{2})\|',(ROOT/FILES[0]).read_text(),re.M)
 assert ids==[f'{i:02}' for i in range(1,37)],'ALL36 literal outcomes'
 return len(ids)
def prepare():
 author=read(A+'freeze-v1.json');ab=read(A+'baseline-v1.json');parent=read(PARENT)
 occurrences=[fp(A+'freeze-v1.json')]+author['payloads']+ab['necessary_immutable_guards']
 for body,authority in DIRECT:
  assert read(authority+'.json')['accepted_copy']==fp(body),body
  occurrences += [fp(body),fp(authority+'.md'),fp(authority+'.json')]
 occurrences += [fp(PARENT)]+parent['payloads']
 unique={}
 for rec in occurrences:
  old=unique.setdefault(rec['path'],rec);assert old==rec,rec['path']
 for rec in unique.values():check(rec)
 for path,(size,sha) in EXPECTED.items():
  assert unique[path]['bytes']==size and unique[path]['sha256']==sha,path
 assert author['ALL_obligations']==labels()==36
 assert author['ENTIRE_files']==len(author['payloads'])+1==5
 assert parent['ENTIRE_files']==len(parent['payloads'])+1==5
 read(FILES[1]);rows=[unique[k] for k in sorted(unique)]
 new(P+'baseline-v1.json',{
  'created_UTC':now(),'status':'Necessary exact guards once, OWN compact parent, no growing historical traversal',
  'immutable_records':rows,'declared_occurrences':len(occurrences),'unique_paths':len(rows),
  'canonical_deduplicated_sha256':digest(rows),'compact_OWN_parent':fp(PARENT),
  'OWN_parent_guard_summary_NOT_expanded':parent['guard_summary'],
  'author_JC15_manifest_released_before_documentary_access_not_peer_ET12':True,
  'mutable_context_NOT_guard':{'author_historical_map_observation':ab['mutable_research_map'],
   'current_map_MODEL_read_or_hash_required':False,'no_mutable_map_row_in_immutable_guards':True},
  'NEW_ET12_peer_finding_file_actual_inventory_hash_metadata_commentary_access':False,
  'root_R26_access':False,'mathematical_computation_or_old_helper_replay':False
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
  'reviewer':'/root/review_2021_reasoning_j15_r2','constructor':'/root/review_2022_complexity_r2',
  'constructor_excluded':True,'NEW_construction_contribution':False,
  'claims':['ET1','ET2','ET3'],'whole_obligations':n,'ENTIRE_files':5,
  'payloads':[fp(x) for x in FILES],
  'guard_summary':{'occurrences':b['declared_occurrences'],'unique_paths':b['unique_paths'],
                  'canonical_deduplicated_sha256':b['canonical_deduplicated_sha256']},
  'compact_OWN_parent':b['compact_OWN_parent'],
  'all36_reconstructed_by_hand':True,'unresolved_substantive_defects':0,'required_author_repairs':0,
  'closed_scope_notes':12,'FULL_final_ALL4_payload_MODEL_readbacks_completed':True,
  'FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_REQUIRED':True,
  'NEW_ET12_peer_finding_file_actual_inventory_hash_metadata_commentary_access':False,
  'root_R26_access':False,'findings_require_explicit_BOTH_release':True,
  'requested':{'model':'gpt-6.1-sol','reasoning':'max','inherited':True},
  'independent_effective_setting_readback':None,
  'quota':{'usedPercent':80,'observed_UTC':'2026-10-19 02:13:55 UTC','windowDurationMins':10080,
   'resetsAt':1792874445,'ordinaryUsageAllowed':True,'TOTAL_ceiling':90,'reserve':True,'automatic_later_window':False},
  'mathematical_truth_checked_by_code':False,'old_author_source_helper_freezer_replay':False,
  'Git_shared_old_cache_configuration_mutation':False
 })
 print(json.dumps({'frozen_UTC':read(MF)['frozen_UTC'],'manifest':fp(MF)}))
def verify():
 m=read(MF);b=read(P+'baseline-v1.json')
 for rec in m['payloads']+b['immutable_records']:check(rec)
 assert m['whole_obligations']==labels()==36
 assert m['ENTIRE_files']==len(m['payloads'])+1==5
 assert digest(b['immutable_records'])==b['canonical_deduplicated_sha256']
 assert m['guard_summary']['canonical_deduplicated_sha256']==b['canonical_deduplicated_sha256']
 print(json.dumps({'SEPARATE_readonly_verify_UTC':now(),'result':'PASS','ENTIRE_files':5,'whole_obligations':36,
  'manifest':fp(MF),'initial':fp(FILES[0]),'guard_summary':m['guard_summary'],
  'writes':0,'mathematical_truth_checked_by_code':False}))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['prepare','freeze','verify'])
 args=ap.parse_args();{'prepare':prepare,'freeze':freeze,'verify':verify}[args.mode]()
