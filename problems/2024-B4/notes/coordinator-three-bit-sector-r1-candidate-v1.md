# Three-bit exponents: an explicit intersection budget

2026-10-17 UTC. **Candidate proof - unverified.** Constructor root.
Only open2024B4(b) is studied. TWO OTHER initially blind WHOLE
nonconstructor audits and coordinator reconciliation are required.
No mathematical program, scan, CAS or old certificate is used. No
priority, full exponent classification or annual solution is claimed.

## 0. Domain and proposed results

Work coefficientwise over F2 and K=Fbar2. Retain the established
normalization f_n=R phi_n, where

    f_n=X^n+Y^n+Z^n+(X+Y+Z)^n,
    R=(X+Y)(Y+Z)(Z+X).

The official target is TWO positive-degree factors of phi_n over F2,
not merely factors over K or equality of polynomial functions. Existence
of the quotient is an accepted preliminary input, not rederived here.

Fix integers a>=2,d>=1 and put

    q=2^a, r=2^d, ell=r+1,
    n=q ell+1=1+2^a+2^(a+d),
    N=deg(phi_n)=q ell-2,
    g=gcd(ell,q-1),
    M=((q-2)^2+3(g-1)q^2)/4.                         (1)

These n have EXACTLY three distinct nonzero binary digits, n>=13 and
n=1mod4. They belong to the remaining open sector, rather than the
already established preliminary two-bit family. M is an integer because
q is divisible by4. All quantifiers below are over EVERY such a,d.

**TB1: complete possible-intersection set.** At an intersection of
two coprime positive-degree factors of phi_n over K, the point must be

* P=(1:1:1), an ordinary point of multiplicity q-2; or
* a coordinate permutation of (b:1:1), where b!=1 and
  b^ell=1, b in F_q. There are exactly3(g-1) such points,
  each an ordinary point of multiplicity q.

Here ordinary means that the initial homogeneous form is a product of
distinct lines. There are NO possible intersections elsewhere, including
infinity. Other singular points can exist but cannot be shared by two
factors. TB1 does not say that all components pass through P.

**TB2: coprime-degree obstruction.** Every factorization phi_n=UV
over K with degU=e, degV=N-e, both positive, satisfies

    e(N-e)<=M.                                       (2)

In particular either of the following sufficient conditions implies
that the WHOLE phi_n is absolutely irreducible:

    g=1;                  or                  2(N-2)>M.     (3)

**TB3: an ordinary irreducibility test.** If

    4(N-4)>M,                                       (4)

then phi_n is irreducible over F2, hence n is excluded from the
official reducible set. This conclusion alone does not assert absolute
irreducibility. The g=1 branch of(3) has no size restriction on ell.

**TB4: explicit infinite subfamilies of exclusions.** In particular:

* for EVERY a>=2 and d>=2a-1, the WHOLE phi_n is absolutely irreducible;
* for a=2 and EVERY d>=2, the WHOLE phi_n is absolutely irreducible.

These are sufficient subfamilies, not an iff classification. The omitted
a2,d1 case n13 is not decided by these inequalities. No conclusion is
asserted when all tests fail. No new qualifying reducible family follows.

## 1. Squarefreeness and the accepted small-factor premises

For completeness reconstruct the source-free IC1 squarefreeness proof
in precisely this domain. Set W=X+Y+Z. The two first partials are

    f_(n,X)=(X^ell+W^ell)^q,
    f_(n,Y)=(Y^ell+W^ell)^q.                          (5)

Since ell is odd, X^ell+W^ell splits into distinct lines X+zeta W,
zeta^ell=1, and the second polynomial before its q power splits into
Y+eta W, eta^ell=1. No line from the two lists is associate: their
coefficient vectors are(1+zeta,zeta,zeta) and(eta,1+eta,eta).
If the first were c times the second, the Z and X coefficients would
give zeta=c eta and1+zeta=c eta, contradiction. Thus the derivatives
in(5) are coprime. A repeated irreducible factor of f_n would divide
both partials, impossible. Hence f_n and phi_n are squarefree over K.
In particular any partition of the absolute factors of phi_n gives
coprime U,V; a proposed arbitrary factorization cannot hide repetitions.

Two other exact previously accepted inputs are used:

* T1: for odd n of binary weight>=3, phi_n has NO absolute line factor.
* T2: in that same domain, phi_n has NO positive-degree F2 factor of
  degree1,2 or3.

Their complete accepted proof was freshly read. They do not assume
ordinary irreducibility, a fixed Kasami divisor, that all factors pass P,
or a global APN theorem. Here n has weight exactly3, so both apply.
No original Janwa--Wilson1993 component theorem is a premise.

## 2. A norm-one calculation removes every off-diagonal singularity

Use the affine chart Z=1. Write a possible singular point of phi_n as
(alpha,beta), and lambda=alpha+beta+1. The product f_n=R phi_n shows
that f_n and both its first partials vanish there, whether or not R
vanishes. Injectivity of the q-th power in K and(5) give

    alpha^ell=beta^ell=lambda^ell=u.

