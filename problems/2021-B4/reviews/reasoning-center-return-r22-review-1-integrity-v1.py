#!/usr/bin/env python3
"""NEW independent R22 documentary integrity; no mathematical routine."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
BASE = 'problems/2021-B4/reviews/reasoning-center-return-r22-review-1-'
AUTHOR = 'problems/2021-B4/notes/reasoning-center-return-r22-'
PARENT = 'problems/2025-B4/notes/reasoning-compatible-return-r10-freeze-v1.json'
PAYLOADS = ['initial-v1.md', 'ledger-v1.md', 'issues-v1.md', 'sources-v1.md',
            'sources-v1.json', 'worklog-v1.md', 'integrity-v1.py',
            'baseline-v1.json', 'input-validation-v1.json', 'metadata-v1.json']
FORBIDDEN = [
    'problems/2021-B4/reviews/reasoning-center-return-r22-review-2-',
    'problems/2017-B4/reviews/reasoning-concentration-return-r12-'
]

def now():
    return datetime.now(timezone.utc).isoformat()

def rec(path):
    assert not any(path.startswith(prefix) for prefix in FORBIDDEN), 'embargoed path'
    raw = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}

def obj(path):
    assert not any(path.startswith(prefix) for prefix in FORBIDDEN), 'embargoed path'
    return json.loads((ROOT / path).read_text())

def check(records):
    for item in records:
        clean = {key: item[key] for key in ('path', 'bytes', 'sha256')}
        assert rec(item['path']) == clean, ('changed input', item['path'])

def summary(records):
    unique = {}
    for item in records:
        clean = {key: item[key] for key in ('path', 'bytes', 'sha256')}
        if clean['path'] in unique:
            assert unique[clean['path']] == clean
        unique[clean['path']] = clean
    ordered = [unique[path] for path in sorted(unique)]
    raw = json.dumps(ordered, sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(records), 'unique_paths': len(ordered),
            'canonical_deduplicated_sha256': hashlib.sha256(raw).hexdigest()}

def new_json(suffix, value):
    with (ROOT / (BASE + suffix)).open('x') as stream:
        stream.write(json.dumps(value, indent=2) + '\n')

def author_guard_rows():
    # Independently reconstruct documentary parent bindings, never execute old code.
    pressure = 'problems/2017-B4/reviews/reasoning-pressure-return-r11-review-2-'
    occupation = 'problems/2019-B4/reviews/reasoning-occupation-return-r1-review-2-'
    parent_chain = [
        'problems/2019-B4/notes/reasoning-area-return-r2-',
        'problems/2020-B4/reviews/reasoning-class-return-sq16-review-2-',
        'problems/2020-B4/reviews/reasoning-class-return-sq17-review-2-'
    ]
    pbase = obj(pressure + 'baseline-v1.json')
    rows = pbase['direct_records'] + obj(occupation + 'baseline-v1.json')['records']
    check(rows)
    assert summary(rows) == pbase['effective_guard_summary']
    for prefix in parent_chain:
        old = obj(prefix + 'baseline-v1.json')
        check(old['direct_records'])
        rows = old['direct_records'] + rows
        assert summary(rows) == old['effective_guard_summary']
    author_base = obj(AUTHOR + 'baseline-v1.json')
    check(author_base['direct_records'])
    rows = author_base['direct_records'] + rows
    assert summary(rows) == author_base['effective_guard_summary']
    check(rows)
    return rows

def labels():
    expected = [f'R22-{i:02d}' for i in range(1, 49)]
    text = (ROOT / (BASE + 'ledger-v1.md')).read_text()
    assert re.findall(r'^\|(R22-\d\d)\|', text, re.M) == expected

mode = sys.argv[1] if len(sys.argv) == 2 else ''
if mode == 'prepare':
    expected_author = {'path': AUTHOR + 'freeze-v1.json', 'bytes': 2615,
        'sha256': '48f2fac48332fcde04d01e574b9f45c33e29375ceecc63afada5030058801c6f'}
    expected_main = {'path': AUTHOR + 'candidate-v1.md', 'bytes': 15244,
        'sha256': '21edc50529239da399d622e66d9af7460477e9ac1e9ff8fa7da0a4259ea1eb0a'}
    expected_parent = {'path': PARENT, 'bytes': 3692,
        'sha256': '167e4721b87d245a4dc82e5ffcc11d4fdd1dfad702785906fc732b7cd5f8b306'}
    check([expected_author, expected_main, expected_parent])
    frozen = obj(expected_author['path'])
    check(frozen['payloads'])
    assert frozen['ENTIRE_files'] == 9 and frozen['whole_obligations'] == 48
    parent = obj(PARENT)
    check(parent['payload_records'])
    history = author_guard_rows()
    direct = frozen['payloads'] + [expected_author, expected_parent] + parent['payload_records']
    check(direct)
    info = summary(direct + history)
    new_json('baseline-v1.json', {
        'prepared_utc': now(), 'direct_records': direct,
        'author_guard_summary_verified_not_recopied': summary(history),
        'effective_guard_summary': info,
        'author_guard_metadata': rec(AUTHOR + 'baseline-v1.json'),
        'own_parent': expected_parent,
        'own_parent_prior_guard_summary_bound_not_recopied': parent['guard_summary'],
        'historical_contents_not_claimed_freshly_mathematically_reread': True,
        'NO_NEW_corresponding_peer_content_inventory_path_hash_metadata_access': True
    })
    new_json('input-validation-v1.json', {
        'checked_utc': now(), 'status': 'PASS',
        'author_payloads': len(frozen['payloads']), 'author_whole_obligations': 48,
        'author_guard_summary': summary(history), 'effective_guard_summary': info,
        'own_parent_payloads': len(parent['payload_records']),
        'source_author_old_executable_replay': False
    })
    new_json('metadata-v1.json', {
        'created_utc': now(), 'reviewer': '/root/review_2017_coarsening_r1',
        'role': 'OTHER initially blind ENTIRE WHOLE1',
        'NEW_constructor': '/root/review_2021_reasoning_j15_r2',
        'reviewer_NEW_construction_contribution': False,
        'old_C_roles': ['OLD R17 constructor', 'OLD R19v1.1 OTHER whole3', 'OLD R21 OTHER whole1'],
        'no_old_input_independent_self_recertification': True,
        'requested_model': 'gpt-6.1-sol', 'requested_reasoning': 'max',
        'verified_effective_setting_readback': None,
        'whole_obligations': 48, 'dispositions': {'PASS': 48},
        'substantive_defects': 0, 'required_repairs': 0, 'closed_scope_notes': 8,
        'ENTIRE_author_files_read': 9,
        'fresh_complete_current_R18_R20_R21_bodies_and_EACH_MDJSON': True,
        'own_parent': expected_parent,
        'effective_guard_summary': info,
        'corresponding_NEW_peer_findings_files_inventory_hash_metadata_access': False,
        'received_peer_admin_completion_identity_only': True,
        'findings_EMBARGO_until_explicit_BOTH': True,
        'mathematical_program_CAS_scan_routine_test': False,
        'new_documentary_only_code': True,
        'source_author_old_freezer_certificate_replay': False,
        'Git_shared_old_cache_mutations': False,
        'CUA_native_browser_download_charge_contact_bypass': False,
        'pending_native_job_or_approval': None,
        'latest_parent_telemetry': {'usedPercent': 65, 'resetsAt': 1792874445,
            'TOTAL_ceiling': 90, 'integration_reserve': True,
            'automatic_later_week': False},
        'annual_solution_or_coordinator_promotion': False,
        'FULL_final_all10_payload_model_readback_then_manifest_then_SEPARATE_verify_required': True
    })
    labels()
    print(json.dumps({'prepared_utc': now(), 'author_guards': summary(history),
                      'effective_guards': info, 'own_payloads': len(PAYLOADS)}, indent=2))
elif mode == 'seal':
    baseline = obj(BASE + 'baseline-v1.json')
    check(baseline['direct_records'])
    history = author_guard_rows()
    assert summary(baseline['direct_records'] + history) == baseline['effective_guard_summary']
    labels()
    records = [rec(BASE + suffix) for suffix in PAYLOADS]
    new_json('manifest-v1.json', {
        'frozen_utc': now(), 'role': 'OTHER initially blind ENTIRE WHOLE1',
        'reviewer': '/root/review_2017_coarsening_r1',
        'whole_obligations': 48, 'ENTIRE_files': len(records) + 1,
        'payload_records': records,
        'effective_guard_summary': baseline['effective_guard_summary'],
        'author': rec(AUTHOR + 'freeze-v1.json'), 'own_parent': rec(PARENT),
        'FULL_final_MODEL_ALL10_payload_readback_completed': True,
        'FULL_manifest_model_readback_then_SEPARATE_readonly_verify_required': True,
        'NO_NEW_peer_findings_files_inventory_hash_metadata_access': True,
        'findings_EMBARGO_until_explicit_BOTH': True,
        'mathematical_program': False, 'old_shared_Git_cache_bytes_changed': False
    })
    print(json.dumps({'initial': rec(BASE + 'initial-v1.md'),
                      'manifest': rec(BASE + 'manifest-v1.json')}, indent=2))
elif mode == 'verify':
    frozen = obj(BASE + 'manifest-v1.json')
    check(frozen['payload_records'])
    baseline = obj(BASE + 'baseline-v1.json')
    check(baseline['direct_records'])
    assert summary(baseline['direct_records'] + author_guard_rows()) == frozen['effective_guard_summary']
    labels()
    for suffix in PAYLOADS + ['manifest-v1.json']:
        text = (ROOT / (BASE + suffix)).read_text()
        if suffix.endswith('.json'):
            json.loads(text)
        assert text
    print(json.dumps({'verified_utc': now(), 'status': 'PASS',
        'readonly_SEPARATE_invocation': True, 'ENTIRE_files': frozen['ENTIRE_files'],
        'whole_obligations': 48, 'initial': rec(BASE + 'initial-v1.md'),
        'manifest': rec(BASE + 'manifest-v1.json'),
        'effective_guard_summary': frozen['effective_guard_summary']}, indent=2))
else:
    raise SystemExit('choose prepare, seal, or verify')
