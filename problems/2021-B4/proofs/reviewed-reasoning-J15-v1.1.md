# Reviewed J15 double-zero restrictions, v1.1

**Proved, independently reviewed (partial results D1–D5 and the stated
low-order family).** Accepted by the coordinator on 2026-10-16 UTC after
two fresh initially blind whole analytic reconstructions and reading both
full reports and issue ledgers. No substantive repair was requested.
The frozen constructor body below is preserved exactly; its historical
candidate wording is superseded by this scoped acceptance. Neither a full
J15 mask nor degree 20 is excluded. The explicit nonunit branch, other
center patterns and lower J remain unresolved. No novelty is claimed.
See ../reviews/reasoning-J15-acceptance.md/json for scope and fingerprints.

---

# J=15, multiplicity two: small-root splitting and a collision obstruction

2026-10-16 UTC. **Candidate proof - unverified.** Constructor: research
worker `owner_2021_reasoning_j15`. Requested model/reasoning: gpt-6.1-sol /
max, as conveyed in the assignment; effective settings could not be read
back. Two fresh independent adversarial reviewers are required before any
deduction is accepted. No full J=15 exclusion, degree-20 solution, annual
classification, or novelty is claimed.

This note treats **multiplicity two at zero**, not the coordinator's
separate triple-root candidate. It derives analytic restrictions; no mask
enumeration or higher-digit search is a proof dependency. The published
and already reviewed inputs below are separated from the new argument.

## Exact scope and accepted inputs

The contest hypothesis is a polynomial over Q, with a **rational** common
root for each nonconstant derivative. Its other roots may be nonrational
and nonreal. Use the accepted normalization

    f(X) = X^20 - 20 X^19 + sum_(j=2)^18 binom(20,j) a_j X^(20-j),
    a_j in Z_(19),  f(0)=f'(0)=f(1)=0.

Here 1 is simple, H_k denotes the Hasse derivative of order k, and
J=max{j : v_19(a_j)=0}. Assume J=15 and ord_0(f)=2. Accepted T1 requires
at least four distinct rational roots to cover the derivatives. The
accepted Newton theorem accounts for fourteen root slots of valuation
1/14, one root 1 of valuation zero, zero twice, and exactly three further
nonzero root slots of valuation greater than 1/14. Rational roots cannot
belong to the fourteen-slot cluster. Thus at least two distinct roots in
the three remaining slots are rational.

Dependencies:

- `rational-witness-p-plus-one-reviewed-v1.2.md`: normalization and the
  rational-witness distinction, with CLO and Draisma--de Jong attribution.
- `padic-rational-newton-reviewed-v1.1.md` and its frozen body: the
  fourteen-slot edge and width-one lemma. The latter says that if the
  unique minimum terms of P(u) have exponents i,i+1, with i<19, then
  H_k(P)(u) is nonzero for 1<=k<=i+1.
- `coordinator-three-rational-witnesses-reviewed-v1.1.md`, T1 and T3:
  at least four rational witness values, and zero multiplicity 2 or 3.

All p-adic valuations below have v_19(19)=1. A root repeated in the full
root multiset is counted repeatedly. Equal reduced residues are allowed.

## Proposed conclusions

**D1.** All three nonzero small root slots lie in Q_19. They need not all
lie in Q. If their values, counted with multiplicity, are u,v,w, then

    f(X)=X^2 (X-u)(X-v)(X-w) B(X),
    B(X)=(X-1)g(X),

where g is monic of degree fourteen and Eisenstein over Z_19. This is
only a factorization over Q_19; no degree-fourteen quotient over Q is
asserted. Put nu_i=v_19(u_i), all positive integers.

**D2.** If the three nu_i are not all equal, at least **two** of
H_2(f)(1), H_3(f)(1), H_4(f)(1) vanish. If all three nu_i differ, all
three center equations vanish.

**D3.** Suppose H_3(f)(1)=0 but H_2(f)(1) and H_4(f)(1) are nonzero.
Then all small-root valuations equal some integer nu>=1. There is a
unique small root r whose residue after dividing by 19^nu is R, while
the other two roots a,b both reduce to 2R, with R nonzero in F_19.
The same actual root r is a rational common witness for both H_2 and
H_4. The roots a,b may coincide, and need not individually be rational
over Q. They do lie in Q_19 by D1.

