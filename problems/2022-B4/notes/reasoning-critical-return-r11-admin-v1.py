"""NEW documentary helper ONLY. No orbit/formula/inequality evaluation.

snapshot -> create this prefix's compact baseline;
freeze -> only after FULL final MODEL readback of all four payloads;
verify -> SEPARATE read-only process after FULL manifest MODEL readback.
No old helper is executed. No peer inventory is constructed.
"""
import hashlib
import json
from pathlib import Path
import re
import sys
from datetime import datetime, timezone

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PREFIX = 'problems/2022-B4/notes/reasoning-critical-return-r11-'
PARENT = 'problems/2024-B4/reviews/coordinator-tensor-family-return-r13-review-2-manifest-v1.json'
EXPECTED_PARENT = '6e4b3e9f647c3f9b28de04a0a461d5858be53bef3a134e0be099fdc7d49957ff'
BASELINE = PREFIX + 'baseline-v1.json'
FREEZE = PREFIX + 'freeze-v1.json'
PAYLOADS = [PREFIX + x for x in ['candidate-v1.md', 'sources-v1.json', 'admin-v1.py', 'baseline-v1.json']]
GUARDS = [
    'AGENTS.md',
    'problems/2022-B4/statement.md',
    'problems/2022-B4/proofs/reviewed-reasoning-dynamics-return-r9-v1.1.md',
    'problems/2022-B4/reviews/reasoning-dynamics-return-r9-acceptance.md',
    'problems/2022-B4/reviews/reasoning-dynamics-return-r9-acceptance.json',
    'problems/2022-B4/proofs/reviewed-reasoning-collision-return-r10-v1.1.md',
    'problems/2022-B4/reviews/reasoning-collision-return-r10-acceptance.md',
    'problems/2022-B4/reviews/reasoning-collision-return-r10-acceptance.json',
    'problems/2022-B4/proofs/reviewed-reasoning-fiber-return-r5-v1.1.md',
    'problems/2022-B4/proofs/reviewed-arithmetic-complexity-v1.1.md',
    'problems/2022-B4/proofs/reviewed-reasoning-return-r5-v1.1.md',
    PARENT,
]
OBSERVATIONS = ['problems/2022-B4/research.md', 'problems/2022-B4/references.md']

def now():
    return datetime.now(timezone.utc).isoformat()

def read_json(path):
    return json.loads((ROOT / path).read_text())

def fp(path):
    b = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}

def check(row):
    actual = fp(row['path'])
    assert actual == row, (row, actual)

def canonical(rows):
    raw = json.dumps(sorted(rows, key=lambda r: r['path']), sort_keys=True, separators=(',', ':')).encode()
    return hashlib.sha256(raw).hexdigest()

def create(path, obj):
    with (ROOT / path).open('x') as stream:
        json.dump(obj, stream, indent=2, ensure_ascii=False)
        stream.write('\n')

def literal_checks():
    text = (ROOT / PAYLOADS[0]).read_text()
    labels = re.findall(r'^### O11-(\d\d) — ', text, flags=re.M)
    assert labels == [str(i).zfill(2) for i in range(1, 49)], labels
    sources = read_json(PAYLOADS[1])
    assert sources['whole_obligations'] == 48
    assert sources['independent_effective_readback'] is None
    assert sources['root_NEW_mathematical_contribution'] is False
    return {'literal_obligations': len(labels), 'closed_scope_notes': 8, 'mathematical_truth_checked_by_code': False}

def guard_check():
    base = read_json(BASELINE)
    for row in base['immutable_guard_records']:
        check(row)
    assert canonical(base['immutable_guard_records']) == base['guard_summary']['canonical_sha256']
    # These are mutable coordinator observations, deliberately NOT identity guards.
    return base

