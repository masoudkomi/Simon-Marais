# Single-center review 2: source checks and provenance

2026-10-16 UTC. Joint initial audit of the sole-H4 and sole-H2 candidates. Completed before any peer sole-H4, sole-H2, or single-center findings were read.

Requested settings: gpt-6.1-sol / max, unchanged from the coordinator assignment and AGENTS.md. Independent effective-setting readback: unavailable. No model setting is asserted effective from the request alone.

## Official source fidelity

Opened the live [2021 Official Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf). Page 2 confirms a polynomial over \(\mathbb Q\), a common root in \(\mathbb Q\) separately for every derivative order \(1\le k\le d-1\), and the part (b) degree question. Witnesses need not coincide. Both candidates work only in a conditional normalized degree-20 branch of that open target. The preliminary part (a) was not solved or reproduced, and no other problem was investigated.

The existing ignored official cache was hashed read-only:

    .cache/official/2021-paper_b.pdf
    SHA-256 2d507d593500f762e90b041d03a451e884ea33c8769f9a2132427e14d8f926d1

This is a local-cache hash, not a claimed fresh byte-for-byte comparison with the web viewer. No paper was downloaded or copied into tracked files. No new external mathematical theorem or conjecture is invoked by either candidate; their published normalization and Newton sources enter through accepted dependencies.

## Frozen candidates and accepted inputs

Read both candidate files, their freeze records, AGENTS.md, the local statement, the accepted D1/D2 packet, and its named normalization, Newton, and rational-cover dependencies. I also read the existing J15 acceptance JSON for status and fingerprints. I did not read its linked old review reports or any new single-center peer reports. The small-cluster degeneration acceptance register was read for context but is not a new dependency of either residue classification.

| Path | SHA-256 |
|---|---|
| AGENTS.md | 28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff |
| problems/2021-B4/statement.md | 5cd9750a2458191370590120fb4ae7d547740784eb1de38ee9e2e7890a2fabed |
| problems/2021-B4/notes/coordinator-J15-soleH4-candidate-v1.md | 042b15f45a39f6773ec8e5eea6c4294eab5e794e98a961534b899ef2568b508e |
| problems/2021-B4/notes/coordinator-J15-soleH4-freeze-v1.json | dc50056b31fc1f0b34a93978d0dd52ea097e7d44a88305b30b6f837d75f89bbd |
| problems/2021-B4/notes/coordinator-J15-soleH2-candidate-v1.md | a21d53ab434ea715b85cca9bcf98c715a1522f4faa33d1977c1ad9411b7f9d39 |
| problems/2021-B4/notes/coordinator-J15-soleH2-freeze-v1.json | d3506b8d8cf735f66d9219a830a60c8e8fed3475b946bc01c34cb4fa7af28cfb |
| problems/2021-B4/proofs/reviewed-reasoning-J15-v1.1.md | fbc5d212b5b560c8e4e42397d19663f3fc882fa8f206bdcbb4ed897c715627f6 |
| problems/2021-B4/reviews/reasoning-J15-acceptance.json | c69ca02744dbb4066dd62db5adb471920ab6a3660ed482818ddf956e619a0465 |
| problems/2021-B4/notes/rational-witness-p-plus-one-reviewed-v1.2.md | fa71a4269a061b09ed74b3cd333b62c2ed7d3ffd39d1c28624a58a6d8fc18d09 |
| problems/2021-B4/notes/padic-rational-newton-reviewed-v1.1.md | 691c7c04be6b7d63b528724a59f43636e0e71dd2135f7c0d14e25487f738e963 |
| problems/2021-B4/notes/padic-rational-newton-obstructions-v1.md | ce3ff564b48841ae3ae1bf66c3cf5303ed2833c2166590cb2460706f01b5c335 |
| problems/2021-B4/notes/coordinator-three-rational-witnesses-reviewed-v1.1.md | 7ff6b3d92d3268405381c2732d83516d21e6eb7d74e897d4c01ec8bb70342be4 |
| problems/2021-B4/notes/coordinator-newton-degeneration-reviewed-v1.1.md | 11c49a9084c5257476d3278b5e05054916a05d4315973cda0205850372d85aeb |

The sole-H4 freeze records the 6778-byte candidate, the accepted 18931-byte J15 packet, and its acceptance JSON; all stated hashes match. The sole-H2 freeze records its 5784-byte candidate and identifies the same accepted J15 packet; its candidate hash matches. Earlier accepted dependencies remain inputs in their stated scopes; this review is not a new audit of their unrelated large finite certificates.

## Exact reconstruction, commands, and limits

All new mathematical checks were performed by hand: Hasse differentiation, explicit integral rescaling, the three sole-H4 witness branches, the four sole-H2 branches, discriminants, factorizations, and actual-slot identification. The full report displays all needed calculations, including the nonsquares 2,13,18, and the derivative double-root cases. No residue-table enumeration or CAS result is a premise.

Read commands used cat, sed, rg --files, nl -ba, ls -ld, and shasum -a 256 on the named files. Public source access used the web open tool for the official paper. Files were written only with the assigned single-center-review-2 prefix. Python is used only for the output hash manifest and byte-integrity checks; no mathematical search or numerical approximation was run. No Git operations, native CAS jobs, separately billed APIs, or new agents were launched by this reviewer.

The coordinator-supplied authoritative weekly usage was 17% total at 2026-10-16 22:11 UTC, reset Unix 1792745187; the same 90%-total ceiling and reserve apply. This short audit remains in that reported window. No substitute per-task usage is inferred.
