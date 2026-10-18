"""R20 byte/JSON/label administration ONLY. No mathematical execution.

Modes prepare, freeze, verify; writes are restricted to this NEW prefix.
No network, subprocess, CAS, coefficient calculation or directory scan.
Final verify is a separate read-only invocation after full model readback.
"""
from pathlib import Path
import datetime
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
PREFIX = 'problems/2021-B4/notes/reasoning-center-return-r20-'
BASELINE = PREFIX + 'baseline-v1.json'
VALIDATION = PREFIX + 'input-validation-v1.json'
METADATA = PREFIX + 'metadata-v1.json'
FREEZE = PREFIX + 'freeze-v1.json'
STATIC = [PREFIX + name for name in (
    'candidate-v1.md', 'obligations-v1.md', 'checks-v1.md',
    'issues-v1.md', 'failures-v1.md', 'sources-v1.md',
    'sources-v1.json', 'worklog-v1.md', 'administrative-code-v1.py')]
R18 = 'problems/2021-B4/reviews/reasoning-center-return-r18-acceptance.json'
R19 = 'problems/2021-B4/notes/reasoning-center-return-r19-freeze-v1.1.json'
D7 = 'problems/2022-B4/reviews/reasoning-dynamics-return-r7-review-2-manifest-v1.json'

def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def fp(path):
    blob = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(blob),
            'sha256': hashlib.sha256(blob).hexdigest()}

def read(path):
    return json.loads((ROOT / path).read_text())

def put(path, value):
    assert path.startswith(PREFIX)
    with (ROOT / path).open('x') as stream:
        json.dump(value, stream, indent=2)
        stream.write('\n')

def check(record):
    actual = fp(record['path'])
    assert actual['bytes'] == record['bytes'], actual
    assert actual['sha256'] == record['sha256'], actual
    return actual

def canonical(records):
    by_path = {}
    for record in records:
        old = by_path.setdefault(record['path'], record)
        assert old == record
    unique = [by_path[path] for path in sorted(by_path)]
    encoded = json.dumps(unique, sort_keys=True, separators=(',', ':')).encode()
    return unique, hashlib.sha256(encoded).hexdigest()

def labels():
    wanted = {f'R20-{n:02d}' for n in range(1, 49)}
    for path in STATIC[1:3]:
        found = re.findall(r'^\|(R20-\d\d)\|', (ROOT / path).read_text(), re.M)
        assert len(found) == 48 and set(found) == wanted
    return {'whole_obligations': 48, 'constructor_check_rows': 48}

def parents():
    fixed = [
        {'path': 'problems/2021-B4/proofs/reviewed-reasoning-center-return-r18-v1.1.md',
         'bytes': 26067, 'sha256': 'f26de3a17895354408e514d6a0b0066715a1c0f0234d494fd53485ea3feb8284'},
        {'path': R19, 'bytes': 4753,
         'sha256': '1b86a88b22a1cf755836900d314e26b7ac109f83e3031b03254a78a3d36f49fd'},
        {'path': D7, 'bytes': 3846,
         'sha256': '76b2f9a9dceb9423d5b20378a20eb8715df0d2fc5f23b0e0606883a35ae578ab'}]
    checked = [check(record) for record in fixed]
    checked += [fp(R18), fp('problems/2021-B4/reviews/reasoning-center-return-r18-acceptance.md'),
                fp('problems/2021-B4/statement.md'), fp('AGENTS.md')]
    r18, r19, d7 = read(R18), read(R19), read(D7)
    declared = [r18['candidate'], r18['accepted_copy']]
    declared += r18['verification_metadata'] + r19['payloads'] + d7['payloads']
    checked += [check(record) for record in declared]
    unique, digest = canonical(checked)
    summaries = [
        {'metadata': fp(R18), 'historical_occurrences': r18['record_occurrences_verified'],
         'historical_unique_paths': r18['unique_paths_verified'],
         'current_direct_declared_records_checked': 2 + len(r18['verification_metadata']),
         'role': 'operative accepted R18; old historic inventory retained by immutable binding'},
        {'metadata': fp(R19), 'historical_occurrences': r19['protected_current_occurrences'],
         'historical_unique_paths': r19['protected_current_unique_paths'],
         'current_direct_payload_records_checked': len(r19['payloads']),
         'role': 'own frozen repair parent, historically unverified; acceptance later reported only; NOT a mathematical premise; no NEW affected review access'},
        {'metadata': fp(D7), 'historical_occurrences': d7['protected_occurrences'],
         'historical_unique_paths': d7['protected_unique_paths'],
         'current_direct_payload_records_checked': len(d7['payloads']),
         'role': 'immediately preceding own immutable review; administrative parent only'}]
    return checked, unique, digest, summaries

