# Accepted conditional OW1--OW3: original-weight orbit selection

2026-10-17 UTC. **Proved, independently reviewed conditional partial results.**

OW1 proves that an ASSUMED positive half-weight element u in I_f with nonzero inverse moment produces TWO nonconjugate free positive elements at ORIGINAL augmentation p-1, for p>=5. The actual constructions2u andu+sigma_hu are separated by a strict INTEGER coefficient-norm identity. The optional Fueter application retains direct-action-zero as a separate explicit hypothesis.

OW2 assumes an actual0/1/2 coefficient vector theta in I_f with complement2N and nonzero inverse moment. If its zero-countz satisfies the STRICT inequality2z(z-1)+2<p-1, a ratio-set count finds disjoint current defect supports. It proves ACTUAL positivity after subtractingN, preserves originalweight and freeness, doubles the zero-count and separates the conjugacyclass. OW3 iterates using the CURRENT support and the stated largest-input inequality, givingr+1pairwise separated original-weight orbits. Faithful Fourier consequences are exact; no reciprocal injectivity is transferred.

Neither a suitable half-weight starting element nor the sparse-zero hypothesis is proved universally. FS2 is not used to grant either condition. No solution-specific Jacobi integrality, higher-jet rank, every-conjugate cancellation, size/nonzero-delta estimate, Diophantine exclusion, full annual answer or novelty follows.

Root constructed NEWOW and is NOT an independent reviewer. Reviewers review_2017_coarsening_r1 and review_2021_reasoning_j15_r2 froze their COMPLETE initially blind WHOLE reports before peer comparison, reconstructing all18obligations in18/30checks. Reviewer1's OLD FS authorship and reviewer2's OLD FSreview/PG/CF1/unrelated2021roles are disclosed. This is not independent self-review of any old authored theorem. Root read the complete candidate, BOTH full reports, ALL ledgers and BOTH source records. No substantive issue or required repair was found in the written conditional scopes. No mathematical scan,CAS,certificate orauthorrerun was used. Internal review is not externalvalidation; novelty remains unestablished.

The complete frozen submission follows as a byte-identical suffix. Its historical unverified label records submission status; this header and acceptance state the current exact conditional scope.

---

# Original-weight free-orbit selection in two explicit branches

2026-10-17 UTC. **Candidate proof — unverified.** Root constructor, AFTER the complete initially blind FS1–FS3 wholeR1 was frozen. This is a NEW separate construction, outside FS and its audit scope. Two other initially blind whole audits are required before promotion. It gives conditional algebraic selection results, not a new Nagell–Ljunggren exclusion or a universal solution of the remaining selection problem. Novelty is unestablished.

Fix an odd prime p>=5. Use direct indices sigma_a(zeta)=zeta^a, G=F_p^*, j=sigma_(-1), N=sum_a sigma_a. For theta=sum n_a sigma_a define

    wt(theta)=sum n_a,
    F(theta)=sum n_a*a in F_p,
    M(theta)=sum n_a/a in F_p,
    ||theta||²=sum n_a² in Z.

Let I=(vartheta Z[G]) intersect Z[G], vartheta=(1/p)sum_(c=1)^(p-1)c sigma_c^-1, and I_f=I intersect kerF. Positivity means all integer coefficients are nonnegative. The module is G-stable and additive. It containsN: psi1=(2-sigma2)vartheta has inverse-basis coefficients floor(2c/p) in{0,1}, with opposite coefficients summing1, so psi1+jpsi1=N. Both F(N) andM(N) are0. Direct reindexing gives

    F(sigma_h theta)=hF(theta), M(sigma_h theta)=h^-1 M(theta).

In particular M(theta)!=0 implies trivial G-stabilizer. These facts follow directly from the definitions; no annihilation/class-field theorem is imported.

## OW1. A free positive half-weight element supplies TWO original-weight orbits

Suppose there is a positive u in I_f with wt(u)=(p-1)/2 andM(u)!=0. Its coefficients need not be binary for the following conclusion. Choose ANY h inG other than1,-1, which exists becausep>=5. Then

    theta1=2u, theta2=u+sigma_h u

are positive elements ofI_f of the SAME original weightp-1. Their inverse moments are2M(u) and(1+h^-1)M(u), both nonzero. Thus both are free. They are NOT Galois conjugate, because

    ||u+sigma_h u||²
       =4||u||²-||u-sigma_h u||²
       <4||u||²=||2u||².

The strict inequality uses h!=1 and the freeness ofu. The Euclidean norm is invariant under coefficient permutations. This proof uses a positive sum of translates; no negative coefficient is hidden in an automorphism index.