The equation f_n(alpha,beta,1)=0 then becomes

    0=(alpha+beta+lambda)u^q+1=u^q+1.

Thus u=1, and alpha,beta,lambda are NONZERO ell-th roots of unity.
No nonzero-coordinate assumption was made before this deduction.

Now ell=r+1 with r a power of2. For every one of these three roots,
its r-th power equals its reciprocal. Raising lambda=alpha+beta+1
to the r-th power therefore gives the exact identity

    1/lambda=1/alpha+1/beta+1.                        (6)

Set S=alpha+beta and T=alpha beta, both in K, T!=0 and lambda=S+1!=0.
Multiplying(6) by T lambda gives

    T=(S+T)(S+1),
    S(T+S+1)=0.

Consequently either alpha=beta, or

    0=T+S+1=(alpha+1)(beta+1).

EVERY possible singular point therefore lies on one of the prescribed
diagonals X=Y, X=Z, Y=Z. In the customary literature table this removes
all TypeIII points. It is the special ell=2^d+1 assumption, not an
inference from a general upper bound on their number, that does so.

This analysis covers projective points globally. The homogeneous
polynomial is symmetric in X,Y,Z. At any projective point choose a
nonzero coordinate, permute it into Z and scale it to1; the same exact
argument applies. It implies in addition that every singular point
has all three homogeneous coordinates nonzero. Points with a zero
coordinate, including any point on the Z0 line, are therefore NOT
missing singularities. We do not discard or guess a third homogeneous
partial: these are invertible affine charts on the projective curve.

The three diagonals meet in just P. Away from P, their possible
singular points are exactly among the coordinate permutations of
(b:1:1), b^ell=1,b!=1. These three lists are disjoint; for instance
(b:1:1)=(1:c:1) projectively would force b=c=1. No root at b0 exists.

## 3. Exact local forms, including the nonintersection branch

At P use X=1+x,Y=1+y,Z=1. The denominator is exactly xy(x+y).
The accepted tangent calculation T3, also immediate from
(1+z)^n=(1+z)(1+z^q)^ell, gives the first surviving numerator
term x^q y+x y^q. Thus phi_n has local order q-2 and initial form

    (x^(q-1)+y^(q-1))/(x+y)
       =product_(c in F_q minus F2)(x+c y).            (7)

It is squarefree, so P is ordinary of multiplicity q-2.

Fix now b^ell=1,b!=1. Put c=b+1, E=b^(-q) and B=1+b^(1-q).
Near(b:1:1) set X=b+x,Y=1+y,Z=1. The denominator is EXACTLY

    c^2 y+c y^2+x^2 y+x y^2.

The accepted S3B computation, whose complete proof was freshly read,
gives the first two possible numerator terms

    F_q=B y^q,
    F_(q+1)=y[E x^q+E x y^(q-1)+(1+E)y^q].          (8)

If B!=0, the quotient has local order q-1, initial form
(B/c^2)y^(q-1), and its degree-q term is

    (E/c^2)x^q+(E/c^2)xy^(q-1)
        +[(1+E)/c^2+B/c^3]y^q.                       (9)

The correction B/c^3 is retained. In particular the next term is NOT
divisible by the unique initial tangent y. No factorization can have
BOTH factors vanish here. To recall the full local reason, if positive
local orders s,t split the initial pure power y^(q-1), their leading
forms are constant multiples of y^s,y^t. Every term at the next degree
of their product is divisible by y, contrary to the x^q coefficient
E/c^2!=0 in(9). Thus any factor through this point has a unit cofactor.
This is an actual nonintersection conclusion, not a multiplicity bound.

We have B=0 exactly when b^(q-1)=1, equivalently b in F_q. In that
case E=b^-1, and(8) gives local order q with initial form

    (1/(b c^2))[x^q+x y^(q-1)+c y^q].                (10)

On y1 the bracket is x^q+x+c. Its derivative is1, so it has q DISTINCT
roots in K. At y0 its value is x^q, so the projective binary form has
no additional root there. Hence(10) is the product of q distinct
linear factors. Each such point is ordinary of multiplicity q.

The common solutions to b^ell=b^(q-1)=1 are the g-th roots of unity.
Indeed the integer Bezout identity for gcd(ell,q-1) gives b^g=1,
and the converse follows from g dividing both exponents. As g is odd,
the polynomial T^g-1 has exactly g distinct roots in K. Removing b1
and taking the three disjoint coordinate lists gives exactly3(g-1)
ordinary q-fold points. All other diagonal singular points are the
unit-cofactor branch(9), which cannot carry an intersection.

If U,V are two vanishing factors of phi_n, product differentiation
makes their common point singular on phi_n. Sections2--3 exhaust that
possibility in every chart. This proves the proposed TB1 without any
all-components-through-P premise.

## 4. Projective Bezout and the finite intersection budget

Consider ANY factorization phi_n=UV with U,V positive-degree and
homogeneous over K. Factors of a homogeneous nonzero polynomial can
be taken homogeneous: minimal and maximal degree comparison leaves
only one degree in each factor. Section1 makes U,V coprime.

