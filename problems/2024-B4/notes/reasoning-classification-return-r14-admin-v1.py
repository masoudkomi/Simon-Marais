#!/usr/bin/env python3
"""CL14 documentary integrity ONLY: no mathematical computation or replay.
prepare creates NEW baseline. FULL final ALL4 payload MODEL readbacks must
precede freeze; FULL manifest MODEL readback precedes SEPARATE verify.
Only explicit current accepted input identities are followed. Historical
inventories remain bound by immutable outer metadata plus count/digest.
"""
import argparse
import datetime as dt
import hashlib
import json
import re
from pathlib import Path

ROOT=Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PFX='problems/2024-B4/notes/reasoning-classification-return-r14-'
BASE=PFX+'baseline-v1.json'
FREEZE=PFX+'freeze-v1.json'
PAYLOADS=[PFX+'candidate-v1.md',PFX+'sources-v1.json',PFX+'admin-v1.py',BASE]
PARENT='problems/2021-B4/reviews/reasoning-deep-return-r24-review-2-manifest-v1.json'
AUTH=[
('reasoning-frobenius-return-r10',27940,'ce9a3c9e00ce931716fe00d6ea0a605167ddf58a29779d459a62cbc9dd04d173'),
('reasoning-frobenius-return-r11',18332,'d585689283fe2dcd748c8c4385bdaf9faef5d66763b72e15ad4f213c76475d28'),
('coordinator-tensor-return-r12',29355,'48b6926a174202e447e04673f0507fc8e4708c7ee212fd3a68d6b90957a2845f'),
('coordinator-tensor-family-return-r13',24196,'d63364d6f874e52f0a1610d3d168213993034ff8d293b20259009072d779787b')]
DIRECT={
'AGENTS.md':(4707,'28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff'),
'problems/2024-B4/statement.md':(2470,'60244f7752634772adb434efbdb41a63fb02029dc3be4238f3718c6e5ec84e5f'),
'problems/2024-B4/research.md':(21963,'ebd9895b2a670b27d22c7b782a6744833bd7f296d4dac89eb0b5d664006f2cbf'),
PARENT:(2096,'ea9c59b120bb0a89b6b53f375c81296ac014ea96b23b4f037079d2916a22e328')}

def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()

def path(p):
    assert isinstance(p,str) and not p.startswith('/') and '..' not in Path(p).parts
    return ROOT/p

def fp(p):
    b=path(p).read_bytes()
    return {'path':p,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}

def read(p):
    return json.loads(path(p).read_text())

def check(row):
    got=fp(row['path'])
    assert got=={k:row[k] for k in ('path','bytes','sha256')},row['path']
    return got

def rows(value):
    if isinstance(value,dict):
        if all(k in value for k in ('path','bytes','sha256')):
            yield {k:value[k] for k in ('path','bytes','sha256')}
        for v in value.values():
            yield from rows(v)
    elif isinstance(value,list):
        for v in value:
            yield from rows(v)

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
    text=path(PAYLOADS[0]).read_text()
    assert re.findall(r'^\| (CL14-O\d\d) \|',text,re.M)==['CL14-O%02d'%i for i in range(1,49)]
    assert 'Candidate proof - unverified' in text
    read(PAYLOADS[1])

def collect():
    direct=[]
    for p,expected in DIRECT.items():
        got=fp(p)
        assert (got['bytes'],got['sha256'])==expected,p
        direct.append(got)
    authority=[]
    for stem,size,sha in AUTH:
        md='problems/2024-B4/reviews/'+stem+'-acceptance.md'
        js='problems/2024-B4/reviews/'+stem+'-acceptance.json'
        value=read(js)
        body=check(value['accepted_copy'])
        assert (body['bytes'],body['sha256'])==(size,sha)
        assert value['status']=='proved, independently reviewed scoped partial result'
        direct.extend([body,fp(md),fp(js)])
        authority.append({'authority':fp(js),
            'declared_records_NOT_recursively_opened':summary(list(rows(value))),
            'only_necessary_accepted_body_validated':True})
    parent=read(PARENT)
    parent_rows=[check(r) for r in parent['payload_records']]
    assert len(parent_rows)==4 and parent['WHOLE_obligations']==32
    direct.extend(parent_rows)
    return {'necessary_records_verified':direct,'guard_summary':summary(direct),
        'current_authority_outer_bindings':authority,
        'immediate_own_parent':fp(PARENT),'own_parent_payloads_verified':4,
        'own_parent_historical_summary_bound_NOT_expanded':parent['guard_summary'],
        'no_growing_historical_inventory_replayed':True}

