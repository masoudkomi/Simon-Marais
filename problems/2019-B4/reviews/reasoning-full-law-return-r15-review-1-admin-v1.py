"""Documentary integrity only for a NEW initially blind FL15 whole review.

Never execute author/old code or evaluate mathematical formulas/word counts.
prepare creates compact baseline metadata after exact guard checks.
freeze follows final MODEL readback of ALL four payloads.
verify is a SEPARATE read-only call after FULL manifest MODEL readback.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PREFIX = 'problems/2019-B4/reviews/reasoning-full-law-return-r15-review-1-'
AUTHOR = 'problems/2019-B4/notes/reasoning-full-law-return-r15-'
AUTHOR_FREEZE = AUTHOR + 'freeze-v1.json'
AUTHOR_FREEZE_SHA = '9d65c7cf66efa14925fc15ef081aec846157db3c853ea0744b09afd165e1cbfb'
AUTHOR_MAIN_SHA = '38a770fac7bdc044b672038353a8b2140899f1607f86a0bcc1cfb2f33c077ab8'
PARENT = 'problems/2021-B4/notes/reasoning-deep-return-r24-freeze-v1.json'
PARENT_SHA = 'f2124aa5804550b00eb81e665937718ce24c220929f9003be29fad895c64e833'
BASELINE = PREFIX + 'baseline-v1.json'
MANIFEST = PREFIX + 'manifest-v1.json'
PAYLOADS = [PREFIX + item for item in [
    'initial-v1.md', 'sources-v1.json', 'admin-v1.py', 'baseline-v1.json'
]]
FORBIDDEN = 'problems/2019-B4/reviews/reasoning-full-law-return-r15-review-2-'
FAMILIES = ['reasoning-return-r7', 'reasoning-area-return-r2',
            'reasoning-occupation-return-r1', 'reasoning-cut-transfer-r6',
            'reasoning-cut-transfer-r4']
ERRATUM = 'problems/2019-B4/reviews/reasoning-cut-transfer-r4-presentation-erratum-v1.json'

def utc():
    return datetime.now(timezone.utc).isoformat()

def safe(path):
    assert isinstance(path, str) and not Path(path).is_absolute()
    assert '..' not in Path(path).parts
    assert not path.startswith(FORBIDDEN), 'Embargoed corresponding NEW peer path'
    return ROOT / path

def fp(path):
    raw = safe(path).read_bytes()
    return {'path': path, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}

def load(path):
    return json.loads(safe(path).read_text())

def check(row):
    expected = {key: row[key] for key in ('path', 'bytes', 'sha256')}
    assert fp(expected['path']) == expected, expected
    return expected

def unique(rows):
    dedup = {}
    for row in rows:
        value = {key: row[key] for key in ('path', 'bytes', 'sha256')}
        if value['path'] in dedup:
            assert dedup[value['path']] == value
        dedup[value['path']] = value
    return sorted(dedup.values(), key=lambda row: row['path'])

def summary(rows):
    dedup = unique(rows)
    raw = json.dumps(dedup, sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(rows), 'unique_paths': len(dedup),
            'canonical_deduplicated_sha256': hashlib.sha256(raw).hexdigest()}

def create(path, value):
    assert path.startswith(PREFIX)
    with safe(path).open('x') as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write('\n')

def collect():
    assert fp(AUTHOR_FREEZE)['sha256'] == AUTHOR_FREEZE_SHA
    author = load(AUTHOR_FREEZE)
    assert author['ENTIRE_files'] == 6 and author['whole_obligations'] == 48
    assert len(author['payload_records']) == 5
    rows = [fp(AUTHOR_FREEZE)] + [check(row) for row in author['payload_records']]
    assert fp(AUTHOR + 'candidate-v1.md')['sha256'] == AUTHOR_MAIN_SHA
    guard = load(AUTHOR + 'baseline-v1.json')
    declared = guard['effective_guard_summary']
    old_rows = [check(row) for row in guard['immutable_guard_records']]
    old_summary = summary(old_rows)
    assert old_summary['unique_paths'] == declared['unique_paths']
    assert old_summary['canonical_deduplicated_sha256'] == declared['canonical_deduplicated_sha256']
    rows += old_rows
    # Current exact authorities are model-read; only their necessary declared
    # accepted copies are checked, not their growing historical inventories.
    for family in FAMILIES:
        authority = load(f'problems/2019-B4/reviews/{family}-acceptance.json')
        assert authority['unresolved_substantive_issues'] == 0
        rows.append(check(authority['accepted_copy']))
    rows.append(check(load(ERRATUM)['operative_accepted_copy']))
    # Own immediate parent is a preservation binding, not an FL15 premise.
    assert fp(PARENT)['sha256'] == PARENT_SHA
    parent = load(PARENT)
    assert parent['ENTIRE_files'] == 5 and len(parent['payloads']) == 4
    rows += [fp(PARENT)] + [check(row) for row in parent['payloads']]
    return rows, author, guard, parent

def literals():
    main = safe(PAYLOADS[0]).read_text()
    labels = re.findall(r'^\| FL15-(\d\d) \| PASS\.', main, re.M)
    assert labels == [str(i).zfill(2) for i in range(1, 49)], labels
    notes = re.findall(r'^\| FL15R1-N(\d) \|', main, re.M)
    assert notes == [str(i) for i in range(1, 10)], notes
    source = load(PAYLOADS[1])
    assert source['whole_obligations'] == 48
    assert source['NEW_FL15_construction_contribution'] is False
    assert source['independent_effective_setting_readback'] is None
    assert source['peer_nonexposure']['actual_peer_inventory_open_hash_content_or_baseline_use'] is False
    return {'whole_obligation_labels': len(labels), 'closed_note_labels': len(notes),
            'mathematical_truth_checked_by_code': False}

def prepare():
    rows, author, guard, parent = collect()
    create(BASELINE, {
        'created_UTC': utc(), 'reviewer': '/root/review_2021_reasoning_j15_r2',
        'role': 'OTHER initially blind ENTIRE WHOLE1',
        'whole_obligations': 48, 'ENTIRE_files': 5,
        'target': fp(AUTHOR + 'candidate-v1.md'),
        'author_manifest': fp(AUTHOR_FREEZE),
        'author_baseline': fp(AUTHOR + 'baseline-v1.json'),
        'author_declared_guard_summary_bound': guard['effective_guard_summary'],
        'author_all26_deduplicated_direct_guard_paths_rechecked': True,
        'author_own_parent_older_summary_bound_NOT_reexpanded': guard['own_parent_older_summary_transitively_bound_NOT_replayed'],
        'own_immediate_parent': fp(PARENT),
        'own_all4_parent_payloads_verified': True,
        'own_parent_historical_guard_summary_bound_NOT_reexpanded': parent['effective_fresh_guard_summary'],
        'own_parent_mathematics_FL15_premise': False,
        'effective_fresh_guard_summary': summary(rows),
        'giant_historical_inventory_recopied_or_traversed': False,
        'current_authority_declared_accepted_copies_verified': 5,
        'CT_erratum_operative_v1_2_verified_historical_v1_1_not_operative': True,
        'literal_document_checks': literals(),
        'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'independent_effective_setting_readback': None,
        'peer_nonexposure': load(PAYLOADS[1])['peer_nonexposure'],
        'direct_quota': {'usedPercent': 73, 'windowDurationMins': 10080,
                         'resetsAt': 1792874445, 'ordinaryUsageAllowed': True,
                         'observed_UTC': '2026-10-18 23:54:29 UTC; transition tool again73%',
                         'TOTAL_ceiling': 90, 'integration_reserve': True,
                         'automatic_later_window': False},
        'no_mathcode_CAS_scan_test_optimizer_old_source_author_replay': True,
        'no_Git_shared_old_cache_mutation': True,
        'FULL_final_ALL4_payload_MODEL_readbacks_then_manifest_MODEL_readback_then_SEPARATEverify_required': True
    })
    print(json.dumps({'baseline': fp(BASELINE), 'guards': summary(rows), 'at_UTC': utc()}))

def guards():
    rows, author, guard, parent = collect()
    baseline = load(BASELINE)
    assert summary(rows) == baseline['effective_fresh_guard_summary']
    assert literals() == baseline['literal_document_checks']
    assert fp(AUTHOR_FREEZE) == baseline['author_manifest']
    assert fp(PARENT) == baseline['own_immediate_parent']
    return baseline

def freeze():
    baseline = guards()
    create(MANIFEST, {
        'frozen_UTC': utc(), 'reviewer': '/root/review_2021_reasoning_j15_r2',
        'status': 'initial whole review; sealed until explicit BOTH release',
        'role': 'OTHER initially blind ENTIRE WHOLE1',
        'whole_obligations': 48, 'ENTIRE_files': 5, 'payload_count': 4,
        'payloads': [fp(path) for path in PAYLOADS],
        'author_manifest': fp(AUTHOR_FREEZE),
        'own_immediate_parent': fp(PARENT),
        'effective_fresh_guard_summary': baseline['effective_fresh_guard_summary'],
        'FULL_final_ALL4_payload_MODEL_readbacks_completed': True,
        'FULL_manifest_MODEL_readback_then_SEPARATE_readonly_verify_REQUIRED': True,
        'peer_nonexposure': baseline['peer_nonexposure'],
        'findings_embargo_until_explicit_BOTH_ENTIRE_confirmation': True,
        'mathematical_truth_checked_by_code': False,
        'no_Git_shared_old_cache_mutation': True
    })
    print(json.dumps({'manifest': fp(MANIFEST), 'at_UTC': utc()}))

def verify():
    manifest = load(MANIFEST)
    assert manifest['ENTIRE_files'] == 5 and manifest['whole_obligations'] == 48
    assert [row['path'] for row in manifest['payloads']] == PAYLOADS
    for row in manifest['payloads']:
        check(row)
    baseline = guards()
    assert manifest['effective_fresh_guard_summary'] == baseline['effective_fresh_guard_summary']
    assert manifest['peer_nonexposure'] == baseline['peer_nonexposure']
    check(manifest['author_manifest'])
    check(manifest['own_immediate_parent'])
    print(json.dumps({'SEPARATE_readonly_verify': 'PASS', 'at_UTC': utc(),
                      'manifest': fp(MANIFEST), 'payloads': 4,
                      'whole_obligations': 48,
                      'guards': manifest['effective_fresh_guard_summary'],
                      'mathematical_truth_checked_by_code': False}))

if __name__ == '__main__':
    assert len(sys.argv) == 2 and sys.argv[1] in {'prepare', 'freeze', 'verify'}
    {'prepare': prepare, 'freeze': freeze, 'verify': verify}[sys.argv[1]]()
