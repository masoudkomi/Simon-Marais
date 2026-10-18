"""FR11 OTHER WHOLE1 documentary integrity; no mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
BASE = 'problems/2024-B4/reviews/reasoning-frobenius-return-r11-review-1-'
AUTHOR = 'problems/2024-B4/notes/reasoning-frobenius-return-r11-'
PARENT = 'problems/2021-B4/notes/reasoning-center-return-r22-'
FORBIDDEN = ('problems/2024-B4/reviews/reasoning-frobenius-return-r11-review-2-',
             'problems/2021-B4/reviews/reasoning-center-return-r22-review-')
AUTHOR_ID = {'path': AUTHOR + 'freeze-v1.json', 'bytes': 3460,
             'sha256': '90ba8a8a0d07918bc738696b9619cef07b3577c85af5fea82766f322c6af2e38'}
PARENT_ID = {'path': PARENT + 'freeze-v1.json', 'bytes': 2615,
             'sha256': '48f2fac48332fcde04d01e574b9f45c33e29375ceecc63afada5030058801c6f'}


def now():
    return datetime.now(timezone.utc).isoformat()


def rec(path):
    assert not path.startswith(FORBIDDEN), 'Embargoed NEW peer'
    data = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def obj(path):
    assert not path.startswith(FORBIDDEN)
    return json.loads((ROOT / path).read_text())


def check(rows):
    for row in rows:
        assert rec(row['path']) == {k: row[k] for k in ('path', 'bytes', 'sha256')}, row['path']


def unique(rows):
    result = {}
    for row in rows:
        clean = {k: row[k] for k in ('path', 'bytes', 'sha256')}
        assert row['path'] not in result or result[row['path']] == clean, row['path']
        result[row['path']] = clean
    return [result[p] for p in sorted(result)]


def summary(rows):
    clean = unique(rows)
    serial = json.dumps(clean, sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(rows), 'unique_paths': len(clean),
            'canonical_deduplicated_sha256': hashlib.sha256(serial).hexdigest()}


def put(suffix, data):
    with (ROOT / (BASE + suffix)).open('x') as stream:
        stream.write(json.dumps(data, indent=2) + '\n')


def current_rows():
    check([AUTHOR_ID, PARENT_ID])
    author_rows = obj(AUTHOR + 'freeze-v1.json')['payload_records'] + [AUTHOR_ID]
    assert len(author_rows) == 13
    check(author_rows)
    author_base = obj(AUTHOR + 'baseline-v1.json')
    guard = author_base['direct_operative_and_comparison_records']
    author_parent = author_base['immediate_own_parent']
    check([author_parent])
    ap = obj(author_parent['path'])
    guard = guard + [author_parent] + ap['payload_records']
    check(guard)
    author_summary = summary(guard)
    expected = author_base['all_guard_summary']
    assert author_summary['occurrences'] == expected['occurrences']
    assert author_summary['unique_paths'] == expected['unique_paths']
    assert author_summary['canonical_deduplicated_sha256'] == expected['canonical_sha256']
    fr10prefix = 'problems/2024-B4/reviews/reasoning-frobenius-return-r10-acceptance'
    fr10 = obj(fr10prefix + '.json')
    authority_rows = [fr10['candidate'], fr10['accepted_copy']] + fr10['verification_metadata']
    check(authority_rows)
    comparisons = []
    for r in (6, 7, 8, 9):
        prefix = 'problems/2024-B4/reviews/reasoning-cofactor-return-r' + str(r) + '-acceptance'
        current = obj(prefix + '.json')
        assert current['unresolved_substantive_issues'] == 0
        check([current['accepted_copy']])
        comparisons += [current['accepted_copy'], rec(prefix + '.md'), rec(prefix + '.json')]
    parent_rows = obj(PARENT + 'freeze-v1.json')['payloads'] + [PARENT_ID]
    assert len(parent_rows) == 9
    check(parent_rows)
    parent_declared = obj(PARENT + 'baseline-v1.json')['direct_records']
    check(parent_declared)
    rows = author_rows + guard + authority_rows + comparisons + parent_rows
    return rows, parent_declared, author_summary


def protect(baseline):
    rows, parent_declared, author_summary = current_rows()
    assert unique(rows) == baseline['direct_records']
    assert summary(rows) == baseline['current_occurrence_summary']
    assert summary(parent_declared) == baseline['parent_declared_current_guard_summary']
    assert summary(unique(rows) + parent_declared) == baseline['effective_fresh_guard_summary']
    assert author_summary == baseline['author_current_guard_summary']


mode = sys.argv[1]
if mode == 'prepare':
    rows, parent_declared, author_summary = current_rows()
    put('baseline-v1.json', {
        'prepared_utc': now(), 'direct_records': unique(rows),
        'current_occurrence_summary': summary(rows),
        'author_current_guard_summary': author_summary,
        'parent_ENTIRE_identity': PARENT_ID,
        'parent_declared_guard_metadata_bound_not_recopied': rec(PARENT + 'baseline-v1.json'),
        'parent_declared_current_guard_summary': summary(parent_declared),
        'parent_historical_effective_guard_bound_not_recursively_reexecuted': obj(PARENT + 'freeze-v1.json')['effective_guard_summary'],
        'effective_fresh_guard_summary': summary(unique(rows) + parent_declared),
        'fingerprint_read_not_full_mathematical_read_claim': True,
        'corresponding_NEW_peer_finding_file_inventory_hash_metadata_public_verdict_seen': False,
        'mathematical_program_or_author_old_script_executed': False})
    print(json.dumps({'mode': mode, 'current': summary(rows),
                      'effective_fresh': summary(unique(rows) + parent_declared)}))
elif mode == 'freeze':
    baseline = obj(BASE + 'baseline-v1.json')
    protect(baseline)
    labels = re.findall(r'^\|(FR11-R1-\d{2})\|', (ROOT / (BASE + 'report-v1.md')).read_text(), re.M)
    assert labels == ['FR11-R1-' + str(i).zfill(2) for i in range(1, 49)]
    paths = sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / 'problems/2024-B4/reviews').glob('reasoning-frobenius-return-r11-review-1-*'))
    assert len(paths) == 4, paths
    put('manifest-v1.json', {
        'frozen_utc': now(), 'reviewer': '/root/review_2021_reasoning_j15_r2',
        'role': 'OTHER initially blind ENTIRE WHOLE1', 'whole_obligations': 48,
        'payload_count': 4, 'ENTIRE_files': 5, 'payloads': [rec(path) for path in paths],
        'current_occurrence_summary': baseline['current_occurrence_summary'],
        'effective_fresh_guard_summary': baseline['effective_fresh_guard_summary'],
        'FULL_final_ALL4_payload_model_readback_completed': True,
        'FULL_manifest_model_readback_then_SEPARATE_readonly_verify_REQUIRED': True,
        'corresponding_NEW_B_FR11_finding_file_inventory_hash_metadata_public_verdict_seen': False,
        'corresponding_peer_completion_identity_received': False,
        'NEW_FR11_constructive_contribution': False,
        'older_accepted_input_roles_disclosed_not_newly_self_recertified': True,
        'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'independent_effective_setting_readback': None,
        'mathematical_program_CAS_scan_test_optimizer_source_author_old_replay': False,
        'findings_release_requires_explicit_BOTH_ENTIRE_confirmation': True,
        'status': 'Independent whole review recommendation only; root reconciliation required'})
    print(json.dumps(rec(BASE + 'manifest-v1.json')))
elif mode == 'verify':
    manifest = obj(BASE + 'manifest-v1.json')
    check(manifest['payloads'])
    protect(obj(BASE + 'baseline-v1.json'))
    print(json.dumps({'SEPARATE_readonly_verify_utc': now(), 'status': 'PASS',
                      'ENTIRE_files': 5, 'whole_obligations': 48,
                      'effective_fresh_guard_summary': manifest['effective_fresh_guard_summary'],
                      'report': rec(BASE + 'report-v1.md'),
                      'manifest': rec(BASE + 'manifest-v1.json')}))
else:
    raise SystemExit('Unknown documentary mode')
