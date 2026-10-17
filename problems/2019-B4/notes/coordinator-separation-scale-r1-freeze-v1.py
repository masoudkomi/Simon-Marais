"""Documentary freeze only; never reruns mathematical code."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re
r=Path(__file__).resolve().parents[3]
p='problems/2019-B4/notes/coordinator-separation-scale-r1-'
def rec(x):
 actual=x if(r/x).exists()else 'problems/2019-B4/'+x
 b=(r/actual).read_bytes();return dict(path=actual,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def save(s,x):
 with(r/(p+s)).open('x')as f:json.dump(x,f,indent=2);f.write('\n')
 return rec(p+s)
def rows(x):
 if isinstance(x,dict):
  if isinstance(x.get('path'),str)and re.fullmatch('[0-9a-f]{64}',str(x.get('sha256',''))):yield x
  for k,v in x.items():
   if '/'in k and isinstance(v,str)and re.fullmatch('[0-9a-f]{64}',v):yield dict(path=k,sha256=v)
   yield from rows(v)
 elif isinstance(x,list):
  for v in x:yield from rows(v)
authority=['problems/2019-B4/reviews/'+s+'-acceptance.json'for s in ['secondpass','thirdpass','moment-tail']]
cache={};bindings=[]
for x in authority:
 count=0
 for y in rows(json.loads((r/x).read_text())):
  if y['path']not in cache:cache[y['path']]=rec(y['path'])
  assert cache[y['path']]['sha256']==y['sha256'],(x,y)
  if 'bytes'in y:assert cache[y['path']]['bytes']==y['bytes'],(x,y)
  count+=1
 bindings.append(dict(metadata=rec(x),declared_occurrences_verified=count))
deps=['problems/2019-B4/notes/'+s for s in ['secondpass-canonical-renewal.md','secondpass-rigidity-obstructions.md','secondpass-staircases-and-pumping.md','thirdpass-bounded-separation-v1.md','coordinator-moment-regular-tail-candidate-v1.md']]
deps+=['problems/2019-B4/proofs/reviewed-moment-tail-v1.1.md']
deps+=['problems/2019-B4/reviews/'+s+'-acceptance.md'for s in ['secondpass','thirdpass','moment-tail']]
assert (r/deps[5]).read_bytes().endswith((r/deps[4]).read_bytes())
now=datetime.now(timezone.utc).isoformat()
source=save('sources-v1.json',dict(recorded_at_utc=now,accepted_mathematical_inputs=[rec(x)for x in deps],immutable_authority_bindings=bindings,new_external_mathematical_theorem_imported=False,primary_discovery=dict(url='https://lipn.univ-paris13.fr/~banderier/Papers/Dyck/',actual_read='entire20-line unfinished outline, no counting theorem',theorem_imported=False),root_old_moment_constructor_roles_disclosed=True,all_third_party_papers_local_ignored=True,novelty_established=False))
job=json.loads((r/(p+'sign-job-v1.json')).read_text())
assert job['child_pid']==31896 and job['reaped'] and job['exit_code']==0 and not job['timed_out']
sign=json.loads((r/(p+'sign-v1.json')).read_text())
assert sign['new_sign']==-1 and sign['old_sign']==1
validation=save('input-validation-v1.json',dict(checked_at_utc=now,administrative_only=True,all_declared_records_verified=True,record_occurrences=sum(x['declared_occurrences_verified']for x in bindings),unique_paths=len(cache),historical_inventory_not_copied=True,reproduction='Recursive path/sha256 and legacy path->sha256 declarations in exact immutable authority JSON; resolve existing repository-relative first, otherwise exact2019 problem-relative; every available bytes value also checked.',authority_bindings=bindings,exact_direct_dependencies_in=source,accepted_moment_suffix_unchanged=True,mathematical_sign_not_rerun_in_freeze=True,first_admin_attempt_failed_before_outputs=True,original_metadata_checker_preserved=True,one_child_job=rec(p+'sign-job-v1.json'),two_OTHER_whole_initially_blind_nonconstructor_audits_still_required=True))
names=['candidate-v1.md','obligations-v1.md','source-worklog-v1.md','sign-v1.py','sign-v1.json','sign-start-v1.json','sign-job-v1.json','sign-stdout-v1.txt','sign-stderr-v1.txt','freeze-v1.py','freeze-before-path-repair-v0.py','admin-failure-v1.md','sources-v1.json','input-validation-v1.json']
manifest=save('freeze-v1.json',dict(frozen_at_utc=now,status='COMPLETE candidate proof - unverified',constructor='coordinator root',whole_obligations=13,claims=['SS1 first capped count discrepancy in[2D+2,2D+8/10]','SS2 exact actual union of both known infinite tails','SS3 candidate strict lower lambda>1.765224'],root_excluded_from_both_auditor_counts=True,old_known_family_not_claimed_new=True,no_exact_lambda_defect_entropy_lower_gap_original_output_ratio_annual_or_priority_claim=True,requested_settings=dict(model='gpt-6.1-sol',reasoning='max'),independently_verified_effective_settings=None,account_weekly_total_used_percent_last_observed=55,total_ceiling_percent=90,one_finite_fixed_rational_sign_child_pid=31896,no_history_factor_count_or_automaton_enumeration=True,artifacts=[rec(p+x)for x in names]))
print(json.dumps(dict(main=rec(p+'candidate-v1.md'),manifest=manifest,artifacts=len(names),record_occurrences=sum(x['declared_occurrences_verified']for x in bindings),unique_paths=len(cache)),indent=2))
