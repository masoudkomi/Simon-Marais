"""Administrative-only exclusive freeze of root's entire blind R9 R1.
No mathematical computation, author program, peer read or history replay.
"""
from pathlib import Path
import hashlib,json,re,datetime
ROOT=Path(__file__).resolve().parents[3]
PRE='problems/2025-B4/reviews/reasoning-return-r9-review-1-'
FORBIDDEN='problems/2025-B4/reviews/reasoning-return-r9-review-2-'

def fp(p):
    assert not p.startswith(FORBIDDEN)
    path=(ROOT/p).resolve();assert path.is_relative_to(ROOT)
    b=path.read_bytes()
    return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())

def check(r):
    actual=fp(r['path'])
    assert actual=={k:r[k]for k in ('path','bytes','sha256')},r['path']
    return actual

def write(s,x):
    with(ROOT/(PRE+s)).open('x')as f:json.dump(x,f,indent=2);f.write('\n')

def summary(rows):
    unique={}
    for r in rows:
        assert r['path']not in unique or unique[r['path']]==r
        unique[r['path']]=r
    data=[unique[p]for p in sorted(unique)]
    return dict(occurrences=len(rows),unique_paths=len(data),canonical_deduplicated_sha256=hashlib.sha256(json.dumps(data,sort_keys=True,separators=(',',':')).encode()).hexdigest())

freeze='problems/2025-B4/notes/reasoning-return-r9-freeze-v1.json'
assert fp(freeze)['sha256']=='93eed518f1584c8e4f1a7cbe4d6229c9532caae4269d18cf0393c1f0e934aa8f'
author=json.loads((ROOT/freeze).read_text())
current=[fp(freeze)]+[check(r)for r in author['artifacts']]
assert len(current)==11
main=fp('problems/2025-B4/notes/reasoning-return-r9-candidate-v1.md')
assert main['bytes']==22574 and main['sha256']=='8fae8c0dd3e951fd4c847954f75186b8969f1dbdec9592b8cebcbda8394a9aa2'
base=json.loads((ROOT/'problems/2025-B4/notes/reasoning-return-r9-baseline-v1.json').read_text())
declared=[check(r)for r in base['declared_records']]
other=[check(r)for r in base['other_actual_read_inputs']]
assert len(declared)==21 and len(other)==6
extra=[fp(p)for p in ['problems/2025-B4/reviews/reasoning-return-r8-acceptance.md','problems/2025-B4/reviews/reasoning-return-r6-acceptance.md','problems/2025-B4/reviews/reasoning-return-r6-acceptance.json']]
inputs=current+declared+other+extra
ledger=(ROOT/(PRE+'ledger-v1.md')).read_text()
assert re.findall(r'^\|(\d\d)\|',ledger,re.M)==[f'{i:02d}'for i in range(1,49)]
issue=(ROOT/(PRE+'issues-v1.md')).read_text()
assert re.findall(r'^\|(R9R1-\d+)\|',issue,re.M)==['R9R1-01']
payload=[fp(PRE+s)for s in ['initial-v1.md','ledger-v1.md','issues-v1.md','source-audit-v1.md','worklog-v1.md','freeze-v1.py']]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
budget=dict(at_utc='2026-10-18 00:28:04 UTC',total_used_percent=3,reset_unix=1792874445,window_minutes=10080,ordinary_allowed=True,explicit_new_window_authorization=True,total_ceiling=90,reserve=True,no_automatic_further_reset=True)
validation=dict(verified_at_utc=now,administrative_only=True,all_current_records_match=True,input_summary=summary(inputs),exact_current_constructor_records=current,constructor_direct_unique_declarations_verified=21,constructor_other_input_occurrences_verified=6,extra_accepted_authorities=extra,historical_constructor_485_own_paths_bound_not_replayed=base['immutable_own_parent'],historical_parent_payloads_bound_by_exact_baseline_not_new_mathematical_reviews=True,all48_ledger_rows_once=True,one_required_issue='R9R1-01',new_peer_R9_reports_findings_and_metadata_read=False,no_mathcode_CAS_scan_author_rerun_certificate_replay=True,budget=budget)
write('integrity-v1.json',validation)
payload.append(fp(PRE+'integrity-v1.json'))
manifest=dict(frozen_at_utc=now,status='ENTIRE initially blind OTHER WHOLE R1 complete; limited versioned radius repair required',reviewer='/root',constructor='/root/review_2017_coarsening_r1',new_R9_constructor_contribution=False,old_UW_source_R6_R8_roles_disclosed_no_self_recertification=True,target=main,constructor_freeze=fp(freeze),whole_claims=['R9A','R9B','R9C','R9D','R9E','R9F'],all48_obligations_individually_reconstructed=True,required_issues=['R9R1-01'],affected_ledger_rows=[24,25],other_scoped_inferences_no_defect_found=True,ENTIRE_initial_before_ANY_NEW_peer_R9_findings_or_metadata=True,versioned_author_repair_and_BOTH_affected_reaudits_required=True,another_OTHER_whole_initial_and_reconciliation_required=True,no_annual_exclusion_or_final_source_theorem_refutation=True,input_summary=summary(inputs),requested_settings=dict(model='gpt-6.1-sol',reasoning='max'),effective_readback=None,budget=budget,artifacts=payload)
write('manifest-v1.json',manifest)
for r in inputs+payload:check(r)
print(json.dumps(dict(manifest=fp(PRE+'manifest-v1.json'),initial=payload[0],ledger=payload[1],input_summary=summary(inputs),required_issues=['R9R1-01'],whole_obligations=48),indent=2))
