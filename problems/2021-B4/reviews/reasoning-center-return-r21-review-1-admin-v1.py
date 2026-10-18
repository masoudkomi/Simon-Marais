#!/usr/bin/env python3
"""New R21 review documentary checks only; no mathematics or old replay."""
from pathlib import Path
import datetime
import hashlib
import json
import re
import sys

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
BASE = 'problems/2021-B4/reviews/reasoning-center-return-r21-review-1-'
AUTHOR = 'problems/2021-B4/notes/reasoning-center-return-r21-freeze-v1.json'
AUTHOR_SHA = '04ea7e21dc8ace2654acdbda4b3c67973c49218d358aff6d80edfc46842d48fd'
MAIN = 'problems/2021-B4/notes/reasoning-center-return-r21-candidate-v1.md'
MAIN_SHA = '27b372d98923309d2253cc491c641ab293ce10428d9b5e24589b1f2959399094'
PARENT = 'problems/2017-B4/notes/reasoning-pressure-return-r11-freeze-v1.json'
PARENT_SHA = '041cd6fa331d5737b71b721247b3d7706ecdf88edd115c7387055b840d0fe5e3'
SUFFIXES = ['report-v1.md', 'ledger-v1.md', 'issues-v1.md',
            'sources-v1.md', 'sources-v1.json', 'worklog-v1.md',
            'admin-v1.py', 'baseline-v1.json', 'input-validation-v1.json',
            'metadata-v1.json']


def stamp():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def record(path):
    data = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}


def load(path):
    return json.loads((ROOT / path).read_text())


