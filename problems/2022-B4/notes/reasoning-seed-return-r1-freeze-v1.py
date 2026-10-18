#!/usr/bin/env python3
"""Exclusive administrative record creation; no mathematical computation."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re

ROOT = Path.cwd().resolve()
P = 'problems/2022-B4/notes/reasoning-seed-return-r1-'
NOW = datetime.now(timezone.utc).isoformat()
assert ROOT.name == 'Website'

def rec(path):
    assert not path.startswith('problems/2024-B4/notes/cofactor-global-r2-')
    assert not path.startswith('problems/2024-B4/reviews/cofactor-global-r2-')
    assert not path.startswith('problems/2022-B4/reviews/reasoning-seed-return-r1-')
    raw = (ROOT / path).read_bytes()
    return dict(path=path, bytes=len(raw), sha256=sha256(raw).hexdigest())

def read(path):
    rec(path)
    return json.loads((ROOT / path).read_text())

def out(suffix, obj):
    path = ROOT / (P + suffix)
    assert str(path).startswith(str(ROOT / P))
    with path.open('x', encoding='utf-8') as handle:
        json.dump(obj, handle, indent=2, ensure_ascii=False)
        handle.write('\n')

unique = {}
occurrences = []
def bind(path, role, expected=None):
    row = rec(path)
    if expected is not None:
        assert row == {key: expected[key] for key in ('path', 'bytes', 'sha256')}, path
    assert path not in unique or unique[path] == row
    unique[path] = row
    occurrences.append(dict(path=path, role=role))
    return row

bind('AGENTS.md', 'actual current project protocol', dict(
    path='AGENTS.md', bytes=4707,
    sha256='28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff'))
bind('problems/2022-B4/statement.md', 'normalized official statement freshly read')

parent_path = 'problems/2025-B4/reviews/reasoning-Runge-return-r2-review-2-manifest-v1.json'
parent = bind(parent_path, 'compact immutable immediate own parent', dict(
    path=parent_path, bytes=3239,
    sha256='b536454f7d71d2b0c3ca3b9a0bc18d24584a4f780581f097823ad0c063ce990e'))
pm = read(parent_path)
assert pm['own_paths_after_this_packet'] == 632
for row in pm['artifacts']:
    if row['path'].endswith(('metadata-v1.json', 'input-validation-v1.json')):
        bind(row['path'], 'necessary immutable own-parent metadata', row)

accepted = []
for stem, scope in [
    ('reasoning-return-r5', 'accepted F5A/B exact canonical-fiber premise'),
    ('reasoning-complexity-return-r9-v3', 'accepted ENTIRE Q1--Q8 v3 seed/rank premise')
]:
    ap = 'problems/2022-B4/reviews/' + stem + '-acceptance.json'
    a = read(ap)
    bind(ap, scope + ' authority JSON')
    bind(ap[:-5] + '.md', scope + ' ENTIRE authority Markdown freshly read')
    assert a['unresolved_substantive_issues'] == 0 and a['repair_required'] is False
    for key in ('candidate', 'accepted_copy'):
        bind(a[key]['path'], scope + ' ' + key, a[key])
    assert (ROOT / a['accepted_copy']['path']).read_bytes().endswith(
        (ROOT / a['candidate']['path']).read_bytes())
    for row in a['verification_metadata']:
        bind(row['path'], 'direct immutable authority metadata; no recursive expansion', row)
    accepted.append(dict(scope=scope, authority=rec(ap), candidate=a['candidate'],
        accepted_copy=a['accepted_copy'],
        historical_occurrences_bound_not_recursively_rehashed=a['record_occurrences_verified'],
        historical_unique_paths_bound_not_recursively_rehashed=a['unique_paths_verified']))

assert accepted[0]['accepted_copy'] == dict(
    path='problems/2022-B4/proofs/reviewed-reasoning-return-r5-v1.1.md',
    bytes=30324, sha256='1a2544cb8ced3bba9cc6efed1870c242c652b3e6029f39881028d4637d7c6da6')
assert accepted[1]['accepted_copy'] == dict(
    path='problems/2022-B4/proofs/reviewed-reasoning-complexity-return-r9-v3.1.md',
    bytes=49080, sha256='18e681d69b29d3495fea0cc2a29dbcb8a9c34db60644b981b3f653d666bef4ad')

contexts = [
    'problems/2022-B4/proofs/reviewed-partials-v1.md',
    'problems/2022-B4/proofs/reviewed-return-r3-v1.1.md',
    'problems/2022-B4/notes/reasoning-return-r8-candidate-v1.md',
    'problems/2022-B4/notes/reasoning-return-r8-source-audit-v1.md',
    'problems/2022-B4/reviews/reasoning-return-r8-acceptance.md',
    'problems/2022-B4/reviews/reasoning-return-r8-acceptance.json'
]
for path in contexts:
    bind(path, 'OLD overlap/failed-route context, not a new ordinary-survivor premise')
r8 = read(contexts[-1])
bind(r8['accepted_copy']['path'], 'OLD fork context accepted-copy identity only', r8['accepted_copy'])

labels = re.findall(r'^\|SR-O(\d{2})\|', (ROOT / (P + 'obligations-v1.md')).read_text(), re.M)
assert labels == [f'{number:02d}' for number in range(1, 49)]
assert 'candidate proof - unverified' in (ROOT / (P + 'candidate-v1.md')).read_text().lower()
assert 'Sdagger' in (ROOT / (P + 'candidate-v1.md')).read_text()
ordered = [unique[path] for path in sorted(unique)]
summary = dict(occurrences=len(occurrences), unique_paths=len(ordered),
    canonical_record_array_sha256=sha256(json.dumps(
        ordered, sort_keys=True, separators=(',', ':')).encode()).hexdigest())

primary = [
    dict(authors='Official Simon Marais 2022 Paper B',
        url='https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2022-paper-b.pdf',
        scope='page2 B4(b) actual positive simultaneous/product domain; no preliminary proof',
        local_new_PDF_sha256=None),
    dict(authors='Akiyama--Frougny--Sakarovitch',
        url='https://perso.telecom-paristech.fr/jsaka/PUB/Files/RBNS-rev.pdf',
        scope='opening definitions; Section5.1, ENTIRE Proposition37/Corollary38 proofs; Lemma29 integer hypotheses, not entire Lemma29/source chain',
        mathematical_import='only separately accepted F5 specialization', local_new_PDF_sha256=None),
    dict(authors='Dubickas--Mossinghoff',
        url='https://www.researchgate.net/publication/220576840_Lower_bounds_for_Z-numbers',
        scope='actual author-uploaded introduction and ENTIRE Lemma3.1/Propositions3.1--3.2 proofs; no tables or algorithms imported',
        mathematical_import='no general termination theorem; singleton argument rederived', local_new_PDF_sha256=None),
    dict(authors='Andrieu--Eliahou--Vivion v2',
        url='https://arxiv.org/html/2510.11723v2',
        scope='definitions and entire operative Section3.3 Proposition3.10/3.13 proofs and conjecture/question contexts',
        mathematical_import='conjecture boundary only, proper-S qualification retained', local_new_PDF_sha256=None),
    dict(authors='Akiyama--Marsault--Sakarovitch',
        url='https://victor.marsault.xyz/resources/articles/RatBaseAutoSim_v10_2018-02-27.pdf',
        scope='span definitions, TheoremII/Proposition57, ENTIRE Section6.2 proof, conclusion Problem71; not entire33pages',
        mathematical_import='failed closure-to-attained-seed inference only', local_new_PDF_sha256=None)
]

out('sources-v1.json', dict(recorded_at_utc=NOW, status='candidate proof - unverified',
    accepted_mathematical_dependencies=accepted, primary_read_contexts=primary,
    overlap_context_paths=contexts, exact_scope_companion=P+'source-audit-v1.md',
    no_new_cached_PDF_download_or_fabricated_source_hash=True,
    no_unread_external_theorem_supplies_ordinary_survivor=True,
    old_input_authorship_not_independent_recertification=True))

out('baseline-v1.json', dict(captured_at_utc=NOW,
    operation='exact bytes/SHA/JSON/label integrity only; NO mathematics',
    compact_immediate_own_parent=parent, prior_own_paths_bound_transitively=632,
    summary=summary, protected_direct_records=ordered, occurrence_roles=occurrences,
    no_recursive_historical_inventory_copy_or_rehash=True,
    current_mutable_shared_status_files_read_or_hashed=False,
    NEW_queued_2024_CG_candidate_and_peer_material_read_or_hashed=False))

out('input-validation-v1.json', dict(validated_at_utc=NOW,
    administrative_only_not_mathematical_validation=True,
    all_direct_accepted_identity_and_authority_metadata_exact=True,
    both_accepted_copies_end_with_exact_declared_candidates=True,
    all48_obligation_labels_present_once_in_order=True,
    compact_own_parent=parent, prior_own_paths_bound=632,
    fingerprint_summary=summary, no_recursive_old_inventory_rehash=True,
    no_NEW_queued_2024_CG_material_opened=True, errors=[]))

suffixes = ['candidate-v1.md', 'obligations-v1.md', 'failed-routes-v1.md',
    'source-audit-v1.md', 'worklog-v1.md', 'freeze-v1.py', 'sources-v1.json',
    'baseline-v1.json', 'input-validation-v1.json']
artifacts = [rec(P + suffix) for suffix in suffixes]
out('freeze-v1.json', dict(frozen_at_utc=NOW, status='candidate proof - unverified',
    constructor='/root/review_2017_coarsening_r1',
    scope='2022 B4(b) only; SR1A/SR1B/SR2/SR3/SR4 exact partial results',
    ENTIRE_main_all48_obligations_failures_sources_worklog_code_ALL_metadata_frozen=True,
    author_self_promotion=False, two_OTHER_ENTIRE_blind_WHOLE_audits_required=True,
    root_broad_target_not_new_proof_contribution=True,
    old_C_R4_R7_R8_authorship_and_F5_Q_reviews_disclosed=True,
    old_B_F5_Q_and_root_F5_roles_disclosed=True,
    requested_settings=dict(model='gpt-6.1-sol', reasoning='max', inherited=True),
    independently_verified_effective_settings=None,
    no_mathematical_code_CAS_scan_sample_or_author_rerun=True,
    no_native_mathematical_child_or_pending_approval=True,
    no_official_infinite_survivor_termination_fullannual_or_novelty_claim=True,
    actual_advance='exact unconditional first central entry for whole unbounded orphan family',
    unresolved='future after central entry; eightfold/tenfold existence; arbitrary born/varying-difference future',
    telemetry=dict(observed_at_utc='2026-10-18 08:17:12 UTC', used_percent_TOTAL=17,
        window_duration_minutes=10080, resets_at=1792874445, ordinary_usage_allowed=True,
        authorized_ceiling_TOTAL_percent=90, reserve_required=True, no_automatic_later_reset=True),
    whole_obligations=48, compact_immediate_own_parent=parent,
    prior_own_paths_bound=632, new_packet_paths_including_freeze=10,
    older_plus_new_own_paths_bound_transitively=642,
    direct_fingerprint_summary=summary, artifacts=artifacts))

print(json.dumps(dict(freeze=rec(P+'freeze-v1.json'), main=rec(P+'candidate-v1.md'),
    artifacts_including_freeze=10, whole_obligations=48, direct_summary=summary,
    no_mathematical_computation=True), indent=2))
