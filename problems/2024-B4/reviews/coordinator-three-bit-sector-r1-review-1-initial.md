# Three-bit sector TB1–TB4: initially blind WHOLE R1

2026-10-17 UTC. Reviewer `/root/review_2022_complexity_r2` (B).
Requested inherited **gpt-6.1-sol / max**; independent effective-setting
readback unavailable. This is an independent review, not coordinator
acceptance. The submission remains **candidate proof - unverified**
pending the other entire initially blind audit and reconciliation.

**Whole initial result: no substantive defect or required repair found.**
I reconstructed every TB1–TB4 implication and all 36 author obligations,
including the accepted small-factor premises, projective completion,
squarefreeness, local intersection equality and both infinite sufficient
families. The inequalities are sufficient tests and do not classify the
whole three-bit sector or the official reducible set. The issue ledger
records no open mathematical issue; its four scope notes are safeguards,
not objections or proposed extensions.

## 1. Identity, independence, exact reads and domain

The exact reviewed main is
`notes/coordinator-three-bit-sector-r1-candidate-v1.md`, 14660 bytes,
SHA256 `29878868615f42848918067fbed5067339cef3b254b3b836a1fa191502e41a77`.
The constructor freeze is 2711 bytes, SHA256
`0dc4b47373a3f071178bf0068a593b7a55a8451d41a42fda8f76c681e393a47a`.
I read all SIX packet files: main, 36 obligations, source/failed-route
record, administrative freezer, input record, and immutable freeze.
The freezer was read as administrative code and was NOT executed.

Root constructed TB1–TB4. I supplied no new inference or construction
to this packet. I previously independently reviewed T1–T4 as R2 and
S3A–S3D as R1; those older accepted-input roles are disclosed, not counted
as new independent recertification. Older GK/CP/NJ/HR/CS context and
review roles likewise do not construct the present proof. I freshly read
the COMPLETE accepted structural body and COMPLETE accepted sector3 body,
including their scope headers. I reconstructed the operative T1, T2,
point-P cone and S3B calculations below. I also read the accepted IC
scope header and COMPLETE Section1; the derivative proof is independently
given in the new main and needs no IC2–IC4 or original Kasami theorem.
All three accepted authority JSONs were read entirely. I did not read
any NEW TB peer report, issue record, metadata or finding before this
entire initial packet froze. No conclusion was requested from a peer.

The official Paper B, PDF page2 B4 hypothesis and(b), was freshly read
through primary web text. Other problems and preliminary(a) text returned
by that tool were not investigated or reproduced. The target is a
coefficientwise factorization in F2[X,Y,Z] into TWO positive-degree
factors after removing the prescribed R. Integer lifts of their
coefficients give the stated integer-polynomial congruence. A factor
solely over K=Fbar2 would not by itself qualify officially. Conversely
absolute irreducibility excludes an F2 factorization.

Here a>=2,d>=1, q=2^a, r=2^d, ell=r+1 and
n=1+q+qr. The bit positions 0,a,a+d are pairwise distinct: n is odd,
has weight exactly3, n>=13 and n=1mod4. Its nonzero homogeneous quotient
has N=n-3=q ell-2>=10. This does not enter the preliminary two-bit family.
The definitions g=gcd(ell,q-1) and
M=((q-2)^2+3(g-1)q^2)/4 are integral; q is divisible by4 and g>=1.
All statements quantify over every a,d in this stated domain; neither
r=q nor any divisibility between a and d is assumed.

## 2. Global squarefreeness and the exact low-factor premises

Put W=X+Y+Z. Formal differentiation in characteristic2 gives

    f_X=(X^ell+W^ell)^q,  f_Y=(Y^ell+W^ell)^q.

Because ell is odd, the roots of T^ell-1 are distinct and nonzero.
Before the qth powers, the first polynomial splits into X+zeta W and
the second into Y+eta W. Their coefficient vectors are
(1+zeta,zeta,zeta) and(eta,1+eta,eta). If the first were c times the
second, the Z and X coefficients would simultaneously give
zeta=c eta and 1+zeta=c eta, impossible. Thus the derivatives have
no common irreducible divisor over K. If H occurred repeatedly in f,
the product rule would make H divide BOTH derivatives, also in
characteristic2 when the repeated exponent itself differentiates to0.
It follows that f and its divisor phi are squarefree globally. This
also rules out a repeated factor avoiding P; a squarefree cone at P
alone would not have sufficed. Every factorization phi=UV is coprime.

