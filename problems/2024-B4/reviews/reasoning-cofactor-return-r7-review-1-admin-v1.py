#!/usr/bin/env python3
"""R7 review byte integrity only; no mathematical computation or old replay."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,re,sys
ROOT=Path(__file__).resolve().parents[3]
PRE='problems/2024-B4/reviews/reasoning-cofactor-return-r7-review-1-'
AUTHOR='problems/2024-B4/notes/reasoning-cofactor-return-r7-freeze-v1.json'
PIN=dict(path=AUTHOR,bytes=3129,sha256='18d2a87ffb4f0f7ca2140659a0883f697974620ba507453fdfda01b8cff49cd1')
STATIC=('report-v1.md','ledger-v1.md','issues-v1.md','sources-v1.md','sources-v1.json','worklog-v1.md','admin-v1.py')
GENERATED=('baseline-v1.json','input-validation-v1.json','metadata-v1.json')
def now():return datetime.now(timezone.utc).isoformat()
def raw(p):
    assert p=='AGENTS.md' or p.startswith('problems/2024-B4/')
    assert not p.startswith('/') and '..'not in Path(p).parts
    assert not p.startswith('problems/2024-B4/reviews/reasoning-cofactor-return-r7-review-2-')
    return(ROOT/p).read_bytes()
def obj(p):return json.loads(raw(p))
def fp(p):
    b=raw(p);return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def check(x):
    y={k:x[k]for k in('path','bytes','sha256')};assert fp(x['path'])==y,x['path'];return y
def inputs():
    rows=[check(PIN)];a=obj(AUTHOR)
    assert a['whole_obligations']==64 and a['all_files_including_freeze']==13
    rows += [check(x)for x in a['artifacts']]
    for stem,key in [('structural','accepted_proof'),('reasoning-cofactor-return-r6','accepted_copy')]:
        p='problems/2024-B4/reviews/'+stem+'-acceptance.json';v=obj(p)
        assert v['status'].startswith('proved, independently reviewed')
        if stem=='structural':
            assert v['remaining_substantive_objections']==0 and not v['substantive_author_repair_required']
        else:
            assert v['unresolved_substantive_issues']==0 and not v['repair_required']
            assert raw(v[key]['path']).endswith(raw(v['candidate']['path']))
        rows += [fp(p),fp(p[:-5]+'.md'),check(v[key])]
    rows += [fp('AGENTS.md'),fp('problems/2024-B4/statement.md')]
    assert len(rows)==len({x['path']for x in rows})==21
    return sorted(rows,key=lambda x:x['path'])
def labels():
    assert re.findall(r'(?m)^(\d+)\. PASS — ',raw(PRE+'ledger-v1.md').decode())==[str(i)for i in range(1,65)]
    assert obj(PRE+'sources-v1.json')['no_corresponding_NEW_A_R7_finding_file_hash_metadata_access']
def put(s,v):
    assert s in GENERATED+('manifest-v1.json',)
    with(ROOT/(PRE+s)).open('x')as f:json.dump(v,f,indent=2);f.write('\n')
def prepare():
    rows=inputs();labels()
    put('baseline-v1.json',dict(at_utc=now(),fingerprints=rows,protected_unique_paths=21,author_ENTIRE13_and_two_current_authorities_bound=True,unrelated_pending_review_ancestry_not_copied=True))
    put('input-validation-v1.json',dict(at_utc=now(),result='PASS',protected21=True,ALL64_labels_checked=True,author13_and_current_accepted_bodies_byte_checked=True,mathematical_computation=False))
    put('metadata-v1.json',dict(at_utc=now(),status='ENTIRE initially blind WHOLE1; findings embargoed',reviewer='/root',constructor='/root/review_2017_coarsening_r1',constructor_excluded=True,root_NEW_inference=False,whole_obligations=64,ENTIRE_files_including_manifest=11,no_corresponding_NEW_A_R7_finding_file_hash_metadata_access=True,ALL_files_freeze_FULL_final_readback_SEPARATE_verify_before_peer=True,BOTH_explicit_before_release=True,substantive_defects=0,required_repairs=0,closed_scope_notes=6,requested_settings=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),independent_effective_readback=None,authorized_weekly_reset=1792874445,ceiling_TOTAL_percent=90,integration_reserve=True,automatic_later_window_authorized=False,mathematical_program_CAS_scan_author_source_or_old_replay=False))
    print(json.dumps(dict(prepare='PASS',protected21=True,ALL64=True)))
def preserved():
    assert inputs()==obj(PRE+'baseline-v1.json')['fingerprints'];labels()
def freeze():
    preserved();put('manifest-v1.json',dict(frozen_at_utc=now(),status='ENTIRE initially blind WHOLE1 initial; findings embargoed',reviewer='/root',constructor_excluded=True,whole_obligations=64,ENTIRE_files_including_manifest=11,all_report_ALL64_issues_sources_logs_code_ALLmetadata=True,FULL_final_ALL11_model_readback_and_SEPARATE_verify_follow_freeze=True,no_corresponding_NEW_A_R7_finding_file_hash_metadata_access=True,BOTH_explicit_before_release=True,mathematical_computation=False,payloads=[fp(PRE+s)for s in STATIC+GENERATED]));print(json.dumps(dict(manifest=fp(PRE+'manifest-v1.json'),ENTIRE_files=11,ALL64=True)))
def verify():
    preserved();v=obj(PRE+'manifest-v1.json')
    assert[x['path']for x in v['payloads']]==[PRE+s for s in STATIC+GENERATED]
    for x in v['payloads']:check(x)
    print(json.dumps(dict(SEPARATE_postfreeze_verify='PASS',at_utc=now(),manifest=fp(PRE+'manifest-v1.json'),report=fp(PRE+'report-v1.md'),ENTIRE_files=11,whole_obligations=64,protected21=True,administrative_not_proof=True)))
if __name__=='__main__':dict(prepare=prepare,freeze=freeze,verify=verify)[sys.argv[1]]()
