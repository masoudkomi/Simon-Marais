# Actual residual sets and coinvariant fibers: complete blind WHOLE R2

2026-10-17 UTC. Reviewer `/root/review_2022_complexity_r2`.
Requested gpt-6.1-sol/max; independent effective-setting readback is
unavailable. **Complete initially blind NONCONSTRUCTOR whole audit;
not coordinator promotion.**

I find no substantive scoped defect in R6A–R6D. All54 obligations are
covered by65 inference checks, including the exact overlap correction,
the individual fixed-group step needed for Baer freeness, the actual
residual-plane/reset argument, relative-unit and order-four exceptions,
the strict faithfulness cutoff and the character-bound extra fixed point.
The arguments give necessary restrictions in their stated actual-set
domains. They do not solve the residual incidence/phase problem or
the official unrestricted taut classification.

No mathematical code, scan, CAS, certificate, source algorithm or
constructor program was run. The only executable verification is
metadata preservation after the full mathematical report is complete.

## 1. Independence, complete target and accepted dependencies

C (`/root/review_2017_coarsening_r1`) constructed this NEW2020R6
packet. I did not construct it or supply a proof step. I authored
the older R4 and its final-moment repair and the older R5 packet.
Those roles are disclosed and excluded from any supposed fresh
independent recertification of my own work. They had been accepted
after TWO OTHER whole audits and coordinator reconciliation before
this new review. C's older R3 authorship is likewise disclosed;
accepted R3 is a premise, not a fresh self-certification by C.

The current reviewer prepared from the official statement and exact
accepted bodies/sources while R6 was inflight, without opening the
new notes. The complete frozen target was first opened after root
supplied its exact hash. No NEW2020R6 peer report, ledger, source
check or finding was read before this ENTIRE initial freeze. Root's
notice that its own initial had frozen contained no mathematical
finding; the noticed manifest and companions were left unopened.

Exact main: `notes/reasoning-return-r6-candidate-v1.md`,19423bytes,
SHA256 `1c71e9225a8e7881a4a640cd420c4cac55d86ddd09f8538fabe7cb630099f24c`.
Exact freeze: `notes/reasoning-return-r6-freeze-v1.json`,3821bytes,
SHA256 `d0f3c1f2697af5198971034696c77cac542d3553bc429aab31c1ce7428605f29`.
Paths here are relative to `problems/2020-B4/` unless specified.
I read the complete main,54-obligation list, constructor checks,
failed routes, source audit/JSON and worklog, the full metadata-only
constructor freezer as TEXT, and the validation schema/declared
records. The constructor freezer was not executed. Its nine frozen
artifact hashes are checked by the separate reviewer metadata record.

The COMPLETE accepted mathematical inputs were freshly read, including
their headers and linked bodies:

- `proofs/reviewed-partial-v1.1.md` and `proofs/partial-v1.md`;
- `proofs/reviewed-return-r3-v1.2.md`;
- `proofs/reviewed-reasoning-return-r4-v1.2.md`;
- `proofs/reviewed-reasoning-return-r5-v1.1.md`.

Their exact acceptance scopes, source clarification and repair history
were checked. In particular, R4's final moment remains automatic and
its interior list sufficient for its prescribed actual subgroup shapes.
No old error is reinstated. The old common/individual fixed-group
counterexample stays visible. The separate quadratic-character matrix
lead is unverified context, not an R6 premise; no theorem is extracted
from it here. Actual source scopes are in the separate source report.

## 2. Official domain, one normalization and actual intersections

The official open question is ONLY2020B4(b), which asks precisely
which integers n>=2 are taut. The initial dictionary sets

    q=n-1, k=q+1, v=q²+q+1, G=Z/vZ.

New statements use q>=2. The accepted n=2,q=1 boundary is retained
outside them. D is an ACTUAL k-element subset, with distinct points
and one ordered representation of every nonzero group element.
It is not a quotient vector, signed group-ring relaxation or Gram
matrix. No proof or construction of preliminary part(a) is reproduced.

