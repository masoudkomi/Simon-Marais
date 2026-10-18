# FP0–FP2: OTHER initially blind ENTIRE WHOLE audit R1

2026-10-18 UTC. Reviewer `/root/review_2021_reasoning_j15_r2` (A).
Requested inherited gpt-6.1-sol/max; independent effective-setting readback
unavailable. This is an independent audit recommendation, not coordinator
promotion. The submitted proof remains candidate proof - unverified until
the required second OTHER whole audit and coordinator reconciliation.

The entire frozen nine-file constructor packet was read, including all36
obligations, sources, failures/worklog, administrative code and metadata.
Main:14313 bytes, SHA256
`68accf09323d692e4d4d6850e8c2c04d735d667e1ddaa56cbb73c451fb6402ef`.
Freeze:2465 bytes, SHA256
`3bab98755fd2df8b13ca531e408f1f543762bad9f4289230a9d9668135d45d28`.
No NEW C FP report, findings, ledger, source record, code or metadata was
read or hashed before this entire initial freeze. Root is sole NEW
constructor and is excluded from the independent reviewer count.

I constructed older T1–T4/C7/C11 and IC component results and reviewed
older CP/GK/CJ/NJ/HR/NF packets. Those roles are disclosed; I did not
construct, suggest or contribute the NEW FP degree gap, exact six-line
contact argument or grouping proof. Accepted old bodies are not being
self-recertified. In particular, the full accepted NF body and authority
were read to verify the branch boundary; its conclusion is not used as
a substitute for any FP inference.

**Finding:** all36 obligations close. I found zero substantive defects,
zero unresolved issues and zero required author repairs. Five closed scope
notes are retained in the issue ledger. I recommend the exact FP0–FP2
partial claims for coordinator reconciliation after the other complete
blind audit. The possible nonconstant small F2 cofactor remains unresolved.

## 1. Exact domain and proof dependencies

The official2024 B4(b) target is coefficientwise factorization of the
prescribed quotient into two positive-degree F2 polynomials, equivalently
integer lifts of such factors. Extension-field factorization and APN
nonexceptionality do not answer that target. Only(b) is audited here.
For this packet q=8^k, k>=2, so q>=64; n=7q+1 and N=n-3=7q-2.
Thus n is positive and odd, and its four binary ones are in positions
3k through3k+2 and0. No n1/n3 convention is needed in this subfamily.

Work in K=the algebraic closure of F2. Put W=X+Y+Z,
R=(X+Y)(Y+Z)(Z+X), f=X^n+Y^n+Z^n+W^n and phi=f/R. Divisibility by
R is the established normalization of the official target. The only
general geometric imports are projective Bezout for coprime curves,
local contact additivity, the local multiplicity lower bound and equality
for disjoint tangent cones. Their operative statements and hypotheses
were checked in the primary Hernando–McGuire paper; the source record
states exact read limits. All special projective counts, expansions,
contacts, inequalities and descent steps below were reconstructed by hand.

NF covers the ell7 branch a=log2(q) with 3 not dividing a; here a=3k.
The degree-q local term that enabled NF vanishes in this branch. I do
not borrow that argument. Theorem16 of Hernando–McGuire already gives
some absolute F2 component since7 is a proper divisor of q-1. That
published qualitative context supplies no quantitative step below.
Theorem15 assumes ordinary F2 irreducibility, which is not assumed here.

## 2. Squarefreeness and every projective singularity

The X^(n-1)Y coefficient of f is1, so f is not zero. R is homogeneous
of degree3, giving nonzero homogeneous phi of degreeN. If a product in
a graded polynomial domain is homogeneous, its least and greatest
degrees add separately; their spreads sum to zero. Each factor is
therefore homogeneous. This includes arbitrary, unequal factor degrees.

