"""NEW DR6 metadata only,not mathematical computation or old program replay."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re,sys
ROOT=Path.cwd();P='problems/2025-B4/reviews/reasoning-diagonal-return-r6-review-1-';A='problems/2025-B4/notes/reasoning-diagonal-return-r6-'
def now():return datetime.now(timezone.utc).isoformat()
def fp(p):
    assert not p.startswith('/') and '..' not in Path(p).parts and 'reasoning-diagonal-return-r6-review-2-'not in p
    b=(ROOT/p).read_bytes();return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def load(p):return json.loads((ROOT/p).read_text())
def exact(r):assert fp(r['path'])=={k:r[k]for k in ['path','bytes','sha256']}
def write(s,v):
    with(ROOT/(P+s)).open('x')as f:json.dump(v,f,indent=2);f.write('\n')
def inputs():
    m=load(A+'freeze-v1.json');assert m['whole_obligations']==48 and len(m['artifacts'])==12
    assert fp(A+'candidate-v1.md')['sha256']=='d8833575a24f27dc586790580e42423dd0ad36232d8164a0b41f76b75e05a643'
    assert fp(A+'freeze-v1.json')['sha256']=='a9edb267e1b417beedcfbe57dec293b9d494fe878f2758ccbdc4f5c300188b8d'
    rows=m['artifacts']+[fp(A+'freeze-v1.json')]
    for r in rows:exact(r)
    b=load(A+'baseline-v1.json')
    for r in b['direct_frozen_input_bindings']:exact(r)
    paths=['AGENTS.md','problems/2025-B4/statement.md']
    for stem in ['reasoning-diagonal-return-r5','reasoning-branch-return-r4','reasoning-Runge-return-r3','reasoning-Runge-return-r2','reasoning-return-r6']:
        j='problems/2025-B4/reviews/'+stem+'-acceptance.json';v=load(j)
        assert v['status'].startswith('proved, independently reviewed') and v['unresolved_substantive_issues']==0
        exact(v['accepted_copy']);exact(v['candidate'])
        assert(ROOT/v['accepted_copy']['path']).read_bytes().endswith((ROOT/v['candidate']['path']).read_bytes())
        paths += [j,j[:-5]+'.md']
    paths += ['problems/2025-B4/proofs/reviewed-reasoning-diagonal-return-r5-v1.1.md','problems/2025-B4/notes/reasoning-diagonal-return-r5-sources-v1.md','problems/2025-B4/notes/reasoning-diagonal-return-r5-failed-routes-v1.md','problems/2025-B4/notes/reasoning-branch-return-r4-failed-routes-v1.md','problems/2025-B4/notes/reasoning-Runge-return-r3-failed-routes-v1.md','problems/2025-B4/notes/reasoning-Runge-return-r2-failed-routes-v1.md','problems/2025-B4/notes/coordinator-higher-trace-frontier-r6-v1.md','problems/2025-B4/notes/coordinator-higher-trace-frontier-r6-v1.json']
    rows += [fp(p)for p in paths];u={r['path']:r for r in rows};assert len(rows)==len(u)==33
    return sorted(u.values(),key=lambda r:r['path'])
def labels():assert re.findall(r'^\|DR6-(\d{2})\|PASS', (ROOT/(P+'ledger-v1.md')).read_text(),re.M)==[f'{i:02d}'for i in range(1,49)]
def prepare():
    labels();r=inputs();write('baseline-v1.json',dict(at_utc=now(),necessary_guard_records=r,necessary_unique_paths=33,author_direct_bindings_also_checked=True,historical_mutable_context_not_current_frozen_premise=True,no_NEW_corresponding_C_peer_access=True))
    write('input-validation-v1.json',dict(at_utc=now(),status='PASS administrativeonly',baseline=fp(P+'baseline-v1.json'),whole_obligations=48,author_ENTIRE_files=13,no_mathematics_run=True))
    write('metadata-v1.json',dict(at_utc=now(),reviewer='/root',constructor='/root/review_2021_reasoning_j15_r2',constructor_excluded=True,whole_obligations=48,ENTIRE_files=11,substantive_defects=0,required_repairs=0,closed_notes=7,old_RS_formalnote_roles_disclosed_unused=True,requested_model='gpt-6.1-sol',requested_reasoning='max',effective_readback=None,authorized_weekly_reset=1792874445,ceiling_TOTAL_percent=90,integration_reserve=True,FULLfinal_ALLfiles_readback_then_SEPARATEverify_required=True,BOTH_explicit_before_peer=True,no_NEW_corresponding_C_peer_access=True,no_mathematics_run=True))
    print(json.dumps(dict(prepared=True,necessary_unique_paths=33,whole_obligations=48)))
def guard():labels();assert inputs()==load(P+'baseline-v1.json')['necessary_guard_records']
def freeze():
    guard();paths=sorted(str(p.relative_to(ROOT))for p in (ROOT/'problems/2025-B4/reviews').glob('reasoning-diagonal-return-r6-review-1-*'));assert len(paths)==10
    write('manifest-v1.json',dict(frozen_at_utc=now(),status='ENTIRE initially blind OTHER WHOLE1;findings embargoed',whole_obligations=48,ENTIRE_files=11,substantive_defects=0,required_repairs=0,closed_notes=7,no_NEW_corresponding_C_peer_access=True,FULLfinal_ALL11_model_readback_then_SEPARATEverify_required=True,BOTH_explicit_before_peer=True,payloads=[fp(p)for p in paths]))
    print(json.dumps(dict(manifest=fp(P+'manifest-v1.json'),report=fp(P+'report-v1.md'),ENTIRE_files=11,whole_obligations=48)))
def verify():
    guard();m=load(P+'manifest-v1.json');assert len(m['payloads'])==10
    for r in m['payloads']:exact(r)
    print(json.dumps(dict(verified_at_utc=now(),status='PASS SEPARATE read-only integrity',ENTIRE_files=11,whole_obligations=48,manifest=fp(P+'manifest-v1.json'),no_NEW_corresponding_C_peer_access=True,no_mathematics_run=True)))
if __name__=='__main__':{'prepare':prepare,'freeze':freeze,'verify':verify}[sys.argv[1]]()
