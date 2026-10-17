"""Administrative whole-review integrity freeze. No mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
BASE = Path('problems/2022-B4/reviews')
PRE = 'reasoning-return-r6-review-2'
OUT = BASE / (PRE + '-manifest-v1.json')
NOW = datetime.now(timezone.utc).isoformat()
assert not (ROOT / OUT).exists()

def rec(path):
    path = str(path)
    data = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def check(expected):
    actual = rec(expected['path'])
    assert actual == {key: expected[key] for key in ('path', 'bytes', 'sha256')}, (expected, actual)
    return actual

def put(path, obj):
    assert not (ROOT / path).exists()
    (ROOT / path).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n')

previous_record = {
    'path': 'problems/2025-B4/notes/reasoning-return-r6-freeze-v1.json',
    'bytes': 3350,
    'sha256': '72885d683855f2bf61f5aeb225f7d17ccecc2dc1e8898c7aae88161b549a26f0'}
check(previous_record)
previous = json.loads((ROOT / previous_record['path']).read_text())
previous_validation_record = next(row for row in previous['artifacts'] if row['path'].endswith('-input-validation-v1.json'))
check(previous_validation_record)
previous_validation = json.loads((ROOT / previous_validation_record['path']).read_text())
items = previous_validation['earlier_unique_records_preserved'] + previous['artifacts'] + [previous_record]
unique = {}
for row in items:
    row = {key: row[key] for key in ('path', 'bytes', 'sha256')}
    assert row['path'] not in unique or unique[row['path']] == row
    unique[row['path']] = row
preserved = [check(row) for row in unique.values()]
assert len(preserved) == 328

target = {
    'path': 'problems/2022-B4/notes/reasoning-return-r6-candidate-v1.md',
    'bytes': 15412,
    'sha256': '051c9fec0b67dc6569d5e3be1d3c96c0c60ff977165bd67202504f738bb39832'}
author_manifest_record = {
    'path': 'problems/2022-B4/notes/reasoning-return-r6-freeze-v1.json',
    'bytes': 3784,
    'sha256': '44415c8ddcd197c8593e3738bc70ba52d07b408ee4302e0db7beb80408f39fee'}
check(target)
check(author_manifest_record)
author_manifest = json.loads((ROOT / author_manifest_record['path']).read_text())
assert len(author_manifest['artifacts']) == 9
assert author_manifest['whole_independent_audit_obligations'] == 40
author_records = [check(row) for row in author_manifest['artifacts']]
assert author_records[0] == target

fingerprint_occurrences = []
def walk(value):
    if isinstance(value, dict):
        if {'path', 'bytes', 'sha256'} <= value.keys():
            fingerprint_occurrences.append({key: value[key] for key in ('path', 'bytes', 'sha256')})
        for child in value.values():
            walk(child)
    elif isinstance(value, list):
        for child in value:
            walk(child)

for path in [
    'problems/2022-B4/notes/reasoning-return-r6-freeze-v1.json',
    'problems/2022-B4/notes/reasoning-return-r6-input-validation-v1.json',
    'problems/2022-B4/notes/reasoning-return-r6-sources-v1.json']:
    walk(json.loads((ROOT / path).read_text()))
for row in fingerprint_occurrences:
    check(row)
author_unique = {}
for row in fingerprint_occurrences:
    assert row['path'] not in author_unique or author_unique[row['path']] == row
    author_unique[row['path']] = row

accepted_f5 = {
    'path': 'problems/2022-B4/proofs/reviewed-reasoning-return-r5-v1.1.md',
    'bytes': 30324,
    'sha256': '1a2544cb8ced3bba9cc6efed1870c242c652b3e6029f39881028d4637d7c6da6'}
check(accepted_f5)
accepted_context = [accepted_f5] + [rec(path) for path in [
    'problems/2022-B4/reviews/reasoning-return-r5-acceptance.md',
    'problems/2022-B4/reviews/reasoning-return-r5-acceptance.json',
    'problems/2022-B4/proofs/reviewed-rational-base-shadow-return-v1.1.md',
    'problems/2022-B4/reviews/reasoning-return-r5-review-2-source-checks-v1.md']]
protocol_context = [rec(path) for path in [
    'AGENTS.md', 'problems/2022-B4/statement.md',
    '.cache/official/2022-paper_b.pdf',
    '.cache/literature/2022/akiyama-frougny-sakarovitch-rbns-rev.pdf',
    '.cache/literature/2022/andrieu-eliahou-vivion-2510.11723v2.pdf']]

main = (ROOT / BASE / (PRE + '-initial-v1.md')).read_text()
for section in range(10):
    assert '## %d.' % section in main
ledger = (ROOT / BASE / (PRE + '-issues-v1.md')).read_text()
for index in range(1, 41):
    assert '| R6R2-%02d |' % index in ledger

source_reads = [
    {'url': 'https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2022-paper-b.pdf', 'scope': 'actual B4(b), positive ordinary starts/product/simultaneous updates; no preliminary proof'},
    {'url': 'https://www.numdam.org/item/10.1051/ita/2011114.pdf', 'scope': 'Introduction/MD-GMD direction, complete Theorem3.26 proof; p>q,numerator-prime/canonical conditions preserved'},
    {'url': 'https://arxiv.org/pdf/1510.04121', 'scope': 'definitions, exact Theorem1 statement, Theorem2 complete written proof; bounded interval/point reachability and density limits preserved'},
    {'url': 'https://perso.telecom-paristech.fr/jsaka/PUB/Files/RBNS-rev.pdf', 'scope': 'definitions and complete Proposition37/Corollary38 proof context; old full finite-prefix reads retained'},
    {'url': 'https://arxiv.org/html/2510.11723v2', 'scope': 'exact global representation and relevant complete Section3.3 through Proposition3.13; normality remains conjectural'},
    {'url': 'https://www.researchgate.net/publication/220576840_Lower_bounds_for_Z-numbers', 'scope': 'original proper-set question, complete Lemma3.1/Propositions3.1-3.2 proof passages; singleton/conditional scope'},
    {'url': 'https://arxiv.org/pdf/2505.14150', 'scope': 'introduction, Theorem1 and available beginning of proof; later bounded web-open internal error, not full32-page proof or binary hash'}]

validation_path = BASE / (PRE + '-input-validation-v1.json')
put(validation_path, {
    'validated_at_utc': NOW,
    'administrative_integrity_only': True,
    'target_nine_artifacts_and_manifest': author_records + [author_manifest_record],
    'all_declared_author_fingerprint_occurrences_verified': len(fingerprint_occurrences),
    'all_declared_author_fingerprints_unique_records': sorted(author_unique.values(), key=lambda row: row['path']),
    'accepted_context': accepted_context,
    'protocol_official_cache_context': protocol_context,
    'primary_reads_and_limits': source_reads,
    'new_native_binary_hash_for_live_web_PDFs_claimed': False,
    'reviewer_OLD_R4_authorship_and_F5_complexity_R3_review_roles_disclosed': True,
    'NEW_R6_constructor_or_contributor': False,
    'new_R6_peer_or_root_report_findings_read_before_freeze': False,
    'mathematical_program_CAS_scan_table_certificate_or_author_rerun': False,
    'earlier_unique_records_preserved': sorted(preserved, key=lambda row: row['path']),
    'earlier_unique_record_count': len(preserved)})

suffixes = ['-initial-v1.md', '-issues-v1.md', '-source-checks-v1.md', '-freeze-v1.py', '-input-validation-v1.json']
artifacts = [rec(BASE / (PRE + suffix)) for suffix in suffixes]
manifest = {
    'frozen_at_utc': NOW,
    'status': 'complete initially blind WHOLE R6 R2; all40 obligations pass in exact finite-prime finite-shadow strategy-obstruction scopes; coordinator reconciliation pending',
    'reviewer': '/root/review_2017_coarsening_r1',
    'new_R6_constructor_or_contributor': False,
    'older_R4_authorship_and_F5_complexity_R3_review_roles_disclosed': True,
    'requested_settings': {'model': 'gpt-6.1-sol', 'reasoning': 'max'},
    'verified_effective_settings': None,
    'target': target,
    'target_manifest': author_manifest_record,
    'whole_author_obligations': 40,
    'independent_inference_rows': 40,
    'open_substantive_issues': 0,
    'required_author_repairs': 0,
    'optional_wording_only_note': 'N1 finite-S witness may depend on S; no fixed noninteger witness is integral at all primes; no inference affected',
    'complete_actual_cycle_prime_cancellations_every_phase_and_rational_function_stability_reconstructed': True,
    'ordinary_integrality_both2_5_actual_branches_and_contest_intermediates_reconstructed': True,
    'arbitrary_J_fixed_cycle_before_depth_exact_endpoint_feature_and_positive_log_quantifiers_checked': True,
    'ordinary_infinite_lift_termination_annual_or_novelty_claim': False,
    'new_R6_peer_or_root_findings_read_before_initial_freeze': False,
    'mathematical_program_CAS_scan_table_certificate_or_author_rerun': False,
    'declared_author_fingerprint_occurrences_verified': len(fingerprint_occurrences),
    'declared_author_unique_paths_verified': len(author_unique),
    'earlier_frozen_and_context_records_verified_unchanged': len(preserved),
    'last_direct_weekly_telemetry': {'at_utc': '2026-10-17 15:17:06 UTC', 'total_used_percent': 47, 'window_minutes': 10080, 'reset_unix': 1792745187, 'total_ceiling_percent': 90, 'review_integration_reserve': True},
    'administrative_command': '/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 problems/2022-B4/reviews/reasoning-return-r6-review-2-freeze-v1.py',
    'artifacts': artifacts}
put(OUT, manifest)
print(json.dumps({'manifest': rec(OUT), 'report': artifacts[0], 'artifacts': len(artifacts), 'obligations': 40, 'inference_rows': 40, 'author_occurrences_verified': len(fingerprint_occurrences), 'author_unique_paths_verified': len(author_unique), 'prior_records_preserved': len(preserved), 'status': manifest['status']}, indent=2))
