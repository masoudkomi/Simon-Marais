"""New LF14 review1 documentary checks only; no mathematics or old replay."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
P = 'problems/2017-B4/reviews/reasoning-lower-return-r14-review-1-'
A = 'problems/2017-B4/notes/reasoning-lower-return-r14-'
FREEZE = A + 'freeze-v1.json'
BASE = P + 'baseline-v1.json'
MANIFEST = P + 'manifest-v1.json'
FILES = [P + x for x in ('initial-v1.md', 'sources-v1.json', 'admin-v1.py', 'baseline-v1.json')]
AUTHORITIES = [
    'problems/2017-B4/reviews/reasoning-pressure-return-r11-acceptance.json',
    'problems/2017-B4/reviews/reasoning-concentration-return-r12-acceptance.json']
DIRECT = [
    'AGENTS.md', 'problems/2017-B4/statement.md',
    'problems/2017-B4/proofs/reviewed-reasoning-pressure-return-r11-v1.1.md',
    'problems/2017-B4/reviews/reasoning-pressure-return-r11-acceptance.md',
    AUTHORITIES[0],
    'problems/2017-B4/proofs/reviewed-reasoning-concentration-return-r12-v1.1.md',
    'problems/2017-B4/reviews/reasoning-concentration-return-r12-acceptance.md',
    AUTHORITIES[1]]
EXPECTED = {
    FREEZE: (2710, '54f1548395da878a822fcf78dfd472819ae09d3a70b021d56b507710c4a9dbad'),
    A + 'candidate-v1.md': (18859, '697c6ebe1f78429a456cfa2a8e100a4fb252365431f61ae41c4aa5208899b22a'),
    DIRECT[0]: (4707, '28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff'),
    DIRECT[2]: (26687, '56688cd6030db910fbbc9162436b25acbf61a69869e2501dbd6f50b088bc3b60'),
    DIRECT[5]: (24123, '15823ad1a7c54b8e06de3692f19d3395d2458786dcb8d2d51a2eb3c592734554')}


def now():
    return datetime.now(timezone.utc).isoformat()


def path(name):
    p = Path(name)
    assert not p.is_absolute() and '..' not in p.parts
    assert 'reasoning-lower-return-r14-review-2-' not in name
    assert 'reasoning-negative-return-r23-review-' not in name
    assert 'coordinator-tensor-family-return-r13-review-' not in name
    result = (ROOT / p).resolve()
    assert result.is_relative_to(ROOT)
    return result


def record(name):
    b = path(name).read_bytes()
    r = {'path': name, 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}
    if name in EXPECTED:
        assert (r['bytes'], r['sha256']) == EXPECTED[name], name
    return r


def check(r):
    assert record(r['path']) == r, r['path']


def read(name):
    return json.loads(path(name).read_text())


def put(name, value):
    with path(name).open('x') as f:
        json.dump(value, f, indent=2)
        f.write('\n')


def summary(rows):
    unique = {}
    for r in rows:
        assert r['path'] not in unique or unique[r['path']] == r
        unique[r['path']] = r
    data = json.dumps([unique[p] for p in sorted(unique)],
                      sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(rows), 'unique_paths': len(unique),
            'canonical_deduplicated_sha256': hashlib.sha256(data).hexdigest()}


def inputs():
    f = read(FREEZE)
    assert f['ENTIRE_files'] == 9 and f['whole_obligations'] == 56
    assert f['constructor_excluded'] is True
    rows = [record(FREEZE)]
    for r in f['payload_records']:
        check(r)
        rows.append(r)
    assert len(rows) == 9
    rows += [record(p) for p in DIRECT]
    authorities = []
    for p in AUTHORITIES:
        a = read(p)
        assert a['whole_initials_blind'] is True
        assert a['unresolved_substantive_issues'] == 0
        assert a['status'] == 'proved, independently reviewed scoped partial result'
        declared = [a['candidate'], a['accepted_copy']] + a['verification_metadata']
        for r in declared:
            check(r)
        assert path(a['accepted_copy']['path']).read_bytes().endswith(
            path(a['candidate']['path']).read_bytes())
        rows += declared
        authorities.append({'authority': record(p), 'declared': summary(declared),
                            'accepted_copy_exact_candidate_suffix': True})
    return {'records': rows, 'summary': summary(rows), 'current_authorities': authorities,
            'no_transitive_or_future_NEW_peer_inventory_import': True,
            'previous_root_R18_initial_separately_sealed_not_input': True}


def labels():
    text = path(P + 'initial-v1.md').read_text()
    found = re.findall(r'^\|LF14-(\d\d)\|PASS\|', text, re.M)
    assert found == [f'{i:02}' for i in range(1, 57)]
    s = read(P + 'sources-v1.json')
    assert s['initially_blind_whole_obligations'] == 56
    assert s['NEW_corresponding_review2_findings_actual_files_inventory_open_hash_metadata_access'] is False
    return 56


def validate():
    b = read(BASE)
    assert b['inputs'] == inputs()
    assert b['whole_obligations'] == labels()
    return b


mode = sys.argv[1]
if mode == 'baseline':
    assert not path(MANIFEST).exists()
    put(BASE, {'prepared_utc': now(), 'inputs': inputs(),
               'whole_obligations': labels(), 'reviewer': '/root',
               'author_ENTIRE_files_read': 9,
               'initially_blind': True, 'NEW_peer_access': False,
               'ALL_obligations_issues_sources_logs_code_metadata_embedded': True,
               'mathematical_program_or_author_source_old_replay': False})
    print(json.dumps({'baseline_created': record(BASE), 'whole_obligations': 56}))
elif mode == 'freeze':
    b = validate()
    put(MANIFEST, {'frozen_utc': now(), 'reviewer': '/root',
                   'constructor': '/root/review_2017_coarsening_r1',
                   'constructor_excluded': True, 'ENTIRE_files': 5,
                   'whole_obligations': 56, 'initially_blind': True,
                   'payload_records': [record(p) for p in FILES],
                   'input_summary': b['inputs']['summary'],
                   'FULL_final_MODEL_ALL4_payload_readback_completed': True,
                   'FULL_manifest_MODEL_readback_then_SEPARATE_verify_required': True,
                   'NEW_peer_findings_actual_files_inventory_hash_metadata_access': False,
                   'findings_sealed_pending_explicit_BOTH': True})
    print(json.dumps({'manifest': record(MANIFEST), 'ENTIRE_files': 5}))
elif mode == 'verify':
    validate()
    m = read(MANIFEST)
    assert m['ENTIRE_files'] == 5 and m['whole_obligations'] == 56
    assert [r['path'] for r in m['payload_records']] == FILES
    for r in m['payload_records']:
        check(r)
    print(json.dumps({'separate_readonly_verified_utc': now(), 'PASS': True,
                      'ENTIRE_files': 5, 'whole_obligations': 56,
                      'report': record(P + 'initial-v1.md'),
                      'manifest': record(MANIFEST)}))
else:
    raise SystemExit('baseline | freeze | verify')
