#!/usr/bin/env python3
"""Exclusive ENTIRE review administrative freeze; no mathematics evaluated."""
from datetime import datetime,timezone
from hashlib import sha256
from pathlib import Path
import json,re
ROOT=Path.cwd().resolve()
P='problems/2017-B4/reviews/reasoning-global-return-r7-review-1-'
C='problems/2017-B4/notes/reasoning-global-return-r7-'
def rec(path):
    b=(ROOT/path).read_bytes()
    return dict(path=path,bytes=len(b),sha256=sha256(b).hexdigest())
def read(path):return json.loads((ROOT/path).read_text())
def out(suffix,value):
    with(ROOT/(P+suffix)).open('x',encoding='utf-8')as f:
        json.dump(value,f,indent=2,ensure_ascii=False);f.write('\n')
rows=[];unique={}
def bind(path,label,expected=None):
    row=rec(path)
    if expected is not None:assert row=={k:expected[k]for k in('path','bytes','sha256')},path
    assert path not in unique or unique[path]==row
    unique[path]=row;rows.append(dict(label=label,**row));return row
freeze=bind(C+'freeze-v1.json','ENTIRE constructor freeze',dict(path=C+'freeze-v1.json',
    bytes=3015,sha256='545e1131036b4e298bfb2957584e2186e6b92a2f0c94ed3f2b4a4036653d9199'))
assert len(read(C+'freeze-v1.json')['artifacts'])==10
for item in read(C+'freeze-v1.json')['artifacts']:
    bind(item['path'],'ENTIRE constructor artifact',item)
baseline=read(C+'baseline-v1.json')
bind(baseline['immutable_own_parent']['path'],'constructor compact parent',baseline['immutable_own_parent'])
for item in baseline['inputs']:bind(item['path'],'necessary direct constructor input',item)
assert len(baseline['inputs'])==25
old=sorted([baseline['immutable_own_parent']]+baseline['inputs'],key=lambda x:x['path'])
digest=sha256(json.dumps(old,sort_keys=True,separators=(',',':')).encode()).hexdigest()
assert digest==read(C+'input-validation-v1.json')['canonical_direct_input_summary_sha256']
for path in baseline['accepted_authority_paths']:
    authority=read(path)
    assert authority['unresolved_substantive_issues']==0 and authority['repair_required'] is False
    assert(ROOT/authority['accepted_copy']['path']).read_bytes().endswith((ROOT/authority['candidate']['path']).read_bytes())
parent_path='problems/2024-B4/notes/cofactor-symmetry-r1-freeze-v1.json'
parent=bind(parent_path,'compact own latest ENTIRE constructor parent',dict(path=parent_path,
    bytes=2406,sha256='2fdb3fc025f2bf89e6d3bdf060373103fecf428db8ff4f407f170bed86bab327'))
for item in read(parent_path)['artifacts']:
    if item['path'].endswith(('metadata-v1.json','input-validation-v1.json')):
        bind(item['path'],'necessary own-parent compact metadata',item)
ids=re.findall(r'^\|(R7O\d{2})\|',(ROOT/(P+'ledger-v1.md')).read_text(),re.M)
author=re.findall(r'^\|(R7O\d{2})\|',(ROOT/(C+'obligations-v1.md')).read_text(),re.M)
assert ids==author==[f'R7O{i:02d}'for i in range(1,61)]
assert 'zero substantive issues' in(ROOT/(P+'initial-v1.md')).read_text()
ordered=[unique[p]for p in sorted(unique)]
summary=dict(occurrences=len(rows),unique_paths=len(ordered),sha256=sha256(
    json.dumps(ordered,sort_keys=True,separators=(',',':')).encode()).hexdigest())
NOW=datetime.now(timezone.utc).isoformat()
out('baseline-v1.json',dict(captured_at_utc=NOW,constructor_freeze=freeze,
    compact_own_parent=parent,summary=summary,records=ordered,
    occurrence_labels=[dict(label=x['label'],path=x['path'])for x in rows],
    no_recursive_historical_inventory_expansion=True))
out('metadata-v1.json',dict(status='ENTIRE initially blind OTHER WHOLE R1',reviewer='/root',
    constructor='/root/review_2017_coarsening_r1',constructor_excluded=True,
    requested_model='gpt-6.1-sol',requested_reasoning='max',verified_effective_settings=None,
    all60_obligations=True,substantive_issues=0,required_repairs=0,closed_scope_notes=5,
    full_main_all_companions_sources_failures_interim_worklog_code_ALL_metadata_read=True,
    old_PM_G_PUS_root_roles_disclosed_not_independently_self_recertified=True,
    root_not_NEW_R7_constructor=True,
    NEW_B2017_peer_findings_files_metadata_read_or_hashed=False,
    peer_completion_identity_only_received=True,status_filename_listing_only=True,
    no_mathematical_program_CAS_scan_count_rule_compiler_author_rerun_certificate_replay=True,
    finite_angle_original_source_and_explicit_D4_endpoint_checked=True,
    no_new_upper_R_value_two_sided_computability_annual_priority_claim=True,
    compact_summary=summary,
    latest_authoritative_budget=dict(at_utc='2026-10-18 07:38 UTC',used_percent_TOTAL=14,
        window_minutes=10080,reset_unix=1792874445,ordinary_usage_allowed=True,
        current_window_user_authorized_through_TOTAL=90,integration_reserve=True,
        automatic_later_window_spending=False)))
for path,row in unique.items():assert rec(path)==row,path
out('input-validation-v1.json',dict(validated_at_utc=NOW,summary=summary,
    all11_constructor_files_verified=True,all26_direct_constructor_records_verified=True,
    four_accepted_copy_suffixes_verified=True,all60_author_reviewer_IDs_match_in_order=True,
    exact_direct_bytes_before_after_new_writes=True,no_peer2017_paths_read_or_hashed=True,
    administrative_integrity_not_mathematical_testing=True))
suffixes=['initial-v1.md','ledger-v1.md','issues-v1.md','source-checks-v1.md','worklog-v1.md',
    'freeze-v1.py','baseline-v1.json','metadata-v1.json','input-validation-v1.json']
out('manifest-v1.json',dict(frozen_at_utc=NOW,status='ENTIRE initially blind OTHER WHOLE R7 R1',
    reviewer='/root',constructor='/root/review_2017_coarsening_r1',constructor_excluded=True,
    all60_obligations=True,substantive_issues=0,required_repairs=0,closed_scope_notes=5,
    exact_target=rec(C+'candidate-v1.md'),constructor_freeze=freeze,
    compact_own_parent=parent,current_input_summary=summary,
    no_NEW_B2017_review_material_read_or_hashed=True,
    entire_report_ledger_sources_worklog_code_ALL_metadata_frozen=True,
    artifacts=[rec(P+s)for s in suffixes],promotion=False))
for path,row in unique.items():assert rec(path)==row,path
print(json.dumps(dict(manifest=rec(P+'manifest-v1.json'),report=rec(P+'initial-v1.md'),
    all60_obligations=True,summary=summary,promotion=False),indent=2))
