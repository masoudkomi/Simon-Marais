"""NEW author documentary byte/JSON/label preservation only; no math or old code."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,sys
R=Path.cwd();P='problems/2024-B4/notes/coordinator-tensor-return-r12-'
INPUTS=['AGENTS.md','problems/2024-B4/statement.md',
 'problems/2024-B4/proofs/reviewed-reasoning-frobenius-return-r10-v1.1.md',
 'problems/2024-B4/reviews/reasoning-frobenius-return-r10-acceptance.md',
 'problems/2024-B4/reviews/reasoning-frobenius-return-r10-acceptance.json']
def now():return datetime.now(timezone.utc).isoformat()
def safe(p):
    assert not Path(p).is_absolute() and '..' not in Path(p).parts
    assert 'reasoning-frobenius-return-r11-review-' not in p
def rec(p):
    safe(p);b=(R/p).read_bytes()
    return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def obj(p):safe(p);return json.loads((R/p).read_text())
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
    for x in rows:assert rec(x['path'])=={k:x[k] for k in ('path','bytes','sha256')},x['path']
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def summary(rows):
    u={}
    for x in rows:
        c={k:x[k] for k in ('path','bytes','sha256')};assert u.setdefault(x['path'],c)==c
    return dict(occurrences=len(rows),unique_paths=len(u),canonical_sha256=digest([u[p] for p in sorted(u)]))
def labels():
    t=(R/(P+'candidate-v1.md')).read_text()
    found=[l.split('|')[1].strip() for l in t.splitlines() if l.startswith('| TR12-O')]
    assert found==['TR12-O'+str(i).zfill(2) for i in range(1,49)]
    return len(found)
def put(s,x):
    with (R/(P+s)).open('x') as f:f.write(json.dumps(x,indent=2)+'\n')
def guards():
    direct=[rec(p) for p in INPUTS]
    assert direct[2]['sha256']=='ce9a3c9e00ce931716fe00d6ea0a605167ddf58a29779d459a62cbc9dd04d173'
    authority=obj(INPUTS[-1]);assert authority['whole_initials_blind'] and authority['unresolved_substantive_issues']==0
    rows=declared(authority);check(rows)
    return direct,rows
def prepare():
    assert labels()==48
    direct,old=guards()
    put('baseline-v1.json',dict(prepared_at_utc=now(),direct_inputs=direct,
      immutable_authority_binding=rec(INPUTS[-1]),authority_declared_summary=summary(old),
      all_guard_summary=summary(direct+old),administrative_only=True,
      fresh_model_read_limits='Literal in candidate/sourceJSON; historical hashes are preservation only.',
      corresponding_NEW_peer_findings_files_inventory_hash_metadata_access=False))
    print(json.dumps(dict(action='prepare',PASS=True,whole_obligations=48,summary=summary(direct+old))))
def validate():
    b=obj(P+'baseline-v1.json');check(b['direct_inputs']+[b['immutable_authority_binding']]);direct,old=guards()
    assert direct==b['direct_inputs'] and summary(old)==b['authority_declared_summary'] and summary(direct+old)==b['all_guard_summary']
    assert labels()==48
    return b
def freeze():
    b=validate();payloads=[rec(P+s) for s in ['candidate-v1.md','sources-v1.json','admin-v1.py','baseline-v1.json']]
    put('freeze-v1.json',dict(frozen_at_utc=now(),status='candidate proof - unverified',constructor='/root',
      root_and_C_excluded_from_NEW_audit_count=True,OTHER_whole_audits_required=2,
      whole_obligations=48,ENTIRE_files=5,payloads=payloads,all_guard_summary=b['all_guard_summary'],
      FULL_final_MODEL_ALL4_payload_readback_completed=True,
      FULL_manifest_MODEL_readback_then_SEPARATE_readonly_verify_required=True,
      corresponding_NEW_peer_findings_files_inventory_hash_metadata_access=False,
      mathematical_program_CAS_scan_test_or_old_replay=False,
      requested=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),effective_setting_readback=None,
      authorized_weekly_reset=1792874445,TOTAL_ceiling_percent=90))
    print(json.dumps(dict(action='freeze',manifest=rec(P+'freeze-v1.json'),ENTIRE=5,whole_obligations=48)))
def verify():
    b=validate();f=obj(P+'freeze-v1.json');check(f['payloads'])
    assert f['all_guard_summary']==b['all_guard_summary']
    print(json.dumps(dict(action='SEPARATE read-only verify',at_utc=now(),PASS=True,
      ENTIRE=5,whole_obligations=48,manifest=rec(P+'freeze-v1.json'),main=rec(P+'candidate-v1.md'))))
if __name__=='__main__':
    assert len(sys.argv)==2 and sys.argv[1] in ('prepare','freeze','verify')
    {'prepare':prepare,'freeze':freeze,'verify':verify}[sys.argv[1]]()