**D4.** In D3, if a_14 is a 19-adic unit, then nu is even, and

    -2 R beta_14 a_14/(beta_15 a_15)

is a nonzero square in F_19, where beta_j=binom(20,j)/19. In particular
nu=1 is impossible in this subcase. More generally the exact formula
in section 4 is a necessary square condition even when a_14 is not a
unit.

**D5.** For a canonical center mask, let a_j^0 be the normalized
derivative recursion with every noncenter witness replaced by zero,
and q_0=-1+sum_(j=2)^18 beta_j a_j^0. In the D3 subcase,

    q_0 nonzero  ==>  nu <= v_19(q_0).

Consequently a mask with only H_3 among the three low center equations,
v_19(q_0)=1, and a_14^0 nonzero modulo 19 cannot have an actual
multiplicity-two realization. This does not remove a complete J=15
mask unless its multiplicity-three realization has also been excluded.

## 1. Proof of D1 and exact low-coefficient identities

Choose two distinct rational small roots u,v. Remove one copy of each
from the small-root multiset, leaving one slot w. The absolute Galois
group of Q_19 preserves valuation, fixes u,v, and preserves the full
root multiset. It therefore fixes its one remaining small slot w.
Hence w is in Q_19. This also covers a repeated small root: if w equals
u or v, that value is already fixed. Thus all three slots lie in Q_19
and their valuations are positive integers. This proves neither that w
belongs to Q nor that it can be selected as a contest witness.

Monic division by X^2(X-1)(X-u)(X-v)(X-w) over Q_19 defines g. Its
fourteen roots are exactly the roots of valuation 1/14. Each nonleading
coefficient, as a symmetric sum of products of these roots, has positive
valuation. It lies in Q_19, so that valuation is an integer and is at
least one. The constant coefficient has valuation 14/14=1. This proves
that g is Eisenstein over Z_19.

Write B=sum b_i X^i. Then v(b_0)=1, b_i is in 19 Z_19 for 1<=i<=13,
b_14 is congruent to -1 modulo 19, and b_15=1. Let

    s_1=u+v+w, s_2=uv+uw+vw, s_3=uvw.

The exact identities, with c_i the ordinary coefficients of f, are

    c_2 = -b_0 s_3,
    c_3 =  b_0 s_2 - b_1 s_3,
    c_4 = -b_0 s_1 + b_1 s_2 - b_2 s_3,
    c_5 =  b_0 - b_1 s_1 + b_2 s_2 - b_3 s_3,
    c_6 =  b_1 - b_2 s_1 + b_3 s_2 - b_4 s_3.

For nu=min nu_i, these give

    v(c_5)=1,
    v(a_18)>=3nu, v(a_17)>=2nu, v(a_16)>=nu,
    b_1/b_0 = c_6/c_5 = beta_14 a_14/(beta_15 a_15) mod19.

The last equality is in Z_19 and is a residue identity; it does not
assert equal valuations if both numerator residues vanish. The signs
above are for **three** small factors. With two small factors and a
triple zero, the corresponding signs differ.

## 2. Proof of D2: unequal valuations force two center equations

All rescalings used here are integral after division by their leading
coefficient valuation. This follows either directly from D1's factor
form or from the relevant Newton supporting line. Hasse differentiation
commutes with rescaling and reduction. A rational witness at the center
is handled separately. Every other rational witness is zero or one of
the three small roots; allowing a non-Q small root as a possible witness
only enlarges this necessary cover.

First suppose exactly one root, say u, has the minimum valuation nu_1,
strictly below the other two. At that scale the degree-five reduction is

    F(T)=T^4(T-U), U nonzero.

H_4(F)=5T-U has value -U at 0 and 4U at U. Neither is zero in F_19.
Thus H_4 can use none of the noncenter roots and must use the center.
The outer root u is on the width-one edge with exponent endpoints 4,5;
the accepted lemma excludes it as a witness for H_2 and H_3 as well.

If the remaining roots v,w have equal valuation nu_2, divide by the
scale associated with the inner degree-four cluster. Its reduction is

    G(T)=T^2(T-V)(T-W), V,W nonzero.

At its nonzero roots the H_2 values are

    V(3V-2W), W(3W-2V),

