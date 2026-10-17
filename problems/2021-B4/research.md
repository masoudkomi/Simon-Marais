# 2021 B4 research log

## Reviewed single-center classifications

The sole-H4 and sole-H2 double-zero J15 classifications are now **proved,
independently reviewed necessary conditions**. Both candidates passed two
fresh whole initially blind audits, full coordinator report/issue reading,
and exact manifest verification. See proofs/reviewed-J15-soleH4-v1.1.md,
proofs/reviewed-J15-soleH2-v1.1.md and reviews/single-center-acceptance.md/json.
These add seven patterns and precise actual witness roles. No complete
mask is removed and no row is proved to lift. Their distinct small
residues preclude directly importing the sole-H3 collision parity argument.

## Current reviewed result

The new J15 double-zero analytic restrictions D1–D5 and the stated
low-order rational family are **proved, independently reviewed partial
results**. Both fresh initially blind whole reviews are complete, fully
read and reconciled by the coordinator, with all manifest records matching
and no repair requested. See proofs/reviewed-reasoning-J15-v1.1.md and
reviews/reasoning-J15-acceptance.md/json. The nonunit-a14 branch, other
center patterns, multiplicity three and lower J remain unresolved. No
complete J15 mask or degree-20 solution follows. Earlier accepted J16 and
other restrictions remain in force. The first-investigation prose below
is historical and does not supersede later acceptance records.

Status: first investigation checkpoint, 2026-10-16. No full solution claimed.
All proposed arguments remain **candidate proof - unverified**. No candidate
has received the two required independent adversarial audits.

Requested worker setting: `gpt-6.1-sol`, reasoning `max`. This was explicitly
requested through the launch interface by the coordinator. Verified effective
model/effort readback was unavailable; the request is not a verified readback.
The coordinator monitors authoritative account-wide weekly telemetry and owns
Git checkpoints. This worker made no commits, pushes, installs, or shared-file
edits, and spawned no agents.

## Statement checks

See statement.md and official PDF. The contest requires a rational shared root
for each derivative, not merely a nonconstant gcd over Q. The latter is a
strictly weaker general formulation; known general positive results apply to
the contest but a statement about arbitrary rational coefficients alone does
not erase the shared-root field requirement. Part (a)'s prime-degree result is
used only as attributed context; it was not investigated or reproduced.

## Approaches and results

### Present-day status audit

The literature record does not justify labeling all degrees solved. The active
Ghosh preprint claims all degrees, but an August 2026 research preprint
explicitly withholds independent verification. The 2015 Battiston and 2017
Dobrowolski universal-proof claims are withdrawn for acknowledged errors. The
accepted Ghosh finiteness paper is a different work. Source versions, dates,
publication distinctions and the 20-versus-24 frontier discrepancy are saved
in references.md. No specific flaw in Ghosh's current proof was established
by this initial pass. It would be misleading to call it refuted or accepted.

### Route 1: integral normalization and local arithmetic

The rational witness tuple admits a centered monic integral normalization with
primitive integer witnesses. The proof uses a triangular Hasse recurrence,
without integrality assumptions on nonwitness roots. A sufficient local test
then asks for absence of nontrivial centered polynomials over F_p with shared
F_p-roots. This potentially needs less than absence over the algebraic closure,
but no new successful prime was established. Both reductions, with explicit
hypotheses, are candidate lemmas in proof.md.

The easiest attempted primes fail concretely: for both d=20 and 24 and every
p in {2,3,5,7,11}, the saved exact run finds x^d-x^m over F_p with the required
Hasse conditions at 0 and 1. This is a known bad-prime mechanism, attributed
in proof.md. Thus rationality of the witnesses does not itself eliminate
small-field failures. A higher p-adic lifting obstruction remains possible;
the finite-field examples were not claimed to lift to Q or Q_p.

### Route 2: exact elimination for two lower terms

For a centered trinomial x^d+A x^a+B x^b, H_b and the shared-root equality
express A,B in terms of its nonzero witness v. The other active condition at
u gives two power equations for t=u/v. A binomial-ratio equality is necessary
even for complex t. The candidate derivation is in notes/two-support.md.
An exact Fraction-arithmetic script checks all exponent pairs in degrees
20,24,28,30: respectively 153,231,325,378 pairs, no equality. This removes
rational-height bounds for the scanned trinomial family, but is finite
computational evidence and is not an unrestricted support theorem. It is
related to the two-support result in Marashdeh's preprint; no novelty claimed.

The obstruction is structural: the next family has three lower terms and up
to three nonzero witness values. Two active conditions no longer determine
both coefficients as functions of a single ratio. General resultants or
Groebner computations have not been run, since their cost needs a separately
monitored plan.

### Route 3: sparse integer-witness interpolation search

The triangular Hasse equations reconstruct coefficients exactly for any fixed
support and witness tuple. For d=20,24,28,30, all supports of at most three
lower terms and all nonzero witnesses in {-2,-1,1,2} were considered. Gcd and
reflection symmetries skip equivalent tuples. In total 544616 tuples were
visited, 237112 were solved after those filters; none satisfied all shared
polynomial-root equations. Each discovered finite-field example was also
independently checked by direct evaluation of every Hasse derivative.

These are exact arithmetic searches, not numerical root approximations. They
cannot exclude witnesses of larger normalized height, more than three lower
terms, or general complex coefficient configurations. The support restriction
and witness-height restriction are independent and both are recorded in the
script and exact output.

### Route 4: real geometry and high derivatives (not completed)

