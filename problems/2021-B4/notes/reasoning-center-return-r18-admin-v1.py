"""R18 metadata ONLY: no mathematical coefficient/table evaluation."""
import datetime
import hashlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path('/Users/uqmkamga/Documents/ChatGPT/Website')
STEM = 'problems/2021-B4/notes/reasoning-center-return-r18-'
DIRECT = [
    'AGENTS.md', 'problems/2021-B4/statement.md',
    'problems/2021-B4/proofs/reviewed-reasoning-center-return-r17-v1.1.md',
    'problems/2021-B4/reviews/reasoning-center-return-r17-acceptance.md',
    'problems/2021-B4/reviews/reasoning-center-return-r17-acceptance.json',
    'problems/2021-B4/proofs/reviewed-reasoning-return-r8-v1.1.md',
    'problems/2021-B4/reviews/reasoning-return-r8-acceptance.md',
    'problems/2021-B4/reviews/reasoning-return-r8-acceptance.json',
    'problems/2021-B4/proofs/reviewed-reasoning-return-r5-v1.1.md',
    'problems/2021-B4/reviews/reasoning-return-r5-acceptance.md',
    'problems/2021-B4/reviews/reasoning-return-r5-acceptance.json',
    'problems/2021-B4/reviews/reasoning-center-return-r17-review-2-manifest-v1.json',
    'problems/2021-B4/reviews/reasoning-center-return-r17-review-2-sources-v1.json',
]
PAYLOAD_SUFFIXES = [
    'candidate-v1.md', 'working-v1.md', 'obligations-v1.md', 'checks-v1.md',
    'failures-v1.md', 'sources-v1.md', 'sources-v1.json', 'log-v1.md',
    'code-log-v1.md', 'admin-v1.py', 'baseline-v1.json',
    'input-validation-v1.json', 'metadata-v1.json',
]

def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()

