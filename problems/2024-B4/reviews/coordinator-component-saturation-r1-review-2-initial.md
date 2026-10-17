# CS1--CS2: initially blind nonconstructor WHOLE review R2

2026-10-17 UTC. Reviewer `/root/review_2022_complexity_r2`.
Requested inherited `gpt-6.1-sol/max`; independent effective-setting
readback unavailable. Target: the COMPLETE13194-byte root-constructed
`notes/coordinator-component-saturation-r1-candidate-v1.md`, SHA256
`61f8c60491880e941149649c2c4180abef91671496d56c5869f8543a915aba46`,
and its complete nine-artifact freeze, SHA256
`13dff01ab6757aa2214d4be9667c96f8381446f7b41c0b06b3458babfe80f0fb`.

I reconstructed the WHOLE CS1--CS2 argument and every one of the30
author obligations. I found no substantive mathematical defect in its
stated base-Kasami common-component scope. There is one optional
expository clarification about the word separable, recorded as N1;
it does not affect any conclusion or require a mathematical repair.
This is a reviewer recommendation, not promotion: only the coordinator
may reconcile it with the other fresh whole audit. The annual question
and all non-base-factor classifications remain open here.

## Independence and actual read scope

I did not construct this NEW CS argument and supplied no new CS proof
inference. My prior2024 CP/GK/NV/NJ/HR and related review context is
disclosed; accepted old premises are not counted as freshly independent
self-recertification. Root is the CS constructor and cannot count as
an independent CS reviewer. The prefix was checked unused before any
write. I have not opened another NEW CS review, its conclusions, or
root's later CS inspection. This entire report, all30 issue rows,
source checks and integrity records freeze before any comparison.

Fresh reads include the complete main, all nine constructor artifacts,
all30 obligations, source audit, failures, log and administrative source;
the full accepted KC/GK/IC mathematical bodies and their current scope
records; local and actual official B4(b); the full two-page authored
Lueroth proof; the actual MCM definition/adjacent hypotheses; and the
primary-coauthor statement J for the optional labelled interpretation.
The one relevant existing McGuire printed35 image was visually checked.
Long combined outputs that truncated were filled by bounded reads;
no complete-read claim relies on an unseen middle. Detailed scopes,
including the unread original1993 proof, appear in the source record.

## 1. Univariate invariant and exact trace form

Put U=t^2+t. Reduction by t^2=t+U writes every polynomial uniquely as
A(U)+tB(U). Its two leading-degree parities cannot cancel. Translation
t=>t+1 fixes U and changes that expression by B(U). Thus the invariant
t^j+(t+1)^j has a unique g_j(U), monic of degree(j-1)/2 for odd j>=3:
the t^j terms cancel and the next coefficient is j=1 in characteristic2.
This is an invariant-ring calculation, not an assertion that an
arbitrary factor descends through the quadratic cover.

For q=2^k,k>=2, the telescoping sum T(U)=sum_(i=0)^(k-1)U^(2^i)
satisfies T(t^2+t)=t^q+t. Write S=T/U. Its constant coefficient is1,
its degree is q/2-1 and T'=1. I independently expanded the product
in Section1: the relation d+q=q^2+1 cancels the two t^(q^2) terms
after multiplication, leaving exactly the four displayed terms, also
equal to (t^(q^2)+t^q)(t^q+t). Cancellation is in F2[t], by the
nonzero polynomial U(t)^q. Substitution is injective by leading degree.
Consequently the identity is exactly

    g_d(U)=1+F(U),   F(U)=U*S(U)^(q+1),
    deg F=N=(q/2)(q-1).

