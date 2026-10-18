#!/usr/bin/env python3
"""NEW R14 documentary integrity only; no mathematical computation/replay."""
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
P = 'problems/2017-B4/notes/reasoning-lower-return-r14-'
FILES = [P + s for s in (
    'working-v1.md', 'candidate-v1.md', 'obligations-v1.md',
    'research-v1.md', 'sources-v1.json', 'integrity-v1.py',
    'baseline-v1.json', 'metadata-v1.json')]
BASELINE = P + 'baseline-v1.json'
METADATA = P + 'metadata-v1.json'
FREEZE = P + 'freeze-v1.json'
PARENT = 'problems/2022-B4/reviews/reasoning-collision-return-r10-review-1-manifest-v1.json'
AUTHORITIES = [
    'problems/2017-B4/reviews/reasoning-pressure-return-r11-acceptance.json',
    'problems/2017-B4/reviews/reasoning-concentration-return-r12-acceptance.json']
THEOREM_INPUTS = [
    'AGENTS.md', 'problems/2017-B4/statement.md',
    'problems/2017-B4/proofs/reviewed-reasoning-pressure-return-r11-v1.1.md',
    'problems/2017-B4/reviews/reasoning-pressure-return-r11-acceptance.md',
    AUTHORITIES[0],
    'problems/2017-B4/proofs/reviewed-reasoning-concentration-return-r12-v1.1.md',
    'problems/2017-B4/reviews/reasoning-concentration-return-r12-acceptance.md',
    AUTHORITIES[1]]
EXPECTED = {
    'AGENTS.md': (4707, '28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff'),
    THEOREM_INPUTS[2]: (26687, '56688cd6030db910fbbc9162436b25acbf61a69869e2501dbd6f50b088bc3b60'),
    THEOREM_INPUTS[5]: (24123, '15823ad1a7c54b8e06de3692f19d3395d2458786dcb8d2d51a2eb3c592734554'),
    PARENT: (3336, '6f911026df258a3ec5c6c95549aaa5b8a0e197ac71a12a8c85ad0cb2158b9a1c')}


def now():
    return datetime.now(timezone.utc).isoformat()


def safe(path):
    p = Path(path)
    assert not p.is_absolute() and '..' not in p.parts
    assert not path.startswith('problems/2017-B4/reviews/reasoning-lower-return-r14-review-')
    if path.startswith('problems/2017-B4/'):
        assert 'r13' not in p.name.lower() and 'tensor' not in p.name.lower()
    resolved = (ROOT / path).resolve()
    assert resolved.is_relative_to(ROOT)
    return resolved


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


def read_json(path):
    return json.loads(safe(path).read_text())


def put(path, obj):
    with safe(path).open('x') as f:
        json.dump(obj, f, indent=2)
        f.write('\n')


def summary(records):
    unique = {}
    for r in records:
        assert r['path'] not in unique or unique[r['path']] == r
        unique[r['path']] = r
    canonical = json.dumps([unique[k] for k in sorted(unique)],
                           sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(records), 'unique_paths': len(unique),
            'canonical_deduplicated_sha256': digest(canonical)}


def inputs():
    theorem = [record(p) for p in THEOREM_INPUTS]
    parent = read_json(PARENT)
    parent_records = [record(PARENT)] + parent['payload_records']
    for r in parent_records:
        check(r)
    inherited = parent['effective_guard_summary']
    assert inherited == {
        'occurrences': 83, 'unique_paths': 79,
        'canonical_deduplicated_sha256':
        'e993773c8a56b0ea74bb6efbe9c7b009302749811d37f755f75a38673021ad67'}
    authorities, declarations = [], []
    for path in AUTHORITIES:
        a = read_json(path)
        assert a['status'] == 'proved, independently reviewed scoped partial result'
        assert a['whole_initials_blind'] is True
        assert a['unresolved_substantive_issues'] == 0
        declared = [a['candidate'], a['accepted_copy']] + a['verification_metadata']
        for r in declared:
            check(r)
        old_candidate = safe(a['candidate']['path']).read_bytes()
        old_accepted = safe(a['accepted_copy']['path']).read_bytes()
        assert old_accepted.endswith(old_candidate), path
        declarations += declared
        authorities.append({'authority': record(path),
                            'declared_summary': summary(declared),
                            'accepted_copy_exact_candidate_suffix': True,
                            'whole_initials_blind': True,
                            'unresolved_substantive_issues': 0})
    all_records = theorem + parent_records + declarations
    return {
        'direct_theorem_inputs': theorem,
        'own_immediate_parent_binding': record(PARENT),
        'own_parent_payload_records': parent['payload_records'],
        'own_parent_inherited_summary_binding_only': inherited,
        'accepted_authorities': authorities,
        'effective_guard_summary': summary(all_records),
        'older_guard_inventory_not_recursively_copied_or_replayed': True}


