#!/usr/bin/env python3
"""DR6 R2 administrative preservation only: no mathematics or old rerun."""
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BASE = Path('problems/2025-B4/reviews')
PREFIX = 'reasoning-diagonal-return-r6-review-2-'
AUTHOR = 'problems/2025-B4/notes/reasoning-diagonal-return-r6-'
AF = AUTHOR + 'freeze-v1.json'
EXPECTED_AF = (3623, 'a9edb267e1b417beedcfbe57dec293b9d494fe878f2758ccbdc4f5c300188b8d')
EXPECTED_MAIN = (16586, 'd8833575a24f27dc586790580e42423dd0ad36232d8164a0b41f76b75e05a643')
PARENT = 'problems/2022-B4/notes/reasoning-dynamics-return-r7-freeze-v1.json'
EXPECTED_PARENT = (3391, '305eb7fbd3a9c6282c34310e72c8ffd862c4ac5315996cf2cced945d503994b2')


def now():
    return datetime.now(timezone.utc).isoformat()


def own(name):
    return str(BASE / (PREFIX + name))


def rec(path):
    p = Path(path)
    assert not p.is_absolute() and '..' not in p.parts
    assert not str(p).startswith('problems/2025-B4/reviews/reasoning-diagonal-return-r6-review-1-')
    data = (ROOT / p).read_bytes()
    return {'path': str(p), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def load(path):
    return json.loads((ROOT / path).read_text())


def validate(row):
    actual = rec(row['path'])
    assert actual == row, {'declared': row, 'actual': actual}
    return actual


def rows(value):
    if isinstance(value, dict):
        if isinstance(value.get('path'), str) and isinstance(value.get('bytes'), int) and re.fullmatch(r'[0-9a-f]{64}', str(value.get('sha256', ''))):
            yield {k: value[k] for k in ('path', 'bytes', 'sha256')}
        for item in value.values():
            yield from rows(item)
    elif isinstance(value, list):
        for item in value:
            yield from rows(item)


def canonical(records):
    unique = {}
    for row in records:
        row = validate(row)
        assert row['path'] not in unique or unique[row['path']] == row
        unique[row['path']] = row
    values = sorted(unique.values(), key=lambda row: row['path'])
    return {'record_occurrences': len(records), 'deduplicated_paths': len(values),
            'canonical_sha256': hashlib.sha256(json.dumps(values, sort_keys=True, separators=(',', ':')).encode()).hexdigest()}


def labels():
    expected = [f'DR6-{i:02d}' for i in range(1, 49)]
    for path in (AUTHOR + 'obligations-v1.md', AUTHOR + 'checks-v1.md', own('ledger-v1.md')):
        found = re.findall(r'^\| (DR6-\d{2}) \|', (ROOT / path).read_text(), re.M)
        assert found == expected, (path, found)
    notes = re.findall(r'^\| (DR6R2-N\d+) \|', (ROOT / own('issues-v1.md')).read_text(), re.M)
    assert notes == [f'DR6R2-N{i}' for i in range(1, 8)]


def inputs():
    af = rec(AF)
    assert (af['bytes'], af['sha256']) == EXPECTED_AF
    main = rec(AUTHOR + 'candidate-v1.md')
    assert (main['bytes'], main['sha256']) == EXPECTED_MAIN
    frozen = load(AF)
    assert len(frozen['artifacts']) == 12 and frozen['ENTIRE_files'] == 13
    author_records = [af] + frozen['artifacts']
    author_summary = canonical(author_records)
    author_paths = {str(p.relative_to(ROOT)) for p in (ROOT / 'problems/2025-B4/notes').glob('reasoning-diagonal-return-r6-*') if p.is_file()}
    assert author_paths == {r['path'] for r in author_records}
    baseline = load(AUTHOR + 'baseline-v1.json')
    protected = list(baseline['direct_frozen_input_bindings'])
    containers = baseline['compact_immutable_parent_container_bindings']
    for item in containers:
        validate(item)
        protected.append(item)
        protected.extend(rows(load(item['path'])))
    old_summary = canonical(protected)
    assert old_summary['record_occurrences'] == baseline['protected_occurrences'] == frozen['protected_occurrences']
    assert old_summary['deduplicated_paths'] == baseline['protected_unique_paths'] == frozen['protected_unique_paths']
    assert old_summary['canonical_sha256'] == baseline['canonical_deduplicated_sha256'] == frozen['canonical_deduplicated_sha256']
    parent = rec(PARENT)
    assert (parent['bytes'], parent['sha256']) == EXPECTED_PARENT
    all_guard = author_records + protected + [parent]
    labels()
    return {'author_freeze': af, 'author_main': main, 'author_ENTIRE_files': 13,
            'author_artifact_summary': author_summary,
            'direct_operative_bindings': baseline['direct_frozen_input_bindings'],
            'bound_old_containers': containers, 'old_input_deduplicated_summary': old_summary,
            'immediate_own_parent': parent, 'all_guard_summary': canonical(all_guard),
            'recipe': 'Validate all13 constructor bytes and all standard records in the bound immediate old containers; preserve full historical inventory by exact container binding and deduplicated summary. No further historical recursion, old program replay or corresponding NEW peer access.'}


def write(name, value):
    with (ROOT / own(name)).open('x') as f:
        json.dump(value, f, indent=2, ensure_ascii=False)
        f.write('\n')


def prepare():
    data = inputs()
    write('baseline-v1.json', {'created_at_utc': now(), 'status': 'independent whole initial review; findings embargoed', **data})
    write('input-validation-v1.json', {'validated_at_utc': now(), 'status': 'PASS administrative preservation only',
          'baseline': rec(own('baseline-v1.json')), 'author_ENTIRE_files': 13, 'author_obligations_checks_and_review_ledger': [48, 48, 48],
          'closed_scope_notes': 7, 'all_guard_summary': data['all_guard_summary'],
          'no_mathematical_program_or_old_author_rerun': True, 'corresponding_NEW_peer_access': False})
    write('metadata-v1.json', {'created_at_utc': now(), 'reviewer': '/root/review_2017_coarsening_r1',
          'constructor': '/root/review_2021_reasoning_j15_r2', 'NEW_DR6_nonconstructor': True,
          'review_kind': 'OTHER initially blind ENTIRE WHOLE2', 'whole_obligations': 48,
          'disposition': 'all48 pass exact scoped partial result', 'substantive_open_issues': 0, 'closed_scope_notes': 7,
          'older_C_R6_constructor_and_RS_BR_BD_review_roles_disclosed': True,
          'no_independent_self_recertification_of_old_inputs': True,
          'only_old_nonelementary_new_proof_import': 'accepted RD3 exact actual signed residual cofactor inequality',
          'corresponding_NEW_root_DR6_finding_file_hash_metadata_accessed': False,
          'identity_only_handoff_until_explicit_BOTH_ENTIRE_confirmation': True,
          'FULL_final_model_readback_ALLfiles_then_SEPARATE_readonly_verify_required': True,
          'requested_model': 'gpt-6.1-sol', 'requested_reasoning': 'max', 'effective_readback': 'unavailable',
          'authorized_weekly_reset': 1792874445, 'total_used_percent_last_reported': 41,
          'worker_new_meter_read': False, 'total_ceiling_percent': 90, 'integration_reserve': True,
          'automatic_future_window_spending': False, 'mathematical_program_CAS_scan_test_or_old_replay': False,
          'pending_tool_approval_native_child_PID_or_source_wait': None,
          'Git_shared_cache_old_mutation_or_annual_priority_promotion': False})
    print(json.dumps({'prepared_at_utc': now(), 'all_guard_summary': data['all_guard_summary'], 'whole_ledger': 48}, indent=2))


def freeze():
    data = inputs()
    baseline = load(own('baseline-v1.json'))
    for key in ('author_freeze', 'author_main', 'all_guard_summary', 'old_input_deduplicated_summary', 'immediate_own_parent'):
        assert data[key] == baseline[key]
    files = sorted(p for p in (ROOT / BASE).glob(PREFIX + '*') if p.is_file())
    assert len(files) == 10, [str(p) for p in files]
    for path in files:
        if path.suffix == '.json':
            json.loads(path.read_text())
    write('manifest-v1.json', {'frozen_at_utc': now(), 'reviewer': '/root/review_2017_coarsening_r1',
          'status': 'ENTIRE initially blind OTHER WHOLE2 initial frozen; findings embargoed',
          'whole_obligations': 48, 'payload_files': 10, 'ENTIRE_files': 11,
          'constructor_excluded': True, 'corresponding_NEW_peer_access_before_ENTIRE': False,
          'identity_only_until_explicit_BOTH_ENTIRE': True,
          'FULL_final_ALLfiles_model_readback_then_SEPARATE_readonly_verify_required': True,
          'author_freeze': data['author_freeze'], 'author_main': data['author_main'],
          'immediate_own_parent': data['immediate_own_parent'], 'all_guard_summary': data['all_guard_summary'],
          'artifacts': [rec(p.relative_to(ROOT)) for p in files]})
    print(json.dumps({'manifest': rec(own('manifest-v1.json')), 'initial': rec(own('initial-v1.md')), 'ENTIRE_files': 11, 'whole_obligations': 48}, indent=2))


def verify():
    data = inputs()
    manifest = load(own('manifest-v1.json'))
    assert len(manifest['artifacts']) == 10
    for row in manifest['artifacts']:
        validate(row)
        if row['path'].endswith('.json'):
            load(row['path'])
    files = {str(p.relative_to(ROOT)) for p in (ROOT / BASE).glob(PREFIX + '*') if p.is_file()}
    assert files == {r['path'] for r in manifest['artifacts']} | {own('manifest-v1.json')}
    assert data['all_guard_summary'] == manifest['all_guard_summary'] == load(own('baseline-v1.json'))['all_guard_summary']
    print(json.dumps({'separate_readonly_verify_at_utc': now(), 'status': 'PASS', 'ENTIRE_files': 11,
          'whole_obligations': 48, 'manifest': rec(own('manifest-v1.json')), 'initial': rec(own('initial-v1.md')),
          'all_guard_summary': data['all_guard_summary'], 'no_math_computation_old_mutation_or_NEW_peer_access': True}, indent=2))


if __name__ == '__main__':
    modes = {'prepare': prepare, 'freeze': freeze, 'verify': verify}
    assert len(sys.argv) == 2 and sys.argv[1] in modes
    modes[sys.argv[1]]()
