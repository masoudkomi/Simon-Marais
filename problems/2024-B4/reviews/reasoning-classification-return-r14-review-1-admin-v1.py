#!/usr/bin/env python3
"""NEW CL14 review1 documentary guard helper. NO mathematical computation.
Only exact literal paths, byte/SHA/JSON/48-label checks; no old helper execution,
peer review listing or mathematical certificate. Only this NEW prefix is written.
"""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PFX = 'problems/2024-B4/reviews/reasoning-classification-return-r14-review-1-'
AUTH = 'problems/2024-B4/notes/reasoning-classification-return-r14-'
OWN = 'problems/2022-B4/notes/reasoning-itinerary-return-r12-'
PAYLOADS = [PFX+'initial-v1.md',PFX+'sources-v1.json',PFX+'admin-v1.py',PFX+'baseline-v1.json']
BASELINE = PFX+'baseline-v1.json'
MANIFEST = PFX+'manifest-v1.json'
STEMS = ['reasoning-frobenius-return-r10','reasoning-frobenius-return-r11',
         'coordinator-tensor-return-r12','coordinator-tensor-family-return-r13']
EXPECTED = {
 AUTH+'freeze-v1.json': '89a6e276fe28ba0bc2f1a5ffe94636353efc6c457f613dbb1f5767c4dd683d73',
 AUTH+'candidate-v1.md': '9f6041dcfda7e87d5b7c4c0c73a2e757bc0d1413c3c45d1e4683f7cc69dc8d29',
 OWN+'freeze-v1.json': '32927019eee4697bfed786bb9713f8d7af90359db121d75b5a16922cb336fceb'
}

def now():
    return datetime.now(timezone.utc).isoformat()

def fp(p):
    b=(ROOT/p).read_bytes()
    return {'path':p,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}

def read(p):
    return json.loads((ROOT/p).read_text())

def check(row):
    actual=fp(row['path'])
    assert actual=={k:row[k] for k in ('path','bytes','sha256')},row['path']
    return actual

def summary(rows):
    dedup={}
    for row in rows:
        if row['path'] in dedup:
            assert dedup[row['path']]==row,row['path']
        dedup[row['path']]=row
    out=[dedup[k] for k in sorted(dedup)]
    raw=json.dumps(out,sort_keys=True,separators=(',',':')).encode()
    return out,{'occurrences':len(rows),'unique_paths':len(out),
                'canonical_deduplicated_sha256':hashlib.sha256(raw).hexdigest()}

def write_new(p,value):
    assert p.startswith(PFX)
    with (ROOT/p).open('x') as f:
        json.dump(value,f,indent=2)
        f.write('\n')

def labels():
    text=(ROOT/PAYLOADS[0]).read_text()
    assert re.findall(r'^\|R1-O(\d{2})\|CL14-O\d{2}\|',text,re.M)==[f'{j:02}' for j in range(1,49)]
    author=(ROOT/(AUTH+'candidate-v1.md')).read_text()
    assert re.findall(r'^\| (CL14-O\d{2}) \|',author,re.M)==[f'CL14-O{j:02}' for j in range(1,49)]
    read(PAYLOADS[1])

