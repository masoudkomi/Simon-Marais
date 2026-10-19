#!/usr/bin/env python3
"""AR19 review2 documentary byte/JSON/label checks only, no mathematics.

prepare creates only NEW baseline. After FULL final ALL4 model readbacks,
freeze creates manifest. FULL manifest model readback then a SEPARATE
verify invocation is mandatory. No old/author helper is imported/run;
no corresponding NEW root review1 inventory/content/hash is accessed.
"""
import argparse
import datetime as dt
import hashlib
import json
import re
from pathlib import Path

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PFX = 'problems/2020-B4/reviews/reasoning-realization-return-r19-review-2-'
BASE = PFX + 'baseline-v1.json'
MANIFEST = PFX + 'manifest-v1.json'
PAYLOADS = [PFX + 'initial-v1.md', PFX + 'sources-v1.json',
            PFX + 'admin-v1.py', BASE]
AUTHOR = 'problems/2020-B4/notes/reasoning-realization-return-r19-freeze-v1.json'
PARENT = 'problems/2025-B4/reviews/reasoning-global-return-r11-review-1-manifest-v1.json'
EXPECTED = {
    AUTHOR: (2637, 'a4967473504c2ff3a481487e84a5a07ae9305bf8da00b6594ef298185eed01d5'),
    PARENT: (2349, '437702e41264c07bf2f4ebdedfabc013054615d32b276eed5d698b5c31836123'),
    'problems/2020-B4/notes/reasoning-realization-return-r19-candidate-v1.md':
        (31284, '570203928d79da6c43ff1046775699c62029360e39ff1885a0057dd1bd570727')}
FORBIDDEN = [
    'problems/2020-B4/reviews/reasoning-realization-return-r19-review-1-',
    'problems/2025-B4/reviews/reasoning-global-return-r11-review-2-',
    'problems/2024-B4/reviews/coordinator-tensor-family-return-r13-']

def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()

def safe(path):
    assert isinstance(path, str) and not path.startswith('/')
    assert '..' not in Path(path).parts
    assert not any(path.startswith(p) for p in FORBIDDEN), path
    return ROOT / path

def fp(path):
    value = safe(path).read_bytes()
    return {'path': path, 'bytes': len(value), 'sha256': hashlib.sha256(value).hexdigest()}

def read(path):
    return json.loads(safe(path).read_text())

def check(row):
    got = fp(row['path'])
    assert got == {k: row[k] for k in ('path', 'bytes', 'sha256')}, row['path']
    return got

def summary(items):
    unique = {}
    for row in items:
        if row['path'] in unique:
            assert unique[row['path']] == row
        unique[row['path']] = row
    ordered = [unique[k] for k in sorted(unique)]
    value = json.dumps(ordered, sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(items), 'unique_paths': len(ordered),
            'canonical_deduplicated_sha256': hashlib.sha256(value).hexdigest()}

def labels():
    text = safe(PAYLOADS[0]).read_text()
    values = re.findall(r'^\| (AR19-\d\d) \|', text, re.M)
    assert values == ['AR19-%02d' % i for i in range(1, 49)]
    assert len(re.findall(r'^\| AR19R2-N\d+ \|', text, re.M)) == 10
    read(PAYLOADS[1])

def collect():
    for path, expected in EXPECTED.items():
        got = fp(path)
        assert (got['bytes'], got['sha256']) == expected, path
    author = read(AUTHOR)
    payloads = [check(r) for r in author['payload_records']]
    assert len(payloads) == 4 and author['whole_obligations'] == 48
    author_base_path = next(r['path'] for r in payloads if r['path'].endswith('-baseline-v1.json'))
    author_base = read(author_base_path)
    direct = [check(r) for r in author_base['direct_guard_records']]
    assert summary(direct) == author_base['direct_guard_summary']
    parent = read(PARENT)
    parent_payloads = [check(r) for r in parent['payload_records']]
    assert len(parent_payloads) == 5
    # Only exact declared current authorities and their accepted-body identity.
    # Historical review inventories stay transitively bound, not re-expanded.
    counts = []
    for row in author_base['immutable_authority_parent_summaries']:
        authority = read(row['authority']['path'])
        check(row['authority'])
        check(authority['accepted_copy'])
        counts.append({'authority': row['authority'],
            'historical_occurrences_bound': authority['record_occurrences_verified'],
            'historical_paths_bound': authority['unique_paths_verified']})
    all_rows = [fp(AUTHOR)] + payloads + direct + [fp(PARENT)] + parent_payloads
    return {'guard_summary': summary(all_rows),
        'author_ENTIRE5': fp(AUTHOR), 'author_payloads_verified': len(payloads),
        'author_direct_guard_summary_verified': summary(direct),
        'current_authorities_bound_not_historical_inventory_replayed': counts,
        'immediate_own_parent': fp(PARENT),
        'own_parent_payloads_verified': len(parent_payloads),
        'own_parent_historical_summary_bound_NOT_expanded': parent['guard_summary']}

