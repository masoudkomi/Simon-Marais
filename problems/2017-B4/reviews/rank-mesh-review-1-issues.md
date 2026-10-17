# Rank-mesh/UR3 R1: whole initial issue ledger

2026-10-17 UTC. Initially blind independent whole audit of main candidate
SHA-256 `e0f2e55e62aabe5547120f4fc72c506c3f680844a90aa98ece7147d404178d27`
and supplement SHA-256
`40ad9b252b6c34f5dee5c8cd3eedea8e8feeabb0cec1497b224bf5c32ba58aab`.

## RMR1-01: missing boundary-component hypothesis in the window helper

**Severity:** substantive for the standalone stated window extension.
**Location:** main candidate lines 173-178.
**Status:** open; author versioned repair required before accepting this
helper in its current domain. The RM1 disk theorem, scoped RM2 and
UR3-GE Jordan-disk argument are not contradicted by it.

The assertion uses perimeter O(L) for a rectifiable window to bound its
r-boundary tube and all touching selected faces by O_D(rL+r^2). A single
connected window may have many boundary components. Perimeter alone
does not imply this tube estimate.

Exact hand counterexample: use the D=2 full grid of content (L,L), L
even, and fix r=2. There are Theta(L^2) interior selected cells containing
one unselected odd/odd tile apiece. In each, remove a disjoint round hole
of radius L^-3 centered in that residual tile. The connected perforated
window has outer perimeter 2L(1+sqrt(2)) and total hole perimeter O(1/L),
hence perimeter O(L). Every interior selected face touches one of its
hole boundaries. The prescribed discard therefore removes Theta(L^2)
residual tiles, whereas the proposed bound at this fixed r is O(L).
This also refutes the claimed lower-order conclusion at fixed r.

Suggested scope repair, not implemented by this reviewer: require a
Jordan window/one connected rectifiable boundary curve, or retain the
number b of boundary curves and use O_D(rP+b r^2), where P is total
perimeter. Repeated windows must still have their actual boundary costs
summed. If “window” was intended to mean Jordan, make that explicit.
The counterexample and frozen original should remain preserved.

## N1: finite alphabet wording (editorial)

Main line 155 says “six” types within an RM1a argument stated for fixed
general D. Use binom(D,2) types, or explicitly specialize that sentence
to D4. The O_D estimate and its proof survive this correction.

## Complete claim audit

