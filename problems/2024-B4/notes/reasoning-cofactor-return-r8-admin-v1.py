#!/usr/bin/env python3
"""R8 administration only: fingerprints/JSON/labels, never mathematics."""
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BASE = Path('problems/2024-B4/notes')
PREFIX = 'reasoning-cofactor-return-r8-'
PARENT = 'problems/2025-B4/reviews/reasoning-diagonal-return-r6-review-2-manifest-v1.json'
EXPECTED_PARENT = (3450, 'a8489d9b8b932cf48f1237f01b1521ff93fd773d5becb9658c75e2e972701ce6')
THESIS = '.cache/literature/deep-literature-r2/2024-mcguire-thesis-1995.pdf'
EXPECTED_THESIS = (2610589, 'd8e8e62d873c5ec69e2fd40473a9aee257bb8d4994cb5ffc1a42cb70f8bcbd24')
AUTHORITIES = [
    ('structural-acceptance', 'reviewed-structural-v1.1.md', 17079, '082dc054ce2cdaea80eee009f4c97c877c6968afb54b5a8f3141b7354031dd3f'),
    ('reasoning-cofactor-return-r6-acceptance', 'reviewed-reasoning-cofactor-return-r6-v1.1.md', 20658, 'fb988a13187b5765619532ad14077ae2f32a948e04704252e3d8981e10d65d98'),
    ('reasoning-cofactor-return-r7-acceptance', 'reviewed-reasoning-cofactor-return-r7-v1.1.md', 22608, 'b8e2cc3a37cf8c80c724c0d26f6768261e5d339fee073351e8b4c9b56b94cf72'),
]
CONTEXTS = [
    'AGENTS.md', 'problems/2024-B4/statement.md',
    'problems/2024-B4/proofs/reviewed-cofactor-dominant-r4-v1.1.md',
    'problems/2024-B4/proofs/reviewed-cofactor-Frobenius-r5-v2.1.md',
    'problems/2024-B4/notes/reasoning-cofactor-return-r6-failed-routes-v1.md',
    'problems/2024-B4/notes/reasoning-cofactor-return-r7-issues-failures-v1.md',
    'problems/2024-B4/notes/reasoning-cofactor-return-r7-source-audit-v1.md',
    'problems/2024-B4/notes/reasoning-sector3-return-r1-source-audit-v1.md',
]
IMAGES = [f'.cache/literature/deep-literature-r2/2024-mcguire-thesis-1995-{i:02d}.png' for i in range(21, 32)]


def now():
    return datetime.now(timezone.utc).isoformat()


def own(name):
    return str(BASE / (PREFIX + name))


