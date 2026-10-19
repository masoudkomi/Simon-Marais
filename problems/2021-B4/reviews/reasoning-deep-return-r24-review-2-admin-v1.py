#!/usr/bin/env python3
"""R24 review2 documentary integrity only; no mathematical computation.
prepare writes only NEW baseline. FULL final ALL4 MODEL readbacks precede
freeze; FULL manifest MODEL readback precedes a SEPARATE verify command.
No corresponding NEW B review1 or root R19 review1 is enumerated/accessed.
No author/old/source helper or mathematical certificate is executed.
"""
import argparse
import datetime as dt
import hashlib
import json
import re
from pathlib import Path

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PFX = 'problems/2021-B4/reviews/reasoning-deep-return-r24-review-2-'
BASE = PFX + 'baseline-v1.json'
MANIFEST = PFX + 'manifest-v1.json'
PAYLOADS = [PFX+'initial-v1.md', PFX+'sources-v1.json', PFX+'admin-v1.py', BASE]
AUTHOR = 'problems/2021-B4/notes/reasoning-deep-return-r24-freeze-v1.json'
PARENT = 'problems/2020-B4/reviews/reasoning-realization-return-r19-review-2-manifest-v1.json'
EXPECTED = {
    AUTHOR: (2564, 'f2124aa5804550b00eb81e665937718ce24c220929f9003be29fad895c64e833'),
    PARENT: (2071, '15ace6e5601215ef6d5cae280f38f2df1d9306d3a72d3cc3e2d04ece698e39a7'),
    'problems/2021-B4/notes/reasoning-deep-return-r24-candidate-v1.md':
        (22043, '7bb65d69ec32e00050b0dd0bc6d7ce3b6b12a5e9b4dafc43e1a7c60e67ca2a70')}
FORBIDDEN = [
    'problems/2021-B4/reviews/reasoning-deep-return-r24-review-1-',
    'problems/2020-B4/reviews/reasoning-realization-return-r19-review-1-',
    'problems/2024-B4/reviews/coordinator-tensor-family-return-r13-']

def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()

def safe(path):
    assert isinstance(path, str) and not path.startswith('/')
    assert '..' not in Path(path).parts
    assert not any(path.startswith(p) for p in FORBIDDEN), path
    return ROOT/path