| ID | Claim / inference | Disposition |
|---|---|---|
| RMR1-02 | Full arrangement and selected-cell disks | Pass. Proper arcs and single crossings are explicit full-zonogon hypotheses; sign restoration rules out a second cell visit, and successive cuts give disks. |
| RMR1-03 | Rank gaps and physical diameter | Pass. Each color contributes at most r-1 unselected arcs; continuous heights have range at most r, including tails and absent selected colors. |
| RMR1-04 | Residual graph has no unfilled bounded face | Pass. A non-residual neighbor is a skeleton tile; its selected arc escapes to the exterior without crossing the residual graph. |
| RMR1-05 | Biconnected tile blocks are Jordan disks | Pass. Simple block boundary and absence of non-tile bounded faces rule out holes; cut vertices are split without splitting any tile cycle. |
| RMR1-06 | Single residual chain and aggregate ports | Pass. Only entry/exit crossing tiles can be selected; the middle chain lies in one block. Every boundary edge is a port, giving aggregate perimeter <=2n_F, not one such allowance per block. |
| RMR1-07 | Tile count and small/boundary cases | Pass. Each residual tile is one distinct pair crossing, so total <=binom(n_F,2). Empty residuals and original-boundary tails are covered under the actual disk input. |
| RMR1-08 | Skeleton count and decoding | Pass. Fixed ranked endpoints and other-color words recover signed midpoint displacements, actual origins and all rank lifts with a finite alphabet. |
| RMR1-09 | Four-face rare-tile bound and conditional loss | Pass. Selected arcs never pass vertices or run along edges; whole-tile closure meets at most four sectors. Fixed domains and reference neighborhoods give the claimed exponential bad-region code. N1 affects wording only. |
| RMR1-10 | Fixed good-disk boundaries and independent filling | Pass. Fixed skeleton geometry fixes residual domains and ports; a new selected-level track would have to close internally. Zero minor flux preserves absence of the designated types when invoked. |
| RMR1-11 | Additional arbitrary rectifiable-window loss | Fails in written generality; see RMR1-01. A Jordan or component-count condition is required. |
| RMR1-12 | Positive global deformation before merging | Pass. Ordered directions, positive tile orientation, cyclic fans and degree-one boundary give a homeomorphism of full disks. |
| RMR1-13 | Connected limit fibers | Pass. Convex-target preimages are compact connected supersets of the fiber; uniform convergence identifies their Hausdorff limit with exactly that fiber. |
| RMR1-14 | Closed clean stars and disk embedding | Pass. All incident within-group tiles are excluded; repeated group rays would need one. A fiber meeting the local homeomorphism point is a singleton. Boundary vertices are included. |
| RMR1-15 | Actual full coarse tiling at the limit | Pass. Positive overlaps would persist before degeneration, collapsed faces cannot enter positive interiors, and primitive integer edges exclude hidden subdivisions. |
| RMR1-16 | D4 one-pair/two-singleton two-port theorem | Pass in exactly this scope. Any exit must cross a fixed singleton barrier; a second visit would require a second crossing of that same coarse curve. No general several-merged-groups claim is inferred. |
| RMR1-17 | Exact lifting and reverse count equality | Pass. Boundary ports assign fine identities; closed edge increments integrate over the disk; positive degree yields a fine tiling. Zero boundary minor flux excludes all forbidden pair tiles in every fine filling. |
| RMR1-18 | Integer-dilated ports and exact exteriors | Pass. Consecutive multiplied rank levels inherit the same fine colors, and reference dilation supplies the unchanged full exterior. No product-squared entropy inequality is assumed. |
| RMR1-19 | Zero-row and two-group endpoints | Pass with stated compatible positive orientation. Zero tracks act by a constant translation; the two-group grid has boundary-determined straight fine segments and a unique compatible filling. Antiparallel reduction remains open. |
| RMR1-20 | GE3 small full exterior | Pass. Inactive curves have constant side contribution on the connected disk; deleting them translates it and leaves only O(r) active curves. Positive three-direction deformation preserves the count. |
| RMR1-21 | Per-face component aggregation | Pass. Aggregate perimeter plus isoperimetry controls small blocks; large blocks are O(1/delta). The error is sqrt(delta)+eta/delta, not one per selected cell. |
| RMR1-22 | LC3 exact primary theorem and lozenge extension | Pass as a published input with the explicit uniform extraction reconstructed in the full report. No varying ragged limiting domain is substituted into the primary theorem. |
| RMR1-23 | LC3 refined from-within metric and omitted area | Pass. The inset and convex-triangle Lipschitz bound verify restrictions of every admissible target height; missing area is O(tau). |
| RMR1-24 | LC3 total upper count and affine uniformity | Pass. Fixed-exterior compactness, finite target-profile cover, Jensen's inequality and a finite affine-parameter cover give common constants; frozen slopes use continuity. |
| RMR1-25 | Scalar compactness and profile cover | Pass. Full convex exteriors give global Lipschitz bounds; ordinary extensions outside are used only for compactness. The gamma_j profile code is subquadratic. |
| RMR1-26 | Actual triangular core, no holes and boundary code | Pass. The fixed inset lies in one residual block; removed tiles escape through the triangle boundary. Band geometry and recorded heights fix every complete core boundary. |
| RMR1-27 | Admissible planes on retained triangles | Pass with the standard tangent-plane construction explained in the report. Good differentiability points in a retained triangle have gradient in P; local height recentering keeps constants uniformly bounded. |
| RMR1-28 | UR3 boundary and discarded-region losses | Pass for expressly Jordan B_j. The connected-curve tube estimate is valid here; matching choices give the 3^A bound even when the discarded region is disconnected. |
| RMR1-29 | U3-U5 and order of limits | Pass. Largest fibers pay subquadratic codes; dilated core insertions are independent and exact. M tends to infinity with j fixed before the final compactness contradiction. |
| RMR1-30 | Uniform deficit tends to zero | Pass within GE3. A positive normalized-deficit sequence contradicts the fixed-mesh upper/lower entropy comparisons; finiteness at fixed r alone is not used. |
| RMR1-31 | Global and source boundaries | Pass. Rare-count S is input; chart/orientation, macroscopic profile assembly, balanced remainder scales, H and exact official values remain outside the theorem. |

## Required disposition

Preserve this blind initial report and the original candidate. Obtain an
author's full versioned repair for RMR1-01 and both independent affected
re-audits before accepting the whole packet. The coordinator may separately
consider scoped unaffected claims after the other whole audit, but this
reviewer does not promote them. No peer conclusions were read before freeze.
