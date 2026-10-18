"""NEW independent documentary checks only; no math or old executable replay."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, sys
R = Path.cwd()
P = 'problems/2019-B4/reviews/reasoning-area-return-r2-review-1-'
A = 'problems/2019-B4/notes/reasoning-area-return-r2-'
PEER = 'problems/2019-B4/reviews/reasoning-area-return-r2-review-2-'
OLD = 'problems/2017-B4/reviews/reasoning-pressure-return-r11-review-2-'
AU = 'problems/2019-B4/reviews/reasoning-occupation-return-r1-review-2-'

def now(): return datetime.now(timezone.utc).isoformat()
def safe(p):
    assert not p.startswith(PEER) and not Path(p).is_absolute() and '..' not in Path(p).parts
def obj(p):
    safe(p)
    return json.loads((R / p).read_text())
def rec(p):
    safe(p)
    b = (R / p).read_bytes()
    return dict(path=p, bytes=len(b), sha256=hashlib.sha256(b).hexdigest())
def check(rows):
    for r in rows:
        assert rec(r['path']) == {k:r[k] for k in ('path','bytes','sha256')}, r['path']
def summary(rows):
    unique = {}
    for r in rows:
        clean = {k:r[k] for k in ('path','bytes','sha256')}
        assert unique.setdefault(r['path'], clean) == clean
    ordered = [unique[p] for p in sorted(unique)]
    raw = json.dumps(ordered, sort_keys=True, separators=(',',':')).encode()
    return dict(occurrences=len(rows), unique_paths=len(ordered),
                canonical_deduplicated_sha256=hashlib.sha256(raw).hexdigest())
def old_guards():
    b = obj(A+'baseline-v1.json')
    parent = obj(OLD+'baseline-v1.json')
    rows = parent['direct_records'] + obj(AU+'baseline-v1.json')['records']
    check(rows)
    assert summary(rows) == b['parent_historical_guard_summary']
    allrows = b['direct_records'] + rows
    check(allrows)
    assert summary(allrows) == b['effective_guard_summary']
    return allrows
def ledger():
    text = (R/(P+'report-v1.md')).read_text()
    labels = [line.split('|')[1].strip() for line in text.splitlines()
              if line.startswith('| ') and line[2:4].isdigit()]
    assert labels == [str(i).zfill(2) for i in range(1,49)], labels
    return len(labels)
def put(suffix, value):
    with (R/(P+suffix)).open('x') as f:
        f.write(json.dumps(value, indent=2)+'\n')
def prepare():
    f = obj(A+'freeze-v1.json')
    assert rec(A+'freeze-v1.json')['sha256'] == '4aac68a1c6a818030c70066019828eee565d60bffdacb14487dd9e9c972f346d'
    assert f['ENTIRE_files'] == 11 and len(f['payloads']) == 10 and ledger() == 48
    direct = f['payloads'] + [rec(A+'freeze-v1.json'),rec('AGENTS.md')]
    for name in ('reasoning-return-r7','reasoning-cut-transfer-r6','reasoning-occupation-return-r1'):
        direct += [rec('problems/2019-B4/reviews/'+name+'-acceptance'+ext) for ext in ('.md','.json')]
    check(direct)
    inherited = old_guards()
    put('baseline-v1.json',dict(created_at_utc=now(),direct=direct,
        compact_author_guard=rec(A+'baseline-v1.json'),
        author_guard_summary=summary(inherited),
        effective_summary=summary(direct+inherited),
        fresh_read_limits='Literal full and excerpted scopes in report; historical hashing is preservation only.',
        NEW_peer_actual_inventory_open_hash_findings_access=False,
        administrative_peer_identity_only_received=True,
        mathematical_program_or_old_replay=False))
    print(json.dumps(dict(action='prepare',PASS=True,ENTIRE_author=11,whole_obligations=48,summary=summary(direct+inherited))))
def validate():
    b = obj(P+'baseline-v1.json')
    check(b['direct']+[b['compact_author_guard']])
    inherited = old_guards()
    assert summary(inherited) == b['author_guard_summary']
    assert summary(b['direct']+inherited) == b['effective_summary']
    assert ledger() == 48
    return b
def freeze():
    b = validate()
    rows = [rec(P+s) for s in ('report-v1.md','admin-v1.py','baseline-v1.json')]
    put('manifest-v1.json',dict(frozen_at_utc=now(),status='initial WHOLE1; EMBARGO until explicit BOTH ENTIRE',
        reviewer='/root',constructor='/root/review_2021_reasoning_j15_r2',constructor_excluded=True,
        ENTIRE_files=4,whole_obligations=48,independent_dispositions=48,payloads=rows,
        unresolved_substantive_defects=0,required_repair=False,closed_scope_notes=7,
        FULL_final_ALL3_payload_model_readback='actually completed before this freeze',
        FULL_manifest_model_readback_then_SEPARATE_verify_required=True,
        effective_summary=b['effective_summary'],NEW_peer_actual_inventory_open_hash_findings_access=False,
        administrative_peer_identity_only_received=True,
        requested=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),effective_setting_readback=None))
    print(json.dumps(dict(action='freeze',manifest=rec(P+'manifest-v1.json'),ENTIRE=4,whole_obligations=48)))
def verify():
    b = validate()
    m = obj(P+'manifest-v1.json')
    check(m['payloads'])
    assert m['effective_summary'] == b['effective_summary']
    print(json.dumps(dict(action='SEPARATE read-only verify',verified_at_utc=now(),PASS=True,
        ENTIRE=4,whole_obligations=48,manifest=rec(P+'manifest-v1.json'),summary=b['effective_summary'])))
if __name__ == '__main__':
    assert len(sys.argv)==2 and sys.argv[1] in ('prepare','freeze','verify')
    {'prepare':prepare,'freeze':freeze,'verify':verify}[sys.argv[1]]()
