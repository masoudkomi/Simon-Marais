# The next critical coefficient excludes every later composition through P2

2026-10-17 UTC. **Candidate proof - unverified.** Constructor: coordinator
root. Two OTHER independent initially blind WHOLE audits are required.
No mathematical code, CAS, sample or scan was used. Priority is
unestablished. This is a complete proposed classification of ONE
composition question within the already accepted GK family; it is NOT
the complete official polynomial-factorization classification.

## Exact objects and proposed claims

Fix q=2^k>=4. Over F2 put

    A=T^q+(T+1)^(q-1), B=(T+1)^(q-1),
    P0=1, P1=T,
    P_(r+2)=A^(q^(2r+1))*P_(r+1)+B^(q^(2r+1))*P_r.

The exact accepted GK result gives

    F:=P2=T^(q^2+1)+(T+1)^(q^2-q+1),
    deg P_r=E_r=1+q^2+...+q^(2r-2)  (r>=1).

**NJ1.** For every algebraically closed field K of characteristic2,
every integer s>=1 and every H in K[T],

    P_s=H(F)  if and only if  s=2 and H=T.

The coefficients of P_s and F are regarded in K. In particular the
assertion includes arbitrary extension coefficients and inseparable H.
P0 is separately the constant1 and is excluded by s>=1. This is NOT
an assertion that F itself has no decomposition (the separate DI
candidate concerns that different question and is NOT a premise here).

For the factor consequence use the accepted definitions

    d=q^2-q+1, L_r=(q^(2r+1)+1)/(q+1),
    x^n+(x+1)^n=g_n(x^2+x),
    phi_n=[x^n+y^n+z^n+(x+y+z)^n]/[(x+y)(y+z)(z+x)].

**NJ2.** Among this fixed-q GK family with s>=1,

    the WHOLE phi_(L_2) divides phi_(L_s) over F2
          if and only if s=2.

Thus equality is the sole such whole-divisor case. This does not exclude
individual components, other divisors, compositions through a different
polynomial, or genuine factorizations already supplied by phi_d.

## 1. Degree leaves only even s

F has degree q^2+1. A hypothetical composition with nonconstant P_s
has nonconstant H and degree (q^2+1)deg H=E_s. Reduction of the sum
defining E_s modulo q^2+1 gives1 when s is odd and0 when s is even,
since q^2=-1 in that integer quotient. Therefore s must be even.
The s=1 degree obstruction is included. Write s=2j, j>=1.

For j=1, P_s=F and injectivity of substitution Y->F(T) in K[Y]
immediately forces H=Y. It remains to exclude every j>=2.

## 2. Reconstruct one critical fiber and its exact local order

The accepted GK recurrence is the only mathematical theorem needed
for NJ1. The local information from accepted CJ is reconstructed here.
Work over K and choose ANY root alpha of A. Such roots exist since
K is algebraically closed and A has degree q. The identity

    (T+1)A=T^(q+1)+1

shows that the roots are exactly the q elements of mu_(q+1) other
than1. The numerator has q+1 distinct roots (its derivative is T^q,
and none is zero). In particular alpha!=0,1, alpha^q=alpha^-1,
alpha lies in F_(q^2), and A'(alpha) is nonzero.

Put u=alpha+1. Then u!=0, u^q=u/alpha, u^(q^2)=u, and

    B(alpha)=alpha^-1,
    B(alpha)^(q^(2r+1))=alpha  for every r>=0,
    F(alpha)=alpha.

The last equality follows explicitly from
u^(q^2-q+1)=alpha*u and alpha^(q^2+1)=alpha^2.
Both A' and B' equal (T+1)^(q-2), so in particular

    a:=A'(alpha)=u^(q-2)!=0.

