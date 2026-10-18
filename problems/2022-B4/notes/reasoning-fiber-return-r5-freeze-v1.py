"""Administrative-only SHA/JSON/label checks; no mathematical computation."""
from pathlib import Path
import datetime as dt
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[3]
P='problems/2022-B4/notes/reasoning-fiber-return-r5-'
PARENT='problems/2024-B4/reviews/cofactor-dominant-r4-review-2-manifest-v1.json'

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

initial=['candidate-v1.md','obligations-v1.md','failed-routes-v1.md',
         'sources-v1.md','sources-v1.json','worklog-v1.md','freeze-v1.py']
actual={str(x.relative_to(ROOT)) for x in (ROOT/'problems/2022-B4/notes').glob('reasoning-fiber-return-r5-*')}
assert actual=={P+s for s in initial},actual
labels=re.findall(r'^\| (FR5-\d{2}) \|',(ROOT/(P+'obligations-v1.md')).read_text(),re.M)
assert labels==['FR5-'+str(i).zfill(2) for i in range(1,49)]
assert read(P+'sources-v1.json')['new_external_theorem_imported_for_CF1_through_CF5'] is False

parent_id={'path':PARENT,'bytes':2892,
           'sha256':'09ceeb941ee51f6d700f2c4d64264ebebca4373cc851d3a50a6f7baf4b056083'}
agents={'path':'AGENTS.md','bytes':4707,
        'sha256':'28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff'}
check(parent_id);check(agents)
parent=read(PARENT);assert len(parent['artifacts'])==9
declared=[agents,parent_id]+parent['artifacts']
for path in ['problems/2022-B4/statement.md','problems/2022-B4/research.md',
             'problems/2022-B4/references.md',
             'problems/2022-B4/notes/reasoning-seed-return-r1-source-audit-v1.md']:
    declared.append(rec(path))

accepted_specs=[
 ('reasoning-seed-return-r1','00b47afc07c762063325a190e3b3dda02fe884a78018b9b33880f7d424d9385d',24820),
 ('reasoning-complexity-return-r9-v3','18e681d69b29d3495fea0cc2a29dbcb8a9c34db60644b981b3f653d666bef4ad',49080),
 ('reasoning-return-r5','1a2544cb8ced3bba9cc6efed1870c242c652b3e6029f39881028d4637d7c6da6',30324),
 ('reasoning-return-r7','739a88f2a5b4e3cdd13681094f420def99259c0d52b63aef3b394a407c29a342',23574),
 ('reasoning-return-r8','f09e43748bdc2c8d1cd4b7bccdfd733265b4fe0b8f24986b00051fea7c799b9f',20660)]
accepted=[]
for name,sha,size in accepted_specs:
    authority='problems/2022-B4/reviews/'+name+'-acceptance.json'
    a=read(authority)
    assert a['status']=='proved, independently reviewed scoped partial result'
    assert a['unresolved_substantive_issues']==0
    assert a['accepted_copy']['sha256']==sha and a['accepted_copy']['bytes']==size
    check(a['accepted_copy']);check(a['candidate'])
    assert (ROOT/a['accepted_copy']['path']).read_bytes().endswith((ROOT/a['candidate']['path']).read_bytes())
    md=authority[:-5]+'.md'
    declared.extend([rec(authority),rec(md),a['accepted_copy'],a['candidate']])
    accepted.append({'authority':rec(authority),'accepted_copy':a['accepted_copy'],
                     'candidate':a['candidate'],'accepted_body_candidate_suffix_exact':True})

