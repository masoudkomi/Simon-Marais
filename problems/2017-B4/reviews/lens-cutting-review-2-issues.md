# CUT1/CUT2 initial issue ledger, reviewer 2

2026-10-17 UTC. Initially blind nonconstructor whole audit.
Target SHA-256:
1937c12d4cf9c9e2d7b4f713566a77e1b32e1a88ea0c55f09ae7e43870b8482f.
No peer CUT report or finding was read before this ledger and the full
report/source checks were completed and frozen.

No substantive open issue found. The entries below are adversarial concerns
resolved by reconstructing the written hypotheses and proof, not requests
to weaken those hypotheses or unrecorded author repairs.

| ID | Concern | Disposition |
| --- | --- | --- |
| CUT2-R2-01 | Equal meshes might fail kappa ell>=2E; incident sides might choose different corner vertices. | Closed by the explicit N=floor(1/(A sqrt(epsilon))) construction and L0(epsilon) in report section 2. The candidate explicitly reuses each selected corner vertex. |
| CUT2-R2-02 | A DG path could leave the affine region before its confinement can be justified. | Closed: DG2 confinement uses endpoint lifts alone; the entire target neighborhood has the required buffer, including sampling tiles. No affine assumption along an unproved path is needed. |
| CUT2-R2-03 | One-sided distance from a path to a chain might not bound vertical graph error. | Closed: fixed chain slopes give |g(x)-f(x)|<=(1+M)R on the common x-domain. Endpoint-domain discrepancies are confined to the extreme boxes. |
| CUT2-R2-04 | Corner contacts might leave no actual nonempty main Jordan lobe. | Closed: the exact straight gap gives a strict central slab; last initial and first final common vertices are ordered and leave no other contact. Planarity excludes interior edge crossings. |
| CUT2-R2-05 | Mere side bands do not by themselves prove inclusion of the full inner parallel set. | Closed by the fixed-shape distance-to-side and x-extreme estimates in report section 4, with C2 sufficiently large and epsilon sufficiently small. |
| CUT2-R2-06 | Equal projected endpoints need not imply equal ranked content. | Closed: both paths inherit the same canonical full-tiling lift at actual common vertices. No injectivity of V on Z^D is asserted. |
| CUT2-R2-07 | Restricting pseudolines might produce multiple components or negative weak-order crossings. | Closed: exactly two boundary crossings and properness give one lower-to-upper arc; the oriented ij tile tangents have positive determinant. Endpoint alternation gives only ij to ji. |
| CUT2-R2-08 | Discarded cut tiles, arbitrary outside completions or huge rank translations might invalidate the fiber bound. | Closed under the stated input and range conventions: one representative per restriction; finite local alphabet on a deterministic strip with a fixed halo; explicit logarithmic coordinate-range cost outside O(L) boxes. |
| CUT2-R2-09 | An upper recovery-fiber bound might be used as a replacement insertion theorem or a full entropy result. | Not claimed. The candidate explicitly separates the annulus/stratum/recovery interfaces and H. This scope restriction is essential. |

Recommendation: coordinator may resolve this review as having no substantive
objection to the stated conditional CUT1 and upper-fiber CUT2, after completing
the independent second audit and reconciliation. This reviewer does not
promote any result.
