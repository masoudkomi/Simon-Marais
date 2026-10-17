# Initially blind whole audit of the local rank-mesh code

2026-10-17 UTC. Reviewer `review_2017_coarsening_r1`; requested
gpt-6.1-sol/max, effective-setting readback unavailable. I read the complete
new candidate and its six-input freeze, the exact full repaired RM1 body
and the accepted structural dictionary/local-lift proof. No other fresh
local-rank-mesh reviewer report, issue, source check or conclusion was read
before this initial report and its complete freeze.

**Disposition: no substantive defect found in LW1, conditional on the
EXACT stated RM1 disk/port/diameter premises.** This does not accept RM1
on the author's authority or promote either packet. No UR4, H, PR,
lower-dimensional entropy theorem or full annual limit follows here.

Independence boundary: I authored the earlier general rank-mesh/RM1 and
fixed-D background, including its separate Jordan-window repair. I did
not construct the coordinator's NEW local rank-range/boundary-trace/
piece-word code, and do not count this audit as an independent review
of my own RM1 construction. The present whole reconstruction is explicitly
conditional on its stated conclusions; it avoids using the global M2
code under a false local content bound.

## Exact target and domain

The new target `notes/coordinator-local-rank-mesh-candidate-v1.md` is
11850 bytes, SHA256
`09c206718f1acecb9f23ae9bdb54122a4e9a9420b4549326413a664cb44230c5`.
Its freeze SHA256 is
`a3e76f8d6dcb6a2db900e810aa75c076b4b479235e95e6bbe021a85799fdc781`.
The theorem fixes D, contents N, position and ONE known Jordan window W
of diameter/perimeter O_c(L), L>=1, with a fixed-width tiled neighborhood.
The full zonogon is convex and its tilings have the canonical marked
lift. Coordinates/heights are bounded by R>=2; R and N may greatly exceed
L. Every source has at most S designated rare whole tiles meeting the
specified fixed-width enlargement, including contacts. Select every
rth rank curve, r>=2. The claim is a local code of cost

    O_(D,c)(L^2/r+Sr^2+rL+r^2+log(R+2)),

fixing skeleton, discarded information and complete boundaries of the
remaining actual RM1 disks. Their arbitrary complete-boundary fillings
must glue to the same full exterior of one reference and recover by
restriction. All of2017B4 is authorized, but this local fixed-D conditional
lemma does not determine the official regular-polygon liminf/limsup.
The official B4 statement was checked directly during this audit sequence.

## 1. Local rank ranges do replace the invalid global-content count

On a type ij tile the canonical lift is affine with fixed gradients
depending only on D. The accepted structural proof supplies these rows
explicitly. The full lift is continuous; integration along a straight
segment in the convex full zonogon gives one extrinsic Lipschitz constant
G_D independent of N and of the chosen filling. This is legitimate even
when a path in the ragged window itself would be long.

A fixed-width enlargement of W has diameter O_c(L+1). Therefore each
coordinate's values there lie in an interval of length O_(D,c)(L+1).
Only that many integer/half-integer levels, and O_(D,c)(L/r+1) selected
levels, can meet it. A skeleton tile meeting W or its required constant
enlargement has its center within a further fixed tile diameter, so both
crossing curves lie in the same enlarged local rank ranges after fixing
that allowance once. Different-color full curves cross at most once;
same-color curves never cross. Counting a selected local curve against
all local curves gives

    O((L/r+1)(L+1))=O(L^2/r+L+1)

skeleton tiles. Counting a selected/selected tile twice changes only a
fixed constant. No N_i=O(L) assumption appears, and the bound remains
valid for a huge absolute rank near the middle of a large zonogon.

## 2. One connected boundary trace determines all local absolute ranks

For ONE rectifiable Jordan boundary of length P<=cL, sample its arclength
at unit spacing. A fixed-width tube, enlarged by the tile diameter, is
covered by O(P+1) disks of fixed radius. Each disk contains a bounded
number of integer origins. Thus a finite tile-presence alphabet over the
known possible-origin list records all tiles needed near the curve,
including tangent and vertex-only contacts, in O_(D,c)(L+1) bits.
The list depends on known W, not on an encoded coordinate for every tile.

The trace can be chosen deterministically as all tiles meeting a fixed
connected boundary tube, within this enlarged origin list. Its tile-edge
graph is connected: follow a continuous path through the connected tube;
successive intersected tiles share an edge or vertex, and each tile's
edge cycle is connected. This also proves connectivity for the thinner
tiles meeting the original curve, with thicker needed parts attached
inside the same bounded tube. Vertex contacts do not require edge
connectivity of the TILE adjacency graph; connectedness of the tile-edge
graph is exactly what height integration needs.

Choose a trace vertex by a fixed index/tie rule. Its integer height costs
O_D(log(R+2)). Integrate known colored edge increments along a deterministic
spanning tree of this connected edge graph. This gives every trace vertex
height and every midpoint rank; consistency around cycles is guaranteed
by the actual source tiling. An anchor index costs O(log(L+2)), absorbed
in O(L+1); its physical location is already in the known list. Separate
boundary contacts do not need separate absolute lift anchors.