def guard(baseline):
    for record in baseline['protected']:
        check(record)
    _, digest = canonical(baseline['protected'])
    assert digest == baseline['canonical_deduplicated_sha256']
    return len(baseline['protected'])

mode = sys.argv[1]
if mode == 'prepare':
    for path in (BASELINE, VALIDATION, METADATA, FREEZE):
        assert not (ROOT / path).exists(), path
    rows = labels()
    occurrences, unique, digest, summaries = parents()
    put(BASELINE, {
        'captured_at_utc': utc(), 'status': 'candidate proof - unverified',
        'scope': 'compact immutable parents and currently needed direct declarations only',
        'parent_bindings': summaries,
        'verified_record_occurrences': len(occurrences), 'unique_paths': len(unique),
        'canonical_deduplicated_sha256': digest, 'protected': unique,
        'historical_mutable_research_map_reasserted_unchanged': False,
        'NEW_R19_affected_or_2019_AT_peer_material_opened': False})
    put(VALIDATION, {
        'checked_at_utc': utc(), 'PASS': True, **rows,
        'verified_record_occurrences': len(occurrences), 'unique_paths': len(unique),
        'canonical_deduplicated_sha256': digest,
        'mathematical_computation': False,
        'parent_metadata_binding_is_fresh_whole_historical_math_reading': False,
        'only_assigned_NEW_prefix_written': True})
    print(json.dumps({'prepare': 'PASS', **rows, 'occurrences': len(occurrences),
                      'unique_paths': len(unique), 'baseline': fp(BASELINE),
                      'validation': fp(VALIDATION)}))
elif mode == 'freeze':
    baseline = read(BASELINE)
    guard(baseline)
    rows = labels()
    assert not (ROOT / METADATA).exists() and not (ROOT / FREEZE).exists()
    put(METADATA, {
        'created_at_utc': utc(), 'status': 'candidate proof - unverified',
        'constructor': '/root/review_2021_reasoning_j15_r2', 'constructor_excluded': True,
        'two_OTHER_initially_blind_ENTIRE_WHOLE_audits_required': True,
        'whole_obligations': 48, 'payload_files': 12, 'ENTIRE_files': 13,
        'requested_settings': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'independent_effective_readback': None,
        'mathematical_code_CAS_scan_author_source_old_replay': False,
        'NEW_R19_affected_review_or_corresponding_2019_AT_peer_access': False,
        'root_supplied_NEW_R20_inference': False,
        'operative_accepted_input': fp('problems/2021-B4/proofs/reviewed-reasoning-center-return-r18-v1.1.md'),
        'compact_baseline': fp(BASELINE),
        'FULL_final_ALL13_file_model_readback_and_SEPARATE_verify_required_before_handoff': True,
        'quota': {'own_latest_authoritative_total_used_percent': 45,
                  'root_later_reported_total_used_percent': 46, 'reset': 1792874445,
                  'ceiling_total_percent': 90, 'integration_reserve': True,
                  'automatic_later_window_spend_authorized': False}})
    payloads = [fp(path) for path in STATIC + [BASELINE, VALIDATION, METADATA]]
    put(FREEZE, {
        'frozen_at_utc': utc(), 'status': 'candidate proof - unverified',
        'claims': ['R20A', 'R20B'], **rows,
        'constructor_excluded': True, 'two_OTHER_whole_audits_required': True,
        'payload_files': len(payloads), 'ENTIRE_files': len(payloads) + 1,
        'compact_baseline': fp(BASELINE),
        'verified_input_record_occurrences': baseline['verified_record_occurrences'],
        'verified_unique_paths': baseline['unique_paths'],
        'canonical_deduplicated_sha256': baseline['canonical_deduplicated_sha256'],
        'FULL_final_ALL_file_model_readback_and_SEPARATE_readonly_verify_required_before_handoff': True,
        'mathematical_program_CAS_scan_replay': False, 'payloads': payloads})
    print(json.dumps({'freeze': 'created; FULL final readback and separate verify still required',
                      'manifest': fp(FREEZE), 'main': fp(STATIC[0]),
                      'ENTIRE_files': len(payloads) + 1, **rows}))
elif mode == 'verify':
    baseline, manifest = read(BASELINE), read(FREEZE)
    count = guard(baseline)
    for record in manifest['payloads']:
        check(record)
    rows = labels()
    assert manifest['payload_files'] == 12 and manifest['ENTIRE_files'] == 13
    assert len(manifest['payloads']) == 12
    print(json.dumps({'SEPARATE_readonly_verify_at_utc': utc(), 'PASS': True,
                      **rows, 'protected_unique_paths': count,
                      'input_record_occurrences': baseline['verified_record_occurrences'],
                      'ENTIRE_files': manifest['ENTIRE_files'],
                      'manifest': fp(FREEZE), 'main': fp(STATIC[0]),
                      'mathematical_execution': False}))
else:
    raise SystemExit('prepare, freeze or verify only')
