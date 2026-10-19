"""NEW documentary fixed-path SHA/JSON helper. No mathematical calculation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PREFIX = 'problems/2024-B4/reviews/reasoning-frontier-return-r15-review-1-'
AUTHOR = 'problems/2024-B4/notes/reasoning-frontier-return-r15-'
BASE = PREFIX + 'baseline-v1.json'
MANIFEST = PREFIX + 'manifest-v1.json'
PAYLOADS = [PREFIX + s for s in ('initial-v1.md', 'sources-v1.json', 'admin-v1.py', 'baseline-v1.json')]
PARENT = {'path': 'problems/2022-B4/reviews/reasoning-physical-return-r13-review-2-manifest-v1.json',
          'bytes': 2093, 'sha256': '18f11c5b855400d9c8c5de05aa99e8fec37c19524fc6b8551ee69bc9d8ed9f8a'}
NAMES = ['reasoning-classification-return-r14', 'reasoning-frobenius-return-r10',
         'reasoning-frobenius-return-r11', 'coordinator-tensor-return-r12',
         'coordinator-tensor-family-return-r13']

def utc():
    return datetime.now(timezone.utc).isoformat()

def row(path):
    data = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def read_json(path):
    return json.loads((ROOT / path).read_text())

def write_new(path, value):
    with (ROOT / path).open('x', encoding='utf-8') as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write('\n')

def labels():
    text = (ROOT / PAYLOADS[0]).read_text()
    found = re.findall(r'^\|F15R1-(\d\d)\|', text, re.M)
    assert found == [str(i).zfill(2) for i in range(1, 25)], found

def prepare():
    af = AUTHOR + 'freeze-v1.json'
    author = read_json(af)
    paths = ['AGENTS.md', 'problems/2024-B4/statement.md', af]
    paths += [r['path'] for r in author['payloads']]
    pairs = []
    for name in NAMES:
        proof = 'problems/2024-B4/proofs/reviewed-' + name + '-v1.1.md'
        auth = 'problems/2024-B4/reviews/' + name + '-acceptance'
        paths += [proof, auth + '.md', auth + '.json']
        pairs.append((proof, auth + '.json'))
    paths.append(PARENT['path'])
    assert len(paths) == len(set(paths)) == 23
    # Each necessary immutable path is bound once; no historical recursion.
    guards = [row(p) for p in paths]
    by_path = {r['path']: r for r in guards}
    assert by_path[af] == {'path': af, 'bytes': 2505, 'sha256': 'd5d9804d237c368818cfaa7dcc9dda188cb474f7c4f5b7e97d50e1d561b283d2'}
    for declared in author['payloads']:
        assert by_path[declared['path']] == declared, declared['path']
    for proof, authority in pairs:
        assert by_path[proof] == read_json(authority)['accepted_copy'], proof
    assert by_path[PARENT['path']] == PARENT
    write_new(BASE, {'prepared_UTC': utc(), 'purpose': 'Necessary immutable guards ONCE, no recursive inventories or mutable-map guards',
                     'guards': guards, 'guard_occurrences': len(guards), 'guard_unique_paths': len(by_path),
                     'ONE_exact_OWN_parent': PARENT, 'parent_payloads_or_inventory_expanded': False,
                     'guard_hashes_are_not_MODEL_read_claims': True,
                     'quota': {'usedPercent': 86, 'observed_UTC': '2026-10-19 03:56:41 UTC',
                               'resetsAt': 1792874445, 'TOTAL_ceiling': 90, 'reserve': True,
                               'automatic_later_window': False}})
    print(json.dumps({'baseline': row(BASE), 'necessary_paths': 23, 'status': 'PASS documentary identities only'}))

def freeze():
    assert '--FULL-final-ALL4-MODEL-readbacks-completed' in sys.argv
    labels()
    baseline = read_json(BASE)
    write_new(MANIFEST, {'frozen_UTC': utc(), 'status': 'sealed OTHER independent WHOLE1 initial; not promotion',
                         'reviewer': '/root/review_2022_complexity_r2', 'constructor_excluded': True,
                         'claims': ['DS1', 'DS2', 'DS3'], 'ENTIRE_files': 5, 'ALL_obligations': 24,
                         'payloads': [row(p) for p in PAYLOADS],
                         'guard_occurrences': baseline['guard_occurrences'], 'guard_unique_paths': baseline['guard_unique_paths'],
                         'ONE_exact_OWN_parent': PARENT, 'FULL_final_ALL4_payload_MODEL_readbacks_completed': True,
                         'FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_REQUIRED': True,
                         'findings_sealed_until_explicit_BOTH': True, 'corresponding_NEW_peer_access': False,
                         'no_mathematical_executable_or_old_replay': True,
                         'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
                         'independent_effective_backend_readback': None, 'quota': baseline['quota']})
    print(json.dumps({'manifest': row(MANIFEST)}))

def verify():
    manifest = read_json(MANIFEST)
    for declared in manifest['payloads']:
        assert row(declared['path']) == declared, declared['path']
    labels()
    baseline = read_json(BASE)
    assert manifest['ONE_exact_OWN_parent'] == baseline['ONE_exact_OWN_parent'] == PARENT
    assert manifest['ALL_obligations'] == 24 and len(manifest['payloads']) == 4
    assert baseline['guard_occurrences'] == baseline['guard_unique_paths'] == 23
    print(json.dumps({'SEPARATE_readonly_verify_UTC': utc(), 'status': 'PASS', 'ENTIRE_files': 5,
                      'literal_obligations': 24, 'once_bound_necessary_paths': 23, 'manifest': row(MANIFEST),
                      'writes': 0, 'mathematics_certified': False}))

if __name__ == '__main__':
    {'prepare': prepare, 'freeze': freeze, 'verify': verify}[sys.argv[1]]()
