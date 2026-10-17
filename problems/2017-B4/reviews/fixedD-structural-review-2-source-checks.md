# Fixed-D structural review 2: source checks and provenance

2026-10-17 UTC. Blind initial whole review. Requested settings gpt-6.1-sol / max; independent effective-setting readback unavailable. No peer fixed-D structural reports, issues, or conclusions were read before the initial freeze.

## Primary checks

[Official Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-2_1.pdf), p.2: checked the full n-at-least-two target, fixed regular polygon, unit sides, and both requested normalized limits. [Official notes](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-solutions-preliminary_1.pdf), p.12: checked A006245 and the terms \(C(3)=2,C(4)=8\) supporting the established marked/oriented convention. No other contest problem was investigated.

[Felsner--Valtr, author PDF](https://page.math.tu-berlin.de/~felsner/Paper/new-pla.pdf), Section 1: checked the marked north-cell convention, orientation-preserving identification, local crossing orders, wiring diagrams, and the zonotopal dual representation. This supports the attributed dictionary; the packet separately explains its repeated-color integer deformation. Historical asymptotic constants in that source are not used as new conclusions.

[Balister--Bollobas--Quas, author manuscript](https://web.uvic.ca/~aquas/papers/paper15.pdf), definitions and Theorems A--B, PDF pp.2--4: N(Lambda) counts restrictions of points of an infinite subshift. Theorem A concerns convex sets with growing inradius. Strong irreducibility requires a uniform filling distance for separated restrictions; Theorem B assumes it. The packet establishes neither that filling property nor transfer to one fixed lifted zonogon boundary. Its source warning is correct.

These sources were read through the public web PDF viewer. No new full PDF was downloaded, and no raw retrieval-byte hash is supplied by that viewer. Existing official caches were hashed read-only; no fresh byte-for-byte identity with the viewer is claimed.

## Frozen input fingerprints

| Path | SHA-256 |
|---|---|
| AGENTS.md | 28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff |
| problems/2017-B4/statement.md | e459750064b4e25e3eaa71f25f236c046548147e415b06d8bd097839020228f3 |
| problems/2017-B4/notes/fixedD-reasoning-r1-structural-candidate-v1.md | c776e81d0fd44c0e8042ddc00a0d949966cdc106ba9b7e67486dc4d14a1b7d87 |
| problems/2017-B4/notes/fixedD-reasoning-r1-profile-reduction-v1.md | 973e8d7da034082b4416100d51650798ec3eb90e75cfd44106b5810dd9ec7e8d |
| problems/2017-B4/notes/fixedD-reasoning-r1-freeze-v1.json | fb277c1a3fe5fe3a0283992168b009094d05699c1f47d7ba10123b61e95eb6dd |
| problems/2017-B4/notes/fixedD-reasoning-r1-sources-v1.json | e33ef844964e5cdfa0420696c2ee08ab90600ac766b9d7aa3667e8776c7ac3c0 |
| .cache/official/2017-paper_b.pdf | 69d7cf84128c2464d962136ed613808b6c7a7b07122cfba9c06b5adf775e2a68 |
| .cache/official/2017-solutions.pdf | c272a72239ef4c2ccd54df0702140179e0a9b85f5a9028c87d485841eb1a2c12 |

All three artifacts listed in the constructor freeze match their hashes and byte sizes. The source JSON points to an older coarsening review source record; I did not read that review or its peer findings. Its pointer is provenance, not a theorem newly audited here.

## Mathematical and operational boundary

The review reconstructs every candidate structural argument and the compact-profile lemma. It supplies one exact analytic counterexample family to the unqualified prefix-height padding consequence. The family is proved for every integer \(M\ge2\) by its explicit inversion sets; there is no enumeration, CAS, search box, or numerical evidence premise.

Read commands used cat, nl -ba, rg --files, and shasum -a 256. Public source checks used web open/find. Files were written only with the assigned fixedD-structural-review-2 prefix. Python is used only for output hashes, preservation checks, and the freeze manifest. No candidate/shared edits, Git operation, agent, native long-running job, paid API, or third-party PDF redistribution was used.

Coordinator telemetry supplied at assignment: 18% total weekly used at 2026-10-17 00:00 UTC. Fresh authoritative telemetry at 00:26:37 UTC returned 19%, the same 10080-minute window and reset 1792745187. The 90%-total ceiling and reserve remain in force. No per-task usage substitute or account identifiers are recorded.
