"""Independent metadata-only immutable R13 review freeze.

No finite-field calculation, math scan, author script or certificate is
run. Checks only exact bytes, JSON declarations, accepted suffixes and
presence/order of the44 review ledger labels.
"""
from pathlib import Path
import datetime
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = 'problems/2021-B4/reviews/reasoning-return-r13-review-1-'
FORBIDDEN = 'problems/2021-B4/reviews/reasoning-return-r13-review-2-'


def raw(path):
    assert not path.startswith(FORBIDDEN), 'NEW root peer review forbidden'
    return (ROOT / path).read_bytes()


def record(path):
    value = raw(path)
    return {'path': path, 'bytes': len(value),
            'sha256': hashlib.sha256(value).hexdigest()}


def check(row):
    actual = record(row['path'])
    assert actual == {k: row[k] for k in ('path', 'bytes', 'sha256')}, row['path']
    return actual


def summary(rows):
    unique = {}
    for row in rows:
        previous = unique.setdefault(row['path'], row)
        assert previous == row
    ordered = [unique[p] for p in sorted(unique)]
    digest = hashlib.sha256(json.dumps(ordered, sort_keys=True,
                            separators=(',', ':')).encode()).hexdigest()
    return {'occurrences': len(rows), 'unique_paths': len(unique),
            'canonical_deduplicated_summary_sha256': digest}


def write_new(path, value):
    with (ROOT / path).open('x') as stream:
        stream.write(json.dumps(value, indent=2) + '\n')


baseline_path = PREFIX + 'baseline-v1.json'
baseline = json.loads(raw(baseline_path))
rows = [check(row) for row in baseline['inputs']]
target = check(baseline['exact_target'])
constructor_freeze = check(baseline['constructor_freeze'])
assert target['bytes'] == 15806
assert target['sha256'] == '25a871da93b7cd375e0af43c8643094463ac45ce913722805ba6958dee004148'
assert constructor_freeze['bytes'] == 4152
assert constructor_freeze['sha256'] == '4d6b95b7c5b70301f227af7cce5169c8c691c01f6b287fdadacf0b337c40c656'
parent = check(baseline['compact_own_parent'])
assert parent['sha256'] == 'cc19751925533064c90e80e9974fe402d8808eb2910936b54d493e5d2966dfe0'
assert baseline['older_own_paths_bound_transitively'] == 522

# Current declared copies only; do not expand historical review inventories.
authorities = []
for number in (5, 8, 12):
    path = f'problems/2021-B4/reviews/reasoning-return-r{number}-acceptance.json'
    authority = json.loads(raw(path))
    accepted = check(authority['accepted_copy'])
    candidate = check(authority['candidate'])
    assert raw(accepted['path']).endswith(raw(candidate['path']))
    rows.append(accepted)
    authorities.append({'authority': record(path), 'accepted_copy': accepted,
                        'exact_candidate_suffix_preserved': True})

# Independently reconstruct the constructor's compact SIX current groups.
# This is JSON/SHA validation, not a rerun of its executable.
cv_path = 'problems/2021-B4/notes/reasoning-return-r13-input-validation-v1.json'
cv = json.loads(raw(cv_path))
constructor_rows = []
for group in cv['groups']:
    if 'records' in group:
        constructor_rows.extend(check(x) for x in group['records'])
        continue
    metadata = check(group['metadata'])
    constructor_rows.append(metadata)
    document = json.loads(raw(metadata['path']))
    if group['group'] == 'operative accepted input':
        constructor_rows.append(record(metadata['path'].replace('.json', '.md')))
        constructor_rows.extend(check(document[key]) for key in ('candidate', 'accepted_copy'))
    else:
        constructor_rows.extend(check(x) for x in document['artifacts'])
cs = summary(constructor_rows)
assert cs['occurrences'] == 33 and cs['unique_paths'] == 32
assert cs['canonical_deduplicated_summary_sha256'] == cv['summary']['canonical_deduplicated_summary_sha256']

labels = re.findall(r'^\| (\d\d) \|',
                    raw(PREFIX + 'ledger-v1.md').decode(), re.MULTILINE)
