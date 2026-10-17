# Reviewed rank mesh, scoped clean lifting and block aggregation

**Proved, independently reviewed partial results**, 2026-10-17 UTC.
Accepts FULL author-repaired main v1.1 after both initially blind WHOLE
audits, substantive author repair, BOTH affected targeted reaudits and
complete coordinator reconciliation. Original v1's perimeter-only window
assertion is false; both exact hole counterexamples remain preserved.
Only the repaired one-rectifiable-Jordan-boundary tube estimate and
actual r sum P_j+M r² window cost are accepted. General-D alphabet
N1 is corrected. Both full original reports, ledgers, sources, full
repair and both full targeted packets were read and integrity checked.

RM1's disks/ports and global-content skeleton code, special clean
D4 one-pair/two-singleton lifting, zero-row/two-group endpoints,
actual GE3 exterior and aggregate block-error interface retain ALL
stated hypotheses. The separate reviewed UR3-GE copy supplies its
precise three-direction recovery input. No general-D one-pair
extension, local-window mesh code, uniform-strict, global H/PR
or official limit is imported or proved here. Novelty unestablished.

The FULL repaired main follows as a byte-identical suffix. Historical
candidate/source-status labels describe its pre-acceptance history.

---

# Rank cells as actual disks, with a scoped clean D4 lifting theorem

2026-10-17 UTC, full author repair v1.1. **Candidate proof - unverified.** Constructor
`review_2017_coarsening_r1`; requested `gpt-6.1-sol` / `max`, effective
readback unavailable. Two fresh independent nonconstructor whole audits
are required. No full balanced-zonogon (H), full 2017 solution, or novelty
is claimed. No mathematical computation, enumeration or CAS was used.

Version1.1 repairs RMR1-01/RM2-01 by restricting the auxiliary
window estimate to one rectifiable Jordan boundary and recording the
actual sum for multiple such windows. It also corrects N1's general-D
tile alphabet. No other result or new extension is introduced. The
complete v1 and unchanged UR3 supplement remain frozen; both affected
independent reaudits and coordinator resolution are still required.

This is a construction checkpoint. The coordinator's rank-mesh program
and its FL1/CL1/OB1 packet were read as unverified leads. FL1's bound
on rare events is not assumed proved here: the bounds below take the
number S of designated rare tiles as an input. The exact OB1 obstruction
motivates retaining every rank and forbidding rare tiles near a good cell.
No annulus, CUT, strict-transfer or remainder-padding candidate is a
premise of this packet.

## 0. Full arrangement and the exact mesh

Fix D and v_i=(1,i-1), with V having these columns. Start with an
actual full marked tiling of the zonogon of content N, 0<=N_i<=cL.
The outer words are ascending color blocks and their block reversal.
Use its canonical continuous affine-on-tiles lift a, with Va(x)=x.
The marked arrangement dictionary gives one proper de Bruijn arc
gamma_(i,k) for each color i and rank1<=k<=N_i. It is the level
a_i=k-1/2, passing through opposite color-i edge midpoints in every
incident tile. Same-color arcs do not cross. Distinct-color arcs cross
exactly once, at the center of their shared tile. No three arcs meet.
These are the full-zonogon hypotheses; an arbitrary incomplete wiring
window is not silently substituted.

Choose integer r>=2 and select precisely the arcs with k divisible by
r in each color. Let m be their total number, and let F range over
the cells of this selected arrangement in the closed outer disk. The
selected tile skeleton S_mesh is the union of all whole tiles crossed
by at least one selected arc. Keep the full physical tiles and their
rank lifts, not only midpoint curves.

Every selected cell is a disk at the curve-arrangement level. One way
to check this is to add the proper arcs successively. A new arc cannot
leave and revisit an earlier cell: doing so would have to restore a
previously changed separating-arc sign, requiring a second crossing
of that arc. It therefore cuts each cell in at most one proper arc.
Starting from the outer disk, each such cut splits a disk into disks.
Euler counting gives at most 1+m+binom(m,2) cells. This curve-level
observation alone is not asserted to give tile-boundary disk patches.

## RM1. Whole tiles and the correct disk decomposition

