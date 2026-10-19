#!/usr/bin/env python3
"""NEW CM16 WHOLE1 documentary identity helper only.

No moment, coefficient, word, inequality or probability is computed.
No author/old helper is imported or run. Only this exclusive prefix writes.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import re

ROOT=Path('/Users/uqmkamga/Documents/ChatGPT/Website')
P='problems/2019-B4/reviews/reasoning-critical-law-return-r16-review-1-'
A='problems/2019-B4/notes/reasoning-critical-law-return-r16-'
PARENT='problems/2021-B4/reviews/coordinator-dyadic-depth-return-r25-review-2-manifest-v1.json'
DIRECT=[
 ('problems/2019-B4/proofs/reviewed-reasoning-return-r7-v1.1.md','problems/2019-B4/reviews/reasoning-return-r7-acceptance','accepted_copy'),
 ('problems/2019-B4/proofs/reviewed-reasoning-cut-transfer-r6-v1.1.md','problems/2019-B4/reviews/reasoning-cut-transfer-r6-acceptance','accepted_copy'),
 ('problems/2019-B4/proofs/reviewed-moment-tail-v1.1.md','problems/2019-B4/reviews/moment-tail-acceptance','proof_register'),
 ('problems/2019-B4/proofs/reviewed-reasoning-full-law-return-r15-v1.1.md','problems/2019-B4/reviews/reasoning-full-law-return-r15-acceptance','accepted_copy'),
 ('problems/2019-B4/proofs/reviewed-reasoning-area-return-r2-v1.1.md','problems/2019-B4/reviews/reasoning-area-return-r2-acceptance','accepted_copy'),
 ('problems/2019-B4/proofs/reviewed-reasoning-occupation-return-r1-v1.1.md','problems/2019-B4/reviews/reasoning-occupation-return-r1-acceptance','accepted_copy')
]
FILES=[P+s for s in ['initial-v1.md','sources-v1.json','admin-v1.py','baseline-v1.json']]
MF=P+'manifest-v1.json'
EXPECTED={
 A+'candidate-v1.md':(22118,'cf3bc455ab866ec0cc0ddaeb6a18fa93b7b4427dcb2c781c86b28081e98af77b'),
 A+'freeze-v1.json':(2415,'b293b0aba2ac626219e7e4fd170d6a9780528446a860d7cada5edee81cc3ccda'),
 PARENT:(2876,'088a1fe247a6bc2deb3da9ff898eb513178774ea00163989626289397cff1f29')
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
 ids=re.findall(r'^\|CM16-(\d{2})\|',(ROOT/FILES[0]).read_text(),re.M)
 assert ids==[f'{i:02}' for i in range(1,33)],'ALL32 literal outcomes'
 return len(ids)
def prepare():
 author=read(A+'freeze-v1.json');ab=read(A+'baseline-v1.json');parent=read(PARENT)
 occurrences=[fp(A+'freeze-v1.json')]+author['payloads']+ab['immutable_records']
 for body,authority,key in DIRECT:
  assert read(authority+'.json')[key]==fp(body),body
  occurrences += [fp(body),fp(authority+'.md'),fp(authority+'.json')]
 occurrences += [fp(PARENT)]+parent['payloads']
 unique={}
 for rec in occurrences:
  old=unique.setdefault(rec['path'],rec);assert old==rec,rec['path']
 for rec in unique.values():check(rec)
 for path,(size,sha) in EXPECTED.items():
  assert unique[path]['bytes']==size and unique[path]['sha256']==sha,path
 assert author['whole_obligations']==labels()==32
 assert author['ENTIRE_files']==len(author['payloads'])+1==5
 assert parent['ENTIRE_files']==len(parent['payloads'])+1==5
 read(FILES[1]);rows=[unique[k] for k in sorted(unique)]
 new(P+'baseline-v1.json',{
  'created_UTC':now(),'status':'Exact necessary guards once, compact OWN parent, no historical recursive expansion',
  'immutable_records':rows,'declared_occurrences':len(occurrences),'unique_paths':len(rows),
  'canonical_deduplicated_sha256':digest(rows),'compact_OWN_parent':fp(PARENT),
  'OWN_parent_summary_NOT_expanded':parent['effective_fresh_guard_summary'],
  'author_parent_declared_records_verified_once_already_released_R25_only':True,
  'mutable_context_NOT_guard':{'historical_author_observation':ab['mutable_context_NOT_immutable_guard'],
    'current_fingerprint_not_MODEL_content_read':fp('problems/2019-B4/research.md'),
    'neither_observation_expected_immutable':True},
  'NEW_CM16_peer_finding_inventory_file_hash_metadata_commentary_access':False,
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
  'frozen_UTC':now(),'status':'Immutable initially blind independent OTHER WHOLE1; coordinator reconciliation pending',
  'reviewer':'/root/review_2021_reasoning_j15_r2','constructor':'/root/review_2017_coarsening_r1',
  'constructor_excluded':True,'NEW_construction_contribution':False,
  'claims':['CM16A','CM16B','CM16C'],'whole_obligations':n,'ENTIRE_files':5,
  'payloads':[fp(x) for x in FILES],
  'guard_summary':{'occurrences':b['declared_occurrences'],'unique_paths':b['unique_paths'],
                   'canonical_deduplicated_sha256':b['canonical_deduplicated_sha256']},
  'compact_OWN_parent':b['compact_OWN_parent'],
  'all32_reconstructed_by_hand':True,'unresolved_substantive_defects':0,'required_author_repairs':0,
  'closed_scope_notes':9,'FULL_final_ALL4_payload_MODEL_readbacks_completed':True,
  'FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_REQUIRED':True,
  'NEW_CM16_peer_finding_inventory_file_hash_metadata_commentary_access':False,
  'root_R26_access':False,'findings_require_explicit_BOTH_release':True,
  'requested':{'model':'gpt-6.1-sol','reasoning':'max','inherited':True},
  'independent_effective_setting_readback':None,
  'quota':{'usedPercent':79,'observed_UTC':'2026-10-19 02:05:41 UTC','windowDurationMins':10080,
   'resetsAt':1792874445,'ordinaryUsageAllowed':True,'TOTAL_ceiling':90,'reserve':True,'automatic_later_window':False},
  'mathematical_truth_checked_by_code':False,'old_author_source_helper_freezer_replay':False,
  'Git_shared_old_cache_mutation':False
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
