# Whole initial R1 audit: diagonal coefficient and moment lemmas MS1–MS5

2026-10-17 UTC. Reviewer `review_2022_complexity_r2`. **Independent audit of a candidate proof; no promotion.** No substantive objection found to the consolidated five algebraic claims in their written scopes. There is no new Diophantine exclusion or completed repair of an external proof.

The complete 7096-byte consolidated candidate, all four preserved earlier moment notes, the appendix inspection note, source records, all fourteen obligations and constructor manifest were read. Primary definitions and the relevant proof/application passages were inspected directly. This complete report, separate inference ledger, source checks and integrity record freeze before any new peer MS finding is read. Root constructed the packet; I supplied no contribution to it. Earlier roles include independent PG and CF1 reviews, not construction of MS or reconstruction of the entire diagonal literature. Requested settings are `gpt-6.1-sol`/`max`; independent effective-setting readback remains unavailable.

## Scope and conventions

The official 2025 B4(b) concerns integer quadruples with n,q≥2 and a geometric sum of degree n, hence n+1 terms. MS1–MS5 are supporting cyclotomic algebra, not an exclusion for all or any new subset of that full signed domain. No step solves preliminary part (a). Old PG/CF1 acceptances are independent background and are not premises of these proofs.

Fix an odd prime p, a primitive pth root ζ, K=Q(ζ), O=Z[ζ], λ=1−ζ, and direct indices σ_a(ζ)=ζ^a. Left multiplication by σ_h on Z[G] multiplies direct indices by h modulo p. The word “conjugate” for group-ring elements in this packet means that left G-action, as the displayed formulas specify; it does not mean internal conjugation in the abelian ring. Put

\[
M_-(\theta)=\sum_a n_a a^{-1}\in\mathbb F_p,\quad
E(\theta)=\sum_a n_a\zeta^a,\quad
R_c(\theta)=\sum_a n_a\frac{\lambda}{1-\zeta^{ac}}
\]

for \(\theta=\sum_a n_a\sigma_a\in\mathbb Z[G]\). Coefficients may be negative. M_- reduces coefficients modulo p, while E and R use their actual integer values. No arbitrary change of an integer lift is made in an exact equality in K.

## MS1: residue separation of the reciprocal coordinates

The presentation O=Z[Z]/(Φ_p(Z)) yields

\[
O/(\lambda)\cong\mathbb Z[Z]/(\Phi_p(Z),1-Z)\cong\mathbb Z/(p)=\mathbb F_p.
\]

Thus (λ) is maximal. For the representative 1≤t<p of a nonzero residue, the geometric sum \(S_t=1+\zeta+\cdots+\zeta^{t-1}\) reduces to t, so it is a unit in O_(λ). Its inverse equals λ/(1−ζ^t) and reduces to t^-1. The substitution t≡ac mod p is legitimate because a,c are units and ζ has order p; no denominator vanishes. Additivity applies to arbitrary integer coefficients, including negative ones. Therefore

\[
R_c(\theta)\bmod\lambda=c^{-1}M_-(\theta).
\]

If M_-(θ) is nonzero, these p−1 residues are pairwise different, so the elements of K are different. Multiplying the entire list by a single common nonzero field scalar preserves inequality, even if the scalar is not a local unit; this latter conclusion is ordinary field cancellation, not an unwarranted residue calculation.

A critical normalization check is that R_c is an array obtained by shifting θ, not necessarily the actual conjugate array of R_1(θ):

\[
\sigma_c(R_1(\theta))=\frac{1-\zeta^c}{1-\zeta}\,R_c(\theta).
\]

For example θ=σ_1 has R_1=1, whose Galois conjugates are all one, although the R_c array is distinct by MS1. The candidate correctly calls the R_c a list of numbers and does not assert the false Galois-orbit interpretation. This check also shows why a different scalar at every c cannot be silently allowed.

## MS2: faithful and equivariant Fourier evaluation

