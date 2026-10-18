"""AR2 documentary preservation only; no mathematical routine or enumeration."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sys

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
BASE = 'problems/2019-B4/notes/reasoning-area-return-r2-'
PARENT = 'problems/2017-B4/reviews/reasoning-pressure-return-r11-review-2-'
AU_PARENT = 'problems/2019-B4/reviews/reasoning-occupation-return-r1-review-2-'
FORBIDDEN = ('problems/2020-B4/reviews/reasoning-class-return-sq16-review-1-',
             'problems/2021-B4/reviews/reasoning-center-return-r21-')


def now():
    return datetime.now(timezone.utc).isoformat()


def allowed(path):
    assert not path.startswith(FORBIDDEN), 'Embargoed new peer material'


def rec(path):
    allowed(path)
    raw = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(raw),
            'sha256': hashlib.sha256(raw).hexdigest()}


def load(path):
    allowed(path)
    return json.loads((ROOT / path).read_text())


def check(rows):
    for row in rows:
        assert rec(row['path']) == {k: row[k] for k in ('path', 'bytes', 'sha256')}, row['path']


def unique(rows):
    seen = {}
    for row in rows:
        clean = {k: row[k] for k in ('path', 'bytes', 'sha256')}
        assert row['path'] not in seen or seen[row['path']] == clean
        seen[row['path']] = clean
    return [seen[p] for p in sorted(seen)]


def summary(rows):
    clean = unique(rows)
    raw = json.dumps(clean, sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(rows), 'unique_paths': len(clean),
            'canonical_deduplicated_sha256': hashlib.sha256(raw).hexdigest()}


def put(suffix, data):
    with (ROOT / (BASE + suffix)).open('x') as stream:
        stream.write(json.dumps(data, indent=2) + '\n')


def parent_guards():
    parent = load(PARENT + 'baseline-v1.json')
    rows = parent['direct_records'] + load(AU_PARENT + 'baseline-v1.json')['records']
    check(rows)
    assert summary(rows) == parent['effective_guard_summary']
    return rows


def protected(baseline):
    check(baseline['direct_records'])
    old = parent_guards()
    rows = baseline['direct_records'] + old
    assert summary(rows) == baseline['effective_guard_summary']
    return rows


mode = sys.argv[1]
if mode == 'prepare':
    own = sorted(p.name for p in (ROOT / 'problems/2019-B4/notes').glob('reasoning-area-return-r2-*'))
    assert own == ['reasoning-area-return-r2-admin-v1.py'], own
    parent_id = {'path': PARENT + 'manifest-v1.json', 'bytes': 1959,
                 'sha256': 'd059a9f0be6a247ae32a4c62f382cd7d3f070a02ae7f42552c2198223e27d2ff'}
    check([parent_id])
    parent = load(PARENT + 'manifest-v1.json')
    parent_rows = parent['payloads'] + [parent_id]
    check(parent_rows)
    old = parent_guards()
    direct_paths = [
        'problems/2019-B4/statement.md',
        'problems/2019-B4/proof.md',
        'problems/2019-B4/notes/secondpass-canonical-renewal.md',
        'problems/2019-B4/reviews/secondpass-acceptance.md',
        'problems/2019-B4/reviews/secondpass-acceptance.json',
        'problems/2019-B4/notes/coordinator-unmarked-greedy-failure-v1.md',
        'problems/2019-B4/notes/coordinator-critical-code-countermodel-v1.md',
        'problems/2019-B4/notes/linear-output-return-r1-candidate-v1.md',
        'problems/2019-B4/notes/reasoning-return-r3-candidate-v1.md',
        'problems/2019-B4/proofs/reviewed-reasoning-cut-transfer-r4-v1.2.md',
        'problems/2019-B4/proofs/reviewed-reasoning-cut-number-r3-v1.1.md',
        'problems/2019-B4/proofs/reviewed-reasoning-critical-return-r2-v1.1.md',
        'problems/2019-B4/reviews/walk-Frechet-review-2-source-checks-v1.md',
    ]
    authorities = []
    for name in ['reasoning-return-r7', 'reasoning-cut-transfer-r6',
                 'reasoning-occupation-return-r1', 'reasoning-growth-return-r1']:
        ap = 'problems/2019-B4/reviews/' + name + '-acceptance.json'
        authority = load(ap)
        rows = [authority['candidate'], authority['accepted_copy']] + authority['verification_metadata']
        check(rows)
        authorities += rows
        direct_paths += [ap, ap[:-5] + '.md']
    direct = unique(parent_rows + authorities + [rec(p) for p in direct_paths])
    check(direct)
    put('baseline-v1.json', {
        'prepared_utc': now(), 'status': 'PASS; compact immutable parent bindings',
        'direct_records': direct,
        'direct_summary': summary(parent_rows + authorities + [rec(p) for p in direct_paths]),
        'effective_guard_summary': summary(direct + old),
        'parent_metadata_identity': rec(PARENT + 'baseline-v1.json'),
        'parent_historical_guard_summary': parent['effective_guard_summary'],
        'guard_model_read_scope': 'Historical bytes hashed for preservation only; fresh mathematics is listed literally in sources.',
        'mutable_protocol_observation_not_an_immutable_guard': rec('AGENTS.md'),
        'all_old_mathematical_payloads_preserved': True,
        'new_SQ16_peer_file_inventory_open_hash_or_findings_access': False,
        'new_R21_peer_file_inventory_open_hash_or_findings_access': False,
        'historical_AU_release_and_admin_identity_exception_preserved_in_parent': True,
        'mathematical_code_CAS_scan_test_or_old_replay': False})
    print(json.dumps({'mode': mode, 'direct': summary(direct),
                      'effective': summary(direct + old)}))
elif mode == 'freeze':
    baseline = load(BASE + 'baseline-v1.json')
    protected(baseline)
    ledger = (ROOT / (BASE + 'obligations-v1.md')).read_text()
    labels = [line.split('|')[1].strip() for line in ledger.splitlines() if line.startswith('| AR2-O')]
    assert labels == ['AR2-O' + str(i).zfill(2) for i in range(1, 49)]
    paths = sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / 'problems/2019-B4/notes').glob('reasoning-area-return-r2-*'))
    assert len(paths) == 10, paths
    put('freeze-v1.json', {
        'frozen_utc': now(), 'constructor': '/root/review_2021_reasoning_j15_r2',
        'status': 'candidate proof - unverified', 'claims': ['AR1', 'AR2', 'AR3', 'AR4'],
        'whole_obligations': 48, 'payload_count': 10, 'ENTIRE_files': 11,
        'payloads': [rec(p) for p in paths],
        'effective_guard_summary': baseline['effective_guard_summary'],
        'FULL_final_ALL10_payload_model_readback_completed': True,
        'FULL_manifest_model_readback_then_SEPARATE_readonly_verify_REQUIRED': True,
        'two_OTHER_initially_blind_ENTIRE_whole_audits_and_root_reconciliation_required': True,
        'constructor_and_any_new_inference_contributor_excluded_from_review_count': True,
        'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'independent_effective_setting_readback': None,
        'latest_authoritative_weekly_total_used': 60,
        'latest_authoritative_telemetry_utc': '2026-10-18T18:31:22+00:00',
        'authorized_reset': 1792874445, 'ceiling_total': 90,
        'mathematical_program_CAS_scan_test_source_author_old_replay': False,
        'full_uniform_RN_quadratic_area_upper_or_actual_regime_or_exact_lambda_or_annual_or_novelty_claim': False})
    print(json.dumps(rec(BASE + 'freeze-v1.json')))
elif mode == 'verify':
    frozen = load(BASE + 'freeze-v1.json')
    check(frozen['payloads'])
    protected(load(BASE + 'baseline-v1.json'))
    print(json.dumps({'SEPARATE_read_only_verify_utc': now(), 'status': 'PASS',
                      'ENTIRE_files': 11, 'whole_obligations': 48,
                      'effective_guard_summary': frozen['effective_guard_summary'],
                      'main': rec(BASE + 'candidate-v1.md'),
                      'manifest': rec(BASE + 'freeze-v1.json')}))
else:
    raise SystemExit('Unknown documentary mode')
