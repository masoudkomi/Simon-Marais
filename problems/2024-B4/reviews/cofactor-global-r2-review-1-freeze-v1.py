#!/usr/bin/env python3
"""Exclusive administrative WHOLE-review freeze; NO mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
import re

ROOT = Path.cwd().resolve()
P = 'problems/2024-B4/reviews/cofactor-global-r2-review-1-'
C = 'problems/2024-B4/notes/cofactor-global-r2-'
FORBIDDEN = 'problems/2024-B4/reviews/cofactor-global-r2-review-2-'
NOW = datetime.now(timezone.utc).isoformat()
assert ROOT.name == 'Website'

def rec(path):
    assert not path.startswith(FORBIDDEN), 'NEW corresponding peer material forbidden'
    raw = (ROOT / path).read_bytes()
    return dict(path=path, bytes=len(raw), sha256=sha256(raw).hexdigest())

def read(path):
    rec(path)
    return json.loads((ROOT / path).read_text())

def out(suffix, obj):
    with (ROOT / (P + suffix)).open('x', encoding='utf-8') as handle:
        json.dump(obj, handle, indent=2, ensure_ascii=False)
        handle.write('\n')

unique = {}
occurrences = []
def bind(path, role, expected=None):
    row = rec(path)
    if expected is not None:
        assert row == {key: expected[key] for key in ('path', 'bytes', 'sha256')}, path
    assert path not in unique or unique[path] == row
    unique[path] = row
    occurrences.append(dict(path=path, role=role))
    return row

constructor = bind(C+'freeze-v1.json', 'ENTIRE exact constructor freeze', dict(
    path=C+'freeze-v1.json', bytes=2322,
    sha256='3e63984333d64dcfe8bb32395d28e948ab1023ce8f4ab367e0ea374d51dfeaef'))
cf = read(C+'freeze-v1.json')
assert len(cf['artifacts']) == 8
for row in cf['artifacts']:
    assert row['path'].startswith(C)
    bind(row['path'], 'exact immutable constructor artifact', row)
assert rec(C+'candidate-v1.md') == dict(path=C+'candidate-v1.md', bytes=15586,
    sha256='9dac8137a3b47637e25ee66a5c2bf5ff00146e9d1d54ba55764002111d5376f9')
cb = read(C+'baseline-v1.json')
assert len(cb['protected']) == cf['protected_paths'] == 16
for row in cb['protected']:
    bind(row['path'], 'declared exact protected OLD constructor input', row)
bind(cb['compact_immediate_own_parent']['path'],
    'repeated constructor compact-parent binding', cb['compact_immediate_own_parent'])

accepted = []
for stem, key in [('structural', 'accepted_proof'),
                  ('coordinator-F8-pencil-r1', 'accepted_copy'),
                  ('cofactor-symmetry-r1', 'accepted_copy')]:
    ap = 'problems/2024-B4/reviews/'+stem+'-acceptance.json'
    a = read(ap)
    bind(ap, 'exact current accepted OLD authority JSON')
    bind(ap[:-5]+'.md', 'exact current accepted OLD scope Markdown')
    bind(a[key]['path'], 'exact accepted OLD full body', a[key])
    bind(a['candidate']['path'], 'exact original accepted OLD candidate', a['candidate'])
    if key == 'accepted_copy':
        assert a['unresolved_substantive_issues'] == 0 and a['repair_required'] is False
        assert (ROOT / a[key]['path']).read_bytes().endswith(
            (ROOT / a['candidate']['path']).read_bytes())
    else:
        assert a['remaining_substantive_objections'] == 0
        assert a['editorial_change'] == 'Section3 heading binary -> ternary; lemma and proof unchanged'
    accepted.append(dict(authority=rec(ap), accepted_body=a[key],
        candidate=a['candidate'], exact_suffix_checked=(key == 'accepted_copy'),
        historical_metadata_bound_by_authority_not_recursively_expanded=True))

parent_path = 'problems/2022-B4/notes/reasoning-seed-return-r1-freeze-v1.json'
parent = bind(parent_path, 'compact immutable immediate own parent', dict(
    path=parent_path, bytes=3871,
    sha256='78beb6e2f0f2ce43c51029f68bd42da1e9693cbcde63fa71c1d5df881443dccc'))
pm = read(parent_path)
assert pm['older_plus_new_own_paths_bound_transitively'] == 642
for row in pm['artifacts']:
    if row['path'].endswith(('baseline-v1.json', 'input-validation-v1.json')):
        bind(row['path'], 'necessary compact immutable own-parent metadata', row)
assert read('problems/2022-B4/notes/reasoning-seed-return-r1-baseline-v1.json')[
    'summary'] == pm['direct_fingerprint_summary']
assert read('problems/2022-B4/notes/reasoning-seed-return-r1-input-validation-v1.json')[
    'fingerprint_summary'] == pm['direct_fingerprint_summary']

expected = [f'{number:02d}' for number in range(1, 57)]
assert re.findall(r'^\| CG-(\d{2}) \|', (ROOT/(C+'obligations-v1.md')).read_text(), re.M) == expected
assert re.findall(r'^\|CG-(\d{2})\|', (ROOT/(P+'ledger-v1.md')).read_text(), re.M) == expected
assert 'candidate proof - unverified' in (ROOT/(P+'initial-v1.md')).read_text().lower()
ordered = [unique[path] for path in sorted(unique)]
summary = dict(occurrences=len(occurrences), unique_paths=len(ordered),
    canonical_record_array_sha256=sha256(json.dumps(
        ordered, sort_keys=True, separators=(',', ':')).encode()).hexdigest())

out('baseline-v1.json', dict(captured_at_utc=NOW,
    operation='exact bytes/SHA/JSON/label checks ONLY, not mathematics',
    constructor_freeze=constructor, exact_constructor_artifacts_including_freeze=9,
    constructor_protected_direct_inputs=16, accepted_authorities=accepted,
    compact_immediate_own_parent=parent, prior_own_paths_bound_transitively=642,
    summary=summary, direct_records=ordered, occurrence_roles=occurrences,
    no_recursive_historical_inventory_copy_or_rehash=True,
    historical_live_notes_are_not_mathematical_authorities=True,
    NEW_corresponding_peer_material_read_or_hashed=False))

out('metadata-v1.json', dict(status='ENTIRE OTHER initially blind WHOLE CG1--CG3 R1',
    reviewer='/root/review_2017_coarsening_r1', constructor='/root', root_excluded=True,
    reviewer_supplied_no_NEW_CG_inference=True,
    older_CP_sector3_authorship_T1_FP_FS_review_roles_disclosed=True,
    no_independent_self_recertification_of_own_OLD_input=True,
    requested_settings=dict(model='gpt-6.1-sol', reasoning='max', inherited=True),
    independently_verified_effective_settings=None,
    whole_obligations=56, all56_independently_reconstructed=True,
    substantive_mathematical_issues=0, required_proof_repairs=0,
    closed_source_domain_qualifications=1,
    closed_qualification='HM16 PROPER divisor automatic under CG3 threshold, not a k1 component claim',
    mathematical_verdict_WITHHELD_until_BOTH_ENTIRE_initials=True,
    first_completion_notice_IDENTITY_ONLY=True,
    no_NEW_corresponding_peer_report_findings_files_hashes_metadata_read=True,
    exact_domain='Q=2^s,s>=3;ell=Q-1;q=Q^k,k>=1;n=ell*q+1',
    actual_irreducibility_threshold='q>=max(2ell+7,(ell-1)(ell-2)(ell+1)^2/4)',
    uniform_corollary='s>=3,k>=4 only; no universal smaller-k classification',
    all_projective_cones_contacts_both_square_completions_reconstructed=True,
    reduced_c_minus_1_and_char2_polar_argument_checked=True,
    no_factor_F2_definition_unique_large_component_or_orbit_uniformity_assumed=True,
    source=dict(Fulton_entire_operative_5_4_Theorem2_proof=True,
        local_intersection_property_and_AppendixA_checked=True,
        no_whole129page_or_full_genus_source_chain_audit_claim=True,
        HM16_proper_divisor_statement_checked_not_imported=True,
        Ferard2017_operative_proof_unread_no_priority_claim=True,
        no_Frobenius_Gauss_map_theorem_import=True, new_cached_PDF_hash=None),
    no_mathematical_code_CAS_scan_sample_constructor_rerun_or_native_child=True,
    no_cache_shared_old_or_Git_mutation=True,
    whole_annual_classification_novelty_external_validation_or_promotion=False,
    compact_immediate_own_parent=parent,
    telemetry=dict(latest_direct_worker_utc='2026-10-18 08:17:12 UTC', used_percent_TOTAL=17,
        resets_at=1792874445, authorized_current_ceiling_TOTAL=90,
        reserve_required=True, no_automatic_later_window=True)))

out('input-validation-v1.json', dict(validated_at_utc=NOW,
    administrative_only_not_mathematical_validation=True,
    exact_constructor_all9_artifacts=True, all16_protected_direct_inputs_exact=True,
    repeated_constructor_parent_binding_counted=True,
    exact_OLD_accepted_bodies_and_declared_candidates=True,
    FP_FS_exact_suffixes_and_structural_editorial_exception_respected=True,
    all56_author_and_reviewer_labels_once_in_order=True,
    compact_immediate_own_parent=parent, prior_own_paths_bound=642,
    direct_fingerprint_summary=summary,
    no_recursive_old_inventory_copy_or_rehash=True,
    no_NEW_corresponding_peer_material_opened_or_hashed=True, errors=[]))

suffixes = ['initial-v1.md', 'ledger-v1.md', 'issues-v1.md',
    'source-checks-v1.md', 'worklog-v1.md', 'freeze-v1.py', 'baseline-v1.json',
    'metadata-v1.json', 'input-validation-v1.json']
out('manifest-v1.json', dict(frozen_at_utc=NOW,
    status='ENTIRE OTHER initially blind WHOLE CG1--CG3 R1',
    reviewer='/root/review_2017_coarsening_r1', root_constructor_excluded=True,
    whole_obligations=56,
    full_report_ALL56_ledger_issues_source_log_code_ALL_metadata_frozen=True,
    no_NEW_corresponding_peer_files_findings_hashes_metadata_read_before_ENTIRE_freeze=True,
    mathematical_verdict_WITHHELD_until_BOTH_ENTIRE_initials=True,
    first_completion_IDENTITY_ONLY=True, no_mathematical_program_or_promotion=True,
    constructor_freeze=constructor, compact_immediate_own_parent=parent,
    prior_own_paths_bound=642, new_packet_paths_including_manifest=10,
    own_paths_after_this_packet=652, direct_fingerprint_summary=summary,
    artifacts=[rec(P+suffix) for suffix in suffixes]))
print(json.dumps(dict(manifest=rec(P+'manifest-v1.json'), report=rec(P+'initial-v1.md'),
    artifacts_including_manifest=10, all_obligations=56, direct_summary=summary,
    findings_withheld=True, no_mathematical_computation=True), indent=2))
