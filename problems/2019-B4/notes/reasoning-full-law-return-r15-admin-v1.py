"""NEW documentary preservation only; NEVER mathematical verification.

snapshot creates baseline/metadata only in this NEW author prefix.
freeze follows FULL final MODEL readback of ALL five payloads.
verify is a SEPARATE read-only call after FULL manifest MODEL readback.
No old helper or source routine runs. No orbit/count/formula is evaluated.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PREFIX = 'problems/2019-B4/notes/reasoning-full-law-return-r15-'
PARENT = 'problems/2022-B4/reviews/reasoning-critical-return-r11-review-2-manifest-v1.json'
PARENT_SHA = 'a991265ff7ca25d4c960d648958a1fafda75c16ef03eb9f87283474128631f56'
BASELINE = PREFIX + 'baseline-v1.json'
METADATA = PREFIX + 'metadata-v1.json'
FREEZE = PREFIX + 'freeze-v1.json'
PAYLOADS = [PREFIX + suffix for suffix in [
    'candidate-v1.md', 'sources-v1.json', 'admin-v1.py',
    'baseline-v1.json', 'metadata-v1.json',
]]
FAMILIES = [
    ('reasoning-area-return-r2', 'v1.1'),
    ('reasoning-occupation-return-r1', 'v1.1'),
    ('reasoning-cut-transfer-r6', 'v1.1'),
    ('reasoning-return-r7', 'v1.1'),
    ('reasoning-cut-transfer-r4', 'v1.2'),
]
DIRECT = ['AGENTS.md', 'problems/2019-B4/statement.md']
for family, version in FAMILIES:
    DIRECT.extend([
        f'problems/2019-B4/proofs/reviewed-{family}-{version}.md',
        f'problems/2019-B4/reviews/{family}-acceptance.md',
        f'problems/2019-B4/reviews/{family}-acceptance.json',
    ])
ERRATUM = 'problems/2019-B4/reviews/reasoning-cut-transfer-r4-presentation-erratum-v1'
DIRECT += [ERRATUM + '.md', ERRATUM + '.json']
FORBIDDEN = [
    'problems/2022-B4/reviews/reasoning-critical-return-r11-review-1-',
    'r13', 'tensor',
]

def now():
    return datetime.now(timezone.utc).isoformat()

def safe(path):
    assert isinstance(path, str) and not Path(path).is_absolute()
    assert '..' not in Path(path).parts
    assert not any(token in path for token in FORBIDDEN), path
    return ROOT / path

def fp(path):
    data = safe(path).read_bytes()
    return {'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def read_json(path):
    return json.loads(safe(path).read_text())

def check(row):
    expected = {key: row[key] for key in ['path', 'bytes', 'sha256']}
    assert fp(expected['path']) == expected, expected
    return expected

def unique(rows):
    values = {}
    for row in rows:
        value = {key: row[key] for key in ['path', 'bytes', 'sha256']}
        if value['path'] in values:
            assert values[value['path']] == value
        values[value['path']] = value
    return sorted(values.values(), key=lambda row: row['path'])

def summary(rows):
    deduplicated = unique(rows)
    raw = json.dumps(deduplicated, sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(rows), 'unique_paths': len(deduplicated),
            'canonical_deduplicated_sha256': hashlib.sha256(raw).hexdigest()}

def create(path, value):
    assert path.startswith(PREFIX), path
    with safe(path).open('x') as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write('\n')

def literal_checks():
    main = safe(PAYLOADS[0]).read_text()
    obligations = re.findall(r'^\| FL15-(\d\d) \| CHECKED\.', main, flags=re.M)
    assert obligations == [str(i).zfill(2) for i in range(1, 49)], obligations
    claims = re.findall(r'^\*\*(FL15[A-D]) — ', main, flags=re.M)
    assert claims == ['FL15A', 'FL15B', 'FL15C', 'FL15D'], claims
    source = read_json(PAYLOADS[1])
    assert source['whole_obligations'] == 48
    assert source['root_NEW_mathematical_inference'] is False
    assert source['independent_effective_readback'] is None
    assert source['NEW_corresponding_CR11_peer_findings_files_inventory_hash_metadata_access'] is False
    return {'literal_obligations': len(obligations), 'literal_claims': claims,
            'mathematical_truth_checked_by_code': False}

def snapshot():
    assert fp(PARENT)['sha256'] == PARENT_SHA
    parent = read_json(PARENT)
    assert parent['ENTIRE_files'] == 6 and parent['whole_obligations'] == 48
    assert len(parent['payload_records']) == 5
    rows = [fp(PARENT)] + [check(row) for row in parent['payload_records']]
    rows += [fp(path) for path in DIRECT]
    # Bind necessary declared accepted copies only, not growing historical
    # review inventories, baselines, scripts or any unrelated sealed parent.
    for family, _ in FAMILIES:
        path = f'problems/2019-B4/reviews/{family}-acceptance.json'
        authority = read_json(path)
        assert authority['unresolved_substantive_issues'] == 0
        rows.append(check(authority['accepted_copy']))
    erratum = read_json(ERRATUM + '.json')
    rows.append(check(erratum['operative_accepted_copy']))
    expected = {
        'AGENTS.md': '28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff',
        'problems/2019-B4/proofs/reviewed-reasoning-area-return-r2-v1.1.md': '98297c1d51c4adb78e5083a710bf66e7147013be846b17a5dd41407a90c91fd3',
        'problems/2019-B4/proofs/reviewed-reasoning-occupation-return-r1-v1.1.md': '1fa9770945b5e1b74f6ef7e6016cdf6804a73034b17433251e9a62a2895f2004',
        'problems/2019-B4/proofs/reviewed-reasoning-cut-transfer-r6-v1.1.md': 'f43bd14fbec8b827dadbdbc33161e34aad3082f946a858bbf8d78880d0024ff8',
        'problems/2019-B4/proofs/reviewed-reasoning-return-r7-v1.1.md': '4fe222b8b1d89b6b3d66bb16c6a1985390d537eee55bb42bfefdb2d4821e351a',
        'problems/2019-B4/proofs/reviewed-reasoning-cut-transfer-r4-v1.2.md': '1dcaef71bdc599028e4bb2459b3491d8e572656662d4ccaa8695b3152821106f',
    }
    for row in rows:
        if row['path'] in expected:
            assert row['sha256'] == expected[row['path']]
    create(BASELINE, {
        'snapshot_utc': now(), 'documentary_only': True,
        'immutable_guard_records': unique(rows),
        'effective_guard_summary': summary(rows),
        'own_immediate_parent': fp(PARENT),
        'own_parent_older_summary_transitively_bound_NOT_replayed': parent['effective_guard_summary'],
        'historical_review_inventory_recopied_or_traversed': False,
        'CT_historical_v1_1_header_is_not_operative': True,
        'mutable_research_context_NOT_identity_guarded': True,
        'literal_checks': literal_checks(),
        'corresponding_NEW_CR11_peer_access': False,
        'unrelated_root_R13_access': False,
    })
    create(METADATA, {
        'created_utc': now(), 'constructor': '/root/review_2017_coarsening_r1',
        'status': 'candidate proof - unverified',
        'constructor_excluded_from_TWO_OTHER_whole_audits': True,
        'root_NEW_mathematical_inference': False,
        'ENTIRE_files_including_freeze': 6, 'whole_obligations': 48,
        'claims': ['FL15A', 'FL15B', 'FL15C', 'FL15D'],
        'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'independent_effective_readback': None,
        'all_mathematics_hand_reasoned': True,
        'code_documentary_only': True,
        'no_mathematical_program_CAS_scan_optimizer_test_old_source_author_replay': True,
        'no_Git_shared_old_cache_mutation_spawn_charge_contact_bypass': True,
        'CR11_peer_embargo_preserved': True,
        'CR11_explicit_BOTH_release_received_before_handoff': True,
        'unrelated_root_R13_access': False,
        'R23_explicit_BOTH_release_received': True,
        'annual_and_every_positive_density_law_OPEN': True,
        'new_numerical_lambda_bound_or_priority_claim': False,
        'weekly': read_json(PAYLOADS[1])['weekly'],
        'FULL_final_MODEL_ALL5_payload_readback_then_freeze_MODEL_readback_then_SEPARATE_verify_required': True,
    })
    print(json.dumps({'snapshot': fp(BASELINE), 'metadata': fp(METADATA),
                      'guards': summary(rows), 'at_utc': now()}))

def guard_check():
    baseline = read_json(BASELINE)
    for row in baseline['immutable_guard_records']:
        check(row)
    current = summary(baseline['immutable_guard_records'])
    declared = baseline['effective_guard_summary']
    assert current['unique_paths'] == declared['unique_paths']
    assert current['canonical_deduplicated_sha256'] == declared['canonical_deduplicated_sha256']
    assert declared['occurrences'] >= declared['unique_paths']
    assert literal_checks() == baseline['literal_checks']
    return baseline

def freeze():
    baseline = guard_check()
    create(FREEZE, {
        'frozen_utc': now(), 'status': 'candidate proof - unverified',
        'constructor': '/root/review_2017_coarsening_r1',
        'constructor_excluded_from_TWO_OTHER_whole_audits': True,
        'root_NEW_mathematical_inference': False,
        'ENTIRE_files': 6, 'whole_obligations': 48,
        'payload_records': [fp(path) for path in PAYLOADS],
        'own_parent': fp(PARENT),
        'effective_guard_summary': baseline['effective_guard_summary'],
        'FULL_final_MODEL_ALL5_payload_readback_completed': True,
        'FULL_freeze_MODEL_readback_then_SEPARATE_readonly_verify_required': True,
        'NO_NEW_CR11_corresponding_peer_access': True,
        'unrelated_root_R13_access': False,
        'mathematical_program': False,
        'old_shared_Git_cache_bytes_changed': False,
    })
    print(json.dumps({'freeze': fp(FREEZE), 'at_utc': now()}))

def verify():
    frozen = read_json(FREEZE)
    assert frozen['ENTIRE_files'] == 6 and frozen['whole_obligations'] == 48
    assert [row['path'] for row in frozen['payload_records']] == PAYLOADS
    for row in frozen['payload_records']:
        check(row)
    check(frozen['own_parent'])
    baseline = guard_check()
    assert frozen['effective_guard_summary'] == baseline['effective_guard_summary']
    assert frozen['NO_NEW_CR11_corresponding_peer_access'] is True
    print(json.dumps({'SEPARATE_readonly_verify': 'PASS', 'at_utc': now(),
                      'freeze': fp(FREEZE), 'payloads': 5,
                      'whole_obligations': 48,
                      'guards': baseline['effective_guard_summary'],
                      'mathematical_truth_checked_by_code': False}))

if __name__ == '__main__':
    assert len(sys.argv) == 2 and sys.argv[1] in {'snapshot', 'freeze', 'verify'}
    {'snapshot': snapshot, 'freeze': freeze, 'verify': verify}[sys.argv[1]]()