Since gcd(k,v)=1, a unique translate has sum zero. If tD=D+c,
summing in that frame gives kc=0, hence c=0. Thus every numerical
multiplier fixes this ONE chosen D setwise. M is the full group;
T and U can be proper subgroups. All are abelian subgroups of the
unit group, with identity understood modulo v. A setwise action is
not pointwise fixedness.

For a nonidentity U, accepted F1 supplies the ACTUAL fixed intersection
E=D intersect H, H=G^U. H is proper. If h=1, E has size0 or1.
If h>1, its ordered differences exhaust H minus zero, so

    f=m+1, h=m²+m+1, 1<=m<=sqrt(q), m<q.

The order-one subdifference-set boundary m=1 is allowed; it is not
a nondegenerate subplane. The proper-subplane bound for m>=2 and
its trivial m=1 extension are already explicit in accepted F1.
The prime-divisor multiplier theorem and Cohen unit theorem remain
attributed accepted external imports, with hypotheses checked below.

## 3. R6A: exact cyclic coinvariants and energy

Let h=gcd(v,u-1 for generators of U). In the cyclic group, the
simultaneous annihilator has size h and is H=(v/h)G. The subgroup
generated by all images (u-1)G is A=hG, of order b=v/h.
The generator description suffices because products satisfy
uw-1=(u-1)w+(w-1), and inverses preserve the generated ideal.
No averaging by the group order or coprime splitting is required.

The intersection of the unique subgroups of orders h and b has
size c=gcd(h,b). Keeping c is necessary when v has repeated factors.
Every U-orbit stays in one G/A fiber, because ux-x lies in A.
Define g_y and w_y as the actual fixed and nonfixed D-point counts
in that fiber. Counting distinct ordered pairs with difference in A
gives

    sum_y(g_y+w_y)(g_y+w_y-1)=b-1.

For E, the same count is c-1: its differences exhaust H minus zero
and the ones lying in A are exactly the nonzero elements of H intersect A.
When h=1, g has at most one point in total and both sides are zero.
Subtracting, including both ordered cross directions, proves EXACTLY

    b-c=sum_y[w_y(w_y-1)+2g_yw_y].

Let rho be the smallest prime factor of abs(U). Any nonfixed orbit
has length a divisor of abs(U) greater than one, hence at least rho.
The w_y are unions of these whole orbits. Thus either w_y=0 or
w_y>=rho, giving

    b-c>=(rho-1)sum_y w_y=(rho-1)(k-f).

Only when h>1 may k-f be replaced by q-m. Multiplying by h and
using v-h=(q-m)(q+m+1) gives

    (q-m)[q+m+1-(rho-1)h]>=(c-1)h.

Here q-m>0, so the bracket is nonnegative and is positive if c>1.
This establishes both A4 and A5 without discarding overlap or using
a sign division at zero.

For U generated by one PRIME-order t of order ell, every nonfixed
orbit has length ell even if ell divides v. Write w_y=ell*a_y.
Subtracting (ell-1)sum w_y from the exact energy yields

    b-c-(ell-1)(k-f)
      =ell² sum_y a_y(a_y-1)+2ell sum_y g_y a_y.

Both sums are nonnegative integers. Equality holds exactly when
each a_y is0 or1 and no occupied nonfixed fiber contains a fixed
D-point. Since each active orbit has length ell, that says exactly
one orbit per active fiber. The fixed intersection here is that of
<t> itself; an unrelated common fixed subgroup is never substituted.

Overlap c>1 can occur for an ACTUAL example, not merely an abstract
cyclic group. Use attributed known Singer existence at q=128=2^7,
v=16513=49*337 in the common sum-zero frame. Hall makes8 a
multiplier; 8^7-1=2^21-1=127*16513 and8!=1 show that
U=<8> has prime order7. Then h=gcd(7,16513)=7,
b=2359=7*337 and c=7. Accepted F1 gives E of size3 and
its six ordered nonzero differences lie in H intersect A=H.
Thus the exact energy subtracts6 from b-1, giving b-c=2352.
Silently replacing c by1 would lose those six pairs. This hand
diagnostic also exhibits abs(U) sharing a factor with v; no averaging
or explicit construction of the known example was used.

