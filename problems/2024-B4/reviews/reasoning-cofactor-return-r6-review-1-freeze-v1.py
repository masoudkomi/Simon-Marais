#!/usr/bin/env python3
"""R6 OTHER root whole48 metadata preservation only, never mathematics."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re,sys
ROOT=Path(__file__).resolve().parents[3]
PRE='problems/2024-B4/reviews/reasoning-cofactor-return-r6-review-1-'
AUTHOR='problems/2024-B4/notes/reasoning-cofactor-return-r6-'
FORBIDDEN='problems/2024-B4/reviews/reasoning-cofactor-return-r6-review-2-'
EXPECTED=dict(path=AUTHOR+'freeze-v1.json',bytes=3001,sha256='ea0a7c41741ca3655c36825a6a299c1859505855c786ea7494a9204995a0b8a9')
PAYLOADS=('report-v1.md','ledger-v1.md','issues-v1.md','source-checks-v1.md','sources-v1.json','worklog-v1.md','freeze-v1.py','baseline-v1.json','metadata-v1.json','input-validation-v1.json')
def now():return datetime.now(timezone.utc).isoformat()
def raw(p):
 assert isinstance(p,str)and not p.startswith('/')and '..'not in Path(p).parts
 assert not p.startswith(FORBIDDEN),p
 return(ROOT/p).read_bytes()
def obj(p):return json.loads(raw(p))
def fp(p):
 b=raw(p);return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def check(x):
 y={k:x[k]for k in ('path','bytes','sha256')};assert fp(x['path'])==y,x['path'];return y
def put(s,v):
 assert s in ('baseline-v1.json','metadata-v1.json','input-validation-v1.json','manifest-v1.json')
 with(ROOT/(PRE+s)).open('x')as f:json.dump(v,f,indent=2);f.write('\n')
def inputs():
 rows=[check(EXPECTED)];a=obj(EXPECTED['path']);assert a['whole_obligations']==48 and len(a['artifacts'])==11
 for x in a['artifacts']:
  assert x['path'].startswith(AUTHOR);rows.append(check(x))
 bindings=[]
 for stem,field in [('structural','accepted_proof'),('cofactor-dominant-r4','accepted_copy')]:
  p='problems/2024-B4/reviews/'+stem+'-acceptance.json';v=obj(p);assert v['status'].startswith('proved, independently reviewed')
  body,candidate=check(v[field]),check(v['candidate']);rows += [fp(p),fp(p[:-5]+'.md'),body,candidate]
  if stem=='cofactor-dominant-r4':assert raw(body['path']).endswith(raw(candidate['path']))
  bindings.append(dict(authority=p,accepted_body=body,candidate=candidate,editorial_T1_heading_change_not_falsely_suffix_asserted=stem=='structural'))
 rows += [fp('AGENTS.md'),fp('problems/2024-B4/statement.md')]
 assert len(rows)==len({x['path']for x in rows})==22
 return sorted(rows,key=lambda x:x['path']),bindings
def labels():
 assert [int(x)for x in re.findall(r'(?m)^(\d+)\. PASS',raw(PRE+'ledger-v1.md').decode())]==list(range(1,49))
 s=obj(PRE+'sources-v1.json');assert s['whole_obligations']==48 and s['constructor_excluded']and not s['root_NEW_construction_contribution']
 assert s['no_corresponding_NEW_A_R6_finding_file_hash_or_metadata_accessed']
def baseline():
 rows,b=inputs();labels();put('baseline-v1.json',dict(at_utc=now(),protected_paths=22,fingerprints=rows,current_accepted_bindings=b,no_recursive_historical_or_mutable_guard_replay=True,forbidden_NEW_peer_prefix_never_opened_or_hashed=FORBIDDEN));print(json.dumps(dict(baseline=fp(PRE+'baseline-v1.json'),protected_paths=22)))
def preserved():
 v=obj(PRE+'baseline-v1.json');rows,b=inputs();labels();assert rows==v['fingerprints']and b==v['current_accepted_bindings']
def freeze():
 preserved();put('metadata-v1.json',dict(at_utc=now(),role='OTHER initiallyblind ENTIRE WHOLE R6 review1',reviewer='/root',constructor='/root/review_2017_coarsening_r1',constructor_excluded=True,root_NEW_construction_contribution=False,root_OLD_CG_R4_R5_constructor_not_new_self_recertification=True,whole_obligations=48,substantive_defects=0,required_repairs=0,closed_scope_notes=6,no_corresponding_NEW_peer_findings_files_hash_metadata_accessed=True,requested_settings=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),independent_effective_readback=None,metadata_only_not_proof=True))
 put('input-validation-v1.json',dict(at_utc=now(),ENTIRE_author12_hashes_checked=True,T1_R4_current_MD_JSON_body_candidate_bindings_checked=True,R4_suffix_exact_T1_editorial_exception_retained=True,ALL48_ordered_dispositions_present=True,protected_paths=22,no_NEW_peer_read_or_hash=True,no_mathematical_executable_author_source_old_certificate_rerun=True,FULL_readback_and_SEPARATE_verify_required_before_identity_handoff=True))
 artifacts=[fp(PRE+s)for s in PAYLOADS];put('manifest-v1.json',dict(frozen_at_utc=now(),status='initial OTHER ENTIRE whole R6 review1; not acceptance',whole_obligations=48,ENTIRE_report_ALL48_issues_sources_log_code_ALLmetadata=True,reviewer='/root',constructor_excluded=True,root_NEW_construction_contribution=False,substantive_defects=0,required_repairs=0,closed_scope_notes=6,protected_paths=22,no_corresponding_NEW_peer_access_or_hash=True,BOTH_ENTIRE_initials_required_before_findings_release=True,artifacts=artifacts));print(json.dumps(dict(manifest=fp(PRE+'manifest-v1.json'),report=artifacts[0],ENTIRE_files=11,whole_obligations=48)))
def verify():
 preserved();v=obj(PRE+'manifest-v1.json');assert[x['path']for x in v['artifacts']]==[PRE+s for s in PAYLOADS]
 for x in v['artifacts']:check(x)
 print(json.dumps(dict(separate_postfreeze_verify='PASS',at_utc=now(),ENTIRE_files=11,whole_obligations=48,protected_paths=22,no_NEW_peer_read_or_hash=True,manifest=fp(PRE+'manifest-v1.json'),report=v['artifacts'][0])))
if __name__=='__main__':dict(baseline=baseline,freeze=freeze,verify=verify)[sys.argv[1]]()
