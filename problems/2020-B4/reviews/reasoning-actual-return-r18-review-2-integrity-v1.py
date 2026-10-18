#!/usr/bin/env python3
"""NEW R18 review documentary integrity, never mathematical verification."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
P = 'problems/2020-B4/reviews/reasoning-actual-return-r18-review-2-'
A = 'problems/2020-B4/notes/reasoning-actual-return-r18-'
BASE = P + 'baseline-v1.json'
META = P + 'metadata-v1.json'
MANIFEST = P + 'manifest-v1.json'
PAYLOADS = [P + s for s in (
    'initial-v1.md', 'ledger-v1.md', 'research-v1.md', 'sources-v1.json',
    'integrity-v1.py', 'baseline-v1.json', 'metadata-v1.json')]
PARENT = 'problems/2017-B4/notes/reasoning-lower-return-r14-freeze-v1.json'
SPECS = [
    ('problems/2020-B4/proofs/reviewed-reasoning-return-r8-v1.1.md',
     'problems/2020-B4/reviews/reasoning-return-r8-acceptance'),
    ('problems/2020-B4/proofs/reviewed-reasoning-arithmetic-return-r14-v1.2.md',
     'problems/2020-B4/reviews/reasoning-arithmetic-return-r14-repair-v1.1-acceptance'),
    ('problems/2020-B4/proofs/reviewed-reasoning-class-return-sq15-v1.1.md',
     'problems/2020-B4/reviews/reasoning-class-return-sq15-acceptance'),
    ('problems/2020-B4/proofs/reviewed-reasoning-class-return-sq16-v1.1.md',
     'problems/2020-B4/reviews/reasoning-class-return-sq16-acceptance'),
    ('problems/2020-B4/proofs/reviewed-reasoning-class-return-sq17-v1.1.md',
     'problems/2020-B4/reviews/reasoning-class-return-sq17-acceptance')]
EXPECTED = {
    A + 'candidate-v1.md': (36654, 'ec8f52badb1c22bdb846f1804be9cb1604171aa683c919df61c76d3b636528e9'),
    A + 'freeze-v1.json': (2747, '564db489529aa7030df95abbd6461fe82a5e1acf32d4499838f3472c6ae7e9be'),
    PARENT: (2710, '54f1548395da878a822fcf78dfd472819ae09d3a70b021d56b507710c4a9dbad'),
    'AGENTS.md': (4707, '28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff')}


def now():
    return datetime.now(timezone.utc).isoformat()


def safe(path):
    p = Path(path)
    assert not p.is_absolute() and '..' not in p.parts
    assert not path.startswith('problems/2020-B4/reviews/reasoning-actual-return-r18-review-1-')
    if path.startswith('problems/2017-B4/'):
        assert 'r13' not in p.name.lower() and 'tensor' not in p.name.lower()
    result = (ROOT / p).resolve()
    assert result.is_relative_to(ROOT)
    return result


def digest(data):
    return hashlib.sha256(data).hexdigest()


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
    unique = {}
    for r in records:
        assert r['path'] not in unique or unique[r['path']] == r
        unique[r['path']] = r
    b = json.dumps([unique[k] for k in sorted(unique)],
                   sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(records), 'unique_paths': len(unique),
            'canonical_deduplicated_sha256': digest(b)}


def input_binding():
    author = read(A + 'freeze-v1.json')
    assert author['ENTIRE_files'] == 5 and author['whole_obligations'] == 64
    author_records = [record(A + 'freeze-v1.json')] + author['payload_records']
    for r in author_records:
        check(r)
    direct = [record('AGENTS.md'), record('problems/2020-B4/statement.md')]
    authority_bindings, declared_records = [], []
    for body, authority in SPECS:
        direct += [record(body), record(authority + '.md'), record(authority + '.json')]
        value = read(authority + '.json')
        assert value['status'] == 'proved, independently reviewed scoped partial result'
        assert value['whole_initials_blind'] is True
        assert value['unresolved_substantive_issues'] == 0
        assert value['accepted_copy'] == record(body)
        declarations = [value['candidate'], value['accepted_copy']] + value['verification_metadata']
        for r in declarations:
            check(r)
        assert safe(body).read_bytes().endswith(safe(value['candidate']['path']).read_bytes())
        declared_records += declarations
        authority_bindings.append({
            'authority': record(authority + '.json'),
            'all_declared_fingerprints_summary': summary(declarations),
            'accepted_copy_exact_candidate_suffix': True,
            'whole_initials_blind': True, 'unresolved_substantive_issues': 0})
    parent = read(PARENT)
    assert parent['ENTIRE_files'] == 9 and parent['whole_obligations'] == 56
    parent_records = [record(PARENT)] + parent['payload_records']
    for r in parent_records:
        check(r)
    assert parent['effective_guard_summary'] == {
        'occurrences': 44, 'unique_paths': 42,
        'canonical_deduplicated_sha256':
        '35e3bb498318bb8bf1dfcad21166e82d9e318177ca464d4468e4de43faed8650'}
    return {
        'author_freeze': record(A + 'freeze-v1.json'),
        'author_ENTIRE5_summary': summary(author_records),
        'direct_current_input_records': direct,
        'current_accepted_authority_bindings': authority_bindings,
        'own_immediate_parent': record(PARENT),
        'own_ENTIRE9_parent_summary': summary(parent_records),
        'own_parent_inherited_guard_binding_only': parent['effective_guard_summary'],
        'effective_guard_summary': summary(author_records + direct + declared_records + parent_records),
        'historical_mutable_research_reference_context_not_theorem_guards': True,
        'historical_inventory_not_recursively_copied_or_old_code_replayed': True}


def labels():
    ids = re.findall(r'^\|AR18-(\d\d)\|', safe(P + 'ledger-v1.md').read_text(), re.M)
    assert ids == [f'{i:02}' for i in range(1, 65)]
    author_ids = re.findall(r'^\|AR18-(\d\d)\|', safe(A + 'candidate-v1.md').read_text(), re.M)
    assert author_ids == ids
    s = read(P + 'sources-v1.json')
    assert s['whole_obligations'] == 64 and s['substantive_defects_required_repairs'] == 0
    assert s['closed_scope_notes'] == 10
    return {'literal_whole_author_and_review_obligations': 64,
            'closed_scope_notes': 10, 'mathematical_truth_verified_by_code': False}


def baseline():
    b = read(BASE)
    assert b['binding'] == input_binding()
    assert b['literal_checks'] == labels()
    return b


mode = sys.argv[1]
if mode == 'prepare':
    assert not safe(MANIFEST).exists()
    binding = input_binding()
    literal = labels()
    put(BASE, {'prepared_utc': now(), 'binding': binding, 'literal_checks': literal,
               'NO_NEW_corresponding_peer_findings_files_inventory_hash_metadata_access': True})
    put(META, {
        'reviewer': '/root/review_2017_coarsening_r1',
        'role': 'OTHER initially blind ENTIRE WHOLE2',
        'whole_obligations': 64, 'ENTIRE_files': 8,
        'NEW_constructor': '/root/review_2022_complexity_r2',
        'reviewer_NEW_construction_contribution': False,
        'old_SQ15_C_authorship_not_independent_self_recertification': True,
        'old_SQ14_fractional_domain_miss_and_full_repair_preserved': True,
        'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'verified_effective_setting_readback': None,
        'full_final_MODEL_ALL7_payloads_then_manifest_readback_required': True,
        'SEPARATE_readonly_verify_after_full_manifest_MODEL_readback_required': True,
        'NO_NEW_corresponding_peer_findings_files_inventory_hash_metadata_access': True,
        'findings_EMBARGO_until_explicit_BOTH_ENTIRE': True,
        'all_mathematics_hand_reconstruction': True,
        'documentary_code_not_mathematical_program': True,
        'no_mathematical_CAS_scan_test_source_author_old_replay': True,
        'old_shared_Git_cache_bytes_changed': False,
        'no_native_browser_CUA_fee_contact_bypass_spawn_pending_child_or_approval': True,
        'author': binding['author_freeze'],
        'own_parent': record(PARENT), 'guard_summary': binding['effective_guard_summary'],
        'direct_weekly_used_percent': 69, 'direct_at_utc': '2026-10-18 23:02:29 UTC',
        'ordinaryUsageAllowed': True, 'legacy_and_by_limit_agree': True,
        'authorised_weekly_reset': 1792874445,
        'hard_TOTAL_ceiling': 90, 'integration_reserve': True,
        'automatic_later_weekly_window_spending': False})
    print(json.dumps({'prepared_utc': now(), 'guard_summary': binding['effective_guard_summary'],
                      'literal_checks': literal}))
elif mode == 'freeze':
    b = baseline()
    put(MANIFEST, {
        'frozen_utc': now(), 'reviewer': '/root/review_2017_coarsening_r1',
        'role': 'OTHER initially blind ENTIRE WHOLE2',
        'ENTIRE_files': 8, 'whole_obligations': 64,
        'payload_records': [record(p) for p in PAYLOADS],
        'author': b['binding']['author_freeze'], 'own_parent': record(PARENT),
        'effective_guard_summary': b['binding']['effective_guard_summary'],
        'FULL_final_MODEL_ALL7_payload_readback_completed': True,
        'FULL_manifest_MODEL_readback_then_SEPARATE_readonly_verify_required': True,
        'NO_NEW_corresponding_peer_findings_files_inventory_hash_metadata_access': True,
        'findings_EMBARGO_until_explicit_BOTH_ENTIRE': True,
        'mathematical_program': False, 'old_shared_Git_cache_bytes_changed': False})
    print(json.dumps({'manifest': record(MANIFEST), 'ENTIRE_files': 8}))
elif mode == 'verify':
    b = baseline()
    m = read(MANIFEST)
    assert m['ENTIRE_files'] == 8 and m['whole_obligations'] == 64
    assert [r['path'] for r in m['payload_records']] == PAYLOADS
    for r in m['payload_records']:
        check(r)
    assert m['author'] == b['binding']['author_freeze']
    assert m['own_parent'] == record(PARENT)
    assert m['effective_guard_summary'] == b['binding']['effective_guard_summary']
    print(json.dumps({'separate_readonly_verified_utc': now(), 'PASS': True,
                      'ENTIRE_files': 8, 'whole_obligations': 64,
                      'initial': record(P + 'initial-v1.md'), 'manifest': record(MANIFEST)}))
else:
    raise SystemExit('usage: prepare | freeze | verify')