An actual retained check against the rejected freeness shortcut is
the accepted q=4 set D={7,9,14,15,18} modulo21 with U=<2> of
order6. Its orbit lengths are2 and3, common fixed group is{0},
and E is empty. Here b-c=20 and k-f=5, so replacing rho by
abs(U) would assert20>=25, falsely. The submitted A3 instead uses
rho=2. This is a counterexample to the REJECTED shortcut, not R6A.

The Arasu/Gordon method is properly attributed as earlier within-orbit
difference counting. Gordon's direct-product theorem has extra coprime
factor and specified-power hypotheses. R6A proves its own cyclic
coinvariant identity; it does not import that theorem more broadly.

## 4. R6B: common Baer fixed subgroup forces a numerical involution

Assume q=m², m>=2, and G^U has order m²+m+1. For EVERY
nonidentity u in U, its OWN fixed subgroup contains H. F1 bounds
its actual smaller order m_u by m, whereas containment forces
m_u>=m. Hence each of these individual fixed subgroups equals H.
A point outside H therefore has no nonidentity stabilizer in U:
the U-action there is genuinely free. The inference would fail if
only the common fixed set were known; the proof supplies the stronger
individual equality first.

The factorization of v gives b=m²-m+1. The two factors are odd;
a common divisor divides2m and is coprime to m, so c=1. Also
k-f=m²-m=q-m=b-1>0. Applying the justified orbit lower bound
abs(U) to A3 gives

    q-m>=(abs(U)-1)(q-m),

so abs(U)<=2. Nonidentity forces exactly two elements; accepted F2
identifies the nonidentity multiplier as m³ modulo v. q=4,m=2
is allowed here. No Cohen input or q!=4 exception is needed for
R6B. This is a conclusion for numerical multiplier subgroups of an
actual cyclic planar set, not arbitrary pointwise Baer collineations.

## 5. R6C1: actual residual and every smaller-group reset

Assume q!=4. Cohen supplies a unit d in the ACTUAL sum-zero D.
For any known T<=M of size s, O=dT has exactly s points by unit
cancellation. O and R=D minus O are T-invariant. Write r=k-s
and let K be the pointwise action kernel on R.

If r>=2 and K is nonidentity, every point of R lies in H=G^K.
No point of O does: a nonidentity multiplier cannot fix a unit.
Since D is precisely the disjoint union O and R, this proves

    R=D intersect H,
    h=r²-r+1, m=r-1>=1, q>=(r-1)².

It is this equality, rather than an occupancy inequality, that makes
the residual an ACTUAL smaller difference set. H is proper and
cannot have size1 in this r>=2 case.

Abelianness makes T preserve H. The restriction kernel consists
exactly of K: fixing H fixes R; conversely, fixing every R-point
fixes every difference from R, and those exhaust H minus zero.
The image has size a=abs(T/K) and consists of actual numerical
automorphisms fixing R in its own cyclic group H. These are units
relative to H's order. A generator of H identifies its coordinates;
ambient normalization is not silently assumed to be its own sum-zero
normalization. Numerical multiplier groups are unchanged by translating
the difference set, so the classical bound can be reset when needed.

The bound a<=A_r has three correctly separated domains:

- At r=2, H has order3 and Aut(H) has size2. This direct argument
  avoids Cohen's nontriviality convention for the order-one set.
- At r>=3,r!=5, the smaller order is m=r-1>=2,m!=4, so the
  accepted classical bound gives a<=m+1=r.
- At r=5, H has order21. If this actual R has a RELATIVE unit,
  its orbit under the setwise image has a points, giving a<=5.
  This relative unit need not be a unit in the ambient group.
  Otherwise Cohen's exact literal exceptions apply and a<=6.

For the last clause, E1={3,6,7,12,14} has additive-order-three
pair{7,14}, preserved by both units modulo3. Its order-seven triple
is3{1,2,4}, whose multiplier stabilizer modulo7 is exactly the
three-element subgroup{1,2,4}. CRT combines these independent
conditions into precisely2*3=6 units modulo21. E2=-E1 has the
same stabilizer. No equivalence-class or arbitrary-translation claim
is substituted for Cohen's literal theorem, and no subset scan is used.

