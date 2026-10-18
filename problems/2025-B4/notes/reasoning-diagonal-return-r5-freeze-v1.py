"""RD constructor metadata only: no mathematical evaluation or old-code replay."""
import datetime
import hashlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PREFIX = 'problems/2025-B4/notes/reasoning-diagonal-return-r5-'
OWN_PARENT = {
    'path': 'problems/2021-B4/reviews/reasoning-center-return-r18-review-1-manifest-v1.json',
    'bytes': 7546,
    'sha256': 'e120e51aa4f11421a964419da71e0e2d924d07a5373569630beb07bf385daad0',
}
ACCEPTED = [
    ('reasoning-branch-return-r4', 25278, 'c5bbac8c0671adc8a3b06b750a46b6b2df732b9d896506870f4c374f0f07843c'),
    ('reasoning-Runge-return-r3', 28696, 'd27502c014cfd83d56923cea1740daf6d159bee19e15b4b17d18749e16a0ba98'),
    ('reasoning-Runge-return-r2', 27717, '33222ffbc2a756fe5f7a9641c248654b0d5626e8283d3d054624b69496c658a3'),
    ('reasoning-return-r6', 28748, '4e157819789da12d6f26e89929d88ec886d52947405d836fe3957ab8ee727d3a'),
]
CONTEXT = [
    'AGENTS.md', 'problems/2025-B4/statement.md',
    'problems/2025-B4/references.md', 'problems/2025-B4/research.md',
    'problems/2025-B4/notes/coordinator-literature-return-r5-source-access-v1.md',
    'problems/2025-B4/notes/coordinator-literature-return-r5-source-access-v1.json',
    'problems/2025-B4/notes/reasoning-branch-return-r4-failed-routes-v1.md',
    'problems/2025-B4/notes/reasoning-Runge-return-r3-failed-routes-v1.md',
    'problems/2025-B4/notes/reasoning-Runge-return-r2-failed-routes-v1.md',
]
PAYLOAD_SUFFIXES = [
    'candidate-v1.md', 'obligations-v1.md', 'constructor-checks-v1.md',
    'failed-routes-v1.md', 'sources-v1.md', 'sources-v1.json',
    'worklog-v1.md', 'freeze-v1.py', 'baseline-v1.json',
    'input-validation-v1.json',
]
FORBIDDEN = [
    'problems/2024-B4/reviews/',
    'problems/2021-B4/reviews/reasoning-center-return-r18-review-2-',
    'problems/2020-B4/reviews/reasoning-arithmetic-return-r13-review-',
]


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def safe(name):
    assert isinstance(name, str) and not pathlib.Path(name).is_absolute()
    assert '..' not in pathlib.Path(name).parts
    assert not any(token in name for token in FORBIDDEN), ('forbidden peer', name)
    return ROOT / name


