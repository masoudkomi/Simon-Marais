# Every even-index inner polynomial is excluded from all later GK compositions

2026-10-17 UTC. **Candidate proof - unverified.** Constructor: coordinator
root. This COMPLETE submission strengthens the separately preserved
P2-only v1. No v1 byte was changed and no audit of v1 is used. Two OTHER
independent initially blind WHOLE audits of this complete v2 are required.
No mathematical program, CAS, scan or example calculation was used.
Priority is unestablished. The classification is restricted to the
fixed-q accepted GK family and to EVEN inner indices; it is not the
complete official factorization problem.

## Exact definitions and proposed results

Let q=2^k>=4, and use the exact accepted polynomials over F2:

    A=T^q+(T+1)^(q-1), B=(T+1)^(q-1),
    P0=1, P1=T,
    P_(i+2)=A^(q^(2i+1))*P_(i+1)+B^(q^(2i+1))*P_i,
    F=P2=T^(q^2+1)+(T+1)^(q^2-q+1).

The accepted GK degree formula is

    deg P_i=E_i=1+q^2+...+q^(2i-2), i>=1.

**NJ1-v2.** For EVERY algebraically closed field K of characteristic2,
EVERY even integer r>=2, EVERY integer s>=1 and EVERY H in K[T],

    P_s=H(P_r)  if and only if  s=r and H=T.           (NJ1)

Coefficients of the displayed F2 polynomials are viewed in K. Arbitrary
extension coefficients and inseparable H are allowed. P0=1 is explicitly
outside s>=1. Nothing is asserted here for an ODD inner r>1. The result
does not say that P_r has no decomposition through some other polynomial.
In particular the separate unverified DI candidate is NOT a premise.

For the original polynomial application put

    d=q^2-q+1, L_i=(q^(2i+1)+1)/(q+1),
    x^n+(x+1)^n=g_n(x^2+x),
    phi_n=[x^n+y^n+z^n+(x+y+z)^n]/[(x+y)(y+z)(z+x)].

**NJ2-v2.** For EVERY even r>=2 and integer s>=1 in this SAME fixed-q
family,

    the WHOLE phi_(L_r) divides phi_(L_s) over F2
           if and only if s=r.                      (NJ2)

This is a whole-divisor classification inside one explicit family. It
does not exclude a proper component of phi_(L_r), any other divisor,
an odd-index inner polynomial, or any exponent outside this family.
The GK factorizations through the smaller whole phi_d remain valid.

## 1. Degrees dispose of smaller indices and odd target indices

The degrees E_i increase strictly for i>=1. Since P_s is nonconstant,
a hypothetical H is nonconstant and

    E_s=(deg H)E_r.

Thus s<r is impossible. At s=r, H has degree1 and the equality
H(P_r)=P_r forces H=T by injectivity of substitution by a nonconstant
polynomial (alternatively compare its leading term and its constant).

Since r is even, E_r=0 modulo q^2+1: its defining sum reduces to an
even alternating sum. For odd s, E_s=1 modulo q^2+1. Hence degree
divisibility excludes every odd s. It remains ONLY to exclude even
s>r. We do not need or assume the stronger integer equivalence between
E_r|E_s and r|s, nor any decomposition classification.

## 2. Critical point, finite constants and all-index value/derivative recurrences

Work over K and choose a root alpha of A. The exact identity

    (T+1)A=T^(q+1)+1

shows that A has q simple roots, the roots of unity of order dividing
q+1 other than1. The numerator has q+1 distinct nonzero roots, because
its derivative is T^q, and division removes only the simple root1.
In particular alpha!=0,1, alpha lies in F_(q^2), alpha^q=alpha^-1,
and u=alpha+1 is nonzero. Directly

    u^q=u/alpha, u^(q^2)=u,
    B(alpha)=alpha^-1,
    B(alpha)^(q^(2i+1))=alpha  for EVERY i>=0,
    F(alpha)=alpha^2+alpha*u=alpha,
    a:=A'(alpha)=B'(alpha)=u^(q-2)!=0.                (1)

At alpha the A term in every recurrence vanishes, so
P_(i+2)(alpha)=alpha P_i(alpha). Starting with P0=1,P1=T gives

    P_(2h)(alpha)=alpha^h,
    P_(2h+1)(alpha)=alpha^(h+1),   h>=0.             (2)

