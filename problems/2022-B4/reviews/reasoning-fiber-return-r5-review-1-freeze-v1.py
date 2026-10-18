#!/usr/bin/env python3
"""Administrative preservation only; no mathematical computation or tests."""
from pathlib import Path
import argparse,datetime,hashlib,json,re
ROOT=Path(__file__).resolve().parents[3]
P='problems/2022-B4/reviews/reasoning-fiber-return-r5-review-1-'
A='problems/2022-B4/notes/reasoning-fiber-return-r5-'
PARENT='problems/2019-B4/reviews/reasoning-cut-number-r3-review-1-manifest-v1.json'
PAYLOAD=['initial-v1.md','ledger-v1.md','issues-v1.md','source-checks-v1.md','sources-v1.json','worklog-v1.md','freeze-v1.py','baseline-v1.json','input-validation-v1.json','metadata-v1.json']
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def raw(p):
 assert not p.startswith('problems/2022-B4/reviews/reasoning-fiber-return-r5-review-2-')
 assert not p.startswith('problems/2020-B4/reviews/reasoning-Todd-return-r12-review-2-')
 return (ROOT/p).read_bytes()
def obj(p):return json.loads(raw(p))
def fp(p):
 b=raw(p);return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def check(v):
 assert fp(v['path'])=={k:v[k]for k in ['path','bytes','sha256']},v['path']
 return fp(v['path'])
def put(s,v):
 with (ROOT/(P+s)).open('x')as f:json.dump(v,f,indent=2);f.write('\n')
def digest(v):return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def baseline():
 author=obj(A+'freeze-v1.json')
 assert fp(A+'freeze-v1.json')['sha256']=='22283a8f95e7a2a489596a418b1dce4d9ab3f619296309b0ed33863fbd75c2ca'
 assert author['whole_obligations']==48 and len(author['artifacts'])==10
 rows=[fp(A+'freeze-v1.json')]+[check(v)for v in author['artifacts']]
 ab=obj(A+'baseline-v1.json')
 assert len(ab['protected'])==35
 for v in ab['protected']:check(v)
 bindings=[]
 for b in ab['accepted']:
  p=b['authority']['path'];v=obj(p)
  assert not v['repair_required'] and not v['unresolved_substantive_issues']
  body=check(v['accepted_copy']);candidate=check(v['candidate'])
  assert raw(body['path']).endswith(raw(candidate['path']))
  recs=[check(b['authority']),fp(p[:-5]+'.md'),body,candidate];rows+=recs
  bindings.append(dict(authority=recs[0],accepted_body=body,candidate=candidate,
    historical_occurrences_bound_not_replayed=v['record_occurrences_verified'],historical_paths_bound_not_replayed=v['unique_paths_verified']))
 parent=fp(PARENT);pv=obj(PARENT)
 assert pv['whole_obligations']==48 and len(pv['artifacts'])==9
 rows +=[parent]+[check(v)for v in pv['artifacts']]+[fp('AGENTS.md'),fp('problems/2022-B4/statement.md')]
 unique={}
 for v in rows:
  assert v['path']not in unique or unique[v['path']]==v
  unique[v['path']]=v
 ordered=[unique[k]for k in sorted(unique)]
 put('baseline-v1.json',dict(captured_at_utc=now(),administrative_only=True,prefix_confirmed_unused_before_first_write=True,
  accepted_bindings=bindings,constructor_all11_current=True,author_current35_guards_verified_at_capture=True,
  author_baseline_identity=fp(A+'baseline-v1.json'),author_baseline35_historical_rows_not_recopied=True,
  immediate_own_parent=parent,own_parent_all9_payloads_preserved=True,
  old_inventories_bound_by_authority_not_recopied_or_recursively_replayed=True,
  occurrences=len(rows),unique_paths=len(ordered),canonical_summary_sha256=digest(ordered),protected_rows=ordered,
  mutable_living_research_not_future_operative_immutability_guard=True,NO_NEW_corresponding_R2_material_access=True))
 print(json.dumps(dict(baseline=fp(P+'baseline-v1.json'),occurrences=len(rows),paths=len(ordered))))
def inputs():
 b=obj(P+'baseline-v1.json')
 for v in b['protected_rows']:check(v)
 assert digest(b['protected_rows'])==b['canonical_summary_sha256']
 return b
def freeze():
 b=inputs();assert re.findall(r'^(\d+)\. PASS',raw(P+'ledger-v1.md').decode(),re.M)==[str(i)for i in range(1,49)]
 stamp=now()
 put('input-validation-v1.json',dict(verified_at_utc=stamp,administrative_only=True,all48_once_in_order=True,
  current_paths=b['unique_paths'],canonical_summary_sha256=b['canonical_summary_sha256'],all_protected_bytes_preserved=True,
  no_mathematical_program_scan_CAS_test_certificate_or_author_rerun=True))
 put('metadata-v1.json',dict(recorded_at_utc=stamp,reviewer='/root',constructor='/root/review_2017_coarsening_r1',
  OTHER_NEW_nonconstructor=True,root_generic_assignment_only=True,whole_obligations=48,all48_pass=True,
  substantive_issues=0,required_repairs=0,closed_scope_notes=5,
  requested_settings=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),independent_effective_readback=None,
  ENTIRE_initial_ALL48_issues_sources_log_code_ALLmetadata_frozen_together=True,
  CF1_CF5_unconditional_CF6_explicitly_conditional=True,
  NO_NEW_corresponding_R2_finding_content_hash_or_metadata_access=True,
  other_ENTIRE_R2_and_coordinator_reconciliation_required=True,promotion=False,annual_or_priority_claim=False))
 put('manifest-v1.json',dict(frozen_at_utc=stamp,status='ENTIRE initially blind OTHER WHOLE CF1-CF6 review1',
  reviewer='/root',constructor='/root/review_2017_coarsening_r1',target=fp(A+'candidate-v1.md'),constructor_freeze=fp(A+'freeze-v1.json'),
  whole_obligations=48,all48_pass=True,substantive_issues=0,required_repairs=0,closed_scope_notes=5,
  ENTIRE_initial_ALL48_issues_sources_log_code_ALLmetadata_frozen_together=True,
  NO_NEW_corresponding_R2_finding_content_hash_or_metadata_access=True,
  immediate_own_parent=fp(PARENT),current_inputs={k:b[k]for k in ['occurrences','unique_paths','canonical_summary_sha256']},
  other_ENTIRE_R2_and_coordinator_reconciliation_required=True,promotion=False,artifacts=[fp(P+s)for s in PAYLOAD]))
 verify()
def verify():
 inputs();v=obj(P+'manifest-v1.json');assert len(v['artifacts'])==10
 for row in v['artifacts']:check(row)
 print(json.dumps(dict(postverified=True,whole_obligations=48,files_including_manifest=11,manifest=fp(P+'manifest-v1.json'),target=fp(A+'candidate-v1.md'))))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('operation',choices=['baseline','freeze','verify']);{'baseline':baseline,'freeze':freeze,'verify':verify}[p.parse_args().operation]()
