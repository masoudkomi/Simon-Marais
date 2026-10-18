#!/usr/bin/env python3
"""Review integrity freeze only; no mathematical computation or author rerun."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re

ROOT = Path.cwd().resolve()
assert ROOT.name == 'Website' and (ROOT / 'AGENTS.md').is_file()
P = 'problems/2017-B4/reviews/coordinator-plane-recovery-r1-review-1-'
TARGET = 'problems/2017-B4/notes/coordinator-plane-recovery-r1-'
NOW = datetime.now(timezone.utc).isoformat()


def rec(path):
    raw = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(raw), 'sha256': sha256(raw).hexdigest()}


rows = []
dedup = {}


def bind(expected, label):
    path = expected['path']
    actual = rec(path)
    assert actual == {key: expected[key] for key in ('path', 'bytes', 'sha256')}, (label, path)
    assert path not in dedup or dedup[path] == actual
    dedup[path] = actual
    rows.append({'label': label, **actual})
    return actual


def out(suffix, obj):
    with (ROOT / (P + suffix)).open('x', encoding='utf-8') as handle:
        json.dump(obj, handle, indent=2, ensure_ascii=False)
        handle.write('\n')


target_freeze = bind({'path': TARGET + 'freeze-v1.json', 'bytes': 2239,
                     'sha256': '19c9c464f0c1f60000113b7a71ff3076d4501a23e1099671ff66b91cadf5a515'},
                    'exact assigned immutable PUS target freeze')
target = json.loads((ROOT / target_freeze['path']).read_text())
for item in target['artifacts']:
    bind(item, 'complete constructor artifact read; NOT executed')
bind({'path': TARGET + 'candidate-v1.md', 'bytes': 12840,
      'sha256': 'c156e2e2c26559bf5c5c7f9f29ecb0fc333d2582c58ce271fa09821087b1bd2d'},
     'independent exact assigned main identity')

target_validation = json.loads((ROOT / (TARGET + 'input-validation-v1.json')).read_text())
for item in target_validation['records']:
    bind(item, 'declared direct constructor input occurrence')
assert len(target_validation['records']) == 13

for name in ('reasoning-value-return-r6', 'allD-uniform-strict'):
    path = 'problems/2017-B4/reviews/' + name + '-acceptance.json'
    authority = json.loads((ROOT / path).read_text())
    assert authority['unresolved_substantive_issues'] == 0 and not authority['repair_required']
    for key in ('candidate', 'accepted_copy'):
        bind(authority[key], 'necessary accepted scope identity, not a new old-proof review')
    assert (ROOT / authority['accepted_copy']['path']).read_bytes().endswith(
        (ROOT / authority['candidate']['path']).read_bytes())

parent_path = 'problems/2020-B4/notes/reasoning-arithmetic-return-r9-freeze-v1.json'
parent_rec = bind({'path': parent_path, 'bytes': 2811,
                   'sha256': 'c90992cdc72cc411b8dbec2b811bbd39fb3e9e948e1559dd4e6163487a4ec5ef'},
                  'immutable own completed constructor parent')
parent = json.loads((ROOT / parent_path).read_text())
assert parent['own_paths_after_this_packet'] == 541
for suffix in ('metadata-v1.json', 'input-validation-v1.json'):
    path = 'problems/2020-B4/notes/reasoning-arithmetic-return-r9-' + suffix
    bind(next(item for item in parent['artifacts'] if item['path'] == path),
         'compact necessary own-parent metadata')

canonical = [dedup[path] for path in sorted(dedup)]
canonical_hash = sha256(json.dumps(canonical, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
ids = re.findall(r'^\|(\d{2})\|', (ROOT / (P + 'ledger-v1.md')).read_text(), re.M)
assert ids == [f'{number:02d}' for number in range(1, 37)]
author_ids = re.findall(r'^\|(\d{2})\|', (ROOT / (TARGET + 'obligations-v1.md')).read_text(), re.M)
assert ids == author_ids

out('baseline-v1.json', {
    'captured_at_utc': NOW,
    'scope': 'compact direct target/accepted inputs and immutable own parent only',
    'target_freeze': target_freeze,
    'immutable_own_parent': parent_rec,
    'historical_own_paths_bound': 541,
    'declared_occurrences_verified': len(rows),
    'deduplicated_paths_verified': len(canonical),
    'canonical_deduplicated_sha256': canonical_hash,
    'records': canonical,
    'occurrence_labels': [{'label': item['label'], 'path': item['path']} for item in rows],
    'no_NEW_peer_PUS_record_read_or_hashed': True,
    'fresh_recursive_rehash_or_recopy_of_old_history_claimed': False,
})
out('metadata-v1.json', {
    'status': 'COMPLETE ENTIRE initially blind independent WHOLE R1',
    'reviewer': '/root/review_2017_coarsening_r1',
    'NEW_constructor': '/root',
    'NEW_constructor_excluded_from_OTHER_audit_count': True,
    'requested_model': 'gpt-6.1-sol',
    'requested_reasoning': 'max',
    'independently_verified_effective_setting_readback': None,
    'complete_target_all_companions_accepted_PM_US_and_acceptance_scopes_read': True,
    'whole_author_obligations': 36,
    'whole_independent_ledger_rows': 36,
    'old_C_PM_annulus_authorship_and_US_review_roles_disclosed': True,
    'independent_NEW_proof_not_self_recertification_of_old_inputs': True,
    'no_NEW_peer_PUS_report_findings_source_code_or_metadata_read_or_hashed': True,
    'no_premature_mathematical_verdict_fragment_sent': True,
    'substantive_issues': 0,
    'requested_repairs': 0,
    'advisories': 0,
    'conclusion': 'no substantive defect identified in written fixed-D compact-strict local PUS1--PUS3 scope',
    'no_mathematical_code_CAS_count_scan_constructor_rerun': True,
    'only_new_code_is_administrative_byte_JSON_freezer': True,
    'no_download_charge_contact_bypass_pending_approval_or_Git_change': True,
    'no_mass_upper_R_numerical_scalar_annual_or_novelty_promotion': True,
    'coordinator_and_SECOND_OTHER_whole_audit_still_required': True,
    'latest_direct_budget': {'at_utc': '2026-10-18 01:13:51 UTC', 'used_percent_TOTAL': 7,
                             'reset': 1792874445, 'ordinary_allowed': True,
                             'explicit_current_window_authorization': True,
                             'ceiling_TOTAL_with_reserve': 90,
                             'automatic_further_reset_spending': False},
})

for path, expected in dedup.items():
    assert rec(path) == expected, path
out('input-validation-v1.json', {
    'verified_at_utc': NOW,
    'declared_occurrences_verified': len(rows),
    'deduplicated_paths_verified': len(canonical),
    'canonical_deduplicated_sha256': canonical_hash,
    'all_target7_artifacts_and13_input_occurrences_match': True,
    'both_exact_accepted_copy_suffix_relations_hold': True,
    'all_selected_inputs_unchanged_before_and_after_new_writes': True,
    'all36_author_IDs_equal_all36_review_ledger_IDs_in_order': True,
    'compact_own_parent_historical_paths': 541,
    'no_peer_PUS_material_read_or_hashed': True,
    'administrative_integrity_only_not_mathematical_testing': True,
})

suffixes = ['initial-v1.md', 'ledger-v1.md', 'issues-v1.md', 'source-checks-v1.md',
            'worklog-v1.md', 'freeze-v1.py', 'baseline-v1.json', 'metadata-v1.json',
            'input-validation-v1.json']
out('manifest-v1.json', {
    'frozen_at_utc': NOW,
    'status': 'ENTIRE initially blind independent WHOLE R1 frozen before any NEW peer PUS material',
    'whole_author_obligations': 36,
    'complete_whole_review': True,
    'substantive_issues': 0,
    'requested_repairs': 0,
    'advisories': 0,
    'target_freeze': target_freeze,
    'immutable_own_parent': parent_rec,
    'historical_own_paths_bound': 541,
    'this_packet_paths_including_manifest': 10,
    'own_paths_after_this_packet': 551,
    'declared_occurrences_verified': len(rows),
    'deduplicated_paths_verified': len(canonical),
    'old_constructor_roles_disclosed_no_self_recertification': True,
    'no_NEW_peer_PUS_file_or_hash_accessed': True,
    'no_coordinator_promotion_or_annual_claim': True,
    'artifacts': [rec(P + suffix) for suffix in suffixes],
})
for path, expected in dedup.items():
    assert rec(path) == expected, path
print(json.dumps({'manifest': rec(P + 'manifest-v1.json'),
                  'whole_report': rec(P + 'initial-v1.md'),
                  'all36': True, 'substantive_issues': 0, 'requested_repairs': 0,
                  'declared_occurrences_verified': len(rows),
                  'deduplicated_paths_verified': len(canonical),
                  'peer_blind_through_ENTIRE_freeze': True}, indent=2))
