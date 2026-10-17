"""Administrative WHOLE-review freeze only; no mathematical rerun.

Verify exact inputs and compact immutable parents, compare saved finite
certificate strings, and bind the complete initial report before peers.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = 'problems/2019-B4/reviews/coordinator-separation-scale-r1-review-1-'
AUTHOR = 'problems/2019-B4/notes/coordinator-separation-scale-r1-'
PRIOR = 'problems/2024-B4/reviews/coordinator-component-saturation-r1-review-1-'

def resolve(path):
    candidate = ROOT / path
    if candidate.exists():
        return candidate
    legacy = ROOT / 'problems/2019-B4' / path
    assert legacy.exists(), path
    return legacy

def fingerprint(path):
    actual = resolve(path)
    data = actual.read_bytes()
    try:
        name = actual.relative_to(ROOT).as_posix()
    except ValueError:
        name = actual.as_posix()
    return dict(path=name, bytes=len(data), sha256=hashlib.sha256(data).hexdigest())

def rows(value):
    if isinstance(value, dict):
        if isinstance(value.get('path'), str) and re.fullmatch('[0-9a-f]{64}', str(value.get('sha256', ''))):
            yield value
        for key, child in value.items():
            if isinstance(child, str) and re.fullmatch('[0-9a-f]{64}', child):
                if '/' in key or (ROOT / key).is_file() or (ROOT / 'problems/2019-B4' / key).is_file():
                    yield dict(path=key, sha256=child)
            yield from rows(child)
    elif isinstance(value, list):
        for child in value:
            yield from rows(child)

def new(suffix, value):
    with (ROOT / (PREFIX + suffix)).open('x') as handle:
        json.dump(value, handle, indent=2)
        handle.write('\n')

generated = ['input-validation-v1.json', 'sources-v1.json', 'freeze-output-v1.json', 'manifest-v1.json']
assert all(not (ROOT / (PREFIX + suffix)).exists() for suffix in generated)
assert fingerprint(AUTHOR + 'candidate-v1.md') == dict(
    path=AUTHOR + 'candidate-v1.md', bytes=9068,
    sha256='d08d778d7bfe2e915b67d85833d4dfb312d78393f0e80aeecdc7859abae5070e')
assert fingerprint(AUTHOR + 'freeze-v1.json') == dict(
    path=AUTHOR + 'freeze-v1.json', bytes=3809,
    sha256='33abb0fd6e571f623f31c9d767be471b95cad1990f39d898700f3568acad732c')
assert fingerprint(PRIOR + 'manifest-v1.json') == dict(
    path=PRIOR + 'manifest-v1.json', bytes=3358,
    sha256='ecac39bcef8df420738d992cae75053730f7b12086452b863658fcae469e75ac')

metadata = [
    AUTHOR + 'freeze-v1.json', AUTHOR + 'sources-v1.json', AUTHOR + 'input-validation-v1.json',
    'problems/2019-B4/reviews/acceptance.json',
    'problems/2019-B4/reviews/secondpass-acceptance.json',
    'problems/2019-B4/reviews/thirdpass-acceptance.json',
    'problems/2019-B4/reviews/moment-tail-acceptance.json',
    PRIOR + 'manifest-v1.json', PRIOR + 'input-validation-v1.json',
]
cache = {}
summaries = []
for name in metadata:
    count = 0
    for expected in rows(json.loads(resolve(name).read_text())):
        absolute = resolve(expected['path'])
        assert 'problems/2019-B4/reviews/coordinator-separation-scale-r1-' not in absolute.as_posix(), expected['path']
        path = fingerprint(expected['path'])['path']
        if path not in cache:
            cache[path] = fingerprint(path)
        assert cache[path]['sha256'] == expected['sha256'], (name, path)
        if 'bytes' in expected:
            assert cache[path]['bytes'] == expected['bytes'], (name, path)
        count += 1
    summaries.append(dict(metadata=fingerprint(name), declared_record_occurrences_verified=count))

author = json.loads((ROOT / (AUTHOR + 'sign-v1.json')).read_text())
independent = json.loads((ROOT / (PREFIX + 'integer-output-v1.json')).read_text())
assert independent['E_union'] == author['E_union_r']
assert independent['E_previous_union'] == author['E_previous_union_r']
assert independent['homogeneous_integers']['a_h'] == author['F3_denominator']['numerator']
assert independent['homogeneous_integers']['b_h'] == author['rigid_denominator_base']['numerator']
assert independent['signs'] == dict(new=-1, old=1)
job = json.loads((ROOT / (PREFIX + 'integer-job-v1.json')).read_text())
assert job['child_pid'] == 33186 and job['reaped'] and job['exit_code'] == 0 and not job['timed_out']
assert job['external_timeout_seconds'] == 10
assert fingerprint(PREFIX + 'integer-certificate-v1.py')['sha256'] == job['script_sha256']
assert (ROOT / (PREFIX + 'integer-stderr-v1.txt')).read_bytes() == b''
assert json.loads((ROOT / (PREFIX + 'integer-stdout-v1.txt')).read_text()) == independent

obligations = re.findall(r'^(\d+)\. ', (ROOT / (AUTHOR + 'obligations-v1.md')).read_text(), re.M)
assert obligations == [str(i) for i in range(1, 14)]
checks = re.findall(r'^\|R1-(\d\d)\|', (ROOT / (PREFIX + 'issues-v1.md')).read_text(), re.M)
assert checks == [f'{i:02}' for i in range(1, 31)]
now = datetime.now(timezone.utc).isoformat()
canonical = json.dumps([cache[path] for path in sorted(cache)], sort_keys=True, separators=(',', ':')).encode()
new('input-validation-v1.json', dict(
    checked_at_utc=now, administrative_only=True, all_verified=True,
    record_occurrences=sum(row['declared_record_occurrences_verified'] for row in summaries),
    unique_paths=len(cache), deduplicated_path_bytes_sha256_digest=hashlib.sha256(canonical).hexdigest(),
    immutable_metadata=summaries,
    assigned_main=fingerprint(AUTHOR + 'candidate-v1.md'), assigned_freeze=fingerprint(AUTHOR + 'freeze-v1.json'),
    previous_complete_own_CS_freeze=fingerprint(PRIOR + 'manifest-v1.json'),
    constructor14_artifacts_and_all_declared_dependencies_unchanged=True,
    exact_saved_fraction_string_comparison_only=True,
    independent_one_child_not_rerun_in_freeze=True,
    author_obligations=obligations, whole_review_checks=checks,
    compact_parent_bindings_no_historical_inventory_copy=True,
    no_new_peer_SS_file_or_finding_opened=True, old_shared_Git_or_cache_edit=False))

source_inputs = json.loads((ROOT / (AUTHOR + 'sources-v1.json')).read_text())['accepted_mathematical_inputs']
new('sources-v1.json', dict(
    recorded_at_utc=now, detailed_source_checks=fingerprint(PREFIX + 'source-checks-v1.md'),
    exact_accepted_inputs=source_inputs,
    additional_actual_reads=[fingerprint(path) for path in [
        'AGENTS.md', 'problems/2019-B4/statement.md', 'problems/2019-B4/proof.md',
        'problems/2019-B4/reviews/acceptance.md']],
    primary_reads=[
        dict(url='https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-paper-b_1.pdf',
             actual_read='Page2 B4 definition and part(b)', role='Actual distinct-string open target'),
        dict(url='https://lipn.univ-paris13.fr/~banderier/Papers/Dyck/',
             actual_read='Entire20-line unfinished authored outline', theorem_imported=False),
    ],
    no_new_external_counting_or_language_theorem_imported=True,
    old_2019_research_and_review_roles_disclosed_no_new_SS_contribution=True,
    finite_critical_certificate=dict(
        method='Independent hand-derived cleared degree46/40 homogeneous integer forms; one fixed trial, no author input or Fraction',
        source=fingerprint(PREFIX + 'integer-certificate-v1.py'),
        derivation=fingerprint(PREFIX + 'integer-certificate-v1.md'),
        output=fingerprint(PREFIX + 'integer-output-v1.json'),
        job=fingerprint(PREFIX + 'integer-job-v1.json'),
        child_pid=33186, external_timeout_seconds=10, exit_code=0, reaped=True),
    no_history_factor_count_automaton_enumeration_or_constructor_rerun=True,
    no_native_source_wait_fee_contact_access_bypass_or_cache_edit=True,
    original_published_or_old_finite_certificates_not_claimed_freshly_reconstructed=True,
    exact_lambda_annual_solution_or_novelty_claim=False))

names = [
    'initial-v1.md', 'issues-v1.md', 'source-checks-v1.md', 'worklog-v1.md',
    'integer-certificate-v1.md', 'integer-certificate-v1.py', 'integer-output-v1.json',
    'integer-start-v1.json', 'integer-job-v1.json', 'integer-stdout-v1.txt', 'integer-stderr-v1.txt',
    'freeze-v1.py', 'input-validation-v1.json', 'sources-v1.json',
]
artifacts = [fingerprint(PREFIX + suffix) for suffix in names]
output = dict(
    frozen_at_utc=now,
    status='COMPLETE initially blind NONCONSTRUCTOR WHOLE R1; recommendation only',
    report=artifacts[0], author_obligations=13, whole_inference_checks=30,
    substantive_open_issues=0, required_author_repair=False,
    fingerprint_occurrences=sum(row['declared_record_occurrences_verified'] for row in summaries),
    unique_paths=len(cache), independent_exact_new_old_signs=dict(new=-1,old=1),
    no_new_peer_SS_finding_read=True)
new('freeze-output-v1.json', output)
artifacts.append(fingerprint(PREFIX + 'freeze-output-v1.json'))
new('manifest-v1.json', dict(
    frozen_at_utc=now,
    status='COMPLETE initially blind NONCONSTRUCTOR WHOLE R1 audit; not promotion',
    reviewer='/root/review_2021_reasoning_j15_r2', constructor='coordinator root',
    requested_settings=dict(model='gpt-6.1-sol', reasoning='max'), independently_verified_effective_settings=None,
    all_author_obligations=13, whole_inference_checks=30,
    recommendation='No substantive defect found in exact SS1/SS2/SS3 partial scope; other whole audit and root reconciliation still required',
    substantive_open_issues=0, required_author_repair=False,
    complete_initial_before_any_new_peer_SS_report_ledger_source_manifest_or_finding=True,
    prior_research_review_roles_disclosed_no_new_SS_construction_contribution=True,
    older_known_families_not_rediscovered=True,
    independent_fixed_trial_integer_certificate_child=dict(pid=33186,timeout_seconds=10,exit_code=0,reaped=True),
    mathematical_history_factor_count_or_automaton_scan_or_constructor_rerun=False,
    old_shared_Git_or_cache_bytes_changed=False,
    exact_value_entropy_lower_mass_renewal_defect_annual_or_novelty_claim=False,
    latest_authoritative_account_weekly=dict(
        at_utc='2026-10-17 18:54:22 UTC', total_used_percent=56,
        window_minutes=10080, reset_unix=1792745187, ordinary_usage_allowed=True,
        total_ceiling_percent=90, review_integration_reserve=True),
    administrative_command='.venv/bin/python ' + PREFIX + 'freeze-v1.py',
    artifacts=artifacts))
print(json.dumps(dict(output=output, manifest=fingerprint(PREFIX + 'manifest-v1.json')),indent=2))