Use the local variable Z=T-alpha. Direct differentiation gives
F'=A^q. A binary-exponent expansion of F about alpha is needed to
avoid confusing derivative multiplicity and local order: q^2+1 has
binary exponents0,2k; q^2-q+1 has exponents0,k,k+1,...,2k-1.
There are no terms Z^e for2<=e<q in either expansion; the linear
term cancels by F'(alpha)=0; and the coefficient of Z^q is
u^(q^2-2q+1)!=0. Consequently

    V(Z):=F(alpha+Z)-alpha has ord_Z V=q EXACTLY.       (1)

All q-power statements on indeterminates in this proof use Frobenius,
not a finite-field polynomial-function identification.

## 3. The old common jet and its first previously unused coefficient

Set M=q^5. For every even r>=2 the recurrence exponent
q^(2r+1) is at least M. At alpha, the A coefficient vanishes, and
the B coefficient has value alpha. Frobenius therefore gives

    P_(r+2)(alpha+Z)=alpha P_r(alpha+Z) mod Z^M.

Iterating from r2 yields for every j>=1

    P_(2j)(alpha+Z)=alpha^(j-1)F(alpha+Z) mod Z^M.      (2)

We now retain ONE more coefficient instead of discarding everything
at order M. The exact first two recurrence instances needed are

    P3=A^(q^3)F+B^(q^3)T,
    P4=A^M P3+B^M F.

All q^3-th-power coefficient derivatives vanish, so

    P3'(alpha)=A(alpha)^(q^3)F'(alpha)+B(alpha)^(q^3)
              =alpha!=0.                            (3)

Since A(alpha)=0 and A'(alpha)=a, the coefficient of Z^M in
A(alpha+Z)^M is a^M. All its other exponents are multiples of M,
so it has NO term of exponent M+1. Similarly B(alpha+Z)^M-alpha
has order at least M and only multiples of M, because
B(alpha)^M=alpha. Finally F(alpha+Z) has linear coefficient0.
It follows from P4-alpha F that

    [Z^(M+1)](P4(alpha+Z)-alpha F(alpha+Z))
          =a^M P3'(alpha)=a^M alpha!=0.              (4)

Indeed the second summand (B^M-alpha)F has no Z^(M+1) term:
it would require the zero linear coefficient of F. No omitted
coefficient of A^M or B^M can contribute, since M>1.

For every subsequent even recurrence r>=4 the exponent is at least
q^9, and q^9>M+1. Therefore the same recurrence, now modulo
Z^(M+2), gives

    P_(2j)(alpha+Z)=alpha^(j-2)P4(alpha+Z)
                       mod Z^(M+2),  j>=2.

In particular, with c=alpha^(j-1), equations(4) and this identity give

    [Z^(M+1)](P_(2j)(alpha+Z)-c F(alpha+Z))
          =alpha^(j-2)*a^M*alpha!=0.                 (5)

This coefficient is nonzero for EVERY j>=2. The integer j is not
being replaced by a field element; no divisibility of j by2 or by
q+1 can make the displayed nonzero power of alpha vanish.

## 4. No composition can have this next coefficient

Suppose P_(2j)=H(F) with j>=2, and put K_alpha(Y)=H(Y)-cY,
where c=alpha^(j-1). Equation(2) says K_alpha(F(alpha+Z)) has
order at least M. If K_alpha were identically zero, equation(5)
would already contradict it. Otherwise let m be its EXACT order
at Y=alpha. Factoring it there and applying (1) gives

    ord_Z K_alpha(F(alpha+Z))=q*m,

including an inseparable K_alpha and any zero derivative. Thus
m>=M/q=q^4. Write its ordinary polynomial expansion at alpha as

    K_alpha(alpha+Y)=b_(q^4)Y^(q^4)
                       +sum_(h>=q^4+1) b_h Y^h,     (6)

allowing the first displayed coefficient and any later ones to vanish.
On substituting Y=V(Z), the first term has exponents all divisible
by q^4, since q^4 is a power of the characteristic. But M+1=q^5+1
is NOT divisible by q^4. Every later term has order at least
q(q^4+1)=M+q>M+1. Hence

    [Z^(M+1)] K_alpha(F(alpha+Z))=0.                  (7)