For one selected cell F, let K_F be the union of all closed tiles not
in S_mesh whose interiors lie in F, together with their edges and
vertices. An unselected tile cannot be cut by a selected arc, so its
whole closed tile is in the closure of the same cell. Let G_F be its
finite embedded edge graph. Split G_F into its biconnected blocks
containing tile cycles. Each tile's four-cycle lies in exactly one
block. These blocks, filled by their tile faces, are the patches used
below. Blocks can meet at cut vertices; they are counted separately.
An empty K_F supplies no patch.

**Claim RM1.** Each such filled block is a Jordan tile disk. If n_F
is the number of unselected full arcs meeting F, then

    n_F<=D(r-1),
    sum_(blocks B in F) number_of_boundary_edges(B)<=2 n_F,
    total_tiles(K_F)<=binom(n_F,2),
    diameter(F)<=r sum_i ||v_i||.                         (M1)

Every residual full arc meeting one block has exactly two boundary
edge ports and is one consecutive tile chain there. No rank pairing
or boundary strip thickening remains unspecified.

Here are the topological details, including possible pinches. A bounded
face of G_F that is not an original tile face would have a boundary
edge with a non-K_F tile on its other side. That neighboring tile
must be in S_mesh. Otherwise the two unselected tiles share an edge,
are not separated by a selected arc, and belong to the same K_F.
The neighboring skeleton tile's center lies on a selected arc. Follow
that selected arc to the original outer boundary. It never meets G_F:
the arc only traverses skeleton tiles, crosses their selected-color
edges into other skeleton tiles, and never visits a tile vertex.
It would give a path from the bounded face to the exterior without
crossing its boundary, a contradiction. Thus every bounded face of
G_F is exactly an original tile face.

A biconnected embedded plane graph has a simple outer-face boundary:
a repeated vertex on its outer boundary would be a cut vertex separating
the incident boundary sectors. A block here has no unfilled bounded
face. Such a face would either be one of the already excluded holes
of G_F or contain another block hanging into an original tile face,
which a geometric tiling does not permit. Consequently its simple
outer cycle encloses precisely its own tile faces. This gives an
actual Jordan disk, rather than assuming that edge connectivity by
itself removes a vertex pinch. Splitting at cut vertices duplicates
no edge; a tile cycle cannot be split between blocks. In fact two
tile cycles sharing an edge lie in the same block.

To check the perimeter and ports, follow an unselected full arc gamma
through F. It meets F in at most one arc by the same separating-sign
argument. A tile on this arc belongs to S_mesh exactly when its other
crossing arc is selected. Those can only be its entry and exit tiles
at the selected-cell boundary. All intervening crossing tiles are
therefore a consecutive chain in K_F, sharing the opposite edges of
gamma's color. Their tile cycles belong to one block. If the chain
is nonempty, only its first and last such edges are boundary edges;
these are exactly its two ports. A chain starting at the original
outer boundary has the same two-port description. Every boundary edge
belongs to such an unselected arc; a selected-rank edge cannot adjoin
an unselected tile. Summing gives the aggregate bound2 n_F across
all blocks, not an additional bound for each independent component.

Between successive selected arcs of any color there are at most r-1
unselected arcs. The same bound holds in the initial and final tails.
Thus n_F<=D(r-1). A tile of K_F is a crossing of two of these arcs,
and each pair crosses at most once, proving the tile bound. Throughout
F every a_i lies between consecutive selected half-integer levels, or
an endpoint and the nearest such level. Its range has length at most r.
Using x=Va(x) gives the stated physical diameter, even for an original
boundary cell. Both metric and word perimeters are therefore controlled
by constants depending only on D,c. Boundary and degenerate small
cells are included in RM1.

## RM1a. A skeleton code and a rare-cell loss bound

There are O_D,c(L/r) selected arcs. A selected color-i arc crosses
exactly sum_(j!=i)N_j other arcs, hence at most O_D,c(L) tiles.
The skeleton contains O_D,c(L^2/r+L) tiles.

