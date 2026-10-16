# 2024 B4 proof register

No candidate full solution has been proposed. All arguments below have status **candidate proof - unverified**. They have not received the two independent adversarial audits required for promotion.

Every future proof begins as **candidate proof - unverified**. Distinguish published reproductions from original results. Do not relabel until two independent adversarial audits, a reconstruction and all repairs are complete.

## v0.1: Boundary and invariant lemmas, candidate proof - unverified

All identities here are in F2[x,y,z]. Put w=x+y+z, R=(x+y)(y+z)(z+x), and define Q,D as in research.md.

The elementary symmetric functions of x,y,z,w are 0,Q,R,D. Therefore

    product_{a in {x,y,z,w}} (1+a t)=1+Qt²+Rt³+Dt⁴.

Logarithmic differentiation is valid in the formal power-series ring because the denominator has constant term 1. Its derivative is Rt² (the other terms have even degree), while differentiating the product gives

    sum_a a/(1+a t)=Rt²/(1+Qt²+Rt³+Dt⁴).

Expanding 1/(1+a t) geometrically and multiplying by t gives

    sum_{n>=1} (x^n+y^n+z^n+w^n)t^n
        =Rt³/(1+Qt²+Rt³+Dt⁴).

Coefficient comparison and cancellation of the nonzero R in the integral domain proves

    sum_{n>=3} phi_n t^(n-3)=1/(1+Qt²+Rt³+Dt⁴).

Equivalently, H_0=1, H_j=0 for j<0, and H_j=QH_{j-2}+RH_{j-3}+DH_{j-4}, where phi_n=H_{n-3}. In the geometric expansion, each monomial Q^a R^b D^c in H_j has 2a+3b+4c=j. For odd n, j=n-3 is even, so b is even. This parity argument does not assert anything about individual factors.

The n=1 numerator is zero. Since zero is constant modulo 2 and F2[x,y,z] is an integral domain, two nonconstant polynomials cannot produce the prescribed zero product. The generating identity gives phi_3=1, so n=3 is excluded too. For every odd n>1 the original numerator is nonzero: in its binomial expansion the coefficient of x^(n-1)y is n=1 in F2, and pure terms do not cancel it. Thus the quotient is nonzero and has degree n-3.

## v0.1: finite identity at n205, candidate proof - unverified

The known Hernando--McGuire degree-10 factor, after homogenization, is phi_13=Q^5+QD²+R²D. This identification and phi_205=phi_13 B are checked by the exact script and certificate in computations/. The coefficient arrays in n205-certificate.json specify B completely. A reviewer can check multiplication over F2 without needing any irreducibility theorem or factorization oracle. This is an attributed published counterexample with an independently reproducible finite certificate, not a new solution to B4(b).

No proof based on a bounded scan has been proposed.
