#!/usr/bin/env python3
"""Exclusive administrative constructor freeze; no mathematical computation."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re

ROOT=Path.cwd().resolve()
P='problems/2024-B4/notes/coordinator-F8-pencil-r1-'
NOW=datetime.now(timezone.utc).isoformat()
assert ROOT.name=='Website' and (ROOT/'AGENTS.md').is_file()
def rec(path):
    b=(ROOT/path).read_bytes()
    return dict(path=path,bytes=len(b),sha256=sha256(b).hexdigest())
def read(path): return json.loads((ROOT/path).read_text())
def out(suffix,value):
    with(ROOT/(P+suffix)).open('x',encoding='utf-8')as f:
        json.dump(value,f,indent=2,ensure_ascii=False);f.write('\n')
rows=[]; unique={}
def bind(path,label,expected=None):
    row=rec(path)
    if expected is not None: assert row=={k:expected[k]for k in ('path','bytes','sha256')},path
    assert path not in unique or unique[path]==row
    unique[path]=row;rows.append(dict(label=label,**row));return row

parent_path='problems/2020-B4/reviews/reasoning-arithmetic-return-r10-review-2-manifest-v1.json'
parent=bind(parent_path,'compact own last ENTIRE whole-review parent',dict(
    path=parent_path,bytes=3173,sha256='184fbfcbe879f9707daa0f07b4ba58eb0b548720e7cec24f7bb55fe638e1be3e'))
for item in read(parent_path)['artifacts']:
    if item['path'].endswith(('metadata-v1.json','input-validation-v1.json')):
        bind(item['path'],'necessary compact own-parent metadata',item)
for path in ['AGENTS.md','problems/2024-B4/statement.md',
    'problems/2024-B4/reviews/coordinator-neighbor-Frobenius-r1-acceptance.md',
    'problems/2024-B4/reviews/coordinator-neighbor-Frobenius-r1-acceptance.json',
    'problems/2024-B4/reviews/coordinator-component-saturation-r1-acceptance.md',
    'problems/2024-B4/reviews/Kasami-whole-criterion-acceptance.md',
    'problems/2024-B4/reviews/coordinator-three-bit-sector-r2-acceptance.md']:
    bind(path,'actual current official/accepted frontier context')
authority=read('problems/2024-B4/reviews/coordinator-neighbor-Frobenius-r1-acceptance.json')
bind(authority['accepted_copy']['path'],'accepted NF body identity; rebuilt local algebra only',authority['accepted_copy'])
bind(authority['candidate']['path'],'exact old NF frozen body identity',authority['candidate'])
assert (ROOT/authority['accepted_copy']['path']).read_bytes().endswith((ROOT/authority['candidate']['path']).read_bytes())
ids=re.findall(r'^\|(\d{2})\|',(ROOT/(P+'obligations-v1.md')).read_text(),re.M)
assert ids==[f'{n:02d}'for n in range(1,37)]
assert 'Candidate proof - unverified' in(ROOT/(P+'candidate-v1.md')).read_text()
ordered=[unique[p]for p in sorted(unique)]
summary=dict(occurrences=len(rows),unique_paths=len(ordered),sha256=sha256(
    json.dumps(ordered,sort_keys=True,separators=(',',':')).encode()).hexdigest())
out('baseline-v1.json',dict(captured_at_utc=NOW,compact_own_parent=parent,
    summary=summary,records=ordered,occurrence_labels=[dict(label=x['label'],path=x['path'])for x in rows],
    unrelated_old_history_recursively_rehashed_or_recopied=False))
out('metadata-v1.json',dict(status='candidate proof - unverified; ENTIRE FP0–FP2 constructor',
    constructor='/root',root_is_EXCLUDED_from_TWO_OTHER_audit_count=True,
    requested_model='gpt-6.1-sol',requested_reasoning='max',verified_effective_settings=None,
    whole_obligations=36,claims=['FP0 six-line multiplicity/tangent constraint',
    'FP1 no absolute factor degree2q+9 through5q-11',
    'FP2 unique dominant F2-defined absolute component degree at least5q-10'],
    domain=dict(q='8^k',k_minimum=2,n='7q+1',q_minimum=64),
    all_projective_singularities_and_local_cones_reconstructed=True,
    FP1_uses_global_offdiagonal_maximum_not_FP0_extra_bound=True,
    published_qualitative_F2_component_existence_attributed=True,
    small_nonconstant_cofactor_possible_ordinary_reducibility_OPEN=True,
    new_numerical_factorization_annual_or_novelty_claim=False,
    mathematical_code_CAS_scan_factor_table_or_author_rerun=False,
    source_limits=P+'source-audit-v1.md',new_third_party_pdf_downloads=0,
    peer_NEW_FP_reports_findings_metadata_read_or_hashed=False,
    all_old_proofs_reviews_shared_cache_Git_bytes_preserved_by_this_packet=True,
    preliminary_part_a_reproduced_or_investigated=False,
    latest_budget=dict(at_utc='2026-10-18 06:29:15 UTC',source='A direct account meter',
        weekly_used_percent_TOTAL=11,window_minutes=10080,reset_unix=1792874445,
        ordinary_usage_allowed=True,current_window_user_authorized=True,
        ceiling_TOTAL_with_integration_reserve=90,automatic_later_reset_spending=False)))
for path,row in unique.items(): assert rec(path)==row,path
out('input-validation-v1.json',dict(validated_at_utc=NOW,summary=summary,
    exact_current_inputs_match_before_and_after_new_writes=True,
    accepted_NF_copy_has_exact_old_candidate_suffix=True,all36_obligation_IDs_in_order=True,
    no_old_inventory_recursive_rehash=True,administrative_integrity_not_mathematical_testing=True))
suffixes=['candidate-v1.md','obligations-v1.md','source-audit-v1.md','failed-routes-worklog-v1.md',
    'freeze-v1.py','baseline-v1.json','metadata-v1.json','input-validation-v1.json']
out('freeze-v1.json',dict(frozen_at_utc=NOW,status='ENTIRE FP0–FP2 constructor - candidate proof unverified',
    constructor='/root',constructor_excluded_from_TWO_OTHER_whole_audits=True,
    all_obligations=36,compact_own_parent=parent,current_input_summary=summary,
    no_NEW_peer_FP_findings_before_ENTIRE_freeze=True,
    full_main_sources_failed_routes_worklog_code_ALL_metadata_frozen=True,
    ordinary_reducibility_small_cofactor_and_annual_still_OPEN=True,
    artifacts=[rec(P+s)for s in suffixes]))
for path,row in unique.items(): assert rec(path)==row,path
print(json.dumps(dict(freeze=rec(P+'freeze-v1.json'),main=rec(P+'candidate-v1.md'),
    all_obligations=36,summary=summary,promotion=False),indent=2))
