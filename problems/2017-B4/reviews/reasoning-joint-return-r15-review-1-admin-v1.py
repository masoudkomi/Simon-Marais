#!/usr/bin/env python3
"""JC15 review1 documentary integrity ONLY; no mathematical computation.
prepare creates NEW baseline. FULL final ALL4 payload MODEL readbacks
precede freeze; FULL manifest MODEL readback precedes SEPARATE verify.
No author/source/old helper is executed; current NEW peer is forbidden.
"""
import argparse
import datetime as dt
import hashlib
import json
import re
from pathlib import Path

ROOT=Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PFX='problems/2017-B4/reviews/reasoning-joint-return-r15-review-1-'
BASE=PFX+'baseline-v1.json'
MANIFEST=PFX+'manifest-v1.json'
PAYLOADS=[PFX+'initial-v1.md',PFX+'sources-v1.json',PFX+'admin-v1.py',BASE]
AUTHOR='problems/2017-B4/notes/reasoning-joint-return-r15-freeze-v1.json'
PARENT='problems/2024-B4/notes/reasoning-classification-return-r14-freeze-v1.json'
FORBIDDEN='problems/2017-B4/reviews/reasoning-joint-return-r15-review-2-'
EXPECTED={
PARENT:(1836,'89a6e276fe28ba0bc2f1a5ffe94636353efc6c457f613dbb1f5767c4dd683d73'),
'problems/2017-B4/notes/reasoning-joint-return-r15-candidate-v1.md':
    (30299,'a17fb4f40f8f46be18ec0ac1a3631f1448a2d15570591417f7a9b6a9c24136bf')}

def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()

def safe(p):
    assert isinstance(p,str) and not p.startswith('/') and '..' not in Path(p).parts
    assert not p.startswith(FORBIDDEN),p
    return ROOT/p

def fp(p):
    b=safe(p).read_bytes()
    return {'path':p,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}

def load(p):
    return json.loads(safe(p).read_text())

def check(row):
    got=fp(row['path'])
    assert got=={k:row[k] for k in ('path','bytes','sha256')},row['path']
    return got

def summary(records):
    unique={}
    for r in records:
        if r['path'] in unique:
            assert unique[r['path']]==r
        unique[r['path']]=r
    ordered=[unique[k] for k in sorted(unique)]
    raw=json.dumps(ordered,sort_keys=True,separators=(',',':')).encode()
    return {'occurrences':len(records),'unique_paths':len(ordered),
        'canonical_deduplicated_sha256':hashlib.sha256(raw).hexdigest()}

def labels():
    text=safe(PAYLOADS[0]).read_text()
    assert re.findall(r'^\| (JC15-\d\d) \|',text,re.M)==['JC15-%02d'%i for i in range(1,37)]
    assert len(re.findall(r'^\| JC15R1-N\d+ \|',text,re.M))==10
    source=load(PAYLOADS[1])
    assert source['ALL_obligations']==36
    assert source['NEW_corresponding_peer_findings_files_actual_inventory_hash_metadata_access'] is False

def collect():
    for p,expected in EXPECTED.items():
        got=fp(p)
        assert (got['bytes'],got['sha256'])==expected,p
    author=load(AUTHOR)
    assert author['ENTIRE_files']==5 and author['whole_obligations']==36
    ap=[check(r) for r in author['payloads']]
    assert len(ap)==4
    ab=load(next(r['path'] for r in ap if r['path'].endswith('-baseline-v1.json')))
    direct=[check(r) for r in ab['necessary_direct_records']]
    assert len(direct)==11
    accepted=[]
    for r in direct:
        if r['path'].endswith('-acceptance.json'):
            authority=load(r['path'])
            assert authority['unresolved_substantive_issues']==0
            accepted.append(check(authority['accepted_copy']))
    assert len(accepted)==3
    old_parent=check(ab['compact_own_parent'])
    old_meta=load(old_parent['path'])
    old_payloads=[check(r) for r in old_meta['payloads']]
    assert len(old_payloads)==4
    author_guards=direct+accepted+[old_parent]+old_payloads
    assert summary(author_guards)==author['effective_fresh_guard_summary']
    parent=load(PARENT)
    pp=[check(r) for r in parent['payload_records']]
    assert len(pp)==4 and parent['ALL_obligations']==48
    guards=[fp(AUTHOR)]+ap+author_guards+[fp(PARENT)]+pp
    return {'guard_summary':summary(guards),'author':fp(AUTHOR),
        'author_payloads_verified':4,'author_current_operative_direct_records':11,
        'author_effective_summary_verified':summary(author_guards),
        'author_OLD_parent_outer_binding':old_parent,'author_OLD_parent_payloads_verified':4,
        'author_OLD_parent_historical_summary_bound_NOT_expanded':ab['parent_historical_guard_summary_bound_NOT_reexpanded'],
        'immediate_own_parent':fp(PARENT),'own_parent_payloads_verified':4,
        'own_parent_historical_summary_bound_NOT_expanded':parent['guard_summary'],
        'NEW_peer_access':False}

