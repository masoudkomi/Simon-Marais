# A subgroup translation defect in the actual component budget

18 October 2026 UTC. **Candidate proof - unverified.** Sole NEW
constructor C, `/root/review_2017_coarsening_r1`. TWO OTHER initially
blind ENTIRE WHOLE audits and coordinator reconciliation are required;
C is excluded. Root supplied the generic research target and no new
proof inference. Requested inherited gpt-6.1-sol/max; independently
verified effective-setting readback is unavailable.

Only the open 2024 B4(b) is investigated. This extends the explicit
positive-gap range of accepted FR10 by sharpening its root quadruple
count. No routine computation, parameter scan or factorization is used.
The count is elementary multiplicative-subgroup/additive reasoning;
the underlying intersection framework is classical. No publication
priority, full factor classification or annual solution is claimed.

## 0. Exact object and accepted input

Work over K, the algebraic closure of F2. With W=X+Y+Z, put

    R=(X+Y)(Y+Z)(Z+X),
    f_n=X^n+Y^n+Z^n+W^n, phi_n=f_n/R.

The established POLYNOMIAL quotient is used; preliminary (a) is not
reproduced. Official (b) asks whether phi_n is a product of two
nonconstant coefficientwise reductions over F2. Whole absolute
irreducibility is a sufficient obstruction to that requested product;
one absolutely irreducible F2 component alone would not suffice.

Throughout the geometric criterion use

    n=ell*q+1, ell>=3 odd, q=2^i, i>=2,
    d=gcd(ell,q-1), N=ell*q-2.

Thus q is exactly the maximal two-power dividing n-1 and the binary
weight of n is at least three. In particular n>=13. No n1/n3, ell1,
q2 or zero-polynomial endpoint is silently included.

The ONE operative geometric input is the complete accepted FR10 body,
`proofs/reviewed-reasoning-frobenius-return-r10-v1.1.md`, with its
current acceptance MD/JSON, freshly read in FULL. Its exact scope is:

* phi_n is reduced and EVERY absolute component has degree at least q.
* If reducible, choose an ACTUAL least absolute component of degree e
  and its FULL actual coprime complementary product. The SAME pair has
  q<=e<=N/2, so its degree product is at least q(N-q).
* For odd s let M_s count ordered pairs (a,b) with a,b,c=a+b+1,1
  four DISTINCT members of mu_s, the s-th roots of unity in K. The
  same pair's projective intersection sum is at most

    B_actual=(q-2)^2/4+3(d-1)q^2/4
                   +q*M_ell+q(q-2)*M_d/4.               (1)

This input includes ALL center, diagonal, ordinary and nonordinary
off-diagonal intersections and the explicit infinity check. The
nonordinary local intersection, when both factors meet, is exactly q;
it is not discarded because of its single tangent. The ordinary
off-diagonal points are EXACTLY those counted by M_d, not M_ell.
The complement may be reducible and need not pass through any specified
point. Absolute factors need not be F2-defined or have equal degree.
Reducedness and degree lower bounds retain their accepted R6/T1 scope.

C constructed FR10 and older R6/R7/R8, and reviewed R9. These are
disclosed accepted-input/context roles, not independent re-review of
those older results. Root and B supplied FR10's two OTHER whole audits.
Both were explicitly released before C accessed them; neither supplied
a new FR11 inference. Root's unrelated unverified degree-gap note was
not read or used. No pending/unaccepted packet is a premise.

## Proposed FR11A--FR11D

For an odd integer s>=1 define the explicit integer bound

    U(1)=0;
    U(s)=(s-3)^2,
       if s>=3, 3 divides s, and s+1 is NOT a power of two;
    U(s)=(s-1)(s-3) otherwise, for s>=3.                 (2)

**FR11A.** For every such s, M_s<=U(s). More precisely, with

    H=mu_s, A_s=|H intersect (1+H)|,

one has, for s>=3,

    M_s<=(s-1)(s-3)-A_s(s-1-A_s).                     (3)

If s+1 is a power of two, H is the full multiplicative group of that
finite field and M_s=(s-1)(s-3). If s+1 is not a power of two and
A_s>0, then M_s<=(s-3)^2. The condition 3|s guarantees A_s>0 without
enumeration. This is a finite subgroup count, not a factor-existence
assertion.

**FR11B.** In the geometric domain above define

    P_U=(4ell-3d-2-U(d))*q^2
             -[4+4U(ell)-2U(d)]*q-4.                  (4)

Absolute reducibility of phi_n implies P_U<=0. Therefore P_U>0
implies the WHOLE phi_n is absolutely irreducible, and excludes the
official coefficientwise two-factor product. No converse is asserted.

**FR11C.** For EVERY integer t>=1,

    n=105*2^(12t+6)+1                                  (5)

has absolutely irreducible whole phi_n. At every member the OLD FR10
expression is strictly negative, so this is not obtained by applying
its positive-P criterion. The literal old R7 gcd and R8/R9 NF4/J
sufficient hypotheses fail too, as checked below. No exhaustive
published-nonoverlap claim is made.