Formal differentiation gives f_X=(X^7+W^7)^q and
f_Y=(Y^7+W^7)^q. Their pre-qth-power linear factors have vectors
(1+zeta,zeta,zeta) and (eta,1+eta,eta), with zeta,eta in F8*.
Proportionality by c would give zeta=c*eta from Z and
1+zeta=c*eta from X, a contradiction. These two derivatives are
coprime. Any repeated irreducible factor of f divides both partials,
also when its repeated power has derivative zero. Hence f and phi
are squarefree. Every complementary factorization phi=UV is coprime.

A singular point of phi has f=f_X=f_Y=0 by f=R*phi, even on R=0.
Permute a nonzero coordinate into Z and normalize Z=1. Write
alpha=X, beta=Y, lambda=alpha+beta+1. Injectivity of qth powers gives
alpha^7=beta^7=lambda^7=u. The value of f is
u^q*(alpha+beta+lambda)+1=u^q+1, so u=1. All three are nonzero
elements of F8. This applies after any coordinate permutation, and
therefore excludes singularities with a zero homogeneous coordinate,
including every point at infinity of the original Z=1 chart.

The necessary singularity set is exactly the projective F8 points
where X,Y,Z,W are nonzero; the next local expansions prove sufficiency.
There are73 points in P2(F8). The four zero lines have9 points each,
six distinct pairwise intersections and no triple intersection. The
complete six pair intersections are
(0:0:1),(0:1:0),(1:0:0),(0:1:1),(1:0:1),(1:1:0).
Consequently their union has30 points and its complement has43.
Each prescribed diagonal X=Y,Y=Z,Z=X contains7 of these points,
namely P=(1:1:1) and six more. Their only mutual intersection is P.
The count is thus1 central,18 nontrivial diagonal,24 off-diagonal.
No numerical finite-field enumeration is being used.

## 3. Ordinary local cones at all43 points

At P put X=1+x,Y=1+y,Z=1. Since
(1+t)^n=(1+t)(1+t^q)^7, the first surviving numerator piece is
x^q*y+x*y^q. R=xy(x+y), so phi has order q-2 and cone

    (x^(q-1)+y^(q-1))/(x+y)
       = product_(b in F_q minus F2)(x+b*y).

Its q-2 lines are distinct. None is a prescribed diagonal x=0,y=0
or x+y=0. All multiplicities here are orders of the local polynomial,
not just apparent degrees before division.

At a nontrivial diagonal point (b:1:1), b in F8* minus{1}, set
c=b+1,E=b^-1,X=b+x,Y=1+y. The degree-q piece of f vanishes because
q fixes F8. Its next piece is
y[E*x^q+E*x*y^(q-1)+(1+E)*y^q]. Directly,
R=c^2*y+c*y^2+x^2*y+x*y^2. Dividing the initial pieces gives orderq
and cone (E/c^2)[x^q+x*y^(q-1)+c*y^q], since (1+E)/E=c.
After y=1 its derivative in x is1; at (1:0) its value is nonzero.
Thus it has q distinct projective tangent directions and y=0 is
transverse. Coordinate permutations cover all18 points.

At an off-diagonal point (alpha,beta), R is a unit. The first
nonzero piece has degreeq+1 and equals
a*x^(q+1)+b0*y^(q+1)+d*(x^q*y+x*y^q), with
a=alpha^-1+lambda^-1, b0=beta^-1+lambda^-1, d=lambda^-1.
Its derivative matrix on (x^q,y^q) has determinant
a*b0+d^2=1/(alpha*beta*lambda). Indeed the numerator after clearing
denominators is (lambda+alpha)(lambda+beta)+alpha*beta=lambda.
It is nonzero, so the two derivatives have no common projective root.
The binary degreeq+1 form is nonzero and has q+1 distinct linear
factors. Thus these24 points are ordinary of multiplicityq+1.

