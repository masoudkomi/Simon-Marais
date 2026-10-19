#!/usr/bin/env python3
"""NEW JC15 review2 documentary fingerprint/label helper; NO math computations.
Only explicit necessary paths, no peer inventory/old helper/source execution.
Writes ONLY this NEW review2 baseline/manifest; verify is read-only.
"""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PFX='problems/2017-B4/reviews/reasoning-joint-return-r15-review-2-'
AUTHOR='problems/2017-B4/notes/reasoning-joint-return-r15-'
PARENT='problems/2024-B4/reviews/reasoning-classification-return-r14-review-1-'
PAYLOADS=[PFX+'initial-v1.md',PFX+'sources-v1.json',PFX+'admin-v1.py',PFX+'baseline-v1.json']
BASE=PFX+'baseline-v1.json'
MANIFEST=PFX+'manifest-v1.json'
STEMS=['reasoning-pressure-return-r11','reasoning-concentration-return-r12','reasoning-lower-return-r14']
EXPECTED={
 AUTHOR+'freeze-v1.json':'40c82ab0e7f7a9678a31f763fc7960c54e8963f5e226f0da185cdf5441a0c6ac',
 AUTHOR+'candidate-v1.md':'a17fb4f40f8f46be18ec0ac1a3631f1448a2d15570591417f7a9b6a9c24136bf',
 PARENT+'manifest-v1.json':'579811347bf12b72697b3eaeb3adb8a08b086f4d2aa7b4375bd3fa55c44f3eae'
}

def now():
    return datetime.now(timezone.utc).isoformat()

