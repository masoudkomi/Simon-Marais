#!/usr/bin/env python3
"""Exclusive administrative whole-audit freeze; no mathematical computation."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re

ROOT = Path.cwd().resolve()
P = 'problems/2024-B4/reviews/coordinator-F8-pencil-r1-review-1-'
C = 'problems/2024-B4/notes/coordinator-F8-pencil-r1-'
assert ROOT.name == 'Website' and (ROOT/'AGENTS.md').is_file()

def rec(path):
    raw = (ROOT/path).read_bytes()
    return dict(path=path, bytes=len(raw), sha256=sha256(raw).hexdigest())

def read(path):
    return json.loads((ROOT/path).read_text())

def out(suffix, value):
    with (ROOT/(P+suffix)).open('x', encoding='utf-8') as f:
        json.dump(value, f, indent=2, ensure_ascii=False)
        f.write('\n')

rows = []
unique = {}

def bind(path, label, expected=None):
    actual = rec(path)
    if expected is not None:
        assert actual == {k: expected[k] for k in ('path', 'bytes', 'sha256')}, path
    assert path not in unique or unique[path] == actual, path
    unique[path] = actual
    rows.append(dict(label=label, **actual))
    return actual

constructor_freeze = bind(C+'freeze-v1.json', 'entire constructor freeze', dict(
    path=C+'freeze-v1.json', bytes=2465,
    sha256='3bab98755fd2df8b13ca531e408f1f543762bad9f4289230a9d9668135d45d28'))
constructor = read(C+'freeze-v1.json')
assert len(constructor['artifacts']) == 8 and constructor['all_obligations'] == 36
for item in constructor['artifacts']:
    bind(item['path'], 'entire constructor payload', item)
assert rec(C+'candidate-v1.md') == dict(path=C+'candidate-v1.md', bytes=14313,
    sha256='68accf09323d692e4d4d6850e8c2c04d735d667e1ddaa56cbb73c451fb6402ef')

baseline = read(C+'baseline-v1.json')
for item in baseline['records']:
    bind(item['path'], 'exact constructor current input', item)
baseline_ordered = sorted(baseline['records'], key=lambda item: item['path'])
baseline_digest = sha256(json.dumps(baseline_ordered, sort_keys=True,
    separators=(',', ':')).encode()).hexdigest()
assert baseline_digest == baseline['summary']['sha256']
assert baseline['summary']['occurrences'] == len(baseline['occurrence_labels']) == 12
assert baseline['summary']['unique_paths'] == len(baseline_ordered) == 12

parent_path = 'problems/2022-B4/reviews/reasoning-complexity-return-r9-review-1-v3-manifest-v1.json'
parent = bind(parent_path, 'compact own last entire whole-audit parent', dict(
    path=parent_path, bytes=3969,
    sha256='88ea1178eb20243ad0cf1499fb68123a901bfbad9657f7f5cd2a0636c1311a9f'))
for item in read(parent_path)['artifacts']:
    bind(item['path'], 'compact own parent payload identity only', item)

authority_path = 'problems/2024-B4/reviews/coordinator-neighbor-Frobenius-r1-acceptance.json'
authority = read(authority_path)
for key in ('candidate', 'accepted_copy'):
    bind(authority[key]['path'], 'exact accepted NF body identity', authority[key])
for item in authority['verification_metadata']:
    bind(item['path'], 'old accepted NF declared metadata only', item)
assert (ROOT/authority['accepted_copy']['path']).read_bytes().endswith(
    (ROOT/authority['candidate']['path']).read_bytes())

ids = re.findall(r'^\|(\d{2})\|', (ROOT/(P+'issues-v1.md')).read_text(), re.M)
author_ids = re.findall(r'^\|(\d{2})\|', (ROOT/(C+'obligations-v1.md')).read_text(), re.M)
assert ids == author_ids == [f'{n:02d}' for n in range(1, 37)]
assert len(re.findall(r'^\*\*N[1-5] ', (ROOT/(P+'issues-v1.md')).read_text(), re.M)) == 5
assert 'zero substantive defects' in (ROOT/(P+'initial-v1.md')).read_text()
assert not (ROOT/(P+'manifest-v1.json')).exists()

NOW = datetime.now(timezone.utc).isoformat()
ordered = [unique[path] for path in sorted(unique)]
summary = dict(occurrences=len(rows), unique_paths=len(ordered), sha256=sha256(
    json.dumps(ordered, sort_keys=True, separators=(',', ':')).encode()).hexdigest())
out('baseline-v1.json', dict(captured_at_utc=NOW,
    constructor_freeze=constructor_freeze, compact_own_parent=parent,
    summary=summary, records=ordered,
    occurrence_labels=[dict(label=item['label'], path=item['path']) for item in rows],
    unrelated_parent_inventory_recursively_rehashed_or_recopied=False))
out('metadata-v1.json', dict(status='ENTIRE initially blind OTHER WHOLE R1 frozen',
    reviewer='/root/review_2021_reasoning_j15_r2', constructor='/root',
    root_constructor_excluded_from_TWO_OTHER_audits=True,
    requested_model='gpt-6.1-sol', requested_reasoning='max',
    verified_effective_settings=None, whole_obligations=36,
    inference_dispositions_closed=36, substantive_defects=0, unresolved_issues=0,
    author_repairs_required=0, closed_scope_notes=5,
    NEW_peer_FP_reports_findings_ledger_source_code_metadata_read_or_hashed=False,
    complete_main_companions_code_metadata_read=True,
    all_mathematics_reconstructed_by_hand=True,
    mathematical_code_scan_CAS_author_rerun_or_certificate_replay=False,
    new_third_party_download_cache_write_contact_charge_or_spawn=False,
    older_construction_review_roles_disclosed=True,
    accepted_old_bodies_not_independently_self_recertified=True,
    FP0_proved_separately_from_global_T_optimization_for_FP1=True,
    q8_n57_ordinary_small_cofactor_annual_and_novelty_not_concluded=True,
    no_promotion_or_old_shared_Git_cache_mutation=True,
    compact_input_summary=summary,
    latest_authoritative_budget=dict(at_utc='2026-10-18 06:40:54 UTC',
        tool='mcp__codex_app__get_usage_limits', used_percent_TOTAL=12,
        window_minutes=10080, reset_unix=1792874445,
        ordinaryUsageAllowed=True, legacy_by_limit_agree=True,
        current_window_user_authorized=True,
        ceiling_TOTAL_with_integration_reserve=90,
        automatic_further_window_spending=False)))

for path, expected in unique.items():
    assert rec(path) == expected, path
out('input-validation-v1.json', dict(validated_at_utc=NOW, summary=summary,
    constructor_payloads=8, constructor_manifest_verified=True,
    constructor_declared_current_inputs=12, compact_parent_bound=True,
    accepted_NF_exact_candidate_suffix=True,
    all_declared_necessary_fingerprints_match_before_and_after_new_writes=True,
    all36_author_and_reviewer_obligation_labels_in_order=True,
    five_closed_scope_note_labels=True,
    no_NEW_peer_FP_path_read_or_hashed=True,
    administrative_integrity_only_not_mathematical_testing=True))

payloads = ['initial-v1.md', 'issues-v1.md', 'source-checks-v1.md',
    'worklog-v1.md', 'freeze-v1.py', 'baseline-v1.json', 'metadata-v1.json',
    'input-validation-v1.json']
out('manifest-v1.json', dict(frozen_at_utc=NOW,
    status='ENTIRE initially blind OTHER WHOLE FP0–FP2 R1',
    reviewer='/root/review_2021_reasoning_j15_r2', constructor='/root',
    constructor_excluded_from_independent_review=True,
    whole_obligations=36, substantive_defects=0, unresolved_issues=0,
    author_repairs_required=0, closed_scope_notes=5,
    NEW_peer_FP_reports_findings_metadata_read_or_hashed=False,
    entire_report_ledger_sources_worklog_code_ALL_metadata_frozen=True,
    constructor_freeze=constructor_freeze, compact_own_parent=parent,
    current_input_summary=summary,
    artifacts=[rec(P+suffix) for suffix in payloads],
    mathematical_computation=False, promotion=False))
for path, expected in unique.items():
    assert rec(path) == expected, path
print(json.dumps(dict(manifest=rec(P+'manifest-v1.json'),
    report=rec(P+'initial-v1.md'), ledger=rec(P+'issues-v1.md'),
    whole_obligations=36, substantive_defects=0, repairs_required=0,
    closed_scope_notes=5, input_summary=summary), indent=2))
