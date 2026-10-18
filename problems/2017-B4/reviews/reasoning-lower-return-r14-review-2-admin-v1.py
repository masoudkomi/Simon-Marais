"""NEW documentary integrity only. No mathematical evaluation or replay.

snapshot, then FULL final all-payload MODEL readback; freeze, then FULL
manifest MODEL readback; verify in a SEPARATE read-only process.
"""
import hashlib
import json
from pathlib import Path
import re
import sys
from datetime import datetime, timezone

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
P = 'problems/2017-B4/reviews/reasoning-lower-return-r14-review-2-'
A = 'problems/2017-B4/notes/reasoning-lower-return-r14-'
AF = A + 'freeze-v1.json'
AB = A + 'baseline-v1.json'
PARENT = 'problems/2022-B4/notes/reasoning-critical-return-r11-freeze-v1.json'
EXPECTED = {
    AF: (2710, '54f1548395da878a822fcf78dfd472819ae09d3a70b021d56b507710c4a9dbad'),
    A + 'candidate-v1.md': (18859, '697c6ebe1f78429a456cfa2a8e100a4fb252365431f61ae41c4aa5208899b22a'),
    PARENT: (2538, '789bff4a55821c867d0e1d627f3f3c961940f570e812e8bc35980f96b9e8e3a7'),
}
BASE = P + 'baseline-v1.json'
FREEZE = P + 'manifest-v1.json'
PAYLOADS = [P + s for s in ['initial-v1.md', 'sources-v1.json', 'admin-v1.py', 'baseline-v1.json']]

def now():
    return datetime.now(timezone.utc).isoformat()

def path(p):
    assert not p.startswith('problems/2017-B4/reviews/reasoning-lower-return-r14-review-1-')
    relative = Path(p)
    assert not relative.is_absolute() and '..' not in relative.parts
    return ROOT / relative

def read(p):
    return json.loads(path(p).read_text())

def fp(p):
    b = path(p).read_bytes()
    row = {'path': p, 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}
    if p in EXPECTED:
        assert (row['bytes'], row['sha256']) == EXPECTED[p], p
    return row

def check(row):
    assert fp(row['path']) == row, row['path']

def summary(rows):
    unique = {}
    for row in rows:
        assert row['path'] not in unique or unique[row['path']] == row
        unique[row['path']] = row
    raw = json.dumps([unique[p] for p in sorted(unique)], sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(rows), 'unique_paths': len(unique), 'canonical_deduplicated_sha256': hashlib.sha256(raw).hexdigest()}

def put(p, obj):
    with path(p).open('x') as stream:
        json.dump(obj, stream, indent=2, ensure_ascii=False)
        stream.write('\n')

def declarations():
    binding = read(AB)['binding']
    rows = binding['direct_theorem_inputs'] + [binding['own_immediate_parent_binding']] + binding['own_parent_payload_records']
    for info in binding['accepted_authorities']:
        check(info['authority'])
        authority = read(info['authority']['path'])
        assert authority['status'] == 'proved, independently reviewed scoped partial result'
        assert authority['whole_initials_blind'] is True
        assert authority['unresolved_substantive_issues'] == 0
        declared = [authority['candidate'], authority['accepted_copy']] + authority['verification_metadata']
        for row in declared:
            check(row)
        assert summary(declared) == info['declared_summary']
        assert path(authority['accepted_copy']['path']).read_bytes().endswith(path(authority['candidate']['path']).read_bytes())
        rows += declared
    for row in rows:
        check(row)
    result = summary(rows)
    assert result == binding['effective_guard_summary']
    assert result == read(AF)['effective_guard_summary']
    return result

def labels():
    author = re.findall(r'^\|LF14-(\d\d)\|', path(A + 'obligations-v1.md').read_text(), flags=re.M)
    reviewer = re.findall(r'^### LF14-(\d\d) — PASS:', path(PAYLOADS[0]).read_text(), flags=re.M)
    expected = [str(i).zfill(2) for i in range(1, 57)]
    assert author == reviewer == expected
    sources = read(PAYLOADS[1])
    assert sources['whole_obligations'] == 56 and sources['independent_effective_readback'] is None
    assert sources['corresponding_NEW_root_LF14_findings_files_actual_inventory_hash_metadata_access'] is False
    return {'author_literal_obligations': len(author), 'review_literal_dispositions': len(reviewer), 'closed_scope_notes': 10, 'mathematical_truth_checked_by_code': False}

