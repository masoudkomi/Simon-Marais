"""Administrative source/preservation freeze only; no mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
BASE = Path('problems/2025-B4/notes')
PRE = 'reasoning-return-r6'
NOW = datetime.now(timezone.utc).isoformat()
OUT = BASE / (PRE + '-freeze-v1.json')
assert not (ROOT / OUT).exists()

def rec(path):
    path = str(path)
    data = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def check(expected):
    actual = rec(expected['path'])
    assert actual == {k: expected[k] for k in ('path', 'bytes', 'sha256')}, (expected, actual)
    return actual

def put(path, value):
    assert not (ROOT / path).exists()
    (ROOT / path).write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')

previous_record = {
    'path': 'problems/2025-B4/reviews/reciprocal-kernel-review-2-manifest-v1.json',
    'bytes': 3081,
    'sha256': '5a4c6aa8cb413df837ccd84532b80a2f9a8bb10f4de4ec0c56fee0a7da48b07c'}
check(previous_record)
previous = json.loads((ROOT / previous_record['path']).read_text())
validation_record = next(x for x in previous['artifacts'] if x['path'].endswith('-input-validation-v1.json'))
check(validation_record)
validation = json.loads((ROOT / validation_record['path']).read_text())
items = validation['earlier_unique_records_preserved'] + previous['artifacts'] + [previous_record]
unique = {}
for row in items:
    row = {k: row[k] for k in ('path', 'bytes', 'sha256')}
    assert row['path'] not in unique or unique[row['path']] == row
    unique[row['path']] = row
preserved = [check(row) for row in unique.values()]
assert len(preserved) == 319

accepted_paths = [
    'problems/2025-B4/proofs/reviewed-partial-v1.1.md',
    'problems/2025-B4/proofs/reviewed-power-gap-return-v1.1.md',
    'problems/2025-B4/proofs/reviewed-diagonal-firstcase-v1.1.md',
    'problems/2025-B4/proofs/reviewed-diagonal-moment-v1.1.md',
    'problems/2025-B4/proofs/reviewed-Fueter-selection-return-v1.1.md',
    'problems/2025-B4/proofs/reviewed-original-weight-selection-v1.1.md',
    'problems/2025-B4/proofs/reviewed-original-weight-universal-v1.1.md',
    'problems/2025-B4/proofs/reviewed-reciprocal-kernel-v1.1.md']
accepted = [rec(path) for path in accepted_paths]
known = {
    'reviewed-diagonal-moment-v1.1.md': '4e25e67e6459134cb5b6c618baef91c37f30bb1dae542d7426fb61450ce4a4f7',
    'reviewed-Fueter-selection-return-v1.1.md': '230dfe9da040e98506bc6fabd5c37c356fb756d5128f990eb9a4fe2ee7e3181a',
    'reviewed-original-weight-selection-v1.1.md': '06071958bafd1fa51d5ceba798b2dab18fb1e441c4a105f093595be78c96110f'}
for row in accepted:
    name = Path(row['path']).name
    if name in known:
        assert row['sha256'] == known[name]
context = [rec(path) for path in [
    'AGENTS.md', 'problems/2025-B4/statement.md', 'problems/2025-B4/proof.md',
    '.cache/official/2025-paper_b.pdf', '.cache/official/2025-solutions.pdf',
    'problems/2025-B4/notes/coordinator-diagonal-appendix-inspection-v1.md',
    'problems/2025-B4/notes/coordinator-diagonal-moment-separation-v1.3.md']]
cached_primary = rec('.cache/literature/deep-literature-r1/2025-bartolome-mihailescu-binary-thue-v2.pdf')
assert cached_primary['bytes'] == 300321
assert cached_primary['sha256'] == '7108b665ebed8b2364c5a6629951d21abd400c96d4e7d5f4f81028f12ed424aa'

source_path = BASE / (PRE + '-sources-v1.json')
sources = {
    'recorded_at_utc': NOW,
    'status': 'candidate-unverified; documentary source scope, not full external theorem certification',
    'official': {
        'paper_url': 'https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2025_paper_b.pdf',
        'open_part': 'B4(b) only, integers x,y,n,q, n,q>=2',
        'actual_arithmetic_sector_here': 'n=p-1,q=p,p>=37 prime,|x|>=2'},
    'primary_sources': [
        {
            'author': 'Preda Mihailescu',
            'title': 'Class Number Conditions for the Diagonal Case of the Equation of Nagell and Ljunggren',
            'doi': '10.1007/978-3-211-74280-8_15',
            'year': 2008,
            'internal_version': '2.0, 2007-09-17',
            'url': 'https://www.researchgate.net/publication/226863681_Class_Number_Conditions_for_the_Diagonal_Case_of_the_Equation_of_Nagell_and_Ljunggren',
            'read': 'Complete relevant Section2.2 and2.3, COMPLETE Section4.3 including both phase systems and singular/second-case branches; prior actual Section4.1-4.2 and signed-normalization reads retained',
            'imported': 'Classical matched-prime Jacobi ideal formula equation11 and Gauss-sum absolute-value identity; ordinary cyclotomic arithmetic context',
            'proved_here_instead': 'Integral module generation, normalization by character counting, positive-ideal integrality, exact e0 pth-power lift and weak full-kernel height construction',
            'not_imported': 'Theorems3/4, full source upper/lower bounds, source basis-cardinality statement, generalized e1 normalization, elementary-target conclusion',
            'binary_retrieved': False,
            'binary_sha256': None,
            'primary_text_overbar_limitation_explicit': True},
        {
            'authors': ['B. Bartolome', 'P. Mihailescu'],
            'title': 'On the equation X^n-1=BZ^n',
            'url': 'https://arxiv.org/pdf/1412.5798v2',
            'internal_version': '1.13, 2021-11-02',
            'read': 'Complete relevant PDFpp5-18 including moments, Lemmas2.4-2.10, application, and COMPLETE Appendices5.1,5.1.1,5.2; actual jet/bouquet sections reread during R6',
            'cached_binary': cached_primary,
            'imported_as_method_attribution': 'Binomial/Vandermonde method and proper-space diagonal/bouquet dimension growth; both rederived for new exact scope',
            'jet_theorem_exact_scope': 'Lemma2.10 states0<N<p-1; new endpoint/all-k recurrence independently proved, not assumed from source',
            'not_imported': 'Binary-Thue theorem, unverified arithmetic parameter conditions, entire singular-case repair, or all-conjugate elementary targets'}],
    'accepted_context_records': accepted,
    'prior_Hasse_read_role': 'RK is now accepted exact separation background; its published cotangent input is not needed as a new premise of recurrence or weak height bound',
    'new_primary_binary_download_or_redistribution': False,
    'mathematical_program_CAS_scan_table_certificate_rerun': False,
    'novelty_or_external_theorem_refutation_claim': False}
put(source_path, sources)

main_path = BASE / (PRE + '-candidate-v1.md')
main = (ROOT / main_path).read_text()
for section in range(9):
    assert '## %d.' % section in main
obligations = (ROOT / BASE / (PRE + '-obligations-v1.md')).read_text()
for index in range(1, 51):
    assert '| R6-%02d |' % index in obligations

input_path = BASE / (PRE + '-input-validation-v1.json')
put(input_path, {
    'validated_at_utc': NOW,
    'administrative_integrity_only': True,
    'context': context,
    'accepted_inputs': accepted,
    'cached_primary': cached_primary,
    'original_author_text_viewer_has_no_claimed_binary_hash': True,
    'earlier_unique_records_preserved': sorted(preserved, key=lambda x: x['path']),
    'earlier_unique_record_count': len(preserved),
    'whole_obligation_count': 50,
    'mathematical_computation': False,
    'read_later_2022_R6_target_or_new_peer_findings_before_constructor_freeze': False,
    'edited_only_new_assigned_prefix': True})

suffixes = [
    '-candidate-v1.md', '-obligations-v1.md', '-source-audit-v1.md',
    '-constructor-check-v1.md', '-worklog-v1.md', '-sources-v1.json',
    '-freeze-v1.py', '-input-validation-v1.json']
artifacts = [rec(BASE / (PRE + suffix)) for suffix in suffixes]
manifest = {
    'frozen_at_utc': NOW,
    'status': 'candidate proof - unverified; complete constructor checkpoint; TWO OTHER initially blind WHOLE audits required',
    'constructor': '/root/review_2017_coarsening_r1',
    'requested_settings': {'model': 'gpt-6.1-sol', 'reasoning': 'max'},
    'verified_effective_settings': None,
    'whole_obligations': 50,
    'claims': ['J1 all-k normalized reciprocal recurrence', 'J2 specially arranged joint p-1 reciprocal jets', 'P1 exact complex/real phase system and formal obstruction', 'A1 attributed-classical-input normalized Jacobi lift for actual e0 solutions', 'H1 actual all-conjugate constant cancellation with one nonzero jet', 'H2 explicit weak signed prime-diagonal height bound, both delta branches'],
    'new_Diophantine_exclusion_full_annual_solution_or_novelty_claim': False,
    'formal_bad_signature_claimed_arithmetically_realized': False,
    'higher_target_rank_or_all_but_one_first_jet_cancellation_claim': False,
    'published_Jacobi_ideal_theorem_fully_reproved': False,
    'earlier_FS_authorship_and_MS_OW_UW_RK_review_roles_disclosed': True,
    'original_methods_and_bouquet_attribution_explicit': True,
    'mathematical_program_CAS_scan_table_certificate_rerun': False,
    'prior_frozen_and_context_records_verified_unchanged': len(preserved),
    'last_direct_weekly_telemetry': {'at_utc': '2026-10-17 15:07:14 UTC', 'total_used_percent': 46, 'window_minutes': 10080, 'reset_unix': 1792745187, 'total_ceiling_percent': 90, 'review_integration_reserve': True},
    'administrative_command': '/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 problems/2025-B4/notes/reasoning-return-r6-freeze-v1.py',
    'artifacts': artifacts}
put(OUT, manifest)
print(json.dumps({'manifest': rec(OUT), 'main': artifacts[0], 'artifacts': len(artifacts), 'obligations': 50, 'prior_records_preserved': len(preserved), 'status': manifest['status']}, indent=2))
