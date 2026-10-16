# Coordinator acceptance: the concavity upper bound

2026-10-16 UTC. **Proved, independently reviewed — partial result.**
For the official fixed-polygon count,

    limsup_(n→∞) log2 C(n)/n² < 324757/500000 = 0.649514.

The coordinator read both full initially blind reports and issue logs,
their post-freeze addenda, and verified the construction/review manifests.
Both nonconstructor reviewers reconstructed the whole argument and primary
source hypotheses. No substantive mathematical objection or author repair
remains. The frozen candidate is
`../notes/deep-literature-r2-concavity-candidate-v1.md`, SHA256
`07dc9766e56eca4ec3359289a537072d47e6f5ce6b48129538552f54899728fc`.
The source and every initially frozen review artifact remain unchanged.

The accepted argument uses Dallant's actual six-variable cutpath domain,
joint concavity of two perspectives, symmetrization of the minimum of the
directional bounds, and two global supporting-plane bounds. Both reviewers
independently proved the endpoint cases and uniform strict slack before
taking a supremum. R1 used separate96-term Mercator enclosures; R2 used an
independently written96-term atanh enclosure. Exact arithmetic checks the
explicit constants in this analytic proof; finite grids and numerical
optimization are not premises.

Two source/presentation points are explicitly discharged:

1. Use the zone estimate only in its needed size range and initialize
   deletion/insertion at B2=1. Sum j=2,...,n−1. The literal stronger edge
   bound has an irrelevant n=1 exception. Both reviewers independently
   reconstructed this initialization; it changes no asymptotic inference.
2. The pruned encoding tree has **at most one** blue successor, which may
   be absent. The independent tree recurrence with zero-sized blocks
   proves the imported bound even when m<n−u. The older stronger wording
   is not required.

The accepted exposition is `../proofs/reviewed-concavity-v1.1.md`; its changes
are acceptance annotations and the already reviewed finite-size
clarification. No substantive mathematical repair was introduced by the
coordinator. R1's read-only Git-status wording correction is retained in
its separate operational addendum.

The coordinator's46 manifest-entry checks include repeated source/initial
records; they establish integrity, not another mathematical audit. See
`concavity-acceptance-integrity.json` and the companion acceptance JSON.

This improves the located0.6496 published bound within the project, using
attributed zone, cutpath and tiling-dictionary results. **Originality and
priority are not established.** The exact rates and existence of the
official normalized limit remain unresolved. The fixed-direction entropy
result is a separate earlier partial theorem.