for row in declared: check(row)
protected,protected_hash=canonical(declared)
parent_rows=rows(parent);parent_unique,parent_hash=canonical(parent_rows)
out(P+'baseline-v1.json',{
 'created_utc':stamp(),'purpose':'Compact administrative preservation; not a mathematical proof',
 'assigned_prefix_unused_before_first_write':True,
 'protected_fingerprint_occurrences':len(declared),'protected_unique_paths':len(protected),
 'canonical_protected_summary_sha256':protected_hash,'protected':protected,
 'five_complete_accepted_bodies_and_direct_authorities_read_and_exact':True,
 'accepted':accepted,
 'compact_immutable_parent':{
    'identity':parent_id,'declared_fingerprint_occurrences':len(parent_rows),
    'deduplicated_paths':len(parent_unique),'canonical_summary_sha256':parent_hash,
    'historical_inventory_not_recopied_or_recursively_reverified':True},
 'no_old_shared_Git_cache_mutation':True})

out(P+'metadata-v1.json',{
 'created_utc':stamp(),'status':'candidate proof - unverified; ENTIRE constructor checkpoint',
 'constructor':'/root/review_2017_coarsening_r1',
 'root_generic_assignment_supplied_NEW_proof_inference':False,
 'TWO_OTHER_initially_blind_ENTIRE_whole_audits_required':True,
 'constructor_excluded_from_both_reviews':True,'coordinator_only_promotion':True,
 'whole_obligations':48,'proposed_claims':['CF1','CF2','CF3','CF4','CF5','CF6'],
 'CF1_CF5_unconditional_CF6_explicitly_conditional':True,
 'older_C_SR_R7_R8_authorship_and_F5_Q_review_roles_disclosed':True,
 'new_external_theorem_used_for_CF1_CF5':False,
 'no_infinite_positive_avoider_termination_no_tenfold_annual_or_novelty_claim':True,
 'no_math_program_scan_CAS_native_child_source_or_author_rerun':True,
 'no_old_shared_Git_cache_edit_spawn_contact_charge_bypass':True,
 'pending_tool_job_approval_or_stall':False,
 'requested_settings':{'model':'gpt-6.1-sol','reasoning':'max','inherited':True},
 'verified_effective_settings':None,
 'telemetry':{'latest_parent_TOTAL_percent':23,'latest_parent_utc':'2026-10-18 09:54:07 UTC',
              'reset_unix':1792874445,'human_authorized_current_window':True,
              'ceiling_TOTAL_percent':90,'integration_reserve':True,
              'automatic_later_window_spending':False},
 'immediate_own_parent':parent_id,'compact_baseline':rec(P+'baseline-v1.json')})

for row in protected: check(row)
out(P+'input-validation-v1.json',{
 'checked_utc':stamp(),'administrative_only_not_mathematical_evidence':True,
 'protected_fingerprint_occurrences':len(declared),'protected_unique_paths':len(protected),
 'canonical_protected_summary_sha256':protected_hash,
 'parent_identity_and_all_nine_parent_payloads_exact':True,
 'five_accepted_bodies_candidates_and_authorities_exact':True,
 'all_five_accepted_body_candidate_suffixes_exact':True,
 'ordered_FR5_01_through_48_once':True,'mathematical_programs_run':0,'errors':[]})
payloads=[rec(P+s) for s in initial+['baseline-v1.json','metadata-v1.json','input-validation-v1.json']]
for row in protected+payloads: check(row)
out(P+'freeze-v1.json',{
 'frozen_utc':stamp(),'status':'candidate proof - unverified; ENTIRE constructor frozen',
 'claims':['CF1','CF2','CF3','CF4','CF5','CF6'],'whole_obligations':48,
 'constructor_file_count':11,'ENTIRE_main_ALL48_failures_sources_worklog_code_ALL_metadata_frozen':True,
 'TWO_OTHER_initially_blind_ENTIRE_whole_audits_REQUIRED_before_promotion':True,
 'mathematical_computation_or_source_rerun':False,
 'unconditional_CF1_CF5_conditional_CF6_no_annual_claim':True,
 'immediate_own_parent':parent_id,'artifacts':payloads})
print(json.dumps({'freeze':rec(P+'freeze-v1.json'),'main':rec(P+'candidate-v1.md'),
                 'files':11,'whole_obligations':48,
                 'protected_occurrences':len(declared),'protected_unique_paths':len(protected)},indent=2))