Projective Bezout therefore gives

    degU degV=sum_Q I_Q(U,V).                        (11)

At an ordinary point of the WHOLE phi_n, the tangent cones of U and V
partition its distinct tangent lines, so they share no line. The exact
local intersection rule is then I_Q(U,V)=m_Q(U)m_Q(V), including
zero if one factor is a unit at Q. This is the classical coprime-
tangent equality, in precisely the projective/algebraically closed
setting, not merely a lower intersection inequality.

At P the two multiplicities sum to q-2; their product is at most
(q-2)^2/4. At each of the3(g-1) other possible points the sum is q,
so the product is at most q^2/4. TB1 and(11) give(2) exactly, with
no contribution hidden at infinity or at a unit-cofactor point.

T1 makes both degrees at least2. Since their sum is N>=10,
their product is at least2(N-2): explicitly

    e(N-e)-2(N-2)=(e-2)(N-e-2)>=0.

Thus2(N-2)>M precludes ANY factorization over K and proves the second
branch of(3). If a factorization exists over F2, T2 makes both degrees
at least4, and similarly

    e(N-e)-4(N-4)=(e-4)(N-e-4)>=0.

This proves(4), keeping ordinary and absolute irreducibility separate.

There is a stronger argument when g1. Then P is the ONLY possible
intersection, so(11) becomes

    degU degV=m_P(U)m_P(V).                          (12)

For ANY positive-degree divisor A of phi_n, T1 implies
degA>m_P(A). If equality held, move P to the affine origin. Its local
expansion would have only the highest total degree degA. Homogenizing
back would make A a binary homogeneous polynomial in the two local
linear coordinates; over K it splits into lines through P, contrary
to T1. The case m_P(A)=0 is also strict since degA>0.
Apply this to U and V: their degree product is strictly larger than
the multiplicity product, contradicting(12). Thus g1 always gives
WHOLE absolute irreducibility, regardless of the crude bound M.
This proves every assertion in TB2 and TB3.

## 5. Explicit sufficient subfamilies, with exact inequality signs

Suppose d>=2a-1. Since r=2^d>=q^2/2,

    ell>=q^2/2+1,
    2(N-2)=2q ell-8>=q^3+2q-8.

Also g<=q-1. Hence

    M<=((q-2)^2+3(q-2)q^2)/4
      =((3q-5)q^2-4q+4)/4.

Subtracting this upper bound from the preceding lower bound gives

    q^3/4+5q^2/4+3q-9>0  for q>=4.

The strict positivity already holds at q4 and every displayed positive
power term increases thereafter. Thus2(N-2)>M, proving TB4's first
family WITHOUT any root enumeration or numerical test.

For a2, q4 and q-1=3. If d is even,2^d+1 is2mod3, so g1 and(3)
applies. If d is odd and d>=3, g3 and ell>=9. Then

    M=(4+3*2*16)/4=25,
    N=4ell-2>=34,
    2(N-2)>=64>25.

This proves the second family for EVERY d>=2. At a2,d1 one has n13,
N10,M25: the absolute lower product16 and ordinary lower product24
do not exceed25. The tests therefore do NOT falsely exclude that
known reducible-over-K endpoint. No separate classification of n13
is needed or asserted in this packet.

## 6. Attribution, failed shortcuts and remaining scope

The singularity-table/Bezout method is classical and is expressly
documented by Hernando--McGuire0903.2016v4, especially its definitions,
Section3 and Corollary8. Its general absolute-COMPONENT existence
theorem is NOT a WHOLE-polynomial theorem. The new deduction here is
the special norm-one identity(6), removal of all TypeIII possibilities,
and the consequent whole-intersection budget and sufficient tests.
Literature priority is unestablished; the identities and criteria may
already have appeared. No absence claim follows from targeted searches.

The proof uses accepted T1,T2 and exact S3B, with their complete
operative proofs freshly read. Section1 reconstructs IC1 independently
of its separate Kasami-component premise. The point-P cone is fully
displayed. Only the classical coprime projective Bezout theorem and
its coprime-tangent intersection equality are additional standard
facts; their actual statements/hypotheses were read in the primary
coauthor paper. An external textbook proof was not freshly reread.

Rejected shortcuts: a general TypeIII count does not prove zero;
ordinary F2 irreducibility cannot be assumed; extension-field factors
do not automatically qualify officially; tangent multiplicity alone
does not force every component through P; a generic diagonal point
need not be ordinary; and affine analysis alone misses projective
points unless the charts are closed. All are addressed explicitly
above. The failed general2026 degree-gap source adaptation is not a
premise or a literature refutation. No blocked access path is bypassed.

When g>1 and both inequalities fail, component allocation among the
ordinary points can remain possible. The argument does not exclude
or produce such factors. More general binary weights, every remaining
1mod4 exponent and the official full reducibility set remain OPEN.
All TB claims stay UNVERIFIED until TWO OTHER whole audits and root
reconciliation. Only a new constructor prefix is written; older
candidate, proof, review, source and cache bytes are preserved.
