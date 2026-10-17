# Low factors and ordinary-point descent for 2024 B4(b)

2026-10-16 UTC. **Candidate proof - unverified.** Constructor:
`review_2021_reasoning_j15_r2`, reassigned to constructive 2024 research
after freezing the independent J15 review. Requested model/reasoning:
gpt-6.1-sol / max; independent effective-setting readback unavailable.
Two fresh independent nonconstructor audits are required. No complete
exponent classification or novelty is claimed.

This packet studies only the open part (b). It does not derive or
reproduce the preliminary construction. The new arguments below are
self-contained; the Kasami source premise and the previously accepted
whole-phi13 criterion are context, not proof dependencies of T1–T4.

## Exact domain and proposed results

Over F2 put

    f_n=X^n+Y^n+Z^n+(X+Y+Z)^n,
    R=(X+Y)(Y+Z)(Z+X),       phi_n=f_n/R.

The quotient and the official interpretation are already established in
the project. The target in part (b) is reducibility of phi_n over F2,
with two factors of positive degree. Factorization solely over an
extension field is insufficient. This packet assumes that n is odd and
its binary expansion has at least three nonzero digits; hence n≥7.
The elementary boundary cases and the preliminary exponent family are
outside this packet.

Let P=(1:1:1), and write n=2^i ell+1 with ell odd. When i≥2 set q=2^i.
An absolute component means an irreducible factor over Fbar_2, regarded
up to a nonzero scalar. Its minimal coefficient field means the smallest
finite field over which a normalized defining polynomial is defined.
All multiplicities at P are orders of the local expansion.

**T1: no absolute line factor.** If n is odd with binary weight at
least three, phi_n has no linear factor over Fbar_2.

**T2: no F2 factor of degree at most three.** Under the same hypothesis,
every nonconstant F2-irreducible factor of phi_n has degree at least four.
Equivalently, a positive-degree F2 divisor of phi_n cannot have degree
one, two or three.

**T3: descent controlled by each tangent direction.** Suppose i≥2 and
H is an F2-irreducible homogeneous factor of phi_n with H(P)=0. Its
absolute factors form one Frobenius orbit of size r. If the tangent cone
of H at P contains the direction U+alpha V, and alpha has exact degree
d over F2, then

    r divides d,     d divides i.

In particular every absolute factor of H is defined over F_(2^r), with

    r | gcd(i, deg H, m_P(H)),

and r divides every tangent-field degree occurring in H. The assertion
does not assume that phi_n itself is irreducible and does not claim that
all factors of phi_n pass through P.

**T4: an exact local trichotomy when i=3.** Let n=8 ell+1 with ell≥3
odd. Exactly one of the following occurs among the F2-irreducible factors
of phi_n that vanish at P. All other factors avoid P.

1. There is one such factor H. It is absolutely irreducible over F2,
   m_P(H)=6, and deg H≥7.
2. There are two such factors H_1,H_2. Both are absolutely irreducible
   over F2, both have multiplicity three at P, and they have the same
   degree, at least four. Every odd coordinate permutation exchanges
   them.
3. There are two such factors H_1,H_2, each irreducible over F2 and each
   the product of three distinct Frobenius-conjugate absolute factors
   of minimal field F8. Every absolute factor is smooth at P. The two
   F2 factors have the same degree, a multiple of three and at least
   six, and every odd coordinate permutation exchanges them.

These are necessary alternatives, not existence claims for each n.
For example the known Kasami n=57 factorization lies in alternative 3.
Nothing here asserts that the factor through P is the whole polynomial.
The trichotomy applies without an APN classification or a fixed phi13
divisor, including exponents whose full factorization remains unsettled.

## 1. Proof of T1 by three binary-supported coefficients

Work in an algebraic closure k of F2. Suppose a homogeneous linear form
L divides f_n. After permuting X,Y,Z and multiplying L by a scalar,
we can write L=X+aY+bZ. Substitution gives the zero polynomial

    (aY+bZ)^n+Y^n+Z^n+((a+1)Y+(b+1)Z)^n.                 (1)

