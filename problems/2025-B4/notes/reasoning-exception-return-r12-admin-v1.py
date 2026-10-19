#!/usr/bin/env python3
"""NEW ET12 documentary bytes/SHA/JSON/labels ONLY; no mathematical execution.
Explicit exact guards only; no peer inventory, old helper or recursive ancestry.
Writes only this NEW namespace baseline/freeze. Verify is separate/read-only.
"""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PFX='problems/2025-B4/notes/reasoning-exception-return-r12-'
PARENT='problems/2017-B4/reviews/reasoning-joint-return-r15-review-2-manifest-v1.json'
BASE=PFX+'baseline-v1.json'
FREEZE=PFX+'freeze-v1.json'
PAYLOADS=[PFX+'candidate-v1.md',PFX+'sources-v1.json',PFX+'admin-v1.py',BASE]
INPUT_STEMS=['reasoning-compatible-return-r10','reasoning-global-return-r11']
EXPECTED={
 'AGENTS.md':'28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff',
 'problems/2025-B4/proofs/reviewed-reasoning-compatible-return-r10-v1.1.md':'dbbce8dcc26f1251e30c3ab939dd013062fe96bf98652fd06a2bb53bff527448',
 'problems/2025-B4/proofs/reviewed-reasoning-global-return-r11-v1.1.md':'6a72f0d8348fc39f6343a3381975f8fbc02bc001036bc88acbd32a93a51f1196',
 PARENT:'3a66ce5b0fe4bd29688fc85af114fb0e53eae596b7e75d8f179d85aa6e64c166'
}

