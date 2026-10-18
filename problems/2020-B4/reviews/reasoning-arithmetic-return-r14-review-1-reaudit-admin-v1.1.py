#!/usr/bin/env python3
"""NEW SQ14 affected WHOLE1 documentary bytes/JSON/labels, no mathematics."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,sys
ROOT=Path(__file__).resolve().parents[3]
P='problems/2020-B4/reviews/reasoning-arithmetic-return-r14-review-1-reaudit-'
A='problems/2020-B4/notes/reasoning-arithmetic-return-r14-'
PARENT='problems/2024-B4/reviews/reasoning-cofactor-return-r9-review-1-manifest-v1.json'
STATIC=['initial-v1.1.md','ledger-v1.1.md','issues-v1.1.md','sources-v1.1.md','sources-v1.1.json','worklog-v1.1.md','admin-v1.1.py']
PAYLOADS=STATIC+['baseline-v1.1.json','input-validation-v1.1.json','metadata-v1.1.json']
def now():return datetime.now(timezone.utc).isoformat()
def path(s):
    assert 'reasoning-arithmetic-return-r14-review-2-reaudit' not in s
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
    want=[f'SQ14-{i:02d}' for i in range(1,65)]+[f'SQ14-R{i:02d}' for i in range(1,13)]
    assert re.findall(r'^\| (SQ14-(?:R)?\d{2}) \|',path(A+'obligations-v1.1.md').read_text(),re.M)==want
    assert re.findall(r'^\|(SQ14-(?:R)?\d{2})\|PASS\|',path(P+'ledger-v1.1.md').read_text(),re.M)==want
def gather():
    check(dict(path=A+'candidate-v1.1.md',bytes=23705,sha256='55afd51e3f83be9f7f1291a9817499bf863d5dbff6900211a93446f169f8f8f7'))
    check(dict(path=A+'freeze-v1.1.json',bytes=7882,sha256='6468e2ee52ca8d0ef18e27d65ce57cda932e3072eb8f95e2c3565233026395c9'))
    m=read(A+'freeze-v1.1.json');assert m['ENTIRE_files_including_manifest']==14 and m['all_original64_plus_repair12']==76
    rows=[fp(A+'freeze-v1.1.json')]+[check(q) for q in m['payloads']]
    rows += [check(q) for q in read(A+'baseline-v1.1.json')['records']]
    for stem in ['reasoning-Todd-return-r12','reasoning-arithmetic-return-r9']:
        ap='problems/2020-B4/reviews/'+stem+'-acceptance';a=read(ap+'.json')
        rows += [fp(ap+'.md'),fp(ap+'.json'),check(a['candidate']),check(a['accepted_copy'])]
        assert path(a['accepted_copy']['path']).read_bytes().endswith(path(a['candidate']['path']).read_bytes())
    rows += [fp('AGENTS.md'),fp('problems/2020-B4/statement.md')]
    par=read(PARENT);assert len(par['payloads'])==10
    rows += [fp(PARENT)]+[check(q) for q in par['payloads']]
    labels();return rows
def write(s,v):
    with path(P+s).open('x') as f:json.dump(v,f,indent=2,ensure_ascii=False);f.write('\n')
def prepare():
    rows=gather();pro=summary(rows)
    write('baseline-v1.1.json',dict(at_utc=now(),records=rows,protection=pro,historical_parent_identity_not_fresh_mathematical_reread=True))
    write('input-validation-v1.1.json',dict(at_utc=now(),result='PASS',author_ENTIRE=14,original64_plus_repair12=76,protection=pro,mathematical_execution=False))
    write('metadata-v1.1.json',dict(status='OTHER initially blind affected WHOLE1; not promotion',reviewer='/root',constructor='/root/review_2022_complexity_r2',constructor_excluded=True,ALL_obligations=76,hand_PASS_rows=76,additional_substantive_defects=0,required_additional_repairs=0,original_fractional_defect_substantive=True,root_old_initial_miss_preserved=True,closed_scope_notes=8,new_peer_files_inventory_hash_metadata_dispositions_access=False,administrative_completion_identity_only_received=True,findings_embargo_until_explicit_BOTH=True,requested_inherited=dict(model='gpt-6.1-sol',reasoning='max'),independent_effective_readback=None,no_mathematical_program_or_old_replay=True,weekly_TOTAL_percent=54,authorized_reset=1792874445,TOTAL_ceiling=90,automatic_later_window=False))
    print(json.dumps(dict(prepare='PASS',**pro)))
def validate():
    b=read(P+'baseline-v1.1.json')
    for q in b['records']:check(q)
    assert summary(gather())==b['protection'];return b['protection']
def freeze():
    pro=validate();write('manifest-v1.1.json',dict(frozen_at_utc=now(),status='ENTIRE initially blind OTHER affected WHOLE1; findings EMBARGOED',reviewer='/root',ALL_obligations=76,ENTIRE_files=11,FULL_final_ALL10_payload_model_readback_complete=True,FULL_manifest_model_readback_then_SEPARATE_verify_required=True,explicit_BOTH_required_before_NEW_peer_access_or_release=True,new_peer_files_inventory_hash_metadata_dispositions_access=False,administrative_completion_identity_only_received=True,protection=pro,payloads=[fp(P+s) for s in PAYLOADS]))
    print(json.dumps(dict(freeze='PASS',manifest=fp(P+'manifest-v1.1.json'))))
def verify():
    pro=validate();m=read(P+'manifest-v1.1.json');assert m['ENTIRE_files']==11 and m['ALL_obligations']==76
    assert [q['path'] for q in m['payloads']]==[P+s for s in PAYLOADS]
    for q in m['payloads']:check(q)
    assert m['protection']==pro
    print(json.dumps(dict(SEPARATE_readonly_verify='PASS',at_utc=now(),ENTIRE_files=11,ALL_obligations=76,manifest=fp(P+'manifest-v1.1.json'),protection=pro,no_file_written=True)))
if __name__=='__main__':
    assert len(sys.argv)==2 and sys.argv[1] in ('prepare','freeze','verify')
    dict(prepare=prepare,freeze=freeze,verify=verify)[sys.argv[1]]()
