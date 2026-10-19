#!/usr/bin/env python3
"""NEW CL14 WHOLE2 documentary helper; no mathematical computation.

Only exact named immutable inputs are read. No corresponding NEW WHOLE1
inventory, file, hash, metadata, commentary, or finding is accessed. No old
or author helper is executed. Historical mutable maps stay observations.
"""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
BASE = 'problems/2024-B4/reviews/reasoning-classification-return-r14-review-2-'
AUTHOR = 'problems/2024-B4/notes/reasoning-classification-return-r14-'
PARENT = 'problems/2022-B4/reviews/reasoning-itinerary-return-r12-review-1-'
MUTABLE_MAP = 'problems/2024-B4/research.md'
PAYLOADS = [BASE + suffix for suffix in
            ('initial-v1.md', 'sources-v1.json', 'admin-v1.py', 'baseline-v1.json')]
BASELINE = BASE + 'baseline-v1.json'
MANIFEST = BASE + 'manifest-v1.json'
EXPECTED_AUTHOR = {
    AUTHOR + 'candidate-v1.md': '9f6041dcfda7e87d5b7c4c0c73a2e757bc0d1413c3c45d1e4683f7cc69dc8d29',
    AUTHOR + 'sources-v1.json': '1a41d4794c7fb75020d380144181f08cbc94c546e54b285c6fc1d5c4be89a52d',
    AUTHOR + 'admin-v1.py': '5b0d392a0ae5000efc3702b01887e7c902a54618dda283ea9241b32bc99e6fa2',
    AUTHOR + 'baseline-v1.json': '86d317bb147feeac7889b94e006d77dfdc992100a204b46ab6deaaade82d5fbc',
}
EXPECTED_OWN_PARENT = 'b3615debade7a6d75c3392742e25d15600a1551249f57f36a0e069c0b6ef980e'
AUTHORITIES = ('reasoning-frobenius-return-r10', 'reasoning-frobenius-return-r11',
               'coordinator-tensor-return-r12', 'coordinator-tensor-family-return-r13')

def now():
    return datetime.now(timezone.utc).isoformat()

