"""Exclusive administrative freeze only; no mathematical scan or certificate replay."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re
R=Path(__file__).resolve().parents[3]
P='problems/2021-B4/reviews/reasoning-return-r12-review-2-'
C='problems/2021-B4/notes/reasoning-return-r12-'
PEER='problems/2021-B4/reviews/reasoning-return-r12-review-1-'
def fp(path):
    assert not path.startswith(PEER)
    b=(R/path).read_bytes()
    return {'path':path,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def verify(row):
    a=fp(row['path']);assert a=={k:row[k]for k in('path','bytes','sha256')},row['path']
    return a
def load(path):
    assert not path.startswith(PEER)
    return json.loads((R/path).read_text())
def save(suffix,obj):
    with(R/(P+suffix)).open('x')as f:json.dump(obj,f,indent=2);f.write('\n')
    return fp(P+suffix)
assert not(R/(P+'manifest-v1.json')).exists()
assert fp(C+'candidate-v1.md')['sha256']=='7600005b20756bf9613e2b02177d5ae50aa5d3f573a6aa267bf245ee0a5c8f19'
assert fp(C+'freeze-v1.json')['sha256']=='3ed49540ef24d6b947add1abc2db155f6c3bda82c8e2a40c7615547aa3351f02'
cm=load(C+'freeze-v1.json');assert len(cm['artifacts'])==10
rows=[fp(C+'freeze-v1.json')]+[verify(x)for x in cm['artifacts']]
ci=load(C+'input-validation-v1.json')
keys=['necessary_current_direct_inputs','accepted_authority_current_candidate_copy_and_register_declarations',
 'immutable_R11_constructor_manifest_and_payloads','immutable_immediate_own_NF_review_manifest_and_payloads']
declared=[verify(x)for key in keys for x in ci[key]];assert len(declared)==55
rows+=declared
parent='problems/2025-B4/reviews/reasoning-return-r9-runge-review-1-manifest-v1.json'
assert fp(parent)['sha256']=='dfd09d56856267e15f153db8c4f65086a91872840c2764b5a08d0bb243c3d242'
rows.append(fp(parent));rows.extend(verify(x)for x in load(parent)['artifacts'])
unique={}
for row in rows:
 if row['path']in unique:assert unique[row['path']]==row
 unique[row['path']]=row
summary={'occurrences':len(rows),'unique_paths':len(unique),
 'deduplicated_summary_sha256':hashlib.sha256(json.dumps([unique[p]for p in sorted(unique)],sort_keys=True,separators=(',',':')).encode()).hexdigest()}
ledger=(R/(P+'ledger-v1.md')).read_text()
assert re.findall(r'^\|R12-(\d\d)\|',ledger,re.M)==[str(i).zfill(2)for i in range(1,61)]
suffixes=['initial-v1.md','ledger-v1.md','issues-v1.md','source-audit-v1.md','worklog-v1.md','freeze-v1.py']
payload=[fp(P+s)for s in suffixes]
budget={'observed_at_utc':'2026-10-18T00:53:20+00:00','used_percent_total':5,'window_minutes':10080,
 'reset_unix':1792874445,'ordinary_usage_allowed':True,'current_window_explicitly_authorized':True,
 'ceiling_total_percent':90,'integration_reserve':True,'automatic_further_reset_authorized':False}
integrity=save('integrity-v1.json',{'verified_at_utc':datetime.now(timezone.utc).isoformat(),
 'administrative_only':True,'all_current_rows':rows,'summary':summary,
 'all_eleven_constructor_files_preserved':True,'all55_constructor_declared_rows_preserved':True,
 'immediate_own_parent_preserved_not_history_rewalked':fp(parent),
 'all60_obligations_once':True,'substantive_issues':0,'required_repairs':0,
 'NEW_B_R12_findings_files_metadata_unread_through_ENTIRE_initial':True,
 'no_mathematical_program_CAS_scan_old_certificate_replay_or_constructor_rerun':True,
 'payload_before_metadata':payload,'budget':budget})
manifest=save('manifest-v1.json',{'frozen_at_utc':datetime.now(timezone.utc).isoformat(),
 'status':'COMPLETE initially blind OTHER nonconstructor WHOLE R12 R2; no substantive defect found; not acceptance',
 'reviewer':'/root','constructor':'/root/review_2021_reasoning_j15_r2','constructor_excluded':True,
 'root_no_NEW_R12_construction_contribution':True,
 'old_root_PN_authorship_R5_strategy_R8_R11_TA1_review_roles_disclosed_no_self_recertification':True,
 'target':fp(C+'candidate-v1.md'),'constructor_freeze':fp(C+'freeze-v1.json'),
 'whole_claims':['R12A','R12B','R12C'],'whole_obligations':60,'all60_individually_reconstructed':True,
 'every_proof_critical_table_entry_reconstructed_by_hand':True,
 'substantive_issues':0,'required_repairs':0,'unresolved_issues':0,'retained_scope_notes':4,
 'NEW_B_R12_findings_files_sources_ledgers_metadata_unread_through_ENTIRE_initial':True,
 'another_OTHER_ENTIRE_whole_initial_and_reconciliation_required':True,
 'no_entire_repeated_J15_degree20_annual_lift_sign_height_or_novelty_claim':True,
 'no_mathematical_program_CAS_scan_old_certificate_replay_or_constructor_rerun':True,
 'input_summary':summary,'requested_settings':{'model':'gpt-6.1-sol','reasoning':'max','inherited':True},
 'independently_verified_effective_readback':None,'budget':budget,'artifacts':payload+[integrity]})
for row in rows+payload+[integrity,manifest]:verify(row)
print(json.dumps({'report':payload[0],'ledger':payload[1],'manifest':manifest,'input_summary':summary,
 'whole_obligations':60,'substantive_issues':0,'required_repairs':0,'all_postfreeze_records_match':True},indent=2))
