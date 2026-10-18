#!/usr/bin/env python3
"""Exclusive administrative review freeze; no mathematical computation."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re

ROOT = Path.cwd().resolve()
P = 'problems/2024-B4/reviews/cofactor-symmetry-r1-review-1-'
C = 'problems/2024-B4/notes/cofactor-symmetry-r1-'
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
    assert not path.startswith('problems/2024-B4/reviews/cofactor-symmetry-r1-review-2-')
    row = rec(path)
    if expected is not None:
        assert row == {k: expected[k] for k in ('path', 'bytes', 'sha256')}, path
    assert path not in unique or unique[path] == row
    unique[path] = row
    rows.append(dict(label=label, **row))
    return row

constructor = bind(C + 'freeze-v1.json', 'entire frozen constructor identity', dict(
    path=C + 'freeze-v1.json', bytes=2406,
    sha256='2fdb3fc025f2bf89e6d3bdf060373103fecf428db8ff4f407f170bed86bab327'))
cf = read(constructor['path'])
assert cf['all_obligations'] == 48 and len(cf['artifacts']) == 8
for item in cf['artifacts']:
    assert item['path'].startswith(C)
    bind(item['path'], 'current complete constructor payload', item)
cb = read(C + 'baseline-v1.json')
assert cb['summary']['occurrences'] == 18 and len(cb['records']) == 18
for item in cb['records']:
    bind(item['path'], 'constructor declared necessary current binding, nonrecursive', item)
assert cb['summary']['sha256'] == sha256(json.dumps(
    cb['records'], sort_keys=True, separators=(',', ':')).encode()).hexdigest()

parent_path = 'problems/2019-B4/reviews/reasoning-growth-return-r1-review-2-manifest-v1.json'
parent = bind(parent_path, 'compact immediately previous own entire whole-review parent', dict(
    path=parent_path, bytes=2908,
    sha256='8363737a4ea876d9cc1a1d00d58923b54770380ab2c95db7f42d34353acac2b5'))
pf = read(parent_path)
assert len(pf['artifacts']) == 8
for item in pf['artifacts']:
    assert item['path'].startswith('problems/2019-B4/reviews/reasoning-growth-return-r1-review-2-')
    bind(item['path'], 'compact immutable own-parent payload identity', item)

for name in ['coordinator-F8-pencil-r1', 'coordinator-neighbor-Frobenius-r1']:
    authority = read('problems/2024-B4/reviews/' + name + '-acceptance.json')
    assert authority['unresolved_substantive_issues'] == 0
    assert (ROOT / authority['accepted_copy']['path']).read_bytes().endswith(
        (ROOT / authority['candidate']['path']).read_bytes())
structural = read('problems/2024-B4/reviews/structural-acceptance.json')
assert structural['remaining_substantive_objections'] == 0

source_ids = re.findall(r'^\|(\d{2})\|', (ROOT / (C + 'obligations-v1.md')).read_text(), re.M)
ledger_text = (ROOT / (P + 'issues-v1.md')).read_text()
review_ids = re.findall(r'^\| (\d{2}) \|', ledger_text, re.M)
expected_ids = [f'{n:02d}' for n in range(1, 49)]
assert source_ids == review_ids == expected_ids
assert len(re.findall(r'^- \*\*FSR1-N\d', ledger_text, re.M)) == 5
assert len(re.findall(r'^\| \d{2} \|.*\| Closed \|$', ledger_text, re.M)) == 48
report = (ROOT / (P + 'initial-v1.md')).read_text()
assert not re.search(r',\+[A-Za-z]', report)
assert 'candidate proof -' in report and 'No mathematical' in report

ordered = [unique[path] for path in sorted(unique)]
summary = dict(occurrences=len(rows), unique_paths=len(ordered), sha256=sha256(
    json.dumps(ordered, sort_keys=True, separators=(',', ':')).encode()).hexdigest())
assert summary['occurrences'] == summary['unique_paths'] == 36
out('baseline-v1.json', dict(captured_at_utc=NOW,
    entire_constructor=constructor, compact_own_parent=parent, summary=summary,
    records=ordered, occurrence_labels=[dict(label=x['label'], path=x['path']) for x in rows],
    unrelated_historical_inventories_recopied_or_recursively_rehashed=False,
    NEW_corresponding_peer_FS_files_opened_or_hashed=False))
out('metadata-v1.json', dict(
    status='ENTIRE initially blind WHOLE FS1-FS5 R1 initial; candidate not promoted',
    reviewer='/root/review_2021_reasoning_j15_r2', constructor='/root',
    constructor_excluded_from_TWO_OTHER_whole_audits=True,
    requested_model='gpt-6.1-sol', requested_reasoning='max',
    verified_effective_settings=None, all_obligations=48, closed_obligations=48,
    substantive_defects=0, unresolved_issues=0, required_author_repairs=0,
    closed_scope_notes=5,
    combined_obligation_issue_ledger=P + 'issues-v1.md',
    full_whole_hand_reconstruction=True,
    old_roles=['accepted T1-T4 author', 'older NF whole R1', 'older FP whole R1'],
    old_accepted_inputs_not_newly_self_certified=True,
    pretarget_work_only_generic_source_and_old_input_preparation=True,
    no_NEW_problem_specific_constructor_inference_supplied=True,
    NEW_corresponding_peer_FS_findings_files_ledgers_sources_code_metadata_or_hashes_seen=False,
    mathematical_verdict_withheld_until_BOTH_entire_initials_frozen=True,
    release_identity_only_after_entire_metadata_read=True,
    no_mathematical_code_CAS_scan_author_rerun_or_certificate_replay=True,
    administrative_bytes_JSON_labels_suffix_checks_only=True,
    old_shared_Git_cache_bytes_preserved=True,
    downloaded_Fulton_PDF_binary_sha256=None,
    whole_book_or_complete_external_foundations_audit_claimed=False,
    preliminary_part_a_researched_or_reproduced=False,
    annual_classification_or_novelty_claim=False,
    budget=dict(source='direct authoritative get_usage_limits',
        observed_at_utc='2026-10-18 07:42:43 UTC', weekly_used_percent_TOTAL=14,
        window_minutes=10080, reset_unix=1792874445, ordinary_usage_allowed=True,
        legacy_and_by_limit_agree=True, account_suffix='ac3a',
        current_window_explicitly_authorized=True, stopping_ceiling_percent_TOTAL=90,
        integration_reserve_required=True, automatic_later_reset_spending=False)))
for path, expected in unique.items():
    assert rec(path) == expected, path
out('input-validation-v1.json', dict(validated_at_utc=NOW, summary=summary,
    constructor_payloads_verified=8, constructor_declared_current_inputs_verified=18,
    compact_own_parent_payloads_verified=8,
    all48_constructor_and_review_IDs_in_exact_order=True,
    all48_dispositions_closed=True, five_closed_scope_notes=True,
    accepted_FP_NF_exact_historical_candidate_suffixes_match=True,
    structural_editorial_heading_change_disclosed_no_false_suffix_assertion=True,
    current_input_bytes_match_before_and_after_new_review_writes=True,
    only_necessary_current_parent_bindings_not_recursive_inventory=True,
    NEW_corresponding_peer_FS_paths_opened_or_hashed=False,
    administrative_integrity_not_mathematical_testing=True))

payloads = ['initial-v1.md', 'issues-v1.md', 'sources-v1.md', 'worklog-v1.md',
            'freeze-v1.py', 'baseline-v1.json', 'metadata-v1.json', 'input-validation-v1.json']
out('manifest-v1.json', dict(frozen_at_utc=NOW,
    status='ENTIRE initially blind WHOLE FS1-FS5 R1 initial frozen; no promotion',
    reviewer='/root/review_2021_reasoning_j15_r2', entire_constructor=constructor,
    all_obligations=48, compact_own_parent=parent, current_input_summary=summary,
    complete_report_combined_ledger_issues_sources_worklog_code_ALL_metadata=True,
    NEW_corresponding_peer_FS_material_seen_or_hashed_before_entire_freeze=False,
    mathematical_verdict_not_released_until_BOTH_initials_frozen=True,
    only_completion_identity_to_be_released=True,
    artifacts=[rec(P + suffix) for suffix in payloads]))
for path, expected in unique.items():
    assert rec(path) == expected, path
print(json.dumps(dict(manifest=rec(P + 'manifest-v1.json'),
    report=rec(P + 'initial-v1.md'), all_obligations=48,
    current_input_summary=summary, completion_identity_only=True), indent=2))
