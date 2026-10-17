# Critical points of the first higher Kasami polynomial

2026-10-17 UTC. **Research deductions — unverified.** Root constructor. This is separate from the accepted CP/GK/KC packets and their audit scopes. It needs two other whole audits before promotion. It investigates the higher-family composition obstruction, without claiming a new annual exponent classification or novelty. No mathematical code, scan or CAS was used.

Fix q=2^k>=4. The separately accepted GK recurrence has

    A(T)=T^q+(T+1)^(q-1), B(T)=(T+1)^(q-1),
    P0=1, P1=T,
    P_(r+2)=A^(q^(2r+1))*P_(r+1)+B^(q^(2r+1))*P_r.

In particular P2=T^(q²+1)+(T+1)^(q²-q+1). These are exact accepted project identities, not a new external theorem import.

Multiplying A by T+1 gives T^(q+1)+1, hence A has exactly the q distinct roots alpha in mu_(q+1) other than1 in the algebraic closure of F2. All lie in F_(q²), and alpha^q=alpha^-1. The excluded alpha1 is not a root of A because A(1)=1. Differentiation gives

    P2'(T)=T^(q²)+(T+1)^(q²-q)=A(T)^q.

Thus those q roots are exactly the finite critical points. Every one is FIXED by P2. To check it, let u=alpha+1!=0. Then u^q=u/alpha and u^(q²)=u, so

    u^(q²-q+1)=u²/u^q=alpha*u,
    P2(alpha)=alpha²+alpha*u=alpha.

The finite local ramification index is q, not q+1. In the expansion at alpha, the linear term vanishes by P2'(alpha)=0. There are no exponents2,...,q-1: the binary exponents of q²+1 are0,2k, and those of q²-q+1 are0,k,...,2k-1. Its first surviving term is

    (alpha+1)^(q²-2q+1) Z^q,

whose coefficient is nonzero. This follows directly from the characteristic-two binary product for (u+Z)^n; it is not a claim that a derivative-zero of multiplicity q automatically has tame ramification q+1. Here the ramification is wild. The derivative zero itself has order q because A is separable at alpha.

The full GK recurrence also has simple exact evaluations at these critical points. A(alpha)=0, B(alpha)=alpha^-1, and raising the latter to q^(2r+1) gives alpha. Therefore

    P_(r+2)(alpha)=alpha*P_r(alpha),
    P_(2j)(alpha)=alpha^j,
    P_(2j+1)(alpha)=alpha^(j+1).

Differentiating the recurrence kills the Frobenius coefficient derivatives, since every exponent q^(2r+1) is even. With P0'=0,P1'=1 this gives

    P'_(2j)(alpha)=0,
    P'_(2j+1)(alpha)=alpha^j.

Consequently a hypothetical composition P_s=H(P2) requires s even by the derivative test at alpha. This agrees with the separately recorded necessary index divisibility and does not strengthen it by itself. At s=2j it also imposes H(alpha)=alpha^j on every such alpha; those finitely many values alone are not a composition criterion. The earlier symbolic0/1 example still rules out P4=H(P2), despite the degree condition2|4.

These observations identify an actual critical-fixed, wild polynomial structure that any decomposition argument must respect. They do NOT prove that P2 is indecomposable, classify compositions P_s=H(P_r), invoke a characteristic-zero Ritt theorem in characteristic2, classify individual Kasami components or settle arbitrary F2 factors. A postcritically finite observation alone is not a monodromy theorem.
