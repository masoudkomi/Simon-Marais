#!/usr/bin/env python3
"""Documentary-only IT12 review helper. It never evaluates an orbit or a proof.

Only creates NEW files in the assigned review-1 prefix. No author/old helper is
executed; no corresponding new peer file is listed, opened, or hashed. Hashes
of the explicitly released OLD R24 parent are preservation, not proof reading.
"""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
BASE = 'problems/2022-B4/reviews/reasoning-itinerary-return-r12-review-1-'
AUTHOR = 'problems/2022-B4/notes/reasoning-itinerary-return-r12-'
PARENT = 'problems/2017-B4/notes/reasoning-joint-return-r15-'
PAYLOADS = [BASE + suffix for suffix in
            ('initial-v1.md', 'sources-v1.json', 'admin-v1.py', 'baseline-v1.json')]
BASELINE = BASE + 'baseline-v1.json'
MANIFEST = BASE + 'manifest-v1.json'
EXPECTED_AUTHOR = {
    AUTHOR + 'candidate-v1.md': '50c4816c270fa6f3c1508ec93ffdcffedbe06514e74b0f097f037752e2c47ad7',
    AUTHOR + 'sources-v1.json': 'e32fecb35d1c82b9fd1d8ba395bcb276782e721e58f390c8f59017bd1ecea551',
    AUTHOR + 'admin-v1.py': 'c482248756ecf9a60ae39324264bba056128e1ec4f2fbb59bfeedbb4c0a8492e',
    AUTHOR + 'baseline-v1.json': 'c1bae43b2be026b40928d7fade6da77d300d703e396c83ea6e9eb23da7ee3967',
}
EXPECTED_PARENT_FREEZE = '40c82ab0e7f7a9678a31f763fc7960c54e8963f5e226f0da185cdf5441a0c6ac'

def now():
    return datetime.now(timezone.utc).isoformat()

