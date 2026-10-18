#!/usr/bin/env python3
"""NEW R10 review1 documentary integrity only; no mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PREFIX = 'problems/2025-B4/reviews/reasoning-compatible-return-r10-review-1-'
AUTHOR = 'problems/2025-B4/notes/reasoning-compatible-return-r10-'
AUTHOR_FREEZE = AUTHOR + 'freeze-v1.json'
AUTHOR_SHA = '167e4721b87d245a4dc82e5ffcc11d4fdd1dfad702785906fc732b7cd5f8b306'
PARENT = 'problems/2024-B4/reviews/coordinator-tensor-return-r12-review-1-manifest-v1.json'
PARENT_SHA = '31d124586f7812dffa10cffd852c3b88ad327d6e0cc91da9683f6e86d696735b'
PAYLOADS = ['report-v1.md', 'sources-v1.json', 'admin-v1.py', 'baseline-v1.json']
MUTABLE = {'problems/2025-B4/research.md'}

def now():
    return datetime.now(timezone.utc).isoformat()

def allowed(path):
    forbidden = [
        'reasoning-compatible-return-r10-review-2-',
        'reasoning-center-return-r22-review-'
    ]
    assert not any(item in path for item in forbidden), path
    return ROOT / path

def rec(path):
    data = allowed(path).read_bytes()
    return {'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def js(path):
    return json.loads(allowed(path).read_text())

def fresh(suffix, data):
    with (ROOT / (PREFIX + suffix)).open('x', encoding='utf-8') as stream:
        stream.write(json.dumps(data, indent=2, ensure_ascii=False) + '\n')

def records(value):
    out = []
    if isinstance(value, dict):
        if {'path', 'bytes', 'sha256'} <= value.keys():
            out.append({key: value[key] for key in ('path', 'bytes', 'sha256')})
        for child in value.values():
            out.extend(records(child))
    elif isinstance(value, list):
        for child in value:
            out.extend(records(child))
    return out

def check(items):
    for item in items:
        assert rec(item['path']) == item, ('protected bytes changed', item['path'])

def compact(items):
    unique = {}
    for item in items:
        assert item['path'] not in unique or unique[item['path']] == item
        unique[item['path']] = item
    ordered = [unique[path] for path in sorted(unique)]
    canon = json.dumps(ordered, sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(items), 'unique_paths': len(ordered),
            'canonical_deduplicated_sha256': hashlib.sha256(canon).hexdigest()}

def labels():
    report = allowed(PREFIX + 'report-v1.md').read_text()
    actual = re.findall(r'^\| (R10-\d\d) \| PASS \|', report, re.MULTILINE)
    assert actual == [f'R10-{i:02d}' for i in range(1, 65)], actual
    notes = re.findall(r'^\| (R10R1-N\d) \| CLOSED \|', report, re.MULTILINE)
    assert len(notes) == 9 and len(set(notes)) == 9

def verified_guards():
    author_record = rec(AUTHOR_FREEZE)
    assert author_record['bytes'] == 3692 and author_record['sha256'] == AUTHOR_SHA
    author = js(AUTHOR_FREEZE)
    assert author['ENTIRE_files'] == 14 and author['whole_obligations'] == 64
    check(author['payload_records'])
    declared = js(AUTHOR + 'baseline-v1.json')['guard_records']
    fixed_declared = [item for item in declared if item['path'] not in MUTABLE]
    check(fixed_declared)
    mutable = [{'historical_author_record': item, 'current_record': rec(item['path']),
                'historical_is_frozen_observation_not_current_identity': True}
               for item in declared if item['path'] in MUTABLE]
    for item in mutable:
        item['changed_since_author_snapshot'] = item['historical_author_record'] != item['current_record']
    parent_record = rec(PARENT)
    assert parent_record['bytes'] == 2300 and parent_record['sha256'] == PARENT_SHA
    parent = js(PARENT)
    check(parent['payloads'])
    parent_baseline = js('problems/2024-B4/reviews/coordinator-tensor-return-r12-review-1-baseline-v1.json')
    check(parent_baseline['direct_records'])
    current_paths = [
        'AGENTS.md', 'problems/2025-B4/statement.md', 'problems/2025-B4/research.md',
        'problems/2025-B4/proofs/reviewed-reasoning-diagonal-return-r8-v1.1.md',
        'problems/2025-B4/reviews/reasoning-diagonal-return-r8-acceptance.md',
        'problems/2025-B4/reviews/reasoning-diagonal-return-r8-acceptance.json',
        'problems/2025-B4/proofs/reviewed-reasoning-return-r9-v1.1.md',
        'problems/2025-B4/reviews/reasoning-return-r9-acceptance.md',
        'problems/2025-B4/reviews/reasoning-return-r9-acceptance.json',
        'problems/2025-B4/reviews/reasoning-return-r6-acceptance.md',
        'problems/2025-B4/reviews/reasoning-return-r6-acceptance.json'
    ]
    direct = [author_record] + author['payload_records'] + [rec(path) for path in current_paths]
    authority_records = []
    for suffix in ('diagonal-return-r8', 'return-r9', 'return-r6'):
        path = 'problems/2025-B4/reviews/reasoning-' + suffix + '-acceptance.json'
        authority_records.extend(records(js(path)))
    check(authority_records)
    all_items = direct + fixed_declared + [parent_record] + parent['payloads'] + parent_baseline['direct_records'] + authority_records
    return direct, all_items, mutable, {
        'author_freeze': author_record,
        'author_all_payloads_verified': len(author['payload_records']),
        'author_declared_immutable_guard_occurrences_verified': len(fixed_declared),
        'author_historical_guard_summary_bound': author['guard_summary'],
        'author_mutable_observations': mutable,
        'immediate_own_parent': parent_record,
        'parent_all_payloads_verified': len(parent['payloads']),
        'parent_direct_guard_occurrences_verified': len(parent_baseline['direct_records']),
        'parent_historical_effective_summary_bound_not_recopied': parent['effective_fresh_guard_summary'],
        'current_each_authority_direct_declared_occurrences_verified': len(authority_records),
        'no_recursive_historical_inventory_copy_or_old_execution': True
    }

mode = sys.argv[1] if len(sys.argv) == 2 else ''
if mode == 'prepare':
    direct, all_items, mutable, detail = verified_guards()
    fresh('baseline-v1.json', {
        'created_utc': now(), 'scope': 'necessary current direct guards and compact immutable parents',
        'direct_records': direct, 'current_occurrence_summary': compact(direct),
        'effective_fresh_guard_summary': compact(all_items), 'compact_parent_bindings': detail,
        'corresponding_NEW_B_R10_finding_file_actual_inventory_hash_meta_public_commentary_accessed': False,
        'corresponding_peer_completion_identity_received': False,
        'root_unrelated_FR11_TR12_R22_accepted_status_updates_are_not_R10_premises': True,
        'requested_model': 'gpt-6.1-sol', 'requested_reasoning': 'max',
        'effective_setting_readback': None,
        'weekly': {'usedPercent': 66, 'windowDurationMins': 10080, 'resetsAt': 1792874445,
                   'ordinaryUsageAllowed': True, 'authorized_TOTAL_ceiling': 90,
                   'reserve': True, 'automatic_next_window': False},
        'mathematical_program_CAS_scan_test_optimizer_old_source_author_replay': False,
        'Git_shared_old_cache_writes': False
    })
    labels()
    print(json.dumps({'prepared_utc': now(), 'current': compact(direct),
                      'effective_fresh': compact(all_items), 'mutable_observations': mutable,
                      'whole_obligations': 64}, indent=2))
elif mode == 'freeze':
    baseline = js(PREFIX + 'baseline-v1.json')
    direct, all_items, mutable, detail = verified_guards()
    assert direct == baseline['direct_records']
    assert compact(all_items) == baseline['effective_fresh_guard_summary']
    assert detail == baseline['compact_parent_bindings']
    labels()
    payloads = [rec(PREFIX + suffix) for suffix in PAYLOADS]
    fresh('manifest-v1.json', {
        'frozen_utc': now(), 'reviewer': '/root/review_2021_reasoning_j15_r2',
        'role': 'OTHER initially blind ENTIRE WHOLE1', 'whole_obligations': 64,
        'payload_count': len(payloads), 'ENTIRE_files': len(payloads) + 1,
        'payloads': payloads,
        'current_occurrence_summary': baseline['current_occurrence_summary'],
        'effective_fresh_guard_summary': baseline['effective_fresh_guard_summary'],
        'FULL_final_ALL4_payload_model_readback_completed': True,
        'FULL_manifest_model_readback_then_SEPARATE_readonly_verify_REQUIRED': True,
        'corresponding_NEW_B_R10_finding_file_actual_inventory_hash_metadata_public_commentary_seen': False,
        'corresponding_peer_completion_identity_received': False,
        'NEW_R10_constructive_contribution': False,
        'OLD_DR6_DR7_DR8_authorship_and_other_roles_disclosed_not_self_recertified': True,
        'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'independent_effective_setting_readback': None,
        'mathematical_program_CAS_scan_test_optimizer_source_author_old_replay': False,
        'findings_release_requires_explicit_BOTH_ENTIRE_confirmation': True,
        'status': 'Independent whole review recommendation only; root reconciliation required'
    })
    print(json.dumps({'manifest': rec(PREFIX + 'manifest-v1.json')}, indent=2))
elif mode == 'verify':
    manifest = js(PREFIX + 'manifest-v1.json')
    baseline = js(PREFIX + 'baseline-v1.json')
    assert manifest['ENTIRE_files'] == 5 and manifest['whole_obligations'] == 64
    check(manifest['payloads'])
    direct, all_items, mutable, detail = verified_guards()
    assert direct == baseline['direct_records']
    assert compact(all_items) == baseline['effective_fresh_guard_summary']
    assert detail == baseline['compact_parent_bindings']
    labels()
    for suffix in PAYLOADS + ['manifest-v1.json']:
        content = allowed(PREFIX + suffix).read_text()
        assert content
        if suffix.endswith('.json'):
            json.loads(content)
    print(json.dumps({'verified_utc': now(), 'status': 'PASS',
                      'SEPARATE_readonly_invocation': True, 'ENTIRE_files': 5,
                      'whole_obligations': 64, 'manifest': rec(PREFIX + 'manifest-v1.json'),
                      'report': rec(PREFIX + 'report-v1.md'),
                      'effective_fresh_guard_summary': compact(all_items)}, indent=2))
else:
    raise SystemExit('choose prepare, freeze, or verify')