Its possible geometry and lifts have a code of that same order in
bits. Order selected arcs by their predetermined color/rank. Their
initial boundary edges are fixed by N and those labels. Traverse an
i arc in the direction in which the normal to v_i increases, and
record just the other color j at each crossing. The next midpoint
is displaced by +v_j for j>i and by -v_j for j<i, so the tile and
next midpoint are recovered. The crossing word length is known from
N. The current rank of color j is also recovered: it starts at0 or
N_j at the fixed endpoint and changes by one at each recorded j.
Thus this code records actual whole tiles, their positions and all
rank lifts with a fixed finite alphabet. It does not assign an
independent O(log L)-bit coordinate to each tile or lose a matching
factor. Repeated recording of selected/selected tiles is harmless.

Designate any set of S rare tiles. Mark a selected face bad whenever
its closure meets one of those whole tiles. A tile contains at most
two selected arcs, so it meets at most four selected faces. There are
therefore at most4S bad faces. Discard the skeleton and every remaining
tile in a bad face. By RM1 the latter loss is O_D(Sr^2) tiles.

Conditioning on this information costs

    O_D,c(L^2/r + S r^2 + L + 1) bits.                    (M2)

For clarity, this is an encoding statement. The skeleton code determines
the selected geometry and all complement domains. Record one bad/not-bad
bit per selected face, costing O(L^2/r^2+L/r+1), even if S=0.
The union of bad complement domains has O_D(Sr^2) tiles in its given
filling. In any fixed tileable integer domain, the binom(D,2) finite tile types
and their possible origins in the domain plus a bounded boundary tube
give at most an exponential number in its area of fillings. The boundary
tube has that same order: a reference filling bounds its perimeter and
component count by a constant times its number of tiles. Recording a
tile-presence bitmask in those known locations therefore costs O_D(Sr^2)
bits. The skeleton and bad flags fix those locations first; their global
coordinates are not separately encoded for each filling.

After this conditioning, all good disks have their full fine boundaries
and lifts fixed. Choices of fillings are independent and recovered by
restriction. Conversely any such filling glues to a full tiling with
the fixed exterior. The full selected arcs already lie in the skeleton;
an additional selected-level component in a filled disk would be a
closed arc, impossible for de Bruijn tracks. Thus an arbitrary replacement
does not change the selected skeleton. When rare types have zero boundary
flux on a good disk, their absence is preserved as well.

For this auxiliary estimate, a window W must be the bounded interior
of one rectifiable Jordan curve, with boundary length P. Discard every
selected face whose closure meets that boundary before using interior
good disks. The diameter bound places all tiles of those faces in the
O_D(r)-tube of this one curve. This tube has area O_D(rP+r^2):
sample its arclength parametrization at spacing at most rho=C_D r;
at most ceil(P/rho)+1 disks of radius2rho cover its rho-tube.
Every original tile has area at least1 and the tiling interiors are
disjoint, so the additional whole-tile loss is O_D(rP+r^2).
Consequently P=O(L) gives O_D(rL+r^2), lower order than L^2
when r is fixed and L tends to infinity.

This is a one-Jordan-boundary estimate. It is not asserted for an
arbitrary connected region with rectifiable boundary and many tiny
holes. For an actual finite collection W_1,...,W_M of such Jordan
windows, each with perimeter P_j, charge each application separately:
the safe total upper loss is O_D(r sum_j P_j+M r^2), with any
overlap only reducing the union. It is lower order only under the
actual chosen scales and this summed bound. No unbounded collection
is paid for by a single O_D(rL+r^2) allowance.

## RM2. Clean closed disks after a consecutive merge

The following argument concerns a full arrangement, not arbitrary local
coarse insertion. Merge consecutive colors into groups, assigning each
group a vector w_g=(1,g-1). Call every within-group tile forbidden.
For a good disk C supplied by RM1, assume its selected face F has
closure disjoint from every forbidden tile, including tiles outside C
that merely meet its boundary. Work with an interior F. The full outer zonogon boundary is one
rectifiable Jordan polygon of perimeter O_D,c(L), so its touching
faces may be discarded at the O_D,c(rL+r^2) cost just proved.