**FR11D, exact limitation.** The new strict subgroup discount cannot
be imposed on full finite-field multiplicative groups: the old
quadruple bound is attained there. Also the remaining sector
ell21,q=2^(6t),t>=1 still has P_U<0. Thus neither the improved test nor
its failure decides the whole remaining factorization problem.

## 1. Translation counts and the equality obstruction

Let H=mu_s for odd s>=3, so H has exactly s elements. For t in K put

    r_H(t)=#{b in H:b+t in H}, A=A_s=r_H(1).

For every t!=0 the map b -> b+t is a fixed-point-free involution of
H intersect (t+H). Therefore r_H(t) is even. Since |H|=s is odd,

    0<=r_H(t)<=s-1.                                    (6)

In particular A is even and 0<=A<=s-1. If t is itself in H, division
by t is a bijection of H, and hence

    r_H(t)=A for every t in H.                         (7)

We need to distinguish an ACTUAL subfield from a subgroup of comparable
size. Suppose A=s-1. The element 1 is the only member of H whose
translate by 1 is zero, so every b in H except 1 then has b+1 in H.
Consequently S=H union {0} satisfies S+1=S. For every h in H,
multiplication by h preserves S; multiplying S+1=S gives S+h=S.
Together with the zero translate, S+v=S for EVERY v in S. Thus S is
closed under addition. It is also closed under multiplication, contains
0,1, and all its nonzero elements have inverses in H. It is a finite
field. Its cardinality s+1 is therefore a power of two.

Conversely, if s+1=2^a, the unique s-th roots in K are precisely
F_(2^a)^*: both sets have s elements and every nonzero field element
has s-th power 1. Then A=s-1. We have proved the exact equivalence

    A=s-1 iff s+1 is a power of two.                    (8)

It follows, using evenness, that

    s+1 not a power of two IMPLIES A<=s-3.              (9)

No quantitative sum-product theorem or unverified subfield avoidance
condition has been imported. In particular (8) follows from translations
of THIS subgroup, not from its cardinality being near a field size.

## 2. The normalized quadruple deficit

Fix a in H except 1 and set t=1+a, which is nonzero. The values b
with b,c=t+b both in H are counted by r_H(t). Two of these values,
b=1 and b=a, are always present. They are exactly the two that violate
pairwise distinctness among a,b,c,1. Indeed b=c would force t=0;
c=1 iff b=a and c=a iff b=1. Thus the number of VALID b for this a is

    r_H(1+a)-2.                                       (10)

There are exactly A choices of a in H except 1 with 1+a in H; this is
the definition of A and does not include a1. For these, (7) gives
r_H(1+a)=A. For the other s-1-A choices, (6) gives the upper bound
s-1. Summing the ACTUAL counts (10), without dividing by an orbit
size, yields

    M_s<=A(A-2)+(s-1-A)(s-3)
        =(s-1)(s-3)-A(s-1-A).                         (11)

This also holds at A0, when the first summand is zero. It proves (3).
No claim is made that an arbitrary assignment of these intersection
numbers can be realized by a multiplicative subgroup.

If s+1 is not a power of two and A>0, evenness and (9) give
2<=A<=s-3. The elementary factorization

    A(s-1-A)-2(s-3)=(A-2)(s-3-A)>=0

then gives M_s<=(s-3)^2. If 3|s, choose a primitive cube root omega
in H. In characteristic two, 1+omega=omega^2 and
1+omega^2=omega, so A>=2. This proves the improved branch of (2).
The remaining branch follows from (11) since 0<=A<=s-1; M1=0 is
immediate and separate. FR11A follows in FULL.

For sharpness, when s+1=2^a and H=F_(2^a)^*, any a in H except 1
has r_H(1+a)=s-1. Equation(10) then gives exactly s-3 valid b, so

    M_s=(s-1)(s-3).                                    (12)

This includes s3/M3=0. A strict uniform deficit without the non-field
hypothesis would be false. None of the reasoning divides by 2 or 4
inside K; all counts and inequalities are ordinary integers.

## 3. Preserve the actual global pair while inserting the count

Suppose phi_n is absolutely reducible. The exact accepted FR10 input
provides the same actual least component and FULL complement with

    (ell-1)q^2-2q=q(N-q)<=e(N-e)<=B_actual.              (13)

In (1), the coefficients of M_ell and M_d are respectively q>0 and
q(q-2)/4>=0 because q>=4. Therefore FR11A gives

    B_actual<=B_U=(q-2)^2/4+3(d-1)q^2/4
                         +q*U(ell)+q(q-2)*U(d)/4.      (14)

All3(d-1) ordinary diagonal points and the full central cost are still
present. The new count has NOT discarded any actual nonordinary
intersection or made a local bound on an arbitrarily grouped formal
factor. At infinity the accepted zero contribution is retained in its
n>=13 domain. No equal-degree, common-center or F2-definition assumption
is inserted into (13).