Every coefficient A^(q^(2i+1)),B^(q^(2i+1)) has formal derivative0,
since its exponent is a positive power of characteristic2. Differentiate
the entire recurrence BEFORE evaluating. At alpha it gives
P_(i+2)'(alpha)=alpha P_i'(alpha). Initial derivatives0,1 therefore give

    P_(2h)'(alpha)=0,
    P_(2h+1)'(alpha)=alpha^h,      h>=0.             (3)

These are exact formal derivative identities at the indicated constants;
Frobenius is not declared periodic on an indeterminate or a transcendental
field. No value or derivative of an unspecified H has been inferred yet.

## 3. Exact local order q at every even-index P_r

Put Z=T-alpha. First reconstruct the local order of F. Differentiation
of its displayed formula gives F'=A^q, so the linear coefficient at
alpha is zero. The binary exponents of q^2+1 are0,2k; those of
q^2-q+1 are0,k,k+1,...,2k-1. The characteristic-two binomial product
therefore has no term Z^e for2<=e<q in either summand. The coefficient
of Z^q comes only from the second summand and is
u^(q^2-2q+1)!=0. It follows that

    ord_Z(F(alpha+Z)-alpha)=q EXACTLY.               (4)

For even i>=2 the recurrence exponent q^(2i+1) is at least q^5.
Because A(alpha)=0 and B(alpha)^(q^(2i+1))=alpha, Frobenius gives

    P_(i+2)(alpha+Z)=alpha P_i(alpha+Z) mod Z^(q^5).

Iterating from P2 gives, for every h>=1,

    P_(2h)(alpha+Z)=alpha^(h-1)F(alpha+Z)
                                             mod Z^(q^5).     (5)

For the fixed even r=2h, equations(2),(4),(5) show that

    beta:=P_r(alpha)=alpha^h,
    V(Z):=P_r(alpha+Z)-beta has ord_Z V=q EXACTLY.   (6)

Indeed its leading coefficient is alpha^(h-1)u^(q^2-2q+1), nonzero,
and the error threshold q^5 is strictly larger than q. Notice that
beta need not equal alpha and may repeat for different h. No distinct
critical-value assertion about P_r is used.

## 4. The first two terms of the NEXT even recurrence

Now fix this r, put M=q^(2r+1), and use the EXACT recurrence

    P_(r+2)=A^M P_(r+1)+B^M P_r.                    (7)

We have M>=q^5>1. In the local variable Z, A^M has coefficient a^M
at Z^M and all its exponents are multiples of M. Similarly B^M-alpha
has only multiples of M and has no constant term. Consequently

    P_(r+2)(alpha+Z)-alpha P_r(alpha+Z)
                         has order at least M,              (8)
    [Z^(M+1)] of this difference
         =a^M P_(r+1)'(alpha)=a^M alpha^h!=0.       (9)

For the second equality use(3): the contribution of A^M P_(r+1)
is its degree-M term times the derivative of P_(r+1), with no other
possible M+1 exponent from A^M. The contribution of (B^M-alpha)P_r
is zero because it would require the zero derivative P_r'(alpha).
No omitted power of A^M or B^M is small enough to contribute.

Every subsequent even recurrence has exponent at least q^(2r+5),
which is strictly larger than M+1. Hence for every even s>=r+2,
iteration of those later recurrences modulo Z^(M+2) gives

    P_s(alpha+Z)=alpha^((s-r-2)/2)P_(r+2)(alpha+Z)
                                             mod Z^(M+2).    (10)

Set c=alpha^((s-r)/2). Combining(8)--(10) yields BOTH

    ord_Z(P_s(alpha+Z)-cP_r(alpha+Z))>=M,             (11)
    [Z^(M+1)](P_s(alpha+Z)-cP_r(alpha+Z))
          =alpha^((s-r-2)/2)*a^M*alpha^h!=0.        (12)

This includes s=r+2 with multiplier1. For larger s no sum of repeated
contributions at this exponent occurs: all later errors begin strictly
ABOVE M+1. The index exponent is a nonnegative integer; no reduction
of the number of steps modulo the characteristic can kill(12).

## 5. A polynomial in P_r cannot have that coefficient

Suppose P_s=H(P_r) for even s>r and set K_beta(Y)=H(Y)-cY. If
K_beta is identically zero, its composition contradicts(12) immediately.
Otherwise let m>=0 be the EXACT order of K_beta at Y=beta.
By ordinary factorization there is a polynomial W with W(beta)!=0
such that K_beta(Y)=(Y-beta)^m W(Y). Equation(6) then gives

    ord_Z K_beta(P_r(alpha+Z))=q*m.

