# Independent whole audit of structural reasoning T1--T4

2026-10-16--17 UTC. Reviewer: `review_2017_coarsening_r1`. Constructor:
`review_2021_reasoning_j15_r2`. **Initial blind whole report, frozen before
peer comparison.** I did not construct this proof and have read no peer
structural review or its conclusions. Requested settings: `gpt-6.1-sol`
and `max`; effective settings have no verified readback.

Candidate: `../notes/structural-reasoning-r2-candidate-v1.md`, SHA-256
`0c451d5f9410573625725bc6be35af91fe938deee4dc1d92910572374dc69f52`.
I read the complete candidate, six-artifact freeze manifest, source audit,
research log, source JSON, freeze script and freeze output. The script was
read, not executed. Every frozen artifact was independently fingerprinted.

## Verdict and exact scope

I found no substantive mathematical defect in T1--T4. I recommend
accepting them as the stated **partial structural restrictions**, after
the coordinator reconciles a second independent whole audit. No author
repair is requested. This report reconstructs all four proofs rather
than relying on a few sample exponents or the constructor's calculations.
No enumeration, CAS or finite-field scan was used.

The domain is odd n of binary weight at least3. In particular n>=7.
T3 additionally uses i=v2(n-1)>=2. T4 is specifically i=3, namely
n=8*ell+1 with ell>=3 odd; its conclusion is a necessary local trichotomy,
not a claim that all three alternatives occur, nor that every global
factor passes through P. The result does not classify all exponents,
force a factorization for every such n, or solve the annual question.
No novelty is established. The contextual Kasami decomposition and
whole-phi13 criterion are not premises of T1--T4.

## Official domain, quotient and boundary audit

I checked page2, B4(b), of the current public [2024 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf)
and visually inspected the cached page. It asks for odd positive n,
integer polynomial factors, and coefficientwise congruence modulo2 with
both remaining factors nonconstant modulo2. The text explicitly defines
that congruence. This is a polynomial-ring question, not equality of
functions on F2³. I did not investigate or reproduce the preliminary
infinite-family construction.

In F2[X,Y,Z], each diagonal line is a prime divisor of f_n because
substitution of equal coordinates gives the zero polynomial. The three
lines are distinct, so their product R divides f_n. For odd n>1 the
quotient phi_n is nonzero homogeneous of degree n-3. Nonvanishing also
follows directly from the local expansion below. A factorization of
phi_n into two nonconstant F2 polynomials is equivalent to the requested
integer congruence, by reduction and coefficient lifts in{0,1}. A
factorization over an extension field alone does not suffice.

The candidate excludes the boundary cases explicitly by its binary-weight
hypothesis. At n1 the numerator is zero, whereas R times two nonconstant
reductions cannot vanish in an integral domain; zero itself is constant
modulo2. At n3 the quotient is1, so the target also fails. No deduction
here extends T1/T2 to binary-weight2 exponents: that omitted domain is
essential. In T4 the condition ell>=3 excludes n9, and ell odd makes
v2(n-1) exactly3 rather than merely at least3. The smallest T4 exponent
is25. The i1 case is used only for the point pattern, not for the descent
theorem whose point P must lie on the curve.

Every irreducible factor of a homogeneous polynomial is homogeneous.
For example minimum and maximum total degrees add in a domain, so if
a product has only one degree then both factors do. This justifies all
homogeneous line, curve and degree arguments in the candidate, including
absolute factors. Component scalars are removed by a fixed monomial-order
leading coefficient normalization.

## T1 reconstructed: arbitrary absolute line restriction

Work in k=Fbar2. Any line factor of f_n has, after a coordinate
permutation and scalar normalization, equation X+aY+bZ. Its restriction
is the polynomial identity

    (aY+bZ)^n+Y^n+Z^n+((a+1)Y+(b+1)Z)^n=0.            (1)

For every supported middle binomial index0<j<n,

    a^j b^(n-j)+(a+1)^j(b+1)^(n-j)=0.                (2)

