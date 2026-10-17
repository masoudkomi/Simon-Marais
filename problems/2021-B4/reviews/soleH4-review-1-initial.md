# Independent whole audit: J15 sole-H4 residue classification

2026-10-16 UTC. Reviewer: `review_2017_coarsening_r1`; constructor: coordinator.
**Initial blind report, frozen before peer comparison.** Requested settings:
`gpt-6.1-sol` / `max`; effective settings have no verified readback. I did
not construct this argument. I have read no other new sole-H4 or sole-H2
review or its conclusions. Earlier accepted dependency registers are
identified below and are not fresh reviews of this candidate.

Candidate audited: `../notes/coordinator-J15-soleH4-candidate-v1.md`, SHA-256
`042b15f45a39f6773ec8e5eea6c4294eab5e794e98a961534b899ef2568b508e`,
with its v1 freeze. I reconstructed the whole argument by hand, including
the source-domain check, D1/D2 applications, scaling, exhaustive actual
witness split, finite-field calculations, degenerate cases and final
identification of actual root slots. No enumeration or CAS was used.

## Verdict and exact accepted scope

I found no substantive mathematical defect. I recommend accepting the
three stated **necessary** residue patterns, uniqueness of the actual H2
and H3 witnesses as stated, and forced H4 center equation, conditional on
the explicitly accepted earlier inputs. The candidate does not exclude
this branch, any complete center mask, all J15 polynomials, degree20 or
the annual classification. Only the coordinator may promote its status
after the second independent audit and reconciliation.

There is no inference from a compatible residue pattern to a lift over
Q19 or Q. In particular, the unselected third small root is not asserted
to be globally rational. No new theorem from the literature is invoked
by the candidate; its substantial earlier inputs remain explicit accepted
dependencies, not newly verified certificate streams in this review.

## Official domain and dependency checks

I checked B4 on page2 of the official [2021 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf),
using the current public PDF text and a rendered page from the cached
copy. The polynomial has rational coefficients, and for **each** derivative
order1 through d-1 there must be a common root in Q; the selected root
may depend on the order. The open part(b) asks for the degree
classification. I did not investigate or reproduce preliminary part(a).
Multiplying a characteristic-zero derivative by the nonzero scalar1/k!
does not alter its roots, so Hasse derivatives preserve this hypothesis.

The present claim is a necessary restriction on a hypothetical nontrivial
degree20 polynomial in the accepted 19-adic normalization, with J=15 and
zero multiplicity exactly2. It also assumes H2(f)(1) and H3(f)(1) are
nonzero. These are stronger hypotheses than the official problem, and
are stated throughout. The candidate does not replace rational common
roots by a nonconstant gcd over Q or assume all roots of f rational.

I read the accepted J15 proof through D2, its acceptance register, the
normalization register, the Newton register and relevant frozen Newton
body, and the rational-witness-count register and T1 derivation. The
following are the actual dependencies used:

* `../notes/rational-witness-p-plus-one-reviewed-v1.2.md`: rational affine
  normalization; simple center1; integral normalized coefficients; all
  other nonzero roots of positive 19-adic valuation. Published inputs are
  attributed there to Castryck--Laterveer--Ounaies and the two-recycled-root
  observation in Draisma--de Jong. No all-roots-rational assumption is added.
* `../notes/padic-rational-newton-reviewed-v1.1.md` and its frozen body:
  the long Newton edge, counting slots with multiplicity; and the width-one
  derivative lemma with lower exponent i<19. At J15 the long edge has
  endpoints(5,1),(19,0), hence14 slots of valuation1/14. The supporting-line
  inequalities hold because J15>=10. These cannot be rational roots.
* `../notes/coordinator-three-rational-witnesses-reviewed-v1.1.md`, T1:
  at least4 distinct rational root values are needed to cover derivatives.
  This is an accepted exact finite-certificate result, not a new
  enumeration in this audit. Zero and center account for at most2 values;
  hence the3 small slots include at least2 distinct Q-rational values.
* `../proofs/reviewed-reasoning-J15-v1.1.md`, D1/D2: local splitting,
  residual Eisenstein factor and unequal-valuation forcing. Its hash and
  acceptance hash agree with the candidate's frozen dependency entries.

The classical Newton theorem is used over an algebraic closure of Q19,
counting repeated roots repeatedly. Rational roots have integral valuation.
Those precise hypotheses match this use. The cited accepted Newton
register explicitly supplies the multiplicity convention via Stoll
Theorem3.6. I do not extend its assertion to arbitrary smaller J.

## Reconstruction of D1 and the D2 reduction