def baseline():
    author=read(AUTH+'freeze-v1.json')
    rows=[fp(AUTH+'freeze-v1.json')]
    assert author['ENTIRE_files']==5 and author['ALL_obligations']==48
    rows.extend(check(r) for r in author['payload_records'])
    historical=read(AUTH+'baseline-v1.json')
    mutable=[]
    for row in historical['integrity']['necessary_records_verified']:
        if row['path']=='problems/2024-B4/research.md':
            mutable.append({'historical_author_observation':row,'current_observation':None,
                            'immutable_proof_guard':False,'current_contents_and_hash_not_accessed_for_peer_blindness':True})
        else:
            rows.append(check(row))
    current=[]
    for stem in STEMS:
        md='problems/2024-B4/reviews/'+stem+'-acceptance.md'
        js='problems/2024-B4/reviews/'+stem+'-acceptance.json'
        authority=read(js)
        assert authority['status']=='proved, independently reviewed scoped partial result'
        body=check(authority['accepted_copy'])
        rows.extend([body,fp(md),fp(js)])
        current.append({'body':body,'authority_md':fp(md),'authority_json':fp(js),
                        'FULL_body_and_EACH_authority_read':True,
                        'historical_authority_inventories_NOT_expanded':True})
    own=read(OWN+'freeze-v1.json')
    rows.append(fp(OWN+'freeze-v1.json'))
    rows.extend(check(r) for r in own['payloads'])
    for rel,sha in EXPECTED.items():
        assert fp(rel)['sha256']==sha,rel
    guards,totals=summary(rows)
    value={'created_UTC':now(),'status':'Initially blind WHOLE1; findings sealed',
        'author_packet':fp(AUTH+'freeze-v1.json'),'ALL_obligations':48,
        'necessary_immutable_guards':guards,'guard_summary':totals,
        'author_declared_guard_summary_bound_not_recursively_expanded':historical['integrity']['guard_summary'],
        'current_accepted_interfaces':current,'mutable_observations_NOT_immutable_guards':mutable,
        'immediate_own_parent':fp(OWN+'freeze-v1.json'),
        'new_corresponding_peer_findings_files_actual_inventory_hash_metadata_access':False,
        'requested':{'model':'gpt-6.1-sol','reasoning':'max','inherited':True},
        'independent_effective_backend_readback':None,
        'quota':{'usedPercent':76,'observed_UTC':'2026-10-19 00:50:21 UTC',
                 'resetsAt':1792874445,'windowDurationMins':10080,'ordinaryUsageAllowed':True,
                 'TOTAL_ceiling':90,'reserve':True,
                 'automatic_later_window_spending':False},
        'mathematical_program_CAS_scan_test_old_author_source_helper_replay':False,
        'Git_shared_old_cache_mutation':False}
    labels()
    write_new(BASELINE,value)
    print(json.dumps({'baseline':fp(BASELINE),'guard_summary':totals}))

def freeze(confirmed):
    assert confirmed,'Full final payload MODEL readbacks required'
    base=read(BASELINE)
    for row in base['necessary_immutable_guards']:
        check(row)
    labels()
    value={'frozen_UTC':now(),'status':'OTHER initially blind WHOLE1; findings SEALED until explicit BOTH',
        'reviewer':'/root/review_2022_complexity_r2','NEW_constructor':'/root/review_2017_coarsening_r1',
        'reviewer_not_NEW_constructor':True,'ENTIRE_files':5,'payload_count':4,'ALL_obligations':48,
        'author_packet':base['author_packet'],'payloads':[fp(p) for p in PAYLOADS],
        'guard_summary':base['guard_summary'],'immediate_own_parent':base['immediate_own_parent'],
        'FULL_final_ALL4_payload_MODEL_readbacks_completed':True,
        'FULL_manifest_MODEL_readback_then_SEPARATE_readonly_verify_REQUIRED':True,
        'new_corresponding_peer_findings_files_actual_inventory_hash_metadata_access':False,
        'explicit_BOTH_release_required':True,'requested':base['requested'],
        'independent_effective_backend_readback':None,'quota':base['quota'],
        'mathematical_program_CAS_scan_test_old_replay':False,'Git_shared_old_cache_mutation':False}
    write_new(MANIFEST,value)
    print(json.dumps({'manifest':fp(MANIFEST),'frozen_UTC':value['frozen_UTC']}))

def verify():
    value=read(MANIFEST)
    for row in value['payloads']:
        check(row)
    base=read(BASELINE)
    for row in base['necessary_immutable_guards']:
        check(row)
    assert value['guard_summary']==base['guard_summary']
    labels()
    assert len(value['payloads'])+1==value['ENTIRE_files']==5
    print(json.dumps({'SEPARATE_readonly_verify_UTC':now(),'documentary_status':'PASS',
        'ENTIRE_files':5,'literal_obligations':48,'guard_summary':base['guard_summary'],
        'manifest':fp(MANIFEST),'writes':0,'mathematical_verification_claimed':False}))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode',choices=['baseline','freeze','verify'])
    parser.add_argument('--final-payload-readback-confirmed',action='store_true')
    args=parser.parse_args()
    if args.mode=='baseline': baseline()
    elif args.mode=='freeze': freeze(args.final_payload_readback_confirmed)
    else: verify()
