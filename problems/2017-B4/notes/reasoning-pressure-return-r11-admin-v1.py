#!/usr/bin/env python3
"""R11 documentary identities only. No mathematical calculation or replay.

Modes prepare / freeze / verify. Writes are exclusive creation in this
NEW namespace. Verify is read-only. Historical inventories are not expanded.
"""
from pathlib import Path
import hashlib
import json
import re
import sys
from datetime import datetime, timezone

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
BASE = 'problems/2017-B4/notes/reasoning-pressure-return-r11-'
PARENT = 'problems/2025-B4/reviews/reasoning-diagonal-return-r8-review-2-manifest-v1.json'
PARENT_SHA = '81cdb6c65fb4c8c89c79df9a6155ed4d0be5acda429ac18cc0363bfd1dc43e95'
PAYLOAD_SUFFIXES = [
    'candidate-v1.md', 'obligations-v1.md', 'constructor-checks-v1.md',
    'issues-v1.md', 'failures-v1.md', 'sources-v1.md', 'sources-v1.json',
    'worklog-v1.md', 'admin-v1.py', 'baseline-v1.json',
    'input-validation-v1.json', 'metadata-v1.json',
]
ACCEPTED = [
    ('WC', 'reviewed-weighted-cutpath-r1-v1.1.md',
     'coordinator-weighted-cutpath-r1-acceptance',
     '93c08b0a43426c972bd6a0042c7e496cb08a106873c931f0231901e9f425f14b'),
    ('WO', 'reviewed-weighted-optimum-r2-v1.1.md',
     'coordinator-weighted-optimum-r2-acceptance',
     'dcc12d2989e5ab657960498179e2585e62ad35ffb1989a4bca72fef8fb953f9a'),
    ('PM8', 'reviewed-reasoning-path-mass-return-r8-v1.1.md',
     'reasoning-path-mass-return-r8-acceptance',
     '4e538d9369ae4a2ae9c7c47fa400e947740de08d7ce84a8579f837fd9f9b18d3'),
    ('PM9', 'reviewed-coordinator-path-moment-r3-v1.1.md',
     'coordinator-path-moment-r3-acceptance',
     'a02b6edeed84cb984749a4418c8c02a67a7fffb3f8098523231757d07ee9c2bb'),
    ('R10_context', 'reviewed-reasoning-path-mass-return-r10-v1.1.md',
     'reasoning-path-mass-return-r10-acceptance',
     '1159751417de0853cd2b6ac0c190b13f8423e06a5b88701ce09e675389d21058'),
]


def now():
    return datetime.now(timezone.utc).isoformat()


def fingerprint(path):
    value = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(value),
            'sha256': hashlib.sha256(value).hexdigest()}


def load(path):
    return json.loads((ROOT / path).read_text())


