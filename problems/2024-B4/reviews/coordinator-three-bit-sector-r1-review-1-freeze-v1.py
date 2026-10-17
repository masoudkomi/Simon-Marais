#!/usr/bin/env python3
"""Create-new review preservation only: SHA/JSON/text labels, no math."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = 'problems/2024-B4/reviews/coordinator-three-bit-sector-r1-review-1-'


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


def write_new(suffix, value):
    path = PREFIX + suffix
    with (ROOT / path).open('x') as handle:
        json.dump(value, handle, indent=2)
        handle.write('\n')
    return fp(path)


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


def main():
    for suffix in ('sources-v1.json', 'input-validation-v1.json', 'manifest-v1.json'):
        if (ROOT / (PREFIX + suffix)).exists():
            raise RuntimeError('Refuse any output overwrite')
    baseline_row = fp(PREFIX + 'baseline-v1.json')
    assert baseline_row['bytes'] == 12673
    assert baseline_row['sha256'] == '2e138816acaad19991d76f0dfe2d09209bb13008bc6020d301896ef4c9484361'
    baseline = read_json(baseline_row['path'])
    packet = [verify(row) for row in baseline['complete_constructor_artifacts_including_freeze']]
    inputs = [verify(row) for row in baseline['constructor_current_inputs_35_records_unchanged']]
    own = [verify(row) for row in baseline['own_parent_new_artifacts_including_freeze']]
    old_rows = packet + inputs + own
    old_summary = summary(old_rows)
    assert old_summary['occurrences'] == baseline['necessary_fingerprint_occurrences'] == 53
    assert old_summary['unique_paths'] == baseline['necessary_unique_paths'] == 53
    assert old_summary['canonical_deduplicated_summary_sha256'] == baseline['canonical_deduplicated_summary_sha256']
    assert len(packet) == 6 and len(inputs) == 35 and len(own) == 12
    assert baseline['older_own_paths_bound_transitively_including_R8'] == 421
    own_manifest = verify(baseline['compact_own_parent_manifest'])
    own_validation = verify(baseline['compact_own_parent_validation'])
    expected_main = verify(baseline['exact_main'])
    expected_freeze = verify(baseline['exact_constructor_freeze'])
    assert expected_main['sha256'] == '29878868615f42848918067fbed5067339cef3b254b3b836a1fa191502e41a77'
    assert expected_freeze['sha256'] == '0dc4b47373a3f071178bf0068a593b7a55a8451d41a42fda8f76c681e393a47a'
    prose_suffixes = ['initial.md', 'issues-v1.md', 'ledger-v1.md', 'source-checks-v1.md']
    prose = [fp(PREFIX + suffix) for suffix in prose_suffixes]
    ledger = (ROOT / prose[2]['path']).read_text()
    ids = re.findall(r'^\|(TB-\d{2})\|(.+)\|Pass\.\|$', ledger, re.MULTILINE)
    assert [row[0] for row in ids] == ['TB-%02d' % n for n in range(1, 37)]
    assert all(len(row[1]) > 100 for row in ids)
    issues = (ROOT / prose[1]['path']).read_text()
    assert 'Substantive issues:0. Required repairs:0. Unresolved issues:0.' in issues
    assert all('TB-R1-N%d' % n in issues for n in range(1, 5))
    stamp = datetime.now(timezone.utc).isoformat()
    sources = {
        'recorded_at_utc': stamp,
        'reviewer': '/root/review_2022_complexity_r2',
        'requested_settings': baseline['requested_settings'],
        'independently_verified_effective_settings': None,
        'status': 'COMPLETE initially blind NONCONSTRUCTOR WHOLE R1; no substantive issue found; not acceptance',
        'exact_target': expected_main,
        'exact_constructor_freeze': expected_freeze,
        'entire_six_file_packet_read': True,
        'all36_author_obligations_reconstructed': True,
        'complete_accepted_structural_header_and_body_read': True,
        'complete_accepted_sector3_header_and_body_read': True,
        'accepted_IC_actual_fresh_scope': 'scope header and COMPLETE Section1; not all IC2-IC4; no J dependency used',
        'all_three_accepted_authority_JSONs_read_entirely': True,
        'classical_intersection_imports': 'projective Bezout for no common component; local product multiplicity equality when no common tangent',
        'primary_web_sources': [
            {'title': 'Official SMMC2024 Paper B',
             'url': 'https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf',
             'actual_read_scope': 'page2 B4 hypothesis and(b); unrelated returned problems ignored; no preliminary proof',
             'fresh_native_PDF_sha256': None},
            {'title': 'Hernando-McGuire arXiv0903.2016v4',
             'url': 'https://arxiv.org/pdf/0903.2016v4',
             'actual_read_scope': 'matching setup, Section3 operative intersection statements and relevant whole/component scopes; not whole19pages',
             'fresh_native_PDF_sha256': None},
            {'title': 'Fulton author textbook public PDF attempt',
             'url': 'https://www.math.lsa.umich.edu/~wfulton/CurveBook.pdf',
             'actual_read_scope': 'indexed statement/proof start only; direct full opens502 and department-host404; no full proof read or new dependency',
             'fresh_native_PDF_sha256': None}],
        'old_roles_disclosed': 'B structuralR2 and sector3R1; older2024 context/review roles; no new TB construction or self-recertification',
        'root_constructor_excluded': True,
        'new_TB_peer_files_findings_or_metadata_read': False,
        'no_math_code_scan_CAS_or_author_replay': True,
        'no_old_shared_cache_Git_edit_spawn_charge_contact_or_bypass': True,
        'necessary_current_fingerprint_summary': old_summary,
        'compact_own_parent_manifest': own_manifest,
        'compact_own_parent_validation': own_validation,
        'older_own_paths_bound_transitively': 421,
        'source_check_prose': prose[3],
        'direct_weekly_total_used_percent': 64,
        'direct_weekly_telemetry_at_utc': '2026-10-17 20:26:58 UTC',
        'reset_unix': 1792745187,
        'total_ceiling_percent': 90,
        'review_integration_reserve': True}
    sources_row = write_new('sources-v1.json', sources)
    freezer_row = fp(PREFIX + 'freeze-v1.py')
    current = [baseline_row] + prose + [freezer_row, sources_row]
    validation_row = write_new('input-validation-v1.json', {
        'checked_at_utc': stamp,
        'administrative_only_no_mathematical_evidence': True,
        'exact_target': expected_main,
        'exact_constructor_freeze': expected_freeze,
        'all_six_constructor_files_unchanged': True,
        'all35_current_inputs_unchanged': True,
        'all12_own_R8_parent_files_unchanged': True,
        'baseline': baseline_row,
        'necessary_current_fingerprint_summary': old_summary,
        'old_historical_inventories_bound_not_expanded': True,
        'compact_own_parent_manifest': own_manifest,
        'compact_own_parent_validation': own_validation,
        'older_own_paths_bound_transitively': 421,
        'all36_ledger_rows_present_once': True,
        'substantive_issues': 0,
        'required_repairs': 0,
        'retained_scope_notes': 4,
        'new_peer_material_read_before_initial_freeze': False,
        'new_review_records_before_validation': current,
        'input_and_current_summary': summary(old_rows + current),
        'no_math_code_CAS_scan_native_child_or_author_rerun': True,
        'no_old_shared_cache_Git_edit_spawn_contact_charge_or_bypass': True})
    artifacts = current + [validation_row]
    manifest_row = write_new('manifest-v1.json', {
        'frozen_at_utc': datetime.now(timezone.utc).isoformat(),
        'reviewer': '/root/review_2022_complexity_r2',
        'review_kind': 'fresh initially blind NONCONSTRUCTOR WHOLE R1 of complete TB1-TB4',
        'status': 'complete initial; no substantive defect found; candidate remains unverified pending other whole audit and coordinator reconciliation',
        'requested_settings': baseline['requested_settings'],
        'independently_verified_effective_settings': None,
        'exact_target': expected_main,
        'exact_constructor_freeze': expected_freeze,
        'all36_obligations_and_every_TB1_TB4_inference_reconstructed': True,
        'substantive_issues': 0,
        'required_repairs': 0,
        'retained_scope_notes': 4,
        'entire_initial_frozen_before_any_new_peer_findings': True,
        'new_TB_peer_material_read': False,
        'root_constructor_excluded': True,
        'old_input_roles_disclosed_no_self_recertification': True,
        'necessary_old_summary': old_summary,
        'compact_own_parent_manifest': own_manifest,
        'compact_own_parent_validation': own_validation,
        'older_own_paths_bound_transitively': 421,
        'new_own_paths_including_this_manifest': len(artifacts) + 1,
        'older_plus_new_own_paths_bound_transitively': 421 + len(artifacts) + 1,
        'no_mathematical_program_CAS_scan_or_author_rerun': True,
        'no_old_shared_cache_Git_edit_spawn_contact_charge_or_bypass': True,
        'direct_weekly_total_used_percent': 64,
        'direct_weekly_telemetry_at_utc': '2026-10-17 20:26:58 UTC',
        'reset_unix': 1792745187,
        'total_ceiling_percent': 90,
        'review_integration_reserve': True,
        'artifacts': artifacts})
    for row in old_rows + artifacts + [manifest_row]:
        verify(row)
    print(json.dumps({'manifest': manifest_row, 'initial': prose[0],
                      'issues': prose[1], 'ledger': prose[2],
                      'source_checks': prose[3], 'validation': validation_row,
                      'whole_obligations': 36, 'substantive_issues': 0,
                      'old_bytes_preserved': True,
                      'new_peer_material_unread': True,
                      'total_artifacts_including_manifest': len(artifacts) + 1}, indent=2))


if __name__ == '__main__':
    main()
