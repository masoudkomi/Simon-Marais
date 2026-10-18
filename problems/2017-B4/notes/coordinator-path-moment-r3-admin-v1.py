#!/usr/bin/env python3
"""PM9 constructor metadata only: no path, probability, or proof computation."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re,sys
ROOT=Path(__file__).resolve().parents[3]
PRE='problems/2017-B4/notes/coordinator-path-moment-r3-'
NAMES=('working-v1.md','candidate-v1.md','obligations-v1.md','constructor-checks-v1.md','failures-worklog-v1.md','source-audit-v1.md','sources-v1.json','admin-v1.py','baseline-v1.json','input-validation-v1.json','metadata-v1.json')
PINNED=[dict(path='problems/2017-B4/proofs/reviewed-weighted-cutpath-r1-v1.1.md',bytes=15914,sha256='93c08b0a43426c972bd6a0042c7e496cb08a106873c931f0231901e9f425f14b'),dict(path='problems/2017-B4/proofs/reviewed-weighted-optimum-r2-v1.1.md',bytes=18824,sha256='dcc12d2989e5ab657960498179e2585e62ad35ffb1989a4bca72fef8fb953f9a'),dict(path='problems/2017-B4/proofs/reviewed-reasoning-path-mass-return-r8-v1.1.md',bytes=29343,sha256='4e538d9369ae4a2ae9c7c47fa400e947740de08d7ce84a8579f837fd9f9b18d3')]
def now():return datetime.now(timezone.utc).isoformat()
def raw(p):
 assert isinstance(p,str) and not p.startswith('/') and '..'not in Path(p).parts
 assert p.startswith('problems/2017-B4/') or p=='AGENTS.md'
 return(ROOT/p).read_bytes()
def obj(p):return json.loads(raw(p))
def fp(p):
 b=raw(p);return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def check(x):
 y={k:x[k]for k in('path','bytes','sha256')};assert fp(x['path'])==y,x['path'];return y
def put(s,v):
 assert s in('baseline-v1.json','input-validation-v1.json','metadata-v1.json','freeze-v1.json')
 with(ROOT/(PRE+s)).open('x')as f:json.dump(v,f,indent=2);f.write('\n')
def inputs():
 for x in PINNED:check(x)
 rows=[]
 for name in('coordinator-weighted-cutpath-r1','coordinator-weighted-optimum-r2','reasoning-path-mass-return-r8'):
  p='problems/2017-B4/reviews/'+name+'-acceptance.json';a=obj(p)
  assert a['status'].startswith('proved, independently reviewed') and not a['repair_required'] and a['unresolved_substantive_issues']==0
  b,c=check(a['accepted_copy']),check(a['candidate']);assert raw(b['path']).endswith(raw(c['path']))
  rows += [fp(p),fp(p[:-5]+'.md'),b,c]
 for p in('AGENTS.md','problems/2017-B4/statement.md','problems/2017-B4/notes/coordinator-weighted-cutpath-r1-source-audit-v1.md','problems/2017-B4/notes/coordinator-weighted-cutpath-r1-sources-v1.json','problems/2017-B4/notes/coordinator-weighted-cutpath-r1-failures-worklog-v1.md','problems/2017-B4/notes/coordinator-weighted-optimum-r2-sources-v1.md','problems/2017-B4/notes/coordinator-weighted-optimum-r2-failed-routes-v1.md','problems/2017-B4/reviews/reasoning-path-mass-return-r8-review-1-manifest-v1.json','problems/2017-B4/reviews/reasoning-path-mass-return-r8-review-2-manifest-v1.json'):
  rows.append(fp(p))
 assert len(rows)==len({x['path']for x in rows})==21
 assert fp('AGENTS.md')['sha256']=='28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff'
 return sorted(rows,key=lambda x:x['path'])
def labels():
 assert re.findall(r'(?m)^\|PM9-(\d{2})\|',raw(PRE+'obligations-v1.md').decode())==[f'{i:02d}'for i in range(1,49)]
 s=obj(PRE+'sources-v1.json');assert s['constructor']=='/root' and s['constructor_excluded_from_TWO_OTHER_whole_audits'] and s['whole_obligations']==48
 assert b'Candidate proof - unverified' in raw(PRE+'candidate-v1.md')
def prepare():
 rows=inputs();labels()
 put('baseline-v1.json',dict(at_utc=now(),protected_unique_paths=21,fingerprints=rows,current_accepted_PM8_WC_WO_suffixes_checked=True,old_PUBLIC_PM8_root_and_B_whole_manifests_bound=True,unrelated_NEW_BT_or_active_other_year_packets_opened_or_copied=False,mutable_progress_or_research_maps_not_immutable_inputs=True,historical_inventory_recopied_or_recursive_replay=False))
 put('input-validation-v1.json',dict(at_utc=now(),all21_current_necessary_inputs_match=True,ALL48_obligation_labels_checked=True,all3_current_authorities_and_unchanged_candidate_suffixes_checked=True,administrative_only_not_mathematical_proof=True))
 put('metadata-v1.json',dict(at_utc=now(),constructor='/root',constructor_excluded_from_TWO_OTHER_whole_audits=True,workers_supplied_NEW_inference=False,status='candidate proof - unverified',whole_claims=['PM9A','PM9B','PM9C'],whole_obligations=48,ENTIRE_files_including_freeze=12,TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits_and_root_reconciliation_required=True,FULL_final_model_readback_ALL_files_then_SEPARATE_readonly_verify_required=True,requested_settings=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),effective_independent_readback=None,authorized_weekly_reset=1792874445,latest_root_authoritative_TOTAL_percent=38,ceiling_TOTAL_percent=90,integration_reserve=True,automatic_later_reset_authorized=False,math_program_CAS_scan_test_optimizer_author_source_or_old_replay=False,annual_value_effectiveR_novelty_or_external_validation_claim=False))
 print(json.dumps(dict(prepared=True,protected21=True,whole_obligations=48)))
def preserved():
 assert inputs()==obj(PRE+'baseline-v1.json')['fingerprints'];labels()
def freeze():
 preserved();payloads=[fp(PRE+s)for s in NAMES]
 put('freeze-v1.json',dict(frozen_at_utc=now(),status='ENTIRE PM9 constructor checkpoint; candidate proof - unverified',constructor='/root',constructor_excluded_from_TWO_OTHER_whole_audits=True,whole_claims=['PM9A','PM9B','PM9C'],whole_obligations=48,ENTIRE_files_including_freeze=12,ENTIRE_working_main_ALL48_checks_issues_failures_sources_logs_code_ALLmetadata=True,FULL_final_model_readback_then_SEPARATE_verify_follow_this_immutable_freeze=True,TWO_OTHER_initially_blind_ENTIRE_WHOLE_reviews_and_reconciliation_required=True,mathematical_computation=False,payloads=payloads))
 print(json.dumps(dict(freeze=fp(PRE+'freeze-v1.json'),main=fp(PRE+'candidate-v1.md'),ENTIRE_files=12,whole_obligations=48)))
def verify():
 preserved();v=obj(PRE+'freeze-v1.json');assert[x['path']for x in v['payloads']]==[PRE+s for s in NAMES]
 for x in v['payloads']:check(x)
 print(json.dumps(dict(SEPARATE_postfreeze_verify='PASS',at_utc=now(),freeze=fp(PRE+'freeze-v1.json'),main=fp(PRE+'candidate-v1.md'),ENTIRE_files=12,whole_obligations=48,administrative_not_proof=True)))
if __name__=='__main__':dict(prepare=prepare,freeze=freeze,verify=verify)[sys.argv[1]]()
