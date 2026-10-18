#!/usr/bin/env python3
"""Exclusive administrative whole-review freeze, without mathematical code."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re

ROOT = Path.cwd().resolve()
P = 'problems/2019-B4/reviews/reasoning-growth-return-r1-review-2-'
C = 'problems/2019-B4/notes/reasoning-growth-return-r1-'
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
        assert actual == {k:expected[k] for k in ('path','bytes','sha256')}, path
    assert path not in unique or unique[path] == actual, path
    unique[path] = actual
    rows.append(dict(label=label, **actual))
    return actual

constructor_freeze = bind(C+'freeze-v1.json', 'entire constructor freeze', dict(
    path=C+'freeze-v1.json', bytes=4377,
    sha256='25d04505390ddad2020300d6459445741967ad9142be311540a5f14e2690b4b7'))
constructor = read(C+'freeze-v1.json')
assert len(constructor['artifacts']) == 9
for item in constructor['artifacts']:
    bind(item['path'], 'entire constructor payload', item)
assert rec(C+'candidate-v1.md') == dict(path=C+'candidate-v1.md', bytes=23211,
    sha256='7e721249102d37af67d14283f27adb5c6156375baa97bcfb3837ea98578fe195')

baseline = read(C+'baseline-v1.json')
assert len(baseline['inputs']) == 20
for item in baseline['inputs']:
    bind(item['path'], 'declared necessary current constructor input', item)
bind(baseline['immediate_own_parent']['path'],
    'duplicate declared constructor compact parent', baseline['immediate_own_parent'])
constructor_digest = sha256(json.dumps(baseline['inputs'], sort_keys=True,
    separators=(',',':')).encode()).hexdigest()
assert constructor_digest == constructor['canonical_input_summary_sha256']
assert constructor_digest == read(C+'input-validation-v1.json')['canonical_input_summary_sha256']
assert constructor['declared_occurrences_verified_in_baseline'] == 21

parent_path = 'problems/2024-B4/reviews/coordinator-F8-pencil-r1-review-1-manifest-v1.json'
parent = bind(parent_path, 'compact own last entire whole-audit parent', dict(
    path=parent_path, bytes=2894,
    sha256='6ed19f5eea8681155f4d2684fb65b338bf6a37fbe335aff9159835d387cdea26'))
for item in read(parent_path)['artifacts']:
    bind(item['path'], 'compact own parent payload identity only', item)

author_ids = re.findall(r'^\| (G\d{2}) \|',
    (ROOT/(C+'obligations-v1.md')).read_text(), re.M)
review_ids = re.findall(r'^\|(G\d{2})\|',
    (ROOT/(P+'issues-v1.md')).read_text(), re.M)
assert author_ids == review_ids == [f'G{i:02d}' for i in range(1,61)]
assert len(re.findall(r'^\*\*N[1-5] ',
    (ROOT/(P+'issues-v1.md')).read_text(), re.M)) == 5
assert 'zero substantive defects' in (ROOT/(P+'initial-v1.md')).read_text()
assert not (ROOT/(P+'manifest-v1.json')).exists()

NOW = datetime.now(timezone.utc).isoformat()
ordered = [unique[path] for path in sorted(unique)]
summary = dict(occurrences=len(rows), unique_paths=len(ordered), sha256=sha256(
    json.dumps(ordered,sort_keys=True,separators=(',',':')).encode()).hexdigest())
out('baseline-v1.json', dict(captured_at_utc=NOW,
    constructor_freeze=constructor_freeze, constructor_input_digest=constructor_digest,
    compact_own_parent=parent, summary=summary, records=ordered,
    occurrence_labels=[dict(label=row['label'],path=row['path']) for row in rows],
    unrelated_parent_inventory_recursively_rehashed_or_recopied=False))
out('metadata-v1.json', dict(status='ENTIRE initially blind OTHER WHOLE R2 frozen',
    reviewer='/root/review_2021_reasoning_j15_r2',
    constructor='/root/review_2022_complexity_r2',
    constructor_excluded_from_TWO_OTHER_audits=True,
    requested_model='gpt-6.1-sol', requested_reasoning='max',
    verified_effective_settings=None,
    whole_obligations=60, closed_dispositions=60, substantive_defects=0,
    unresolved_issues=0, author_repairs_required=0, closed_scope_notes=5,
    NEW_root_growth_R1_findings_report_ledger_sources_code_metadata_read_or_hashed=False,
    root_entire_R1_freeze_identity_only_received=True,
    complete_constructor_sources_failures_log_code_metadata_read=True,
    all_new_mathematics_hand_reconstructed=True,
    old_R7_NR_authorship_and_prior_review_roles_disclosed=True,
    accepted_dependencies_not_independently_self_recertified=True,
    mathematical_program_scan_CAS_author_rerun_certificate_replay=False,
    actual_regime_exact_lambda_new_numeric_annual_novelty_not_claimed=True,
    conditional_finite_criticality_and_actual_pressure_hypotheses_retained=True,
    no_old_shared_Git_cache_mutation_or_spawn_contact_charge=True,
    compact_input_summary=summary,
    latest_authoritative_budget=dict(at_utc='2026-10-18 06:54:23 UTC',
        tool='mcp__codex_app__get_usage_limits',used_percent_TOTAL=13,
        window_minutes=10080,reset_unix=1792874445,
        ordinaryUsageAllowed=True,legacy_by_limit_agree=True,
        current_window_explicitly_user_authorized=True,
        ceiling_TOTAL_with_integration_reserve=90,
        automatic_further_window_spending=False)))
for path, expected in unique.items():
    assert rec(path) == expected, path
out('input-validation-v1.json',dict(validated_at_utc=NOW,summary=summary,
    constructor_payloads=9,constructor_manifest_verified=True,
    constructor_declared_necessary_input_paths=20,
    constructor_declared_input_occurrences=21,
    compact_own_parent_and_payloads_verified=True,
    exact_inputs_match_before_and_after_new_writes=True,
    ALL60_author_and_reviewer_obligation_IDs_match_in_order=True,
    five_closed_scope_notes=True,
    NEW_root_growth_R1_review_paths_not_read_or_hashed=True,
    historical_inventory_not_recursively_rehashed_or_recopied=True,
    administrative_integrity_only_not_mathematical_testing=True))

payloads=['initial-v1.md','issues-v1.md','source-checks-v1.md','worklog-v1.md',
    'freeze-v1.py','baseline-v1.json','metadata-v1.json','input-validation-v1.json']
out('manifest-v1.json',dict(frozen_at_utc=NOW,
    status='ENTIRE initially blind OTHER WHOLE G1–G5 R2',
    reviewer='/root/review_2021_reasoning_j15_r2',
    constructor='/root/review_2022_complexity_r2',
    constructor_excluded=True,whole_obligations=60,
    substantive_defects=0,unresolved_issues=0,author_repairs_required=0,
    closed_scope_notes=5,
    NEW_root_growth_R1_findings_files_metadata_read_or_hashed=False,
    entire_report_ledger_sources_worklog_code_ALL_metadata_frozen=True,
    constructor_freeze=constructor_freeze,compact_own_parent=parent,
    current_input_summary=summary,
    artifacts=[rec(P+suffix) for suffix in payloads],
    mathematical_computation=False,promotion=False))
for path, expected in unique.items():
    assert rec(path) == expected, path
print(json.dumps(dict(manifest=rec(P+'manifest-v1.json'),
    report=rec(P+'initial-v1.md'),ledger=rec(P+'issues-v1.md'),
    whole_obligations=60,substantive_defects=0,required_repairs=0,
    closed_scope_notes=5,input_summary=summary),indent=2))
