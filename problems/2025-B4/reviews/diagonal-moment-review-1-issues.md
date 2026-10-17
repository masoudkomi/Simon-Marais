# MS R1: full per-inference issue ledger

2026-10-17 UTC. Reviewer `review_2022_complexity_r2`, nonconstructor. Frozen before new peer MS findings. **Unresolved substantive issues: 0. Author repairs requested: 0.** Scope is the five exact algebraic lemmas, not an enlarged Diophantine result.

| ID | Challenged inference | Reconstruction / adversarial check | Result | Obligation |
| --- | --- | --- | --- | --- |
| MS-R1-01 | Official scope | Part (b) degree n means n+1 terms, full signed integer domain. Supporting lemmas make no new exclusion and do not solve part (a). | Pass | O14 |
| MS-R1-02 | Direct action | σ_a sends ζ to ζ^a; left multiplication shifts a to ha. Group-ring “conjugacy” uses that action, not internal conjugation in an abelian group. | Pass | O01/O05 |
| MS-R1-03 | Integer coefficients versus modular moment | E and R use actual integer coefficients; M reduces modulo p. Negative coefficients cause no local-residue problem; no lift change is made in an exact K identity. | Pass | O01/O02 |
| MS-R1-04 | Residue field | Quotient Z[Z]/(Φ_p,1−Z)=Z/(p); (λ) maximal. | Pass | O02 |
| MS-R1-05 | Geometric-sum unit | S_t reduces to nonzero t for 1≤t<p, so its inverse lies in the localization and has residue t^-1. | Pass | O02 |
| MS-R1-06 | Representative ac | ac is nonzero mod p; ζ^(ac) equals ζ^t for its nonzero representative. All denominators are nonzero. | Pass | O02 |
| MS-R1-07 | Reciprocal residue | Sum n_a/(ac) equals c^-1 M_-, including negative n_a. | Pass | O03 |
| MS-R1-08 | Distinct R_c values | Multiplication by nonzero M_- and inversion are injective in F_p; different residues imply different field elements. | Pass | O03 |
| MS-R1-09 | Common scalar | A single nonzero field multiplier preserves distinctions by cancellation even if not a local unit; no per-coordinate scaling permitted. | Pass | O03/O12 |
| MS-R1-10 | R-array versus true orbit | σ_cR_1=((1−ζ^c)/λ)R_c. At θ=σ_1, R_1=1 has repeated actual conjugates although R_c are distinct. Candidate only asserts distinctness of its normalized array. | Pass; extension would fail | O03/O12 |
| MS-R1-11 | Fourier kernel | P has degree≤p−1 and constant zero; its minimal-polynomial multiple must be a rational scalar times Φ_p, killed by constant comparison. Handles zero P. | Pass | O04 |
| MS-R1-12 | Prime hypothesis | Φ_p is the minimal polynomial; shift-Eisenstein verifies irreducibility. No unjustified analogous statement for composite conductors. | Pass | O04 |
| MS-R1-13 | Fourier assumptions | Injection needs no weight, positivity, module membership or moment. E is linear, not asserted multiplicative. | Pass | O04 |
| MS-R1-14 | Equivariance | Direct-index multiplication gives E(σ_cθ)=σ_cE(θ) exactly. | Pass | O05 |
| MS-R1-15 | Stabilizer equality | Injection converts equality of Fourier values back to equality of integer group-ring elements. Both directions hold. | Pass | O05 |
| MS-R1-16 | Cross-list disjointness | One cross-list equality would give σ_cθ_1=σ_dθ_2. Nonconjugacy excludes it, regardless of repetition within lists. | Pass | O05 |
| MS-R1-17 | Moment transformation | M_-(σ_hθ)=h^-1M_-(θ). Inverse, not direct factor, is required here. | Pass | O06 |
| MS-R1-18 | Freeness from nonzero moment | If h fixes θ, nonzero M_- forces h=1. MS2 then gives p−1 distinct Fourier conjugates. | Pass | O06 |
| MS-R1-19 | Sufficiency only | pσ_1 has M_-=0 and trivial stabilizer, so the inverse moment is not necessary. Candidate says only sufficient. | Pass | O06 |
| MS-R1-20 | Norm counterexample including ideal membership | N=(1+j)Θ_2 lies in the Stickelberger ideal, has positive coefficients/weight p−1, acts trivially on ζ, and has E(N)=−1 with full stabilizer. | Pass | O07 |
| MS-R1-21 | Reciprocal injection temptation | σ_1+σ_-1−σ_b−σ_-b is a nonzero R-kernel vector for b≠±1, p≥5, by opposite-denominator identity. Its M_-=0. Candidate never transfers Fourier injection. | Pass; extension would fail | O12 |
| MS-R1-22 | Exact source reindexing | Coefficient at σ_c^-1 has direct index c^-1; its inverse-moment weight is c. The action-on-ζ weight is c^-1 instead. | Pass | O01/O09 |
| MS-R1-23 | Positive a without bound | r_c=ac−p floor(ac/p) is the least positive residue for every a>0 prime to p, including a≥p. It permutes 1,...,p−1. | Pass | O08 |
| MS-R1-24 | Integer square identity | Sum r_c²=sum c² gives 2apK_0=(a²−1)S+p²L_0 with correct sign. | Pass | O08 |
| MS-R1-25 | Divide p before reducing | p divides S for p≥5. Divide the integer equality by p, then reduce; S/p≡1/6. p=3 would not allow this step. | Pass | O08/O10 |
| MS-R1-26 | Exact moment formula | Invert 2a and 6 to obtain (a−a^-1)/12. No p|a allowed; a=1 gives zero correctly. | Pass | O08/O09/O10 |
| MS-R1-27 | Θ_2 constant | Substitute a=2: 1/8, nonzero for all p≥5. | Pass | O10 |
| MS-R1-28 | ψ_2 constant | Subtract a=2 from a=3: 7/72. Defined for p>3; vanishes at seven. | Pass | O10 |
| MS-R1-29 | p>7 restriction | Both moments nonzero there. At p=7, ψ_2=σ_3+σ_5+σ_6 is fixed by σ_2, showing an actual failure of Fourier freeness if extended. Hand calculation only. | Pass; restriction meaningful | O10 |
| MS-R1-30 | p=3 scope | MS4/MS5 excluded; MS1–MS3 retain their hypotheses and proofs at p=3. No denominator-12 formula asserted there. | Pass | O10 |
| MS-R1-31 | General Fueter subtraction | For defined positive indices and p∤n(n+1), difference is (n²+n+1)/(12n(n+1)); the floor identity would also extend to integer negative indices. | Pass | O11 |
| MS-R1-32 | Vanishing Fueter moment | n=3,p=13 has zero numerator and nonzero denominator. No arbitrary Fueter or unspecified second-case pair is granted a nonzero moment. | Pass | O11/O13 |
| MS-R1-33 | First-case application boundary | Concrete Θ_2,ψ_2 algebra is unconditional. Their actual module selection in a source argument still retains that source's hypotheses. No new Wieferich proof. | Pass | O13 |
| MS-R1-34 | Second-case application boundary | MS2 only says what follows IF chosen elements satisfy the source nonconjugacy conclusion. It neither proves that source conclusion nor within-list freeness for arbitrary choices. | Pass | O05/O06/O13 |
| MS-R1-35 | Exact two primary maps | Original η is E after direct reindexing. Later normalized b_1 on σ_cθ is R_c by the formal derivative. Their analogous role does not make their formulas equal. | Pass | O12 |
| MS-R1-36 | Preserved research-note chronology | Four notes and appendix read fully; tentative old application is superseded by explicit normalization/separation limits in consolidated v2. No old bytes edited. | Pass | O12/O14 |
| MS-R1-37 | Bouquet dimension observation | If a proper subspace were invariant under a distinct-coordinate diagonal map, w,vw,...,v^(m−1)w would give a full Vandermonde basis inside it. No escape-index bound used. | Pass as scoped observation | O14 |
| MS-R1-38 | Matrix label and cofactor observations | Annihilating row-space basis annihilates original A; augmented row can instead prescribe one. The last-basis-vector column replacement removes the appended row from surviving cofactors, so size objection was correctly discarded. | Pass as scoped observations | O14 |
| MS-R1-39 | Final claim ceiling | No proof of full source Lemma3/Wieferich theorem, singular inhomogeneous solvability, all-conjugate cancellation, δ≠0, norm bound, stronger range exclusion, annual answer or novelty. No CAS/scan/rerun. | Pass | O13/O14 |

All fourteen constructor obligations are covered. The exact excluded-domain examples and tempting-map counterexamples strengthen the need for the written hypotheses; none contradicts MS1–MS5. The whole report contains the derivations. No substantive issue requires author repair, and no new peer MS report/findings were read before this freeze.
