# Q1–Q8 v3: fresh independent ENTIRE WHOLE R1

2026-10-18 UTC. A, `/root/review_2021_reasoning_j15_r2`.
**Recommendation only; no coordinator promotion.**

I reconstructed the ENTIRE jointly proposed Q1–Q8 argument, including
the complete v1/v2 appendices, all100 obligations and the twenty exact
outside-parent intervals. I found no substantive defect and request no
author repair. I recommend accepting the eight claims ONLY as the
ordinary-fiber classification, stated rank/merger lemmas, constructive
subfamily and exact UNBOUNDED seed equivalences actually proved. No
remaining seed family has its entire future decided.

Exact target:
`problems/2022-B4/notes/reasoning-complexity-return-r9-candidate-v3.md`,
44042B,SHA77bf84340543589d96698a64df5e3850cdf22fe953ee45587ab0d79997184ff5;
freeze-v3.json4828B,SHAe5c079493fd134eb05318d3b298565c0a4679ed0806431b9973230762d9c3ce2.
The full v2 main31982B SHA4d3d81540f7f928e4aff9f865e9384cab2c45ca2a7d4e28d971c1531c943c578
is its exact suffix, and the v1 main16457B
SHA2fdb1a495afa4f607b9fb63b7a1535e7ba6797ae5b699fd9d25124b503bfe211
is the v2 exact suffix. The obligation suffixes also match literally.
Those checks establish preservation, not mathematical correctness.

## Independence, accepted context and actual official domain

B is the sole NEW Q1–Q8 constructor, and root supplied no new proof
inference. I contributed none of these new lattice, rank, orphan or
seed arguments. I have not read, hashed or received any NEW C R9 v3
review, finding, ledger, source or metadata before the ENTIRE initial
freeze. The old narrower v1 R1 is mine and remains immutable; it does
not substitute for this complete fresh whole v3 reconstruction. Root
announced v1 acceptance during this audit, conveying no NEW v3 peer
finding. I did not use that announcement to skip any of the100 checks
or open a new peer report; the old submission labels remain historical.

Older roles include2022 R6 authorship and R3/R4/R5/R7/R8 whole review.
The older accepted input scopes are not independently self-recertified.
The ONLY earlier mathematical input to the universal equivalences is
the attributed eventual entry into the strip I=[−13,23]∩Z. I read the
complete accepted P1–P4 body and its exact acceptance scope, and checked
that preliminary STATEMENT in the official paper and organizer report.
No proof of part(a) is reproduced or investigated. The older rational-
base, fiber, density and complexity results are context and limits,
not undisclosed premises for Q1–Q8.

The actual question has positive ordinary integer starts, a0b0>=600,
simultaneous updates

    F(a,b)=(a+2 floor(b/20), b+3 floor(a/30)),

and equality at ANY nonnegative time, including zero. A survivor means
nonequality at every such time. Extending F temporarily to Z² with
Euclidean floors does not enlarge the final official domain. Every
backward or merger transfer used below separately proves positivity,
product>=600, the strip and its own nonequality at time zero.

## 1. Q1: full ordinary lattice fibers, with all converse steps

Write a=30l+r,b=20k+s with l,k∈Z, 0<=r<=29,0<=s<=19. This remains
valid at negative inputs. Then F(a,b)=k(2,20)+l(30,3)+(r,s). Put
v=(2,20),w=(30,3). I checked all four lattice identities directly:

    (594,0)=−3v+20w,       (−386,1)=2v−13w,
    v=13(594,0)+20(−386,1),
    w=2(594,0)+3(−386,1).

They show L=Zv+Zw is precisely the kernel of Γ(A,B)=A+386B mod594.
For if Γ(A,B)=0, A+386B=594m yields (A,B)=m(594,0)+B(−386,1).
The converse is immediate. Γ is onto, so there are exactly594 classes;
det(v,w)=−594 gives unique k,l for any fixed remainder pair.

For two remainder pairs with difference (dr,ds)=hv+jw, inversion gives
h=(30ds−3dr)/594,j=(20dr−2ds)/594. The digit bounds imply
|h|<=657/594<2 and |j|<=618/594<2. The four nonzero axial choices
give |ds|20 or |dr|30; the two same-sign diagonal choices give32,23;
all are outside the rectangle. The zero choice is equality. The only
nonzero possibilities are the two orientations of (28,−17)=w−v.
Thus the coincident pairs are EXACTLY

    (r,s),(r+28,s−17), r∈{0,1},s∈{17,18,19}.

There are six disjoint pairs. Three distinct members of a class would
require a first-coordinate separation56, impossible in0..29. Therefore
the600 digit pairs occupy600−6=594 classes, ALL quotient classes.
For every output choose a digit pair in its class; the residual vector
lies in L and its unique integer k,l constructs an actual ordinary
preimage. There are exactly one or two such inputs, not merely real
inverse candidates. The six double-output classes are
{28,29,206,207,414,415}; for example386·17,18,19 have residues28,414,206.