These calculations also prove that all43 necessary points are actual
singularities. In phi=UV their cones partition distinct lines, so the
two cones are disjoint. At each point the local intersection is
m_P(U)m_P(V); it is zero if either factor is a local unit. Any common
zero of U,V is singular on their product. There are no omitted global
intersection contributions outside this list.

## 4. Exact diagonal rank and six pencil contacts

Let e=deg U, m=m_P(U), and let u_i and v_j be its multiplicities at
the18 nontrivial diagonal and24 off-diagonal points. Their respective
ranges are0..q and0..q+1; m lies in0..q-2. Define S=sum u_i and
T=sum v_j. No hypothesis requires U to pass P.

Differentiate f=R*phi transversely to Y=Z, then restrict:

    (X+Y)^2*phi(X,Y,Y)=X^(7q)+Y^(7q).

The right side is (X^7+Y^7)^q. It yields only the root P of contact
q-2 and six other seventh-root points of contactq. At infinity
(1:0:0) the quotient is nonzero. It is a nonzero homogeneous
degreeN restriction, so the line is not a component of either factor.
The proved transversality makes each factor's line contact equal to
its multiplicity at every listed point. The total degree of the
nonzero homogeneous restriction of U is e, including any infinity
zeros; there are none outside this list. Hence on each prescribed
line e=m+sum_six u_i. Adding gives S=3(e-m). In particular z=e-m>=0.

There are9 F8 lines through P. Removing the3 prescribed diagonals
leaves6. Each off-diagonal F8 point lies on exactly one of them,
because its join with P is an F8 line and cannot be prescribed.
No uniform count of points on an individual line is required.

For such a line write x=t,y=b*t, b in F8 minus F2. In the numerator
the supported nonconstant degrees are jq and jq+1, j=0..7. The
degree1 coefficient vanishes, as do those at q,q+1,2q. Here b^q=b,
so the latter coefficients reduce respectively to the degree1 and
degree2 Frobenius identities. The coefficient at2q+1 is
1+b^3+(1+b)^3=b(1+b), which is nonzero. There is no intervening
supported degree. Dividing by the exact R=b(1+b)t^3 proves a
nonzero line restriction of phi with contact2q-2 and leading
coefficient1. Thus none of these6 lines is a component of phi,U or V.

If the direction is absent from U's cone, its contact with U is m.
If present, it is absent from V's cone; V therefore has contact
q-2-m, even if V misses P. Contact additivity then gives U contact
(2q-2)-(q-2-m)=q+m. Thus it is m+q*epsilon_L in both cases.
This also deals with either factor being constant: its cone has no
directions and its contacts are zero. Bezout against a constant
means simply the empty zero set, and the asserted degree0 identity
is immediate without applying a positive-degree curve theorem.

At any off-diagonal point the line contact with U is at least v_j.
Equality is not assumed if that line is tangent. Sum the6 degree-e
line contact identities; all other zeros contribute nonnegative
amounts. The result is T<=6(e-m)-q*t, proving FP0. If U has F2
coefficients its local cone at the F2 point P is squaring-invariant.
The6 F8 directions split into two3-cycles (F8 has no elements of
degree2 over F2), so t is0,3 or6. For arbitrary K factors that
restriction is neither needed nor asserted. Slopes and reciprocal
cone coefficients have the same orbit lengths.

## 5. Complete real optimization for FP1

For positive complementary degrees, the ordinary local calculation
and projective Bezout give the exact equality

    e(N-e)=m(q-2-m)+sum_18 u_i(q-u_i)
                         +sum_24 v_j(q+1-v_j).

Cauchy gives sum u_i^2>=S^2/18 and sum v_j^2>=T^2/24.
Using S=3z yields the upper bound

    m(q-2-m)+3q*z-z^2/2+(q+1)T-T^2/24.

These inequalities concern real numbers representing nonnegative
integer multiplicities, not field arithmetic. Completing the T square
gives the GLOBAL maximum6(q+1)^2, at T=12(q+1). This is valid for
every actual T; FP0 is an independent additional restriction. There
is no substitution of a T upper bound on a decreasing quadratic.

