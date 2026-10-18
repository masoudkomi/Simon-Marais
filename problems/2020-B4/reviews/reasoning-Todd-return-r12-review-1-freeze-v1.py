#!/usr/bin/env python3
"""Preserve an entire blind review; no mathematical executable or test."""
from pathlib import Path
import argparse,datetime,hashlib,json,re
ROOT=Path(__file__).resolve().parents[3]
P='problems/2020-B4/reviews/reasoning-Todd-return-r12-review-1-'
AUTHOR='problems/2020-B4/notes/reasoning-Todd-return-r12-'
PARENT='problems/2024-B4/notes/cofactor-Frobenius-r5-freeze-v1.json'
PARENT_SHA='cda866d3b82dfe335c78643d15d857e21bcda5439c2ecf308956281b02a8b545'
SUFFIXES=['initial-v1.md','ledger-v1.md','issues-v1.md','source-checks-v1.md','sources-v1.json','worklog-v1.md','freeze-v1.py','baseline-v1.json','input-validation-v1.json','metadata-v1.json']
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def raw(p):
 assert not p.startswith('problems/2020-B4/reviews/reasoning-Todd-return-r12-review-2-')
 assert not p.startswith('problems/2024-B4/reviews/cofactor-Frobenius-r5-review-')
 return (ROOT/p).read_bytes()
def obj(p):return json.loads(raw(p))
def rec(p):
 b=raw(p);return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def check(v):
 assert rec(v['path'])=={k:v[k]for k in ['path','bytes','sha256']},v['path']
 return rec(v['path'])
def put(s,v):
 with (ROOT/(P+s)).open('x')as f:json.dump(v,f,indent=2);f.write('\n')
def digest(v):return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def baseline():
 a=obj(AUTHOR+'freeze-v1.json')
 assert rec(AUTHOR+'freeze-v1.json')['sha256']=='cac7580782285028c7e71207097a3566232306a764fa7d174a7a1fd21973dcc0'
 assert a['whole_obligations']==72 and len(a['artifacts'])==10
 b=obj(AUTHOR+'baseline-v1.json')
 rows=[rec(AUTHOR+'freeze-v1.json')]+[check(v)for v in a['artifacts']]+[check(v)for v in b['protected_rows']]
 for v in a['accepted_authorities']:
  auth=obj(v['authority']['path'])
  assert not auth['repair_required'] and not auth['unresolved_substantive_issues']
  assert raw(v['accepted_body']['path']).endswith(raw(v['exact_candidate_suffix']['path']))
 p=rec(PARENT);assert p['sha256']==PARENT_SHA
 parent=obj(PARENT);assert len(parent['artifacts'])==8
 rows +=[p]+[check(v)for v in parent['artifacts']]
 unique={}
 for v in rows:
  assert v['path']not in unique or unique[v['path']]==v
  unique[v['path']]=v
 ordered=[unique[k]for k in sorted(unique)]
 put('baseline-v1.json',dict(captured_at_utc=now(),administrative_only=True,assigned_prefix_unused_before_first_write=True,
  constructor_freeze=rec(AUTHOR+'freeze-v1.json'),author_all11_and_current37_protected_paths_verified=True,
  accepted_body_suffixes_all_five_exact=True,immediate_own_parent=p,own_parent_eight_payloads_verified_unchanged=True,
  older_inventories_bound_by_current_authority_not_recopied_or_recursively_replayed=True,
  fingerprint_occurrences=len(rows),unique_paths=len(ordered),canonical_summary_sha256=digest(ordered),protected_rows=ordered,
  NO_NEW_corresponding_Todd_R2_finding_content_hash_or_metadata_access=True,
  NO_NEW_R5_peer_content_hash_findings_or_metadata_access=True))
 print(json.dumps(dict(baseline=rec(P+'baseline-v1.json'),occurrences=len(rows),paths=len(ordered))))
def verify_inputs():
 b=obj(P+'baseline-v1.json')
 for v in b['protected_rows']:check(v)
 assert digest(b['protected_rows'])==b['canonical_summary_sha256']
 return b
def freeze():
 b=verify_inputs()
 assert re.findall(r'^(\d+)\. PASS',raw(P+'ledger-v1.md').decode(),re.M)==[str(i)for i in range(1,73)]
 stamp=now()
 put('input-validation-v1.json',dict(verified_at_utc=stamp,administrative_only=True,
  occurrences=b['fingerprint_occurrences'],unique_paths=b['unique_paths'],canonical_summary_sha256=b['canonical_summary_sha256'],
  all72_once_in_order=True,all_constructor_current_authorities_and_own_parent_unchanged=True,
  no_mathematical_program_test_scan_CAS_certificate_or_author_rerun=True))
 put('metadata-v1.json',dict(recorded_at_utc=stamp,reviewer='/root',constructor='/root/review_2022_complexity_r2',
  OTHER_NEW_nonconstructor=True,root_assignment_generic_no_NEW_inference=True,whole_obligations=72,all72_pass=True,
  substantive_issues=0,required_repairs=0,closed_scope_notes=6,
  requested_settings=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),independent_effective_readback=None,
  ENTIRE_initial_ledger_issues_sources_log_code_ALLmetadata_frozen_together=True,
  NO_NEW_corresponding_Todd_R2_finding_content_hash_or_metadata_access=True,
  no_mathematical_program_test_scan_CAS_certificate_or_author_rerun=True,
  other_ENTIRE_R2_and_full_coordinator_reconciliation_required=True,promotion=False,annual_or_priority_claim=False))
 put('manifest-v1.json',dict(frozen_at_utc=stamp,status='ENTIRE initially blind OTHER WHOLE TD1-TD5 review1',
  reviewer='/root',constructor='/root/review_2022_complexity_r2',exact_target=rec(AUTHOR+'candidate-v1.md'),
  constructor_freeze=rec(AUTHOR+'freeze-v1.json'),whole_obligations=72,all72_pass=True,
  substantive_issues=0,required_repairs=0,closed_scope_notes=6,ENTIRE_packet_complete=True,
  NO_NEW_corresponding_Todd_R2_finding_content_hash_or_metadata_access=True,
  immediate_own_parent=rec(PARENT),current_input_summary={k:b[k]for k in ['fingerprint_occurrences','unique_paths','canonical_summary_sha256']},
  other_ENTIRE_R2_and_full_coordinator_reconciliation_required=True,promotion=False,
  artifacts=[rec(P+s)for s in SUFFIXES]))
 verify()
def verify():
 verify_inputs();m=obj(P+'manifest-v1.json');assert len(m['artifacts'])==10
 for v in m['artifacts']:check(v)
 print(json.dumps(dict(postverified=True,whole_obligations=72,files_including_manifest=11,
  manifest=rec(P+'manifest-v1.json'),target=rec(AUTHOR+'candidate-v1.md'))))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('operation',choices=['baseline','freeze','verify'])
 {'baseline':baseline,'freeze':freeze,'verify':verify}[p.parse_args().operation]()
