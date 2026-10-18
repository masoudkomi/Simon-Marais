#!/usr/bin/env python3
"""One-shot administrative hash/text/JSON freeze; no mathematics or replay."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import difflib
import re

ROOT=Path(__file__).resolve().parents[3]
P='problems/2025-B4/reviews/reasoning-return-r9-review-2-reaudit-v1.1-'
N='problems/2025-B4/notes/reasoning-return-r9-'

def fp(path):
    b=(ROOT/path).read_bytes()
    return dict(path=path,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())

def check(row):
    assert fp(row['path'])=={k:row[k] for k in ('path','bytes','sha256')},row['path']

def new(suffix,x):
    with (ROOT/(P+suffix)).open('x',encoding='utf-8') as f:
        json.dump(x,f,indent=2,ensure_ascii=False);f.write('\n')

def unique(rows):
    out={}
    for row in rows:
        core={k:row[k] for k in ('path','bytes','sha256')}
        assert out.setdefault(row['path'],core)==core
    return [out[k] for k in sorted(out)]

def digest(rows):
    return hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(',',':')).encode()).hexdigest()

base=json.loads((ROOT/(P+'baseline-v1.json')).read_text())
check(base['exact_target']);check(base['constructor_freeze'])
c=json.loads((ROOT/base['constructor_freeze']['path']).read_text())
crows=[base['constructor_freeze']]+c['artifacts']
assert len(crows)==12 and c['full_obligations']==56
check(base['author_preservation_baseline'])
arows=json.loads((ROOT/base['author_preservation_baseline']['path']).read_text())['records']
assert len(arows)==35
check(base['original_own_whole_baseline'])
original_base=json.loads((ROOT/base['original_own_whole_baseline']['path']).read_text())
inputs=original_base['necessary_current_context_records']
assert len(inputs)==28
check(base['immediate_own_parent_manifest'])
par=json.loads((ROOT/base['immediate_own_parent_manifest']['path']).read_text())
prows=[base['immediate_own_parent_manifest']]+par['artifacts']
assert len(prows)==9 and par['older_plus_new_own_paths_bound_transitively']==493
rows=crows+arows+inputs+prows
dedup=unique(rows)
for row in dedup:
    assert 'reasoning-return-r9-review-1-reaudit' not in row['path']
    check(row)

old=(ROOT/(N+'candidate-v1.md')).read_text()
replacement=(ROOT/(N+'candidate-v1.1.md')).read_text()
def segment(txt,start,end=None):
    tail=txt.split(start,1)[1]
    return tail if end is None else tail.split(end,1)[0]
blocks={}
for name,start,end in [('sections1_to3','## 1.','## 4.'),
                       ('sections5_to6','## 5.','## 7.'),
                       ('section8','## 8.',None),
                       ('cofactor','A safe replacement is elementary.','## 5.')]:
    a,b=segment(old,start,end),segment(replacement,start,end)
    assert a==b,name
    blocks[name]=dict(byte_identical=True,sha256=hashlib.sha256(a.encode()).hexdigest())
diff=[]
for stem in ('candidate','obligations','sources','failed-routes','worklog'):
    a,b=N+stem+'-v1.md',N+stem+'-v1.1.md'
    diff.extend(difflib.unified_diff((ROOT/a).read_text().splitlines(keepends=True),
                                    (ROOT/b).read_text().splitlines(keepends=True),
                                    fromfile=a,tofile=b))
assert ''.join(diff)==(ROOT/(N+'diff-v1-to-v1.1.patch')).read_text()
ledger=(ROOT/(P+'ledger-v1.md')).read_text()
tags=re.findall(r'^\|R9-(\d{2})\|Pass\|',ledger,re.M)
assert tags==[f'{i:02d}' for i in range(1,57)]
assert 'Unresolved substantive issues: 0' in (ROOT/(P+'issues-v1.md')).read_text()

validation=dict(verified_at_utc=datetime.now(timezone.utc).isoformat(),
    administrative_only_hash_textdiff_JSON_tags_no_mathcode=True,
    repair_manifest_and_payloads_verified=len(crows),
    author_declared_old_records_verified=len(arows),
    selected_original_necessary_current_context_records_verified=len(inputs),
    immediate_own_parent_manifest_and_payloads_verified=len(prows),
    fingerprint_occurrences_verified=len(rows),unique_paths_verified=len(dedup),
    canonical_deduplicated_summary_sha256=digest(dedup),
    unchanged_mathematical_blocks=blocks,five_file_diff_independently_text_reconstructed=True,
    all56_original_plus_affected_ledger_tags_present_once_in_order=True,
    radius_issues_R9R1_01_R9R2_01_resolved=True,
    N3_correct_chosen_generator_scope_explicit_everywhere=True,
    unresolved_substantive_issues=0,further_author_repairs_required=0,retained_scope_notes=4,
    original_countercertificate_and_both_initials_preserved=True,
    NEW_root_affected_review_files_findings_or_metadata_unopened_through_ENTIRE_own_freeze=True,
    root_identity_only_message_received_without_findings=True,
    no_later_Runge_live_or_new_2022_math_used_as_premise=True,
    older_own_paths_bound_transitively=493,new_own_files_including_manifest=9,
    older_plus_new_own_paths_bound_transitively=502,
    old_inventory_bound_not_recopied_or_recursively_rehashed=True,
    no_old_shared_Git_cache_edit_spawn_contact_charge_bypass_or_mathematical_program=True,
    requested_settings=base['requested_settings'],independently_verified_effective_settings=None,
    authoritative_weekly_telemetry=base['telemetry'])
new('input-validation-v1.json',validation)
payloads=[fp(P+s) for s in ('baseline-v1.json','initial.md','ledger-v1.md','issues-v1.md',
                          'source-checks-v1.md','sources-v1.json','freeze-v1.py','input-validation-v1.json')]
manifest=dict(frozen_at_utc=datetime.now(timezone.utc).isoformat(),
    status='COMPLETE OTHER NONCONSTRUCTOR affected WHOLE R9v1.1 reaudit2; radius repaired and N3 scope explicit; not coordinator promotion',
    reviewer='/root/review_2022_complexity_r2',exact_target=base['exact_target'],
    exact_constructor_freeze=base['constructor_freeze'],
    all_six_claims_and_all48_original_plus8_affected_obligations_checked=True,
    issues_R9R1_01_R9R2_01_disposition='resolved in explicit author equality/nonzero radius split',
    N3_disposition='chosen a0^p nonlinearity only; no ideal-level all-generator exclusion',
    unresolved_substantive_issues=0,further_author_repairs_required=0,retained_scope_notes=4,
    original_countercertificate_and_both_whole_initials_preserved=True,
    entire_unchanged_arithmetic_chain_and_both_evaluation_branches_retained=True,
    no_actual_solution_new_exclusion_useful_unconditional_height_annual_or_source_theorem_refutation_claim=True,
    NEW_root_affected_review_material_unopened_through_ENTIRE_own_freeze=True,
    identity_only_message_received_without_findings=True,
    C_NEW_constructor_excluded=True,B_did_not_construct_NEW_R9_or_author_repair=True,
    B_old_R8_UW_authorship_and_R6_R7_reviews_disclosed_no_self_recertification=True,
    B_old_adversarial_radius_certificate_and_unit_diagnostic_explicitly_attributed=True,
    BOTH_OTHER_affected_reaudits_and_root_full_reconciliation_required=True,
    exact_fresh_vs_original_source_read_limits_recorded=True,
    no_new_Runge_or_live_math_premise=True,
    fingerprint_occurrences_verified=len(rows),unique_paths_verified=len(dedup),
    canonical_deduplicated_summary_sha256=digest(dedup),
    compact_own_parent_manifest=base['immediate_own_parent_manifest'],
    older_own_paths_bound_transitively=493,new_own_files_including_manifest=9,
    older_plus_new_own_paths_bound_transitively=502,
    no_growing_old_inventory_recopied_or_recursively_rehashed=True,
    no_mathcode_CAS_scan_native_child_author_rerun_or_old_certificate_replay=True,
    no_old_shared_Git_cache_edit_spawn_contact_charge_or_bypass=True,
    requested_settings=base['requested_settings'],independently_verified_effective_settings=None,
    authoritative_weekly_telemetry=base['telemetry'],artifacts=payloads)
new('manifest-v1.json',manifest)
for r in payloads+dedup:check(r)
print(json.dumps(dict(complete=True,manifest=fp(P+'manifest-v1.json'),
                     validation=fp(P+'input-validation-v1.json'),obligations=56,
                     issues=0,repairs=0,verified_occurrences=len(rows),unique_paths=len(dedup)),indent=2))