For 0<j<n with binom(n,j) odd, its coefficient at Y^j Z^(n-j)
requires

    a^j b^(n-j)+(a+1)^j(b+1)^(n-j)=0.                   (2)

First dispose of all zero denominators. Taking j=1, if a=0 then
(b+1)^(n-1)=0 and b=1; if a=1 then b^(n-1)=0 and b=0. Taking
j=n−1, if b=0 then a=1, and if b=1 then a=0. Thus these cases give
only one of the prescribed diagonal lines.

Assume now a,b are outside {0,1}, and set

    A=a/(a+1), B=b/(b+1), T=A/B.

Equation (2) becomes B^n T^j=1. Since n is odd, bit zero of n is set.
Choose any other set bit h=2^s. There is a third set bit, so both j=1
and j=1+h lie strictly between 0 and n and their binomial coefficients
are odd. This follows directly from
(1+t)^n=product_(set bits e)(1+t^(2^e)) in characteristic two.
Dividing their two equations gives T^h=1. The Frobenius h-th power is
injective, so T=1. Therefore A=B, a=b, and B^n=1. The coefficient
of Y^n in (1), however, is

    a^n+(a+1)^n+1=1,

because B^n=1 gives a^n=(a+1)^n. This contradiction excludes the
remaining lines. Thus f_n has no linear factors except X+Y,Y+Z,Z+X.

Each diagonal appears only once. For example, modulo X+Y,

    partial f_n/partial X = Y^(n-1)+Z^(n-1),

which is a nonzero polynomial since n>1. If (X+Y)^2 divided f_n,
that derivative would also vanish modulo X+Y. Coordinate symmetry
handles the other two diagonals. Dividing by R removes all line
factors and proves T1. This is an identity in polynomial rings, not
an argument about values on finitely many field elements.

## 2. Rational points and the ordinary tangent cone

At each of the six points of P2(F2) other than P, phi_n takes the value
one. There are two coordinate-permutation types: (1:0:0) and (1:1:0).
At the first, partial f_n/partial Y and partial R/partial Y both equal
one; at the second, partial f_n/partial X and partial R/partial X both
equal one. Differentiating f_n=R phi_n at these points, where R=0,
gives the assertion.

Use affine coordinates X=1+U,Y=1+V,Z=1 near P. The denominator is
exactly UV(U+V). Since n=q ell+1 and ell is odd,

    (1+T)^n=(1+T)(1+T^q)^ell
            =1+T+T^q+T^(q+1)+terms of degree at least 2q.

In the four-term numerator the constants, linear terms and q-th powers
cancel. The first surviving homogeneous term is
U^q V+U V^q. Thus the lowest homogeneous term of phi_n is

    C_i(U,V)=(U^(q-1)+V^(q-1))/(U+V)
             =product_(alpha in F_q minus F2)(U+alpha V).    (3)

For i=1 this is the constant 1. For i≥2 it has degree q−2 and is
squarefree, with no F2-defined tangent direction. Consequently:

- if n≡3 mod 4, phi_n has no F2-projective point;
- if n≡1 mod 4, its unique F2-projective point is P;
- in the second case every component through P has a tangent cone
  formed from a disjoint subset of the lines in (3).

In particular no F2-defined factor can be smooth at P: its single
tangent would have coefficients in F2, contrary to (3). Repeated
factors through P are also impossible because (3) is squarefree.

## 3. An elementary lemma on point-free binary cubics

Here “point-free” means no zero in P2(F2), not irreducibility. Every
homogeneous cubic C over F2 that is point-free is a product of three
conjugate lines over F8.

There are exactly eight such cubic polynomials. Indeed evaluation at
the three coordinate points forces the coefficients of X^3,Y^3,Z^3
to be one. Evaluation at (1:1:0),(1:0:1),(0:1:1) forces the sum
of the two coefficients in each pair

    {X^2Y,XY^2}, {X^2Z,XZ^2}, {Y^2Z,YZ^2}

