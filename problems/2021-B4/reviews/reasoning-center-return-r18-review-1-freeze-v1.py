"""NEW R18 review metadata only. Never evaluates mathematical statements."""
import datetime
import hashlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PREFIX = 'problems/2021-B4/reviews/reasoning-center-return-r18-review-1-'
AUTHOR_PREFIX = 'problems/2021-B4/notes/reasoning-center-return-r18-'
AUTHOR_FREEZE = {
    'path': AUTHOR_PREFIX + 'freeze-v1.json', 'bytes': 8034,
    'sha256': '14a572167f6ea76658d87a61c951b94f111adc437555f7388b7b0cf47b2829be',
}
AUTHOR_MAIN = {
    'path': AUTHOR_PREFIX + 'candidate-v1.md', 'bytes': 21624,
    'sha256': 'a8b25286023c0d04fd1ff3060062a33f9076cba72f9811425ef30dea054194c5',
}
OWN_PARENT = {
    'path': 'problems/2019-B4/reviews/reasoning-cut-transfer-r4-review-1-manifest-v1.json',
    'bytes': 7145,
    'sha256': '92e7872c0aa8af19e662b6b20c3ad7f044e5413f75ee038cc672285438df1af2',
}
AUTHORITIES = [
    'problems/2021-B4/reviews/reasoning-center-return-r17-acceptance.json',
    'problems/2021-B4/reviews/reasoning-return-r8-acceptance.json',
    'problems/2021-B4/reviews/reasoning-return-r5-acceptance.json',
]
FORBIDDEN = [
    'problems/2021-B4/reviews/reasoning-center-return-r18-review-2-',
    'problems/2020-B4/reviews/reasoning-arithmetic-return-r13-review-',
    'problems/2025-B4/reviews/reasoning-branch-return-r4-review-',
]
PAYLOAD_SUFFIXES = [
    'initial-v1.md', 'ledger-v1.md', 'issues-v1.md',
    'source-checks-v1.md', 'sources-v1.json', 'worklog-v1.md',
    'freeze-v1.py', 'baseline-v1.json', 'input-validation-v1.json',
]
TELEMETRY = {
    'observed_at_utc': '2026-10-18 12:13:38 UTC',
    'method': 'direct clock/get_usage_limits same awaited batch',
    'TOTAL_used_percent': 33, 'window_minutes': 10080,
    'reset_unix': 1792874445, 'ordinary_usage_allowed': True,
    'legacy_by_limit_agree': True, 'account_label': '029a8928...1334ac3a',
    'human_authorized_current_window_only': True,
    'TOTAL_ceiling_percent': 90, 'integration_reserve': True,
    'automatic_later_window_spending': False,
}


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def safe_path(name):
    assert isinstance(name, str) and not pathlib.Path(name).is_absolute()
    assert '..' not in pathlib.Path(name).parts
    assert not any(token in name for token in FORBIDDEN), ('forbidden peer', name)
    return ROOT / name


def fingerprint(name):
    data = safe_path(name).read_bytes()
    return {'path': name, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def check(record):
    actual = fingerprint(record['path'])
    expected = {key: record[key] for key in ('path', 'bytes', 'sha256')}
    assert actual == expected, ('changed fingerprint', record['path'])
    return actual


def read_json(name):
    return json.loads(safe_path(name).read_text())


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()


def write_new(suffix, obj):
    name = PREFIX + suffix
    assert name.startswith(PREFIX)
    with safe_path(name).open('x') as stream:
        json.dump(obj, stream, indent=2, ensure_ascii=False)
        stream.write('\n')


def gather():
    check(AUTHOR_FREEZE)
    check(AUTHOR_MAIN)
    author = read_json(AUTHOR_FREEZE['path'])
    assert author['whole_obligations'] == 64 and len(author['payloads']) == 13
    records = [AUTHOR_FREEZE]
    records.extend(author['payloads'])
    records.extend(author['protected_direct_inputs'])
    check(OWN_PARENT)
    parent = read_json(OWN_PARENT['path'])
    assert parent['older_plus_new_own_paths_bound_transitively'] == 739
    records.append(OWN_PARENT)
    records.extend(parent['artifacts'])
    accepted_bindings = []
    for name in AUTHORITIES:
        authority = read_json(name)
        candidate = check(authority['candidate'])
        body = check(authority['accepted_copy'])
        assert safe_path(body['path']).read_bytes().endswith(
            safe_path(candidate['path']).read_bytes()), ('accepted suffix', name)
        records.append(candidate)
        accepted_bindings.append({
            'authority': fingerprint(name), 'accepted_body': body,
            'candidate_suffix': candidate,
            'historical_record_occurrences_bound_not_replayed': authority.get('record_occurrences_verified'),
            'historical_unique_paths_bound_not_replayed': authority.get('unique_paths_verified'),
        })
    checked = [check(record) for record in records]
    unique = {}
    for record in checked:
        if record['path'] in unique:
            assert unique[record['path']] == record
        unique[record['path']] = record
    ordered = [unique[name] for name in sorted(unique)]
    return {
        'protected_inputs': ordered,
        'protected_fingerprint_occurrences': len(checked),
        'protected_unique_paths': len(ordered),
        'canonical_protected_summary_sha256': hashlib.sha256(canonical(ordered)).hexdigest(),
        'author_main': AUTHOR_MAIN, 'author_freeze': AUTHOR_FREEZE,
        'author_parent_historical_occurrences_bound_not_replayed': author['current_declared_fingerprint_occurrences_verified'],
        'author_parent_historical_paths_bound_not_replayed': author['current_deduplicated_paths_verified'],
        'accepted_operative_bindings': accepted_bindings,
        'immediate_own_parent': OWN_PARENT,
        'older_own_paths_bound_transitively': 739,
        'new_review_files_including_manifest': len(PAYLOAD_SUFFIXES) + 1,
        'older_plus_new_own_paths_bound_transitively': 739 + len(PAYLOAD_SUFFIXES) + 1,
        'no_historical_inventory_recopy_or_recursive_replay': True,
    }


def labels():
    author = safe_path(AUTHOR_PREFIX + 'obligations-v1.md').read_text()
    reviewer = safe_path(PREFIX + 'ledger-v1.md').read_text()
    expected = [f'{i:02}' for i in range(1, 65)]
    assert re.findall(r'^\|(\d{2})\|', author, re.M) == expected
    assert re.findall(r'^\|(\d{2})\|', reviewer, re.M) == expected
    return {'author_labels': 64, 'reviewer_dispositions': 64, 'consecutive': True}


def baseline_verified():
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
        'validated_at_utc': now(), 'status': 'PASS administrative only; not proof',
        **checked_labels,
        'protected_fingerprint_occurrences': data['protected_fingerprint_occurrences'],
        'protected_unique_paths': data['protected_unique_paths'],
        'canonical_protected_summary_sha256': data['canonical_protected_summary_sha256'],
        'accepted_R17_R8_R5_suffixes_match': True,
        'old_own_739_paths_bound_transitively_not_recopied': True,
        'corresponding_NEW_root_R18_peer_material_read_or_hashed': False,
        'no_mathematical_code_scan_CAS_test_author_source_or_old_freezer_replay': True,
    })
    print(json.dumps({'mode': mode, 'UTC': now(), 'labels': checked_labels,
                      'occurrences': data['protected_fingerprint_occurrences'],
                      'paths': data['protected_unique_paths']}))