By(11), m>=M/q=q^(2r). Expand K_beta at beta:

    K_beta(beta+Y)=b_(q^(2r))*Y^(q^(2r))
                        +sum_(j>=q^(2r)+1) b_j Y^j,          (13)

where the first displayed coefficient and any later ones may vanish.
On substituting Y=V(Z), the first term has exponents all divisible by
q^(2r), since that exponent is a power of characteristic2. But
M+1=q^(2r+1)+1 is not divisible by q^(2r). Every subsequent term in
(13) has order at least

    q(q^(2r)+1)=M+q>M+1.

Therefore its composition has coefficient ZERO at Z^(M+1), contradicting
(12). This argument includes an inseparable H, a multiple or zero
derivative at beta, and m strictly larger than q^(2r). It does not
assume a nonzero coefficient at the first allowed order in(13).

All even s>r are excluded. Together with Section1 this proves NJ1
in the complete stated range. Only one root alpha was required.

## 6. The original whole-polynomial divisibility consequence

The exact accepted GK identity is g_(L_i)=P_i(g_d) for every i>=1.
The exact accepted CP1 criterion, for odd a,b>=3, is

    phi_a|phi_b over F2 iff g_b=H(g_a) with H in F2[T].

For q>=4 the integers L_r,L_s are odd and at least3 whenever
r,s>=1. If phi_(L_r)|phi_(L_s), this criterion and GK give

    P_s(g_d)=H(P_r(g_d)).

Substitution by the nonconstant g_d is injective over F2, by leading
degrees. It follows that P_s=H(P_r). NJ1 forces s=r and H=T.
Conversely s=r is equality and hence divisibility. This proves NJ2.
No absolute-factor field or finite-point test is used in this descent.

L0=1 is the auxiliary zero-numerator boundary and was not passed
through CP1. Equality at s=r has a unit cofactor in NJ2, so it does
not add a qualifying two-positive-degree factorization. For s>=2
the smaller whole phi_d still supplies the accepted GK factorizations;
NJ2 does not declare these polynomials irreducible. The full official
part(b) remains unresolved. No preliminary part(a) proof is reproduced.

## Sources, failed routes and limits

The ONLY mathematical theorem inputs are accepted
[GK recurrence/degrees/identity](../proofs/reviewed-generalized-Kasami-v1.1.md)
and, solely for NJ2, accepted
[CP1 whole-divisor/composition criterion](../proofs/reviewed-composition-Kasami-v1.1.md).
Exact bodies and acceptance records are frozen in the manifest.
[Accepted CJ](../proofs/reviewed-P2-critical-jet-v1.1.md) motivated
retaining the next coefficient; all needed local steps are reconstructed
in Sections2--5. The P2-only candidate v1 is preserved history, not a
separate theorem premise. The unverified DI criterion is not used.
No new external source import, download or monodromy theorem is used.
Published methods/provenance of accepted inputs remain as recorded there;
no priority assertion is made for the current deductions.

Weaker failed routes: degree alone leaves even s; the0/1 endpoint test
only excludes indices congruent1 modulo3; the older CJ modulus alone
allows large remainder multiples. None gives the present all-index
conclusion. The crucial extra information is the NONZERO coefficient
M+1 in(12) and its FORBIDDEN exponent in(13). A repeated derivative
root alone would not justify the exact local order, so(4) is explicitly
proved instead. General decomposition theorems and full APN
classification are unnecessary and are not inferred.

The proof leaves odd inner r>1, all other composition factors, individual
components and arbitrary n open. It is stronger than the preserved
P2-only version but remains a scoped partial result. Every proposed
theorem is unverified until TWO other whole audits and coordinator
reconciliation are complete. Administrative hashes are not proof.

## Ten required whole-audit obligations

1. Exact accepted definitions, degrees, all quantifiers and K/H domains.
2. Smaller/odd s excluded by degrees, s=r uniquely H=T, P0 separate.
3. Root alpha, nonzero a, all value/derivative recurrences(1)--(3).
4. Binary support gives exact order q for F, and(5)--(6) for EVERY even r.
5. Fixed-r exponent M=q^(2r+1) and exact next recurrence(7)--(8).
6. Nonzero coefficient(9), including both summands and vanishing P_r'.
7. Every later recurrence retains it via(10)--(12), without step counting.
8. Exact-order multiplication and(13), allowing zero/inseparable cases.
9. Frobenius exponent gap forbids M+1 and proves the all-index contradiction.
10. CP1/GK injective substitution proves ONLY the fixed-family WHOLE
    divisor classification NJ2, with all official scope boundaries retained.

Root is constructor and cannot count as either independent auditor.
