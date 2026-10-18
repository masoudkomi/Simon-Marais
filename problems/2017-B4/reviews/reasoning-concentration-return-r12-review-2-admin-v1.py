"""NEW documentary byte/JSON/label checks; no mathematics or old executable replay."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, sys
R=Path.cwd()
P='problems/2017-B4/reviews/reasoning-concentration-return-r12-review-2-'
A='problems/2017-B4/notes/reasoning-concentration-return-r12-'
PEER='problems/2017-B4/reviews/reasoning-concentration-return-r12-review-1-'
def now():return datetime.now(timezone.utc).isoformat()
def safe(p):
    assert not p.startswith(PEER) and not Path(p).is_absolute() and '..' not in Path(p).parts
def obj(p):
    safe(p)
    return json.loads((R/p).read_text())
def rec(p):
    safe(p)
    b=(R/p).read_bytes()
    return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def declared(x):
    out=[]
    if isinstance(x,dict):
        if isinstance(x.get('path'),str) and isinstance(x.get('bytes'),int) and isinstance(x.get('sha256'),str):
            out.append({k:x[k] for k in ('path','bytes','sha256')})
        for v in x.values():out+=declared(v)
    elif isinstance(x,list):
        for v in x:out+=declared(v)
    return out
def check(rows):
    for r in rows:assert rec(r['path'])=={k:r[k] for k in ('path','bytes','sha256')},r['path']
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def summary(rows):
    unique={}
    for r in rows:
        c={k:r[k] for k in ('path','bytes','sha256')}
        assert unique.setdefault(r['path'],c)==c
    ordered=[unique[p] for p in sorted(unique)]
    return dict(occurrences=len(rows),unique_paths=len(ordered),canonical_deduplicated_sha256=digest(ordered))
def guards():
    b=obj(A+'baseline-v1.json')
    direct=b['direct_inputs'];check(direct);rows=list(direct)
    for binding in b['immutable_parent_metadata']:
        check([binding]);own=declared(obj(binding['path']));check(own)
        assert len(own)==binding['declared_occurrences_verified'] and digest(own)==binding['declared_canonical_sha256']
        rows+=own
    s=summary(rows)
    assert (s['occurrences'],s['unique_paths'],s['canonical_deduplicated_sha256'])==(b['guard_occurrences_verified'],b['unique_guard_paths'],b['deduplicated_canonical_sha256'])
    return rows
def ledger():
    text=(R/(P+'report-v1.md')).read_text()
    labels=[l.split('|')[1].strip() for l in text.splitlines() if l.startswith('| ') and l[2:4].isdigit()]
    assert labels==[str(i).zfill(2) for i in range(1,49)]
    return len(labels)
def put(s,x):
    with (R/(P+s)).open('x') as f:f.write(json.dumps(x,indent=2)+'\n')
def prepare():
    f=obj(A+'freeze-v1.json')
    assert rec(A+'freeze-v1.json')['sha256']=='6a6e5ccccbc9c5416aeeac4240a8a4f96bc44b90167d5275e8ab2bf563c17c1c'
    assert f['ENTIRE_files']==13 and len(f['payload_records'])==12 and ledger()==48
    direct=f['payload_records']+[rec(A+'freeze-v1.json'),rec('AGENTS.md')]
    check(direct);old=guards()
    put('baseline-v1.json',dict(created_at_utc=now(),direct=direct,compact_author_guard=rec(A+'baseline-v1.json'),
        author_guard_summary=summary(old),effective_summary=summary(direct+old),
        administrative_only=True,read_scopes='Literal full/excerpted scopes in report; old hashes are preservation only.',
        NEW_peer_actual_inventory_open_hash_findings_access=False,administrative_peer_identity_only_received=True))
    print(json.dumps(dict(action='prepare',PASS=True,ENTIRE_author=13,whole_obligations=48,summary=summary(direct+old))))
def validate():
    b=obj(P+'baseline-v1.json');check(b['direct']+[b['compact_author_guard']]);old=guards()
    assert summary(old)==b['author_guard_summary'] and summary(b['direct']+old)==b['effective_summary'] and ledger()==48
    return b
def freeze():
    b=validate();payloads=[rec(P+s) for s in ('report-v1.md','admin-v1.py','baseline-v1.json')]
    put('manifest-v1.json',dict(frozen_at_utc=now(),status='initial OTHER WHOLE2; EMBARGO until explicit BOTH ENTIRE',
        reviewer='/root',constructor='/root/review_2017_coarsening_r1',constructor_excluded=True,
        ENTIRE_files=4,whole_obligations=48,independent_dispositions=48,payloads=payloads,
        unresolved_substantive_defects=0,required_repair=False,closed_scope_notes=8,
        FULL_final_ALL3_payload_model_readback='actually completed before this freeze',
        FULL_manifest_model_readback_then_SEPARATE_verify_required=True,effective_summary=b['effective_summary'],
        NEW_peer_actual_inventory_open_hash_findings_access=False,administrative_peer_identity_only_received=True,
        requested=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),effective_setting_readback=None))
    print(json.dumps(dict(action='freeze',manifest=rec(P+'manifest-v1.json'),ENTIRE=4,whole_obligations=48)))
def verify():
    b=validate();m=obj(P+'manifest-v1.json');check(m['payloads'])
    assert m['effective_summary']==b['effective_summary']
    print(json.dumps(dict(action='SEPARATE read-only verify',verified_at_utc=now(),PASS=True,ENTIRE=4,
        whole_obligations=48,manifest=rec(P+'manifest-v1.json'),summary=b['effective_summary'])))
if __name__=='__main__':
    assert len(sys.argv)==2 and sys.argv[1] in ('prepare','freeze','verify')
    {'prepare':prepare,'freeze':freeze,'verify':verify}[sys.argv[1]]()
