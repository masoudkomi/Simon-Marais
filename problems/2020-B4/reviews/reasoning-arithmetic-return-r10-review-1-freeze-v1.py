#!/usr/bin/env python3
"""Exclusive review metadata freeze. No mathematics or author-code execution."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re

ROOT = Path.cwd().resolve()
P = 'problems/2020-B4/reviews/reasoning-arithmetic-return-r10-review-1-'
C = 'problems/2020-B4/notes/reasoning-arithmetic-return-r10-'
NOW = datetime.now(timezone.utc).isoformat()
rows, unique, groups = [], {}, []


def record(path):
    raw = (ROOT / path).read_bytes()
    return dict(path=path, bytes=len(raw), sha256=sha256(raw).hexdigest())


def bind(path, expected=None, role=''):
    actual = record(path)
    if expected is not None:
        assert actual == {k: expected[k] for k in ('path', 'bytes', 'sha256')}, path
    assert path not in unique or unique[path] == actual, path
    unique[path] = actual
    rows.append(dict(role=role, **actual))
    return actual


def digest(records):
    dedup = {x['path']: {k: x[k] for k in ('path', 'bytes', 'sha256')} for x in records}
    ordered = [dedup[path] for path in sorted(dedup)]
    return sha256(json.dumps(ordered, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def group(role, start, metadata=None, **extra):
    selected = rows[start:]
    groups.append(dict(role=role, metadata=metadata,
                       occurrences=len(selected), unique_paths=len({x['path'] for x in selected}),
                       canonical_deduplicated_sha256=digest(selected), **extra))


def out(suffix, obj):
    with (ROOT / (P + suffix)).open('x', encoding='utf-8') as handle:
        json.dump(obj, handle, indent=2, ensure_ascii=False)
        handle.write('\n')


assert ROOT.name == 'Website'
for suffix in ('metadata-v1.json', 'input-validation-v1.json', 'manifest-v1.json'):
    assert not (ROOT / (P + suffix)).exists()

start = len(rows)
constructor = bind(C + 'freeze-v1.json', dict(
    path=C + 'freeze-v1.json', bytes=3016,
    sha256='68dd827ca8c9f4156317022115f0981d818335508067299167cfd2d85541de43'),
    'entire assigned constructor freeze')
frozen = json.loads((ROOT / constructor['path']).read_text())
assert frozen['full_obligations'] == 52 and len(frozen['artifacts']) == 9
for item in frozen['artifacts']:
    bind(item['path'], item, 'entire assigned constructor payload')
main = next(x for x in frozen['artifacts'] if x['path'].endswith('candidate-v1.md'))
assert main['bytes'] == 20380 and main['sha256'] == '774da07295679d39d7aa3b22485f986e2a2dfc9445d25d4a56a0a4c0d7bce233'
group('entire constructor packet', start, constructor)

start = len(rows)
baseline = json.loads((ROOT / (C + 'baseline-v1.json')).read_text())
for item in baseline['records']:
    bind(item['path'], item, 'necessary constructor baseline declaration')
assert len(baseline['records']) == 13
assert digest(rows[start:]) == baseline['canonical_deduplicated_sha256']
group('constructor compact baseline, all13 declared records checked', start,
      record(C + 'baseline-v1.json'),
      old_historical_inventory_rewalked=False,
      historical_constructor_own_paths_bound=baseline['historical_own_research_paths_bound'])

for number in (7, 8):
    start = len(rows)
    base = f'problems/2020-B4/reviews/reasoning-return-r{number}-acceptance'
    authority = bind(base + '.json', role=f'accepted R{number} authority')
    accepted = json.loads((ROOT / authority['path']).read_text())
    assert accepted['unresolved_substantive_issues'] == 0 and not accepted['repair_required']
    bind(base + '.md', role=f'accepted R{number} full scope')
    candidate = bind(accepted['candidate']['path'], accepted['candidate'], f'accepted R{number} frozen body')
    copied = bind(accepted['accepted_copy']['path'], accepted['accepted_copy'], f'accepted R{number} exact copy')
    assert (ROOT / copied['path']).read_bytes().endswith((ROOT / candidate['path']).read_bytes())
    group(f'operative accepted R{number}, complete copy/scope read', start, authority,
          exact_candidate_copy_suffix=True,
          historical_occurrences_bound_not_replayed=accepted['record_occurrences_verified'],
          historical_paths_bound_not_replayed=accepted['unique_paths_verified'])

start = len(rows)
for path in ('AGENTS.md', 'problems/2020-B4/statement.md',
             'problems/2020-B4/references.md', 'problems/2020-B4/notes/deep-literature-r1-report-v1.md'):
    bind(path, role='current protocol/official scope/dated local context')
group('current protocol, official domain and complete dated source context', start)

start = len(rows)
parent_path = 'problems/2021-B4/notes/reasoning-return-r14-freeze-v1.json'
parent = bind(parent_path, dict(path=parent_path, bytes=4436,
    sha256='08b6fb33c91302e8fc5222504bcae08f84175f140be981851d94495c049d7b58'),
    'immediate OWN immutable parent, not a mathematical premise')
parent_data = json.loads((ROOT / parent_path).read_text())
for item in parent_data['artifacts']:
    bind(item['path'], item, 'immediate OWN parent payload preservation only')
group('immediate OWN R14 frozen packet preservation; no unrelated mathematical reread', start, parent,
      old_input_summary_bound_not_replayed=parent_data['compact_current_summary'],
      mathematical_premise=False)

ids = re.findall(r'^\|(\d{2})\|', (ROOT / (C + 'obligations-v1.md')).read_text(), re.M)
review_ids = re.findall(r'^\|(\d{2})\|.*\|CLOSED\|$', (ROOT / (P + 'issues-v1.md')).read_text(), re.M)
assert ids == review_ids == [f'{n:02d}' for n in range(1, 53)]
summary = dict(occurrences=len(rows), unique_paths=len(unique), canonical_deduplicated_sha256=digest(rows))
out('metadata-v1.json', dict(
    frozen_at_utc=NOW,
    status='COMPLETE initially blind ENTIRE WHOLE R1; recommendation only',
    reviewer='/root/review_2021_reasoning_j15_r2',
    sole_NEW_constructor='/root/review_2017_coarsening_r1',
    whole_constructor_obligations=52, whole_closed_checks=52,
    substantive_issues=0, repairs_required=0, closed_scope_notes=4,
    requested_inherited_settings=dict(model='gpt-6.1-sol', reasoning='max'),
    independently_verified_effective_settings=None,
    any_NEW_root_R10_review_finding_file_ledger_source_or_metadata_read_or_hashed=False,
    completion_IDENTITY_ONLY_until_root_ENTIRE_initial_confirmed=True,
    any_NEW_queued_2022_v3_target_or_peer_review_opened=False,
    old_R3_R5_R8_roles_disclosed_no_accepted_input_self_recertification=True,
    accepted_A9_announced_but_not_read_or_needed=True,
    no_mathematical_code_CAS_scan_author_rerun_or_certificate_replay=True,
    old_shared_cache_Git_mutation_spawn_contact_charge_or_bypass=False,
    actual_primary_read_limits_in_source_checks=True,
    all52_obligations_closed=True,
    no_exact_contest_N_q0_joint_composite_tuple_taut_order_or_annual_claim=True,
    authoritative_weekly_snapshot=dict(
        tool='mcp__codex_app__get_usage_limits', at_utc='2026-10-18 06:10:45 UTC',
        total_used_percent=10, window_minutes=10080, reset=1792874445,
        ordinaryUsageAllowed=True, legacy_and_by_limit_agree=True,
        account_suffix='ac3a', earlier_raw_plus_one_second_boundary=1792874446,
        user_authorized_current_window=True, ceiling_TOTAL_with_reserve=90,
        automatic_later_reset_spending=False),
    compact_current_summary=summary,
    older_inventory_rows_bound_not_recopied_or_recursively_rewalked=True))

for path, expected in unique.items():
    assert record(path) == expected, path
out('input-validation-v1.json', dict(
    verified_at_utc=NOW, administrative_only=True,
    records=[unique[path] for path in sorted(unique)],
    compact_current_summary=summary, groups=groups,
    constructor_all9_payloads_and_freeze_verified=True,
    constructor_all13_baseline_declarations_verified=True,
    accepted_R7_R8_exact_scopes_and_suffixes_verified=True,
    immediate_OWN_R14_all_payloads_preserved=True,
    all52_constructor_and_review_row_identifiers_match=True,
    no_NEW_root_R10_or_C_queued_v3_peer_material_read_or_hashed=True,
    old_history_not_replayed=True,
    writes_only_NEW_assigned_review_prefix=True))

payloads = ['initial-v1.md', 'issues-v1.md', 'source-checks-v1.md', 'worklog-v1.md',
            'freeze-v1.py', 'metadata-v1.json', 'input-validation-v1.json']
out('manifest-v1.json', dict(
    frozen_at_utc=NOW,
    status='COMPLETE ENTIRE initially blind WHOLE R1 initial freeze; recommendation not promotion',
    reviewer='/root/review_2021_reasoning_j15_r2',
    assigned_constructor_main=main, assigned_constructor_freeze=constructor,
    all_constructor_obligations=52, closed_per_inference_checks=52,
    substantive_issues=0, repairs_required=0, closed_scope_notes=4,
    all_NEW_peer_R10_material_unread_unhashed_through_ENTIRE_initial_freeze=True,
    completion_IDENTITY_ONLY_pending_other_ENTIRE_initial=True,
    next_queued_2022_v3_target_and_peer_material_unopened=True,
    old_roles_and_source_read_limits_explicit=True,
    no_mathcode_CAS_scan_author_rerun_shared_old_cache_or_Git_write=True,
    compact_current_summary=summary, compact_parent_metadata=parent,
    this_review_paths_including_manifest=8,
    TWO_OTHER_whole_audits_and_root_reconciliation_before_promotion=True,
    annual_or_new_taut_order_or_novelty_claim=False,
    administrative_command='python3 ' + P + 'freeze-v1.py',
    artifacts=[record(P + suffix) for suffix in payloads]))
for path, expected in unique.items():
    assert record(path) == expected, path
print(json.dumps(dict(manifest=record(P + 'manifest-v1.json'),
                      report=record(P + 'initial-v1.md'),
                      ledger=record(P + 'issues-v1.md'), all_obligations=52,
                      compact_current_summary=summary,
                      all_frozen_review_artifacts_verified=True), indent=2))
