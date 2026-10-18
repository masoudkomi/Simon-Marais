#!/usr/bin/env python3
"""NEW D8 WHOLE1 documentary integrity and literal labels only."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
P = 'problems/2022-B4/reviews/reasoning-dynamics-return-r8-review-1-'
A = 'problems/2022-B4/notes/reasoning-dynamics-return-r8-'
PARENT = 'problems/2017-B4/reviews/reasoning-path-mass-return-r10-review-1-manifest-v1.json'
EXPECTED = [
    (A+'candidate-v1.md', 18637, 'ea5c5b96714e0e12f10d6ce88bd4e8b7e89fcaf0baa64528e9fe5136e8f0c435'),
    (A+'freeze-v1.json', 3911, 'add639e38da1227a8382f8e5994dfeee78c414f53665b05d072b39251c7d77dd'),
    (PARENT, 2672, '593c0556fc30c65b393c97caa780d36277569e769a5dda6384f4782aff96c1dc'),
]
AUTH = ['reasoning-dynamics-return-r7', 'reasoning-fiber-return-r5',
        'reasoning-complexity-return-r9-v3', 'reasoning-dynamics-return-r6']
STATIC = ['initial-v1.md','ledger-v1.md','issues-v1.md','sources-v1.md',
          'sources-v1.json','worklog-v1.md','admin-v1.py']
PAYLOADS = STATIC + ['baseline-v1.json','input-validation-v1.json','metadata-v1.json']

def now():
    return datetime.now(timezone.utc).isoformat()

def path(rel):
    assert 'reasoning-dynamics-return-r8-review-2-' not in rel
    p = Path(rel)
    assert not p.is_absolute() and '..' not in p.parts
    full = ROOT/p
    assert full.resolve().is_relative_to(ROOT)
    return full

def fp(rel):
    data = path(rel).read_bytes()
    return dict(path=rel, bytes=len(data), sha256=hashlib.sha256(data).hexdigest())

def read(rel):
    return json.loads(path(rel).read_text())

def check(row):
    expected = {k:row[k] for k in ('path','bytes','sha256')}
    assert fp(row['path']) == expected, row['path']
    return expected

def summary(rows):
    unique = {}
    for row in rows:
        assert unique.setdefault(row['path'],row) == row
    ordered = [unique[k] for k in sorted(unique)]
    data = json.dumps(ordered,sort_keys=True,separators=(',',':')).encode()
    return dict(occurrences=len(rows),unique_paths=len(ordered),canonical_sha256=hashlib.sha256(data).hexdigest())

def labels():
    expected = [f'D8-{i:02d}' for i in range(1,49)]
    for rel in (A+'obligations-v1.md',P+'ledger-v1.md'):
        assert re.findall(r'^\| (D8-\d\d) \|',path(rel).read_text(),re.M) == expected

def gather():
    for rel,n,h in EXPECTED:
        check(dict(path=rel,bytes=n,sha256=h))
    author = read(A+'freeze-v1.json')
    assert author['ENTIRE_files'] == 14 and author['whole_obligations'] == 48
    rows = [fp(A+'freeze-v1.json')] + [check(r) for r in author['payloads']]
    rows += [fp('AGENTS.md'),fp('problems/2022-B4/statement.md')]
    for name in AUTH:
        ap = 'problems/2022-B4/reviews/'+name+'-acceptance'
        authority = read(ap+'.json')
        assert authority['unresolved_substantive_issues'] == 0
        rows += [fp(ap+'.md'),fp(ap+'.json'),check(authority['candidate']),check(authority['accepted_copy'])]
        assert path(authority['accepted_copy']['path']).read_bytes().endswith(path(authority['candidate']['path']).read_bytes())
    rows += [fp('problems/2022-B4/notes/reasoning-dynamics-return-r7-'+s+'-v1.md') for s in ('sources','failed-routes')]
    parent = read(PARENT)
    assert len(parent['payloads']) == 10
    rows += [fp(PARENT)] + [check(r) for r in parent['payloads']]
    labels()
    return rows

def write(suffix,value):
    with path(P+suffix).open('x') as out:
        json.dump(value,out,indent=2,ensure_ascii=False)
        out.write('\n')

def prepare():
    rows = gather()
    write('baseline-v1.json',dict(prepared_at_utc=now(),kind='necessary immutable records and immediate own parent only',records=rows,protection=summary(rows),historical_parent_not_mathematical_reread_claim=True))
    write('input-validation-v1.json',dict(at_utc=now(),result='PASS',ALL_obligations=48,author_ENTIRE_files=14,accepted_exact_suffixes=True,protection=summary(rows),mathematical_execution=False))
    write('metadata-v1.json',dict(status='initially blind OTHER ENTIRE WHOLE1; not promotion',reviewer='/root',constructor='/root/review_2017_coarsening_r1',constructor_excluded=True,NEW_constructive_contribution=False,ALL_obligations=48,hand_PASS_rows=48,substantive_defects=0,required_repairs=0,closed_notes=8,corresponding_NEW_peer_material_access=False,findings_embargo_until_explicit_BOTH=True,requested_inherited=dict(model='gpt-6.1-sol',reasoning='max'),independent_effective_readback=None,mathematical_program_or_old_replay=False,weekly_TOTAL_percent=50,authorized_reset=1792874445,TOTAL_ceiling=90,automatic_later_window_authorized=False))
    print(json.dumps(dict(prepare='PASS',ALL48=True,**summary(rows))))

def validate():
    old = read(P+'baseline-v1.json')
    for row in old['records']:
        check(row)
    assert summary(gather()) == old['protection']
    return old['protection']

def freeze():
    protected = validate()
    write('manifest-v1.json',dict(frozen_at_utc=now(),status='ENTIRE initially blind OTHER WHOLE1; findings EMBARGOED',reviewer='/root',ALL_obligations=48,ENTIRE_files=11,FULL_final_ALL10_payload_model_readback_completed=True,FULL_manifest_readback_then_SEPARATE_verify_required=True,corresponding_NEW_peer_material_access=False,findings_embargo_until_explicit_BOTH=True,protection=protected,payloads=[fp(P+s) for s in PAYLOADS]))
    print(json.dumps(dict(freeze='PASS',manifest=fp(P+'manifest-v1.json'))))

def verify():
    protected = validate()
    manifest = read(P+'manifest-v1.json')
    assert manifest['ENTIRE_files']==11 and manifest['ALL_obligations']==48
    assert [r['path'] for r in manifest['payloads']] == [P+s for s in PAYLOADS]
    for row in manifest['payloads']:
        check(row)
    assert manifest['protection'] == protected
    print(json.dumps(dict(SEPARATE_readonly_verify='PASS',at_utc=now(),manifest=fp(P+'manifest-v1.json'),initial=fp(P+'initial-v1.md'),ENTIRE_files=11,ALL_obligations=48,protection=protected,no_file_written=True)))

if __name__=='__main__':
    assert len(sys.argv)==2 and sys.argv[1] in ('prepare','freeze','verify')
    dict(prepare=prepare,freeze=freeze,verify=verify)[sys.argv[1]]()
