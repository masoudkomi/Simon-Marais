#!/usr/bin/env python3
"""Exclusive R1 integrity records only; no mathematical calculation or rerun."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
import re

ROOT = Path.cwd().resolve()
P = 'problems/2017-B4/reviews/coordinator-weighted-cutpath-r1-review-1-'
C = 'problems/2017-B4/notes/coordinator-weighted-cutpath-r1-'
NOW = datetime.now(timezone.utc).isoformat()
FORBIDDEN = (
    'problems/2017-B4/reviews/coordinator-weighted-cutpath-r1-review-2-',
    'problems/2021-B4/reviews/reasoning-unit-return-r15-review-1-',
)
assert ROOT.name == 'Website'

def rec(path):
    assert not any(path.startswith(x) for x in FORBIDDEN), path
    raw = (ROOT / path).read_bytes()
    return dict(path=path, bytes=len(raw), sha256=sha256(raw).hexdigest())

def check(row):
    actual = rec(row['path'])
    assert actual == {k: row[k] for k in ('path', 'bytes', 'sha256')}, row['path']
    return actual

def read(path):
    rec(path)
    return json.loads((ROOT / path).read_text())

def out(suffix, obj):
    with (ROOT / (P + suffix)).open('x') as stream:
        json.dump(obj, stream, ensure_ascii=False, indent=2)
        stream.write('\n')

expected_main = dict(path=C+'candidate-v1.md', bytes=12695,
    sha256='f77d09e57a7462faaf6d48077c6815b9d33ffa722470596a947b9f46c4205928')
expected_freeze = dict(path=C+'freeze-v1.json', bytes=2672,
    sha256='2ff11ebea88c684a2d86be972ae6f937ec5aec95040904eb27fc5c392ad7b4d4')
check(expected_main)
check(expected_freeze)
constructor = read(expected_freeze['path'])
assert constructor['whole_obligations'] == 40
assert constructor['sole_new_constructor'] is True
assert constructor['constructor_excluded'] is True
constructor_rows = [check(row) for row in constructor['artifacts']]
assert len(constructor_rows) == 9

occurrences = [expected_freeze] + constructor_rows
old_baseline = read(C+'baseline-v1.json')
occurrences += [check(row) for row in old_baseline['protected_direct_records']]
old_parent = check(old_baseline['compact_own_parent'])
occurrences.append(old_parent)
# Bind historical parent metadata by its exact identity. Do not replay a growing
# historical inventory or read unrelated mathematics solely for preservation.
authority_path = 'problems/2017-B4/reviews/concavity-acceptance.json'
authority = read(authority_path)
assert authority['unresolved_substantive_objections'] == 0
assert authority['substantive_author_repair_required'] is False
occurrences.append(check(authority['accepted_proof']))
for key in ('candidate', 'integrity_record'):
    occurrences.append(check(authority[key]))
for key in ('reports', 'issue_logs'):
    occurrences += [check(row) for row in authority[key]]

own_parent = check(dict(
    path='problems/2024-B4/notes/cofactor-literature-followup-r3-freeze-v1.json',
    bytes=2142,
    sha256='11d982548d265237f1896dd4c11bc5bc58ec8a1709064873945fab342aaa873a'))
own_parent_data = read(own_parent['path'])
occurrences.append(own_parent)
occurrences += [check(row) for row in own_parent_data['artifacts']]
occurrences += [check(row) for row in own_parent_data['immutable_parents']]

unique = {}
for row in occurrences:
    old = unique.setdefault(row['path'], row)
    assert old == row, row['path']
protected = [unique[path] for path in sorted(unique)]
canonical = json.dumps(protected, ensure_ascii=False, sort_keys=True,
    separators=(',', ':')).encode()

body = (ROOT / (P+'ledger-v1.md')).read_text()
labels = re.findall(r'^\|WC-O(\d{2})\|', body, re.M)
assert labels == [f'{i:02}' for i in range(1, 41)]
constructor_labels = re.findall(r'^\|WC-O(\d{2})\|',
    (ROOT / (C+'obligations-v1.md')).read_text(), re.M)
assert labels == constructor_labels
assert 'no substantive defect found' in (ROOT / (P+'initial-v1.md')).read_text()
assert 'Open substantive issues: 0' in (ROOT / (P+'issues-v1.md')).read_text()
# The preceding assertions inspect document/identity strings, not graph,
# rational, logarithmic, entropy or arithmetic computations.

out('baseline-v1.json', dict(captured_utc=NOW,
    administrative_integrity_only=True,
    direct_fingerprint_occurrences=len(occurrences),
    deduplicated_path_count=len(protected),
    canonical_deduplicated_sha256=sha256(canonical).hexdigest(),
    protected_records=protected,
    constructor_packet_files_verified=10,
    own_parent=own_parent,
    own_parent_artifacts_verified=len(own_parent_data['artifacts']),
    historical_parent_metadata_bound_without_recursive_inventory_replay=True,
    no_corresponding_new_peer_file_hash_or_metadata_access=True))
out('metadata-v1.json', dict(recorded_utc=NOW,
    status='one OTHER initially blind ENTIRE WHOLE audit; not promotion',
    reviewer='/root/review_2017_coarsening_r1', reviewer_role='R1',
    new_constructor='/root', reviewer_did_not_construct_WC=True,
    older_roles='C authored older annulus/rank-mesh/profile/plane-interface work; not newly self-certified; not new WC premises',
    exact_scope='WC1-WC3, all n>=2 marked cutpaths and official limsup<0.648 only',
    whole_obligations=40, entire_constructor_packet_read=True,
    no_substantive_issue_found=True, required_author_repairs=0,
    no_mathematical_program_CAS_scan_source_rerun_or_certificate_run=True,
    no_corresponding_NEW_R2_findings_files_hashes_or_metadata_opened=True,
    findings_withheld_until_both_entire_initials_confirmed=True,
    requested_settings=dict(model='gpt-6.1-sol', reasoning='max', inherited=True),
    effective_readback=None,
    telemetry=dict(authority='coordinator direct account report',
        observed_utc='2026-10-18T09:27:42+00:00', total_weekly_used_percent=21,
        reset_unix=1792874445, total_ceiling_percent=90,
        integration_reserve=True, no_automatic_later_window=True),
    promotion=False))
out('input-validation-v1.json', dict(validated_utc=NOW,
    administrative_only=True, mathematics_executed=False,
    exact_target_main_and_freeze=True,
    constructor_all_ten_files_verified=True,
    all_direct_declared_fingerprints_verified=True,
    direct_fingerprint_occurrences=len(occurrences),
    deduplicated_path_count=len(protected),
    canonical_deduplicated_sha256=sha256(canonical).hexdigest(),
    ledger_exactly_all40=True, own_parent_exact=True, errors=[]))
suffixes = ['initial-v1.md', 'ledger-v1.md', 'issues-v1.md',
    'source-audit-v1.md', 'worklog-v1.md', 'freeze-v1.py',
    'baseline-v1.json', 'metadata-v1.json', 'input-validation-v1.json']
artifacts = [rec(P+x) for x in suffixes]
out('manifest-v1.json', dict(frozen_utc=NOW,
    status='ENTIRE initially blind OTHER WHOLE R1 frozen; no promotion',
    whole_obligations=40, new_packet_file_count=10,
    report_all40_issues_sources_worklog_code_ALL_metadata_frozen=True,
    no_corresponding_NEW_R2_file_hash_metadata_or_finding_access=True,
    identity_only_handoff_until_both_entire_initials=True,
    target_main=expected_main, target_freeze=expected_freeze,
    own_parent=own_parent, artifacts=artifacts))
for row in read(P+'manifest-v1.json')['artifacts']:
    check(row)
print(json.dumps(dict(main=rec(P+'initial-v1.md'),
    manifest=rec(P+'manifest-v1.json'), whole_obligations=40,
    files=10, fingerprint_occurrences=len(occurrences),
    deduplicated_paths=len(protected)), indent=2))
