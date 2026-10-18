#!/usr/bin/env python3
"""Exclusive administrative constructor freeze; no mathematical computation."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re

ROOT=Path.cwd().resolve()
P='problems/2024-B4/notes/cofactor-symmetry-r1-'
NOW=datetime.now(timezone.utc).isoformat()
assert ROOT.name=='Website' and (ROOT/'AGENTS.md').is_file()
def rec(path):
    b=(ROOT/path).read_bytes()
    return dict(path=path,bytes=len(b),sha256=sha256(b).hexdigest())
def read(path): return json.loads((ROOT/path).read_text())
def out(suffix,value):
    with (ROOT/(P+suffix)).open('x',encoding='utf-8') as f:
        json.dump(value,f,indent=2,ensure_ascii=False);f.write('\n')
rows=[];unique={}
def bind(path,label,expected=None):
    row=rec(path)
    if expected is not None:
        assert row=={k:expected[k] for k in ('path','bytes','sha256')},path
    assert path not in unique or unique[path]==row
    unique[path]=row;rows.append(dict(label=label,**row));return row

parent_path='problems/2019-B4/reviews/reasoning-growth-return-r1-review-1-manifest-v1.json'
parent=bind(parent_path,'compact own last ENTIRE whole-review parent',dict(
    path=parent_path,bytes=3019,sha256='ac9223020790e586ee46ee3b1e44a56abf6a983172137571c23687e512bf96b3'))
for item in read(parent_path)['artifacts']:
    if item['path'].endswith(('metadata-v1.json','input-validation-v1.json')):
        bind(item['path'],'necessary compact own-parent metadata',item)
bind('problems/2019-B4/reviews/reasoning-growth-return-r1-review-1-metadata-scope-clarification-v1.md',
     'own-parent additive disclosure, no original bytes changed')
for path in ['AGENTS.md','problems/2024-B4/statement.md']:
    bind(path,'protocol and actual official target')
for path,key,suffix_expected in [
    ('problems/2024-B4/reviews/coordinator-F8-pencil-r1-acceptance.json','accepted_copy',True),
    ('problems/2024-B4/reviews/structural-acceptance.json','accepted_proof',False),
    ('problems/2024-B4/reviews/coordinator-neighbor-Frobenius-r1-acceptance.json','accepted_copy',True)]:
    bind(path,'operative accepted-input authority')
    authority=read(path)
    assert authority.get('unresolved_substantive_issues',authority.get('remaining_substantive_objections'))==0
    bind(authority[key]['path'],'operative complete accepted body',authority[key])
    bind(authority['candidate']['path'],'exact accepted historical candidate identity',authority['candidate'])
    md_path=path[:-5]+'.md'
    if (ROOT/md_path).is_file(): bind(md_path,'accepted authority narrative')
    if suffix_expected:
        assert (ROOT/authority[key]['path']).read_bytes().endswith((ROOT/authority['candidate']['path']).read_bytes())
ids=re.findall(r'^\|(\d{2})\|',(ROOT/(P+'obligations-v1.md')).read_text(),re.M)
assert ids==[f'{n:02d}' for n in range(1,49)]
assert 'Candidate proof - unverified' in (ROOT/(P+'candidate-v1.md')).read_text()
ordered=[unique[p] for p in sorted(unique)]
summary=dict(occurrences=len(rows),unique_paths=len(ordered),sha256=sha256(
    json.dumps(ordered,sort_keys=True,separators=(',',':')).encode()).hexdigest())
out('baseline-v1.json',dict(captured_at_utc=NOW,compact_own_parent=parent,summary=summary,
    records=ordered,occurrence_labels=[dict(label=x['label'],path=x['path']) for x in rows],
    unrelated_old_history_recursively_rehashed_or_recopied=False))
out('metadata-v1.json',dict(status='candidate proof - unverified; ENTIRE FS1–FS5 constructor',
    constructor='/root',root_EXCLUDED_from_TWO_OTHER_whole_audits=True,
    requested_model='gpt-6.1-sol',requested_reasoning='max',verified_effective_settings=None,
    all_whole_obligations=48,domain=dict(q='8^k',k_minimum=2,q_minimum=64,n='7q+1'),
    claims=['FS1 exact S4 invariance of actual G/H','FS2 uniform diagonal/off-diagonal multiplicities',
        'FS3 reducible multiplicity bound forces positive integer D',
        'FS4 small-cofactor contradiction, absolute irreducibility for all k>=2',
        'FS5 with accepted NF3 excludes family 7*2^a+1 for a>=2 except a=3'],
    accepted_FP_scope_preserved=True,accepted_T1_is_ABSOLUTE_line_exclusion=True,
    reducible_component_correction_retained=True,
    Fulton_5_4_entire_operative_proof_read_characteristic_2_checked=True,
    no_full_book_read_or_new_third_party_pdf_claim=True,
    prospective_reviewers_only_generic_source_preparation_no_problem_specific_inference=True,
    NEW_FS_peer_reports_findings_metadata_read_or_hashed=False,
    old_unrelated_FP_peer_findings_read_after_their_ENTIRE_freezes=True,
    mathematical_code_CAS_scan_source_author_program_or_certificate_rerun=False,
    all_old_proof_review_shared_Git_bytes_preserved=True,
    preliminary_part_a_investigated_or_reproduced=False,
    annual_answer_or_priority_claim=False,
    latest_budget=dict(at_utc='2026-10-18 07:34:10 UTC',source='B direct account meter',
        weekly_used_percent_TOTAL=14,window_minutes=10080,reset_unix=1792874445,
        ceiling_TOTAL_with_integration_reserve=90,current_window_authorized=True,
        ordinary_usage_allowed=True,automatic_later_reset_spending=False)))
for path,row in unique.items(): assert rec(path)==row,path
out('input-validation-v1.json',dict(validated_at_utc=NOW,summary=summary,
    exact_current_inputs_match_before_and_after_new_writes=True,
    accepted_FP_NF_copies_have_exact_old_candidate_suffix=True,
    accepted_T1_original_heading_editorial_change_disclosed_no_suffix_assertion=True,
    all48_obligation_IDs_in_order=True,no_old_inventory_recursive_rehash=True,
    administrative_integrity_not_mathematical_testing=True))
suffixes=['candidate-v1.md','obligations-v1.md','source-audit-v1.md','failed-routes-worklog-v1.md',
    'freeze-v1.py','baseline-v1.json','metadata-v1.json','input-validation-v1.json']
out('freeze-v1.json',dict(frozen_at_utc=NOW,status='ENTIRE FS1–FS5 constructor - candidate proof unverified',
    constructor='/root',constructor_excluded_from_TWO_OTHER_whole_audits=True,
    all_obligations=48,compact_own_parent=parent,current_input_summary=summary,
    no_NEW_FS_peer_findings_before_ENTIRE_freeze=True,
    full_main_sources_failed_routes_worklog_code_ALL_metadata_frozen=True,
    annual_answer_and_priority_unclaimed=True,
    artifacts=[rec(P+s) for s in suffixes]))
for path,row in unique.items(): assert rec(path)==row,path
print(json.dumps(dict(freeze=rec(P+'freeze-v1.json'),main=rec(P+'candidate-v1.md'),
    all_obligations=48,summary=summary,promotion=False),indent=2))
