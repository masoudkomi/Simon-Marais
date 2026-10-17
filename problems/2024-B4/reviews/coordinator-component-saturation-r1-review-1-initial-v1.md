# Initially blind WHOLE review R1 of component saturation CS1–CS2

2026-10-17 UTC. Reviewer: `/root/review_2021_reasoning_j15_r2`.
This is a complete NONCONSTRUCTOR WHOLE initial audit, finished before
reading any new peer CS report, ledger, source record, manifest or finding.
Requested inherited settings: gpt-6.1-sol/max. Independently verified
effective-setting readback is unavailable. Only the coordinator can promote
the submission after both independent audits and reconciliation.

## Verdict and exact review boundary

I find no substantive mathematical defect in CS1 or CS2 in the stated
domain: every k>=2, q=2^k, d=q²−q+1, and every odd n>=3. The proof really
upgrades one common absolute component to the WHOLE base Kasami divisor.
The exact progression then uses the separately accepted KC theorem in its
whole-divisor domain. The review recommends scoped acceptance after the
other whole audit and coordinator reconciliation; it is not a promotion.

The new steps checked here are the trace identity, the ALL-k composition
indecomposability argument, the polynomial intermediate-field consequence
of classical Lüroth, the actual common-pair construction on a projective
component, and globalization with multiplicities. No Janwa–Wilson factor
theorem is needed by those steps. The optional labelled interpretation
retains the separately attributed published input in accepted IC.

I authored old T1–T4/C7/C11 and IC1–IC4 and reviewed earlier CP/GK/KC/CJ/
DI/NJ/HR packets. In particular, accepted IC is my earlier construction,
supported by TWO OTHER whole audits; this report does not count as an
independent recertification of IC. I did not construct, suggest, repair or
contribute any NEW CS trace identity, multiplicity argument, common-pair
lemma or globalization inference. The direct exclusion of X+Y in the new
proof makes even the optional IC1 shortcut unnecessary for the core result.

The complete nine-artifact submission, all thirty obligations, all failed
routes and source limits were read. The companion issue ledger contains
forty inference checks covering every obligation. The three exact accepted
KC/GK/IC bodies and their acceptance records were read in full. This review
does not infer a complete annual answer, irreducibility from a failed base
test, or priority. No mathematical program, CAS, exponent scan, finite-field
test, constructor script or old mathematical certificate was run.

## 1. Official target and invariant polynomial

The official B4(b) asks for coefficientwise congruence modulo two with TWO
integer polynomials whose reductions are nonconstant. For odd n>=3 this is
ordinary factorization of the nonzero homogeneous phi_n=f_n/R over F2.
Absolute splitting alone would not suffice. The source was freshly checked
in the official Paper B, page2, B4(b), including the two definitions of
congruence and constant modulo two. No preliminary-part research is used.

Put U=t²+t. Every polynomial in t has a unique expression A(U)+tB(U):
repeatedly use t²=t+U, and observe that the two possible leading degrees
are even and odd and therefore cannot cancel. The transformation t↦t+1
fixes U and changes this expression by B(U). Consequently the invariant
t^j+(t+1)^j is exactly g_j(U). For odd j>=3 its leading term is t^(j−1),
since the highest t^j terms cancel and the next binomial coefficient j is
one. Thus g_j is an actual monic polynomial of degree (j−1)/2, not merely
a rational function or a finite-field function. Substitution by U=t²+t is
injective by its effect on degree.

## 2. Exact trace identity and ALL-k indecomposability

Let T=Σ_(i=0)^(k−1) U^(2^i), S=T/U, and F=U S^(q+1). These are
polynomials, S(0)=1, deg S=q/2−1, and T'=1. The telescoping substitution
gives T(t²+t)=t^q+t.

I checked the displayed four-term identity independently by multiplying
the three summands separately. Because d+q=q²+1 and (t+1)^q=t^q+1,
the first two summands each contribute t^(q²+q+1), and these cancel. The
two remaining t^q terms also cancel. What remains is exactly

    t^(q²+1)+t^(q²+q)+t^(q+1)+t^(2q)
      =(t^(q²)+t^q)(t^q+t)=(t^q+t)^(q+1).

