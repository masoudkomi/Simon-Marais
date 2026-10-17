# Accepted diagonal-moment: coordinator status and scope

2026-10-17 UTC. **Proved, independently reviewed scoped partial result.**

MS1–MS5 are accepted as the exact elementary cyclotomic algebraic lemmas in the consolidated submission. They distinguish direct automorphism indices, inverse source indices, multiplicative action on zeta, Fourier evaluation E and fixed-normalization reciprocal arrays R_c. A nonzero inverse moment separates R_c residues at1−zeta and forces a trivial Fourier stabilizer. E is a faithful Z-linear equivariant map, so nonconjugate group-ring elements have disjoint Fourier value SETS; this does not grant freeness within either set. The exact square-sum calculation gives the inverse moment of Theta_a for p>=5 and arbitrary positive a prime to p, and the two concrete first-case moments are nonzero for p>7.

Both fresh initially blind nonconstructor WHOLE audits reconstructed every one of the14 obligations, with39 separate checks in R1 and a complete14-row R2 ledger. Root read the full consolidated candidate, four preserved research notes, appendix inspection, all source records and BOTH entire reports, inference ledgers and source checks before reconciliation. No substantive issue or required repair remains. Root is the constructor and is NOT an independent auditor; reviewer roles in earlier PG/CF1 work are disclosed and those results are not premises here.

The exact primary source definitions and relevant proof/application passages were checked. The original Fourier coefficient map is not the later reciprocal map. In particular R_c is a shifted array with a COMMON normalization; it is not in general the actual Galois conjugate list of R_1. The norm element shows that positive weight and Fermat-module membership alone do not imply freeness. Opposite-index pairs give a nonzero reciprocal kernel, preventing transfer of Fourier injectivity. The p7 Fueter endpoint can actually have a nontrivial stabilizer; arbitrary Fueter moments can vanish. These are hand-derived boundary checks, not scans.

The concrete algebraic moments are unconditional. Applying those elements to a solution-specific first-case source argument still retains its additional membership/Wieferich hypotheses. Applying cross-list disjointness to a second-case pair remains conditional on actual nonconjugacy; this packet supplies neither that source's pair-existence theorem nor within-list freeness for unspecified choices. It does not settle the singular inhomogeneous equations, cancellation through EVERY conjugate, a nonzero delta branch, a stronger class-number theorem or any new Diophantine exclusion. No full external proof is accepted or refuted, no full annual solution is claimed, and novelty remains unestablished. No mathematical program, CAS, scan, certificate replay or author rerun supplies the proofs.

The complete frozen submission follows as a byte-identical suffix. Its historical unverified labels and conditional statuses record the submission date; this header and the acceptance record state the current scope.

---

# Coefficient separation for the diagonal literature: exact algebraic lemmas

2026-10-17 UTC. **Candidate proof — unverified.** Root constructor. Two fresh independent nonconstructor WHOLE audits are required. This consolidates the four preserved moment research notes into a single auditable set of algebraic claims. It supplies no new Nagell–Ljunggren exclusion or complete repair of an external proof.

## Definitions and proposed claims

Let p be an odd prime, ζ a primitive p-th root, K=Q(ζ), O=Z[ζ], λ=1−ζ and G=Gal(K/Q). All group-ring indices in the statements below are DIRECT: σ_a(ζ)=ζ^a for a in F_p^*. For θ=sum n_a σ_a in Z[G], put

    M_minus(θ)=sum n_a a^(-1) in F_p,
    E(θ)=sum n_a ζ^a in O,
    R_c(θ)=sum n_a (1−ζ)/(1−ζ^(ac)) in K.

MS1. If M_minus(θ)!=0, the p−1 numbers R_c(θ), c in F_p^*, are pairwise distinct.

MS2. E is an injective Z-linear G-equivariant map. In particular the stabilizers of θ and E(θ) coincide, and nonconjugate group-ring elements have DISJOINT sets of Fourier conjugate values.

MS3. If M_minus(θ)!=0, θ has trivial G-stabilizer, and all p−1 Fourier values E(σ_c θ) are pairwise distinct. The hypothesis is sufficient, not necessary.

MS4. If p>=5 and a is a positive integer not divisible by p, define the Fuchsian coefficient element in INVERSE source indices by

    Θ_a=sum_(c=1)^(p−1) floor(ac/p) σ_c^(-1).

Then, reindexed into the direct basis,

    M_minus(Θ_a)=(a−a^(-1))/12 mod p.

MS5. For prime p>7, Θ2 and ψ2=Θ3−Θ2 have nonzero inverse moments1/8 and7/72 respectively. Each therefore satisfies both MS1 and MS3. This statement about the concrete elements is unconditional; application to a particular Fermat-module selection has to retain that source's additional hypotheses.

## 1. Residues prove MS1

For the representative1<=t<p,

    (1−ζ^t)/(1−ζ)=1+ζ+...+ζ^(t−1)

reduces to t modulo λ. The standard residue field O/(λ)=F_p follows by setting ζ=1 in Φ_p(ζ)=0: Φ_p(1)=p, and the quotient is Z/(p). Thus this geometric sum is a unit in the localization O_(λ). Its reciprocal lies there and reduces to t^(-1). Since ac is nonzero modulo p, this applies to every summand of R_c, including negative integer coefficients. Hence

    R_c(θ) = c^(-1)M_minus(θ) mod λ.