def snapshot():
    author = read(AF)
    assert author['ENTIRE_files'] == 9 and author['whole_obligations'] == 56
    check(fp(AF))
    for row in author['payload_records']:
        check(row)
    parent = read(PARENT)
    check(fp(PARENT))
    for row in parent['payload_records']:
        check(row)
    direct = read(AB)['binding']['direct_theorem_inputs']
    rows = [fp(AF)] + author['payload_records'] + direct + [fp(PARENT)] + parent['payload_records']
    for row in rows:
        check(row)
    count = parent['older_plus_NEW5_own_paths_bound_transitively']
    put(BASE, {
        'snapshot_utc': now(),
        'direct_guard_records': rows,
        'direct_guard_summary': summary(rows),
        'ALL_author_declared_fingerprints_verified_compact_summary': declarations(),
        'author_baseline_binding_no_historical_inventory_recopy': fp(AB),
        'own_immediate_parent': fp(PARENT),
        'older_own_paths_bound_transitively': count,
        'older_plus_NEW5_own_paths_bound_transitively': count + 5,
        'literal_checks': labels(),
        'corresponding_NEW_root_LF14_actual_inventory_open_hash_metadata_access': False,
        'documentary_only': True,
    })
    print(json.dumps({'snapshot': fp(BASE), 'at_utc': now()}))

def baseline_check():
    base = read(BASE)
    for row in base['direct_guard_records']:
        check(row)
    assert summary(base['direct_guard_records']) == base['direct_guard_summary']
    assert declarations() == base['ALL_author_declared_fingerprints_verified_compact_summary']
    assert labels() == base['literal_checks']
    return base

def freeze():
    base = baseline_check()
    put(FREEZE, {
        'frozen_utc': now(),
        'role': 'OTHER initially blind ENTIRE WHOLE2 LF14A-D',
        'reviewer': '/root/review_2022_complexity_r2',
        'NEW_constructor_C_excluded': True,
        'ENTIRE_files': 5,
        'whole_obligations': 56,
        'payload_records': [fp(p) for p in PAYLOADS],
        'author_main': fp(A + 'candidate-v1.md'),
        'author_freeze': fp(AF),
        'direct_guard_summary': base['direct_guard_summary'],
        'ALL_author_declared_fingerprints_verified_compact_summary': base['ALL_author_declared_fingerprints_verified_compact_summary'],
        'own_immediate_parent': base['own_immediate_parent'],
        'older_own_paths_bound_transitively': base['older_own_paths_bound_transitively'],
        'older_plus_NEW5_own_paths_bound_transitively': base['older_plus_NEW5_own_paths_bound_transitively'],
        'literal_checks': base['literal_checks'],
        'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'independent_effective_readback': None,
        'FULL_final_MODEL_ALL4_payload_readback_completed': True,
        'FULL_manifest_MODEL_readback_then_SEPARATE_readonly_verify_required': True,
        'corresponding_NEW_root_LF14_findings_files_actual_inventory_hash_metadata_access': False,
        'findings_EMBARGO_until_explicit_BOTH_ENTIRE': True,
        'mathematical_program_CAS_scan_test_optimizer_source_author_old_replay': False,
        'Git_shared_old_cache_mutation_spawn_charge_contact_bypass': False,
        'weekly': read(PAYLOADS[1])['weekly'],
    })
    print(json.dumps({'freeze': fp(FREEZE), 'at_utc': now()}))

def verify():
    base = baseline_check()
    manifest = read(FREEZE)
    assert manifest['ENTIRE_files'] == 5 and manifest['whole_obligations'] == 56
    assert [r['path'] for r in manifest['payload_records']] == PAYLOADS
    for row in manifest['payload_records']:
        check(row)
    assert manifest['literal_checks'] == base['literal_checks']
    print(json.dumps({'SEPARATE_readonly_verify': 'PASS', 'at_utc': now(), 'manifest': fp(FREEZE), 'ENTIRE_files': 5, 'whole_obligations': 56, 'direct_guard_summary': base['direct_guard_summary'], 'author_declarations': base['ALL_author_declared_fingerprints_verified_compact_summary'], 'mathematical_truth_checked_by_code': False}))

if __name__ == '__main__':
    assert len(sys.argv) == 2 and sys.argv[1] in {'snapshot', 'freeze', 'verify'}
    {'snapshot': snapshot, 'freeze': freeze, 'verify': verify}[sys.argv[1]]()
