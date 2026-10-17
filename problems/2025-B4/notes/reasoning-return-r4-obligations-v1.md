# R4 complete proof obligations and constructor dispositions

2026-10-17 UTC. **Candidate proof - unverified.** These are constructor
checks and reviewer targets, not independent reviews. Every FS claim and
its source boundary is included. No open obligation below is silently
assumed to establish a Diophantine result.

| ID | Whole-audit obligation | Constructor disposition / exact location |
|---|---|---|
| FS01 | Match official integer domain, degree versus term count and part(b) only. | Main introduction: m=n_off+1; algebraic statements do not classify x,y. |
| FS02 | Separate prime p, Fueter t, weight k and official exponent q. | Definitions, t=1,...,p-2; FS2 p>7, FS3 k>=2. |
| FS03 | Direct indices for F and M_r versus inverse indices in Theta and psi. | Main definitions and coefficient calculation(4). |
| FS04 | Prove both transformation rules under sigma_h, including inverse exponent. | Equation(1), multiplying direct indices. |
| FS05 | Prove Theta_a and psi_t belong to the explicitly defined I; no annihilator import. | Equation(4), residue coefficient r_a(c)/p. |
| FS06 | Show integer coefficients nu are0 or1 and complementary under c to p-c. | Section1, equation(5). |
| FS07 | Establish N membership, Fueter weight and positive G-translate closure. | Equation(5); no linear independence or basis theorem used. |
| FS08 | Establish F(N)=M_1(N)=0 and the nonzero M_1 freeness criterion. | Section1 and(1), p odd. |
| FS09 | Reconstruct S_2 expansion modulo p^2 and valid division by p. | Section2, p>=5; denominator6 and a are units. |
| FS10 | Identify the resulting sum as M_1 rather than action functional F. | Equation(6), inverse-index coefficient c. |
| FS11 | Check exact fourth-power sum and S_4/p=-1/30. | Section2, p>=7; no p=5 use. |
| FS12 | Expand fourth powers, eliminate p^2 terms and derive M_3. | Equation(7), denominator120 a^3 invertible. |
| FS13 | Derive both Fueter moments by subtracting a=t+1 and a=t. | Equations(8),(9), exact distinct prime thresholds. |
| FS14 | Prove nonexceptional exact stabilizer, not only Fourier distinctness. | Section3, M_1 nonzero and(1). |
| FS15 | Handle Q(t)=0: t has actual order3, and p>=7. | Section3; p>=5 excludes t=1. |
| FS16 | Prove literal integer coefficient invariance under t using residues. | Equation(10); cyclic permutation of three canonical residues. |
| FS17 | Use M_3=-1/40 to exclude every larger stabilizer. | Section3; root count for h^3=1. |
| FS18 | Establish F(psi_t)=0 in the exceptional case without confusing moments. | Invariance and F(sigma_t psi)=t F(psi). |
| FS19 | Audit p=3 and p=5 endpoints. | Explicit p3 psi_1=sigma_2 exception to attempted extension; no cubic-root case at p5. |
| FS20 | Derive Fermat action functional from product of canonical residues. | Section4, units in Z_(p), cancellation of factorial. |
| FS21 | Verify f(t), its polynomial integrality, zeros at0,-1 and highest five coefficients. | Equations(12),(13), binomial formula. |
| FS22 | State nonconstancy on nonexceptional indices, excluding simultaneous zero moments. | Section5, domain Q(t)!=0 and t!=0,-1. |
| FS23 | Explain every zero of P in F_p, including deleted domain points. | Equation(14), separate cases Q=0 and0,-1. |
| FS24 | Distinguish polynomial divisibility by X^p-X from polynomial/function confusion. | P vanishes on all p distinct field elements; degree p+3 and quotient degree3. |
| FS25 | Reconstruct the exact X^(p-1) coefficient 7/10 and rule out low/high overlap. | Equation(15), p>7; C-term degree4. |
| FS26 | Treat f(s)=0 or f(t)=0 explicitly; no division by them. | Twice the corresponding Fueter element; other zero cannot also occur. |
| FS27 | Treat both f values nonzero with positive translates rather than signed subtraction. | a=f(t), b=-f(s), equation(16); sigma_b permutes coefficients. |
| FS28 | Recheck I_f membership, weight p-1, relative identity and nonzero moment of theta. | Section5, equations(3),(16). |
| FS29 | Attribute the already-stated one-element selection conclusion to source Lemma2.7. | FS2 statement and Section5 ending; no novelty/new method claim. |
| FS30 | Prove theta coefficients are0,1,2 and have at least two actual zeros. | Equation(17), singleton-zero F=-2v contradiction. |
| FS31 | Obtain h!=1,-1 with an actual common zero for theta and sigma_h theta. | h=v/w, DIRECT coefficient at v; opposite zeros impossible. |
| FS32 | Establish gamma minimum0 maximum4, kernel membership and nonzero inverse moment. | Equation(18) and gamma+j gamma=4N. |
| FS33 | Prove all A_l and B positive with identical weight k(p-1). | Equation(19), k>=2; all coefficients nonnegative. |
| FS34 | Prove freeness of A_l for arbitrary k, including k or k-l divisible by p. | Integer torsion-free argument, not reduced moment assertion. |
| FS35 | Prove B free after invariant norm addition. | Same stabilizer as gamma. |
| FS36 | Prove every A_l pair nonconjugate and separate B except one candidate by minima. | Minimum coefficients l versus k-2. |
| FS37 | Separate B from A_(k-2) by strict integer squared norm after equal norm addition. | Equation(20), theta free, h!=1 and equal augmentations. |
| FS38 | Reconstruct Fourier injectivity/equivariance and both within-list and cross-list conclusions. | Section6 ending, accepted MS2 reconstructed; reciprocal injectivity not inferred. |
| FS39 | Keep source weights, higher coefficients, all-conjugate cancellation and source hypotheses distinct. | Section7; no external Diophantine proof imported. |
| FS40 | Preserve exact failed endpoints and remaining task; no k1 or p7 extrapolation. | Section7 gamma-N has coefficient-1; 7/10 vanishes at p7; no new local exclusion. |

The mathematical gaps in Section7 are deliberately outside FS1–FS3:
two nonconjugate free positive elements at the original weight, or a
complete higher-weight Diophantine interpolation/size argument. Their
unresolved status does not depend on any program or a finite sample.
