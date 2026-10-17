# Independent whole audit: J15 sole-H2 residue classification

2026-10-16 UTC. Reviewer: `review_2017_coarsening_r1`; constructor: coordinator.
**Initial blind report, frozen before peer comparison.** Requested settings:
`gpt-6.1-sol` / `max`; effective settings have no verified readback. I did
not construct this argument. I have read no peer sole-H2 or sole-H4 audit
or conclusions. My separate sole-H4 initial audit was already frozen;
it is not a mathematical premise for this report. All calculations below
are a fresh hand reconstruction of the present candidate.

Candidate: `../notes/coordinator-J15-soleH2-candidate-v1.md`, SHA-256
`a21d53ab434ea715b85cca9bcf98c715a1522f4faa33d1977c1ad9411b7f9d39`,
and its v1 freeze. No enumeration, CAS or mathematical subprocess was used.

## Verdict and scope

I found no substantive mathematical defect and request no author repair.
I recommend accepting the four stated **necessary** split residue patterns,
their exact actual-witness roles, and the forced H2 center equation,
under the stated accepted earlier inputs. Acceptance remains the
coordinator's decision after the second independent whole audit.

The result is a restriction on a hypothetical J15, double-zero degree20
polynomial with H3(f)(1) and H4(f)(1) nonzero. It is neither an exclusion
of that branch nor a classification of actual global solutions. No
residue pattern is asserted to lift, no complete mask is removed, and
neither degree20 nor the annual part(b) question is solved. The candidate
does not depend on the separate sole-H4 classification or on D3--D5.

## Official hypothesis and accepted inputs

I checked the hypothesis and open part(b) against page2 of the official
[2021 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf),
both current public text and the rendered cached PDF. For each derivative
order1 through d-1 a common root **in Q** is required, with the root allowed
to depend on the order. Other polynomial roots need not be rational or
real. H_k=f^(k)/k! has the same roots as f^(k) in characteristic zero.
I did not solve or reproduce preliminary part(a).

The candidate applies this official condition only inside a stated
normalized hypothetical nontrivial degree20 branch. I checked the
following accepted input statements and their applicability:

* `../notes/rational-witness-p-plus-one-reviewed-v1.2.md`: the rational
  affine normalization with zero a repeated root, center1 simple, and
  all other nonzero roots of positive 19-adic valuation; normalized
  coefficients a_j are 19-integral. The register attributes its published
  facts to Castryck--Laterveer--Ounaies and Draisma--de Jong. It carefully
  distinguishes rational chosen witnesses from all polynomial roots.
* `../notes/padic-rational-newton-reviewed-v1.1.md` and its frozen body:
  J15 gives the Newton edge(5,1)--(19,0), with14 root slots of valuation
  1/14, counted with multiplicity. Such roots cannot lie in Q. The
  supporting-line hypothesis J>=d/2 is met. The width-one lemma requires
  lower exponent i<19, and its D2 applications use i=2,3,4 only.
* `../notes/coordinator-three-rational-witnesses-reviewed-v1.1.md`, T1:
  at least4 distinct rational values are required to cover the derivatives.
  With double zero and the simple center, at least2 distinct values in
  the3 remaining small slots must lie in Q. This previously accepted
  finite-certificate theorem is a dependency; its large certificate stream
  was not regenerated during this purely analytic review.
* `../proofs/reviewed-reasoning-J15-v1.1.md`, D1/D2, with the accepted
  hash recorded in the sources file. I reconstructed those arguments as
  described below. No unproved all-roots-rational premise is introduced.

These accepted restrictions have the correct rational witness domains,
Newton multiplicity convention and characteristic-zero derivative
interpretation. The present candidate imports no additional external
theorem. The official statement, dependency proofs and acceptance records
are separately fingerprinted in the sources file.

## D1/D2 reconstructed in the present branch

The accepted root count leaves exactly3 nonzero slots beyond zero,
center and the14 fractional-valuation roots. Choose2 distinct globally
rational small values. Local Galois fixes both and preserves the
valuation-separated root multiset, so it fixes the remaining small slot.
This proves all3 slots belong to Q19, including the possibility of a
repeated root, without proving the third value lies in Q. Their positive
valuations are integers. The factorization is local:

    f=X²(X-u)(X-v)(X-w)B, B=(X-1)g.

The residual monic degree14 polynomial g has all roots of valuation1/14.
Each nonleading coefficient has positive valuation as a sum of products,
and since it lies in Q19 that valuation is an integer>=1. Its constant
coefficient has valuation1. Hence g is Eisenstein. If B=sum b_iX^i,
then v(b0)=1, v(b_i)>=1 for1<=i<=13, b14 is a unit and b15=1.