while its value at zero is VW, nonzero. H_3 at 0,V,W has values

    -(V+W), 3V-W, 3W-V.

Therefore noncenter witnesses for both H_2 and H_3 would require W/V
in both {3/2,2/3}={11,7} and {-1,3,1/3}={18,3,13}. These sets are
disjoint in F_19. At least one of H_2,H_3 uses the center, in addition
to H_4. No distinctness of V and W was assumed.

If v and w instead have different valuations, the intermediate
degree-four reduction is T^3(T-V). Its H_3 values at 0,V are -V,3V,
both nonzero, so H_3 uses the center. The intermediate root is on the
width-one edge with endpoints 3,4, and the deepest root is on the
width-one edge with endpoints 2,3; these and the outer edge exclude
every nonzero small root as an H_2 witness. Zero is not an H_2 witness
because c_2 is nonzero. Hence H_2 uses the center too. This proves the
all-three-distinct assertion.

The remaining unequal case has two roots u,v at the minimum valuation
nu and a single deeper root w. The outer reduction is

    F(T)=T^3(T-U)(T-V), U,V nonzero.

The deeper root is on the width-one edge with endpoints 2,3 and cannot
witness H_2 or H_3. Zero cannot witness H_2. It cannot witness H_3
either: the term b_0 uv has uniquely smallest valuation in c_3.
For the outer roots, the H_2 values are

    U^2(4U-3V), V^2(4V-3U),

and the H_3 values are

    3U(2U-V), 3V(2V-U).

H_4 at the two outer roots has values 4U-V,4V-U; at zero or the deeper
root its reduced value is -(U+V). Thus a noncenter witness requires

    H_2: V/U in {4/3,3/4}={14,15};
    H_3: V/U in {2,1/2}={2,10};
    H_4: V/U in {-1,4,1/4}={18,4,5}.

These three sets are pairwise disjoint in F_19. At most one derivative
can have a noncenter witness, so at least two use the center. This
completes D2, including repeated-root and coincident-residue cases.

## 3. Proof of D3: the sole-H3 case forces a repeated residue

D2 forces equal valuations nu. Divide the three roots by 19^nu and
write their nonzero residues as U,V,W. The degree-five reduction is

    F(T)=T^2(T-U)(T-V)(T-W)
        =T^5-s T^4+t T^3-z T^2.

All three residues belong to F_19 by D1; z=UVW is nonzero. At a nonzero
root R of its cubic factor,

    H_2(F)(R)=R(9R^2-5sR+2t),
    H_3(F)(R)=10R^2-4sR+t,
    H_4(F)(R)=5R-s.

The H_2 value at zero is -z, nonzero, so its actual noncenter witness
reduces to a nonzero root.

If H_4's noncenter witness reduces to zero, then s=0. Let R be the
H_2 witness residue. Its equation gives t=-9R^2/2. The other two roots
then have sum -R, product -7R^2/2, and discriminant 15R^2. But 15 is a
nonsquare in F_19. This is impossible because the three roots split over
F_19.

Otherwise H_4 has a witness residue S nonzero and s=5S. Name the other
two residues A,B; thus A+B=4S. If H_2 uses one of them, say A, its
equation becomes

    7A^2-17SA+8S^2=0.

Its discriminant is 65S^2=8S^2 in F_19, again a nonsquare. This covers
possible equality of A and S too; no root difference was divided out.
Therefore H_2 must use S. Its equation gives t=8S^2, so A+B=4S and
AB=4S^2. Hence A=B=2S. The squares modulo 19 are

    {1,4,9,16,6,17,11,7,5};

neither 8 nor 15 is among them. No exhaustive root table is needed.

There is exactly one root slot reducing to S, and the other two reduce
to 2S, a different nonzero residue. Thus the actual H_2 and H_4 witnesses
must coincide at that unique root r. It is rational over Q because the
contest witnesses are rational. This proves D3. In this pattern H_3's
values at 0,S,2S are 8S^2,-2S^2,8S^2, respectively, so its center
equation is also consistent with the necessary reduction.

## 4. Proof of D4: an exact discriminant formula

Keep r,a,b from D3. Put q=19^nu and R=r/q modulo 19, and define

    A=a/r, B=b/r,
    C(T)=B_res(rT)/B_res(r),
    c_k=H_k(C)(1)=r^k H_k(B_res)(r)/B_res(r),

