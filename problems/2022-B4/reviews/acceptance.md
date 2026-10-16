# Coordinator acceptance: 2022 B4(b) partial results

Date: 2026-10-16. **proved, independently reviewed (partial results)**.

Accepted: the standalone repaired v3 fixed-offset density theorem, and the supplementary v1 finite lifting, strip-restricted density, arbitrary finite delays, and exclusion of ultimately periodic full residue states. **The universal equality question remains unresolved.** Density zero does not imply an empty exceptional set. No two-dimensional density conclusion or novelty claim is made.

Both fresh independent reviewers initially audited identical frozen v1/v2 versions, blind to one another, and reconstructed their full arguments. They found no substantive defect in v1. Each independently found a genuine flaw in v2: its initial-state hitting bound was reused after prefixes where it no longer applied. Their distinct admissible integer witnesses, original reports and failed v2 are preserved.

The author supplied a separate, self-contained v3 repair. Exact floor remainders give 10D=9d+u-v, hence the initial-data-dependent radius M=max(abs(delta),29) is invariant. The uniform hitting bound K=M+1 applies after every surviving prefix. The finite lifting and repeated-block density proof are rebuilt with this fixed K.

Both original reviewers independently re-audited the whole repaired theorem and dependencies against frozen v3 SHA-256 `0238f99a93b0ba1076484db1c16b173efcc02be4410e859f2c5bafc55f0f2a3f`, without seeing the other's re-audit conclusions. Both closed their original objections and found no new substantive gap. Their analytic reconstructions cover negative floor arguments, radius endpoints, all-prefix uniformity, path counts, exact finite moduli and the upper-density limit. Separate exact evidence supplements the proofs; it does not replace them.

The coordinator read the initial findings and both full re-audits, checked frozen fingerprints, issue disposition and the exact scope, and accepted the partial results. Accepted copies in proofs/ change status annotations only. Frozen v1 is preserved at proofs/candidate-v1.md (originally proof.md); v2 and constructor v3 remain at their original paths. The current proof.md is a result register. No failed argument is silently relabelled valid.

Immutable evidence scripts that check the original proof.md hash can be rerun using tools/reproduce_frozen_review.py, which copies the year to ignored local cache, restores the frozen proof there, records the child PID/timeout, and preserves the real reports and evidence. See computations/README.md for commands.
