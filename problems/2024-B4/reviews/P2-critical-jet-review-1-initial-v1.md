# CJ1: initially blind nonconstructor whole review R1

2026-10-17 UTC. Reviewer `/root/review_2021_reasoning_j15_r2`.
Requested gpt-6.1-sol/max; independently verified effective settings
unavailable. Complete target main:6774 bytes, SHA256
`fa5b79ce59303a06a61da18ee902235bc299add309aa0725846bbfd3a7716f26`.
Constructor manifest:1089 bytes, SHA256
`d1926b3e81b4952ad29c46dcda57b932365d8b36728b228a31d169dfda67cec3`.

I reconstructed the WHOLE CJ1 proof and all six end obligations. No
substantive defect or required author repair was found. I recommend the
stated necessary congruence in its exact scope, subject to coordinator
reconciliation of two full independent audits. No promotion, sufficient
composition criterion, general decomposition classification or annual
solution is made by this review.

I authored older T1–T4/C7/C11 material and previously whole-reviewed CP,
GK and KC. Those older roles are disclosed context, not contribution to
the NEW critical-jet construction. I did not supply its local-order,
common-jet, multiplicity-transfer or congruence arguments. Root constructed
CJ1 and is not an independent reviewer. No new peer CJ report, conclusion
or later root inspection was read before this complete initial freeze.
Only this assigned prefix was written. There was no mathematical code,
CAS, scan, sampling, author rerun, candidate/shared/Git mutation or spawning.

## Scope and accepted input

The official open target is2024 B4(b), coefficientwise factorization modulo
two with integer polynomial lifts and two nonconstant reductions. This
candidate studies only a necessary condition for one F2 univariate
composition; it makes no new preliminary-part claim or claim to cover all
possible factors. The original official PDF and local normalization were
read. No equality of polynomial functions on a finite field is substituted
for a polynomial identity.

The COMPLETE accepted GK body and its acceptance text were read. CJ uses
its exact polynomials over F2:

    A=T^q+(T+1)^(q-1), B=(T+1)^(q-1),
    P0=1, P1=T,
    P_(r+2)=A^(q^(2r+1))*P_(r+1)+B^(q^(2r+1))*P_r,
    deg P_r=E_r=(q^(2r)-1)/(q^2-1), r>=1,
    P2=T^(q^2+1)+(T+1)^(q^2-q+1).

The monic degree assertion is valid: the first recurrence summand has
degree E_(r+2), strictly above the second by q^(2r)(q+1). No leading
cancellation occurs. No source factor, APN, monodromy or decomposition
theorem is needed. The older unverified critical-fixed and higher-family
notes were read as context only. Every mathematical step needed from
their subject matter is rederived in the present target and below; this
review does not accept their additional assertions.

Fix q=2^k>=4 and j>=1, and suppose P_(2j)=H(P2) with H in F2[T].
Since P_(2j) is nonconstant, H is nonconstant. The claimed necessary
congruence is

    H(T)=T^(1+(j-1)q^4) modulo A(T)^(q^4).

The power q^4 is an ordinary integer exponent; the modulus degree is
q*q^4=q^5. Its two distinct roles below are local multiplicity and
Frobenius power. Neither role identifies Frobenius with the identity on
an indeterminate.

## Critical points, fixed values and exact local order

In characteristic two, (T+1)A=T^(q+1)+1. The numerator has derivative
T^q, which is nonzero at each of its roots. Those roots are nonzero,
distinct and number q+1. Its simple root1 is removed on division by
T+1; A is monic of degree q and A(1)=1. Thus A has exactly q simple
roots alpha with alpha^(q+1)=1 and alpha!=1. Every such alpha lies in
F_(q^2), because q+1 divides q^2-1, and alpha^q=alpha^-1.

Put u=alpha+1. It is nonzero and satisfies u^q=u/alpha and u^(q^2)=u.
Consequently B(alpha)=u^(q-1)=alpha^-1 and
u^(q^2-q+1)=alpha*u. Hence

    P2(alpha)=alpha^2+alpha*u=alpha.

For any r>=0, the coefficient B(alpha) raised to q^(2r+1) is alpha:
Frobenius on these constants has period two, and the exponent index is
odd. A(alpha)=0, so P_(r+2)(alpha)=alpha*P_r(alpha). No such period-two
identity is assumed on the polynomial ring or auxiliary function field.

The formal derivative is P2'=A^q. It vanishes at alpha, but this alone
would not determine a tame ramification index. The direct binary product
calculation does: q^2+1 has bits0,2k; q^2-q+1 has bits0,k,...,2k-1.
There are no local exponents2,...,q-1. The two linear terms cancel at
alpha. At exponent q, only the second summand contributes, with coefficient

    u^(q^2-2q+1) != 0.

