#!/usr/bin/env python3
"""NEW affected WHOLE1 documentary bytes/labels; no mathematical program."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys
ROOT=Path(__file__).resolve().parents[3]
P='problems/2020-B4/reviews/reasoning-class-return-sq15-review-1-reaudit-'
A='problems/2020-B4/notes/reasoning-class-return-sq15-'
PARENT='problems/2022-B4/reviews/reasoning-dynamics-return-r8-review-1-manifest-v1.json'
STATIC=['initial-v1.1.md','ledger-v1.1.md','issues-v1.1.md','sources-v1.1.md','sources-v1.1.json','worklog-v1.1.md','admin-v1.1.py']
PAYLOADS=STATIC+['baseline-v1.1.json','input-validation-v1.1.json','metadata-v1.1.json']
def now():return datetime.now(timezone.utc).isoformat()
def path(s):
    assert 'reasoning-class-return-sq15-review-2-reaudit-' not in s
    assert not Path(s).is_absolute() and '..' not in Path(s).parts
    p=ROOT/s;assert p.resolve().is_relative_to(ROOT);return p
def fp(s):
    b=path(s).read_bytes();return dict(path=s,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def read(s):return json.loads(path(s).read_text())
def check(q):
    row={k:q[k] for k in ('path','bytes','sha256')};assert fp(row['path'])==row,row['path'];return row
def summary(rows):
    d={}
    for q in rows:assert d.setdefault(q['path'],q)==q
    arr=[d[k] for k in sorted(d)];b=json.dumps(arr,sort_keys=True,separators=(',',':')).encode()
    return dict(occurrences=len(rows),unique_paths=len(arr),canonical_sha256=hashlib.sha256(b).hexdigest())
def labels():
    want=[f'SQ15-{i:02d}' for i in range(1,49)]+[f'SQ15-R{i:02d}' for i in range(1,13)]
    for s in [A+'obligations-v1.1.md',P+'ledger-v1.1.md']:
        assert re.findall(r'^\|(SQ15-(?:R)?\d{2})\|',path(s).read_text(),re.M)==want
def gather():
    check(dict(path=A+'candidate-v1.1.md',bytes=25788,sha256='4d2696117fa8f8af5760e5034b83602c780f44f81b839fc4bcb6a3086c4825bd'))
    check(dict(path=A+'freeze-v1.1.json',bytes=4621,sha256='b84c394b1d1e7feb1b351e59bd2f91e4f08aaea232f0537083cf73be8f3a3e9e'))
    m=read(A+'freeze-v1.1.json');assert m['ENTIRE_files']==16 and m['whole_obligations']==60
    rows=[fp(A+'freeze-v1.1.json')]+[check(q) for q in m['payloads']]
    b=read(A+'baseline-v1.1.json');rows += [check(q) for q in b['guards']]
    rows += [fp('AGENTS.md'),fp('problems/2020-B4/statement.md'),fp('problems/2020-B4/reviews/reasoning-arithmetic-return-r14-scope-hold-v1.md')]
    for stem in ['reasoning-arithmetic-return-r14','reasoning-return-r8','reasoning-Todd-return-r12']:
        p='problems/2020-B4/reviews/'+stem+'-acceptance';a=read(p+'.json')
        rows += [fp(p+'.md'),fp(p+'.json'),check(a['candidate']),check(a['accepted_copy'])]
        assert path(a['accepted_copy']['path']).read_bytes().endswith(path(a['candidate']['path']).read_bytes())
    par=read(PARENT);assert len(par['payloads'])==10
    rows += [fp(PARENT)]+[check(q) for q in par['payloads']]
    labels();return rows
def write(s,v):
    with path(P+s).open('x') as f:json.dump(v,f,indent=2,ensure_ascii=False);f.write('\n')
def prepare():
    rows=gather();protection=summary(rows)
    write('baseline-v1.1.json',dict(at_utc=now(),records=rows,protection=protection,historical_inventory_bound_not_fresh_mathematical_reread=True))
    write('input-validation-v1.1.json',dict(at_utc=now(),result='PASS',author_ENTIRE=16,ALL_obligations=60,protection=protection,mathematical_execution=False))
    write('metadata-v1.1.json',dict(status='affected OTHER WHOLE1; not promotion',reviewer='/root',constructor='/root/review_2017_coarsening_r1',constructor_excluded=True,ALL_obligations=60,hand_PASS_rows=60,additional_substantive_defects=0,required_additional_repairs=0,closed_scope_notes=8,original_root_missing_qualifier_miss_preserved=True,new_affected_peer_contents_inventory_files_access=False,administrative_completion_identity_only_received=True,findings_embargo_until_explicit_BOTH=True,requested_inherited=dict(model='gpt-6.1-sol',reasoning='max'),independent_effective_readback=None,no_mathematical_program_or_old_replay=True,weekly_TOTAL_percent=52,authorized_reset=1792874445,TOTAL_ceiling=90,automatic_later_window_authorized=False))
    print(json.dumps(dict(prepare='PASS',**protection)))
def validate():
    b=read(P+'baseline-v1.1.json')
    for q in b['records']:check(q)
    assert summary(gather())==b['protection'];return b['protection']
def freeze():
    pro=validate();write('manifest-v1.1.json',dict(frozen_at_utc=now(),status='ENTIRE affected OTHER WHOLE1; findings EMBARGOED',reviewer='/root',ALL_obligations=60,ENTIRE_files=11,FULL_final_ALL10_payload_model_readback_complete=True,FULL_manifest_readback_then_SEPARATE_verify_required=True,explicit_BOTH_required_before_NEW_peer_access_or_release=True,new_affected_peer_contents_inventory_files_access=False,administrative_completion_identity_only_received=True,protection=pro,payloads=[fp(P+s) for s in PAYLOADS]))
    print(json.dumps(dict(freeze='PASS',manifest=fp(P+'manifest-v1.1.json'))))
def verify():
    pro=validate();m=read(P+'manifest-v1.1.json');assert m['ENTIRE_files']==11 and m['ALL_obligations']==60
    assert [q['path'] for q in m['payloads']]==[P+s for s in PAYLOADS]
    for q in m['payloads']:check(q)
    assert m['protection']==pro
    print(json.dumps(dict(SEPARATE_readonly_verify='PASS',at_utc=now(),ENTIRE_files=11,ALL_obligations=60,manifest=fp(P+'manifest-v1.1.json'),protection=pro,no_file_written=True)))
if __name__=='__main__':
    assert len(sys.argv)==2 and sys.argv[1] in ('prepare','freeze','verify')
    dict(prepare=prepare,freeze=freeze,verify=verify)[sys.argv[1]]()
