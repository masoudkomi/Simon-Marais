#!/usr/bin/env python3
"""NEW D9 documentary integrity only. No map/orbit/source code is run."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
REL = 'problems/2022-B4/notes/reasoning-dynamics-return-r9-'
PARENT = 'problems/2020-B4/reviews/reasoning-arithmetic-return-r14-review-2-reaudit-v1.1-manifest.json'
PARENT_EXPECT = (3879, '4183b31f780a567146793ae74fdabfd6ac9a52ff92efb105f177869b6ae34e4f')
INTERIM = REL + 'interim-v1.md'
INTERIM_EXPECT = (3448, '77a6ac9c69f6668ac66cab77b648208c3340764d1d054630fabb61bbbef17c35')
INTERIM_FREEZE = REL + 'interim-freeze-v1.json'
INTERIM_FREEZE_EXPECT = (734, 'ebca4c438b6cbae4645c92f306a3fe479ecc73478ac0671f5ee608f507607591')
PAYLOADS = [REL + x for x in [
    'candidate-v1.md', 'obligations-v1.md', 'constructor-checks-v1.md',
    'issues-failures-v1.md', 'sources-v1.md', 'sources-v1.json',
    'worklog-v1.md', 'admin-v1.py', 'baseline-v1.json',
    'input-validation-v1.json', 'metadata-v1.json']]
FREEZE = REL + 'freeze-v1.json'
AUTHORITIES = [
    'problems/2022-B4/reviews/reasoning-dynamics-return-r8-acceptance',
    'problems/2022-B4/reviews/reasoning-dynamics-return-r7-acceptance',
    'problems/2022-B4/reviews/reasoning-fiber-return-r5-acceptance']

def now():
    return datetime.now(timezone.utc).isoformat()

def record(path):
    b = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}

def readj(path):
    return json.loads((ROOT / path).read_text())

def check(r):
    got = record(r['path'])
    assert got == r, (r['path'], 'fingerprint changed')
    return got

def expected(path, value):
    return check({'path': path, 'bytes': value[0], 'sha256': value[1]})

def write_new(path, obj):
    with (ROOT / path).open('x') as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
        f.write('\n')

def summary(rows):
    dedup = {}
    for r in rows:
        if r['path'] in dedup:
            assert dedup[r['path']] == r
        dedup[r['path']] = r
    ordered = sorted(dedup.values(), key=lambda r: r['path'])
    raw = json.dumps(ordered, sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(rows), 'unique_paths': len(ordered),
            'canonical_deduplicated_sha256': hashlib.sha256(raw).hexdigest()}, ordered

def inputs():
    rows = [expected(PARENT, PARENT_EXPECT), expected(INTERIM, INTERIM_EXPECT),
            expected(INTERIM_FREEZE, INTERIM_FREEZE_EXPECT)]
    parent = readj(PARENT)
    assert parent['ENTIRE_files'] == 11
    assert len(parent['payloads']) == 10
    rows += [check(r) for r in parent['payloads']]
    bindings = []
    for stem in AUTHORITIES:
        rows += [record(stem + '.md'), record(stem + '.json')]
        authority = readj(stem + '.json')
        accepted = check(authority['accepted_copy'])
        candidate = check(authority['candidate'])
        assert (ROOT / accepted['path']).read_bytes().endswith(
            (ROOT / candidate['path']).read_bytes())
        rows += [accepted, candidate]
        bindings.append({'authority': stem + '.json', 'body': accepted,
                         'exact_candidate_suffix': True,
                         'historical_inventory_reexpanded': False})
    rows += [record('AGENTS.md'), record('problems/2022-B4/statement.md'),
             record('problems/2022-B4/notes/reasoning-dynamics-return-r8-sources-v1.md'),
             record('problems/2022-B4/notes/reasoning-dynamics-return-r8-failed-routes-v1.md')]
    return rows, {'own_parent_ENTIRE_files_verified': 11,
                  'own_parent_guard_summary_bound_by_identity': parent['guard_summary'],
                  'interim_both_bytes_unchanged': True,
                  'current_accepted_bindings': bindings,
                  'no_historical_inventory_recursive_copy': True,
                  'no_old_executable_or_mathematical_instance_run': True}

def labels():
    text = (ROOT / (REL + 'obligations-v1.md')).read_text()
    found = re.findall(r'^\|(D9-\d{2})\|', text, flags=re.M)
    assert found == ['D9-%02d' % i for i in range(1, 49)]
    return {'whole_obligations': 48, 'distinct_labels': 48,
            'label_check_is_not_mathematical_proof': True}

def prepare():
    assert not (ROOT / FREEZE).exists()
    rows, details = inputs()
    totals, dedup = summary(rows)
    write_new(REL + 'baseline-v1.json', {
        'captured_at_utc': now(), 'status': 'documentary integrity only',
        'guard_summary': totals, 'details': details, 'guards': dedup})
    write_new(REL + 'input-validation-v1.json', {
        'validated_at_utc': now(), 'status': 'documentary PASS only',
        'labels': labels(), 'guard_summary': totals,
        'own_immediate_parent_ENTIRE_preserved': True,
        'interim_preserved': True,
        'accepted_current_exact_suffixes_verified': True,
        'mathematical_map_source_or_old_program_executed': False})
    write_new(REL + 'metadata-v1.json', {
        'created_at_utc': now(), 'status': 'candidate proof - unverified',
        'constructor': '/root/review_2017_coarsening_r1',
        'root_NEW_proof_contribution': False,
        'two_OTHER_initially_blind_ENTIRE_whole_reviews_required': True,
        'constructor_excluded': True, 'proposed_claims': ['D9A', 'D9B', 'D9C', 'D9D'],
        'whole_obligations': 48, 'payload_files': 11, 'ENTIRE_files': 12,
        'requested_model': 'gpt-6.1-sol', 'requested_reasoning': 'max',
        'verified_effective_readback': None,
        'FULL_final_ALL11_payload_model_readback_REQUIRED_before_freeze': True,
        'FULL_freeze_model_readback_then_SEPARATE_verify_REQUIRED': True,
        'mathematical_code_CAS_scan_test_source_author_or_old_replay': False,
        'old_shared_Git_cache_mutation_spawn_charge_contact_bypass': False,
        'pending_tool_or_native_child': False,
        'only_authorized_weekly_reset': 1792874445,
        'last_direct_TOTAL_percent': 53, 'TOTAL_ceiling_percent': 90,
        'integration_reserve': True, 'automatic_later_window': False,
        'annual_solution_actual_infinite_avoider_or_priority_claim': False})
    print(json.dumps({'prepared': True, 'guard_summary': totals, 'labels': labels()}))

def check_baseline():
    b = readj(REL + 'baseline-v1.json')
    for r in b['guards']:
        check(r)
    current_rows, details = inputs()
    totals, dedup = summary(current_rows)
    assert totals == b['guard_summary'] and dedup == b['guards']
    assert details == b['details']
    assert readj(REL + 'input-validation-v1.json')['labels'] == labels()
    return b

def freeze(attested):
    assert attested, 'Do FULL final model readback first; then attest explicitly.'
    b = check_baseline()
    write_new(FREEZE, {
        'frozen_at_utc': now(), 'status': 'candidate proof - unverified',
        'constructor': '/root/review_2017_coarsening_r1',
        'two_OTHER_initially_blind_ENTIRE_whole_reviews_required': True,
        'constructor_excluded': True, 'whole_obligations': 48,
        'payload_files': 11, 'ENTIRE_files': 12,
        'immediate_own_parent': record(PARENT),
        'preserved_interim': record(INTERIM),
        'preserved_interim_freeze': record(INTERIM_FREEZE),
        'guard_summary': b['guard_summary'],
        'FULL_final_model_readback_ALL11_payloads_completed': True,
        'FULL_freeze_model_readback_then_SEPARATE_verify_REQUIRED': True,
        'mathematical_execution_or_old_author_source_replay': False,
        'payloads': [record(p) for p in PAYLOADS]})
    print(json.dumps({'freeze': record(FREEZE), 'at_utc': readj(FREEZE)['frozen_at_utc']}))

def verify():
    f = readj(FREEZE)
    assert f['ENTIRE_files'] == len(f['payloads']) + 1 == 12
    assert {r['path'] for r in f['payloads']} == set(PAYLOADS)
    for r in f['payloads']:
        check(r)
    b = check_baseline()
    assert b['guard_summary'] == f['guard_summary']
    print(json.dumps({'SEPARATE_readonly_verify': 'PASS', 'verified_at_utc': now(),
                      'ENTIRE_files': 12, 'whole_obligations': 48,
                      'guard_summary': b['guard_summary'],
                      'main': record(REL + 'candidate-v1.md'),
                      'freeze': record(FREEZE)}, indent=2))

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
