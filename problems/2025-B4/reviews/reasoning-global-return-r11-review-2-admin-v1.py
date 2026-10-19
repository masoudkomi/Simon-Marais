"""GR11 review2 NEW documentary byte/JSON/label helper; no mathematics.

prepare: bind exact author5/current operative authority declarations/own
immediate R19 parent5 without expanding growing historical inventories.
freeze: AFTER FULL final MODEL readbacks, record ALL4 payload fingerprints.
verify: separate read-only check AFTER FULL manifest MODEL readback.
Never inventories or reads corresponding NEW peer GR11 review material.
"""
import datetime
import hashlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
P = 'problems/2025-B4/reviews/reasoning-global-return-r11-review-2-'
AUTHOR = 'problems/2025-B4/notes/reasoning-global-return-r11-'
PARENT = 'problems/2020-B4/notes/reasoning-realization-return-r19-'
EXPECTED = {
    AUTHOR+'freeze-v1.json': (2639, '1e6953c80d9d17efbb2b94c5ae6af3a0b9880119d46c1e0fde7dc4c28a266771'),
    AUTHOR+'candidate-v1.md': (25923, 'aa1e1242621a9bd99b42bb306827e41e8ee6309b963ce2c63c8e503cd325bbe3'),
    PARENT+'freeze-v1.json': (2637, 'a4967473504c2ff3a481487e84a5a07ae9305bf8da00b6594ef298185eed01d5')
}

def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def readj(path):
    return json.loads((ROOT/path).read_text())

def fp(path):
    b = (ROOT/path).read_bytes()
    return {'path': path, 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}

def check(r):
    assert not ('reasoning-global-return-r11-review-1-' in r['path']), 'NEW peer forbidden'
    assert fp(r['path']) == {k:r[k] for k in ('path','bytes','sha256')}, r['path']
    return {k:r[k] for k in ('path','bytes','sha256')}

def records(o):
    if isinstance(o, dict):
        if all(k in o for k in ('path','bytes','sha256')):
            yield {k:o[k] for k in ('path','bytes','sha256')}
        for v in o.values():
            yield from records(v)
    elif isinstance(o, list):
        for v in o:
            yield from records(v)

def payloads(m):
    for key in ('payloads','payload_records','files','artifacts'):
        if key in m:
            return m[key]
    raise ValueError('No payload key')

def directguards():
    for path, (n,h) in EXPECTED.items():
        check({'path':path, 'bytes':n, 'sha256':h})
    af = readj(AUTHOR+'freeze-v1.json')
    ab = readj(AUTHOR+'baseline-v1.json')
    pf = readj(PARENT+'freeze-v1.json')
    rr = [fp(AUTHOR+'freeze-v1.json')]
    rr += payloads(af)
    rr += ab['necessary_direct_records']
    for suffix in ('reasoning-compatible-return-r10-acceptance.json',
                   'reasoning-diagonal-return-r8-acceptance.json'):
        rr += list(records(readj('problems/2025-B4/reviews/'+suffix)))
    rr += [fp(PARENT+'freeze-v1.json')]+payloads(pf)
    return [check(r) for r in rr]

def dedup(rr):
    d = {}
    for r in rr:
        if r['path'] in d:
            assert d[r['path']] == r
        d[r['path']] = r
    return [d[k] for k in sorted(d)]

