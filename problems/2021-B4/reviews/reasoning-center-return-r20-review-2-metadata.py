"""NEW R20 review2 metadata only: exact paths, bytes, SHA, JSON and labels.

No mathematics, network, subprocess, directory enumeration or old script
execution. Writes use exclusive creation under this NEW review prefix.
Run prepare, read every final payload, freeze, read manifest, then invoke
verify separately. verify is read-only.
"""
from pathlib import Path
import datetime
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
PREFIX = 'problems/2021-B4/reviews/reasoning-center-return-r20-review-2-'
AUTHOR = 'problems/2021-B4/notes/reasoning-center-return-r20-'
AUTHOR_FREEZE = AUTHOR + 'freeze-v1.json'
AUTHOR_BASELINE = AUTHOR + 'baseline-v1.json'
PARENT = 'problems/2024-B4/reviews/reasoning-cofactor-return-r8-review-2-manifest.json'
R18_BODY = 'problems/2021-B4/proofs/reviewed-reasoning-center-return-r18-v1.1.md'
R18_AUTHORITY = 'problems/2021-B4/reviews/reasoning-center-return-r18-acceptance.json'
MANIFEST = PREFIX + 'manifest.json'
BASELINE = PREFIX + 'baseline.json'
VALIDATION = PREFIX + 'input-validation.json'
SOURCES_JSON = PREFIX + 'sources.json'
PAYLOAD_NAMES = [
    'report.md', 'ledger.md', 'issues.md', 'sources.md', 'sources.json',
    'worklog.md', 'metadata.py', 'baseline.json', 'input-validation.json']
PAYLOADS = [PREFIX + name for name in PAYLOAD_NAMES]

KNOWN = [
    {'path': AUTHOR + 'candidate-v1.md', 'bytes': 15053,
     'sha256': '7363e0002bddfb05864af81d1bad2c469e4adeff3b7b7703bbf9b203e4ecc371'},
    {'path': AUTHOR_FREEZE, 'bytes': 3306,
     'sha256': '8b69fb88b967acd31605e9189cbd02b5566ba4f656fe5e0811b616efbff5cbb4'},
    {'path': PARENT, 'bytes': 4551,
     'sha256': '42a27cbd1875ad02b21543871335028eb0b57a1d2377eb7281611d0cc99f326e'},
    {'path': R18_BODY, 'bytes': 26067,
     'sha256': 'f26de3a17895354408e514d6a0b0066715a1c0f0234d494fd53485ea3feb8284'}]

TELEMETRY = {
    'at_utc': '2026-10-18 15:17:43 UTC',
    'method': 'own same-awaited clock/get_usage_limits',
    'TOTAL_used_percent': 46, 'window_minutes': 10080,
    'resetsAt': 1792874445, 'ordinary_usage_allowed': True,
    'legacy_by_limit_agree': True, 'account_label': '029a8928...1334ac3a',
    'TOTAL_ceiling_percent': 90, 'integration_reserve': True,
    'human_authorized_current_window_only': True,
    'automatic_later_window_spending': False}

