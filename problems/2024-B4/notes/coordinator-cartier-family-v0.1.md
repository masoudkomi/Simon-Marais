# Cartier-operator route to an infinite fixed-factor family

Coordinator construction, 2026-10-16. **Candidate proof - unverified.** This is a partial family, not the requested full classification. Neither a novelty claim nor two independent mathematical audits has been established. An owner must verify every displayed identity and the localization/descent argument before freezing a candidate for independent reviews.

Proposed statement: phi_13 divides phi_n whenever

    n = (4^(2m+3)+1)/5, m>=0.

For m>=1 this would give a nontrivial factorization, since n>13. The m=1 example n205 is already attributed to Hernando--McGuire. The previously computed n3277 is m=2. No novelty for the larger family is asserted.

Use independent formal invariants Q,R,D and T=R². From the invariant generating function in proof.md, its even-index part is

    sum_{j>=0} phi_(2j+3) s^j
      = (1+Qs+Ds²)/(1+Q²s²+Ts³+D²s⁴).

This follows by multiplying the full denominator by its odd-term conjugate in characteristic two. Let A=Q⁵+QD²+TD (the formal phi_13), invert Q,D, put b=D/Q², and rescale z=Qs. Modulo A, T/Q³=b+b^-1, so the normalized even part becomes

    F(z,b) = (1+z+bz²)/K(z,b),
    K(z,b) = 1+z²+(b+b^-1)z³+b²z⁴.

Its coefficient at z^j is phi_(2j+3)/Q^j in the localized quotient.

Define C_r(sum a_j z^j)=sum a_(16j+r) z^j, with coefficients in F2(b). Since K(z,b)^16=K(z^16,b^16), for any numerator P of degree at most 3,

    C_r(P/K) = C_r(P K^15)/K(z,b^16).

These operators are linear over the coefficient field F2(b). All following identities are Laurent-polynomial identities in the formal b, not tests at finitely many b values.

Put

    L = b^-7+b^-5+b^-3+b^-1+b+b³+b⁵+b⁷,
    M = b^-6+b^-4+b^-2+1+b²+b⁶+b⁸,
    J = M+b⁴+b^-12.

Direct sparse multiplication of K*K²*K⁴*K⁸ gave the following identities, which still need independent reconstruction:

    C_5((1+z+bz²)/K)
      = [(L+M)z+(L+J)(z²+b^16 z³)]/K(z,b^16),

    C_6(z/K)
      = L[z+z²+b^16 z³]/K(z,b^16),

    C_6((z²+bz³)/K)
      = [Mz+J(z²+b^16 z³)]/K(z,b^16).

Thus C_5 F has numerator in the span of z and z²+b^16 z³, and C_6 carries that span (with b replaced by a current parameter c) into the corresponding span with parameter c^16. Every such numerator has zero constant term. Consequently the proposed induction gives

    [z^j_m]F=0,  j_m=(32*16^m-7)/5.

Indeed j_m has hexadecimal digits 6...65, with m copies of 6, so extract its final digit 5 and then m digits 6 via C_5 followed by C_6 repeatedly. The remaining constant coefficient is zero. Since 2j_m+3=(64*16^m+1)/5, these are exactly the proposed exponents.

Descent obligation: in S=F2[Q,T,D], A is primitive and linear in T, with gcd(D,Q(Q⁴+D²))=1, hence irreducible and prime. It divides neither Q nor D. Vanishing after localizing at Q,D should therefore imply A divides the formal phi_n in S. Then substitute T=R² and the actual x,y,z invariants. Both factors must be shown nonzero, with actual degrees 10 and n-13, so m>=1 is genuinely a nonconstant factorization in the official ring. The original numerator/nonzero boundary argument is available in proof.md but still requires audit.

The two short exploratory commands ran exact standard-library sparse multiplication in characteristic two, with Laurent exponents, and printed all numerator coefficients. They did not use numeric specialization or a factorization oracle. A reproducible script/certificate and a complete versioned owner proof are still required; do not promote this exploratory note.
