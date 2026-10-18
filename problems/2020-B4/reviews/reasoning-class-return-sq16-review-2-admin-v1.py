"""Independent SQ16 WHOLE2 documentary integrity only; no mathematical code."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
BASE = 'problems/2020-B4/reviews/reasoning-class-return-sq16-review-2-'
AUTHOR = 'problems/2020-B4/notes/reasoning-class-return-sq16-'
PARENT = 'problems/2019-B4/notes/reasoning-area-return-r2-'
PR_PARENT = 'problems/2017-B4/reviews/reasoning-pressure-return-r11-review-2-'
AU_PARENT = 'problems/2019-B4/reviews/reasoning-occupation-return-r1-review-2-'
FORBIDDEN = ('problems/2020-B4/reviews/reasoning-class-return-sq16-review-1-',
             'problems/2020-B4/reviews/reasoning-class-return-sq17-review-1-',
             'problems/2021-B4/reviews/reasoning-center-return-r21-')


def now():
    return datetime.now(timezone.utc).isoformat()


def rec(path):
    assert not path.startswith(FORBIDDEN), 'Embargoed new peer material'
    raw = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}


def load(path):
    assert not path.startswith(FORBIDDEN)
    return json.loads((ROOT / path).read_text())


def check(rows):
    for row in rows:
        assert rec(row['path']) == {k: row[k] for k in ('path', 'bytes', 'sha256')}, row['path']


def unique(rows):
    result = {}
    for row in rows:
        clean = {k: row[k] for k in ('path', 'bytes', 'sha256')}
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


def inherited_guards():
    pr = load(PR_PARENT + 'baseline-v1.json')
    old = pr['direct_records'] + load(AU_PARENT + 'baseline-v1.json')['records']
    check(old)
    assert summary(old) == pr['effective_guard_summary']
    parent = load(PARENT + 'baseline-v1.json')
    check(parent['direct_records'])
    rows = parent['direct_records'] + old
    assert summary(rows) == parent['effective_guard_summary']
    return rows


def protected(baseline):
    check(baseline['direct_records'])
    old = inherited_guards()
    rows = baseline['direct_records'] + old
    assert summary(rows) == baseline['effective_guard_summary']


mode = sys.argv[1]
if mode == 'prepare':
    own = sorted(p.name for p in (ROOT / 'problems/2020-B4/reviews').glob('reasoning-class-return-sq16-review-2-*'))
    assert own == ['reasoning-class-return-sq16-review-2-admin-v1.py'], own
    author_id = {'path': AUTHOR + 'freeze-v1.json', 'bytes': 4322,
                 'sha256': '29ed9edd4cea75a4248b9661f06518649c97e122c437262c4c7dd32750847087'}
    parent_id = {'path': PARENT + 'freeze-v1.json', 'bytes': 3299,
                 'sha256': '4aac68a1c6a818030c70066019828eee565d60bffdacb14487dd9e9c972f346d'}
    check([author_id, parent_id])
    author_rows = load(AUTHOR + 'freeze-v1.json')['payloads'] + [author_id]
    assert len(author_rows) == 12
    check(author_rows)
    author_guard = load(AUTHOR + 'baseline-v1.json')['records']
    check(author_guard)
    parent_rows = load(PARENT + 'freeze-v1.json')['payloads'] + [parent_id]
    assert len(parent_rows) == 11
    check(parent_rows)
    authority_rows = []
    for stem in ['reasoning-arithmetic-return-r14-repair-v1.1', 'reasoning-class-return-sq15']:
        ap = 'problems/2020-B4/reviews/' + stem + '-acceptance.json'
        obj = load(ap)
        rows = [obj['candidate'], obj['accepted_copy']] + obj['verification_metadata']
        check(rows)
        authority_rows += rows + [rec(ap), rec(ap[:-5] + '.md')]
    direct = unique(author_rows + author_guard + parent_rows + authority_rows)
    old = inherited_guards()
    put('baseline-v1.json', {
        'prepared_utc': now(), 'status': 'PASS; compact immutable bindings',
        'direct_records': direct,
        'direct_summary': summary(author_rows + author_guard + parent_rows + authority_rows),
        'effective_guard_summary': summary(direct + old),
        'groups': {'author_ENTIRE': 12, 'author_immediate_guards': len(author_guard),
                   'own_AR_parent_ENTIRE': 11, 'authority_occurrences': len(authority_rows)},
        'own_parent_guard_metadata_identity': rec(PARENT + 'baseline-v1.json'),
        'own_parent_guard_summary_bound_not_recopied': load(PARENT + 'baseline-v1.json')['effective_guard_summary'],
        'historical_author_D9_parent_metadata_not_a_fresh_mathematical_read': True,
        'corresponding_NEW_root_SQ16_finding_file_inventory_hash_metadata_commentary_seen': False,
        'SQ16_peer_completion_count_time_only_admin_received': True,
        'old_SQ15_diagnostic_authorship_not_NEW_SQ16_contribution': True,
        'mathematical_program_CAS_scan_test_or_old_replay': False})
    print(json.dumps({'mode': mode, 'author_ENTIRE': 12, 'direct': summary(direct),
                      'effective': summary(direct + old)}))
elif mode == 'freeze':
    baseline = load(BASE + 'baseline-v1.json')
    protected(baseline)
    report = (ROOT / (BASE + 'report-v1.md')).read_text()
    labels = [line.split('|')[1].strip() for line in report.splitlines()
              if re.match(r'^\| SQ16-R2-\d{2} \|', line)]
    assert labels == ['SQ16-R2-' + str(i).zfill(2) for i in range(1, 49)]
    paths = sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / 'problems/2020-B4/reviews').glob('reasoning-class-return-sq16-review-2-*'))
    assert len(paths) == 4, paths
    put('manifest-v1.json', {
        'frozen_utc': now(), 'reviewer': '/root/review_2021_reasoning_j15_r2',
        'role': 'OTHER initially blind ENTIRE WHOLE2', 'whole_obligations': 48,
        'payload_count': 4, 'ENTIRE_files': 5, 'payloads': [rec(p) for p in paths],
        'effective_guard_summary': baseline['effective_guard_summary'],
        'FULL_final_ALL4_payload_model_readback_completed': True,
        'FULL_manifest_model_readback_then_SEPARATE_readonly_verify_REQUIRED': True,
        'corresponding_NEW_root_SQ16_finding_file_inventory_hash_metadata_commentary_seen': False,
        'peer_count_time_only_administrative_completion_received': True,
        'new_SQ16_constructive_contribution': False,
        'old_SQ15_diagnostic_role_disclosed': True,
        'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'independent_effective_setting_readback': None,
        'mathematical_program_CAS_scan_test_source_author_old_replay': False,
        'status': 'Independent review recommendation only; root reconciliation and promotion required'})
    print(json.dumps(rec(BASE + 'manifest-v1.json')))
elif mode == 'verify':
    frozen = load(BASE + 'manifest-v1.json')
    check(frozen['payloads'])
    protected(load(BASE + 'baseline-v1.json'))
    print(json.dumps({'SEPARATE_read_only_verify_utc': now(), 'status': 'PASS',
                      'ENTIRE_files': 5, 'whole_obligations': 48,
                      'effective_guard_summary': frozen['effective_guard_summary'],
                      'report': rec(BASE + 'report-v1.md'),
                      'manifest': rec(BASE + 'manifest-v1.json')}))
else:
    raise SystemExit('Unknown documentary mode')