## 6. R6C2: exact kernel inequality and the cutoff

For U=K the only D-points outside its fixed subgroup H are O.
Every K-orbit on O is free because its points are units; the orbit
length is abs(K)=s/a. Therefore A3, or its exact-energy derivation,
gives

    v/h-c>=(s/a-1)s.

As c>=1 and a<=A_r, the valid replacement direction is

    (v-h)/h >= s²/a-s >= s²/A_r-s.

With q=s+r-1 and h=r²-r+1, direct expansion gives
v-h=s(s+2r-1). Here s>0, so cancellation is legitimate.
Also h>A_r: for r!=5, h-r=(r-1)²>0; at r=5,
h-A_r=21-6=15. Rearranging proves

    s<=A_r(h+2r-1)/(h-A_r)
      =r²(r+1)/(r-1)²   for r!=5,
      =12               for r=5.

For r>=6 the first upper bound is at most2r because
r²-5r+2>0. But the actual proper-subplane bound gives
s=q+1-r>=(r-1)(r-2)>2r, with the last inequality supplied
by the SAME positive quadratic. This is a genuine contradiction.
For r=2,3,4 the respective upper bounds are12,9,80/9; r=5
gives12. Thus nonidentity K with r>=2 forces2<=r<=5 and s<=12.
No existence classification for the surviving small inequalities follows.

## 7. R6C3–C4: faithful abelian actions and the actual sharp endpoint

If s>12 and r>=2, K is therefore trivial. On each residual T-orbit
of size r_i, abelianness makes the point stabilizer T_i the same
at every point and normal. Its quotient has size r_i. Faithfulness
means the intersection of all T_i is trivial, so the diagonal map

    T -> product_i T/T_i

is injective. Hence s divides product_i r_i. A fixed point contributes
a factor1 and causes no exception. The integer inequality
u<=3^(u/3) holds at1,2,3; for u>=3, the successive ratio
(u+1)/u is at most4/3<3^(1/3). Multiplication yields

    s<=product_i r_i<=3^(r/3), hence r>=3log_3 s.

This is for ANY actual known subgroup T, including proper ones,
and ANY chosen unit orbit as specified. r=0 or1 is excluded from
the faithfulness step and belongs to the already accepted extra
saturated case s>=q. Neither r small nor saturation is forced in
general. The rejected bound s<=r is not used: for example the
abstract C3 x C3 quotient actions on two disjoint three-point orbits
are faithful of degree6 and order9. This is an abstract-action
counterexample to that shortcut, not a realized difference set.

The strict s>12 cutoff for FAITHFULNESS is challenged by the known
ACTUAL classical order16 example, using attributed Singer existence
only. Here v=273 and Hall gives T=<2>. Since2^12-1=15*273,
its order divides12; every proper divisor is at most6 and
0<2^d-1<=63<273, so the order is exactly12. Cohen supplies a
unit d; its orbit has size12 and the residual has size5.

The nonidentity involution64=2^6 has fixed subgroup of size
gcd(63,273)=21. Accepted F1 makes its fixed D-intersection size5.
It is disjoint from the unit orbit, so it exhausts R. Thus64 lies
in K and this actual residual action is nonfaithful. No assertion
that the full multiplier group equals T is needed, and no explicit
preliminary construction is given. The example refutes extension
of faithfulness to s=12; it does not assert that the logarithmic
inequality itself fails at12.

## 8. R6D: nonsquare q=1 modulo3, exact fixed pair and DFT bound

Assume q is nonsquare and q=1 mod3; then q>=7. Accepted F2
implies there is no numerical involution. A finite group of even
order would contain one, so abs(M) is odd. Its reduction modulo3
is a subgroup of the two-element unit group and is therefore trivial:
every multiplier is1 modulo3. Hence G^M contains the size-three
subgroup of G.

Hall gives q in M. The congruence q³=1 modulo v follows from
q³-1=(q-1)v, while q!=1 and q²!=1 modulo v by their actual
integer sizes. Its OWN fixed subgroup has size
gcd(q-1,v)=gcd(q-1,3)=3. Since q belongs to M, G^M is
contained in this subgroup; the preceding containment gives equality.
This establishes the common/individual equality BEFORE using it.

