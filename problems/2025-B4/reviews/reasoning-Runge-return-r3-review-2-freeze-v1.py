"""Administrative-only exclusive review freezer: SHA, JSON, labels; no mathematics."""
from pathlib import Path
import datetime as dt
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
P = 'problems/2025-B4/reviews/reasoning-Runge-return-r3-review-2-'
T = 'problems/2025-B4/notes/reasoning-Runge-return-r3-'
PARENT = 'problems/2021-B4/reviews/reasoning-unit-return-r15-review-2-manifest-v1.json'

def stamp():
    return dt.datetime.now(dt.timezone.utc).isoformat()

def rec(path):
    data = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def checked(expected):
    actual = rec(expected['path'])
    assert actual == {k: expected[k] for k in ('path', 'bytes', 'sha256')}, (expected, actual)
    return actual

def read_json(path):
    return json.loads((ROOT / path).read_text())

def write_json(path, data):
    with (ROOT / path).open('x', encoding='utf-8') as output:
        json.dump(data, output, indent=2, ensure_ascii=False)
        output.write('\n')

def fingerprint_rows(value):
    result = []
    if isinstance(value, dict):
        if all(k in value for k in ('path', 'bytes', 'sha256')):
            result.append({k: value[k] for k in ('path', 'bytes', 'sha256')})
        for child in value.values():
            result.extend(fingerprint_rows(child))
    elif isinstance(value, list):
        for child in value:
            result.extend(fingerprint_rows(child))
    return result