Choose two distinct Q-rational values among the3 small slots. Local
Galois automorphisms fix each value, preserve valuation and the entire
root multiset, and therefore fix its remaining one small slot. A repeated
slot is covered as well. Thus all3 slots belong to Q19; this gives no
conclusion that the remaining value lies in Q. Their valuations are
positive integers. Monic division gives

    f=X²(X-u)(X-v)(X-w)B(X),  B=(X-1)g,

where g has degree14 and all roots of valuation1/14. A nonleading
coefficient of g has positive valuation as a sum of positive-valuation
products. It belongs to Q19, so its valuation is an integer>=1; the
constant coefficient has valuation1. Hence g is Eisenstein. In B=sum b_iX^i,
v(b0)=1, v(b_i)>=1 for1<=i<=13, b14 is a unit and b15=1.

For completeness I checked all unequal-valuation cases of D2, rather
than assuming the conclusion merely from its label. A unique outer
root produces T^4(T-U): H4 has nonzero values -U and4U at the available
reduced roots, so H4 must use the center. Its width-one edge(4,5)
also excludes the outer root for H2/H3. If the2 inner valuations agree,
T²(T-V)(T-W) requires W/V in{3/2,2/3}={11,7} for H2 and in
{-1,3,1/3}={18,3,13} for H3, disjoint sets in F19. Zero cannot supply H2.
Thus another center equation is forced. If the2 inner valuations differ,
T³(T-V) and the width-one edges(3,4),(2,3) force H3 and H2 respectively
to the center; H2(0)=c2 is nonzero. If exactly2 outer roots share the
minimum valuation and the third is deeper, the three necessary ratio
sets are {14,15} for H2, {2,10} for H3 and {18,4,5} for H4. They are
pairwise disjoint. The deeper width-one root cannot witness H2/H3;
H3(0)=c3 is nonzero because its b0uv term has uniquely least valuation.
The lower exponents in every width-one use are2,3 or4, all<19.

Consequently unequal valuations force at least2 center equations among
H2,H3,H4. In the present candidate H2 and H3 are both noncenter, so the
3 valuations must be a common integer nu>=1. This is the only D2
consequence needed. Coincident roots or residues have not been excluded
at this stage.

## Integral scaling and derivative equations

The candidate's short scaling sentence has the following direct
justification from D1. Put q=19^nu, u_i=q A_i with A_i units in Z19, and

    G(T)=f(qT)/(q^5 b0)
        =T² product_i(T-A_i) B(qT)/b0.

The coefficient q^i b_i/b0 has valuation>=i*nu for1<=i<=13;
for i14,15 it has valuation14*nu-1 and15*nu-1 respectively. All are
positive. Therefore B(qT)/b0 is integral and reduces to1, and

    G mod19=F=T^5-sT^4+tT^3-zT²,
    s=U+V+W, t=UV+UW+VW, z=UVW !=0.

This establishes the claimed initial form without assuming a rational
residual factor. Hasse differentiation satisfies

    H_k(G)(T)=q^k H_k(f)(qT)/(q^5 b0).

Thus an exact common-root equation at a noncenter small root or zero
reduces to the stated equation for F. The center is kept separate; its
scaled coordinate is not integral. The14 fractional roots are unavailable
as rational witnesses, independent of any derivative equation.

Direct differentiation gives

    H2(F)=10T³-6sT²+3tT-z,
    H3(F)=10T²-4sT+t,
    H4(F)=5T-s.

At a nonzero root A of T³-sT²+tT-z, substitution of
z=A³-sA²+tA gives H2(F)(A)=A(9A²-5sA+2t).
At zero the three values are -z,t,-s. Every numerical coefficient
used here is reduced only after characteristic-zero Hasse differentiation.

H2(0) is in fact exactly nonzero because f has zero multiplicity2;
its reduced value -z also confirms this. Its actual noncenter rational
witness must therefore be a small root r. Its residue R=r/q mod19 is
nonzero. Replacing every residue by its ratio to R preserves the zero
equations by homogeneity. Write the other two slots as x,y. They may
initially coincide with each other or with1, and lie in F19*. Then

    s=1+x+y, t=x+y+xy, 2t=5s-9.                 (A)

No root difference has been divided out.

## Complete actual H3 witness split and arithmetic

The full contest hypothesis gives an actual Q-rational H3 witness. It
cannot be center by assumption, and is zero or one of the3 small slots.
Allowing the third local but possibly non-Q slot in this necessary
analysis only enlarges the candidate cover. There are precisely the
following possibilities, classified by that actual witness's residue.

1. **Actual witness zero.** Here t=0. Equation(A) gives
   s=9/5=17; hence x+y=16 and xy=3. The discriminant is
   16²-12=16 in F19, with square roots±4. Since2 is a unit,
   {x,y}={(16+4)/2,(16-4)/2}={10,6}. Both are nonzero and differ from1.
