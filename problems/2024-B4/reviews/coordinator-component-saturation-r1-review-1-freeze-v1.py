"""Independent administrative review freeze; no mathematical computation.

Reads declared SHA/byte metadata, not peer findings. Never invokes the
constructor's freezer or any source mathematical certificate. Compact
parent bindings retain reproducibility without recopying old inventories.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = 'problems/2024-B4/reviews/coordinator-component-saturation-r1-review-1-'
AUTHOR = 'problems/2024-B4/notes/coordinator-component-saturation-r1-'
PRIOR = 'problems/2017-B4/notes/reasoning-value-return-r4-'

def fingerprint(path):
    data = (ROOT / path).read_bytes()
    return dict(path=path, bytes=len(data), sha256=hashlib.sha256(data).hexdigest())

def records(value):
    if isinstance(value, dict):
        if isinstance(value.get('path'), str) and re.fullmatch('[0-9a-f]{64}', str(value.get('sha256', ''))):
            yield value
        for key, child in value.items():
            if '/' in key and isinstance(child, str) and re.fullmatch('[0-9a-f]{64}', child):
                yield dict(path=key, sha256=child)
            yield from records(child)
    elif isinstance(value, list):
        for child in value:
            yield from records(child)

def new_json(suffix, value):
    with (ROOT / (PREFIX + suffix)).open('x') as handle:
        json.dump(value, handle, indent=2)
        handle.write('\n')

generated = ['input-validation-v1.json', 'sources-v1.json', 'freeze-output-v1.json', 'manifest-v1.json']
assert all(not (ROOT / (PREFIX + suffix)).exists() for suffix in generated)
assert fingerprint(AUTHOR + 'candidate-v1.md') == dict(
    path=AUTHOR + 'candidate-v1.md', bytes=13194,
    sha256='61f8c60491880e941149649c2c4180abef91671496d56c5869f8543a915aba46')
assert fingerprint(AUTHOR + 'freeze-v1.json') == dict(
    path=AUTHOR + 'freeze-v1.json', bytes=3452,
    sha256='13dff01ab6757aa2214d4be9667c96f8381446f7b41c0b06b3458babfe80f0fb')
assert fingerprint(PRIOR + 'freeze-v1.json') == dict(
    path=PRIOR + 'freeze-v1.json', bytes=3773,
    sha256='99df2683197f1a6e6e0f5c5696859c8c57b8a601bff3bf07d1bd6bd1fa831dca')

author_inputs = json.loads((ROOT / (AUTHOR + 'input-validation-v1.json')).read_text())
metadata = [AUTHOR + 'freeze-v1.json', AUTHOR + 'sources-v1.json', AUTHOR + 'input-validation-v1.json']
metadata += [row['metadata']['path'] for row in author_inputs['immutable_metadata']]
metadata += [PRIOR + 'freeze-v1.json', PRIOR + 'input-validation-v1.json']
assert len(metadata) == len(set(metadata))

cache = {}
summaries = []
for path in metadata:
    count = 0
    for expected in records(json.loads((ROOT / path).read_text())):
        name = expected['path']
        assert not name.startswith('problems/2024-B4/reviews/coordinator-component-saturation-r1-'), name
        assert not name.startswith('problems/2019-B4/notes/coordinator-separation-scale-r1-'), name
        assert not name.startswith('problems/2019-B4/reviews/coordinator-separation-scale-r1-'), name
        if name not in cache:
            cache[name] = fingerprint(name)
        actual = cache[name]
        assert actual['sha256'] == expected['sha256'], (path, name)
        if 'bytes' in expected:
            assert actual['bytes'] == expected['bytes'], (path, name)
        count += 1
    summaries.append(dict(metadata=fingerprint(path), declared_record_occurrences_verified=count))

obligation_text = (ROOT / (AUTHOR + 'obligations-v1.md')).read_text()
author_ids = re.findall(r'^\|CS-(\d\d)\|', obligation_text, re.M)
assert author_ids == [f'{i:02}' for i in range(1, 31)]
ledger = (ROOT / (PREFIX + 'issues-v1.md')).read_text()
review_ids = re.findall(r'^\|R1-(\d\d)\|', ledger, re.M)
assert review_ids == [f'{i:02}' for i in range(1, 41)]
assert set(re.findall(r'CS-(\d\d)', ledger)) == set(author_ids)

now = datetime.now(timezone.utc).isoformat()
canonical = json.dumps([cache[path] for path in sorted(cache)], sort_keys=True, separators=(',', ':')).encode()
summary = dict(
    verified_at_utc=now, administrative_only=True, all_verified=True,
    record_occurrences=sum(row['declared_record_occurrences_verified'] for row in summaries),
    unique_paths=len(cache),
    deduplicated_path_bytes_sha256_digest=hashlib.sha256(canonical).hexdigest(),
    immutable_metadata=summaries,
    direct_assigned_inputs=[fingerprint(AUTHOR + 'candidate-v1.md'), fingerprint(AUTHOR + 'freeze-v1.json')],
    prior_own_complete_checkpoint=fingerprint(PRIOR + 'freeze-v1.json'),
    author_obligations=author_ids, reviewer_checks=review_ids,
    compact_binding_instead_of_copying_historical_inventory=True,
    exact_declared_records_reproducible_in_bound_parent_metadata=True,
    no_new_peer_CS_findings_or_queued_2019_packet_opened_before_complete_freeze=True,
    no_old_bytes_changed=True, mathematical_code_CAS_scan_or_author_rerun=False)
new_json('input-validation-v1.json', summary)

new_json('sources-v1.json', dict(
    recorded_at_utc=now,
    detailed_source_record=fingerprint(PREFIX + 'source-checks-v1.md'),
    actual_primary_reads=[
        dict(name='Official2024 Paper B', url='https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf',
             read='Page2 B4(b) and exact congruence/constant definitions', role='Actual open target only'),
        dict(name='Bensimhoun2004 authored Lueroth proof', url='https://upload.wikimedia.org/wikipedia/commons/3/3e/Another_elementary_proof_of_Luroth%27s_theorem-06.2004.pdf',
             read='COMPLETE theorem and BOTH written proof pages', role='Classical foundational arbitrary-characteristic theorem'),
        dict(name='Mesnager--Qu1907.01066v1', url='https://arxiv.org/pdf/1907.01066v1',
             read='Actual Section5.4 Definition44, parameter paragraph, Proposition45',
             role='Classical trace-form attribution only; NO exceptionality or permutation theorem',
             two_screenshot_cache_miss_failures_disclosed=True, full28page_audit=False),
    ],
    accepted_bodies_read_in_full=[fingerprint(path) for path in [
        'problems/2024-B4/proofs/reviewed-Kasami-whole-criterion-v1.1.md',
        'problems/2024-B4/proofs/reviewed-generalized-Kasami-v1.1.md',
        'problems/2024-B4/proofs/reviewed-reasoning-components-r1-v1.1.md']],
    old_IC_authorship_not_independently_self_recertified=True,
    original_JW1993_full_proof_and_Ferard2014_exact_theorem_unread_unused_by_core_CS=True,
    binary_remote_source_hash_claim=False, new_download_or_source_cache_mutation=False,
    novelty_full_annual_solution_or_general_irreducibility_claim=False))

artifacts = [fingerprint(PREFIX + suffix) for suffix in [
    'initial-v1.md', 'issues-v1.md', 'source-checks-v1.md', 'worklog-v1.md',
    'freeze-v1.py', 'input-validation-v1.json', 'sources-v1.json']]
output = dict(
    frozen_at_utc=now,
    status='COMPLETE initially blind NONCONSTRUCTOR WHOLE R1 audit; recommendation only',
    report=artifacts[0], author_obligations=30, whole_inference_checks=40,
    substantive_open_issues=0, required_author_repair=False,
    record_occurrences=summary['record_occurrences'], unique_paths=summary['unique_paths'],
    no_new_peer_CS_findings_read=True, old_IC_authorship_boundary_disclosed=True)
new_json('freeze-output-v1.json', output)
artifacts.append(fingerprint(PREFIX + 'freeze-output-v1.json'))
new_json('manifest-v1.json', dict(
    frozen_at_utc=now,
    status='COMPLETE initially blind NONCONSTRUCTOR WHOLE R1 review; not coordinator promotion',
    reviewer='/root/review_2021_reasoning_j15_r2', constructor='coordinator root',
    requested_settings=dict(model='gpt-6.1-sol', reasoning='max'), independently_verified_effective_settings=None,
    whole_author_obligations=30, whole_inference_checks=40,
    report_recommendation='No substantive defect found in CS1/CS2 exact scoped partial; second whole audit and root reconciliation still required',
    substantive_open_issues=0, required_author_repair=False,
    old_T1_T4_C7_C11_IC_authorship_and_CP_GK_KC_CJ_DI_NJ_HR_review_roles_disclosed=True,
    no_NEW_CS_construction_contribution=True,
    prior_own_accepted_IC_is_not_independently_self_recertified=True,
    complete_initial_before_any_new_peer_CS_findings=True,
    source_original_proof_and_reading_limits_explicit=True,
    mathematical_code_CAS_scan_author_rerun=False,
    old_shared_Git_or_cache_bytes_changed=False,
    full_annual_answer_novelty_or_promotion_claim=False,
    latest_authoritative_account_weekly=dict(
        at_utc='2026-10-17 18:45:15 UTC', total_used_percent=56,
        window_minutes=10080, reset_unix=1792745187,
        ordinary_usage_allowed=True, total_ceiling_percent=90, review_integration_reserve=True),
    administrative_command='.venv/bin/python ' + PREFIX + 'freeze-v1.py',
    artifacts=artifacts))
print(json.dumps(dict(output=output, manifest=fingerprint(PREFIX + 'manifest-v1.json')), indent=2))
