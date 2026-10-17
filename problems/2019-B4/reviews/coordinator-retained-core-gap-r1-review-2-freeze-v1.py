"""Administrative fingerprint/preservation only; never evaluates mathematics."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[3]
PREFIX = 'problems/2019-B4/reviews/coordinator-retained-core-gap-r1-review-2-'
AUTHOR = 'problems/2019-B4/notes/coordinator-retained-core-gap-r1-'
PARENT = 'problems/2025-B4/reviews/reasoning-return-r8-review-2-manifest-v1.json'
ACCEPT = 'problems/2019-B4/reviews/coordinator-cap-gap-r1-acceptance.json'
EXPECTED = {
    AUTHOR + 'candidate-v1.md': (6152, '9bea48691719c0384e0a027131e6db1fad83ddd0572e8ae59578f72d71431b42'),
    AUTHOR + 'freeze-v1.json': (1965, 'd2ea714f15cc653c044943a0485bfd0908fa0279b350c07a42a811ff9b4f0681'),
    PARENT: (3375, '0567ac1077215e74c85e88bbae3477f414b7d202f20e9f1acec600dbfbd8c73d'),
}


def safe(path):
    assert isinstance(path, str) and not Path(path).is_absolute()
    assert '..' not in Path(path).parts
    assert 'coordinator-retained-core-gap-r1-review-1-' not in path
    return ROOT / path


def fp(path):
    data = safe(path).read_bytes()
    return {'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def rows(value):
    if isinstance(value, dict):
        if (isinstance(value.get('path'), str)
                and isinstance(value.get('bytes'), int)
                and isinstance(value.get('sha256'), str)):
            yield value
        for child in value.values():
            yield from rows(child)
    elif isinstance(value, list):
        for child in value:
            yield from rows(child)


def write(suffix, value):
    with safe(PREFIX + suffix).open('x') as stream:
        json.dump(value, stream, indent=2)
        stream.write('\n')


def check(row):
    actual = fp(row['path'])
    assert actual == {key: row[key] for key in actual}, row['path']
    return actual


def baseline():
    existing = list(safe(PREFIX).parent.glob(Path(PREFIX).name + '*'))
    assert existing == [Path(__file__).resolve()], existing
    for path, (size, digest) in EXPECTED.items():
        assert fp(path) == {'path': path, 'bytes': size, 'sha256': digest}
    unique = {}
    occurrences = 0
    metadata = []
    for path in [AUTHOR + 'freeze-v1.json', AUTHOR + 'inputs-v1.json', ACCEPT, PARENT]:
        doc = json.loads(safe(path).read_bytes())
        count = 0
        for row in rows(doc):
            actual = check(row)
            unique[actual['path']] = actual
            count += 1
            occurrences += 1
        own = fp(path)
        unique[path] = own
        occurrences += 1
        metadata.append({'metadata': own, 'fingerprint_occurrences': count})
    write('baseline-v1.json', {
        'recorded_at_utc': datetime.now(timezone.utc).isoformat(),
        'administrative_only': True,
        'assigned_prefix_confirmed_unused_before_this_helper': True,
        'current_record_occurrences_verified': occurrences,
        'current_deduplicated_paths_verified': len(unique),
        'metadata_sources': metadata,
        'records': [unique[path] for path in sorted(unique)],
        'compact_immutable_own_parent': fp(PARENT),
        'earlier_own_paths_bound_by_parent': 455,
        'historical_inventory_not_recopied_or_claimed_freshly_rehashed': True,
        'new_peer_retained_core_report_findings_and_metadata_unread': True,
    })
    print(json.dumps({'baseline': fp(PREFIX + 'baseline-v1.json'),
                      'occurrences': occurrences, 'paths': len(unique)}, indent=2))


def freeze():
    assert not safe(PREFIX + 'manifest-v1.json').exists()
    base = json.loads(safe(PREFIX + 'baseline-v1.json').read_bytes())
    for row in base['records']:
        check(row)
    ledger = safe(PREFIX + 'ledger-v1.md').read_text()
    for n in range(1, 17):
        assert ledger.count('|RC-%02d|' % n) == 1
    stamp = datetime.now(timezone.utc).isoformat()
    write('input-validation-v1.json', {
        'verified_at_utc': stamp,
        'all_declared_current_fingerprints_still_match': True,
        'record_occurrences': base['current_record_occurrences_verified'],
        'deduplicated_paths': base['current_deduplicated_paths_verified'],
        'immutable_own_parent': fp(PARENT),
        'earlier_own_paths_preserved_through_compact_parent': 455,
        'mathematical_program_CAS_scan_sign_evaluation_or_author_replay': False,
        'new_peer_retained_core_material_unread': True,
    })
    write('metadata-v1.json', {
        'recorded_at_utc': stamp,
        'reviewer': '/root/review_2017_coarsening_r1',
        'new_constructor': '/root',
        'requested_settings': {'model': 'gpt-6.1-sol', 'reasoning': 'max'},
        'independently_verified_effective_settings': None,
        'whole_obligations': 16,
        'old_CG_hand_method_role_disclosed_not_new_RC_constructor': True,
        'two_OTHER_whole_audits_and_root_reconciliation_required': True,
        'new_peer_RC_reports_findings_and_metadata_unread_before_entire_freeze': True,
        'latest_direct_weekly_telemetry': {
            'at_utc': '2026-10-17 20:04:23 UTC', 'usedPercent': 62,
            'windowDurationMins': 10080, 'resetsAt': 1792745187,
            'ordinaryUsageAllowed': True, 'stop_at_total_percent': 90,
        },
        'native_mathematical_job': None,
        'new_external_theorem_import': False,
        'official_PDF_B4b_read_through_web_no_download_or_remote_hash_claim': True,
        'verdict': 'no substantive defect in exact scoped retained-core estimate and hand endpoint',
    })
    suffixes = ['initial-v1.md', 'issues-v1.md', 'ledger-v1.md', 'sources-v1.md',
                'worklog-v1.md', 'baseline-v1.json', 'metadata-v1.json',
                'input-validation-v1.json', 'freeze-v1.py']
    artifacts = [fp(PREFIX + suffix) for suffix in suffixes]
    write('manifest-v1.json', {
        'frozen_at_utc': stamp,
        'status': 'COMPLETE initially blind WHOLE retained-core gap R2 initial',
        'reviewer': '/root/review_2017_coarsening_r1',
        'new_constructor': '/root',
        'target_main': fp(AUTHOR + 'candidate-v1.md'),
        'target_freeze': fp(AUTHOR + 'freeze-v1.json'),
        'whole_obligations': 16,
        'all_five_constructor_artifacts_and_exact_accepted_inputs_covered': True,
        'new_peer_RC_reports_findings_and_metadata_unread_until_entire_initial_frozen': True,
        'old_CG_hand_method_role_disclosed_no_self_recertification': True,
        'verdict': 'no substantive defect in exact scoped retained-core estimate and hand endpoint',
        'substantive_issues': 0,
        'required_repairs': 0,
        'record_occurrences_verified': base['current_record_occurrences_verified'],
        'deduplicated_paths_verified': base['current_deduplicated_paths_verified'],
        'compact_immutable_own_parent': fp(PARENT),
        'earlier_own_paths_preserved': 455,
        'mathematical_code_CAS_scan_sign_child_or_author_rerun': False,
        'no_exact_rate_annual_renewal_regime_matching_scale_or_novelty_claim': True,
        'artifacts': artifacts,
    })
    print(json.dumps({'manifest': fp(PREFIX + 'manifest-v1.json'),
                      'artifacts': len(artifacts), 'whole_obligations': 16}, indent=2))


if __name__ == '__main__':
    assert len(sys.argv) == 2 and sys.argv[1] in ['baseline', 'freeze']
    {'baseline': baseline, 'freeze': freeze}[sys.argv[1]]()
