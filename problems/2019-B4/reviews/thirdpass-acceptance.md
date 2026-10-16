# Coordinator acceptance: bounded-separation partial results

2026-10-16 UTC. **Proved, independently reviewed — partial results.**
The coordinator read both full initially blind reports and both issue logs,
checked the operational addendum, and verified the frozen construction and
review manifests. No substantive mathematical objection or author repair
remains. This acceptance covers the frozen mathematical body
`../notes/thirdpass-bounded-separation-v1.md`, SHA256
`3364e8c6cf23ba3ecb250f13a5873732c108b6904a68126f52f5d7234eb916d4`.
The original candidate and initial reports remain unchanged.

Accepted additional results are:

- Each finite separation cap defines a regular avoidance language whose
  minimal forbidden words are exactly the actual minimal obstructions with
  a witness within that cap. The legal-path envelope is essential here.
- These obstruction subsets increase coefficientwise to the full set, and
  their growth rates are nonincreasing and converge to the official rate.
- The exact separation-three obstruction language is
  `RRLL | RRLRRLRL (RRLRL | LRLRL | LRLRRLRL)* LRLL`, with generating function
  `z^4+z^12/(1−2z^5−z^8)`.
- The separation-seven integer-vector certificate proves
  **1.76521 < lambda < 1.834856083**, using the previously accepted lower
  bound. The numerical Perron estimate is not a proof input.

Both nonconstructor reviewers independently reconstructed the whole chain,
built a separate queue monitor before consulting constructor tables, and
checked all11,662 strict certificate rows. Both completely checked the
grammar product and all143 earlier obstruction witnesses/widths. Their
finite grid checks have explicitly stated sizes; neither claims a fresh
full length24 exhaustion. See `thirdpass-review-1.md` and
`thirdpass-review-2.md`, their issue logs, independent sources and manifests.

The coordinator verified208 recorded manifest entries, including repeated
initial/final records; this is integrity evidence, not a third independent
mathematical review. Exact report/manifest hashes are in the companion JSON
and `thirdpass-acceptance-integrity.json`.

Scope qualifications are retained: cap1 is universal; growth monotonicity
need not be strict at every cap; regularity/rationality at a fixed cap does
not imply it for the limit. The four length19 contexts with three histories
remain counterexamples to universal two-history rigidity. The R1 ignored
bytecode-cache side effect is documented in its dated addendum, with all70
constructor artifacts unchanged; it has no mathematical effect.

The exact growth constant, full generating function, stronger entropy-tail
control and novelty remain unresolved. This is no complete solution of
B4(b). Generic synchronization and automaton techniques are attributed to
their earlier literature; no inaccessible theorem fills a proof gap.
