"""NEW R24 review1 documentary helper, never mathematical computation.

prepare writes exact necessary guards/compact parent binding.
freeze is used only AFTER final ALL4 MODEL payload readbacks.
verify is a SEPARATE read-only operation AFTER manifest MODEL readback.
No corresponding NEW C review path is inventoried or read.
"""
from pathlib import Path
import datetime as dt
import hashlib
import json
import re
import sys

ROOT=Path(__file__).resolve().parents[3]
P='problems/2021-B4/reviews/reasoning-deep-return-r24-review-1-'
A='problems/2021-B4/notes/reasoning-deep-return-r24-'
OLD='problems/2025-B4/reviews/reasoning-global-return-r11-review-2-'
TARGET={
 A+'freeze-v1.json':(2564,'f2124aa5804550b00eb81e665937718ce24c220929f9003be29fad895c64e833'),
 A+'candidate-v1.md':(22043,'7bb65d69ec32e00050b0dd0bc6d7ce3b6b12a5e9b4dafc43e1a7c60e67ca2a70'),
 OLD+'manifest-v1.json':(2173,'4ef58c57f3b8f8c534ac81f8c6800345784b3ca7de3e6d8698a3c3abf5dcf868')}

def utc(): return dt.datetime.now(dt.timezone.utc).isoformat()
def path(s):
    assert not s.startswith('/') and '..' not in Path(s).parts
    assert 'reasoning-deep-return-r24-review-2-' not in s,'NEW peer forbidden'
    return ROOT/s
def read(s): return json.loads(path(s).read_text())
def row(s):
    b=path(s).read_bytes()
    return {'path':s,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def ck(r):
    out=row(r['path'])
    assert out=={k:r[k] for k in ('path','bytes','sha256')},r['path']
    return out
def declared(o):
    if isinstance(o,dict):
        if all(k in o for k in ('path','bytes','sha256')):
            yield {k:o[k] for k in ('path','bytes','sha256')}
        for v in o.values(): yield from declared(v)
    elif isinstance(o,list):
        for v in o: yield from declared(v)
def unique(rs):
    d={}
    for r in rs:
        if r['path'] in d: assert d[r['path']]==r
        d[r['path']]=r
    return [d[s] for s in sorted(d)]
def sha(rs):
    return hashlib.sha256(json.dumps(rs,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def new(s,o):
    assert s.startswith(P)
    with path(s).open('x') as f:
        json.dump(o,f,indent=2,ensure_ascii=False)
        f.write('\n')
def guards():
    for s,(n,h) in TARGET.items(): ck({'path':s,'bytes':n,'sha256':h})
    rs=[row(A+'freeze-v1.json')]+read(A+'freeze-v1.json')['payloads']
    rs+=read(A+'baseline-v1.json')['necessary_direct_records']
    for name in ('reasoning-negative-return-r23','reasoning-center-return-r18'):
        rs+=list(declared(read('problems/2021-B4/reviews/'+name+'-acceptance.json')))
    rs+=[row(OLD+'manifest-v1.json')]+read(OLD+'manifest-v1.json')['payloads']
    return [ck(r) for r in rs]
def labels():
    want=['O%02d'%i for i in range(1,33)]
    for s in (A+'candidate-v1.md',P+'initial-v1.md'):
        got=re.findall(r'^\|\s*(O\d{2})\s*\|',path(s).read_text(),re.M)
        assert got==want
def verifyguards(b):
    for r in b['necessary_guards']: ck(r)
    assert sha(b['necessary_guards'])==b['deduplicated_digest']

mode=sys.argv[1]
if mode=='prepare':
    labels(); rs=guards(); us=unique(rs)
    ab=read(A+'baseline-v1.json')
    new(P+'baseline-v1.json',{
      'created_UTC':utc(),'reviewer':'/root/review_2022_complexity_r2','whole_obligations':32,
      'necessary_guards':us,'declared_occurrences_verified':len(rs),'unique_paths':len(us),
      'deduplicated_digest':sha(us),
      'author_42_occurrence_history_bound_NOT_reexpanded':ab['effective_fresh_guard_summary'],
      'author_66_occurrence_parent_history_bound_NOT_reexpanded':ab['compact_parent_binding']['parent_historical_guard_summary_bound_NOT_reexpanded'],
      'own_immediate_GR11_parent_ENTIRE5_verified':row(OLD+'manifest-v1.json'),
      'own_older_1025_path_chain_bound_transitively_NOT_recopied':True,
      'mutable_current_observations_NOT_immutable_live_guards':True,
      'requested':{'model':'gpt-6.1-sol','reasoning':'max','inherited':True},
      'independent_effective_backend_readback':None,
      'NEW_C_R24_findings_files_actual_inventory_hash_metadata_accessed':False,
      'quota':{'usedPercent':74,'observed_UTC':'2026-10-19 00:04:04 UTC','resetsAt':1792874445,'windowDurationMins':10080,'ordinaryUsageAllowed':True,'TOTAL_ceiling':90,'reserve':True,'automatic_later_window_spending':False},
      'mathematical_code_CAS_scan_test_source_author_old_replay':False})
    print(json.dumps({'prepared':True,'occurrences':len(rs),'unique_paths':len(us),'ALL_labels':32}))
elif mode=='freeze':
    labels(); b=read(P+'baseline-v1.json'); verifyguards(b)
    names=['initial-v1.md','sources-v1.json','admin-v1.py','baseline-v1.json']
    new(P+'manifest-v1.json',{
      'frozen_UTC':utc(),'status':'OTHER initially blind WHOLE1; findings sealed pending explicit BOTH',
      'reviewer':'/root/review_2022_complexity_r2','constructor':'/root/review_2021_reasoning_j15_r2','constructor_excluded':True,
      'ENTIRE_files':5,'payload_count':4,'whole_obligations':32,
      'payloads':[row(P+s) for s in names],
      'declared_occurrences_verified':b['declared_occurrences_verified'],'unique_paths':b['unique_paths'],'guard_digest':b['deduplicated_digest'],
      'FULL_final_ALL4_payload_MODEL_readbacks_completed':True,
      'FULL_manifest_MODEL_readback_then_SEPARATE_readonly_verify_REQUIRED':True,
      'NEW_C_R24_findings_files_actual_inventory_hash_metadata_accessed':False,
      'findings_EMBARGO_until_explicit_BOTH':True,
      'requested':b['requested'],'independent_effective_backend_readback':None,'quota':b['quota'],
      'mathematical_program_CAS_scan_test_source_author_old_replay':False,'Git_shared_old_cache_mutation':False})
    print(json.dumps({'frozen':True,'manifest':row(P+'manifest-v1.json')}))
elif mode=='verify':
    labels(); m=read(P+'manifest-v1.json')
    for r in m['payloads']: ck(r)
    b=read(P+'baseline-v1.json'); verifyguards(b)
    assert m['guard_digest']==b['deduplicated_digest']
    print(json.dumps({'SEPARATE_readonly_verify':'PASS','verified_UTC':utc(),'ENTIRE_files':5,'ALL_obligations':32,'necessary_unique_paths':b['unique_paths'],'manifest':row(P+'manifest-v1.json')}))
else: raise ValueError(mode)