def record(rel):
    assert isinstance(rel, str) and not rel.startswith('/') and '..' not in Path(rel).parts
    data = (ROOT / rel).read_bytes()
    return {'path': rel, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def read(rel):
    return json.loads((ROOT / rel).read_text())

def check(item):
    assert record(item['path']) == item, 'Changed immutable bytes: ' + item['path']

def write_new(rel, value):
    assert rel.startswith(BASE), 'Write outside assigned prefix'
    with (ROOT / rel).open('x') as stream:
        json.dump(value, stream, indent=2)
        stream.write('\n')

def summary(rows):
    unique = {}
    for item in rows:
        if item['path'] in unique:
            assert unique[item['path']] == item
        unique[item['path']] = item
    ordered = [unique[key] for key in sorted(unique)]
    raw = json.dumps(ordered, sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(rows), 'unique_paths': len(ordered),
            'canonical_deduplicated_sha256': hashlib.sha256(raw).hexdigest()}

def baseline_rows(value):
    return (value['author_packet_records'] + value['author_declared_immutable_records']
            + value['own_parent_records'])

def labels():
    text = (ROOT / PAYLOADS[0]).read_text()
    actual = re.findall(r'^\|CL14-O(\d\d)\|', text, re.M)
    assert actual == [f'{i:02d}' for i in range(1, 49)]
    for name in ('CL14A', 'CL14B', 'CL14C', 'CL14D'):
        assert name in text
    return 48

def prepare():
    author_freeze = read(AUTHOR + 'freeze-v1.json')
    assert author_freeze['ENTIRE_files'] == 5 and author_freeze['ALL_obligations'] == 48
    author_rows = [record(AUTHOR + 'freeze-v1.json')] + author_freeze['payload_records']
    for item in author_rows:
        check(item)
        if item['path'] in EXPECTED_AUTHOR:
            assert item['sha256'] == EXPECTED_AUTHOR[item['path']]
    author_baseline = read(AUTHOR + 'baseline-v1.json')
    old_rows = author_baseline['integrity']['necessary_records_verified']
    assert len(old_rows) == 20
    immutable = [row for row in old_rows if row['path'] != MUTABLE_MAP]
    historical_map = [row for row in old_rows if row['path'] == MUTABLE_MAP]
    assert len(immutable) == 19 and len(historical_map) == 1
    for item in immutable:
        check(item)
    # Root owns this living map. Its old identity is not an immutable proof.
    # Record current bytes without MODEL-reading any possible new status text.
    current_map = record(MUTABLE_MAP)

    authority_matches = []
    for stem in AUTHORITIES:
        rel = 'problems/2024-B4/reviews/' + stem + '-acceptance.json'
        value = read(rel)
        assert value['status'] == 'proved, independently reviewed scoped partial result'
        accepted = value['accepted_copy']
        check(accepted)
        assert accepted in immutable
        authority_matches.append(accepted)

    parent_manifest_record = record(PARENT + 'manifest-v1.json')
    assert parent_manifest_record['sha256'] == EXPECTED_OWN_PARENT
    parent = read(PARENT + 'manifest-v1.json')
    parent_rows = [parent_manifest_record] + parent['payloads']
    assert len(parent_rows) == 5
    for item in parent_rows:
        check(item)
    all_rows = author_rows + immutable + parent_rows
    value = {
        'created_UTC': now(),
        'status': 'OTHER initially blind WHOLE2 documentary preservation; not proof verification',
        'reviewer': '/root/review_2021_reasoning_j15_r2',
        'author_packet_records': author_rows,
        'author_declared_immutable_records': immutable,
        'author_historical_guard_summary_bound_NOT_reexpanded': author_freeze['guard_summary'],
        'author_mutable_map_historical_observation_NOT_immutable': historical_map[0],
        'current_mutable_map_metadata_observation_NOT_guard': current_map,
        'old_map_unchanged_claimed': False,
        'current_map_contents_MODEL_read_for_this_review': False,
        'current_authority_accepted_copy_matches': authority_matches,
        'author_released_OLD_R24_parent': author_freeze['immediate_own_parent'],
        'author_OLD_R24_historical_summary_NOT_reexpanded':
            author_baseline['integrity']['own_parent_historical_summary_bound_NOT_expanded'],
        'OLD_R24_prior_explicit_BOTH_release_and_acceptance_confirmed': True,
        'OLD_R24_peer_mathematical_report_MODEL_read_for_CL14': False,
        'own_parent_records': parent_rows,
        'own_IT12_initial_completed_before_root_explicit_BOTH_release_received_during_CL14_draft': True,
        'NEW_IT12_peer_files_accessed_for_CL14': False,
        'own_IT12_mathematics_CL14_premise': False,
        'own_parent_historical_guard_summary_bound_NOT_reexpanded':
            parent['effective_fresh_guard_summary'],
        'effective_fresh_guard_summary': summary(all_rows),
        'historical_inventories_copied_or_recursively_traversed': False,
        'NEW_corresponding_CL14_peer_findings_actual_inventory_open_hash_meta_commentary_access': False,
        'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'independent_effective_setting_readback': None,
        'direct_quota': {'observed_UTC': '2026-10-19 01:14:46 UTC', 'usedPercent': 77,
                        'windowDurationMins': 10080, 'resetsAt': 1792874445,
                        'ordinaryUsageAllowed': True, 'TOTAL_ceiling': 90,
                        'integration_review_reserve': True, 'automatic_later_window': False},
        'mathematical_program_CAS_scan_test_author_source_old_replay': False,
        'Git_shared_old_cache_mutation': False,
    }
    write_new(BASELINE, value)
    print(json.dumps({'baseline': record(BASELINE), 'guards': summary(all_rows),
        'historical_map_identity_equals_current': historical_map[0] == current_map}))

def freeze():
    value = read(BASELINE)
    for item in baseline_rows(value):
        check(item)
    assert summary(baseline_rows(value)) == value['effective_fresh_guard_summary']
    assert labels() == 48
    read(PAYLOADS[1])
    result = {
        'frozen_UTC': now(),
        'status': 'Immutable OTHER initially blind WHOLE2; coordinator acceptance pending',
        'reviewer': '/root/review_2021_reasoning_j15_r2',
        'constructor': '/root/review_2017_coarsening_r1', 'constructor_excluded': True,
        'claims': ['CL14A', 'CL14B', 'CL14C', 'CL14D'],
        'ENTIRE_files': 5, 'payload_count': 4, 'ALL_obligations': 48,
        'payload_records': [record(rel) for rel in PAYLOADS],
        'effective_fresh_guard_summary': value['effective_fresh_guard_summary'],
        'compact_own_parent': record(PARENT + 'manifest-v1.json'),
        'all48_reconstructed_by_hand': True,
        'unresolved_substantive_defects': 0, 'required_author_repairs': 0,
        'closed_scope_notes': 10,
        'FULL_final_ALL4_payload_MODEL_readbacks_completed': True,
        'FULL_manifest_MODEL_readback_then_SEPARATE_readonly_verify_REQUIRED': True,
        'NEW_corresponding_CL14_peer_findings_inventory_open_hash_meta_commentary_access': False,
        'own_IT12_prior_initial_NOW_explicit_BOTH_released_no_peer_files_needed': True,
        'mutable_map_current_identity_not_asserted_as_immutable_parent': True,
        'requested': value['requested'], 'independent_effective_setting_readback': None,
        'direct_quota': value['direct_quota'],
        'mathematical_truth_checked_by_code': False,
        'mathematical_program_CAS_scan_test_author_source_old_replay': False,
        'Git_shared_old_cache_mutation': False,
        'findings_release_requires_root_explicit_BOTH_ENTIRE_confirmation': True,
    }
    write_new(MANIFEST, result)
    print(json.dumps({'manifest': record(MANIFEST), 'frozen_UTC': result['frozen_UTC']}))

def verify():
    value = read(MANIFEST)
    assert value['ENTIRE_files'] == len(value['payload_records']) + 1 == 5
    for item in value['payload_records']:
        check(item)
    base = read(BASELINE)
    for item in baseline_rows(base):
        check(item)
    assert labels() == value['ALL_obligations'] == 48
    assert summary(baseline_rows(base)) == value['effective_fresh_guard_summary']
    print(json.dumps({'SEPARATE_readonly_verify_UTC': now(), 'result': 'PASS',
        'ENTIRE_files': 5, 'ALL_obligations': 48,
        'manifest': record(MANIFEST), 'initial': record(PAYLOADS[0]),
        'guard_summary': value['effective_fresh_guard_summary'],
        'writes': 0, 'mathematical_truth_checked_by_code': False}))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=('prepare', 'freeze', 'verify'))
    args = parser.parse_args()
    {'prepare': prepare, 'freeze': freeze, 'verify': verify}[args.mode]()
