# 2022 B4 issue log

The coordinator accepted the repaired v3 density theorem and supplementary v1 partial claims after both initial audits and both independent repair re-audits. All substantive objections are closed in the accepted versions. V2 remains a failed historical proof; its defect is not erased. The universal equality gap remains open. See reviews/acceptance.md.

| ID | Version / location | Objection | Severity | Repair / evidence | Re-review | Status |
|---|---|---|---|---|---|---|
| 2022-P1 | proof.md P1 | Verify the exact simultaneous quotient arithmetic and finite control-word bijection modulo 60*10^N, including negative r+d in residue representatives. | substantive audit | Algebra and shift induction supplied; exact graph evidence only. | R1/R2 complete; v3 repair separately re-audited | closed for accepted v1/v3; v2 defect preserved |
| 2022-P2 | proof.md P2; proof-extension-v2.md | Verify that abstract sign-based choices exist, all floor bounds and endpoint cases hold, and the finite path bound is uniform for fixed d. | substantive audit | Analytic proofs supplied; finite graph checks are supplementary evidence. | R1/R2 complete; v3 repair separately re-audited | closed for accepted v1/v3; v2 defect preserved |
| 2022-P3 | both density drafts | Check the counting-to-upper-natural-density argument; ensure it does not assume stochastic independence or turn density zero into emptiness. | substantive audit | Exact congruence classes counted; full universal gap explicitly retained. | R1/R2 complete; v3 repair separately re-audited | closed for accepted v1/v3; v2 defect preserved |
| 2022-P4 | proof.md P3 | Check arbitrary-delay formula and full official hypotheses; no claim about later hitting time. | boundary audit | Exact formula and 2,400 finite parameter checks. | R1/R2 complete; v3 repair separately re-audited | closed for accepted v1/v3; v2 defect preserved |
| 2022-P5 | proof.md P4 | Verify periodic-state quotient equation, fixed-integer divisibility for all periods, and the stationary-product contradiction. | substantive audit | Analytic candidate supplied; d-only periodicity explicitly excluded from the claim. | R1/R2 complete; v3 repair separately re-audited | closed for accepted v1/v3; v2 defect preserved |
| 2022-GAP | full B4(b) | Could an ordinary positive integer lift follow a nonperiodic infinite avoiding path? Density zero does not eliminate it. | unresolved research gap | No proof or counterexample. | future research | open |

## Initial audit findings and constructor repair

The initial reports reviews/review-1.md and reviews/review-2.md were read only
and remain immutable. Their fingerprints and the frozen proof versions are
recorded in repair-v3-notes.md. The entries below acknowledge the objections;
an author-supplied repair does not close them before reviewer re-audit.

| ID | Version / location | Objection | Severity | Repair / evidence | Re-review | Status |
|---|---|---|---|---|---|---|
| R1-2022-01 | v2 density conclusion | K(-1)=3 does not work after every prefix: (599,600) reaches state (3,12) after three avoiding steps, needing four more abstract steps. | blocking mathematical defect | V3 Sections 3-6 use M=max(abs(initial difference),29), K=M+1, uniformly over every reachable state; exact witness reproduced. | Both v3 re-audits complete | closed in v3; frozen v2 remains defective |
| R2-2022-01 | v2 lines 54-77 | K(1)=4 fails at a later block boundary: (25,24) reaches state (6,27) after four avoiding steps, needing five more abstract steps. | blocking mathematical defect | Same uniform v3 radius/path/counting repair; boundary-product witness reproduced exactly. V2 remains frozen and is not accepted. | Both v3 re-audits complete | closed in v3; frozen v2 remains defective |
| 2022-V3-UNIFORM | v3 Sections 3-6 | Audit the integer remainder inequality, invariant radius, at-most-K path from every reached state, and the repeated-block count with that fixed K. | required substantive audit | Standalone analytic proof plus bounded standard-library evidence; all computations labelled evidence only. | Both full independent v3 reconstructions accepted | closed |

The original P1-P5 obligations received both initial audits: v1 had no
substantive findings, while P2/P3's v2 extension has the defect above. Only
the coordinator may promote any reviewed partial result. The full-question
gap 2022-GAP is unchanged by this repair.
