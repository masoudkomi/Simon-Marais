# Direction coarsening: blind review 2 issue log

Date: 2026-10-16 UTC. Candidate SHA-256:
`6379079ab65bd0976058bcc323bf411beaa33c455a20eec5782885c3c72bab5a`.
Frozen independently with the initial report before comparison with any
other coarsening review.

| ID | Concern | Independent disposition | Remaining obligation |
| --- | --- | --- | --- |
| CR2-01 | P might depend on a reduced-word representative. | Resolved: local commuting swaps have disjoint position intervals, unchanged color decisions, and identical or commuting projected outputs. | None for DC1. |
| CR2-02 | Projected segments or port orders might depend on the chosen embedding or sweep. | Resolved: identify a gap by projected boundary-strand label and directed retained-vertex gap index. Original local commutations preserve the decorated graph and all port orders. | Exposition improvement: state these canonical gap IDs and the decoration-invariance argument explicitly. |
| CR2-03 | Adjacent original labels might require more than two partner choices after smoothing. | Resolved: full-order adjacency implies neighboring same-color ranks, which remain ordered on projected tracks. | Rejecting impossible full-order contacts is unnecessary for an upper bound. |
| CR2-04 | Repeated contacts could require an S! pairing factor. | Resolved: for each neighboring-rank pair, match the k-th port pointing toward the other rank on each directed track. Original monotone sweep order forces this. | None for DC1. |
| CR2-05 | Pairings might leave global sweep/rotation information unrecorded. | Resolved: cross-route at the restored vertices, retain projected routing at the other vertices, and follow boundary labels. This recovers original-strand event orders; all global linear extensions differ by disjoint commutations. | Exposition improvement: include this reconstruction rather than relying only on the words "including local rotations." |
| CR2-06 | Weak-composition count may hide label or event-order choices. | Resolved: canonical gaps are labelled, each port position is its gap index, bits identify the partner-rank pair, and matching is forced. Count is binom(n^2-1,2S)2^(2S). | None. |
| CR2-07 | n=1, D=1, D=n, S=0 or balanced remainders might invalidate the formula. | Resolved: natural n=1 extension gives binom(0,0)=1; D=n is equality; positive blocks require n>=D; all entropy endpoints and fixed-D remainders are valid. | Official domain remains n>=2. |
| CR2-08 | Strand-addition monotonicity in the conditional step was asserted briefly. | Resolved by thin-strip cloning of a specified extreme same-color strand, with deletion as a left inverse. | Optional exposition expansion. |
| CR2-09 | Fixed-direction full-count limit (H) may be replaced by a restricted patch/fiber or a physical thermodynamic heuristic. | **Open external premise, blocking any unconditional limit-existence conclusion from this argument.** The candidate correctly labels it as a hypothesis. The inspected sources do not verify it for all D. | Supply an exact theorem/proof with the present full count, fixed boundaries and normalization; audit its hypotheses separately. No objection to the stated conditional implication. |
| CR2-10 | Conditional limit equality might be promoted to exact numerical rates or a full 2017 solution. | Not a defect of the candidate, which expressly disclaims this. DC1/DC2 and (H)=>equality remain partial results. | Preserve the distinction; no value or priority claim follows. |

Recommendation: DC1, DC2 and the implication from precise finite-real (H)
may be accepted mathematically once the coordinator compares the two
independent audits. No substantive counterexample was found. (H) remains
unproved by this review, and no unconditional/full-solution promotion is
recommended.