Distinct c,d give different residues when the moment is nonzero, and consequently different elements of K. Multiplication of ALL coordinates by one common nonzero field element also preserves distinctness. Nothing about a real ordering, complex size bound, or positivity is needed.

## 2. Faithfulness proves MS2

If E(θ)=0, P(Z)=sum_(a=1)^(p−1)n_a Z^a vanishes at ζ, has degree at most p−1 and has constant coefficient0. Its minimal polynomial Φ_p(Z)=1+Z+...+Z^(p−1) has degree p−1 and constant1. Divisibility in Q[Z] forces P to be a rational constant multiple of Φ_p. Comparing constant coefficients makes that multiple0, so every n_a=0. This proves injectivity for arbitrary integer coefficient vectors, without imposing their weight.

Equivariance follows from multiplication of indices modulo p:

    E(σ_c θ)=σ_c E(θ).

Thus E(σ_c θ)=E(θ) if and only if σ_c θ=θ. More generally E(σ_c θ1)=E(σ_d θ2) implies σ_c θ1=σ_d θ2. Nonconjugacy of θ1,θ2 therefore prevents every cross-list equality. This conclusion does NOT require that entries within either list be distinct.

## 3. The inverse moment proves MS3

Multiplication by σ_h sends the coefficient at direct index a to index ha and therefore

    M_minus(σ_h θ)=h^(-1) M_minus(θ).

If σ_h θ=θ and M_minus(θ)!=0, then h^(-1)=1 in F_p, hence h=1. The stabilizer is trivial; MS2 yields pairwise distinct Fourier conjugates. This proof does not identify the Fourier map with the reciprocal map in MS1.

The moment condition is not necessary for freeness, and is not automatic for positive Fermat-module elements. For example N=sum σ_a has positive weight p−1, acts trivially on ζ because sum a=0 modulo p, and has E(N)=−1 fixed by every automorphism. Thus those three properties alone cannot replace an actual stabilizer/moment check.

## 4. A square-sum identity proves MS4 and MS5

Write k_c=floor(ac/p), r_c=ac−pk_c. The r_c permute1,...,p−1 because p does not divide a. The exact integer identity

    sum c² = sum r_c²
            =a² sum c²−2ap sum c k_c+p² sum k_c²

may be divided by p: sum c²=p(p−1)(2p−1)/6, an integer multiple of p for p>=5. Reduction modulo p gives

    2a sum c k_c=(a²−1)/6,
    sum c k_c=(a−a^(-1))/12.

In the DIRECT group-ring basis the source term σ_c^(-1) has index c^(-1), whose inverse is c. Thus this sum is precisely M_minus(Θ_a), proving MS4. It is not the source's action-on-ζ moment sum k_c c^(-1).

Substituting a=2 gives1/8. Subtracting a=2 from a=3 gives

    (3−1/3−2+1/2)/12=7/72.

For primes p>7 the denominators are invertible and both values are nonzero. MS1/MS3 give MS5. At p=7 the second value is0, so this note supplies no separation for ψ2 there. The p=3 case of MS4/MS5 is excluded. MS1–MS3 themselves remain valid at p=3 under their written hypothesis.

For any n with p not dividing n(n+1), the same calculation gives

    M_minus(Θ_(n+1)−Θ_n)=(n²+n+1)/(12n(n+1)),

when p>=5. This may vanish and is not used to grant freeness to arbitrary Fueter elements.

## 5. Exact source role and unresolved applications

The [original author-uploaded diagonal chapter](https://www.researchgate.net/publication/226863681_Class_Number_Conditions_for_the_Diagonal_Case_of_the_Equation_of_Nagell_and_Ljunggren), internal version2.0,2007-09-17, uses a Fourier map η[θ]=E(θ). Its inverse-index Fuchsian formula and the selected first-case Θ2,ψ2 have been checked in the actual source passages. MS5 discharges a distinctness test for those particular elements. For a second-case pair satisfying the source's NONCONJUGACY conclusion, MS2 also separates their TWO Fourier value sets from one another. It leaves the stabilizer of each separate element to be checked. This note does not newly prove the source's existence/nonconjugacy theorem or its Wieferich conditions.

The later [Bartolome–Mihailescu1412.5798v2](https://arxiv.org/pdf/1412.5798v2), internal version1.13,2021-11-02, has a scaled reciprocal b1 coefficient map. MS1 is a direct residue lemma of the corresponding form, conditional on the moment and the exact normalization. A correspondence of roles in an appendix footnote is not a literal equality with the original Fourier map. In particular MS2's injectivity is NOT transferred to that reciprocal map.

No application-specific second-case moment choice, singular inhomogeneous system, propagation of cancellation through every conjugate, nonzero δ argument, stronger class-number theorem or enlarged Diophantine range is proved here. The earlier CF1 and PG acceptances retain their independent scopes. All elementary proofs above are mathematical arguments, with no code, CAS, finite scan or numerical evidence. Source hashes/reading limits are recorded separately. Novelty is unestablished.
