"""R21 documentary integrity only. No polynomial arithmetic or search."""
from pathlib import Path
import datetime, hashlib, json, sys

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PREFIX = 'problems/2021-B4/notes/reasoning-center-return-r21-'

def stamp():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def record(path):
    data = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def save(suffix, data):
    path = ROOT / (PREFIX + suffix)
    if path.exists():
        raise SystemExit('Refusing overwrite: ' + str(path))
    path.write_text(json.dumps(data, indent=2) + '\n')

def verify(rows):
    failures = []
    for row in rows:
        actual = record(row['path'])
        if actual != row:
            failures.append({'expected': row, 'actual': actual})
    if failures:
        raise SystemExit(json.dumps(failures, indent=2))

def parent_rows():
    paths = [
        'AGENTS.md', 'problems/2021-B4/statement.md',
        'problems/2021-B4/notes/coordinator-frame-III-exploration-r1.md',
        'problems/2021-B4/reviews/reasoning-center-return-r18-acceptance.md',
        'problems/2021-B4/reviews/reasoning-center-return-r18-acceptance.json',
        'problems/2021-B4/reviews/reasoning-center-return-r20-acceptance.md',
        'problems/2021-B4/reviews/reasoning-center-return-r20-acceptance.json',
    ]
    rows = [record(p) for p in paths]
    parent_counts = []
    for label in ['r18', 'r20']:
        path = 'problems/2021-B4/reviews/reasoning-center-return-' + label + '-acceptance.json'
        obj = json.loads((ROOT / path).read_text())
        declared = [obj['candidate'], obj['accepted_copy']] + obj['verification_metadata']
        verify(declared)
        rows.extend(declared)
        parent_counts.append({
            'authority': path,
            'direct_declared_fingerprints_checked_now': len(declared),
            'historical_occurrences_recorded_by_authority': obj['record_occurrences_verified'],
            'historical_paths_recorded_by_authority': obj['unique_paths_verified'],
            'historical_ancestry_not_recopied_or_claimed_freshly_reconstructed': True,
        })
    return rows, parent_counts

mode = sys.argv[1]
if mode == 'prepare':
    other = [p for p in (ROOT / 'problems/2021-B4/notes').glob('reasoning-center-return-r21-*') if p.name != 'reasoning-center-return-r21-admin-v1.py']
    if other:
        raise SystemExit('Prefix not unused: ' + repr(other))
    rows, parents = parent_rows()
    unique = {r['path']: r for r in rows}
    save('baseline-v1.json', {'prepared_utc': stamp(), 'occurrences': len(rows), 'unique_paths': len(unique), 'rows': rows, 'compact_parent_bindings': parents, 'no_mutable_research_map_protection_claim': True})
    save('input-validation-v1.json', {'checked_utc': stamp(), 'status': 'PASS', 'occurrences': len(rows), 'unique_paths': len(unique), 'scope': 'Direct current authority fingerprints and explicit frozen parent metadata only; no ancestry inflation.'})
    print(json.dumps({'mode': mode, 'occurrences': len(rows), 'unique_paths': len(unique), 'status': 'PASS'}))
elif mode == 'freeze':
    baseline = json.loads((ROOT / (PREFIX + 'baseline-v1.json')).read_text())
    verify(baseline['rows'])
    obligations = (ROOT / (PREFIX + 'obligations-v1.md')).read_text()
    labels = [line.split('|')[1].strip() for line in obligations.splitlines() if line.startswith('| R21-')]
    expected = ['R21-' + str(i).zfill(2) for i in range(1, 49)]
    if labels != expected:
        raise SystemExit('Documentary obligation labels incomplete')
    paths = sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / 'problems/2021-B4/notes').glob('reasoning-center-return-r21-*'))
    if len(paths) != 14:
        raise SystemExit('Expected 14 payloads: ' + repr(paths))
    payloads = [record(p) for p in paths]
    save('freeze-v1.json', {
        'frozen_utc': stamp(), 'status': 'candidate proof - unverified; complete research/failure checkpoint, no actual-frame exclusion',
        'constructor': '/root/review_2021_reasoning_j15_r2', 'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True}, 'independent_effective_readback': None,
        'payload_count': len(payloads), 'entire_file_count_including_manifest': len(payloads) + 1, 'obligations': len(labels), 'payloads': payloads,
        'parent_baseline': record(PREFIX + 'baseline-v1.json'), 'protected_occurrences': baseline['occurrences'], 'protected_unique_paths': baseline['unique_paths'],
        'mathematical_program_or_scan': False, 'two_OTHER_whole_audits_required_before_any_promotion': True,
        'constructor_and_root_excluded_if_coordinator_exploration_used': True,
        'final_model_readback_and_separate_verify_are_later_explicit_events_not_assumed_here': True,
    })
    print(json.dumps(record(PREFIX + 'freeze-v1.json')))
elif mode == 'verify':
    manifest = json.loads((ROOT / (PREFIX + 'freeze-v1.json')).read_text())
    baseline = json.loads((ROOT / (PREFIX + 'baseline-v1.json')).read_text())
    verify(manifest['payloads'])
    verify(baseline['rows'])
    verify([manifest['parent_baseline']])
    print(json.dumps({'separate_read_only_verify_utc': stamp(), 'status': 'PASS', 'entire_files': manifest['entire_file_count_including_manifest'], 'obligations': manifest['obligations'], 'protected_occurrences': len(baseline['rows']), 'protected_unique_paths': len({r['path'] for r in baseline['rows']}), 'manifest': record(PREFIX + 'freeze-v1.json')}))
else:
    raise SystemExit('Unknown mode')
