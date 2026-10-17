# An exact proposed criterion for every whole Kasami divisor

2026-10-17 UTC. **Candidate proof — unverified.** Constructor: coordinator root. Two fresh initially blind nonconstructor WHOLE audits are required. This proposes necessity for the already accepted sufficient family. It concerns a WHOLE divisor, not every factor or the annual classification. No novelty claim.

Fix k>=2, q=2^k, d=q²−q+1, and odd n>=3. The proposed criterion(KC) is

    phi_d divides phi_n over F2
      iff n=(q^(2r+1)+1)/(q+1) for an integer r>=1.

The sufficient direction is precisely accepted GK1–GK2, including r=1 equality with a unit cofactor. The new argument below proves the necessary direction, conditional on the separately accepted exact CP1. Both dependencies retain their accepted scopes. No numerical experiment, CAS, finite orbit test or external monodromy classification is used.

## 1. Two homogeneous forms with a common finite symmetry

Work in the algebraic closure K of F2. It is infinite. Accepted CP1 gives from the hypothesis an ACTUAL polynomial identity

    g_n(U)=H(g_d(U)), H in F2[T],
    G_j(x):=x^j+(x+1)^j=g_j(x²+x).

Introduce independent variables X,Y and the homogeneous binary forms

    F(X,Y)=X^(q+1)+Y^(q+1),
    C(X,Y)=X^(q³+1)+Y^(q³+1),
    P_m(X,Y)=X^m+Y^m, m=(q+1)n.

For ANY point (X,Y) in K² with F(X,Y)=1, let x=X^(q+1), so x+1=Y^(q+1). Since (q+1)d=q³+1, the CP1 identity implies the POINTWISE equality

    P_m(X,Y)=G_n(x)=H(G_d(x))=H(C(X,Y)).       (1)

No division or evaluation of a rational function is involved. This equality is used only on F=1; it is not asserted to be a homogeneous identity with H(C) on all K².

Choose t in F_q minus {0,1}; k>=2 ensures existence. Choose roots a,b in K with

    a^(q+1)=t,  b^(q+1)=t+1.

Both are nonzero and belong to F_(q²): for example a^(q²−1)=t^(q−1)=1, so a^(q²)=a. Define the linear substitution

    M = [[a,b],[b^q,a^q]].

It has determinant a^(q+1)+b^(q+1)=1, and all four entries are nonzero. Write M^[j] for entrywise q^j-th powers. Direct multiplication gives

    M^T M^[1]=I.

Indeed each diagonal entry is t+(t+1)=1 and each off-diagonal entry is a repeated identical product, zero in characteristic2. Since all entries lie in F_(q²), M^[3]=M^[1]. For the column vector v=(X,Y)^T,

    F(Mv)=v^T M^T M^[1] v^[1]=F(v),
    C(Mv)=v^T M^T M^[3] v^[3]=C(v).          (2)

These are actual homogeneous polynomial identities. We do not assume that q²-Frobenius fixes X,Y; only the CONSTANT entries of M are in F_(q²).

## 2. Symmetry on F=1 forces symmetry of the full binary power sum

For any point v with F(v)=1, equations(1)–(2) give

    P_m(Mv)=H(C(Mv))=H(C(v))=P_m(v).

Let D(v)=P_m(Mv)+P_m(v), a homogeneous binary polynomial of degree m. For ANY v with F(v)!=0, choose lambda in K with lambda^(q+1)=1/F(v). Then lambda!=0, F(lambda v)=1 and

    0=D(lambda v)=lambda^m D(v),

so D(v)=0. To justify the polynomial conclusion explicitly, put v=(X,1). There are only q+1 roots of F(X,1)=X^(q+1)+1, whereas K is infinite. Thus D(X,1) vanishes at infinitely many X and is the zero polynomial. Homogeneity then makes D(X,Y) the zero polynomial. Consequently

    (aX+bY)^m+(b^q X+a^q Y)^m=X^m+Y^m.      (3)

This argument uses neither irreducibility of the curve F=1 nor a finite-field functional identity. It is a statement over the infinite algebraic closure.