Also U(t)^q=t^q(t^q+1), which is a NONZERO polynomial. Cancellation
in F2[t] and injective substitution therefore give

    g_d=1+F,             deg F=N=q(q−1)/2.

No specialization at a zero of the canceled polynomial is excluded from
this polynomial identity. The quotient notation T^(q+1)/U^q denotes the
already displayed polynomial U S^(q+1).

Since T'=1, T has q/2 distinct roots in K. Removing its single zero root
gives the simple nonzero roots of S. It follows that F has one simple
zero at0 and every other zero has EXACT multiplicity q+1. Differentiating
U S^(q+1) yields S^q(S+U S')=S^q T'=S^q. In particular g_d' is nonzero.
Even if “separable polynomial” is taken to mean squarefree rather than a
separable polynomial map, the assertion here is true: at a zero of S,
g_d=1, so gcd(g_d,g_d')=gcd(1+U S^(q+1),S^q)=1. A nonzero derivative
alone would not prove squarefreeness for an arbitrary polynomial; this
extra identity removes that possible ambiguity without affecting the proof.

Suppose F=A∘B, with both degrees>1, and set c=B(0), b=deg B. The local
multiplicity formula at0 is

    1=mult_c(A) · mult_0(B−c).

Both multiplicities are therefore1. Every other root of B−c is a nonzero
root of F and has multiplicity q+1 in B−c, because A is simple at c.
Counting ALL roots with multiplicity in this one fiber over the
algebraically closed field gives b=1+j(q+1). Separability, tameness or
generic ramification assumptions are unnecessary. Also b|N by degrees.

Write b=2^a e with a<=k−1 and e an odd divisor of q−1. If a=0, the
congruence b≡1 mod(q+1) with 1<=e<=q−1 forces e=1. If a>=1,

    2^a · (−2^(k−a)) = −q ≡1 mod(q+1).

Thus e is the unique representative q+1−2^(k−a) in [1,q−1]. Its size is
at least q/2+1, greater than (q−1)/2. A positive proper divisor of q−1
cannot be this large. Hence e=q−1, then 2^(k−a)=2, a=k−1, and b=N.
The only possible inner degrees are1 and N. Neither permits both A and B
to have degree>1. This proves geometric polynomial indecomposability for
EVERY k>=2, including k even and the first k=2 endpoint. Translation of
the outer value gives the same conclusion for g_d=1+F. The proof never
confuses multiplicity q+1 with the odd degree factor q−1.

## 3. Lüroth, the one-pole conversion and the common-pair lemma

The external input is the classical Lüroth theorem over an arbitrary
field. I read Bensimhoun's complete two-page authored proof and statement;
it imposes no characteristic-zero or separability condition. Its use in
characteristic2 is legitimate. No Ritt or monodromy classification is
substituted for it.

Here is the full consequence needed by the new proof. If
K(f(z))⊆E⊆K(z), with f a nonconstant indecomposable polynomial, Lüroth
writes E=K(B(z)) for a rational B, and f=A∘B for a rational A. A
nonconstant rational map P1→P1 is surjective over K, including in
inseparable characteristic: each projective fiber is the zero set of a
nonzero homogeneous form of positive degree. Pulling back a pole of A
produces a pole of f; local pole orders multiply and cannot cancel.
Since f has the one pole infinity, A has exactly one pole c and the
whole fiber B^−1(c) is supported at infinity. A fractional linear
change μ taking c to infinity makes μ∘B and A∘μ^−1 polynomials.
Degrees and E are unchanged. A field strictly between both endpoints
would make both degrees>1, contradicting indecomposability. This argument
works for finite c, c=infinity, wild ramification and inseparable maps.

For the common-pair lemma, take transcendental distinct a,b in ONE common
extension field, with f(a)=f(b) and h(a)=h(b), and let
E=K(f(a),h(a)). Evaluation a↦b is a genuine K-isomorphism K(a)→K(b).
It fixes each rational expression in the two equal values. Therefore E
cannot be K(a): if a were a rational expression in f(a),h(a), its
denominator would remain nonzero under this isomorphism and substitution
would give a=b. This also directly verifies the candidate's fixed-field
argument when K(a) and K(b) have not themselves been identified.

The only remaining intermediate field is K(f(a)), so h(a)=H(f(a)) for
a rational H. If H had a finite pole c, the nonconstant polynomial f−c
would have a finite root in K. The pole of H would pull back there with
positive order, making h have a finite pole. Thus H has no finite poles
and is polynomial. Finally transcendence of a makes h=H(f) an identity
in K[z]. Constant h causes no difficulty. The proof really needs a
distinct transcendental pair, not an arbitrary divisor descended through
a cover; the next step supplies exactly that pair.

## 4. Actual projective component and the two curve functions

A common nonconstant factor of the two homogeneous polynomials has a
common homogeneous irreducible factor P. Factors can be taken homogeneous
because highest and lowest total degrees add under products in a domain.
The factor X+Y is absent from phi_d. Directly, put Y=X+e. The coefficient
of e in f_d is X^(d−1)+Z^(d−1), and in R phi_d it is
(X+Z)² phi_d(X,X,Z). The numerator is nonzero, so the stated restriction
is a nonzero polynomial. This proves the required coprimality without
using the reviewer's old IC construction.

Write ell=X+Y and use X=t ell, Y=(t+1)ell, Z=u ell. The localized ring
is K[t,u,ell,ell^−1]. A homogeneous prime other than ell becomes
ell^deg(P) times a nonconstant irreducible polynomial Pbar(t,u). If Pbar
were a unit, P would be a power of ell; if Pbar factored, localization
and homogenization would contradict primality of P. Thus
C=Frac(K[t,u]/(Pbar)) is an actual curve function field of transcendence
degree1. It is not merely an individual finite intersection point.

On ell=1, put a=t²+t and b=u²+u in C. With
D_j(V,W)=(g_j(V)+g_j(W))/(V+W), the chart identity is EXACT:

    R(t,t+1,u)=(t+u)(t+u+1)=a+b,
    phi_j(t,t+1,u)=D_j(t²+t,u²+u).

It follows by a polynomial identity, so it remains valid even along
a+b=0; no pointwise division there has been assumed.

For EVERY c in K, D_d(c,W) is monic of degree N−1: its numerator
g_d(W)+g_d(c) is monic of degree N, and its divisor W+c is monic of
degree1. Since N>=6, this is a nonzero polynomial. If a were algebraic
over K it would be in K, and D_d(a,b)=0 would force b algebraic. The
equations for t and u would then make both algebraic, contradicting
trdeg C=1. The same argument interchanging a,b proves both transcendental.

The diagonal identity D_d(V,V)=g_d'(V)=S(V)^q now matters. A nonzero
polynomial over K cannot vanish at transcendental a. Hence a=b would
contradict D_d(a,b)=0. This removes both possible diagonal lifts t=u and
t=u+1, and any other supposed diagonal collapse of the quadratic
coordinates. The two actual common component equations therefore give

    g_d(a)=g_d(b),       g_n(a)=g_n(b),       a!=b.

All hypotheses of the common-pair lemma have now been checked inside
ONE function field. Its conclusion is g_n=H(g_d), H∈K[T]. Coefficient
Frobenius fixes g_n,g_d, and substitution into a nonconstant polynomial
is injective. Therefore σ(H)=H and the coefficients of H lie in F2.
This is a coefficient-field descent, not an assertion that the original
absolute component was defined over F2.

## 5. Whole division, multiplicities and the exact gcd

For a polynomial H the two-value difference is divisible by its argument
difference. Thus, as an identity in K[V,W],

    D_n(V,W)=D_d(V,W) · Q(g_d(V),g_d(W))

for an actual polynomial Q. This gives whole division on ell=1 after
substitution; no claim about faithfully descending an arbitrary factor
has been inserted. Restoring the homogeneous degrees gives a quotient
in K[X,Y,Z,ell^−1]. Because ell is coprime to phi_d, every prime valuation
of phi_d survives this localization. Unique factorization then gives
phi_d|phi_n in K[X,Y,Z], retaining every multiplicity. Coefficient
Frobenius and uniqueness of the quotient descend this quotient to F2.

Consequently ANY common absolute prime forces the entire phi_d.
Normalized gcd is therefore exactly1 or phi_d over K and over F2. This
does not need squarefreeness of phi_d, although that property is separately
accepted. It certainly does not infer multiplication irreducibility from
composition indecomposability.

Only at this stage is KC applied. Its accepted hypothesis is WHOLE
phi_d division, for every k>=2 and odd n>=3; the conclusion is exactly
n=(q^(2r+1)+1)/(q+1), r>=1. GK gives whole division for every such r.
The resulting CS2 iff has both directions. Failure of that test means
no base component at all, not irreducibility of the target polynomial.

In the optional J language, every labelled absolute base component and
every F2 Frobenius-orbit factor has this same occurrence criterion. For
q16 this excludes the proper A-only and B-only intersections left open
by my old IC argument. The stronger conclusion uses the NEW all-k field
argument, not an unproved transitivity assertion about the old six
symmetries. IC's older weaker possibility list and frozen status are
not retroactively altered.

## 6. Endpoints and adversarial checks

The submission handles the genuine official boundaries. For n=1 the
numerator is zero, while R times two nonconstant reductions is nonzero
in the polynomial domain; zero itself is constant modulo2. For n=3,
g_3=U+1 and D_3=1, so phi_3=1. The main gcd/iff domain excludes n=1
and includes the correctly rejected n=3. q=2 has d=3, a unit base, and
is correctly excluded; its whole-divisor progression would not be an iff.
The auxiliary r=0 gives n=1 and is excluded. At r=1, n=d and the whole
cofactor is a unit, so this alone is not an official two-factor
construction. J may separately give proper F2 orbit factors where there
is more than one orbit. At r>=2, q>=4, GK supplies two positive degrees
and their coefficientwise0/1 integer lifts.

I specifically tried the possible failures below; each is excluded by
an explicit step already present in the submission:

- Proper even-k composition degrees: the b|N, b≡1 mod(q+1) argument
  leaves only1 and N, rather than borrowing odd-k exceptionality.
- A purely inseparable intermediate or factorization: Lüroth is
  arbitrary-characteristic; the one-pole conversion is geometric, and
  the simple zero also forbids an inseparable composition factor.
- A common component at the removed chart line, a vertical curve, a
  finite point, or a diagonal in a,b: the restriction, leading-degree,
  transcendence and derivative checks exclude these separately.
- A rational H with a finite pole, or denominators canceled only
  generically: local pole pullback makes H polynomial, and all later
  difference and localization identities are genuine polynomial ones.
- Loss of a prime multiplicity or of a coefficient field: the UFD
  localization and two separate Frobenius-uniqueness arguments retain
  them. Pointwise equality on a finite field is never used.
- Applying KC directly to a single factor, claiming all reducibility,
  or treating r=1 as a positive-degree cofactor: none occurs.

The source-based failed Hermitian shortcut is also accurate as stated.
The displayed q4 factor in McGuire's printed35 contains a nonzero X³Y
term before degree5 homogenization, hence a nonzero X³YZ term after it.
Any linear transform of a degree5 Hermitian form has support only in
monomials X_i^4 X_j, so this factor cannot be such a linear transform.
This observation is context only and is not a premise of CS1–CS2.

## 7. Sources, preservation and recommendation

Primary theorem use and actual read limits are recorded separately.
Lüroth is attributed; the MCM trace form is classical attribution only;
no permutation, two-to-one, exceptionality, group classification, APN,
Hasse–Weil, transversality or unread Férard theorem is imported. I do not
claim to have reconstructed the original1993 JW proof or every source
proof hidden behind an accepted dependency. The exact accepted KC/GK/IC
bodies and scopes were checked, without independently self-certifying
my own old IC theorem.

The constructor's nine artifacts and frozen manifest match their
assigned hashes. Compact preservation binds immutable parent metadata
by path/bytes/SHA and verifies its declared fingerprints; it does not
duplicate the historical inventory. The prior 2017 value-R4 checkpoint
and older declared frozen inputs are included in the preservation chain.
No old proof, review, candidate, source cache, shared file or Git state
was changed. No new peer CS file was opened during the initial audit.

There is no unresolved substantive issue and no required author repair
from this review. CS1–CS2 should be considered only for their exact
base-Kasami common-component/gcd scope after the second independent
whole audit and coordinator reconciliation. The ordinary reducibility
classification for arbitrary odd n remains open.
