"""Independent metadata-only review freeze; no mathematical computation.

Does not run the constructor's freezer or any arithmetic/source program.
Only hashes files, validates compact declarations and obligation labels,
then exclusively creates this review's immutable administrative outputs.
"""
from pathlib import Path
import datetime
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = 'problems/2020-B4/reviews/reasoning-arithmetic-return-r9-review-2-'
FORBIDDEN = 'problems/2020-B4/reviews/reasoning-arithmetic-return-r9-review-1-'


def record(path):
    assert not path.startswith(FORBIDDEN), 'NEW peer review forbidden'
    assert not path.startswith('problems/2021-B4/reviews/reasoning-return-r13-review-2-')
    raw = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(raw),
            'sha256': hashlib.sha256(raw).hexdigest()}


def check(expected):
    actual = record(expected['path'])
    assert actual == {key: expected[key]
                      for key in ('path', 'bytes', 'sha256')}, expected['path']
    return actual


def write_new(path, data):
    with (ROOT / path).open('x') as output:
        output.write(json.dumps(data, indent=2) + '\n')


baseline_path = PREFIX + 'baseline-v1.json'
baseline = json.loads((ROOT / baseline_path).read_text())
assert baseline['older_own_paths_bound_transitively'] == 512
rows = [check(row) for row in baseline['inputs']]
target = check(baseline['exact_target'])
constructor_freeze = check(baseline['constructor_freeze'])
assert target['sha256'] == 'aab97b7ba5c91d17e9e82f18a58db400bcddd1afb11081917d6f12a1f31fd892'
assert constructor_freeze['sha256'] == 'c90992cdc72cc411b8dbec2b811bbd39fb3e9e948e1559dd4e6163487a4ec5ef'
parent = check(baseline['compact_own_parent'])
assert parent['sha256'] == '13f4c9b46055c02b5f535706aa338bcc5167ea719120075aa0616e1298669142'

# Verify each CURRENT accepted-copy declaration. Preserve the existing
# full verification inventories transitively; never walk new peer data.
authorities = []
for number in range(4, 9):
    path = f'problems/2020-B4/reviews/reasoning-return-r{number}-acceptance.json'
    data = json.loads((ROOT / path).read_text())
    accepted = check(data['accepted_copy'])
    rows.append(accepted)
    authorities.append({'authority': record(path), 'accepted_copy': accepted})

constructor_baseline_path = 'problems/2020-B4/notes/reasoning-arithmetic-return-r9-baseline-v1.json'
cb = json.loads((ROOT / constructor_baseline_path).read_text())
cb_rows = [check(row) for row in cb['records']]
cb_raw = json.dumps(cb_rows, sort_keys=True, separators=(',', ':')).encode()
assert hashlib.sha256(cb_raw).hexdigest() == cb['canonical_deduplicated_summary_sha256']
assert len(cb['occurrence_labels']) == cb['declared_occurrences'] == 24
assert len(cb_rows) == cb['deduplicated_paths'] == 22

unique = {}
for row in rows:
    previous = unique.setdefault(row['path'], row)
    assert previous == row
ordered = [unique[path] for path in sorted(unique)]
canonical = json.dumps(ordered, sort_keys=True, separators=(',', ':')).encode()
summary_sha = hashlib.sha256(canonical).hexdigest()
ledger = (ROOT / (PREFIX + 'ledger-v1.md')).read_text()
labels = re.findall(r'^\| (\d\d) \|', ledger, re.MULTILINE)
assert labels == [f'{i:02}' for i in range(1, 57)]
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
validation_path = PREFIX + 'input-validation-v1.json'
validation = {
    'validated_utc': now,
    'metadata_only_not_mathematical_test': True,
    'baseline': record(baseline_path),
    'exact_target': target,
    'constructor_freeze': constructor_freeze,
    'all_constructor_payload_fingerprints_match': True,
    'all_selected_old_inputs_match': True,
    'accepted_copy_authorities': authorities,
    'constructor_compact_baseline_summary_recomputed': True,
    'constructor_declared_occurrences': 24,
    'constructor_unique_paths_verified': 22,
    'fingerprint_occurrences_verified': len(rows),
    'unique_paths_verified': len(unique),
    'canonical_deduplicated_summary_sha256': summary_sha,
    'all56_ledger_IDs_present': True,
    'compact_own_parent': parent,
    'older_own_paths_bound_transitively': 512,
    'no_growing_historical_inventory_recopy_or_recursive_rehash': True,
    'no_NEW_peer_A9_or_R13_review_path_read_or_hashed': True,
    'no_math_program_CAS_scan_or_author_rerun': True,
}
write_new(validation_path, validation)

suffixes = [
    'baseline-v1.json', 'initial.md', 'ledger-v1.md', 'issues-v1.md',
    'source-checks-v1.md', 'sources-v1.json', 'worklog-v1.md',
    'freeze-v1.py', 'input-validation-v1.json',
]
artifacts = [record(PREFIX + suffix) for suffix in suffixes]
manifest_path = PREFIX + 'manifest-v1.json'
manifest = {
    'frozen_utc': now,
    'status': 'COMPLETE OTHER initially blind NONCONSTRUCTOR ENTIRE WHOLE A9 R2 initial',
    'reviewer': '/root/review_2022_complexity_r2',
    'exact_target': target,
    'constructor_freeze': constructor_freeze,
    'all_six_claims_and_all56_obligations_reconstructed': True,
    'unresolved_substantive_issues': 0,
    'required_author_repairs': 0,
    'retained_scope_notes': 5,
    'not_coordinator_promotion_or_external_validation': True,
    'no_annual_new_order_numeric_cutoff_classicality_or_novelty_claim': True,
    'NEW_root_A9_review_files_findings_sources_metadata_unread_through_ENTIRE_freeze': True,
    'root_completion_identities_received_without_findings': True,
    'NEW_root_R13_peer_review_material_also_unread': True,
    'C_NEW_constructor_excluded': True,
    'B_did_not_construct_or_contribute_NEW_A9': True,
    'B_OLD_R4_R5_R7_R8_authorship_and_R6_review_disclosed_no_self_recertification': True,
    'exact_fresh_source_proof_and_accepted_read_limits_recorded': True,
    'two_OTHER_whole_audits_and_full_root_reconciliation_required': True,
    'no_math_code_CAS_scan_classgroup_calculation_author_rerun_or_certificate_replay': True,
    'no_old_candidate_shared_Git_cache_edit_spawn_charge_contact_or_bypass': True,
    'fingerprint_occurrences_verified': len(rows),
    'unique_paths_verified': len(unique),
    'canonical_deduplicated_summary_sha256': summary_sha,
    'compact_own_parent': parent,
    'older_own_paths_bound_transitively': 512,
    'new_own_files_including_manifest': 10,
    'older_plus_new_own_paths_bound_transitively': 522,
    'no_growing_historical_inventory_recopy_or_recursive_rehash': True,
    'requested_settings': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
    'independently_verified_effective_settings': None,
    'authoritative_weekly_telemetry': {
        'at_utc': '2026-10-18 01:31:02 UTC',
        'method': 'mcp__codex_app__get_usage_limits({}); codex.primary and legacy agree',
        'account_label': '029a8928…1334ac3a',
        'used_percent_TOTAL': 8,
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
                  'all56_obligations': True,
                  'all_payloads_postverified': True,
                  'fingerprint_occurrences': len(rows),
                  'unique_paths': len(unique)}, indent=2))
