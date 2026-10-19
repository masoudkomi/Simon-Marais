#!/usr/bin/env python3
"""NEW R25 whole2 documentary helper. No arithmetic/proof computation.

Reads only exact author/current-input/own-parent records. Does not list or
open corresponding new R25 peers or R26. No old/author helper is executed.
"""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
BASE = 'problems/2021-B4/reviews/coordinator-dyadic-depth-return-r25-review-2-'
AUTHOR = 'problems/2021-B4/notes/coordinator-dyadic-depth-return-r25-'
PARENT = 'problems/2024-B4/reviews/reasoning-classification-return-r14-review-2-'
PAYLOADS = [BASE + end for end in
            ('initial-v1.md', 'sources-v1.json', 'admin-v1.py', 'baseline-v1.json')]
BASELINE = BASE + 'baseline-v1.json'
MANIFEST = BASE + 'manifest-v1.json'
EXPECTED_AUTHOR_FREEZE = 'fa65dcb84789d0db25218940ff5957e234d10cf30a699973d255c9b3c55ab5b6'
EXPECTED_MAIN = '4ebcb8df634d91edc5b380effc883f795ce817dbdd992c5182da1f659eb203cc'
EXPECTED_PARENT = '05076bddd705fdc3c28cbf05511295c7db73055cfbf340e0c9d379b398acc4cc'

def now():
    return datetime.now(timezone.utc).isoformat()

def read(rel):
    return json.loads((ROOT / rel).read_text())

