# DI1–DI2: initially blind nonconstructor whole review R1

2026-10-17 UTC. Reviewer `/root/review_2021_reasoning_j15_r2`.
Requested gpt-6.1-sol/max; independently verified effective settings unknown.
Target8550 bytes, SHA256
`44a91d25943bb3d25f3c4a9c7fc2c2b7f498692889bf82b7dabbdb610b57c957`.
Constructor manifest1108 bytes, SHA256
`ab71ed21157e434de2d487628fae2c72748e6582e2f0e16fc7ed6e37005fc17b`.

I reconstructed the WHOLE submission and all eight obligations, including
the original primary source's relevant Section2. No substantive defect
or required author repair was found. I recommend the exact DI1 criterion
and DI2 composition-indecomposability result after coordinator reconciliation
of both complete initially blind whole audits. No reviewer promotion,
multiplicative irreducibility, full composition classification or official
annual solution is asserted.

I authored older T1–T4/C7/C11 and previously whole-reviewed CP, GK, KC and
CJ. Those roles are disclosed inputs, not contribution to NEW DI1/DI2.
I did not construct its general criterion, coprime-local-order argument
or application. Root constructed DI and cannot count independently.
No new peer DI report, conclusion or later root inspection was read
before this entire initial freeze. R7 was fully frozen before the first
DI target read. Only this review prefix was written. No mathematical
program, CAS, sample, scan, certificate replay, author rerun or worker
Git/shared edit was used.

## DI1: reconstruction of the complete general argument

Let K be algebraically closed of characteristic p>0, and let deg f=n>1
with p not dividing n. The critical points mean zeros of the formal
derivative; e_f(alpha) is the EXACT order of f(T)-f(alpha), not the
multiplicity in f'. The two assumptions concern distinct critical POINTS
and their values, and the integer gcd(n,e_f(alpha)). They do not require
simple derivative zeros or tame local behavior.

Suppose f=g(h) with a=deg g>1,b=deg h>1. Nonconstant polynomial degrees
multiply, independently of characteristic and leading coefficients:
ab=n. Consequently p divides neither a nor b. In particular the leading
term of g' is a times the nonzero leading coefficient, so deg g'=a-1>=1.
Algebraic closure now gives a finite root beta of g'. This root existence
would not follow in an arbitrary nonclosed base field, nor when p divides
the degree of the outer polynomial. DI1 has both hypotheses needed here.

Every root alpha of the degree-b polynomial h-beta satisfies
f'(alpha)=g'(beta)h'(alpha)=0 and f(alpha)=g(beta). This reasoning applies
to ALL distinct roots, regardless of multiplicities or vanishing h'.
Since distinct critical points have distinct values, h-beta has only
one distinct root alpha0. It has at least one root over K. Factoring
the polynomial over K thus gives EXACTLY

    h(T)-beta=c(T-alpha0)^b, c!=0.

This is a single-fiber statement, not an assertion that h is inseparable.
There is no root-count-to-multiplicity inference over an unclosed field.

Since g is nonconstant, g(Y)-g(beta) is a nonzero polynomial. Factor it
as (Y-beta)^e V(Y), e>=1 and V(beta)!=0. Its substituted unit satisfies
V(h(alpha0))=V(beta)!=0, so

    f(T)-f(alpha0)=c^e(T-alpha0)^(b e)V(h(T))

has EXACT order b*e at alpha0. In particular b divides e_f(alpha0)
and also n. The assumed gcd is one, so b=1, contradicting the proposed
nontrivial decomposition. This proves the complete DI1 assertion.
It needs no inverse derivative, separability of that fiber, tame formula,
monodromy theorem or characteristic-zero decomposition theorem.

## Adversarial checks of the hypotheses

The prime-to-characteristic assumption is substantive. If it were removed,
in characteristic2 the decomposed f=T^4+T=(T^2+T) composed with itself
has derivative1. There are no finite critical points, so the two displayed
critical-point hypotheses would be vacuous. This elementary hand example
does not meet DI1's degree assumption and therefore does not refute it.

The injective-value premise also matters. In characteristic2 let h=T^3+T
and f=h composed with h, of degree9. The critical points are1 and the
three roots of h(T)=1. The latter are simple roots of that fiber because
h'= (T+1)^2 and h(1)=0. All four f-values are zero. Each exact local
order is2: at1 the inner h has order2 at value0 and the outer derivative
there is1; over h=1 the inner map has order1 and the outer map order2.
Hence gcd(9,2)=1 at every critical point, but the values collide. This
checks precisely why condition1 cannot be dropped. No field enumeration
or program is involved. Likewise a monomial of composite degree prime
to p has an injective singleton critical value but fails the local gcd
condition; its evident decomposition does not contradict DI1.

