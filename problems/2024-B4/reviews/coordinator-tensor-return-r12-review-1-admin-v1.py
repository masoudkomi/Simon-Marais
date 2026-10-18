"""TR12 OTHER WHOLE1 documentary integrity only; no mathematical code."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
BASE = 'problems/2024-B4/reviews/coordinator-tensor-return-r12-review-1-'
AUTHOR = 'problems/2024-B4/notes/coordinator-tensor-return-r12-'
PARENT = 'problems/2024-B4/reviews/reasoning-frobenius-return-r11-review-1-'
FORBIDDEN = ('problems/2024-B4/reviews/coordinator-tensor-return-r12-review-2-',
             'problems/2024-B4/reviews/reasoning-tensor-return-r12-review-2-',
             'problems/2021-B4/reviews/reasoning-center-return-r22-review-')
AUTHOR_ID = {'path': AUTHOR + 'freeze-v1.json', 'bytes': 1749,
             'sha256': 'd55148b98cfcf714fc80c88e92942d84181261185c212e7f4331a484025677a0'}
PARENT_ID = {'path': PARENT + 'manifest-v1.json', 'bytes': 2291,
             'sha256': '99179f71005561367a6b6b98639bdfac539e7023c63996d2592d6073241dd36d'}


def now():
    return datetime.now(timezone.utc).isoformat()


def rec(path):
    assert not path.startswith(FORBIDDEN), 'Embargoed NEW peer'
    raw = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}


def obj(path):
    assert not path.startswith(FORBIDDEN)
    return json.loads((ROOT / path).read_text())


def check(rows):
    for row in rows:
        assert rec(row['path']) == {k: row[k] for k in ('path', 'bytes', 'sha256')}, row['path']


def unique(rows):
    out = {}
    for row in rows:
        clean = {k: row[k] for k in ('path', 'bytes', 'sha256')}
        assert row['path'] not in out or out[row['path']] == clean, row['path']
        out[row['path']] = clean
    return [out[p] for p in sorted(out)]


def summary(rows):
    raw = json.dumps(unique(rows), sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(rows), 'unique_paths': len(unique(rows)),
            'canonical_deduplicated_sha256': hashlib.sha256(raw).hexdigest()}


def put(suffix, data):
    with (ROOT / (BASE + suffix)).open('x') as stream:
        stream.write(json.dumps(data, indent=2) + '\n')


def current():
    check([AUTHOR_ID, PARENT_ID])
    author_rows = obj(AUTHOR + 'freeze-v1.json')['payloads'] + [AUTHOR_ID]
    assert len(author_rows) == 5
    check(author_rows)
    author_base = obj(AUTHOR + 'baseline-v1.json')
    guard = author_base['direct_inputs']
    check(guard + [author_base['immutable_authority_binding']])
    authority = obj('problems/2024-B4/reviews/reasoning-frobenius-return-r10-acceptance.json')
    assert authority['unresolved_substantive_issues'] == 0
    old_rows = [authority['candidate'], authority['accepted_copy']] + authority['verification_metadata']
    check(old_rows)
    old = summary(old_rows)
    expected = author_base['authority_declared_summary']
    assert (old['occurrences'], old['unique_paths'], old['canonical_deduplicated_sha256']) == (
        expected['occurrences'], expected['unique_paths'], expected['canonical_sha256'])
    total = summary(guard + old_rows)
    expected = author_base['all_guard_summary']
    assert (total['occurrences'], total['unique_paths'], total['canonical_deduplicated_sha256']) == (
        expected['occurrences'], expected['unique_paths'], expected['canonical_sha256'])
    parent_rows = obj(PARENT + 'manifest-v1.json')['payloads'] + [PARENT_ID]
    assert len(parent_rows) == 5
    check(parent_rows)
    parent_direct = obj(PARENT + 'baseline-v1.json')['direct_records']
    check(parent_direct)
    return author_rows + guard + old_rows + parent_rows, parent_direct


def protect(baseline):
    rows, parent_direct = current()
    assert unique(rows) == baseline['direct_records']
    assert summary(rows) == baseline['current_occurrence_summary']
    assert summary(parent_direct) == baseline['parent_declared_guard_summary']
    assert summary(unique(rows) + parent_direct) == baseline['effective_fresh_guard_summary']


mode = sys.argv[1]
if mode == 'prepare':
    rows, parent_direct = current()
    put('baseline-v1.json', {
        'prepared_utc': now(), 'direct_records': unique(rows),
        'current_occurrence_summary': summary(rows),
        'parent_ENTIRE_identity': PARENT_ID,
        'parent_declared_guard_metadata_bound_not_recopied': rec(PARENT + 'baseline-v1.json'),
        'parent_declared_guard_summary': summary(parent_direct),
        'parent_historical_effective_guard_not_recursively_reexecuted': obj(PARENT + 'manifest-v1.json')['effective_fresh_guard_summary'],
        'effective_fresh_guard_summary': summary(unique(rows) + parent_direct),
        'fingerprints_are_integrity_not_fresh_mathematical_read_claims': True,
        'corresponding_NEW_peer_finding_file_inventory_hash_metadata_public_verdict_seen': False,
        'mathematical_program_or_author_old_script_executed': False})
    print(json.dumps({'mode': mode, 'current': summary(rows),
                      'effective_fresh': summary(unique(rows) + parent_direct)}))
elif mode == 'freeze':
    baseline = obj(BASE + 'baseline-v1.json')
    protect(baseline)
    labels = re.findall(r'^\|(TR12-R1-\d{2})\|', (ROOT / (BASE + 'report-v1.md')).read_text(), re.M)
    assert labels == ['TR12-R1-' + str(i).zfill(2) for i in range(1, 49)]
    paths = sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / 'problems/2024-B4/reviews').glob('coordinator-tensor-return-r12-review-1-*'))
    assert len(paths) == 4, paths
    put('manifest-v1.json', {
        'frozen_utc': now(), 'reviewer': '/root/review_2021_reasoning_j15_r2',
        'role': 'OTHER initially blind ENTIRE WHOLE1', 'whole_obligations': 48,
        'payload_count': 4, 'ENTIRE_files': 5, 'payloads': [rec(path) for path in paths],
        'current_occurrence_summary': baseline['current_occurrence_summary'],
        'effective_fresh_guard_summary': baseline['effective_fresh_guard_summary'],
        'FULL_final_ALL4_payload_model_readback_completed': True,
        'FULL_manifest_model_readback_then_SEPARATE_readonly_verify_REQUIRED': True,
        'corresponding_NEW_B_TR12_finding_file_actual_inventory_hash_metadata_public_verdict_seen': False,
        'corresponding_peer_completion_identity_received': False,
        'NEW_TR12_constructive_contribution': False,
        'old_accepted_input_and_FR11_roles_disclosed_not_new_self_recertification': True,
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
