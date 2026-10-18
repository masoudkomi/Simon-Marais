#!/usr/bin/env python3
"""Create-only root OTHER BT WHOLE56 metadata; no mathematics implemented."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re,sys
ROOT=Path(__file__).resolve().parents[3]
PRE='problems/2019-B4/reviews/reasoning-cut-transfer-r5-review-1-'
AUTHOR='problems/2019-B4/notes/reasoning-cut-transfer-r5-'
FORBIDDEN='problems/2019-B4/reviews/reasoning-cut-transfer-r5-review-2-'
EXPECTED=dict(path=AUTHOR+'freeze-v1.json',bytes=8902,sha256='52f8a794c3d82d3803a6b9700496cac2dff4b81a84e3f6c935b1bb9fbe107896')
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
 rows=[check(EXPECTED)];v=obj(EXPECTED['path'])
 assert v['whole_obligations']==56 and len(v['payloads'])==10
 for x in v['payloads']:
  assert x['path'].startswith(AUTHOR);rows.append(check(x))
 baseline=obj(AUTHOR+'baseline-v1.json');assert len(baseline['records'])==43
 for x in baseline['records']:check(x)
 for name in('reasoning-cut-transfer-r4','reasoning-critical-return-r2','reasoning-return-r7','reasoning-cut-number-r3','reasoning-growth-return-r1'):
  p='problems/2019-B4/reviews/'+name+'-acceptance.json';a=obj(p)
  assert a['status'].startswith('proved, independently reviewed')
  body,can=check(a['accepted_copy']),check(a['candidate'])
  assert raw(body['path']).endswith(raw(can['path']))
  rows += [fp(p),fp(p[:-5]+'.md'),body,can]
 ep='problems/2019-B4/reviews/reasoning-cut-transfer-r4-presentation-erratum-v1.json';e=obj(ep)
 for k in('old_accepted_copy','operative_accepted_copy','unchanged_candidate_suffix','historical_authority'):check(e[k])
 assert raw(e['old_accepted_copy']['path']).replace(b't0=010',b't0=10',1)==raw(e['operative_accepted_copy']['path'])
 rows += [fp(ep),fp(ep[:-5]+'.md'),check(e['operative_accepted_copy']),fp('AGENTS.md'),fp('problems/2019-B4/statement.md')]
 for p in('notes/secondpass-canonical-renewal.md','proofs/reviewed-secondpass-v1.1.md','reviews/secondpass-acceptance.md','notes/reasoning-cut-transfer-r4-failed-routes-v1.md','notes/reasoning-critical-return-r2-failed-routes-v1.md','notes/coordinator-unmarked-greedy-failure-v1.md'):
  rows.append(fp('problems/2019-B4/'+p))
 assert len(rows)==len({x['path']for x in rows})==42
 return sorted(rows,key=lambda x:x['path'])
def labels():
 assert[int(x)for x in re.findall(r'(?m)^(\d+)\. PASS',raw(PRE+'ledger-v1.md').decode())]==list(range(1,57))
 s=obj(PRE+'sources-v1.json');assert s['whole_obligations']==56 and s['constructor_excluded'] and not s['root_NEW_construction_contribution']
 assert s['no_corresponding_NEW_A_BT_finding_file_hash_metadata_accessed']
def prepare():
 rows=inputs();labels()
 put('baseline-v1.json',dict(at_utc=now(),protected_unique_paths=42,fingerprints=rows,author_current43_declarations_checked_not_recopied=True,recursive_historical_inventory_replay=False,forbidden_NEW_peer_prefix_never_opened_or_hashed=FORBIDDEN))
 put('input-validation-v1.json',dict(at_utc=now(),ENTIRE_author11_checked=True,author_current43_declarations_checked=True,all5_current_bodies_MD_JSON_candidate_suffix_checked=True,CT_v12_erratum_exact_token_checked=True,ALL56_ordered_dispositions=True,no_NEW_peer_access_or_hash=True,administrative_not_proof=True))
 put('metadata-v1.json',dict(at_utc=now(),reviewer='/root',constructor='/root/review_2022_complexity_r2',constructor_excluded=True,root_NEW_construction_contribution=False,older_2019_roles_disclosed_not_self_recertified=True,role='OTHER initially blind ENTIRE WHOLE BT review1',whole_obligations=56,ENTIRE_files_including_manifest=11,substantive_defects=0,required_repairs=0,closed_notes=8,no_corresponding_NEW_peer_access_or_hash=True,requested_settings=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),effective_independent_readback=None,FULL_entire_readback_then_SEPARATE_verify_required=True))
 print(json.dumps(dict(prepared=True,protected42=True,author_current43_checked=True)))
def preserved():
 assert inputs()==obj(PRE+'baseline-v1.json')['fingerprints'];labels()
def freeze():
 preserved();payloads=[fp(PRE+s)for s in PAYLOADS]
 put('manifest-v1.json',dict(frozen_at_utc=now(),status='initial OTHER ENTIRE WHOLE BT review1, not acceptance',reviewer='/root',constructor_excluded=True,root_NEW_construction_contribution=False,whole_obligations=56,ENTIRE_files=11,ENTIRE_report_ALL56_issues_sources_log_code_ALLmetadata=True,substantive_defects=0,required_repairs=0,closed_notes=8,no_corresponding_NEW_peer_finding_file_hash_metadata_accessed=True,BOTH_ENTIRE_before_findings_release_required=True,protected_unique_paths=42,payloads=payloads))
 print(json.dumps(dict(manifest=fp(PRE+'manifest-v1.json'),report=payloads[0],ENTIRE_files=11,whole_obligations=56)))
def verify():
 preserved();v=obj(PRE+'manifest-v1.json');assert[x['path']for x in v['payloads']]==[PRE+s for s in PAYLOADS]
 for x in v['payloads']:check(x)
 print(json.dumps(dict(SEPARATE_postfreeze_verify='PASS',at_utc=now(),manifest=fp(PRE+'manifest-v1.json'),report=v['payloads'][0],ENTIRE_files=11,whole_obligations=56,no_NEW_peer_access_or_hash=True,metadata_only_not_proof=True)))
if __name__=='__main__':dict(prepare=prepare,freeze=freeze,verify=verify)[sys.argv[1]]()
