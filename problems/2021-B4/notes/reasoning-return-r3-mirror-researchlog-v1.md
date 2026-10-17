# Mirror supplement research log

2026-10-17 UTC. Candidate construction after freezing
reasoning-return-r3-candidate-v1.md. Its bytes are preserved.

The next target was the triple-weight tie retained by the old low-order
family. The parity test cannot exclude it because its even Taylor part
has three terms of equal weight. Rather than ignoring that case, I
asked what its actual high rational witnesses would require.

If the repeated root is exactly2r and all even derivatives through14
vanish at r, double roots0,2r fix the even part exactly. The top
three normalized derivatives then reduce to three low-degree equations.
Their witness set is exactly{0,1,r,2r}; fractional roots remain
unavailable. The proof excludes a3 unit by the different center
requirements of D3 and D4, then has only six symbolic witness pairs.
Two leading pairs survive, and two exact rational comparisons exclude
them. This gives M1 for the precise mirrored subfamily, not all tied
cases or all repeated2R residues.

Construction correction, preserved candidly: my first UNFROZEN message
used the wrong sign for D4's linear a3 coefficient. The correct formula
is +4a3 X. Before any supplement file froze I recomputed the elimination
and all six residues from the correct formula. The table is eta0:
15,13,10 and eta2:9,6,4. Thus two cases, not one, survive the first
congruence. Their exact r values9690/15517 and9690/3863 contradict
H18's95/48 and95/142 respectively. The correction was immediately sent
to the coordinator. The earlier frozen G1/G2/C1/C2/W packet contains no
such D4 elimination and remains unchanged.

Self-checks:
- E(r)=E'(r)=0 uses double roots at BOTH0 and2r, not just a repeated
  residue. Removing that exact equality invalidates this reduction.
- h16=r4,h18=-2r2 follow by a two-equation identity; r!=0.
- D2,D3,D4 use binomial-normalized coefficients with their signs
  embedded in a_j, not a manually alternating convention.
- a2,a4 are nonunit for every integer nu>=1; a3 is treated in two
  cases without assuming its valuation.
- In the unit case the D4 difference is a unit times x-y throughout
 19Z19, while its value at r has valuation4nu-1>nu.
- Once a3 is nonunit, the center is excluded for all three top
  derivatives and r is excluded for H16,H18 by their exact values.
- H18 forces the two exact rational r values and hence nu=1; it is
  not assumed at the start from a finite test or q0 condition.
- Every coefficient19A is a nonzero residue in the six-case table.
- Exact comparisons use positive rational inequalities, avoiding any
  rounded numerical conclusions.
- All roots selected are rational actual f roots. The quotient is
  rational here only because0,1,r,2r account for its removed factors;
  the general local-to-global factor issue is not swept aside.
- No J16 work, old finite-cover certificate rerun, higher mask search,
  Hensel table, CAS or mathematical program was executed.

An intermediate attempt considered improving the old low-order
family by adding an even residual T4 coefficient to force H5(1)=0.
The3-by3 system at r=0 has matrix rows(1,1,1),(10,35,84),(1,21,126)
with determinant1645, a19-unit, suggesting that such a modification
could supply another partial family. I did not develop it into a
separate claimed result or create or test that larger family. The stronger
M1 exclusion covers all residual even polynomials subject to(M),
so that illustrative construction was dropped rather than enlarged.

Primary-source and scope checks use the same accepted D1/D3
normalization and the previously rechecked published boundary. No new
external theorem, source download, novelty or prime5 exclusion is
claimed. Only the assigned reasoning-return-r3-mirror-* files are
written. Metadata hashing and JSON creation will freeze this proof
and preserve all twelve earlier own packets. No Git/shared edit,
charge, contact, bypass, spawn or separately billed API.

Latest authoritative weekly total23%, window10080 minutes,
reset1792745187. Stop below90% total with integration reserve.
Two fresh independent nonconstructor whole audits are required;
only the coordinator may accept or promote M1.

