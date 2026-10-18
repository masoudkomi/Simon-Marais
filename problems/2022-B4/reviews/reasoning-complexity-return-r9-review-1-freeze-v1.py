"""Administrative-only immutable Q1-Q4 whole review freeze, no mathematics."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
P = 'problems/2022-B4/reviews/reasoning-complexity-return-r9-review-1-'
T = 'problems/2022-B4/notes/reasoning-complexity-return-r9-'
OWN_PARENT = 'problems/2017-B4/reviews/coordinator-plane-recovery-r1-review-2-'

def read(path):
    if path.startswith('problems/2022-B4/reviews/') and (
        'reasoning-complexity-return-r9-review-' in path
        or 'reasoning-return-r9-review-' in path):
        assert path.startswith(P), 'No NEW peer2022 R9 access'
    return (ROOT / path).read_bytes()

def record(path):
    content = read(path)
    return dict(path=path, bytes=len(content),
                sha256=hashlib.sha256(content).hexdigest())

def verify(row):
    expected = {key: row[key] for key in ('path', 'bytes', 'sha256')}
    assert record(row['path']) == expected, row['path']
    return expected

def pinned(path, size, sha):
    return verify(dict(path=path, bytes=size, sha256=sha))

def decoded(path):
    return json.loads(read(path))

def summarize(rows):
    unique = {}
    for row in rows:
        assert unique.setdefault(row['path'], row) == row
    ordered = [unique[key] for key in sorted(unique)]
    sha = hashlib.sha256(json.dumps(
        ordered, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return dict(occurrences=len(rows), unique_paths=len(unique),
                canonical_deduplicated_sha256=sha)

def write_new(suffix, data):
    path = P + suffix
    with (ROOT / path).open('x', encoding='utf-8') as stream:
        json.dump(data, stream, indent=2, ensure_ascii=False)
        stream.write('\n')
    return record(path)

for suffix in ('input-validation-v1.json', 'freeze-output-v1.json',
               'manifest-v1.json'):
    assert not (ROOT / (P + suffix)).exists(), 'Never overwrite frozen bytes'

target_manifest = pinned(
    T + 'freeze-v1.json', 4389,
    '13f4c9b46055c02b5f535706aa338bcc5167ea719120075aa0616e1298669142')
pinned(T + 'candidate-v1.md', 16457,
       '2fdb1a495afa4f607b9fb63b7a1535e7ba6797ae5b699fd9d25124b503bfe211')
target = decoded(target_manifest['path'])
assert target['all_48_obligations'] is True
assert len(target['artifacts']) == 9
target_rows = [verify(row) for row in target['artifacts']] + [target_manifest]
baseline = decoded(T + 'baseline-v1.json')
validation = decoded(T + 'input-validation-v1.json')
assert len(baseline['inputs']) == 23
assert verify(validation['baseline']) in target_rows
input_rows = [verify(row) for row in baseline['inputs']]

# Follow exactly the constructor's CURRENT direct authority records.
# Lists of hundreds of historical verification rows remain bound by the
# current metadata; no recursive file walk, copy or mathematical reread.
authority_bindings = []
for authority in validation['direct_current_authorities']:
    authority_record = verify(authority['authority'])
    assert authority_record in input_rows
    data = decoded(authority_record['path'])
    expected_direct = []
    for key in ('candidate', 'accepted_copy', 'verification_metadata'):
        row = data[key]
        if isinstance(row, dict) and {'path', 'bytes', 'sha256'} <= row.keys():
            expected_direct.append(verify(row))
    declared_direct = [verify(row) for row in authority['direct_records_verified']]
    assert expected_direct == declared_direct
    input_rows.extend(expected_direct)
    authority_bindings.append(dict(
        metadata=authority_record,
        direct_current_records=len(expected_direct),
        historical_occurrences_bound_not_replayed=
        authority['historical_verified_occurrences_as_declared_not_replayed'],
        historical_unique_paths_bound_not_replayed=
        authority['historical_unique_paths_as_declared_not_replayed']))

input_summary = summarize(input_rows)
assert input_summary == {
    'occurrences': 31, 'unique_paths': 27,
    'canonical_deduplicated_sha256':
    '6a55743998f896bc7d976a660d48bcb690b0213bd62bbc259b56ebbe36f1f2f1'}
assert target['fingerprint_occurrences_verified'] == input_summary['occurrences']
assert target['unique_paths_verified'] == input_summary['unique_paths']
assert target['canonical_deduplicated_summary_sha256'] == input_summary[
    'canonical_deduplicated_sha256']

own_parent_manifest = pinned(
    OWN_PARENT + 'manifest-v1.json', 3480,
    'c2d7b7cc3c8139bbd42a896f8a637c9a7616e9f0eadaaa6776c8e8be862faa99')
parent = decoded(own_parent_manifest['path'])
assert len(parent['artifacts']) == 7
parent_rows = [verify(row) for row in parent['artifacts']] + [own_parent_manifest]
assert parent['compact_current_summary'] == {
    'occurrences': 32, 'unique_paths': 30,
    'canonical_deduplicated_sha256':
    '0bd367c69b286cc250f6a277af7062386cf9db8cbe1b2c096747c107f47a63ca'}

target_ids = re.findall(
    r'^\| (QO[0-9]{2}) \|', read(T + 'obligations-v1.md').decode(), re.M)
review_ids = re.findall(
    r'^\|(QO[0-9]{2})\|[^\n]*\|Closed\|$',
    read(P + 'issues-v1.md').decode(), re.M)
assert target_ids == review_ids == [f'QO{i:02d}' for i in range(1, 49)]

rows = target_rows + input_rows + parent_rows
summary = summarize(rows)
assert summary['occurrences'] == 49 and summary['unique_paths'] == 45
now = datetime.now(timezone.utc).isoformat()
groups = [
    dict(role='ENTIRE ten-file constructor target', metadata=target_manifest,
         **summarize(target_rows)),
    dict(role='constructor31 CURRENT input occurrences',
         metadata=record(T + 'input-validation-v1.json'), **input_summary,
         historical_inventory_rows_rewalked_or_copied=False),
    dict(role='immediate immutable OWN PUS whole initial; NOT a Q premise',
         metadata=own_parent_manifest, **summarize(parent_rows),
         historical_summary_bound_not_replayed=parent['compact_current_summary']),
]
input_validation = write_new('input-validation-v1.json', dict(
    verified_at_utc=now, administrative_only=True,
    groups=groups, current_authority_bindings=authority_bindings,
    records=rows, compact_current_summary=summary,
    all48_exact_obligation_ids_and_closed_review_dispositions=True,
    all_target_payloads_current_direct_inputs_and_own_parent_verified=True,
    no_NEW_peer2022_R9_report_finding_ledger_source_or_metadata_read_or_hashed=True,
    old_historical_inventories_bound_not_recopied_or_rewalked=True,
    mathematical_executable_CAS_scan_inverse_procedure_or_author_rerun=False,
    writes_only_assigned_NEW_review_prefix=True))

report = record(P + 'initial-v1.md')
ledger = record(P + 'issues-v1.md')
freeze_output = write_new('freeze-output-v1.json', dict(
    at_utc=now, report=report, ledger=ledger,
    compact_current_summary=summary,
    whole_obligations=48, closed=48,
    unresolved_substantive_issues=0, required_author_repairs=0,
    closed_already_explicit_scope_notes=3,
    ENTIRE_initial_before_ANY_NEW_peer_R9_access=True,
    all_current_inputs_preserved=True, administrative_only=True,
    no_promotion_or_annual_solution=True))

suffixes = ['initial-v1.md', 'issues-v1.md', 'source-checks-v1.md',
            'worklog-v1.md', 'freeze-v1.py', 'input-validation-v1.json',
            'freeze-output-v1.json']
artifacts = [record(P + suffix) for suffix in suffixes]
manifest = write_new('manifest-v1.json', dict(
    frozen_at_utc=datetime.now(timezone.utc).isoformat(),
    status='ENTIRE initially blind nonconstructor WHOLE2022 Q1-Q4 R1 frozen',
    reviewer='/root/review_2021_reasoning_j15_r2',
    NEW_constructor='/root/review_2022_complexity_r2',
    constructor_excluded_from_TWO_OTHER_whole_audits=True,
    reviewer_old_R6_authorship_and_prior_review_roles_disclosed=True,
    no_NEW_Q1_Q4_construction_contribution=True,
    whole_obligations=48, closed=48,
    unresolved_substantive_issues=0, required_author_repairs=0,
    closed_already_explicit_scope_notes=['Q9-R1-N1', 'Q9-R1-N2', 'Q9-R1-N3'],
    ENTIRE_initial_before_ANY_NEW_C_R9_report_finding_source_ledger_or_metadata=True,
    TWO_OTHER_whole_audits_and_root_reconciliation_required=True,
    preliminary_a_proof_investigated_or_reproduced=False,
    no_residual_family_hitting_survivor_annual_or_novelty_claim=True,
    requested_settings=dict(model='gpt-6.1-sol', reasoning='max', inherited=True),
    independently_verified_effective_settings=None,
    fresh_web_primary_scopes=[
        dict(url='https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2022-paper-b.pdf',
             scope='actual page2 B4 lines58-70; operative official b domain'),
        dict(url='https://austms.org.au/wp-content/uploads/2023/04/501Web.pdf',
             scope='actual printed pp29-30 B4 lines1167-1209; attributed strip context only')],
    no_new_pdf_download_cache_write_or_fabricated_original_hash=True,
    authoritative_weekly_snapshot=dict(
        tool='mcp__codex_app__get_usage_limits',
        at_utc='2026-10-18 01:30:53 UTC', total_weekly_used_percent=8,
        window_minutes=10080, raw_reported_reset_unix=1792874446,
        preceding_authorized_reset_unix=1792874445,
        reported_boundary_drift_seconds=1,
        root_explicit_current_window_boundary_drift_disposition=True,
        ordinary_usage_allowed=True, legacy_and_by_limit_agree=True,
        new_window_explicitly_user_authorized=True,
        ceiling_total_percent=90, integration_reserve_retained=True,
        automatic_later_reset_spending_authorized=False),
    compact_current_summary=summary, compact_parent_groups=3,
    old_inventory_rows_bound_not_recopied=True,
    mathematical_executable_CAS_scan_inverse_procedure_or_author_rerun=False,
    old_shared_Git_cache_writes_spawn_contact_charge_or_bypass=False,
    administrative_command='python3 ' + P + 'freeze-v1.py',
    artifacts=artifacts))

for item in rows + artifacts + [manifest]:
    verify(item)
print(json.dumps(dict(
    ENTIRE_initial_frozen=True, manifest=manifest, report=report, ledger=ledger,
    whole_obligations=48, closed=48, substantive_issues=0, required_repairs=0,
    compact_current_summary=summary, all_postverified=True,
    no_NEW_peer2022_R9_access=True, administrative_only=True), indent=2))
