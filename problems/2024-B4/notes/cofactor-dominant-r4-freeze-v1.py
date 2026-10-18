#!/usr/bin/env python3
"""Preservation/label checks only. No mathematical computation or peer access."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,re
ROOT=Path.cwd().resolve();P='problems/2024-B4/notes/cofactor-dominant-r4-'
NOW=datetime.now(timezone.utc).isoformat()
ALLOW=('problems/2024-B4/notes/cofactor-dominant-r4-',
       'problems/2024-B4/notes/cofactor-cubic-r3-',
       'problems/2024-B4/notes/cofactor-global-r2-',
       'problems/2024-B4/proofs/reviewed-cofactor-global-r2-',
       'problems/2024-B4/reviews/cofactor-global-r2-acceptance')
def rec(path):
    assert path.startswith(ALLOW) or path in ['AGENTS.md','problems/2024-B4/statement.md']
    b=(ROOT/path).read_bytes()
    return dict(path=path,bytes=len(b),sha256=sha256(b).hexdigest())
def read(path):return json.loads((ROOT/path).read_text())
def check(row):
    assert rec(row['path'])=={k:row[k] for k in ('path','bytes','sha256')}
def out(suffix,obj):
    with (ROOT/(P+suffix)).open('x') as f:json.dump(obj,f,indent=2);f.write('\n')
ap='problems/2024-B4/reviews/cofactor-global-r2-acceptance.json';a=read(ap)
assert a['proposed_claims_accepted']==['CG1','CG2','CG3']
assert a['unresolved_substantive_issues']==0 and a['repair_required'] is False
proof=a['accepted_copy'];oldcandidate=a['candidate'];check(proof);check(oldcandidate)
assert proof['sha256']=='fd110d1615e730d754063b157cc1906b418702f510b2640bfd1b5c63e898548d'
assert (ROOT/proof['path']).read_bytes().endswith((ROOT/oldcandidate['path']).read_bytes())
parent=dict(path='problems/2024-B4/notes/cofactor-cubic-r3-freeze-v1.json',
    bytes=2786,sha256='fcb6f42f7aa824110a5bb60178b2f9db9dc80e37a5827dbc03895484957be263')
check(parent)
for row in read(parent['path'])['artifacts']:check(row)
paths=['AGENTS.md','problems/2024-B4/statement.md',ap,ap[:-5]+'.md',
    'problems/2024-B4/reviews/cofactor-global-r2-acceptance-integrity.json',
    proof['path'],oldcandidate['path'],
    'problems/2024-B4/notes/cofactor-global-r2-freeze-v1.json',
    'problems/2024-B4/notes/cofactor-global-r2-source-audit-v1.md',parent['path'],
    P+'research-v0.md',P+'Frobenius-source-v0.md']
guards=[rec(path) for path in paths]
assert len(guards)==len({r['path'] for r in guards})==12
labels=re.findall(r'^\| DC-(\d{2}) \|',(ROOT/(P+'obligations-v1.md')).read_text(),re.M)
assert labels==[f'{i:02}' for i in range(1,49)]
out('baseline-v1.json',dict(captured_at_utc=NOW,administrative_only=True,
    protected=guards,protected_paths=12,exact_accepted_authority=rec(ap),
    exact_operative_accepted_body=proof,operative_accepted_claims=['CG1','CG2'],
    accepted_candidate_suffix_verified=True,
    historical_CG_141_occurrences_50_paths_bound_not_replayed=True,
    own_parent=parent,own_parent_nine_payloads_verified=True,
    parent_cubic_is_NOT_accepted_or_a_mathematical_premise=True,
    any_NEW_corresponding_cubic_peer_findings_file_hash_or_metadata_opened=False,
    no_OTHER_agent_NEW_mathematical_contribution=True))
out('metadata-v1.json',dict(recorded_at_utc=NOW,
    status='candidate proof - unverified; ENTIRE R4A-R4E constructor checkpoint',
    constructor='/root',constructor_excluded=True,whole_obligations=48,
    all48_constructor_hand_dispositions_complete=True,
    TWO_OTHER_initially_blind_ENTIRE_WHOLE_reviews_and_full_reconciliation_required=True,
    proposed_scope=['every smaller factor e<A','unique F2/S4 invariant large component',
      'all k>=2 bounded cofactor','actual invariant cofactor 4 divides D',
      'exact pA/16+ell-1+4/p threshold','Q16 all k>=2 absolute irreducibility'],
    p_is_ordinary_ell_minus_1_NOT_a_prime_or_characteristic=True,
    mathematical_program_CAS_scan_optimizer_or_source_rerun=False,
    requested_settings=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),
    effective_settings_readback=None,novelty_established=False,full_annual_answer=False,
    latest_worker_weekly_TOTAL_percent=22,latest_worker_meter_utc='2026-10-18 09:40:27 UTC',
    weekly_reset=1792874445,ceiling_TOTAL_percent=90,reserve_required=True,
    automatic_later_window=False))
out('input-validation-v1.json',dict(validated_at_utc=NOW,
    administrative_only_not_mathematical_proof=True,
    all12_protected_records_unchanged=True,exact_accepted_CG_body_suffix_verified=True,
    own_parent_and_nine_payloads_verified=True,all48_labels_exact=True,
    any_corresponding_NEW_peer_review_access=False,errors=[]))
suffixes=['research-v0.md','Frobenius-source-v0.md','candidate-v1.md',
    'obligations-v1.md','sources-v1.md','failures-worklog-v1.md','freeze-v1.py',
    'baseline-v1.json','metadata-v1.json','input-validation-v1.json']
out('freeze-v1.json',dict(frozen_at_utc=NOW,
    status='candidate proof - unverified; ENTIRE dominant/symmetry R4A-R4E',
    constructor='/root',constructor_excluded=True,whole_obligations=48,
    all48_constructor_hand_dispositions_complete=True,
    TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits_and_full_reconciliation_required=True,
    root_supplied_all_NEW_inferences=True,other_agent_NEW_contribution=False,
    exact_accepted_CG_authority=rec(ap),operative_accepted_claims=['CG1','CG2'],
    own_parent=parent,own_parent_not_a_mathematical_premise=True,
    mathematical_computation=False,
    no_general_s5plus_k2_full_annual_or_novelty_conclusion=True,
    artifacts=[rec(P+s) for s in suffixes]))
for row in read(P+'freeze-v1.json')['artifacts']:check(row)
for row in guards:check(row)
print(json.dumps(dict(freeze=rec(P+'freeze-v1.json'),main=rec(P+'candidate-v1.md'),
    whole_obligations=48,new_constructor_paths=11,no_math_program=True),indent=2))
