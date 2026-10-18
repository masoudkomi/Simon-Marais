**Candidate proof - unverified. Working follow-up saved 2026-10-18 UTC.**

This is a NEW extension of frozen Q1--Q4, not a repair or an acceptance.
No v1 bytes are changed. TWO OTHER whole audits are required for any new
proof. The root supplied no new mathematical inference. Requested inherited
gpt-6.1-sol/max; independent effective readback unavailable.

Let c_0=0,c_1=-4,c_2=-3,c_3=-2,c_4=4, indexed by the Euclidean residue
of d modulo5. Define h(d)=|d-c_(d mod5)|/5 and Phi(a,b)=a+b+2h(a-b).
The height is a nonnegative integer; the centers lie in[-4,4]. If |d-D|<=4,
then |h(d)-h(D)|<=12/5 and integrality improves this to<=2.

For central Q3 outputs B>=43,D in[-9,19], any ordinary parent is positive,
official, inI and (outside FDelta) off-diagonal. Its difference satisfies
|d-D|<=4. Moreover a>=30: otherwise floor(a/30)=0 gives b=B>=43 and
d=a-b<=29-43=-14, contradicting d inI. Since b>=31, the sum drop is at
least2+3=5. Therefore Phi(parent)-Phi(output)<=-5+4=-1.

For a critical output/start Y=(A,B), B>=43, whose difference lies in the
eight outer offsets or whose point lies in FDelta\Delta, Q1 gives the
following complete double-input possibilities. R_L means A mod30 in{0,1},
B mod20 in{17,18,19}; R_H means A mod30 in{28,29}, B mod20 in{0,1,2}.
R_L forces D mod10 in{1,2,3,4}; R_H forces it in{6,7,8,9}.
Thus critical R_L differences are1,2,21,22,23, and critical R_H differences
are-13,-12,-11,-1. Their actual same-output partners are respectively
(A-2,B+3), difference D-5, and(A+2,B-3), differenceD+5.
The displayed choice of centers makes h drop by exactly1 in EVERY listed
case, so Phi drops by1 for R_L and by3 for R_H. Both partner differences
are inI and nonzero. Since A>=30,B>=43, partner coordinates are bounded
below by(28,46) or(32,40); their products exceed600. A hypothetical
survivor transfers to its off-diagonal same-output partner.

Consequently a least-Phi actual survivor inI, if any, lies in the set
Sstar of official off-diagonal pairs inI satisfying either B<=42, or
B>=43 and(D in{-13,-12,-11,-10,20,21,22,23} OR Y inFDelta\Delta)
and Y outside BOTH R_L,R_H. The latter exclusion says exactly
F^{-1}(F(Y))={Y}, NOT that F^{-1}(Y) is singleton and NOT that no later
iterate merges. Hitting all Sstar is equivalent to official universal
hitting, by attributed eventual-strip entry and positive-integer Phi
well-ordering. Sstar is still UNBOUNDED and unproved.

The B43 cutoff is deliberate. Y=(27,36), parent(25,36), has Phi(Y)=65,
Phi(parent)=67; Y=(33,40), parent(29,40), has both potentials75. Thus the
old B36 positivity cutoff cannot simply be reused for STRICT Phi descent.

An entire legal diagonal-image family is removed by the new merger step:
Y_j=(660j+239,660j+240), j>=0, has unique diagonal parent
(600j+219,600j+219), but the alternate SAME-OUTPUT INPUT is
Z_j=(660j+241,660j+237). Both next outputs equal
(726j+263,726j+261), Phi(Z_j)=Phi(Y_j)-3. This asserts no future survival
or hitting of these families.

An elementary additional hitting subfamily: if an actual input has
D=2 and belongs to R_L, then B=60m+58 or60m+59, A=B+2. Substitution gives
F(A,B)=(66m+64,66m+64) or(66m+65,66m+65), respectively.
Thus these particular official states meet the diagonal in one step.
No other complete residual ray family is concluded to hit.

Literature checked freshly: Baake--Roberts--Weiss2008 introduction and
Section2.2 concern INTEGER matrices acting modulo1 on a torus and finite
rational lattices. Guiheneuf2018 definitions10--12/Lemmas13--14 concern
nearest-lattice discretizations and GENERIC bounded determinant-one
matrix sequences (with perturbations/translations in the collision
argument). Guiheneuf--Joly2017 Section5.2/Theorem5.4 concerns GENERIC
orthogonal sequences and density loss. None is imported for this FIXED
rational floor map with linear determinant99/100, nor for an EVERY-orbit
diagonal assertion. Full proof/imports of those papers were not audited.

Failed stronger conclusions: Phi is a descent for selected inverse or
merger moves, not asserted to decrease along the original forward orbit.
An off-diagonal orbit cannot enter FDelta at time>=1, by Q2, but deleting
FDelta from the minimum argument simply moves its birth obstruction to
later images; no termination follows. Q1 surjectivity onZ2 need not give
an official or strip-preserving parent outside Q3. Density loss and finite
fibers cannot exclude an exceptional ordinary survivor. Full completed
proof, obligations, sources, failures, worklog and compact immutable freeze
will be written before any handoff; this draft itself is not that freeze.
