# FL1/CL1/OB1 initial issue ledger, reviewer 2

2026-10-17 UTC. Whole initially blind nonconstructor audit. Target SHA-256:
aa4c79b1fb3136ecd3e7c5ab845733697cca925ba8203b2988fba5c9a793bd95.
No peer clean-strata conclusion was read before freeze.

No substantive open objection found. These adversarial concerns are
resolved by the hypotheses and reconstructions in the full report.

| ID | Concern | Disposition |
| --- | --- | --- |
| CS2-01 | Boundary Green identity could have a wrong sign or require interior affine error. | Closed: exact expansion plus integration of d(b_i e_j) gives e_i da_j-e_j db_i. Only whole-boundary error is used. |
| CS2-02 | Tile flux might count areas rather than tile numbers, or miss cut tiles and oscillating boundaries. | Closed: ij minor is 1/(j-i), tile area j-i; fractional count differs only on O_D,C(L+1) boundary tiles, by the fixed-radius arclength tube argument. |
| CS2-03 | Coarsening might forget within-group label assignments or inversion signs. | Closed precisely when all within-group comparisons are fixed and groups are consecutive. Full r_g sequences give the inverse; totals alone do not. |
| CS2-04 | Interval isomorphism might only count word paths instead of tilings. | Closed: covers use the same fine ranked labels, and disjoint-swap commutations are preserved both ways. |
| CS2-05 | Coarse boundary could acquire an interior common vertex or nonvertex contact even in the clean case. | Closed: increasing swaps strictly raise the relevant prefix y whenever the count vector changes. Equality forces the same fine prefix vector, contradicting the assumed fine Jordan lens. Unit x steps handle between-vertex contacts. |
| CS2-06 | OB1 may miss another fine cover chain or another assignment above BACB. | Closed by the exhaustive four-word cover argument and the two possible first-B assignments. Fine class count 1, coarse count 2, and the obstruction are hand proofs. |
| CS2-07 | OB1 could be only an abstract/nonconsecutive-group failure, or contradict global DC1. | Closed: groups are consecutive, fine geometry has interior gaps 3,4,1, coarse common tail leaves an actual hexagon, and DC1 has different full sorted/reversed endpoints. |
| CS2-08 | The 0.137-second search might be needed as an unrestricted proof. | Not a proof premise. Frozen metadata read, no rerun; the standalone exact proof supplies the counterexample. |
| CS2-09 | Rare flux plus clean insertion could be silently promoted to general stratum recovery. | Not claimed; OB1 blocks that promotion. No annulus, EAI, PR, H or official rate is established. |

The O(epsilon L^2+L) large-scale convention uses L>=1; the preceding
exact boundary count includes L+1. This is harmless in the stated
macroscopic application and should be retained when using the estimate
outside that regime.

Recommendation: no substantive objection to the three stated partial
claims, subject to the other independent audit and coordinator review.
No status promotion is made by this reviewer.