The indices1 and n-1 are supported because n is odd. At j1, a0
forces b1 and a1 forces b0; at j=n-1, b0 forces a1 and b1 forces a0.
Here n-1>0, so no exponent-zero exception occurs. These possibilities
give only prescribed diagonal lines. This checks every zero numerator
or denominator before introducing ratios.

Now assume a,b are both outside{0,1}. Put

    A=a/(a+1), B=b/(b+1), T=A/B.

All quantities divided by are nonzero. Equation(2) gives B^n T^j=1.
Choose a nonzero set bit h=2^s of n besides bit0. A third set bit
exists; hence both1 and1+h lie strictly between0 and n. The identity
(1+t)^n=product over set bits e of(1+t^(2^e)) proves their binomial
coefficients are1 in F2, without a numerical binomial test. Dividing the
two equations gives T^h=1. Since h is a power of2, (T+1)^h=0 and T=1
in the field k. Thus A=B, which by cross multiplication gives a=b,
and the equation at j1 gives B^n=1.

But the Y^n coefficient in(1) is a^n+(a+1)^n+1. Its first two terms
are equal because B^n=1, so the coefficient is1, a contradiction. No
restriction on the coefficient field of the hypothetical line was
silently imposed: a,b were arbitrary algebraic-closure elements.

Thus the only line factors of f_n are the prescribed three. Each has
multiplicity exactly1. Modulo X+Y, the derivative with respect to X is
Y^(n-1)+Z^(n-1), a nonzero polynomial for n>1. If(X+Y)² divided f_n,
this derivative would vanish modulo X+Y. Coordinate symmetry treats the
others. Therefore dividing by R removes every absolute line factor,
including the possibility of an additional diagonal copy. T1 follows.

The argument is coefficientwise throughout. In particular it never
deduces a polynomial identity from evaluation on the finite field.

## Point pattern and full ordinary tangent cone

There are7 points of P²(F2). Apart from P=(1:1:1), coordinate symmetry
gives representatives(1:0:0) and(1:1:0). At the first, both partial_Y f_n
and partial_Y R are1. At the second, both partial_X f_n and partial_X R
are1. Since R=0 at these points, differentiating f_n=R phi_n gives
phi_n=1 at each of the6 points. This use of derivatives avoids dividing
the zero values of f_n and R at finite-field points.

For P use X=1+U,Y=1+V,Z=1 and write n=q*ell+1, q=2^i, ell odd.
For i>=1,

    (1+T)^n=(1+T)(1+T^q)^ell
            =1+T+T^q+T^(q+1)+terms of degree>=2q.

The numerator is the sum of the expansions at U,V,0,U+V. Constants,
linear terms and q-th powers cancel. Since q+1<2q, its first nonzero
homogeneous part is U^q V+UV^q, of degree q+1. The denominator is
exactly UV(U+V), of degree3. As the local polynomial quotient exists,
its first nonzero homogeneous part is

    C_i=(U^(q-1)+V^(q-1))/(U+V)
        =product_(alpha in Fq minus{0,1})(U+alpha V).     (3)

For i1 this is1 and phi_n(P)=1, so there is no F2 projective zero.
For i>=2 it has degree q-2>0 and P is the unique F2 projective zero.
All q-2 directions are distinct. There are no F2 directions: the
horizontal and diagonal possibilities alpha0,1 were removed, and the
vertical direction is absent as well. Hence an F2 factor through P
cannot have multiplicity1; its linear tangent would be defined over F2.

For a product, local lowest homogeneous terms multiply and orders add.
Consequently a component through P has a tangent cone consisting of a
subset of(3), different components have disjoint tangent sets, and no
factor through P can occur repeatedly in phi_n. None of this says that
a global factor avoiding P cannot exist.

## Point-free quadratics and cubics: complete hand classification