First construct the global geometric coarsening. Move the fine slopes
continuously to the constant group slopes, keeping the first coordinate
one. At each positive parameter before equality, the vectors have the
original strict cyclic order. The affine-on-tiles map defined by their
height coordinates sends every tile with positive orientation and sends
the outer boundary once around the corresponding convex zonogon. A
regular image point has degree one and each tile-interior preimage has
positive sign. The images have disjoint interiors and fill that zonogon.
The cyclic ordering of incident rays gives local degree one at vertices
and edges as well. Thus these maps are homeomorphisms of the full disks.

Their limiting map F0 is continuous. Its fibers are connected. Indeed
let epsilon_t be the uniform distance to F0. The preimage under the
homeomorphism Ft of the convex set
Z_t intersect closed_ball(y,2epsilon_t) is connected, contains the
whole fiber F0^-1(y), and every Hausdorff limit lies in that fiber.
Compactness gives exactly that fiber as a limit of connected sets.
The case epsilon_t=0 is immediate. This proves connected fibers
without presuming them from a diagram.

Every point of C has a full neighborhood containing no forbidden tile.
There the limiting map is a local homeomorphism: all incident tile faces
still have positive determinant, and there cannot be two equal outgoing
group rays in the fan without an intervening within-group tile. Thus
every fiber meeting C has an isolated point. A connected fiber with an
isolated point is a singleton. Hence F0 embeds the entire closed C,
including all its vertices, into the actual coarse tiling. Its coarse
boundary is Jordan. This explains why avoiding forbidden tiles only in
the disk interior would not have been a sufficient assertion.

The limiting positive faces form a genuine coarse full tiling: any
positive overlap would persist before the limit, and all omitted faces
have zero area. Unit-horizontal integer edges exclude partial-edge
subdivision. The zero-area faces lie in its edge skeleton, since an image
in a positive face interior would again force an overlap before the limit.

For D=4 with exactly one merged pair and the other two groups singleton,
every coarse rank curve meets F0(C) in at most one arc. A singleton
curve is the same fine full curve, so RM1 already gives this. For a
curve of the merged group, follow its consecutive fine-curve pieces.
It can change fine identity only at a deleted within-group event.
It cannot cross a selected same-group barrier at the boundary of F:
that would be a forbidden tile meeting F. Therefore any departure from
F must cross a selected singleton barrier. To return to the same F
it must restore that barrier's sign, requiring a second crossing of
that same singleton coarse curve. The full coarse arrangement forbids
this. Its single visit inside F is consequently a single fine residual
chain and belongs to one disk block. It has exactly two ports there.

This proof uses the D4 singleton-group restriction. With several
different nonsingleton groups, a barrier itself can change fine identity
outside F. The sign-restoration argument above is then unavailable.
No general-D coarse two-port assertion is claimed.

**Clean lifting conclusion.** In this D4 case, any coarse tiling of
the same complete Jordan coarse disk boundary lifts to a fine tiling
with the original fine boundary and ranks. Glue the coarse replacement
to its unchanged full coarse exterior. Every coarse level curve has
exactly the same two boundary ports and no closed component. The boundary
therefore uniquely assigns it its original fine color and rank. Recolor
its track with that assignment. Each face uses two different groups,
so the two fine vectors have positive determinant. The edge increments
close around every face and around every disk loop. Integrating them
gives the fine physical map, with the original Jordan boundary. Positive
face orientation and boundary degree one then give an actual fine tiling.
Restriction and coarsening recover the coarse replacement, so distinct
choices remain distinct.

Conversely every fine filling with that complete lifted boundary has
no forbidden tile: the boundary integral of the relevant height minor
counts those nonnegative tile events and is zero for the given clean
reference. Thus whole counts agree, not merely one map on a selected
family. The same construction works after integer dilation, with each
boundary port repeated M times at its consecutive multiplied rank
levels. The prescribed fine colors of those M copies are fixed.

## RM2a. Zero rows and the two-direction endpoint

For a zero-row color, designate all its incident tiles rare. In a good
closed disk and its neighborhood none occur, so that height coordinate
is constant. Deleting those global tracks acts on the disk by a fixed
translation. Remaining singleton tracks keep their identities, their
two ports and the RM1 rank bounds. With one zero color and three
remaining singleton colors this gives the same exact reduction to a
three-direction Jordan disk, with arbitrary complete boundary.