2. **A small actual witness whose normalized residue is1.** Its equation
   is10-4s+t=0. With(A) this gives3s=11, s=10,t=11,
   x+y=9,xy=2. Discriminant9²-8=16 yields{12,16}. This computation
   includes a possible *different* root slot reducing to1; the resulting
   distinct residues rule that possibility out, rather than assuming
   slot uniqueness in advance.
3. **A small actual witness of residue x!=1.** Rewrite(A) as
   (2x-3)y-3x+4=0. If2x-3 vanished, x=3/2 and
   -3x+4=-1/2 would remain nonzero, contradiction. Thus
   y=(3x-4)/(2x-3). The H3 equation is
   6x²-3x+y(1-3x)=0. Multiplication by the now nonzero denominator
   gives12x³-33x²+24x-4=0. Modulo19 this factors as
   (x-3)(12x²+3x+14). The quadratic has leading coefficient12!=0
   and discriminant9-672=-663=2. The nonzero square list from the
   residues1²,...,9² is{1,4,9,16,6,17,11,7,5}; it omits2.
   Therefore x=3 and y=(9-4)/(6-3)=5/3=8.

The cubic factorization is modulo19, as stated, not an identity of
integer polynomials: its integer expansion has linear term5x and
constant-42, differing from the numerator by19x+38. These differences
vanish in F19. This distinction causes no issue. No omitted zero leading
coefficient, forbidden denominator, repeated discriminant root, repeated
slot or unsplit quadratic branch survives.

## Table check and passage back to actual roots

I checked the table algebraically through factorizations, not a residue
search. The nonzero H2 test polynomial q2(T)=9T²-5sT+2t and the H3
polynomial factor as follows:

| Case | Small residue slots | (s,t) | q2(T) | H3(F)(T) | H4 root s/5 |
| --- | --- | --- | --- | --- | --- |
| I | {1,6,10} | (17,0) | 9T(T-1) | 10T(T-3) | 11 |
| II | {1,12,16} | (10,11) | 9(T-1)(T-13) | 10(T-1)(T-3) | 2 |
| III | {1,3,8} | (12,16) | 9(T-1)(T-12) | 10(T-3)(T-17) | 10 |

In caseI q2 has the extra root0, but H2(F)(0)=-z!=0;
the nonzero-root elimination formula for H2 must not be applied at0.
The candidate correctly treats0 separately. The H3 root3 in caseI is
not a small root, so the only eligible H3 residue is0 there. In caseII
only1 is eligible; in caseIII only3 is eligible. All H4 roots in the
last column miss the small slots. Since s!=0 in every row, H4 also
does not vanish at0.

Each of the3 small residues occurs in exactly one slot in every row.
Thus the actual small values are distinct and simple in this cluster;
two equal actual values would give repeated residues. A rational H2
witness exists and can lie only in the unique residue-R slot, so that
actual root r is rational and is its unique possible small witness.
Likewise H3's actual witness is zero in caseI, the same actual r in
caseII, and the unique residue-3R slot in caseIII. In caseIII global
rationality of that slot follows from existence of the rational H3
witness and uniqueness, not from a false implication Q19=>Q. The
unselected slot remains allowed to be non-Q.

H4 has no rational noncenter witness: zero and every small slot have
nonzero necessary initial H4 value, and the14 fractional roots are
not rational. The full derivative-witness hypothesis leaves only center1.
Therefore H4(f)(1)=0. This uses the existence quantifier for H4, not a
claim that a residue-zero equation suffices for an exact common root.

## Adversarial checks, limitations and record

I explicitly tested the potential logical failures: treating local roots
as rational witnesses; identifying roots from equal residues prematurely;
discarding repeated slots before the split; dividing by2x-3 without
checking it; applying the nonzero-root H2 formula at zero; using only a
necessary H3 residue equation to assert an exact root; and promoting a
residue classification to branch emptiness. None occurs in the candidate.
The witness existence plus final slot uniqueness repairs the apparent
residue-to-exact-root concern. The discriminant calculation exhausts the
only remaining cubic branch over the actual split field F19.

There are **zero unresolved substantive objections** and no requested
author repair. This is a partial, dependency-based acceptance recommendation.
No new odd-valuation collision obstruction or lift existence is proved.
No native mathematical subprocess, CAS, enumeration, Git command, new
source download or shared-state edit was performed. Tools only read,
rendered the official PDF, hashed inputs and wrote this assigned review
packet. Source fingerprints and the freeze manifest accompany this report.
Last coordinator-supplied weekly telemetry:17% used at22:11 UTC,
reset1792745187; ceiling90% total. No budget-window transition occurred.
