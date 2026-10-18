#!/usr/bin/env python3
"""Administrative exclusive creation and integrity; no mathematical evaluation."""
from pathlib import Path
import argparse,datetime,hashlib,json,re
ROOT=Path(__file__).resolve().parents[3]
P='problems/2017-B4/notes/coordinator-weighted-optimum-r2-'
PARENT='problems/2021-B4/reviews/reasoning-center-return-r17-review-1-manifest-v1.json'
WC='problems/2017-B4/reviews/coordinator-weighted-cutpath-r1-acceptance.json'
PAYLOAD=['candidate-v1.md','obligations-v1.md','hand-checks-v1.md','failed-routes-v1.md','sources-v1.md','worklog-v1.md','freeze-v1.py','baseline-v1.json','metadata-v1.json','input-validation-v1.json']
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def raw(p):
 assert not p.startswith('problems/2017-B4/reviews/coordinator-weighted-optimum-r2-')
 return(ROOT/p).read_bytes()
def obj(p):return json.loads(raw(p))
def fp(p):
 b=raw(p);return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def check(r):
 assert fp(r['path'])=={k:r[k]for k in ['path','bytes','sha256']},r['path']
 return fp(r['path'])
def put(s,v):
 with(ROOT/(P+s)).open('x')as f:json.dump(v,f,indent=2);f.write('\n')
def digest(v):return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def baseline():
 wc=obj(WC)
 assert wc['status']=='proved, independently reviewed scoped partial result'
 assert not wc['repair_required']and not wc['unresolved_substantive_issues']
 body=check(wc['accepted_copy']);candidate=check(wc['candidate'])
 assert body['sha256']=='93c08b0a43426c972bd6a0042c7e496cb08a106873c931f0231901e9f425f14b'
 assert raw(body['path']).endswith(raw(candidate['path']))
 rows=[fp(WC),fp(WC[:-5]+'.md'),body,candidate]
 for p in ['problems/2017-B4/notes/coordinator-weighted-cutpath-r1-source-audit-v1.md','problems/2017-B4/notes/coordinator-weighted-cutpath-r1-sources-v1.json','problems/2017-B4/notes/coordinator-weighted-cutpath-r1-freeze-v1.json','AGENTS.md','problems/2017-B4/statement.md']:
  rows.append(fp(p))
 par=fp(PARENT);pv=obj(PARENT)
 assert par['sha256']=='84ff5c98f08062fed06581d78d37c5b733de1cd4c2a0c19f9900b353c8b37ab3'
 assert pv['whole_obligations']==60 and len(pv['artifacts'])==10
 rows+=[par]+[check(r)for r in pv['artifacts']]
 unique={}
 for r in rows:
  assert r['path']not in unique or unique[r['path']]==r
  unique[r['path']]=r
 ordered=[unique[k]for k in sorted(unique)]
 put('baseline-v1.json',dict(captured_at_utc=now(),administrative_only=True,assigned_prefix_confirmed_unused_before_first_write=True,WC_current_accepted_status_and_literal_candidate_suffix_exact=True,WC_authority=fp(WC),WC_accepted_body=body,WC_original_candidate=candidate,WC_older_occurrences_bound_not_replayed=wc['record_occurrences_verified'],WC_older_paths_bound_not_replayed=wc['unique_paths_verified'],immediate_own_parent=par,immediate_own_parent_all10_payloads_exact=True,older_historical_inventory_bound_not_recursively_replayed=True,occurrences=len(rows),unique_paths=len(ordered),canonical_summary_sha256=digest(ordered),protected_rows=ordered,mutable_living_context_snapshots_not_immutable_premises=[fp('problems/2017-B4/research.md'),fp('problems/2017-B4/references.md')],no_NEW_corresponding_WO_peer_content_or_metadata_access=True))
 print(json.dumps(dict(baseline=fp(P+'baseline-v1.json'),occurrences=len(rows),paths=len(ordered))))
def inputs():
 b=obj(P+'baseline-v1.json')
 for r in b['protected_rows']:check(r)
 assert digest(b['protected_rows'])==b['canonical_summary_sha256']
 return b
def freeze():
 b=inputs()
 labels=re.findall(r'^\|(WO-\d{2})\|',raw(P+'obligations-v1.md').decode(),re.M)
 assert labels==[f'WO-{i:02d}'for i in range(1,49)]
 main=raw(P+'candidate-v1.md').decode()
 assert 'Candidate proof - unverified' in main
 assert all(c in main for c in ['WO1','WO2','WO3','WO4'])
 stamp=now()
 put('metadata-v1.json',dict(recorded_at_utc=stamp,status='candidate proof - unverified; ENTIRE constructor checkpoint only',constructor='/root',constructor_excluded_from_required_audits=True,no_worker_supplied_NEW_construction_inference=True,whole_obligations=48,proposed_claims=['WO1 exact specified-family optimum','WO2 strict algebraic upper certificate','WO3 unconditional weighted actual count','WO4 explicit conditional low-cost interface'],requested_settings=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),independently_verified_effective_readback=None,all_new_mathematics_hand_reasoning=True,no_mathematical_executable_CAS_optimizer_degree_scan_enumeration_source_author_or_old_certificate_rerun=True,two_OTHER_initially_blind_ENTIRE_WHOLE_audits_required=True,current_authorized_reset=1792874445,latest_root_TOTAL_percent=30,latest_root_telemetry_utc='2026-10-18T11:26:04+00:00',TOTAL_ceiling_percent=90,integration_reserve_and_no_automatic_later_window=True,actual_low_cost_bound_uniform_positive_density_global_tightness_exact_value_or_priority_proved=False,immediate_own_parent=fp(PARENT)))
 put('input-validation-v1.json',dict(verified_at_utc=stamp,administrative_only=True,all48_labels_once_in_order=True,all_protected_bytes_exact=True,protected_paths=b['unique_paths'],canonical_summary_sha256=b['canonical_summary_sha256'],current_WC_accepted_scope_and_literal_suffix_exact=True,no_mathematical_test_or_certificate=True,ENTIRE_full_readback_then_SEPARATE_postverify_still_required=True))
 put('freeze-v1.json',dict(frozen_at_utc=stamp,status='ENTIRE WO1-WO4 constructor checkpoint; candidate proof - unverified',whole_obligations=48,constructor='/root',constructor_excluded=True,constructor_files_including_freeze=11,ENTIRE_main_ALL48_hand_checks_failures_sources_log_code_ALLmetadata_frozen=True,immediate_own_parent=fp(PARENT),proposed_claims=['WO1','WO2','WO3','WO4 explicitly conditional'],two_OTHER_ENTIRE_WHOLE_reviews_and_coordinator_reconciliation_required=True,no_mathematical_computation_or_annual_priority_claim=True,artifacts=[fp(P+s)for s in PAYLOAD]))
 verify()
def verify():
 inputs();v=obj(P+'freeze-v1.json');assert v['whole_obligations']==48 and len(v['artifacts'])==10
 for r in v['artifacts']:check(r)
 print(json.dumps(dict(postverified=True,files=11,whole_obligations=48,main=fp(P+'candidate-v1.md'),freeze=fp(P+'freeze-v1.json'))))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('operation',choices=['baseline','freeze','verify']);{'baseline':baseline,'freeze':freeze,'verify':verify}[p.parse_args().operation]()
