#!/usr/bin/env python3
"""NEW R10 documentary integrity only; no mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PREFIX = 'problems/2025-B4/notes/reasoning-compatible-return-r10-'
PARENT = 'problems/2024-B4/notes/reasoning-frobenius-return-r11-freeze-v1.json'
PARENT_SHA = '90ba8a8a0d07918bc738696b9619cef07b3577c85af5fea82766f322c6af2e38'
AUTH = 'problems/2025-B4/reviews/reasoning-diagonal-return-r8-acceptance.json'
PAYLOAD_SUFFIXES = [
    'candidate-v1.md', 'obligations-v1.md', 'checks-v1.md', 'issues-v1.md',
    'failures-v1.md', 'sources-v1.md', 'sources-v1.json', 'worklog-v1.md',
    'code-v1.md', 'integrity-v1.py', 'baseline-v1.json',
    'input-validation-v1.json', 'metadata-v1.json'
]

def now():
    return datetime.now(timezone.utc).isoformat()

def record(path):
    data = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}

def read_json(path):
    return json.loads((ROOT / path).read_text())

def write_new(suffix, value):
    path = ROOT / (PREFIX + suffix)
    with path.open('x', encoding='utf-8') as stream:
        stream.write(json.dumps(value, indent=2, ensure_ascii=False) + '\n')

def collect_records(value):
    found = []
    if isinstance(value, dict):
        if all(key in value for key in ('path', 'bytes', 'sha256')):
            found.append({key: value[key] for key in ('path', 'bytes', 'sha256')})
        for child in value.values():
            found.extend(collect_records(child))
    elif isinstance(value, list):
        for child in value:
            found.extend(collect_records(child))
    return found

def checked_records(records):
    for item in records:
        assert record(item['path']) == item, ('changed input', item['path'])

def summary(records):
    unique = {}
    for item in records:
        if item['path'] in unique:
            assert unique[item['path']] == item
        unique[item['path']] = item
    ordered = [unique[key] for key in sorted(unique)]
    canonical = json.dumps(ordered, sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(records), 'unique_paths': len(ordered),
            'canonical_sha256': hashlib.sha256(canonical).hexdigest()}

def check_labels():
    expected = [f'R10-{number:02d}' for number in range(1, 65)]
    for suffix in ('obligations-v1.md', 'checks-v1.md'):
        text = (ROOT / (PREFIX + suffix)).read_text()
        actual = re.findall(r'^\| (R10-\d\d) \|', text, re.MULTILINE)
        assert actual == expected, (suffix, actual)

mode = sys.argv[1] if len(sys.argv) == 2 else ''
if mode == 'prepare':
    parent_record = record(PARENT)
    assert parent_record['bytes'] == 3460 and parent_record['sha256'] == PARENT_SHA
    parent = read_json(PARENT)
    direct_authority_records = collect_records(read_json(AUTH))
    checked_records(direct_authority_records)
    checked_records(parent['payload_records'])
    direct_paths = [
        'AGENTS.md', 'problems/2025-B4/statement.md',
        'problems/2025-B4/research.md',
        'problems/2025-B4/reviews/reasoning-diagonal-return-r8-acceptance.md',
        AUTH, PARENT,
        'problems/2025-B4/proofs/reviewed-reasoning-return-r9-v1.1.md',
        'problems/2025-B4/proofs/reviewed-reasoning-return-r6-v1.1.md',
        'problems/2025-B4/notes/deep-literature-r1-report-v1.md',
        'problems/2025-B4/notes/deep-literature-r1-sources-v1.json'
    ]
    guards = ([record(path) for path in direct_paths]
              + direct_authority_records + parent['payload_records'])
    checked_records(guards)
    compact = summary(guards)
    write_new('baseline-v1.json', {
        'created_utc': now(), 'scope': 'necessary direct inputs and bound immutable parent',
        'guard_records': guards, 'guard_summary': compact,
        'parent_historical_inventory_copied': False,
        'parent_prior_guard_summary_bound_by_freeze': parent['all_guard_summary'],
        'direct_authority_declared_occurrences_checked': len(direct_authority_records),
        'authority_older_recursive_verification_not_rerun': True
    })
    write_new('input-validation-v1.json', {
        'checked_utc': now(), 'status': 'PASS', 'guard_summary': compact,
        'immediate_own_parent': parent_record,
        'parent_all_payloads_verified': len(parent['payload_records']),
        'direct_DR8_authority_records_verified': len(direct_authority_records),
        'no_recursive_historical_inventory_copy_or_old_executable': True
    })
    write_new('metadata-v1.json', {
        'created_utc': now(), 'status': 'candidate proof - unverified',
        'constructor': '/root/review_2017_coarsening_r1',
        'constructor_excluded': True, 'OTHER_whole_audits_required': 2,
        'whole_obligations': 64,
        'requested_model': 'gpt-6.1-sol', 'requested_reasoning': 'max',
        'effective_setting_readback': 'unavailable',
        'root_NEW_math_inference': False,
        'old_roles': ['C OLD R6/R9 constructor', 'C OLD DR8 OTHER whole reviewer'],
        'old_inputs_not_independently_self_recertified': True,
        'immediate_own_parent': parent_record,
        'guard_summary': compact,
        'direct_weekly_telemetry': {
            'usedPercent': 64, 'windowDurationMins': 10080,
            'resetsAt': 1792874445, 'ordinaryUsageAllowed': True,
            'legacy_by_limit_agree': True, 'authorized_TOTAL_ceiling': 90,
            'integration_reserve': True, 'automatic_next_window': False
        },
        'mathematical_program': False, 'CAS_scan_routine_test': False,
        'old_source_author_freezer_or_certificate_replay': False,
        'raw_PDF_downloaded_or_hash_claimed': False,
        'CUA_native_browser': False, 'pending_approval_or_child_PID': None,
        'new_peer_R12_FR11_content_inventory_hash_metadata_accessed': False,
        'Git_shared_old_cache_writes': False,
        'source_limits': 'FULL web-text CM2026; no visual/raw hash; BMv2 lines0-445 only',
        'annual_solved': False, 'new_Diophantine_exclusion': False,
        'publication_priority_claim': False,
        'FULL_final_model_readback_then_separate_verify_required': True
    })
    check_labels()
    print(json.dumps({'prepared_utc': now(), 'guard_summary': compact,
                      'payload_files': len(PAYLOAD_SUFFIXES), 'labels': 64}, indent=2))
elif mode == 'seal':
    baseline = read_json(PREFIX + 'baseline-v1.json')
    checked_records(baseline['guard_records'])
    check_labels()
    payloads = [record(PREFIX + suffix) for suffix in PAYLOAD_SUFFIXES]
    write_new('freeze-v1.json', {
        'frozen_utc': now(), 'status': 'candidate proof - unverified',
        'constructor': '/root/review_2017_coarsening_r1',
        'constructor_excluded': True, 'OTHER_whole_audits_required': 2,
        'whole_obligations': 64, 'ENTIRE_files': len(payloads) + 1,
        'payload_records': payloads,
        'guard_summary': baseline['guard_summary'],
        'immediate_own_parent': record(PARENT),
        'FULL_final_MODEL_ALL13_payload_readback_completed': True,
        'FULL_freeze_readback_then_SEPARATE_readonly_verify_required': True,
        'new_peer_R12_FR11_findings_files_inventory_hash_metadata_accessed': False,
        'mathematical_program': False, 'old_shared_Git_cache_bytes_changed': False,
        'new_Diophantine_exclusion': False, 'annual_solved': False
    })
    print(json.dumps({'freeze': record(PREFIX + 'freeze-v1.json'),
                      'candidate': record(PREFIX + 'candidate-v1.md')}, indent=2))
elif mode == 'verify':
    freeze = read_json(PREFIX + 'freeze-v1.json')
    assert freeze['ENTIRE_files'] == 14 and freeze['whole_obligations'] == 64
    assert len(freeze['payload_records']) == len(PAYLOAD_SUFFIXES)
    checked_records(freeze['payload_records'])
    baseline = read_json(PREFIX + 'baseline-v1.json')
    checked_records(baseline['guard_records'])
    assert summary(baseline['guard_records']) == freeze['guard_summary']
    check_labels()
    for suffix in PAYLOAD_SUFFIXES + ['freeze-v1.json']:
        data = (ROOT / (PREFIX + suffix)).read_text()
        if suffix.endswith('.json'):
            json.loads(data)
        assert data
    print(json.dumps({'verified_utc': now(), 'status': 'PASS',
                      'readonly_separate_invocation': True,
                      'ENTIRE_files': freeze['ENTIRE_files'], 'whole_obligations': 64,
                      'freeze': record(PREFIX + 'freeze-v1.json'),
                      'candidate': record(PREFIX + 'candidate-v1.md'),
                      'guard_summary': freeze['guard_summary']}, indent=2))
else:
    raise SystemExit('choose prepare, seal, or verify')