def write_new(p,value):
    assert p.startswith(PFX)
    with path(p).open('x') as f:
        json.dump(value,f,indent=2)
        f.write('\n')

def prepare():
    labels()
    value={'created_utc':now(),'status':'candidate proof - unverified',
        'constructor':'/root/review_2017_coarsening_r1','ALL_obligations':48,
        'integrity':collect(),'two_OTHER_whole_audits_required':True,
        'constructor_excluded':True,'root_generic_target_not_NEW_inference':True,
        'old_roles_disclosed_not_self_recertification':True,
        'requested':{'model':'gpt-6.1-sol','reasoning':'max','inherited':True},
        'independently_verified_effective_setting':None,
        'quota':{'usedPercent':75,'windowDurationMins':10080,'resetsAt':1792874445,
            'ordinaryUsageAllowed':True,'TOTAL_ceiling':90,'integration_reserve':True,
            'automatic_later_window':False},
        'mathematical_code_CAS_scan_test_optimizer_old_source_author_replay':False,
        'documentary_code_only':True,'old_shared_Git_cache_mutation':False,
        'charge_contact_bypass_redistribution_spawn':False,
        'FULL_final_ALL4_MODEL_then_manifest_MODEL_then_SEPARATE_verify_required':True}
    write_new(BASE,value)
    print(json.dumps({'baseline':fp(BASE),'guards':value['integrity']['guard_summary']},indent=2))

def validate():
    labels()
    value=read(BASE)
    assert collect()==value['integrity']
    return value

def freeze(confirmed):
    assert confirmed,'FULL final ALL4 MODEL payload readbacks required'
    base=validate()
    value={'frozen_utc':now(),'status':'candidate proof - unverified',
        'constructor':'/root/review_2017_coarsening_r1','ENTIRE_files':5,'ALL_obligations':48,
        'payload_records':[fp(p) for p in PAYLOADS],
        'guard_summary':base['integrity']['guard_summary'],'immediate_own_parent':fp(PARENT),
        'TWO_OTHER_initially_blind_ENTIRE_whole_audits_required':True,
        'constructor_excluded':True,'root_NEW_mathematical_contribution':False,
        'FULL_final_MODEL_ALL4_payload_readbacks_completed':True,
        'FULL_manifest_MODEL_readback_then_SEPARATE_verify_REQUIRED':True,
        'mathematical_program_CAS_scan_test_old_replay':False,
        'old_shared_Git_cache_mutation':False}
    write_new(FREEZE,value)
    print(json.dumps({'freeze':fp(FREEZE),'frozen_utc':value['frozen_utc']},indent=2))

def verify(expected):
    assert expected and fp(FREEZE)['sha256']==expected
    value=read(FREEZE)
    for r in value['payload_records']:
        check(r)
    base=validate()
    assert value['guard_summary']==base['integrity']['guard_summary']
    print(json.dumps({'verified_utc':now(),'result':'PASS','ENTIRE_files':5,
        'ALL_obligations':48,'freeze':fp(FREEZE),'writes':0,
        'mathematical_computation':False},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode',choices=['prepare','freeze','verify'])
    parser.add_argument('--final-payload-readback-confirmed',action='store_true')
    parser.add_argument('--freeze-sha')
    args=parser.parse_args()
    if args.mode=='prepare': prepare()
    elif args.mode=='freeze': freeze(args.final_payload_readback_confirmed)
    else: verify(args.freeze_sha)
