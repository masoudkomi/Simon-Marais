"""NEW documentary byte/JSON/label helper only; no mathematical verification."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sys

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PREFIX = 'problems/2021-B4/notes/reasoning-coverage-synthesis-r30-'
PAYLOADS = [PREFIX + s for s in ('candidate-v1.md', 'sources-v1.json', 'docadmin-v1.py', 'baseline-v1.json')]
BASE = ROOT / PAYLOADS[3]
FREEZE = ROOT / (PREFIX + 'freeze-v1.json')
PARENT_PATH = 'problems/2022-B4/notes/reasoning-frontier-reserve-r14.md'

def utc():
    return datetime.now(timezone.utc).isoformat()

def row(path):
    data = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def write_new(path, value):
    assert str(path.relative_to(ROOT)).startswith(PREFIX)
    with path.open('x', encoding='utf-8') as out:
        json.dump(value, out, indent=2, ensure_ascii=False)
        out.write('\n')

def prepare():
    source = json.loads((ROOT / PAYLOADS[1]).read_text())
    paths = ['AGENTS.md', 'problems/2021-B4/statement.md']
    accepted = []
    for name in source['authorities_complete_current_MD_JSON_read']:
        auth = 'problems/2021-B4/reviews/' + name + '-acceptance'
        record = json.loads((ROOT / (auth + '.json')).read_text())
        proof = record['accepted_copy']
        assert row(proof['path']) == proof
        accepted.append(proof)
        paths.extend([proof['path'], auth + '.md', auth + '.json'])
    paths.append(PARENT_PATH)
    assert len(paths) == len(set(paths)) == 36
    guards = [row(path) for path in paths]
    summary = {'occurrences': len(guards), 'unique_paths': len(set(paths)),
               'canonical_deduplicated_sha256': hashlib.sha256(json.dumps(guards, sort_keys=True).encode()).hexdigest()}
    write_new(BASE, {'prepared_UTC': utc(), 'guards': guards, 'guard_summary': summary,
                     'current_accepted_copy_authorities_match': len(accepted),
                     'ONE_OWN_parent_note': guards[-1],
                     'guard_policy': 'Necessary accepted copies/MDJSON ONCE plus one exact own note; no recursive inventories/maps',
                     'hash_is_not_mathematical_read_or_truth': True,
                     'NEW_corresponding_R30_peer_access': False})
    print(json.dumps({'baseline': row(PAYLOADS[3]), 'guard_summary': summary}, indent=2))

def freeze():
    base = json.loads(BASE.read_text())
    source = json.loads((ROOT / PAYLOADS[1]).read_text())
    main = (ROOT / PAYLOADS[0]).read_text()
    assert all('R30-O' + str(i).zfill(2) in main for i in range(1, 13))
    # Documentary text length only, not a mathematical check.
    words = len(main.split())
    assert words <= 1200, words
    value = {'frozen_UTC': utc(), 'status': 'candidate proof - unverified; integration synthesis',
             'constructor': 'C /root/review_2017_coarsening_r1', 'constructor_excluded_from_OTHER_audits': True,
             'root_NEW_inference_contributor': False, 'ENTIRE_files': 5, 'ALL_obligations': 12,
             'claims': ['R30A', 'R30B expressly attributed corollary'], 'main_whitespace_word_count': words,
             'payloads': [row(path) for path in PAYLOADS], 'guard_summary': base['guard_summary'],
             'ONE_OWN_parent_note': base['ONE_OWN_parent_note'],
             'FULL_final_ALL4_payload_MODEL_readbacks_completed': True,
             'FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_REQUIRED': True,
             'TWO_OTHER_initially_blind_whole_audits_required': True,
             'NEW_corresponding_R30_peer_access': False, 'mathematical_executable_or_old_replay': False,
             'Git_shared_old_cache_configuration_mutation': False,
             'requested': source['requested'], 'independent_effective_backend_readback': None,
             'start_quota': source['start_quota']}
    write_new(FREEZE, value)
    print(json.dumps({'freeze': row(str(FREEZE.relative_to(ROOT))), 'frozen_UTC': value['frozen_UTC']}, indent=2))

def verify():
    manifest = json.loads(FREEZE.read_text())
    baseline = json.loads(BASE.read_text())
    for declared in manifest['payloads']:
        assert row(declared['path']) == declared
    for declared in baseline['guards']:
        assert row(declared['path']) == declared
    assert manifest['guard_summary'] == baseline['guard_summary']
    assert manifest['ONE_OWN_parent_note'] == baseline['ONE_OWN_parent_note']
    print(json.dumps({'SEPARATE_readonly_documentary_verify': 'PASS', 'verified_UTC': utc(),
                      'freeze': row(str(FREEZE.relative_to(ROOT))), 'payloads_match': 4,
                      'necessary_input_guards_preserved': baseline['guard_summary'],
                      'no_mathematical_truth_check': True, 'no_recursive_parent_access': True}, indent=2))

if __name__ == '__main__':
    {'prepare': prepare, 'freeze': freeze, 'verify': verify}[sys.argv[1]]()
