"""SQ17 OTHER WHOLE2 documentary preservation only; no mathematical code."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
BASE = 'problems/2020-B4/reviews/reasoning-class-return-sq17-review-2-'
AUTHOR = 'problems/2020-B4/notes/reasoning-class-return-sq17-'
PARENT = 'problems/2020-B4/reviews/reasoning-class-return-sq16-review-2-'
AR = 'problems/2019-B4/notes/reasoning-area-return-r2-'
PR = 'problems/2017-B4/reviews/reasoning-pressure-return-r11-review-2-'
AU = 'problems/2019-B4/reviews/reasoning-occupation-return-r1-review-2-'
FORBIDDEN = ('problems/2020-B4/reviews/reasoning-class-return-sq17-review-1-',
             'problems/2020-B4/reviews/reasoning-class-return-sq16-review-1-')


def now():
    return datetime.now(timezone.utc).isoformat()


def rec(path):
    assert not path.startswith(FORBIDDEN), 'Embargoed corresponding NEW peer'
    data = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def obj(path):
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


def old_guards():
    pr = obj(PR + 'baseline-v1.json')
    older = pr['direct_records'] + obj(AU + 'baseline-v1.json')['records']
    check(older)
    assert summary(older) == pr['effective_guard_summary']
    ar = obj(AR + 'baseline-v1.json')
    check(ar['direct_records'])
    older = ar['direct_records'] + older
    assert summary(older) == ar['effective_guard_summary']
    parent = obj(PARENT + 'baseline-v1.json')
    check(parent['direct_records'])
    older = parent['direct_records'] + older
    assert summary(older) == parent['effective_guard_summary']
    return older


def protected(baseline):
    check(baseline['direct_records'])
    assert summary(baseline['direct_records'] + old_guards()) == baseline['effective_guard_summary']


mode = sys.argv[1]
if mode == 'prepare':
    own = sorted(p.name for p in (ROOT / 'problems/2020-B4/reviews').glob('reasoning-class-return-sq17-review-2-*'))
    assert own == ['reasoning-class-return-sq17-review-2-admin-v1.py'], own
    author_id = {'path': AUTHOR + 'freeze-v1.json', 'bytes': 3901,
                 'sha256': 'd7b19f6e852178d83db1adad70e2fdb10c8dfa30d28b538e893cf1f0b567aab1'}
    parent_id = {'path': PARENT + 'manifest-v1.json', 'bytes': 1987,
                 'sha256': '1c33d6c4a9cfd3ea84ea836bb179347289debbb5aa2449740de6fe1883ca0b22'}
    check([author_id, parent_id])
    author_rows = obj(AUTHOR + 'freeze-v1.json')['payloads'] + [author_id]
    assert len(author_rows) == 8
    check(author_rows)
    author_guard = obj(AUTHOR + 'baseline-v1.json')['records']
    check(author_guard)
    parent_rows = obj(PARENT + 'manifest-v1.json')['payloads'] + [parent_id]
    assert len(parent_rows) == 5
    check(parent_rows)
    direct = unique(author_rows + author_guard + parent_rows)
    inherited = old_guards()
    put('baseline-v1.json', {
        'prepared_utc': now(), 'direct_records': direct,
        'direct_occurrence_summary': summary(author_rows + author_guard + parent_rows),
        'effective_guard_summary': summary(direct + inherited),
        'groups': {'author_ENTIRE': 8, 'author_immediate_guard_records': len(author_guard),
                   'own_SQ16_parent_ENTIRE': 5},
        'parent_guard_metadata': rec(PARENT + 'baseline-v1.json'),
        'parent_guard_summary_bound_not_recopied': obj(PARENT + 'baseline-v1.json')['effective_guard_summary'],
        'author_R21_manifest_guard_only_not_fresh_mathematical_peer_read': True,
        'NEW_C_SQ17_finding_file_inventory_hash_metadata_commentary_seen': False,
        'root_related_NEW_source_objection_note_opened_inventoried_hashed': False,
        'NEW_root_SQ16_material_seen': False,
        'mathematical_program_CAS_scan_test_source_author_old_replay': False})
    print(json.dumps({'mode': mode, 'author_ENTIRE': 8, 'direct': summary(direct),
                      'effective': summary(direct + inherited)}))
elif mode == 'freeze':
    baseline = obj(BASE + 'baseline-v1.json')
    protected(baseline)
    report = (ROOT / (BASE + 'report-v1.md')).read_text()
    labels = re.findall(r'^\| (SQ17-R2-\d{2}) \|', report, re.M)
    assert labels == ['SQ17-R2-' + str(i).zfill(2) for i in range(1, 41)]
    paths = sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / 'problems/2020-B4/reviews').glob('reasoning-class-return-sq17-review-2-*'))
    assert len(paths) == 4, paths
    put('manifest-v1.json', {
        'frozen_utc': now(), 'reviewer': '/root/review_2021_reasoning_j15_r2',
        'role': 'OTHER initially blind ENTIRE WHOLE2', 'whole_obligations': 40,
        'payload_count': 4, 'ENTIRE_files': 5, 'payloads': [rec(p) for p in paths],
        'effective_guard_summary': baseline['effective_guard_summary'],
        'FULL_final_ALL4_payload_model_readback_completed': True,
        'FULL_manifest_model_readback_then_SEPARATE_readonly_verify_REQUIRED': True,
        'NEW_C_SQ17_finding_file_inventory_hash_metadata_commentary_seen': False,
        'root_related_NEW_source_objection_note_opened_inventoried_hashed': False,
        'NEW_root_SQ16_material_seen_at_freeze': False,
        'new_SQ17_constructive_contribution': False,
        'older_SQ14_SQ15_review_diagnostic_roles_disclosed': True,
        'primary_Schmidt_ALL16_page_images_read': True,
        'publisher_final_Prop3_1_or_errata_read': False,
        'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'independent_effective_setting_readback': None,
        'mathematical_program_CAS_scan_test_source_author_old_replay': False,
        'status': 'Independent review recommendation only; root reconciliation and promotion required'})
    print(json.dumps(rec(BASE + 'manifest-v1.json')))
elif mode == 'verify':
    frozen = obj(BASE + 'manifest-v1.json')
    check(frozen['payloads'])
    protected(obj(BASE + 'baseline-v1.json'))
    print(json.dumps({'SEPARATE_read_only_verify_utc': now(), 'status': 'PASS',
                      'ENTIRE_files': 5, 'whole_obligations': 40,
                      'effective_guard_summary': frozen['effective_guard_summary'],
                      'report': rec(BASE + 'report-v1.md'),
                      'manifest': rec(BASE + 'manifest-v1.json')}))
else:
    raise SystemExit('Unknown documentary mode')
