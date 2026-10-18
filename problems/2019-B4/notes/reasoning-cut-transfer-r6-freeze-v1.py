#!/usr/bin/env python3
"""NEW metadata only: no mathematical enumeration, test or certificate replay.

--prepare writes only this prefix's validation; --freeze writes only its
new freeze after the model's full payload readback; --verify is read-only.
No old/source/author program is executed or historical inventory expanded.
"""
from pathlib import Path
import datetime
import hashlib
import json
import re
import sys

BASE = Path(__file__).resolve().parents[3]
PREFIX = 'problems/2019-B4/notes/reasoning-cut-transfer-r6-'
BASELINE = PREFIX + 'baseline-v1.json'
VALIDATION = PREFIX + 'input-validation-v1.json'
FREEZE = PREFIX + 'freeze-v1.json'
SUFFIXES = ['candidate-v1.md', 'obligations-v1.md', 'failed-routes-v1.md',
            'issues-v1.md', 'sources-v1.md', 'sources-v1.json',
            'worklog-v1.md', 'baseline-v1.json', 'freeze-v1.py',
            'input-validation-v1.json']
EXPECTED = list(range(1, 65))


def read_json(path):
    return json.loads((BASE / path).read_text())


def fingerprint(path):
    blob = (BASE / path).read_bytes()
    return {'path': path, 'bytes': len(blob),
            'sha256': hashlib.sha256(blob).hexdigest()}


def check_row(row):
    actual = fingerprint(row['path'])
    assert actual == {k: row[k] for k in ['path', 'bytes', 'sha256']}, (
        'fingerprint mismatch', row['path'], actual, row)
    return actual


def inspect_inputs():
    baseline = read_json(BASELINE)
    rows = [check_row(row) for row in baseline['direct_inputs']]
    accepted = []
    for path in baseline['accepted_authorities']:
        authority = read_json(path)
        assert authority['status'] == 'proved, independently reviewed scoped partial result'
        candidate = check_row(authority['candidate'])
        accepted_copy = check_row(authority['accepted_copy'])
        assert (BASE / accepted_copy['path']).read_bytes().endswith(
            (BASE / candidate['path']).read_bytes()), ('suffix', path)
        rows.extend([candidate, accepted_copy])
        accepted.append({'authority': fingerprint(path),
                         'accepted_copy': accepted_copy,
                         'unchanged_candidate_suffix': candidate,
                         'historical_occurrences_bound_not_replayed':
                             authority.get('record_occurrences_verified'),
                         'historical_paths_bound_not_replayed':
                             authority.get('unique_paths_verified')})
    erratum_path = ('problems/2019-B4/reviews/'
                    'reasoning-cut-transfer-r4-presentation-erratum-v1.json')
    erratum = read_json(erratum_path)
    operative = check_row(erratum['operative_accepted_copy'])
    suffix = check_row(erratum['unchanged_candidate_suffix'])
    assert (BASE / operative['path']).read_bytes().endswith(
        (BASE / suffix['path']).read_bytes())
    rows.extend([operative, suffix])
    parent_path = baseline['older_own_parent']['path']
    parent = read_json(parent_path)
    parent_payloads = [check_row(row) for row in parent['payloads']]
    assert len(parent_payloads) + 1 == parent['ENTIRE_review_files_including_manifest'] == 10
    assert parent['older_plus_new_own_paths_bound_transitively'] == 813
    rows.extend(parent_payloads)
    unique = {}
    for row in rows:
        assert row['path'] not in unique or unique[row['path']] == row
        unique[row['path']] = row
    canonical = json.dumps([unique[k] for k in sorted(unique)],
                           sort_keys=True, separators=(',', ':')).encode()
    labels = [int(x) for x in re.findall(r'\*\*R6-(\d{2})',
                  (BASE / (PREFIX + 'obligations-v1.md')).read_text())]
    assert labels == EXPECTED, labels
    summary = {
        'direct_baseline_rows': len(baseline['direct_inputs']),
        'necessary_fingerprint_occurrences': len(rows),
        'necessary_unique_paths': len(unique),
        'canonical_necessary_guard_sha256': hashlib.sha256(canonical).hexdigest(),
        'whole_obligation_labels': len(labels),
        'accepted_suffixes_verified': len(accepted),
        'operative_CT_v1_2_suffix_verified': True,
        'immediate_own_parent_payloads_verified': len(parent_payloads),
        'older_own_paths_bound_transitively_not_all_freshly_rehashed': 813,
        'historical_nested_inventories_replayed': False,
        'mathematical_claims_evaluated_by_code': False,
    }
    return summary, accepted