D2 exhausts unequal valuations. With one unique outer root the reduced
polynomial T^4(T-U) forces H4 to center; the outer width-one edge also
excludes that root for H2/H3. If the2 inner roots share a valuation,
T²(T-V)(T-W) would require W/V in{11,7} for a noncenter H2 witness
and in{18,3,13} for a noncenter H3 witness. These sets are disjoint,
forcing a second center equation. If all3 valuations differ, the inner
T³(T-V) reduction and edges(4,5),(3,4),(2,3) force all3 low derivatives
to center; H2(0) is nonzero. If exactly2 outer roots have the minimum
valuation, T³(T-U)(T-V) gives the pairwise disjoint necessary ratio
sets {14,15}, {2,10}, {18,4,5} for noncenter H2,H3,H4 witnesses.
The deeper root cannot witness H2/H3 by the width-one lemma; zero cannot
witness H3 because the b0uv term in c3 has uniquely minimum valuation.
Therefore at least2 center equations hold in every unequal case.

Here H3 and H4 are assumed nonzero at center. Unequal valuations could
not supply2 center equations among H2,H3,H4, so all3 small valuations
equal a common integer nu>=1. This argument allows repeated roots or
coincident residues and relies only on D1/D2, not another single-center
classification.

## Exact reduction and Hasse formulas

Put q=19^nu and write u_i=q A_i with A_i in Z19*. The polynomial

    G(T)=f(qT)/(q^5 b0)
        =T² product_i(T-A_i) B(qT)/b0

is integral. Indeed for1<=i<=13 the coefficient q^i b_i/b0 has
valuation>=i*nu; at i14,15 its valuations are14*nu-1 and15*nu-1.
All nonconstant coefficients of B(qT)/b0 vanish modulo19. Therefore

    F=G mod19=T²(T-U)(T-V)(T-W)
               =T^5-sT^4+tT³-zT²,
    U,V,W in F19*, z=UVW !=0.

The identity H_k(G)(T)=q^k H_k(f)(qT)/(q^5 b0) proves that exact
common roots among zero and the small roots yield necessary reduced
Hasse equations. Center is handled separately. No potentially nonunit
binomial coefficient is inverted after reduction.

Differentiation gives

    H2(F)=10T³-6sT²+3tT-z,
    H3(F)=10T²-4sT+t,
    H4(F)=5T-s.

At a nonzero root A of the cubic factor, z=A³-sA²+tA, giving
H2(F)(A)=A(9A²-5sA+2t). At0 the three values are-z,t,-s.
The nonzero-root H2 expression is not used at0. The only possible
noncenter rational witnesses are zero and the3 small slots; the third
local slot is allowed in the necessary cover even if it is non-Q.

## Exhaustive split by the actual H4 and H3 witnesses

The contest supplies actual rational noncenter witnesses for both H3
and H4. First choose such an H4 witness. It is zero or a small root.
This is an existential split; it does not assume that two possible
witnesses cannot coexist. That uniqueness follows from the final rows.

**H4 at zero.** The necessary equation is s=0. If the actual H3 witness
is also zero, t=0 and the nonzero roots split T³-z. Normalize any one
small residue to1. Then z becomes1 and the other residues solve
T²+T+1=0, with discriminant-3=16 and roots7,11. They are nonzero,
distinct, of product1 and sum-1. Hence the normalized multiset is
{1,7,11}. Scaling by any member of this order3 subgroup leaves the
same unordered normalized set, justifying the candidate's freedom in R.

If the actual H3 witness is nonzero, normalize its residue to1 instead.
Its equation is10+t=0, so t=9. The other roots would have sum-1=18
and product t+1=10, hence discriminant18²-40=18. The nonzero squares
in F19 are{1,4,9,16,6,17,11,7,5}, so18 is a nonsquare. This contradicts
the already proved splitting over F19. Coincident slots cannot change
a nonsquare into a split quadratic. Thus the first row, caseA, is the
only H4-zero possibility.

**H4 at a nonzero small root.** Let its residue be R!=0 and normalize
it to1, naming the other two slots x,y without assuming distinctness.
Then s=5 and x+y=4, xy=t-4. Split the actual H3 witness into zero,
a small slot of residue1, or another small slot:

* At zero, t=0, so xy=15 and the discriminant16-60=13 is a nonsquare.
  Thus this branch is impossible.
* At residue1,10-20+t=0 gives t=10, so xy=6. The discriminant
  16-24=11 has square roots±7, and (4±7)/2 gives{8,15}. This is B.
  If another actual slot had also reduced to1, it was included in this
  calculation; the resulting distinct residues now exclude that possibility.
