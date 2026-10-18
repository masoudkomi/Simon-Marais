"""NEW exclusive review byte/JSON/label administration, no mathematics."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,sys
ROOT=Path(__file__).resolve().parents[3]
P='problems/2021-B4/reviews/reasoning-center-return-r20-review-1-'
A='problems/2021-B4/notes/reasoning-center-return-r20-'
PARENT='problems/2024-B4/reviews/reasoning-cofactor-return-r8-review-1-manifest-v1.json'
STATIC=['report-v1.md','ledger-v1.md','issues-v1.md','sources-v1.md','sources-v1.json','worklog-v1.md','admin-v1.py']
GENERATED=['baseline-v1.json','input-validation-v1.json','metadata-v1.json']
def now():return datetime.now(timezone.utc).isoformat()
def path(p):
    assert not Path(p).is_absolute() and '..' not in Path(p).parts
    assert not p.startswith('problems/2021-B4/reviews/reasoning-center-return-r20-review-2-')
    return ROOT/p
def fp(p):
    b=path(p).read_bytes();return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def obj(p):return json.loads(path(p).read_text())
def check(r):assert fp(r['path'])=={k:r[k] for k in ['path','bytes','sha256']},r['path']
def put(s,v):
    with path(P+s).open('x') as f:json.dump(v,f,indent=2);f.write('\n')
def snap():
    check(dict(path=A+'candidate-v1.md',bytes=15053,sha256='7363e0002bddfb05864af81d1bad2c469e4adeff3b7b7703bbf9b203e4ecc371'))
    check(dict(path=A+'freeze-v1.json',bytes=3306,sha256='8b69fb88b967acd31605e9189cbd02b5566ba4f656fe5e0811b616efbff5cbb4'))
    author=obj(A+'freeze-v1.json');assert author['ENTIRE_files']==13 and author['whole_obligations']==48
    records=[fp(A+'freeze-v1.json')]
    for row in author['payloads']:check(row);records.append(fp(row['path']))
    records.extend(fp(p) for p in ['AGENTS.md','problems/2021-B4/statement.md',PARENT,
        'problems/2021-B4/proofs/reviewed-reasoning-center-return-r18-v1.1.md',
        'problems/2021-B4/reviews/reasoning-center-return-r18-acceptance.md',
        'problems/2021-B4/reviews/reasoning-center-return-r18-acceptance.json',
        'problems/2021-B4/notes/reasoning-center-return-r18-failures-v1.md'])
    authority=obj('problems/2021-B4/reviews/reasoning-center-return-r18-acceptance.json');check(authority['accepted_copy']);check(authority['candidate'])
    assert path(authority['accepted_copy']['path']).read_bytes().endswith(path(authority['candidate']['path']).read_bytes())
    for p in [A+'obligations-v1.md',P+'ledger-v1.md']:
        labels=re.findall(r'(?m)^\|\s*R20-(\d{2})\s*\|',path(p).read_text());assert labels==[f'{i:02d}' for i in range(1,49)]
    unique={r['path']:r for r in records};ordered=[unique[p] for p in sorted(unique)]
    return dict(fingerprints=ordered,record_occurrences=len(records),unique_paths=len(ordered),all13_author_bound=True,all48_labels=True,accepted_R18_suffix_verified=True,own_immediate_parent_only_no_recursive_expansion=fp(PARENT),administration_only=True)
def prepare():
    s=snap()
    for suffix in STATIC:fp(P+suffix)
    put('baseline-v1.json',dict(at_utc=now(),**s))
    put('input-validation-v1.json',dict(at_utc=now(),result='PASS',whole_obligations=48,record_occurrences=s['record_occurrences'],unique_paths=s['unique_paths'],administration_only=True))
    put('metadata-v1.json',dict(at_utc=now(),reviewer='/root',A_constructor_excluded=True,whole_obligations=48,ENTIRE_files=11,no_NEW_corresponding_peer_R20_finding_file_hash_metadata_access=True,FULL_final_ALL11_readback_then_SEPARATE_verify_required=True,requested_inherited=dict(model='gpt-6.1-sol',reasoning='max'),independent_effective_readback=None,authorized_reset_only=1792874445,TOTAL_ceiling=90,integration_reserve=True,no_mathcode_or_old_replay=True))
    print(json.dumps(dict(prepare='PASS',record_occurrences=s['record_occurrences'],unique_paths=s['unique_paths'])))
def validate():
    s=snap();b=obj(P+'baseline-v1.json');assert all(b[k]==v for k,v in s.items());return s
def freeze():
    s=validate();put('manifest-v1.json',dict(frozen_at_utc=now(),status='ENTIRE initially blind OTHER WHOLE1;findings embargoed',whole_obligations=48,ENTIRE_files=11,FULL_final_ALL10_payload_model_readback_complete=True,FULL_manifest_readback_then_SEPARATE_verify_required=True,explicit_BOTH_required_before_NEW_peer_access_or_release=True,no_NEW_corresponding_peer_finding_file_hash_metadata_access=True,record_occurrences=s['record_occurrences'],unique_paths=s['unique_paths'],payloads=[fp(P+p) for p in STATIC+GENERATED]));print(json.dumps(dict(freeze=fp(P+'manifest-v1.json'))))
def verify():
    s=validate();m=obj(P+'manifest-v1.json');assert m['whole_obligations']==48 and len(m['payloads'])==10
    for r in m['payloads']:check(r)
    print(json.dumps(dict(SEPARATE_readonly_verify='PASS',at_utc=now(),ENTIRE_files=11,whole_obligations=48,record_occurrences=s['record_occurrences'],unique_paths=s['unique_paths'],manifest=fp(P+'manifest-v1.json'),report=fp(P+'report-v1.md')),indent=2))
if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)==2 else '';assert mode in ['prepare','freeze','verify'];dict(prepare=prepare,freeze=freeze,verify=verify)[mode]()
