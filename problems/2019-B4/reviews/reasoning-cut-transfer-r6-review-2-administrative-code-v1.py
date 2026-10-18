"""AT WHOLE2 administration: exact fingerprints, suffixes and labels ONLY.

No mathematical computation, source/author/old replay or directory scan.
Writes exclusively new assigned-prefix metadata. Verify is read-only and
must be invoked separately after FULL final model readback of ALL11 files.
Corresponding NEW root AT review paths are explicitly forbidden.
"""
from pathlib import Path
import datetime
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
PREFIX = 'problems/2019-B4/reviews/reasoning-cut-transfer-r6-review-2-'
FORBIDDEN = 'problems/2019-B4/reviews/reasoning-cut-transfer-r6-review-1-'
AUTHOR = 'problems/2019-B4/notes/reasoning-cut-transfer-r6-'
AUTHOR_FREEZE = AUTHOR + 'freeze-v1.json'
PARENT = 'problems/2021-B4/notes/reasoning-center-return-r20-freeze-v1.json'
BASELINE = PREFIX + 'baseline-v1.json'
VALIDATION = PREFIX + 'input-validation-v1.json'
METADATA = PREFIX + 'metadata-v1.json'
MANIFEST = PREFIX + 'manifest-v1.json'
STATIC = [PREFIX + name for name in (
    'report-v1.md', 'ledger-v1.md', 'issues-v1.md', 'sources-v1.md',
    'sources-v1.json', 'worklog-v1.md', 'administrative-code-v1.py')]

def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def permitted(path):
    assert not path.startswith(FORBIDDEN), 'Corresponding NEW peer access forbidden'

def fp(path):
    permitted(path)
    blob = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(blob),
            'sha256': hashlib.sha256(blob).hexdigest()}

def read(path):
    permitted(path)
    return json.loads((ROOT / path).read_text())

def check(spec):
    actual = fp(spec['path'])
    assert actual == {key: spec[key] for key in ('path', 'bytes', 'sha256')}, actual
    return actual

def put(path, value):
    assert path.startswith(PREFIX)
    with (ROOT / path).open('x') as stream:
        json.dump(value, stream, indent=2)
        stream.write('\n')

def canonical(records):
    grouped = {}
    for record in records:
        assert grouped.setdefault(record['path'], record) == record
    ordered = [grouped[path] for path in sorted(grouped)]
    raw = json.dumps(ordered, sort_keys=True, separators=(',', ':')).encode()
    return ordered, hashlib.sha256(raw).hexdigest()

def labels():
    found = re.findall(r'^\|(R6-\d\d)\|PASS\|',
                       (ROOT / (PREFIX + 'ledger-v1.md')).read_text(), re.M)
    assert found == [f'R6-{index:02d}' for index in range(1, 65)]
    return {'whole_obligations': 64, 'independent_PASS_rows': 64,
            'substantive_issues': 0, 'required_author_repairs': 0,
            'closed_scope_notes': 8}

def gather():
    records = [check({'path': AUTHOR_FREEZE, 'bytes': 5022,
                      'sha256': '4b8e9a485850e2410f045ad4d83e13184d2d6ce60a327b153cd47313f483b4cc'})]
    freeze = read(AUTHOR_FREEZE)
    assert freeze['whole_obligations'] == 64
    assert freeze['ENTIRE_files_including_freeze'] == 11
    records += [check(spec) for spec in freeze['payloads']]
    check({'path': AUTHOR + 'candidate-v1.md', 'bytes': 20223,
           'sha256': '1f5e0b02047806420b52fe503f85567f23dccfd05045a710b802d03dc9e0f40d'})
    baseline = read(AUTHOR + 'baseline-v1.json')
    records += [check(spec) for spec in baseline['direct_inputs']]
    accepted_bindings = []
    for path in baseline['accepted_authorities']:
        authority = read(path)
        assert authority['status'] == 'proved, independently reviewed scoped partial result'
        candidate = check(authority['candidate'])
        accepted = check(authority['accepted_copy'])
        assert (ROOT / accepted['path']).read_bytes().endswith(
            (ROOT / candidate['path']).read_bytes())
        records += [candidate, accepted]
        accepted_bindings.append({'authority': fp(path),
            'candidate': candidate, 'accepted_copy': accepted,
            'historical_occurrences_bound': authority.get('record_occurrences_verified'),
            'historical_paths_bound': authority.get('unique_paths_verified')})
    erratum_path = 'problems/2019-B4/reviews/reasoning-cut-transfer-r4-presentation-erratum-v1.json'
    erratum = read(erratum_path)
    operative = check(erratum['operative_accepted_copy'])
    suffix = check(erratum['unchanged_candidate_suffix'])
    assert (ROOT / operative['path']).read_bytes().endswith((ROOT / suffix['path']).read_bytes())
    records += [operative, suffix]
    author_parent = read(baseline['older_own_parent']['path'])
    records += [check(spec) for spec in author_parent['payloads']]
    records.append(check({'path': PARENT, 'bytes': 3306,
        'sha256': '8b69fb88b967acd31605e9189cbd02b5566ba4f656fe5e0811b616efbff5cbb4'}))
    own_parent = read(PARENT)
    records += [check(spec) for spec in own_parent['payloads']]
    unique, digest = canonical(records)
    return records, unique, digest, accepted_bindings, operative, own_parent

def guard(baseline):
    for spec in baseline['protected']:
        check(spec)
    _, digest = canonical(baseline['protected'])
    assert digest == baseline['canonical_deduplicated_sha256']