The accepted T1 and T2 have exactly the needed hypotheses: odd n of
binary weight at least3. I checked the operative proofs rather than
assuming they say the whole polynomial is irreducible.

For T1, normalize a putative line as X+aY+bZ after a coordinate
permutation. Substitution in f gives the coefficient conditions at
Y^j Z^(n-j). The j=1,n-1 cases dispose of a or b in{0,1}, leaving
only the prescribed diagonals. Otherwise set A=a/(a+1),B=b/(b+1),
T=A/B. For supported j the condition is B^n T^j=1. The two supported
strict-interior indices 1 and 1+2^s, using a nonzero higher bit and
the third bit, imply T^(2^s)=1, hence T=1. Then a=b and B^n=1,
whereas the pure Y^n coefficient is1, a contradiction. Each prescribed
diagonal is simple in f: for X+Y its X derivative restricts to
Y^(n-1)+Z^(n-1), a nonzero polynomial. Dividing R removes all of
them. Thus phi has no absolute line factor.

For T2, phi takes value1 at the six F2-projective points other than
P. At P the tangent cone in this domain has no F2 line. Every F2
quadratic has a rational point; a point-free ternary cubic is one of
the eight F8 norm forms and hence has absolute line factors. The eight
claim follows by the three binary mixed-coefficient choices and the
168 ordered bases of F8 modulo21 scalar/Frobenius choices. Therefore
an F2 quadratic or cubic factor must pass P and have multiplicity at
least2. Multiplicity equal to degree makes a binary cone and contradicts
T1. A cubic of multiplicity2 restricted to an F2 line through P has
an exact double root at P and a distinct remaining rational root,
contradicting uniqueness of P. Thus neither F2 irreducible factors nor
positive-degree F2 divisors can have degree1,2 or3. This supplies a
degree lower bound, not any global ordinary irreducibility premise.

## 3. The root identity and projective exhaustion (TB1)

Let (alpha,beta) in chart Z=1 be singular on phi, and put
lambda=alpha+beta+1. Even on R=0, differentiating f=R phi shows
f=f_x=f_y=0. Injectivity of q-Frobenius gives

    alpha^ell=beta^ell=lambda^ell=u.

Substitution in f=0 gives (alpha+beta+lambda)u^q+1=u^q+1=0.
Hence u=1 and all three entries are nonzero. This validates every
later reciprocal and does not presuppose nonzero coordinates.

Now r, rather than q, is the Frobenius used: ell=r+1 implies
alpha^r=alpha^-1, beta^r=beta^-1 and lambda^r=lambda^-1. Raising
lambda=alpha+beta+1 to the rth power gives

    1/lambda=1/alpha+1/beta+1.

With S=alpha+beta,T=alpha beta, multiply by T(S+1), which is nonzero.
The result is T=(S+T)(S+1), equivalently

    S(T+S+1)=0.

When S=0, alpha=beta. Otherwise
T+S+1=(alpha+1)(beta+1)=0, so alpha=1 or beta=1.
No division by S or exclusion of its zero case is made. This is an
identity for roots in K; it is not an estimate on the number of
singularities and does not require a primitive root.

For any projective point choose a nonzero coordinate, permute it into
Z, and scale to1. The same symmetric polynomial and invertible chart
then apply. The argument proves that the two remaining coordinates
are nonzero as well. Thus there is no singular point with a zero
homogeneous coordinate, including on Z=0. It also forces every possible
singularity onto X=Y, X=Z or Y=Z. This closes infinity without using
the source paper's terse affine assertion as a proof.

These diagonals intersect only at P. Other possible points are the
three projective lists obtained by permuting(b:1:1), b^ell=1,b!=1.
For example (b:b:1) is represented by(1:1:b^-1), and inversion
permutes the same nontrivial roots. Distinct lists can coincide only
at b=1: normalization of their coordinate equalities forces all
coordinates equal. There is no b=0 case.

## 4. Both local germs and all tangent multiplicities

