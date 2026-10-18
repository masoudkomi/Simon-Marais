"""Independent AU R2 documentary administration; no mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, sys

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PREFIX = 'problems/2019-B4/reviews/reasoning-occupation-return-r1-review-2-'
AUTHOR = 'problems/2019-B4/notes/reasoning-occupation-return-r1-'
PARENT = 'problems/2021-B4/notes/reasoning-center-return-r21-'

def now():
    return datetime.now(timezone.utc).isoformat()

def rec(path):
    raw = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}

def read(path):
    return json.loads((ROOT / path).read_text())

def check(rows):
    for row in rows:
        expected = {k: row[k] for k in ['path', 'bytes', 'sha256']}
        if rec(row['path']) != expected:
            raise SystemExit('Changed protected path: ' + row['path'])

def put(suffix, obj):
    dest = ROOT / (PREFIX + suffix)
    if dest.exists():
        raise SystemExit('Refusing overwrite: ' + str(dest))
    dest.write_text(json.dumps(obj, indent=2) + '\n')

def dedup(rows):
    bypath = {}
    for row in rows:
        reduced = {k: row[k] for k in ['path', 'bytes', 'sha256']}
        if reduced['path'] in bypath and bypath[reduced['path']] != reduced:
            raise SystemExit('Conflicting identity')
        bypath[reduced['path']] = reduced
    return [bypath[p] for p in sorted(bypath)]

mode = sys.argv[1]
if mode == 'prepare':
    existing = [p for p in (ROOT / 'problems/2019-B4/reviews').glob('reasoning-occupation-return-r1-review-2-*') if p.name != 'reasoning-occupation-return-r1-review-2-admin-v1.py']
    if existing:
        raise SystemExit('Assigned prefix already used')
    author_freeze = read(AUTHOR + 'freeze-v1.json')
    expected_author = {'path': AUTHOR + 'freeze-v1.json', 'bytes': 4361, 'sha256': 'e4b6369f4733f2e418ecc43e24329b011aa538799f1afaeb9dcc667abfe75ee9'}
    check([expected_author])
    author_rows = author_freeze['payloads'] + [expected_author]
    check(author_rows)
    guard = read(AUTHOR + 'baseline-v1.json')
    check(guard['exact_guard_records'])
    parent = read(PARENT + 'freeze-v1.json')
    check(parent['payloads'])
    parent_rows = parent['payloads'] + [rec(PARENT + 'freeze-v1.json')]
    parent_guard = read(PARENT + 'baseline-v1.json')['rows']
    check(parent_guard)
    rows = author_rows + guard['exact_guard_records'] + parent_rows + parent_guard
    compact = dedup(rows)
    put('baseline-v1.json', {'prepared_utc': now(), 'occurrences': len(rows), 'unique_paths': len(compact), 'records': compact,
        'groups': {'author_ENTIRE_files': len(author_rows), 'author_direct_guard_paths': len(guard['exact_guard_records']), 'own_immediate_parent_ENTIRE_files': len(parent_rows), 'own_parent_direct_guard_records': len(parent_guard)},
        'author_historical_summary_not_expanded': guard['summary'], 'own_parent_identity': rec(PARENT + 'freeze-v1.json'),
        'NEW_root_AU_peer_file_inventory_hash_access': False, 'root_admin_identity_received_but_not_baseline_premise': True,
        'historical_metadata_binding_is_not_fresh_mathematical_read': True})
    put('input-validation-v1.json', {'checked_utc': now(), 'status': 'PASS', 'occurrences': len(rows), 'unique_paths': len(compact), 'author_ENTIRE_files': len(author_rows), 'no_math_execution': True, 'no_NEW_corresponding_peer_file_access': True})
    print(json.dumps({'mode': mode, 'status': 'PASS', 'occurrences': len(rows), 'unique_paths': len(compact), 'author_ENTIRE_files': len(author_rows)}))
elif mode == 'freeze':
    baseline = read(PREFIX + 'baseline-v1.json')
    check(baseline['records'])
    ledger = (ROOT / (PREFIX + 'ledger-v1.md')).read_text()
    labels = [line.split('|')[1].strip() for line in ledger.splitlines() if line.startswith('| AU-R2-')]
    if labels != ['AU-R2-' + str(i).zfill(2) for i in range(1, 65)]:
        raise SystemExit('Missing documentary ledger labels')
    paths = sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / 'problems/2019-B4/reviews').glob('reasoning-occupation-return-r1-review-2-*'))
    if len(paths) != 10:
        raise SystemExit('Expected10 payloads: ' + repr(paths))
    put('manifest-v1.json', {'frozen_utc': now(), 'reviewer': '/root/review_2021_reasoning_j15_r2', 'role': 'OTHER initially blind ENTIRE WHOLE2', 'obligations': 64,
        'payload_count': len(paths), 'ENTIRE_files_including_manifest': len(paths) + 1, 'payloads': [rec(p) for p in paths],
        'protected_occurrences': baseline['occurrences'], 'protected_unique_paths': baseline['unique_paths'],
        'root_administrative_identity_message_received': True, 'root_AU_mathematical_conclusion_public_status_or_peer_content_seen': False,
        'root_NEW_AU_review_file_inventory_open_or_hash_operation': False, 'peer_admin_identity_not_in_baseline_or_reasoning': True,
        'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True}, 'independent_effective_readback': None,
        'mathematical_program_scan_CAS_or_old_replay': False, 'status': 'independent review recommendation only; coordinator promotion required',
        'FULL_final_payload_model_readback_done': True, 'manifest_model_readback_then_SEPARATE_verify_required': True})
    print(json.dumps(rec(PREFIX + 'manifest-v1.json')))
elif mode == 'verify':
    manifest = read(PREFIX + 'manifest-v1.json')
    check(manifest['payloads'])
    baseline = read(PREFIX + 'baseline-v1.json')
    check(baseline['records'])
    print(json.dumps({'SEPARATE_read_only_verify_utc': now(), 'status': 'PASS', 'ENTIRE_files': manifest['ENTIRE_files_including_manifest'], 'obligations': manifest['obligations'], 'protected_occurrences': baseline['occurrences'], 'protected_unique_paths': baseline['unique_paths'], 'manifest': rec(PREFIX + 'manifest-v1.json')}))
else:
    raise SystemExit('Unknown documentary mode')
