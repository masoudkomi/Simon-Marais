"""Exclusive administrative freeze; no mathematical computation or Git operations."""
from pathlib import Path
import hashlib,json,datetime
root=Path(__file__).resolve().parents[3]
base=root/'problems/2024-B4'
prefix='coordinator-generalized-Kasami-r1-'
def rec(rel):
 b=(root/rel).read_bytes();return {'path':rel,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def nested(x):
 if isinstance(x,dict):
  if isinstance(x.get('path'),str) and isinstance(x.get('sha256'),str) and isinstance(x.get('bytes'),int):yield x
  for v in x.values():yield from nested(v)
 elif isinstance(x,list):
  for v in x:yield from nested(v)
def dump(p,x):
 with p.open('x') as f:json.dump(x,f,indent=2);f.write('\n')
inputs=[
 'AGENTS.md','problems/2024-B4/statement.md',
 'problems/2024-B4/proofs/reviewed-composition-Kasami-v1.1.md',
 'problems/2024-B4/reviews/composition-Kasami-acceptance.md',
 'problems/2024-B4/reviews/composition-Kasami-acceptance.json',
 'problems/2024-B4/notes/zero-automaton-criterion-reviewed-v1.1.md',
 'problems/2024-B4/reviews/criterion-acceptance.md',
 'problems/2024-B4/reviews/criterion-acceptance.json',
 'problems/2024-B4/notes/coordinator-MCM-literature-bridge-v1.md',
 'problems/2024-B4/reviews/reasoning-return-r3-review-1-manifest-v1.json',
 'problems/2024-B4/reviews/reasoning-return-r3-review-1-input-checks-v1.json']
checks=[]
for rel in inputs:
 a=rec(rel);checks.append({**a,'verification_origin':'direct input','verified':True})
 if rel.endswith('.json'):
  for x in nested(json.loads((root/rel).read_text())):
   a=rec(x['path']);assert all(a[k]==x[k] for k in ['path','bytes','sha256']),(rel,x,a)
   checks.append({**x,'verification_origin':rel,'verified':True})
cp=rec('problems/2024-B4/proofs/reviewed-composition-Kasami-v1.1.md')
assert cp['sha256']=='f1e82d443b5ac997889c7a7f7f340437f8401516cccf9516eac132558df220c5'
old=rec('problems/2024-B4/notes/zero-automaton-criterion-reviewed-v1.1.md')
assert old['sha256']=='362f2541b2bb1ab1e22ba768b41d55e7282f08631b0ad39522682244d213f226'
cache=rec('.cache/literature/2024/root-MCM/zieve-biv.pdf')
assert cache['sha256']=='c46313e0c187246b720d8424c3004c42902b2ff11747285da0f698b25dad0e47'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
validation=base/'notes'/f'{prefix}input-validation-v1.json'
dump(validation,{'verified_at_utc':now,'all_verified':True,'record_occurrences':len(checks),'unique_paths':len({x['path'] for x in checks}),'records':checks,'motivation_cache_only_not_new_theorem_premise':cache,'metadata_not_mathematical_evidence':True})
files=[f'problems/2024-B4/notes/{prefix}{suffix}' for suffix in ['candidate-v1.md','sources-v1.md','worklog-v1.md','obligations-v1.json','freeze-v1.py','input-validation-v1.json']]
manifest={'frozen_at_utc':now,'status':'candidate proof - unverified; COMPLETE GK1-GK3 packet','constructor':'coordinator root','claims':['GK1 all-q all-index polynomial recurrence','GK2 genuine infinite whole-divisor families for each q>=4','GK3 all-index absence of whole phi13 when k>=3'],'required_fresh_initially_blind_whole_nonconstructor_audits':2,'root_inspection_counts_as_independent_audit':False,'mathematical_computation_CAS_or_finite_extrapolation':False,'no_new_external_factor_monodromy_or_APN_theorem':True,'full_classification_or_novelty_claim':False,'exact_CP1_and_phi13_dependency_scopes_retained':True,'input_occurrences_verified':len(checks),'input_paths_verified':len({x['path'] for x in checks}),'records':[rec(rel) for rel in files]}
dest=base/'notes'/f'{prefix}manifest-v1.json';dump(dest,manifest)
print(json.dumps({'manifest':rec(str(dest.relative_to(root))),'candidate':rec(files[0]),'input_occurrences':len(checks),'input_paths':len({x['path'] for x in checks})},indent=2))