def fp(name):
    data = safe(name).read_bytes()
    return {'path': name, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def check(record):
    actual = fp(record['path'])
    assert actual == {key: record[key] for key in ('path', 'bytes', 'sha256')}, record['path']
    return actual


def read_json(name):
    return json.loads(safe(name).read_text())


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()


def write_new(suffix, obj):
    name = PREFIX + suffix
    assert name.startswith(PREFIX)
    with safe(name).open('x') as stream:
        json.dump(obj, stream, indent=2, ensure_ascii=False)
        stream.write('\n')


def gather():
    protected = [fp(name) for name in CONTEXT]
    check(OWN_PARENT)
    parent = read_json(OWN_PARENT['path'])
    assert parent['older_plus_new_own_paths_bound_transitively'] == 749
    protected.append(OWN_PARENT)
    protected.extend(check(record) for record in parent['artifacts'])
    accepted = []
    for name, size, digest in ACCEPTED:
        md = f'problems/2025-B4/reviews/{name}-acceptance.md'
        js = f'problems/2025-B4/reviews/{name}-acceptance.json'
        authority = read_json(js)
        assert authority['status'] == 'proved, independently reviewed scoped partial result'
        body = check(authority['accepted_copy'])
        assert body['bytes'] == size and body['sha256'] == digest
        candidate = check(authority['candidate'])
        assert safe(body['path']).read_bytes().endswith(safe(candidate['path']).read_bytes())
        protected.extend([fp(md), fp(js), body, candidate])
        accepted.append({
            'authority': fp(js), 'accepted_body': body, 'candidate_suffix': candidate,
            'historical_record_occurrences_bound_not_replayed': authority.get('record_occurrences_verified'),
            'historical_unique_paths_bound_not_replayed': authority.get('unique_paths_verified'),
        })
    unique = {}
    for record in protected:
        check(record)
        if record['path'] in unique:
            assert unique[record['path']] == record
        unique[record['path']] = record
    ordered = [unique[name] for name in sorted(unique)]
    return {
        'protected_inputs': ordered,
        'protected_fingerprint_occurrences': len(protected),
        'protected_unique_paths': len(ordered),
        'canonical_protected_summary_sha256': hashlib.sha256(canonical(ordered)).hexdigest(),
        'accepted_operative_bindings': accepted,
        'immediate_own_parent': OWN_PARENT,
        'older_own_paths_bound_transitively': 749,
        'new_constructor_files_including_freeze': len(PAYLOAD_SUFFIXES) + 1,
        'older_plus_new_own_paths_bound_transitively': 749 + len(PAYLOAD_SUFFIXES) + 1,
        'no_historical_inventory_recopy_or_recursive_replay': True,
        'research_md_actual_read_scope_only_opening1_100': True,
        'context_is_not_a_new_mathematical_premise': True,
    }


def labels():
    text = safe(PREFIX + 'obligations-v1.md').read_text()
    expected = [f'{i:02}' for i in range(1, 49)]
    assert re.findall(r'^\|(\d{2})\|', text, re.M) == expected
    return {'whole_obligation_labels': 48, 'all_consecutive': True}


def verified_baseline():
    old = read_json(PREFIX + 'baseline-v1.json')
    current = gather()
    for key, value in current.items():
        assert old[key] == value, ('baseline changed', key)
    return current


mode = sys.argv[1] if len(sys.argv) == 2 else ''
if mode == 'prepare':
    data = gather()
    checked_labels = labels()
    write_new('baseline-v1.json', {'prepared_at_utc': now(), **data})
    write_new('input-validation-v1.json', {
        'validated_at_utc': now(), 'status': 'PASS administrative only; NOT proof or independent review',
        **checked_labels,
        'protected_fingerprint_occurrences': data['protected_fingerprint_occurrences'],
        'protected_unique_paths': data['protected_unique_paths'],
        'canonical_protected_summary_sha256': data['canonical_protected_summary_sha256'],
        'all_four_accepted_body_suffixes_match': True,
        'older_own_749_paths_bound_transitively': True,
        'mathematical_code_CAS_scan_test_optimizer_author_source_or_old_freezer_replay': False,
        'no_peer_active_review_content_read_or_hashed': True,
    })
    print(json.dumps({'mode': mode, 'UTC': now(), 'labels': checked_labels,
                      'occurrences': data['protected_fingerprint_occurrences'],
                      'paths': data['protected_unique_paths']}))
elif mode == 'freeze':
    data = verified_baseline()
    labels()
    source = read_json(PREFIX + 'sources-v1.json')
    payloads = [fp(PREFIX + suffix) for suffix in PAYLOAD_SUFFIXES]
    write_new('freeze-v1.json', {
        'frozen_at_utc': now(), 'status': 'candidate proof - unverified',
        'claims': ['RD1', 'RD2', 'RD3', 'RD4'], 'whole_obligations': 48,
        'constructor': '/root/review_2022_complexity_r2', 'constructor_excluded': True,
        'root_supplied_NEW_mathematical_inference': False,
        'two_OTHER_initially_blind_ENTIRE_WHOLE_audits_required': True,
        'ENTIRE_main_companions_code_ALLmetadata_model_readback_required_before_handoff': True,
        'separate_postfreeze_verify_required': True,
        'actual_signed_prime_diagonal_p_ge37_only': True,
        'new_trace_degree_all_finite_prime_division_and_real_ramified_parity_proved': True,
        'actual_cofactor_bound_is_proposed_not_independently_reviewed': True,
        'unrestricted_prime_bound_all_generator_or_annual_claim': False,
        'new_2026_distinct_prime_source_is_not_an_operative_import': True,
        'requested_settings': source['requested_settings'],
        'independently_verified_effective_readback': None,
        'authoritative_weekly_telemetry': source['authoritative_weekly_telemetry'],
        'main': fp(PREFIX + 'candidate-v1.md'),
        'compact_necessary_baseline': fp(PREFIX + 'baseline-v1.json'),
        'protected_fingerprint_occurrences': data['protected_fingerprint_occurrences'],
        'protected_unique_paths': data['protected_unique_paths'],
        'canonical_protected_summary_sha256': data['canonical_protected_summary_sha256'],
        'accepted_operative_bindings': data['accepted_operative_bindings'],
        'immediate_own_parent': OWN_PARENT,
        'older_own_paths_bound_transitively': 749,
        'ENTIRE_files_including_freeze': len(payloads) + 1,
        'older_plus_new_own_paths_bound_transitively': 749 + len(payloads) + 1,
        'no_historical_inventory_recopy_or_recursive_replay': True,
        'no_mathematical_program_CAS_scan_test_optimizer_author_source_or_old_freezer_replay': True,
        'no_Git_shared_old_cache_write_download_upload_spawn_charge_contact_bypass': True,
        'no_NEW_peer_active_review_content_used': True,
        'payloads': payloads,
    })
    print(json.dumps({'mode': mode, 'UTC': now(),
                      'freeze': fp(PREFIX + 'freeze-v1.json'),
                      'main': fp(PREFIX + 'candidate-v1.md'),
                      'ENTIRE_files': len(payloads)+1, 'whole_obligations': 48}))
elif mode == 'verify':
    frozen = read_json(PREFIX + 'freeze-v1.json')
    for record in frozen['payloads']:
        check(record)
    data = verified_baseline()
    labels()
    assert frozen['canonical_protected_summary_sha256'] == data['canonical_protected_summary_sha256']
    assert frozen['older_plus_new_own_paths_bound_transitively'] == 760
    print(json.dumps({'mode': mode, 'verified_at_utc': now(),
                      'status': 'PASS SEPARATE read-only metadata verification; NOT proof',
                      'ENTIRE_files': len(frozen['payloads'])+1, 'whole_obligations': 48,
                      'protected_paths': data['protected_unique_paths'],
                      'own_paths_bound_transitively': 760,
                      'freeze': fp(PREFIX + 'freeze-v1.json'),
                      'main': fp(PREFIX + 'candidate-v1.md')}))
else:
    raise SystemExit('Use prepare,freeze,verify. Metadata only; no mathematical evaluation.')
