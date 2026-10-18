#!/usr/bin/env python3
"""Exclusive administrative whole-review freeze; no mathematical computation."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re

ROOT = Path.cwd().resolve()
P = 'problems/2025-B4/reviews/reasoning-Runge-return-r2-review-1-'
C = 'problems/2025-B4/notes/reasoning-Runge-return-r2-'
NOW = datetime.now(timezone.utc).isoformat()
assert ROOT == Path('/Users/uqmkamga/Documents/ChatGPT/Website')

def rec(path):
    b = (ROOT / path).read_bytes()
    return dict(path=path, bytes=len(b), sha256=sha256(b).hexdigest())

def read(path):
    return json.loads((ROOT / path).read_text())

def out(suffix, value):
    with (ROOT / (P + suffix)).open('x', encoding='utf-8') as f:
        json.dump(value, f, indent=2, ensure_ascii=False)
        f.write('\n')

rows = []
unique = {}

def bind(path, label, expected=None):
    assert not path.startswith('problems/2025-B4/reviews/reasoning-Runge-return-r2-review-2-')
    item = rec(path)
    if expected is not None:
        assert item == {k: expected[k] for k in ('path', 'bytes', 'sha256')}, path
    assert path not in unique or unique[path] == item
    unique[path] = item
    rows.append(dict(label=label, **item))
    return item

constructor = bind(C + 'freeze-v1.json', 'exact complete ten-file constructor identity', dict(
    path=C + 'freeze-v1.json', bytes=4617,
    sha256='34bf0623be5cc897f681e0bcaf81c0bd1fc2a57fecc460f4b11177aab29c2e34'))
cf = read(constructor['path'])
assert len(cf['artifacts']) == 9
for item in cf['artifacts']:
    assert item['path'].startswith(C)
    bind(item['path'], 'entire current constructor payload', item)
cb = read(C + 'baseline-v1.json')
assert cb['protected_unique_paths'] == 22
assert cb['protected_declared_occurrences_including_parent_binding'] == 23
assert cb['canonical_protected_summary_sha256'] == sha256(json.dumps(
    cb['protected_inputs'], sort_keys=True, separators=(',', ':')).encode()).hexdigest()
for item in cb['protected_inputs']:
    bind(item['path'], 'necessary current declared protected input, nonrecursive', item)
bind(cb['compact_immediate_own_parent']['path'],
     'constructor compact parent repeated declaration', cb['compact_immediate_own_parent'])
# The two mutable context observations are historical metadata only.
assert len(cb['context_only_observed']) == 2

tags = ['original-weight-universal', 'reasoning-return-r6', 'reasoning-return-r8',
        'reasoning-return-r9', 'reasoning-return-r9-runge']
for tag in tags:
    authority = read('problems/2025-B4/reviews/' + tag + '-acceptance.json')
    assert authority['unresolved_substantive_issues'] == 0
    bind(authority['candidate']['path'], 'exact operative accepted historical candidate',
         authority['candidate'])
    bind(authority['accepted_copy']['path'], 'accepted authority repeated body declaration',
         authority['accepted_copy'])
    assert (ROOT / authority['accepted_copy']['path']).read_bytes().endswith(
        (ROOT / authority['candidate']['path']).read_bytes())

parent_path = 'problems/2024-B4/reviews/cofactor-symmetry-r1-review-1-manifest-v1.json'
parent = bind(parent_path, 'compact own preceding complete whole-review parent, no math premise', dict(
    path=parent_path, bytes=2762,
    sha256='a1efa037aada8f0dc638505131e61964bcb6901d894f3a2f2717864cd4f22435'))
pf = read(parent_path)
assert len(pf['artifacts']) == 8
for item in pf['artifacts']:
    assert item['path'].startswith('problems/2024-B4/reviews/cofactor-symmetry-r1-review-1-')
    bind(item['path'], 'compact immutable own-parent payload identity only', item)

expected_ids = [f'{n:02d}' for n in range(1, 61)]
source_ids = re.findall(r'^\| RS-(\d{2}) \|',
    (ROOT / (C + 'obligations-v1.md')).read_text(), re.M)
ledger = (ROOT / (P + 'issues-v1.md')).read_text()
review_ids = re.findall(r'^\| RS-(\d{2}) \|', ledger, re.M)
assert source_ids == review_ids == expected_ids
assert len(re.findall(r'^\| RS-\d{2} \|.*\| Closed \|$', ledger, re.M)) == 60
assert len(re.findall(r'^- \*\*RSR1-N\d', ledger, re.M)) == 7
report = (ROOT / (P + 'initial-v1.md')).read_text()
assert not re.search(r',\+[A-Za-z]', report)
for label in ['RS1', 'RS2', 'RS3', 'RS4']:
    assert label in report

ordered = [unique[path] for path in sorted(unique)]
summary = dict(occurrences=len(rows), unique_paths=len(ordered), sha256=sha256(
    json.dumps(ordered, sort_keys=True, separators=(',', ':')).encode()).hexdigest())
assert summary['occurrences'] == 52 and summary['unique_paths'] == 46
out('baseline-v1.json', dict(captured_at_utc=NOW, entire_constructor=constructor,
    compact_own_parent=parent, summary=summary, records=ordered,
    occurrence_labels=[dict(label=x['label'], path=x['path']) for x in rows],
    historical_inventories_not_recursively_rehashed_or_recopied=True,
    constructor_mutable_context_observations_not_protected_or_rehashed=True,
    previous_FS_review_is_metadata_parent_only_not_mathematical_premise=True,
    NEW_corresponding_peer_RS_files_or_hashes_accessed=False))
out('metadata-v1.json', dict(
    status='ENTIRE initially blind WHOLE RS1-RS4 R1; candidate not promoted',
    reviewer='/root/review_2021_reasoning_j15_r2',
    constructors_excluded=['/root/review_2022_complexity_r2', '/root'],
    requested_model='gpt-6.1-sol', requested_reasoning='max',
    independently_verified_effective_settings=None,
    all_whole_obligations=60, closed_obligations=60,
    substantive_defects=0, unresolved_issues=0, required_author_repairs=0,
    closed_scope_notes=7, combined_obligation_issue_ledger=P + 'issues-v1.md',
    complete_connected_whole_hand_reconstruction=True,
    original_analytic_operative_proof_read_with_external_finite_component_retained=True,
    raw_source_computations_reproved_or_replayed=False,
    all_five_accepted_bodies_and_all_ten_authority_records_read=True,
    old_UW_RG_and_original_weight_reviewer_roles_disclosed_not_recertification=True,
    NEW_RS_construction_inference_supplied_by_reviewer=False,
    unverified_root_quotient_note_not_accepted_premise=True,
    NEW_corresponding_peer_RS_findings_files_ledgers_sources_code_metadata_or_hashes_seen=False,
    peer_completion_identity_only_received_before_own_freeze=True,
    mathematical_verdict_withheld_until_BOTH_entire_initials_release=True,
    completion_identity_only_after_entire_metadata_read=True,
    no_mathematical_code_CAS_scan_author_rerun_L_value_RR_or_certificate_replay=True,
    administrative_integrity_only=True, all_old_shared_Git_cache_bytes_preserved=True,
    new_source_PDF_binary_hashes=None,
    full_external_analytic_foundations_or_entire_textbook_audit_claim=False,
    fixed_support_r0_not_forced_by_actual_solution=True,
    no_new_useful_X_bound_prime_exclusion_all_generator_or_annual_claim=True,
    no_preliminary_part_a_research_or_novelty_claim=True,
    budget=dict(source='direct authoritative get_usage_limits',
        observed_at_utc='2026-10-18 08:04:40 UTC', weekly_used_percent_TOTAL=16,
        window_minutes=10080, reset_unix=1792874445, ordinary_usage_allowed=True,
        legacy_and_by_limit_views_agree=True, account_suffix='ac3a',
        explicitly_authorized_current_window=True, stopping_ceiling_percent_TOTAL=90,
        integration_reserve=True, automatic_later_window_spending=False)))
for path, item in unique.items():
    assert rec(path) == item, path
out('input-validation-v1.json', dict(validated_at_utc=NOW, summary=summary,
    all9_constructor_payloads_verified=True, all22_protected_input_paths_verified=True,
    constructor_repeated_parent_and_five_repeated_body_declarations_verified=True,
    five_accepted_historical_candidate_identities_and_exact_suffixes_verified=True,
    all8_compact_own_parent_payloads_verified=True,
    all60_constructor_and_review_IDs_in_order=True, all60_dispositions_closed=True,
    seven_closed_scope_notes=True,
    all_necessary_current_inputs_unchanged_before_and_after_new_writes=True,
    no_recursive_historical_inventory_or_mutable_context_freeze=True,
    no_NEW_corresponding_peer_RS_file_or_hash_access=True,
    administrative_integrity_not_mathematical_testing=True))
payloads = ['initial-v1.md', 'issues-v1.md', 'sources-v1.md', 'worklog-v1.md',
            'freeze-v1.py', 'baseline-v1.json', 'metadata-v1.json', 'input-validation-v1.json']
out('manifest-v1.json', dict(frozen_at_utc=NOW,
    status='ENTIRE initially blind WHOLE RS1-RS4 R1 frozen; no promotion',
    reviewer='/root/review_2021_reasoning_j15_r2', entire_constructor=constructor,
    all_whole_obligations=60, compact_own_parent=parent, current_input_summary=summary,
    complete_main_report_ledger_issues_sources_worklog_code_ALL_metadata=True,
    NEW_corresponding_peer_RS_files_findings_or_hashes_seen_before_entire_freeze=False,
    mathematical_verdict_withheld_until_both_initials_release=True,
    only_completion_identity_to_be_released=True,
    artifacts=[rec(P + suffix) for suffix in payloads]))
for path, item in unique.items():
    assert rec(path) == item, path
print(json.dumps(dict(manifest=rec(P + 'manifest-v1.json'),
    report=rec(P + 'initial-v1.md'), all_obligations=60,
    current_input_summary=summary, completion_identity_only=True), indent=2))
