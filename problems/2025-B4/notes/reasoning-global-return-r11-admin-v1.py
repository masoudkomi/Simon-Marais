#!/usr/bin/env python3
"""R11 documentary integrity only. No mathematical computation or source replay.

Usage:
  python3 THIS prepare
  # FULL final model readback of candidate, sources, this file and baseline.
  python3 THIS freeze --final-payload-readback-confirmed
  # FULL manifest model readback.
  python3 THIS verify --manifest-sha EXACT_PRINTED_SHA

Only NEW R11 baseline/freeze files are created, using exclusive creation.
Verify is read-only. It does not enumerate any peer prefix. Old metadata
is bound compactly and checks only explicit necessary fingerprints;
historical mutable maps are observations, never live immutable guards.
"""
import argparse
import datetime as dt
import hashlib
import json
import re
from pathlib import Path

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PFX = 'problems/2025-B4/notes/reasoning-global-return-r11-'
BASELINE = PFX + 'baseline-v1.json'
MANIFEST = PFX + 'freeze-v1.json'
PAYLOADS = [PFX + 'candidate-v1.md', PFX + 'sources-v1.json',
            PFX + 'admin-v1.py', BASELINE]
PARENT = ('problems/2024-B4/reviews/'
          'coordinator-tensor-family-return-r13-review-1-manifest-v1.json')
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
    AUTHORITIES[1],
    'problems/2025-B4/notes/reasoning-diagonal-return-r8-sources-v1.md',
    'problems/2025-B4/notes/reasoning-diagonal-return-r5-sources-v1.md']
FORBIDDEN = 'problems/2021-B4/reviews/reasoning-negative-return-r23-'

def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()

def safe(path):
    assert isinstance(path, str) and not path.startswith('/')
    assert '..' not in Path(path).parts
    assert not path.startswith(FORBIDDEN), 'NEW R23 peer material forbidden'
    return ROOT / path

def fp(path):
    data = safe(path).read_bytes()
    return {'path': path, 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}

def read(path):
    return json.loads(safe(path).read_text())

def check(row):
    actual = fp(row['path'])
    assert actual == {k: row[k] for k in ('path', 'bytes', 'sha256')}, row['path']
    return actual

def rows(value):
    if isinstance(value, dict):
        if all(k in value for k in ('path', 'bytes', 'sha256')):
            yield {k: value[k] for k in ('path', 'bytes', 'sha256')}
        for child in value.values():
            yield from rows(child)
    elif isinstance(value, list):
        for child in value:
            yield from rows(child)

def summary(occurrences):
    unique = {}
    for item in occurrences:
        if item['path'] in unique:
            assert unique[item['path']] == item
        unique[item['path']] = item
    ordered = [unique[k] for k in sorted(unique)]
    raw = json.dumps(ordered, sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(occurrences), 'unique_paths': len(ordered),
            'canonical_deduplicated_sha256': hashlib.sha256(raw).hexdigest()}

def write_new(path, value):
    assert path.startswith(PFX)
    with safe(path).open('x') as stream:
        json.dump(value, stream, indent=2)
        stream.write('\n')

def collect_guards():
    occurrences = [fp(p) for p in DIRECT]
    authority_counts = []
    for path in AUTHORITIES:
        declared = list(rows(read(path)))
        for row in declared:
            occurrences.append(check(row))
        authority_counts.append({'path': path, 'declared_occurrences': len(declared)})
    parent_fp = fp(PARENT)
    parent = read(PARENT)
    parent_payloads = [check(row) for row in parent['payloads']]
    occurrences.extend([parent_fp] + parent_payloads)
    parent_baseline_path = next(row['path'] for row in parent_payloads
                               if row['path'].endswith('-baseline-v1.json'))
    parent_baseline = read(parent_baseline_path)
    parent_direct = [check(row) for row in parent_baseline['necessary_direct_records']]
    occurrences.extend(parent_direct)
    ancestor = parent_baseline['compact_parent_binding']['immediate_own_parent']
    occurrences.append(check(ancestor))
    # These are the old OWN constructor payloads, never NEW R23 review metadata.
    old_constructor = read(ancestor['path'])
    old_payloads = old_constructor.get('payloads', old_constructor.get('artifacts', []))
    assert isinstance(old_payloads, list) and old_payloads
    old_checked = [check(row) for row in old_payloads]
    occurrences.extend(old_checked)
    bindings = {
        'immediate_parent': parent_fp,
        'all_parent_payloads_verified': len(parent_payloads),
        'parent_direct_immutable_records_verified': len(parent_direct),
        'old_own_constructor_ancestor_verified': ancestor,
        'old_own_constructor_payloads_verified': len(old_checked),
        'parent_historical_summary_bound_NOT_reexpanded':
            parent['effective_fresh_guard_summary'],
        'older_history_is_metadata_binding_not_new_mathematical_premise': True}
    return occurrences, authority_counts, bindings