def fp(path):
    p = pathlib.Path(path)
    if p.is_absolute():
        p = p.relative_to(ROOT)
    name = p.as_posix()
    data = (ROOT / p).read_bytes()
    return {'path': name, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def check(record):
    got = fp(record['path'])
    assert got['bytes'] == record['bytes'], ('bytes', record['path'])
    assert got['sha256'] == record['sha256'], ('sha256', record['path'])
    return got

def records(obj):
    if isinstance(obj, dict):
        if ('path' in obj and 'bytes' in obj and 'sha256' in obj
                and isinstance(obj['path'], str)
                and isinstance(obj['bytes'], int)
                and isinstance(obj['sha256'], str)
                and re.fullmatch(r'[0-9a-f]{64}', obj['sha256'])):
            yield {k: obj[k] for k in ('path', 'bytes', 'sha256')}
        for value in obj.values():
            yield from records(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from records(value)

def gather():
    direct = [fp(name) for name in DIRECT]
    occurrences = list(direct)
    parents = []
    for name in DIRECT:
        if not name.endswith('.json'):
            continue
        obj = json.loads((ROOT / name).read_text())
        declared = list(records(obj))
        occurrences.extend(declared)
        parents.append({
            **fp(name), 'declared_occurrences_in_this_parent': len(declared),
            'historical_record_occurrences_reported': obj.get('record_occurrences_verified'),
            'historical_unique_paths_reported': obj.get('unique_paths_verified'),
            'historical_parent_not_recursively_copied': True,
        })
        if 'accepted_copy' in obj and 'candidate' in obj:
            accepted = (ROOT / obj['accepted_copy']['path']).read_bytes()
            submitted = (ROOT / obj['candidate']['path']).read_bytes()
            assert accepted.endswith(submitted), ('accepted suffix', name)
    unique = {}
    for record in occurrences:
        checked = check(record)
        if checked['path'] in unique:
            assert checked == unique[checked['path']], ('conflicting record', checked['path'])
        unique[checked['path']] = checked
    ordered = [unique[name] for name in sorted(unique)]
    return {
        'direct_inputs': direct,
        'immutable_parent_bindings': parents,
        'current_declared_fingerprint_occurrences_verified': len(occurrences),
        'current_deduplicated_paths_verified': len(ordered),
        'current_deduplicated_fingerprint_digest_sha256': hashlib.sha256(canonical(ordered)).hexdigest(),
        'compact_rule': 'Direct metadata bound by exact path/bytes/SHA; declared current records verified but not recopied as a growing historical inventory.',
    }

def write_new(suffix, obj):
    path = ROOT / (STEM + suffix)
    with path.open('x') as stream:
        json.dump(obj, stream, indent=2, ensure_ascii=False)
        stream.write('\n')

def verify_baseline():
    expected = json.loads((ROOT / (STEM + 'baseline-v1.json')).read_text())
    actual = gather()
    for key in actual:
        assert actual[key] == expected[key], ('baseline changed', key)
    return actual

mode = sys.argv[1] if len(sys.argv) == 2 else ''
if mode == 'prepare':
    summary = gather()
    text = (ROOT / (STEM + 'obligations-v1.md')).read_text()
    labels = re.findall(r'^\|(\d{2})\|', text, re.M)
    assert labels == [f'{i:02}' for i in range(1, 65)], 'obligation labels'
    write_new('baseline-v1.json', {'prepared_utc': now(), **summary})
    write_new('input-validation-v1.json', {
        'validated_utc': now(), 'status': 'PASS administrative only',
        'whole_obligation_labels': 64, 'all_consecutive': True,
        'direct_inputs': len(DIRECT),
        'current_declared_occurrences': summary['current_declared_fingerprint_occurrences_verified'],
        'current_unique_paths': summary['current_deduplicated_paths_verified'],
        'current_digest': summary['current_deduplicated_fingerprint_digest_sha256'],
        'accepted_R17_R8_R5_suffixes_match': True,
        'no_mathematical_certificate_evaluated': True,
    })
    write_new('metadata-v1.json', {
        'prepared_utc': now(), 'status': 'candidate proof - unverified',
        'constructor': '/root/review_2021_reasoning_j15_r2',
        'claims': ['R18A', 'R18B', 'R18C'], 'whole_obligations': 64,
        'root_supplied_new_proof_inference': False,
        'two_OTHER_initially_blind_ENTIRE_WHOLE_audits_required': True,
        'requested_settings': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'verified_effective_settings': None,
        'mathematical_code_CAS_scan_or_author_rerun': False,
        'all_new_files_within_assigned_prefix': True,
        'no_worker_Git_shared_old_cache_writes_spawn_charge_contact_bypass': True,
        'no_native_mathematical_PID_wait_or_pending_approval': True,
        'future_2020_R13_review_target_or_peer_content_not_opened': True,
        'no_NEW_root_R13_mathematical_conclusion_or_peer_file_hash_metadata_content_seen': True,
        'administrative_R13_identity_messages_only_seen_dates_counts_no_peer_path_hash_or_disposition': True,
        'current_authorized_weekly_reset': 1792874445,
        'TOTAL_ceiling_percent': 90, 'integration_reserve': True,
        'latest_own_telemetry': {'TOTAL_weekly_used_percent': 31, 'UTC': '2026-10-18 11:45:29 UTC'},
        'ENTIRE_model_payload_readback_required_before_freeze': True,
        'separate_postfreeze_verify_required': True,
    })
    print(json.dumps({'mode': mode, 'UTC': now(), 'direct': len(DIRECT),
                      'occurrences': summary['current_declared_fingerprint_occurrences_verified'],
                      'unique_paths': summary['current_deduplicated_paths_verified'],
                      'digest': summary['current_deduplicated_fingerprint_digest_sha256']}))
elif mode == 'freeze':
    summary = verify_baseline()
    payloads = [fp(STEM + suffix) for suffix in PAYLOAD_SUFFIXES]
    manifest = {
        'frozen_utc': now(), 'status': 'candidate proof - unverified',
        'claims': ['R18A', 'R18B', 'R18C'], 'whole_obligations': 64,
        'payload_files': len(payloads), 'ENTIRE_files_including_this_freeze': len(payloads) + 1,
        'ENTIRE_payload_model_readback_complete': True,
        'two_OTHER_initially_blind_ENTIRE_WHOLE_audits_and_root_reconciliation_required': True,
        'root_supplied_new_proof_inference': False,
        'mathematical_executable_CAS_scan_author_or_source_rerun': False,
        'separate_postfreeze_verify_required': True,
        'payloads': payloads,
        'protected_direct_inputs': summary['direct_inputs'],
        'compact_parent_metadata_bindings': summary['immutable_parent_bindings'],
        'current_declared_fingerprint_occurrences_verified': summary['current_declared_fingerprint_occurrences_verified'],
        'current_deduplicated_paths_verified': summary['current_deduplicated_paths_verified'],
        'current_deduplicated_fingerprint_digest_sha256': summary['current_deduplicated_fingerprint_digest_sha256'],
    }
    write_new('freeze-v1.json', manifest)
    print(json.dumps({'mode': mode, 'UTC': now(), 'manifest': fp(STEM + 'freeze-v1.json'),
                      'main': fp(STEM + 'candidate-v1.md'), 'files': len(payloads)+1,
                      'obligations': 64}))
elif mode == 'verify':
    manifest = json.loads((ROOT / (STEM + 'freeze-v1.json')).read_text())
    for record in manifest['payloads'] + manifest['protected_direct_inputs']:
        check(record)
    summary = verify_baseline()
    assert summary['current_deduplicated_fingerprint_digest_sha256'] == manifest['current_deduplicated_fingerprint_digest_sha256']
    print(json.dumps({'mode': mode, 'verified_utc': now(), 'status': 'PASS administrative only',
                      'payloads': len(manifest['payloads']), 'whole_obligations': 64,
                      'protected_unique_paths': summary['current_deduplicated_paths_verified'],
                      'manifest': fp(STEM+'freeze-v1.json'),
                      'main': fp(STEM+'candidate-v1.md')}))
else:
    raise SystemExit('Use prepare, freeze or verify; metadata-only code.')