This step is the essential difference from starting each interior curve
piece with an independently encoded global rank. The one boundary trace
supplies all those ranks through one common canonical lift.

## 3. The interior piece code needs no exit permutation

Remove the recorded boundary trace/strip and consider only its remaining
INTERIOR selected-curve pieces. A component has entry and exit at known
trace edges: a full curve is a proper simple arc ending on the full outer
boundary outside the buffered W, so it cannot be a closed component
trapped in W. If the curve exits/reenters W, each separate visit meets
the recorded strip. Tangencies or pieces wholly in the strip are already
recorded. With the fixed orientation of each color, all inward starts
are known and can be ordered by their edge coordinates, color and rank.
There are O(L+1) starts, since each recorded tile has only a bounded
number of curve/edge contacts.

At a known color-i entry edge midpoint and height, a letter j uniquely
determines its crossing tile and next midpoint. The displacement is
+v_j for j>i and -v_j for j<i, since det(v_i,displacement)>0 fixes
the curve orientation. For j<i the known entry edge is the opposite
i edge of the ordered j,i tile, so its origin is recovered by subtracting
v_j. For j>i the entry edge directly gives the origin. The full lift is
recovered by the corresponding signed e_j increment; the selected i
rank remains fixed and all other ranks are determined. There is no
hidden choice of the other strand's absolute rank.

Continue until the known trace is hit, with one fixed terminator if
needed. Its location AND rank have now been determined by the letters;
no permutation matching this exit to a start outside W is transmitted.
The next piece starts independently from its already anchored trace edge.
Even many oscillatory visits through a nonconvex Jordan window cost only
their O(L) known contacts plus their actual crossing letters. Each tile
is traversed by at most two selected curves, so the sum of word lengths
is O(L^2/r+L+1). Fixed alphabets and terminators prove the claimed skeleton
code, with only the one O(log R) anchor cost.

Duplicate descriptions of selected/selected tiles are harmless: on actual
source data they agree, and reconstruction of a tile cannot branch once
entry edge and next other color have been specified. Impossible strings
need not be accepted. A mathematical program or a broad finite scan is
not needed to establish injectivity of this code.

## 4. Which local cells are actual global selected faces

Retain only faces whose whole closure and incident fixed tile-star margin
are inside W. RM1's diameter bound is uniform in global contents, because
every coordinate is trapped between successive selected half-integer
levels or a tail of width <=r. Hence any nonretained face with a tile
meeting W is within O_D(r) of the one boundary curve, allowing the fixed
tile diameter/star allowance. A bounded connected set meeting both W
and its complement must meet the boundary; the same reasoning with the
fixed margin handles a face that stays inside but approaches it.

Arclength sampling at spacing r covers the O(r) fringe by O(P/r+1)
disks of radius O(r). Each has O(r^2) possible integer tile origins.
The full finite alphabet records every discarded original tile there
in O_(D,c)(rL+r^2) bits. This is a Jordan/one-connected-boundary argument,
not the invalid perimeter-only bound for arbitrarily many tiny holes.
It also includes the initial fixed-width trace and all boundary-cut
faces, so no outside face filling is subsequently needed.

The locally known selected pieces determine each strictly interior
enclosed face and whether it has the stated margin. Such a face cannot
connect to an outside unknown region without crossing its known selected
boundary. It is therefore an actual GLOBAL selected face, rather than
an artificial component produced by cutting a global cell at W.
Only m=O(L/r+1) distinct selected full curves meet W. Curves missing the
connected W have constant side signs there and do not subdivide it.
For a retained whole face, every bounding selected arc meets W; removing
the other curves cannot open that cell. It is a cell of the subarrangement
of those m full curves. The disk arrangement cell bound
1+m+binom(m,2) gives O((L/r+1)^2) retained faces, even if their curves
oscillate across W many times. Counting cut components by this formula
would have been false; they have already been put in the fringe.

This use of RM1 only imports its exact uniform per-face diameter,
disk/port and perimeter statements. Its earlier whole-zonogon M2 code
and the earlier global N_i<=cL condition are not substituted for a local
bound. The actual derivation of the per-face RM1 bounds contains no N
constant that would invalidate this conditional use.

## 5. Rare flags and the cost of bad residual tiles

A whole tile contains at most two selected midpoint arcs. These arcs
divide its interior into at most four parts. Selected curves avoid tile
vertices, so a face meeting that tile only through a vertex is the same
local face as a nearby interior corner portion. Thus the tile meets the
closures of at most four selected faces, including all contacts. A rare
tile incident to a retained F is in the fixed enlargement covered by S.
At most4S retained faces are bad.

One flag per retained face costs O((L/r+1)^2), absorbed by the displayed
LW bound for L>=1,r>=2, even when S=0. Skeleton geometry fixes each bad
face's position and O_D(r)-diameter box before the residual filling is
recorded. A finite alphabet over its O_D(r^2) possible integer origins
then records all its residual tiles at O_D(Sr^2) cost. The position and
all large global rank coordinates are not charged independently at each
tile or bad face.

