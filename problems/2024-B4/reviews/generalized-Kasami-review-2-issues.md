# GK1–GK3 R2: complete inference ledger and issue log

2026-10-17 UTC. Initially blind whole nonconstructor audit. This ledger and the full initial report are frozen before any GK peer findings or coordinator reconciliation. Status `pass` means no objection found in the stated scope; it does not promote the candidate. No substantive or editorial repair is requested. Open issues: **none**.

| Check | Author obligation | Inference and adversarial reconstruction | Result |
|---|---|---|---|
| GKR2-01 | GK-O1 | Official B4(b) was reopened directly. Positive odd integers, coefficientwise congruence and actual integer lifts of F2 factors are the exact domain. Finite polynomial functions and extension-only factorizations would be insufficient. | pass |
| GKR2-02 | GK-O1 | n=1 gives zero and cannot be a product R*g*h with both reduced factors nonconstant/nonzero in a domain. n=3 is a unit quotient. Neither is claimed to qualify. No preliminary-part proof is supplied. | pass |
| GKR2-03 | GK-O2 | Alternating integer division gives L_r=(q^(2r+1)+1)/(q+1), positive and odd for all r>=0,q=2^k,k>=1. L_0=1,L_1=d. No q=1 or negative-index claim is present. | pass |
| GKR2-04 | GK-O2 | L_r increases strictly with r. m=r−1 changes exponent 2r+1 to 2m+3; r>=2 is exactly m>=1. CP1 is invoked only for r>=1. | pass |
| GKR2-05 | GK-O3 | In an algebraic closure of F2(a), the two (q+1)-st roots exist; a,a+1 are nonzero functions. No finite-field root or fixed-field restriction has been imposed. | pass |
| GKR2-06 | GK-O3 | (q+1)L_r=q^(2r+1)+1 proves D_r=a^L_r+(a+1)^L_r. Root-choice independence applies to D_r, without requiring it for the vector v. | pass |
| GKR2-07 | GK-O4 | The four pairing orders are 0+1,2+1,0+3,2+3. The second is the q-power of the original identity; the fourth is its q²-power. Ordinary bilinearity, not a Hermitian or periodic-Frobenius theorem, suffices. | pass |
| GKR2-08 | GK-O5 | c=g_d(a²+a) has positive polynomial degree d−1 in a, including q=2,d=3. Thus c+1 is nonzero in K. Treating this as nonvanishing at every finite point would be false, but is not done. | pass |
| GKR2-09 | GK-O5 | Pairing matrix [[1,1],[1,c]] has determinant c+1. Dependence of either the ordered vectors or the functionals would force matrix rank<=1, so both pairs are independent. Isotropic-vector concerns do not defeat the explicit determinant. | pass |
| GKR2-10 | GK-O6 | The column vectors form a basis of K², giving existence and uniqueness of the FULL relation v^[4]=alpha v^[2]+beta v. This is established before solving scalar equations. | pass |
| GKR2-11 | GK-O6 | Pairings of v^[4] with v^[1],v^[3] are c^q and 1 respectively, giving alpha+beta=c^q and alpha+c*beta=1 with the coefficients in the correct positions. | pass |
| GKR2-12 | GK-O6 | Addition gives (c+1)beta=(c+1)^q. Generic division yields beta=(c+1)^(q−1), alpha=c^q+(c+1)^(q−1). Both are polynomials with F2 coefficients. No denominator remains. | pass |
| GKR2-13 | GK-O6 | Independence of the two functionals proves the equations determine the full vector. A scalar-only reconstruction would leave a gap, but here the existing basis relation and invertible matrix close it. | pass |
| GKR2-14 | GK-O7 | Raising the vector relation to q^(2r+1) produces indices 2r+5,2r+3,2r+1, with both coefficients raised too. Frobenius composition adds the bracket indices. Valid for every r>=0. | pass |
| GKR2-15 | GK-O7 | The subsequent dot product uses the ORIGINAL v. The three scalar products are D_(r+2),D_(r+1),D_r. Raising this first factor as well would be wrong; the candidate does not. | pass |
| GKR2-16 | GK-O8 | D_0=1,D_1=c agree with P_0(c),P_1(c). The proved recurrence gives D_r=P_r(c) by ordinary induction with no finite-index extrapolation. | pass |
| GKR2-17 | GK-O8 | Both sides after substitution belong to F2[a]; equality in K descends to that subring. U->a²+a is injective by degree 2e, so the final identity is in F2[U]. | pass |
| GKR2-18 | GK-O9 | The c=1 finite locus can make the auxiliary basis degenerate, but the final polynomial identity has no denominator and specializes everywhere. Analytically A_q(1)=1,B_q(1)=0 gives P_r(1)=1, so a=0,1 yield no contradiction. No generic division is repeated at those points. | pass |
| GKR2-19 | GK-O10 | A_q is monic degree q; B_q is monic degree q−1, also at q=2. The two summands defining A_q have distinct degrees. | pass |
| GKR2-20 | GK-O10 | Recurrence first-term degree is q^(2r+2)+E_(r+1)=E_(r+2). Second is (q−1)q^(2r+1)+E_r. Their exact gap q^(2r)(q+1)>0 prevents cancellation for all r, including r=0. | pass |
| GKR2-21 | GK-O10 | P_0=1,P_1=T supply monic induction. E_0=0 is consistent with the constant 1. The independent composition degree ratio (L_r−1)/(d−1)=E_r agrees. | pass |
| GKR2-22 | GK-O11 | Expanding only the r=0 recurrence gives P_2=T^(q²+1)+(T+1)^(q²−q+1). CP2 is the stated comparison and was not used to infer the all-index vector recurrence. | pass |
| GKR2-23 | GK-O12 | Exact accepted CP1 has all odd d,n>=3 and whole divisibility over F2. Its degree result applies to d=q²−q+1. No nontrivial-factor, prime-d, squarefree-d, or extension-field hypothesis is hidden. | pass |
| GKR2-24 | GK-O12 | Reconstructed invariant ring, exact full-degree dehomogenization, rank-four free-cover descent and h-adic composition criterion. Whole quotient descent preserves multiplicities and repeated diagonals; cancellation uses the same U+V and requires no coprimality. | pass |
| GKR2-25 | GK-O12 | For r>=1 the input n=L_r satisfies CP1. P_r lies in F2[T], not only K[T]. Therefore actual whole homogeneous phi_d divides phi_(L_r) over F2. | pass |
| GKR2-26 | GK-O13 | q>=4 gives divisor degree q²−q−2>0. r>=2 gives L_r>d, hence positive cofactor degree L_r−d. Both are nonzero because the accepted phi polynomials are nonzero. | pass |
| GKR2-27 | GK-O13 | In a graded domain a quotient of two nonzero homogeneous polynomials, when polynomial, is homogeneous of the degree difference. Nonhomogeneous or repeated-factor concerns do not invalidate the actual factor construction. | pass |
| GKR2-28 | GK-O13 | Coefficientwise 0/1 integer lifts of the actual F2 factors satisfy the official congruence, and their positive degrees persist modulo two. Absolute irreducibility is neither asserted nor required. | pass |
| GKR2-29 | GK-O14 | Each fixed q>=4 has every advertised m>=1, with strictly increasing exponents. The displayed q8 integers follow by exact symbolic substitution; no finite experiment is a proof premise. | pass |
| GKR2-30 | GK-O14 | q=2 has unit phi3; r=0 is auxiliary n1 only; r=1 is equality with unit cofactor. No endpoint is used as a genuine two-positive-degree factorization, or as an assertion that alternative factors are impossible. | pass |
| GKR2-31 | GK-O15 | For r>=1, q+1 divides q^(2r)−1; the integer quotient is odd. Hence v2(L_r−1)=k exactly, not merely at least k. No valuation of zero at r=0 is taken. | pass |
| GKR2-32 | GK-O15 | Exact accepted phi13 necessity says ALL such exponents have n−1=4*(16^(j+1)−1)/5 and valuation two. k>=3 rules out whole phi13 at every r>=1, using necessity rather than an old sufficient list. | pass |
| GKR2-33 | GK-O15 | At q=4, r=m+1 gives the exact old progression and aligns r1 with j0, r>=2 with j>=1. Whole phi13 absence for k>=3 excludes no individual component by itself. | pass |
| GKR2-34 | GK-O16 | No general-q necessity, full exponent/factor classification, novelty, monodromy/APN/component theorem or full annual solution is claimed. MCM literature and the earlier unverified bridge are motivation only. | pass |
| GKR2-35 | all | Read all sixteen author obligations, main/source/log/freeze records and complete accepted mathematical dependencies. No new GK peer review/conclusion read before this freeze. Prior 2024 structural/divisor audit context is disclosed. | pass |
| GKR2-36 | all | All six author artifact records, 417 core input occurrences/214 paths, separate cache hash, CP acceptance embeds, phi13 acceptance map and all 147 prior own paths are intact. Only the assigned new review prefix is written; fingerprints are metadata, not proof. | pass |