At P set X=1+x,Y=1+y,Z=1. The denominator is EXACTLY xy(x+y).
Using (1+z)^n=(1+z)(1+z^q)^ell, the constant, linear and qth terms
in the four-term numerator cancel. The first surviving term is
x^q y+x y^q. Thus the local order is q-2 and the initial quotient is

    (x^(q-1)+y^(q-1))/(x+y)
      =product_(c in F_q minus F2)(x+c y).

The q-2 factors are distinct; none is x or y or x+y. Consequently
P really is ordinary and has positive multiplicity q-2>=2.

At(b:1:1), let c=b+1!=0, E=b^-q!=0 and B=1+b^(1-q), and
translate X=b+x,Y=1+y,Z=1. Multiplication of the three denominator
factors gives c²y+c y²+x²y+x y². The root condition b^ell=1
reduces the first possible numerator terms to

    F_q=B y^q,
    F_(q+1)=E x^q y+E x y^q+(1+E)y^(q+1).

I checked these directly by expanding the q and q+1 terms of
(b+z)^n. The two pure x terms cancel between bases b; the terms with
base1 supply y^q and y^(q+1). All intermediate degrees2,...,q-1
vanish. Since q>=4 and ell>=3, no higher supported bit interferes.

If B!=0, the quotient begins with (B/c²)y^(q-1). At the next
degree the denominator's c y² term contributes the correction
B/c³ to the y^q coefficient, so that term is exactly

    (E/c²)x^q+(E/c²)x y^(q-1)
           +((1+E)/c²+B/c³)y^q.

In particular its x^q coefficient is nonzero. If two factors vanished
here with positive local orders s,t, their leading forms would be
nonzero scalar multiples of y^s,y^t, with s+t=q-1. Their degree-q
product term is necessarily divisible by y, contradicting this x^q
coefficient. Thus every factor through this point has a UNIT cofactor.
This is the needed zero intersection contribution. A single tangent
of high multiplicity alone would not have justified it, and I make
no stronger local analytic irreducibility assertion.

If B=0, then b^(q-1)=1, precisely b in F_q, and E=b^-1.
The order instead is q, with initial form

    (1/(b c²)) (x^q+x y^(q-1)+c y^q).

The affine root polynomial x^q+x+c has derivative1 and degree q,
so it has q distinct roots over K. Its binary homogenization has
value1 at(x:y)=(1:0), hence no missing tangent at infinity. This is
an ordinary q-fold point. The B=0 and B!=0 alternatives exhaust
every diagonal root, including cases where its coefficient field is
neither F_q nor prescribed to be a particular extension.

The roots satisfying both b^ell=1 and b^(q-1)=1 are exactly b^g=1:
the integer gcd identity works with negative powers because b!=0.
Since g is odd there are exactly g distinct roots in K. Deleting1
and using the three disjoint projective lists gives exactly3(g-1)
ordinary q-fold points. All remaining diagonal singularities have a
unit cofactor. Every common zero of U,V is singular on UV=phi, so
the foregoing exhaustion proves TB1 in full. It does not assert
that every factor passes through P or through any other listed point.

## 5. Projective intersection budget and the two degree tests

Any factors U,V of a nonzero homogeneous polynomial are homogeneous:
their least total degrees add to N and their greatest total degrees
also add to N, so the sum of their nonnegative degree spreads is0.
Section2 gives gcd(U,V)=1. The hypotheses of projective Bézout over
the algebraically closed K are therefore satisfied, with no common
curve. Its sum of local intersections is degU degV.

At every ordinary point of the WHOLE phi, the leading forms of U
and V multiply to a product of distinct lines. They consequently
share no tangent direction. The standard local equality then gives
I_Q(U,V)=m_Q(U)m_Q(V); this includes0 when either local factor is
a unit. The relevant equality, rather than only the usual lower
intersection inequality, is essential to the upper budget. At P the
two multiplicities sum to q-2 and their product is at most(q-2)²/4;
at every other allowed common point their sum is q and the product
is at most q²/4. There are no further terms. This proves

    e(N-e)<=((q-2)²+3(g-1)q²)/4=M.

Over K, T1 forces both factor degrees to be at least2. The exact
identity

    e(N-e)-2(N-2)=(e-2)(N-e-2)