Changing to the paired digit requires k↦k+1,l↦l−1, so the actual
partner of an input in R_L is (a−2,b+3), and the reverse applies in R_H:

    R_L: a mod30∈{0,1},   b mod20∈{17,18,19};
    R_H: a mod30∈{28,29}, b mod20∈{0,1,2}.

These are disjoint and exhaustive double-input rectangles. Partner
differences change by−5/+5 and sums by+1/−1. This describes the
next-output fiber F^−1(F(a,b)), not generally F^−1(a,b).

Direct elimination also gives

    99a=100A−10B−r+10s,
    99b=100B−10A−s+10r.

The resulting closed interval for a has width219/99=73/33<3, hence
at most three integer candidates. Recovering b=B−3 floor(a/30) and
checking the first update would find the entire fiber; no such procedure
was executed. The fiber size theorem, not that interval alone, proves
the final one/two classification.

## 2. Q2: diagonal singleton images and the time-zero obstruction

At a diagonal input the two remainders agree modulo10. Neither R_L
nor R_H permits that agreement, so no diagonal input has a partner.
For EVERY integer t, F^−1(F(t,t))={(t,t)}. Together with surjectivity,
this proves BOTH directions of

    F(Z²\Delta)=Z²\F(Delta).

An output in F(Delta) has only its diagonal parent; an output outside
that image has at least one parent and none can be diagonal. This does
not say Delta is forward invariant. Nor may a single off-diagonal
starting state be assumed to have a never-hit past.

For t=60k+u,0<=u<=59, direct floor translation gives the common66k
part and the following four exact rows:

|u|Output beyond(66k,66k)|Difference|
|---|---|---|
|0..19|(u,u)|0|
|20..29|(u+2,u)|2|
|30..39|(u+2,u+3)|−1|
|40..59|(u+4,u+3)|1|

The three off-diagonal rows give40 distinct rays modulo the common
(66,66) translation. Within a row the B residues are distinct, and
different rows have different differences. For a positive output,
t>0 since t<=0 would make both outputs<=t, hence k>=0. Official
product restrictions are on the output used as a start, not on an
arbitrary small diagonal parent. For k>=1, (66k+22,66k+20) is an actual
legal start with its UNIQUE parent (60k+20,60k+20), already diagonal.
This is an inverse obstruction, not a future-survival counterexample.

## 3. Q3 and Q4: actual positive central parents and first seed equivalence

At B>=36,D=A−B∈I the inverse formula gives for EVERY ordinary parent

    a>=(90B+100D−29)/99>=1911/99>19,
    b>=(90B−10D−19)/99>=2991/99>30.

The two worst cases use D−13 and D23 separately, which is legitimate
for independent bounds. Integrality gives a>=20,b>=31,ab>=620. Thus
ordinary surjectivity is converted into actual official positive parents
by inequalities, rather than presumed to have that consequence. Their
floors are nonnegative, so a<=A,b<=B and A−a>=2; the sum strictly drops.

The exact difference identity is

    10D=9d+r−s,
    ceil((10D−29)/9)<=d<=floor((10D+19)/9).

For D∈[−9,19], this forces d∈[−13,23]. If Y lies outside F(Delta),
ALL parents are off-diagonal by Q2. Each therefore transfers an entire
never-hit future, including its own time zero, and stays in the official
strip. The range is material: (60k+30,60k+4) maps to(66k+30,66k+7),
whose differences are26 and23. Remainders0,4 make its parent unique;
both points are official for k>=1. Full-strip inverse invariance is false.

Let E_I be official survivors already in I. By attributed eventual
entry and forward nondecrease of positive coordinates, official E is
nonempty iff E_I is. A minimum-sum member of E_I, if it exists, cannot
have B>=36, central D and be outside F(Delta), since Q3 would produce
a smaller member. Thus it belongs to Bset: the finite B<=35 patch,
the eight outer offsets or the40 off-diagonal diagonal-image rays.
Conversely Bset consists of official starts. This proves both universal
hitting directions in Q4. The finite patch has A<=58,B<=35 with all
filters retained; unions need not be disjoint. Iterated descent is finite
by the positive integer sum. No residual future is decided.

## 4. Q5: a single integer rank for central parents and critical mergers

The five centers (0,−4,−3,−2,4) have respectively residues0,1,2,3,4
modulo5. Hence h(d)=|d−c_(d mod5)|/5 is an ordinary nonnegative
integer even at negative d, and Phi(a,b)=a+b+2h(a−b) is a positive
integer on official starts. The optional h<=5 on I follows by checking
the residue-specific endpoints; it is not needed in the strict proof.
For |d−D|<=4 the triangle inequality and center spread8 give
|h(d)−h(D)|<=12/5, and integer heights improve this to<=2.