Subtract (14) from the lower bound in (13), multiplying by 4 as an
ordinary integer inequality. Direct collection of terms gives

    4[(ell-1)q^2-2q-B_U]
       =[4ell-4-1-3(d-1)-U(d)]q^2
          +[-8+4-4U(ell)+2U(d)]q-4
       =(4ell-3d-2-U(d))q^2
          -[4+4U(ell)-2U(d)]q-4=P_U.                  (15)

The bracket on the left cannot be positive under reducibility, proving
FR11B. Reducedness rules out a nontrivial power of just one absolute
component. Thus the contrapositive is WHOLE absolute irreducibility,
not merely the existence of a distinguished absolute component.

To compare EXACTLY with FR10, let V(s)=(s-1)(s-3) for odd s>=1;
V1=0. From (2), 0<=U(s)<=V(s). The old expression P has

    P_U-P=q(q-2)[V(d)-U(d)]
                         +4q[V(ell)-U(ell)]>=0.        (16)

Thus no previously positive P case is lost. This is a numerical
comparison of two valid sufficient tests, not a converse for either.

## 4. The concrete family and exact older-scope checks

Let t>=1, i=12t+6, q=2^i and ell=105=3*5*7. The orders of 2 modulo
3,5,7 are respectively 2,4,3: 2=-1 mod3, 2^2=-1 mod5, and
2^3=1 mod7 with 2!=1 there. Since i is divisible by 6 and is 2
modulo4, both 3 and 7 divide q-1 while 5 does not. Therefore

    d=gcd(105,q-1)=21 exactly.                         (17)

The integers 105 and 21 are divisible by 3, while 106 and 22 are
not powers of two. Hence

    U(105)=102^2=10404, U(21)=18^2=324,
    P_U=31q^2-40972q-4.                                (18)

For every real q>=2048,

    31q-40972>=31*2048-40972=22516>0,
    P_U>=2048*22516-4>0.                              (19)

Our family has i>=18, q>=2^18>2048. All geometric hypotheses hold,
and FR11B proves WHOLE absolute irreducibility for EVERY t>=1. The
t0/q64 endpoint is not included; no factorization claim is made there.
The separated bits of 105=2^6+2^5+2^3+1 give binary weight five in n,
so this is not simply the binary-weight-three sector.

For the OLD FR10 expression at these SAME parameters,

    4ell-d^2+d-5=-5,
    4(ell-2)^2-2(d-1)(d-3)=41716,
    P=-5q^2-41716q-4<0.                               (20)

Thus the new family is strictly beyond that explicit positive-P test.
The difference in (16) is exactly 36q^2+744q: the discounts in M_d and
M_ell both matter and both have nonnegative weights.

For precise comparisons with other named scopes, ord_105(2) is
lcm(2,4,3)=12, so gcd(i,ord_105(2))=6, not1. The odd part 105 is not
Q-1 for a power Q of two (105+1=106). Thus the literal old R7 gcd
hypothesis and R6D Mersenne odd-part hypothesis are unavailable.

There are actual witnesses against NF4/J as well. In F8 choose a
two-dimensional F2-subspace V and b outside V. The four points b+V
are distinct, nonzero, and have zero sum. Each has seventh power1,
hence 105th power1. Since i is divisible by3, q=1 modulo7 and
delta=q^2-q+1=1 modulo7. Raising these four points to delta leaves
them unchanged, so their delta-power sum is zero. Consequently the
accepted R8 NF4 and R9 J sufficient hypotheses both fail. This is a
witness in the exact root group, not a tested list or an abstract
assignment. Failure of these sufficient hypotheses does not contradict
their theorems or prove exhaustive nonoverlap with prior literature.

## 5. Genuine limitations and official consequence

The full-field sharpness (12) proves the first part of FR11D. Even
away from that sharp case the new criterion is incomplete. For ell21
and q=2^(6t),t>=1, ord_21(2)=6 gives d21. Both U values are324, so

    P_U=(84-63-2-324)q^2-[4+4*324-2*324]q-4
        =-305q^2-652q-4<0.                            (21)

That nonpositive result proves neither reducibility nor irreducibility.
It is an explicit surviving limitation, not a new classification. No
unproved stronger Gauss-map, monodromy or point-count inference is used
to remove it. This proves FR11D in its stated negative scope.

In the positive range, a purported official integer product reduces
coefficientwise to phi_n=g_bar*h_bar in F2[X,Y,Z], since the nonzero R
cancels in this integral domain. Both reductions have positive degree.
This contradicts WHOLE absolute irreducibility, even if g_bar,h_bar
were initially nonhomogeneous. A claim about polynomial functions on
F2^3 or one F2-defined absolute component would not establish this.

No converse at P_U<=0, all-odd-n result, general Frobenius-orbit
classification, effective full enumeration or preliminary construction
is asserted. The new elementary count and global substitution are fully
exposed, but possible earlier published formulations/family overlap
remain unresolved. Original Jedlicka/Ferard operative bodies remain
unread in the literal scopes recorded in the source file. No abstract
is promoted to a theorem. Two OTHER whole audits remain mandatory.
