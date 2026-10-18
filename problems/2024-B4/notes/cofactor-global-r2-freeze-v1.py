#!/usr/bin/env python3
"""CG constructor byte preservation only; no mathematical computation."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,sys
ROOT=Path(__file__).resolve().parents[3]
P='problems/2024-B4/notes/cofactor-global-r2-'
OWN='problems/2020-B4/reviews/reasoning-arithmetic-return-r11-review-1-manifest-v1.json'
PROTECTED=['AGENTS.md','problems/2024-B4/statement.md',OWN,
 'problems/2024-B4/proofs/reviewed-structural-v1.1.md',
 'problems/2024-B4/reviews/structural-acceptance.md',
 'problems/2024-B4/reviews/structural-acceptance.json',
 'problems/2024-B4/proofs/reviewed-coordinator-F8-pencil-r1-v1.1.md',
 'problems/2024-B4/reviews/coordinator-F8-pencil-r1-acceptance.md',
 'problems/2024-B4/reviews/coordinator-F8-pencil-r1-acceptance.json',
 'problems/2024-B4/proofs/reviewed-cofactor-symmetry-r1-v1.1.md',
 'problems/2024-B4/reviews/cofactor-symmetry-r1-acceptance.md',
 'problems/2024-B4/reviews/cofactor-symmetry-r1-acceptance.json',
 'problems/2024-B4/notes/cofactor-symmetry-r1-source-audit-v1.md',
 'problems/2024-B4/notes/cofactor-global-r2-research-v0.md',
 'problems/2024-B4/notes/cofactor-global-r2-Frobenius-lead-v0.md',
 'problems/2024-B4/notes/cofactor-symmetry-literature-followup-v1.md']
def now():return datetime.now(timezone.utc).isoformat()
def rec(p):
 b=(ROOT/p).read_bytes()
 return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def read(p):return json.loads((ROOT/p).read_text())
def out(s,value):
 with(ROOT/(P+s)).open('x')as f:json.dump(value,f,indent=2);f.write('\n')
def check(rows):
 for r in rows:assert rec(r['path'])==r,r['path']
def baseline():
 authorities=[]
 for stem,key in [('structural','accepted_proof'),('coordinator-F8-pencil-r1','accepted_copy'),('cofactor-symmetry-r1','accepted_copy')]:
  a=f'problems/2024-B4/reviews/{stem}-acceptance.json'
  value=read(a)
  assert rec(value[key]['path'])==value[key]
  authorities.append(dict(authority=rec(a),accepted_body=value[key],
                          prior_inventories_bound_not_expanded=True))
 out('baseline-v1.json',dict(recorded_utc=now(),
   actual_baseline_after_hand_draft_before_complete_freeze=True,
   protected=[rec(p)for p in PROTECTED],compact_immediate_own_parent=rec(OWN),
   accepted_authorities=authorities,earlier_live_notes_not_mathematical_authorities=True,
   no_recursive_historical_inventory_replay=True))
 print(json.dumps(dict(baseline=rec(P+'baseline-v1.json'),protected_paths=len(PROTECTED))))
def freeze():
 b=read(P+'baseline-v1.json');check(b['protected'])
 labels=re.findall(r'^\| (CG-\d\d) \|',(ROOT/(P+'obligations-v1.md')).read_text(),re.M)
 assert labels==[f'CG-{i:02d}'for i in range(1,57)]
 out('metadata-v1.json',dict(status='candidate proof - unverified',constructor='/root',
   NEW_claims=['CG1 actual general geometry','CG2 arbitrary-factor inequalities','CG3 whole absolute irreducibility at explicit threshold'],
   root_excluded_from_TWO_OTHER_independent_whole_audits=True,
   other_NEW_contributors=[],whole_obligations_and_author_checks=56,
   requested_settings=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),
   verified_effective_settings=None,
   exact_domain='Q=2^s,s>=3;ell=Q-1;q=Q^k,k>=1;n=ell*q+1',
   irreducibility_hypothesis='q>=max(2ell+7,(ell-1)(ell-2)(ell+1)^2/4)',
   proposed_family='every s>=3,k>=4,n=(2^s-1)*2^(sk)+1',
   all_projective_singularities_and_both_global_square_completions_reconstructed=True,
   reduced_c_minus_1_correction_retained=True,no_factor_F2_definition_or_orbit_uniformity_needed=True,
   Frobenius_Gauss_map_theorem_import=False,
   general_annual_classification_novelty_external_validation=False,
   mathematical_code_CAS_scan_factor_table_author_or_certificate_replay=False,
   source_PDF_binary_hashes=None,compact_immediate_own_parent=rec(OWN),
   latest_root_direct_meter=dict(utc='2026-10-18 08:06:51 UTC',percent_TOTAL=16,reset=1792874445),
   later_worker_direct_meter=dict(utc='2026-10-18 08:17:12 UTC',percent_TOTAL=17,reset=1792874445),
   authorized_current_window_only_ceiling_TOTAL=90,integration_reserve=True,
   automatic_later_window=False,no_charge_contact_access_bypass=True))
 out('input-validation-v1.json',dict(verified_utc=now(),
   protected_paths_verified=len(PROTECTED),old_bytes_unchanged=True,
   all56_labels_once_in_order=True,metadata_only_not_mathematical_validation=True))
 suffixes=['candidate-v1.md','obligations-v1.md','source-audit-v1.md','failures-worklog-v1.md',
           'freeze-v1.py','baseline-v1.json','metadata-v1.json','input-validation-v1.json']
 out('freeze-v1.json',dict(frozen_at_utc=now(),status='ENTIRE CG1–CG3 constructor checkpoint; candidate-unverified',
   constructor='/root',root_excluded=True,TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits_REQUIRED=True,
   all56_obligations_and_constructor_checks_complete=True,
   full_main_sources_failures_log_code_ALL_metadata_frozen=True,
   compact_immediate_own_parent=rec(OWN),protected_paths=len(PROTECTED),
   artifacts=[rec(P+s)for s in suffixes],no_mathematical_executable=True,
   mathematical_annual_answer_or_novelty_promotion=False))
 verify()
def verify():
 check(read(P+'baseline-v1.json')['protected'])
 check(read(P+'freeze-v1.json')['artifacts'])
 print(json.dumps(dict(postverified=True,manifest=rec(P+'freeze-v1.json'),
   candidate=rec(P+'candidate-v1.md'),all_obligations=56,status='candidate-unverified')))
if __name__=='__main__':{'baseline':baseline,'freeze':freeze,'verify':verify}[sys.argv[1]]()