At a Q3 central output, d−D=(D−r+s)/9. The numerator is in[−38,38],
so the integral change has absolute value<=4. For B>=43 the parent
has a>=30: if a<=29, then b=B and d<=29−43=−14, contrary to d∈I.
Together with b>=31, this gives sum drop at least2+3=5. Thus EVERY
such parent has Phi at least1 smaller. B36 alone cannot replace B43:
(25,36)→(27,36) has Phi67→65; (29,40)→(33,40) has Phi75→75.
Both are actual official points. No optimal cutoff is asserted.

Critical starts have the eight outer differences or lie in F(Delta)
off the diagonal, giving eleven possible differences in total. R_L
forces D mod10∈{1,2,3,4}; R_H forces{6,7,8,9}. Intersecting these
sets with the eleven actual critical differences gives exactly:

|Rectangle|D|Partner D|h before→after|Phi change|
|---|---|---|---|---|
|R_L|1,2|−4,−3|1→0|−1|
|R_L|21,22,23|16,17,18|5→4|−1|
|R_H|−13,−12|−8,−7|2→1|−3|
|R_H|−11|−6|3→2|−3|
|R_H|−1|4|1→0|−3|

Each partner uses the same residue center and is nonzero in I. The
sum changes+1 in R_L,−1 in R_H, and the twice-height changes−2.
All partners are official: since A>=30,B>=43, coordinates are bounded
below by(28,46) or(32,40), with products1288 or1280. Since next outputs
agree and the new start is off-diagonal, survival transfers completely.
There is no double critical point at difference20 or−10.

I checked both unbounded identities in v2 directly. The birth
Yj=(660j+239,660j+240),j>=0 has its unique diagonal parent600j+219,
yet the partner Zj=(660j+241,660j+237) has the same next output
(726j+263,726j+261) and Phi3 smaller. Incoming and next-output fibers
must not be interchanged. For D2 in R_L, congruences force B60m+58
or60m+59; the next pair is respectively(66m+64,66m+64) or
(66m+65,66m+65). Positive official inputs require m>=0. This entire
specific subfamily hits in one step, with no extension to all births.

## 5. Q6: refined singleton-next-output seeds

Sstar has the official off-diagonal strip filters, the B<=42 finite
patch, and above it only critical points outside R_L∪R_H. The finite
patch has A<=65,B<=42. At a hypothetical minimum-Phi member of E_I,
a noncritical high point has a smaller central parent. A critical
double input has a smaller same-output partner. The only remaining
minimums are precisely in Sstar. Inclusion proves the other universal
direction. The selected-move version terminates finitely because each
move transfers an actual survivor and decreases a positive integer.
It need not be a single backward trajectory and does not use compactness.

Sstar remains unbounded. The birth family(660j+682,660j+680) has unique
diagonal incoming parent and singleton NEXT-output fiber; the offsets
20 and−10 are not double inputs at all. No future hit follows merely
from removing a point as a possible minimum. Phi is not a forward
Lyapunov: large difference1 examples increase it forward, while the
displayed low examples can decrease it. Q1 also implies F^n(Z²)=Z²
for every finite n, with exact full-image/output-box density ratio1;
this says nothing about images of a fixed finite starting box or the
official survivor density.

## 6. Q7: all available strip parents and the complete orphan iff

For B>=43 and ANY D∈I, d−D=(D−r+s)/9 now has numerator in[−42,42].
Integrality still gives |d−D|<=4. If an actual parent has d∈I, the same
a>=30 argument and sum drop prove Phi(parent)<=Phi(Y)−1. Positivity
of ALL ordinary parents already follows from Q3's full-I intermediate
bounds. The extended rank estimate does not assert an inside parent
exists. If Y is outside F(Delta), an inside parent is off-diagonal;
a birth instead has only its diagonal parent.

An orphan means NO parent in the strip, not no ordinary parent. Q1
guarantees some ordinary parent, and the inverse ceilings over I confine
its difference to[−17,27]. At a central output, some parent must be in
I; therefore only the eight outer differences can be orphan outputs.
An orphan's parents all have differences in K={−17,…,−14,24,…,27}.
Two parents have difference separation5, impossible within a component
of diameter3 or across the gap of at least38. Thus every large orphan
has exactly ONE ordinary parent, official but outside I.

For each outside parent difference d and output D define
u=d−D, δ=10D−9d, e∈{0,1} congruent to u mod2. The exact floor
equations give

    r=s+δ, 3l−2k=u,
    l=2z+e, k=3z+(3e−u)/2,
    B=66z+33e−10u+s,
    max(0,−δ)<=s<=min(19,29−δ).

