# Initially blind whole R2: the P2 critical-jet congruence

2026-10-17 UTC. Independent reviewer /root/review_2017_coarsening_r1.
Requested gpt-6.1-sol/max; effective-setting readback unavailable.
Root constructed NEW CJ1; I did not construct it.

**Verdict:** all six whole-proof obligations reconstruct. No
substantive defect or required author repair was found. The
conclusion is the stated NECESSARY polynomial congruence, over
F2, for a hypothetical P_(2j)=H(P2). It is neither a sufficient
composition test nor a reducibility classification.

I authored older CP composition work and reviewed earlier
structural/Kasami packets. This is not an independent re-audit
of my old CP theorem. The only accepted mathematical input here
is GK's explicit P recurrence and degree formula. The new local
critical-root/jet reasoning is reconstructed below without
assuming the earlier unverified critical-fixed note.

## Target, reads and domain

Read ENTIRE6774B candidate, including all six end obligations,
source/scope section and manifest; complete accepted GK body
and exact acceptance scope; complete earlier critical-fixed
and higher-family composition notes as UNVERIFIED context;
and the complete local official statement. The primary2024
Paper B was directly reopened at page2 B4. No new CJ1 peer
report, ledger or findings was read before this complete
report/source/ledger/integrity freeze.

Target main SHA256:
fa5b79ce59303a06a61da18ee902235bc299add309aa0725846bbfd3a7716f26.

Fix q=2^k>=4 throughout and j>=1; H is an actual polynomial
in F2[T]. Recurrence exponents q^4,q^5 are ordinary powers
of q. The official(b) domain is odd positive n and
coefficientwise F2 polynomial factors, not functions on
F2^3 and not only factors over an extension. CJ1 does not
claim to decide that whole official domain. No preliminary
proof, math code, CAS, scan, sample or author rerun is used.

## 1. Accepted recurrence, degrees and even-index necessity

The exact imported recurrence is

    A=T^q+(T+1)^(q-1), B=(T+1)^(q-1),
    P0=1,P1=T,
    P_(r+2)=A^(q^(2r+1))P_(r+1)+B^(q^(2r+1))P_r.

GK supplies deg P_r=E_r=1+q²+...+q^(2r-2) for r>=1.
At r0 the recurrence directly gives

    P2=T^(q²+1)+(T+1)^(q²-q+1), deg P2=q²+1.

For nonconstant P_s=H(P2), the degree product forces
q²+1 to divide E_s. Reduction q²=-1 modulo q²+1 makes
E_s zero for even s and one for odd s. Thus only even
s can occur. This elementary integer degree argument is
valid; it is not used as a sufficient composition criterion.

## 2. All finite critical roots and their fixed values

Direct multiplication in characteristic two gives

    (T+1)A=T^(q+1)+1.

The latter polynomial has q+1 distinct nonzero roots:
its derivative is T^q, nonzero at each root. Its root1
is simple and A(1)=1. Hence A has exactly the q other
simple roots alpha, all with alpha^(q+1)=1. They lie in
F_(q²) since q+1 divides q²-1, and alpha^q=alpha^(-1).
Neither alpha0 nor alpha1 is among them.

Put u=alpha+1!=0. Then u^q=u/alpha and
u^(q²)=u. Therefore

    B(alpha)=u^(q-1)=alpha^(-1),
    u^(q²-q+1)=u/B(alpha)=alpha*u,
    P2(alpha)=alpha²+alpha*u=alpha.

Differentiating the explicit P2 gives P2'=A^q. Thus these
q roots are exactly its finite critical points. For every
r>=0, B(alpha)^(q^(2r+1))=alpha, because the q-Frobenius
interchanges alpha and alpha^(-1). Evaluating the recurrence
therefore gives P_(r+2)(alpha)=alpha P_r(alpha).
No assumption that arbitrary coefficients are fixed by
q-Frobenius is made.

## 3. Exact local order q, including wild characteristic

At alpha write the local variable Z. The binary support of
q²+1 is{0,2k}; that of q²-q+1 is{0,k,k+1,...,2k-1}.
The characteristic-two binary product formula consequently
gives NO Z exponent2,...,q-1 in either summand of
P2(alpha+Z). Its linear coefficient vanishes because
P2'(alpha)=0.

The first summand has no Z^q term. The second has exactly
the coefficient

    u^(q²-q+1-q)=u^(q²-2q+1)

at Z^q, obtained by selecting only its q factor. This
coefficient is nonzero. The constant term is alpha, so

    ord_(T-alpha)(P2(T)-alpha)=q EXACTLY.

Later terms, including orderq+1, do not affect this order.
The proof does not infer a tame ramification index q+1
from the derivative's multiplicity. The q-power term is
allowed in characteristic two; no separability assumption
on a later outer H is hidden.