to be one. Evaluation at P then forces the coefficient of XYZ to be
one. The three pair choices are free, giving 2^3=8 cubics.

Now let L=aX+bY+cZ, where a,b,c are an ordered F2-basis of F8, and
let sigma square coefficients while fixing the variables. The polynomial

    N(L)=L sigma(L) sigma^2(L)

is a homogeneous cubic over F2. For every nonzero vector v∈F2^3,
L(v) is nonzero, so N(L)(v)=L(v)^7=1. It is point-free and splits
into three conjugate lines.

There are (8−1)(8−2)(8−4)=168 ordered bases. Two bases give the same
norm polynomial precisely when their forms are related by L↦s sigma^j(L),
with s∈F8^* and j∈{0,1,2}. To justify “precisely”, the three
conjugate lines are pairwise nonassociate: otherwise a,b,c would lie
in one F2-dimensional subspace after a common scaling. Unique
factorization then forces any form with the same norm polynomial to
be an associate of one of those three lines. The scaling lies in F8,
and its norm is s^7=1. The 21 possibilities are distinct. Hence there
are 168/21=8 distinct norm polynomials. They exhaust the eight cubics
above. This is an exact counting argument, not a computer enumeration.

Also, a homogeneous quadratic over F2 cannot be point-free. If it took
value one at all seven projective points, its three square coefficients
would be one and its three mixed coefficients would be one. At P it
would then take value 3+3=0, a contradiction.

## 4. Proof of T2

Suppose phi_n has an F2-irreducible factor H of degree two or three.
It is homogeneous. If H had no F2 point, the quadratic observation or
the cubic norm lemma would either rule it out or give an absolute line
factor of phi_n, contradicting T1. Thus H has an F2 point.

Section 2 forces n≡1 mod 4 and that point to be P. Because there is
no F2 tangent in (3), m_P(H)≥2. If m_P(H)=deg H, its affine
expansion at P consists solely of its top homogeneous part and splits
into lines over Fbar_2. After homogenization these are line factors
of phi_n, again impossible. This excludes degree two and the
multiplicity-three cubic case.

The remaining case is a cubic H with m_P(H)=2. Its tangent cone has
no F2-projective zero. Restrict H to any F2-projective line through P.
This line is not a component by T1. The restriction is a nonzero binary
cubic, and its root at P has exact multiplicity two, since the tangent
cone is nonzero on that F2 direction. Removing that double root leaves
a linear factor over F2 with a root different from P. This is a second
F2 point of phi_n, contradicting Section 2. Degree one was already
excluded by T1. Therefore every F2-irreducible factor has degree at
least four, proving T2.

## 5. Proof of T3 without whole-polynomial irreducibility

Normalize each absolute factor by fixing its leading coefficient in a
monomial order to one. For an F2-irreducible H, Frobenius sigma acts
transitively on these factors: the product of a proper invariant orbit
would be a proper F2 factor. Thus H is the product of r distinct
conjugates of an absolute factor G of minimal coefficient field F_(2^r).
Distinctness here also follows locally from the squarefree cone (3).

Since P is F2-rational and H(P)=0, every conjugate of G passes through
P, with the same multiplicity mu. Thus

    deg H=r deg G,       m_P(H)=r mu.                       (4)

Pick a tangent L_alpha=U+alpha V belonging to G. Its least field of
definition is F_(2^d), where d is the degree of alpha. Frobenius^d
fixes L_alpha and sends G to another absolute factor of H with that
same tangent. Two distinct absolute factors through P cannot share a
tangent, since their lowest terms would give a repeated factor in (3).
Therefore sigma^d(G)=G. The orbit length r divides d. Since alpha∈F_q,
d divides i. The same reasoning applies to every tangent of every
absolute factor of H; all have orbit length r. Together with (4) this
proves every assertion in T3.

