"""NEW SQ14 root metadata ONLY. No mathematics or old executable replay."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,sys
ROOT=Path.cwd();P='problems/2020-B4/reviews/reasoning-arithmetic-return-r14-review-1-'
A='problems/2020-B4/notes/reasoning-arithmetic-return-r14-'
def now():return datetime.now(timezone.utc).isoformat()
def fp(p):
    assert not p.startswith('/') and '..' not in Path(p).parts
    assert 'reasoning-arithmetic-return-r14-review-2-' not in p
    b=(ROOT/p).read_bytes();return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def load(p):return json.loads((ROOT/p).read_text())
def exact(r):
    assert fp(r['path'])=={k:r[k]for k in ['path','bytes','sha256']};return r
def write(s,v):
    with(ROOT/(P+s)).open('x')as f:json.dump(v,f,indent=2);f.write('\n')
def inputs():
    m=load(A+'freeze-v1.json');assert len(m['payloads'])==11 and m['whole_obligations']==64
    assert fp(A+'candidate-v1.md')['sha256']=='673bcde7cadb391baf6a8362295bc4ba833e40a69dd4836725b5b3de2015df7f'
    assert fp(A+'freeze-v1.json')['sha256']=='e10b1b5ed9b573e181846b4403d1dbda20515fab3ff39091ce1c8c51124919d5'
    rows=[exact(r)for r in m['payloads']]+[fp(A+'freeze-v1.json')]
    for r in load(A+'baseline-v1.json')['guard_records']:exact(r)
    paths=['AGENTS.md','problems/2020-B4/statement.md']
    for stem in ['reasoning-Todd-return-r12','reasoning-arithmetic-return-r9','reasoning-arithmetic-return-r13']:
        j='problems/2020-B4/reviews/'+stem+'-acceptance.json';v=load(j)
        assert v['status'].startswith('proved, independently reviewed') and v['unresolved_substantive_issues']==0
        exact(v['candidate']);exact(v['accepted_copy'])
        assert(ROOT/v['accepted_copy']['path']).read_bytes().endswith((ROOT/v['candidate']['path']).read_bytes())
        paths += [j,j[:-5]+'.md',v['accepted_copy']['path']]
        paths += ['problems/2020-B4/notes/'+stem+'-sources-v1.md','problems/2020-B4/notes/'+stem+'-failed-routes-v1.md']
    rows += [fp(p)for p in paths]
    unique={r['path']:r for r in rows};assert len(rows)==len(unique)==29
    return sorted(unique.values(),key=lambda r:r['path'])
def labels():
    t=(ROOT/(P+'ledger-v1.md')).read_text();assert re.findall(r'^\|SQ14-(\d{2})\|PASS:',t,re.M)==[f'{i:02d}'for i in range(1,65)]
def prepare():
    labels();rows=inputs();write('baseline-v1.json',dict(at_utc=now(),necessary_guard_records=rows,necessary_unique_paths=len(rows),author_baseline_30_declared_guards_checked_not_recopied=True,mathematical_reading_separately_recorded=True,no_NEW_corresponding_C_peer_access=True))
    write('input-validation-v1.json',dict(at_utc=now(),status='PASS administrative only',baseline=fp(P+'baseline-v1.json'),whole_obligations=64,author_ENTIRE_files=12,no_mathematical_computation=True))
    write('metadata-v1.json',dict(at_utc=now(),reviewer='/root',constructor='/root/review_2022_complexity_r2',constructor_excluded=True,whole_obligations=64,ENTIRE_files_including_manifest=11,substantive_defects=0,required_repairs=0,closed_notes=7,requested_model='gpt-6.1-sol',requested_reasoning='max',effective_readback=None,authorized_weekly_reset=1792874445,ceiling_TOTAL_percent=90,integration_reserve=True,old_roles_disclosed=True,no_NEW_corresponding_C_peer_access=True,FULL_final_ALLfiles_model_readback_and_SEPARATE_verify_required=True,BOTH_explicit_before_release=True,no_mathematical_computation=True))
    print(json.dumps(dict(prepared=True,necessary_unique_paths=len(rows),whole_obligations=64)))
def guard():
    labels();b=load(P+'baseline-v1.json');assert inputs()==b['necessary_guard_records'];return b
def freeze():
    guard();paths=sorted(str(p.relative_to(ROOT))for p in (ROOT/'problems/2020-B4/reviews').glob('reasoning-arithmetic-return-r14-review-1-*'))
    assert len(paths)==10
    write('manifest-v1.json',dict(frozen_at_utc=now(),status='ENTIRE initially blind OTHER WHOLE1;findings embargoed',whole_obligations=64,ENTIRE_files=11,substantive_defects=0,required_repairs=0,closed_notes=7,no_NEW_corresponding_C_peer_access=True,FULL_final_ALL11_model_readback_then_SEPARATE_verify_required=True,BOTH_explicit_before_release=True,payloads=[fp(p)for p in paths]))
    print(json.dumps(dict(manifest=fp(P+'manifest-v1.json'),report=fp(P+'report-v1.md'),ENTIRE_files=11,whole_obligations=64)))
def verify():
    guard();m=load(P+'manifest-v1.json');assert len(m['payloads'])==10
    for r in m['payloads']:exact(r)
    print(json.dumps(dict(verified_at_utc=now(),status='PASS SEPARATE read-only integrity',ENTIRE_files=11,whole_obligations=64,manifest=fp(P+'manifest-v1.json'),no_NEW_corresponding_C_peer_access=True,no_mathematics_run=True)))
if __name__=='__main__':{'prepare':prepare,'freeze':freeze,'verify':verify}[sys.argv[1]]()
