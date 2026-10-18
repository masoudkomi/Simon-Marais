"""R22 documentary integrity only: no mathematical code or old-code execution."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
BASE = 'problems/2021-B4/notes/reasoning-center-return-r22-'
PARENT = 'problems/2020-B4/reviews/reasoning-class-return-sq17-review-2-'
SQ16 = 'problems/2020-B4/reviews/reasoning-class-return-sq16-review-2-'
AR = 'problems/2019-B4/notes/reasoning-area-return-r2-'
PR = 'problems/2017-B4/reviews/reasoning-pressure-return-r11-review-2-'
AU = 'problems/2019-B4/reviews/reasoning-occupation-return-r1-review-2-'
PARENT_ID = {'path': PARENT + 'manifest-v1.json', 'bytes': 2145,
             'sha256': '12fa9c1a98587e96ed64e915129976f7b099871413fea38eafe88f9c67498d08'}


def now():
    return datetime.now(timezone.utc).isoformat()


def obj(path):
    return json.loads((ROOT / path).read_text())


def rec(path):
    data = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}


def check(rows):
    for row in rows:
        assert rec(row['path']) == {k: row[k] for k in ('path', 'bytes', 'sha256')}, row['path']


def unique(rows):
    result = {}
    for row in rows:
        clean = {k: row[k] for k in ('path', 'bytes', 'sha256')}
        assert row['path'] not in result or result[row['path']] == clean, row['path']
        result[row['path']] = clean
    return [result[p] for p in sorted(result)]


def summary(rows):
    clean = unique(rows)
    raw = json.dumps(clean, sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(rows), 'unique_paths': len(clean),
            'canonical_deduplicated_sha256': hashlib.sha256(raw).hexdigest()}


def put(suffix, data):
    with (ROOT / (BASE + suffix)).open('x') as stream:
        stream.write(json.dumps(data, indent=2) + '\n')


def inherited():
    pr = obj(PR + 'baseline-v1.json')
    rows = pr['direct_records'] + obj(AU + 'baseline-v1.json')['records']
    check(rows)
    assert summary(rows) == pr['effective_guard_summary']
    for prefix in (AR, SQ16, PARENT):
        baseline = obj(prefix + 'baseline-v1.json')
        check(baseline['direct_records'])
        rows = baseline['direct_records'] + rows
        assert summary(rows) == baseline['effective_guard_summary']
    assert summary(rows) == obj(PARENT + 'manifest-v1.json')['effective_guard_summary']
    return rows


def protect(baseline):
    check(baseline['direct_records'])
    assert summary(baseline['direct_records'] + inherited()) == baseline['effective_guard_summary']


mode = sys.argv[1]
if mode == 'prepare':
    check([PARENT_ID])
    parent_rows = obj(PARENT + 'manifest-v1.json')['payloads'] + [PARENT_ID]
    assert len(parent_rows) == 5
    check(parent_rows)
    sources = obj(BASE + 'sources-v1.json')
    source_rows = sources['operative_accepted_full_body_and_each_full_MDJSON']
    direct_rows = parent_rows[:]
    authority_occurrences = []
    for source in source_rows:
        check([source])
        prefix = source['authority_prefix']
        authority = obj(prefix + '.json')
        assert authority['unresolved_substantive_issues'] == 0
        rows = [authority['candidate'], authority['accepted_copy']] + authority['verification_metadata']
        check(rows)
        authority_occurrences.extend(rows)
        direct_rows.extend(rows + [rec(prefix + '.md'), rec(prefix + '.json')])
    local_paths = ['AGENTS.md', 'problems/2021-B4/statement.md'] + sources['old_complete_context_only']
    direct_rows.extend(rec(path) for path in local_paths)
    direct = unique(direct_rows)
    old = inherited()
    put('baseline-v1.json', {
        'prepared_utc': now(), 'direct_records': direct,
        'current_input_occurrence_summary': summary(direct_rows),
        'authority_declared_occurrence_summary': summary(authority_occurrences),
        'effective_guard_summary': summary(direct + old),
        'parent_ENTIRE_identity': PARENT_ID,
        'parent_guard_metadata': rec(PARENT + 'baseline-v1.json'),
        'parent_guard_summary_bound_not_recopied': summary(old),
        'guard_checks_are_byte_preservation_not_fresh_mathematical_reads': True,
        'mutable_coordinator_map_or_NEW_R22_peer_material_used': False,
        'all_older_bytes_preserved': True})
    put('metadata-v1.json', {
        'created_utc': now(), 'constructor': '/root/review_2021_reasoning_j15_r2',
        'status': 'candidate proof - unverified', 'whole_obligations': 48,
        'claims': ['R22A', 'R22B', 'R22C'],
        'entire_integral_frame_branch_proposed_excluded': True,
        'negative_tied_frameIII_or_degree20_or_annual_excluded': False,
        'two_OTHER_initially_blind_ENTIRE_whole_audits_and_root_reconciliation_required': True,
        'constructor_excluded_from_audits': True,
        'NEW_root_proof_inference_supplied': False,
        'older_R18_R20_R21_and_root_OLD_exploration_roles_disclosed': True,
        'effective_guard_summary': summary(direct + old),
        'parent_immutable_bound_not_giant_recopied': True,
        'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'independent_effective_setting_readback': None,
        'authoritative_telemetry': {
            'observed_utc': '2026-10-18 22:00:35 UTC', 'TOTAL_weekly_usedPercent': 63,
            'windowDurationMins': 10080, 'resetsAt': 1792874445,
            'ordinaryUsageAllowed': True, 'legacy_and_by_limit_agree': True,
            'account_id': '029a8928-15a9-456a-84f9-d2e61334ac3a',
            'TOTAL_ceiling': 90, 'integration_reserve': True,
            'automatic_later_week_authorized': False},
        'mathematical_program_CAS_scan_test_optimizer_author_source_old_replay': False,
        'new_own_documentary_code_only': True,
        'shared_Git_old_cache_mutation_spawn_charge_contact_bypass': False,
        'pending_native_job_retrieval_or_approval': False,
        'FULL_final_all8_payloads_then_freeze_manifest_model_readback_and_SEPARATE_verify_required': True})
    print(json.dumps({'mode': mode, 'direct': summary(direct),
                      'effective': summary(direct + old)}))
elif mode == 'freeze':
    baseline = obj(BASE + 'baseline-v1.json')
    protect(baseline)
    labels = re.findall(r'^\|(R22-\d{2})\|', (ROOT / (BASE + 'obligations-v1.md')).read_text(), re.M)
    assert labels == ['R22-' + str(i).zfill(2) for i in range(1, 49)]
    paths = sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / 'problems/2021-B4/notes').glob('reasoning-center-return-r22-*'))
    assert len(paths) == 8, paths
    put('freeze-v1.json', {
        'frozen_utc': now(), 'status': 'candidate proof - unverified',
        'constructor': '/root/review_2021_reasoning_j15_r2',
        'whole_obligations': 48, 'payload_count': 8, 'ENTIRE_files': 9,
        'payloads': [rec(path) for path in paths],
        'effective_guard_summary': baseline['effective_guard_summary'],
        'FULL_final_ALL8_payload_model_readback_completed': True,
        'FULL_manifest_model_readback_then_SEPARATE_readonly_verify_REQUIRED': True,
        'constructor_excluded_two_OTHER_initially_blind_ENTIRE_whole_audits_required': True,
        'NEW_root_proof_inference_supplied': False,
        'negative_tied_case_full_frameIII_degree20_annual_priority_claim': False,
        'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'independent_effective_setting_readback': None,
        'mathematical_program_CAS_scan_test_optimizer_source_author_old_replay': False})
    print(json.dumps(rec(BASE + 'freeze-v1.json')))
elif mode == 'verify':
    frozen = obj(BASE + 'freeze-v1.json')
    check(frozen['payloads'])
    protect(obj(BASE + 'baseline-v1.json'))
    print(json.dumps({'SEPARATE_readonly_verify_utc': now(), 'status': 'PASS',
                      'ENTIRE_files': 9, 'whole_obligations': 48,
                      'effective_guard_summary': frozen['effective_guard_summary'],
                      'candidate': rec(BASE + 'candidate-v1.md'),
                      'manifest': rec(BASE + 'freeze-v1.json')}))
else:
    raise SystemExit('Unknown documentary mode')
