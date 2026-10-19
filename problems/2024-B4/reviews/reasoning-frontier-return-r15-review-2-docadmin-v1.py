"""NEW documentary-only byte/JSON helper. No mathematics or author/old replay."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sys

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PREFIX = 'problems/2024-B4/reviews/reasoning-frontier-return-r15-review-2-'
AUTHOR = 'problems/2024-B4/notes/reasoning-frontier-return-r15-'
PAYLOADS = [PREFIX + suffix for suffix in
            ('initial-v1.md', 'sources-v1.json', 'docadmin-v1.py', 'baseline-v1.json')]
BASE = ROOT / PAYLOADS[3]
MANIFEST = ROOT / (PREFIX + 'manifest-v1.json')
PARENT = {'path': 'problems/2025-B4/reviews/reasoning-joint-trace-return-r13-review-1-manifest-v1.json',
          'bytes': 2240, 'sha256': 'c526c121b9d0cc62f3ce3294ca79e8fb107e1677aa1075533f91d2eec9286ddc'}
NAMES = ['reasoning-classification-return-r14', 'reasoning-frobenius-return-r10',
         'reasoning-frobenius-return-r11', 'coordinator-tensor-return-r12',
         'coordinator-tensor-family-return-r13']

def utc():
    return datetime.now(timezone.utc).isoformat()

def row(path):
    data = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def write_new(path, value):
    assert str(path.relative_to(ROOT)).startswith(PREFIX)
    with path.open('x', encoding='utf-8') as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write('\n')

def prepare():
    paths = ['AGENTS.md', 'problems/2024-B4/statement.md']
    paths.extend(AUTHOR + suffix for suffix in
                 ('candidate-v1.md', 'sources-v1.json', 'admin-v1.py',
                  'baseline-v1.json', 'freeze-v1.json'))
    pairs = []
    for name in NAMES:
        proof = 'problems/2024-B4/proofs/reviewed-' + name + '-v1.1.md'
        auth = 'problems/2024-B4/reviews/' + name + '-acceptance'
        paths.extend([proof, auth + '.md', auth + '.json'])
        pairs.append((proof, auth + '.json'))
    paths.append(PARENT['path'])
    assert len(paths) == len(set(paths)) == 23
    guards = [row(path) for path in paths]
    by_path = {r['path']: r for r in guards}
    assert by_path[PARENT['path']] == PARENT
    freeze_path = AUTHOR + 'freeze-v1.json'
    assert by_path[freeze_path]['bytes'] == 2505
    assert by_path[freeze_path]['sha256'] == 'd5d9804d237c368818cfaa7dcc9dda188cb474f7c4f5b7e97d50e1d561b283d2'
    declared = json.loads((ROOT / freeze_path).read_text())
    assert len(declared['payloads']) == 4
    for payload in declared['payloads']:
        assert by_path[payload['path']] == payload
    assert by_path[AUTHOR + 'candidate-v1.md']['bytes'] == 19639
    assert by_path[AUTHOR + 'candidate-v1.md']['sha256'] == 'b12c04780620c440ee88fb734ef97e25c85ed5b21402198a672c153938082ffa'
    for proof, authority in pairs:
        accepted = json.loads((ROOT / authority).read_text())['accepted_copy']
        assert by_path[proof] == accepted
    summary = {'occurrences': len(guards), 'unique_paths': len(by_path),
               'canonical_deduplicated_sha256': hashlib.sha256(json.dumps(guards, sort_keys=True).encode()).hexdigest()}
    write_new(BASE, {'prepared_UTC': utc(), 'guards': guards, 'guard_summary': summary,
                    'ONE_OWN_parent_manifest': PARENT, 'author_payloads_match_freeze': 4,
                    'current_accepted_copy_authorities_match': 5,
                    'guard_policy': 'Necessary exact paths ONCE; parent outer binding only; no recursive historical or mutable-map inventory',
                    'mathematical_read_or_truth_inferred_from_hash': False,
                    'NEW_corresponding_F15_peer_access': False,
                    'NEW_JT13_peer_access': False, 'PH13_peer_access': False})
    print(json.dumps({'baseline': row(PAYLOADS[3]), 'guard_summary': summary}, indent=2))

def freeze():
    baseline = json.loads(BASE.read_text())
    initial = (ROOT / PAYLOADS[0]).read_text()
    # Literal label presence, NOT mathematical verification.
    assert all('F15-O' + str(i).zfill(2) in initial for i in range(1, 25))
    sources = json.loads((ROOT / PAYLOADS[1]).read_text())
    manifest = {'frozen_UTC': utc(), 'status': 'sealed initially blind whole2; explicit BOTH release required',
                'reviewer': 'C /root/review_2017_coarsening_r1', 'ENTIRE_files': 5,
                'ALL_obligations': 24, 'payloads': [row(path) for path in PAYLOADS],
                'guard_summary': baseline['guard_summary'], 'ONE_OWN_parent_manifest': PARENT,
                'FULL_final_ALL4_payload_MODEL_readbacks_completed': True,
                'FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_REQUIRED': True,
                'NEW_corresponding_F15_peer_access_before_entire_freeze': False,
                'NEW_JT13_peer_access': False, 'PH13_peer_access': False,
                'root_R28_future_access': False, 'mathematical_executable_or_old_replay': False,
                'author_documentary_code_executed': False,
                'Git_shared_old_cache_configuration_mutation': False,
                'requested': sources['requested'], 'independent_effective_backend_readback': None,
                'start_quota': sources['start_quota'], 'latest_direct_quota': sources['latest_direct_quota']}
    write_new(MANIFEST, manifest)
    print(json.dumps({'manifest': row(str(MANIFEST.relative_to(ROOT))), 'frozen_UTC': manifest['frozen_UTC']}, indent=2))

def verify():
    manifest = json.loads(MANIFEST.read_text())
    baseline = json.loads(BASE.read_text())
    assert manifest['ENTIRE_files'] == 5 and manifest['ALL_obligations'] == 24
    assert len(manifest['payloads']) == 4
    for declared in manifest['payloads']:
        assert row(declared['path']) == declared, declared['path']
    for declared in baseline['guards']:
        assert row(declared['path']) == declared, declared['path']
    summary = {'occurrences': len(baseline['guards']),
               'unique_paths': len({r['path'] for r in baseline['guards']}),
               'canonical_deduplicated_sha256': hashlib.sha256(json.dumps(baseline['guards'], sort_keys=True).encode()).hexdigest()}
    assert summary == baseline['guard_summary'] == manifest['guard_summary']
    assert manifest['ONE_OWN_parent_manifest'] == baseline['ONE_OWN_parent_manifest'] == PARENT
    print(json.dumps({'SEPARATE_readonly_documentary_verify': 'PASS', 'verified_UTC': utc(),
                      'manifest': row(str(MANIFEST.relative_to(ROOT))), 'payloads_match': 4,
                      'necessary_input_guards_preserved': summary,
                      'no_mathematical_truth_check': True, 'no_recursive_parent_access': True}, indent=2))

if __name__ == '__main__':
    {'prepare': prepare, 'freeze': freeze, 'verify': verify}[sys.argv[1]]()
