#!/usr/bin/env python3
"""Affected R19 WHOLE1 byte/label preservation only; no math execution."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, sys
ROOT=Path(__file__).resolve().parents[3]
PRE='problems/2021-B4/reviews/reasoning-center-return-r19-review-1-'
AUTHOR='problems/2021-B4/notes/reasoning-center-return-r19-'
PIN={'path':AUTHOR+'freeze-v1.1.json','bytes':4753,'sha256':'1b86a88b22a1cf755836900d314e26b7ac109f83e3031b03254a78a3d36f49fd'}
STATIC=('report-v1.1.md','ledger-v1.1.md','issues-v1.1.md','sources-v1.1.md','sources-v1.1.json','worklog-v1.1.md','admin-v1.1.py')
GENERATED=('baseline-v1.1.json','input-validation-v1.1.json','metadata-v1.1.json')
def now():return datetime.now(timezone.utc).isoformat()
def raw(p):
    assert p=='AGENTS.md' or p.startswith('problems/2021-B4/')
    assert '..' not in Path(p).parts and not p.startswith('/')
    assert not ('reasoning-center-return-r19-review-2-' in p and ('v1.1' in p or 'reaudit' in p))
    return (ROOT/p).read_bytes()
def obj(p):return json.loads(raw(p))
def fp(p):
    b=raw(p);return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def check(x):
    y={k:x[k] for k in ('path','bytes','sha256')};assert fp(x['path'])==y,x['path'];return y
def inputs():
    rows=[check(PIN)];a=obj(PIN['path'])
    assert (a['whole_obligations'],a['ENTIRE_files'],len(a['payloads']))==(76,16,15)
    rows += [check(x) for x in a['payloads']]
    assert fp(AUTHOR+'candidate-v1.1.md')==dict(path=AUTHOR+'candidate-v1.1.md',bytes=23302,sha256='fd5a5399414c60c20797b63dfa9f55b8f66ac679fdd5458488c3250e3605a56a')
    for n in ('reasoning-center-return-r18','reasoning-center-return-r17','reasoning-return-r8','reasoning-return-r5'):
        p='problems/2021-B4/reviews/'+n+'-acceptance.json';v=obj(p)
        assert v['status'].startswith('proved, independently reviewed') and v['unresolved_substantive_issues']==0 and not v['repair_required']
        c,b=check(v['candidate']),check(v['accepted_copy']);assert raw(b['path']).endswith(raw(c['path']))
        rows += [fp(p),fp(p[:-5]+'.md'),b]
    for p in ('AGENTS.md','problems/2021-B4/statement.md',PRE+'manifest-v1.json',PRE+'sources-v1.json','problems/2021-B4/reviews/reasoning-center-return-r19-review-2-manifest-v1.json','problems/2021-B4/reviews/reasoning-center-return-r19-coordinator-reconciliation-v1.md','problems/2021-B4/reviews/reasoning-center-return-r19-coordinator-reconciliation-v1.json'):
        rows.append(fp(p))
    assert len(rows)==len({x['path'] for x in rows})==35
    return sorted(rows,key=lambda x:x['path'])
def labels():
    text=raw(PRE+'ledger-v1.1.md').decode()
    assert re.findall(r'(?m)^\| R19-(\d{2}) \| PASS',text)==[f'{i:02d}'for i in range(1,65)]
    assert re.findall(r'(?m)^\| R19-FC(\d{2}) \| PASS',text)==[f'{i:02d}'for i in range(1,13)]
    assert obj(PRE+'sources-v1.1.json')['no_corresponding_NEW_B_affected_finding_file_hash_metadata_access']
def put(s,v):
    assert s in GENERATED+('manifest-v1.1.json',)
    with(ROOT/(PRE+s)).open('x')as f:json.dump(v,f,indent=2);f.write('\n')
def prepare():
    rows=inputs();labels()
    put('baseline-v1.1.json',dict(at_utc=now(),fingerprints=rows,protected_unique_paths=35,all16_author_files_four_current_authorities_and_original_review_identities_bound=True,historical_mutable_map_not_current_proof_premise=True,no_recursive_historical_inventory_copy=True))
    put('input-validation-v1.1.json',dict(at_utc=now(),result='PASS',protected35=True,author16=True,ALL76_ledger_labels=True,exact_candidate_suffixes=True,administrative_only=True))
    put('metadata-v1.1.json',dict(at_utc=now(),reviewer='/root',constructor='/root/review_2021_reasoning_j15_r2',constructor_excluded=True,status='affected ENTIRE WHOLE1 initial; findings embargoed',whole_obligations=76,original64_plus_repair12=True,ENTIRE_files_including_manifest=11,original_R19R2_01_resolved=True,original_root_miss_disclosed=True,new_substantive_defects_or_required_repairs=0,closed_scope_notes=6,no_corresponding_NEW_B_affected_finding_file_hash_metadata_access=True,FULL_final_ALL11_readback_then_SEPARATE_verify_required=True,BOTH_explicit_before_release=True,requested_inherited=dict(model='gpt-6.1-sol',reasoning='max'),effective_readback=None,authorized_weekly_reset=1792874445,ceiling_TOTAL_percent=90,integration_reserve=True,automatic_later_window_authorized=False,mathematical_program_CAS_scan_or_old_replay=False))
    print(json.dumps(dict(prepare='PASS',protected35=True,ALL76=True,ENTIRE_files=11)))
def preserved():assert inputs()==obj(PRE+'baseline-v1.1.json')['fingerprints'];labels()
def freeze():
    preserved()
    put('manifest-v1.1.json',dict(frozen_at_utc=now(),status='ENTIRE affected initially blind WHOLE1 initial; findings embargoed',whole_obligations=76,ENTIRE_files_including_manifest=11,all_report_ALL76_issues_sources_log_code_ALLmetadata=True,FULL_final_ALL11_model_readback_then_SEPARATE_verify_follow_freeze=True,no_corresponding_NEW_B_affected_finding_file_hash_metadata_access=True,BOTH_explicit_before_release=True,payloads=[fp(PRE+s)for s in STATIC+GENERATED]))
    print(json.dumps(dict(manifest=fp(PRE+'manifest-v1.1.json'),ENTIRE_files=11,ALL76=True)))
def verify():
    preserved();v=obj(PRE+'manifest-v1.1.json')
    assert[x['path']for x in v['payloads']]==[PRE+s for s in STATIC+GENERATED]
    for x in v['payloads']:check(x)
    print(json.dumps(dict(SEPARATE_postfreeze_verify='PASS',at_utc=now(),manifest=fp(PRE+'manifest-v1.1.json'),report=fp(PRE+'report-v1.1.md'),ENTIRE_files=11,whole_obligations=76,protected35=True,administrative_not_proof=True)))
if __name__=='__main__':dict(prepare=prepare,freeze=freeze,verify=verify)[sys.argv[1]]()
