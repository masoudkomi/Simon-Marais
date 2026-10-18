"""Independent PR11 WHOLE2 documentary guard; no mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sys

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
BASE = 'problems/2017-B4/reviews/reasoning-pressure-return-r11-review-2-'
AUTHOR = 'problems/2017-B4/notes/reasoning-pressure-return-r11-'
PARENT = 'problems/2019-B4/reviews/reasoning-occupation-return-r1-review-2-'
FORBIDDEN = 'problems/2017-B4/reviews/reasoning-pressure-return-r11-review-1-'


def now():
    return datetime.now(timezone.utc).isoformat()


def rec(path):
    assert not path.startswith(FORBIDDEN), 'No corresponding NEW peer access'
    raw = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(raw),
            'sha256': hashlib.sha256(raw).hexdigest()}


def load(path):
    assert not path.startswith(FORBIDDEN)
    return json.loads((ROOT / path).read_text())


def check(rows):
    for row in rows:
        assert rec(row['path']) == {k: row[k] for k in ['path', 'bytes', 'sha256']}, row['path']


def unique(rows):
    result = {}
    for row in rows:
        clean = {k: row[k] for k in ['path', 'bytes', 'sha256']}
        assert row['path'] not in result or result[row['path']] == clean
        result[row['path']] = clean
    return [result[p] for p in sorted(result)]


def summary(rows):
    clean = unique(rows)
    raw = json.dumps(clean, sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(rows), 'unique_paths': len(clean),
            'canonical_deduplicated_sha256': hashlib.sha256(raw).hexdigest()}


def put(suffix, data):
    with (ROOT / (BASE + suffix)).open('x') as stream:
        stream.write(json.dumps(data, indent=2) + '\n')


def protected(baseline):
    check(baseline['direct_records'])
    parent_guard = load(PARENT + 'baseline-v1.json')['records']
    check(parent_guard)
    rows = baseline['direct_records'] + parent_guard
    assert summary(rows) == baseline['effective_guard_summary']
    return rows


mode = sys.argv[1]
if mode == 'prepare':
    assert sorted(p.name for p in (ROOT / 'problems/2017-B4/reviews').glob('reasoning-pressure-return-r11-review-2-*')) == ['reasoning-pressure-return-r11-review-2-admin-v1.py']
    author_identity = {'path': AUTHOR + 'freeze-v1.json', 'bytes': 3407,
        'sha256': '041cd6fa331d5737b71b721247b3d7706ecdf88edd115c7387055b840d0fe5e3'}
    check([author_identity])
    author_rows = load(AUTHOR + 'freeze-v1.json')['payloads'] + [author_identity]
    assert len(author_rows) == 13
    check(author_rows)
    author_guard = load(AUTHOR + 'baseline-v1.json')['records']
    assert len(author_guard) == 28
    # Root expressly confirmed BOTH DR8 release before these guard hashes.
    # These historical bytes are not newly model-read mathematical premises.
    check(author_guard)
    parent_identity = {'path': PARENT + 'manifest-v1.json', 'bytes': 3132,
        'sha256': '5dbc0a5a5f5d56c4a020b0b50d027cbbf38ce8b2f675352a4f3bbd2149a8572b'}
    check([parent_identity])
    parent_rows = load(PARENT + 'manifest-v1.json')['payloads'] + [parent_identity]
    assert len(parent_rows) == 11
    check(parent_rows)
    parent_guard = load(PARENT + 'baseline-v1.json')['records']
    check(parent_guard)
    direct_rows = author_rows + author_guard + parent_rows
    direct = unique(direct_rows)
    all_rows = direct + parent_guard
    put('baseline-v1.json', {
        'prepared_utc': now(), 'status': 'PASS; compact immutable bindings',
        'direct_records': direct, 'direct_summary': summary(direct_rows),
        'effective_guard_summary': summary(all_rows),
        'groups': {'author_ENTIRE': 13, 'author_guard': 28, 'own_AU_parent_ENTIRE': 11,
                   'own_parent_guard_paths_bound_via_frozen_metadata': len(parent_guard)},
        'own_parent_metadata_identity': rec(PARENT + 'baseline-v1.json'),
        'parent_historical_summary': load(PARENT + 'baseline-v1.json')['author_historical_summary_not_expanded'],
        'corresponding_NEW_root_PR11_file_inventory_open_hash_or_findings_access': False,
        'DR8_parent_identities_seen_inside_author_metadata': True,
        'root_explicit_DR8_BOTH_release_confirmed_before_historical_guard_hashes': True,
        'historical_DR8_model_content_not_newly_read_as_mathematics': True,
        'mathematical_program_CAS_scan_test_or_old_code_replay': False})
    print(json.dumps({'mode': mode, 'author_ENTIRE': 13,
                      'direct': summary(direct_rows), 'effective': summary(all_rows)}))
elif mode == 'freeze':
    baseline = load(BASE + 'baseline-v1.json')
    protected(baseline)
    report = (ROOT / (BASE + 'report-v1.md')).read_text()
    labels = [line.split('|')[1].strip() for line in report.splitlines() if line.startswith('| PR11-R2-')]
    assert labels == ['PR11-R2-' + str(i).zfill(2) for i in range(1, 65)]
    paths = sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / 'problems/2017-B4/reviews').glob('reasoning-pressure-return-r11-review-2-*'))
    assert len(paths) == 4
    put('manifest-v1.json', {
        'frozen_utc': now(), 'reviewer': '/root/review_2021_reasoning_j15_r2',
        'role': 'OTHER initially blind ENTIRE WHOLE2', 'whole_obligations': 64,
        'payload_count': 4, 'ENTIRE_files': 5, 'payloads': [rec(p) for p in paths],
        'effective_guard_summary': baseline['effective_guard_summary'],
        'FULL_final_ALL4_payload_model_readback_completed': True,
        'FULL_manifest_model_readback_then_SEPARATE_readonly_verify_REQUIRED': True,
        'corresponding_NEW_root_PR11_finding_file_inventory_hash_metadata_commentary_seen': False,
        'root_counts_times_only_administrative_completion_received': True,
        'historical_DR8_guard_access_after_explicit_BOTH_release': True,
        'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'independent_effective_setting_readback': None,
        'mathematical_program_CAS_scan_test_source_author_old_replay': False,
        'status': 'Independent review recommendation only; coordinator promotion required'})
    print(json.dumps(rec(BASE + 'manifest-v1.json')))
elif mode == 'verify':
    frozen = load(BASE + 'manifest-v1.json')
    check(frozen['payloads'])
    protected(load(BASE + 'baseline-v1.json'))
    print(json.dumps({'SEPARATE_read_only_verify_utc': now(), 'status': 'PASS',
                      'ENTIRE_files': 5, 'all_obligations': 64,
                      'effective_guard_summary': frozen['effective_guard_summary'],
                      'report': rec(BASE + 'report-v1.md'),
                      'manifest': rec(BASE + 'manifest-v1.json')}))
else:
    raise SystemExit('Unknown documentary mode')
