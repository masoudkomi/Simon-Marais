#!/usr/bin/env python3
"""NEW R20 WHOLE2 documentary bytes/JSON/literal-label binding only.

No group, polynomial, matrix, content or valuation is computed. No old
or author/source helper is executed. Exclusive NEW review writes only.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import re

ROOT=Path('/Users/uqmkamga/Documents/ChatGPT/Website')
P='problems/2020-B4/reviews/reasoning-global-return-r20-review-2-'
A='problems/2020-B4/notes/reasoning-global-return-r20-'
PARENT='problems/2021-B4/reviews/coordinator-dyadic-return-r26-review-1-manifest-v1.json'
DIRECT=[
 ('problems/2020-B4/proofs/reviewed-reasoning-actual-return-r18-v1.1.md','problems/2020-B4/reviews/reasoning-actual-return-r18-acceptance'),
 ('problems/2020-B4/proofs/reviewed-reasoning-realization-return-r19-v1.1.md','problems/2020-B4/reviews/reasoning-realization-return-r19-acceptance')
]
FILES=[P+s for s in ['initial-v1.md','sources-v1.json','admin-v1.py','baseline-v1.json']]
MF=P+'manifest-v1.json'
EXPECTED={
 A+'candidate-v1.md':(24526,'f424c011ac4c397898b39e2488e736728a73b57fcda5d60adaa0f348c0c2e71a'),
 A+'freeze-v1.json':(1776,'ba2ea31635915d211efac6fc28024e6fefebe0f07e59df7eca31c6a52c831664'),
 PARENT:(2685,'f6bd87f071b1d626102c9beb6e7bde908e6441c19a8c3ce76182f1520ba70da1')
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
 ids=re.findall(r'^\|GR20-(\d{2})\|',(ROOT/FILES[0]).read_text(),re.M)
 assert ids==[f'{i:02}' for i in range(1,41)],'ALL40 literal outcomes'
 return len(ids)
def prepare():
 author=read(A+'freeze-v1.json');ab=read(A+'baseline-v1.json');parent=read(PARENT)
 occurrences=[fp(A+'freeze-v1.json')]+author['payloads']+ab['immutable_guards']
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
 assert author['whole_obligations']==labels()==40
 assert author['entire_file_count_including_manifest']==len(author['payloads'])+1==5
 assert parent['ENTIRE_files']==len(parent['payloads'])+1==5
 read(FILES[1]);rows=[unique[k] for k in sorted(unique)]
 new(P+'baseline-v1.json',{
  'created_UTC':now(),'status':'Necessary immutable guards once, ONE exact OWN parent, no recursive historical inventory or mutable map guard',
  'immutable_records':rows,'declared_occurrences':len(occurrences),'unique_paths':len(rows),
  'canonical_deduplicated_sha256':digest(rows),'compact_OWN_parent':fp(PARENT),
  'OWN_parent_guard_summary_NOT_expanded':parent['guard_summary'],
  'author_historical_mutable_observations_NOT_guards':ab['mutable_observations_not_immutable_guards'],
  'NEW_R20_peer_finding_file_actual_inventory_hash_metadata_commentary_access':False,
  'R26_initially_sealed_then_BOTH_release_received':True,'R26_peer_file_access':False,'root_R27_access':False,
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
  'reviewer':'/root/review_2021_reasoning_j15_r2','constructor':'B /root/review_2022_complexity_r2',
  'constructor_excluded':True,'NEW_construction_contribution':False,
  'claims':['GR20A','GR20B','GR20C','GR20D'],'whole_obligations':n,'ENTIRE_files':5,
  'payloads':[fp(x) for x in FILES],
  'guard_summary':{'occurrences':b['declared_occurrences'],'unique_paths':b['unique_paths'],
                  'canonical_deduplicated_sha256':b['canonical_deduplicated_sha256']},
  'compact_OWN_parent':b['compact_OWN_parent'],
  'all40_reconstructed_by_hand':True,'unresolved_substantive_defects':0,'required_author_repairs':0,
  'closed_scope_notes':11,'FULL_final_ALL4_payload_MODEL_readbacks_completed':True,
  'FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_REQUIRED':True,
  'NEW_R20_peer_finding_file_actual_inventory_hash_metadata_commentary_access':False,
  'R26_initially_sealed_then_BOTH_release_received':True,'R26_peer_file_access':False,'root_R27_access':False,
  'findings_require_explicit_BOTH_release':True,
  'requested':{'model':'gpt-6.1-sol','reasoning':'max','inherited':True},
  'independent_effective_setting_readback':None,
  'quota':{'usedPercent':82,'observed_UTC':'2026-10-19 02:32:23 UTC','windowDurationMins':10080,
   'resetsAt':1792874445,'ordinaryUsageAllowed':True,'TOTAL_ceiling':90,'reserve':True,'automatic_later_window':False},
  'mathematical_truth_checked_by_code':False,'old_author_source_helper_freezer_replay':False,
  'Git_shared_old_cache_configuration_mutation':False
 })
 print(json.dumps({'frozen_UTC':read(MF)['frozen_UTC'],'manifest':fp(MF)}))
def verify():
 m=read(MF);b=read(P+'baseline-v1.json')
 for rec in m['payloads']+b['immutable_records']:check(rec)
 assert m['whole_obligations']==labels()==40
 assert m['ENTIRE_files']==len(m['payloads'])+1==5
 assert digest(b['immutable_records'])==b['canonical_deduplicated_sha256']
 assert m['guard_summary']['canonical_deduplicated_sha256']==b['canonical_deduplicated_sha256']
 print(json.dumps({'SEPARATE_readonly_verify_UTC':now(),'result':'PASS','ENTIRE_files':5,'whole_obligations':40,
  'manifest':fp(MF),'initial':fp(FILES[0]),'guard_summary':m['guard_summary'],
  'writes':0,'mathematical_truth_checked_by_code':False}))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['prepare','freeze','verify'])
 args=ap.parse_args();{'prepare':prepare,'freeze':freeze,'verify':verify}[args.mode]()