SOURCE_RECORDS = {
    'date_utc': '2026-10-18',
    'status': 'OTHER initially blind WHOLE2 initial, not promotion; findings embargoed',
    'whole_obligations': 48,
    'sources': [
        {'id': 'O1',
         'url': 'https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf',
         'fresh_read': 'Page2 B4 setup and(b); actual rational coefficients and per-order rational common values',
         'local_statement_freshly_read': True,
         'preliminary_proof_researched': False, 'raw_pdf_sha256': None},
        {'id': 'A1', 'path': R18_BODY,
         'fresh_read': 'ENTIRE accepted body/current complete MD and JSON; clipped combined display recovered by overlapping bounded reads',
         'operative_scope': 'actual(S),(W),m4,adjacent centers; actual Section3 equation(8); frameII full gcds and actual origin pairing',
         'historical_label_distinguished_from_current_acceptance': True,
         'old_ancestor_full_math_freshly_recertified': False},
        {'id': 'L1', 'authors': 'Castryck, Laterveer, Ounaies',
         'url': 'https://arxiv.org/pdf/1208.5404',
         'fresh_read': 'CA/type/scenario definitions; Lemma6; ENTIRE Sections3.1-3.3 including Lemma14 and Proposition15 proof; Proposition16 statement and ENTIRE proof',
         'role': 'established valuation and coefficient methods, rederived for rational localization',
         'Proposition19_or_unramified_variant_imported': False,
         'whole_paper_or_source_program_audited': False,
         'raw_pdf_sha256': None},
        {'id': 'L2', 'author': 'Cesar Massri',
         'url': 'https://arxiv.org/pdf/1806.09561v6',
         'version': 'v6 25Aug2023',
         'fresh_read': 'CA and recycled-value definitions; normalized/net derivative notation; ENTIRE Proposition7.7 proof/Remark7.8; ENTIRE Theorem7.10 proof and computation boundary',
         'role': 'known SAME-value H4/H16 prohibition and three-value scope; neither supplies the new four-value proof',
         'source_computation_replayed_or_certified': False,
         'whole_paper_audit_or_priority_claim': False,
         'raw_pdf_sha256': None},
        {'id': 'L3', 'author': 'Mohammad F. Marashdeh',
         'url': 'https://arxiv.org/abs/2608.14726',
         'fresh_read': 'author/title/version/submission record and abstract ONLY',
         'Theorem4_proof_read': False, 'theorem_imported': False,
         'role': 'nonoperative discovery context only'}],
    'author_ENTIRE13_files_freshly_read': True,
    'reviewer_did_not_construct_NEW_R20': True,
    'older_roles': '2021R9 constructor; older whole reviewers including R18 and original/affected R19; not self-recertification',
    'R19_theorem_used': False,
    'own_R8_disposition_release_only_after_its_explicit_BOTH_confirmation': True,
    'NEW_root_R20_filename_content_finding_hash_metadata_access': False,
    'mathematical_program_CAS_scan_test_optimizer_old_author_source_replay': False,
    'Git_shared_old_cache_mutation_spawn_charge_contact_bypass': False,
    'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
    'independent_effective_readback': None,
    'authoritative_weekly_telemetry': TELEMETRY}


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def checked_path(path):
    assert isinstance(path, str) and not Path(path).is_absolute()
    assert '..' not in Path(path).parts
    assert not path.startswith('problems/2021-B4/reviews/reasoning-center-return-r20-review-1-')
    assert not path.startswith('.cache/')
    resolved = (ROOT / path).resolve()
    assert resolved.is_relative_to(ROOT)
    return resolved


def blob(path):
    return checked_path(path).read_bytes()


def read(path):
    return json.loads(blob(path))


def fp(path):
    value = blob(path)
    return {'path': path, 'bytes': len(value),
            'sha256': hashlib.sha256(value).hexdigest()}


def check(record):
    result = fp(record['path'])
    assert result == {key: record[key] for key in ('path', 'bytes', 'sha256')}, result
    return result


def put(path, value):
    assert path.startswith(PREFIX)
    with checked_path(path).open('x') as stream:
        json.dump(value, stream, indent=2)
        stream.write('\n')


def canonical(records):
    by_path = {}
    for record in records:
        row = {key: record[key] for key in ('path', 'bytes', 'sha256')}
        old = by_path.setdefault(row['path'], row)
        assert old == row
    unique = [by_path[path] for path in sorted(by_path)]
    encoded = json.dumps(unique, sort_keys=True, separators=(',', ':')).encode()
    return unique, hashlib.sha256(encoded).hexdigest()


def labels():
    wanted = {f'R20-{i:02d}' for i in range(1, 49)}
    paths = [AUTHOR + 'obligations-v1.md', AUTHOR + 'checks-v1.md', PREFIX + 'ledger.md']
    for path in paths:
        found = re.findall(r'^\|(R20-\d\d)\|', blob(path).decode(), re.M)
        assert len(found) == 48 and set(found) == wanted, path
    return {'ALL48_author_obligation_constructor_and_separate_reviewer_labels_match': True}


def current_inputs():
    for record in KNOWN:
        check(record)
    author = read(AUTHOR_FREEZE)
    assert author['ENTIRE_files'] == 13 and len(author['payloads']) == 12
    rows = [fp(AUTHOR_FREEZE)] + [check(row) for row in author['payloads']]
    base = read(AUTHOR_BASELINE)
    protected = base['protected']
    assert len(protected) == base['unique_paths'] == 48
    _, declared_digest = canonical(protected)
    assert declared_digest == base['canonical_deduplicated_sha256']
    rows += [check(row) for row in protected]
    parent = read(PARENT)
    assert parent['ENTIRE_review_files_including_manifest'] == 10
    assert len(parent['payloads']) == 9
    rows += [fp(PARENT)] + [check(row) for row in parent['payloads']]
    assert parent['older_plus_new_own_paths_bound_transitively'] == 844
    authority = read(R18_AUTHORITY)
    check(authority['candidate'])
    check(authority['accepted_copy'])
    assert blob(R18_BODY).endswith(blob(authority['candidate']['path']))
    unique, digest = canonical(rows)
    summary = {
        'fingerprint_occurrences': len(rows), 'unique_paths': len(unique),
        'canonical_sha256': digest,
        'author_ENTIRE13_fingerprints_verified': True,
        'author_baseline_direct48_verified_without_recursive_history': True,
        'author_stored49_occurrence_summary_bound_without_reasserting_historical_math_read': True,
        'own_immediate_parent_payloads_verified': 9,
        'own_older_paths_bound_transitively': 844,
        'accepted_R18_copy_suffix_and_current_authority_verified': True,
        'mathematical_assertions_evaluated_by_code': False,
        **labels()}
    return unique, summary


