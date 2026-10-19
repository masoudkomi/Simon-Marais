#!/usr/bin/env python3
"""R11 review1 documentary integrity only; no mathematical computation.

prepare writes compact baseline/metadata exclusively in this NEW prefix.
After FULL final ALL5 payload model readback, freeze writes the manifest.
After FULL manifest model readback, verify is a separate read-only call.
The author helper is never executed, and its unrelated R13 parent is never
followed. No corresponding NEW review2 path is enumerated/opened/hashed.
"""
import argparse
import datetime as dt
import hashlib
import json
import re
from pathlib import Path

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PFX = 'problems/2025-B4/reviews/reasoning-global-return-r11-review-1-'
BASE = PFX + 'baseline-v1.json'
META = PFX + 'metadata-v1.json'
MANIFEST = PFX + 'manifest-v1.json'
PAYLOADS = [PFX + 'initial-v1.md', PFX + 'sources-v1.json',
            PFX + 'admin-v1.py', BASE, META]
AUTHOR = 'problems/2025-B4/notes/reasoning-global-return-r11-freeze-v1.json'
PARENT = 'problems/2019-B4/notes/reasoning-full-law-return-r15-freeze-v1.json'
AUTHORITIES = [
    'problems/2025-B4/reviews/reasoning-compatible-return-r10-acceptance.json',
    'problems/2025-B4/reviews/reasoning-diagonal-return-r8-acceptance.json']
DIRECT = [
    'AGENTS.md', 'problems/2025-B4/statement.md',
    'problems/2025-B4/proofs/reviewed-reasoning-compatible-return-r10-v1.1.md',
    'problems/2025-B4/reviews/reasoning-compatible-return-r10-acceptance.md',
    AUTHORITIES[0],
    'problems/2025-B4/proofs/reviewed-reasoning-diagonal-return-r8-v1.1.md',
    'problems/2025-B4/reviews/reasoning-diagonal-return-r8-acceptance.md',
    AUTHORITIES[1]]
EXPECTED = {
    AUTHOR: (2639, '1e6953c80d9d17efbb2b94c5ae6af3a0b9880119d46c1e0fde7dc4c28a266771'),
    PARENT: (2055, '9d65c7cf66efa14925fc15ef081aec846157db3c853ea0744b09afd165e1cbfb'),
    'problems/2025-B4/notes/reasoning-global-return-r11-candidate-v1.md':
        (25923, 'aa1e1242621a9bd99b42bb306827e41e8ee6309b963ce2c63c8e503cd325bbe3')}
FORBIDDEN = [
    'problems/2025-B4/reviews/reasoning-global-return-r11-review-2-',
    'problems/2024-B4/reviews/coordinator-tensor-family-return-r13-',
    'problems/2017-B4/notes/coordinator-tensor-',
    'problems/2017-B4/reviews/coordinator-tensor-']

def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()

def safe(path):
    assert isinstance(path, str) and not path.startswith('/')
    assert '..' not in Path(path).parts
    assert not any(path.startswith(p) for p in FORBIDDEN), path
    return ROOT / path

def fp(path):
    b = safe(path).read_bytes()
    return {'path': path, 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}

def read(path):
    return json.loads(safe(path).read_text())

def check(row):
    got = fp(row['path'])
    assert got == {k: row[k] for k in ('path', 'bytes', 'sha256')}, row['path']
    return got

def rows(value):
    if isinstance(value, dict):
        if all(k in value for k in ('path', 'bytes', 'sha256')):
            yield {k: value[k] for k in ('path', 'bytes', 'sha256')}
        for item in value.values():
            yield from rows(item)
    elif isinstance(value, list):
        for item in value:
            yield from rows(item)

def summary(items):
    unique = {}
    for item in items:
        if item['path'] in unique:
            assert unique[item['path']] == item
        unique[item['path']] = item
    ordered = [unique[k] for k in sorted(unique)]
    raw = json.dumps(ordered, sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(items), 'unique_paths': len(ordered),
            'canonical_deduplicated_sha256': hashlib.sha256(raw).hexdigest()}

def guards():
    for path, expected in EXPECTED.items():
        got = fp(path)
        assert (got['bytes'], got['sha256']) == expected, path
    author = read(AUTHOR)
    author_rows = [check(r) for r in author['payloads']]
    assert len(author_rows) == 4 and author['whole_obligations'] == 32
    parent = read(PARENT)
    parent_rows = [check(r) for r in parent['payload_records']]
    assert len(parent_rows) == 5
    direct = [fp(p) for p in DIRECT]
    declared_counts = []
    declared = []
    for path in AUTHORITIES:
        value = list(rows(read(path)))
        declared.extend(check(r) for r in value)
        declared_counts.append({'path': path, 'occurrences': len(value)})
    items = [fp(AUTHOR)] + author_rows + direct + [fp(PARENT)] + parent_rows + declared
    return items, direct, declared_counts, {
        'author_ENTIRE_binding': fp(AUTHOR),
        'author_payloads_verified': len(author_rows),
        'author_declared_historical_summary_bound_NOT_expanded':
            author['effective_fresh_guard_summary'],
        'author_external_R13_parent_followed_opened_hashed': False,
        'immediate_own_parent': fp(PARENT),
        'own_parent_payloads_verified': len(parent_rows),
        'own_parent_historical_summary_bound_NOT_expanded': parent['effective_guard_summary']}

