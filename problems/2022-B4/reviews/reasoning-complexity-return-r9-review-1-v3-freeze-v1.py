#!/usr/bin/env python3
"""Review byte/JSON/suffix/label integrity only; no mathematical execution."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
import re

ROOT = Path.cwd().resolve()
C = 'problems/2022-B4/notes/reasoning-complexity-return-r9-'
P = 'problems/2022-B4/reviews/reasoning-complexity-return-r9-review-1-v3-'
NOW = datetime.now(timezone.utc).isoformat()
rows, unique, groups = [], {}, []


def rec(path):
    assert not path.startswith('problems/2022-B4/reviews/reasoning-complexity-return-r9-review-2'), path
    raw = (ROOT / path).read_bytes()
    return dict(path=path, bytes=len(raw), sha256=sha256(raw).hexdigest())


def bind(path, expected=None, role=''):
    actual = rec(path)
    if expected is not None:
        assert actual == {k: expected[k] for k in ('path', 'bytes', 'sha256')}, path
    assert path not in unique or unique[path] == actual, path
    unique[path] = actual
    rows.append(dict(role=role, **actual))
    return actual


def fingerprints(obj):
    result = []
    if isinstance(obj, dict):
        if {'path', 'bytes', 'sha256'} <= obj.keys():
            result.append({k: obj[k] for k in ('path', 'bytes', 'sha256')})
        for value in obj.values():
            result.extend(fingerprints(value))
    elif isinstance(obj, list):
        for value in obj:
            result.extend(fingerprints(value))
    return result


def digest(records):
    dedup = {x['path']: {k: x[k] for k in ('path', 'bytes', 'sha256')} for x in records}
    ordered = [dedup[path] for path in sorted(dedup)]
    return sha256(json.dumps(ordered, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def group(role, start, metadata=None, **extra):
    selected = rows[start:]
    groups.append(dict(role=role, metadata=metadata, occurrences=len(selected),
                       unique_paths=len({x['path'] for x in selected}),
                       canonical_deduplicated_sha256=digest(selected), **extra))


def out(suffix, obj):
    with (ROOT / (P + suffix)).open('x', encoding='utf-8') as stream:
        json.dump(obj, stream, indent=2, ensure_ascii=False)
        stream.write('\n')


assert ROOT.name == 'Website'
for suffix in ('metadata-v1.json', 'input-validation-v1.json', 'manifest-v1.json'):
    assert not (ROOT / (P + suffix)).exists()

expected = {
    1: (4389, '13f4c9b46055c02b5f535706aa338bcc5167ea719120075aa0616e1298669142'),
    2: (5354, '3c1759ee6e7b7e018444f1d5b703b8847b90dea8ecf2fc1d71e81e1fbcbe6444'),
    3: (4828, 'e5c079493fd134eb05318d3b298565c0a4679ed0806431b9973230762d9c3ce2'),
}
constructor_records = {}
for v in (1, 2, 3):
    start = len(rows)
    path = C + f'freeze-v{v}.json'
    metadata = bind(path, dict(path=path, bytes=expected[v][0], sha256=expected[v][1]),
                    f'complete constructor v{v} manifest')
    constructor_records[v] = metadata
    source = json.loads((ROOT / path).read_text())
    for item in source['artifacts']:
        bind(item['path'], item, f'complete constructor v{v} payload')
    group(f'ENTIRE frozen constructor v{v} packet', start, metadata,
          historical_own_paths_bound_not_replayed=source.get('older_own_paths_bound_transitively'))

for v, count in ((1, 24), (2, 25), (3, 16)):
    start = len(rows)
    path = C + f'baseline-v{v}.json'
    baseline = json.loads((ROOT / path).read_text())
    declared = fingerprints(baseline)
    assert len(declared) == count
    for item in declared:
        bind(item['path'], item, f'necessary current constructor-v{v} baseline declaration')
    group(f'constructor v{v} necessary baseline declarations', start, rec(path),
          old_inventory_recursively_rewalked=False,
          historical_own_paths_bound_not_replayed=baseline['older_own_paths_bound_transitively'])

start = len(rows)
v1_validation_path = C + 'input-validation-v1.json'
v1_validation = json.loads((ROOT / v1_validation_path).read_text())
for authority in v1_validation['direct_current_authorities']:
    for item in fingerprints(authority):
        bind(item['path'], item, 'v1 recorded DIRECT accepted-context authority declaration')
group('direct old authority bindings as declared, not historical recursive review inventories',
      start, rec(v1_validation_path),
      v1_recorded_summary=dict(occurrences=v1_validation['fingerprint_occurrences_verified'],
                               unique_paths=v1_validation['unique_paths_verified'],
                               canonical_deduplicated_sha256=v1_validation['canonical_deduplicated_summary_sha256']),
      new_independent_recertification=False)

start = len(rows)
for path in ('AGENTS.md', 'problems/2022-B4/statement.md', 'problems/2022-B4/references.md',
             'problems/2022-B4/proofs/reviewed-partials-v1.md',
             'problems/2022-B4/reviews/acceptance.md'):
    bind(path, role='current official/protocol/sole operative attributed-context scope')
group('actual official scope and accepted preliminary-statement authority', start)

start = len(rows)
parent_path = 'problems/2020-B4/reviews/reasoning-arithmetic-return-r10-review-1-manifest-v1.json'
parent = bind(parent_path, dict(path=parent_path, bytes=3384,
    sha256='1b21dbcba67f26ef134fd1690848553a31f8a4b275d86d3a844a27f035ef0a05'),
    'immediate OWN immutable parent, not mathematical premise')
parent_data = json.loads((ROOT / parent_path).read_text())
for item in parent_data['artifacts']:
    bind(item['path'], item, 'immediate OWN completed parent preservation')
group('immediate OWN ENTIRE R10 R1 preservation', start, parent,
      older_summary_bound_not_replayed=parent_data['compact_current_summary'], mathematical_premise=False)

start = len(rows)
old_own_path = 'problems/2022-B4/reviews/reasoning-complexity-return-r9-review-1-manifest-v1.json'
old_own = bind(old_own_path, dict(path=old_own_path, bytes=4265,
    sha256='19688a525ac39b152e8db716b025204de135055c1d7045fb423f04eb0ae78ed8'),
    'immutable narrower OWN v1 initial, not substitute for whole v3')
old_data = json.loads((ROOT / old_own_path).read_text())
for item in old_data['artifacts']:
    bind(item['path'], item, 'immutable narrower OWN v1 review preservation')
group('original OWN v1 review preservation only', start, old_own, mathematical_premise=False)

for v in (2, 3):
    assert (ROOT / (C + f'candidate-v{v}.md')).read_bytes().endswith(
        (ROOT / (C + f'candidate-v{v-1}.md')).read_bytes())
    assert (ROOT / (C + f'obligations-v{v}.md')).read_bytes().endswith(
        (ROOT / (C + f'obligations-v{v-1}.md')).read_bytes())
labels = [('QO', 48), ('QV2', 32), ('QW3', 20)]
author_text = (ROOT / (C + 'obligations-v3.md')).read_text()
review_text = (ROOT / (P + 'issues-v1.md')).read_text()
for prefix, count in labels:
    expected_labels = [prefix + f'{n:02d}' for n in range(1, count + 1)]
    author_labels = re.findall(r'^\| (' + prefix + r'\d\d) \|', author_text, re.M)
    review_labels = re.findall(r'^\|(' + prefix + r'\d\d)\|.*\|CLOSED\|$', review_text, re.M)
    assert author_labels == review_labels == expected_labels, prefix
summary = dict(occurrences=len(rows), unique_paths=len(unique), canonical_deduplicated_sha256=digest(rows))
main = rec(C + 'candidate-v3.md')
assert main['bytes'] == 44042 and main['sha256'] == '77bf84340543589d96698a64df5e3850cdf22fe953ee45587ab0d79997184ff5'

out('metadata-v1.json', dict(
    frozen_at_utc=NOW,
    status='COMPLETE fresh initially blind ENTIRE WHOLE Q1-Q8 v3 R1; recommendation only',
    reviewer='/root/review_2021_reasoning_j15_r2',
    sole_NEW_constructor='/root/review_2022_complexity_r2',
    root_supplied_no_new_Q1_Q8_inference=True,
    whole_obligations=100, closed_checks=100, substantive_issues=0, repairs_required=0,
    closed_scope_notes=5,
    no_NEW_C_R9_v3_finding_report_ledger_source_or_metadata_read_or_hashed=True,
    entire_v1_v2_proofs_and_all_obligations_reconstructed_not_self_accepted=True,
    own_narrower_v1_review_not_substitute_for_NEW_whole_v3=True,
    root_announced_v1_acceptance_without_NEW_v3_finding=True,
    new_v1_accepted_copy_and_peer_R9_reviews_not_opened_for_this_audit=True,
    older_R6_authorship_and_R3_R4_R5_R7_R8_review_roles_disclosed=True,
    only_old_mathematical_input_is_attributed_eventual_strip_statement=True,
    no_preliminary_a_proof_reproduced_or_investigated=True,
    all_twenty_exact_intervals_and_both_deletions_independently_hand_checked=True,
    no_math_program_CAS_scan_author_rerun_or_certificate_replay=True,
    no_old_shared_cache_Git_edit_spawn_contact_charge_or_bypass=True,
    source_hypotheses_and_fresh_read_limits_explicit=True,
    no_seed_future_hitting_survival_finite_decision_annual_or_novelty_claim=True,
    requested_inherited_settings=dict(model='gpt-6.1-sol', reasoning='max'),
    independently_verified_effective_settings=None,
    authoritative_weekly_snapshot=dict(
        tool='mcp__codex_app__get_usage_limits', at_utc='2026-10-18 06:29:15 UTC',
        total_used_percent=11, window_minutes=10080, reset=1792874445,
        ordinaryUsageAllowed=True, legacy_and_by_limit_agree=True,
        account_suffix='ac3a', transition_at_utc='2026-10-18 06:19:30 UTC',
        transition_total_used_percent=10, earlier_raw_boundary_drift=1792874446,
        user_authorized_current_window=True, ceiling_TOTAL_with_reserve=90,
        automatic_further_reset_spending=False),
    compact_current_summary=summary,
    immutable_parent_inventory_bound_not_copied_or_recursively_rewalked=True))

for path, expected_row in unique.items():
    assert rec(path) == expected_row, path
out('input-validation-v1.json', dict(
    verified_at_utc=NOW, administrative_only=True,
    records=[unique[path] for path in sorted(unique)], groups=groups,
    compact_current_summary=summary,
    all_three_complete_constructor_packets_and_necessary_declarations_match=True,
    both_literal_main_and_obligation_suffix_chains_exact=True,
    all100_author_and_review_label_checks_match=True,
    immediate_OWN_R10_and_old_OWN_Q_v1_packets_unchanged=True,
    no_NEW_C_R9_review2_material_read_or_hashed=True,
    old_historical_inventories_not_recursively_replayed=True,
    administrative_only_not_mathematical_validation=True,
    writes_only_NEW_assigned_v3_review_prefix=True))

payloads = ['initial-v1.md', 'issues-v1.md', 'hand-checks-v1.md', 'source-checks-v1.md',
            'worklog-v1.md', 'freeze-v1.py', 'metadata-v1.json', 'input-validation-v1.json']
out('manifest-v1.json', dict(
    frozen_at_utc=NOW,
    status='COMPLETE fresh initially blind ENTIRE WHOLE Q1-Q8 v3 R1; recommendation not promotion',
    reviewer='/root/review_2021_reasoning_j15_r2',
    assigned_v3_main=main, assigned_v3_freeze=constructor_records[3],
    complete_v1_v2_chain_frozen_and_reconstructed=True,
    all_obligations=100, closed_per_inference_checks=100,
    substantive_issues=0, repairs_required=0, closed_scope_notes=5,
    all_NEW_C_v3_peer_material_unread_unhashed_through_ENTIRE_initial_freeze=True,
    old_roles_and_actual_primary_read_limits_explicit=True,
    all_twenty_exact_finite_intervals_are_hand_proof_not_program_evidence=True,
    no_mathematical_code_CAS_scan_author_rerun_old_shared_cache_or_Git_write=True,
    compact_current_summary=summary,
    compact_immediate_OWN_parent=parent, immutable_OWN_v1_initial=old_own,
    older_historical_inventory_rows_bound_not_recopied=True,
    this_review_paths_including_manifest=9,
    TWO_OTHER_ENTIRE_WHOLE_audits_and_root_reconciliation_before_promotion=True,
    retained_seed_future_finite_decision_annual_or_novelty_claim=False,
    administrative_command='python3 ' + P + 'freeze-v1.py',
    artifacts=[rec(P + suffix) for suffix in payloads]))
for path, expected_row in unique.items():
    assert rec(path) == expected_row, path
manifest = json.loads((ROOT / (P + 'manifest-v1.json')).read_text())
for item in manifest['artifacts']:
    assert rec(item['path']) == item, item['path']
print(json.dumps(dict(manifest=rec(P + 'manifest-v1.json'),
                      report=rec(P + 'initial-v1.md'), ledger=rec(P + 'issues-v1.md'),
                      all100_obligations_closed=True, compact_current_summary=summary,
                      all_payloads_and_current_inputs_postverified=True), indent=2))
