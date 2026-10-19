#!/usr/bin/env python3
"""NEW CM16 review2 documentary bytes/SHA/JSON/literal labels ONLY.
No moment/word/count/inequality calculation or author/old executable replay.
Only own baseline/manifest writes. No peer inventory/recursive ancestors.
"""
import argparse
import hashlib
import json
import re
from datetime import datetime,timezone
from pathlib import Path

ROOT=Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PFX='problems/2019-B4/reviews/reasoning-critical-law-return-r16-review-2-'
AUTHOR='problems/2019-B4/notes/reasoning-critical-law-return-r16-'
PARENT='problems/2025-B4/notes/reasoning-exception-return-r12-freeze-v1.json'
BASE=PFX+'baseline-v1.json'
MAN=PFX+'manifest-v1.json'
PAYLOADS=[PFX+'initial-v1.md',PFX+'sources-v1.json',PFX+'admin-v1.py',BASE]
STEMS=['reasoning-return-r7','reasoning-cut-transfer-r6','moment-tail',
       'reasoning-full-law-return-r15','reasoning-area-return-r2','reasoning-occupation-return-r1']
EXPECTED={
 AUTHOR+'candidate-v1.md':'cf3bc455ab866ec0cc0ddaeb6a18fa93b7b4427dcb2c781c86b28081e98af77b',
 AUTHOR+'freeze-v1.json':'b293b0aba2ac626219e7e4fd170d6a9780528446a860d7cada5edee81cc3ccda',
 PARENT:'79e7c6bd6746a38b1cceb44a773f7b267795560ed7439a88564994ec93e3d68b',
 'AGENTS.md':'28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff'
}
def now():return datetime.now(timezone.utc).isoformat()
def load(rel):return json.loads((ROOT/rel).read_text())
def fp(rel):
 assert not Path(rel).is_absolute() and '..' not in Path(rel).parts
 data=(ROOT/rel).read_bytes()
 return {'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
def check(row):
 got=fp(row['path']);assert got=={k:row[k] for k in ('path','bytes','sha256')},row['path']
 return got
def new(rel,value):
 assert rel.startswith(PFX)
 with (ROOT/rel).open('x') as out:json.dump(value,out,indent=2);out.write('\n')
def labels():
 own=(ROOT/PAYLOADS[0]).read_text();author=(ROOT/(AUTHOR+'candidate-v1.md')).read_text()
 assert re.findall(r'^\| R2-O(\d{2}) \| CM16-\d{2} \|',own,re.M)==[f'{i:02}' for i in range(1,33)]
 assert re.findall(r'^\|CM16-(\d{2})\|CHECKED\.',author,re.M)==[f'{i:02}' for i in range(1,33)]
 load(PAYLOADS[1])
def summarize(rows):
 unique={}
 for row in rows:
  if row['path'] in unique:assert unique[row['path']]==row
  unique[row['path']]=row
 ordered=[unique[k] for k in sorted(unique)]
 digest=hashlib.sha256(json.dumps(ordered,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 return ordered,{'occurrences':len(rows),'unique_paths':len(ordered),'canonical_deduplicated_sha256':digest}
def baseline():
 author=load(AUTHOR+'freeze-v1.json')
 assert author['ENTIRE_files']==5 and author['whole_obligations']==32
 rows=[fp(AUTHOR+'freeze-v1.json')]+[check(x) for x in author['payloads']]
 rows.extend([fp('AGENTS.md'),fp('problems/2019-B4/statement.md')])
 interfaces=[]
 for stem in STEMS:
  md='problems/2019-B4/reviews/'+stem+'-acceptance.md';js=md[:-3]+'.json'
  a=load(js);assert a['unresolved_substantive_issues']==0 if 'unresolved_substantive_issues' in a else a['substantive_objections']==[]
  body=check(a['proof_register'] if stem=='moment-tail' else a['accepted_copy'])
  rows.extend([body,fp(md),fp(js)])
  interfaces.append({'body':body,'authority_md':fp(md),'authority_json':fp(js),
      'FULL_body_and_EACH_current_MDJSON_MODEL_read':True,'older_histories_NOT_expanded':True})
 parent=load(PARENT);rows.append(fp(PARENT))
 for rel,sha in EXPECTED.items():assert fp(rel)['sha256']==sha,rel
 guards,counts=summarize(rows);labels();old=load(AUTHOR+'baseline-v1.json')
 value={'created_UTC':now(),'status':'OTHER initially blind WHOLE2; findings SEALED',
   'ALL_obligations':32,'necessary_immutable_guards':guards,'guard_summary':counts,
   'current_accepted_interfaces':interfaces,'author_freeze':fp(AUTHOR+'freeze-v1.json'),
   'author_historical_summary_bound_NOT_expanded':{'occurrences':old['declared_occurrences'],
      'unique_paths':old['unique_paths'],'digest_sha256':old['guard_digest_sha256']},
   'author_R25_parent_filename_byte_hash_receipt_disclosed':True,
   'underlying_R25_parent_files_NOT_inventoried_opened_read_or_hashed':True,
   'immediate_OWN_ET12_parent':fp(PARENT),'own_parent_guard_summary_NOT_expanded':parent['guard_summary'],
   'mutable_research_maps_NOT_immutable_guards':True,'old_mutable_observations_NOT_rewritten':True,
   'NEW_corresponding_CM16_peer_finding_file_actual_inventory_hash_meta_commentary_access':False,
   'root_R26_access':False,'requested':{'model':'gpt-6.1-sol','reasoning':'max','inherited':True},
   'independent_effective_backend_readback':None,
   'quota':{'usedPercent':79,'observed_UTC':'2026-10-19 02:08:05 UTC','resetsAt':1792874445,
      'windowDurationMins':10080,'ordinaryUsageAllowed':True,'legacy_by_limit_agree':True,
      'account_label':'...ac3a','TOTAL_ceiling':90,'integration_review_reserve':True,'automatic_later_window_spending':False},
   'mathematical_program_CAS_scan_test_source_author_old_helper_freezer_certificate_replay':False,
   'Git_shared_old_cache_mutation_spawn_charge_contact_bypass':False}
 new(BASE,value);print(json.dumps({'baseline':fp(BASE),'guard_summary':counts}))
def freeze(confirmed):
 assert confirmed,'FULL final ALL payload MODEL readbacks required'
 b=load(BASE)
 for row in b['necessary_immutable_guards']:check(row)
 labels()
 value={'frozen_UTC':now(),'status':'OTHER initially blind ENTIRE WHOLE2; findings SEALED until explicit BOTH',
   'reviewer':'/root/review_2022_complexity_r2','NEW_constructor':'/root/review_2017_coarsening_r1',
   'reviewer_not_NEW_constructor':True,'ENTIRE_files':5,'payload_count':4,'ALL_obligations':32,
   'payloads':[fp(p) for p in PAYLOADS],'guard_summary':b['guard_summary'],'author_freeze':b['author_freeze'],
   'immediate_OWN_ET12_parent':b['immediate_OWN_ET12_parent'],
   'FULL_final_ALL4_payload_MODEL_readbacks_completed':True,
   'FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_REQUIRED':True,
   'explicit_BOTH_release_before_corresponding_NEW_peer_access_REQUIRED':True,
   'NEW_corresponding_CM16_peer_finding_file_actual_inventory_hash_meta_commentary_access':False,
   'unrelated_author_R25_metadata_receipt_disclosed_without_underlying_file_access':True,
   'requested':b['requested'],'independent_effective_backend_readback':None,'quota':b['quota'],
   'mathematical_program_CAS_scan_test_source_author_old_replay':False,'Git_shared_old_cache_mutation':False}
 new(MAN,value);print(json.dumps({'manifest':fp(MAN),'frozen_UTC':value['frozen_UTC']}))
def verify():
 m=load(MAN);b=load(BASE)
 for row in m['payloads']+b['necessary_immutable_guards']:check(row)
 assert len(m['payloads'])+1==m['ENTIRE_files']==5
 assert m['guard_summary']==b['guard_summary'];labels()
 print(json.dumps({'SEPARATE_readonly_verify_UTC':now(),'documentary_status':'PASS','ENTIRE_files':5,
   'literal_obligations':32,'guard_summary':b['guard_summary'],'manifest':fp(MAN),'writes':0,'mathematical_verification_claimed':False}))
if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('mode',choices=['baseline','freeze','verify'])
 parser.add_argument('--final-payload-readback-confirmed',action='store_true');args=parser.parse_args()
 if args.mode=='baseline':baseline()
 elif args.mode=='freeze':freeze(args.final_payload_readback_confirmed)
 else:verify()