def write_new(path, value):
    assert path.startswith(PFX)
    with safe(path).open('x') as f:
        json.dump(value, f, indent=2)
        f.write('\n')

def validate_labels():
    text = safe(PAYLOADS[0]).read_text()
    labels = re.findall(r'^\| (O\d\d) \|', text, re.M)
    assert labels == ['O%02d' % i for i in range(1, 33)]
    assert len(re.findall(r'^\| R11R1-N\d \|', text, re.M)) == 9

def prepare():
    validate_labels()
    items, direct, counts, bindings = guards()
    baseline = {'created_utc': now(), 'reviewer': '/root/review_2017_coarsening_r1',
        'necessary_direct_records': direct, 'current_authority_declared_counts': counts,
        'compact_bindings': bindings, 'effective_guard_summary': summary(items),
        'no_growing_historical_inventory_recopy': True,
        'guard_scope': 'Exact author ENTIRE5, current operative authorities and own immediate ENTIRE6 parent; no author helper or external R13 parent replay'}
    write_new(BASE, baseline)
    write_new(META, {
        'created_utc': now(), 'WHOLE_obligations': 32, 'claims': ['GR0', 'GR1', 'GR2', 'GR3'],
        'whole_initial_blind': True, 'corresponding_NEW_review2_access': False,
        'root_NEW_proof_inference_supplied_to_reviewer': False,
        'OLD_R10_constructor_role_disclosed': True,
        'not_independent_recertification_of_OLD_R10': True,
        'NEW_R11_construction_contribution': False,
        'mathematical_work': 'hand reconstruction only',
        'mathematical_program_CAS_scan_test_optimizer_old_source_author_replay': False,
        'author_parent_R13_followed_opened_hashed': False,
        'old_shared_Git_cache_mutation': False,
        'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'independent_effective_setting_readback': None,
        'quota': {'usedPercent': 72, 'observed_utc': '2026-10-18 23:51:09 UTC',
            'windowDurationMins': 10080, 'resetsAt': 1792874445,
            'ordinaryUsageAllowed': True, 'TOTAL_ceiling': 90,
            'integration_reserve': True, 'automatic_later_window': False},
        'findings_EMBARGOED_until_explicit_BOTH': True,
        'separate_verification_required_after_FULL_manifest_model_readback': True})
    print(json.dumps({'baseline': fp(BASE), 'metadata': fp(META),
                      'guard_summary': baseline['effective_guard_summary']}, indent=2))

def validate():
    validate_labels()
    items, direct, counts, bindings = guards()
    base = read(BASE)
    assert base['necessary_direct_records'] == direct
    assert base['current_authority_declared_counts'] == counts
    assert base['compact_bindings'] == bindings
    assert base['effective_guard_summary'] == summary(items)
    return base

def freeze(confirmed):
    assert confirmed, 'FULL final ALL5 payload model readback required first'
    base = validate()
    manifest = {'frozen_utc': now(), 'reviewer': '/root/review_2017_coarsening_r1',
        'type': 'OTHER initially blind ENTIRE WHOLE1 initial audit',
        'WHOLE_obligations': 32, 'ENTIRE_files': len(PAYLOADS)+1,
        'payload_records': [fp(p) for p in PAYLOADS],
        'guard_summary': base['effective_guard_summary'],
        'author': fp(AUTHOR), 'immediate_own_parent': fp(PARENT),
        'FULL_final_MODEL_ALL5_payload_readback_completed': True,
        'FULL_manifest_MODEL_readback_then_SEPARATE_readonly_verify_required': True,
        'corresponding_NEW_review2_access': False,
        'findings_EMBARGOED_until_explicit_BOTH': True,
        'OLD_R10_constructor_disclosed_not_self_recertified': True,
        'author_external_R13_parent_followed_opened_hashed': False,
        'mathematical_program_CAS_scan_test_or_replay': False,
        'old_shared_Git_cache_mutation': False}
    write_new(MANIFEST, manifest)
    print(json.dumps({'manifest': fp(MANIFEST), 'frozen_utc': manifest['frozen_utc'],
                      'ENTIRE_files': manifest['ENTIRE_files']}, indent=2))

def verify(expected):
    assert expected and fp(MANIFEST)['sha256'] == expected
    manifest = read(MANIFEST)
    for row in manifest['payload_records']:
        check(row)
    base = validate()
    assert manifest['guard_summary'] == base['effective_guard_summary']
    print(json.dumps({'verified_utc': now(), 'result': 'PASS',
        'ENTIRE_files': len(manifest['payload_records'])+1,
        'WHOLE_obligations': 32, 'manifest': fp(MANIFEST),
        'writes': 0, 'mathematical_computation': False,
        'corresponding_NEW_review2_access': False}, indent=2))

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
