# R2 recovery checkpoint

Written on recovery, 2026-10-16 UTC (local date 2026-10-17). This is this reviewer's own blind checkpoint, not another reviewer's conclusions. The original assignment and write ownership persist.

## Findings already reconstructed

- Frozen target `proofs/partial-v1.md` was checked at SHA-256 `f53945e49bd626847e52a61f7e39e96defd2ae44900f9d235c2c14e720f41525`.
- Official B4(b) asks which integers n >= 2 are taut for a regular polygon with n^2-n+1 vertices. The statement was checked in the official PDF text and a locally rendered B4 crop. No preliminary construction or proof was reproduced.
- P1 reconstructs: monotone chord lengths correspond to signed cyclic differences, with v odd and k(k-1)=v-1; n=2 is correctly retained separately.
- P2 reconstructs both directions for q >= 2, provided the reverse action is by collineations, as the candidate explicitly clarifies. The quadrangle count v-3q=(q-1)^2>0 is valid. The line-stabilizer argument uses gcd(q+1,v)=1. No arbitrary-plane or Desarguesian converse is assumed.
- P3 reconstructs: translation to include 0,1 is existence-complete, not an equivalence-class transversal; sum-zero translation is unique because gcd(k,v)=1 and fixes every numerical multiplier. Gordon (1994), Theorem 2, was independently retrieved and visually inspected: divisors of the difference-set order are numerical multipliers in the planar abelian case. In the more general prime form p>lambda is automatic here, and p does not divide v.
- P4 reconstructs by ordered-pair counting including the k diagonal pairs in the zero quotient class; d=1 and d=v cause no exception. The character identity uses every nontrivial vth root, not just primitive roots.
- P5 reconstructs the norm identity and inert-prime even-valuation argument, including p=2 and x=0 or y=0. The implication q=10 mod 12 is valid and the condition is necessary only.
- P6 reconstructs stratum orbit sizes via units modulo d. It includes d=1, the singleton zero orbit, and bounded multiplicities. Passing the subset sum does not prove existence.
- Square descent is stated exactly in the independently retrieved Gordon (1994), Theorem 6, and the 3-divisibility restriction exactly in Theorem 8. The candidate's abelian/cyclic use is within this scope. The resulting order 48 has 3 dividing it exactly once and is not 3, so 2304=48^2 is excluded under these published imports.
- The source-access limit is explicit: original Jungnickel-Vedder and Wilbrink full PDFs returned HTTP 403 at the publisher, not a missing theorem. Their primary publisher abstracts were returned by web search; Gordon's complete theorem statements were retrieved and visually checked. Original proofs were not audited.
- Ancillary Gordon small-lambda preprint v1 Theorem 3 was read through web extraction. Its literal word 'positive' for orbit counts must not be used to discard b=0; the author's nonnegative implementation is a safe correction, with ord_1(m)=1 and o<=1 skipped. This does not produce a defect in frozen P1-P6.

## Saved finite evidence

The independent standard-library child `initial-review-2-check.py` completed successfully, preserving incremental stdout and JSON evidence. The runner used an explicit 90-second subprocess timeout, recorded child PID 38854, and reaped it with exit 0. Parent independently reported completion at 16:07:21 UTC in about 1.107 seconds; the saved job is authoritative for exact timing. No new computation is needed.

Checks include coprimality for q=1..5000; 240 quotient contraction cases; 581528 residue pairs for primes 2 mod 3 through 257; the norm valuation box [-50,50]^2; 67 occupancy/norm cases q=1 mod 3 through 199; direct orbits for 85 odd moduli 3..171; independent residual orbit histograms and plain-set subset sums at q=1944,2304,2435; and ancillary nonnegative Arasu diagnostics. All passed. These are finite evidence, not an unrestricted proof.

## Exact interrupted operation

- Optional render command (unified exec session 86629): `pdftoppm -f 1 -l 3 -scale-to 1400 -png .cache/literature/2020/initial-review-2/gordon-small-lambda-v1.pdf .cache/literature/2020/initial-review-2/gordon-small-lambda-v1 && pdftoppm -f 6 -l 7 -scale-to 1400 -png .cache/literature/2020/initial-review-2/alexeev-mixon-v2.pdf .cache/literature/2020/initial-review-2/alexeev-mixon-v2`.
- It repeatedly emitted Fontconfig errors about unavailable writable caches. Two output calls returned it still running. No successful completion is asserted.
- A sandboxed `ps -eo pid,ppid,command | rg 'pdftoppm.*initial-review-2|[p]dftoppm -f 1 -l 3'` failed with `operation not permitted: ps`.
- The required escalated retry of that exact read-only process query was pending, then returned `aborted by user after 2340.2s`; it supplied no PID or process result. The render child PID is therefore unknown. The parent interrupted the review to release the stalled call. No cleanup or termination of that renderer is asserted.
- The already successful official crop and Gordon (1994) pages 2-3 renders remain sufficient for the central source checks. Optional render failure does not alter the arithmetic job, which had already completed.

## Remaining work

Finish the analytic reconstruction report, issue dispositions and provenance/hash manifest using the sources already retrieved. Recheck the target hash, retain the distinction between audited theorem statements and unaudited imported proofs, and freeze the report without reading any peer review or shared status. No further full-text chase or new arithmetic run is required.

Requested launch: gpt-6.1-sol/max. Verified effective-setting readback: unavailable. Latest parent-reported account-wide weekly usage: 11%, same reset 1792745187; 90% cutoff with reserve remains in force.

## Recovery follow-up before freeze

At 16:48:33 UTC the authoritative usage tool reported 12% total weekly used with the same reset. Own cache inventory showed that the optional Gordon small-lambda and Alexeev-Mixon PNGs had been written around 16:07-16:08 UTC. The relevant existing pages were then visually inspected successfully; no new rendering job was launched. Their presence is not a returned renderer exit status. The coordinator reported that a targeted Ctrl-C attempt on tool session 86629 returned `Unknown process id 86629`: no active tool session was found, but OS-process cleanup was not independently verified. The final report preserves that distinction, the original access limitations, the full reconstruction, and the successful bounded finite evidence.
