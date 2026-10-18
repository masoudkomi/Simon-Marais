#!/usr/bin/env python3
"""Exclusive administrative WHOLE-review freeze; NO mathematical computation."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re

ROOT=Path.cwd().resolve()
P='problems/2025-B4/reviews/reasoning-Runge-return-r2-review-2-'
C='problems/2025-B4/notes/reasoning-Runge-return-r2-'
FORBIDDEN='problems/2025-B4/reviews/reasoning-Runge-return-r2-review-1-'
NOW=datetime.now(timezone.utc).isoformat()
assert ROOT.name=='Website' and (ROOT/'AGENTS.md').is_file()

def rec(path):
    assert not path.startswith(FORBIDDEN), 'NEW corresponding peer material forbidden'
    b=(ROOT/path).read_bytes()
    return dict(path=path,bytes=len(b),sha256=sha256(b).hexdigest())

def read(path):
    assert not path.startswith(FORBIDDEN)
    return json.loads((ROOT/path).read_text())

def out(suffix,value):
    with (ROOT/(P+suffix)).open('x',encoding='utf-8') as f:
        json.dump(value,f,indent=2,ensure_ascii=False)
        f.write('\n')

unique={}
occurrences=[]
def bind(path,label,expected=None):
    row=rec(path)
    if expected is not None:
        assert row=={k:expected[k] for k in ('path','bytes','sha256')},path
    assert path not in unique or unique[path]==row,path
    unique[path]=row
    occurrences.append(dict(path=path,label=label))
    return row

constructor=bind(C+'freeze-v1.json','ENTIRE exact constructor freeze',dict(
    path=C+'freeze-v1.json',bytes=4617,
    sha256='34bf0623be5cc897f681e0bcaf81c0bd1fc2a57fecc460f4b11177aab29c2e34'))
cf=read(C+'freeze-v1.json')
assert len(cf['artifacts'])==9
for row in cf['artifacts']:
    assert row['path'].startswith(C)
    bind(row['path'],'exact constructor artifact',row)
assert rec(C+'candidate-v1.md')==dict(path=C+'candidate-v1.md',bytes=22619,
    sha256='118ec93c2f8f34778dbf5160a38a854c6ded136684e846d986a6c3d9ddf859c0')
cb=read(C+'baseline-v1.json')
assert len(cb['protected_inputs'])==cb['protected_unique_paths']==22
assert cf['protected_input_unique_paths']==22
assert cb['protected_declared_occurrences_including_parent_binding']==23
assert cf['protected_declared_occurrences_including_parent']==23
assert sha256(json.dumps(cb['protected_inputs'],sort_keys=True,
    separators=(',',':')).encode()).hexdigest()==cb['canonical_protected_summary_sha256']
assert cf['canonical_protected_summary_sha256']==cb['canonical_protected_summary_sha256']
for row in cb['protected_inputs']:
    bind(row['path'],'declared constructor protected OLD input',row)
bind(cb['compact_immediate_own_parent']['path'],
    'declared repeated constructor compact-parent binding',cb['compact_immediate_own_parent'])
assert read(cb['compact_immediate_own_parent']['path'])['older_plus_new_own_paths_bound_transitively']==574
assert len(cb['context_only_observed'])==cf['context_only_mutable_observations']==2

own_path='problems/2024-B4/reviews/cofactor-symmetry-r1-review-2-manifest-v1.json'
own_parent=bind(own_path,'compact immutable immediate own parent',dict(path=own_path,
    bytes=3044,sha256='dd7aca7dd7f4609dc83f6a7a5024cae8e6dd7e400a55bbaf78b5f247924a083c'))
own=read(own_path)
assert own['own_paths_after_this_packet']==622
for row in own['artifacts']:
    if row['path'].endswith(('metadata-v1.json','input-validation-v1.json')):
        bind(row['path'],'necessary compact own-parent metadata',row)

authority_paths=[
    'problems/2025-B4/reviews/original-weight-universal-acceptance.json',
    'problems/2025-B4/reviews/reasoning-return-r6-acceptance.json',
    'problems/2025-B4/reviews/reasoning-return-r8-acceptance.json',
    'problems/2025-B4/reviews/reasoning-return-r9-acceptance.json',
    'problems/2025-B4/reviews/reasoning-return-r9-runge-acceptance.json']
for path in authority_paths:
    a=read(path)
    assert a['unresolved_substantive_issues']==0
    assert rec(a['accepted_copy']['path'])=={k:a['accepted_copy'][k] for k in ('path','bytes','sha256')}
    bind(a['candidate']['path'],'exact accepted original/repaired candidate identity',a['candidate'])
    assert (ROOT/a['accepted_copy']['path']).read_bytes().endswith(
        (ROOT/a['candidate']['path']).read_bytes())

expected=[f'{i:02d}' for i in range(1,61)]
assert re.findall(r'^\| RS-(\d{2}) \|',(ROOT/(C+'obligations-v1.md')).read_text(),re.M)==expected
assert re.findall(r'^\|RS-(\d{2})\|',(ROOT/(P+'ledger-v1.md')).read_text(),re.M)==expected
assert 'candidate proof - unverified' in (ROOT/(P+'initial-v1.md')).read_text()
ordered=[unique[p] for p in sorted(unique)]
summary=dict(occurrences=len(occurrences),unique_paths=len(ordered),sha256=sha256(
    json.dumps(ordered,sort_keys=True,separators=(',',':')).encode()).hexdigest())
assert len(occurrences)==41 and len(ordered)==40

out('baseline-v1.json',dict(captured_at_utc=NOW,
    operation='direct bytes/SHA/JSON; administrative only, not mathematics',
    constructor_freeze=constructor,compact_own_parent=own_parent,
    summary=summary,records=ordered,occurrence_labels=occurrences,
    constructor_protected_inputs=22,constructor_protected_occurrences_including_parent=23,
    historical_mutable_context_observations=cb['context_only_observed'],
    current_mutable_context_files_opened_hashed_or_used_as_mathematical_premises=False,
    no_recursive_old_inventory_copy_or_rehash=True,
    NEW_corresponding_peer_material_read_or_hashed=False))

out('metadata-v1.json',dict(status='ENTIRE initially blind OTHER WHOLE RS1–RS4 R2 frozen',
    reviewer='/root/review_2017_coarsening_r1',constructor='/root/review_2022_complexity_r2',
    root_quotient_contributor=True,B_and_root_EXCLUDED=True,
    reviewer_no_NEW_RS_construction_contribution=True,
    old_R6_R9_RG_authorship_UW_R8_review_roles_disclosed=True,
    not_fresh_independent_recertification_of_own_old_inputs=True,
    requested_settings=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),
    independently_verified_effective_settings=None,
    whole_obligations=60,all60_reconstructed=True,
    substantive_issues=0,required_mathematical_repairs=0,
    closed_source_normalization_clarifications=1,
    mathematical_verdict_withheld_until_BOTH_ENTIRE_initials_confirmed=True,
    no_NEW_corresponding_peer_report_findings_hash_metadata_read=True,
    no_unaccepted_FS_result_used_as_premise=True,
    exact_domain=dict(official='2025 B4(b) only',p='prime>=37',
        X='ordinary integer, either sign, abs(X)>=2',e='0 only',
        norm_field='E=Q(zeta_(p-1)), degree Euler_phi(p-1)',
        Jacobi_field='K=Q(zeta_p), degree p-1'),
    primary_source=dict(original_Louboutin_Cor2_and_entire_operative_proof_read=True,
        later_MST_entire_section5_and_exact_conductor_context_read=True,
        source_finite_L_certificate_external_not_replayed=True,
        Levin_entire_operative_section2_read_no_new_bound_import=True,
        no_full_book_all_source_chain_or_new_PDF_byte_hash_claim=True),
    no_mathematical_program_CAS_scan_RR_L_value_or_author_rerun=True,
    no_old_shared_Git_cache_mutation_spawn_contact_charge_or_bypass=True,
    no_actual_new_exclusion_useful_height_ALL_linear_generator_annual_or_priority_claim=True,
    compact_own_parent=own_parent,prior_own_paths_bound=622,
    new_packet_paths_including_manifest=10,own_paths_after_this_packet=632,
    fingerprint_summary=summary,
    latest_direct_weekly_telemetry=dict(at_utc='2026-10-18 08:00:07 UTC',
        source='mcp__codex_app__get_usage_limits; legacy/by-limit primary agree',
        used_percent_TOTAL=15,window_minutes=10080,reset_unix=1792874445,
        ordinary_usage_allowed=True,current_window_explicitly_human_authorized=True,
        ceiling_percent_TOTAL_with_review_integration_reserve=90,
        automatic_later_reset_spending=False)))

for path,row in unique.items():
    assert rec(path)==row,path
out('input-validation-v1.json',dict(validated_at_utc=NOW,
    administrative_only_not_mathematical_validation=True,
    constructor_all10_artifacts_exact=True,all22_protected_old_inputs_exact=True,
    repeated_constructor_parent_counted=True,five_exact_accepted_candidates_and_suffixes_verified=True,
    all60_author_and_review_ledger_labels_once_in_order=True,
    compact_own_parent=own_parent,prior_own_paths_bound=622,
    fingerprint_summary=summary,current_mutable_context_not_promised_immutable=True,
    no_NEW_corresponding_peer_file_or_metadata_opened_or_hashed=True,
    no_recursive_historical_inventory_copy_or_rehash=True,errors=[]))

suffixes=['initial-v1.md','ledger-v1.md','issues-v1.md','source-checks-v1.md',
    'worklog-v1.md','freeze-v1.py','baseline-v1.json','metadata-v1.json','input-validation-v1.json']
out('manifest-v1.json',dict(frozen_at_utc=NOW,
    status='ENTIRE OTHER initially blind WHOLE RS1–RS4 R2',
    reviewer='/root/review_2017_coarsening_r1',whole_obligations=60,
    full_report_ALL60_ledger_issues_sources_worklog_code_ALL_metadata_frozen=True,
    no_NEW_corresponding_peer_files_findings_hashes_metadata_read_before_ENTIRE_freeze=True,
    mathematical_verdict_withheld_until_BOTH_ENTIRE_initials=True,
    constructor_B_and_root_contributor_EXCLUDED=True,
    old_roles_disclosed_no_independent_self_recertification=True,
    no_mathematical_code_rerun_or_proof_promotion=True,
    constructor_freeze=constructor,compact_own_parent=own_parent,
    prior_own_paths_bound=622,new_packet_paths_including_manifest=10,
    own_paths_after_this_packet=632,fingerprint_summary=summary,
    artifacts=[rec(P+s) for s in suffixes]))
for path,row in unique.items():
    assert rec(path)==row,path
print(json.dumps(dict(manifest=rec(P+'manifest-v1.json'),report=rec(P+'initial-v1.md'),
    whole_obligations=60,input_summary=summary,
    mathematical_verdict='withheld until BOTH entire initial freezes'),indent=2))
