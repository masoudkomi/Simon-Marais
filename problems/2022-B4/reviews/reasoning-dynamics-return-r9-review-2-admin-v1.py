#!/usr/bin/env python3
"""NEW D9 WHOLE2 documentary integrity only; never evaluate mathematics."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
REL = 'problems/2022-B4/reviews/reasoning-dynamics-return-r9-review-2-'
AUTHOR = 'problems/2022-B4/notes/reasoning-dynamics-return-r9-'
AUTHOR_FREEZE = AUTHOR + 'freeze-v1.json'
AUTHOR_EXPECT = (3635, '4427de51ab82207eb673d983f9abfedec5553f783bbd1093e29f6ca49659036a')
TARGET = AUTHOR + 'candidate-v1.md'
TARGET_EXPECT = (16389, 'e15f1ad442916acda5c27cff79107dcf0236b1f4f748f7f5e521214bad6b410c')
PARENT = 'problems/2025-B4/reviews/reasoning-diagonal-return-r8-review-1-manifest-v1.json'
PARENT_EXPECT = (4363, '1087dc101f639a64fc56c6621e7c0687da7058d8aacfe57c902cfcc738fe34d7')
PAYLOADS = [REL + name for name in [
    'initial-v1.md', 'ledger-v1.md', 'issues-v1.md', 'sources-v1.md',
    'sources-v1.json', 'worklog-v1.md', 'admin-v1.py',
    'baseline-v1.json', 'input-validation-v1.json']]
FREEZE = REL + 'manifest-v1.json'
CURRENT = [
    'problems/2022-B4/reviews/reasoning-dynamics-return-r8-acceptance.json',
    'problems/2022-B4/reviews/reasoning-dynamics-return-r7-acceptance.json',
    'problems/2022-B4/reviews/reasoning-fiber-return-r5-acceptance.json']
WEEKLY = {'at_utc': '2026-10-18 17:34:30 UTC',
          'method': 'own same-awaited clock/get_usage_limits',
          'TOTAL_used_percent': 56, 'window_minutes': 10080,
          'resetsAt': 1792874445, 'ordinaryUsageAllowed': True,
          'legacy_by_limit_agree': True,
          'account_label': '029a8928...1334ac3a',
          'TOTAL_ceiling_percent': 90, 'integration_reserve': True,
          'automatic_later_window_spending': False}


def now():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    prefix = 'problems/2022-B4/reviews/reasoning-dynamics-return-r9-'
    assert not path.startswith(prefix) or path.startswith(REL), 'NEW peer path forbidden'
    assert not Path(path).is_absolute() and '..' not in Path(path).parts
    return (ROOT / path).read_bytes()


def readj(path):
    return json.loads(raw(path))


def record(path):
    b = raw(path)
    return {'path': path, 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}


def check(r):
    got = record(r['path'])
    assert got == r, (r['path'], 'fingerprint changed')
    return got


def expected(path, identity):
    return check({'path': path, 'bytes': identity[0], 'sha256': identity[1]})


def write_new(path, obj):
    assert path in PAYLOADS + [FREEZE] and path.startswith(REL)
    with (ROOT / path).open('x') as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
        f.write('\n')


def summary(rows):
    unique = {}
    for r in rows:
        if r['path'] in unique:
            assert unique[r['path']] == r
        unique[r['path']] = r
    ordered = sorted(unique.values(), key=lambda r: r['path'])
    canonical = json.dumps(ordered, sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(rows), 'unique_paths': len(ordered),
            'canonical_sha256': hashlib.sha256(canonical).hexdigest()}, ordered


def labels():
    wanted = ['D9-%02d' % i for i in range(1, 49)]
    a = re.findall(r'^\|(D9-\d{2})\|', raw(AUTHOR + 'obligations-v1.md').decode(), re.M)
    b = re.findall(r'^\|(D9-\d{2})\|', raw(REL + 'ledger-v1.md').decode(), re.M)
    assert a == b == wanted
    return {'whole_obligations': 48, 'separate_reviewer_dispositions': 48,
            'label_matching_is_not_mathematical_proof': True}


def inputs():
    rows = [expected(AUTHOR_FREEZE, AUTHOR_EXPECT)]
    f = readj(AUTHOR_FREEZE)
    assert f['ENTIRE_files'] == 12 and len(f['payloads']) == 11
    assert f['whole_obligations'] == 48
    assert all(r['path'].startswith(AUTHOR) for r in f['payloads'])
    rows += [check(r) for r in f['payloads']]
    expected(TARGET, TARGET_EXPECT)
    b = readj(AUTHOR + 'baseline-v1.json')
    rows += [check(r) for r in b['guards']]
    assert len(b['guards']) == 29
    current = []
    protected = {r['path'] for r in rows}
    for path in CURRENT:
        assert path in protected
        authority = readj(path)
        assert authority['status'] == 'proved, independently reviewed scoped partial result'
        for key in ['accepted_copy', 'candidate']:
            assert authority[key]['path'] in protected
            check(authority[key])
        assert raw(authority['accepted_copy']['path']).endswith(raw(authority['candidate']['path']))
        current.append({'authority': path, 'accepted_copy': authority['accepted_copy'],
                        'candidate_suffix_byte_identical': True,
                        'historical_metadata_reexpanded': False})
    rows += [expected(PARENT, PARENT_EXPECT)]
    p = readj(PARENT)
    assert p['ENTIRE_review_files_including_manifest'] == 10
    assert len(p['payloads']) == 9
    rows += [check(r) for r in p['payloads']]
    return rows, {
        'author_ENTIRE_files_verified': 12, 'author_whole_obligations': 48,
        'author_declared_guard_paths_verified': 29,
        'author_guard_summary_bound': f['guard_summary'],
        'current_accepted_bindings': current,
        'immediate_own_parent': record(PARENT),
        'immediate_own_parent_ENTIRE_files_verified': 10,
        'older_own_paths_bound_transitively': p['older_plus_new_own_paths_bound_transitively'],
        'older_plus_new_own_paths_bound_transitively': p['older_plus_new_own_paths_bound_transitively'] + 10,
        'historical_inventories_not_recursively_copied': True,
        'mathematical_or_old_executable_rerun': False}


def prepare():
    assert not (ROOT / FREEZE).exists()
    rows, details = inputs()
    totals, guards = summary(rows)
    write_new(REL + 'baseline-v1.json', {
        'captured_at_utc': now(), 'status': 'documentary preservation only',
        'guard_summary': totals, 'details': details, 'guards': guards})
    write_new(REL + 'input-validation-v1.json', {
        'validated_at_utc': now(), 'status': 'documentary PASS only',
        'labels': labels(), 'guard_summary': totals,
        'author_ENTIRE12_and_declared29_guards_preserved': True,
        'current_accepted_suffixes_verified': True,
        'own_parent_ENTIRE10_preserved': True,
        'mathematical_program_source_author_old_freezer_replayed': False,
        'corresponding_NEW_peer_path_access': False})
    print(json.dumps({'prepare': 'PASS', 'at_utc': now(),
                      'guard_summary': totals, 'labels': labels()}))


def check_baseline():
    b = readj(REL + 'baseline-v1.json')
    for r in b['guards']:
        check(r)
    rows, details = inputs()
    totals, guards = summary(rows)
    assert totals == b['guard_summary'] and guards == b['guards']
    assert details == b['details']
    assert readj(REL + 'input-validation-v1.json')['labels'] == labels()
    return b


def freeze(attested):
    assert attested, 'FULL final model readback of all9 payloads required first'
    b = check_baseline()
    write_new(FREEZE, {
        'frozen_at_utc': now(),
        'role': 'OTHER initially blind ENTIRE WHOLE2 initial review; findings sealed',
        'reviewer': '/root/review_2022_complexity_r2',
        'nonconstructor': True, 'constructor': '/root/review_2017_coarsening_r1',
        'constructor_excluded': True, 'root_supplied_new_inference': False,
        'target': record(TARGET), 'author_freeze': record(AUTHOR_FREEZE),
        'author_ENTIRE_files_read': 12, 'whole_obligations': 48,
        'separate_independent_hand_dispositions': 48,
        'ENTIRE_review_files_including_manifest': 10,
        'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'independent_effective_readback': None,
        'FULL_final_model_readback_ALL9_payloads_code_generated_metadata_completed': True,
        'FULL_manifest_model_readback_then_SEPARATE_readonly_verify_required': True,
        'guard_summary': b['guard_summary'],
        'immediate_own_parent': b['details']['immediate_own_parent'],
        'older_own_paths_bound_transitively': b['details']['older_own_paths_bound_transitively'],
        'older_plus_new_own_paths_bound_transitively': b['details']['older_plus_new_own_paths_bound_transitively'],
        'no_NEW_corresponding_peer_finding_file_actual_inventory_hash_metadata_commentary_access': True,
        'findings_embargoed_until_explicit_BOTH_ENTIRE_confirmation': True,
        'no_mathematical_program_CAS_scan_test_old_author_source_freezer_replay': True,
        'no_Git_shared_old_cache_mutation_spawn_charge_contact_bypass': True,
        'weekly': WEEKLY, 'payloads': [record(p) for p in PAYLOADS]})
    print(json.dumps({'freeze': 'PASS', 'at_utc': readj(FREEZE)['frozen_at_utc'],
                      'ENTIRE_files': 10, 'whole_obligations': 48,
                      'identity': record(FREEZE), 'main': record(REL + 'initial-v1.md'),
                      'administrative_only_handoff_until_BOTH': True}))


def verify():
    f = readj(FREEZE)
    assert f['ENTIRE_review_files_including_manifest'] == len(f['payloads']) + 1 == 10
    assert {r['path'] for r in f['payloads']} == set(PAYLOADS)
    for r in f['payloads']:
        check(r)
    b = check_baseline()
    assert f['guard_summary'] == b['guard_summary']
    assert f['whole_obligations'] == labels()['whole_obligations'] == 48
    print(json.dumps({'SEPARATE_readonly_verify': 'PASS', 'at_utc': now(),
                      'ENTIRE_files': 10, 'whole_obligations': 48,
                      'identity': record(FREEZE), 'main': record(REL + 'initial-v1.md'),
                      'guard_summary': b['guard_summary'], 'no_file_written': True,
                      'administrative_only_handoff_until_BOTH': True}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['prepare', 'freeze', 'verify'])
    parser.add_argument('--attest-final-model-readback', action='store_true')
    args = parser.parse_args()
    if args.mode == 'prepare':
        prepare()
    elif args.mode == 'freeze':
        freeze(args.attest_final_model_readback)
    else:
        verify()
