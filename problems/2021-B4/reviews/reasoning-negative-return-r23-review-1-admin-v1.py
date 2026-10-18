"""NEW root R23 documentary metadata only; no mathematics or old replay."""
from pathlib import Path
import datetime,hashlib,json,re,sys
ROOT=Path(__file__).resolve().parents[3]
P='problems/2021-B4/reviews/reasoning-negative-return-r23-review-1-'
A='problems/2021-B4/notes/reasoning-negative-return-r23-'
PARENT='problems/2017-B4/reviews/reasoning-lower-return-r14-review-1-manifest-v1.json'
PAYLOAD=[P+'initial-v1.md',P+'sources-v1.json',P+'admin-v1.py',P+'baseline-v1.json']
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def read(p):return json.loads((ROOT/p).read_text())
def rec(p):
    assert not p.startswith('/') and '..' not in Path(p).parts
    assert 'reasoning-negative-return-r23-review-2-' not in p
    assert 'reasoning-critical-return-r11-review-2-' not in p
    b=(ROOT/p).read_bytes();return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def rows(x):
    if isinstance(x,dict):
        if isinstance(x.get('path'),str) and isinstance(x.get('bytes'),int) and isinstance(x.get('sha256'),str):yield {k:x[k] for k in ('path','bytes','sha256')}
        for v in x.values():yield from rows(v)
    elif isinstance(x,list):
        for v in x:yield from rows(v)
def summary(xs):
    d={}
    for x in xs:
        assert rec(x['path'])==x,x['path']
        assert x['path'] not in d or d[x['path']]==x
        d[x['path']]=x
    raw=json.dumps([d[k] for k in sorted(d)],sort_keys=True,separators=(',',':')).encode()
    return dict(occurrences=len(xs),unique_paths=len(d),canonical_deduplicated_sha256=hashlib.sha256(raw).hexdigest())
def guards():
    af=read(A+'freeze-v1.json'); own=read(PARENT)
    direct=[rec('AGENTS.md'),rec('problems/2021-B4/statement.md'),rec(A+'freeze-v1.json')]
    direct += af['payloads']+[rec(PARENT)]+own['payload_records']
    declared=list(af['payloads'])+read(A+'baseline-v1.json')['direct_records']
    for n in (18,21,22):
        q=f'problems/2021-B4/reviews/reasoning-center-return-r{n}-acceptance'
        direct += [rec(f'problems/2021-B4/proofs/reviewed-reasoning-center-return-r{n}-v1.1.md'),rec(q+'.md'),rec(q+'.json')]
        declared += list(rows(read(q+'.json')))
    return direct,declared
def labels():
    a=re.findall(r'^\|R23-O(\d\d)\|',(ROOT/(A+'obligations-v1.md')).read_text(),re.M)
    b=re.findall(r'^\|R23-O(\d\d)\|',(ROOT/(P+'initial-v1.md')).read_text(),re.M)
    expected=[f'{n:02}' for n in range(1,49)]
    assert a==b==expected
    return len(a)
def create(p,x):
    assert p.startswith(P)
    with (ROOT/p).open('x') as f:json.dump(x,f,indent=2);f.write('\n')
mode=sys.argv[1]
if mode=='prepare':
    direct,declared=guards()
    create(P+'baseline-v1.json',dict(prepared_utc=now(),direct_records=direct,direct_summary=summary(direct),author_declared_summary=summary(declared),whole_obligations=labels(),own_immediate_parent=rec(PARENT),historical_mutable_maps_not_current_immutable_guards=True,hashing_not_a_claim_of_fresh_whole_mathematical_read=True,corresponding_NEW_peer_access=False))
    print(json.dumps(dict(prepare='PASS',baseline=rec(P+'baseline-v1.json'))))
elif mode in ('seal','verify'):
    base=read(P+'baseline-v1.json');direct,declared=guards()
    assert summary(direct)==base['direct_summary']
    assert summary(declared)==base['author_declared_summary']
    if mode=='seal':
        create(P+'manifest-v1.json',dict(frozen_utc=now(),reviewer='/root',constructor='/root/review_2021_reasoning_j15_r2',constructor_excluded=True,ENTIRE_files=5,whole_obligations=labels(),initially_blind=True,payload_records=[rec(p) for p in PAYLOAD],direct_guard_summary=base['direct_summary'],author_declared_guard_summary=base['author_declared_summary'],FULL_final_MODEL_ALL4_payload_readback_completed=True,FULL_manifest_MODEL_readback_then_SEPARATE_readonly_verify_required=True,corresponding_NEW_peer_findings_files_actual_inventory_hash_metadata_access=False,findings_sealed_until_explicit_BOTH=True))
        print(json.dumps(dict(seal='PASS',manifest=rec(P+'manifest-v1.json'))))
    else:
        manifest=read(P+'manifest-v1.json');summary(manifest['payload_records']);labels()
        print(json.dumps(dict(SEPARATE_readonly_verify='PASS',at_utc=now(),manifest=rec(P+'manifest-v1.json'),ENTIRE_files=5,whole_obligations=48,direct=summary(direct),author_declared=summary(declared),writes=False,mathematical_program=False)))
else:raise SystemExit('prepare|seal|verify')