is nonnegative. Thus 2(N-2)>M contradicts any factorization and
proves WHOLE absolute irreducibility. Over F2, T2 instead makes
both degrees at least4; replacing2 by4 gives the corresponding
identity and 4(N-4)>M implies ordinary irreducibility. N>=10
keeps both degree intervals legitimate. The latter test alone is
not labelled an absolute irreducibility theorem.

There is a genuinely stronger g=1 branch. Then only P can be a
common point, so Bézout says degU degV=m_P(U)m_P(V). For ANY
positive-degree divisor A, m_P(A)<=degA. If equality held, the
invertible homogeneous coordinates u=X+Z,v=Y+Z,w=Z would turn A
into a homogeneous polynomial only in u,v: the local expansion at
w=1 would have just its top degree. Such a binary form splits into
linear forms over K, giving line factors of phi and violating T1.
Therefore degA>m_P(A). This is also immediate for m_P(A)=0.
Applying the strict inequality to U,V contradicts their product
equality, even when one of their local multiplicities is0. TB2's
unrestricted g=1 test is valid without assuming all components meet P.

## 6. Infinite families, strict signs and endpoint attacks

For d>=2a-1, r>=q²/2 and ell>=q²/2+1, giving
2(N-2)=2q ell-8>=q³+2q-8. Since g<=q-1,

    M<=((3q-5)q²-4q+4)/4.

The difference of these two bounds is exactly
q³/4+5q²/4+3q-9. It equals39 at q=4 and strictly increases for
larger positive q, so is positive for the entire allowed range.
Thus this first TB4 family is a strict absolute test, including the
threshold equality d=2a-1; no asymptotic qualification is needed.

For q=4, if d is even then ell=2mod3 and g=1. If d is odd and
d>=3, then ell>=9, g=3, M=25, N>=34 and2(N-2)>=64>25.
These two cases exhaust d>=2 and prove the second TB4 family.
At a=2,d=1, n=13, N=10 and M=25. The absolute minimum product
is16 and the ordinary minimum is24; neither is strictly larger
than25. Also g=3, so the g=1 argument is unavailable. This endpoint
does NOT produce a contradiction with known Kasami context, and
the packet makes no new factorization or ordinary classification of13.

I also challenged: coincident diagonal lists; a root0 or1 hidden in a
denominator; a singularity on a zero coordinate; an off-diagonal root
over a larger coefficient field; nonhomogeneous factors; repeated
components avoiding P; factors missing P when g=1; a missing tangent
at y=0; and reversal of strict inequality or degree minima. The
arguments above resolve these attacks symbolically. No finite scan,
CAS, finite-field table or author certificate replay was used.

## 7. Sources, limitations and disposition

The methodological paper is Hernando–McGuire arXiv0903.2016v4. I
freshly read its matching quotient definition and whole-versus-component
distinction, local singularity data in Section3, the projective Bézout
and coprime-tangent statements in Section3.2, and relevant scope of
Theorems15/16. These are classical intersection imports, not new
theorems reconstructed from a search abstract. Its generic TypeIII
count is only an upper bound and does not prove the required zero;
the reciprocal identity supplies that step. Theorem15 assumes
ordinary irreducibility and Theorem16 gives a component, so neither
is used to conclude whole irreducibility here. The source's affine
notation for the projective sum is not used to omit any chart.

An additional public author-textbook check of Fulton was attempted.
The search index exposed the relevant standard statements, but full
author-PDF opens failed502 and404. I do not claim a fresh full textbook
proof read, a successful download, or an access bypass. The primary
coauthor paper's explicit operative statements were successfully read;
the whole proof's classical theorem imports retain their stated limits.

No result here gives a new qualifying reducible family, every three-bit
case, every1mod4 exponent, the annual answer, an effective classification
or priority. The excluded domain a=1 or d=0 is not silently included.
The conclusion for the ordinary-only inequality stays ordinary.
The author must handle any later substantive repair. No such repair
is requested by this initial review, and coordinator acceptance is
not supplied by this report.

The separate ledger covers all36 obligations individually. Source
checks record exact read scopes and source failures. Administrative
preservation verifies the complete6-file target and all35 declared
current inputs; older inventories are bound by immutable metadata.
The compact own-parent chain binds421 older own paths, including the
entire frozen2020R8 packet, without duplicating its history. No old,
shared, cache or Git file is changed. This entire initial was frozen
before any NEW TB peer material was read.
