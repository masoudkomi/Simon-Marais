# A proposed all-field common-component saturation theorem

2026-10-17 UTC. **Candidate proof - unverified.** Constructor:
coordinator root. TWO OTHER fresh initially blind NONCONSTRUCTOR WHOLE
audits and coordinator reconciliation are required. Requested inherited
gpt-6.1-sol/max; independently verified effective settings unavailable.
This studies only B4(b). No annual classification or novelty is claimed.

Root constructed older KC/GK and reviewed IC1--IC4, but supplied no IC
construction inference. Those accepted results retain their own scopes.
The NEW argument here was constructed by root AFTER IC acceptance.
No worker's new proof inference is used. No mathematical program,
CAS, sample, exponent scan or source-certificate replay was run.

## 0. Domain and the proposed stronger conclusion

Work over K=the algebraic closure of F2. For odd j>=3 write

    f_j=X^j+Y^j+Z^j+(X+Y+Z)^j,
    R=(X+Y)(Y+Z)(Z+X),       phi_j=f_j/R.

The official question requires ordinary F2 factorization with both
factors positive degree, equivalently the specified coefficientwise
integer congruence with nonconstant reductions. Absolute factors alone
do not give that conclusion.

Fix k>=2, q=2^k, d=q^2-q+1. Proposed **CS1** is

    gcd_K(phi_d,phi_n) is either 1 or phi_d
    for EVERY odd n>=3.                              (CS1)

Equivalently, ANY one common absolute prime forces the WHOLE base
Kasami divisor. This includes every k, not only IC's transitive cases.
Combining with the accepted exact KC whole-divisor criterion gives
proposed **CS2**:

    gcd_K(phi_d,phi_n)=phi_d
      iff n=(q^(2r+1)+1)/(q+1), r>=1;
    otherwise gcd_K(phi_d,phi_n)=1.                   (CS2)

The normalized gcd statements also hold over F2. If valid, this would
exclude the proper A-only/B-only q16 alternatives left OPEN in IC4;
their earlier possibility list remains a valid weaker statement.
No old byte or proof status is changed by this candidate.

Janwa--Wilson J is NOT needed for CS1 or CS2. J is needed only to
translate the result into its published labelled-component language.
The original1993 proof remains unread and is not silently imported.
Lueroth's classical theorem is explicitly used in Section3; no
monodromy, finite-group classification, transversality, APN or Férard
irreducibility theorem is used. KC is used only in the final CS2 step.

## 1. Exact univariate coordinate, trace identity and root multiplicities

For every odd j there is a unique g_j in F2[U] such that

    t^j+(t+1)^j=g_j(t^2+t).                           (1)

Here is the elementary invariant argument, rather than an assumption
about composition of arbitrary factors. F2[t] is a free F2[U]-module
with basis1,t for U=t^2+t, by repeated division using t^2=t+U.
Uniqueness follows from the distinct parity of the leading degrees
of A(U) and t B(U). The left side is invariant under t->t+1.
For A(U)+tB(U), that involution adds B(U), so invariance forces B0.
This proves (1). For j>=3 odd, g_j has degree(j-1)/2 and is monic,
because the left side is monic of degree j-1.

Set

    T(U)=U+U^2+...+U^(q/2),
    S(U)=T(U)/U,
    F(U)=U S(U)^(q+1)=T(U)^(q+1)/U^q.                (2)

These are actual polynomials; the latter quotient is notation for the
first expression. T'(U)=1, S(0)=1 and deg S=q/2-1. The identity

    T(t^2+t)=t^q+t

telescopes. Since d+q=q^2+1, direct multiplication gives

    (t^d+(t+1)^d+1) t^q(t^q+1)
      =t^(q^2+1)+t^(q^2+q)+t^(q+1)+t^(2q)
      =(t^(q^2)+t^q)(t^q+t)
      =T(t^2+t)^(q+1).

Also (t^2+t)^q=t^q(t^q+1). Cancelling this NONZERO polynomial and
using injectivity of substitution U=t^2+t proves the exact identity

    g_d(U)=1+F(U).                                   (3)

F is the classical Muller--Cohen--Matthews trace-form polynomial
with parameters c1,d=q+1. The identity (3), and all properties needed
below, are proved here; no permutation/exceptionality theorem is used.

Its degree is

    N=1+(q/2-1)(q+1)=q(q-1)/2.                       (4)

Over K, T has q/2 distinct roots because T'=1. Thus F has EXACTLY
one simple root,0, and every other root has multiplicity q+1. The
nonzero roots of T are simple roots of S; S(0)=1 excludes an extra
zero. Also F'=S^q is nonzero, so g_d is separable. Do not confuse the
fiber multiplicity q+1 with the odd factor q-1 of degree N.

