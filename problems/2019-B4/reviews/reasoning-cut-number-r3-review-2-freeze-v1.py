"""Independent administrative checks only; no mathematics or author rerun."""
from pathlib import Path
import datetime as dt
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[3]
P='problems/2019-B4/reviews/reasoning-cut-number-r3-review-2-'
T='problems/2019-B4/notes/reasoning-cut-number-r3-'
PARENT='problems/2022-B4/notes/reasoning-fiber-return-r5-freeze-v1.json'

def stamp(): return dt.datetime.now(dt.timezone.utc).isoformat()
def read(path): return json.loads((ROOT/path).read_text())
def rec(path):
    data=(ROOT/path).read_bytes()
    return {'path':path,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
def check(row):
    actual=rec(row['path'])
    assert actual=={k:row[k] for k in ('path','bytes','sha256')},(row,actual)
    return actual
def out(path,obj):
    assert path.startswith(P)
    with (ROOT/path).open('x',encoding='utf-8') as f:
        json.dump(obj,f,indent=2,ensure_ascii=False);f.write('\n')
def rows(obj):
    result=[]
    if isinstance(obj,dict):
        if all(k in obj for k in ('path','bytes','sha256')):
            result.append({k:obj[k] for k in ('path','bytes','sha256')})
        for value in obj.values(): result.extend(rows(value))
    elif isinstance(obj,list):
        for value in obj: result.extend(rows(value))
    return result
def canonical(records):
    unique={}
    for row in records:
        assert row['path'] not in unique or unique[row['path']]==row
        unique[row['path']]=row
    result=[unique[k] for k in sorted(unique)]
    digest=hashlib.sha256(json.dumps(result,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return result,digest
def brief(records):
    unique,digest=canonical(records)
    return {'fingerprint_occurrences_verified':len(records),
            'deduplicated_paths_verified':len(unique),
            'canonical_deduplicated_record_summary_sha256':digest}

main={'path':T+'candidate-v1.md','bytes':20668,
      'sha256':'70bd911506828e64f101028125594871a3e0325fe861deb99e4d9651991f6388'}
freeze={'path':T+'freeze-v1.json','bytes':5393,
        'sha256':'4a172e842aabf71d774ee5c8cfca458135e571ce7328c98be0eee1b3d0279089'}
parent_id={'path':PARENT,'bytes':2791,
           'sha256':'22283a8f95e7a2a489596a418b1dce4d9ab3f619296309b0ed33863fbd75c2ca'}
for row in [main,freeze,parent_id]: check(row)
constructor=read(freeze['path']);ab=read(T+'baseline-v1.json');parent=read(PARENT)
assert len(constructor['artifacts'])==10 and len(parent['artifacts'])==10
assert constructor['all_author_obligations']==48
initial=['initial-v1.md','ledger-v1.md','issues-v1.md','sources-v1.md',
         'worklog-v1.md','freeze-v1.py']
actual={str(x.relative_to(ROOT)) for x in (ROOT/'problems/2019-B4/reviews').glob('reasoning-cut-number-r3-review-2-*')}
assert actual=={P+s for s in initial},actual
for path in [P+'ledger-v1.md',T+'obligations-v1.md']:
    labels=re.findall(r'^\| (CN-\d{2}) \|',(ROOT/path).read_text(),re.M)
    assert labels==['CN-'+str(i).zfill(2) for i in range(1,49)]

author_parent=read(ab['own_immutable_immediate_parent']['manifest']['path'])
author_current=list(ab['direct_inputs'])+rows(author_parent)
accepted=[];authority_md=[]
for entry in ab['accepted_inputs']:
    authority=entry['authority'];check(authority)
    doc=read(authority['path'])
    assert doc['unresolved_substantive_issues']==0 and doc['repair_required'] is False
    assert doc['accepted_copy']==entry['accepted_body']
    check(doc['accepted_copy']);check(doc['candidate'])
    assert (ROOT/doc['accepted_copy']['path']).read_bytes().endswith((ROOT/doc['candidate']['path']).read_bytes())
    md=authority['path'][:-5]+'.md';authority_md.append(rec(md))
    declared=rows(doc)
    for row in declared: check(row)
    assert brief(declared)==entry['declared_current_fingerprints']
    author_current.extend(declared)
    accepted.append({'authority':authority,'accepted_body':entry['accepted_body'],
                     'candidate_suffix_exact':True,'current_declared_summary':brief(declared)})
assert len(accepted)==6
for row in author_current: check(row)
assert brief(author_current)==ab['current_existing_summary']
assert brief(author_current+constructor['artifacts'])==constructor['current_inputs_and_payloads_summary']
assert brief(rows(author_parent))==ab['own_immutable_immediate_parent']['manifest_declared_records']

declared=[freeze]+constructor['artifacts']+ab['direct_inputs']+[parent_id]+parent['artifacts']+authority_md
for row in declared: check(row)
protected,protected_hash=canonical(declared)
out(P+'baseline-v1.json',{
 'created_utc':stamp(),'purpose':'Compact independent administrative preservation; not mathematical evidence',
 'assigned_prefix_confirmed_unused_before_first_write':True,
 'target_main':main,'target_freeze':freeze,
 'protected_fingerprint_occurrences':len(declared),'protected_unique_paths':len(protected),
 'canonical_protected_summary_sha256':protected_hash,'protected':protected,
 'all_six_complete_accepted_bodies_MD_JSON_authorities_read_and_exact':True,'accepted_inputs':accepted,
 'independently_reconstructed_author_current_existing_summary':brief(author_current),
 'independently_reconstructed_author_current_and_payload_summary':brief(author_current+constructor['artifacts']),
 'compact_immutable_parents':[
    {'identity':freeze,'declared_summary':brief(rows(constructor)),
     'historical_inventory_not_recopied_or_recursively_reverified':True},
    {'identity':parent_id,'declared_summary':brief(rows(parent)),
     'historical_inventory_not_recopied_or_recursively_reverified':True}],
 'no_corresponding_NEW_root_CN_R1_finding_file_hash_metadata_accessed':True,
 'no_Git_old_shared_cache_mutation':True})

out(P+'metadata-v1.json',{
 'created_utc':stamp(),'status':'ENTIRE initially blind OTHER WHOLE CN R2; not promotion',
 'reviewer':'/root/review_2017_coarsening_r1','NEW_constructor_A_excluded':True,
 'reviewer_NEW_CN_construction_contribution':False,'whole_obligations':48,
 'older_linear_output_authorship_CCL_AF_finite_bound_review_roles_disclosed':True,
 'all48_hand_reconstructed_no_mathematical_program':True,
 'no_corresponding_NEW_root_CN_R1_findings_files_hashes_metadata_accessed':True,
 'identity_only_completion_until_explicit_BOTH_entire_initial_confirmation':True,
 'no_Git_old_shared_cache_write_spawn_contact_charge_bypass':True,
 'no_math_scan_CAS_source_algorithm_certificate_or_author_rerun':True,
 'pending_tool_approval_job_or_stall':False,
 'requested_settings':{'model':'gpt-6.1-sol','reasoning':'max','inherited':True},
 'verified_effective_settings':None,
 'telemetry':{'latest_parent_TOTAL_percent':26,'latest_parent_utc':'2026-10-18 10:40:59 UTC',
              'reset_unix':1792874445,'human_authorized_current_window':True,
              'ceiling_TOTAL_percent':90,'integration_reserve':True,
              'automatic_later_window_spending':False},
 'target_main':main,'target_freeze':freeze,'immediate_own_parent':parent_id,
 'compact_baseline':rec(P+'baseline-v1.json')})

for row in author_current+protected: check(row)
out(P+'input-validation-v1.json',{
 'checked_utc':stamp(),'administrative_only_not_mathematical_proof':True,
 'all_eleven_author_files_exact':True,'given_target_main_and_freeze_exact':True,
 'all_six_accepted_MD_JSON_body_authorities_and_candidate_suffixes_exact':True,
 'author_current_existing_summary':brief(author_current),
 'author_current_and_payload_summary':brief(author_current+constructor['artifacts']),
 'protected_fingerprint_occurrences':len(declared),'protected_unique_paths':len(protected),
 'canonical_protected_summary_sha256':protected_hash,
 'own_parent_and_all_ten_payloads_exact':True,
 'author_and_review_ALL48_labels_exact_ordered_once':True,
 'no_corresponding_NEW_root_CN_R1_material_accessed':True,
 'mathematical_executables_run':0,'errors':[]})
payloads=[rec(P+s) for s in initial+['baseline-v1.json','metadata-v1.json','input-validation-v1.json']]
for row in author_current+protected+payloads: check(row)
out(P+'manifest-v1.json',{
 'frozen_utc':stamp(),'status':'ENTIRE initially blind OTHER WHOLE CN R2 frozen; not promotion',
 'whole_obligations':48,'review_file_count':10,
 'ENTIRE_report_ALL48_ledger_issues_sources_log_code_ALL_metadata_frozen':True,
 'no_corresponding_NEW_root_CN_R1_findings_files_hashes_metadata_accessed':True,
 'identity_only_completion_until_explicit_BOTH_entire_confirmation':True,
 'target_main':main,'target_freeze':freeze,'immediate_own_parent':parent_id,'artifacts':payloads})
print(json.dumps({'manifest':rec(P+'manifest-v1.json'),'initial':rec(P+'initial-v1.md'),
                 'all48':True,'files':10,'protected_occurrences':len(declared),
                 'protected_unique_paths':len(protected),'author_current':brief(author_current)},indent=2))
