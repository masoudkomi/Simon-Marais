# Exact first-case inverse moments

2026-10-17 UTC. **Candidate proof — unverified; research continuation.** Root constructor. This continues the two preserved earlier moment notes. It does not accept the original chapter's second-case theorem, matrix construction, or nonzero-cancellation step.

The [author-uploaded original chapter](https://www.researchgate.net/publication/226863681_Class_Number_Conditions_for_the_Diagonal_Case_of_the_Equation_of_Nagell_and_Ljunggren), internal version2.0,2007-09-17, was directly reread at §2.3 equations14–18, Lemma3 and its proof, and §4.3's first/second-case selections and Fourier coefficient definition. The source uses inverse automorphism indices in its Fuchsian coefficient formula. Its selected first-case elements are Θ2 and ψ2=Θ3−Θ2, once the stated Wieferich conditions put them in the Fermat module. The following calculation is elementary and does not use an unproved moment-selection assertion.

Let p>=5 be prime and let a be any positive integer coprime to p. Define

    Θ_a = sum_(c=1)^(p−1) floor(ac/p) σ_c^(-1).

In DIRECT indices σ_t, the inverse moment of Θ_a is therefore

    M_minus(Θ_a) = sum_(c=1)^(p−1) c floor(ac/p) mod p.

The reindexing matters: the source's Fermat-module functional is the OTHER moment, sum floor(ac/p)c^(-1), since it describes the action on ζ. It is not the moment calculated here.

Put k_c=floor(ac/p) and r_c=ac−pk_c. Because a is invertible modulo p, the r_c permute1,...,p−1. Thus, as an exact equality of integers,

    sum c² = sum r_c²
            = a² sum c² −2ap sum c k_c +p² sum k_c².

Divide by p and reduce modulo p. The integer sum c² equals p(p−1)(2p−1)/6; division by6 is valid modulo p because p>=5. Consequently

    2a sum c k_c = (a²−1)/6 mod p,
    M_minus(Θ_a) = (a−a^(-1))/12 mod p.             (FM1)

In particular,

    M_minus(Θ2)=1/8,
    M_minus(ψ2)=M_minus(Θ3)−M_minus(Θ2)=7/72.       (FM2)

The first identity holds for every p>=5. The second is stated for p>3; for p=7 its value is0, and for every prime p>7 it is nonzero. Both selected FIRST-CASE elements therefore have nonzero direct-index inverse moment for p>7, assuming they are selected in the exact source setting. Their positive half-weight is consistent with that setting. No doubling to weight p−1 is needed for this conclusion.

By the elementary Fourier-separation lemma in the preserved v1.1 note, the actual original Fourier coefficients η[σ_c Θ2] are pairwise distinct as c ranges over F_p^*. For p>7 the same holds for η[σ_c ψ2]. Thus the moment hypothesis for these PARTICULAR original first-case selections can be verified explicitly, rather than left conditional. The analogous reciprocal-map separation from v1 is also available with its own normalization; the Fourier and reciprocal formulas are still distinct maps.

For a general Fueter element ψ_n=Θ_(n+1)−Θ_n with p not dividing n(n+1), the same calculation gives

    M_minus(ψ_n)=(n²+n+1)/(12n(n+1)) mod p.         (FM3)

This may vanish. Accordingly, no arbitrary positive Fermat-module element, no unspecified pair from Lemma3, and no second-case selection is granted a nonzero inverse moment by this note. Even a nonzero moment for each selected element would establish only distinctness within its own conjugate list; disjointness of TWO different lists and compatibility with the signature system need additional arguments.

What this closes is the conditional moment test for two exact first-case elements. It does not show that the later appendix's scaled reciprocal coefficients equal the original Fourier coefficients; does not establish solvability of any singular inhomogeneous system; does not prove all-conjugate cancellation or δ!=0; and does not enlarge the accepted 2025 Diophantine exclusion. These candidate lemmas require two independent whole audits before promotion. No mathematical computation, scan, author contact, charge, new PDF redistribution, or novelty claim occurred.