After centering, the coefficient of x^(d-2) must be
-binom(d,2) s_(d-2)^2 because that Hasse derivative is quadratic and its
witness is rational. This gives a square constraint and a nonpositive
coefficient. It does not imply that all roots of f are real. Neither Rolle's
theorem nor a sum-of-squares argument can be applied to all roots from the
contest's rational shared witnesses alone. Even the real-root version of
Casas-Alvero should not be casually asserted solved: the primary Draisma-de
Jong exposition explicitly invited progress on that subcase. This route was
stopped at the precise missing implication instead of assuming real-rootedness.

## Next steps

1. Obtain two fresh independent adversarial audits of the candidate reductions
   if the coordinator wishes to promote any lemma. One reviewer must reconstruct
   the full argument. Reviewers must not see one another's first reports.
2. Verify the binomial-ratio elimination with an independent symbolic
   reconstruction; decide whether a general inequality adds value beyond the
   attributed 2026 support theorem.
3. For a focused new-degree attempt, test higher p-adic lifting constraints on
   normalized primitive witnesses. The displayed small-field examples explain
   why mod-p emptiness at the smallest primes is unavailable.
4. A type-three scenario elimination in degree 20 is substantially more
   targeted than unrestricted coefficient search. Before attempting it, check
   new primary-source claims and bound the computation's runtime.

## Focused second-pass checkpoint, 2026-10-16

The source audit in `notes/ghosh-full-context-audit-v1.md` reconstructs Ghosh
v2's relevant proof chain and checks that Theorem A, if valid, would apply to
the exact contest statement. It identifies the missing nilpotent-coefficient
argument after (4.23), strengthens the initial ambient example to a local
determinantal model satisfying the numerical generator conditions, and records
two additional general inference failures in the earlier generator/topological
arguments. These are candidate source objections awaiting independent review.
They do not supply a derivative-family counterexample or disprove the theorem.
The existence of a specialized repair remains unresolved. The paper cannot be
used as a validated all-degree result on the basis of this pass.

The final Koszul/homology mechanism was reconstructed conditionally on its
injectivity input; no separate fatal problem there was established. The audit
does not certify all cited results or the entire preprint. The distinct accepted
finiteness work is not conflated with the universal-proof claim.

A bounded fresh rational-witness direction is saved in
`notes/rational-witness-p-plus-one-v1.md`: in the published p+1 normalization,
if the first nonzero coefficient at the double root had p-adic valuation 1,
the residual factor would be Eisenstein and leave only rational roots 0 and 1.
The precise published two-recycled-root obstruction, which is stronger than a
bound on the full root set, would then contradict the rational-witness contest
hypothesis. The resulting candidate condition is valuation >=2. It makes no
assumption that the remaining algebraic roots are rational.

For d=20/p=19 an exact standard-library calculation visits all 131072 binary
center choices, reproduces 6680 necessary congruence survivors, and conditionally
excludes 3043 by this candidate restriction; 3637 remain. This is finite necessary
condition evidence, not an emptiness result or full degree proof. Both the
partial lemma and its computation need two independent audits.

The targeted literature search also found Massri's active v6 primary preprint
arXiv:1806.09561, Theorem 7.10, claiming the degree-20 three-recycled-root exclusion.
Earlier withdrawn versions and the present active version are distinguished in
references.md. Its complete resultant calculation was not reproduced, and its
degenerate parameter treatment still needs checking; no new 3^17 CAS run was
launched. The coordinator cached the paper. This avoids treating the earlier
social-media description as the only evidence for that family.

All new scripts run child processes with explicit 30-second timeouts and
incremental output. Both completed in under one second; PIDs, exact parameters,
dependencies and outputs are saved. No process remains running. Only the
assigned year directory was edited; `proof.md` remains unchanged. The worker
made no commits/pushes, spawned no agents, and did not change shared telemetry
or source manifests. Coordinator settings/telemetry authority is unchanged.

Checkpoint verification: `git diff --check -- problems/2021-B4` passed, and
`git diff --exit-code -- problems/2021-B4/proof.md` confirmed no change. The
proof-register SHA-256 is
`453cd604409526ddf7bd37a44b9d7f6a9d7f7173f4f7bc0b7a178affc3fd85a9`.
The authoritative `get_usage_limits` readback at this checkpoint reported
**4% total weekly used** in the 10080-minute window, below the 90% cutoff.

## Coordinator integration, 2026-10-16

The rational-witness Eisenstein restriction and finite filter are now
**proved, independently reviewed (partial result)** after both fresh blind
full reconstructions. See reviews/witness-acceptance.md. Presentation repairs
are versioned separately; no mathematical repair was requested. This does
not promote the original reductions or the later Newton packet.

The later candidate Newton packet proposes long-edge rational-root bounds,
a width-one derivative obstruction, complete height-free J17 compatibility
exclusion and a J16 restriction in degree20. All29928 compatibility records
and parameters are saved; the combined necessary filter leaves1164 patterns.
These new claims remain unverified and solve no full degree. The first fresh
adversarial audit is active; the second is pending.

## Reviewed rational J=16 exclusion and literature expansion

2026-10-16 UTC: the whole L1–L4 argument is **proved, independently reviewed (partial result)** after two fresh blind full reconstructions, every coefficient/fiber record and all final exact obstructions. The 840396→361194→2026→90→14→0 necessary digit tree is empty at precision six. All88J16 masks are removed, leaving684 other necessary patterns; degree20 remains unresolved. See notes/coordinator-J16-exclusion-reviewed-v1.1.md and reviews/J16-acceptance.md/json.

The separate frozen J15 triple-zero leading candidate only restricts that multiplicity subcase, not entire masks. It is unverified and must not be used as an accepted dependency. A new deep primary-literature pass checks known degree families and rational versus all-roots-rational hypotheses before extending computations.
