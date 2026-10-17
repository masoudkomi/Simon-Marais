"""Administrative byte/source/obligation freeze only; no mathematical computation."""
from pathlib import Path
import hashlib,json,datetime
r=Path.cwd();now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def rec(rel):
 b=(r/rel).read_bytes();return {'path':rel,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def write(rel,obj):
 with (r/rel).open('x') as f:f.write(json.dumps(obj,indent=2)+'\n')
script='progress/freeze-local-algebra-2026-10-17-1129.py'
specs=[{
 'year':2024,'prefix':'coordinator-Kasami-necessary-valuation',
 'candidate':'problems/2024-B4/notes/coordinator-Kasami-necessary-valuation-v1.md',
 'claims':['NV: whole phi_(q²−q+1) divides phi_n implies v2(n−1)=k, for q=2^k,k>=2,odd n>=3'],
 'inputs':['problems/2024-B4/proofs/reviewed-composition-Kasami-v1.1.md','problems/2024-B4/reviews/composition-Kasami-acceptance.md','problems/2024-B4/reviews/composition-Kasami-acceptance.json'],
 'obligations':[
  'Match accepted CP1 WHOLE divisor, odd d/n domains and degree relation; not individual Kasami factors.',
  'Obtain q(q−1)|n−1, n>=d and v2(n−1)>=k, including equality n=d.',
  'Verify G_j(0)=G_j prime(0)=1 for every odd j>=3; hence H(1)=H prime(1)=1.',
  'Factor H(T)+1=(T+1)Q(T) with Q(1)=1 and preserve exact local order after substitution.',
  'Use alpha in F_q minus F2 only when k>=2; both alpha and alpha+1 nonzero.',
  'Check all terms through q+1 of G_d(alpha+z), including absent intermediate degrees and the q/q+1 binomial coefficients.',
  'Check constant1, linear0, q coefficient0 and q+1 coefficient1/(alpha(alpha+1))!=0.',
  'For s>k check the binomial support of n=1+2^s h and cancellation of constant/linear terms at alpha.',
  'Verify finite order and 2^s>=2q>q+1 contradict the preserved order.',
  'Retain q=2 unit-divisor counterexample n=5 and no claim of general-q full progression necessity.',
  'No new external MCM/APN/ramification theorem, empirical test or novelty premise.'
 ],
 'sources':{'accepted_premise':'Exact CP1 body and full scope read; SHA below. Its factor-composition equivalence is the only non-elementary project premise.', 'new_external_theorem':False, 'official_scope':'2024 B4(b) only; the result is a necessary condition for a WHOLE fixed divisor, not full reducibility.', 'mathematical_code_CAS_or_scan':False}
},{
 'year':2025,'prefix':'coordinator-diagonal-moment',
 'candidate':'problems/2025-B4/notes/coordinator-diagonal-moment-candidate-v2.md',
 'claims':['MS1 reciprocal residue separation under nonzero inverse moment','MS2 faithful equivariant Fourier evaluation and cross-list disjointness','MS3 nonzero inverse moment implies trivial stabilizer','MS4 exact inverse Fuchsian moment','MS5 exact first-case-element separations for p>7'],
 'inputs':['problems/2025-B4/notes/coordinator-diagonal-moment-separation-v1.md','problems/2025-B4/notes/coordinator-diagonal-moment-separation-v1.1.md','problems/2025-B4/notes/coordinator-diagonal-moment-separation-v1.2.md','problems/2025-B4/notes/coordinator-diagonal-moment-separation-v1.3.md','problems/2025-B4/notes/coordinator-diagonal-appendix-inspection-v1.md','.cache/literature/deep-literature-r1/2025-bartolome-mihailescu-binary-thue-v2.pdf'],
 'obligations':[
  'Direct indices sigma_a(zeta)=zeta^a; original inverse source indices must be reindexed explicitly.',
  'Prove O/(lambda)=F_p and geometric-sum unit in localization, including t=ac mod p representatives and negative coefficients.',
  'Nonzero inverse moment separates all reciprocal coordinates by their residues; common nonzero scalar preserves distinction.',
  'Fourier map injectivity: degree at most p−1, zero constant, minimal polynomial Phi_p constant1; no weight hypothesis.',
  'Prove equivariance and exact stabilizer equality, then disjoint Fourier value SETS from group-ring nonconjugacy.',
  'Distinctness WITHIN each Fourier list is separate; nonzero inverse moment is sufficient by its h^(-1) transformation.',
  'Norm element counterexample: positivity/weight/Fermat membership alone do not imply trivial stabilizer.',
  'Square-sum permutation identity is exact for any positive a prime to p; division by p and reduction are valid for p>=5.',
  'Source inverse-index moment is sum c floor(ac/p), not the action-on-zeta moment sum c^(-1)floor(ac/p).',
  'Compute (a−a^(-1))/12, Theta2 value1/8 and psi2 value7/72; p=7 zero, p=3 excluded from this formula.',
  'Check general Fueter formula and its possible zero; do not grant arbitrary source selections nonzero moments.',
  'Source definition is original Fourier eta versus later scaled reciprocal b1; correspondence of roles is not formula equality.',
  'No new proof of source Lemma3, Wieferich conditions or arbitrary second-case moment selection.',
  'No singular-system solvability/all-conjugate cancellation/nonzero delta/stronger Diophantine range/full annual theorem/novelty.'
 ],
 'sources':{
  'original':{'url':'https://www.researchgate.net/publication/226863681_Class_Number_Conditions_for_the_Diagonal_Case_of_the_Equation_of_Nagell_and_Ljunggren','edition':'Author-uploaded chapter, internal version2.0,2007-09-17; published2008','actual_read_scope':'Section2.3 equations14–18 and Lemma3/proof; section4.3 first/second-case selections, Fourier eta definitions, Lemma14 and relevant singular-system passages. The entire Diophantine proof was not newly reconstructed.','binary_sha256':None,'hash_limit':'web text viewer, no invented binary hash'},
  'later':{'url':'https://arxiv.org/pdf/1412.5798v2','edition':'Internal version1.13,2021-11-02','actual_read_scope':'Section2.4 coefficient definitions, Lemmas2.8/2.10 context and relevant complete proof; Appendix5.1–5.1.1 and previously rendered two application pages. No full proof import.','cache_path':'.cache/literature/deep-literature-r1/2025-bartolome-mihailescu-binary-thue-v2.pdf'},
  'new_external_theorem':False,'mathematical_code_CAS_or_scan':False,
  'source_role':'Exact definitions and application boundary only; MS1–MS5 are proved explicitly. Old notes remain unchanged historical research; consolidated v2 states the current candidate scope.'}
}]
for s in specs:
 base=f"problems/{s['year']}-B4/notes/{s['prefix']}"
 obligations=[{'id':f"O{i+1:02d}",'obligation':x} for i,x in enumerate(s['obligations'])]
 write(base+'-obligations-v1.json',{'status':'candidate proof — unverified','claims':s['claims'],'whole_review_required':True,'obligations':obligations})
 write(base+'-sources-v1.json',{'recorded_at_utc':now,**s['sources'],'input_fingerprints':[rec(x) for x in s['inputs']]})
 write(base+'-manifest-v1.json',{'frozen_at_utc':now,'status':'candidate proof — unverified; two independent nonconstructor WHOLE audits required','constructor':'coordinator root','claims':s['claims'],'no_mathematical_computation_or_CAS':True,'no_novelty_or_full_annual_solution':True,'requested_worker_model':'gpt-6.1-sol','requested_reasoning_effort':'max','verified_effective_settings':None,'records':[rec(s['candidate']),rec(base+'-obligations-v1.json'),rec(base+'-sources-v1.json'),rec(script)]})
 print(s['year'],json.dumps(rec(base+'-manifest-v1.json')),json.dumps(rec(s['candidate'])))
