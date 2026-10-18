"""Exclusive administrative freeze only; no mathematical computation or RR run."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,re
R=Path(__file__).resolve().parents[3]
P='problems/2025-B4/reviews/reasoning-return-r9-runge-review-1-'
C='problems/2025-B4/notes/reasoning-return-r9-runge-'
PEER='problems/2025-B4/reviews/reasoning-return-r9-runge-review-2-'
def fp(path):
    assert not path.startswith(PEER)
    raw=(R/path).read_bytes()
    return {'path':path,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
def verify(row):
    assert fp(row['path'])=={k:row[k]for k in('path','bytes','sha256')},row['path']
    return fp(row['path'])
def load(path):
    assert not path.startswith(PEER)
    return json.loads((R/path).read_text())
def save(suffix,value):
    with(R/(P+suffix)).open('x')as f:json.dump(value,f,indent=2);f.write('\n')
    return fp(P+suffix)
assert not(R/(P+'manifest-v1.json')).exists()
assert fp(C+'candidate-v1.md')['sha256']=='8bcd69dfa97441b23fd456268e655312aea55a0f7a64a5237f0117f6a192b90a'
assert fp(C+'freeze-v1.json')['sha256']=='cb5073bbce53c07b12e5b253af51f278ebd6475c0600d700bef6a9064a7ec32b'
constructor=load(C+'freeze-v1.json')
assert len(constructor['artifacts'])==8
current=[fp(C+'freeze-v1.json')]+[verify(x)for x in constructor['artifacts']]
declared=load(C+'baseline-v1.json')['records']
assert len(declared)==13
current.extend(verify(x)for x in declared)
for path in ['AGENTS.md','problems/2025-B4/statement.md',
 'problems/2025-B4/reviews/reasoning-return-r8-acceptance.md',
 'problems/2025-B4/reviews/reasoning-return-r8-acceptance.json',
 'problems/2025-B4/reviews/reasoning-return-r6-acceptance.md',
 'problems/2025-B4/reviews/reasoning-return-r6-acceptance.json']:
 current.append(fp(path))
parent='problems/2025-B4/reviews/reasoning-return-r9-review-1-manifest-v1.json'
assert fp(parent)['sha256']=='8d8370530a3eb92359e1f5d693c1f385e0622b99078e57d7a1674cd7a183397a'
current.append(fp(parent)); current.extend(verify(x)for x in load(parent)['artifacts'])
unique={}
for row in current:
 if row['path']in unique:assert unique[row['path']]==row
 unique[row['path']]=row
summary={'occurrences':len(current),'unique_paths':len(unique),
 'deduplicated_summary_sha256':hashlib.sha256(json.dumps([unique[p]for p in sorted(unique)],sort_keys=True,separators=(',',':')).encode()).hexdigest()}
ledger=(R/(P+'ledger-v1.md')).read_text()
assert re.findall(r'^\|(\d\d)\|',ledger,re.M)==[str(i).zfill(2)for i in range(1,35)]
suffixes=['initial-v1.md','ledger-v1.md','issues-v1.md','source-audit-v1.md','worklog-v1.md','freeze-v1.py']
payload=[fp(P+s)for s in suffixes]
budget={'observed_at_utc':'2026-10-18T00:42:14+00:00','used_percent_total':4,
 'window_minutes':10080,'reset_unix':1792874445,'ordinary_usage_allowed':True,
 'current_window_explicitly_authorized':True,'ceiling_total_percent':90,
 'integration_reserve':True,'automatic_further_reset_authorized':False}
integrity=save('integrity-v1.json',{'verified_at_utc':datetime.now(timezone.utc).isoformat(),
 'administrative_only':True,'current_records':current,'summary':summary,
 'all_necessary_current_fingerprints_match':True,'constructor_nine_files_preserved':True,
 'constructor_thirteen_declared_rows_preserved':True,'own_immediate_parent_bound_not_history_rewalked':fp(parent),
 'all34_obligations_once':True,'substantive_defects':0,'required_repairs':0,
 'NEW_A_Runge_files_findings_or_metadata_unread_through_ENTIRE_initial':True,
 'no_mathematical_program_CAS_RR_scan_certificate_or_constructor_replay':True,
 'payload_before_metadata':payload,'budget':budget})
manifest=save('manifest-v1.json',{'frozen_at_utc':datetime.now(timezone.utc).isoformat(),
 'status':'ENTIRE initially blind OTHER nonconstructor WHOLE RG1–RG3 R1 complete; no substantive defect found; not acceptance',
 'reviewer':'/root','constructor':'/root/review_2017_coarsening_r1','constructor_excluded':True,
 'root_no_NEW_submitted_Runge_construction_contribution':True,
 'older_UW_R6_R8_source_roles_disclosed_no_self_recertification':True,
 'target':fp(C+'candidate-v1.md'),'constructor_freeze':fp(C+'freeze-v1.json'),
 'whole_claims':['RG1','RG2','RG3'],'whole_obligations':34,'all34_individually_reconstructed':True,
 'substantive_defects':0,'required_repairs':0,'unresolved_issues':0,'retained_scope_notes':5,
 'another_OTHER_ENTIRE_whole_initial_and_reconciliation_required':True,
 'NEW_A_Runge_files_findings_sources_ledger_metadata_unread_through_ENTIRE_initial':True,
 'no_numerical_improvement_fixed_p_novelty_new_exclusion_bound_on_p_or_annual_claim':True,
 'no_mathematical_executable_CAS_RR_scan_certificate_or_constructor_replay':True,
 'input_summary':summary,'requested_settings':{'model':'gpt-6.1-sol','reasoning':'max','inherited':True},
 'independently_verified_effective_readback':None,'budget':budget,'artifacts':payload+[integrity]})
for row in current+payload+[integrity,manifest]:verify(row)
print(json.dumps({'report':payload[0],'ledger':payload[1],'manifest':manifest,'input_summary':summary,
 'whole_obligations':34,'substantive_defects':0,'required_repairs':0,'all_postfreeze_records_match':True},indent=2))