This argument is equivalently the unique-component argument at an
ordinary point after blowing up one tangent. The proof above needs no
resolution theorem and keeps the field condition at a singular point
explicit. It strengthens the usable local information beyond the total
multiplicity divisibility in McGuire's Proposition 9, without claiming
that his assumed F2-irreducibility has been proved.

## 6. Proof of T4

When i=3, (3) is

    C_3=(U^3+U^2V+V^3)(U^3+UV^2+V^3)=A B.                 (5)

Both binary cubics have no F2-projective root and are irreducible over
F2. Their six roots have exact field F8. Each F2 factor through P
must have a tangent cone equal to A, B, or A B. Squarefreeness gives
one or two F2-irreducible factors through P. Swapping X and Y swaps
U,V and exchanges A and B.

Suppose first there is only one factor H through P. Every coordinate
permutation preserves H as a component, because it preserves phi_n
and P. Its absolute factors form a transitive Frobenius r-cycle. T3
gives r∈{1,3}. Coordinate permutations commute with Frobenius; their
permutations of these r factors therefore lie in the centralizer of
that cycle, which is the cyclic group generated by it. The image of
S3 is abelian. Its commutator subgroup A3 consequently fixes every
absolute component.

Let tau cyclically permute X,Y,Z. In the affine coordinates at P its
linear action is

    (U,V) |-> (U+V,U).

Its fixed projective tangent directions are the two roots of
T^2+T+1, which lie in F4 and not in F8. Thus tau has orbits of size
three on the six directions in (5). Since each absolute component
of H is tau-stable, its tangent set has size divisible by three.
If r=3, however, (4) gives mu=6/3=2, impossible. Hence r=1 and
H is absolutely irreducible. Its multiplicity is six. A degree-six
curve with multiplicity six at P would split into lines after moving
P to the origin, contrary to T1, so deg H≥7. This is alternative 1.

Suppose instead there are two factors H_1,H_2 through P. Each has
one cubic tangent cone in (5), so both have multiplicity three.
Swapping X,Y exchanges their tangent cones and hence exchanges the
two actual F2-irreducible factors. Their degrees are equal, and they
have the same absolute-factor field degree. Every transposition is
conjugate in S3; the induced action on these two factors is the sign
map, so all odd coordinate permutations exchange them.

T3 again gives r=1 or 3 for each. If r=1 they are absolutely
irreducible, and T2 gives degree at least four. If r=3, each has three
conjugate absolute factors over F8, each of multiplicity one at P.
These are smooth there; T1 makes their degrees at least two, so the
common F2-factor degree is a multiple of three and at least six.
The two alternatives cannot mix because the coordinate exchange
preserves absolute irreducibility and the field of definition.
This proves alternatives 2 and 3 and completes T4.

## Relation to literature, unsuccessful routes and limits

McGuire's full thesis, printed pp. 10–11 and 29, supplies the classical
Frobenius background and explicitly assumes F2-irreducibility in
Proposition 9. The tangent calculation is standard singularity data;
the present proofs reconstruct the individual-factor consequence and
the i=3 incidence alternatives. No novelty is claimed.

An intermediate whole-polynomial deduction from T3 would restrict the
possible constant-field degree sharply. That deduction does not advance
the known exponent classification: Hernando–McGuire already prove an
F2-defined absolute component for every nonexceptional exponent. For
an F2-irreducible whole polynomial that component is the whole
polynomial. This published component theorem is explicitly separated
from the stronger question of whole-polynomial irreducibility. It is
not used as a substitute for part (b).

T1–T4 exclude small factors and describe necessary local incidence;
they do not force an F2 factor for an arbitrary exponent, identify a
whole divisor, or decide whether every other component passes P.
The accepted phi13-divisibility criterion remains separate. The original
Janwa–Wilson general Kasami proof and Férard's exact full theorem remain
access gaps; the accompanying source audit describes what was actually
read and why no conclusion depends on the unverified later source
inference. No enumeration, CAS or large finite-field scan was used.

Freeze this candidate and obtain two fresh independent nonconstructor
audits before any coordinator acceptance.