If only two nonzero direction groups remain, a clean coarse disk has
only one parallelogram type and hence a fixed grid filling. Each straight
coarse track segment in the disk hits its boundary; its fine color is
determined there and remains constant because no internal group event
is allowed. If the boundary is compatible, as the reference proves,
the fine filling is unique. There is no quadratic clean-cell entropy
in this two-group case. This observation is not a theorem that arbitrary
defect-bearing regions have zero entropy.

The argument assumes that the nonzero groups already have a compatible
cyclic orientation and consist of positive parallel row multiples.
Reducing antiparallel rows to such a chart is a separate obligation.
This packet does not prove that orientation reduction.

## RM3. The actual three-direction boundary class and error aggregation

A coarse good disk above belongs to the following class GE3(r): it
has a fixed Jordan tile boundary of perimeter O_D(r), has at most
O_D(r) active rank curves, and extends by a fixed exterior to a full
three-direction zonogon with at most O_D(r) curves of each color.

To check the last assertion, start with the actual full coarse tiling
and delete every curve that never meets the disk. Its height contribution
is constant on the connected disk, so deleting it changes the disk only
by a translation and a fixed rank shift. The remaining full arrangement
has just the active curves, whose number is at most n_F. It supplies
the small full-zonogon exterior. Now continuously change its three
ordered directions to the standard unit-lozenge directions. All tile
determinants remain positive, so the preceding degree argument gives
a homeomorphism. Boundary word length, rank range and tile count are
unchanged; diameter and perimeter stay O_D(r). Every alternative filling
glues to that same exterior. In particular its scalar lozenge height
is the restriction of a uniformly Lipschitz height on a convex domain
of diameter O_D(r). This is stronger than merely bounding intrinsic
path lengths in a ragged disk.

The companion `rank-mesh-reasoning-r1-UR3-v1.md` gives a proposed
uniform dilation recovery for this actual class, based on a local
triangular consequence of the original Cohn--Kenyon--Propp theorem.
It does not invoke a balanced-hexagon formula. The primary theorem's
precise approximation quantifiers and the corollary need fresh audits.

Several disk blocks may arise in one F, so one cannot multiply a
per-block error eta(r)r^2 by just the number of selected faces. Here
is the correct aggregation. The sum of physical perimeters in F is
O_D(r), and its total area is O_D(r^2). Discard blocks with area
less than delta r^2. Isoperimetry gives

    area(B)<=sqrt(delta) r sqrt(area(B))
            <=sqrt(delta) r perimeter(B)/(2 sqrt(pi)).

Their total area in one face is O_D(sqrt(delta)r^2). At most O_D(1/delta)
remaining blocks occur in that face. If each GE3(r) disk has uniform
recovery error eta(r)r^2, these contribute O_D(eta(r)r^2/delta).
Over O_D(L^2/r^2+L/r+1) selected faces the normalized losses are
therefore O_D(sqrt(delta)+eta(r)/delta), plus terms vanishing as
L->infinity at fixed r,delta. Taking delta=eta(r)^(2/3) gives a
loss O_D(eta(r)^(1/3)) when eta(r)>0. Fine and standard coarse tile
areas are comparable by fixed D-dependent constants.

Finally, dilating one full reference tiling gives an exact exterior
for every dilated good disk. Independent fine insertions recovered
by restriction therefore transfer their entropy to that dilated full
frame, subject to the stated recovery estimates. This is not an
unreviewed assumption that an arbitrary coarse interior survives one
erased event; all incident rare events were excluded and their data
retained in the skeleton/bad-cell code.

## Limits of this checkpoint

No estimate S=O(epsilon L^2+L) is proved here; that is FL1's separate
candidate. No orientation chart, global profile partition, strict-window
matching, balanced remainder padding or original-frame entropy recovery
is imported. The local mask-boundary helper applies only to the stated Jordan
windows. Its r*sum P_j+M*r^2 cost must be summed over the actual
chosen windows before taking limits. Uniform UR3 is proposed only for
the globally extendable disk class just proved relevant, not for an
arbitrary nonextendable paired boundary. All claims remain candidates
pending two independent whole reconstructions and coordinator resolution.