It follows that P2(alpha+Z)-alpha has order EXACTLY q. Later terms,
including possible exponent q+1, do not change this order. The exclusions
alpha=0 and alpha=1 are essential and already justified. The minimum
allowed q=4 has the same binary argument; q=2 is outside CJ's stated
scope and no extension is asserted.

## The common q^5 jet at every even index

For an even r>=2 let N_r=q^(2r+1). It is a power of two and is at
least q^5. Since A(alpha)=0, A(T)^N_r is divisible by
(T-alpha)^N_r. Frobenius gives

    B(T)^N_r-B(alpha)^N_r=(B(T)-B(alpha))^N_r,

also divisible by (T-alpha)^N_r. The constant B(alpha)^N_r equals
alpha by the odd-index calculation. Multiplication by the polynomials
P_(r+1) and P_r cannot reduce these orders. Therefore the exact accepted
recurrence gives

    P_(r+2)=alpha*P_r modulo (T-alpha)^(q^5)

for every even r>=2. Starting at r=2 and iterating reaches EVERY
P_(2j), with the uniform conclusion

    P_(2j)=alpha^(j-1)*P2 modulo (T-alpha)^(q^5).

The smallest coefficient threshold is q^5 at the first step; later
ones are larger. Induction combines sums and multiplication by a
nonzero constant, so the threshold does not deteriorate with j. At
j=1 the difference is zero identically. No low-index sample or
extrapolation is used.

## Multiplicity transfer, including inseparable H and zero K

For a fixed root alpha define K_alpha(Y)=H(Y)-alpha^(j-1)*Y over the
algebraic closure. Composition and the jet show that K_alpha(P2(T))
is divisible by (T-alpha)^(q^5). If K_alpha is nonzero, write
K_alpha(Y)=(Y-alpha)^m*V(Y), with V(alpha)!=0. Because P2(alpha)=alpha,
the factor V(P2(T)) is a unit at alpha. The first factor has order
q*m by the EXACT order q proved above. Therefore

    ord_alpha K_alpha(P2)=q*m>=q^5, so m>=q^4.

The calculation does not divide by a derivative or assume H separable.
It applies equally when H is inseparable. Nonconstant substitution
cannot turn a nonzero K_alpha into the zero polynomial, by degree.
If K_alpha is identically zero, the desired divisibility holds directly
and no finite order is assigned to zero. Hence for every root alpha,

    H(T)-alpha^(j-1)*T is divisible by (T-alpha)^(q^4).

Since alpha belongs to F_(q^2), alpha^(q^4)=alpha. Frobenius yields
T^(q^4)=alpha modulo (T-alpha)^(q^4). Raising this congruence to
j-1, including zero when j=1, and multiplying by T shows that the
comparison monomial has the same local remainder alpha^(j-1)*T.
Subtracting it from H therefore gives divisibility by every
(T-alpha)^(q^4).

These local factors are pairwise coprime because the q roots of A are
distinct; their product is exactly A^(q^4), including its monic scalar.
This proves the asserted divisibility in the algebraic closure. The
numerator and the MONIC divisor lie in F2[T]. Euclidean division there
has a remainder of degree below q^5, which must also be the remainder
after extending the field; uniqueness forces it to vanish. Thus the
congruence descends as a polynomial congruence over F2, not a function
identity on F_(q^2).

## Degree restrictions, small indices and failure of sufficiency

For any nonconstant composition P_s=H(P2), deg P2=q^2+1 divides E_s.
Modulo that integer, q^2=-1, so the sum E_s alternates between residues
zero for even s and one for odd s. Hence s must be even. This is a
necessary degree condition only, not an assertion of composition at
every even index. CJ explicitly excludes j=0.

At j=1, H=T works and satisfies CJ exactly. The nonconstant substitution
also forces this H uniquely. At j=2 the degree ratio is q^4+1, smaller
than q^5. CJ would force H=T^(q^4+1), since a nonzero difference of
degree below the monic modulus cannot be divisible by it. Independently,
the exact recurrence evaluated at0 gives P0,...,P4 values1,0,1,1,0,
whereas at1 it gives P_r(1)=1 for all r>=1. Thus P2(0)=P2(1)=1 but
P4(0)!=P4(1), disproving P4=H(P2). This is a rechecked previously
recorded endpoint obstruction, not a new composition classification.

For all j>=1, deg H=E_(2j)/E2=1+q^4+...+q^(4j-4), if the composition
exists. Beginning at j=3 this is above q^5; a nonzero multiple of
A^(q^4) is not excluded by the degree comparison. The candidate
correctly supplies necessity only and leaves a possible higher-degree
remainder multiple. It does not prove indecomposability of P2, classify
P_s=H(P_r), characterize arbitrary factors, or turn this condition into
the official complete exponent answer. No characteristic-zero Ritt
theorem or unverified earlier note fills that gap.

The separate30-check ledger covers all six whole obligations. All
asserted CJ1 inferences are clear in the stated scope. No substantive
objection or author repair is requested. Only the coordinator may
accept the result after both complete initially blind whole audits.
