#!/usr/bin/env python3
"""NEW R9 documentary metadata only; no mathematical computation or old replay."""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PREFIX = 'problems/2024-B4/notes/reasoning-cofactor-return-r9-'
BASELINE = PREFIX + 'baseline-v1.json'
VALIDATION = PREFIX + 'input-validation-v1.json'
FREEZE = PREFIX + 'freeze-v1.json'
PARENT = 'problems/2025-B4/reviews/reasoning-diagonal-return-r7-review-2-manifest.json'
EXPECTED = {
    'AGENTS.md': (4707, '28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff'),
    PARENT: (5011, 'd31303212238ddb54cf775043b059a53757bdf99e948124c07bc96ee444dd366'),
    'problems/2024-B4/proofs/reviewed-structural-v1.1.md': (17079, '082dc054ce2cdaea80eee009f4c97c877c6968afb54b5a8f3141b7354031dd3f'),
    'problems/2024-B4/proofs/reviewed-reasoning-cofactor-return-r6-v1.1.md': (20658, 'fb988a13187b5765619532ad14077ae2f32a948e04704252e3d8981e10d65d98'),
    'problems/2024-B4/proofs/reviewed-reasoning-cofactor-return-r7-v1.1.md': (22608, 'b8e2cc3a37cf8c80c724c0d26f6768261e5d339fee073351e8b4c9b56b94cf72'),
    'problems/2024-B4/proofs/reviewed-reasoning-cofactor-return-r8-v1.1.md': (19878, 'acdfa8d740a762de8a4070867d6e9ebf68a1d54ff7a92e0a9126e2e339b19023'),
}
AUTHORITY = [
    'problems/2024-B4/reviews/structural-acceptance.json',
    'problems/2024-B4/reviews/reasoning-cofactor-return-r6-acceptance.json',
    'problems/2024-B4/reviews/reasoning-cofactor-return-r7-acceptance.json',
    'problems/2024-B4/reviews/reasoning-cofactor-return-r8-acceptance.json',
]
CONTEXT = [
    'AGENTS.md', 'problems/2024-B4/statement.md',
    'problems/2024-B4/notes/reasoning-cofactor-return-r8-issues-failures-v1.md',
    'problems/2024-B4/notes/reasoning-cofactor-return-r8-source-audit-v1.md',
    'problems/2024-B4/notes/reasoning-cofactor-return-r6-failed-routes-v1.md',
]
PAYLOAD_SUFFIXES = [
    'candidate-v1.md', 'obligations-v1.md', 'constructor-checks-v1.md',
    'issues-failures-v1.md', 'source-audit-v1.md', 'sources-v1.json',
    'worklog-v1.md', 'admin-v1.py', 'baseline-v1.json', 'input-validation-v1.json',
]


def now():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    p = Path(path)
    assert not p.is_absolute() and '..' not in p.parts
    assert 'reasoning-cofactor-return-r9-review-' not in path
    assert 'sq15' not in path.lower()
    return (ROOT / p).read_bytes()


