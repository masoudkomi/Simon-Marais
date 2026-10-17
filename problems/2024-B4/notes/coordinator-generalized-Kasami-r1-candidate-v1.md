# Generalized Kasami whole divisors from a two-dimensional Frobenius recurrence

2026-10-17 UTC. **Candidate proof — unverified.** Constructor: coordinator root. This complete packet requires TWO fresh initially blind whole nonconstructor audits before acceptance. No novelty, full exponent classification, or unrestricted factor classification is claimed. No computation or finite extrapolation is used.

## Claim GK1: a polynomial recurrence for every q and every index

Work throughout over F2. For odd n>=3 use the separately accepted invariant polynomial g_n defined by

    x^n+(x+1)^n = g_n(x²+x).

For the auxiliary n=1 set g_1=1, which satisfies the same identity. Fix any integer k>=1, write q=2^k and

    d=q²−q+1,
    L_r=(q^(2r+1)+1)/(q+1)        (r>=0).

These are positive odd integers: q+1 divides q^(2r+1)+1 by the integer alternating-sum identity, and the resulting quotient is odd. In particular L_0=1, L_1=d, and L_2=(q⁵+1)/(q+1).

Define polynomials in F2[T] by

    A_q(T)=T^q+(T+1)^(q−1),
    B_q(T)=(T+1)^(q−1),
    P_0(T)=1,   P_1(T)=T,
    P_(r+2)(T)=A_q(T)^(q^(2r+1)) P_(r+1)(T)
                 + B_q(T)^(q^(2r+1)) P_r(T)    (r>=0).

Then the candidate assertion is the unrestricted polynomial identity

    g_(L_r)(U)=P_r(g_d(U))                  for EVERY r>=0.       (GK1)

For r>=1 the polynomial P_r is monic of degree

    E_r=(q^(2r)−1)/(q²−1)=1+q²+...+q^(2r−2);

P_0 has degree0. At r=2 the recurrence reduces exactly to the separately accepted CP2 identity

    P_2(T)=T^(q²+1)+(T+1)^(q²−q+1).

The argument below proves GK1 directly for every index; CP2 is a consistency check rather than an induction premise.

## 1. The auxiliary field and what is actually being paired

Let a be transcendental over F2, put b=a+1, and work inside an algebraic closure K of F2(a). Choose A,B in K with

    A^(q+1)=a,    B^(q+1)=b.

Such roots exist in K. Both are nonzero because a and b are nonzero rational functions. In particular

    A^(q+1)+B^(q+1)=1.                                      (1)

For vectors in K² use the ordinary bilinear dot product, and apply Frobenius coordinatewise: v=(A,B), v^[j]=(A^(q^j),B^(q^j)). There is no assumption that q²-Frobenius is the identity on K. No positivity, analytic inner-product property, or finite-field Hermitian theorem is used. The bracket is merely convenient notation for iterated Frobenius.

Define scalars

    D_r = v dot v^[2r+1]
        = A^(q^(2r+1)+1)+B^(q^(2r+1)+1).                     (2)

Because (q+1)L_r=q^(2r+1)+1, these scalars satisfy

    D_r = a^(L_r)+b^(L_r)=g_(L_r)(a²+a).                     (3)

This equality shows directly that D_r is independent of the choices of (q+1)-st roots. It does not turn a function identity on a finite field into a polynomial identity. We are working at a transcendental element.

Set c=D_1=g_d(a²+a); equation(1) gives D_0=1. The accepted invariant-degree result says g_d is monic of degree(d−1)/2>=1, including d=3 at q=2. Thus c+1 is a NONZERO element of K. This nonvanishing permits a temporary field calculation; no assertion about evaluating a denominator at every finite point is needed.

## 2. The exact vector relation

The following four pairings follow solely from (1)–(2) and Frobenius:

    v dot v^[1] = 1,
    v^[2] dot v^[1] = 1,
    v dot v^[3] = c,
    v^[2] dot v^[3] = 1.                                    (4)

For example, the second equality is (A^(q+1)+B^(q+1))^q=1, and the fourth is the same equality raised to q². Relative to the two linear functionals w -> w dot v^[1] and w -> w dot v^[3], the column vectors v^[2],v have pairing matrix

    [ 1  1 ]
    [ 1  c ].

Its determinant is c+1, nonzero. Hence v^[2] and v are linearly independent and form a basis of K². This is an actual two-dimensional basis argument, with no assumption about a Galois group or monodromy.

Write uniquely v^[4]=alpha v^[2]+beta v. Pairing with v^[1] and v^[3] gives

    alpha+beta = c^q,
    alpha+c beta = 1,                                      (5)

since v^[4] dot v^[1]=(v^[3] dot v)^q=c^q and v^[4] dot v^[3]=1. Adding the equations and using c^q+1=(c+1)^q yields

    beta=(c+1)^(q−1)=B_q(c),
    alpha=c^q+(c+1)^(q−1)=A_q(c).                          (6)

The coefficients are POLYNOMIALS in c. The sole division by c+1 in deriving them has canceled completely. Since(4) makes the two functionals independent, the coefficients recovered from(5) give the full vector relation, not only two necessary scalar equations.

## 3. Frobenius propagation gives every index at once

Raise the vector identity v^[4]=alpha v^[2]+beta v to q^(2r+1), for each integer r>=0. Frobenius preserves addition and multiplication in K, so

    v^[2r+5] = alpha^(q^(2r+1)) v^[2r+3]
                 + beta^(q^(2r+1)) v^[2r+1].               (7)