A point-free homogeneous polynomial over F2 must have value1 at all7
projective points. For a quadratic, coordinate points force all3 square
coefficients to1 and pair points force all3 mixed coefficients to1.
At P the resulting value is3+3=0, contradiction. Thus there is no
point-free homogeneous quadratic.

For a cubic, coordinate points force coefficients of X³,Y³,Z³ to1.
Each pair point forces the two coefficients in the corresponding pair
{X²Y,XY²}, {X²Z,XZ²}, {Y²Z,YZ²} to sum to1. At P the cube terms
and these3 pair sums cancel, so the XYZ coefficient must be1. The
three independent pair choices are free. Thus there are exactly8
point-free cubic **polynomials**, not just a count of polynomial functions.

Let(a,b,c) be any ordered F2 basis of F8 and L=aX+bY+cZ. Its norm

    N(L)=L sigma(L) sigma²(L)

is a homogeneous cubic over F2. For any nonzero F2-vector v, the basis
condition gives L(v)!=0 and N(L)(v)=L(v)^7=1. Thus each norm is one
of those8 point-free cubics. The3 conjugate lines are pairwise
nonassociate: if sigma^j(L)=sL, j1 or2, every ratio of its nonzero
coefficients is fixed by sigma^j on F8, hence lies in F2, contradicting
the basis condition.

