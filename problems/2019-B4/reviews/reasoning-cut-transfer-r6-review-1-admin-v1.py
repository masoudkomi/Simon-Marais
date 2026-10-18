#!/usr/bin/env python3
"""AT WHOLE1 integrity administration only; no mathematics or old replay."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,sys
ROOT=Path(__file__).resolve().parents[3]
PRE='problems/2019-B4/reviews/reasoning-cut-transfer-r6-review-1-'
AUTHOR='problems/2019-B4/notes/reasoning-cut-transfer-r6-'
PIN=dict(path=AUTHOR+'freeze-v1.json',bytes=5022,sha256='4b8e9a485850e2410f045ad4d83e13184d2d6ce60a327b153cd47313f483b4cc')
STATIC=('report-v1.md','ledger-v1.md','issues-v1.md','sources-v1.md','sources-v1.json','worklog-v1.md','admin-v1.py')
GENERATED=('baseline-v1.json','input-validation-v1.json','metadata-v1.json')
NAMES=('reasoning-cut-transfer-r5','reasoning-cut-transfer-r4','reasoning-return-r7','reasoning-critical-return-r2','reasoning-cut-number-r3','reasoning-growth-return-r1')
def now():return datetime.now(timezone.utc).isoformat()
def raw(p):
    assert p=='AGENTS.md' or p.startswith('problems/2019-B4/')
    assert '..'not in Path(p).parts and not p.startswith('/')
    assert not p.startswith('problems/2019-B4/reviews/reasoning-cut-transfer-r6-review-2-')
    return(ROOT/p).read_bytes()
def obj(p):return json.loads(raw(p))
def fp(p):
    b=raw(p);return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def check(x):
    r={k:x[k]for k in('path','bytes','sha256')};assert fp(r['path'])==r,r['path'];return r
def inputs():
    rows=[check(PIN)];a=obj(PIN['path'])
    assert(a['whole_obligations'],a['ENTIRE_files_including_freeze'],len(a['payloads']))==(64,11,10)
    rows +=[check(x)for x in a['payloads']]
    assert fp(AUTHOR+'candidate-v1.md')==dict(path=AUTHOR+'candidate-v1.md',bytes=20223,sha256='1f5e0b02047806420b52fe503f85567f23dccfd05045a710b802d03dc9e0f40d')
    for n in NAMES:
        p='problems/2019-B4/reviews/'+n+'-acceptance.json';v=obj(p)
        assert v['status'].startswith('proved, independently reviewed')and v['unresolved_substantive_issues']==0 and not v['repair_required']
        c,b=check(v['candidate']),check(v['accepted_copy']);assert raw(b['path']).endswith(raw(c['path']))
        rows +=[fp(p),fp(p[:-5]+'.md'),b]
    p='problems/2019-B4/reviews/reasoning-cut-transfer-r4-presentation-erratum-v1.json';e=obj(p)
    operative=check(e['operative_accepted_copy']);suffix=check(e['unchanged_candidate_suffix']);assert raw(operative['path']).endswith(raw(suffix['path']))
    rows +=[fp(p),fp(p[:-5]+'.md'),operative,fp('AGENTS.md'),fp('problems/2019-B4/statement.md')]
    assert len(rows)==len({x['path']for x in rows})==34
    return sorted(rows,key=lambda x:x['path'])
def labels():
    assert re.findall(r'(?m)^\| R6-(\d{2}) \| PASS',raw(PRE+'ledger-v1.md').decode())==[f'{i:02d}'for i in range(1,65)]
    assert obj(PRE+'sources-v1.json')['no_corresponding_NEW_A_AT_finding_file_hash_metadata_access']
def put(s,v):
    assert s in GENERATED+('manifest-v1.json',)
    with(ROOT/(PRE+s)).open('x')as f:json.dump(v,f,indent=2);f.write('\n')
def prepare():
    rows=inputs();labels()
    put('baseline-v1.json',dict(at_utc=now(),fingerprints=rows,protected_unique_paths=34,ENTIRE_author11_six_current_authorities_CToperative_erratum_bound=True,unrelated_historical_inventory_not_copied=True))
    put('input-validation-v1.json',dict(at_utc=now(),result='PASS',author11=True,protected34=True,ALL64_labels=True,current_acceptances_and_exact_suffixes_checked=True,administrative_only=True))
    put('metadata-v1.json',dict(at_utc=now(),reviewer='/root',constructor='/root/review_2022_complexity_r2',constructor_excluded=True,status='ENTIRE initially blind WHOLE1 initial; findings embargoed',whole_obligations=64,ENTIRE_files_including_manifest=11,no_substantive_defect_or_required_repair=True,closed_scope_notes=8,no_corresponding_NEW_A_AT_finding_file_hash_metadata_access=True,FULL_final_ALL11_model_readback_then_SEPARATE_verify_required=True,BOTH_explicit_before_release=True,requested_inherited=dict(model='gpt-6.1-sol',reasoning='max'),effective_readback=None,authorized_weekly_reset=1792874445,ceiling_TOTAL_percent=90,integration_reserve=True,automatic_later_window_authorized=False,mathematical_program_CAS_scan_or_old_replay=False))
    print(json.dumps(dict(prepare='PASS',protected34=True,ALL64=True,ENTIRE_files=11)))
def preserved():assert inputs()==obj(PRE+'baseline-v1.json')['fingerprints'];labels()
def freeze():
    preserved()
    put('manifest-v1.json',dict(frozen_at_utc=now(),status='ENTIRE initially blind WHOLE1 initial; findings embargoed',whole_obligations=64,ENTIRE_files_including_manifest=11,report_ALL64_issues_sources_log_code_ALLmetadata=True,FULL_final_ALL11_model_readback_then_SEPARATE_verify_follow_freeze=True,no_corresponding_NEW_A_AT_finding_file_hash_metadata_access=True,BOTH_explicit_before_release=True,payloads=[fp(PRE+s)for s in STATIC+GENERATED]))
    print(json.dumps(dict(manifest=fp(PRE+'manifest-v1.json'),ENTIRE_files=11,ALL64=True)))
def verify():
    preserved();m=obj(PRE+'manifest-v1.json')
    assert[x['path']for x in m['payloads']]==[PRE+s for s in STATIC+GENERATED]
    for x in m['payloads']:check(x)
    print(json.dumps(dict(SEPARATE_postfreeze_verify='PASS',at_utc=now(),manifest=fp(PRE+'manifest-v1.json'),report=fp(PRE+'report-v1.md'),ENTIRE_files=11,whole_obligations=64,protected34=True,administrative_not_proof=True)))
if __name__=='__main__':dict(prepare=prepare,freeze=freeze,verify=verify)[sys.argv[1]]()
