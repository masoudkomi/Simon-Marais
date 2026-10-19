#!/usr/bin/env python3
"""NEW R24 documentary integrity only; no mathematical computation.

prepare creates the NEW compact baseline. After FULL final model readback
of ALL4 payloads, freeze --final-payload-readback-confirmed creates the
manifest. After FULL manifest readback, a SEPARATE verify --manifest-sha
EXACT_SHA command checks every bound current fingerprint read-only.
No old/source/author program or mathematical certificate is executed.
"""
import argparse
import datetime as dt
import hashlib
import json
import re
from pathlib import Path

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PFX = 'problems/2021-B4/notes/reasoning-deep-return-r24-'
BASELINE = PFX + 'baseline-v1.json'
MANIFEST = PFX + 'freeze-v1.json'
PAYLOADS = [PFX+'candidate-v1.md', PFX+'sources-v1.json',
            PFX+'admin-v1.py', BASELINE]
AUTHORITIES = [
 'problems/2021-B4/reviews/reasoning-negative-return-r23-acceptance.json',
 'problems/2021-B4/reviews/reasoning-center-return-r18-acceptance.json']
DIRECT = ['AGENTS.md', 'problems/2021-B4/statement.md',
 'problems/2021-B4/proofs/reviewed-reasoning-negative-return-r23-v1.1.md',
 'problems/2021-B4/reviews/reasoning-negative-return-r23-acceptance.md', AUTHORITIES[0],
 'problems/2021-B4/proofs/reviewed-reasoning-center-return-r18-v1.1.md',
 'problems/2021-B4/reviews/reasoning-center-return-r18-acceptance.md', AUTHORITIES[1]]
PARENT = 'problems/2025-B4/notes/reasoning-global-return-r11-freeze-v1.json'
PARENT_EXPECTED = {'path': PARENT, 'bytes': 2639,
 'sha256': '1e6953c80d9d17efbb2b94c5ae6af3a0b9880119d46c1e0fde7dc4c28a266771'}
FORBIDDEN = 'problems/2019-B4/'

def utc():
    return dt.datetime.now(dt.timezone.utc).isoformat()

def safe(path):
    assert isinstance(path, str) and not path.startswith('/')
    assert '..' not in Path(path).parts and not path.startswith(FORBIDDEN)
    return ROOT/path

def fp(path):
    data = safe(path).read_bytes()
    return {'path': path, 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}

def read(path):
    return json.loads(safe(path).read_text())

def check(row):
    actual = fp(row['path'])
    assert actual == {key: row[key] for key in ('path','bytes','sha256')}, row['path']
    return actual

def declared(value):
    if isinstance(value, dict):
        if all(key in value for key in ('path','bytes','sha256')):
            yield {key: value[key] for key in ('path','bytes','sha256')}
        for child in value.values():
            yield from declared(child)
    elif isinstance(value, list):
        for child in value:
            yield from declared(child)

def digest(items):
    unique = {}
    for row in items:
        if row['path'] in unique:
            assert unique[row['path']] == row
        unique[row['path']] = row
    data = [unique[path] for path in sorted(unique)]
    raw = json.dumps(data,sort_keys=True,separators=(',',':')).encode()
    return {'occurrences':len(items),'unique_paths':len(data),
            'canonical_deduplicated_sha256':hashlib.sha256(raw).hexdigest()}

def collect():
    items = [fp(path) for path in DIRECT]
    authorities = []
    for path in AUTHORITIES:
        rows = list(declared(read(path)))
        items.extend(check(row) for row in rows)
        authorities.append({'path':path,'declared_occurrences':len(rows)})
    check(PARENT_EXPECTED)
    parent = read(PARENT)
    parent_payloads = [check(row) for row in parent['payloads']]
    items.extend([PARENT_EXPECTED]+parent_payloads)
    binding = {'parent':PARENT_EXPECTED,'all_parent_payloads_verified':len(parent_payloads),
      'parent_historical_guard_summary_bound_NOT_reexpanded':parent['effective_fresh_guard_summary'],
      'parent_mathematics_NOT_R24_premise':True,
      'mutable_historical_maps_not_live_immutable_guards':True}
    return items, authorities, binding

def write_new(path, data):
    assert path.startswith(PFX)
    with safe(path).open('x') as stream:
        json.dump(data,stream,indent=2)
        stream.write('\n')

