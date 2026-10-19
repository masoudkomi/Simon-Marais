"""NEW documentary administration only; no mathematical evaluations.

prepare checks exact necessary input bytes/current authorities, binds one
own parent and creates compact baseline metadata in this NEW prefix.
freeze follows FULL final MODEL readback of ALL four payloads.
verify is a SEPARATE read-only invocation after FULL freeze MODEL readback.
No old/author/source routine is executed; no equations or degrees tested.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PREFIX = 'problems/2017-B4/notes/reasoning-joint-return-r15-'
BASELINE = PREFIX + 'baseline-v1.json'
FREEZE = PREFIX + 'freeze-v1.json'
PAYLOADS = [PREFIX + name for name in [
    'candidate-v1.md', 'sources-v1.json', 'admin-v1.py', 'baseline-v1.json'
]]
PARENT = 'problems/2019-B4/reviews/reasoning-full-law-return-r15-review-1-manifest-v1.json'
PARENT_SHA = '2ef8164bbb02f81d1a990ff585bd7148ff6a513c0ee329572cac825b35f69e41'
FAMILIES = ['reasoning-pressure-return-r11',
            'reasoning-concentration-return-r12', 'reasoning-lower-return-r14']
DIRECT = ['AGENTS.md', 'problems/2017-B4/statement.md']
EXPECTED_BODIES = {
    'reasoning-pressure-return-r11': '56688cd6030db910fbbc9162436b25acbf61a69869e2501dbd6f50b088bc3b60',
    'reasoning-concentration-return-r12': '15823ad1a7c54b8e06de3692f19d3395d2458786dcb8d2d51a2eb3c592734554',
    'reasoning-lower-return-r14': '88eed98d9ae634700fd23d571aad68cb4c59fd2fcd45e44dc48f9634c3d208c7'
}
for family in FAMILIES:
    DIRECT += [f'problems/2017-B4/proofs/reviewed-{family}-v1.1.md',
               f'problems/2017-B4/reviews/{family}-acceptance.md',
               f'problems/2017-B4/reviews/{family}-acceptance.json']
FORBIDDEN_PREFIXES = [
    'problems/2021-B4/reviews/reasoning-deep-return-r24-review-',
    'problems/2017-B4/reviews/reasoning-joint-return-r15-review-'
]

def now():
    return datetime.now(timezone.utc).isoformat()

def safe(path):
    assert isinstance(path, str) and not Path(path).is_absolute()
    assert '..' not in Path(path).parts
    assert not any(path.startswith(prefix) for prefix in FORBIDDEN_PREFIXES)
    return ROOT / path

def fp(path):
    data = safe(path).read_bytes()
    return {'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def load(path):
    return json.loads(safe(path).read_text())

def check(row):
    expected = {key: row[key] for key in ('path', 'bytes', 'sha256')}
    assert fp(expected['path']) == expected, expected
    return expected

def unique(rows):
    result = {}
    for row in rows:
        value = {key: row[key] for key in ('path', 'bytes', 'sha256')}
        if value['path'] in result:
            assert result[value['path']] == value
        result[value['path']] = value
    return sorted(result.values(), key=lambda value: value['path'])

def summary(rows):
    values = unique(rows)
    raw = json.dumps(values, sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(rows), 'unique_paths': len(values),
            'canonical_deduplicated_sha256': hashlib.sha256(raw).hexdigest()}

def create(path, value):
    assert path.startswith(PREFIX)
    with safe(path).open('x') as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write('\n')

def collect():
    rows = [fp(path) for path in DIRECT]
    for family in FAMILIES:
        authority = load(f'problems/2017-B4/reviews/{family}-acceptance.json')
        assert authority['unresolved_substantive_issues'] == 0
        accepted = check(authority['accepted_copy'])
        assert accepted['sha256'] == EXPECTED_BODIES[family]
        rows.append(accepted)
    assert fp(PARENT)['sha256'] == PARENT_SHA
    parent = load(PARENT)
    assert parent['ENTIRE_files'] == 5 and len(parent['payloads']) == 4
    rows += [fp(PARENT)] + [check(row) for row in parent['payloads']]
    return rows, parent

def literals():
    main = safe(PAYLOADS[0]).read_text()
    labels = re.findall(r'^\| JC15-(\d\d) \| CHECKED\.', main, re.M)
    assert labels == [str(i).zfill(2) for i in range(1, 37)]
    claims = re.findall(r'^\*\*(JC15[A-C]) \(', main, re.M)
    assert claims == ['JC15A', 'JC15B', 'JC15C'], claims
    source = load(PAYLOADS[1])
    assert source['whole_obligations'] == 36
    assert source['constructor_excluded_from_TWO_OTHER_WHOLE_audits'] is True
    assert source['root_supplied_NEW_mathematical_inference'] is False
    assert source['independent_effective_setting_readback'] is None
    assert source['NEW_B_C_R24_peer_findings_files_actual_inventory_open_hash_meta_access'] is False
    return {'literal_obligation_labels': len(labels), 'literal_claim_labels': claims,
            'mathematical_truth_checked_by_code': False}

def prepare():
    rows, parent = collect()
    create(BASELINE, {
        'created_UTC': now(), 'status': 'candidate proof - unverified',
        'constructor': '/root/review_2021_reasoning_j15_r2',
        'whole_obligations': 36, 'claims': ['JC15A', 'JC15B', 'JC15C'],
        'necessary_direct_records': unique([fp(path) for path in DIRECT]),
        'current_authority_accepted_copy_records_verified': 3,
        'compact_own_parent': fp(PARENT),
        'all4_parent_payloads_verified': True,
        'parent_historical_guard_summary_bound_NOT_reexpanded': parent['effective_fresh_guard_summary'],
        'parent_mathematics_new_JC15_premise': False,
        'effective_fresh_guard_summary': summary(rows),
        'historical_inventory_recopied_or_traversed': False,
        'mutable_current_research_map_observation_NOT_guard': fp('problems/2017-B4/research.md'),
        'literal_document_checks': literals(),
        'constructor_excluded_from_TWO_OTHER_WHOLE_audits': True,
        'root_supplied_NEW_mathematical_inference': False,
        'NEW_B_C_R24_peer_material_access': False,
        'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'independent_effective_setting_readback': None,
        'direct_quota': {'usedPercent': 75, 'windowDurationMins': 10080,
                         'resetsAt': 1792874445, 'ordinaryUsageAllowed': True,
                         'TOTAL_ceiling': 90, 'integration_reserve': True,
                         'automatic_later_window': False},
        'no_mathematical_code_CAS_scan_test_optimizer_old_source_author_freezer_replay': True,
        'no_Git_shared_old_cache_mutation': True,
        'FULL_final_ALL4_payload_MODEL_readbacks_then_freeze_MODEL_readback_then_SEPARATEverify_REQUIRED': True
    })
    print(json.dumps({'baseline': fp(BASELINE), 'guards': summary(rows), 'at_UTC': now()}))

def guard_check():
    rows, parent = collect()
    baseline = load(BASELINE)
    for row in baseline['necessary_direct_records']:
        check(row)
    assert summary(rows) == baseline['effective_fresh_guard_summary']
    assert literals() == baseline['literal_document_checks']
    check(baseline['compact_own_parent'])
    return baseline

def freeze():
    baseline = guard_check()
    create(FREEZE, {
        'frozen_UTC': now(), 'status': 'candidate proof - unverified',
        'constructor': '/root/review_2021_reasoning_j15_r2',
        'claims': ['JC15A', 'JC15B', 'JC15C'],
        'whole_obligations': 36, 'payload_count': 4, 'ENTIRE_files': 5,
        'payloads': [fp(path) for path in PAYLOADS],
        'compact_own_parent': fp(PARENT),
        'effective_fresh_guard_summary': baseline['effective_fresh_guard_summary'],
        'FULL_final_ALL4_payload_MODEL_readbacks_completed': True,
        'FULL_freeze_MODEL_readback_then_SEPARATE_readonly_verify_REQUIRED': True,
        'constructor_excluded_from_TWO_OTHER_WHOLE_audits': True,
        'root_supplied_NEW_mathematical_inference': False,
        'actual_one_class_per_size_no_joint_low_cost_or_mass_claim': True,
        'annual_exact_value_new_upper_bound_or_priority_claim': False,
        'requested': baseline['requested'],
        'independent_effective_setting_readback': None,
        'direct_quota': baseline['direct_quota'],
        'NEW_B_C_R24_peer_material_access': False,
        'mathematical_truth_checked_by_code': False,
        'no_Git_shared_old_cache_mutation': True
    })
    print(json.dumps({'freeze': fp(FREEZE), 'at_UTC': now()}))

def verify():
    frozen = load(FREEZE)
    assert frozen['ENTIRE_files'] == 5 and frozen['whole_obligations'] == 36
    assert [row['path'] for row in frozen['payloads']] == PAYLOADS
    for row in frozen['payloads']:
        check(row)
    baseline = guard_check()
    assert frozen['effective_fresh_guard_summary'] == baseline['effective_fresh_guard_summary']
    check(frozen['compact_own_parent'])
    print(json.dumps({'SEPARATE_readonly_verify': 'PASS', 'at_UTC': now(),
                      'freeze': fp(FREEZE), 'payloads': 4,
                      'whole_obligations': 36,
                      'guards': frozen['effective_fresh_guard_summary'],
                      'mathematical_truth_checked_by_code': False}))

if __name__ == '__main__':
    assert len(sys.argv) == 2 and sys.argv[1] in {'prepare', 'freeze', 'verify'}
    {'prepare': prepare, 'freeze': freeze, 'verify': verify}[sys.argv[1]]()