def record(path):
    data = raw(path)
    got = {'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
    if path in EXPECTED:
        assert (got['bytes'], got['sha256']) == EXPECTED[path], path
    return got


def check(rec):
    assert record(rec['path']) == rec, rec['path']
    return rec


def read_json(path):
    return json.loads(raw(path))


def summary(records):
    unique = {}
    for rec in records:
        if rec['path'] in unique:
            assert unique[rec['path']] == rec
        unique[rec['path']] = rec
    canonical = json.dumps([unique[p] for p in sorted(unique)], sort_keys=True,
                           separators=(',', ':')).encode()
    return {'occurrences': len(records), 'unique_paths': len(unique),
            'canonical_deduplicated_sha256': hashlib.sha256(canonical).hexdigest()}


def gather():
    records = [record(p) for p in CONTEXT]
    suffixes = []
    scope_counts = []
    for authority in AUTHORITY:
        records.extend([record(authority), record(authority[:-5] + '.md')])
        meta = read_json(authority)
        accepted = meta.get('accepted_copy', meta.get('accepted_proof'))
        assert accepted is not None
        candidate = meta['candidate']
        records.extend([check(accepted), check(candidate)])
        if 'structural-' not in authority:
            assert raw(accepted['path']).endswith(raw(candidate['path']))
            suffixes.append(accepted['path'])
        scope_counts.append({'authority': authority,
                             'top_level_keys': sorted(meta),
                             'historical_inventory_copied': False})
    parent_record = record(PARENT)
    parent = read_json(PARENT)
    assert parent['older_plus_new_own_paths_bound_transitively'] == 875
    assert len(parent['payloads']) == 9
    records.append(parent_record)
    records.extend(check(rec) for rec in parent['payloads'])
    detail = {
        'necessary_guard_summary': summary(records),
        'four_current_authorities_and_exact_declared_bodies_verified': True,
        'accepted_immutable_candidate_suffixes_verified': suffixes,
        'structural_editorial_heading_scope': 'Accepted body/current authority bound exactly; not falsely called raw-candidate byte-identical suffix.',
        'authority_historical_inventory_bound_compactly': scope_counts,
        'own_immediate_parent_ENTIRE10_fingerprints_verified': True,
        'older_own_paths_bound_transitively': 875,
        'mathematical_assertions_evaluated_by_code': False,
        'no_old_executable_or_freezer_invoked': True,
    }
    return records, detail


def labels():
    expected = [f'O{k:02d}' for k in range(1, 65)]
    obligations = re.findall(r'^(O\d{2})\.', raw(PREFIX + 'obligations-v1.md').decode(), re.M)
    checks = re.findall(r'^(O\d{2}) — CHECKED', raw(PREFIX + 'constructor-checks-v1.md').decode(), re.M)
    assert obligations == expected and checks == expected
    return {'whole_obligation_labels': 64, 'separate_constructor_hand_dispositions': 64,
            'labels_exact_and_unique': True, 'mathematics_proved_by_this_label_check': False}


def write_new(path, value):
    assert path.startswith(PREFIX)
    with (ROOT / path).open('x', encoding='utf-8') as handle:
        json.dump(value, handle, indent=2, ensure_ascii=False)
        handle.write('\n')


def prepare():
    records, detail = gather()
    write_new(BASELINE, {'captured_at_utc': now(), 'records': records,
                         'summary': summary(records), 'detail': detail})
    write_new(VALIDATION, {'prepared_at_utc': now(), 'status': 'documentary PASS only',
                           **labels(), 'guard_detail': detail,
                           'constructor_excluded_from_TWO_OTHER_reviews': True,
                           'no_math_program_CAS_scan_test_optimizer_replay': True,
                           'no_corresponding_NEW_peer_R9_or_SQ15_material_access': True})
    print(json.dumps({'prepare': 'PASS', **summary(records), **labels()}))


def protected():
    baseline = read_json(BASELINE)
    for rec in baseline['records']:
        check(rec)
    records, detail = gather()
    assert records == baseline['records']
    assert summary(records) == baseline['summary']
    assert detail == baseline['detail']
    return detail


def freeze(attest):
    assert attest, 'FULL final model readback must precede the freeze command'
    detail = protected()
    labels()
    manifest = {
        'frozen_at_utc': now(), 'status': 'candidate proof - unverified',
        'constructor': '/root/review_2022_complexity_r2',
        'root_NEW_mathematical_contribution': False,
        'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'independent_effective_readback': None,
        'proposed_claims': ['R9A whole jet criterion', 'R9B reciprocal/cubic sufficient congruences',
                            'R9C actual NF4-failing ell15 family and scoped combined coverage',
                            'R9D variable-odd-part infinite family'],
        'whole_obligations': 64, 'constructor_hand_dispositions': 64,
        'TWO_OTHER_initially_blind_ENTIRE_WHOLE_reviews_required': True,
        'constructor_excluded': True,
        'ENTIRE_constructor_files_including_manifest': 11,
        'immediate_own_parent': record(PARENT),
        'older_own_paths_bound_transitively': 875,
        'older_plus_new_own_paths_bound_transitively': 886,
        'guard_detail': detail,
        'FULL_final_model_readback_ALL10_payloads_including_generated_metadata_attested': True,
        'FULL_manifest_model_readback_then_SEPARATE_readonly_verify_required': True,
        'no_mathematical_execution_or_old_author_source_replay': True,
        'no_old_shared_Git_cache_mutation_spawn_charge_contact_bypass': True,
        'no_SQ15_peer_material_access': True,
        'weekly_telemetry': read_json(PREFIX + 'sources-v1.json')['weekly_telemetry'],
        'payloads': [record(PREFIX + suffix) for suffix in PAYLOAD_SUFFIXES],
    }
    write_new(FREEZE, manifest)
    print(json.dumps({'freeze': 'PASS', 'at_utc': manifest['frozen_at_utc'],
                      'main': manifest['payloads'][0], 'manifest': record(FREEZE)}))


def verify():
    meta = read_json(FREEZE)
    assert len(meta['payloads']) == 10
    for rec in meta['payloads']:
        check(rec)
    protected()
    labels()
    assert meta['guard_detail'] == read_json(BASELINE)['detail']
    print(json.dumps({'SEPARATE_readonly_verify': 'PASS', 'verified_at_utc': now(),
                      'ENTIRE_files': 11, **labels(), 'manifest': record(FREEZE),
                      'main': meta['payloads'][0], 'guard': meta['guard_detail']['necessary_guard_summary']}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['prepare', 'freeze', 'verify'])
    parser.add_argument('--attest-final-model-readback', action='store_true')
    args = parser.parse_args()
    if args.action == 'prepare':
        prepare()
    elif args.action == 'freeze':
        freeze(args.attest_final_model_readback)
    else:
        verify()