def now(): return datetime.now(timezone.utc).isoformat()
def fp(rel):
    assert not Path(rel).is_absolute() and '..' not in Path(rel).parts
    data=(ROOT/rel).read_bytes()
    return {'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
def load(rel): return json.loads((ROOT/rel).read_text())
def check(row):
    got=fp(row['path'])
    assert got=={k:row[k] for k in ('path','bytes','sha256')},row['path']
    return got
def write_new(rel,value):
    assert rel.startswith(PFX)
    with (ROOT/rel).open('x') as out:
        json.dump(value,out,indent=2)
        out.write('\n')
def labels():
    text=(ROOT/PAYLOADS[0]).read_text()
    assert re.findall(r'^\| ET12-O(\d{2}) \|',text,re.M)==[f'{i:02}' for i in range(1,37)]
    load(PAYLOADS[1])
def summary(rows):
    unique={}
    for row in rows:
        if row['path'] in unique: assert unique[row['path']]==row
        unique[row['path']]=row
    ordered=[unique[k] for k in sorted(unique)]
    digest=hashlib.sha256(json.dumps(ordered,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return ordered,{'occurrences':len(rows),'unique_paths':len(ordered),'canonical_deduplicated_sha256':digest}

def baseline():
    rows=[fp('AGENTS.md'),fp('problems/2025-B4/statement.md')]
    interfaces=[]
    for stem in INPUT_STEMS:
        md='problems/2025-B4/reviews/'+stem+'-acceptance.md'
        js='problems/2025-B4/reviews/'+stem+'-acceptance.json'
        authority=load(js)
        assert authority['status']=='proved, independently reviewed scoped partial result'
        body=check(authority['accepted_copy'])
        item={'body':body,'authority_md':fp(md),'authority_json':fp(js),
              'FULL_body_and_EACH_current_MDJSON_MODEL_read':True,'old_histories_NOT_expanded':True}
        rows.extend([body,fp(md),fp(js)])
        interfaces.append(item)
    rows.append(fp('problems/2025-B4/notes/reasoning-global-return-r11-sources-v1.json'))
    parent=load(PARENT)
    rows.append(fp(PARENT))
    for rel,sha in EXPECTED.items(): assert fp(rel)['sha256']==sha,rel
    guards,counts=summary(rows)
    labels()
    value={'created_UTC':now(),'status':'candidate proof - unverified','ALL_obligations':36,
        'constructor':'/root/review_2022_complexity_r2','two_OTHER_whole_reviews_required':True,
        'necessary_immutable_guards':guards,'guard_summary':counts,'accepted_interfaces':interfaces,
        'immediate_own_parent_manifest':fp(PARENT),'parent_guard_summary_bound_NOT_expanded':parent['guard_summary'],
        'parent_full_payloads_not_reinventoried_or_rehashed':True,
        'mutable_research_map':{'path':'problems/2025-B4/research.md','FULL_read_as_dated_observation':True,
            'NOT_immutable_guard':True,'current_hash_not_needed':True,'routine_coordinator_updates_allowed':True},
        'primary_binary_hashes':None,'source_read_limits_recorded_in_main_and_sources':True,
        'requested':{'model':'gpt-6.1-sol','reasoning':'max','inherited':True},
        'independent_effective_backend_readback':None,
        'quota':{'usedPercent':79,'observed_UTC':'2026-10-19 01:59:46 UTC','resetsAt':1792874445,
            'windowDurationMins':10080,'ordinaryUsageAllowed':True,'legacy_by_limit_agree':True,
            'account_label':'...ac3a','TOTAL_ceiling':90,'integration_review_reserve':True,
            'automatic_later_window_spending':False},
        'NEW_R25_R26_peer_or_exploration_access':False,
        'mathematical_program_CAS_scan_test_old_source_author_helper_replay':False,
        'Git_shared_old_cache_mutation_spawn_charge_contact_bypass':False}
    write_new(BASE,value)
    print(json.dumps({'baseline':fp(BASE),'guard_summary':counts}))

def freeze(confirmed):
    assert confirmed,'FULL final payload MODEL readbacks required'
    base=load(BASE)
    for row in base['necessary_immutable_guards']: check(row)
    labels()
    value={'frozen_UTC':now(),'status':'candidate proof - unverified','constructor':base['constructor'],
        'ENTIRE_files':5,'payload_count':4,'ALL_obligations':36,'claims':['ET1','ET2','ET3'],
        'payloads':[fp(p) for p in PAYLOADS],'guard_summary':base['guard_summary'],
        'immediate_own_parent_manifest':base['immediate_own_parent_manifest'],
        'FULL_final_ALL4_payload_MODEL_readbacks_completed':True,
        'FULL_freeze_manifest_MODEL_readback_then_SEPARATE_readonly_verify_REQUIRED':True,
        'two_OTHER_initially_blind_ENTIRE_WHOLE_audits_and_coordinator_reconciliation_REQUIRED':True,
        'constructor_EXCLUDED_from_auditor_count':True,
        'NEW_R25_R26_peer_or_exploration_access':False,
        'requested':base['requested'],'independent_effective_backend_readback':None,'quota':base['quota'],
        'mathematical_program_CAS_scan_test_old_source_author_helper_replay':False,
        'Git_shared_old_cache_mutation_spawn_charge_contact_bypass':False}
    write_new(FREEZE,value)
    print(json.dumps({'freeze':fp(FREEZE),'frozen_UTC':value['frozen_UTC']}))

def verify():
    freeze=load(FREEZE)
    for row in freeze['payloads']: check(row)
    base=load(BASE)
    for row in base['necessary_immutable_guards']: check(row)
    assert freeze['guard_summary']==base['guard_summary']
    assert len(freeze['payloads'])+1==freeze['ENTIRE_files']==5
    labels()
    print(json.dumps({'SEPARATE_readonly_verify_UTC':now(),'documentary_status':'PASS',
        'ENTIRE_files':5,'literal_obligations':36,'guard_summary':base['guard_summary'],
        'freeze':fp(FREEZE),'writes':0,'mathematical_verification_claimed':False}))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode',choices=['baseline','freeze','verify'])
    parser.add_argument('--final-payload-readback-confirmed',action='store_true')
    args=parser.parse_args()
    if args.mode=='baseline': baseline()
    elif args.mode=='freeze': freeze(args.final_payload_readback_confirmed)
    else: verify()