If E(θ)=0, the polynomial P(Z)=Σ_(a=1)^(p−1) n_a Z^a has degree at most p−1, zero constant coefficient and a root ζ. The minimal polynomial is Φ_p of degree p−1 with constant coefficient one. Its irreducibility can also be checked by Eisenstein after the shift Z↦Z+1. Hence P is a rational constant multiple of Φ_p (or zero); comparison of constant coefficients forces that multiple to zero. Every n_a is zero. This proves injectivity with no weight, positivity, Fermat-module or moment assumption.

Multiplication of indices gives E(σ_c θ)=σ_c E(θ). Injectivity then gives exact equality of stabilizers. If E(σ_c θ_1)=E(σ_d θ_2), the two shifted integer group-ring elements are equal, making θ_1 and θ_2 conjugate under the stated action. Consequently nonconjugate elements have disjoint SETS of Fourier conjugate values. This does not require, and does not imply, that entries inside either list are all distinct. E is claimed to be a Z-linear G-map, not a ring homomorphism.

## MS3: inverse moment and trivial stabilizer

Reindexing the sum for σ_h θ gives

\[
M_-(\sigma_h\theta)=h^{-1}M_-(\theta).
\]

If σ_h θ=θ and M_-(θ)≠0, field cancellation yields h=1. Thus the group-ring stabilizer is trivial, and MS2 makes all p−1 Fourier conjugates distinct. This proof uses the Fourier map, not a transferred injectivity assertion about the reciprocal map.

The condition is only sufficient. The element pσ_1, for example, has zero inverse moment and trivial stabilizer. Conversely the norm element N=Σ_a σ_a has M_-(N)=0 and E(N)=−1, fixed by all automorphisms. It has positive coefficients and weight p−1. It belongs to the actual source Fermat module: (1+complex conjugation)Θ_2=N puts it in the Stickelberger ideal, and its multiplicative action on ζ is ζ^(Σa)=1 for odd p. Therefore positivity, that weight and Fermat-module membership alone cannot replace the moment or stabilizer check. This reconstructs the candidate's counterexample with the source's extra ideal membership included.

Nor can Fourier injectivity be transferred to the reciprocal map. For p≥5 and b not congruent to ±1, the nonzero group-ring element

\[
\sigma_1+\sigma_{-1}-\sigma_b-\sigma_{-b}
\]

maps to zero under R_1, because 1/(1−u)+1/(1−u^-1)=1. In fact every R_c vanishes on it. Its inverse moment is zero, so it is no counterexample to MS1. This is an exact algebraic challenge to a tempting extra claim that the candidate expressly avoids.

## MS4: exact Fuchsian inverse moment

The source-index formula is

\[
\Theta_a=\sum_{c=1}^{p-1}\left\lfloor\frac{ac}{p}\right\rfloor\sigma_c^{-1},
\quad a>0,\quad p\nmid a.
\]

In the direct basis, the index of the displayed coefficient is c^-1; its inverse is c. Accordingly M_-(Θ_a)=Σ c floor(ac/p), while the source's action-on-ζ functional is Σ c^-1 floor(ac/p). These are different functionals, and Fermat-module membership constrains the latter. The calculation in the candidate uses the former consistently.

Let k_c=floor(ac/p), r_c=ac−pk_c. For every positive a prime to p, including a≥p, r_c is the least positive residue of ac, so the r_c permute 1,...,p−1. Set S=Σ c², K_0=Σ c k_c, L_0=Σ k_c². The exact integer equality is

\[
S=a^2S-2apK_0+p^2L_0,\quad
2aK_0=(a^2-1)(S/p)+pL_0.
\]

For p≥5, S=p(p−1)(2p−1)/6 is divisible by p and S/p≡1/6 mod p. Thus division by p above is integer arithmetic before reduction. The elements 2,3,a are invertible in F_p, so

\[
M_-(\Theta_a)=K_0\equiv\frac{a-a^{-1}}{12}\pmod p.
\]

There is no division by a residue zero and no hidden bound a<p. For a=1 both sides vanish, as required. The p=3 exclusion is substantive for this general proof: Σ_(c=1)^2 c²=5 is not divisible by three. MS1–MS3 do not use this square-sum division and remain valid at p=3 under their written assumptions.

## MS5 and the remaining selection limits