def put(suffix, obj):
    assert suffix in {'baseline-v1.json', 'input-validation-v1.json',
                      'metadata-v1.json', 'freeze-v1.json'}
    with (ROOT / (BASE + suffix)).open('x') as stream:
        stream.write(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')


def check(record):
    actual = fingerprint(record['path'])
    assert actual['bytes'] == record['bytes'], record['path']
    assert actual['sha256'] == record['sha256'], record['path']


def summary(records):
    unique = {}
    for row in records:
        clean = {key: row[key] for key in ['path', 'bytes', 'sha256']}
        if row['path'] in unique:
            assert unique[row['path']] == clean
        unique[row['path']] = clean
    ordered = [unique[key] for key in sorted(unique)]
    encoded = json.dumps(ordered, sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(records), 'unique_paths': len(ordered),
            'canonical_deduplicated_sha256': hashlib.sha256(encoded).hexdigest()}


def labels():
    text = (ROOT / (BASE + 'obligations-v1.md')).read_text()
    actual = re.findall(r'^\| (R11-\d{2}) \|', text, flags=re.M)
    required = ['R11-' + str(index).zfill(2) for index in range(1, 65)]
    assert actual == required, 'documentary obligation labels differ'
    return len(actual)


def prepare():
    # Exact old source inputs and current accepted authorities only.
    records = [fingerprint('AGENTS.md'),
               fingerprint('problems/2017-B4/statement.md')]
    assert records[0]['sha256'] == '28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff'
    for tag, body, authority, expected in ACCEPTED:
        body_path = 'problems/2017-B4/proofs/' + body
        record = fingerprint(body_path)
        assert record['sha256'] == expected, body_path
        records.append(dict(record, role=tag))
        authority_path = 'problems/2017-B4/reviews/' + authority
        records.append(fingerprint(authority_path + '.md'))
        records.append(fingerprint(authority_path + '.json'))
        accepted = load(authority_path + '.json')['accepted_copy']
        assert accepted == record, authority_path
    parent = fingerprint(PARENT)
    assert parent['bytes'] == 3365 and parent['sha256'] == PARENT_SHA
    parent_data = load(PARENT)
    records.append(dict(parent, role='immediate own immutable parent'))
    # Bind only its direct payloads; do not recursively expand its old inventory.
    for record in parent_data['payloads']:
        check(record)
        records.append(dict(record, role='immediate own parent payload'))
    for record in records:
        check(record)
    guard_summary = summary(records)
    total = labels()
    put('baseline-v1.json', {
        'prepared_at_utc': now(), 'status': 'compact direct-input guards',
        'records': records, 'guard_summary': guard_summary,
        'immediate_own_parent': parent,
        'historical_parent_inventory_recursively_copied': False,
        'corresponding_NEW_D9_or_other_peer_material_opened': False,
    })
    put('input-validation-v1.json', {
        'verified_at_utc': now(), 'pass': True,
        'all_current_accepted_copy_records_match_actual_bytes': True,
        'all_direct_guard_records_match': True, 'guard_summary': guard_summary,
        'whole_documentary_labels': total,
        'mathematical_execution_or_old_replay': False,
    })
    put('metadata-v1.json', {
        'prepared_at_utc': now(), 'status': 'candidate proof - unverified',
        'constructor': '/root/review_2017_coarsening_r1',
        'constructor_EXCLUDED_from_required_TWO_OTHER_audits': True,
        'root_supplied_NEW_mathematical_inference': False,
        'proposed_claims': ['PR11A', 'PR11B', 'PR11C', 'PR11D'],
        'whole_obligations': total, 'payload_files': len(PAYLOAD_SUFFIXES),
        'ENTIRE_files': len(PAYLOAD_SUFFIXES) + 1,
        'requested_settings': {'model': 'gpt-6.1-sol', 'reasoning': 'max',
                               'inherited': True},
        'verified_effective_setting_readback': None,
        'direct_transition_total_used_percent': 56,
        'authorized_reset': 1792874445, 'total_ceiling_percent': 90,
        'integration_reserve_required': True,
        'no_mathematical_program_or_CAS_scan_optimizer_old_replay': True,
        'no_pending_tool_or_native_child': True,
        'all_new_writes_in_assigned_namespace': True,
        'FULL_final_model_readback_ALL_payloads_REQUIRED_before_freeze': True,
        'FULL_freeze_readback_then_SEPARATE_readonly_verify_REQUIRED': True,
    })
    print(json.dumps({'mode': 'prepare', 'guard_summary': guard_summary,
                      'payloads': len(PAYLOAD_SUFFIXES), 'labels': total}))


def freeze():
    baseline = load(BASE + 'baseline-v1.json')
    for record in baseline['records']:
        check(record)
    assert labels() == 64
    payloads = [fingerprint(BASE + suffix) for suffix in PAYLOAD_SUFFIXES]
    put('freeze-v1.json', {
        'frozen_at_utc': now(), 'status': 'candidate proof - unverified',
        'constructor': '/root/review_2017_coarsening_r1',
        'required_TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits': True,
        'whole_obligations': 64, 'payload_files': len(payloads),
        'ENTIRE_files': len(payloads) + 1,
        'immediate_own_parent': baseline['immediate_own_parent'],
        'guard_summary': baseline['guard_summary'],
        'FULL_final_model_readback_ALL12_payloads_completed': True,
        'FULL_freeze_model_readback_then_SEPARATE_readonly_verify_REQUIRED': True,
        'mathematical_program_CAS_scan_optimizer_or_old_replay': False,
        'old_shared_Git_cache_edits': False,
        'payloads': payloads,
    })
    print(json.dumps({'mode': 'freeze',
                      'identity': fingerprint(BASE + 'freeze-v1.json')}))


def verify():
    frozen = load(BASE + 'freeze-v1.json')
    assert frozen['ENTIRE_files'] == 13 and frozen['whole_obligations'] == 64
    assert [row['path'] for row in frozen['payloads']] == [BASE + s for s in PAYLOAD_SUFFIXES]
    for record in frozen['payloads']:
        check(record)
    baseline = load(BASE + 'baseline-v1.json')
    for record in baseline['records']:
        check(record)
    assert summary(baseline['records']) == frozen['guard_summary']
    assert labels() == 64
    print(json.dumps({'mode': 'SEPARATE_READ_ONLY_VERIFY', 'pass': True,
                      'verified_at_utc': now(), 'ENTIRE_files': 13,
                      'all_obligations': 64,
                      'guard_summary': frozen['guard_summary'],
                      'main': fingerprint(BASE + 'candidate-v1.md'),
                      'freeze': fingerprint(BASE + 'freeze-v1.json')}))


if __name__ == '__main__':
    assert Path.cwd() == ROOT
    assert len(sys.argv) == 2
    {'prepare': prepare, 'freeze': freeze, 'verify': verify}[sys.argv[1]]()
