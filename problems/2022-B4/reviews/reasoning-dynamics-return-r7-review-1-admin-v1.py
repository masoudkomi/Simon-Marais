#!/usr/bin/env python3
"""D7 WHOLE1 preservation only. No mathematical executable or old replay."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,re,sys
ROOT=Path(__file__).resolve().parents[3]
PRE='problems/2022-B4/reviews/reasoning-dynamics-return-r7-review-1-'
AUTHOR='problems/2022-B4/notes/reasoning-dynamics-return-r7-'
PIN=dict(path=AUTHOR+'freeze-v1.json',bytes=3391,sha256='305eb7fbd3a9c6282c34310e72c8ffd862c4ac5315996cf2cced945d503994b2')
STATIC=('report-v1.md','ledger-v1.md','issues-v1.md','sources-v1.md','sources-v1.json','worklog-v1.md','admin-v1.py')
GENERATED=('baseline-v1.json','input-validation-v1.json','metadata-v1.json')
def now():return datetime.now(timezone.utc).isoformat()
def raw(p):
    assert p=='AGENTS.md' or p.startswith('problems/2022-B4/')
    assert '..'not in Path(p).parts and not p.startswith('/')
    assert not p.startswith('problems/2022-B4/reviews/reasoning-dynamics-return-r7-review-2-')
    return(ROOT/p).read_bytes()
def obj(p):return json.loads(raw(p))
def fp(p):
    b=raw(p);return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def check(x):
    r={k:x[k]for k in('path','bytes','sha256')};assert fp(r['path'])==r,r['path'];return r
def inputs():
    rows=[check(PIN)];a=obj(PIN['path'])
    assert(a['whole_obligations'],a['all_files_including_freeze'],len(a['payloads']))==(48,13,12)
    rows +=[check(x)for x in a['payloads']]
    assert fp(AUTHOR+'candidate-v1.md')==dict(path=AUTHOR+'candidate-v1.md',bytes=16504,sha256='25ab177d6efebf1c4d5bb6e3c6bb97c4bfebed750ba782f022a4b3c94bb2d508')
    for n in('reasoning-fiber-return-r5','reasoning-dynamics-return-r6','reasoning-complexity-return-r9-v3'):
        p='problems/2022-B4/reviews/'+n+'-acceptance.json';v=obj(p)
        assert v['status'].startswith('proved, independently reviewed')and v['unresolved_substantive_issues']==0 and not v['repair_required']
        c,b=check(v['candidate']),check(v['accepted_copy']);assert raw(b['path']).endswith(raw(c['path']))
        rows +=[fp(p),fp(p[:-5]+'.md'),b]
    for p in('AGENTS.md','problems/2022-B4/statement.md','problems/2022-B4/proofs/reviewed-partials-v1.md','problems/2022-B4/notes/reasoning-fiber-return-r5-failed-routes-v1.md','problems/2022-B4/notes/reasoning-fiber-return-r5-sources-v1.md','problems/2022-B4/notes/reasoning-fiber-return-r5-sources-v1.json','problems/2022-B4/notes/reasoning-dynamics-return-r6-failures-v1.md','problems/2022-B4/notes/reasoning-dynamics-return-r6-sources-v1.md','problems/2022-B4/notes/reasoning-dynamics-return-r6-sources-v1.json'):
        rows.append(fp(p))
    assert len(rows)==len({x['path']for x in rows})==31
    return sorted(rows,key=lambda x:x['path'])
def labels():
    assert re.findall(r'(?m)^\| D7-(\d{2}) \| PASS',raw(PRE+'ledger-v1.md').decode())==[f'{i:02d}'for i in range(1,49)]
    assert obj(PRE+'sources-v1.json')['no_corresponding_NEW_A_D7_finding_file_hash_metadata_access']
def put(s,v):
    assert s in GENERATED+('manifest-v1.json',)
    with(ROOT/(PRE+s)).open('x')as f:json.dump(v,f,indent=2);f.write('\n')
def prepare():
    rows=inputs();labels()
    put('baseline-v1.json',dict(at_utc=now(),fingerprints=rows,protected_unique_paths=31,author13_and_three_current_authorities_bound=True,unrelated_historical_review_inventory_not_copied=True))
    put('input-validation-v1.json',dict(at_utc=now(),result='PASS',author13=True,protected31=True,ALL48_labels=True,three_current_scopes_and_exact_suffixes=True,administrative_only=True))
    put('metadata-v1.json',dict(at_utc=now(),reviewer='/root',constructor='/root/review_2017_coarsening_r1',constructor_excluded=True,status='ENTIRE initially blind WHOLE1 initial; findings embargoed',whole_obligations=48,ENTIRE_files_including_manifest=11,no_substantive_defect_or_required_repair=True,closed_scope_notes=7,no_corresponding_NEW_A_D7_finding_file_hash_metadata_access=True,FULL_final_ALL11_model_readback_then_SEPARATE_verify_required=True,BOTH_explicit_before_release=True,requested_inherited=dict(model='gpt-6.1-sol',reasoning='max'),effective_readback=None,authorized_weekly_reset=1792874445,ceiling_TOTAL_percent=90,integration_reserve=True,automatic_later_window_authorized=False,mathematical_program_CAS_scan_or_old_replay=False))
    print(json.dumps(dict(prepare='PASS',protected31=True,ALL48=True,ENTIRE_files=11)))
def preserved():assert inputs()==obj(PRE+'baseline-v1.json')['fingerprints'];labels()
def freeze():
    preserved()
    put('manifest-v1.json',dict(frozen_at_utc=now(),status='ENTIRE initially blind WHOLE1 initial; findings embargoed',whole_obligations=48,ENTIRE_files_including_manifest=11,report_ALL48_issues_sources_log_code_ALLmetadata=True,FULL_final_ALL11_model_readback_then_SEPARATE_verify_follow_freeze=True,no_corresponding_NEW_A_D7_finding_file_hash_metadata_access=True,BOTH_explicit_before_release=True,payloads=[fp(PRE+s)for s in STATIC+GENERATED]))
    print(json.dumps(dict(manifest=fp(PRE+'manifest-v1.json'),ENTIRE_files=11,ALL48=True)))
def verify():
    preserved();m=obj(PRE+'manifest-v1.json')
    assert[x['path']for x in m['payloads']]==[PRE+s for s in STATIC+GENERATED]
    for x in m['payloads']:check(x)
    print(json.dumps(dict(SEPARATE_postfreeze_verify='PASS',at_utc=now(),manifest=fp(PRE+'manifest-v1.json'),report=fp(PRE+'report-v1.md'),ENTIRE_files=11,whole_obligations=48,protected31=True,administrative_not_proof=True)))
if __name__=='__main__':dict(prepare=prepare,freeze=freeze,verify=verify)[sys.argv[1]]()
