"""Metadata-only immutable constructor freezer. No mathematical program.

Checks exact compact preservation inputs, direct accepted-authority
fingerprints, and presence/count of obligation labels. It does not run
the theoretical inverse recovery, any orbit, or any mathematical test.
Run once from the workspace root. New outputs use exclusive creation.
"""
from pathlib import Path
import datetime
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = 'problems/2022-B4/notes/reasoning-complexity-return-r9-'


def record(path):
    data = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}


def check(row):
    actual = record(row['path'])
    assert actual['bytes'] == row['bytes'], (row['path'], 'bytes')
    assert actual['sha256'] == row['sha256'], (row['path'], 'sha256')
    return actual


def write_new(path, value):
    with (ROOT / path).open('x') as stream:
        stream.write(json.dumps(value, indent=2) + '\n')


baseline_path = PREFIX + 'baseline-v1.json'
baseline = json.loads((ROOT / baseline_path).read_text())
assert baseline['older_own_paths_bound_transitively'] == 502
check(baseline['compact_own_parent'])
occurrences = [check(row) for row in baseline['inputs']]

# Read only current direct authority records. Do not recurse into their
# verification inventories or copy the preserved historical inventories.
authorities = []
for version in (8, 7, 6, 5):
    path = ('problems/2022-B4/reviews/'
            f'reasoning-return-r{version}-acceptance.json')
    data = json.loads((ROOT / path).read_text())
    current_rows = []
    for name in ('candidate', 'accepted_copy', 'verification_metadata'):
        row = data[name]
        if isinstance(row, dict) and {'path', 'bytes', 'sha256'} <= row.keys():
            current_rows.append(check(row))
    occurrences.extend(current_rows)
    authorities.append({
        'authority': record(path),
        'direct_records_verified': current_rows,
        'historical_verified_occurrences_as_declared_not_replayed':
            data.get('record_occurrences_verified'),
        'historical_unique_paths_as_declared_not_replayed':
            data.get('unique_paths_verified'),
    })

unique = {}
for row in occurrences:
    previous = unique.setdefault(row['path'], row)
    assert previous == row, ('conflicting fingerprint', row['path'])
canonical = [unique[path] for path in sorted(unique)]
summary_bytes = json.dumps(canonical, sort_keys=True,
                           separators=(',', ':')).encode()
obligations = (ROOT / (PREFIX + 'obligations-v1.md')).read_text()
labels = re.findall(r'^\| (QO\d\d) \|', obligations, flags=re.MULTILINE)
assert labels == [f'QO{i:02}' for i in range(1, 49)]
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
validation_path = PREFIX + 'input-validation-v1.json'
validation = {
    'validated_utc': now,
    'metadata_only_not_math_verification': True,
    'baseline': record(baseline_path),
    'all_baseline_inputs_preserved': True,
    'direct_current_authorities': authorities,
    'fingerprint_occurrences_verified': len(occurrences),
    'unique_paths_verified': len(unique),
    'canonical_deduplicated_summary_sha256':
        hashlib.sha256(summary_bytes).hexdigest(),
    'declared_obligations_present': len(labels),
    'compact_own_parent': baseline['compact_own_parent'],
    'older_own_paths_bound_transitively': 502,
    'no_historical_inventory_recopy_or_recursive_rehash': True,
    'no_mathematical_code_CAS_or_author_rerun': True,
}
write_new(validation_path, validation)

suffixes = [
    'baseline-v1.json', 'candidate-v1.md', 'obligations-v1.md',
    'failed-routes-v1.md', 'source-audit-v1.md', 'sources-v1.json',
    'worklog-v1.md', 'freeze-v1.py', 'input-validation-v1.json',
]
artifacts = [record(PREFIX + suffix) for suffix in suffixes]
manifest_path = PREFIX + 'freeze-v1.json'
manifest = {
    'frozen_utc': now,
    'status': 'candidate proof - unverified; COMPLETE Q1-Q4 constructor checkpoint',
    'constructor': '/root/review_2022_complexity_r2',
    'new_claims': [
        'Q1 full ordinary Z2 surjectivity and exact one/two-point inverse fibers',
        'Q2 full diagonal-image singleton fibers and actual predecessor obstruction',
        'Q3 ordinary positive strip-preserving smaller predecessors in stated central range',
        'Q4 exact equivalence with explicit unbounded residual seed set',
    ],
    'all_48_obligations': True,
    'full_proof_failed_routes_sources_worklog_present': True,
    'no_survivor_or_residual_family_hitting_or_annual_solution_or_novelty_claim': True,
    'two_OTHER_fresh_initially_blind_WHOLE_audits_required': True,
    'coordinator_prompt_supplies_no_new_Q1_Q4_inference': True,
    'constructor_old_R3_F5_authorship_and_other_review_roles_disclosed': True,
    'queued_2020_R9_target_and_NEW_peer_audit_material_unopened_through_freeze': True,
    'mathematical_computation_CAS_scan_or_certificate_rerun': False,
    'inverse_three_candidate_procedure_executed': False,
    'old_shared_Git_cache_edit_spawn_charge_contact_or_bypass': False,
    'preliminary_a_proof_reproduced_or_investigated': False,
    'actual_fresh_source_read_limits_recorded': True,
    'compact_own_parent': baseline['compact_own_parent'],
    'older_own_paths_bound_transitively': 502,
    'new_own_files_including_manifest': 10,
    'older_plus_new_own_paths_bound_transitively': 512,
    'fingerprint_occurrences_verified': len(occurrences),
    'unique_paths_verified': len(unique),
    'canonical_deduplicated_summary_sha256':
        hashlib.sha256(summary_bytes).hexdigest(),
    'requested_settings': {'model': 'gpt-6.1-sol', 'reasoning': 'max',
                           'inherited': True},
    'independently_verified_effective_settings': None,
    'authoritative_weekly_telemetry': {
        'at_utc': '2026-10-18 01:23:59 UTC',
        'method': 'mcp__codex_app__get_usage_limits({}); codex.primary and legacy agree',
        'account_label': '029a8928…1334ac3a',
        'used_percent_total': 8,
        'window_minutes': 10080,
        'reset_unix': 1792874445,
        'ordinary_usage_allowed': True,
        'new_window_explicitly_user_authorized': True,
        'total_ceiling_percent': 90,
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
                  'candidate': record(PREFIX + 'candidate-v1.md'),
                  'obligations': len(labels),
                  'occurrences': len(occurrences),
                  'unique_paths': len(unique),
                  'all_payloads_postverified': True}, indent=2))