Subtract e(N-e), put m=e-z and expand. The difference is at most

    -3z^2/2+(2e+2q+2)z-6qe+6(q+1)^2
    =-3/2*[z-2(e+q+1)/3]^2
       +2/3*[e^2-(7q-2)e+10(q+1)^2].

The square is discarded over all real z; no feasible or integral
maximizer is presumed. For 2q+9<=e<=N/2 the bracketed polynomial
has endpoint values -3q+109 and -9q^2/4+27q+9. At q64 they are
-83 and -7479. Uniformly for q>=64, the first is <=-83 and the
second is <=-117q+9<0. A convex quadratic is bounded above by
its larger endpoint value on the interval, so this entire upper
difference is strictly negative. Bezout's equality required a
nonnegative upper difference. This is the contradiction.

For any original factor degreeE in [2q+9,5q-11], both E and N-E
are at least2q+9. Taking the smaller degree puts e<=N/2 and gives
exactly the contradiction just proved. Both factors have positive
degree in this interval. This proves the entire FP1 band, including
its endpoints, without a balanced-factor or ordinary-F2-irreducible
hypothesis.

## 6. Grouping and actual F2 descent for FP2

Factor phi into its distinct absolute irreducible factors. Suppose
all component degrees were at most B=2q+8. Since N>B, successive
grouping first exceeds B with a sum e in [2q+9,4q+16]. For q>=64,
4q+16<=5q-11 and4q+16<N, so this is a proper factor in the
forbidden band. Therefore some component exceeds B. FP1 forces
its degree to be at least5q-10; the possibility that this is all of
phi already satisfies the same inequality. Two such components
would require10q-20>N, since3q-18>0. Hence the component G is
unique, and all other degrees total at most N-(5q-10)=2q+8.

Use one fixed monomial ordering and normalize the leading coefficient
of each absolute factor to1. Coefficientwise squaring is an
automorphism of K that fixes phi and permutes these normalized
factors, preserving their degrees. It is not the polynomial-square
operation that doubles monomial exponents. The unique large G is
therefore fixed, and each coefficient satisfies a^2=a, hence lies
in F2. Cancelling G from sigma(phi)=phi also fixes its complementary
quotient, so that quotient is F2-defined, even if it is a unit.
No transitive orbit, equal absolute degrees or irreducibility over
F2 was presumed. This proves FP2 as written.

## 7. Adversarial endpoints and disposition

I checked units/full factors in FP0, m0 and missed singularities,
nontrivial diagonal points from all3 coordinate permutations, all
projective infinity contributions, tangent off-diagonal contacts,
unequal factor degrees and a single absolute component. The lower
endpoint expression at q8 is85, not negative, and the greedy band
inclusion also fails there. Thus there is no extension to q8/n57.
No factorization of that endpoint was needed or inspected for proof.

The proof allows a dominant F2-defined absolute component times a
nonconstant F2 quotient of degree<=2q+8. Such a quotient would give
the official factorization; it has not been excluded or constructed
here. The result is quantitative structural information in a
restricted four-bit subfamily, not ordinary irreducibility, full
absolute irreducibility, an annual classification or a novelty claim.

All math was checked by hand, with no mathematical program, scan,
CAS, factor table, author rerun or certificate replay. Administrative
fingerprinting is separate. Every constructor artifact, all12 of its
declared current inputs and the compact own parent were checked;
the current report's independent freezer binds those exact records
and verifies them again before the entire initial closes. Older
history is referenced through frozen metadata rather than recopied.
There is no proposed reviewer repair and no change to any old byte.

The companion issue ledger gives a separate disposition for each
of the36 obligations and records5 closed scope notes. The source
record specifies actual primary passages and unread/unimported
leads. Only the coordinator can reconcile both OTHER whole audits
and promote this exact scoped partial result.