Taking the ordinary dot product with the ORIGINAL v, which is not raised in this step, gives

    D_(r+2)=A_q(c)^(q^(2r+1)) D_(r+1)
               +B_q(c)^(q^(2r+1)) D_r.                    (8)

The initial values D_0=1,D_1=c and the definition of P_r now prove D_r=P_r(c) by ordinary induction for every r>=0. Together with (3), this is the identity

    g_(L_r)(a²+a)=P_r(g_d(a²+a))                           (9)

in K. Both sides lie in F2[a], and a is transcendental, so it is an equality of polynomials in a. The substitution F2[U] -> F2[a], U->a²+a is injective: a nonzero polynomial of degree e maps to a nonzero polynomial of degree2e. Equation(9) therefore proves GK1 in F2[U]. In particular the final identity holds at every specialization, including zeros of c+1; the auxiliary field division has not excluded any polynomial points.

## 4. Degrees and the known r=2 endpoint

The polynomial A_q is monic of degree q and B_q is monic of degree q−1. Let E_r=(q^(2r)−1)/(q²−1), with E_0=0. Suppose P_r and P_(r+1) are monic with their stated degrees. The first summand defining P_(r+2) has degree

    q^(2r+2)+E_(r+1)=E_(r+2).

The second has degree (q−1)q^(2r+1)+E_r. Its difference from E_(r+2) is exactly q^(2r)(q+1)>0. Thus leading terms cannot cancel, and P_(r+2) is monic of degree E_(r+2). Initial P_0=1,P_1=T supply the induction. This also checks the necessary composition degree

    (L_r−1)/(d−1)=E_r.

At r=0 the recurrence for P_2 reads

    P_2 = [T^(q²)+(T+1)^(q(q−1))]T
              +(T+1)^(q(q−1))
        = T^(q²+1)+(T+1)^(q²−q+1).

This is exactly the accepted CP2 polynomial. No numerical check or extrapolation from that endpoint was used to obtain (7)–(9).

## Claim GK2: genuine official factors for every fixed q>=4 and every r>=2

The exact accepted CP1 criterion states that, for odd d,n>=3, the WHOLE homogeneous phi_d divides phi_n over F2 if and only if g_n is a polynomial in g_d over F2. Apply it to d=q²−q+1 and n=L_r with r>=1. GK1 therefore gives

    phi_(q²−q+1) divides phi_((q^(2r+1)+1)/(q+1))
            for EVERY q=2^k,k>=1, and EVERY r>=1.            (GK2a)

For q>=4 and r>=2 the divisor has degree d−3=q²−q−2>0, and the quotient has degree L_r−d>0. Both polynomials are nonzero: the accepted quotient degree is n−3 for odd n>=3. This gives two actual positive-degree F2 polynomials. Taking coefficientwise0/1 integer lifts supplies the required integer g,h, neither constant modulo2, in the official B4(b) congruence. This is the claimed sufficient family GK2, not an absolute-factor assertion.

The exponent is sometimes more conveniently written

    n_(k,m)=(q^(2m+3)+1)/(q+1),    q=2^k,

where m=r−1>=1. For each FIXED k>=2 these exponents grow strictly with m, so they give an infinite family. Their whole divisor remains the same phi_(q²−q+1), while the cofactor degree grows. The first q=8 case is m=1,n=3641; m=2 gives n=233017. These integers follow from the symbolic formula; no finite certificate for the latter exponent was run or needed.

## Claim GK3: exact scope beyond the older phi13 progression

For every k>=1 and r>=1,

    L_r−1 = q (q^(2r)−1)/(q+1),

and the indicated integer quotient is odd. Hence v2(L_r−1)=k. The separately accepted exact whole-phi13 theorem says its odd exponents n>=3 are precisely

    n=(64*16^j+1)/5, j>=0.

Every such exponent has v2(n−1)=2, since n−1=4(16^(j+1)−1)/5 with odd integer quotient. Thus for EVERY k>=3 and EVERY r>=1, phi13 does NOT divide phi_(L_r). In particular every qualifying new r>=2 member for k>=3 lies outside the old whole-phi13 progression. This conclusion excludes just that whole divisor, not all its individual absolute components.

At q=4 our sufficient progression is exactly n=(64*16^m+1)/5,m>=1, already covered by the accepted iff; no new necessity or novelty is claimed there. At q=2 the fixed divisor is phi3=1, so GK2a supplies no genuine official factorization. At r=0 the auxiliary n=1 is outside CP1 and is used only as a recurrence initial value. At r=1 divisibility is equality, with unit cofactor; it does not qualify by itself. The ordinary n=1 zero-polynomial and n=3 unit boundaries remain excluded under the existing accepted scope.

## Source, review and remaining-problem boundaries

The logical inputs are the exact accepted CP1 invariant/divisor criterion and quotient degree, and the accepted whole-phi13 iff only for GK3. Their precise files, hashes and scopes are in the companion source record. The proof of GK1 is elementary field and polynomial algebra supplied here. No MCM factor, Janwa–Wilson component theorem, exceptionality/APN result, monodromy classification, or group-order claim is imported.

The MCM literature led root to seek a two-dimensional Frobenius relation; the companion earlier literature note remains unverified and is not a theorem premise. The current proof does not require its candidate identification or proposed factor corollary. This is a literature-inspired deduction, with no novelty claim.

GK1–GK3 do not classify all n, all factors, or all possible compositions. They do not prove necessity for general fixed q. An individual phi_n factor need not be an entire phi_d. Failure of these whole-divisor tests is not treated as irreducibility. The full 2024 annual question remains unresolved, and the present complete proof remains UNVERIFIED until two initially blind nonconstructors reconstruct and adversarially audit it.
