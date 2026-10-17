# Fresh initially blind WHOLE KC audit R1

2026-10-17 UTC. Reviewer `review_2021_reasoning_j15_r2`.
Requested gpt-6.1-sol/max; effective-setting readback unavailable.
This is a nonconstructor recommendation, not coordinator promotion.

**Recommendation:** no substantive defect found in KC's exact whole
Kasami divisor criterion. I reconstructed the entire new necessity
argument and both exact accepted dependencies, with40 inference checks
covering all26 obligations. No author repair is required by this audit.
The conclusion is a whole-divisor iff in its stated domain, not a
classification of all factors or of the annual problem. A second
complete fresh whole audit and coordinator reconciliation are required
before promotion.

Target:7192 bytes, SHA256
`390d795343eb32a9496aa9a64c054b4809bd400c37c8195264053d343ba180bf`.
Constructor manifest:1202 bytes, SHA256
`f08044ef0a1a9d8fa38e26f50e2b261d46ef761e68604060f918c5119816a3f3`.
All four submitted artifacts were read: complete candidate,
26-obligation JSON, source-audit MD and source JSON. The source-audit
contains construction/failed-route provenance; no separate current
mathematical program or computation is a premise.

## Independence and exact premises

I authored the older T1–T4/C7/C11 constructions and held the previous
CP whole R2 and GK whole R1 review roles. Those roles are explicit.
I did not construct, suggest, clarify or repair the NEW KC matrix,
homogeneity argument, binary-coefficient obstruction or integer
necessity. Root constructed KC. This review is fresh for KC; it does
not count as a new independent audit of my older authored theorems.
No new peer KC findings/report or later root KC inspection was read
before this COMPLETE initial freeze, and no substantive finding was
sent before it.

The full exact accepted CP1–CP3 and GK1–GK3 bodies and their acceptance
MDs were reread. Their original raw candidates remain byte-exact
suffixes. CP1 and the all-index GK sufficiency are the only mathematical
dependencies of the iff. The full accepted phi13 criterion and NV
exposition were also read for scope/consequence checks; neither gives
the new necessity as a substitute. The unverified MCM bridge is
motivation only. In particular an external absolute-component,
monodromy, exceptionality or finite-group theorem is not a premise.

## 1. Domain and the accepted composition interface

The [official2024 B4(b)](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf)
uses positive odd n and coefficientwise congruence of integer
polynomials modulo2. Its factors must both be nonconstant modulo2.
This is polynomial factorization, not an assertion about functions
on the eight binary triples. Only the designated open part(b) is
researched here; no preliminary proof is supplied.

Fix k>=2, q=2^k, d=q²-q+1 and odd n>=3. Thus d>=13 and the whole
fixed divisor phi_d is a nonzero positive-degree polynomial. The
proposed theorem is exactly

    phi_d | phi_n over F2
       iff n=(q^(2r+1)+1)/(q+1), r an integer>=1.       (KC)

The normalized invariant polynomials are defined by

    G_j(x)=x^j+(x+1)^j=g_j(x²+x).

Accepted CP1 is an ACTUAL polynomial equivalence over F2 for all odd
d,n>=3, including multiplicities:

    phi_d | phi_n iff g_n=H(g_d), H in F2[T].

Its full proof retains full affine degree n-3 under the invertible
linear dehomogenization, descends through the free rank-four module
with basis1,s,t,st, and uses the unique monic h-adic expansion. It
cancels the SAME nonzero U+V factor and does not remove repeated
diagonal factors. No individual-factor descent is asserted. These
details matter: a radical, extension-field, finite-point or
dehomogenized-only version would not be enough for KC.

Assume the whole-divisor hypothesis. Substitute U=x²+x in the exact
composition to obtain

    G_n(x)=H(G_d(x)) in F2[x].                           (5)

It remains a polynomial identity after extension to K=algebraic
closure(F2). The chosen H need not be homogeneous, invertible,
separable, or a permutation polynomial. None of those properties
is used.

## 2. The locus F=1 and the explicit constant matrix

Set m=(q+1)n. It is odd and greater than1. Use homogeneous forms

    F=X^(q+1)+Y^(q+1),
    C=X^(q³+1)+Y^(q³+1),
    P_m=X^m+Y^m.

The ordinary INTEGER identity(q+1)(q²-q+1)=q³+1 holds. For EVERY
point(X,Y) in K² satisfying F=1, put x=X^(q+1). Then x+1=Y^(q+1),
and evaluating(5) gives exactly

    P_m(X,Y)=H(C(X,Y)).                                 (6)

This evaluation makes no division and is valid at zero coordinates
too. Equation(6) is asserted only on F=1. It is not a homogeneous
identity P_m=H(C) on the plane; that stronger assertion would generally
be false when H has several degrees.

