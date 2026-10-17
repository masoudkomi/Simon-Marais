# Fourier faithfulness and disjoint coefficient lists

2026-10-17 UTC. **Candidate proof — unverified; research continuation.** Root constructor. This supplies one further elementary statement about the ORIGINAL Fourier map, supplementing the preserved v1.1–v1.2 notes. It is not a proof of the Diophantine theorem or the later reciprocal-map application.

Let p be prime, ζ a primitive p-th root of unity, and write the integral group ring in DIRECT indices as Z[G]=sum_(a=1)^(p−1) Z σ_a, with σ_a(ζ)=ζ^a. The Z-linear evaluation map

    E: Z[G] -> Z[ζ],   sum n_a σ_a -> sum n_a ζ^a

is injective. Indeed, an element in its kernel gives P(Z)=sum_(a=1)^(p−1)n_a Z^a with P(ζ)=0. Its degree is at most p−1 and its constant coefficient is0. The minimal polynomial Φ_p(Z)=1+Z+...+Z^(p−1) has degree p−1 and constant1. Hence P is a rational constant multiple of Φ_p, and that multiple is0. All n_a vanish. This also handles the zero polynomial and unequal group-ring weights. Equivalently, ζ,...,ζ^(p−1) are an integral basis: the missing constant1 equals minus their sum.

The map is G-equivariant: E(σ_c θ)=σ_c E(θ), by multiplying the direct indices modulo p. Two consequences are exact:

1. The stabilizer of E(θ) under G is exactly the stabilizer of θ. Its conjugate values are pairwise distinct if and only if θ has trivial stabilizer. The nonzero inverse-moment test from v1.1 is a sufficient way to prove this freeness, and is not a necessary condition.
2. If θ1 and θ2 are NOT Galois conjugate in Z[G], the sets {E(σ_c θ1)} and {E(σ_d θ2)} are disjoint. Equality of one pair would imply σ_c θ1=σ_d θ2 by injectivity, contradicting nonconjugacy.

For the original chapter's Fourier definition η[θ]=E(θ), with inverse indices reindexed when needed, the nonconjugacy conclusion of its Lemma3 therefore SUFFICES to separate the TWO coefficient-value sets from each other. No additional moment condition is needed for that cross-list statement. This fills that particular additional argument left open in the preceding v1.2 note, conditional only on using exact group-ring elements satisfying the source's nonconjugacy conclusion.

It does not imply that every element in each separate list is distinct. That still requires trivial stabilizer for EACH chosen θ. Positivity, weight p−1 and Fermat-module membership alone do not prove this: the norm element N=sum σ_a has all three properties and E(N)=−1 is fixed by every automorphism. The first-case elements treated in v1.2 have nonzero inverse moments at the stated primes, so that separate check is available for them. It is not granted for an arbitrary pair from Lemma3.

No analogous injectivity of the later scaled RECIPROCAL coefficient map is asserted. Its opposite-index terms satisfy additional identities, so transferring the Fourier conclusion merely because the maps play similar roles would be invalid. The original and later normalizations remain separate. No singular-system solution, all-conjugate cancellation, nonzero δ, second-case theorem, new Diophantine exclusion, computation, or novelty is established. Two independent whole audits are required before promoting these algebraic lemmas.
