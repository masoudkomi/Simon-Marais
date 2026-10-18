#!/usr/bin/env python3
"""NEW R9 whole-review documentary administration; no mathematical execution."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
P = 'problems/2024-B4/reviews/reasoning-cofactor-return-r9-review-2-'
A = 'problems/2024-B4/notes/reasoning-cofactor-return-r9-'
PARENT = 'problems/2020-B4/notes/reasoning-class-return-sq15-freeze-v1.1.json'
AUTH = ['structural', 'reasoning-cofactor-return-r6',
        'reasoning-cofactor-return-r7', 'reasoning-cofactor-return-r8']
PAYLOADS = ['report-v1.md', 'ledger-v1.md', 'issues-v1.md', 'sources-v1.md',
            'sources-v1.json', 'worklog-v1.md', 'admin-v1.py',
            'baseline-v1.json', 'input-validation-v1.json', 'metadata-v1.json']
EXPECTED = {
    A+'freeze-v1.json': (9271, 'baad7591162df50c28cc4d20794616d165d622ae8c6abc0bb9f699e255d2147d'),
    A+'candidate-v1.md': (20443, '740e85acc2103aa6ed72ac46ac3089b12cfb29962fc4e0593ccf9e8223af66bf'),
    PARENT: (4621, 'b84c394b1d1e7feb1b351e59bd2f91e4f08aaea232f0537083cf73be8f3a3e9e'),
}


def now():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    pp = Path(path)
    if pp.is_absolute() or '..' in pp.parts:
        raise ValueError('exact relative path required')
    if path.startswith('problems/2024-B4/reviews/reasoning-cofactor-return-r9-') and not path.startswith(P):
        raise ValueError('NEW corresponding peer material is embargoed')
    return (ROOT / pp).read_bytes()


def record(path):
    data = raw(path)
    out = {'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
    if path in EXPECTED and (out['bytes'], out['sha256']) != EXPECTED[path]:
        raise ValueError('assigned/parent identity mismatch: '+path)
    return out


def checked(item):
    if record(item['path']) != item:
        raise ValueError('immutable fingerprint mismatch: '+item['path'])
    return item


def readjson(path):
    return json.loads(raw(path))


def canonical(rows):
    data = json.dumps(rows, sort_keys=True, separators=(',', ':')).encode()
    return hashlib.sha256(data).hexdigest()


def summary(rows):
    unique = {}
    for item in rows:
        if item['path'] in unique and unique[item['path']] != item:
            raise ValueError('conflicting immutable record')
        unique[item['path']] = item
    guards = [unique[path] for path in sorted(unique)]
    return guards, {'occurrences': len(rows), 'unique_paths': len(guards),
                    'canonical_deduplicated_sha256': canonical(guards)}


def gather():
    author_path = A+'freeze-v1.json'
    author = readjson(author_path)
    record(author_path)
    if author['whole_obligations'] != 64 or len(author['payloads']) != 10:
        raise ValueError('ENTIRE11/whole64 author coverage mismatch')
    rows = [record(author_path)] + [checked(item) for item in author['payloads']]
    ab = readjson(A+'baseline-v1.json')
    declared = [checked(item) for item in ab['records']]
    _, ds = summary(declared)
    if ds != ab['summary'] or ds != author['guard_detail']['necessary_guard_summary']:
        raise ValueError('author compact baseline mismatch')
    rows.extend(declared)
    scopes = []
    for stem in AUTH:
        authority = 'problems/2024-B4/reviews/'+stem+'-acceptance.json'
        meta = readjson(authority)
        body = meta.get('accepted_copy', meta.get('accepted_proof'))
        checked(body)
        checked(meta['candidate'])
        if stem != 'structural' and not raw(body['path']).endswith(raw(meta['candidate']['path'])):
            raise ValueError('accepted immutable suffix mismatch')
        scopes.append({'authority': authority, 'body': body,
                       'candidate_bound': meta['candidate'],
                       'exact_suffix': stem != 'structural',
                       'structural_editorial_exception_acknowledged': stem == 'structural',
                       'historical_review_inventory_reexpanded': False})
    parent = readjson(PARENT)
    record(PARENT)
    if parent['ENTIRE_files'] != 16 or len(parent['payloads']) != 15:
        raise ValueError('own immediate parent ENTIRE16 mismatch')
    rows.append(record(PARENT))
    rows.extend(checked(item) for item in parent['payloads'])
    guards, ss = summary(rows)
    detail = {'author_ENTIRE_files': 11, 'author_payloads_verified': 10,
              'author_declared_compact_baseline': ds,
              'own_immediate_parent_ENTIRE_files': 16,
              'own_immediate_parent_payloads_verified': 15,
              'parent_necessary_guard_summary_bound_by_parent_identity': {
                  'occurrences': parent['necessary_guard_occurrences'],
                  'unique_paths': parent['necessary_guard_unique_paths'],
                  'canonical_sha256': parent['canonical_guard_sha256']},
              'accepted_scope_bindings': scopes,
              'historical_inventories_reexpanded_or_old_executable_replayed': False,
              'mathematical_instance_evaluated': False}
    return guards, ss, detail


def labels():
    expected = [f'O{i:02d}' for i in range(1, 65)]
    author = re.findall(r'^(O\d{2})\.', raw(A+'obligations-v1.md').decode(), re.M)
    ledger = re.findall(r'^\|(O\d{2})\|', raw(P+'ledger-v1.md').decode(), re.M)
    if author != expected or ledger != expected:
        raise ValueError('ALL64 exact separate ledger labels mismatch')
    return {'author_obligations': 64, 'reviewer_separate_dispositions': 64,
            'exact_unique_order': True, 'mathematics_proved_by_labels': False}


def write(suffix, obj):
    if suffix not in PAYLOADS+['manifest-v1.json']:
        raise ValueError('assigned NEW output only')
    with (ROOT / (P+suffix)).open('x', encoding='utf-8') as out:
        json.dump(obj, out, indent=2, ensure_ascii=False)
        out.write('\n')
    return record(P+suffix)


def prepare():
    guards, ss, detail = gather()
    ll = labels()
    write('baseline-v1.json', {'captured_at_utc': now(), 'status': 'documentary integrity only',
                              'summary': ss, 'detail': detail, 'guards': guards})
    write('input-validation-v1.json', {'validated_at_utc': now(), 'status': 'documentary PASS only',
                                      'assigned_author_ENTIRE11': True, 'own_parent_ENTIRE16': True,
                                      'current_accepted_bodies_authorities_bound': True,
                                      'labels': ll, 'guard_summary': ss,
                                      'old_author_source_reviewer_program_invoked': False})
    write('metadata-v1.json', {
        'created_at_utc': now(), 'status': 'one initially blind independent ENTIRE WHOLE review',
        'reviewer': '/root/review_2017_coarsening_r1', 'NEW_R9_constructor': False,
        'older_own_R6_R7_R8_roles_disclosed_not_independently_recertified': True,
        'whole_obligations': 64, 'payload_files': 10, 'ENTIRE_files': 11,
        'root_B_NEW_mathematical_review_inference_received': False,
        'corresponding_NEW_peer_finding_file_hash_metadata_accessed': False,
        'findings_embargoed_until_explicit_BOTH_entire_confirmation': True,
        'TWO_OTHER_whole_reviews_and_coordinator_reconciliation_required': True,
        'FULL_final_model_readback_ALL10_payloads_REQUIRED_before_freeze': True,
        'FULL_manifest_readback_then_SEPARATE_readonly_verify_REQUIRED': True,
        'requested_model': 'gpt-6.1-sol', 'requested_reasoning': 'max',
        'verified_effective_readback': None,
        'authorized_weekly_reset': 1792874445, 'last_direct_transition_TOTAL_percent': 51,
        'TOTAL_ceiling_percent': 90, 'integration_reserve': True, 'automatic_later_window': False,
        'mathematical_code_CAS_scan_test_optimizer_or_old_replay': False,
        'old_shared_Git_cache_write_spawn_charge_contact_bypass': False})
    print(json.dumps({'prepare': 'PASS', 'guards': ss, 'labels': ll}))


def protected():
    b = readjson(P+'baseline-v1.json')
    for item in b['guards']:
        checked(item)
    guards, ss, detail = gather()
    if (guards, ss, detail) != (b['guards'], b['summary'], b['detail']):
        raise ValueError('preservation baseline changed')
    labels()
    return b


def freeze(attest):
    if not attest:
        raise ValueError('FULL final ALL10 payload model readback required')
    b = protected()
    payloads = [record(P+suffix) for suffix in PAYLOADS]
    for item in payloads:
        if item['path'].endswith('.json'):
            readjson(item['path'])
    m = {'frozen_at_utc': now(), 'status': 'initially blind independent WHOLE review; not acceptance',
         'reviewer': '/root/review_2017_coarsening_r1', 'NEW_R9_nonconstructor': True,
         'whole_obligations': 64, 'separate_dispositions': 64, 'payload_files': 10, 'ENTIRE_files': 11,
         'author': record(A+'freeze-v1.json'), 'immediate_own_parent': record(PARENT),
         'guard_summary': b['summary'], 'compact_baseline': record(P+'baseline-v1.json'),
         'FULL_final_model_readback_ALL10_payloads_completed': True,
         'FULL_manifest_readback_then_SEPARATE_readonly_verify_REQUIRED': True,
         'corresponding_NEW_peer_finding_file_hash_metadata_access_before_freeze': False,
         'findings_embargoed_until_explicit_BOTH_entire_confirmation': True,
         'mathematical_execution_or_old_author_source_replay': False, 'payloads': payloads}
    print(json.dumps({'freeze': write('manifest-v1.json', m), 'at_utc': m['frozen_at_utc']}))


def verify():
    m = readjson(P+'manifest-v1.json')
    if [x['path'] for x in m['payloads']] != [P+s for s in PAYLOADS]:
        raise ValueError('ENTIRE payload coverage mismatch')
    for item in m['payloads']:
        checked(item)
    b = protected()
    if m['guard_summary'] != b['summary'] or m['whole_obligations'] != 64:
        raise ValueError('manifest coverage/summary mismatch')
    print(json.dumps({'SEPARATE_readonly_verify': 'PASS', 'verified_at_utc': now(),
                      'ENTIRE_files': 11, 'ALL_obligations': 64, 'guards': b['summary'],
                      'report': record(P+'report-v1.md'), 'manifest': record(P+'manifest-v1.json')}, indent=2))


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
