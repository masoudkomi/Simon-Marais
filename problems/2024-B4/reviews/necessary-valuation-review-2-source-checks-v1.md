# Necessary valuation: review 2 source and scope checks

2026-10-17 UTC. Full initial review and ledger completed without reading
any new peer NV review or coordinator reconciliation. This file records
what was actually read, which hypotheses were used, and the commands.

## Official source

I read the complete project `statement.md` and opened the official
[2024 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf)
on 2026-10-17. Page2 B4(b) agrees with the normalization: odd positive
integer n; integer polynomials; a coefficientwise modulo-two congruence;
two factors each nonconstant modulo two. The question asks for all such
n. The new NV implication addresses a restricted whole divisor and does
not answer that full question. I did not solve or reproduce part(a).
The original polynomial convention, rather than the induced finite-field
function, is retained throughout.

The web tool supplied the official PDF text and pagination. I do not
claim a new binary retrieval hash for that viewer response. The local
statement and protocol fingerprints are in the administrative validation.

## Accepted CP1 dependency and authorship boundary

I read ALL of `proofs/reviewed-composition-Kasami-v1.1.md` (17366bytes),
not only its CP1 statement, and both the markdown and JSON acceptance
records. Accepted scope: for all odd d,n>=3, whole homogeneous phi_d
divisibility over F2 iff g_n=H(g_d) for an H over F2, with d-1 dividing
n-1. Its complete body handles the linear homogeneous coordinate change,
full affine degree, homogenization, free rank-four module, monic h-adic
expansion, repeated diagonal cancellation, and d=3/n=3 unit endpoints.
NV uses this implication and its degree relation. It does not use CP2's
all-q construction, CP3's family, the old phi13 progression, generalized
Kasami GK1--GK3, or absolute component classifications as proof premises.

I was the constructor of that OLD CP1--CP3 input. This fresh report is
an independent reconstruction of root's NEW NV proof conditional on
the separately accepted CP1, and is not counted as a new nonconstructor
audit of my own old CP1. The acceptance scope explicitly records its two
other initially blind whole reviewers and that its finite q8 computation
was corroboration only. Neither I nor a child reran any old certificate.

## Complete author packet

Read the entire 3446byte main note, entire eleven-obligation JSON and
entire source JSON, plus the 1363byte author manifest. The supplied
hashes/lengths and all four declared author records are independently
fingerprinted in the validation. The author freeze script under
`progress/` is an administrative declared record, not a mathematical
premise: it is hash-checked only and was not executed, edited or imported.

No new external mathematical theorem is cited by NV. Its finite-field
identities, local orders and chain rule are displayed and independently
derived in the report. In particular no Janwa--Wilson, MCM, exceptional
APN, ramification or separability theorem is silently imported. There
is no need to infer F2 reducibility from absolute factorization, and no
such inference is made. The q=4 older criterion is compatibility context
only. No priority or full classification conclusion is asserted.

## Work record and integrity limits

Read commands (independent reads batched, outputs inspected):

```
cat AGENTS.md problems/2024-B4/statement.md
cat problems/2024-B4/notes/coordinator-Kasami-necessary-valuation-v1.md
cat problems/2024-B4/notes/coordinator-Kasami-necessary-valuation-manifest-v1.json
cat problems/2024-B4/notes/coordinator-Kasami-necessary-valuation-obligations-v1.json
cat problems/2024-B4/notes/coordinator-Kasami-necessary-valuation-sources-v1.json
cat problems/2024-B4/proofs/reviewed-composition-Kasami-v1.1.md
cat problems/2024-B4/reviews/composition-Kasami-acceptance.md
cat problems/2024-B4/reviews/composition-Kasami-acceptance.json
cat problems/2021-B4/notes/reasoning-return-r5-freeze-v1.json
```

The official URL above was opened using web.run. A short administrative
Python invocation inspected keys of my own earlier preservation record.
The new review-prefix freeze script only reads/hashes metadata and writes
its own validation/manifest; it contains no mathematical computation.
No scans, CAS, native mathematical child jobs, certificate reruns, peer
new report reads, shared mutations, Git commands, spawning, contact,
charges or access bypass occurred. All earlier own frozen bytes are
verified unchanged through the preceding R5 preservation chain and its
eight artifacts, and the current target/premises are hashed separately.

The complete report is a human reconstruction, not a mechanically
verified proof. Hash matches establish administrative identity only.
Last available direct weekly telemetry at assignment: 34% TOTAL used,
reset1792745187, 90%-TOTAL ceiling with integration/review reserve.
Only the coordinator may reconcile two blind whole reviews and promote
the scoped result. At this freeze no other NV conclusions have been
read, and the separate 2025 task has not been started.