elif mode == 'freeze':
    data = baseline_verified()
    labels()
    artifacts = [fingerprint(PREFIX + suffix) for suffix in PAYLOAD_SUFFIXES]
    write_new('manifest-v1.json', {
        'frozen_at_utc': now(),
        'status': 'ENTIRE initially blind OTHER WHOLE review1; not coordinator acceptance',
        'claims': ['R18A', 'R18B', 'R18C'], 'whole_obligations': 64,
        'ENTIRE_report_ALL64_ledger_issues_sources_log_code_ALLmetadata_frozen': True,
        'reviewer': '/root/review_2022_complexity_r2',
        'requested_settings': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'independently_verified_effective_readback': None,
        'sole_NEW_constructor': '/root/review_2021_reasoning_j15_r2',
        'constructor_excluded': True,
        'root_supplied_NEW_inference': False,
        'reviewer_constructed_or_supplied_NEW_inference': False,
        'older_roles_disclosed_not_fresh_self_recertification': True,
        'corresponding_NEW_root_R18_peer_material_read_or_hashed': False,
        'new_2020_R13_peer_material_read_or_hashed': False,
        'initial_handoff_IDENTITY_ONLY_until_BOTH_ENTIRE_freezes_confirmed': True,
        'review_finding': {'substantive_defects': 0, 'required_author_repairs': 0,
                           'unresolved_issues': 0, 'closed_scope_notes': 8},
        'depth_one_frames_rational_lift_full_m4_m3_degree20_annual_or_novelty_claim': False,
        'author_main': data['author_main'], 'author_freeze': data['author_freeze'],
        'compact_necessary_baseline': fingerprint(PREFIX + 'baseline-v1.json'),
        'protected_fingerprint_occurrences': data['protected_fingerprint_occurrences'],
        'protected_unique_paths': data['protected_unique_paths'],
        'canonical_protected_summary_sha256': data['canonical_protected_summary_sha256'],
        'accepted_operative_bindings': data['accepted_operative_bindings'],
        'immediate_own_parent': OWN_PARENT,
        'older_own_paths_bound_transitively': 739,
        'new_review_files_including_manifest': len(artifacts) + 1,
        'older_plus_new_own_paths_bound_transitively': 739 + len(artifacts) + 1,
        'no_historical_inventory_recopy_or_recursive_replay': True,
        'no_math_code_scan_CAS_test_optimizer_author_source_or_old_freezer_replay': True,
        'no_old_shared_Git_cache_mutation_spawn_download_charge_contact_or_bypass': True,
        'authoritative_weekly_telemetry': TELEMETRY,
        'artifacts': artifacts,
    })
    print(json.dumps({'mode': mode, 'UTC': now(),
                      'manifest': fingerprint(PREFIX + 'manifest-v1.json'),
                      'report': fingerprint(PREFIX + 'initial-v1.md'),
                      'files_including_manifest': len(artifacts) + 1}))
elif mode == 'verify':
    manifest = read_json(PREFIX + 'manifest-v1.json')
    for record in manifest['artifacts']:
        check(record)
    data = baseline_verified()
    labels()
    assert data['canonical_protected_summary_sha256'] == manifest['canonical_protected_summary_sha256']
    assert manifest['older_plus_new_own_paths_bound_transitively'] == 749
    print(json.dumps({'mode': mode, 'verified_at_utc': now(),
                      'status': 'PASS separate read-only integrity verification; not proof',
                      'entire_files': len(manifest['artifacts']) + 1,
                      'whole_obligations': 64,
                      'protected_paths': data['protected_unique_paths'],
                      'own_paths_bound_transitively': 749,
                      'manifest': fingerprint(PREFIX + 'manifest-v1.json'),
                      'report': fingerprint(PREFIX + 'initial-v1.md')}))
else:
    raise SystemExit('Use prepare, freeze or verify. Metadata only; no mathematical evaluation.')