def write_new(p,value):
    assert p.startswith(PFX)
    with safe(p).open('x') as f:
        json.dump(value,f,indent=2)
        f.write('\n')

def prepare():
    labels()
    value={'created_utc':now(),'reviewer':'/root/review_2017_coarsening_r1',
        'type':'OTHER initially blind ENTIRE WHOLE JC15 review1','ALL_obligations':36,
        'integrity':collect(),'OLD_PR11_CI12_LF14_constructor_role_disclosed':True,
        'OLD_inputs_independently_self_recertified':False,
        'NEW_JC15_construction_contribution':False,'NEW_peer_access':False,
        'findings_sealed_until_explicit_BOTH':True,
        'requested':{'model':'gpt-6.1-sol','reasoning':'max','inherited':True},
        'independently_verified_effective_readback':None,
        'quota':{'usedPercent':76,'observed_utc':'2026-10-19 00:49:13 UTC',
            'resetsAt':1792874445,'ordinaryUsageAllowed':True,
            'TOTAL_ceiling':90,'review_integration_reserve':True,'automatic_later_window':False},
        'mathematical_program_CAS_scan_test_old_author_source_replay':False,
        'documentary_code_only':True,'old_shared_Git_cache_mutation':False,
        'FULL_final_ALL4_MODEL_then_manifest_MODEL_then_SEPARATE_verify_required':True}
    write_new(BASE,value)
    print(json.dumps({'baseline':fp(BASE),'guards':value['integrity']['guard_summary']},indent=2))

def validate():
    labels()
    value=load(BASE)
    assert collect()==value['integrity']
    return value

def freeze(confirmed):
    assert confirmed,'FULL final ALL4 MODEL payload readbacks required'
    base=validate()
    value={'frozen_utc':now(),'type':'OTHER initially blind ENTIRE WHOLE JC15 review1',
        'reviewer':'/root/review_2017_coarsening_r1','ENTIRE_files':5,'ALL_obligations':36,
        'payload_records':[fp(p) for p in PAYLOADS],
        'author':fp(AUTHOR),'immediate_own_parent':fp(PARENT),
        'guard_summary':base['integrity']['guard_summary'],
        'FULL_final_ALL4_MODEL_payload_readbacks_completed':True,
        'FULL_manifest_MODEL_readback_then_SEPARATE_verify_REQUIRED':True,
        'NEW_peer_access':False,'findings_sealed_until_explicit_BOTH':True,
        'mathematical_computation':False,'old_shared_Git_cache_mutation':False}
    write_new(MANIFEST,value)
    print(json.dumps({'manifest':fp(MANIFEST),'frozen_utc':value['frozen_utc']},indent=2))

def verify(expected):
    assert expected and fp(MANIFEST)['sha256']==expected
    value=load(MANIFEST)
    for r in value['payload_records']:
        check(r)
    base=validate()
    assert value['guard_summary']==base['integrity']['guard_summary']
    print(json.dumps({'verified_utc':now(),'result':'PASS','manifest':fp(MANIFEST),
        'ENTIRE_files':5,'ALL_obligations':36,'writes':0,'mathematical_computation':False,
        'NEW_peer_access':False,'findings_sealed_until_explicit_BOTH':True},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode',choices=['prepare','freeze','verify'])
    parser.add_argument('--final-payload-readback-confirmed',action='store_true')
    parser.add_argument('--manifest-sha')
    args=parser.parse_args()
    if args.mode=='prepare': prepare()
    elif args.mode=='freeze': freeze(args.final_payload_readback_confirmed)
    else: verify(args.manifest_sha)
