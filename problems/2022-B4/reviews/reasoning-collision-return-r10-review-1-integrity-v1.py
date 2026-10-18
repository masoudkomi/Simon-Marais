#!/usr/bin/env python3
"""NEW RC10 review documentary integrity only; no mathematical routine."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
BASE = 'problems/2022-B4/reviews/reasoning-collision-return-r10-review-1-'
AUTHOR = 'problems/2022-B4/notes/reasoning-collision-return-r10-'
PARENT = 'problems/2021-B4/reviews/reasoning-center-return-r22-review-1-manifest-v1.json'
FORBIDDEN = 'problems/2022-B4/reviews/reasoning-collision-return-r10-review-2-'
PAYLOADS = ['initial-v1.md', 'ledger-v1.md', 'issues-v1.md', 'sources-v1.md',
            'sources-v1.json', 'worklog-v1.md', 'integrity-v1.py',
            'baseline-v1.json', 'input-validation-v1.json', 'metadata-v1.json']

def now():
    return datetime.now(timezone.utc).isoformat()

def full(path):
    assert not path.startswith(FORBIDDEN), 'NEW corresponding peer embargo'
    relative = Path(path)
    assert not relative.is_absolute() and '..' not in relative.parts
    result = ROOT / relative
    assert result.resolve().is_relative_to(ROOT)
    return result

def rec(path):
    raw = full(path).read_bytes()
    return {'path': path, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}

def obj(path):
    return json.loads(full(path).read_text())

def declarations(value):
    rows = []
    if isinstance(value, dict):
        if isinstance(value.get('path'), str) and isinstance(value.get('bytes'), int) and isinstance(value.get('sha256'), str):
            assert len(value['sha256']) == 64
            rows.append({key: value[key] for key in ('path', 'bytes', 'sha256')})
        for child in value.values():
            rows.extend(declarations(child))
    elif isinstance(value, list):
        for child in value:
            rows.extend(declarations(child))
    return rows

def check(rows):
    for row in rows:
        assert rec(row['path']) == {key: row[key] for key in ('path', 'bytes', 'sha256')}, row['path']

def summary(rows):
    unique = {}
    for row in rows:
        clean = {key: row[key] for key in ('path', 'bytes', 'sha256')}
        assert unique.setdefault(clean['path'], clean) == clean
    ordered = [unique[path] for path in sorted(unique)]
    raw = json.dumps(ordered, sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(rows), 'unique_paths': len(ordered),
            'canonical_deduplicated_sha256': hashlib.sha256(raw).hexdigest()}

def new(suffix, value):
    with full(BASE + suffix).open('x') as stream:
        stream.write(json.dumps(value, indent=2) + '\n')

def labels():
    text = full(BASE + 'ledger-v1.md').read_text()
    found = re.findall(r'^\|(RC10-\d\d)\|', text, re.M)
    assert found == [f'RC10-{i:02d}' for i in range(1, 61)]

def guards():
    expected_author = {'path': AUTHOR + 'freeze-v1.json', 'bytes': 2891,
        'sha256': '63f7e02fde4454421e66126bd4ba8decdd23c7dfe24367bed2f132710d30d4f4'}
    expected_main = {'path': AUTHOR + 'candidate-v1.md', 'bytes': 20330,
        'sha256': 'cc1dbec1dd63ebacde74814f0f61c55ffd66ef0908c581df83f9d0bed858100b'}
    expected_parent = {'path': PARENT, 'bytes': 3282,
        'sha256': '5ef00d6fc52ad1dfca0e58cd36676b66fe0102e470278fc7532d1bc886a6b7e7'}
    check([expected_author, expected_main, expected_parent])
    frozen = obj(expected_author['path'])
    assert frozen['ENTIRE_files_including_this_freeze'] == 8 and frozen['whole_obligations'] == 60
    check(frozen['payloads'])
    baseline = obj(AUTHOR + 'baseline-v1.json')
    rows = list(baseline['direct_records'])
    check(rows)
    for item in baseline['direct_records']:
        if item['path'].endswith('.json'):
            extra = declarations(obj(item['path']))
            check(extra)
            rows.extend(extra)
    assert summary(rows) == baseline['all_guard_summary'] == frozen['all_guard_summary']
    parent = obj(PARENT)
    check(parent['payload_records'])
    direct = frozen['payloads'] + [expected_author, expected_parent] + parent['payload_records']
    check(direct)
    return {'direct_records': direct,
        'author_guard_metadata_bound': rec(AUTHOR + 'baseline-v1.json'),
        'author_guard_summary_verified_not_recopied': summary(rows),
        'effective_guard_summary': summary(direct + rows),
        'own_parent': expected_parent,
        'own_parent_prior_guard_summary_bound_not_expanded': parent['effective_guard_summary'],
        'OLD_R12_explicit_BOTH_release_acceptance_confirmed_before_parent_path_follow_or_hash': True,
        'no_NEW_corresponding_peer_access': True}

mode = sys.argv[1] if len(sys.argv) == 2 else ''
if mode == 'prepare':
    g = guards()
    labels()
    new('baseline-v1.json', {'prepared_utc': now(), **g,
        'compact_metadata_no_growing_historical_inventory_copy': True,
        'byte_preservation_not_claim_of_fresh_historical_mathematical_reread': True})
    new('input-validation-v1.json', {'checked_utc': now(), 'status': 'PASS',
        'ENTIRE_author_files': 8, 'whole_obligations': 60,
        'author_guard_summary': g['author_guard_summary_verified_not_recopied'],
        'effective_guard_summary': g['effective_guard_summary'],
        'NEW_documentary_only_code': True, 'author_old_freezer_replay': False})
    new('metadata-v1.json', {'created_utc': now(),
        'reviewer': '/root/review_2017_coarsening_r1',
        'role': 'OTHER initially blind ENTIRE WHOLE1',
        'NEW_constructor': '/root/review_2022_complexity_r2',
        'NEW_construction_contribution': False,
        'old_C_constructor_roles': ['D7', 'D9', 'rational-base-shadow R4', 'R8', 'OLD2017 R12'],
        'old_input_not_independently_self_recertified': True,
        'requested_model': 'gpt-6.1-sol', 'requested_reasoning': 'max',
        'verified_effective_setting_readback': None,
        'whole_obligations': 60, 'dispositions': {'PASS': 60},
        'substantive_defects': 0, 'required_repairs': 0, 'closed_scope_notes': 8,
        'ENTIRE_author_files_read': 8,
        'fresh_complete_current_D9_D7_R4_R8_bodies_and_EACH_MDJSON': True,
        'own_parent': g['own_parent'], 'effective_guard_summary': g['effective_guard_summary'],
        'corresponding_NEW_peer_findings_files_inventory_hash_metadata_access': False,
        'findings_EMBARGO_until_explicit_BOTH': True,
        'mathematical_program_CAS_scan_routine_test_source_author_old_replay': False,
        'Git_shared_old_cache_mutation': False,
        'CUA_native_browser_download_charge_contact_bypass': False,
        'pending_tool_approval_native_child': None,
        'direct_transition_telemetry': {'usedPercent': 66, 'resetsAt': 1792874445,
            'ordinaryUsageAllowed': True, 'legacy_by_limit_agree': True,
            'TOTAL_ceiling': 90, 'reserve': True, 'automatic_later_week': False},
        'ordinary_infinite_avoider_termination_annual_priority_or_promotion_claim': False,
        'FULL_final_ALL10_payload_model_readback_then_manifest_then_SEPARATE_verify_required': True})
    print(json.dumps({'prepared_utc': now(), 'author_guard_summary': g['author_guard_summary_verified_not_recopied'],
        'effective_guard_summary': g['effective_guard_summary'], 'own_payloads': len(PAYLOADS)}, indent=2))
elif mode == 'seal':
    old = obj(BASE + 'baseline-v1.json')
    g = guards()
    assert all(old[key] == value for key, value in g.items())
    labels()
    new('manifest-v1.json', {'frozen_utc': now(),
        'reviewer': '/root/review_2017_coarsening_r1', 'role': 'OTHER initially blind ENTIRE WHOLE1',
        'ENTIRE_files': len(PAYLOADS) + 1, 'whole_obligations': 60,
        'payload_records': [rec(BASE + suffix) for suffix in PAYLOADS],
        'author': rec(AUTHOR + 'freeze-v1.json'), 'own_parent': rec(PARENT),
        'effective_guard_summary': g['effective_guard_summary'],
        'FULL_final_MODEL_ALL10_payload_readback_completed': True,
        'FULL_manifest_model_readback_then_SEPARATE_readonly_verify_required': True,
        'NO_NEW_corresponding_peer_findings_files_inventory_hash_metadata_access': True,
        'findings_EMBARGO_until_explicit_BOTH': True,
        'mathematical_program': False, 'old_shared_Git_cache_bytes_changed': False})
    print(json.dumps({'initial': rec(BASE + 'initial-v1.md'),
        'manifest': rec(BASE + 'manifest-v1.json')}, indent=2))
elif mode == 'verify':
    frozen = obj(BASE + 'manifest-v1.json')
    check(frozen['payload_records'])
    old = obj(BASE + 'baseline-v1.json')
    g = guards()
    assert all(old[key] == value for key, value in g.items())
    assert frozen['effective_guard_summary'] == g['effective_guard_summary']
    labels()
    for suffix in PAYLOADS + ['manifest-v1.json']:
        text = full(BASE + suffix).read_text()
        assert text
        if suffix.endswith('.json'):
            json.loads(text)
    print(json.dumps({'verified_utc': now(), 'status': 'PASS',
        'SEPARATE_readonly_invocation': True, 'ENTIRE_files': frozen['ENTIRE_files'],
        'whole_obligations': 60, 'effective_guard_summary': g['effective_guard_summary'],
        'initial': rec(BASE + 'initial-v1.md'), 'manifest': rec(BASE + 'manifest-v1.json')}, indent=2))
else:
    raise SystemExit('choose prepare, seal, or verify')