def rec(path):
    p = Path(path)
    assert not p.is_absolute() and '..' not in p.parts
    assert not str(p).startswith('problems/2024-B4/reviews/reasoning-cofactor-return-r8-review-')
    data = (ROOT / p).read_bytes()
    return {'path': str(p), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def load(path):
    return json.loads((ROOT / path).read_text())


def validate(row):
    actual = rec(row['path'])
    assert actual == row, {'expected': row, 'actual': actual}
    return actual


def records(value):
    if isinstance(value, dict):
        if isinstance(value.get('path'), str) and isinstance(value.get('bytes'), int) and re.fullmatch(r'[0-9a-f]{64}', str(value.get('sha256', ''))):
            yield {key: value[key] for key in ('path', 'bytes', 'sha256')}
        for child in value.values():
            yield from records(child)
    elif isinstance(value, list):
        for child in value:
            yield from records(child)


def summary(rows):
    unique = {}
    for row in rows:
        validate(row)
        assert row['path'] not in unique or unique[row['path']] == row
        unique[row['path']] = row
    canonical = sorted(unique.values(), key=lambda row: row['path'])
    return {'fingerprint_occurrences': len(rows), 'deduplicated_paths': len(unique),
            'canonical_sha256': hashlib.sha256(json.dumps(canonical, sort_keys=True, separators=(',', ':')).encode()).hexdigest()}


def labels():
    expected = [f'R8-{i:02d}' for i in range(1, 49)]
    for name in ('obligations-v1.md', 'constructor-checks-v1.md'):
        got = re.findall(r'^\| (R8-\d{2}) \|', (ROOT / own(name)).read_text(), re.M)
        assert got == expected, (name, got)


def inputs():
    parent = rec(PARENT)
    assert (parent['bytes'], parent['sha256']) == EXPECTED_PARENT
    thesis = rec(THESIS)
    assert (thesis['bytes'], thesis['sha256']) == EXPECTED_THESIS
    guards = [rec(path) for path in CONTEXTS] + [parent, thesis] + [rec(path) for path in IMAGES]
    authority_matches = []
    for stem, body_name, size, digest in AUTHORITIES:
        body = rec('problems/2024-B4/proofs/' + body_name)
        assert (body['bytes'], body['sha256']) == (size, digest), body
        js = 'problems/2024-B4/reviews/' + stem + '.json'
        md = 'problems/2024-B4/reviews/' + stem + '.md'
        matched = [row for row in records(load(js)) if row['path'] == body['path']]
        assert matched and all(validate(row) == body for row in matched)
        guards += [body, rec(md), rec(js)]
        authority_matches.append({'authority': js, 'accepted_body': body, 'matching_declared_occurrences': len(matched)})
    labels()
    return {'direct_immutable_guard_bindings': guards, 'guard_summary': summary(guards),
            'current_authority_body_matches': authority_matches, 'immediate_own_parent': parent,
            'recipe': 'Bind exact current necessary bodies/MDJSON/source bytes and immediate own immutable parent. Count/deduplicate these direct guard records only; do not copy or recursively replay the growing historical inventory. Parent is preservation, not a mathematical premise.'}


def write(name, value):
    with (ROOT / own(name)).open('x') as f:
        json.dump(value, f, indent=2, ensure_ascii=False)
        f.write('\n')


def prepare():
    data = inputs()
    write('baseline-v1.json', {'created_at_utc': now(), 'status': 'candidate proof - unverified', **data})
    write('input-validation-v1.json', {'validated_at_utc': now(), 'status': 'PASS administrative only',
          'baseline': rec(own('baseline-v1.json')), 'guard_summary': data['guard_summary'],
          'current_body_authority_matches': 3, 'whole_obligations_and_checks': [48, 48],
          'mathematical_code_scan_CAS_author_source_or_old_replay': False})
    write('metadata-v1.json', {'created_at_utc': now(), 'status': 'candidate proof - unverified',
          'constructor': '/root/review_2017_coarsening_r1', 'constructor_excluded': True,
          'root_generic_target_only_no_NEW_inference': True, 'claims': ['R8A', 'R8B', 'R8C'],
          'whole_obligations': 48, 'TWO_OTHER_ENTIRE_initially_blind_WHOLE_audits_required': True,
          'older_C_R6_R7_constructor_and_T1_review_roles_disclosed': True,
          'no_independent_self_recertification_of_old_inputs': True,
          'whole_absolute_not_component_only': True, 'NF4_assumption_explicit': True,
          'odd_ell_min': 3, 'i_min': 2, 'excluded_absolute_pair': [3, 4],
          'published_Theorems6_7_and_arithmetic_conditions_attributed': True,
          'Ferard_journal_JW1993_unread_limits_retained': True,
          'annual_converse_priority_or_external_validation_claim': False,
          'requested_model': 'gpt-6.1-sol', 'requested_reasoning': 'max', 'effective_readback': 'unavailable',
          'fresh_authoritative_total_used_percent': 44, 'observed_utc_minute': '2026-10-18T14:48Z',
          'window_minutes': 10080, 'authorized_weekly_reset': 1792874445,
          'ordinaryUsageAllowed': True, 'total_ceiling_percent': 90, 'integration_reserve': True,
          'automatic_later_window_spending': False,
          'math_program_CAS_scan_test_optimizer_or_old_replay': False,
          'pending_tool_approval_retrieval_or_native_child_PID': None,
          'old_shared_cache_or_Git_mutation': False,
          'FULL_final_ALLfiles_readback_then_SEPARATE_readonly_verify_REQUIRED_before_handoff': True})
    print(json.dumps({'prepared_at_utc': now(), 'guard_summary': data['guard_summary'], 'whole_obligations': 48}, indent=2))


def freeze():
    data = inputs()
    baseline = load(own('baseline-v1.json'))
    assert data['guard_summary'] == baseline['guard_summary']
    assert data['direct_immutable_guard_bindings'] == baseline['direct_immutable_guard_bindings']
    files = sorted(p for p in (ROOT / BASE).glob(PREFIX + '*') if p.is_file())
    assert len(files) == 12, [str(p) for p in files]
    for path in files:
        if path.suffix == '.json':
            json.loads(path.read_text())
    write('freeze-v1.json', {'frozen_at_utc': now(), 'status': 'candidate proof - unverified',
          'constructor': '/root/review_2017_coarsening_r1', 'constructor_excluded': True,
          'claims': ['R8A', 'R8B', 'R8C'], 'whole_obligations': 48,
          'payload_files': 12, 'ENTIRE_files': 13,
          'TWO_OTHER_ENTIRE_initially_blind_WHOLE_audits_required': True,
          'FULL_final_ALLfiles_model_readback_then_SEPARATE_readonly_verify_REQUIRED': True,
          'immediate_own_parent': data['immediate_own_parent'], 'compact_baseline': rec(own('baseline-v1.json')),
          'guard_summary': data['guard_summary'],
          'artifacts': [rec(path.relative_to(ROOT)) for path in files]})
    print(json.dumps({'freeze': rec(own('freeze-v1.json')), 'main': rec(own('candidate-v1.md')),
                      'ENTIRE_files': 13, 'whole_obligations': 48}, indent=2))


def verify():
    data = inputs()
    frozen = load(own('freeze-v1.json'))
    assert len(frozen['artifacts']) == 12
    for row in frozen['artifacts']:
        validate(row)
        if row['path'].endswith('.json'):
            load(row['path'])
    files = {str(p.relative_to(ROOT)) for p in (ROOT / BASE).glob(PREFIX + '*') if p.is_file()}
    assert files == {row['path'] for row in frozen['artifacts']} | {own('freeze-v1.json')}
    assert data['guard_summary'] == frozen['guard_summary'] == load(own('baseline-v1.json'))['guard_summary']
    print(json.dumps({'separate_readonly_verify_at_utc': now(), 'status': 'PASS', 'ENTIRE_files': 13,
          'whole_obligations': 48, 'guard_summary': data['guard_summary'],
          'freeze': rec(own('freeze-v1.json')), 'main': rec(own('candidate-v1.md')),
          'no_mathematical_computation_or_old_mutation': True}, indent=2))


if __name__ == '__main__':
    modes = {'prepare': prepare, 'freeze': freeze, 'verify': verify}
    assert len(sys.argv) == 2 and sys.argv[1] in modes
    modes[sys.argv[1]]()