The converse is important: every such s and integer z gives valid
Euclidean digits r,s, integer l,k, an input difference d and output
(B+D,B), not just a matching difference. For a specified B in its
displayed residue class z is an ordinary integer. Negative u uses
e0 or1, not a negative remainder. Q3 then gives official positivity.

The accompanying hand-check file derives ALL twenty pairs from these
equations with unreduced base33e−10u, including every wrapped negative
interval. Their outside-parent residue sets reproduce the full table.
Only TWO have an additional inside parent. For D20 the inverse interval
is19..24; the outside d24 digits are(0,16),(1,17),(2,18),(3,19).
Exactly(1,17) is in R_L, giving the inside partner d19 and B43mod66.
For D−10 the inverse interval is−14..−9; outside d−14 gives
(26,0),(27,1),(28,2),(29,3). Exactly(28,2) is in R_H, giving d−9
and B42mod66. All other outer inverse intervals have diameter4, so
a pair with separation5 is impossible. Delete precisely those two
residues. This proves BOTH directions of the orphan iff.

The final T_D sets have sizes3,19,41,59 on each side, totaling244
mod66 rays BEFORE the current-input mod60 rectangle exclusion. The40
birth rays have different output differences and are disjoint from
these orphan rays. This is not an actual seed count after mixing the
two periods, positivity or product filters. A common period could be660,
but no count in that larger period is needed or asserted.

## 7. Q8: actual refined equivalence and strict unbounded restriction

Sdagger retains the same finite official off-diagonal B<=42 patch.
For B>=43 it retains only births or the exact orphan-table points,
in both cases outside R_L and R_H. Every such point is critical, so
Sdagger⊂Sstar. If E_I is nonempty, choose an actual minimum-Phi
survivor. Unless it is a birth, any inside parent is off-diagonal and
contradicts minimum rank by Q7. Thus it is a birth or an orphan. If it
belongs to either double-input rectangle, Q5 supplies a lower official
strip survivor. Hence it lies in Sdagger. Together with inclusion this
proves the universal hitting equivalence in both directions. The finite
selected-move formulation exhausts the same cases and drops Phi>=1.

The inclusion is STRICT on an actual unbounded family. For k>=1,
Y=(660k+23,660k) is a legal outer-offset point in Sstar, outside both
rectangles. Its parent X=(600k+23,600k) is also in I and official,
F(X)=Y and Phi(Y)−Phi(X)=120k. It is not an orphan or birth, equivalently
B0mod66 is absent from T_23, so Y∉Sdagger. No future hit or survival
of either point is asserted.

Both remaining source mechanisms are nonempty in unbounded actual
families. The displayed birth(660j+682,660j+680),j>=0 has a unique
DIAGONAL incoming parent and singleton next-output fiber. The orphan
Yj=(660j+30,660j+7),j>=1 has its unique parent(600j+30,600j+4) outside
I, B7mod66∈T_23, and current digits0,7 outside the next-output
rectangles. Positivity/product and the restriction j>=1 are material.
Neither family has its future decided. There is no ordinary infinite
survivor obtained from changing finite or compact shadows.

## 8. Primary-source and failed-import boundaries

The original official domain and organizer statement were freshly checked.
The three newly mentioned dynamical papers were inspected in their actual
operative sections, as specified in the source checks. BRW concerns
integer toral matrices and finite rational lattices; Guiheneuf uses
nearest-lattice discretizations and generic bounded SLn sequences;
Guiheneuf–Joly uses generic orthogonal sequences and permits perturbations.
Our fixed floor map has linear determinant99/100, not1. No eligible
genericity, rounding conjugacy or determinant-preserving reduction was
proved. Neither their density conclusions nor local collisions settle
every ordinary orbit. No external proof is claimed fully reconstructed.

The failed quadratic-rank estimates, the B36/B40 counterexamples,
the two ordinary predecessor obstructions, the source normalization
distinction and the unbounded families are preserved accurately. The
old F5 ninefold fiber is at C; R7's conditional tenfold fiber is at10C.
Neither supplies a no-tenfold theorem. AFS's at-most-two hypothesis
fails at11/10; generic normality, finite shadows, real interval images
and density-one do not supply ordinary existence or termination.

All new mathematics was hand reconstructed, including the finite twenty
intervals essential to the exact iff. No scan, mathematical code, CAS,
author replay or orbit sample was used. Administrative SHA/JSON and
literal-suffix checks establish only integrity. The complete100-row
ledger contains zero substantive issues or required repairs. Five
closed notes preserve inverse versus next-output/time-zero semantics,
the B43 rank threshold, the two orphan exceptions, the pre-filter ray
count and the remaining unbounded future gap. Only root after TWO
OTHER entire whole audits may promote exact scoped claims. No annual,
finite decision, actual survivor or novelty conclusion is recommended.