mode = sys.argv[1]
if mode == 'prepare':
    for path in (BASELINE, VALIDATION, METADATA, MANIFEST):
        assert not (ROOT / path).exists(), path
    rows = labels()
    records, unique, digest, accepted, operative, own_parent = gather()
    put(BASELINE, {
        'captured_at_utc': utc(), 'scope': 'current necessary roots plus compact immutable parent bindings',
        'corresponding_NEW_root_AT_finding_file_hash_metadata_commentary_accessed': False,
        'author_freeze': fp(AUTHOR_FREEZE), 'author_declared_occurrences': 61,
        'author_declared_unique_paths': 54,
        'accepted_bindings': accepted, 'operative_CT_v1_2': operative,
        'immediate_own_parent': fp(PARENT),
        'own_parent_historical_occurrences': own_parent['verified_input_record_occurrences'],
        'own_parent_historical_paths': own_parent['verified_unique_paths'],
        'historical_inventories_recopied_or_recursively_replayed': False,
        'record_occurrences': len(records), 'unique_paths': len(unique),
        'canonical_deduplicated_sha256': digest, 'protected': unique})
    put(VALIDATION, {
        'checked_at_utc': utc(), 'PASS': True, **rows,
        'record_occurrences': len(records), 'unique_paths': len(unique),
        'canonical_deduplicated_sha256': digest,
        'mathematical_claim_evaluation_or_old_freezer_execution': False,
        'only_NEW_assigned_prefix_written': True})
    print(json.dumps({'prepare': 'PASS', **rows, 'record_occurrences': len(records),
                      'unique_paths': len(unique), 'baseline': fp(BASELINE),
                      'validation': fp(VALIDATION)}))
elif mode == 'freeze':
    baseline = read(BASELINE)
    guard(baseline)
    rows = labels()
    assert not (ROOT / METADATA).exists() and not (ROOT / MANIFEST).exists()
    put(METADATA, {
        'created_at_utc': utc(), 'reviewer': '/root/review_2021_reasoning_j15_r2',
        'status': 'ENTIRE initially blind OTHER WHOLE2 initial; recommendation only', **rows,
        'author_sole_NEW_constructor_excluded': True,
        'NEW_AT_construction_contribution': False,
        'older_R7_CN_authorship_and_CR_G_BT_review_roles_disclosed': True,
        'accepted_inputs_freshly_independently_recertified': False,
        'corresponding_NEW_root_AT_finding_file_hash_metadata_commentary_accessed': False,
        'root_administrative_completion_counts_times_only_received': True,
        'findings_embargoed_until_BOTH_ENTIRE_explicit_confirmation': True,
        'payload_files': 10, 'ENTIRE_files': 11,
        'FULL_final_ALL11_model_readback_and_SEPARATE_verify_required_before_handoff': True,
        'mathematical_code_CAS_scan_author_source_old_replay': False,
        'requested_settings': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'independent_effective_readback': None,
        'compact_baseline': fp(BASELINE),
        'quota': {'authoritative_utc': '2026-10-18T15:17:30Z',
                  'total_used_percent': 46, 'reset': 1792874445,
                  'ceiling_total_percent': 90, 'integration_reserve': True,
                  'automatic_later_window_spending': False}})
    payloads = [fp(path) for path in STATIC + [BASELINE, VALIDATION, METADATA]]
    put(MANIFEST, {
        'frozen_at_utc': utc(), 'status': 'ENTIRE initially blind OTHER WHOLE2 initial',
        **rows, 'reviewer': '/root/review_2021_reasoning_j15_r2',
        'author_main': fp(AUTHOR + 'candidate-v1.md'), 'author_freeze': fp(AUTHOR_FREEZE),
        'payload_files': len(payloads), 'ENTIRE_files': len(payloads) + 1,
        'compact_baseline': fp(BASELINE), 'immediate_own_parent': fp(PARENT),
        'protected_occurrences': baseline['record_occurrences'],
        'protected_unique_paths': baseline['unique_paths'],
        'canonical_deduplicated_sha256': baseline['canonical_deduplicated_sha256'],
        'corresponding_NEW_root_AT_finding_file_hash_metadata_commentary_accessed': False,
        'FULL_final_ALL_file_model_readback_and_SEPARATE_verify_required_before_handoff': True,
        'findings_embargoed_until_BOTH_ENTIRE_explicit_confirmation': True,
        'mathematical_execution': False, 'payloads': payloads})
    print(json.dumps({'freeze': 'created; FULL final readback and separate verify required',
                      'manifest': fp(MANIFEST), 'report': fp(STATIC[0]),
                      'ENTIRE_files': len(payloads) + 1, **rows}))
elif mode == 'verify':
    baseline, manifest = read(BASELINE), read(MANIFEST)
    guard(baseline)
    for spec in manifest['payloads']:
        check(spec)
    assert len(manifest['payloads']) == 10 and manifest['ENTIRE_files'] == 11
    rows = labels()
    print(json.dumps({'SEPARATE_readonly_verify_at_utc': utc(), 'PASS': True, **rows,
        'ENTIRE_files': 11, 'protected_occurrences': baseline['record_occurrences'],
        'protected_unique_paths': baseline['unique_paths'],
        'manifest': fp(MANIFEST), 'report': fp(STATIC[0]),
        'corresponding_NEW_root_AT_peer_access': False, 'mathematical_execution': False}))
else:
    raise SystemExit('prepare, freeze or verify only')
