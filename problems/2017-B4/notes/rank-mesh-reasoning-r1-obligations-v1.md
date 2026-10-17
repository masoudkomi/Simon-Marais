# Rank-mesh construction: failed routes, exact scope and review obligations

2026-10-17 UTC. **Candidate proof - unverified.** This is the author's
checkpoint, not an independent audit or acceptance. Requested
`gpt-6.1-sol` / `max`; effective readback unavailable. No computations,
enumeration, CAS or index scans were used to support the mathematics.

The complete candidate has RM1/RM1a, scoped RM2/RM2a and RM3. The
companion UR3 note proposes LC3 and UR3-GE. Both must have two fresh
independent nonconstructor whole reconstructions before coordinator
promotion. The author did not audit the coordinator's FL1/CL1/OB1 as
an independent reviewer and must not be counted as one.

## Rejected shortcuts and their explicit replacements

1. A selected midpoint-curve cell is not by definition an original
   tile-boundary disk. The candidate removes whole selected ribbons,
   builds the remaining tile edge graph, rules out unfilled bounded
   faces using a selected-arc escape path, and splits into biconnected
   tile blocks. Vertex pinches are handled by that construction.
2. One selected face can give several blocks. The correct bound is
   an aggregate perimeter <=2D(r-1), not one error per nominal face.
   Small blocks are discarded by isoperimetry; only O(1/delta) substantial
   blocks then remain per face for the UR3 error sum.
3. Recording the location of every selected tile independently would
   introduce unwanted logarithmic coordinate factors. Selected full
   arcs start at fixed boundary ranks; their other-color crossing words
   recover both geometry and lifts with a finite alphabet. The bad-face
   mask costs one bit per face, and the bad-region filling is encoded
   only after its domain is known.
4. The coordinator's OB1 invalidates arbitrary local coarse insertion
   after even one erased event. A good closed face in RM2 avoids all
   incident forbidden tiles. The global limiting deformation has
   connected fibers and is locally a homeomorphism around its good
   disk, which makes the full coarse boundary an embedding.
5. Fine two-port data alone are not declared to imply coarse two-port
   data. The special D4 proof uses one merged pair and two singleton
   groups. A coarse merged curve cannot restore a selected singleton
   sign after an exit. With several nonsingleton groups that argument
   fails and is not asserted.
6. A diameter/perimeter bound does not make varying normalized disk
   boundaries a compact family of simple curves. Thin necks can collapse
   or boundaries can retrace in a limit. UR3-GE instead uses compact
   ambient scalar heights and compares actual nearly planar triangular
   cores. It imports no smooth limit theorem for the ragged disks.
7. Pointwise convergence of dilated counts for each B does not give
   the uniform additive o(r^2) finite-to-dilated comparison. The proposed
   contradiction fixes a limiting profile, records subquadratic mesh
   boundary data, and compares finite and dilated cores to the same
   local entropy. All orders of limits are stated.
8. The exact inequality Z(MB)>=Z(B)^(M^2) is neither proved nor used.
   Dilating one reference supplies the exterior, while the inserted
   entropy comes from the independently counted dilated cores.
9. A mesh geometry code alone does not necessarily fix scalar-height
   phases on every cut. The UR proof also records their actual integer
   values, at subquadratic cost, before it counts core fibers.

## Critical fresh-audit targets

| Target | Exact inference requiring audit |
|---|---|
| RM1-T | No unfilled bounded face of the residual graph; biconnected block is a filled Jordan disk; zero-area and boundary cases. |
| RM1-P | Every unselected arc has one consecutive residual chain, exactly two ports, and belongs to one block; aggregate perimeter rather than a per-component assumption. |
| RM1-C | Crossing-word skeleton recovers coordinates and ranks; bad tiles touch at most four selected faces; bad-region conditional encoding has the claimed size. |
| RM2-G | Positive full-zonogon deformations are homeomorphisms; the convex-preimage argument proves connected limit fibers; forbidden-free full stars give local homeomorphism. |
| RM2-P | The D4 singleton-barrier argument rules out a second coarse visit; zero rows and the two-direction case retain their exact restricted scope. |
| RM2-L | Coarse ports fix fine identities; integration and positive boundary degree give an actual fine tiling; integer dilation retains these data. |
| RM3-A | Deleting inactive tracks translates the disk without changing its interior; every filling extends to an O(r)-strand full three-direction frame. |
| LC3-S | The original theorem4.3 has the fixed-tolerance, sufficiently-large-scale uniformity used over all approximating Q; its printed lozenge adaptation and entropy units really supply the needed estimate. |
| LC3-U | The fixed-exterior profile cover gives the total-count upper bound; compact affine slopes include frozen cases with no division by a vanishing minor. |
| UR3-C | The actual cut-core is Jordan and contains a fixed inset; cut geometry and height codes fix every complete boundary. |
| UR3-Q | Limit profile slopes are admissible on retained triangles; the subquadratic fiber losses, boundary tube and failed-flatness area have the stated uniform bounds. |
| UR3-D | Fine integer dilation gives exact exteriors for all independent coarse cores; the liminf in M is taken after each fixed r. |

LC3 is an explicit source-import obligation, with a proposed derivation.
If that derivation fails, UR3-GE remains conditional on LC3. The packet
does not replace it by a generic free-boundary entropy theorem or by
balanced-hexagon counts. All other new assertions are also unverified
until the independent audits complete.

## Remaining global work

The supplied count S is not derived from affine closeness in this packet.
That is the coordinator's separate FL1 candidate. Antiparallel row
orientation, consecutive positive grouping in every relevant stratum,
the macroscopic profile partition and its total window-boundary cost,
the strict-slope route, the global original-frame assembly, and all-scale
balanced remainder padding remain outside this checkpoint. No separate
candidate was promoted merely because the coordinator mentioned it.

UR3-GE addresses the exact globally extendable class proved relevant to
these rank cells. It is not a claim for every conceivable locally tileable
disk with no compatible small full exterior. It concerns three directions,
not an all-D induction theorem. The official 2017 liminf and limsup
remain uncomputed and H remains open in this packet.
