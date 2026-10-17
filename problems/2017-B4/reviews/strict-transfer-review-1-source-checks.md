# Strict-transfer R1: sources and accepted dependency scope

2026-10-17 UTC. Independent initially blind whole audit; no new peer
strict-transfer report or findings were read before this freeze. No
mathematical computation or CAS was run.

## Official problem

Directly opened [official 2017 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-2_1.pdf),
page 2, B4. It asks for growth liminf/limsup of fixed polygon tilings.
The present packet is explicitly a partial fixed-D transfer argument,
not an exact answer or a replacement count for all regular polygons.

## Annulus: complete accepted body and exact scope

Read the full `proofs/reviewed-annulus-v1.2.md`, including A1-A5,
all-color rank-domain repair, translated-frame convention, two-color
winding test, rational fixed-phase frame construction, bounded lobe
accounting, exact block gluing and exclusions. Also read
`reviews/annulus-acceptance.md` and its JSON scope.

Verified accepted SHA-256
`51c02b22a36705c736e4debefcfde0afbc1b2678a8d6092213d8ed00e6a75baf`.
The accepted bytes end exactly with the frozen v1.1 author body named by
ST, SHA-256
`c6da61f229ffa72dd830cd40132969717a395e3744b6d775cbe83a32bdd3747c`.
Thus the input is the repaired all-color A2, not the failed v1 assertion.

Its hypotheses require actual comparable Jordan lenses, a common assigned
lift/affine offset, nesting and the quantitative A3 buffer (or A2's full
rank box and ideals directly). Accepted A5 concerns only the receiving
U,W family and has an all-integer-scale limit. The new construction uses
each of those qualifications; it does not infer arbitrary-window thin
frames merely from A5 or uniformity near zero minors.

## CUT: complete accepted body and exact scope

Read the full `proofs/reviewed-lens-cutting-v1.1.md`, plus
`reviews/lens-cutting-acceptance.md` and the JSON scope. Verified
accepted SHA-256
`81f175e2a0f10665e9228d18885180e91b4db6167001584182d9de4b9cb437fc`.
It ends exactly with ST's frozen CUT body, SHA-256
`1937c12d4cf9c9e2d7b4f713566a77e1b32e1a88ea0c55f09ae7e43870b8482f`.

CUT1 requires a genuine full marked tiling and a whole-neighborhood
near-affine estimate, two fixed common positive directions and positive
epsilon with L>=L0(epsilon). It supplies an actual comparable Jordan
lens with canonical global ranks and the required inner/outer geometry.
CUT2 is an upper fiber-recovery result, including logarithmic coordinate
costs unless ranges are O(L). It is not itself an insertion theorem.
The strict-transfer proof supplies the missing insertion with A2-A3
and verifies the coordinate ranges by one common integer rebase.

## DG and fixed-D lift/background inputs

Read the complete accepted `proofs/reviewed-directed-geodesics-v1.1.md`,
SHA-256 `061ae1749e938aad68f1824ab5f33583a3a1c58e556bd62649309c7cb12da9aa`.
Its disk/full-tiling assumptions and whole-segment DG2 buffer are retained
through CUT1. ST does not apply a plane-arc theorem directly to an
arbitrary inner disk or infer an annulus from DG1 alone. The accepted
exposition attributes its arc method to the original Arroyo et al.
Lemma 2.2 with parallel pairs allowed; no new external theorem is imported
by this composition.

Read the acceptance scope and Sections 1-2 of
`proofs/reviewed-fixedD-structural-v1.2.md`: the integer geometry/marked
dictionary, finite local cell alphabet, assigned integer lift and bounded
coordinate gradients. These are the only fixed-D structural properties
used by ST. The old false prefix-discrepancy envelope consequence, EAI,
profile convexity and the unproved H/PR targets are not premises.

## Proof reconstruction and source boundary

The new interfaces are proved geometrically in the whole report: positive
supporting-line gaps for the same shape, bounded integer rounding,
strict A3 error thresholds, exact relative ranks, variable-boundary coding,
inset-frame insertion, O(eta) normalized profile cost, and scale-limit
quantifiers. No inaccessible external paper supplies any of these steps.
No full free-boundary entropy theorem is assumed. No local slope entropy
continuity or all-scale global reference is imported from a similarly
named result.

One initial batched display was truncated; separate displays covered all
the A4-A5 material and scope before a decision was made. The rank-mesh
packet was not read before this audit froze. Earlier accepted sources
are distinguished from the new initially blind strict-transfer reports.

## Integrity and process

The input-validation record fingerprints the candidate, its freeze,
both named frozen bodies, their accepted counterparts, acceptance scope
files, DG, the fixed-D structural source, AGENTS and the official local
statement. It also verifies all earlier own frozen packets unchanged.
Only the assigned review prefix was written. Python was used for metadata
and hashes only; no mathematical script, enumeration, test table or CAS
was run. No new paper download, source redistribution, paid access,
contact, separately billed API, spawning, shared-file edit or Git operation
occurred. Transition telemetry: 24% total weekly used, reset 1792745187;
cutoff 90% total with reserve.
