"""Administrative-only whole PUS R2 freeze; no mathematical executable."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
P = 'problems/2017-B4/reviews/coordinator-plane-recovery-r1-review-2-'
T = 'problems/2017-B4/notes/coordinator-plane-recovery-r1-'
R13 = 'problems/2021-B4/notes/reasoning-return-r13-'

def read(path):
    assert not ('coordinator-plane-recovery-r1-review-' in path
                and not path.startswith(P)), 'No NEW peer PUS access'
    return (ROOT / path).read_bytes()

def record(path):
    content = read(path)
    return dict(path=path, bytes=len(content),
                sha256=hashlib.sha256(content).hexdigest())

def verify(row):
    wanted = {k: row[k] for k in ('path', 'bytes', 'sha256')}
    assert record(row['path']) == wanted, row['path']
    return wanted

def pinned(path, size, digest):
    return verify(dict(path=path, bytes=size, sha256=digest))

def decoded(path):
    return json.loads(read(path))

def write_json(suffix, value):
    path = P + suffix
    with (ROOT / path).open('x', encoding='utf-8') as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write('\n')
    return record(path)

def unique_summary(rows):
    unique = {}
    for row in rows:
        assert unique.setdefault(row['path'], row) == row
    ordered = [unique[k] for k in sorted(unique)]
    digest = hashlib.sha256(json.dumps(
        ordered, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return dict(occurrences=len(rows), unique_paths=len(unique),
                canonical_deduplicated_sha256=digest)

for suffix in ('input-validation-v1.json', 'freeze-output-v1.json',
               'manifest-v1.json'):
    assert not (ROOT / (P + suffix)).exists(), 'Never overwrite frozen files'

target_manifest = pinned(
    T + 'freeze-v1.json', 2239,
    '19c9c464f0c1f60000113b7a71ff3076d4501a23e1099671ff66b91cadf5a515')
pinned(T + 'candidate-v1.md', 12840,
       'c156e2e2c26559bf5c5c7f9f29ecb0fc333d2582c58ce271fa09821087b1bd2d')
target = decoded(target_manifest['path'])
assert target['whole_obligations'] == 36
assert len(target['artifacts']) == 7
target_rows = [verify(x) for x in target['artifacts']] + [target_manifest]

target_validation = decoded(T + 'input-validation-v1.json')
input_rows = [verify(x) for x in target_validation['records']]
input_summary = unique_summary(input_rows)
assert input_summary == {
    'occurrences': 13, 'unique_paths': 11,
    'canonical_deduplicated_sha256':
    '937e77959e1ea81d3234dab5f2e689f1fd813cb85eae7ed0f5bc870d03daaf92'}
assert input_summary == target['compact_input_summary']
assert target_validation['both_accepted_candidate_copy_suffixes_exact']

# Only the two operative authority bindings are followed. Their growing
# historical inventories are bound by the verified current metadata, not
# recursively read, rehashed, copied or represented as fresh mathematics.
acceptances = [
    'problems/2017-B4/reviews/reasoning-value-return-r6-acceptance.json',
    'problems/2017-B4/reviews/allD-uniform-strict-acceptance.json',
]
for path in acceptances:
    authority = decoded(path)
    assert authority['unresolved_substantive_issues'] == 0
    assert authority['repair_required'] is False
    source = verify(authority['candidate'])
    accepted = verify(authority['accepted_copy'])
    assert source in input_rows and accepted in input_rows
    assert read(accepted['path']).endswith(read(source['path']))

parent_manifest = pinned(
    R13 + 'freeze-v1.json', 4152,
    '4d6b95b7c5b70301f227af7cce5169c8c691c01f6b287fdadacf0b337c40c656')
parent = decoded(parent_manifest['path'])
assert parent['whole_obligations'] == 44
assert len(parent['artifacts']) == 10
parent_rows = [verify(x) for x in parent['artifacts']] + [parent_manifest]
assert parent['compact_current_summary'] == {
    'occurrences': 33,
    'unique_paths': 32,
    'canonical_deduplicated_summary_sha256':
    'c1d4beb5b4c668bbb077bc58520926f39c0658c25be3ef17f6f97171f257906b',
    'encoding': 'UTF8 JSON sorted unique path/bytes/sha256; sorted keys; compact separators',
    'old_parent_inventory_rows_bound_not_recopied': True,
}

obligation_ids = re.findall(
    r'^\|([0-9]{2})\|', read(T + 'obligations-v1.md').decode(), re.M)
ledger_ids = re.findall(
    r'^\|([0-9]{2})\|[^\n]*\|Closed\|$',
    read(P + 'issues-v1.md').decode(), re.M)
assert obligation_ids == ledger_ids == [f'{i:02d}' for i in range(1, 37)]

rows = target_rows + input_rows + parent_rows
summary = unique_summary(rows)
assert summary['occurrences'] == 32 and summary['unique_paths'] == 30
now = datetime.now(timezone.utc).isoformat()
groups = [
    dict(role='ENTIRE eight-file constructor target',
         metadata=target_manifest, **unique_summary(target_rows)),
    dict(role='constructor current accepted/direct inputs',
         metadata=record(T + 'input-validation-v1.json'),
         **input_summary),
    dict(role='immutable immediately preceding OWN R13; NOT a PUS premise',
         metadata=parent_manifest, **unique_summary(parent_rows),
         bound_historical_input_summary=parent['compact_current_summary'],
         historical_rows_rewalked_or_represented_as_current=False),
]
validation = write_json('input-validation-v1.json', dict(
    verified_at_utc=now, administrative_only=True,
    groups=groups, records=rows, compact_current_summary=summary,
    both_operating_accepted_candidate_copy_suffixes_exact=True,
    all36_obligation_ids_and_closed_dispositions_exact=True,
    no_NEW_peer_PUS_report_finding_ledger_source_or_metadata_read_or_hashed=True,
    old_parent_inventories_bound_not_recopied=True,
    no_mathematical_program_CAS_scan_or_author_replay=True,
    writes_only_assigned_NEW_review_prefix=True))

report = record(P + 'initial-v1.md')
ledger = record(P + 'issues-v1.md')
freeze_output = write_json('freeze-output-v1.json', dict(
    at_utc=now, report=report, ledger=ledger,
    current_summary=summary, whole_obligations=36, closed=36,
    unresolved_substantive_issues=0, required_author_repairs=0,
    closed_already_explicit_scope_notes=3,
    ENTIRE_initial_before_any_NEW_peer_PUS_access=True,
    all_current_target_inputs_parent_payloads_verified=True,
    administrative_only=True, no_promotion=True))

suffixes = ['initial-v1.md', 'issues-v1.md', 'source-checks-v1.md',
            'worklog-v1.md', 'freeze-v1.py', 'input-validation-v1.json',
            'freeze-output-v1.json']
artifacts = [record(P + suffix) for suffix in suffixes]
manifest = write_json('manifest-v1.json', dict(
    frozen_at_utc=datetime.now(timezone.utc).isoformat(),
    status='ENTIRE initially blind nonconstructor WHOLE PUS R2 initial frozen',
    reviewer='/root/review_2021_reasoning_j15_r2',
    NEW_constructor='/root', root_excluded_from_OTHER_auditor_count=True,
    old_US_authorship_and_PM_review_roles_disclosed_not_self_recertified=True,
    whole_obligations=36, closed=36,
    unresolved_substantive_issues=0, required_author_repairs=0,
    closed_already_explicit_scope_notes=['PUS-R2-N1', 'PUS-R2-N2', 'PUS-R2-N3'],
    ENTIRE_initial_before_ANY_NEW_peer_PUS_read_hash_or_finding=True,
    TWO_OTHER_entire_whole_audits_and_root_reconciliation_required=True,
    no_global_mass_upper_R_value_annual_growing_D_or_novelty_claim=True,
    requested_settings=dict(model='gpt-6.1-sol', reasoning='max', inherited=True),
    independently_verified_effective_settings=None,
    authoritative_weekly_snapshot=dict(
        tool='mcp__codex_app__get_usage_limits',
        at_utc='2026-10-18 01:24:14 UTC', total_weekly_used_percent=8,
        window_minutes=10080, reset_unix=1792874445,
        ordinary_usage_allowed=True, legacy_and_by_limit_agree=True,
        new_window_explicitly_user_authorized=True,
        ceiling_total_percent=90, integration_reserve_retained=True,
        automatic_further_reset_authorized=False),
    compact_current_summary=summary,
    compact_parent_groups=3,
    old_parent_inventory_rows_bound_not_recopied=True,
    mathematical_program_CAS_scan_author_rerun_or_old_certificate_replay=False,
    old_shared_Git_cache_writes_spawn_charge_contact_bypass=False,
    administrative_command='python3 ' + P + 'freeze-v1.py',
    artifacts=artifacts))

for item in rows + artifacts + [manifest]:
    verify(item)
assert ledger_ids == [f'{i:02d}' for i in range(1, 37)]
print(json.dumps(dict(
    ENTIRE_initial_frozen=True, manifest=manifest, report=report, ledger=ledger,
    whole_obligations=36, closed=36, substantive_issues=0, repairs=0,
    compact_current_summary=summary, all_postverified=True,
    no_peer_PUS_access=True, administrative_only=True), indent=2))
