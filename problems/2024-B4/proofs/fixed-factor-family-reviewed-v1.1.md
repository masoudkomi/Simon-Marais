# A fixed factor for an infinite set of exponents, accepted v1.1

**Proved, independently reviewed (partial result).** Coordinator acceptance,
2026-10-16, after two fresh blind full reconstructions. Both reports found
no substantive mathematical objection. This copy changes only the title
and status paragraph of frozen v1; its mathematical argument is unchanged.
The full 2024 B4(b) classification and this family's novelty remain unresolved.
See ../reviews/family-acceptance.md and the immutable initial reports.

Requested owner settings: gpt-6.1-sol, max reasoning. The launch interface
accepted the request; no verified effective-backend readback is available.

## Statement, scope and attribution

For an odd positive integer n, use the official polynomial

    f_n(x,y,z) = x^n+y^n+z^n+(x+y+z)^n

over F2, with coefficientwise equality. Write

    R = (x+y)(y+z)(z+x),    phi_n = f_n/R   (n>=3).

The quotient's existence follows in the argument below. The claim is

    phi_13 divides phi_n in F2[x,y,z]
    whenever n = n_m = (64*16^m+1)/5 = (4^(2m+3)+1)/5,  m>=0.       (1)

For m>=1 this supplies two nonconstant F2 factors of phi_n, and hence
integer polynomials g,h satisfying the congruence in B4(b). The initial
values are 13,205,3277,52429. At m=0 the cofactor is the unit 1; this
argument alone makes no decision about whether n=13 satisfies B4(b).
It also makes no exclusion claim for exponents outside (1).