where B_res is the polynomial called B in D1. A,B here are scalar root
ratios; this temporary notation distinguishes them from B_res. They
belong to Q_19, reduce to 2, and may be equal.

For k=1,2,3 the numerator H_k(B_res)(r) is in 19 Z_19. Indeed its
terms of exponent i<=13 have a factor 19, and its i=14,15 terms have
valuation at least (14-k)nu>=11. Also v(B_res(r))=1. Consequently

    c_1 in q Z_19, c_2 in q^2 Z_19, c_3 in q^3 Z_19.

Set P(T)=T^2(T-A)(T-B)=T^4-s T^3+t T^2 and L=P(1)=1-s+t. Since

    f(rT)=r^5 B_res(r)(T-1)P(T)C(T),

the two exact common-root equations at r say H_1(PC)(1)=0 and
H_3(PC)(1)=0. With C(1)=1, these become

    P'(1)+c_1 L=0,
    H_3(P)(1)+c_1 H_2(P)(1)+c_2 P'(1)+c_3 L=0.

Now P'(1)=2-s+2L, H_2(P)(1)=5-2s+L, H_3(P)(1)=4-s. Thus

    s=2+(2+c_1)L,
    D L=2+c_1,
    D=2+4c_1+2c_1^2+c_1 c_2-c_3.

D is a 19-adic unit congruent to 2, so these divisions are valid. They
give

    s=2+(2+c_1)^2/D,
    t=1+(2+c_1)(3+c_1)/D,
    (A-B)^2=s^2-4t
      =(2+c_1)(c_1^3-2c_1^2-4c_1(1+c_2)+4c_3)/D^2.       (*)

This formula is exact. It divides by neither A-B nor any root
difference, and includes the repeated-root case. In particular

    (A-B)^2 = -2c_1 mod q^2.                               (**)

If a_14 is a unit, section 1 and the same coefficient estimates give

    H_1(B_res)(r)/B_res(r)
       =b_1/b_0=c_6/c_5=beta_14 a_14/(beta_15 a_15) mod19,

with this residue nonzero. Hence v(c_1)=nu. Every other term in (*)'s
parenthesis has valuation greater than nu, and v((A-B)^2)=nu. A
nonzero square in Q_19 has even valuation, so nu is even. Reducing its
leading unit gives precisely

    (A-B)^2/19^nu
      = -2R beta_14 a_14/(beta_15 a_15) mod19.

For even nu the left side is a unit square; this proves D4. If a_14 is
not a unit, no parity claim is made without further analysis of (*).

## 5. Proof of D5: center constants with a possibly non-Q third root

For 2<=j<=18 write w_j for an actual rational common witness of the
normalized derivative D_j=sum_(k=0)^j binom(j,k)a_k X^(j-k). Choose
the center whenever it is available. The exact derivative equation is

    a_j=-sum_(k<j) binom(j,k)a_k w_j^(j-k),
    a_0=1, a_1=-1.

In D3 every nonzero small root has valuation nu, so every selected
noncenter rational witness is in q Z_19; zero is allowed. A non-Q
third small root is never selected. Replacing these selected noncenter
witnesses by zero defines the integral constants a_j^0. Induction in
the displayed recursion gives a_j=a_j^0 modulo q. The exact root
equation at the center, divided by 19, is

    -1+sum_(j=2)^18 beta_j a_j=0.

Thus q divides q_0. If q_0 is nonzero, nu<=v(q_0). Moreover a_14 and
a_14^0 have the same residue modulo 19. Combining this bound with D4
proves the stated mask-condition corollary. This direct proof needs no
two-variable constructor and assumes neither that the third root is in
Q nor that it is an eligible rational witness.

## 6. Why the nonunit case remains: an explicit low-order family

The forced residue collision is not by itself a contradiction. The
following analytic family satisfies the normalization, J=15, m=2, and
exactly the low-order common-root pattern of D3. It is **not asserted to
satisfy the other derivative conditions**, and is not a Casas--Alvero
counterexample. It records the limit of this approach.