def digest(rr):
    return hashlib.sha256(json.dumps(rr,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def labels():
    a = (ROOT/(AUTHOR+'candidate-v1.md')).read_text()
    r = (ROOT/(P+'initial-v1.md')).read_text()
    want = {'O%02d'%i for i in range(1,33)}
    for text in (a,r):
        got = re.findall(r'^\|\s*(O\d{2})\s*\|',text,re.M)
        assert len(got)==32 and set(got)==want

def write_new(path,o):
    with (ROOT/path).open('x') as f:
        json.dump(o,f,indent=2,ensure_ascii=False)
        f.write('\n')

mode=sys.argv[1]
if mode=='prepare':
    labels()
    rr=directguards()
    uu=dedup(rr)
    ab=readj(AUTHOR+'baseline-v1.json')
    write_new(P+'baseline-v1.json', {
        'created_UTC':now(), 'reviewer':'/root/review_2022_complexity_r2',
        'whole_obligations':32, 'author_exact5_and_current_operating_guards':uu,
        'verified_declared_occurrences':len(rr), 'unique_paths':len(uu),
        'canonical_deduplicated_sha256':digest(uu),
        'author_66_occurrence_history_bound_NOT_reexpanded':ab['effective_fresh_guard_summary'],
        'author_69_occurrence_parent_history_bound_NOT_reexpanded':ab['compact_parent_binding']['parent_historical_summary_bound_NOT_reexpanded'],
        'own_immediate_R19_parent_bound_all4_payloads_verified':fp(PARENT+'freeze-v1.json'),
        'own_older_chain_1020_paths_bound_transitively_NOT_recopied':True,
        'mutable_current_maps_are_dated_observations_NOT_immutable_guards':True,
        'requested':{'model':'gpt-6.1-sol','reasoning':'max','inherited':True},
        'independent_effective_setting_readback':None,
        'NEW_C_GR11_peer_findings_files_actual_inventory_hash_metadata_accessed':False,
        'quota':{'usedPercent':73,'observed_UTC':'2026-10-18 23:57:49 UTC','resetsAt':1792874445,'windowDurationMins':10080,'ordinaryUsageAllowed':True,'TOTAL_ceiling':90,'reserve':True,'automatic_later_window':False},
        'mathematical_code_scan_CAS_test_old_replay':False
    })
    print(json.dumps({'prepared':True,'occurrences':len(rr),'unique_paths':len(uu),'labels':32}))
elif mode=='freeze':
    labels()
    b=readj(P+'baseline-v1.json')
    for r in b['author_exact5_and_current_operating_guards']:
        check(r)
    names=['initial-v1.md','sources-v1.json','admin-v1.py','baseline-v1.json']
    write_new(P+'manifest-v1.json',{
        'frozen_UTC':now(),'status':'independent initially blind WHOLE2 initial review; findings sealed pending BOTH release',
        'reviewer':'/root/review_2022_complexity_r2','constructor':'/root/review_2021_reasoning_j15_r2','constructor_excluded':True,
        'ENTIRE_files':5,'payload_count':4,'whole_obligations':32,
        'payloads':[fp(P+n) for n in names],
        'verified_declared_occurrences':b['verified_declared_occurrences'],'unique_paths':b['unique_paths'],
        'guard_digest':b['canonical_deduplicated_sha256'],
        'FULL_final_ALL4_payload_MODEL_readbacks_completed':True,
        'FULL_manifest_MODEL_readback_then_SEPARATE_readonly_verification_REQUIRED':True,
        'NEW_C_GR11_findings_files_actual_inventory_hash_metadata_accessed':False,
        'findings_EMBARGO_until_explicit_BOTH':True,
        'requested':b['requested'],'independent_effective_setting_readback':None,
        'quota':b['quota'],'mathematical_program_CAS_scan_test_source_author_old_replay':False,
        'Git_shared_old_cache_mutation':False
    })
    print(json.dumps({'frozen':True,'manifest':fp(P+'manifest-v1.json')}))
elif mode=='verify':
    labels()
    m=readj(P+'manifest-v1.json')
    for r in m['payloads']:
        check(r)
    b=readj(P+'baseline-v1.json')
    for r in b['author_exact5_and_current_operating_guards']:
        check(r)
    assert digest(b['author_exact5_and_current_operating_guards'])==m['guard_digest']
    print(json.dumps({'SEPARATE_readonly_verify':'PASS','verified_UTC':now(),'ENTIRE_files':5,'ALL_obligations':32,'immutable_necessary_paths':b['unique_paths'],'manifest':fp(P+'manifest-v1.json')}))
else:
    raise ValueError(mode)