def write_new(path, obj):
    target = BASE / path
    assert str(target).startswith(str(BASE / PREFIX)), target
    assert not target.exists(), ('refusing overwrite', path)
    target.write_text(json.dumps(obj, indent=2) + '\n')


def main():
    mode = sys.argv[1] if len(sys.argv) == 2 else '--verify'
    assert mode in ['--prepare', '--freeze', '--verify']
    summary, accepted = inspect_inputs()
    if mode == '--prepare':
        write_new(VALIDATION, {
            'verified_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'status': 'PASS: necessary immutable roots, suffixes, immediate parent and labels only',
            'summary': summary,
            'accepted_operative_bindings': accepted,
            'only_new_assigned_prefix_written': True,
            'no_old_shared_git_cache_write_or_math_program': True,
        })
        print(json.dumps({'mode': mode, 'validation': fingerprint(VALIDATION),
                          'summary': summary}))
        return
    validation = read_json(VALIDATION)
    assert validation['summary'] == summary
    if mode == '--freeze':
        assert not (BASE / FREEZE).exists()
        assert all((BASE / (PREFIX + s)).is_file() for s in SUFFIXES)
        manifest = {
            'frozen_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'status': 'candidate proof - unverified; ENTIRE constructor checkpoint',
            'constructor': '/root/review_2022_complexity_r2',
            'constructor_excluded_from_both_required_audits': True,
            'root_supplied_NEW_mathematical_inference': False,
            'TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits_required': True,
            'claims': ['AT1', 'AT2', 'AT3', 'AT4'],
            'whole_obligations': 64,
            'all64_have_separate_constructor_dispositions': True,
            'only_2019_B4b': True,
            'actual_renewal_regime_or_exact_lambda_or_annual_or_priority_claim': False,
            'actual_delocalization_or_full_high_cut_mass_bound_proved': False,
            'full_area_identity_and_actual_reachability_counterfamily': True,
            'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
            'independent_effective_readback': None,
            'main': fingerprint(PREFIX + 'candidate-v1.md'),
            'necessary_guard_summary': summary,
            'immediate_own_parent': fingerprint(read_json(BASELINE)['older_own_parent']['path']),
            'older_own_paths_bound_transitively': 813,
            'ENTIRE_files_including_freeze': len(SUFFIXES) + 1,
            'older_plus_new_own_paths_bound_transitively': 813 + len(SUFFIXES) + 1,
            'FULL_final_model_readback_ALL10_payloads_code_generated_metadata_attested_before_freeze': True,
            'FULL_manifest_model_readback_then_SEPARATE_readonly_verify_required': True,
            'no_mathematical_program_CAS_scan_test_optimizer_author_source_old_replay': True,
            'no_Git_shared_old_cache_mutation_spawn_charge_contact_bypass': True,
            'NEW_corresponding_R14_or_R19_affected_peer_files_findings_hashes_metadata_accessed': False,
            'authoritative_weekly_telemetry': {
                'observed_at_utc': '2026-10-18 14:30:20 UTC',
                'method': 'own direct clock/get_usage_limits same awaited batch',
                'TOTAL_used_percent': 43, 'window_minutes': 10080,
                'reset_unix': 1792874445, 'ordinary_usage_allowed': True,
                'legacy_by_limit_agree': True, 'account_label': '029a8928...1334ac3a',
                'TOTAL_ceiling_percent': 90, 'integration_reserve': True,
                'human_authorized_current_window_only': True,
                'automatic_later_window_spending': False,
            },
            'payloads': [fingerprint(PREFIX + s) for s in SUFFIXES],
        }
        write_new(FREEZE, manifest)
        print(json.dumps({'mode': mode, 'freeze': fingerprint(FREEZE),
                          'main': manifest['main'], 'summary': summary}))
        return
    manifest = read_json(FREEZE)
    assert manifest['necessary_guard_summary'] == summary
    assert len(manifest['payloads']) == len(SUFFIXES)
    for row in manifest['payloads']:
        check_row(row)
    assert {r['path'] for r in manifest['payloads']} == {PREFIX+s for s in SUFFIXES}
    print(json.dumps({'mode': mode, 'verified_at_utc':
                      datetime.datetime.now(datetime.timezone.utc).isoformat(),
                      'status': 'PASS; SEPARATE read-only verify; no writes',
                      'ENTIRE_files': len(SUFFIXES)+1,
                      'freeze': fingerprint(FREEZE),
                      'main': fingerprint(PREFIX + 'candidate-v1.md'),
                      'summary': summary}))


if __name__ == '__main__':
    main()
