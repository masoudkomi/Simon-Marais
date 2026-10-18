"""NEW independent review preservation helper; no mathematical computation.

Hashes only current declared immutable inputs and compact parents, and
exclusively creates own new R1 records. Does not run the author script,
follow historical inventories recursively or read NEW peer R6 material.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
OWN = 'problems/2017-B4/reviews/reasoning-value-return-r6-review-1-'
FORBIDDEN = 'problems/2017-B4/reviews/reasoning-value-return-r6-review-2-'


def file(rel):
    assert isinstance(rel, str) and not rel.startswith(FORBIDDEN), 'NEW peer-blind guard'
    p = ROOT / rel
    assert p.resolve().is_relative_to(ROOT), 'Outside workspace'
    return p


def fp(rel):
    b = file(rel).read_bytes()
    return {'path': rel, 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}


def check(row):
    expected = {k: row[k] for k in ('path', 'bytes', 'sha256')}
    assert fp(row['path']) == expected, row['path']
    return expected


def extract(value):
    result = []
    if isinstance(value, dict):
        if all(k in value for k in ('path', 'bytes', 'sha256')):
            result.append({k: value[k] for k in ('path', 'bytes', 'sha256')})
        for v in value.values():
            result.extend(extract(v))
    elif isinstance(value, list):
        for v in value:
            result.extend(extract(v))
    return result


def read_json(rel):
    return json.loads(file(rel).read_text())


def compact(rows):
    unique = {}
    for row in rows:
        assert row['path'] not in unique or unique[row['path']] == row
        unique[row['path']] = row
    canonical = [unique[k] for k in sorted(unique)]
    b = json.dumps(canonical, sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(rows), 'unique_paths': len(canonical),
            'deduplicated_summary_sha256': hashlib.sha256(b).hexdigest(),
            'encoding': 'UTF8 JSON sorted unique path/bytes/sha256; sorted keys; compact separators'}


def create(suffix, value):
    rel = OWN + suffix
    with file(rel).open('x') as stream:
        json.dump(value, stream, indent=2)
        stream.write('\n')
    return fp(rel)


target_freeze = check({
    'path': 'problems/2017-B4/notes/reasoning-value-return-r6-freeze-v1.json',
    'bytes': 3298,
    'sha256': 'aba8108ec5191eb5c6d2702944d74c340c06ff949938bbe0bcd197b34998e9d4'})
target = read_json(target_freeze['path'])
target_rows = [check(row) for row in target['artifacts']]
assert len(target_rows) == 9
assert target_rows[0] == {
    'path': 'problems/2017-B4/notes/reasoning-value-return-r6-candidate-v1.md',
    'bytes': 29992,
    'sha256': 'dbb4232858154bbbae385e16ef0444101e02c50cddbe0dbc82402166cd2869af'}

baseline_row = fp('problems/2017-B4/notes/reasoning-value-return-r6-baseline-v1.json')
baseline = read_json(baseline_row['path'])
for row in extract(baseline):
    check(row)

# Reproduce the current declared 80-record selection from immutable
# metadata roots. This is one-level declaration verification, not a
# recursion into all historical proof/review inventories.
roots = [baseline['immutable_parent']] + baseline['authoritative_acceptance_metadata']
declared = []
for root in roots:
    declared.append(check(root))
    declared.extend(extract(read_json(root['path'])))
declared.extend(baseline['explicit_inputs'])
declared = [check(row) for row in declared]
declared_summary = compact(declared)
assert declared_summary['occurrences'] == 80
assert declared_summary['unique_paths'] == 80

authorities = [check(row) for row in baseline['authoritative_acceptance_metadata']]
accepted_body_rows = []
suffix_rows = []
for auth in authorities:
    data = read_json(auth['path'])
    if 'accepted_copy' in data and 'candidate' in data:
        body, original = check(data['accepted_copy']), check(data['candidate'])
        assert file(body['path']).read_bytes().endswith(file(original['path']).read_bytes())
        accepted_body_rows.append(body)
        suffix_rows.append({'accepted': body, 'original': original,
                            'accepted_math_is_exact_original_suffix': True})
    elif 'accepted_proof' in data:
        accepted_body_rows.append(check(data['accepted_proof']))

extra_context = [
    fp('problems/2017-B4/proofs/reviewed-fixedD-structural-v1.2.md'),
    fp('problems/2017-B4/proofs/reviewed-global-value-return-r2-v1.1.md')]
assert fp('AGENTS.md')['sha256'] == '28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff'

prior = check({
    'path': 'problems/2020-B4/reviews/reasoning-return-r8-review-2-manifest-v1.json',
    'bytes': 4584,
    'sha256': 'de2dc15d7cde1a849e5dacb137051d21fde9bda3580c6e9e6c40263b6eb3cc06'})
prior_data = read_json(prior['path'])
prior_payloads = [check(row) for row in prior_data['artifacts']]
assert len(prior_payloads) == 7

ledger = file(OWN + 'issues-v1.md').read_text()
ids = re.findall(r'^\|(PM-\d\d)\|', ledger, re.MULTILINE)
assert ids == ['PM-' + str(i).zfill(2) for i in range(1, 49)]
assert 'N1: closed source-scope observation' in ledger
for suffix in ['initial-v1.md', 'issues-v1.md', 'source-checks-v1.md', 'worklog-v1.md']:
    assert file(OWN + suffix).stat().st_size > 1000

now = datetime.now(timezone.utc).isoformat()
telemetry = {
    'user_explicitly_authorized_new_reported_weekly_window': True,
    'at_utc': '2026-10-18 00:13:53 UTC', 'total_weekly_used_percent': 2,
    'window_minutes': 10080, 'reset_unix': 1792874445,
    'ordinary_usage_allowed': True, 'legacy_and_by_limit_fields_agree': True,
    'ceiling_total_percent': 90, 'integration_reserve_retained': True,
    'no_automatic_further_weekly_reset': True,
    'requested_model': 'gpt-6.1-sol', 'requested_reasoning': 'max',
    'independently_verified_effective_readback': None}

all_rows = ([target_freeze] + target_rows + [baseline_row] + declared +
            authorities + accepted_body_rows + extra_context + [prior] + prior_payloads)
all_summary = compact(all_rows)
validation = {
    'validated_at_utc': now, 'administrative_only_not_mathematical_evidence': True,
    'NEW_peer_R6_guard_applied_before_any_read_or_hash': True,
    'constructor_freeze': target_freeze,
    'constructor_payloads_verified': len(target_rows),
    'constructor_full_packet_compact_summary': compact([target_freeze] + target_rows),
    'constructor_baseline_parent': baseline_row,
    'necessary_declared_parent_selection_verified': declared_summary,
    'authoritative_acceptance_metadata': authorities,
    'exact_current_accepted_bodies': accepted_body_rows,
    'accepted_suffix_checks': suffix_rows,
    'additional_operative_context': extra_context,
    'constructor_historical_parent_bound_not_recopied': {
        'parent': baseline['immutable_parent'],
        'earlier_own_paths': baseline['earlier_own_paths_bound_by_parent'],
        'historical_inventory_not_recursively_replayed': True},
    'immutable_own_prior_review_parent': prior,
    'own_prior_payloads_checked': compact(prior_payloads),
    'own_prior_history_bound_transitively_not_copied': prior_data['compact_current_input_validation_summary'],
    'all_current_inputs_compact_summary': all_summary,
    'all_48_ledger_rows_present_once_in_order': True,
    'closed_source_scope_note_N1_preserved': True,
    'primary_pdf_native_hashes': None,
    'mathematical_program_CAS_scan_certificate_or_author_rerun_count': 0,
    'no_old_shared_Git_cache_edit_spawn_contact_charge_or_bypass': True,
    'NF_new_2024_packet_unopened_until_this_entire_initial_freeze': True,
    'weekly_budget_and_settings': telemetry}
validation_row = create('input-validation-v1.json', validation)

output = {
    'completed_at_utc': now, 'exit_status': 0,
    'whole_PM1_PM2_PM3_PM4_and_all_48_obligations_complete': True,
    'individual_ledger_dispositions': 48,
    'substantive_defects': 0, 'required_repairs': 0, 'open_issues': 0,
    'closed_source_scope_observations': ['N1 finite convexification versus ambient finite-angle convention'],
    'NEW_peer_R6_read_hash_or_finding_count': 0,
    'mathematical_program_count': 0,
    'constructor_frozen_records_unchanged': 10,
    'own_prior_review_frozen_records_unchanged': 8,
    'all_current_inputs_compact_summary': all_summary,
    'not_a_promotion_or_annual_value_claim': True}
output_row = create('freeze-output-v1.json', output)

payloads = [fp(OWN + suffix) for suffix in [
    'initial-v1.md', 'issues-v1.md', 'source-checks-v1.md',
    'worklog-v1.md', 'freeze-v1.py']]
payloads += [validation_row, output_row]
manifest = {
    'frozen_at_utc': now,
    'status': 'ENTIRE initially blind nonconstructor WHOLE R1 complete; coordinator reconciliation pending',
    'reviewer': '/root/review_2021_reasoning_j15_r2',
    'requested_settings': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
    'independently_verified_effective_settings': None,
    'target': target_rows[0], 'constructor_freeze': target_freeze,
    'whole_claims': ['PM1', 'PM2', 'PM3', 'PM4'],
    'all_author_obligations': 48, 'individual_ledger_dispositions': 48,
    'substantive_defects': 0, 'required_repairs': 0, 'open_issues': 0,
    'closed_source_scope_observations': ['N1 finite convexification versus ambient finite-angle convention'],
    'recommendation': 'Accept only exact scoped PM1--PM4 after two OTHER whole audits and coordinator reconciliation; no upper R/numerical/annual claim',
    'root_and_C_contributors_excluded': True,
    'old_S_D_HC_EC_construction_and_G_GR_review_roles_disclosed': True,
    'no_NEW_R6_construction_contribution': True,
    'ENTIRE_initial_blind_to_all_NEW_B_R6_reports_ledgers_sources_metadata_and_findings': True,
    'not_a_promotion': True,
    'current_input_summary': all_summary,
    'immutable_own_prior_parent': prior,
    'weekly_budget_and_settings': telemetry,
    'administrative_command': 'python3 ' + OWN + 'freeze-v1.py',
    'no_mathcode_scan_CAS_author_rerun_shared_Git_cache_edit_spawn_contact_charge_or_bypass': True,
    'artifacts': payloads}
manifest_row = create('manifest-v1.json', manifest)

# Independent post-freeze reread; immutable old records and all own
# payloads are checked without writing them again.
for row in payloads + [target_freeze] + target_rows + [prior] + prior_payloads + declared:
    check(row)
print(json.dumps({'manifest': manifest_row,
    'own_payloads_postverified': len(payloads),
    'all_current_input_summary': all_summary,
    'constructor_records_postverified': 10,
    'own_prior_records_postverified': 8,
    'necessary_declared_parent_records_postverified': len(declared),
    'no_postfreeze_mutation': True}, indent=2))