There are7*6*4=168 ordered bases. Unique factorization says that
N(L')=N(L) precisely when L'=s sigma^j(L) for s in F8* and j0,1,2.
The scalar is in F8 by comparison of a nonzero coefficient, and its
norm is s^7=1. All21 such choices are distinct by the nonassociate
property. They remain bases. Thus there are168/21=8 distinct norm
polynomials. They exhaust the coefficient count, proving every point-free
F2 cubic is a product of3 conjugate absolute lines.

This is a complete mathematical counting proof. It does not require an
enumeration of8 examples, computer factorization or a point-count bound.
The distinction between equal values and equal polynomials is explicit:
UFD proves the norm polynomials distinct, and the coefficient constraints
prove there are exactly8 candidates having those values.

## T2 reconstructed: no factor of degrees1--3 over F2

T1 excludes degree1. Let H be an F2-irreducible factor of degree2 or3.
If it has no F2 projective point, the quadratic result rules it out or
the cubic result gives an absolute line divisor of H and hence phi_n,
contradicting T1. Thus H has an F2 point. The point pattern forces
i>=2 and that point is P.

The absence of F2 tangent directions forces m_P(H)>=2. Always
m_P(H)<=deg H. If equality held, translate P to the affine origin;
the resulting degree-d polynomial consists solely of its homogeneous
degree-d part in two variables. Over the algebraic closure this splits
into linear forms. Homogenizing back gives projective line factors of
H and phi_n, contrary to T1. This excludes degree2 and the multiplicity3
degree3 case.

Only a cubic H of multiplicity2 remains. Its quadratic tangent cone
has no F2 direction, as it divides(3). Restrict to any F2 projective
line through P. The line is not a component by T1, so the restriction
is a nonzero homogeneous binary cubic. Its zero at P has **exact**
multiplicity2, since the tangent cone is nonzero on this F2 direction.
Dividing off that double root leaves a homogeneous linear form over F2,
with a rational zero Q different from P. Hence H(Q)=phi_n(Q)=0,
contradicting uniqueness of the rational point. No point at infinity is
lost: this is a projective binary restriction. This proves T2, including
irreducible cubics that are not absolutely irreducible.

The equivalent divisor formulation is valid: a positive-degree F2
divisor of degree<=3 would contain an F2-irreducible factor of such
a degree. It does not assert that all irreducible factors are absolute.

## T3 reconstructed: individual component coefficient field

Let i>=2 and H be an F2-irreducible factor with H(P)=0. Normalize
absolute factors by leading coefficient1 in a fixed monomial order.
Their coefficients lie in some finite field and Frobenius permutes them.
The action is transitive: an orbit product is fixed by Frobenius, hence
lies in F2[X,Y,Z], and a proper orbit product would be a proper factor
of H over F2. Since one absolute factor vanishes at P and P is rational,
all its conjugates do; by transitivity every absolute factor passes P.
The squarefree cone also excludes any repeated absolute factor here.

For one absolute factor G let the orbit length be r. Fixing its normalized
polynomial by sigma^r is equivalent to defining it over F_(2^r); minimality
of r makes this its **minimal** coefficient field. All conjugates have
the same degree e and the same local multiplicity mu, so

    deg H=r e,          m_P(H)=r mu.                    (4)

Choose any tangent U+alpha V belonging to G, and let alpha have exact
degree d over F2. Equation(3) puts alpha in F_(2^i), so d|i.
Frobenius^d fixes this normalized tangent and sends G to another absolute
factor of H having it. If that factor differed from G, the global cone
would contain the same direction twice, impossible. Thus sigma^d(G)=G
and r|d. Repeating the argument for every tangent proves the stated
divisibility for each tangent-field degree, not just their union.
Together with(4) this yields

    r | gcd(i,deg H,m_P(H)).

The argument applies to an individual F2-irreducible factor even when
the whole phi_n is reducible. It does not assume all global factors
pass P or use a singular point as though it were nonsingular. Its
essential additional hypothesis is the proved squarefree tangent cone,
which supplies uniqueness of the absolute component for each direction.

## T4 reconstructed: exact v2(n-1)=3 local alternatives

Now q8 and the six directions have exact field F8. Direct multiplication
gives

    C_3=A B,
    A=U³+U²V+V³, B=U³+UV²+V³.

Each binary cubic has no root at0,1 or infinity, hence is irreducible
over F2. Any F2-irreducible factor through P has a nonconstant F2
tangent-cone divisor of AB, so its cone is A, B or AB. Squarefreeness
therefore leaves exactly1 or2 such factors. There is at least1 because
phi_n(P)=0. All other factors avoid P. Swapping X,Y swaps U,V and
exchanges A with B.

**One factor H through P.** Its cone is AB and m_P(H)=6. By T3 its
absolute-factor orbit length is r1 or3. Every coordinate permutation
preserves the unique F2 component through P and acts on its r absolute
factors. That action commutes with Frobenius, since the coordinate
permutations are defined over F2. The centralizer of a transitive r-cycle
on r objects is its cyclic group; in particular the image of S3 here
is abelian. Its commutator subgroup A3 fixes each absolute component.

For the coordinate cycle(X,Y,Z)->(Y,Z,X), the actual local map is

    (U,V) -> ((U+V)/(1+U), U/(1+U)),

whose linear part is(U+V,U), as in the candidate. Its projective tangent
action has fixed directions solving T²+T+1=0, lying in F4. Since
F4 intersect F8 equals F2 and those roots are not in F2, none of the
six directions is fixed. They form orbits of length3. A stable absolute
component must contain a union of these orbits in its tangent set,
so its multiplicity is divisible by3. If r3, equation(4) would give
mu=6/3=2, contradiction. Hence r1 and H is absolutely irreducible.
Its degree is at least6 from the multiplicity, and equality6 would
make it a union of lines by the same translated homogeneous argument
used in T2. T1 excludes that; thus deg H>=7. This is alternative1.

**Two factors H1,H2 through P.** Their cones are A and B, so each
has multiplicity3. The swap X,Y exchanges the cones and therefore the
actual global F2 components. Their degrees agree. The induced action
S3->S2 is nontrivial, hence its kernel is A3 and all odd permutations
exchange them. This action cannot send a component through P to a
factor avoiding P, because P is fixed by every coordinate permutation.

For each Hi, T3 gives r1 or3. Coordinate exchange is an F2-defined
automorphism, so it preserves the number and minimal fields of absolute
factors; both Hi have the same r. A mixed absolute/norm pair is thus
excluded. If r1 both are absolutely irreducible and T2 gives their
common degree>=4, which is alternative2. If r3, each splits into3
distinct conjugate absolute components of minimal field F8, and(4)
gives multiplicity1 for each at P. They are smooth **at P**. Each has
degree>=2 by T1, so each Hi has degree divisible by3 and at least6.
This is alternative3. It makes no claim of global smoothness.

The three cases are exhaustive and mutually exclusive by the number
of F2 components through P and their geometric splitting. Repeated
factors, shared tangent directions, a third F2 component through P and
mixed values of r have all been excluded with explicit reasons.

## Primary sources, exact hypotheses and attribution

No cited external theorem is needed to fill a T1--T4 inference: the
finite-field, UFD, multiplicity and group-action facts were reconstructed
above. The source audit nevertheless matters for the surrounding claims.

I visually checked McGuire's thesis printed pp10--11,29,35--37 from the
full cached scan. Proposition B separates a nonsingular-point assertion
from assertions needing base-field irreducibility. Proposition9 on p29
expressly assumes whole-polynomial F2-irreducibility. The candidate does
not use it to establish that assumption. The n57 example on pp36--37
records six absolute degree9 factors over F8 grouped into two F2
irreducibles of degree27, with both having multiplicity3 at P. This
matches alternative3. These are attributed context, not new computations.

The full [Hernando--McGuire paper](https://arxiv.org/pdf/0903.2016)
states the F2-defined absolute-component result outside Gold and
Kasami--Welch exponents. I checked §2.1, §4 and Theorems15--16 in §5:
the former irreducibility implication has an explicit irreducibility
hypothesis; the component theorem removes it. Thus the candidate correctly
treats whole-polynomial implications outside those families as subsumed
by published work. Existence of one absolute F2 component does not
establish whole-polynomial absolute irreducibility or the desired
reducibility classification.

I checked [Delgado--Janwa v1](https://arxiv.org/pdf/1612.05997v1),
§3 equations(5)--(6), and visually read PDF pp7--9. It records the
attributed Janwa--Wilson decomposition and normalized specialization.
The specialization's coefficient of X^q is alpha; Frobenius sends its
label to alpha², so the minimal field is the field generated by alpha,
as the audit says. The later parity step in Lemma1 indeed makes the
invalid inference from t_A*t_B+t_A+t_B=1 to both parities being1.
The displayed example A=1+X+Y, B=1+XY verifies the objection by hand.
This refutes that inference, not the Kasami decomposition or the truth
of its later theorem. T1--T4 do not import that inference or an assertion
that all global components pass P.

The unread original JW1993 proof and Férard full theorem remain access
limitations, accurately labeled as such. I did not repeat the recorded
failed network requests or infer hypotheses from a zero-byte PDF.
The retained failed artifact is actually empty. These limitations do
not obstruct the self-contained T1--T4 proofs. The accepted whole-phi13
criterion and its family were checked only as contextual accepted
registers; neither is a dependency of this theorem and neither was
reproved here. No source novelty or complete classification claim is
supported or requested.

## Adversarial outcome and remaining work

I searched conceptually for failures from arbitrary closure-field line
coefficients, zero ratios, loss of the third binary bit, repeated diagonal
factors, polynomial/function confusion, incomplete cubic norm counting,
projective points at infinity, repeated absolute factors, coefficient-field
normalization, singular-point descent, the projective local group action,
and unexamined components away from P. All are covered by the displayed
arguments. The full candidate and supporting packet present no unresolved
substantive issue and require no repair.

The remaining research gap is global: T1--T4 do not determine whether
phi_n is reducible for arbitrary n, and do not describe components
avoiding P. Their scope must remain the stated partial structural result.

Only assigned `structural-review-1*` review files and temporary read-only
PDF renderings were written. No candidate, shared status, other review,
Git state or cached paper was changed. All earlier frozen packets were
preserved. Fresh authoritative account-wide telemetry during this review
reported18% total weekly used, window10080 minutes, reset1792745187,
below the90% total-used ceiling. Hash manifests and source inspection
details accompany this initial blind report.