def save(suffix, obj):
    assert suffix in {'baseline-v1.json', 'input-validation-v1.json',
                      'metadata-v1.json', 'manifest-v1.json'}
    with (ROOT / (BASE + suffix)).open('x') as target:
        target.write(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')


def check(row):
    assert record(row['path']) == {k: row[k] for k in ['path', 'bytes', 'sha256']}, row['path']


def compact(rows):
    unique = {}
    for row in rows:
        clean = {k: row[k] for k in ['path', 'bytes', 'sha256']}
        if row['path'] in unique:
            assert unique[row['path']] == clean
        unique[row['path']] = clean
    canonical = json.dumps([unique[p] for p in sorted(unique)],
                           sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(rows), 'unique_paths': len(unique),
            'canonical_deduplicated_sha256': hashlib.sha256(canonical).hexdigest()}


def labels():
    content = (ROOT / (BASE + 'ledger-v1.md')).read_text()
    found = re.findall(r'^\| (R21-\d{2}) \|', content, flags=re.M)
    expected = ['R21-' + str(i).zfill(2) for i in range(1, 49)]
    assert found == expected
    return len(found)


def prepare():
    author = record(AUTHOR)
    assert author['bytes'] == 3823 and author['sha256'] == AUTHOR_SHA
    assert record(MAIN)['bytes'] == 15374 and record(MAIN)['sha256'] == MAIN_SHA
    author_obj = load(AUTHOR)
    assert author_obj['entire_file_count_including_manifest'] == 15
    assert author_obj['obligations'] == 48
    rows = [dict(author, role='ENTIRE author freeze')]
    for row in author_obj['payloads']:
        check(row)
        rows.append(dict(row, role='ENTIRE author payload'))
    declared = load('problems/2021-B4/notes/reasoning-center-return-r21-baseline-v1.json')['rows']
    for row in declared:
        check(row)
        rows.append(dict(row, role='author direct declared guard; not fresh mathematical reread'))
    assert len(declared) == 38
    parent = record(PARENT)
    assert parent['bytes'] == 3407 and parent['sha256'] == PARENT_SHA
    rows.append(dict(parent, role='own immediate immutable parent'))
    for row in load(PARENT)['payloads']:
        check(row)
        rows.append(dict(row, role='own immediate parent payload'))
    for tag in ['r18', 'r20']:
        accepted = load('problems/2021-B4/reviews/reasoning-center-return-' + tag + '-acceptance.json')
        check(accepted['accepted_copy'])
    total = labels()
    guard_summary = compact(rows)
    save('baseline-v1.json', {
        'prepared_at_utc': stamp(), 'status': 'compact direct bindings, no recursive ancestry',
        'author': author, 'immediate_own_parent': parent,
        'records': rows, 'guard_summary': guard_summary,
        'corresponding_NEW_OTHER_R21_review_inventory_files_hash_meta_findings_accessed': False,
        'historical_authority_counts_not_new_recursive_validation': True,
    })
    save('input-validation-v1.json', {
        'verified_at_utc': stamp(), 'pass': True,
        'author_ENTIRE_files': 15, 'author_direct_declared_rows': 38,
        'all_direct_bytes_unchanged': True, 'whole_ledger_labels': total,
        'guard_summary': guard_summary,
        'mathematical_execution_author_source_or_old_replay': False,
    })
    save('metadata-v1.json', {
        'prepared_at_utc': stamp(), 'status': 'initially peer-blind OTHER WHOLE1; not acceptance',
        'reviewer': '/root/review_2017_coarsening_r1',
        'NEW_R21_constructor_or_contributor': False,
        'A_and_root_contributors_EXCLUDED': True,
        'old_C_R5_centerR17_roles_not_self_recertification': True,
        'whole_obligations': total, 'payload_files': len(SUFFIXES),
        'ENTIRE_files': len(SUFFIXES) + 1,
        'requested_settings': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'verified_effective_setting_readback': None,
        'authorized_reset': 1792874445, 'total_ceiling': 90,
        'latest_prior_direct_transition_total_used_percent': 56,
        'integration_reserve_required': True,
        'NEW_OTHER_peer_access': False,
        'findings_EMBARGOED_until_explicit_BOTH_ENTIRE_confirmation': True,
        'no_mathematical_program_CAS_scan_test_or_old_author_source_replay': True,
        'no_Git_shared_old_cache_writes_or_pending_child': True,
        'FULL_final_model_readback_ALL_payloads_REQUIRED_before_manifest': True,
        'FULL_manifest_readback_then_SEPARATE_readonly_verify_REQUIRED': True,
    })
    print(json.dumps({'mode': 'prepare', 'pass': True, 'guard_summary': guard_summary,
                      'payloads': len(SUFFIXES), 'all_documentary_obligations': total}))


def freeze():
    baseline = load(BASE + 'baseline-v1.json')
    for row in baseline['records']:
        check(row)
    assert labels() == 48
    payloads = [record(BASE + suffix) for suffix in SUFFIXES]
    save('manifest-v1.json', {
        'frozen_at_utc': stamp(),
        'status': 'OTHER initially blind ENTIRE WHOLE1; not acceptance',
        'reviewer': '/root/review_2017_coarsening_r1',
        'NEW_R21_constructor_or_contributor': False,
        'whole_obligations': 48, 'payload_files': len(payloads),
        'ENTIRE_files': len(payloads) + 1,
        'author': baseline['author'],
        'immediate_own_parent': baseline['immediate_own_parent'],
        'guard_summary': baseline['guard_summary'],
        'FULL_final_model_readback_ALL10_payloads_completed': True,
        'FULL_manifest_model_readback_then_SEPARATE_readonly_verify_REQUIRED': True,
        'NEW_OTHER_peer_material_access_before_freeze': False,
        'findings_EMBARGOED_until_explicit_BOTH_ENTIRE_confirmation': True,
        'no_mathematical_execution_or_old_author_source_replay': True,
        'payloads': payloads,
    })
    print(json.dumps({'mode': 'freeze', 'identity': record(BASE + 'manifest-v1.json')}))


def verify():
    manifest = load(BASE + 'manifest-v1.json')
    assert manifest['ENTIRE_files'] == 11 and manifest['whole_obligations'] == 48
    assert [row['path'] for row in manifest['payloads']] == [BASE + suffix for suffix in SUFFIXES]
    for row in manifest['payloads']:
        check(row)
    baseline = load(BASE + 'baseline-v1.json')
    for row in baseline['records']:
        check(row)
    assert compact(baseline['records']) == manifest['guard_summary']
    assert labels() == 48
    print(json.dumps({'mode': 'SEPARATE_READ_ONLY_VERIFY', 'pass': True,
                      'verified_at_utc': stamp(), 'ENTIRE_files': 11, 'all_obligations': 48,
                      'guard_summary': manifest['guard_summary'],
                      'report': record(BASE + 'report-v1.md'),
                      'manifest': record(BASE + 'manifest-v1.json')}))


if __name__ == '__main__':
    assert Path.cwd() == ROOT
    assert len(sys.argv) == 2
    {'prepare': prepare, 'freeze': freeze, 'verify': verify}[sys.argv[1]]()