## Counterexample attempts and their disposition

1. **Specialize at c=1 before inversion.** The basis determinant then vanishes, so such a pointwise derivation would fail. The actual derivation takes place over a transcendental function field and removes the denominator before recovering a universal polynomial identity. The threatened locus is explicitly included by specialization afterward. No counterexample.
2. **Exploit isotropy or non-periodic Frobenius.** Ordinary bilinear pairings need not be positive and q²-Frobenius need not fix K. The proof assumes neither property. Its explicit pairings and determinant establish exactly the required independence. No counterexample.
3. **Recover only scalar necessary conditions.** This would be insufficient without a vector-space basis. The determinant first proves the basis and independence of the functionals, so the solved coefficients give the actual full relation propagated later. No gap.
4. **Cancel equal-degree recurrence terms.** Their degree gap is the positive integer q^(2r)(q+1), including the first recurrence step, so this cannot occur.
5. **Obtain only affine or extension-field factors.** CP1's exact-degree homogenization and free-cover descent retain the WHOLE divisor over F2. The new H=P_r has F2 coefficients. Thus neither possible defect applies.
6. **Use a non-genuine endpoint as official factors.** The explicit q>=4,r>=2 range removes unit divisor/cofactor cases. The candidate makes no claim that those endpoints lack every possible other factor.
7. **Confuse nonmembership in a sufficient phi13 list with absence.** The imported result is an accepted iff; exact valuation excludes its whole list of possible exponents. It excludes only the whole divisor. No quantifier gap.

All attempts above are hand arguments directed at specific inferences. There were no mathematical code runs, enumeration, CAS operations, or new certificate computations. There is no counterexample or unresolved issue to transmit for author repair.