## 3. A binary support obstruction

We prove directly that an odd m>1 satisfying(3), with all entries nonzero and det M!=0, has binary weight TWO.

For a nonnegative integer m with set-bit positions S, characteristic2 gives

    (1+Z)^m=product_(i in S) (1+Z^(2^i)).

Distinct subsets of S have distinct binary sums. Thus binomial(m,j) is odd precisely for subset sums j of those set bits. This supplies the only binomial-coefficient fact required here.

Suppose m has at least three set bits. Since m is odd, bit0 is present. Pick another set bit h>=1. With at least one further bit, BOTH j=2^h and j+1=2^h+1 satisfy 0<j<j+1<m and both corresponding binomial coefficients are1 in K. (The pick may be any nonzero set bit: the remaining bit makes the strict inequality.) In(3) the coefficients of X^(m-j)Y^j and X^(m-j-1)Y^(j+1) are zero, since they are mixed terms. Hence

    a^(m-j)b^j=(b^q)^(m-j)(a^q)^j,
    a^(m-j-1)b^(j+1)=(b^q)^(m-j-1)(a^q)^(j+1).

All factors are nonzero. Dividing the second equality by the first gives

    b/a=a^q/b^q,
    b^(q+1)=a^(q+1).

This contradicts a^(q+1)+b^(q+1)=1. Thus binary weight(m)<=2. Since m is odd and m=(q+1)n>1, weight1 would force m=1 and is impossible. Therefore

    m=2^s+1 for an integer s>=1.             (4)

The argument would fail without a symmetry having ALL four matrix entries nonzero; this is why q=2 cannot be inserted into it.

## 4. Integer divisibility gives exactly the claimed progression

Since q+1 divides m, equation(4) gives 2^k+1 dividing 2^s+1. Write s=A k+B with A>=0 and 0<=B<k. Modulo q+1,

    2^s+1 = (-1)^A 2^B+1.

If A is even, this representative is 2^B+1, strictly between0 and q+1, so cannot be divisible. If A is odd, its absolute value is 2^B−1, strictly smaller than q+1, so divisibility forces B=0. Consequently s is an ODD multiple of k, say s=k(2r+1), with r>=0. Then

    n=(2^s+1)/(q+1)=(q^(2r+1)+1)/(q+1).

At r=0 this gives n=1, outside the assumed n>=3. Thus r>=1, proving the proposed necessary direction. Accepted GK supplies the converse for every such r, completing KC within its stated scope.

## 5. Endpoints, relation to prior results and limits

At r=1, n=d and whole divisibility is equality; its cofactor is a unit and it is not alone a genuine official factorization. At every r>=2 the accepted GK positive-degree argument supplies two nonconstant modulo-two factors. q=4 recovers the separately accepted exact whole-phi13 criterion. For k>=3 this proposes the exact whole-phi_(q²−q+1) criterion for all exponents, including the sufficient families already established. It implies the separately accepted necessary valuation v2(n−1)=k, but does not edit or retrospectively change that earlier proof.

At q=2, phi3=1 divides every phi_n; for example n=5 is not in the proposed progression. The restriction k>=2 is therefore mathematically necessary, not just a proof convention. n=1 and n=3 retain the project's separate zero/unit boundaries; neither is silently added to KC's domain. For n<d the criterion correctly gives no whole divisor.

This is a WHOLE-polynomial statement over F2, conditional only on accepted CP1 and accepted GK for sufficiency. It does not classify individual Kasami components, arbitrary factors, all reducible phi_n or the annual open part. It uses no Janwa–Wilson absolute-factor theorem, finite group classification, monodromy theorem, MCM exceptionality theorem or group-order assertion. The earlier MCM/Hermitian/Frobenius reading motivated trying a matrix that fixes both displayed forms; every used symmetry and coefficient fact is proved above. Source/read boundaries and all-inference obligations accompany the frozen submission. Novelty is unestablished; the candidate must not be promoted before two complete fresh whole audits and coordinator reconciliation.