The assertion that each GOOD face closure is free of rare tiles includes
skeleton tiles or other tiles incident at an edge or vertex, not just
residual interior tiles. Boundary-cut faces were discarded and the
retained star margin is inside the full tiling. This is precisely the
closed cleanliness premise later coarsening arguments may require;
small S alone is never treated as that premise.

For r comparable to or larger than L, the rL+r^2 fringe allowance may
cover all of W. No retained disk is promised, and this is consistent
with the same code inequality. When r is small and S=0, the flag and
trace costs are absorbed by L^2/r+rL+r^2; they are not silently omitted.

## 6. The residual disk boundaries really are known, with all lifts

For each retained good face, its geometric residual closed set is the
face minus the already known whole skeleton tiles. It is independent
of the still unknown filling. RM1 decomposes this set into filled
biconnected tile blocks. Because RM1 rules out unfilled bounded faces,
its vertex pinches are actual cut points of the residual set; splitting
there gives its Jordan pieces determined by that fixed boundary geometry.
An arbitrary interior diagonal or shelling choice does not select a
different physical disk decomposition.

Every boundary edge of such an interior disk has a known skeleton tile
on its other side. If its neighbor were nonskeleton, the shared edge
would cross no selected arc and both tiles would be in the same selected
face. Their two tile cycles share an edge and hence lie in the same
biconnected block, contrary to the edge being a block boundary. There
is no full outer-boundary edge here because of retention and its margin.
Thus every disk boundary edge position, color and endpoint lift comes
from known skeleton data. Those data were already anchored to the common
boundary-trace lift. Full fine color ranks and RM1's original two ports
are fixed, even if the disks share a cut vertex.

This addresses a substantive possible ambiguity: specifying just the
selected midpoint arcs without their whole crossing tiles or their lifts
would not have fixed the complete fine boundaries. The actual code keeps
the whole tiles and starts from one canonical lift, so that weaker code
is not what is being counted.

## 7. Recovery, arbitrary fillings and the one-reference quantifier

All original tiles in W are now either skeleton, fringe, bad data or
inside the retained good Jordan disks. Given the code and those disk
fillings, reconstruction recovers the whole original restriction.
Choose ONE actual full reference representative of a code class. Its
entire exterior of these fixed disks, including the full original
zonogon boundary, is kept. Every complete-boundary-compatible filling of
each disk glues to that reference exterior. The disks have disjoint
interiors and can share only fixed boundary edges/vertices; no tile
overlap or gap is introduced. Restriction to each designated disk
recovers the chosen filling. The height increments match on the complete
boundary, not just a coarsened or unlabeled boundary.

The selected skeleton remains valid after such a replacement: its full
tracks are outside the residual disks, and no selected rank crosses a
disk boundary. A putative new selected level component inside would be
a closed deBruijn curve in the resulting full tiling, forbidden by the
full dictionary. There is no missing outside exit matching. The exact
fine two-port labels on the boundary remain the reference ones.

LW1 does NOT assert that an arbitrary designated rare type is absent in
every alternative filling merely because it was absent in the reference.
The packet's conditional extra claim uses zero boundary minor flux and
the nonnegative tile-count identity; under THAT hypothesis absence is
preserved. Otherwise alternative fillings may cease to have the original
rare flags/code classification while still gluing to the same fixed
exterior. The stated recovery and insertion claim does not require them
to remain in that source code class. No erroneous rarity invariance is
needed for the local upper-code result.

Combining the trace/pieces, flags, bad-data and fringe costs gives LW.
The O(L+1) terms and O((L/r+1)^2) flag count are absorbed since r>=2,
L>=1. One log R term suffices. For several known windows one charges
each actual fringe rP_j+r^2 and anchor. The proof does not bound an
unbounded number of windows by one perimeter or maximize different
windows' code classes independently of a common full reference.

## Source scope, work performed and limitations

The new proof is an elementary local encoding argument. Its external
mathematical background is explicitly the accepted full marked tiling,
canonical lift and finite alphabet, and its only unaccepted premise is
the exact RM1 conclusions. The full repaired RM1 candidate was inspected
to verify that the alleged per-face premise does not import a bound
proportional to N; no conclusion from its whole M2 or D4 coarsening/UR3
argument is used as a theorem here. No fresh RM1 or LW peer conclusion
was read for this audit.

No mathematical computation, CAS, enumeration, finite experiment or author
rerun was used. Administrative hashing verifies the target/freeze and
prior immutable bytes. All original/repaired candidates and earlier
reviews remain untouched. The full conditional local result passes this
initial whole audit; a second fresh nonconstructor audit and coordinator
reconciliation remain required. The theorem supplies no whole-buffer
affine estimate, rare-count estimate, orientation chart, UR4, strict
transfer, lower-dimensional count theorem, global compatible recovery,
H, PR or official limit.
