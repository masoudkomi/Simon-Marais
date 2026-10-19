#!/usr/bin/env python3
"""NEW documentary-only IT12 whole2 helper. NO mathematical operations.

Only exact allowed inputs and OWN new prefix are touched. No source/author/
old executable is run; no corresponding NEW peer prefix is inventoried.
"""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
BASE = 'problems/2022-B4/reviews/reasoning-itinerary-return-r12-review-2-'
PAYLOADS = [BASE+'initial-v1.md', BASE+'sources-v1.json',
            BASE+'admin-v1.py', BASE+'baseline-v1.json']
MANIFEST = BASE+'manifest-v1.json'
AUTHOR = 'problems/2022-B4/notes/reasoning-itinerary-return-r12-'
AUTHOR_FREEZE = AUTHOR+'freeze-v1.json'
PARENT = 'problems/2017-B4/reviews/reasoning-joint-return-r15-review-1-'
PARENT_MANIFEST = PARENT+'manifest-v1.json'
EXPECTED = {
    AUTHOR+'candidate-v1.md': '50c4816c270fa6f3c1508ec93ffdcffedbe06514e74b0f097f037752e2c47ad7',
    AUTHOR+'sources-v1.json': 'e32fecb35d1c82b9fd1d8ba395bcb276782e721e58f390c8f59017bd1ecea551',
    AUTHOR+'admin-v1.py': 'c482248756ecf9a60ae39324264bba056128e1ec4f2fbb59bfeedbb4c0a8492e',
    AUTHOR+'baseline-v1.json': 'c1bae43b2be026b40928d7fade6da77d300d703e396c83ea6e9eb23da7ee3967',
    PARENT_MANIFEST: '2c41659612a4ef0370d4afa3957fa0767023135d9150bc80b9770403abe9d4df',
    'AGENTS.md': '28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff'
}

def now():
    return datetime.now(timezone.utc).isoformat()

def record(rel):
    data = (ROOT/rel).read_bytes()
    return {'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}

def check(item):
    assert record(item['path']) == item, 'Changed immutable input: '+item['path']

def load(rel):
    return json.loads((ROOT/rel).read_text())

def new_json(rel,value):
    with (ROOT/rel).open('x') as handle:
        handle.write(json.dumps(value,indent=2)+'\n')

def labels():
    text = (ROOT/PAYLOADS[0]).read_text()
    found = re.findall(r'^\|O12-(\d{2})\|',text,re.M)
    assert found == [f'{k:02}' for k in range(1,41)], 'Literal40 labels'
    return len(found)

def baseline():
    author = load(AUTHOR_FREEZE)
    original = load(AUTHOR+'baseline-v1.json')
    parent = load(PARENT_MANIFEST)
    occurrences = [record(AUTHOR_FREEZE)] + author['payloads']
    occurrences += original['immutable_inputs']
    occurrences += [record(PARENT_MANIFEST)] + parent['payload_records']
    unique = {}
    for item in occurrences:
        check(item)
        old = unique.setdefault(item['path'],item)
        assert old == item, 'Conflicting fingerprint: '+item['path']
    for rel,sha in EXPECTED.items():
        assert rel in unique and unique[rel]['sha256'] == sha, rel
    assert author['whole_obligations'] == 40 and author['ENTIRE_files'] == 5
    assert labels() == 40
    load(PAYLOADS[1])
    rows = [unique[key] for key in sorted(unique)]
    digest = hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    new_json(BASE+'baseline-v1.json',{
        'observed_UTC':now(),
        'status':'Necessary exact inputs; compact bound immediate OWN parent; no old historical expansion',
        'immutable_inputs':rows,
        'declared_occurrences_verified':len(occurrences),
        'unique_paths':len(rows),
        'guard_digest_sha256':digest,
        'author_ENTIRE_freeze':record(AUTHOR_FREEZE),
        'immediate_OWN_parent':record(PARENT_MANIFEST),
        'parent_historical_inventory_expanded':False,
        'author_old_R24_parent_released_and_accepted_before_necessary_checks':True,
        'NEW_corresponding_IT12_whole1_actual_inventory_content_hash_metadata_access':False,
        'NEW_corresponding_JC15_whole2_actual_inventory_content_hash_metadata_access':False,
        'mathematical_program_old_helper_replay':False
    })
    print(json.dumps({'baseline':record(BASE+'baseline-v1.json'),
                      'declared_occurrences':len(occurrences),'unique_paths':len(rows)}))

def freeze():
    base = load(BASE+'baseline-v1.json')
    for item in base['immutable_inputs']:
        check(item)
    for rel in PAYLOADS:
        assert (ROOT/rel).is_file(), rel
    load(PAYLOADS[1])
    n = labels()
    new_json(MANIFEST,{
        'frozen_UTC':now(),
        'status':'OTHER initially blind ENTIRE whole2; findings SEALED until explicit BOTH release',
        'reviewer':'/root/review_2017_coarsening_r1',
        'NEW_IT12_constructor':False,
        'old_D9_constructor_not_independently_recertified':True,
        'requested':{'model':'gpt-6.1-sol','reasoning':'max','inherited':True},
        'independent_effective_backend_readback':None,
        'ENTIRE_files':5,'payload_count':4,'whole_obligations':n,
        'payloads':[record(rel) for rel in PAYLOADS],
        'guard_occurrences_verified':base['declared_occurrences_verified'],
        'guard_unique_paths':base['unique_paths'],
        'guard_digest_sha256':base['guard_digest_sha256'],
        'immediate_OWN_parent':base['immediate_OWN_parent'],
        'FULL_final_ALL4_payload_MODEL_readbacks_completed_before_freeze':True,
        'FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_REQUIRED':True,
        'NEW_corresponding_peer_inventory_content_hash_metadata_access':False,
        'separate_JC15_peer_and_findings_embargo_preserved':True,
        'mathematical_program_CAS_scan_test_old_replay':False,
        'Git_shared_old_cache_mutation':False,
        'quota':{'usedPercent':77,'root_confirmation_UTC':'2026-10-19 01:15:01 UTC',
                 'resetsAt':1792874445,'windowDurationMins':10080,
                 'ordinaryUsageAllowed':True,'TOTAL_ceiling':90,
                 'review_integration_reserve':True,'automatic_later_window_spending':False}
    })
    print(json.dumps(record(MANIFEST)))

def verify():
    value = load(MANIFEST)
    for item in value['payloads']:
        check(item)
    base = load(BASE+'baseline-v1.json')
    for item in base['immutable_inputs']:
        check(item)
    assert value['whole_obligations'] == labels() == 40
    assert value['ENTIRE_files'] == len(value['payloads'])+1 == 5
    assert value['guard_digest_sha256'] == base['guard_digest_sha256']
    print(json.dumps({'SEPARATE_readonly_verify_UTC':now(),'documentary_status':'PASS',
        'ENTIRE_files':5,'literal_obligations':40,
        'guard_occurrences':base['declared_occurrences_verified'],
        'guard_unique_paths':base['unique_paths'],
        'manifest':record(MANIFEST),'mathematical_verification_claimed':False}))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode',choices=['baseline','freeze','verify'])
    args = parser.parse_args()
    {'baseline':baseline,'freeze':freeze,'verify':verify}[args.mode]()
