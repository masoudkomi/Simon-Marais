#!/usr/bin/env python3
"""Administrative-only whole-review freeze; no mathematical evaluation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = 'problems/2024-B4/reviews/coordinator-three-bit-sector-r2-review-1-'
TELEMETRY = {'at_utc': '2026-10-17 20:40:24 UTC', 'used_percent_total': 65,
             'window_minutes': 10080, 'reset_unix': 1792745187,
             'ordinary_usage_allowed': True, 'total_ceiling_percent': 90,
             'review_integration_reserve': True,
             'method': 'mcp__codex_app__get_usage_limits({}), rateLimitsByLimitId.codex.primary; legacy agrees',
             'account_label': '029a8928…1334ac3a',
             'conflicting_later_read': {'at_utc': '2026-10-17 20:41:21 UTC',
                                        'used_percent_total': 0,
                                        'window_minutes': 10080,
                                        'reset_unix': 1792874445,
                                        'ordinary_usage_allowed': True},
             'conflict_unresolved_not_new_window_authorization': True,
             'conservative_prior_old_window_total_used_for_checkpoint': 65,
             'new_queued_math_work_held_pending_measurable_budget_handling': True}


def fp(path):
    data = (ROOT / path).read_bytes()
    return {'path': str(path), 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}


def verify(row):
    actual = fp(row['path'])
    if actual != {key: row[key] for key in actual}:
        raise RuntimeError(('Fingerprint changed', row, actual))
    return actual


def read_json(path):
    return json.loads((ROOT / path).read_text())


def summary(rows):
    unique = {}
    for row in rows:
        previous = unique.setdefault(row['path'], row)
        if previous != row:
            raise RuntimeError(('Conflicting fingerprint', row))
    encoded = json.dumps([unique[p] for p in sorted(unique)],
                         sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(rows), 'unique_paths': len(unique),
            'canonical_deduplicated_summary_sha256': hashlib.sha256(encoded).hexdigest()}


def write_new(suffix, value):
    path = PREFIX + suffix
    with (ROOT / path).open('x') as handle:
        json.dump(value, handle, indent=2)
        handle.write('\n')
    return fp(path)


def main():
    for suffix in ('sources-v1.json', 'input-validation-v1.json', 'manifest-v1.json'):
        if (ROOT / (PREFIX + suffix)).exists():
            raise RuntimeError('Refuse output overwrite')
    baseline_row = fp(PREFIX + 'baseline-v1.json')
    assert baseline_row['bytes'] == 12224
    assert baseline_row['sha256'] == '96b515f789d977334a9e9d9b81b030faa81d907cc799f7a1588ac35a3acecaca'
    baseline = read_json(baseline_row['path'])
    packet = [verify(row) for row in baseline['six_constructor_artifacts_including_freeze']]
    inputs = [verify(row) for row in baseline['constructor29_current_unique_records']]
    own = [verify(row) for row in baseline['own_parent_nine_artifacts_including_manifest']]
    initial_source = [verify(row) for row in baseline['five_existing_primary_source_files_read_only']]
    initial_rows = packet + inputs + own + initial_source
    initial_summary = summary(initial_rows)
    assert len(packet) == 6 and len(inputs) == 29 and len(own) == 9 and len(initial_source) == 5
    assert initial_summary['occurrences'] == initial_summary['unique_paths'] == 49
    assert initial_summary['canonical_deduplicated_summary_sha256'] == baseline['canonical_deduplicated_summary_sha256']
    assert baseline['older_own_paths_bound_transitively_including_TBv1'] == 430
    parent = verify(baseline['own_parent_manifest'])
    parent_validation = verify(baseline['own_parent_validation'])
    target = verify(baseline['exact_main'])
    target_freeze = verify(baseline['exact_constructor_freeze'])
    old_source = read_json('problems/2024-B4/notes/reasoning-sector3-return-r1-sources-v1.json')['source_records'][0]
    additional_source = [verify(row) for row in old_source['read_only_source_images']
                         if any(row['path'].endswith('-%02d.png' % page) for page in (20, 21))]
    assert len(additional_source) == 2
    old_rows = initial_rows + additional_source
    old_summary = summary(old_rows)
    assert old_summary['occurrences'] == old_summary['unique_paths'] == 51
    accepted = 'problems/2024-B4/proofs/reviewed-reasoning-sector3-return-r1-v1.1.md'
    old_candidate = 'problems/2024-B4/notes/reasoning-sector3-return-r1-candidate-v1.md'
    assert (ROOT / accepted).read_bytes().endswith((ROOT / old_candidate).read_bytes())
    prose_suffixes = ['initial.md', 'issues-v1.md', 'ledger-v1.md', 'source-checks-v1.md']
    prose = [fp(PREFIX + suffix) for suffix in prose_suffixes]
    ledger = (ROOT / prose[2]['path']).read_text()
    labels = re.findall(r'^\|(R2-\d{2})\|(.+)\|Pass\.\|$', ledger, re.MULTILINE)
    assert [row[0] for row in labels] == ['R2-%02d' % n for n in range(1, 45)]
    assert all(len(row[1]) > 100 for row in labels)
    issues = (ROOT / prose[1]['path']).read_text()
    assert 'Substantive issues:0. Required repairs:0. Unresolved issues:0.' in issues
    assert all('R2-R1-N%d' % n in issues for n in range(1, 5))
    stamp = datetime.now(timezone.utc).isoformat()
    sources_row = write_new('sources-v1.json', {
        'recorded_at_utc': stamp,
        'reviewer': '/root/review_2022_complexity_r2',
        'requested_settings': baseline['requested_settings'],
        'independently_verified_effective_settings': None,
        'entire_six_file_packet_and_all44_obligations_reconstructed': True,
        'complete_accepted_structural_and_sector3_bodies_freshly_read': True,
        'accepted_T1_S3A_S3B_exact_scopes_no_self_recertification': True,
        'r1_unaccepted_not_a_premise_or_substitute_review': True,
        'T2_IC_J_Kasami_factorization_not_needed': True,
        'root_sole_NEW_constructor_excluded': True,
        'new_C_r2_or_TBv1_peer_report_finding_metadata_read': False,
        'old_roles': 'B structuralR2,sector3R1,narrowr1R1 and older2024 reviews/context; no new r2 construction',
        'official_primary_web': {
            'url': 'https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf',
            'actual_read_scope': 'page2 B4 hypothesis and(b); returned unrelated problems ignored; no preliminary construction',
            'fresh_native_PDF_sha256': None},
        'classical_intersection_primary_web': {
            'url': 'https://arxiv.org/pdf/0903.2016v4',
            'actual_read_scope': 'Section3.2 operative projective/local statements and surrounding scope; not full19pages or external textbook proof',
            'fresh_native_PDF_sha256': None},
        'original_coauthor_source': {
            'title': 'McGuire1995, Absolutely irreducible curves with applications to combinatorics and coding theory',
            'url': 'https://thesis.caltech.edu/4053/01/McGuire_gm_1995.pdf',
            'record_url': 'https://thesis.caltech.edu/4053/',
            'doi': '10.7907/1CZ2-6S05',
            'actual_visual_PDF_pages': [14, 15, 20, 21, 24, 25],
            'printed_pages': [9, 10, 15, 16, 19, 20],
            'actual_scope': 'COMPLETE PropA and theorem2.1prime proof pages; matching homogeneous/affine definitions; not entire97page thesis or original journal',
            'existing_source_fingerprints': initial_source + additional_source,
            'read_only_PDF_skill': True,
            'new_render_download_or_cache_write': False},
        'no_new_Fulton_retry_bypass_or_claim_of_fresh_full_textbook_proof': True,
        'whole_source_scope_prose': prose[3],
        'necessary_current_summary': old_summary,
        'initial_baseline_summary': initial_summary,
        'compact_own_parent_manifest': parent,
        'compact_own_parent_validation': parent_validation,
        'older_own_paths_bound_transitively': 430,
        'no_mathcode_scan_CAS_native_mathematical_child_or_author_rerun': True,
        'no_old_shared_Git_cache_edit_spawn_contact_charge_or_bypass': True,
        'next2021R11_files_unopened_through_entire_freeze': True,
        'authoritative_weekly_telemetry': TELEMETRY})
    freezer_row = fp(PREFIX + 'freeze-v1.py')
    current = [baseline_row] + prose + [freezer_row, sources_row]
    validation_row = write_new('input-validation-v1.json', {
        'checked_at_utc': stamp,
        'administrative_only_no_mathematical_evidence': True,
        'exact_target': target,
        'exact_constructor_freeze': target_freeze,
        'all_six_constructor_files_unchanged': True,
        'all29_current_input_paths_unchanged': True,
        'constructor31_occurrences_bound_by_exact_metadata_not_expanded': True,
        'all_nine_own_r1_review_files_preserved': True,
        'all_seven_existing_primary_source_files_preserved': True,
        'initial_baseline': baseline_row,
        'initial_baseline_summary': initial_summary,
        'two_later_definition_page_records': additional_source,
        'necessary_current_summary': old_summary,
        'accepted_S3_exact_frozen_candidate_suffix': True,
        'compact_own_parent_manifest': parent,
        'compact_own_parent_validation': parent_validation,
        'older_own_paths_bound_transitively': 430,
        'all44_ledger_rows_present_once': True,
        'substantive_issues': 0, 'required_repairs': 0, 'retained_scope_notes': 4,
        'new_peer_material_unread_before_entire_initial_freeze': True,
        'one_failed_context_match_patch_no_file_changed_corrected_own_only': True,
        'new_review_records_before_validation': current,
        'all_current_input_and_new_record_summary': summary(old_rows + current),
        'no_mathcode_CAS_scan_or_author_replay': True,
        'no_old_shared_Git_cache_edit_spawn_contact_charge_or_bypass': True,
        'authoritative_weekly_telemetry': TELEMETRY})
    artifacts = current + [validation_row]
    manifest_row = write_new('manifest-v1.json', {
        'frozen_at_utc': datetime.now(timezone.utc).isoformat(),
        'status': 'COMPLETE fresh initially blind NONCONSTRUCTOR WHOLE R1; no substantive defect found; not coordinator acceptance',
        'reviewer': '/root/review_2022_complexity_r2',
        'requested_settings': baseline['requested_settings'],
        'independently_verified_effective_settings': None,
        'exact_target': target,
        'exact_constructor_freeze': target_freeze,
        'entire_r2_all44_obligations_reconstructed_not_extension_only': True,
        'substantive_issues': 0, 'required_repairs': 0, 'retained_scope_notes': 4,
        'new_peer_findings_and_metadata_unread_through_entire_initial': True,
        'root_NEW_constructor_excluded': True,
        'r1_not_accepted_premise_or_substitute_whole_review': True,
        'old_input_review_roles_disclosed_no_self_recertification': True,
        'another_OTHER_entire_initially_blind_whole_review_and_reconciliation_required': True,
        'no_full_annual_weight4plus_classification_or_priority_claim': True,
        'necessary_current_summary': old_summary,
        'compact_own_parent_manifest': parent,
        'compact_own_parent_validation': parent_validation,
        'older_own_paths_bound_transitively': 430,
        'new_own_files_including_manifest': len(artifacts) + 1,
        'older_plus_new_own_paths_bound_transitively': 430 + len(artifacts) + 1,
        'no_mathcode_scan_CAS_native_mathematical_child_or_author_rerun': True,
        'no_old_shared_Git_cache_edit_spawn_contact_charge_or_bypass': True,
        'next2021R11_candidate_unopened_before_current_entire_freeze': True,
        'authoritative_weekly_telemetry': TELEMETRY,
        'artifacts': artifacts})
    for row in old_rows + artifacts + [manifest_row]:
        verify(row)
    print(json.dumps({'manifest': manifest_row, 'initial': prose[0],
                      'issues': prose[1], 'ledger': prose[2],
                      'source_checks': prose[3], 'validation': validation_row,
                      'all44_obligations': True, 'substantive_issues': 0,
                      'necessary_old_paths_verified': 51,
                      'old_bytes_preserved': True, 'new_peer_material_unread': True,
                      'review_artifacts_including_manifest': len(artifacts) + 1}, indent=2))


if __name__ == '__main__':
    main()