No scalar, rational remainder or finite-field specialization is left.
T has q/2 simple roots. Zero is the unique simple root of F; every
other root has multiplicity q+1. Differentiating gives
F'=S^q(S+US')=S^q because (US)'=T'=1. For a squarefree-polynomial
reading of separable, note additionally that S(a)=0 implies g_d(a)=1,
so gcd(g_d,g_d')=1. The inference does not rest on a generally false
claim that nonzero derivative alone implies no repeated root.

## 2. Indecomposability includes even k and inseparable possibilities

Suppose F=A(B) with inner degree b>1 and outer degree>1. At0,
local multiplicities multiply to1; both the root B(0) of A and the
root0 of B-B(0) are simple. Every other root of this latter fiber is
a nonzero F-root, of exact multiplicity q+1 because A is simple at
B(0). Over the algebraically closed K the entire degree is therefore

    b=1+j(q+1), j>=0,   b|N.

This reasoning already excludes inseparable inner or outer factors
at that simple root; no tameness assumption is needed. Write
b=2^a e, a<=k-1, e|(q-1), e odd. At a=0, the congruence b=1mod(q+1)
and 1<=e<=q-1 give b=1. At a>=1, inversion gives

    e=q+1-2^(k-a)>=q/2+1>(q-1)/2.

The representative is unique in1,...,q-1. A divisor e of q-1 above
half must be q-1 itself. Then 2^(k-a)=2, so a=k-1 and b=N. Those
are exactly the two endpoint degrees and no proper composition
survives. This proves geometric composition indecomposability for
every k>=2, not just the odd-k exceptionality cases in the literature.
Translation by1 preserves it for g_d. This is unrelated to ordinary
multiplication irreducibility of phi_d.

## 3. Intermediate fields and a genuine common pair

I checked that the cited Lueroth theorem is over an arbitrary field,
so characteristic2 is allowed, without a separability qualification.
For an intermediate K(f(z)) subset E subset K(z), it gives E=K(B(z))
and f=A(B) with rational A,B. Since f is polynomial, its pole support
on P1 is exactly infinity. Rational B is surjective over algebraically
closed K; distinct poles of A have disjoint nonempty B-fibers. Thus
A has one pole c and B^-1(c) has support {infinity}. A Mobius change
sending c to infinity makes B and the adjusted A polynomials. A proper
intermediate field would make both degrees>1, contrary to composition
indecomposability. Wild multiplicities at the unique pole do not
invalidate this support argument.

For the common-pair lemma, a,b transcendental and distinct give a
field isomorphism K(a)=>K(b) by substitution. If f(a)=f(b) and
h(a)=h(b), this map fixes E=K(f(a),h(a)) pointwise as elements of
the common extension field. If E were all K(a), it would both fix a
and send it to b. Thus E is a proper intermediate field, hence exactly
K(f(a)); it cannot be merely K since f(a) is transcendental. So
h(a)=H(f(a)) with rational H. Any finite pole c of H pulls back to
a finite root of f-c, producing a pole of polynomial h. Therefore
H is polynomial. Transcendence of a makes this a polynomial identity.
The argument works for constant h as well and assumes no Galois
closure or classification theorem.

## 4. The actual common component supplies all those hypotheses

A nonconstant common factor of the two homogeneous polynomials has
a homogeneous irreducible prime P. It is not L=X+Y: with Y=X+e,
the coefficient of e gives the nonzero restriction
(X^(d-1)+Z^(d-1))/(X+Z)^2 of phi_d. This also follows from accepted
IC1, but the direct calculation suffices independently of J.

Changing homogeneous coordinates to L,X,Z and setting L=1 makes
P a nonconstant irreducible polynomial. Otherwise homogenization
would make it a power of L or supply a factorization of P. Its
function field has transcendence degree1. In the chart X=t,Y=t+1,
Z=u, put a=t^2+t,b=u^2+u. The numerator and denominator specialize
to g_j(a)+g_j(b) and a+b respectively, so the identity with D_j is
exact, with no invertible scalar or missing polynomial factor.

For EVERY constant c, D_d(c,W) is monic of degree N-1; its leading
term cannot disappear upon specializing c. Thus constant a would
force algebraic b, then algebraic t and u from their quadratic
equations, contradicting the curve field's transcendence degree.
Both a,b are transcendental. The diagonal specialization of a divided
difference is the derivative; D_d(a,a)=S(a)^q is nonzero. Hence a!=b.
These separate checks exclude the otherwise serious constant-fiber
and removed-diagonal counterexamples. No descent of an arbitrary
factor through the cover was assumed.

The two chart equations now give equal values of both g_d and g_n
at the actual pair. Section3 therefore gives g_n=H(g_d). Squaring
coefficients fixes g_n,g_d, and substitution by a nonconstant
polynomial is injective. It fixes H, whose coefficients consequently
belong to F2. This descent is distinct from the original absolute
factor's possible coefficient extension.

## 5. Full division, KC and exact scope

The difference-of-values identity for H shows that g_d(V)+g_d(W)
divides g_n(V)+g_n(W). Both contain V+W, and cancellation gives
the WHOLE D_d divisor. After the chart substitution, homogeneous
division holds in the localization at L. Explicitly the homogeneous
quotient may at first have a power of L in its denominator, from
the factor L^(n-d). Since L is coprime to phi_d, every prime
valuation of phi_d must already occur in phi_n in the original UFD.
This retains all multiplicities. The quotient descends to F2 by
coefficient Frobenius/uniqueness. Thus ANY common absolute prime
has forced the WHOLE base phi_d, proving CS1.

Only at this point is accepted KC invoked. Its exact accepted
domain is every k>=2 and odd n>=3, and it is an iff for the WHOLE
divisor. It gives exactly n=(q^(2r+1)+1)/(q+1), r>=1. Accepted
every-index GK supplies the converse; gcd(phi_d,phi_n)=phi_d there
and is1 otherwise. Ordinary F2 gcds have the same result. No
unreviewed CS assertion is fed back into KC.

Optional J identifies the labelled absolute primes and ordinary
Frobenius-orbit products, so the same occurrence test applies to
each. I checked the matching primary-coauthor statement; its old
original1993 proof remains unread and explicitly imported only in
that labelled interpretation. Core CS1--2 do not need J or IC's
transitivity cases. The new result would exclude the proper q16 A/B
cases, without altering the earlier IC proof or its then-open scope.

n=1 is the zero numerator and cannot give a product with both
nonconstant reductions in a domain. n=3 gives unit phi3. q=2 is
excluded: phi3 is unit and g3 linear, so a nontrivial base-component
claim would be inappropriate. r=0 gives n1; r=1 gives equality and
unit cofactor, not alone the official two-factor conclusion. For
r>=2,q>=4, accepted GK supplies positive-degree ordinary F2 factors
and coefficientwise integer lifts. None of this classifies arbitrary
non-base factors, higher-family components or the full annual target.

## Initial disposition and operations

All30 author obligations are reconstructed in the separate issue
ledger. There is no substantive counterexample, missing premise or
required repair in the stated scope. N1 is an optional clarification
whose needed extra observation is already immediate from the proved
formula. No peer finding has been read.

No mathematical executable, CAS, exponent scan, finite-field sample,
author script or source certificate was run. Metadata-only Python,
SHA/JSON/text counts and read-only source access preserve exact inputs.
Only this unused review prefix is written. Old own packets and exact
parent metadata remain unchanged, with compact binding and reproduction
references. Actual account telemetry and all artifact hashes are in
the immutable manifest. Requested settings remain separate from any
unavailable effective readback. Two other roles are not conflated:
root's construction cannot replace independent review, and this
recommendation cannot replace coordinator promotion after reconciliation.