def fp(rel):
    assert isinstance(rel, str) and not rel.startswith('/') and '..' not in Path(rel).parts
    data = (ROOT / rel).read_bytes()
    return {'path': rel, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def check(row):
    assert fp(row['path']) == row, 'Changed immutable bytes: ' + row['path']

def new(rel, value):
    assert rel.startswith(BASE)
    with (ROOT / rel).open('x') as stream:
        json.dump(value, stream, indent=2)
        stream.write('\n')

def rows(base):
    return base['author_packet'] + base['necessary_immutable_inputs'] + base['own_parent_payloads']

def summary(items):
    unique = {}
    for item in items:
        if item['path'] in unique:
            assert unique[item['path']] == item
        unique[item['path']] = item
    ordered = [unique[key] for key in sorted(unique)]
    raw = json.dumps(ordered, sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(items), 'unique_paths': len(ordered),
            'canonical_deduplicated_sha256': hashlib.sha256(raw).hexdigest()}

def labels():
    text = (ROOT / PAYLOADS[0]).read_text()
    assert re.findall(r'^\|O(\d\d)\|', text, re.M) == [f'{i:02d}' for i in range(1, 29)]
    assert 'R25A' in text and 'R25B' in text
    return 28

def prepare():
    author_freeze_record = fp(AUTHOR + 'freeze-v1.json')
    assert author_freeze_record['sha256'] == EXPECTED_AUTHOR_FREEZE
    author = read(AUTHOR + 'freeze-v1.json')
    assert author['ENTIRE_files'] == 5 and author['whole_obligations'] == 28
    author_rows = [author_freeze_record] + author['payloads']
    for row in author_rows:
        check(row)
    assert fp(AUTHOR + 'candidate-v1.md')['sha256'] == EXPECTED_MAIN
    declared = read(AUTHOR + 'baseline-v1.json')['necessary_immutable_records']
    assert len(declared) == 5
    for row in declared:
        check(row)
    authority = read('problems/2021-B4/reviews/reasoning-deep-return-r24-acceptance.json')
    assert authority['status'] == 'proved, independently reviewed scoped partial result'
    check(authority['accepted_copy'])
    assert authority['accepted_copy'] in declared

    parent_manifest_record = fp(PARENT + 'manifest-v1.json')
    assert parent_manifest_record['sha256'] == EXPECTED_PARENT
    parent = read(PARENT + 'manifest-v1.json')
    parent_rows = [parent_manifest_record] + parent['payload_records']
    assert len(parent_rows) == 5
    for row in parent_rows:
        check(row)
    value = {
        'created_UTC': now(),
        'status': 'OTHER initially blind WHOLE2 documentary preservation; not proof checking',
        'reviewer': '/root/review_2021_reasoning_j15_r2',
        'author_packet': author_rows,
        'necessary_immutable_inputs': declared,
        'current_R24_authority_accepted_copy_matches': authority['accepted_copy'],
        'own_parent_payloads': parent_rows,
        'own_parent_historical_guard_summary_bound_NOT_reexpanded':
            parent['effective_fresh_guard_summary'],
        'effective_fresh_guard_summary': summary(author_rows + declared + parent_rows),
        'own_CL14_explicit_BOTH_release_received_and_own_disposition_sent': True,
        'own_CL14_peer_material_accessed_for_R25': False,
        'own_parent_mathematics_R25_premise': False,
        'historical_authority_inventories_recursively_opened': False,
        'living_maps_NOT_immutable_guards_and_NOT_MODEL_read': True,
        'NEW_corresponding_R25_peer_finding_inventory_open_hash_meta_commentary_access': False,
        'R26_exploration_or_target_access': False,
        'OLD_R24_authorship_accepted_input_not_fresh_independent_self_review': True,
        'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'independent_effective_setting_readback': None,
        'direct_quota': {'observed_UTC': '2026-10-19 01:42:54 UTC', 'usedPercent': 78,
                        'windowDurationMins': 10080, 'resetsAt': 1792874445,
                        'ordinaryUsageAllowed': True, 'TOTAL_ceiling': 90,
                        'integration_review_reserve': True, 'automatic_later_window': False},
        'mathematical_program_CAS_scan_test_author_source_old_replay': False,
        'Git_shared_old_cache_mutation': False,
    }
    new(BASELINE, value)
    print(json.dumps({'baseline': fp(BASELINE), 'guards': value['effective_fresh_guard_summary']}))

def freeze():
    base = read(BASELINE)
    for row in rows(base):
        check(row)
    assert labels() == 28
    read(PAYLOADS[1])
    value = {
        'frozen_UTC': now(),
        'status': 'Immutable initially blind OTHER WHOLE2; coordinator reconciliation pending',
        'reviewer': '/root/review_2021_reasoning_j15_r2',
        'constructor': '/root', 'constructor_excluded': True,
        'claims': ['R25A', 'R25B attributed accepted-input consequence'],
        'whole_obligations': 28, 'ENTIRE_files': 5, 'payload_count': 4,
        'payloads': [fp(rel) for rel in PAYLOADS],
        'effective_fresh_guard_summary': base['effective_fresh_guard_summary'],
        'compact_own_parent': fp(PARENT + 'manifest-v1.json'),
        'all28_reconstructed_by_hand': True,
        'unresolved_substantive_defects': 0, 'required_author_repairs': 0,
        'closed_scope_notes': 9,
        'FULL_final_ALL4_payload_MODEL_readbacks_complete': True,
        'FULL_manifest_MODEL_readback_then_SEPARATE_readonly_verify_REQUIRED': True,
        'NEW_corresponding_R25_peer_findings_inventory_open_hash_meta_commentary_access': False,
        'R26_exploration_or_target_access': False,
        'OLD_R24_authorship_disclosed_not_new_independent_self_recertification': True,
        'requested': base['requested'], 'independent_effective_setting_readback': None,
        'direct_quota': base['direct_quota'],
        'mathematical_truth_checked_by_code': False,
        'mathematical_program_CAS_scan_test_author_source_old_replay': False,
        'Git_shared_old_cache_mutation': False,
        'findings_release_requires_explicit_BOTH_ENTIRE': True,
    }
    new(MANIFEST, value)
    print(json.dumps({'manifest': fp(MANIFEST), 'frozen_UTC': value['frozen_UTC']}))

def verify():
    value = read(MANIFEST)
    assert value['ENTIRE_files'] == len(value['payloads']) + 1 == 5
    for row in value['payloads']:
        check(row)
    base = read(BASELINE)
    for row in rows(base):
        check(row)
    assert summary(rows(base)) == value['effective_fresh_guard_summary']
    assert labels() == value['whole_obligations'] == 28
    print(json.dumps({'SEPARATE_readonly_verify_UTC': now(), 'result': 'PASS',
        'ENTIRE_files': 5, 'whole_obligations': 28, 'manifest': fp(MANIFEST),
        'initial': fp(PAYLOADS[0]), 'guards': value['effective_fresh_guard_summary'],
        'writes': 0, 'mathematical_truth_checked_by_code': False}))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=('prepare', 'freeze', 'verify'))
    args = parser.parse_args()
    {'prepare': prepare, 'freeze': freeze, 'verify': verify}[args.mode]()
