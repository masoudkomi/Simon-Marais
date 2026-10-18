#!/usr/bin/env python3
"""NEW R8 whole2 metadata only: no mathematics or old-script execution."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
PRE = 'problems/2024-B4/reviews/reasoning-cofactor-return-r8-review-2-'
AUTHOR = 'problems/2024-B4/notes/reasoning-cofactor-return-r8-'
PARENT = 'problems/2021-B4/reviews/reasoning-center-return-r19-review-2-v1.1-manifest.json'
PAYLOADS = ['report.md','ledger.md','issues.md','sources.md','sources.json','worklog.md','metadata.py','baseline.json','input-validation.json']
EXPECTED = {
    AUTHOR+'candidate-v1.md':(15501,'044343181cc87099291f327728fc07cbd1d4e97c59558fcb88b3237f6511eaea'),
    AUTHOR+'freeze-v1.json':(3554,'05075573ae2f40c214473d309de4c9490dbe0c404e60c8f1ddde5b9e2d79dbe3'),
    PARENT:(5133,'d1cfbb317ca09548149ed1025862fd0ee951d68d9015dcd76758a39d83a33d34'),
}
ACCEPTED = [
    ('structural-acceptance','reviewed-structural-v1.1.md',17079,'082dc054ce2cdaea80eee009f4c97c877c6968afb54b5a8f3141b7354031dd3f'),
    ('reasoning-cofactor-return-r6-acceptance','reviewed-reasoning-cofactor-return-r6-v1.1.md',20658,'fb988a13187b5765619532ad14077ae2f32a948e04704252e3d8981e10d65d98'),
    ('reasoning-cofactor-return-r7-acceptance','reviewed-reasoning-cofactor-return-r7-v1.1.md',22608,'b8e2cc3a37cf8c80c724c0d26f6768261e5d339fee073351e8b4c9b56b94cf72'),
]

def now():
    return datetime.now(timezone.utc).isoformat()

def path(p):
    assert not Path(p).is_absolute() and '..' not in Path(p).parts
    assert not p.startswith('problems/2024-B4/reviews/reasoning-cofactor-return-r8-review-1-'), 'NEW root R8 peer forbidden'
    assert not (p.startswith('problems/2021-B4/reviews/reasoning-center-return-r19-review-1-') and 'v1.1' in p)
    assert not p.startswith('problems/2021-B4/reviews/reasoning-center-return-r19-review-3-')
    assert not p.startswith('.git/')
    if p.startswith('.cache/'):
        assert p.startswith('.cache/literature/deep-literature-r2/2024-mcguire-thesis-1995')
    return ROOT/p

def raw(p):
    return path(p).read_bytes()

def load(p):
    return json.loads(raw(p))

def fp(p):
    data=raw(p)
    return {'path':p,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}

def match(r):
    actual=fp(r['path'])
    assert actual == {k:r[k] for k in ('path','bytes','sha256')},r['path']
    return actual

def write(suffix,obj):
    p=PRE+suffix
    assert not path(p).exists(), 'Exclusive NEW writes only: '+p
    with path(p).open('x',encoding='utf-8') as f:
        json.dump(obj,f,indent=2,ensure_ascii=False)
        f.write('\n')

def labels(text):
    return re.findall(r'^\|\s*(R8-\d{2})\s*\|',text,re.M)

def guard():
    rows=[]
    for p,(n,h) in EXPECTED.items():
        rows.append(match({'path':p,'bytes':n,'sha256':h}))
    author=load(AUTHOR+'freeze-v1.json')
    assert author['whole_obligations']==48 and author['ENTIRE_files']==13
    for r in author['artifacts']:
        assert r['path'].startswith(AUTHOR)
        rows.append(match(r))
    declared=load(AUTHOR+'baseline-v1.json')
    for r in declared['direct_immutable_guard_bindings']:
        rows.append(match(r))
    parent=load(PARENT)
    for r in parent['payloads']:
        assert r['path'].startswith('problems/2021-B4/reviews/reasoning-center-return-r19-review-2-v1.1-')
        rows.append(match(r))
    inputs=[]
    for stem,bodyname,n,h in ACCEPTED:
        p='problems/2024-B4/proofs/'+bodyname
        body=match({'path':p,'bytes':n,'sha256':h})
        rows.append(body)
        js='problems/2024-B4/reviews/'+stem+'.json'
        md='problems/2024-B4/reviews/'+stem+'.md'
        authority=load(js)
        rows.extend([fp(md),fp(js)])
        original=match(authority['candidate'])
        rows.append(original)
        if stem=='structural-acceptance':
            original_text=raw(original['path']).decode()
            before='## 3. An elementary lemma on point-free binary cubics'
            after='## 3. An elementary lemma on point-free ternary cubics'
            assert original_text.count(before)==1
            assert raw(p).endswith(original_text.replace(before,after).encode())
            assert authority['remaining_substantive_objections']==0
            adjustment='one accepted editorial heading binary->ternary; no mathematical change'
        else:
            assert raw(p).endswith(raw(original['path']))
            assert authority['unresolved_substantive_issues']==0
            adjustment='byte-identical frozen candidate suffix'
        inputs.append({'body':body,'authority_md':fp(md),'authority_json':fp(js),
            'original_candidate':original,'accepted_identity_verified':True,'exact_adjustment':adjustment,
            'fresh_complete_body_and_current_MDJSON_model_read':True,
            'use':'comparison only, no APN import' if 'r7-' in stem else 'operative accepted premise'})
    expected=[f'R8-{i:02d}' for i in range(1,49)]
    assert labels(raw(AUTHOR+'obligations-v1.md').decode())==expected
    assert labels(raw(AUTHOR+'constructor-checks-v1.md').decode())==expected
    assert labels(raw(PRE+'ledger.md').decode())==expected
    unique={}
    for r in rows:
        previous=unique.setdefault(r['path'],r)
        assert previous==r
    ordered=[unique[k] for k in sorted(unique)]
    return {'fingerprint_occurrences':len(rows),'unique_paths':len(ordered),
        'canonical_sha256':hashlib.sha256(json.dumps(ordered,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
        'necessary_records':ordered,'accepted_inputs':inputs,
        'author_ENTIRE13_fingerprints_verified':True,'author_baseline_direct30_verified_without_recursive_history':True,
        'own_immediate_parent_payloads_verified':9,'own_older_paths_bound_transitively':834,
        'ALL48_author_obligation_constructor_and_separate_reviewer_labels_match':True,
        'accepted_body_identities_verified':3,'mathematical_assertions_evaluated_by_code':False}

def compact(data):
    return {k:data[k] for k in ('fingerprint_occurrences','unique_paths','canonical_sha256',
        'author_ENTIRE13_fingerprints_verified','author_baseline_direct30_verified_without_recursive_history',
        'own_immediate_parent_payloads_verified','own_older_paths_bound_transitively',
        'ALL48_author_obligation_constructor_and_separate_reviewer_labels_match','accepted_body_identities_verified',
        'mathematical_assertions_evaluated_by_code')}

mode=sys.argv[1] if len(sys.argv)==2 else ''
if mode=='prepare':
    data=guard()
    write('baseline.json',{'created_at_utc':now(),'status':'ENTIRE initially blind WHOLE2 necessary integrity only',
        'author_main':fp(AUTHOR+'candidate-v1.md'),'author_freeze':fp(AUTHOR+'freeze-v1.json'),
        'immediate_own_parent':fp(PARENT),'nested_historical_inventory_replayed':False,
        'no_corresponding_NEW_root_R8_filenames_findings_files_hashes_or_metadata_accessed':True,**data})
    write('sources.json',{'date_utc':'2026-10-18','reviewer':'/root/review_2022_complexity_r2',
        'requested':{'model':'gpt-6.1-sol','reasoning':'max','inherited':True},'independent_effective_readback':None,
        'C_sole_NEW_constructor_excluded':True,'reviewer_NEW_R8_contribution':False,
        'older_roles':'Older structural/sector3/GK/NJ/CS/NF/three-bit/cofactor reviewer; not fresh old self-recertification',
        'ALL13_author_files_FULL_read_including_code_as_text':True,'author_code_executed':False,
        'ALL48_separate_hand_dispositions':True,'accepted_complete_current_bodies_MDJSON':data['accepted_inputs'],
        'primary':[
            {'url':'https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf',
             'scope':'B4 setup/(b),57-74; no preliminary proof','binary_sha256':None},
            {'url':'https://thesis.caltech.edu/4053/01/McGuire_gm_1995.pdf','record':'https://thesis.caltech.edu/4053/',
             'scope':'ENTIRE existing images21-31,printed16-26,visual read; local lemmas and complete SUPPLIED Theorems6/7 proofs',
             'literal_limit':'q4 proof invokes JW atn21; original JW proof, journal and Ferard2017 bodies unread; no priority inference',
             'preexisting_binary':fp('.cache/literature/deep-literature-r2/2024-mcguire-thesis-1995.pdf'),
             'new_download_or_cache_mutation':False,'whole_thesis_or_earlier_PropositionA_proof_read_claimed':False},
            {'url':'https://math.stanford.edu/~conrad/145Page/handouts/algcurves.pdf',
             'scope':'COMPLETE operative Section3.3 properties/theorem/proof2419-2624;5.3 Bezout statement/entire proof3829-3924;AppendixA7557-7597; small gap2518-2520 filled',
             'hypotheses':'algebraically closed field; proper intersection, no common component; coprime tangents for local equality; reducible products and characteristic2 allowed',
             'binary_sha256':None,'whole129page_or_foundational_dependency_audit':False}],
        'R7_APN_R4_R5_or_unread_JW_Ferard_theorem_imported':False,
        'all_new_geometry_arithmetic_and_uniform_inequalities_hand_reconstructed':True,
        'no_new_binary_download_cache_write_charge_contact_bypass_or_third_party_upload':True,
        'no_NEW_root_R8_filename_content_finding_hash_metadata_access':True,
        'no_mathematical_program_CAS_scan_test_optimizer_or_author_source_old_replay':True,
        'annual_converse_priority_or_external_validation_claim':False})
    write('input-validation.json',{'checked_at_utc':now(),'result':'PASS metadata only',**compact(data),
        'no_corresponding_NEW_root_R8_peer_access':True,'baseline':fp(PRE+'baseline.json')})
    print(json.dumps({'mode':mode,'result':'PASS',**compact(data)},indent=2))
elif mode in ('freeze','verify'):
    data=guard()
    base=load(PRE+'baseline.json')
    assert data['necessary_records']==base['necessary_records']
    assert compact(data)=={k:load(PRE+'input-validation.json')[k] for k in compact(data)}
    for suffix in PAYLOADS:
        assert path(PRE+suffix).is_file()
    if mode=='freeze':
        write('manifest.json',{'frozen_at_utc':now(),
            'status':'ENTIRE initially blind OTHER WHOLE2 initial; findings EMBARGOED; not promotion',
            'reviewer':'/root/review_2022_complexity_r2','C_sole_NEW_constructor_excluded':True,
            'reviewer_NEW_R8_construction_contribution':False,'older_roles_disclosed_not_self_recertification':True,
            'requested':{'model':'gpt-6.1-sol','reasoning':'max','inherited':True},'independent_effective_readback':None,
            'whole_obligations':48,'separate_hand_dispositions':48,'author_ENTIRE_files_FULLread':13,
            'substantive_defects_or_required_repairs_found':0,'closed_notes':8,
            'ENTIRE_review_files_including_manifest':10,'immediate_own_parent':fp(PARENT),
            'older_own_paths_bound_transitively':834,'older_plus_new_own_paths_bound_transitively':844,
            'necessary_guard_summary':compact(data),'no_corresponding_NEW_root_R8_filenames_contents_findings_hashes_metadata_accessed':True,
            'FULL_final_model_readback_ALL9_payloads_code_generated_metadata_attested':True,
            'FULL_manifest_model_readback_then_SEPARATE_readonly_verification_required':True,
            'findings_EMBARGOED_and_identity_only_until_explicit_BOTH_confirmation':True,
            'no_mathematical_program_CAS_scan_test_optimizer_or_author_source_old_replay':True,
            'no_Git_shared_old_cache_mutation_spawn_charge_contact_bypass':True,
            'authoritative_weekly_telemetry':{'at_utc':'2026-10-18 15:01:05 UTC','method':'own same-awaited clock/get_usage_limits',
                'TOTAL_used_percent':45,'window_minutes':10080,'resetsAt':1792874445,'ordinary_usage_allowed':True,
                'legacy_by_limit_agree':True,'account_label':'029a8928...1334ac3a','TOTAL_ceiling_percent':90,
                'integration_reserve':True,'human_authorized_current_window_only':True,'automatic_later_window_spending':False},
            'payloads':[fp(PRE+s) for s in PAYLOADS]})
        print(json.dumps({'mode':mode,'result':'PASS','manifest':fp(PRE+'manifest.json'),**compact(data)},indent=2))
    else:
        frozen=load(PRE+'manifest.json')
        assert len(frozen['payloads'])==9 and frozen['whole_obligations']==48
        for rec in frozen['payloads']:
            match(rec)
        print(json.dumps({'mode':'SEPARATE read-only verification','at_utc':now(),'result':'PASS',
            'ENTIRE_files':10,'ALL_obligations':48,'manifest':fp(PRE+'manifest.json'),
            'report':fp(PRE+'report.md'),**compact(data)},indent=2))
else:
    raise SystemExit('Use prepare, freeze or verify; NEW metadata-only code')
