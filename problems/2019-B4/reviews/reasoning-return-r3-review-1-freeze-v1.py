"""Administrative whole-review freeze only; no mathematical computation."""
from pathlib import Path
import hashlib,json,datetime
root=Path(__file__).resolve().parents[3];base=root/'problems/2019-B4';pre='reasoning-return-r3-review-1-'
def rec(rel):
 b=(root/rel).read_bytes();return {'path':rel,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def rows(x):
 if isinstance(x,dict):
  if isinstance(x.get('path'),str) and isinstance(x.get('sha256'),str) and isinstance(x.get('bytes'),int):yield x
  for v in x.values():yield from rows(v)
 elif isinstance(x,list):
  for v in x:yield from rows(v)
def dump(p,x):
 with p.open('x') as f:json.dump(x,f,indent=2);f.write('\n')
remarks=[
'Official strings and chronological contexts remain distinct; exact accepted growth identification retained.',
'Full accepted witnesses/endpoints/anti-factoriality/rigidity/cap definitions and moment scope read.',
'Prefix alpha/beta counts checked at both phases, with exact u+K0+j source budget.',
'RR/LL force nonempty a,b; selected time internal, including K0=0.',
'Explicitly exclude passing entire left block, then d<=K0 and contradictory combined count; unrestricted d.',
'm+1 pair states give positive RL-power loop in an accepting run; fixed prefix/phase gives NR1 contradiction.',
'Unrestricted staircase theorem supplies arbitrarily long RL powers, not merely finite evidence.',
'Exact proper prefix/suffix operation and factoriality cover all shorter factors; both single letters canonical.',
'AppendR equivalence gives odd part by right quotient; fixed block image yields even canonical nonregularity.',
'Synchronous lex test/project/complement yields K if E regular; no asynchronous assertion.',
'RR/LL endpoints force every crossing G occurrence to span the whole forbidden power, including seam edges.',
'Right languages afterW exactly initial; minimal accepting DFA resets, is strongly connected, initialLloop.',
'Letter-multiplicity adjacency and positivePerronvector give explicit constant root bounds.',
'F nonregular forces regularG proper; anti-factoriality makes missingf an actual G-avoiding legal path.',
'Finite higher-edge graph is strongly connected and preserves rate; at least one f-edge deleted.',
'Strict spectral comparison valid with reducibleB; positiveleftA/nonnegativeBvector forces contradiction.',
'At block midpoint d<=D keeps both extra/deficit strings wholly in opposite constant halves, including dD.',
'Unique other staircase history has exact prefix surplus maxn+1; n1/n2 and all central/descending steps checked.',
'Every finitecap strict via explicit missinghD; accepted moment/convergence only, possible consecutiveplateaus.',
'No series nonrationality, originalB nonregularity, arbitrarycrosssection, exactlambda or novelty inferred.'
]
obs=json.loads((base/'notes/reasoning-return-r3-obligations-v1.json').read_text())['obligations'];assert len(obs)==len(remarks)==20
checks=[{'id':f'NR-R1-{i+1:02d}','author_obligation':o['id'],'claim':o['claim'],'status':'reconstructed; no substantive issue','reason':v} for i,(o,v) in enumerate(zip(obs,remarks))]
extras=[('E1','K0=0','Strict internality survives zero source budget; immediate d<=0 contradiction.'),('E2','Raw monitor versus minimal DFA','Reset assertion is only for follower-state minimization; no discarded unmatched branch assumption.'),('E3','PF degeneracies','Initial L-loop gives positive radius; reducible deleted graph and zero entries handled.'),('E4','Unbounded G and representation','RegularG may be infinite; no maximum factor length is used. OriginalB and K have same rate only.')]
checks += [{'id':'NR-R1-'+i,'claim':c,'status':'reconstructed; no substantive issue','reason':s} for i,c,s in extras]
dump(base/'reviews'/f'{pre}issues-v1.json',{'reviewer':'coordinator root','status':'initially blind WHOLE audit','candidate_sha256':'6530949cc16310fabb68a3405266ab5f376a9d153a930bafda0d969ba493f296','peer_NR_findings_read_before_freeze':False,'old_moment_authorship_disclosed':True,'new_NR_constructor_or_contributor':False,'checks':checks,'open_substantive_issues':[],'required_author_repairs':[],'promotion':False})
meta=[
'problems/2019-B4/notes/reasoning-return-r3-manifest-v1.json',
'problems/2019-B4/notes/reasoning-return-r3-sources-v1.json',
'problems/2019-B4/notes/reasoning-return-r3-input-validation-v1.json',
'problems/2019-B4/reviews/moment-tail-acceptance.json',
'problems/2024-B4/reviews/reasoning-return-r3-review-1-manifest-v1.json',
'problems/2024-B4/notes/coordinator-generalized-Kasami-r1-manifest-v1.json']
verified=[]
for rel in meta:
 for x in rows(json.loads((root/rel).read_text())):
  a=rec(x['path']);assert all(a[k]==x[k] for k in ['path','bytes','sha256']),(rel,x,a)
  verified.append({**x,'verification_origin':rel,'verified':True})
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
dump(base/'reviews'/f'{pre}input-checks-v1.json',{'verified_at_utc':now,'all_verified':True,'record_occurrences':len(verified),'unique_paths':len({x['path'] for x in verified}),'records':verified,'hashes_not_mathematical_evidence':True})
files=[f'problems/2019-B4/reviews/{pre}{s}' for s in ['initial-v1.md','issues-v1.json','source-checks-v1.md','freeze-v1.py','input-checks-v1.json']]
dest=base/'reviews'/f'{pre}manifest-v1.json'
dump(dest,{'frozen_at_utc':now,'status':'initially blind fresh nonconstructor WHOLE review; no substantive defect found in NR1-NR4 scope','reviewer':'coordinator root','candidate':rec('problems/2019-B4/notes/reasoning-return-r3-candidate-v1.md'),'constructor_manifest':rec(meta[0]),'complete_candidate_reports_source_obligations_and_accepted_bodies_read':True,'whole_inference_checks':len(checks),'substantive_issues':[],'required_author_repairs':[],'peer_NR_findings_read_before_freeze':False,'older_moment_authorship_disclosed':True,'new_NR_constructor_or_contributor':False,'mathematical_code_CAS_rerun_or_enumeration':False,'promotion':False,'records':[rec(p) for p in files]})
print(json.dumps({'manifest':rec(str(dest.relative_to(root))),'checks':len(checks),'input_occurrences':len(verified),'input_paths':len({x['path'] for x in verified})},indent=2))