def fp(path):
    data = safe(path).read_bytes()
    return {'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def read(path):
    return json.loads(safe(path).read_text())

def check(row):
    got = fp(row['path'])
    assert got == {k: row[k] for k in ('path','bytes','sha256')}, row['path']
    return got

def rows(value):
    if isinstance(value, dict):
        if all(k in value for k in ('path','bytes','sha256')):
            yield {k: value[k] for k in ('path','bytes','sha256')}
        for child in value.values():
            yield from rows(child)
    elif isinstance(value, list):
        for child in value:
            yield from rows(child)

def summary(records):
    unique = {}
    for row in records:
        if row['path'] in unique:
            assert unique[row['path']] == row
        unique[row['path']] = row
    ordered = [unique[k] for k in sorted(unique)]
    data = json.dumps(ordered, sort_keys=True, separators=(',',':')).encode()
    return {'occurrences':len(records),'unique_paths':len(ordered),
            'canonical_deduplicated_sha256':hashlib.sha256(data).hexdigest()}

def labels():
    value = safe(PAYLOADS[0]).read_text()
    assert re.findall(r'^\| (O\d\d) \|', value, re.M) == ['O%02d'%i for i in range(1,33)]
    assert len(re.findall(r'^\| R24R2-N\d+ \|', value, re.M)) == 10
    read(PAYLOADS[1])

def collect():
    for path, expected in EXPECTED.items():
        actual = fp(path)
        assert (actual['bytes'],actual['sha256']) == expected, path
    author = read(AUTHOR)
    author_rows = [check(r) for r in author['payloads']]
    assert len(author_rows)==4 and author['whole_obligations']==32
    author_base = read(next(r['path'] for r in author_rows if r['path'].endswith('-baseline-v1.json')))
    direct = [check(r) for r in author_base['necessary_direct_records']]
    declared = []
    counts = []
    for item in author_base['current_authority_declared_records_verified']:
        authority = read(item['path'])
        found = list(rows(authority))
        assert len(found)==item['declared_occurrences']
        declared.extend(check(r) for r in found)
        counts.append({'authority':fp(item['path']),'declared_count':len(found)})
    parent = read(PARENT)
    parent_rows = [check(r) for r in parent['payload_records']]
    assert len(parent_rows)==4
    records = [fp(AUTHOR)]+author_rows+direct+declared+[fp(PARENT)]+parent_rows
    return {'guard_summary':summary(records),'author_ENTIRE':fp(AUTHOR),
        'author_payloads_verified':len(author_rows),'direct_inputs_verified':len(direct),
        'current_authority_bindings':counts,
        'author_historical_summary_bound_NOT_expanded':author['effective_fresh_guard_summary'],
        'author_external_parent_NOT_replayed':True,
        'immediate_own_parent':fp(PARENT),'own_parent_payloads_verified':len(parent_rows),
        'own_parent_historical_summary_bound_NOT_expanded':parent['guard_summary']}

def write_new(path, value):
    assert path.startswith(PFX)
    with safe(path).open('x') as stream:
        json.dump(value,stream,indent=2)
        stream.write('\n')

def prepare():
    labels()
    value = {'created_utc':now(),'reviewer':'/root/review_2017_coarsening_r1',
        'WHOLE_obligations':32,'compact_integrity':collect(),
        'initially_blind':True,'NEW_B_R24_peer_access':False,
        'NEW_root_R19_peer_access':False,
        'R19_own_disposition_released_only_after_explicit_BOTH':True,
        'findings_sealed_until_explicit_BOTH':True,
        'OLD_roles_disclosed_not_independent_self_recertification':True,
        'NEW_R24_construction_contribution':False,
        'requested':{'model':'gpt-6.1-sol','reasoning':'max','inherited':True},
        'independent_effective_setting_readback':None,
        'quota':{'usedPercent':74,'observed_utc':'2026-10-19 00:03:59 UTC',
            'windowDurationMins':10080,'resetsAt':1792874445,'ordinaryUsageAllowed':True,
            'TOTAL_ceiling':90,'integration_reserve':True,'automatic_later_window':False},
        'mathematical_program_CAS_scan_test_optimizer_old_source_author_replay':False,
        'old_shared_Git_cache_mutation':False,
        'FULL_final_ALL4_MODEL_then_manifest_readbacks_and_SEPARATE_verify_required':True}
    write_new(BASE,value)
    print(json.dumps({'baseline':fp(BASE),'guards':value['compact_integrity']['guard_summary']},indent=2))

def validate():
    labels()
    value=read(BASE)
    assert collect()==value['compact_integrity']
    return value

def freeze(confirmed):
    assert confirmed,'FULL final ALL4 MODEL payload readbacks required before freeze'
    base=validate()
    value={'frozen_utc':now(),'type':'OTHER initially blind ENTIRE WHOLE2 R24 initial',
        'reviewer':'/root/review_2017_coarsening_r1','WHOLE_obligations':32,'ENTIRE_files':5,
        'payload_records':[fp(p) for p in PAYLOADS],
        'guard_summary':base['compact_integrity']['guard_summary'],
        'author':fp(AUTHOR),'immediate_own_parent':fp(PARENT),
        'FULL_final_MODEL_ALL4_payload_readback_completed':True,
        'FULL_manifest_MODEL_readback_then_SEPARATE_verify_REQUIRED':True,
        'NEW_B_R24_peer_access':False,'NEW_root_R19_peer_access':False,
        'R19_own_disposition_released_only_after_explicit_BOTH':True,
        'findings_sealed_until_explicit_BOTH':True,
        'mathematical_program_CAS_scan_test_old_replay':False,
        'old_shared_Git_cache_mutation':False}
    write_new(MANIFEST,value)
    print(json.dumps({'manifest':fp(MANIFEST),'frozen_utc':value['frozen_utc'],'ENTIRE_files':5},indent=2))

def verify(expected):
    assert expected and fp(MANIFEST)['sha256']==expected
    value=read(MANIFEST)
    for row in value['payload_records']:
        check(row)
    base=validate()
    assert value['guard_summary']==base['compact_integrity']['guard_summary']
    print(json.dumps({'verified_utc':now(),'result':'PASS','manifest':fp(MANIFEST),
        'ENTIRE_files':5,'WHOLE_obligations':32,'writes':0,'mathematical_computation':False,
        'NEW_B_R24_peer_access':False,'NEW_root_R19_peer_access':False},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode',choices=['prepare','freeze','verify'])
    parser.add_argument('--final-payload-readback-confirmed',action='store_true')
    parser.add_argument('--manifest-sha')
    args=parser.parse_args()
    if args.mode=='prepare': prepare()
    elif args.mode=='freeze': freeze(args.final_payload_readback_confirmed)
    else: verify(args.manifest_sha)