Because q>=4 there is t in F_q distinct from0,1. Choose a,b in K
with a^(q+1)=t and b^(q+1)=t+1. Both are nonzero. Since t,t+1 lie
in F_q*,

    a^(q²-1)=t^(q-1)=1,
    b^(q²-1)=(t+1)^(q-1)=1.

Thus a^(q²)=a and b^(q²)=b: these CONSTANTS lie in F_(q²).
The choice of any(q+1)-st roots works. No finite-field norm-surjectivity
or subgroup-classification theorem is silently needed.

Define M=[[a,b],[b^q,a^q]]. Every entry is nonzero and

    det M=a^(q+1)+b^(q+1)=t+(t+1)=1.

Writing M^[j] for entrywise q^j-th powers, direct multiplication is

    M^T M^[1]
      =[[a*a^q+b^q*b, a*b^q+b^q*a],
         [b*a^q+a^q*b, b*b^q+a^q*a]]
      =I.

All four entries, including both off-diagonals, have been checked;
there is no sign or transpose convention hidden in a group name.
As the constants are fixed by q²-Frobenius, M^[3]=M^[1].

For the VARIABLE column v=(X,Y)^T, Frobenius is still applied
coordinatewise without any q²-periodicity. The identities are

    F(Mv)=v^T M^T M^[1] v^[1]=v^T v^[1]=F(v),
    C(Mv)=v^T M^T M^[3] v^[3]=v^T v^[3]=C(v).            (7)

These are homogeneous polynomial identities over K. Constants, not
variables, are fixed by q²-Frobenius. They are also not the
transcendental auxiliary coordinates used in the earlier GK proof.

## 3. Passing from F=1 to a full homogeneous identity

For F(v)=1, equation(7) puts Mv on the same locus and keeps C fixed.
Applying(6) at both points yields P_m(Mv)=P_m(v). Therefore

    D(v)=P_m(Mv)+P_m(v)

vanishes on F=1. Crucially, D is homogeneous of degree m even though
H(C) need not be homogeneous.

For any v in K² with F(v) nonzero, algebraic closedness supplies a
NONZERO lambda with lambda^(q+1)=F(v)^(-1). Consequently
F(lambda v)=1, and

    0=D(lambda v)=lambda^m D(v)

forces D(v)=0. Normalization is never attempted at F(v)=0. No
division by a point on that hypersurface, no curve irreducibility
and no source parametrization is needed.

Now consider the univariate polynomial D(X,1). The exceptional
equation F(X,1)=X^(q+1)+1 has at most q+1 roots in the INFINITE
field K. Thus D(X,1) has infinitely many zeros and is identically
zero. If D= sum c_i X^i Y^(m-i), its specialization is sum c_i X^i;
all c_i therefore vanish. This recovers the points on F=0 and at
Y=0 as a polynomial conclusion, without normalizing those points.

The resulting full identity is

    (aX+bY)^m+(b^q X+a^q Y)^m=X^m+Y^m.                  (8)

An equality only on F_(q²) points would be insufficient. For example,
X^(q²)-X vanishes on that finite field without being the zero
polynomial. The argument uses K infinite and has not restricted
variable points to the constants' finite field. This checks the
principal field-versus-polynomial danger in the submission.

## 4. Adjacent binary subset sums force a degenerate matrix

Let S be the set of binary1-bit positions of m. Frobenius and finite
ordinary multiplication give

    (1+Z)^m=product_(i in S)(1+Z^(2^i)).

The sums of distinct subsets of these powers of2 are unique. Hence
the coefficient binom(m,j) is1 in characteristic2 exactly when j
is such a subset sum. No outside binomial-parity theorem is needed.

Suppose m has at least three set bits. Oddness supplies bit0.
Choose any other set bit h>=1. There is still a third set bit, so

    j=2^h, j+1=2^h+1

are BOTH subset sums with0<j<j+1<m. This checks strict properness,
including when the unused bit is below h rather than above it.
The two mixed coefficients of(8) are therefore

    a^(m-j)b^j=(b^q)^(m-j)(a^q)^j,
    a^(m-j-1)b^(j+1)=(b^q)^(m-j-1)(a^q)^(j+1).         (9)

Each binomial factor is exactly1, and the corresponding right-hand
mixed coefficient of X^m+Y^m is0. All displayed factors are nonzero,
so division of the second equality by the first is legal. It gives

    b/a=a^q/b^q,
    b^(q+1)=a^(q+1),

contradicting the sum of these norms being1. Equivalently, in the
generic all-entry-nonzero matrix[[a,b],[c,e]], the same two ratios
would give b/a=e/c and hence ae+bc=0. The submission's det M=1
excludes exactly that degeneracy. Thus the coefficient obstruction
has been independently reconstructed without an automorphism-group
classification or a group-order assertion.

It follows that m has binary weight at most2. Weight1 for an ODD
positive integer would make it1, excluded by m>1. Therefore

    m=2^s+1 for an integer s>=1.                        (10)

