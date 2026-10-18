#!/usr/bin/env python3
"""R15 R2 exclusive SHA/JSON/suffix/label metadata; no field calculations."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
import re

ROOT = Path.cwd().resolve()
P = 'problems/2021-B4/reviews/reasoning-unit-return-r15-review-2-'
C = 'problems/2021-B4/notes/reasoning-unit-return-r15-'
NOW = datetime.now(timezone.utc).isoformat()
FORBIDDEN = (
    'problems/2021-B4/reviews/reasoning-unit-return-r15-review-1-',
    'problems/2025-B4/reviews/reasoning-Runge-return-r3-review-1-',
    'problems/2024-B4/reviews/cofactor-dominant-r4-review-1-',
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

main = check(dict(path=C+'candidate-v1.md', bytes=17560,
    sha256='48700c4ed0462f6e916228083ede2520efc8b435be1e8e11d07d3233827c893c'))
target = check(dict(path=C+'freeze-v1.json', bytes=6170,
    sha256='0d2e246accd461704850f34ca056576e2f64ca6247b2fd08538c935535f77f48'))
constructor = read(target['path'])
assert constructor['all48_obligations_and_constructor_checks_complete'] is True
assert constructor['constructor_excluded_from_independent_review_count'] is True
constructor_rows = [check(row) for row in constructor['artifacts']]
assert len(constructor_rows) == 10
occurrences = [target] + constructor_rows
author_baseline = read(C+'baseline-v1.json')
occurrences += [check(row) for row in author_baseline['deduplicated_rows']]

authorities = []
for stem, expected in [
    ('reasoning-return-r13', 'a29ecdb8002f3cbb4250e93f94c65ed83a67b086331fb3497d48ad740959ab6b'),
    ('reasoning-return-r14', 'c574096c94bc4deaab81b54c5dd0599f3089e7122165312d9089ea28d2a9f880'),
]:
    path = 'problems/2021-B4/reviews/'+stem+'-acceptance.json'
    authority = read(path)
    assert authority['unresolved_substantive_issues'] == 0
    assert authority['repair_required'] is False
    proof = check(authority['accepted_copy'])
    candidate = check(authority['candidate'])
    assert proof['sha256'] == expected
    assert (ROOT/proof['path']).read_bytes().endswith((ROOT/candidate['path']).read_bytes())
    if stem.endswith('r14'):
        assert authority['R13C_separate_accepted_old_premise_now_discharged'] is True
    authorities.append(dict(authority=rec(path), accepted_copy=proof,
        exact_candidate_suffix=candidate,
        historical_occurrences_bound=authority['record_occurrences_verified'],
        historical_paths_bound=authority['unique_paths_verified']))
    occurrences += [rec(path), proof, candidate]

parent = check(dict(
    path='problems/2017-B4/reviews/coordinator-weighted-cutpath-r1-review-1-manifest-v1.json',
    bytes=2987,
    sha256='14c5525a21bd9e3e92bd79c968c293d84051d62efb16a1223a01e32829f7f926'))
parent_data = read(parent['path'])
occurrences += [parent] + [check(row) for row in parent_data['artifacts']]
# Do not expand historical nested inventories or read unrelated old bodies
# solely for preservation. Their exact parent metadata remains bound.
unique = {}
for row in occurrences:
    assert unique.setdefault(row['path'], row) == row, row['path']
rows = [unique[path] for path in sorted(unique)]
canonical = json.dumps(rows, ensure_ascii=False, sort_keys=True,
    separators=(',', ':')).encode()

expected_labels = [f'{i:02}' for i in range(1, 49)]
labels = re.findall(r'^\|R15-(\d{2})\|',
    (ROOT/(P+'ledger-v1.md')).read_text(), re.M)
assert labels == expected_labels
for suffix in ('obligations-v1.md', 'hand-checks-v1.md'):
    author_labels = re.findall(r'^\| R15-(\d{2}) \|',
        (ROOT/(C+suffix)).read_text(), re.M)
    assert author_labels == expected_labels
assert 'no substantive defect found' in (ROOT/(P+'initial-v1.md')).read_text()
assert 'Open substantive issues:0' in (ROOT/(P+'issues-v1.md')).read_text()
# Identity, suffix and document-label assertions only: no finite-field,
# affine-entry, valuation, polynomial, arithmetic or certificate execution.

out('baseline-v1.json', dict(captured_utc=NOW,
    administrative_only=True, fingerprint_occurrences=len(occurrences),
    deduplicated_paths=len(rows),
    canonical_deduplicated_sha256=sha256(canonical).hexdigest(),
    protected_records=rows, constructor_packet_files_verified=11,
    constructor_direct_baseline_rows_verified=len(author_baseline['deduplicated_rows']),
    accepted_authorities=authorities, immediate_own_parent=parent,
    immediate_own_parent_payloads_verified=len(parent_data['artifacts']),
    historical_inventories_bound_not_recursively_replayed=True,
    no_corresponding_NEW_R15_peer_findings_files_hashes_or_metadata_access=True))
out('metadata-v1.json', dict(recorded_utc=NOW,
    status='one OTHER initially blind ENTIRE WHOLE R2; not promotion',
    reviewer='/root/review_2017_coarsening_r1', new_constructor='/root/review_2021_reasoning_j15_r2',
    reviewer_did_not_construct_NEW_R15=True,
    old_roles='C authored older R5 and reviewed J15/PN/R14 and other old packets; accepted input roles, no fresh self-recertification',
    whole_obligations=48, entire_constructor_packet_read=True,
    all96_affine_entries_and_all9_critical_products_hand_reconstructed=True,
    exact_scope='R15A field obstruction, R15B actual center nonvanishing, R15C full actual m5 exclusion only in stated double-s branch',
    no_substantive_issue_found=True, required_repairs=0,
    no_math_code_CAS_scan_table_generator_author_rerun_or_old_certificate_run=True,
    no_corresponding_NEW_root_R15_findings_files_hashes_or_metadata_opened=True,
    findings_withheld_until_both_entire_initials_confirmed=True,
    requested_settings=dict(model='gpt-6.1-sol', reasoning='max', inherited=True),
    effective_setting_readback=None,
    telemetry=dict(authority='coordinator account-wide report', most_recent_TOTAL_percent=22,
        reset_unix=1792874445, ceiling_TOTAL_percent=90, integration_reserve=True,
        no_automatic_later_window=True), promotion=False))
out('input-validation-v1.json', dict(validated_utc=NOW,
    administrative_integrity_only=True, mathematical_code_executed=False,
    target_main_and_freeze_exact=True, constructor_all11_files_exact=True,
    current_direct_input_fingerprints_exact=True,
    both_accepted_proof_candidate_suffixes_exact=True,
    current_R14D_R13C_authority_discharge_checked=True,
    all48_ledger_labels_exact_once_in_order=True,
    all48_constructor_obligation_and_handcheck_labels_exact=True,
    fingerprint_occurrences=len(occurrences), deduplicated_paths=len(rows),
    canonical_deduplicated_sha256=sha256(canonical).hexdigest(), errors=[]))
suffixes = ['initial-v1.md', 'ledger-v1.md', 'issues-v1.md', 'sources-v1.md',
    'worklog-v1.md', 'freeze-v1.py', 'baseline-v1.json', 'metadata-v1.json',
    'input-validation-v1.json']
out('manifest-v1.json', dict(frozen_utc=NOW,
    status='ENTIRE initially blind OTHER WHOLE R15 R2 frozen; not promotion',
    whole_obligations=48, review_file_count=10,
    entire_report_ALL48_issues_sources_log_code_ALL_metadata_frozen=True,
    no_corresponding_NEW_root_R15_findings_files_hashes_or_metadata_access=True,
    identity_only_completion_before_mathematical_findings=True,
    target_main=main, target_freeze=target, immediate_own_parent=parent,
    artifacts=[rec(P+x) for x in suffixes]))
for row in read(P+'manifest-v1.json')['artifacts']:
    check(row)
print(json.dumps(dict(initial=rec(P+'initial-v1.md'),
    manifest=rec(P+'manifest-v1.json'), all48=True,
    review_files=10, fingerprint_occurrences=len(occurrences),
    deduplicated_paths=len(rows)), indent=2))