* At a residue x!=1, use y=4-x and t=4+4x-x². The H3 equation becomes
  9x²-16x+4=0. Its leading coefficient9 is nonzero; its discriminant
  256-144=112=17 has square roots±6. Since2*9=18=-1 is a unit, the
  roots are (16±6)/18=16,9. For x16 one obtains y7,t2, giving C;
  for x9 one obtains y14,t16, giving D.

The only divisions were by the explicitly nonzero common scale and
the units2 and18. No root difference was divided out. All3 slots are
visibly distinct and nonzero in every surviving row. A quadratic with
zero discriminant was not discarded anywhere; the H2 check below
explicitly includes that case.

## Exact table check, degeneracy and actual-root roles

CaseA has s=t=0. For each nonzero small root A,
H3(F)(A)=10A², H4(F)(A)=5A and H2(F)(A)=9A³ are nonzero. Thus the
actual H3 and H4 witnesses are both exactly zero, using their existence
and the exclusion of all other rational noncenter roots. This is not an
assertion that t=s=0 alone guarantees those exact equations. H2 also
fails at0 because H2(F)(0)=-z!=0.

For B,C,D, H4(F)=5(T-1). Its value at0 is nonzero, so it has precisely
the normalized residue1 slot available. The following factorizations
check the remainder of the table directly over F19:

| Case | Small slots | (s,t) | H3(F)(T) | Nonzero-root H2 test q2(T) |
| --- | --- | --- | --- | --- |
| B | {1,8,15} | (5,10) | 10(T-1)² | 9(T-13)² |
| C | {1,7,16} | (5,2) | 10(T-16)(T-5) | 9(T-8)(T-18) |
| D | {1,9,14} | (5,16) | 10(T-9)(T-12) | 9(T-3)(T-4) |

Here q2(T)=9T²-25T+2t. Its unreduced discriminants are respectively
625-720=-95=0,625-144=481=6,625-1152=-527=5. Square roots are
respectively0,±5,±9; denominator18 is nonzero. Therefore all its roots,
including the repeated B root13, are exactly those in the table and
miss the relevant small multiset. This confirms the candidate handles
the degenerate H2 discriminant correctly. The double H3 root1 in B is
also harmless: it is a multiplicity of the derivative's reduction,
whereas the small-root multiset has exactly one slot of residue1.

Since t!=0 in B,C,D, zero is not an H3 witness. Its only possible small
slots are respectively1,16,9, because the second listed H3 roots miss
the corresponding small multisets. Each eligible residue has a unique
actual root slot. In B the actual H3 and H4 witnesses must therefore
be the *same actual root*, not just roots with equal residues. In C and
D they occupy the two distinct indicated slots. Those actual values lie
in Q because the contest supplies rational witnesses and no alternative
slot is available. D1 alone would only put them in Q19. In A no global
rationality of the arbitrary normalizing residue's root is implied.
The accepted at-least2 rational small roots condition still applies in
every case; this classification does not specify unselected witnesses.

H2 has no rational noncenter witness in any row: nonzero small slots
fail the necessary q2 equation, zero has nonzero initial value-z (and
also H2(f)(0)!=0 by exact multiplicity2), and the14 fractional roots
are not rational. Consequently the contest hypothesis forces the only
remaining eligible value, center1, to satisfy H2(f)(1)=0. This is a
necessary exact equation inferred from witness existence and exclusion,
not an attempted sufficiency claim for reduction.

## Adversarial coverage and remaining gap

Potentially dangerous cases were checked explicitly: H4 at zero;
H3 at zero in both H4 branches; a different root slot sharing the H4
residue; x=y or another repeated slot; nonsplit versus repeated quadratic
roots; the zero discriminant in B; and confusion between rational and
local roots. The displayed algebra exhausts the actual witness choices,
and none of these cases creates a missing branch. No equality of actual
roots is inferred until the final distinct-slot patterns are established.

There are **zero unresolved substantive objections** and no requested
repairs. The exact remaining gap is the candidate's stated one: no row
has been lifted through all derivative equations or globally excluded.
Distinct leading residues mean the accepted repeated-residue D4 parity
obstruction does not directly apply. Multiple low centers, triple zero,
lower J and full degree20 remain outside this result.

Administrative tooling read files, checked the official PDF, fingerprinted
inputs and wrote only this assigned review prefix. No mathematical
enumeration, CAS, Git operation, new source download or shared-state
edit was performed. Earlier review and construction packets were
preserved byte for byte. Last coordinator-supplied account-wide weekly
telemetry:17% used at22:11 UTC, reset1792745187, ceiling90% total.