Put b=v/3 and H={0,b,2b}. F1 gives exactly two points of D
in H. The nonfixed q-orbits have length3 and sum
x(1+q+q²)=0 in G. The common ambient sum-zero condition then
forces the two fixed D-points to sum zero, so they are exactly
E={b,2b}. Writing q=3t+1 gives b=3t²+3t+1=1 modulo3.
Thus E supplies one actual point in each NONZERO residue class
modulo3. b>1 makes both points nonunits in the ambient group.

Cohen supplies a unit d in D; its full M-orbit has s=abs(M)
points. Because every multiplier is1 modulo3, that orbit lies
in a single nonzero residue class. It is disjoint from E, so that
same class has actual occupancy n_i>=s+1, not merely n_i>=s.

For a primitive cube root omega, accepted character magnitude gives
Z=sum_i n_i omega^i with abs(Z)=sqrt(q). Using the real occupancies,

    3n_i=k+2Re(Z omega^(-i))<=q+1+2sqrt(q).

Combining proves3s<=q-2+2sqrt(q). Every known T has order at
most abs(M), so the same bound holds for its size; alternatively use
its shorter unit orbit and the same fixed point. The DFT equation
uses a nonprincipal character because3 divides v; no relaxation
is reversed to construct D or classify an order.

## 9. Actual examples, source boundaries and the remaining gap

The known classical q=5 example really disproves universal S0.
Its point count31 is prime, so accepted R5B applies to this ACTUAL
classical plane and gives M=<5>, of order3 since5³=1 modulo31
and5!=1. Thus every known T has size at most3<5. This is not
the earlier invalid attempt to use a nonexistent parameter record
as an actual example. No cyclic-implies-classical inference occurs.

Accepted R5's even saturated q>8 branch retains its precise
existence equivalence with an ACTUAL non-Desarguesian flag-transitive
plane, using Xia's attributed reverse reduction. Its odd affine
two-orbit subgroup supplies no flag-transitivity premise for the
full automorphism group. These statements locate a separate open
obstruction; they neither contradict existence nor cover arbitrary
nonsaturated planes. No stronger Kantor restatement is used to
eliminate the odd branch.

At prime v, every nonidentity numerical multiplier fixes only zero.
The energy identity remains valid, but supplies no nontrivial smaller
fixed plane. Faithfulness can leave many residual points, and its
product bound permits large residuals. Actual differences and character
phases remain uncontrolled. Necessary occupancy, orbit or matrix
conditions are not promoted to realizability or annual classification.

Primary source statements were inspected directly. Cohen's full sieve
and exceptional-parameter proof is an attributed import, not newly
reconstructed. Gordon's coprime direct-product method is attribution
only for R6A; the new energy proof is complete. BBB's applicable
involution/trace setup and written lemmas were checked, without
importing its later unital theorem. Singer existence is attributed
from the official discussion and Huang–Schmidt introduction. Xia's
exact extra flag hypotheses were retained. Full CFSG, uniqueness
searches and large published computations were not re-audited or run.

## 10. Disposition, integrity and continuation boundary

All four claims, their endpoints, all54 constructor obligations and
the failed-route limits have been reconstructed. No substantive
issue requiring author repair was identified. Source/read limitations
and old author roles are explicit; this is not self-review of R4/R5.
The65-check ledger includes actual overlap and nonfreeness challenges
and the actual threshold endpoint.

Only NEW `reviews/reasoning-return-r6-review-2-*` files are written.
All old candidates, repairs, reports, source notes, shared files,
Git and other owners' artifacts are preserved. The separate metadata
freeze records exact inputs, accepted scopes and the older own
inventory; metadata equality is not mathematical evidence. Requested
settings remain distinct from unavailable effective readback.

No NEW peer R6 findings were read through completion of the whole
initial report, ledger, source record, validation and manifest. Root
alone may reconcile both whole audits and promote the exact scoped
result. No unrestricted saturation, prime-power proof, numerical
answer, improved verification cutoff, novelty or external validation
is claimed by this audit.
