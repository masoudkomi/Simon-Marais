# Separate the two coefficient maps before applying the moment lemma

2026-10-17 UTC. **Candidate proof — unverified; research continuation.** The earlier v1 elementary local-residue lemma is preserved. This continuation distinguishes an additional source normalization; neither note accepts the stronger diagonal theorem.

The publicly author-uploaded [original diagonal chapter, version2.0,2007-09-17](https://www.researchgate.net/publication/226863681_Class_Number_Conditions_for_the_Diagonal_Case_of_the_Equation_of_Nagell_and_Ljunggren) was reopened. Its actual §4 coefficient map is a Fourier sum of roots of unity. The later binary-Thue paper's b1 is a scaled reciprocal sum. The appendix footnote indicates a correspondence of roles; that alone is not an equality of these two formulas. Thus v1's local residue calculation should not be substituted literally for the original coefficient map.

Here is a different elementary candidate lemma that applies to Fourier sums. Use DIRECT automorphism indices sigma_a(zeta)=zeta^a. Let theta=sum_a n_a sigma_a, with integer n_a, a in F_p^*, and set

    F_theta(zeta)=sum_a n_a zeta^a,
    M_minus(theta)=sum_a n_a a^(-1) mod p.

If M_minus(theta)!=0, the p−1 conjugates F_theta(zeta^c), c in F_p^*, are pairwise distinct. To prove this, suppose the conjugates at c,d agree and put h=d/c. After applying sigma_(c^-1), the difference

    sum_a n_a Z^a − sum_a n_a Z^(ha mod p)

vanishes at zeta, has degree at most p−1, and has constant coefficient0. The minimal polynomial Phi_p=1+Z+...+Z^(p−1) has degree p−1 and constant1. Divisibility therefore forces the difference polynomial to be identically zero. The coefficient vector is invariant under multiplication by h. Taking inverse moments gives

    M_minus(theta)=h^(-1) M_minus(theta),

so h=1 and c=d, as claimed. A common overall minus sign in the coefficient map does not affect distinctness. With INVERSE source indices the same test must first be reindexed; the inverse moment in the direct basis must not be confused with the source's Fermat-module condition.

This is a conditional route to separating the actual original coefficients. The original application uses selected positive Fermat-module elements and particular weights. Their required inverse moment, and compatibility of a new choice with the signature/cancellation argument, still need to be proved in that exact setting. The later paper's existence construction in another context is not silently transplanted. The first-case and second-case selections must each be checked, including the two nonconjugate elements used in the second case.

The remaining matrix, all-conjugate cancellation and delta=0 issues remain open. No proposed theorem is refuted by this analysis; no computational example or stronger range exclusion is asserted. The original chapter's full proof was not newly reconstructed: the coefficient definitions and relevant §4 selections, Lemma14 and singular-system discussion were inspected. No new PDF cache, redistribution, charge or author contact occurred. The preceding proof is elementary and still requires two independent audits before promotion.