## 4. Uniform q^5 jet for every even-index P

For every EVEN r>=2, N_r=q^(2r+1) is a power of two
and at least q^5. Since A(alpha)=0, A(T)^N_r is
divisible by(T-alpha)^N_r. Frobenius gives

    B(T)^N_r-B(alpha)^N_r=(B(T)-B(alpha))^N_r,

also divisible by(T-alpha)^N_r. Its constant value is
B(alpha)^N_r=alpha. Hence

    P_(r+2)-alpha P_r
       =0 mod(T-alpha)^(q^5).

Multiplication by the ordinary polynomial factors
P_(r+1),P_r cannot lower either vanishing order.
Starting with P2 and iterating through r2,4,... proves

    P_(2j)=alpha^(j-1)P2 mod(T-alpha)^(q^5)

for every j>=1. At j1 the difference is identically
zero. The first actual recurrence step already has
threshold q^5, and every later one has at least that
threshold. The proof does NOT incorrectly apply the
smaller r0 threshold to this assertion.

## 5. Ramified substitution, all roots and F2 descent

Assume P_(2j)=H(P2) and define over the algebraic closure

    K_alpha(Y)=H(Y)-alpha^(j-1)Y.

The preceding jet makes K_alpha(P2(T)) divisible by
(T-alpha)^(q^5). If K_alpha is nonzero, factor at alpha

    K_alpha(Y)=(Y-alpha)^m V(Y), V(alpha)!=0.

The exact local order in §3 and P2(alpha)=alpha give

    ord_alpha K_alpha(P2(T))=q*m.

Indeed V(P2(T)) has nonzero constant term V(alpha);
there is no cancellation between this unit factor
and the power. Thus m>=q^4. If K_alpha is the zero
polynomial, the same local divisibility is automatic.
This covers inseparable outer polynomials and
arbitrarily high multiplicities without differentiation
of H or a characteristic-zero decomposition theorem.

For every root alpha of A we therefore have

    H(T)=alpha^(j-1)T mod(T-alpha)^(q^4).

Since alpha is in F_(q²), alpha^(q^4)=alpha, and

    T^(q^4)=alpha mod(T-alpha)^(q^4).

Raising this congruence to the nonnegative ordinary
power j-1 and multiplying by T gives

    T^(1+(j-1)q^4)=alpha^(j-1)T mod(T-alpha)^(q^4).

Subtracting the two proves divisibility of
H(T)-T^(1+(j-1)q^4) by every(T-alpha)^(q^4).
These factors are pairwise coprime because the q
roots are distinct, and A is monic. Their product
is exactly A(T)^(q^4), of degree q*q^4=q^5.
Thus the claimed congruence holds over the closure.

Finally both numerator and MONIC divisor lie in
F2[T]. Divide there. Extending scalars gives the
same quotient/remainder, and divisibility over the
closure forces that remainder zero by uniqueness.
This proves the actual F2 congruence, not only
separate extension-field pointwise equalities.

## 6. Boundary and degree consequences remain limited

At j1, H(P2)=P2 forces H=T by injectivity of
substitution by a nonconstant polynomial. CJ1
also gives that result, since deg H1<q^5.
The zero K_alpha branch is explicitly permitted.

For j2, the accepted degree ratio is q^4+1<q^5.
The comparison monomial has that same degree, so
CJ1 would force H=T^(q^4+1). Independently there
can be no such composition at all: at T0 the
recurrence has coefficients1 and gives
(P0,...,P4)(0)=(1,0,1,1,0); at T1 it has A1,B0
and P_r(1)=1 for all r>=1. Consequently

    P2(0)=P2(1)=1, P4(0)=0 !=1=P4(1).

Equal inputs to H cannot have those different
outputs. This endpoint obstruction is fully
rederived; its earlier unverified note is not
needed as a theorem premise.

For j>=3, deg H=1+q^4+...+q^(4j-4) exceeds
the q^5 modulus degree in the stated q range.
The congruence therefore permits a nonzero
multiple of A^(q^4); it does not determine H
or exclude composition. The congruence is
NECESSARY only. No compatibility of all higher
jets, indecomposability of P2, classification
of general factors, whole phi_(L2) criterion
or official full reducibility theorem follows.

## 7. Disposition and source boundary

All six end obligations pass in the companion
ledger. The new proof is elementary and complete
relative to the exact accepted GK recurrence
and degrees. No new external factorization,
APN/exceptionality, monodromy or Ritt theorem
is imported. The full GK body and its source
boundaries were read; its other sufficient
whole-divisor conclusions are not enlarged.

Recommend scoped acceptance of CJ1 only after
the other fresh whole audit and coordinator
reconciliation. No new CJ1 peer findings were
read before this freeze. All previous bytes
remain unchanged. No numerical experiment,
novelty or complete annual answer is claimed.

