#!/usr/bin/env python3
"""R23 NEW review documentary checks only; no mathematical computation."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
P = 'problems/2021-B4/reviews/reasoning-negative-return-r23-review-2-'
A = 'problems/2021-B4/notes/reasoning-negative-return-r23-'
BASE = P + 'baseline-v1.json'
META = P + 'metadata-v1.json'
MANIFEST = P + 'manifest-v1.json'
PAYLOADS = [P + s for s in ('initial-v1.md', 'sources-v1.json',
                            'integrity-v1.py', 'baseline-v1.json', 'metadata-v1.json')]
PARENT = 'problems/2020-B4/reviews/reasoning-actual-return-r18-review-2-manifest-v1.json'
AUTHORITIES = [f'problems/2021-B4/reviews/reasoning-center-return-r{i}-acceptance'
               for i in (18, 21, 22)]
EXPECTED = {
    A + 'candidate-v1.md': (19525, '86c1774de0e58949606f287b22c2b22d3932d4ed8c8f06c457dab547b186941c'),
    A + 'freeze-v1.json': (3187, '4edff0c97b5d7a180cba0ae4a9975470d35f8542ccb6f841201855f7b2cd054a'),
    PARENT: (2658, '70923e5385fa3fac0e26055f6aa5207dfd96ed6e74076cfbc08982795a05eab4'),
    'AGENTS.md': (4707, '28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff')}


def now():
    return datetime.now(timezone.utc).isoformat()


def safe(path):
    p = Path(path)
    assert not p.is_absolute() and '..' not in p.parts
    peer_prefix = 'problems/2021-B4/reviews/reasoning-negative-return-r23-review-'
    assert not path.startswith(peer_prefix) or path.startswith(P)
    if path.startswith('problems/2017-B4/'):
        assert 'r13' not in p.name.lower() and 'tensor' not in p.name.lower()
    result = (ROOT / p).resolve()
    assert result.is_relative_to(ROOT)
    return result


def digest(b):
    return hashlib.sha256(b).hexdigest()


def record(path):
    b = safe(path).read_bytes()
    r = {'path': path, 'bytes': len(b), 'sha256': digest(b)}
    if path in EXPECTED:
        assert (r['bytes'], r['sha256']) == EXPECTED[path], path
    return r


def check(r):
    assert record(r['path']) == r, r['path']


def read(path):
    return json.loads(safe(path).read_text())


def put(path, obj):
    assert path.startswith(P)
    with safe(path).open('x') as f:
        json.dump(obj, f, indent=2)
        f.write('\n')


def summary(records):
    distinct = {}
    for r in records:
        assert r['path'] not in distinct or distinct[r['path']] == r
        distinct[r['path']] = r
    b = json.dumps([distinct[k] for k in sorted(distinct)],
                   sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(records), 'unique_paths': len(distinct),
            'canonical_deduplicated_sha256': digest(b)}


def bindings():
    author = read(A + 'freeze-v1.json')
    assert author['ENTIRE_files'] == 9 and author['whole_obligations'] == 48
    author_records = [record(A + 'freeze-v1.json')] + author['payloads']
    for r in author_records:
        check(r)
    direct = [record('AGENTS.md'), record('problems/2021-B4/statement.md')]
    authorities, declarations = [], []
    for authority in AUTHORITIES:
        value = read(authority + '.json')
        assert value['status'] == 'proved, independently reviewed scoped partial result'
        assert value['whole_initials_blind'] is True
        assert value['unresolved_substantive_issues'] == 0
        body = value['accepted_copy']
        direct += [record(body['path']), record(authority + '.md'), record(authority + '.json')]
        recs = [value['candidate'], body] + value['verification_metadata']
        for r in recs:
            check(r)
        assert safe(body['path']).read_bytes().endswith(safe(value['candidate']['path']).read_bytes())
        declarations += recs
        authorities.append({'authority': record(authority + '.json'),
                            'declared_fingerprint_summary': summary(recs),
                            'accepted_copy_exact_candidate_suffix': True})
    parent = read(PARENT)
    assert parent['ENTIRE_files'] == 8 and parent['whole_obligations'] == 64
    parent_records = [record(PARENT)] + parent['payload_records']
    for r in parent_records:
        check(r)
    assert parent['effective_guard_summary'] == {
        'occurrences': 101, 'unique_paths': 96,
        'canonical_deduplicated_sha256':
        '2f22a85f20dfa487324204b2972b9f5e9ad73de5def2112280976650c137ee84'}
    return {
        'author_freeze': record(A + 'freeze-v1.json'),
        'author_ENTIRE9_summary': summary(author_records),
        'direct_current_input_records': direct,
        'accepted_authority_bindings': authorities,
        'own_immediate_parent': record(PARENT),
        'own_ENTIRE8_parent_summary': summary(parent_records),
        'own_parent_prior_guard_summary_bound_only': parent['effective_guard_summary'],
        'effective_guard_summary': summary(author_records + direct + declarations + parent_records),
        'old_historical_inventory_not_recursively_copied_or_executed': True}


def labels():
    expected = [f'{i:02}' for i in range(1, 49)]
    own_ids = re.findall(r'^\|R23-O(\d\d)\|', safe(P + 'initial-v1.md').read_text(), re.M)
    author_ids = re.findall(r'^\|R23-O(\d\d)\|', safe(A + 'obligations-v1.md').read_text(), re.M)
    assert own_ids == expected and author_ids == expected
    s = read(P + 'sources-v1.json')
    assert s['whole_obligations'] == 48 and s['closed_scope_notes'] == 10
    assert s['substantive_defects_required_repairs'] == 0
    return {'literal_author_and_review_obligations': 48,
            'closed_scope_notes': 10, 'mathematical_truth_checked_by_code': False}


def baseline():
    b = read(BASE)
    assert b['binding'] == bindings() and b['literal_checks'] == labels()
    return b


mode = sys.argv[1]
if mode == 'prepare':
    assert not safe(MANIFEST).exists()
    binding = bindings()
    put(BASE, {'prepared_utc': now(), 'binding': binding, 'literal_checks': labels(),
               'NO_NEW_corresponding_peer_findings_files_inventory_hash_metadata_access': True})
    put(META, {
        'reviewer': '/root/review_2017_coarsening_r1',
        'role': 'OTHER initially blind ENTIRE WHOLE2',
        'NEW_constructor': '/root/review_2021_reasoning_j15_r2',
        'reviewer_NEW_construction_contribution': False,
        'OLD_R17_authorship_R21_R22_review_roles_not_self_recertification': True,
        'whole_obligations': 48, 'ENTIRE_files': 6,
        'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'verified_effective_setting_readback': None,
        'FULL_final_MODEL_ALL5_payloads_then_manifest_readbacks_required': True,
        'SEPARATE_readonly_verify_after_manifest_MODEL_readback_required': True,
        'NO_NEW_corresponding_peer_findings_files_inventory_hash_metadata_access': True,
        'findings_EMBARGO_until_explicit_BOTH_ENTIRE': True,
        'all_mathematics_hand_reconstructed': True,
        'documentary_code_not_mathematical_program': True,
        'no_mathCAS_scan_test_source_author_old_replay': True,
        'old_shared_Git_cache_bytes_changed': False,
        'no_native_browser_fee_contact_bypass_spawn_pending_child_or_approval': True,
        'author': binding['author_freeze'], 'own_parent': record(PARENT),
        'guard_summary': binding['effective_guard_summary'],
        'direct_weekly_used_percent': 70, 'direct_at_utc': '2026-10-18 23:20:14 UTC',
        'ordinaryUsageAllowed': True, 'legacy_by_limit_agree': True,
        'authorised_weekly_reset': 1792874445, 'hard_TOTAL_ceiling': 90,
        'integration_reserve': True, 'automatic_later_weekly_window': False,
        'deliberate_interruption_recovered_SAME_audit_no_pending_operation': True})
    print(json.dumps({'prepared_utc': now(), 'guard_summary': binding['effective_guard_summary']}))
elif mode == 'freeze':
    b = baseline()
    put(MANIFEST, {
        'frozen_utc': now(), 'reviewer': '/root/review_2017_coarsening_r1',
        'role': 'OTHER initially blind ENTIRE WHOLE2',
        'ENTIRE_files': 6, 'whole_obligations': 48,
        'payload_records': [record(p) for p in PAYLOADS],
        'author': b['binding']['author_freeze'], 'own_parent': record(PARENT),
        'effective_guard_summary': b['binding']['effective_guard_summary'],
        'FULL_final_MODEL_ALL5_payload_readback_completed': True,
        'FULL_manifest_MODEL_readback_then_SEPARATE_readonly_verify_required': True,
        'NO_NEW_corresponding_peer_findings_files_inventory_hash_metadata_access': True,
        'findings_EMBARGO_until_explicit_BOTH_ENTIRE': True,
        'mathematical_program': False, 'old_shared_Git_cache_bytes_changed': False})
    print(json.dumps({'manifest': record(MANIFEST), 'ENTIRE_files': 6}))
elif mode == 'verify':
    b = baseline()
    m = read(MANIFEST)
    assert m['ENTIRE_files'] == 6 and m['whole_obligations'] == 48
    assert [r['path'] for r in m['payload_records']] == PAYLOADS
    for r in m['payload_records']:
        check(r)
    assert m['author'] == b['binding']['author_freeze']
    assert m['own_parent'] == record(PARENT)
    assert m['effective_guard_summary'] == b['binding']['effective_guard_summary']
    print(json.dumps({'separate_readonly_verified_utc': now(), 'PASS': True,
                      'ENTIRE_files': 6, 'whole_obligations': 48,
                      'initial': record(P + 'initial-v1.md'), 'manifest': record(MANIFEST)}))
else:
    raise SystemExit('usage: prepare | freeze | verify')