## 2. Geometric indecomposability from one fiber, for every k

Suppose F=A(B(U)) with A,B in K[U] of degrees greater than1.
Put b=deg B and c=B(0). Since0 is a SIMPLE root of F, c is a
simple root of A and0 is a simple root of B-c. Every other root
of B-c is a nonzero root of F, and because A is simple at c,
its multiplicity in B-c is EXACTLY q+1. Counting the whole degree
of B-c over the algebraically closed field gives

    b=1+j(q+1), j>=0.                                (5)

Also b divides N=(q/2)(q-1). Write

    b=2^a e,   0<=a<=k-1, e | (q-1), e odd.

If a0, then 1<=e<=q-1<q+1 and (5) gives e1, hence b1.
If a>=1, inversion of2^a modulo q+1 gives

    e congruent -2^(k-a) modulo q+1,
    e=q+1-2^(k-a),                                   (6)

because the displayed representative is in1,...,q-1. It is at least
q/2+1, greater than(q-1)/2. A positive divisor of q-1 greater than
half of q-1 must be q-1 itself. Thus e=q-1, (6) gives a=k-1,
and b=N. The only possible inner degrees are1 andN, both incompatible
with a nontrivial composition. Therefore F, and by translation (3)
also g_d, are indecomposable over K for EVERY k>=2.

This is a polynomial COMPOSITION assertion, not multiplication
irreducibility of phi_d. No odd-k exceptionality hypothesis occurs.
The even-k case has been proved directly by the same degree argument.

## 3. Classical intermediate fields and the common-pair lemma

We use the classical Lueroth theorem: every intermediate field strictly
larger than K in K(z), for z transcendental, is K(B(z)) for a rational
function B. It holds in arbitrary characteristic. An actual primary
two-page proof was read; the theorem is an attributed foundational
input, not a newly claimed theorem. The polynomial consequence and
the following common-pair argument are included explicitly.

**Polynomial intermediate-field consequence.** If f in K[z] is
indecomposable and nonconstant, then the only intermediate fields
between K(f(z)) and K(z) are the endpoints. Indeed an intermediate
field is K(B(z)) by Lueroth, and f=A(B(z)) for rational A,B.
The nonconstant map f:P1->P1 has ONLY the pole infinity. Every pole
of A has a nonempty fiber under the surjective rational map B, and
the union of these fibers is the pole set of f. Consequently A has
one pole c and B^(-1)(c) consists of infinity alone. A fractional
linear change sending c to infinity makes BOTH A and B polynomials,
without changing their degrees or the generated field. A proper
intermediate field would give both degrees>1, contradicting polynomial
indecomposability. Nonconstant rational maps are surjective over K:
their homogeneous numerator-minus-value-times-denominator has a
projective zero, including at infinity. No characteristic-zero or
tameness hypothesis is used.

**Common-pair lemma.** Let f be an indecomposable polynomial in K[z]
of degree>1, and h any polynomial. Suppose a,b in a common extension
field are transcendental over K, a!=b, and

    f(a)=f(b),       h(a)=h(b).                       (7)

Then h=H(f) for a polynomial H in K[z]. To prove it, put
E=K(f(a),h(a)) inside K(a). The substitution a->b defines an
isomorphism K(a)->K(b), since both elements are transcendental.
By (7) it fixes every element of E, as an equality in the common
extension field. If E=K(a), it would fix a but also send it to b,
contradiction. Thus E is a PROPER intermediate field. The preceding
consequence forces E=K(f(a)), so h(a)=H(f(a)) for rational H.
If H had a finite pole c, a finite root of f(z)-c would give a finite
pole of h(z), impossible. Thus H is polynomial. Transcendence of a
makes this an identity in K[z].

The lemma concerns a GENUINE common pair in one function field.
It does not descend an arbitrary irreducible factor through a cover,
nor assert that composition indecomposability itself is ordinary
polynomial irreducibility. No Galois-closure/group classification is
needed for this elementary application of the classical field theorem.

## 4. A common projective component gives exactly such a pair

Assume a nonconstant common factor of phi_d and phi_n over K.
Choose a common homogeneous irreducible prime P. It is NOT X+Y.
One can either use accepted IC1 gcd(R,phi_d)=1, or check it directly:
put Y=X+e in f_d=R phi_d and compare the coefficient of e. The
restriction of phi_d to e0 equals

    (X^(d-1)+Z^(d-1))/(X+Z)^2,

which is a nonzero polynomial. Hence X+Y is not a factor.