def fp(rel):
    assert not Path(rel).is_absolute() and '..' not in Path(rel).parts
    data=(ROOT/rel).read_bytes()
    return {'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}

def load(rel):
    return json.loads((ROOT/rel).read_text())

def check(row):
    got=fp(row['path'])
    assert got=={k:row[k] for k in ('path','bytes','sha256')},row['path']
    return got

def summarize(rows):
    unique={}
    for row in rows:
        if row['path'] in unique:
            assert unique[row['path']]==row,row['path']
        unique[row['path']]=row
    ordered=[unique[k] for k in sorted(unique)]
    raw=json.dumps(ordered,sort_keys=True,separators=(',',':')).encode()
    return ordered,{'occurrences':len(rows),'unique_paths':len(ordered),
                   'canonical_deduplicated_sha256':hashlib.sha256(raw).hexdigest()}

def write_new(rel,value):
    assert rel.startswith(PFX)
    with (ROOT/rel).open('x') as out:
        json.dump(value,out,indent=2)
        out.write('\n')

def labels():
    text=(ROOT/PAYLOADS[0]).read_text()
    assert re.findall(r'^\|R2-O(\d{2})\|JC15-\d{2}\|',text,re.M)==[f'{i:02}' for i in range(1,37)]
    original=(ROOT/(AUTHOR+'candidate-v1.md')).read_text()
    assert re.findall(r'^\| JC15-(\d{2}) \| CHECKED\.',original,re.M)==[f'{i:02}' for i in range(1,37)]
    load(PAYLOADS[1])

def baseline():
    author=load(AUTHOR+'freeze-v1.json')
    assert author['ENTIRE_files']==5 and author['whole_obligations']==36
    rows=[fp(AUTHOR+'freeze-v1.json')]+[check(x) for x in author['payloads']]
    old=load(AUTHOR+'baseline-v1.json')
    rows.extend(check(x) for x in old['necessary_direct_records'])
    current=[]
    for stem in STEMS:
        md='problems/2017-B4/reviews/'+stem+'-acceptance.md'
        js='problems/2017-B4/reviews/'+stem+'-acceptance.json'
        authority=load(js)
        assert authority['status']=='proved, independently reviewed scoped partial result'
        body=check(authority['accepted_copy'])
        rows.extend([body,fp(md),fp(js)])
        current.append({'body':body,'authority_md':fp(md),'authority_json':fp(js),
                        'FULL_body_and_EACH_authority_MODEL_read':True,
                        'historical_inventories_NOT_expanded':True})
    parent=load(PARENT+'manifest-v1.json')
    rows.append(fp(PARENT+'manifest-v1.json'))
    rows.extend(check(x) for x in parent['payloads'])
    for rel,sha in EXPECTED.items():
        assert fp(rel)['sha256']==sha,rel
    guards,summary=summarize(rows)
    labels()
    value={'created_UTC':now(),'status':'OTHER initially blind WHOLE2; findings SEALED',
        'ALL_obligations':36,'author_freeze':fp(AUTHOR+'freeze-v1.json'),
        'necessary_immutable_guards':guards,'guard_summary':summary,
        'current_accepted_interfaces':current,
        'author_historical_summary_bound_NOT_recursively_expanded':old['effective_fresh_guard_summary'],
        'author_compact_parent_outer_binding_NOT_opened':old['compact_own_parent'],
        'historical_mutable_map_observation_NOT_guard':old['mutable_current_research_map_observation_NOT_guard'],
        'current_mutable_map_contents_and_hash_NOT_accessed':True,
        'immediate_own_parent':fp(PARENT+'manifest-v1.json'),
        'own_parent_sealed_report_NOT_peer_material':True,
        'NEW_corresponding_peer_findings_files_actual_inventory_hash_metadata_access':False,
        'requested':{'model':'gpt-6.1-sol','reasoning':'max','inherited':True},
        'independent_effective_backend_readback':None,
        'quota':{'usedPercent':77,'observed_UTC':'2026-10-19 01:14:34 UTC',
            'resetsAt':1792874445,'windowDurationMins':10080,'ordinaryUsageAllowed':True,
            'TOTAL_ceiling':90,'integration_review_reserve':True,'automatic_later_window_spending':False},
        'mathematical_program_CAS_scan_test_old_source_author_helper_replay':False,
        'Git_shared_old_cache_mutation':False}
    write_new(BASE,value)
    print(json.dumps({'baseline':fp(BASE),'guard_summary':summary}))

def freeze(confirmed):
    assert confirmed,'FULL final MODEL payload readbacks required'
    base=load(BASE)
    for row in base['necessary_immutable_guards']:
        check(row)
    labels()
    value={'frozen_UTC':now(),'status':'OTHER initially blind WHOLE2; findings SEALED until explicit BOTH',
        'reviewer':'/root/review_2022_complexity_r2','NEW_constructor':'/root/review_2021_reasoning_j15_r2',
        'reviewer_not_NEW_constructor':True,'ENTIRE_files':5,'payload_count':4,'ALL_obligations':36,
        'author_freeze':base['author_freeze'],'payloads':[fp(p) for p in PAYLOADS],
        'guard_summary':base['guard_summary'],'immediate_own_parent':base['immediate_own_parent'],
        'FULL_final_ALL4_payload_MODEL_readbacks_completed':True,
        'FULL_manifest_MODEL_readback_then_SEPARATE_readonly_verify_REQUIRED':True,
        'NEW_corresponding_peer_findings_files_actual_inventory_hash_metadata_access':False,
        'explicit_BOTH_release_required':True,'requested':base['requested'],
        'independent_effective_backend_readback':None,'quota':base['quota'],
        'mathematical_program_CAS_scan_test_old_replay':False,'Git_shared_old_cache_mutation':False}
    write_new(MANIFEST,value)
    print(json.dumps({'manifest':fp(MANIFEST),'frozen_UTC':value['frozen_UTC']}))

def verify():
    value=load(MANIFEST)
    for row in value['payloads']:
        check(row)
    base=load(BASE)
    for row in base['necessary_immutable_guards']:
        check(row)
    assert value['guard_summary']==base['guard_summary']
    assert len(value['payloads'])+1==value['ENTIRE_files']==5
    labels()
    print(json.dumps({'SEPARATE_readonly_verify_UTC':now(),'documentary_status':'PASS',
        'ENTIRE_files':5,'literal_obligations':36,'guard_summary':base['guard_summary'],
        'manifest':fp(MANIFEST),'writes':0,'mathematical_verification_claimed':False}))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode',choices=['baseline','freeze','verify'])
    parser.add_argument('--final-payload-readback-confirmed',action='store_true')
    args=parser.parse_args()
    if args.mode=='baseline': baseline()
    elif args.mode=='freeze': freeze(args.final_payload_readback_confirmed)
    else: verify()