The oddness and all-four-nonzero-entry hypotheses are essential to
this particular argument; they are actually present, not inferred
from an abstract symmetry label.

## 5. Exact integer congruence, without an order heuristic

Since m=(q+1)n, equation(10) implies2^k+1 divides2^s+1. Write
s=A k+B, with A>=0 and0<=B<k. Modulo q+1 the integer is congruent to

    (-1)^A 2^B+1.

If A is even, the representative2^B+1 is positive and strictly less
than q+1, so cannot be divisible. This includes A=0 and B=0.
If A is odd, the representative is1-2^B. Its absolute value is
strictly less than q+1, and it is zero only at B=0. Thus A must be
odd and B=0, so s=k(2r+1) for an integer r>=0. Substitution yields

    n=(q^(2r+1)+1)/(q+1).

The r=0 value is exactly n=1, outside n>=3. Consequently r>=1,
which is the required necessity. Merely bounding the multiplicative
order of2 modulo q+1 would not have given these exact signs and
quotients; the representative argument proves every case directly.

## 6. Sufficiency and every boundary

Accepted GK1 gives the actual F2 polynomial compositions for EVERY
q=2^k,k>=1 and EVERY r>=0. Its complete basis/vector proof, canceled
temporary denominator, all-index Frobenius recurrence and strict
degree comparison were reread. In particular it supplies every r>=1
in(KC), rather than just the older CP2 r=2 member. Applying the
accepted CP1 back in the homogeneous F2 polynomial ring proves the
sufficiency. No root or point-count inference is used in this direction.

The domain and interpretation checks are:

* r=1 gives n=d, so the WHOLE divisibility has unit cofactor. This
  split alone is not a qualifying official factorization and does
  not decide whether phi_d has other nonconstant F2 factors.
* For q>=4 and r>=2, deg phi_d=d-3>0 and the nonzero cofactor has
  degree n-d>0. The accepted homogeneous product has actual F2
  coefficients. Choosing coefficientwise0/1 lifts gives integer
  polynomials, both nonconstant modulo2, for those exponents.
* n=3 gives phi3=1 and cannot admit a nonconstant phi_d divisor.
  More generally,3<=n<d fails by the exact nonzero degrees n-3,d-3.
  At n=1, phi1 is zero and the official factor condition fails in
  the polynomial domain; it is not inserted into(KC). The recurrence's
  auxiliary r=0/g1 value is kept separate.
* At q=2, phi3 is a unit and divides every phi_n. In particular n=5
  is not in the claimed r>=1 progression, whose first terms are3,11.
  Thus extending(KC) to k=1 is actually false, not just unproved.
  This is exactly where no t outside{0,1} can be chosen.
* At q=4, q^(2r+1)=64*16^(r-1). Thus(KC) agrees with the full
  accepted whole-phi13 iff with index r-1>=0. Its first equality
  endpoint13 and first positive-cofactor member205 remain distinct.
* For r>=1,
  n-1=q(q^(2r)-1)/(q+1), and the quotient is an odd INTEGER.
  Hence v2(n-1)=k, consistent with and stronger than old NV.
  No old proof bytes or earlier necessary-only theorem are changed.
  This valuation alone is not substituted for the new progression.

All families here are ordinary odd positive integers, not formal
indices or finite-field exponents reduced modulo a group order.

## 7. Actual source roles and scope

The [Zieve author PDF](https://websites.umich.edu/~zieve/papers/biv.pdf)
introduction and general-method overview were freshly inspected for
the stated bivariate-factorization context. The publicly accessible
author-uploaded [Cohen–Matthews1994 full text](https://www.researchgate.net/publication/239745090_A_Class_of_Exceptional_Polynomials)
was inspected at its definitions and introductory theorem statements.
Their exceptionality/monodromy assertions are neither the theorem
being proved here nor premises for any step. In particular no
odd-k exceptionality hypothesis is extended to all k. No full
external proof reconstruction is claimed. The source file records
the actual bounded read scopes and absence of a new download.

The new argument supplies its finite-field constants, matrix identities,
homogeneous extension, binary coefficient facts and integer divisibility
proof in full. It uses no Janwa–Wilson absolute-factor theorem,
finite subgroup classification, APN nonexceptionality theorem or
unverified MCM bridge assertion. No mathematical program, CAS,
orbit test, exponent scan, source-certificate replay or author rerun
was used in this review. Hash/JSON checks are administrative only.

KC concerns the WHOLE fixed phi_(q²-q+1) over F2. It does not
classify individual Kasami components, arbitrary factors, all
reducible phi_n, or the official annual answer. Failure of its
divisibility criterion is not an irreducibility theorem. No novelty
or literature-wide absence claim is made. I recommend acceptance
only in this exact scope after the other complete blind audit and
coordinator reconciliation.
