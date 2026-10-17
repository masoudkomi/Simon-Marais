# Constructor checks and issue ledger: original-weight universal return

2026-10-17 UTC. **Candidate proof - unverified.** This is constructor
checking, not an independent adversarial review. The new UW1–UW4 require
two OTHER initially blind whole nonconstructor audits. Root supplied
the exploratory cubic invariant and is a co-contributor, not an auditor.

The full proof is in the main file; all40 obligations are itemized in
the companion ledger. No scan/CAS/certificate or author rerun was used.

## Exact checks completed by hand

1. All module constructions use integer sums of coefficient permutations.
   A negative residue in sigma_(-f(s)) is not a negative coefficient.
   The source inverse indexing is maintained through all three moments.
2. The extra fifth inverse moment is obtained from the SIXTH-power sum,
   with S_6/p=1/42 and division by6a^5, giving coefficient1/252. It is
   not an assumption about an actual fifth binomial-series coefficient.
3. With H=t(t+1), normalized moments are
   w_3=-(72/5)(1-3H²/(H+1)³) and
   w_5=(6912/7)(1-5H²/(H+1)³). Expanding
   7w_5+800w_3+4608 gives exactly0. These coefficients are hand algebra.
4. A fixed w_3 value is a nonzero cubic equation in H. Leading coefficient
   comparison and its missing H² term prevent identically zero fibers.
   Composition by t²+t has degree at most6. No pointwise computation
   or value table is used.
5. In the abstract contradiction, common ratio values make BOTH v_r
   constant within a u-fiber. This justifies a bound on u-fibers; it is
   not inferred merely from the known bound on w_3 fibers without that
   earlier implication. The |S|>30 bound gives SIX u-values.
6. Common ratios C_3,C_5 give degree2/4 polynomials with leading terms
   3(b-a)X² and5(b-a)X^4. Thus both ratios must be zero. No assumed
   nonvanishing of their numerators is needed.
7. Constant v_3=A,v_5=B gives the nonzero degree-five polynomial
   4608X^5+800AX²+7B at every u. Its leading coefficient never vanishes
   at the allowed characteristic, even if A=0 or B=0.
8. The zero-action branch is handled BEFORE division by f. OW1's
   integer norm identity is reconstructed and provides two orbits at
   the original weight. The exceptional Q roots are omitted from S;
   no nonexistent nonzero inverse moment is granted there.
9. The complementary branch re-proves u nonconstancy on exactly S:
   P=Q(Qf-12C X(X+1)) is divisible by X^p-X, but its X^(p-1)
   coefficient is7/10. The p-1>4 and p>7 conditions are satisfied.
10. Every allowed theta_(s,t) has M_1!=0, complement2N, binary-sum
    coefficients and augmentation p-1. The ratio formula is an orbit
    invariant; different tuples are enough to separate the classes.
    No claim that all pair parameters give distinct classes is used.
11. The universal threshold is p>=37, with |S|>=p-4>=33. No attempt
    to cover primes below37 or to infer anything from failure of this
    threshold is made. The original research target p>=101 is covered.
12. Exact Fourier faithfulness is retained, while the reciprocal and
    higher-jet applications remain separate. All claims are algebraic,
    with no x,y dependence and no new signed Diophantine conclusion.

## Substantive issues and disposition

|ID|Status at construction freeze|Exact issue or remaining requirement|
|---|---|---|
|UW-I01|SUPPLIED argument; independent audits REQUIRED|Whole UW2 fiber implication, common-ratio polynomial contradiction and its actual group-ring application must be independently reconstructed. Constructor checking cannot promote them.|
|UW-I02|SUPPLIED direct derivation; attribution retained|Fifth inverse moment and constants7,800,4608 must be checked against the inverse-index convention and exact sixth-power sum, not copied as numerical evidence.|
|UW-I03|OPEN outside the theorem|No p<37 extension is supplied. The source's broader statements remain attributed; this proof's threshold is explicit.|
|UW-I04|OPEN source-application obligation|Source-specific Jacobi integer normalization/integrality, augmented singular systems, EVERY-conjugate cancellation, delta!=0 and size estimates still require complete proofs.|
|UW-I05|OPEN external attribution/priority|The source already has pairing/one-element and claimed two-list mechanisms. No novelty or full-source theorem repair is asserted by this additional elementary argument.|
|UW-I06|PRESERVED exact scopes|No actual equation solution, class-number exclusion, universal sparse-zero OW input, arbitrary weighted-jet rank or reciprocal cross-list injectivity is claimed.|

No unresolved mathematical inference is silently treated as an accepted
premise inside UW1–UW4. Their full supplied proof remains unverified
until both OTHER audits and coordinator reconciliation. Existing old
counterexamples and source-inspection obligations remain unchanged.