def prepare():
    assert not safe(BASELINE).exists() and not safe(MANIFEST).exists()
    items, authorities, binding = collect()
    value = {'created_UTC':utc(),'status':'candidate proof - unverified',
      'constructor':'/root/review_2021_reasoning_j15_r2',
      'whole_obligations':32,'claims':['R24A','R24B','R24C'],
      'necessary_direct_records':[fp(path) for path in DIRECT],
      'current_authority_declared_records_verified':authorities,
      'compact_parent_binding':binding,'effective_fresh_guard_summary':digest(items),
      'guard_reconstruction':'collect() rechecks exact bound current authorities and the immediate own parent only; no growing historical inventory copied',
      'root_supplied_NEW_mathematical_inference':False,
      'A_constructor_excluded_from_TWO_OTHER_WHOLE_audits':True,
      'NEW_2019_FL15_author_or_peer_access_inventory_hash':False,
      'no_mathematical_code_CAS_scan_test_or_replay':True,
      'no_Git_shared_old_cache_mutation':True,
      'requested':{'model':'gpt-6.1-sol','reasoning':'max','inherited':True},
      'independent_effective_setting_readback':None,
      'direct_quota':{'usedPercent':73,'observed_UTC':'2026-10-18 23:54:29 UTC',
        'resetsAt':1792874445,'windowDurationMins':10080,'ordinaryUsageAllowed':True,
        'TOTAL_ceiling':90,'integration_reserve':True,'automatic_later_window':False}}
    write_new(BASELINE,value)
    print(json.dumps({'baseline':fp(BASELINE),'guards':digest(items)},indent=2))

def validate():
    value = read(BASELINE)
    for row in value['necessary_direct_records']:
        check(row)
    items, authorities, binding = collect()
    assert authorities == value['current_authority_declared_records_verified']
    assert binding == value['compact_parent_binding']
    assert digest(items) == value['effective_fresh_guard_summary']
    labels = re.findall(r'^\| (O\d\d) \|',safe(PAYLOADS[0]).read_text(),re.M)
    assert labels == ['O%02d'%i for i in range(1,33)]
    return value

def freeze(confirmed):
    assert confirmed, 'FULL final ALL4 payload model readbacks required first'
    assert not safe(MANIFEST).exists()
    base = validate()
    value = {'frozen_UTC':utc(),'status':'candidate proof - unverified',
      'constructor':'/root/review_2021_reasoning_j15_r2','whole_obligations':32,
      'claims':['R24A','R24B','R24C'],'payload_count':4,'ENTIRE_files':5,
      'payloads':[fp(path) for path in PAYLOADS],
      'effective_fresh_guard_summary':base['effective_fresh_guard_summary'],
      'compact_parent_historical_summary_bound':base['compact_parent_binding']
          ['parent_historical_guard_summary_bound_NOT_reexpanded'],
      'FULL_final_ALL4_payload_model_readbacks_completed':True,
      'FULL_manifest_readback_then_SEPARATE_readonly_verify_REQUIRED':True,
      'TWO_OTHER_initially_blind_WHOLE_audits_required':True,
      'constructor_excluded_from_independent_review_count':True,
      'root_supplied_NEW_mathematical_inference':False,
      'NEW_2019_FL15_author_or_peer_access_inventory_hash':False,
      'actual_d_ge3_t_ge2_and_D8_r_subcases_excluded_CANDIDATE_ONLY':True,
      'remaining_actual_subcases_open':True,'annual_or_priority_claim':False,
      'requested':base['requested'],'independent_effective_setting_readback':None,
      'direct_quota':base['direct_quota'],
      'mathematical_program_CAS_scan_test_optimizer_old_source_author_replay':False,
      'Git_shared_old_cache_mutation':False}
    write_new(MANIFEST,value)
    print(json.dumps({'manifest':fp(MANIFEST),'frozen_UTC':value['frozen_UTC'],
                     'ENTIRE_files':5,'whole_obligations':32},indent=2))

def verify(expected):
    assert expected and fp(MANIFEST)['sha256'] == expected
    value = read(MANIFEST)
    for row in value['payloads']:
        check(row)
    base = validate()
    assert value['effective_fresh_guard_summary'] == base['effective_fresh_guard_summary']
    print(json.dumps({'verified_UTC':utc(),'result':'PASS','manifest':fp(MANIFEST),
      'ENTIRE_files':5,'whole_obligations':32,'guards':base['effective_fresh_guard_summary'],
      'writes':0,'mathematical_computation':False,'NEW_2019_FL15_access':False},indent=2))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode',choices=['prepare','freeze','verify'])
    parser.add_argument('--final-payload-readback-confirmed',action='store_true')
    parser.add_argument('--manifest-sha')
    args = parser.parse_args()
    if args.mode == 'prepare': prepare()
    elif args.mode == 'freeze': freeze(args.final_payload_readback_confirmed)
    else: verify(args.manifest_sha)
