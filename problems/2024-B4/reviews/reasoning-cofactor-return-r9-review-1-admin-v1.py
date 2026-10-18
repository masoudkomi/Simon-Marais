#!/usr/bin/env python3
"""NEW R9 root WHOLE1 documentary bytes/JSON/labels; no mathematics."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys
ROOT=Path(__file__).resolve().parents[3]
P='problems/2024-B4/reviews/reasoning-cofactor-return-r9-review-1-'
A='problems/2024-B4/notes/reasoning-cofactor-return-r9-'
PARENT='problems/2020-B4/reviews/reasoning-class-return-sq15-review-1-reaudit-manifest-v1.1.json'
STATIC=['initial-v1.md','ledger-v1.md','issues-v1.md','sources-v1.md','sources-v1.json','worklog-v1.md','admin-v1.py']
PAYLOADS=STATIC+['baseline-v1.json','input-validation-v1.json','metadata-v1.json']
def now():return datetime.now(timezone.utc).isoformat()
def path(s):
    assert 'reasoning-cofactor-return-r9-review-2-' not in s
    p=Path(s);assert not p.is_absolute() and '..' not in p.parts
    q=ROOT/p;assert q.resolve().is_relative_to(ROOT);return q
def fp(s):
    b=path(s).read_bytes();return dict(path=s,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def read(s):return json.loads(path(s).read_text())
def check(q):
    row={k:q[k] for k in ['path','bytes','sha256']};assert fp(row['path'])==row,row['path'];return row
def summary(rows):
    d={}
    for q in rows:assert d.setdefault(q['path'],q)==q
    b=json.dumps([d[k] for k in sorted(d)],sort_keys=True,separators=(',',':')).encode()
    return dict(occurrences=len(rows),unique_paths=len(d),canonical_sha256=hashlib.sha256(b).hexdigest())
def labels():
    want=[f'O{i:02d}' for i in range(1,65)]
    assert re.findall(r'^(O\d{2})\.',path(A+'obligations-v1.md').read_text(),re.M)==want
    assert re.findall(r'^\|(O\d{2})\|PASS\|',path(P+'ledger-v1.md').read_text(),re.M)==want
def gather():
    check(dict(path=A+'candidate-v1.md',bytes=20443,sha256='740e85acc2103aa6ed72ac46ac3089b12cfb29962fc4e0593ccf9e8223af66bf'))
    check(dict(path=A+'freeze-v1.json',bytes=9271,sha256='baad7591162df50c28cc4d20794616d165d622ae8c6abc0bb9f699e255d2147d'))
    m=read(A+'freeze-v1.json');assert m['ENTIRE_constructor_files_including_manifest']==11 and m['whole_obligations']==64
    rows=[fp(A+'freeze-v1.json')]+[check(q) for q in m['payloads']]
    rows += [check(q) for q in read(A+'baseline-v1.json')['records']]
    for stem in ['structural','reasoning-cofactor-return-r6','reasoning-cofactor-return-r7','reasoning-cofactor-return-r8']:
        ap='problems/2024-B4/reviews/'+stem+'-acceptance';a=read(ap+'.json')
        body=a.get('accepted_copy',a.get('accepted_proof'));rows += [fp(ap+'.md'),fp(ap+'.json'),check(a['candidate']),check(body)]
        if stem!='structural':assert path(body['path']).read_bytes().endswith(path(a['candidate']['path']).read_bytes())
    rows += [fp('AGENTS.md'),fp('problems/2024-B4/statement.md')]
    par=read(PARENT);assert len(par['payloads'])==10
    rows += [fp(PARENT)]+[check(q) for q in par['payloads']]
    labels();return rows
def write(s,v):
    with path(P+s).open('x') as f:json.dump(v,f,indent=2,ensure_ascii=False);f.write('\n')
def prepare():
    rows=gather();pro=summary(rows)
    write('baseline-v1.json',dict(at_utc=now(),records=rows,protection=pro,historical_parent_identity_not_fresh_mathematical_reread=True))
    write('input-validation-v1.json',dict(at_utc=now(),result='PASS',author_ENTIRE=11,ALL_obligations=64,protection=pro,mathematical_execution=False))
    write('metadata-v1.json',dict(status='OTHER initially blind WHOLE1; not promotion',reviewer='/root',constructor='/root/review_2022_complexity_r2',constructor_excluded=True,ALL_obligations=64,hand_PASS_rows=64,substantive_defects=0,required_repairs=0,closed_scope_notes=8,new_peer_contents_inventory_files_access=False,administrative_completion_identity_only_received=True,findings_embargo_until_explicit_BOTH=True,requested_inherited=dict(model='gpt-6.1-sol',reasoning='max'),independent_effective_readback=None,no_mathematical_program_or_old_replay=True,weekly_TOTAL_percent=53,authorized_reset=1792874445,TOTAL_ceiling=90,automatic_later_window=False))
    print(json.dumps(dict(prepare='PASS',**pro)))
def validate():
    b=read(P+'baseline-v1.json')
    for q in b['records']:check(q)
    assert summary(gather())==b['protection'];return b['protection']
def freeze():
    pro=validate();write('manifest-v1.json',dict(frozen_at_utc=now(),status='ENTIRE initially blind OTHER WHOLE1; findings EMBARGOED',reviewer='/root',ALL_obligations=64,ENTIRE_files=11,FULL_final_ALL10_payload_model_readback_complete=True,FULL_manifest_readback_then_SEPARATE_verify_required=True,explicit_BOTH_required_before_NEW_peer_access_or_release=True,new_peer_contents_inventory_files_access=False,administrative_completion_identity_only_received=True,protection=pro,payloads=[fp(P+s) for s in PAYLOADS]))
    print(json.dumps(dict(freeze='PASS',manifest=fp(P+'manifest-v1.json'))))
def verify():
    pro=validate();m=read(P+'manifest-v1.json');assert m['ENTIRE_files']==11 and m['ALL_obligations']==64
    assert [q['path'] for q in m['payloads']]==[P+s for s in PAYLOADS]
    for q in m['payloads']:check(q)
    assert m['protection']==pro
    print(json.dumps(dict(SEPARATE_readonly_verify='PASS',at_utc=now(),ENTIRE_files=11,ALL_obligations=64,manifest=fp(P+'manifest-v1.json'),protection=pro,no_file_written=True)))
if __name__=='__main__':
    assert len(sys.argv)==2 and sys.argv[1] in ('prepare','freeze','verify')
    dict(prepare=prepare,freeze=freeze,verify=verify)[sys.argv[1]]()
