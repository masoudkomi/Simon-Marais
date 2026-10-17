"""Administrative preservation/freeze only. No mathematical calculation.

This is independent reviewer code, not an author-script replay. It reads
declared bytes, hashes and structure, and exclusively creates NEW records
in the assigned R2 prefix. It refuses NEW peer R8 paths before reading.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PREFIX = 'problems/2020-B4/reviews/reasoning-return-r8-review-2-'
PEER = 'problems/2020-B4/reviews/reasoning-return-r8-review-1-'


def safe_path(rel):
    assert isinstance(rel, str) and not rel.startswith(PEER), 'Peer-blind guard'
    p = ROOT / rel
    assert p.resolve().is_relative_to(ROOT), 'Outside workspace'
    return p


def fingerprint(rel):
    data = safe_path(rel).read_bytes()
    return {'path': rel, 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}


def verify(row):
    actual = fingerprint(row['path'])
    assert actual == {k: row[k] for k in ('path', 'bytes', 'sha256')}, row['path']
    return actual


def rows_in(value):
    out = []
    if isinstance(value, dict):
        if all(k in value for k in ('path', 'bytes', 'sha256')):
            out.append({k: value[k] for k in ('path', 'bytes', 'sha256')})
        for item in value.values():
            out.extend(rows_in(item))
    elif isinstance(value, list):
        for item in value:
            out.extend(rows_in(item))
    return out


def summary(rows):
    unique = {}
    for row in rows:
        if row['path'] in unique:
            assert unique[row['path']] == row, 'Conflicting declared fingerprints'
        unique[row['path']] = row
    compact = [unique[p] for p in sorted(unique)]
    encoded = json.dumps(compact, sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(rows), 'unique_paths': len(compact),
            'canonical_deduplicated_summary_sha256': hashlib.sha256(encoded).hexdigest(),
            'canonical_encoding': 'UTF8 JSON sorted unique path/bytes/sha256, sorted keys, compact separators'}


def load(rel):
    return json.loads(safe_path(rel).read_text())


def create(suffix, value):
    rel = PREFIX + suffix
    with safe_path(rel).open('x') as f:
        json.dump(value, f, indent=2)
        f.write('\n')
    return fingerprint(rel)


constructor_freeze = verify({
    'path': 'problems/2020-B4/notes/reasoning-return-r8-freeze-v1.json',
    'bytes': 5346,
    'sha256': '6f7d5060bf093304ec26a0268a8098942bd8021e99e056b1970dec12813d102e'})
constructor = load(constructor_freeze['path'])
constructor_payloads = [verify(row) for row in constructor['artifacts']]
assert len(constructor_payloads) == 11
assert constructor_payloads[0] == {
    'path': 'problems/2020-B4/notes/reasoning-return-r8-candidate-v1.md',
    'bytes': 25948,
    'sha256': '2eb3bbc51c282619a4bf0bf2b34f083c9c65abd7b27822355cd4973f391637d8'}

baseline_rel = 'problems/2020-B4/notes/reasoning-return-r8-baseline-v1.json'
baseline_parent = fingerprint(baseline_rel)
baseline = load(baseline_rel)
baseline_all_rows = [verify(row) for row in rows_in(baseline)]
# The author's 54-row selected summary does not count its two separately
# repeated compact parent references. Verify those too, but compare the
# declared summary using its exact selected groups, rather than all 56
# syntactic occurrences. Both have the same 40-path deduplicated digest.
baseline_rows = []
for key in ['exact_accepted_R7', 'direct_scope_context_and_failed_route_records',
            'R7_accepted_authority_declared_records', 'R7_immutable_metadata_parents',
            'R7_declared_frozen_artifacts_unchanged', 'own_parent_new_records']:
    baseline_rows.extend(rows_in(baseline[key]))
baseline_summary = summary(baseline_rows)
assert baseline_summary['occurrences'] == 54
assert baseline_summary['unique_paths'] == 40
assert baseline_summary['canonical_deduplicated_summary_sha256'] == 'ca15e48c25e05be93a48e37a92706b9346bd958abe079445f7d47b412b045aff'

input_parent = fingerprint('problems/2020-B4/notes/reasoning-return-r8-input-validation-v1.json')
author_input = load(input_parent['path'])
assert summary(baseline_rows + author_input['new_constructor_records']) == author_input['all_current_input_and_new_record_summary']
for row in author_input['new_constructor_records']:
    verify(row)

accepted_authority_paths = [
    'problems/2020-B4/proofs/reviewed-reasoning-return-r7-v1.1.md',
    'problems/2020-B4/reviews/reasoning-return-r7-acceptance.md',
    'problems/2020-B4/reviews/reasoning-return-r7-acceptance.json',
    'problems/2020-B4/reviews/reasoning-return-r7-acceptance-integrity.json']
accepted_authority = [fingerprint(rel) for rel in accepted_authority_paths]
r7_acceptance = load(accepted_authority_paths[2])
r7_metadata_rows = [verify(row) for row in rows_in(r7_acceptance)]
assert safe_path(accepted_authority_paths[0]).read_bytes().endswith(
    safe_path('problems/2020-B4/notes/reasoning-return-r7-candidate-v1.md').read_bytes())
assert safe_path('problems/2020-B4/proofs/reviewed-reasoning-return-r5-v1.1.md').read_bytes().endswith(
    safe_path('problems/2020-B4/notes/reasoning-return-r5-candidate-v1.md').read_bytes())

context_paths = [
    'AGENTS.md',
    'problems/2020-B4/statement.md',
    'problems/2020-B4/proofs/reviewed-partial-v1.1.md',
    'problems/2020-B4/proofs/partial-v1.md',
    'problems/2020-B4/notes/reviewed-source-clarifications-v1.md']
context_rows = [fingerprint(rel) for rel in context_paths]
assert context_rows[0]['sha256'] == '28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff'
assert context_rows[3]['sha256'] == 'f53945e49bd626847e52a61f7e39e96defd2ae44900f9d235c2c14e720f41525'

own_parent = verify({
    'path': 'problems/2021-B4/notes/reasoning-return-r11-freeze-v1.json',
    'bytes': 3477,
    'sha256': 'c0b3a0650274e899fb97f84ec042e1edb9d5e6db0f603c7f22ee5bd691e12ca4'})
own_parent_data = load(own_parent['path'])
own_parent_payloads = [verify(row) for row in own_parent_data['artifacts']]
assert len(own_parent_payloads) == 10

issue_text = safe_path(PREFIX + 'issues-v1.md').read_text()
obligation_ids = re.findall(r'^\|(R8-\d\d)\|', issue_text, re.MULTILINE)
assert obligation_ids == ['R8-' + str(i).zfill(2) for i in range(1, 55)]
for rel in ['initial-v1.md', 'issues-v1.md', 'source-checks-v1.md', 'worklog-v1.md']:
    assert safe_path(PREFIX + rel).stat().st_size > 1000

now = datetime.now(timezone.utc).isoformat()
telemetry = {
    'method': 'functions.exec -> tools.mcp__codex_app__get_usage_limits({}); tools.clock__curr_time({})',
    'last_consistent_direct_snapshot': {'at_utc': '2026-10-17 20:39:15 UTC', 'used_percent_total': 65,
       'window_minutes': 10080, 'reset_unix': 1792745187, 'legacy_and_by_limit_agree': True},
    'conflicting_same_account_direct_snapshot': {'at_utc': '2026-10-17 20:43:51 UTC', 'used_percent_total': 0,
       'window_minutes': 10080, 'reset_unix': 1792874445, 'legacy_and_by_limit_agree': True},
    'account_suffix': 'ac3a', 'weekly_total_ceiling_percent': 90,
    'new_window_or_fresh_allowance_NOT_assumed': True,
    'root_authorized_only_completion_of_already_underway_entire_audit_using_reserve': True,
    'queued_2017_R6_unopened_and_not_started_until_budget_continuation_resolved': True}

all_input_rows = ([constructor_freeze] + constructor_payloads + baseline_all_rows +
                  [baseline_parent, input_parent] + r7_metadata_rows + accepted_authority +
                  context_rows + [own_parent] + own_parent_payloads)
all_summary = summary(all_input_rows)
validation = {
    'validated_at_utc': now,
    'administrative_only_not_mathematical_evidence': True,
    'new_peer_R8_material_guarded_before_any_read_or_hash': True,
    'constructor_freeze': constructor_freeze,
    'constructor_payloads_verified': len(constructor_payloads),
    'constructor_payloads_and_freeze_summary': summary([constructor_freeze] + constructor_payloads),
    'necessary_old_declared_baseline_parent': baseline_parent,
    'necessary_old_declared_baseline_verified': baseline_summary,
    'all_syntactic_baseline_declarations_including_two_repeated_parent_references_verified': summary(baseline_all_rows),
    'constructor_input_metadata_parent': input_parent,
    'constructor_current_63_occurrences_49_paths_digest_reproduced': author_input['all_current_input_and_new_record_summary'],
    'exact_accepted_R7_authority': accepted_authority,
    'accepted_R7_direct_metadata_declarations_verified': summary(r7_metadata_rows),
    'accepted_R7_full_math_is_exact_frozen_candidate_suffix': True,
    'accepted_R5_full_math_is_exact_frozen_candidate_suffix': True,
    'R7_historical_acceptance_inventory_bound_not_recopied': {
        'occurrences': r7_acceptance['record_occurrences_verified'],
        'unique_paths': r7_acceptance['unique_paths_verified']},
    'additional_official_and_accepted_context': context_rows,
    'immutable_own_prior_constructor_parent': own_parent,
    'own_prior_payloads_verified': summary(own_parent_payloads),
    'own_prior_older_preservation_bound_transitively_not_replayed': own_parent_data['compact_input_summary'],
    'all_currently_reverified_input_occurrences_compact_summary': all_summary,
    'all_54_issue_rows_present_once_in_order': True,
    'all_old_bytes_declared_here_unchanged': True,
    'no_recursive_historical_inventory_copy_or_claim_of_unrelated_fresh_math_read': True,
    'mathematical_program_CAS_scan_or_author_rerun_count': 0,
    'new_primary_PDF_download_and_invented_native_hash_count': 0,
    'no_old_shared_Git_cache_mutation_spawn_contact_charge_or_bypass': True,
    'weekly_telemetry_conflict_and_stop': telemetry}
validation_row = create('input-validation-v1.json', validation)

output = {
    'completed_at_utc': now, 'exit_status': 0,
    'administrative_preservation_only': True,
    'entire_R8A_through_R8F_and_all_54_obligations_complete': True,
    'whole_initial_source_and_issue_records_complete_before_peer_comparison': True,
    'substantive_defects_found': 0, 'required_repairs': 0, 'advisories_requiring_action': 0,
    'candidate_and_necessary_old_declared_bytes_unchanged': True,
    'current_input_summary': all_summary,
    'new_peer_R8_read_or_hash_count': 0,
    'mathematical_program_count': 0,
    'not_an_acceptance_or_annual_solution': True,
    'queued_2017_R6_not_started_budget_hold': True}
output_row = create('freeze-output-v1.json', output)

artifacts = [fingerprint(PREFIX + suffix) for suffix in [
    'initial-v1.md', 'issues-v1.md', 'source-checks-v1.md', 'worklog-v1.md', 'freeze-v1.py']]
artifacts += [validation_row, output_row]
manifest = {
    'frozen_at_utc': now,
    'status': 'COMPLETE initially blind nonconstructor WHOLE R2 initial audit; coordinator reconciliation pending',
    'reviewer': '/root/review_2021_reasoning_j15_r2',
    'requested_settings': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
    'independently_verified_effective_settings': None,
    'target': constructor_payloads[0], 'constructor_freeze': constructor_freeze,
    'whole_claims': ['R8A', 'R8B', 'R8C', 'R8D', 'R8E', 'R8F'],
    'all_author_obligations': 54, 'individual_issue_dispositions': 54,
    'whole_reconstruction_complete': True,
    'substantive_defects_found': 0, 'required_repairs': 0, 'advisories_requiring_action': 0,
    'recommendation': 'Accept only precise scoped R8A--F after coordinator reconciliation of two OTHER whole audits; no annual or new-order claim',
    'entire_initial_blind_to_all_NEW_peer_R8_reports_ledger_sources_metadata_and_findings': True,
    'older_R3_and_R5_review_roles_disclosed_not_fresh_self_recertification': True,
    'no_NEW_R8_construction_contribution': True,
    'not_a_promotion': True,
    'compact_current_input_validation_summary': all_summary,
    'immutable_own_prior_parent': own_parent,
    'weekly_telemetry_conflict_and_stop': telemetry,
    'administrative_command': 'python3 ' + PREFIX + 'freeze-v1.py',
    'no_mathcode_CAS_scan_author_rerun_shared_Git_cache_edit_spawn_contact_charge_or_bypass': True,
    'artifacts': artifacts}
manifest_row = create('manifest-v1.json', manifest)

# Completion is established by rereading every own payload after the manifest
# exists; nothing is edited during the post-freeze check.
for row in artifacts:
    verify(row)
verify(constructor_freeze)
for row in constructor_payloads:
    verify(row)
verify(own_parent)
for row in own_parent_payloads:
    verify(row)
print(json.dumps({'manifest': manifest_row, 'all_own_payloads_postverified': len(artifacts),
                  'constructor_frozen_records_postverified': 12,
                  'own_prior_frozen_records_postverified': 11,
                  'no_postfreeze_mutation': True}, indent=2))