At a=2, (2−1/2)/12=1/8. For ψ_2=Θ_3−Θ_2, subtracting the two formulas gives

\[
M_-(\psi_2)=\frac{3-1/3-2+1/2}{12}=\frac7{72}.
\]

For primes p>7, 8 and 72 are invertible and the two values are nonzero. Applying MS1 and MS3 to each concrete element proves all the asserted reciprocal-array and Fourier-orbit separations. This algebra does not require that a Nagell–Ljunggren solution exists or that the elements lie in a Fermat module. Such membership remains an additional application hypothesis when the elements are selected in the source argument.

At p=7 the ψ_2 moment vanishes. There is even an exact failure of Fourier freeness if one tried to extend MS5 there: the inverse-index floor differences are supported at c=3,5,6, so in direct indices ψ_2=σ_3+σ_5+σ_6. Multiplication by σ_2 cycles those indices and fixes ψ_2 nontrivially. This is a hand boundary counterexample, not a scan, and agrees with the candidate's p>7 restriction.

For the positive indices n for which Θ_n,Θ_(n+1) are defined and p∤n(n+1), subtraction yields

\[
M_-(\Theta_{n+1}-\Theta_n)
=\frac{n^2+n+1}{12n(n+1)}.
\]

The same floor definition and integer identity would extend this equality to negative integer indices if desired; no such extension is needed for the stated source elements. The numerator can vanish. For instance n=3,p=13 gives zero with nonzero denominator. Thus this formula cannot confer nonzero inverse moments on arbitrary Fueter elements or on an unspecified pair selected in another theorem.

## Primary-source match and historical notes

The [original author-uploaded diagonal chapter](https://www.researchgate.net/publication/226863681_Class_Number_Conditions_for_the_Diagonal_Case_of_the_Equation_of_Nagell_and_Ljunggren) uses inverse-index floor coefficients and Fourier evaluation after reindexing. Its first-case choices are the concrete Θ_2,ψ_2, with additional module hypotheses. The source also has a second-case nonconjugacy conclusion; MS2 is conditional on actual elements satisfying it and does not reprove that conclusion. Within-list freeness remains a separate condition.

The [later binary-Thue source](https://arxiv.org/pdf/1412.5798v2) uses a different coefficient normalization. Differentiating its displayed formal product at D=0 gives first coefficient (1/p)Σ n_a/(1−ζ^a). With its b_1/(pλ) convention, b_1[σ_c θ]=R_c(θ). This is the exact common-λ array checked in MS1. It does not identify this map with E, make it G-equivariant, or transfer the Fourier injection. The appendix footnote describes a corresponding role. The complete applicable source passages and their reading limits are recorded separately, without importing any stronger source theorem.

The four preserved notes progress from a conditional reciprocal argument to separating the Fourier normalization, then calculating the two first-case moments, then proving Fourier faithfulness. The consolidated v2 explicitly retains their limits. The old v1's tentative source application is not treated as a theorem that the two formulas are equal.

The appendix inspection's elementary bouquet observation can be independently reconstructed: if a proper subspace containing a vector w with all coordinates nonzero were invariant under diagonal multiplication by a distinct-coordinate vector v, it would contain w,vw,...,v^(m−1)w. The corresponding Vandermonde matrix times diag(w) is invertible, a contradiction. No asserted bound on the first escaping power is needed. The literal matrix-label observation is also linear algebra: annihilating a basis of the row space of a rank-r matrix annihilates every original row, so cannot yield e_(r+1) for that same original matrix. An augmented independent row can supply that inhomogeneous coordinate instead. Replacing a column by that last basis vector removes the appended row from the surviving cofactor, so the preserved discarded cofactor objection is indeed not a defect.

These observations are research interfaces only. They do not reconstruct application-specific selection, singular-system compatibility, cancellation at every conjugate, a nonzero δ step, a norm estimate or a stronger Diophantine theorem. Neither the candidate nor this review refutes a published theorem. All fourteen obligations are covered by 39 separate checks in the ledger. No mathematical code, CAS, enumeration or author rerun was used. No repair is requested for MS1–MS5; root alone may promote after both independent whole audits.
