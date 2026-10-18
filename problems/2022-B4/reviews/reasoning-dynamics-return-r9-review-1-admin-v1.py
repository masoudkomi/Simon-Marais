#!/usr/bin/env python3
"""NEW D9 root whole1 documentary bytes/JSON/labels, no mathematics."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,sys
ROOT=Path(__file__).resolve().parents[3]
P='problems/2022-B4/reviews/reasoning-dynamics-return-r9-review-1-'
A='problems/2022-B4/notes/reasoning-dynamics-return-r9-'
PARENT='problems/2019-B4/reviews/reasoning-occupation-return-r1-review-1-manifest-v1.json'
STATIC=['initial-v1.md','ledger-v1.md','issues-v1.md','sources-v1.md','sources-v1.json','worklog-v1.md','admin-v1.py']
PAYLOADS=STATIC+['baseline-v1.json','input-validation-v1.json','metadata-v1.json']
def now():return datetime.now(timezone.utc).isoformat()
def path(s):
    assert 'reasoning-dynamics-return-r9-review-2-' not in s
    p=Path(s);assert not p.is_absolute() and '..' not in p.parts
    q=ROOT/p;assert q.resolve().is_relative_to(ROOT);return q
def fp(s):
    b=path(s).read_bytes();return dict(path=s,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def read(s):return json.loads(path(s).read_text())
def check(q):
    v={k:q[k] for k in ['path','bytes','sha256']};assert fp(v['path'])==v,v['path'];return v
def summary(rows):
    d={}
    for q in rows:assert d.setdefault(q['path'],q)==q
    b=json.dumps([d[k] for k in sorted(d)],sort_keys=True,separators=(',',':')).encode()
    return dict(occurrences=len(rows),unique_paths=len(d),canonical_sha256=hashlib.sha256(b).hexdigest())
def labels():
    want=[f'D9-{i:02d}' for i in range(1,49)]
    assert re.findall(r'^\|(D9-\d{2})\|',path(A+'obligations-v1.md').read_text(),re.M)==want
    assert re.findall(r'^\|(D9-\d{2})\|PASS\|',path(P+'ledger-v1.md').read_text(),re.M)==want
def gather():
    check(dict(path=A+'candidate-v1.md',bytes=16389,sha256='e15f1ad442916acda5c27cff79107dcf0236b1f4f748f7f5e521214bad6b410c'))
    check(dict(path=A+'freeze-v1.json',bytes=3635,sha256='4427de51ab82207eb673d983f9abfedec5553f783bbd1093e29f6ca49659036a'))
    m=read(A+'freeze-v1.json');assert m['ENTIRE_files']==12 and m['whole_obligations']==48
    rows=[fp(A+'freeze-v1.json')]+[check(q) for q in m['payloads']]
    rows += [check(q) for q in read(A+'baseline-v1.json')['guards']]
    for stem in ['reasoning-dynamics-return-r8','reasoning-dynamics-return-r7','reasoning-fiber-return-r5']:
        ap='problems/2022-B4/reviews/'+stem+'-acceptance';a=read(ap+'.json')
        assert a['status']=='proved, independently reviewed scoped partial result'
        check(a['candidate']);check(a['accepted_copy'])
        assert path(a['accepted_copy']['path']).read_bytes().endswith(path(a['candidate']['path']).read_bytes())
    par=read(PARENT);assert len(par['payloads'])==10
    rows += [fp(PARENT)]+[check(q) for q in par['payloads']]
    labels();return rows
def write(s,v):
    with path(P+s).open('x') as f:json.dump(v,f,indent=2,ensure_ascii=False);f.write('\n')
def prepare():
    rows=gather();pro=summary(rows)
    write('baseline-v1.json',dict(at_utc=now(),records=rows,protection=pro,historical_parent_identity_not_fresh_mathematical_reread=True))
    write('input-validation-v1.json',dict(at_utc=now(),result='PASS',author_ENTIRE=12,ALL_obligations=48,protection=pro,mathematical_execution=False))
    write('metadata-v1.json',dict(status='OTHER initially blind WHOLE1; not promotion',reviewer='/root',constructor='/root/review_2017_coarsening_r1',constructor_excluded=True,ALL_obligations=48,hand_PASS_rows=48,substantive_defects=0,required_repairs=0,closed_scope_notes=8,new_peer_finding_file_inventory_hash_metadata_commentary_access=False,findings_embargo_until_explicit_BOTH=True,requested_inherited=dict(model='gpt-6.1-sol',reasoning='max'),independent_effective_readback=None,no_mathematical_program_or_old_replay=True,weekly_TOTAL_percent=54,authorized_reset=1792874445,TOTAL_ceiling=90,automatic_later_window=False))
    print(json.dumps(dict(prepare='PASS',**pro)))
def validate():
    b=read(P+'baseline-v1.json')
    for q in b['records']:check(q)
    assert summary(gather())==b['protection'];return b['protection']
def freeze():
    pro=validate();write('manifest-v1.json',dict(frozen_at_utc=now(),status='ENTIRE initially blind OTHER WHOLE1; findings EMBARGOED',reviewer='/root',ALL_obligations=48,ENTIRE_files=11,FULL_final_ALL10_payload_model_readback_complete=True,FULL_manifest_model_readback_then_SEPARATE_verify_required=True,explicit_BOTH_required_before_NEW_peer_access_or_release=True,new_peer_finding_file_inventory_hash_metadata_commentary_access=False,protection=pro,payloads=[fp(P+s) for s in PAYLOADS]))
    print(json.dumps(dict(freeze='PASS',manifest=fp(P+'manifest-v1.json'))))
def verify():
    pro=validate();m=read(P+'manifest-v1.json');assert m['ENTIRE_files']==11 and m['ALL_obligations']==48
    assert [q['path'] for q in m['payloads']]==[P+s for s in PAYLOADS]
    for q in m['payloads']:check(q)
    assert m['protection']==pro
    print(json.dumps(dict(SEPARATE_readonly_verify='PASS',at_utc=now(),ENTIRE_files=11,ALL_obligations=48,manifest=fp(P+'manifest-v1.json'),protection=pro,no_file_written=True)))
if __name__=='__main__':
    assert len(sys.argv)==2 and sys.argv[1] in ('prepare','freeze','verify')
    dict(prepare=prepare,freeze=freeze,verify=verify)[sys.argv[1]]()
