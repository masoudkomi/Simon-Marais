"""NEW documentary helper only. No mathematical calculation or old helper replay."""
from pathlib import Path
import hashlib
import json
import sys
from datetime import datetime, timezone

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PREFIX = 'problems/2024-B4/notes/reasoning-frontier-return-r15-'
BASE = ROOT / (PREFIX + 'baseline-v1.json')
FREEZE = ROOT / (PREFIX + 'freeze-v1.json')
PAYLOADS = [PREFIX + s for s in ('candidate-v1.md', 'sources-v1.json', 'admin-v1.py', 'baseline-v1.json')]
PARENT = {'path': 'problems/2021-B4/reviews/coordinator-contact-return-r27-review-1-manifest-v1.json',
          'bytes': 2703, 'sha256': '9fcdbb714f87a0915b5864c9a98cd8d6c12d3b1bf50f7ad2aedb82590d2c9c79'}
NAMES = ['reasoning-classification-return-r14', 'reasoning-frobenius-return-r10',
         'reasoning-frobenius-return-r11', 'coordinator-tensor-return-r12',
         'coordinator-tensor-family-return-r13']

def utc():
    return datetime.now(timezone.utc).isoformat()

def row(path):
    data = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def write_new(path, value):
    with path.open('x', encoding='utf-8') as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write('\n')

def prepare():
    # Guard each necessary current payload ONCE; no recursive parent inventory.
    paths = ['AGENTS.md', 'problems/2024-B4/statement.md']
    pairs = []
    for name in NAMES:
        proof = 'problems/2024-B4/proofs/reviewed-' + name + '-v1.1.md'
        auth = 'problems/2024-B4/reviews/' + name + '-acceptance'
        paths.extend([proof, auth + '.md', auth + '.json'])
        pairs.append((proof, auth + '.json'))
    paths.append(PARENT['path'])
    guards = [row(path) for path in paths]
    by_path = {r['path']: r for r in guards}
    for proof, authority in pairs:
        declared = json.loads((ROOT / authority).read_text())['accepted_copy']
        assert by_path[proof] == declared, (proof, 'current accepted-copy identity mismatch')
    assert by_path[PARENT['path']] == PARENT, 'OWN parent mismatch'
    summary = {'occurrences': len(guards), 'unique_paths': len(by_path),
               'canonical_deduplicated_sha256': hashlib.sha256(json.dumps(guards, sort_keys=True).encode()).hexdigest()}
    write_new(BASE, {'prepared_UTC': utc(), 'purpose': 'Necessary immutable current input guards ONCE; no recursive historical inventory',
                     'guards': guards, 'guard_summary': summary, 'compact_OWN_parent': PARENT,
                     'maps_guarded': False, 'accepted_metadata_embedded_histories_expanded': False,
                     'parent_payloads_opened_or_hashed_recursively': False,
                     'guard_read_scope': 'Hashing is documentary, never a mathematical MODEL read claim.',
                     'quota': {'usedPercent': 84, 'windowDurationMins': 10080, 'resetsAt': 1792874445,
                               'ordinaryUsageAllowed': True, 'TOTAL_ceiling': 90, 'checkpoint_near': 85,
                               'integration_review_reserve': True, 'automatic_later_window': False}})
    print(json.dumps({'baseline': row(str(BASE.relative_to(ROOT))), 'guard_summary': summary}, indent=2))

def freeze():
    baseline = json.loads(BASE.read_text())
    main = (ROOT / PAYLOADS[0]).read_text()
    # Literal documentary labels only, not mathematical verification.
    assert all('F15-O' + str(i).zfill(2) in main for i in range(1, 25))
    value = {'frozen_UTC': utc(), 'status': 'candidate proof - unverified; bounded actual-factor/failure checkpoint',
             'constructor': '/root/review_2021_reasoning_j15_r2', 'constructor_excluded_from_OTHER_reviews': True,
             'root_NEW_inference_contribution': False, 'claims': ['DS1', 'DS2', 'DS3'],
             'whole_obligations': 24, 'ENTIRE_files': 5, 'payloads': [row(path) for path in PAYLOADS],
             'guard_summary': baseline['guard_summary'], 'compact_OWN_parent': PARENT,
             'new_exponent_classification': False, 'remaining_global_divisor_compatibility_gap': True,
             'TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits_required': True,
             'FULL_final_ALL4_payload_MODEL_readbacks_completed': True,
             'FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_REQUIRED': True,
             'mathematical_truth_checked_by_code': False,
             'old_source_author_helper_freezer_or_certificate_replay': False,
             'Git_shared_old_cache_configuration_mutation': False,
             'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
             'independent_effective_backend_readback': None, 'quota': baseline['quota']}
    write_new(FREEZE, value)
    print(json.dumps({'manifest': row(str(FREEZE.relative_to(ROOT))), 'frozen_UTC': value['frozen_UTC']}, indent=2))

def verify():
    manifest = json.loads(FREEZE.read_text())
    for declared in manifest['payloads']:
        assert row(declared['path']) == declared, declared['path']
    baseline = json.loads(BASE.read_text())
    assert manifest['guard_summary'] == baseline['guard_summary']
    assert manifest['compact_OWN_parent'] == baseline['compact_OWN_parent'] == PARENT
    assert manifest['whole_obligations'] == 24 and len(manifest['payloads']) == 4
    # Input guards are preserved as exact once-checked records; no recursive replay.
    print(json.dumps({'SEPARATE_readonly_documentary_verify': 'PASS', 'verified_UTC': utc(),
                      'manifest': row(str(FREEZE.relative_to(ROOT))), 'payloads_match': 4,
                      'once_checked_necessary_input_guard_summary': baseline['guard_summary'],
                      'no_mathematical_truth_check': True}, indent=2))

if __name__ == '__main__':
    {'prepare': prepare, 'freeze': freeze, 'verify': verify}[sys.argv[1]]()
