"""Administrative-only immutable-input, label and exclusive JSON checks."""
from pathlib import Path
import datetime as dt
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[3]
P='problems/2024-B4/reviews/cofactor-dominant-r4-review-2-'
T='problems/2024-B4/notes/cofactor-dominant-r4-'
PARENT='problems/2025-B4/reviews/reasoning-Runge-return-r3-review-2-manifest-v1.json'

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
    with (ROOT/path).open('x',encoding='utf-8') as f:
        json.dump(obj,f,indent=2,ensure_ascii=False); f.write('\n')
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

main={'path':T+'candidate-v1.md','bytes':14524,
      'sha256':'b6c454eba513c0ebb364f4b53393741c8737239c5b03c75fc2a0ac000871e365'}
freeze={'path':T+'freeze-v1.json','bytes':3054,
        'sha256':'1d0c4e90c0b75a2417539401d4350e13dd29c9d3030fc06074f4cff18358371b'}
parent_id={'path':PARENT,'bytes':2947,
           'sha256':'d44dfd099479ced064ecd3cf5b5bfee2db18271c3a2a70b4792875f67b23bbb7'}
for row in [main,freeze,parent_id]: check(row)
constructor=read(freeze['path']); cb=read(T+'baseline-v1.json'); parent=read(PARENT)
assert len(constructor['artifacts'])==10
assert len(cb['protected'])==12
assert len(parent['artifacts'])==9
initial=['initial-v1.md','ledger-v1.md','issues-v1.md','sources-v1.md','worklog-v1.md','freeze-v1.py']
actual={str(x.relative_to(ROOT)) for x in (ROOT/'problems/2024-B4/reviews').glob('cofactor-dominant-r4-review-2-*')}
assert actual=={P+s for s in initial},actual
labels=re.findall(r'^\| (DC-\d{2}) \|',(ROOT/(P+'ledger-v1.md')).read_text(),re.M)
assert labels==['DC-'+str(i).zfill(2) for i in range(1,49)]

authority='problems/2024-B4/reviews/cofactor-global-r2-acceptance.json'
accepted=read(authority)
assert accepted['proposed_claims_accepted']==['CG1','CG2','CG3']
assert accepted['unresolved_substantive_issues']==0
assert accepted['accepted_copy']['sha256']=='fd110d1615e730d754063b157cc1906b418702f510b2640bfd1b5c63e898548d'
check(accepted['accepted_copy']);check(accepted['candidate'])
assert (ROOT/accepted['accepted_copy']['path']).read_bytes().endswith((ROOT/accepted['candidate']['path']).read_bytes())

declared=constructor['artifacts']+[freeze]+cb['protected']+[parent_id]+parent['artifacts']
for row in declared: check(row)
protected,protected_hash=canonical(declared)
parent_rows=rows(parent); parent_unique,parent_hash=canonical(parent_rows)
constructor_rows=rows(constructor); constructor_unique,constructor_hash=canonical(constructor_rows)
out(P+'baseline-v1.json',{
    'created_utc':stamp(),'purpose':'Administrative-only compact immutable input preservation',
    'assigned_prefix_confirmed_unused_before_first_write':True,
    'given_target_main_freeze_and_parent_exact':True,
    'protected_fingerprint_occurrences':len(declared),'protected_unique_paths':len(protected),
    'canonical_protected_summary_sha256':protected_hash,'protected':protected,
    'accepted_CG_body_candidate_suffix_exact':True,
    'operative_accepted_claims_ONLY':['CG1','CG2'],
    'cubic_parent_is_administrative_NOT_a_mathematical_premise':True,
    'compact_immutable_parents':[
      {'identity':parent_id,'declared_fingerprint_occurrences':len(parent_rows),
       'deduplicated_paths':len(parent_unique),'canonical_summary_sha256':parent_hash,
       'historical_inventory_not_recopied_or_recursively_reverified':True},
      {'identity':freeze,'declared_fingerprint_occurrences':len(constructor_rows),
       'deduplicated_paths':len(constructor_unique),'canonical_summary_sha256':constructor_hash,
       'historical_inventory_not_recopied_or_recursively_reverified':True}],
    'no_corresponding_NEW_A_R4_material_accessed':True,'no_old_shared_Git_cache_mutation':True})

out(P+'metadata-v1.json',{
    'created_utc':stamp(),'status':'ENTIRE initially blind OTHER WHOLE R4 R2; not promotion',
    'reviewer':'/root/review_2017_coarsening_r1','new_constructor_root_excluded':True,
    'reviewer_NEW_construction_contribution':False,'whole_obligations':48,
    'older_C_reviews_and_CP_sector3_construction_disclosed_not_self_recertified':True,
    'all48_hand_reconstructed_no_mathematical_program':True,
    'corresponding_NEW_A_R4_findings_files_hashes_metadata_accessed':False,
    'identity_only_completion_until_BOTH_entire_initials_confirmed':True,
    'no_Git_old_shared_cache_write_spawn_contact_charge_bypass':True,
    'no_math_scan_CAS_optimizer_certificate_constructor_or_source_rerun':True,
    'requested_settings':{'model':'gpt-6.1-sol','reasoning':'max','inherited':True},
    'verified_effective_settings':None,
    'telemetry':{'latest_parent_TOTAL_percent':23,'latest_parent_utc':'2026-10-18 09:54:07 UTC',
                 'reset_unix':1792874445,'human_authorized_current_window':True,
                 'ceiling_TOTAL_percent':90,'integration_reserve':True,
                 'automatic_later_window_spending':False},
    'target_main':main,'target_freeze':freeze,'immediate_own_parent':parent_id,
    'compact_baseline':rec(P+'baseline-v1.json')})

for row in protected: check(row)
before_validation=initial+['baseline-v1.json','metadata-v1.json']
out(P+'input-validation-v1.json',{
    'checked_utc':stamp(),'administrative_only_not_mathematical_proof':True,
    'all_constructor_ten_payloads_and_freeze_exact':True,
    'all_constructor_twelve_guard_records_exact':True,
    'immediate_own_parent_and_nine_payloads_exact':True,
    'accepted_CG_body_candidate_suffix_exact':True,
    'protected_fingerprint_occurrences':len(declared),'protected_unique_paths':len(protected),
    'canonical_protected_summary_sha256':protected_hash,
    'ledger_exact_ordered_DC_01_through_48_once':True,
    'no_corresponding_NEW_A_R4_material_accessed':True,
    'mathematical_executables_run':0,'errors':[]})
payloads=[rec(P+s) for s in before_validation+['input-validation-v1.json']]
for row in protected+payloads: check(row)
out(P+'manifest-v1.json',{
    'frozen_utc':stamp(),'status':'ENTIRE initially blind OTHER WHOLE R4 R2 frozen; not promotion',
    'whole_obligations':48,'review_file_count':10,
    'ENTIRE_report_ALL48_issues_sources_log_code_ALL_metadata_frozen':True,
    'no_corresponding_NEW_A_R4_findings_files_hashes_or_metadata_access':True,
    'identity_only_completion_before_mathematical_findings':True,
    'target_main':main,'target_freeze':freeze,'immediate_own_parent':parent_id,
    'artifacts':payloads})
print(json.dumps({'manifest':rec(P+'manifest-v1.json'),'initial':rec(P+'initial-v1.md'),
    'review_files':10,'whole_obligations':48,
    'protected_occurrences':len(declared),'protected_unique_paths':len(protected)},indent=2))