def prepare():
    assert not safe(BASELINE).exists() and not safe(MANIFEST).exists()
    occurrences, authority_counts, bindings = collect_guards()
    mutable = [fp('problems/2025-B4/research.md'), fp('problems/2025-B4/references.md')]
    record = {
        'created_UTC': now(), 'status': 'candidate proof - unverified',
        'constructor': '/root/review_2021_reasoning_j15_r2',
        'whole_obligations': 32, 'claims': ['GR0', 'GR1', 'GR2', 'GR3'],
        'necessary_direct_records': [fp(p) for p in DIRECT],
        'current_authority_declared_occurrences_verified': authority_counts,
        'compact_parent_binding': bindings,
        'effective_fresh_guard_summary': summary(occurrences),
        'guard_reconstruction': 'collect_guards() verifies declared records from exact bound current authorities and immediate-parent metadata; no growing historical path inventory is recopied',
        'mutable_current_observations_NOT_live_immutable_guards': mutable,
        'root_supplied_NEW_proof_inference': False,
        'NEW_R23_peer_material_accessed': False,
        'A_excluded_from_two_OTHER_initially_blind_WHOLE_audits': True,
        'source_import_boundary':
            'GR1 has explicit center0 height proof with published classical AI; '
            'GR2 imports published signed HB- and no fresh complete matrix proof is claimed',
        'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'independent_effective_setting_readback': None,
        'last_direct_quota': {'usedPercent': 71, 'observed_UTC': '2026-10-18 23:40:10 UTC',
            'windowDurationMins': 10080, 'resetsAt': 1792874445,
            'ordinaryUsageAllowed': True, 'TOTAL_ceiling': 90,
            'integration_reserve': True, 'automatic_later_window': False},
        'administration_only_no_math_code_scan_CAS_test_or_replay': True,
        'writes_only_NEW_R11_prefix': True}
    write_new(BASELINE, record)
    print(json.dumps({'baseline': fp(BASELINE), 'guards': summary(occurrences)}, indent=2))

def validate_baseline():
    value = read(BASELINE)
    for row in value['necessary_direct_records']:
        check(row)
    check(value['compact_parent_binding']['immediate_parent'])
    occurrences, authority_counts, bindings = collect_guards()
    assert authority_counts == value['current_authority_declared_occurrences_verified']
    assert bindings == value['compact_parent_binding']
    assert summary(occurrences) == value['effective_fresh_guard_summary']
    labels = re.findall(r'^\| (O\d\d) \|', safe(PAYLOADS[0]).read_text(), re.M)
    assert labels == ['O%02d' % i for i in range(1, 33)]
    return value

def freeze(confirmed):
    assert confirmed, 'FULL final ALL4 payload model readback must precede freeze'
    assert not safe(MANIFEST).exists()
    baseline = validate_baseline()
    manifest = {
        'frozen_UTC': now(), 'status': 'candidate proof - unverified',
        'constructor': '/root/review_2021_reasoning_j15_r2',
        'whole_obligations': 32, 'claims': ['GR0', 'GR1', 'GR2', 'GR3'],
        'payload_count': len(PAYLOADS), 'ENTIRE_files': len(PAYLOADS)+1,
        'payloads': [fp(p) for p in PAYLOADS],
        'effective_fresh_guard_summary': baseline['effective_fresh_guard_summary'],
        'compact_parent_historical_summary_bound': baseline['compact_parent_binding']
            ['parent_historical_summary_bound_NOT_reexpanded'],
        'FULL_final_ALL4_payload_model_readback_completed': True,
        'FULL_manifest_model_readback_then_SEPARATE_readonly_verify_REQUIRED': True,
        'root_supplied_NEW_proof_inference': False,
        'NEW_R23_peer_finding_file_inventory_hash_metadata_accessed': False,
        'two_OTHER_initially_blind_WHOLE_audits_required': True,
        'constructor_excluded_from_independent_audit_count': True,
        'GR2_published_HB_minus_import_not_external_full_proof_recertification': True,
        'remaining_invariant_class_sector': 'center -1, exact depth 2, both ordinary signs',
        'annual_solution_or_priority_claim': False,
        'requested': baseline['requested'],
        'independent_effective_setting_readback': None,
        'quota': baseline['last_direct_quota'],
        'mathematical_code_CAS_scan_test_optimizer_source_author_old_replay': False,
        'Git_shared_old_cache_mutation': False}
    write_new(MANIFEST, manifest)
    print(json.dumps({'manifest': fp(MANIFEST), 'frozen_UTC': manifest['frozen_UTC'],
                      'ENTIRE_files': manifest['ENTIRE_files'],
                      'whole_obligations': manifest['whole_obligations']}, indent=2))

def verify(expected):
    assert expected and fp(MANIFEST)['sha256'] == expected
    manifest = read(MANIFEST)
    for row in manifest['payloads']:
        check(row)
    baseline = validate_baseline()
    assert manifest['effective_fresh_guard_summary'] == baseline['effective_fresh_guard_summary']
    print(json.dumps({'verified_UTC': now(), 'result': 'PASS',
        'manifest': fp(MANIFEST), 'ENTIRE_files': len(manifest['payloads'])+1,
        'whole_obligations': 32, 'guards': baseline['effective_fresh_guard_summary'],
        'writes': 0, 'mathematical_work': False,
        'NEW_R23_peer_access': False}, indent=2))

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