def write_new(path, value):
    assert path.startswith(PFX)
    with safe(path).open('x') as out:
        json.dump(value, out, indent=2)
        out.write('\n')

def prepare():
    labels()
    bindings = collect()
    baseline = {'created_utc': now(), 'reviewer': '/root/review_2017_coarsening_r1',
        'WHOLE_obligations': 48, 'compact_integrity': bindings,
        'current_metadata_only_no_growing_history_copy': True,
        'whole_initial_blind': True, 'NEW_root_R19_review_access': False,
        'NEW_B_R11_review_access': False, 'findings_sealed_until_explicit_BOTH': True,
        'OLD_R18_review_and_A9_SQ15_construction_roles_disclosed': True,
        'independent_OLD_input_recertification': False,
        'NEW_AR19_construction_contribution': False,
        'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'independent_effective_setting_readback': None,
        'quota': {'usedPercent': 73, 'observed_utc': '2026-10-18 23:57:48 UTC',
            'windowDurationMins': 10080, 'resetsAt': 1792874445,
            'ordinaryUsageAllowed': True, 'TOTAL_ceiling': 90,
            'integration_reserve': True, 'automatic_later_window': False},
        'mathematical_program_CAS_scan_test_optimizer_old_source_author_replay': False,
        'old_shared_Git_cache_mutation': False,
        'FULL_final_ALL4_model_readback_then_manifest_then_SEPARATE_verify_required': True}
    write_new(BASE, baseline)
    print(json.dumps({'baseline': fp(BASE), 'guard_summary': bindings['guard_summary']}, indent=2))

def validate():
    labels()
    baseline = read(BASE)
    assert collect() == baseline['compact_integrity']
    return baseline

def freeze(confirmed):
    assert confirmed, 'FULL final ALL4 payload MODEL readbacks must come first'
    baseline = validate()
    manifest = {'frozen_utc': now(), 'reviewer': '/root/review_2017_coarsening_r1',
        'type': 'OTHER initially blind ENTIRE WHOLE2 AR19 initial',
        'WHOLE_obligations': 48, 'ENTIRE_files': len(PAYLOADS)+1,
        'payload_records': [fp(p) for p in PAYLOADS],
        'guard_summary': baseline['compact_integrity']['guard_summary'],
        'author': fp(AUTHOR), 'immediate_own_parent': fp(PARENT),
        'FULL_final_MODEL_ALL4_payload_readback_completed': True,
        'FULL_manifest_MODEL_readback_then_SEPARATE_readonly_verify_required': True,
        'NEW_root_R19_peer_access': False, 'NEW_B_R11_peer_access': False,
        'findings_sealed_until_explicit_BOTH': True,
        'mathematical_program_CAS_scan_test_old_replay': False,
        'Git_shared_old_cache_mutation': False}
    write_new(MANIFEST, manifest)
    print(json.dumps({'manifest': fp(MANIFEST), 'frozen_utc': manifest['frozen_utc'],
                      'ENTIRE_files': manifest['ENTIRE_files']}, indent=2))

def verify(expected):
    assert expected and fp(MANIFEST)['sha256'] == expected
    manifest = read(MANIFEST)
    for row in manifest['payload_records']:
        check(row)
    baseline = validate()
    assert manifest['guard_summary'] == baseline['compact_integrity']['guard_summary']
    print(json.dumps({'verified_utc': now(), 'result': 'PASS',
        'ENTIRE_files': 5, 'WHOLE_obligations': 48, 'manifest': fp(MANIFEST),
        'writes': 0, 'mathematical_computation': False,
        'NEW_root_R19_peer_access': False, 'NEW_B_R11_peer_access': False}, indent=2))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['prepare', 'freeze', 'verify'])
    parser.add_argument('--final-payload-readback-confirmed', action='store_true')
    parser.add_argument('--manifest-sha')
    args = parser.parse_args()
    if args.mode == 'prepare':
        prepare()
    elif args.mode == 'freeze':
        freeze(args.final_payload_readback_confirmed)
    else:
        verify(args.manifest_sha)