One application, still conditional on the displayed hypothesis, is a Fueter elementu=psi_t with F(psi_t)=0 andt²+t+1!=0 inF_p. Its positivity and half-weight follow from the defining floor increments. Its inverse moment is(t²+t+1)/(12t(t+1)) for1<=t<=p-2 atp>=5, as in the separately acceptedMS square-sum lemma. Thus any such NONEXCEPTIONAL zero of the action functional closes the two-free-orbit selection task at ORIGINALweight. An exceptional order-three Fueter element with both moments zero does not meet OW1. Existence of a suitablet for everyp is NOT asserted. A zero direct moment is distinct from a zero inverse moment.

## OW2. Sparse coefficient defects give a second original-weight orbit

Suppose theta inI_f has integer coefficientsn_a in{0,1,2},

    theta+jtheta=2N, M(theta)!=0.

Its weight is p-1. Let Z={a:n_a=0}, z=|Z|. NonzeroM excludes theta=N, so z>=1. Opposite coefficients sum2, hence the2-coefficient support is exactly-Z and the1-coefficient support is the complement ofZ union(-Z). In particular Z and-Z are disjoint.

If

    2z(z-1)+2 < p-1,                                      (OW)

there is another positive free elementtheta' inI_f of weightp-1, not conjugate totheta. In fact it has exactly2z zero coefficients.

Proof. Put delta=theta-N, with values-1 onZ,+1 on-Z,0else. Its supportS=Z union(-Z) has

    S/S=(Z/Z) union(-Z/Z),
    |S/S|<=2(z(z-1)+1).

The bound counts at mostz(z-1) ratios of distinct ordered points and the single common ratio1. By(OW), chooseh inG outsideS/S. Then hS andS are disjoint. Since1,-1 belong toS/S,h is neither of them. Define

    theta'=N+delta+sigma_h delta=theta+sigma_h theta-N.

This expression has a negative coefficient onN algebraically, but its ACTUAL coefficients are nonnegative: disjoint supports ensure thatdelta+sigma_h delta has values only-1,0,1. Thus theta' has values0,1,2. Its zeros are the disjoint setsZ andhZ, exactly2z points. Opposite coefficients still sum2. Its weight is p-1, since both delta vectors have augmentation0. Additivity/G-stability andN inI give theta' inI, whileF(N)=F(theta)=0 givesF(theta')=0.

Moreover M(theta')=(1+h^-1)M(theta)!=0, proving freeness. Zero-count invariance already separates it fromtheta. Independently, delta is orthogonal toN in the INTEGER Euclidean inner product, and its shifted support is disjoint. Therefore

    ||theta'||²=(p-1)+2||delta||²
             >(p-1)+||delta||²=||theta||².

This is a strict norm comparison at the same weight, with no reduced-field cancellation in an integer norm.

## OW3. Iteration at the same weight

Under OW2, repeat the construction while its stated inequality holds for the CURRENTzero-count. If an integerr>=1 satisfies

    2(2^(r-1)z)(2^(r-1)z-1)+2 < p-1,

then there are r+1 pairwise nonconjugate positive freeI_f elements of ORIGINALweightp-1, with zero-countsz,2z,...,2^r z. The displayed inequality at the largest input count implies every earlier required inequality, since2x(x-1)+2 is increasing forintegersx>=1. Each induction preserves0/1/2 coefficients, opposite-pair identity and nonzeroM. Different zero-counts separate every pair. No assertion is made when the inequality fails, and no universal sparse-zero hypothesis is supplied.

For all these elements, E(theta)=sum n_a zeta^a is faithful and equivariant: a degree<=p-1 polynomial withconstant0 cannot be a nonzero multiple ofPhi_p, whoseconstant is1. Irreducibility ofPhi_p follows, for example, by Eisenstein afterX->X+1. Thus each freeelement gives p-1 distinct Fourier values, and nonconjugateelements give disjoint Fourier sets. No Fourier injectivity is transferred to a reciprocal map.

## Exact remaining gap

OW1 covers a free positive half-weight element already in the Fermat kernel; it does not produce such an element universally. OW2/OW3 cover a specified sparsity regime, without proving that a universal FS2 selection has that sparsity. In particular an element2psi with half its coefficients0 can fail(OW); OW1 is a different argument whenFpsi=0. A generic positive weightp-1 element need not be free. Nothing here proves the two-orbit task for everyprime, higher-jet rank, solution-specific Jacobi integer existence/integrality, the cancellation through every conjugate, a nonzero delta, a class-number consequence or a height bound. The annual equation remains unresolved. Even a completed original-weight selection alone would not supply those later steps.

The new lemmas use only exact group-ring identities, coefficient supports, a cardinality pigeonhole and integer norms. No program, prime scan, coefficient table, CAS or certificate replay was used. Earlier FS andMS proofs/reviews remain byte-for-byte unchanged. Root cannot independently review this new packet.
