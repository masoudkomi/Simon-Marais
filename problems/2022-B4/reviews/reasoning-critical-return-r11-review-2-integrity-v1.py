"""NEW documentary helper only: no orbit/formula/inequality evaluation.

snapshot creates ONLY this review prefix's baseline/metadata.
freeze runs AFTER FULL final MODEL readback of ALL five payloads.
verify is a SEPARATE read-only process AFTER FULL manifest MODEL readback.
No old helper is executed; no peer inventory or recursive ancestry is read.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PREFIX = 'problems/2022-B4/reviews/reasoning-critical-return-r11-review-2-'
AUTHOR = 'problems/2022-B4/notes/reasoning-critical-return-r11-freeze-v1.json'
AUTHOR_SHA = '789bff4a55821c867d0e1d627f3f3c961940f570e812e8bc35980f96b9e8e3a7'
PARENT = 'problems/2021-B4/reviews/reasoning-negative-return-r23-review-2-manifest-v1.json'
PARENT_SHA = '07843f25da4469364108ef0d1b7f867ef6a00600981436b655777998c62fa5b3'
BASELINE = PREFIX + 'baseline-v1.json'
METADATA = PREFIX + 'metadata-v1.json'
MANIFEST = PREFIX + 'manifest-v1.json'
PAYLOADS = [PREFIX + suffix for suffix in [
    'initial-v1.md', 'sources-v1.json', 'integrity-v1.py',
    'baseline-v1.json', 'metadata-v1.json',
]]
DIRECT = [
    'AGENTS.md', 'problems/2022-B4/statement.md',
    'problems/2022-B4/proofs/reviewed-reasoning-dynamics-return-r9-v1.1.md',
    'problems/2022-B4/reviews/reasoning-dynamics-return-r9-acceptance.md',
    'problems/2022-B4/reviews/reasoning-dynamics-return-r9-acceptance.json',
    'problems/2022-B4/proofs/reviewed-reasoning-collision-return-r10-v1.1.md',
    'problems/2022-B4/reviews/reasoning-collision-return-r10-acceptance.md',
    'problems/2022-B4/reviews/reasoning-collision-return-r10-acceptance.json',
]
AUTHORITIES = [DIRECT[4], DIRECT[7]]
FORBIDDEN = [
    'problems/2022-B4/reviews/reasoning-critical-return-r11-review-1-',
    'problems/2021-B4/reviews/reasoning-negative-return-r23-review-1-',
    'r13', 'tensor',
]

def now():
    return datetime.now(timezone.utc).isoformat()

def allowed(path):
    assert isinstance(path, str) and not Path(path).is_absolute()
    assert '..' not in Path(path).parts
    assert not any(token in path for token in FORBIDDEN), path
    return ROOT / path

def read_json(path):
    return json.loads(allowed(path).read_text())

def fp(path):
    data = allowed(path).read_bytes()
    return {'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def check(row):
    expected = {key: row[key] for key in ['path', 'bytes', 'sha256']}
    actual = fp(expected['path'])
    assert actual == expected, (expected, actual)
    return actual

def unique_rows(rows):
    deduplicated = {}
    for row in rows:
        value = {key: row[key] for key in ['path', 'bytes', 'sha256']}
        if value['path'] in deduplicated:
            assert value == deduplicated[value['path']]
        deduplicated[value['path']] = value
    return sorted(deduplicated.values(), key=lambda row: row['path'])

def summary(rows):
    unique = unique_rows(rows)
    raw = json.dumps(unique, sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(rows), 'unique_paths': len(unique),
            'canonical_deduplicated_sha256': hashlib.sha256(raw).hexdigest()}

def create(path, value):
    assert path.startswith(PREFIX), path
    with allowed(path).open('x') as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write('\n')

def literal_checks():
    report = allowed(PAYLOADS[0]).read_text()
    labels = re.findall(r'^\| O11-(\d\d) \| PASS\.', report, flags=re.M)
    assert labels == [str(i).zfill(2) for i in range(1, 49)], labels
    notes = re.findall(r'\* \*\*C11-N(\d+), CLOSED:', report)
    assert notes == [str(i) for i in range(1, 11)], notes
    source = read_json(PAYLOADS[1])
    assert source['whole_obligations'] == 48
    assert source['closed_scope_notes'] == 10
    assert source['independent_effective_readback'] is None
    assert source['corresponding_NEW_peer_access'] is False
    return {'literal_PASS_rows': len(labels), 'closed_scope_notes': len(notes),
            'mathematical_truth_checked_by_code': False}

def snapshot():
    assert fp(AUTHOR)['sha256'] == AUTHOR_SHA
    assert fp(PARENT)['sha256'] == PARENT_SHA
    author = read_json(AUTHOR)
    parent = read_json(PARENT)
    assert author['ENTIRE_files'] == 5 and author['whole_obligations'] == 48
    assert parent['ENTIRE_files'] == 6 and parent['whole_obligations'] == 48
    assert len(author['payload_records']) == 4
    assert len(parent['payload_records']) == 5
    rows = [fp(AUTHOR), fp(PARENT)] + [fp(path) for path in DIRECT]
    rows += [check(row) for row in author['payload_records']]
    rows += [check(row) for row in parent['payload_records']]
    # Only the accepted authorities' immediate declared records are checked.
    # Their older baselines/manifests are bound as bytes, never traversed.
    for path in AUTHORITIES:
        authority = read_json(path)
        rows.append(check(authority['candidate']))
        rows.append(check(authority['accepted_copy']))
        rows.extend(check(row) for row in authority['verification_metadata'])
    known = {
        'AGENTS.md': '28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff',
        DIRECT[2]: '7cfa2c60557935261d7144576f0e39a509fbebb292fdd0027415efe411ae4c55',
        DIRECT[5]: '269bb65792e1c31159b4443726af84083657fe73e8a1440e3cc72ee0c9c99989',
    }
    for row in rows:
        if row['path'] in known:
            assert row['sha256'] == known[row['path']]
    create(BASELINE, {
        'snapshot_utc': now(), 'documentary_only': True,
        'immutable_guard_records': unique_rows(rows),
        'effective_guard_summary': summary(rows),
        'author_ENTIRE_packet': fp(AUTHOR),
        'author_parent_declaration_NOT_followed': {
            'declared_inside_author_packet': True,
            'external_parent_or_payload_open_hash_inventory': False,
            'bound_by_author5_freeze_and_baseline_bytes_only': True,
        },
        'own_immediate_parent': fp(PARENT),
        'own_parent_older_summary_transitively_bound_NOT_replayed': parent['effective_guard_summary'],
        'literal_checks': literal_checks(),
        'corresponding_NEW_peer_access': False,
    })
    create(METADATA, {
        'created_utc': now(), 'reviewer': '/root/review_2017_coarsening_r1',
        'role': 'OTHER initially blind ENTIRE WHOLE2',
        'ENTIRE_files_including_manifest': 6, 'whole_obligations': 48,
        'closed_scope_notes': 10, 'required_repairs': 0,
        'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'independent_effective_readback': None,
        'OLD_roles': 'C OLD D9 constructor and RC10 reviewer; no old independent self-recertification; no NEW CR11 construction.',
        'no_corresponding_NEW_peer_or_root_R23_access': True,
        'unrelated_author_parent_not_followed': True,
        'all_mathematics_hand_reconstructed': True,
        'new_helper_documentary_only': True,
        'no_mathematical_program_CAS_scan_test_old_source_author_executable_replay': True,
        'no_Git_shared_old_cache_mutation_spawn_charge_contact_bypass': True,
        'weekly': {'authority': 'C direct account-wide',
                   'at_utc': '2026-10-18 23:20:14 UTC',
                   'TOTAL_used_percent': 70, 'ordinaryUsageAllowed': True,
                   'resetsAt': 1792874445, 'TOTAL_ceiling': 90,
                   'integration_reserve': True, 'automatic_later_window': False},
        'findings_EMBARGO_until_explicit_BOTH_ENTIRE': True,
        'FULL_final_MODEL_ALL5_payloads_then_manifest_MODEL_readback_then_SEPARATE_verify_required': True,
    })
    print(json.dumps({'snapshot': fp(BASELINE), 'metadata': fp(METADATA),
                      'guards': summary(rows), 'at_utc': now()}))

def guard_check():
    baseline = read_json(BASELINE)
    for row in baseline['immutable_guard_records']:
        check(row)
    deduplicated = summary(baseline['immutable_guard_records'])
    effective = baseline['effective_guard_summary']
    assert deduplicated['unique_paths'] == effective['unique_paths']
    assert deduplicated['canonical_deduplicated_sha256'] == effective['canonical_deduplicated_sha256']
    assert effective['occurrences'] >= effective['unique_paths']
    assert baseline['literal_checks'] == literal_checks()
    return baseline

def freeze():
    baseline = guard_check()
    create(MANIFEST, {
        'frozen_utc': now(), 'reviewer': '/root/review_2017_coarsening_r1',
        'role': 'OTHER initially blind ENTIRE WHOLE2',
        'ENTIRE_files': 6, 'whole_obligations': 48,
        'payload_records': [fp(path) for path in PAYLOADS],
        'author': fp(AUTHOR), 'own_parent': fp(PARENT),
        'effective_guard_summary': baseline['effective_guard_summary'],
        'FULL_final_MODEL_ALL5_payload_readback_completed': True,
        'FULL_manifest_MODEL_readback_then_SEPARATE_readonly_verify_required': True,
        'NO_NEW_corresponding_peer_findings_files_inventory_hash_metadata_access': True,
        'unrelated_author_declared_parent_not_followed': True,
        'findings_EMBARGO_until_explicit_BOTH_ENTIRE': True,
        'mathematical_program': False,
        'old_shared_Git_cache_bytes_changed': False,
    })
    print(json.dumps({'manifest': fp(MANIFEST), 'at_utc': now()}))

def verify():
    manifest = read_json(MANIFEST)
    assert manifest['ENTIRE_files'] == 6 and manifest['whole_obligations'] == 48
    assert [row['path'] for row in manifest['payload_records']] == PAYLOADS
    for row in manifest['payload_records']:
        check(row)
    check(manifest['author'])
    check(manifest['own_parent'])
    baseline = guard_check()
    assert manifest['effective_guard_summary'] == baseline['effective_guard_summary']
    assert manifest['NO_NEW_corresponding_peer_findings_files_inventory_hash_metadata_access'] is True
    print(json.dumps({'SEPARATE_readonly_verify': 'PASS', 'at_utc': now(),
                      'manifest': fp(MANIFEST), 'payloads': 5,
                      'whole_obligations': 48,
                      'guards': baseline['effective_guard_summary'],
                      'mathematical_truth_checked_by_code': False}))

if __name__ == '__main__':
    assert len(sys.argv) == 2 and sys.argv[1] in {'snapshot', 'freeze', 'verify'}
    {'snapshot': snapshot, 'freeze': freeze, 'verify': verify}[sys.argv[1]]()