Choose any nonzero rational r in 19 Z_(19). Put d=1-r,
L=20-19r, S_r(X)=X^2(X-r)(X-2r)^2, and

    P_r(X)=S_r(X)[(X-r)^14(X-L)+19d^13(X-r)^2],
    Q_r(X)=S_r(X)[1-(X-r)^2/d^2],
    K(r)=-H_3(P_r)(1)/(19 H_3(Q_r)(1)),
    B_r(X)=(X-r)^14(X-L)
             +19[K(r)+(d^13-K(r)/d^2)(X-r)^2],
    f_r(X)=S_r(X) B_r(X)=P_r(X)+19K(r)Q_r(X).

H_3(Q_r)(1) is a unit: modulo 19 it is H_3(X^5-X^7)(1)=-25.
The numerator H_3(P_r)(1) is divisible by 19. To compute its next
residue, note that the high-degree factor

    S_r(X)(X-r)^14(X-L)
      =X^20-20X^19+380r X^18+terms divisible by r^2.

Since 380 is divisible by 19 and r is divisible by 19, its H_k value
at 1 divided by 19 has the same residue as at r=0, for k=2,3,4.
The added low-degree term has the same property after division by 19.
At r=0,

    P_0=X^20-20X^19+19X^7,
    Q_0=X^5-X^7,
    H_3(P_0)(1)/19=-925, H_3(Q_0)(1)=-25.

Therefore K(r) is integral and is congruent to -37=1 modulo 19. In
particular B_r(0) has valuation one. B_r(1)=0, its reduction is
X^14(X-1), and g_r=B_r/(X-1) is a monic Eisenstein polynomial of
degree fourteen over Z_(19). The coefficient of X^19 in f_r is
-(L+19r)=-20. Its constant and linear coefficients vanish, its zero
multiplicity is exactly two, and its coefficient of X^5 has valuation
one while the lower coefficients have greater valuation. Thus J=15.

B_r'(r)=H_3(B_r)(r)=0. Around r, the factor
X^2(X-2r)^2 equals ((X-r)^2-r^2)^2 and is even in X-r.
Consequently H_2(f_r)(r)=H_4(f_r)(r)=0. The definition of K forces
H_3(f_r)(1)=0. Finally the same r=0 residue computation gives

    H_2(f_r)(1)/19 =258=11 mod19,
    H_4(f_r)(1)/19 =-2680=-1 mod19.

So neither H_2 nor H_4 uses the center. The small roots are r,2r,2r,
all rational, and a_14 is nonunit. In (*) one has c_1=c_3=0 and hence
(A-B)^2=0, as expected. The double small root is allowed by every
statement above.

This family shows why claiming that the collision must split with odd
valuation, or assuming a_14 is always a unit, would be invalid. A full
exclusion must use additional derivative equations or another global
obstruction.

## Research log, evidence, and remaining gaps

- Initial idea that removing two rational small roots leaves an
  Eisenstein factor over Q was rejected: the third small slot can be
  non-Q. D1 replaces it by a Galois-invariant one-slot argument over
  Q_19 and makes no Q-factor assertion.
- A degree-five good-prime degeneration alone forces only one low
  center; D2 uses the valuation partition to strengthen this to two
  centers in the unequal cases.
- A small residue enumeration was used only for intuition before the
  analytic discriminant proof: normalize one unit root to 1 and inspect
  the 18^2=324 unit pairs in F_19. It suggested the sole-H3 pattern
  (1,2,2). Its command and output are preserved separately. D2--D5
  do not use those counts as proof or claim a lift from them.
- During construction an intermediate message had the wrong sign in
  the even-nu square test by importing the two-small-root sign. The
  exact three-factor identities in section 1 correct it. The parity
  exclusion was unaffected. The correct sign is **-2**, as in D4.
- No numerical CAS, native unbounded operation, mask search, finite
  digit tree, or expansion of the triple-root candidate was launched.
- This note does not settle the equal-valuation cases with only H_2 or
  only H_4 at the center; the nonunit-a_14 branch of D3; any branch
  with two or three low center equations; multiplicity three; or J<=14.
  The exact square condition (*) may help a later narrowly justified
  next step, but its finite sufficiency is not asserted.
- Authoritative account-wide weekly telemetry at 2026-10-16 21:35 UTC:
  16% total used, 10080-minute window, reset 1792745187. Cutoff remains
  90% total used. No separate billed API was used.

This candidate is frozen with its manifest before any independent review.
