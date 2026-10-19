#!/usr/bin/env python3
"""NEW documentary-only IT12 fingerprint/label helper; NO mathematical computation.

Only writes this new namespace's baseline/freeze. Does not execute any old
script, inspect peer review inventories, or decide any proof obligation.
"""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
BASE = 'problems/2022-B4/notes/reasoning-itinerary-return-r12-'
PAYLOADS = [BASE + 'candidate-v1.md', BASE + 'sources-v1.json',
            BASE + 'admin-v1.py', BASE + 'baseline-v1.json']
BASELINE = ROOT / (BASE + 'baseline-v1.json')
FREEZE = ROOT / (BASE + 'freeze-v1.json')
PARENT = 'problems/2021-B4/reviews/reasoning-deep-return-r24-review-1-'
PARENT_MANIFEST = PARENT + 'manifest-v1.json'
GUARDS = [
    'AGENTS.md', 'problems/2022-B4/statement.md',
    'problems/2022-B4/proofs/reviewed-reasoning-dynamics-return-r9-v1.1.md',
    'problems/2022-B4/reviews/reasoning-dynamics-return-r9-acceptance.md',
    'problems/2022-B4/reviews/reasoning-dynamics-return-r9-acceptance.json',
    'problems/2022-B4/proofs/reviewed-reasoning-collision-return-r10-v1.1.md',
    'problems/2022-B4/reviews/reasoning-collision-return-r10-acceptance.md',
    'problems/2022-B4/reviews/reasoning-collision-return-r10-acceptance.json',
    'problems/2022-B4/proofs/reviewed-reasoning-critical-return-r11-v1.1.md',
    'problems/2022-B4/reviews/reasoning-critical-return-r11-acceptance.md',
    'problems/2022-B4/reviews/reasoning-critical-return-r11-acceptance.json',
    PARENT_MANIFEST, PARENT + 'initial-v1.md', PARENT + 'sources-v1.json',
    PARENT + 'admin-v1.py', PARENT + 'baseline-v1.json'
]
EXPECTED = {
    'AGENTS.md': '28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff',
    GUARDS[2]: '7cfa2c60557935261d7144576f0e39a509fbebb292fdd0027415efe411ae4c55',
    GUARDS[5]: '269bb65792e1c31159b4443726af84083657fe73e8a1440e3cc72ee0c9c99989',
    GUARDS[8]: 'f85d1c1a05bcf3b6c8d1a632babd6dce87e2c9bc59165c943172a19d5eb7128e',
    PARENT_MANIFEST: '656ae411b5dec3730370ba1615143afcb78e9d270b0972bfb916a80482f0d3e5',
    PARENT + 'initial-v1.md': 'f6d0352337ab949810e9c495bdd2babff84bb2c9f71895b93fde1437d6da9e61',
    PARENT + 'sources-v1.json': 'b59e8d63cde96c4e2cd80e9992112ba40d23332f02601f8640799085948609d1',
    PARENT + 'admin-v1.py': '21ca4cf06f62e6968eb1c4c922ca1e30fa2acd0e5e00a942bc6f139f410c58f4',
    PARENT + 'baseline-v1.json': 'd9297dd3dde10fd8501cd283d10b59d14ff82ef94472de5b7206ab799d5c6307'
}

def record(rel):
    data = (ROOT / rel).read_bytes()
    return {'path': rel, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def check(rec):
    assert record(rec['path']) == rec, 'Fingerprint changed: ' + rec['path']

def write_new(path, value):
    assert not path.exists(), 'Refuse overwrite: ' + str(path)
    path.write_text(json.dumps(value, indent=2) + '\n')

def labels():
    text = (ROOT / PAYLOADS[0]).read_text()
    found = re.findall(r'^\|O12-(\d{2})\|', text, re.M)
    assert found == [f'{k:02}' for k in range(1, 41)], 'Literal ledger labels'
    return len(found)

def baseline():
    records = [record(rel) for rel in GUARDS]
    for item in records:
        if item['path'] in EXPECTED:
            assert item['sha256'] == EXPECTED[item['path']], item['path']
    parent = json.loads((ROOT / PARENT_MANIFEST).read_text())
    for item in parent['payloads']:
        check(item)
    value = {
        'observed_UTC': datetime.now(timezone.utc).isoformat(),
        'status': 'Necessary immutable guards; compact exact own-parent binding',
        'immutable_inputs': records,
        'immediate_own_parent': record(PARENT_MANIFEST),
        'parent_declared_occurrences': parent['declared_occurrences_verified'],
        'parent_declared_unique_paths': parent['unique_paths'],
        'historical_parent_inventory_freshly_expanded': False,
        'mutable_observations_NOT_immutable_guards': [record('problems/2022-B4/research.md')],
        'new_peer_review_inventory_content_hash_metadata_access': False,
        'source_full_paper_downloads': False
    }
    write_new(BASELINE, value)
    print(json.dumps({'baseline': record(BASE + 'baseline-v1.json'), 'immutable_guards': len(records)}))

def freeze():
    old = json.loads(BASELINE.read_text())
    for item in old['immutable_inputs']:
        check(item)
    for rel in PAYLOADS:
        assert (ROOT / rel).is_file(), rel
    json.loads((ROOT / PAYLOADS[1]).read_text())
    n = labels()
    value = {
        'frozen_UTC': datetime.now(timezone.utc).isoformat(),
        'status': 'candidate proof - unverified; requires TWO OTHER whole audits',
        'author': '/root/review_2022_complexity_r2',
        'constructor_excluded_from_independent_review_count': True,
        'ENTIRE_files': 5, 'payload_count': 4, 'whole_obligations': n,
        'claims': ['IT12A', 'IT12B', 'IT12C', 'IT12D'],
        'payloads': [record(rel) for rel in PAYLOADS],
        'necessary_immutable_inputs': len(old['immutable_inputs']),
        'immediate_own_parent': old['immediate_own_parent'],
        'FULL_final_ALL4_payload_MODEL_readbacks_completed_before_freeze': True,
        'FULL_manifest_MODEL_readback_then_SEPARATE_readonly_verify_REQUIRED': True,
        'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'independent_effective_backend_readback': None,
        'quota': {'usedPercent': 75, 'observed_UTC': '2026-10-19 00:20:17 UTC',
                  'resetsAt': 1792874445, 'windowDurationMins': 10080,
                  'ordinaryUsageAllowed': True, 'TOTAL_ceiling': 90,
                  'integration_review_reserve': True, 'automatic_later_window_spending': False},
        'mathematical_program_CAS_scan_test_old_replay': False,
        'Git_shared_old_cache_mutation': False
    }
    write_new(FREEZE, value)
    print(json.dumps(record(BASE + 'freeze-v1.json')))

def verify():
    value = json.loads(FREEZE.read_text())
    for item in value['payloads']:
        check(item)
    old = json.loads(BASELINE.read_text())
    for item in old['immutable_inputs']:
        check(item)
    assert value['whole_obligations'] == labels() == 40
    assert value['ENTIRE_files'] == len(value['payloads']) + 1 == 5
    print(json.dumps({'SEPARATE_readonly_verify_UTC': datetime.now(timezone.utc).isoformat(),
        'documentary_status': 'PASS', 'ENTIRE_files': 5, 'literal_obligations': 40,
        'immutable_guards': len(old['immutable_inputs']),
        'manifest': record(BASE + 'freeze-v1.json'),
        'mathematical_verification_claimed': False}))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['baseline', 'freeze', 'verify'])
    args = parser.parse_args()
    {'baseline': baseline, 'freeze': freeze, 'verify': verify}[args.mode]()
