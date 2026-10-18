#!/usr/bin/env python3
"""Metadata/text preservation only; no mathematical program or author rerun."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import difflib
import re

ROOT = Path(__file__).resolve().parents[3]
P = 'problems/2017-B4/reviews/reasoning-value-return-r6-review-2-reaudit-v1.1-'
N = 'problems/2017-B4/notes/reasoning-value-return-r6-'

def fp(path):
    raw = (ROOT / path).read_bytes()
    return dict(path=path, bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())

def check(row):
    assert fp(row['path']) == {k: row[k] for k in ('path','bytes','sha256')}, row['path']

def write_new(suffix, obj):
    with (ROOT / (P + suffix)).open('x', encoding='utf-8') as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
        f.write('\n')

def unique(rows):
    out = {}
    for r in rows:
        core = {k:r[k] for k in ('path','bytes','sha256')}
        assert out.setdefault(r['path'], core) == core
    return [out[k] for k in sorted(out)]

def digest(rows):
    raw = json.dumps(rows, sort_keys=True, separators=(',',':')).encode()
    return hashlib.sha256(raw).hexdigest()

base = json.loads((ROOT / (P + 'baseline-v1.json')).read_text())
check(base['exact_target']); check(base['constructor_freeze'])
new_freeze = json.loads((ROOT / base['constructor_freeze']['path']).read_text())
new_rows = [base['constructor_freeze']] + new_freeze['artifacts']
assert len(new_rows) == 12 and new_freeze['full_obligations'] == 60

check(base['constructor_preservation_metadata'])
old_rows = json.loads((ROOT / base['constructor_preservation_metadata']['path']).read_text())['records']
assert len(old_rows) == 38
check(base['original_own_whole_baseline'])
old_own = json.loads((ROOT / base['original_own_whole_baseline']['path']).read_text())
authority_rows = old_own['necessary_current_inputs']
assert len(authority_rows) == 22
check(base['immediate_own_parent_manifest'])
parent = json.loads((ROOT / base['immediate_own_parent_manifest']['path']).read_text())
parent_rows = [base['immediate_own_parent_manifest']] + parent['artifacts']
assert len(parent_rows) == 9 and parent['older_plus_new_own_paths_bound_transitively'] == 484

rows = new_rows + old_rows + authority_rows + parent_rows
dedup = unique(rows)
for row in dedup:
    assert 'reasoning-value-return-r6-review-1-reaudit' not in row['path']
    check(row)

old = (ROOT / (N + 'candidate-v1.md')).read_text()
new = (ROOT / (N + 'candidate-v1.1.md')).read_text()
old_pm1 = old[old.index('## 1.'):old.index('## 4.')]
new_pm1 = new[new.index('## 1.'):new.index('## 4.')]
old_pm4 = old[old.index('## 6.'):]
new_pm4 = new[new.index('## 6.'):]
assert old_pm1 == new_pm1 and old_pm4 == new_pm4
expected_diff = []
for stem in ('candidate','obligations','sources','failures','worklog'):
    a, b = N+stem+'-v1.md', N+stem+'-v1.1.md'
    expected_diff.extend(difflib.unified_diff((ROOT/a).read_text().splitlines(keepends=True),
                                            (ROOT/b).read_text().splitlines(keepends=True),
                                            fromfile=a, tofile=b))
assert ''.join(expected_diff) == (ROOT/(N+'diff-v1-to-v1.1.patch')).read_text()

ledger = (ROOT/(P+'ledger-v1.md')).read_text()
pm = re.findall(r'^\|PM-(\d{2})\|Pass\|', ledger, re.M)
fc = re.findall(r'^\|FC-(\d{2})\|Pass\|', ledger, re.M)
assert pm == [f'{i:02d}' for i in range(1,49)]
assert fc == [f'{i:02d}' for i in range(1,13)]
assert 'Unresolved substantive issues: 0' in (ROOT/(P+'issues-v1.md')).read_text()

validation = dict(
    verified_at_utc=datetime.now(timezone.utc).isoformat(),
    administrative_only_hash_textdiff_tag_JSON_no_mathematical_computation=True,
    complete_repair_manifest_and_payloads_verified=len(new_rows),
    constructor_declared_old_preservation_records_verified=len(old_rows),
    selected_current_original_authority_inputs_verified=len(authority_rows),
    immediate_own_parent_manifest_and_payloads_verified=len(parent_rows),
    fingerprint_occurrences_verified=len(rows), unique_paths_verified=len(dedup),
    canonical_deduplicated_summary_sha256=digest(dedup),
    PM1_sections1_to3_byte_identical=True, PM4_section6_to_end_byte_identical=True,
    five_file_author_diff_independently_reconstructed_as_text_only=True,
    PM1_section_sha256=hashlib.sha256(old_pm1.encode()).hexdigest(),
    PM4_section_sha256=hashlib.sha256(old_pm4.encode()).hexdigest(),
    all_original48_and_new12_FC_tags_present_once_in_order=True,
    PMR2_01_resolved_in_author_version=True, unresolved_substantive_issues=0,
    further_author_repairs_required=0, retained_scope_notes=4,
    original_grid_countercertificate_and_both_original_dispositions_preserved=True,
    NEW_A_affected_review_material_unopened_through_ENTIRE_own_freeze=True,
    no_old_shared_Git_cache_write_spawn_contact_charge_bypass_mathcode_CAS_or_author_rerun=True,
    older_own_paths_bound_transitively=484, new_own_files_including_manifest=9,
    older_plus_new_own_paths_bound_transitively=493,
    original_historical_inventories_bound_not_recopied_or_recursively_rehashed=True,
    requested_settings=base['requested_settings'], independently_verified_effective_settings=None,
    authoritative_weekly_telemetry=base['telemetry'])
write_new('input-validation-v1.json',validation)
payloads = [fp(P+s) for s in ('baseline-v1.json','initial.md','ledger-v1.md','issues-v1.md',
                             'source-checks-v1.md','sources-v1.json','freeze-v1.py','input-validation-v1.json')]
manifest = dict(
    frozen_at_utc=datetime.now(timezone.utc).isoformat(),
    status='COMPLETE OTHER NONCONSTRUCTOR affected WHOLE reaudit2; PMR2-01 resolved for fullv1.1; not coordinator promotion',
    reviewer='/root/review_2022_complexity_r2', exact_target=base['exact_target'],
    exact_constructor_freeze=base['constructor_freeze'], affected_claims=['PM2','PM3'],
    all_original48_and_new12_FC_obligations_checked=True,
    original_PM1_PM4_text_and_scope_unchanged=True,
    original_issue='PMR2-01', issue_disposition='resolved in explicit author finite-T/FC repair',
    unresolved_substantive_issues=0, further_author_repairs_required=0, retained_scope_notes=4,
    original_countercertificate_and_both_initial_dispositions_preserved=True,
    no_infinite_angle_source_extension_or_arbitrary_decoration_sufficiency_claim=True,
    entire_PM3_offset_buffer_conditioning_rank_phase_and_q_safe_chain_checked=True,
    NEW_A_affected_review_files_findings_or_metadata_unopened_through_ENTIRE_own_freeze=True,
    root_C_contributors_excluded_from_independent_count=True,
    B_did_not_construct_NEW_R6_or_repair=True,
    B_old_allD_global_authorship_and_local_value_reviews_disclosed_no_self_recertification=True,
    BOTH_OTHER_affected_whole_reaudits_and_root_full_reconciliation_required=True,
    no_upper_R_value_negligible_collar_free_fixed_entropy_equality_annual_or_novelty_claim=True,
    precise_primary_and_internal_actual_read_limits_recorded=True,
    fingerprint_occurrences_verified=len(rows), unique_paths_verified=len(dedup),
    canonical_deduplicated_summary_sha256=digest(dedup),
    compact_own_parent_manifest=base['immediate_own_parent_manifest'],
    older_own_paths_bound_transitively=484,new_own_files_including_manifest=9,
    older_plus_new_own_paths_bound_transitively=493,
    no_growing_historical_inventory_recopied_or_recursively_rehashed=True,
    no_mathcode_scan_CAS_native_child_author_rerun_or_old_certificate_replay=True,
    no_old_shared_Git_cache_edit_spawn_contact_charge_or_bypass=True,
    requested_settings=base['requested_settings'],independently_verified_effective_settings=None,
    authoritative_weekly_telemetry=base['telemetry'],artifacts=payloads)
write_new('manifest-v1.json',manifest)
for r in payloads+dedup:
    check(r)
print(json.dumps(dict(complete=True,manifest=fp(P+'manifest-v1.json'),
                     validation=fp(P+'input-validation-v1.json'),
                     obligations=60,PMR2_01='resolved',issues=0,repairs=0,
                     verified_occurrences=len(rows),unique_paths=len(dedup)),indent=2))