def check_labels():
    text = safe(P + 'obligations-v1.md').read_text()
    labels = re.findall(r'^\|LF14-(\d\d)\|', text, re.M)
    assert labels == [f'{i:02}' for i in range(1, 57)]
    s = read_json(P + 'sources-v1.json')
    assert s['whole_obligations'] == 56
    assert s['constructor_excluded'] is True
    return 56


def validate_baseline():
    b = read_json(BASELINE)
    assert b['binding'] == inputs()
    assert b['whole_obligation_labels'] == check_labels()
    return b


mode = sys.argv[1]
if mode == 'prepare':
    assert not safe(FREEZE).exists()
    binding = inputs()
    check_labels()
    put(BASELINE, {
        'prepared_utc': now(), 'binding': binding,
        'whole_obligation_labels': 56,
        'all_direct_inputs_and_current_authority_declarations_verified': True,
        'no_future_NEW_peer_or_root_R13_access': True})
    put(METADATA, {
        'status': 'candidate proof - unverified',
        'constructor': '/root/review_2017_coarsening_r1',
        'constructor_excluded': True,
        'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'verified_effective_setting_readback': None,
        'claims': ['LF14A', 'LF14B', 'LF14C', 'LF14D'],
        'whole_obligations': 56,
        'TWO_OTHER_initially_blind_ENTIRE_whole_audits_required': 2,
        'root_NEW_proof_inference': False,
        'older_R11_R12_C_authorship_accepted_input_not_self_recertification': True,
        'actual_marked_classes_not_reduced_word_multiplicity': True,
        'all_mathematics_hand_reasoning': True,
        'documentary_integrity_only_no_mathematical_program': True,
        'no_old_source_author_freezer_certificate_replay': True,
        'no_root_R13_tensor_or_future_NEW_peer_access': True,
        'old_shared_Git_cache_bytes_changed': False,
        'raw_primary_download_hash': None,
        'primary_literal_read_limits': P + 'sources-v1.json',
        'unresolved_global_value_effective_R_J_S_priority': True,
        'own_parent_binding': record(PARENT),
        'guard_summary': binding['effective_guard_summary'],
        'authorised_weekly_reset': 1792874445,
        'latest_direct_used_percent': 68,
        'latest_direct_utc': '2026-10-18 22:53:25 UTC',
        'ordinaryUsageAllowed': True,
        'legacy_and_by_limit_telemetry_agree': True,
        'stop_at_or_below_90_TOTAL_with_integration_reserve': True,
        'no_automatic_further_weekly_window': True,
        'no_pending_approval_or_native_child': True,
        'FULL_final_MODEL_ALL_payload_readback_before_freeze_required': True,
        'FULL_freeze_MODEL_readback_then_SEPARATE_readonly_verify_required': True})
    print(json.dumps({'prepared_utc': now(), 'payload_files': len(FILES),
                      'guard_summary': binding['effective_guard_summary']}))
elif mode == 'freeze':
    b = validate_baseline()
    records = [record(p) for p in FILES]
    put(FREEZE, {
        'frozen_utc': now(), 'status': 'candidate proof - unverified',
        'constructor': '/root/review_2017_coarsening_r1',
        'constructor_excluded': True, 'ENTIRE_files': len(FILES) + 1,
        'claims': ['LF14A', 'LF14B', 'LF14C', 'LF14D'],
        'whole_obligations': 56, 'payload_records': records,
        'own_parent': record(PARENT),
        'effective_guard_summary': b['binding']['effective_guard_summary'],
        'FULL_final_MODEL_ALL8_payload_readback_completed': True,
        'FULL_freeze_MODEL_readback_then_SEPARATE_readonly_verify_required': True,
        'TWO_OTHER_initially_blind_ENTIRE_whole_audits_required': 2,
        'root_NEW_construction_inference': False,
        'NO_NEW_future_peer_or_root_R13_access': True,
        'mathematical_program': False,
        'old_shared_Git_cache_bytes_changed': False})
    print(json.dumps({'freeze': record(FREEZE), 'ENTIRE_files': len(FILES) + 1}))
elif mode == 'verify':
    validate_baseline()
    f = read_json(FREEZE)
    assert f['ENTIRE_files'] == 9 and f['whole_obligations'] == 56
    assert [r['path'] for r in f['payload_records']] == FILES
    for r in f['payload_records']:
        check(r)
    assert f['own_parent'] == record(PARENT)
    assert f['effective_guard_summary'] == inputs()['effective_guard_summary']
    print(json.dumps({'separate_readonly_verified_utc': now(), 'PASS': True,
                      'ENTIRE_files': 9, 'whole_obligations': 56,
                      'main': record(P + 'candidate-v1.md'),
                      'freeze': record(FREEZE)}))
else:
    raise SystemExit('usage: prepare | freeze | verify')
