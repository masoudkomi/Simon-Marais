"""Administrative-only immutable R14 freeze; no mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
P = 'problems/2021-B4/notes/reasoning-return-r14-'
R13 = 'problems/2021-B4/notes/reasoning-return-r13-'
OWN_PARENT = 'problems/2022-B4/reviews/reasoning-complexity-return-r9-review-1-'

def read(path):
    assert not path.startswith('problems/2021-B4/reviews/reasoning-return-r13-'), \
        'No NEW R13 peer review or metadata access'
    if path.startswith('problems/2022-B4/reviews/') and (
        'reasoning-complexity-return-r9-review-' in path
        or 'reasoning-return-r9-review-' in path):
        assert path.startswith(OWN_PARENT), 'No NEW C2022R9 peer access'
    return (ROOT / path).read_bytes()

def record(path):
    data = read(path)
    return dict(path=path, bytes=len(data), sha256=hashlib.sha256(data).hexdigest())

def verify(row):
    wanted = {key: row[key] for key in ('path', 'bytes', 'sha256')}
    assert record(row['path']) == wanted, row['path']
    return wanted

def pinned(path, size, sha):
    return verify(dict(path=path, bytes=size, sha256=sha))

def decoded(path):
    return json.loads(read(path))

def summarize(rows):
    unique = {}
    for row in rows:
        assert unique.setdefault(row['path'], row) == row
    canonical = [unique[path] for path in sorted(unique)]
    sha = hashlib.sha256(json.dumps(
        canonical, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return dict(occurrences=len(rows), unique_paths=len(unique),
                canonical_deduplicated_sha256=sha)

def write_new(suffix, value):
    path = P + suffix
    with (ROOT / path).open('x', encoding='utf-8') as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write('\n')
    return record(path)

for suffix in ('input-validation-v1.json', 'freeze-output-v1.json', 'freeze-v1.json'):
    assert not (ROOT / (P + suffix)).exists(), 'Never overwrite a frozen packet'

rows = []
groups = []
protocol = [
    pinned('AGENTS.md', 4707,
           '28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff'),
    pinned('problems/2021-B4/statement.md', 1745,
           '5cd9750a2458191370590120fb4ae7d547740784eb1de38ee9e2e7890a2fabed'),
]
rows.extend(protocol)
groups.append(dict(role='protocol and official domain', **summarize(protocol)))

for version, size, sha, old_group_digest in [
    (8, 2507, 'b5ca7a381393061192beceb0b34b8222c6ae249f1edc3383ac316786c7cd3ef0',
     '805900a0e77fef8e284779d44d1b427d3c9fd8c7013d050008d6e7a171a834ad'),
    (12, 2801, '28f2a33fd4cdb39bcd899df9bb450628e928afe483f7a6be443a32d649dbd00b',
     '0119fb763929cf40e0950082ae7437a2a3f493bc8f22321898ccf7b02de38d32'),
]:
    path = f'problems/2021-B4/reviews/reasoning-return-r{version}-acceptance.json'
    authority_record = pinned(path, size, sha)
    authority = decoded(path)
    assert authority['unresolved_substantive_issues'] == 0
    assert authority['repair_required'] is False
    source = verify(authority['candidate'])
    accepted = verify(authority['accepted_copy'])
    assert read(accepted['path']).endswith(read(source['path']))
    group_rows = [authority_record,
                  record(path.removesuffix('.json') + '.md'), source, accepted]
    group_summary = summarize(group_rows)
    assert group_summary['canonical_deduplicated_sha256'] == old_group_digest
    rows.extend(group_rows)
    groups.append(dict(role=f'operative accepted R{version}',
                       metadata=authority_record, **group_summary,
                       exact_candidate_copy_suffix=True,
                       historical_occurrences_bound_not_replayed=
                       authority['record_occurrences_verified'],
                       historical_paths_bound_not_replayed=
                       authority['unique_paths_verified']))

proposed_manifest = pinned(
    R13 + 'freeze-v1.json', 4152,
    '4d6b95b7c5b70301f227af7cce5169c8c691c01f6b287fdadacf0b337c40c656')
proposed = decoded(proposed_manifest['path'])
assert len(proposed['artifacts']) == 10
proposed_rows = [proposed_manifest] + [verify(row) for row in proposed['artifacts']]
rows.extend(proposed_rows)
groups.append(dict(
    role='immutable PROPOSED R13C premise used ONLY in conditional R14D',
    metadata=proposed_manifest, **summarize(proposed_rows),
    historical_summary_bound_not_replayed=proposed['compact_current_summary'],
    accepted_status_not_assumed=True, NEW_peer_reports_unread_unhashed=True))

parent_manifest = pinned(
    OWN_PARENT + 'manifest-v1.json', 4265,
    '19688a525ac39b152e8db716b025204de135055c1d7045fb423f04eb0ae78ed8')
parent = decoded(parent_manifest['path'])
assert len(parent['artifacts']) == 7
parent_rows = [parent_manifest] + [verify(row) for row in parent['artifacts']]
rows.extend(parent_rows)
groups.append(dict(
    role='immediate OWN frozen Q1-Q4 whole review, NOT a mathematical premise',
    metadata=parent_manifest, **summarize(parent_rows),
    historical_summary_bound_not_replayed=parent['compact_current_summary']))

labels = re.findall(r'^\|(R14O[0-9]{2})\|',
                    read(P + 'obligations-v1.md').decode(), re.M)
assert labels == [f'R14O{i:02d}' for i in range(1, 57)]
assert decoded(P + 'sources-v1.json')['proposed_not_accepted_premise'][
    'used_ONLY_in'] == 'R14D'
for source in decoded(P + 'sources-v1.json')['accepted_inputs']:
    assert verify(source) in rows
assert verify(decoded(P + 'sources-v1.json')['proposed_not_accepted_premise']) in rows

summary = summarize(rows)
assert summary['occurrences'] == 29 and summary['unique_paths'] == 29
now = datetime.now(timezone.utc).isoformat()
validation = write_new('input-validation-v1.json', dict(
    verified_at_utc=now, administrative_only=True, records=rows,
    compact_current_summary=summary, groups=groups,
    all56_obligation_IDs_exact=True,
    accepted_R8_R12_scope_and_exact_copy_suffixes_verified=True,
    R13_only_proposed_R14D_premise_no_peer_access=True,
    old_inventory_rows_bound_not_recopied_or_rewalked=True,
    mathematical_executable_CAS_scan_table_generator_or_author_replay=False,
    writes_only_NEW_assigned_R14_prefix=True))

main = record(P + 'candidate-v1.md')
output = write_new('freeze-output-v1.json', dict(
    at_utc=now, main=main, whole_obligations=56,
    compact_current_summary=summary, all_inputs_verified=True,
    R14A_B_C_use_accepted_inputs_only=True,
    R14D_EXPLICITLY_conditional_on_PROPOSED_R13C=True,
    no_R13_peer_material_or_repair=True, administrative_only=True,
    status='candidate proof - unverified; TWO OTHER whole audits required'))

suffixes = ['candidate-v1.md', 'obligations-v1.md', 'hand-checks-v1.md',
            'failed-routes-v1.md', 'source-audit-v1.md', 'worklog-v1.md',
            'sources-v1.json', 'freeze-v1.py', 'input-validation-v1.json',
            'freeze-output-v1.json']
artifacts = [record(P + suffix) for suffix in suffixes]
manifest = write_new('freeze-v1.json', dict(
    frozen_at_utc=datetime.now(timezone.utc).isoformat(),
    status='COMPLETE R14 constructor checkpoint - candidate proof unverified',
    constructor='/root/review_2021_reasoning_j15_r2',
    claims=[
        'R14A under Q5/nonunit a7: normalized D10 center is a unit; D9 too if a9 nonunit',
        'R14B either actual NONUNIT EC10/EC11 forces a7 UNIT',
        'R14C actual m5 unit-a9 forces nonunit EC10, a7 UNIT and three higher centers',
        'R14D CONDITIONAL proposed-R13C all-m5 unit-a7 and full T4 exclusion'],
    whole_obligations=56,
    TWO_OTHER_fresh_initially_blind_ENTIRE_WHOLE_audits_required=True,
    constructor_and_prior_input_authorship_not_independent_review=True,
    root_supplied_NO_new_R14_mathematical_inference=True,
    R14A_B_C_independent_of_pending_R13=True,
    R14D_EXPLICITLY_conditional_on_PROPOSED_R13C=True,
    R13_acceptance_NOT_assumed_or_peer_review_metadata_read=True,
    actual_residual_subbranch_excluded_without_R13=
    'm5 with a7 NONUNIT and a9 UNIT in exact actual double-s domain',
    no_full_m5_m3m4_J15_degree20_annual_lift_height_or_novelty_claim=True,
    no_extra_unit_depth_maximum_all_real_root_or_quotient_CA_assumption=True,
    requested_settings=dict(model='gpt-6.1-sol', reasoning='max', inherited=True),
    independently_verified_effective_settings=None,
    authoritative_weekly_snapshot=dict(
        tool='mcp__codex_app__get_usage_limits', at_utc='2026-10-18 01:52:04 UTC',
        total_weekly_used_percent=9, window_minutes=10080, reset_unix=1792874445,
        ordinary_usage_allowed=True, legacy_and_by_limit_agree=True,
        earlier_plus_one_second_raw_reset_preserved=1792874446,
        user_authorized_current_window=True, ceiling_total_percent=90,
        integration_reserve_retained=True, automatic_later_reset_spending=False),
    compact_current_summary=summary, compact_input_groups=5,
    old_historical_rows_bound_not_recopied=True,
    mathematical_executable_CAS_scan_table_generator_or_author_replay=False,
    proof_critical_finite_certificates_entirely_hand_derived=True,
    old_shared_cache_Git_writes_spawn_contact_charge_or_bypass=False,
    administrative_command='python3 ' + P + 'freeze-v1.py', artifacts=artifacts))

for row in rows + artifacts + [manifest]:
    verify(row)
print(json.dumps(dict(
    ENTIRE_constructor_frozen=True, main=main, manifest=manifest,
    whole_obligations=56, compact_current_summary=summary,
    all_postverified=True, no_math_executable_or_peer_access=True,
    R14D_proposed_premise_explicit=True, candidate_unverified=True), indent=2))