def record(rel):
    data = (ROOT / rel).read_bytes()
    return {'path': rel, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def read_json(rel):
    return json.loads((ROOT / rel).read_text())

def check(item):
    assert record(item['path']) == item, 'Changed immutable bytes: ' + item['path']

def write_new(rel, value):
    path = ROOT / rel
    assert rel.startswith(BASE), 'Write outside assigned namespace'
    assert not path.exists(), 'Refuse overwrite: ' + rel
    path.write_text(json.dumps(value, indent=2) + '\n')

def unique_rows(rows):
    result = {}
    for item in rows:
        if item['path'] in result:
            assert result[item['path']] == item, 'Conflicting documentary records'
        result[item['path']] = item
    return [result[key] for key in sorted(result)]

def summary(rows):
    dedup = unique_rows(rows)
    serial = json.dumps(dedup, sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(rows), 'unique_paths': len(dedup),
            'canonical_deduplicated_sha256': hashlib.sha256(serial).hexdigest()}

def labels():
    text = (ROOT / PAYLOADS[0]).read_text()
    found = re.findall(r'^\|O12-(\d{2})\|', text, re.M)
    assert found == [f'{k:02d}' for k in range(1, 41)], 'Literal obligation order'
    for label in ('IT12A', 'IT12B', 'IT12C', 'IT12D'):
        assert label in text
    return {'literal_obligation_labels': len(found),
            'mathematical_truth_checked_by_code': False}

def baseline():
    author_freeze = read_json(AUTHOR + 'freeze-v1.json')
    assert author_freeze['ENTIRE_files'] == 5
    assert author_freeze['whole_obligations'] == 40
    author_rows = [record(AUTHOR + 'freeze-v1.json')] + author_freeze['payloads']
    for item in author_rows:
        check(item)
        if item['path'] in EXPECTED_AUTHOR:
            assert item['sha256'] == EXPECTED_AUTHOR[item['path']]
    author_baseline = read_json(AUTHOR + 'baseline-v1.json')
    declared = author_baseline['immutable_inputs']
    assert len(declared) == 16
    for item in declared:
        check(item)

    # Only the exact released R24 rows ALREADY declared above are hashed.
    # Its historical 47/45 inventory is neither copied nor traversed.
    released_old_parent = author_baseline['immediate_own_parent']
    check(released_old_parent)

    parent_freeze_rec = record(PARENT + 'freeze-v1.json')
    assert parent_freeze_rec['sha256'] == EXPECTED_PARENT_FREEZE
    parent_freeze = read_json(PARENT + 'freeze-v1.json')
    parent_rows = [parent_freeze_rec] + parent_freeze['payloads']
    assert len(parent_rows) == 5
    for item in parent_rows:
        check(item)
    parent_baseline = read_json(PARENT + 'baseline-v1.json')

    authority_matches = []
    for stem in ('reasoning-dynamics-return-r9', 'reasoning-collision-return-r10',
                 'reasoning-critical-return-r11'):
        authority = 'problems/2022-B4/reviews/' + stem + '-acceptance.json'
        accepted = read_json(authority)['accepted_copy']
        check(accepted)
        assert accepted in declared
        authority_matches.append(accepted['path'])

    rows = author_rows + declared + parent_rows
    value = {
        'created_UTC': now(),
        'status': 'Initially blind OTHER WHOLE1 documentary baseline; not proof verification',
        'reviewer': '/root/review_2021_reasoning_j15_r2',
        'author_packet_records': author_rows,
        'all_author_declared_immutable_inputs_checked': declared,
        'current_authority_copy_matches': authority_matches,
        'author_OLD_R24_parent': released_old_parent,
        'author_OLD_parent_historical_summary_bound_NOT_reexpanded': {
            'occurrences': author_baseline['parent_declared_occurrences'],
            'unique_paths': author_baseline['parent_declared_unique_paths']},
        'R24_access_precision': {
            'embedded_administrative_identity_received_before_access': True,
            'actual_open_hash_deferred_until_root_explicit_release_confirmation': True,
            'root_confirmed_BOTH_OLD_R24_initials_released_by_000903UTC': True,
            'only_exact_declared_OLD_payload_fingerprints_checked': True,
            'OLD_R24_peer_mathematical_report_MODEL_read_for_IT12': False,
            'OLD_parent_mathematics_new_IT12_premise': False},
        'own_immediate_parent_records': parent_rows,
        'own_parent_historical_summary_bound_NOT_reexpanded':
            parent_freeze['effective_fresh_guard_summary'],
        'all_preserved_fresh_records': rows,
        'effective_fresh_guard_summary': summary(rows),
        'historical_mutable_maps_current_identity_asserted': False,
        'author_historical_mutable_map_observation_only':
            author_baseline['mutable_observations_NOT_immutable_guards'],
        'own_parent_mutable_map_observation_NOT_new_guard':
            parent_baseline['mutable_current_research_map_observation_NOT_guard'],
        'NEW_corresponding_peer_content_inventory_open_hash_metadata_access': False,
        'administrative_root_R24_release_received_NOT_NEW_IT12_findings': True,
        'historical_inventory_recopied_or_recursively_traversed': False,
        'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'independent_effective_setting_readback': None,
        'direct_quota': {'observed_UTC': '2026-10-19 00:46:56 UTC',
                        'usedPercent': 76, 'windowDurationMins': 10080,
                        'resetsAt': 1792874445, 'ordinaryUsageAllowed': True,
                        'TOTAL_ceiling': 90, 'integration_reserve': True,
                        'automatic_later_window_spending': False},
        'mathematical_code_CAS_scan_test_old_author_source_replay': False,
        'Git_shared_old_cache_mutation': False,
    }
    write_new(BASELINE, value)
    print(json.dumps({'baseline': record(BASELINE),
                      'effective_fresh_guard_summary': summary(rows)}))

def freeze():
    base = read_json(BASELINE)
    for item in base['all_preserved_fresh_records']:
        check(item)
    for rel in PAYLOADS:
        assert (ROOT / rel).is_file(), rel
    read_json(PAYLOADS[1])
    counts = labels()
    value = {
        'frozen_UTC': now(),
        'status': 'Immutable initially blind OTHER WHOLE1; coordinator promotion pending',
        'reviewer': '/root/review_2021_reasoning_j15_r2',
        'constructor': '/root/review_2022_complexity_r2',
        'constructor_excluded': True,
        'claims': ['IT12A', 'IT12B', 'IT12C', 'IT12D'],
        'whole_obligations': 40, 'ENTIRE_files': 5, 'payload_count': 4,
        'payloads': [record(rel) for rel in PAYLOADS],
        'effective_fresh_guard_summary': base['effective_fresh_guard_summary'],
        'compact_own_parent': record(PARENT + 'freeze-v1.json'),
        'all40_obligations_reconstructed_by_hand': True,
        'unresolved_substantive_defects': 0, 'required_author_repairs': 0,
        'closed_scope_notes': 10,
        'FULL_final_ALL4_payload_MODEL_readbacks_completed': True,
        'FULL_manifest_MODEL_readback_then_SEPARATE_readonly_verify_REQUIRED': True,
        'NEW_corresponding_peer_findings_inventory_open_hash_metadata_access': False,
        'R24_historical_administrative_identity_exception_preserved': True,
        'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'independent_effective_setting_readback': None,
        'direct_quota': base['direct_quota'],
        'mathematical_truth_checked_by_code': False,
        'mathematical_code_CAS_scan_test_author_source_old_replay': False,
        'Git_shared_old_cache_mutation': False,
        'findings_release_requires_coordinator_explicit_BOTH_ENTIRE_confirmation': True,
    }
    write_new(MANIFEST, value)
    print(json.dumps({'manifest': record(MANIFEST), 'frozen_UTC': value['frozen_UTC']}))

def verify():
    manifest = read_json(MANIFEST)
    assert manifest['ENTIRE_files'] == len(manifest['payloads']) + 1 == 5
    for item in manifest['payloads']:
        check(item)
    base = read_json(BASELINE)
    for item in base['all_preserved_fresh_records']:
        check(item)
    assert summary(base['all_preserved_fresh_records']) == base['effective_fresh_guard_summary']
    assert labels()['literal_obligation_labels'] == manifest['whole_obligations'] == 40
    print(json.dumps({'SEPARATE_readonly_verify_UTC': now(), 'documentary_status': 'PASS',
        'ENTIRE_files': 5, 'literal_obligations': 40,
        'effective_fresh_guard_summary': base['effective_fresh_guard_summary'],
        'manifest': record(MANIFEST), 'initial': record(PAYLOADS[0]),
        'mathematical_truth_checked_by_code': False}))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=('baseline', 'freeze', 'verify'))
    args = parser.parse_args()
    {'baseline': baseline, 'freeze': freeze, 'verify': verify}[args.mode]()