Equations(5) and(7) contradict each other. This excludes ALL j>=2
and proves NJ1, together with the degree and identity cases in
Section1. Only one critical point was required; no matching of
different critical values, global congruence descent, monodromy
classification or complete decomposition theorem was used.

## 5. Transfer to the actual whole polynomial divisor

The accepted GK identity is g_(L_s)=P_s(g_d), for every s>=1.
The accepted CP1 criterion says for odd a,b>=3 that the WHOLE
phi_a divides phi_b over F2 if and only if g_b is in F2[g_a].
Apply it with a=L_2,b=L_s, noting that q>=4 gives L_s>=3
for every s>=1. We have g_(L_2)=F(g_d). If divisibility holds,
there is H in F2[T] with

    P_s(g_d)=H(F(g_d)).

The nonconstant g_d makes substitution by g_d injective, by degrees.
Thus P_s=H(F), and NJ1 forces s=2. Conversely s2 is equality and
therefore divisibility. This proves NJ2. The case s0 is not included:
L0=1 is the auxiliary zero-numerator boundary rather than an
application of the nonzero CP1 criterion.

For s>=2 the earlier GK factorization through the smaller phi_d
continues to exist. NJ2 does not call any such phi_(L_s) irreducible,
does not rule out a proper component of phi_(L_2), and does not
classify other exponents outside this fixed-q family. Equality at
s2 has unit cofactor in NJ2 and is not an additional genuine official
factorization. The official part(b) remains unresolved.

## Sources, failed routes and audit obligations

Exact mathematical theorem inputs are the accepted
[GK recurrence, degrees and identity](../proofs/reviewed-generalized-Kasami-v1.1.md)
and, ONLY for NJ2, the accepted
[CP1 whole-divisor/composition criterion](../proofs/reviewed-composition-Kasami-v1.1.md).
Their acceptance records and hashes are frozen with this submission.
The [accepted CJ necessary jet](../proofs/reviewed-P2-critical-jet-v1.1.md)
motivated retaining the NEXT coefficient; all its needed local
calculations are reconstructed above. DI is unverified and unused.
No new external source theorem, download or theorem-priority assertion
is needed. Published/provenance boundaries of the accepted inputs
remain unchanged. This is part(b) research, not a reproduction of
official preliminary part(a).

Failed/weaker routes: the degree condition alone leaves all even s;
the0/1 endpoint test excludes s congruent1 modulo3 but leaves other
even s; and CJ's modulus alone allows large remainder multiples for
j>=3. None of those was promoted to an all-index obstruction.
The NEW claim depends on the exact nonzero coefficient(5) and the
Frobenius gap in(6), not an extrapolation from the earlier s4 example.

Two fresh nonconstructor whole audits must check ALL ten obligations:

1. Exact accepted definitions, degrees, original domains and allowed H.
2. Degree divisibility: all odd s excluded, s2 identity unique, P0 separate.
3. Existence/location of alpha, nonzero A'(alpha), B odd-Frobenius values.
4. F(alpha)=alpha, zero linear term and EXACT local order q.
5. Every even recurrence gives (2) with the same M=q^5.
6. Exact P3 derivative alpha and coefficient a^M alpha in (4).
7. Later exponents >=q^9 retain that coefficient for EVERY j>=2.
8. Multiplication of exact local orders and expansion(6), including zero,
   missing leading terms, inseparable H and algebraic-closure coefficients.
9. Frobenius exponent gap makes (7) zero and contradicts(5).
10. CP1/GK injective substitution proves ONLY NJ2's fixed-family WHOLE
    divisor classification; no individual-component/full-annual claim.

Root constructed this argument and cannot supply either independent
review. Candidate/manifest integrity checks are administrative only.
The exact written candidate must survive both audits and coordinator
reconciliation before any claim is labelled proved.