The n=205 factorization was published by Hernando--McGuire, Section 6
of [arXiv:0903.2016v4](https://arxiv.org/pdf/0903.2016). The existing
`computations/n205-certificate.json` identifies their degree-10 factor
with phi_13. The present construction does not claim novelty for (1).
In particular, Férard's 2014
[publisher abstract](https://www.aimsciences.org/article/doi/10.3934/amc.2014.8.497)
announces both a phi_13 divisibility criterion and an infinite family in
the residue class 5 modulo 8. Its full theorem was not accessible in
this pass: the publisher's normal PDF endpoint requires login, and the
HAL deposit's document URL returned 404. The exact relation to (1)
therefore remains to be checked. No theorem from that paper is needed
for the proof below. The established preliminary Gold-family argument
is not reproduced or used.

## 1. An odd-index generating function

In F2[x,y,z], put

    w=x+y+z,
    Q=x^2+y^2+z^2+xy+yz+zx,
    D=xyz(x+y+z).

The elementary symmetric functions of the list x,y,z,w are 0,Q,R,D.
Thus, in a formal power-series ring,

    E(t) = product_(a in {x,y,z,w}) (1+a*t)
         = 1+Q*t^2+R*t^3+D*t^4.

This notation treats the list with multiplicity; it makes no assumption
that its entries have distinct numerical values. E has constant term 1,
so it is invertible as a formal power series. Formal differentiation
and the product rule give

    sum_a a/(1+a*t) = E'(t)/E(t) = R*t^2/E(t).

Expansion of the four geometric series, then multiplication by t, gives

    sum_(n>=1) f_n*t^n = R*t^3/E(t).                              (2)

In particular f_n=R*[t^(n-3)]E(t)^(-1) for every n>=3. This proves the
quotient exists without specialization to functions on a finite set.
Since R is nonzero, the quotient is unique in the polynomial ring.

Characteristic two gives E(t)^(-1)=E(t)/E(t)^2. Its terms of even
t-degree are exactly

    (1+Q*t^2+D*t^4)/(1+Q^2*t^4+R^2*t^6+D^2*t^8).

Consequently, on putting s=t^2,

    sum_(j>=0) phi_(2j+3)*s^j
        = (1+Q*s+D*s^2)/(1+Q^2*s^2+R^2*s^3+D^2*s^4).             (3)

All of these equalities concern formal power series; no convergence
or choice of numeric x,y,z is involved.

Introduce independent indeterminates q,u,d, and define P_j in
S=F2[q,u,d] by

    sum_(j>=0) P_j*s^j
        = (1+q*s+d*s^2)/(1+q^2*s^2+u*s^3+d^2*s^4).              (4)

Then phi_(2j+3)=P_j(Q,R^2,D) by (3). In the grading

    weight(q)=2,  weight(u)=6,  weight(d)=4,

P_j is homogeneous of weight 2j. Indeed, in the geometric expansion
of the denominator in (4), each coefficient has that weight; the
three numerator terms have the compatible weights 0,2,4.

For later identification, (4) gives

    P_0=1,  P_1=q,  P_2=q^2+d,  P_3=q^3+u,
    P_4=q^4+q^2*d+q*u+d^2,
    P_5=q^5+q*d^2+u*d =: A.                                   (5)

Thus A(Q,R^2,D)=phi_13.

## 2. Normalize on the formal divisor A=0

We will first prove A divides P_j for specific j in the independent
formal ring S. This does not assume that all factors of phi_n lie in
an invariant subring.

Let U=S[q^(-1),d^(-1)]. Because d is invertible in U, eliminating u
from A=0 shows

    U/(A) is isomorphic to F2[q,q^(-1),d,d^(-1)],
    u = q^5/d+q*d.

Put b=d/q^2. The same quotient is then
F2[q,q^(-1),b,b^(-1)], with

    d=q^2*b,    u=q^3*(b+b^(-1)).

Substitute s=z/q into (4) in this quotient. The normalized series is

    F(z,b) = (1+z+b*z^2)/K(z,b),
    K(z,b) = 1+z^2+(b+b^(-1))*z^3+b^2*z^4,                      (6)

and its coefficient of z^j is the image of q^(-j)*P_j. Its
coefficients lie in the Laurent ring Lambda=F2[b,b^(-1)], embedded
in the field E=F2(b). Both denominators in (4) and (6) have constant
term 1, so coefficient extraction and substitution commute here.

It remains to prove a coefficient vanishes in the symbolic series
(6), and then to descend from U back to S.

## 3. Three exact Cartier identities

For 0<=r<16 define an E-linear operator on E[[z]] by

    C_r(sum_(j>=0) a_j*z^j) = sum_(j>=0) a_(16j+r)*z^j.

This is coefficient selection only: it takes no sixteenth roots of
coefficients. If H is any series and G any series, their coefficient
convolution gives

    C_r(H(z)*G(z^16)) = C_r(H(z))*G(z).                          (7)

By Frobenius, K(z,b)^16=K(z^16,b^16). Therefore, for any polynomial
P(z) of degree at most 3,

    C_r(P(z)/K(z,b))
       = C_r(P(z)*K(z,b)^15)/K(z,b^16).                         (8)

Here the C_r in the numerator is applied to a finite polynomial.
Its z-degree is at most 63, so its selected polynomial has degree at
most 3. Formula (8) follows by applying (7) to the identity
P/K=(P*K^15)/K(z^16,b^16), whose denominator is a unit series.

Define the following Laurent polynomials in the indeterminate b:

    L = b^-7+b^-5+b^-3+b^-1+b+b^3+b^5+b^7,
    M = b^-6+b^-4+b^-2+1+b^2+b^6+b^8,
    J = b^-12+b^-6+b^-4+b^-2+1+b^2+b^4+b^6+b^8.

In particular J=M+b^4+b^-12. Direct finite multiplication gives

    C_5((1+z+b*z^2)*K(z,b)^15)
        = (L+M)*z+(L+J)*(z^2+b^16*z^3),                       (9)

    C_6(z*K(z,b)^15)
        = L*(z+z^2+b^16*z^3),                                (10)

    C_6((z^2+b*z^3)*K(z,b)^15)
        = M*z+J*(z^2+b^16*z^3).                              (11)

These are identities in F2[b,b^(-1),z], not checks at finitely many
parameter values. For a compact reconstruction, form

    K(z,b)^15 = product_(e in {1,2,4,8})
                 (1+z^(2e)+(b^e+b^(-e))*z^(3e)+b^(2e)*z^(4e)).

For (9), (10), (11), respectively, the coefficients of z^0,z^1,z^2,z^3
in the selected polynomial are

| Selected numerator | z^0 | z^1 | z^2 | z^3 |
|---|---|---|---|---|
| C_5((1+z+bz^2)K^15) | 0 | L+M | L+J | b^16(L+J) |
| C_6(zK^15) | 0 | L | L | b^16 L |
| C_6((z^2+bz^3)K^15) | 0 | M | J | b^16 J |

No higher z powers occur by the preceding degree bound. The exact
standard-library script `computations/cartier_family_certificate_v1.py`
reconstructs K^15 both as this Frobenius product and by 15 ordinary
multiplications. It verifies (9)-(11) by equality of full symbolic
monomial sets and saves those sets and all selected coefficients in
`computations/cartier-family-certificate-v1.json`. Its role is an
auditable finite certificate for the displayed general identities.
The argument for unrestricted m is the induction in the next section,
not the separate finite series checks also recorded by that script.

## 4. A span preserved by coefficient extraction

For each c=b^(16^k), k>=0, consider the E-linear space of series

    V(c) = { [alpha*z+beta*(z^2+c*z^3)]/K(z,c) : alpha,beta in E }.

Every member has zero constant coefficient, because its numerator
has zero constant coefficient and its denominator has constant term 1.
Combining (8) with (9) gives

    C_5 F(z,b) belongs to V(b^16).                              (12)

Equations (8), (10) and (11), with b replaced by c, give

    C_6 V(c) is contained in V(c^16).                           (13)

The replacement is valid because (9)-(11) are Laurent-polynomial
identities. In particular L(c),M(c),J(c) belong to E. Linearity in
the coefficient field E means that alpha,beta stay outside each
coefficient-selection operation; they are not raised to powers.
Explicitly, the input numerator alpha*z+beta*(z^2+c*z^3) maps to

    (alpha*L(c)+beta*M(c))*z
      +(alpha*L(c)+beta*J(c))*(z^2+c^16*z^3).

By induction from (12)-(13), for every m>=0,

    C_6^m C_5 F(z,b) belongs to V(b^(16^(m+1))).                (14)

Its constant coefficient is therefore zero.

Now set

    j_m = 5+6*16+6*16^2+...+6*16^m
        = (32*16^m-7)/5.                                     (15)

For m=0 the sum after 5 is empty. The hexadecimal expression of j_m
has m copies of the digit 6 followed by the digit 5. From the
definition of C_r, sequentially selecting the least significant
digit 5 and then m digits 6 gives

    [z^0](C_6^m C_5 F) = [z^(j_m)]F = 0.                     (16)

This can also be read directly from
C_6^m C_5 F=sum_(a>=0) [z^(16^(m+1)*a+j_m)]F*z^a.
Thus (16) holds for every nonnegative integer m, without a bound on m.

## 5. Descent and genuine factor degrees

Under the quotient map in Section 2, (16) says q^(-j_m)*P_(j_m)=0.
The vanishing in E is also vanishing in Lambda, since Lambda embeds
in E. Since q is a unit in U, P_(j_m) belongs to the principal ideal
A*U.

To clear the localization without losing divisibility, view

    A=d*u+q*(q^4+d^2)

as a polynomial in u over the UFD F2[q,d]. Its two coefficients are
coprime: every common factor of d and q*(q^4+d^2) would divide
both d and q^5, and q,d are independent indeterminates. A is therefore
primitive. It has degree one in u over F2(q,d), hence is irreducible
there; Gauss's lemma makes A irreducible in S. As S is a UFD, A is
prime. It divides neither q nor d (its u-degree is one, whereas those
polynomials have u-degree zero).

Membership P_(j_m) in A*U means that for some nonnegative a,b,

    A divides q^a*d^b*P_(j_m) in S.

Primality and A not dividing q*d imply A divides P_(j_m) in S.
Thus there is B_m in S with

    P_(j_m)=A*B_m.                                           (17)

Since the left side is homogeneous of weight 2j_m and A is
homogeneous of weight 10, B_m is homogeneous of weight 2j_m-10.
For completeness, decompose B_m into its finitely many weight
components. Their products with the nonzero homogeneous A have
distinct weights; all components of the wrong weight must vanish
because S is an integral domain. This justifies homogeneity without
assuming any injectivity of the substitution into x,y,z.

Substitute (q,u,d)=(Q,R^2,D) in (17). Using (3)-(5) gives

    phi_(2j_m+3) = phi_13 * B_m(Q,R^2,D).                      (18)

The integer 2j_m+3 is exactly n_m from (1). It is positive, odd and
integral: 64*16^m+1 is divisible by 5, since 16=1 modulo 5 and
64=-1 modulo 5, and it is odd.

For every odd n>1, the coefficient of x^(n-1)*y in f_n is n=1 in
F2. The three pure-power terms do not contribute to this mixed
monomial. Hence f_n is nonzero, and phi_n is a nonzero homogeneous
polynomial of degree n-3. In particular phi_13 is nonzero and has
degree 10. Equation (18) then forces B_m(Q,R^2,D) to be nonzero.
Its weighted homogeneity and the degrees 2,6,4 of Q,R^2,D show that
its actual total degree is 2j_m-10=n_m-13.

For m>=1, n_m>=205, so both factors in (18) have positive degree.
Choose the integer polynomials g,h obtained by lifting each F2
coefficient to 0 or 1. Equation (2) and (18) yield coefficientwise

    f_(n_m) = (x+y)(y+z)(z+x)*g*h  modulo 2,

where neither g nor h is constant modulo 2. This establishes the
candidate partial family asserted in (1). A determination of all
other qualifying odd n remains open in this research checkpoint.

## Reproduction and limitations

From the repository root, the exact symbolic certificate is generated by

```sh
.venv/bin/python -u problems/2024-B4/computations/cartier_family_certificate_v1.py
```

The completed recorded run used Python 3.12.14, no third-party modules,
a subprocess with a 30-second timeout, and incremental flushed output.
It finished in under one second; the retained job record gives its PID,
command, return code and elapsed time. No native factorization or
unbounded search is used. The separate coefficient checks at
(m,j,n)=(0,5,13),(1,101,205),(2,1637,3277) are finite evidence only.

Review obligations include the official coefficientwise domain, the
generating identity, the symbolic identities (9)-(11), E-linearity in
(13), digit order in (16), saturation in Section 5, and actual
nonvanishing/degrees after substitution. The proof does not use
absolute irreducibility, an exceptional-APN classification, or a
factorization oracle, and makes no assertion that its factors are
irreducible.