assert labels == [f'{i:02}' for i in range(1, 45)]
current = summary(rows)
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
validation_path = PREFIX + 'input-validation-v1.json'
validation = {
    'validated_utc': now,
    'metadata_only_not_mathematical_testing': True,
    'baseline': record(baseline_path),
    'exact_target': target,
    'constructor_freeze': constructor_freeze,
    'all11_constructor_packet_files_and_selected_old_inputs_unchanged': True,
    'accepted_authorities': authorities,
    'constructor_six_group_summary_independently_reconstructed': cs,
    'current_summary': current,
    'all44_review_ledger_labels_present': True,
    'compact_own_parent': parent,
    'older_own_paths_bound_transitively': 522,
    'no_growing_historical_inventory_recopy_or_recursive_rehash': True,
    'no_NEW_peer_R13_report_findings_source_metadata_read_or_hashed': True,
    'no_math_code_CAS_scan_constructor_rerun_or_certificate_replay': True,
}
write_new(validation_path, validation)
suffixes = ['baseline-v1.json', 'initial.md', 'ledger-v1.md', 'issues-v1.md',
            'source-checks-v1.md', 'sources-v1.json', 'worklog-v1.md',
            'freeze-v1.py', 'input-validation-v1.json']
artifacts = [record(PREFIX + name) for name in suffixes]
manifest_path = PREFIX + 'manifest-v1.json'
manifest = {
    'frozen_utc': now,
    'status': 'COMPLETE initially blind OTHER NONCONSTRUCTOR ENTIRE WHOLE R13 R1 initial',
    'reviewer': '/root/review_2022_complexity_r2',
    'exact_target': target,
    'constructor_freeze': constructor_freeze,
    'all_R13A_R13B_R13C_and_all44_obligations_reconstructed': True,
    'entire_hand_quartic_certificate_scaling_actual_fork_and_full_gcd_checked': True,
    'unresolved_substantive_issues': 0,
    'required_author_mathematical_repairs': 0,
    'retained_nonblocking_scope_notes': 5,
    'not_coordinator_promotion_or_external_validation': True,
    'no_full_m5_T4_impossibility_J15_degree20_annual_lift_height_or_novelty_claim': True,
    'NEW_root_R13_reports_findings_ledgers_source_metadata_unread_unhashed_through_ENTIRE_freeze': True,
    'root_ENTIRE_completion_identity_received_without_findings': True,
    'A_NEW_constructor_excluded': True,
    'B_supplied_no_NEW_R13_inference': True,
    'old_B_R5_R6_R7_R10_R11_R12_reviews_and_separate_R9_authorship_disclosed': True,
    'no_accepted_input_self_recertification_counted': True,
    'actual_primary_read_limits_recorded': True,
    'two_OTHER_whole_audits_and_full_root_reconciliation_required': True,
    'no_math_code_CAS_scan_author_program_old_certificate_or_native_child': True,
    'no_old_candidate_peer_shared_Git_cache_edit_spawn_charge_contact_or_bypass': True,
    'current_summary': current,
    'compact_own_parent': parent,
    'older_own_paths_bound_transitively': 522,
    'new_own_files_including_manifest': 10,
    'older_plus_new_own_paths_bound_transitively': 532,
    'no_growing_historical_inventory_recopy_or_recursive_rehash': True,
    'requested_settings': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
    'independently_verified_effective_settings': None,
    'authoritative_weekly_telemetry': {
        'at_utc': '2026-10-18 01:39:45 UTC',
        'method': 'mcp__codex_app__get_usage_limits({}); codex.primary and legacy agree',
        'account_label': '029a8928…1334ac3a',
        'used_percent_TOTAL': 9,
        'window_minutes': 10080,
        'reset_unix': 1792874445,
        'ordinary_usage_allowed': True,
        'current_window_explicitly_user_authorized': True,
        'ceiling_TOTAL_percent': 90,
        'integration_reserve': True,
        'automatic_further_reset_spending': False,
    },
    'artifacts': artifacts,
}
write_new(manifest_path, manifest)
for row in artifacts:
    check(row)
for row in baseline['inputs']:
    check(row)
print(json.dumps({'manifest': record(manifest_path),
                  'initial': record(PREFIX + 'initial.md'),
                  'all44_obligations': True,
                  'all_payloads_postverified': True,
                  'current_summary': current}, indent=2))