def guard():
    baseline = read(BASELINE)
    for row in baseline['protected']:
        check(row)
    _, digest = canonical(baseline['protected'])
    assert digest == baseline['necessary_guard_summary']['canonical_sha256']
    _, summary = current_inputs()
    assert summary == baseline['necessary_guard_summary']
    return baseline, summary


mode = sys.argv[1]
if mode == 'prepare':
    for path in (BASELINE, VALIDATION, SOURCES_JSON, MANIFEST):
        assert not checked_path(path).exists(), path
    protected, summary = current_inputs()
    put(SOURCES_JSON, SOURCE_RECORDS)
    put(BASELINE, {
        'captured_at_utc': utc(),
        'status': 'OTHER initially blind ENTIRE WHOLE2 review baseline; findings embargoed',
        'scope': 'author13 + compact directly declared48 + immediate own parent10; no recursive history copy',
        'author_freeze': fp(AUTHOR_FREEZE), 'author_compact_baseline': fp(AUTHOR_BASELINE),
        'author_stored_occurrence_count': read(AUTHOR_BASELINE)['verified_record_occurrences'],
        'own_immediate_parent': fp(PARENT),
        'older_own_paths_bound_transitively': 844,
        'necessary_guard_summary': summary, 'protected': protected,
        'NEW_root_R20_filename_content_finding_hash_metadata_access': False,
        'preservation_binding_is_fresh_historical_mathematical_reading': False})
    put(VALIDATION, {'at_utc': utc(), 'result': 'PASS',
                     'whole_obligations': 48, 'separate_hand_dispositions': 48,
                     'necessary_guard_summary': summary,
                     'only_assigned_NEW_prefix_written': True,
                     'mathematical_execution': False})
    print(json.dumps({'mode': mode, 'result': 'PASS', **summary,
                      'baseline': fp(BASELINE)}, indent=2))
elif mode == 'freeze':
    assert not checked_path(MANIFEST).exists()
    baseline, summary = guard()
    payloads = [fp(path) for path in PAYLOADS]
    put(MANIFEST, {
        'frozen_at_utc': utc(),
        'status': 'ENTIRE initially blind OTHER WHOLE2 initial; findings EMBARGOED; not promotion',
        'reviewer': '/root/review_2022_complexity_r2',
        'A_sole_NEW_constructor_excluded': True,
        'reviewer_NEW_R20_construction_contribution': False,
        'older_roles_disclosed_not_self_recertification': True,
        'requested': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
        'independent_effective_readback': None,
        'whole_obligations': 48, 'separate_hand_dispositions': 48,
        'author_ENTIRE_files_FULLread': 13,
        'substantive_defects_or_required_repairs_found': 0, 'closed_notes': 8,
        'ENTIRE_review_files_including_manifest': 10,
        'immediate_own_parent': fp(PARENT),
        'older_own_paths_bound_transitively': 844,
        'older_plus_new_own_paths_bound_transitively': 854,
        'necessary_guard_summary': summary,
        'no_corresponding_NEW_root_R20_filenames_contents_findings_hashes_metadata_accessed': True,
        'FULL_final_model_readback_ALL9_payloads_code_generated_metadata_attested': True,
        'FULL_manifest_model_readback_then_SEPARATE_readonly_verification_required': True,
        'findings_EMBARGOED_and_identity_only_until_explicit_BOTH_confirmation': True,
        'no_mathematical_program_CAS_scan_test_optimizer_or_author_source_old_replay': True,
        'no_Git_shared_old_cache_mutation_spawn_charge_contact_bypass': True,
        'authoritative_weekly_telemetry': TELEMETRY,
        'payloads': payloads})
    print(json.dumps({'mode': mode, 'result': 'PASS', 'manifest': fp(MANIFEST),
                      **summary}, indent=2))
elif mode == 'verify':
    baseline, summary = guard()
    manifest = read(MANIFEST)
    assert manifest['whole_obligations'] == manifest['separate_hand_dispositions'] == 48
    assert manifest['ENTIRE_review_files_including_manifest'] == 10
    assert len(manifest['payloads']) == 9
    for row in manifest['payloads']:
        check(row)
    assert manifest['necessary_guard_summary'] == summary
    print(json.dumps({'mode': 'SEPARATE read-only verification', 'at_utc': utc(),
                      'result': 'PASS', 'ENTIRE_files': 10, 'ALL_obligations': 48,
                      'manifest': fp(MANIFEST), 'report': fp(PREFIX + 'report.md'),
                      **summary}, indent=2))
else:
    raise SystemExit('prepare, freeze or verify only')
