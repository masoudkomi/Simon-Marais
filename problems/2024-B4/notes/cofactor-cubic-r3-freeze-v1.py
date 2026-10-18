#!/usr/bin/env python3
"""Constructor record integrity only; no mathematical computation."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,re
ROOT=Path.cwd().resolve();P='problems/2024-B4/notes/cofactor-cubic-r3-'
NOW=datetime.now(timezone.utc).isoformat()
def rec(path):
    assert path.startswith(('problems/2024-B4/notes/cofactor-cubic-r3-',
        'problems/2024-B4/notes/cofactor-global-r2-',
        'problems/2024-B4/proofs/reviewed-cofactor-global-r2-',
        'problems/2024-B4/reviews/cofactor-global-r2-acceptance',
        'problems/2019-B4/reviews/reasoning-critical-return-r2-review-1-')) or path in ['AGENTS.md','problems/2024-B4/statement.md']
    b=(ROOT/path).read_bytes();return dict(path=path,bytes=len(b),sha256=sha256(b).hexdigest())
def read(path):return json.loads((ROOT/path).read_text())
def check(row):
    a=rec(row['path']);assert a=={k:row[k] for k in ('path','bytes','sha256')};return a
def out(suffix,obj):
    with (ROOT/(P+suffix)).open('x') as f:json.dump(obj,f,indent=2);f.write('\n')
ap='problems/2024-B4/reviews/cofactor-global-r2-acceptance.json';a=read(ap)
assert a['unresolved_substantive_issues']==0 and a['repair_required'] is False
assert a['proposed_claims_accepted']==['CG1','CG2','CG3']
assert a['constructor_excluded'] is True
proof=check(a['accepted_copy']);candidate=check(a['candidate'])
assert proof['sha256']=='fd110d1615e730d754063b157cc1906b418702f510b2640bfd1b5c63e898548d'
assert (ROOT/proof['path']).read_bytes().endswith((ROOT/candidate['path']).read_bytes())
guard_paths=['AGENTS.md','problems/2024-B4/statement.md',ap,ap[:-5]+'.md',
    'problems/2024-B4/reviews/cofactor-global-r2-acceptance-integrity.json',
    proof['path'],candidate['path'],'problems/2024-B4/notes/cofactor-global-r2-freeze-v1.json',
    'problems/2024-B4/notes/cofactor-global-r2-source-audit-v1.md']
parent=check(dict(path='problems/2019-B4/reviews/reasoning-critical-return-r2-review-1-manifest-v1.json',
    bytes=3138,sha256='b65f2f7324c9005cf518cc93936c4fb74bdb359ff253379749f4f15c7eb75587'))
guard_paths.append(parent['path'])
for row in read(parent['path'])['artifacts']:check(row)
guards=[rec(path) for path in guard_paths]
assert len(guards)==len({row['path'] for row in guards})==10
labels=re.findall(r'^\| CC-(\d{2}) \|',(ROOT/(P+'obligations-v1.md')).read_text(),re.M)
assert labels==[f'{i:02}' for i in range(1,21)]
out('baseline-v1.json',dict(captured_at_utc=NOW,administrative_integrity_only=True,
    protected=guards,protected_paths=10,exact_accepted_authority=rec(ap),
    exact_accepted_CG_body=proof,operative_accepted_claims=['CG1','CG2'],
    old_CG3_quartic_threshold_NOT_a_new_premise=True,
    accepted_candidate_suffix_verified=True,
    historical_141_occurrences_50_paths_bound_by_authority_not_replayed=True,
    compact_own_parent=parent,own_parent_nine_payloads_verified=True,
    NO_NEW_cubic_review_or_other_pending_corresponding_peer_access=True))
out('metadata-v1.json',dict(recorded_at_utc=NOW,
    status='candidate proof - unverified; ENTIRE R3A-R3B constructor checkpoint',
    constructor='/root',constructor_excluded=True,
    whole_obligations=20,all20_constructor_hand_dispositions_complete=True,
    TWO_OTHER_initially_blind_ENTIRE_WHOLE_reviews_and_full_reconciliation_required=True,
    new_inference='positive T before division gives e<A and exact cubic upper threshold',
    proposed_uniform_family='EVERY s>=3,k>=3; not general k2 or full annual',
    other_agent_NEW_mathematical_contribution=False,
    mathematical_program_CAS_scan_sample_optimizer_or_author_rerun=False,
    requested_settings=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),
    independently_verified_effective_settings=None,
    novelty_established=False,full_annual_answer=False,
    current_weekly_reset=1792874445,ceiling_TOTAL_percent=90,
    reserve_required=True,automatic_later_window=False))
out('input-validation-v1.json',dict(validated_at_utc=NOW,
    administrative_only_not_proof=True,all10_protected_records_unchanged=True,
    exact_accepted_body_candidate_suffix_verified=True,
    own_parent_manifest_and_nine_payloads_verified=True,
    all20_obligation_and_constructor_disposition_labels_exact=True,errors=[]))
suffixes=['research-v0.md','candidate-v1.md','obligations-v1.md','sources-v1.md',
    'failures-worklog-v1.md','freeze-v1.py','baseline-v1.json','metadata-v1.json','input-validation-v1.json']
out('freeze-v1.json',dict(frozen_at_utc=NOW,
    status='candidate proof - unverified; ENTIRE cubic threshold R3A-R3B',
    constructor='/root',constructor_excluded=True,whole_obligations=20,
    all20_constructor_hand_dispositions_complete=True,
    TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits_and_full_reconciliation_required=True,
    root_supplied_all_NEW_inferences=True,other_agent_contribution=False,
    exact_accepted_CG_authority=rec(ap),operative_claims=['CG1','CG2'],
    compact_own_parent=parent,mathematical_computation=False,
    no_general_k2_full_annual_or_novelty_conclusion=True,
    artifacts=[rec(P+s) for s in suffixes]))
for row in read(P+'freeze-v1.json')['artifacts']:check(row)
for row in guards:check(row)
print(json.dumps(dict(freeze=rec(P+'freeze-v1.json'),main=rec(P+'candidate-v1.md'),
    whole_obligations=20,new_constructor_paths=10,no_math_program=True),indent=2))