def snapshot():
    assert fp(PARENT)['sha256'] == EXPECTED_PARENT
    parent = read_json(PARENT)
    parent_rows = parent['payload_records']
    for row in parent_rows:
        check(row)
    all_paths = GUARDS + [row['path'] for row in parent_rows]
    assert len(all_paths) == len(set(all_paths))
    rows = [fp(path) for path in all_paths]
    known = {
        'AGENTS.md': '28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff',
        'problems/2022-B4/proofs/reviewed-reasoning-dynamics-return-r9-v1.1.md': '7cfa2c60557935261d7144576f0e39a509fbebb292fdd0027415efe411ae4c55',
        'problems/2022-B4/proofs/reviewed-reasoning-collision-return-r10-v1.1.md': '269bb65792e1c31159b4443726af84083657fe73e8a1440e3cc72ee0c9c99989',
    }
    for row in rows:
        if row['path'] in known:
            assert row['sha256'] == known[row['path']]
    count = parent['older_plus_NEW5_own_paths_bound_transitively']
    create(BASELINE, {
        'snapshot_utc': now(),
        'purpose': 'Compact immutable current inputs and immediate OWN sealed parent; no historical inventory recopy',
        'immutable_guard_records': rows,
        'guard_summary': {'occurrences': len(rows), 'unique_paths': len(rows), 'canonical_sha256': canonical(rows)},
        'mutable_current_observations_NOT_future_identity_guards': [fp(path) for path in OBSERVATIONS],
        'own_immediate_parent': fp(PARENT),
        'older_own_paths_bound_transitively': count,
        'older_plus_NEW5_own_paths_bound_transitively': count + 5,
        'corresponding_NEW_peer_inventory_or_content_access': False,
        'literal_checks': literal_checks(),
        'documentary_only_no_mathematical_evaluation': True,
    })
    print(json.dumps({'snapshot': fp(BASELINE), 'guards': len(rows), 'older_own_paths': count, 'new_total_own_paths': count + 5, 'at_utc': now()}))

def freeze():
    base = guard_check()
    checks = literal_checks()
    create(FREEZE, {
        'frozen_utc': now(),
        'status': 'candidate proof - unverified',
        'constructor': '/root/review_2022_complexity_r2',
        'constructor_excluded_from_TWO_OTHER_whole_audits': True,
        'root_NEW_construction_contribution': False,
        'ENTIRE_files': 5,
        'whole_obligations': 48,
        'payload_records': [fp(path) for path in PAYLOADS],
        'guard_summary': base['guard_summary'],
        'own_immediate_parent': base['own_immediate_parent'],
        'older_own_paths_bound_transitively': base['older_own_paths_bound_transitively'],
        'older_plus_NEW5_own_paths_bound_transitively': base['older_plus_NEW5_own_paths_bound_transitively'],
        'literal_checks': checks,
        'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'independent_effective_readback': None,
        'FULL_final_MODEL_ALL4_payload_readback_completed': True,
        'FULL_manifest_MODEL_readback_then_SEPARATE_readonly_verify_required': True,
        'corresponding_NEW_A2024R13_peer_access': False,
        'NEW2020R18_peer_access': False,
        'mathematical_program_CAS_scan_test_source_author_old_replay': False,
        'Git_shared_old_cache_mutation_spawn_charge_contact_bypass': False,
        'weekly': read_json(PAYLOADS[1])['weekly'],
    })
    print(json.dumps({'freeze': fp(FREEZE), 'at_utc': now()}))

def verify():
    manifest = read_json(FREEZE)
    assert manifest['ENTIRE_files'] == 5
    assert manifest['whole_obligations'] == 48
    assert [r['path'] for r in manifest['payload_records']] == PAYLOADS
    for row in manifest['payload_records']:
        check(row)
    base = guard_check()
    assert manifest['guard_summary'] == base['guard_summary']
    assert manifest['literal_checks'] == literal_checks()
    print(json.dumps({'SEPARATE_readonly_verify': 'PASS', 'at_utc': now(), 'freeze': fp(FREEZE), 'payloads': 4, 'whole_obligations': 48, 'guards': base['guard_summary'], 'mathematical_truth_checked_by_code': False}))

if __name__ == '__main__':
    assert len(sys.argv) == 2 and sys.argv[1] in {'snapshot', 'freeze', 'verify'}
    {'snapshot': snapshot, 'freeze': freeze, 'verify': verify}[sys.argv[1]]()