Use the projective affine chart X+Y=1 with

    X=t, Y=t+1, Z=u,
    A=t^2+t, B=u^2+u.

For every odd j>=3 let

    D_j(V,W)=(g_j(V)+g_j(W))/(V+W).

The numerator is divisible by V+W, so this is an actual polynomial.
The EXACT chart identity, with no residual multiplier, is

    phi_j(t,t+1,u)=D_j(A,B),                          (8)

because R(t,t+1,u)=(t+u)(t+u+1)=A+B and the numerator is
g_j(A)+g_j(B). A non-X+Y homogeneous prime dehomogenizes to a
nonconstant irreducible polynomial on this chart. Let C be its
function field; it has transcendence degree1 over K. In C put

    a=t^2+t, b=u^2+u.

Both are transcendental. For if a were constant, the identity
D_d(a,b)=0 would make b algebraic over K: as a polynomial in its
second argument D_d(a,W) has degree N-1 and leading coefficient1,
so it is not the zero polynomial. Then t and u would also be
algebraic over K from their quadratic equations. Since K is
algebraically closed, C would have transcendence degree0, impossible.
The same reasoning or f(a)=f(b) treats b.

Moreover a!=b. The elementary diagonal identity

    D_d(V,V)=g_d'(V)=S(V)^q

is nonzero at transcendental a. Equality a=b would contradict
D_d(a,b)=0. Notice that this check removes the diagonal ambiguity
of the quadratic coordinates rather than assuming an arbitrary
factor descends faithfully.

The two common chart equations now give

    g_d(a)=g_d(b),       g_n(a)=g_n(b).

Section2's geometric indecomposability and the common-pair lemma
therefore imply

    g_n=H(g_d), H in K[T].                           (9)

In fact H is over F2. Coefficient Frobenius fixes g_n,g_d, so it
fixes H by uniqueness of substitution into a nonconstant polynomial.
Frobenius-fixed coefficients of K are exactly F2. This field descent
is separate from the original common absolute factor.

## 5. Whole homogeneous division and the exact progression

For (9), g_d(V)+g_d(W) divides g_n(V)+g_n(W): the usual difference
of two values of H has its argument difference as a factor, in
characteristic2 as well. Cancelling the common V+W gives

    D_d(V,W) | D_n(V,W).

By (8), the WHOLE phi_d divides phi_n on the chart X+Y=1.
Equivalently division holds in the localization at X+Y. Since
X+Y is coprime to phi_d, unique factorization implies the same
division in K[X,Y,Z], including all prime multiplicities. The
quotient is over F2 by Frobenius uniqueness again. This proves
CS1: any nonconstant gcd has forced the entire phi_d.

Only NOW apply the separately accepted KC criterion, whose actual
domain is k>=2, odd n>=3 and WHOLE phi_d division. It gives exactly
the progression in CS2; the accepted GK/KC converse supplies whole
division for every such r. Otherwise the gcd is1 even over K.

In the labelled language of attributed J, every individual P_(q,alpha)
or ordinary F2 Frobenius-orbit factor therefore has the SAME occurrence
criterion, for ALL k>=2. Core CS1--2 did not use J. For q16, the
proper A-only/B-only cases are consequently impossible IF this new
candidate passes both full audits. No change to the earlier IC proof
or its honest then-unresolved boundary is made.

## 6. Endpoints, actual progress and source limits

n1 is zero and cannot supply the official positive-degree product;
n3 is a unit. They are not silently inserted into CS1--2's domain.
q2 is excluded: its base phi3 is a unit, g3 is linear, and the
proposed nontrivial base-component conclusion has no content there.
r0 gives n1 and is excluded. r1 is whole equality with unit cofactor;
it does NOT by itself give two official factors. Published J supplies
the separate ordinary orbit factorization when appropriate. r>=2
has the accepted GK positive-degree cofactor and coefficientwise
integer lifts. Nothing here constructs a new exponent family.

CS1--2 classifies common components with a BASE Kasami polynomial.
It does not classify arbitrary factors of phi_n, all higher GK
components, or all ordinary reducible exponents. The annual question
remains open. A failure of every base test is not irreducibility.

The MCM trace formula and Lueroth/intermediate-field mechanism are
classical and attributed. A full priority search is not complete.
Janwa--Wilson1993 original proof and Férard2014 full theorem remain
unread; no conclusion is taken from their abstracts. No source's
odd-k exceptionality, APN, monodromy or later parity/transversality
assertion is a premise. The new mathematical claims above remain
UNVERIFIED until TWO OTHER fresh WHOLE nonconstructor audits.