Constant factors cannot occur in a decomposition of nonconstant f.
The n=1 case is outside the theorem. A composite n is fully allowed:
the proof only uses b dividing n and e_f, never primality of n.

## DI2: all finite critical points and their exact local orders

The COMPLETE accepted GK mathematical body and acceptance text were read.
The only needed identity is

    F=P2=T^(q^2+1)+(T+1)^(q^2-q+1), q=2^k>=4.

No earlier CJ local calculation is imported as an unproved premise; the
new submission rederives it. The degree is n=q^2+1, since the second
summand has strictly smaller degree. It is odd, so characteristic2 does
not divide it. The source's q2 auxiliary/unit boundary is not extended
by this review; q>=4 is the stated DI scope.

Differentiation gives F'=T^(q^2)+(T+1)^(q^2-q)=A^q, with
A=T^q+(T+1)^(q-1). Also (T+1)A=T^(q+1)+1. The latter numerator has
derivative T^q and no zero root. It therefore has q+1 distinct roots.
The simple root1 is removed by division, A is monic of degree q and
A(1)=1. Thus ALL finite critical points are exactly the q simple roots
alpha of A, each appearing q times in F'. There is no omitted critical
point or derivative-identically-zero case.

Every alpha satisfies alpha^(q+1)=1, alpha!=1, lies in F_(q^2), and
has alpha^q=alpha^-1. Put u=alpha+1!=0. Then u^q=u/alpha,
u^(q^2)=u, u^(q-1)=alpha^-1 and u^(q^2-q+1)=alpha*u. Consequently

    F(alpha)=alpha^2+alpha*u=alpha.

Thus the finite critical values are pairwise distinct. Frobenius has
been used on these finite constants, not assumed to be the identity
on the indeterminate or an auxiliary transcendental field.

To obtain the actual e_F, expand in Z about alpha. The binary exponents
of q^2+1 are0,2k; those of q^2-q+1 are0,k,...,2k-1. The characteristic-two
product expansion has no local terms of exponent2,...,q-1. The linear
term cancels by F'(alpha)=0. At exponent q the first summand contributes
nothing and the second contributes u^(q^2-2q+1), which is nonzero.
The constant is F(alpha)=alpha, already computed. Therefore

    F(alpha+Z)-alpha=u^(q^2-2q+1)Z^q+higher terms,
    e_F(alpha)=q EXACTLY.

It would be invalid to read e_F=q+1 from the derivative multiplicity q;
the explicit expansion avoids that wild-characteristic mistake. The
argument includes q4 without a sample. The integer gcd(q^2+1,q)=1
now verifies every DI1 hypothesis, proving that this P2 admits no
nontrivial polynomial composition over the algebraic closure of F2.

The coefficient-extension statement is also valid, including nonalgebraic
extensions: after any such extension, pass to its algebraic closure.
The displayed derivative has the same complete set of algebraic critical
roots, values and exact local orders there, so DI1 applies again. No
separate descent assertion about hypothetical decomposition coefficients
is needed. In particular the composite degree65 at q8 causes no problem;
any proposed inner degree would divide both65 and8 and hence be one.

## Primary source and precise conclusion

Kreso's original primary Section2 was read in full, including the
critical-fiber method and its small-gcd corollaries and Morse discussion.
The source is related methodology; DI supplies its own proof over an
explicitly algebraically closed field. No existence of an outer derivative
root in an arbitrary nonclosed base is imported. Its characteristic-zero
lacunary results and displayed Morse monodromy theorem are not applied.

For this F, the gcd of F-F(alpha) with F' has degree q at a critical
value: only alpha contributes, with exact multiplicity q in both
polynomials. Thus the source's degree-one/two small-gcd corollaries
do not directly apply at q>=4. F' has repeated critical roots, so the
Morse hypothesis of simple critical points fails. No symmetric Galois
group or full external theorem proof is claimed from those readings.

The conclusion is ONLY composition indecomposability of P2. It is not
ordinary multiplicative irreducibility or absolute irreducibility of a
three-variable phi polynomial. It does not forbid P_s=H(P2), where
P2 would be an inner factor in another polynomial rather than a
decomposition of itself. The old CJ necessary congruence, whole-divisor
results and their open higher-degree remainder questions are unchanged.
No annual classification or priority is inferred.

The separate ledger has32 inference checks covering all eight obligations.
No substantive objection or required author repair remains in this
initially blind reconstruction. Reconciliation and promotion belong to
the coordinator after the other complete independent whole audit.