def canonical(rows):
    unique = {}
    for row in rows:
        path = row['path']
        assert path not in unique or unique[path] == row
        unique[path] = row
    ordered = [unique[k] for k in sorted(unique)]
    digest = hashlib.sha256(json.dumps(ordered, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return ordered, digest

expected_main = {'path': T + 'candidate-v1.md', 'bytes': 23038,
    'sha256': '5ccc04e72574187d1959efff22852dbbc5cca41e701afbaeebc9f97adbdf64a0'}
expected_freeze = {'path': T + 'freeze-v1.json', 'bytes': 8661,
    'sha256': '6a010ee19e90b4a07373f64dd375e9df7e6c8d4aee9ec7af001d8410e5bb461a'}
expected_parent = {'path': PARENT, 'bytes': 2959,
    'sha256': 'f1c3bf00f0d55e1d6299a649e3f022f48a90985dcf44d224f4737da33da9d0d7'}
checked(expected_main)
checked(expected_freeze)
checked(expected_parent)
constructor = read_json(expected_freeze['path'])
constructor_baseline = read_json(T + 'baseline-v1.json')
parent = read_json(PARENT)
assert len(constructor['artifacts']) == 9
assert len(constructor_baseline['protected']) == 20
assert len(parent['artifacts']) == 9

initial_suffixes = ['initial-v1.md', 'ledger-v1.md', 'issues-v1.md',
    'sources-v1.md', 'worklog-v1.md', 'freeze-v1.py']
expected_initial = {P + suffix for suffix in initial_suffixes}
actual_initial = {str(x.relative_to(ROOT)) for x in (ROOT / 'problems/2025-B4/reviews').glob('reasoning-Runge-return-r3-review-2-*')}
assert actual_initial == expected_initial, actual_initial
ledger = (ROOT / (P + 'ledger-v1.md')).read_text()
labels = re.findall(r'^\| (R3O-\d{2}) \|', ledger, re.M)
assert labels == ['R3O-' + str(i).zfill(2) for i in range(1, 61)]

declared = constructor['artifacts'] + [expected_freeze]
declared += constructor_baseline['protected']
declared += [expected_parent] + parent['artifacts']
for row in declared:
    checked(row)
protected, protected_hash = canonical(declared)
parent_rows = fingerprint_rows(parent)
parent_unique, parent_hash = canonical(parent_rows)
constructor_rows = fingerprint_rows(constructor)
constructor_unique, constructor_hash = canonical(constructor_rows)

baseline = {
    'created_utc': stamp(),
    'purpose': 'Administrative necessary immutable input guards; no mathematical computation',
    'guard_expected_target_and_parent_identities_given_before_first_write': True,
    'assigned_prefix_confirmed_unused_before_content_write': True,
    'protected_fingerprint_occurrences': len(declared),
    'protected_unique_paths': len(protected),
    'canonical_protected_summary_sha256': protected_hash,
    'protected': protected,
    'compact_immutable_parents': [
        {'identity': expected_parent, 'declared_fingerprint_occurrences': len(parent_rows),
         'deduplicated_paths': len(parent_unique), 'canonical_summary_sha256': parent_hash,
         'historical_inventory_not_recopied_or_recursively_reverified': True},
        {'identity': expected_freeze, 'declared_fingerprint_occurrences': len(constructor_rows),
         'deduplicated_paths': len(constructor_unique), 'canonical_summary_sha256': constructor_hash,
         'historical_inventory_not_recopied_or_recursively_reverified': True}
    ],
    'no_corresponding_NEW_A_R3_review_material_accessed': True,
    'no_old_shared_Git_cache_mutation': True
}
write_json(P + 'baseline-v1.json', baseline)

metadata = {
    'created_utc': stamp(),
    'reviewer': '/root/review_2017_coarsening_r1',
    'status': 'ENTIRE initially blind OTHER WHOLE R3 R2; not promotion',
    'whole_obligations': 60,
    'all60_reconstructed_by_hand': True,
    'new_constructor_B_excluded': True,
    'older_C_R6_RG_R9_FS_authorship_disclosed_not_independently_recertified': True,
    'older_RS_UW_review_roles_disclosed': True,
    'certified_weight_domain': 'nonnegative integers, positive sum; explicit R3O-14',
    'corresponding_NEW_A_R3_files_findings_hashes_metadata_accessed': False,
    'identity_only_completion_until_BOTH_entire_initials_confirmed': True,
    'all_mathematics_in_initial_ledger_and_issues_no_math_code': True,
    'no_math_scan_CAS_constructor_rerun_source_certificate_or_job': True,
    'no_Git_old_shared_cache_write_spawn_contact_charge_bypass': True,
    'requested_settings': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
    'verified_effective_settings': None,
    'telemetry': {'latest_parent_TOTAL_percent': 22, 'reset_unix': 1792874445,
                  'current_window_human_authorized': True, 'ceiling_TOTAL_percent': 90,
                  'integration_reserve': True, 'automatic_later_reset_spending': False},
    'target_main': expected_main,
    'target_freeze': expected_freeze,
    'immediate_own_parent': expected_parent,
    'compact_baseline': rec(P + 'baseline-v1.json')
}
write_json(P + 'metadata-v1.json', metadata)

for row in protected:
    checked(row)
before_validation = initial_suffixes + ['baseline-v1.json', 'metadata-v1.json']
validation = {
    'checked_utc': stamp(),
    'target_main_and_freeze_exact': True,
    'all_constructor_nine_payloads_exact': True,
    'all_constructor_twenty_necessary_guards_exact': True,
    'immediate_own_parent_and_nine_payloads_exact': True,
    'protected_fingerprint_occurrences': len(declared),
    'protected_unique_paths': len(protected),
    'canonical_protected_summary_sha256': protected_hash,
    'whole_ledger_labels_exactly_R3O_01_through_60_once_in_order': True,
    'review_payloads_present_before_validation': len(before_validation),
    'no_corresponding_NEW_A_R3_peer_access': True,
    'mathematical_programs_executed': 0,
    'only_administrative_hash_serialization_and_label_checks': True
}
write_json(P + 'input-validation-v1.json', validation)

payload_suffixes = before_validation + ['input-validation-v1.json']
payloads = [rec(P + suffix) for suffix in payload_suffixes]
for row in protected + payloads:
    checked(row)
manifest = {
    'frozen_utc': stamp(),
    'status': 'ENTIRE initially blind OTHER WHOLE R3 R2 frozen; not promotion',
    'whole_obligations': 60,
    'review_file_count': 10,
    'ENTIRE_report_ALL60_issues_sources_log_code_ALL_metadata_frozen': True,
    'no_corresponding_NEW_A_R3_findings_files_hashes_or_metadata_access': True,
    'identity_only_completion_before_mathematical_findings': True,
    'target_main': expected_main,
    'target_freeze': expected_freeze,
    'immediate_own_parent': expected_parent,
    'artifacts': payloads
}
write_json(P + 'manifest-v1.json', manifest)
print(json.dumps({'manifest': rec(P + 'manifest-v1.json'),
                  'initial': rec(P + 'initial-v1.md'),
                  'files': 10, 'obligations': 60,
                  'protected_occurrences': len(declared),
                  'protected_unique_paths': len(protected)}, indent=2))
