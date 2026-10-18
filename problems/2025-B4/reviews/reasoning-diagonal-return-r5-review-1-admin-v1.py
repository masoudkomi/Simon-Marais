#!/usr/bin/env python3
"""RD OTHER root whole48 metadata only; no mathematical computation."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re,sys
ROOT=Path(__file__).resolve().parents[3]
PRE='problems/2025-B4/reviews/reasoning-diagonal-return-r5-review-1-'
AUTHOR='problems/2025-B4/notes/reasoning-diagonal-return-r5-'
FORBIDDEN='problems/2025-B4/reviews/reasoning-diagonal-return-r5-review-2-'
EXPECTED=dict(path=AUTHOR+'freeze-v1.json',bytes=8179,sha256='b81f17c54ed4df58c1d2ee32a8123c6d0e46aa9f8d05d9df23e5aa06d1c6b6c2')
PAYLOADS=('report-v1.md','ledger-v1.md','issues-v1.md','source-checks-v1.md','sources-v1.json','worklog-v1.md','admin-v1.py','baseline-v1.json','metadata-v1.json','input-validation-v1.json')
def now():return datetime.now(timezone.utc).isoformat()
def raw(p):
 assert isinstance(p,str) and not p.startswith('/') and '..'not in Path(p).parts
 assert not p.startswith(FORBIDDEN),p
 return(ROOT/p).read_bytes()
def obj(p):return json.loads(raw(p))
def fp(p):
 b=raw(p);return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def check(x):
 y={k:x[k]for k in('path','bytes','sha256')};assert fp(x['path'])==y,x['path'];return y
def put(s,v):
 assert s in('baseline-v1.json','input-validation-v1.json','metadata-v1.json','manifest-v1.json')
 with(ROOT/(PRE+s)).open('x')as f:json.dump(v,f,indent=2);f.write('\n')
def inputs():
 rows=[check(EXPECTED)];v=obj(EXPECTED['path']);assert v['whole_obligations']==48 and len(v['payloads'])==10
 for x in v['payloads']:
  assert x['path'].startswith(AUTHOR);rows.append(check(x))
 ab=obj(AUTHOR+'baseline-v1.json');assert len(ab['protected_inputs'])==35
 for x in ab['protected_inputs']:check(x)
 for name in ['reasoning-branch-return-r4','reasoning-Runge-return-r3','reasoning-Runge-return-r2','reasoning-return-r6']:
  p='problems/2025-B4/reviews/'+name+'-acceptance.json';v=obj(p);assert v['status'].startswith('proved, independently reviewed')
  body,can=check(v['accepted_copy']),check(v['candidate']);assert raw(body['path']).endswith(raw(can['path']))
  rows += [fp(p),fp(p[:-5]+'.md'),body,can]
 rows += [fp('AGENTS.md'),fp('problems/2025-B4/statement.md')]
 assert len(rows)==len({x['path']for x in rows})==29
 return sorted(rows,key=lambda x:x['path'])
def labels():
 assert[int(x)for x in re.findall(r'(?m)^(\d+)\. PASS',raw(PRE+'ledger-v1.md').decode())]==list(range(1,49))
 s=obj(PRE+'sources-v1.json');assert s['whole_obligations']==48 and s['constructor_excluded'] and not s['root_NEW_construction_contribution']
 assert s['no_corresponding_NEW_A_RD_finding_file_hash_metadata_accessed']
def prepare():
 rows=inputs();labels()
 put('baseline-v1.json',dict(at_utc=now(),protected_unique_paths=29,fingerprints=rows,author_current35_fingerprints_checked_not_recopied=True,no_recursive_historical_inventory_replay=True,forbidden_NEW_peer_prefix_never_read_or_hashed=FORBIDDEN))
 put('input-validation-v1.json',dict(at_utc=now(),ENTIRE_author11_checked=True,author_necessary35_checked=True,all_four_current_accepted_body_MD_JSON_candidate_suffix_bindings_checked=True,ALL48_ordered_dispositions=True,no_NEW_peer_access_or_hash=True,administrative_not_proof=True))
 put('metadata-v1.json',dict(at_utc=now(),reviewer='/root',constructor='/root/review_2022_complexity_r2',constructor_excluded=True,root_NEW_construction_contribution=False,root_OLDER_RS_quotient_contribution_disclosed_geometry_unused=True,role='OTHER initiallyblind ENTIRE WHOLE RD review1',whole_obligations=48,ENTIRE_files=11,substantive_defects=0,required_repairs=0,closed_notes=7,no_corresponding_NEW_peer_access_or_hash=True,requested_settings=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),effective_independent_readback=None,FULL_entire_readback_then_SEPARATE_verify_required=True))
 print(json.dumps(dict(prepared=True,protected29=True,author_current35_checked=True)))
def preserved():
 assert inputs()==obj(PRE+'baseline-v1.json')['fingerprints'];labels()
def freeze():
 preserved();payloads=[fp(PRE+s)for s in PAYLOADS]
 put('manifest-v1.json',dict(frozen_at_utc=now(),status='initial OTHER ENTIRE WHOLE RD review1,not acceptance',reviewer='/root',constructor_excluded=True,root_NEW_construction_contribution=False,whole_obligations=48,ENTIRE_files=11,ENTIRE_report_ALL48_issues_sources_log_code_ALLmetadata=True,substantive_defects=0,required_repairs=0,closed_notes=7,no_corresponding_NEW_peer_finding_file_hash_metadata_accessed=True,BOTH_ENTIRE_before_findings_release_required=True,protected_unique_paths=29,payloads=payloads))
 print(json.dumps(dict(manifest=fp(PRE+'manifest-v1.json'),report=payloads[0],ENTIRE_files=11,whole_obligations=48)))
def verify():
 preserved();v=obj(PRE+'manifest-v1.json');assert[x['path']for x in v['payloads']]==[PRE+s for s in PAYLOADS]
 for x in v['payloads']:check(x)
 print(json.dumps(dict(SEPARATE_postfreeze_verify='PASS',at_utc=now(),manifest=fp(PRE+'manifest-v1.json'),report=v['payloads'][0],ENTIRE_files=11,whole_obligations=48,no_NEW_peer_access_or_hash=True,metadata_only_not_proof=True)))
if __name__=='__main__':dict(prepare=prepare,freeze=freeze,verify=verify)[sys.argv[1]]()
