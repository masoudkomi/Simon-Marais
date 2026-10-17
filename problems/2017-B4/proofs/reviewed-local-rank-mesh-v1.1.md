# Accepted ['LW1'] — coordinator status and scope

2026-10-17 UTC. **Proved, independently reviewed scoped partial result.**

LW1 holds for every fixed D, ONE known rectifiable Jordan window of diameter/perimeter O(L) with its fixed tiled buffer, the full canonical lift and the separate absolute range R. The code costs O(L²/r+Sr²+rL+r²+log(R+2)) without assuming global contents O(L). It uses local rank ranges, one connected boundary trace and one absolute height anchor, and crossing words whose exits require no outside matching permutation. Only actual global selected faces wholly inside the window are retained; discarded data pay the actual one-curve fringe. Complete ranked disk boundaries and independent replacement into ONE full reference exterior are fixed. Rare absence in arbitrary replacements is asserted only under the additional zero-flux condition.

The exact RM1 disk/port/diameter dependency that was conditional in the frozen candidate is now discharged by the separately accepted repaired packet, reviewed-rank-mesh-v1.2.md. Its entire RM1 body was compared across the original and repaired candidates and is identical; the repaired auxiliary window statement is not used to derive LW1. Reviewer1 authored that older RM1 background and disclosed this boundary: this is an independent audit of the coordinator's NEW local code, not a fresh independent review of that reviewer's own RM1.

The complete frozen candidate below is preserved byte-for-byte; its historical unverified labels record its submission status. This acceptance header and the separate acceptance record give the current scoped status.

---

# A local rank-mesh code without a global-content loss

2026-10-17 UTC. **Candidate proof - unverified**, coordinator root.
Two fresh initially blind whole nonconstructor audits are required.
This is a local coding lemma, not UR4, H, PR or an official limit.
No mathematical program or CAS was used and no novelty is claimed.

## Conditional background and the new issue

Use the accepted full marked tiling dictionary and canonical lifts in
`proofs/reviewed-fixedD-structural-v1.2.md`. The exact RM1 disk, port
and diameter conclusions in the FULL repaired candidate
`notes/rank-mesh-reasoning-r1-candidate-v1.1.md`, SHA-256
f6c1681ae288b37d2e845e31ca1ef4503d659c9669ec6801266f3564de771ee3,
are EXPLICIT CONDITIONAL premises. That packet is still awaiting both
affected reaudits. No similarly named unreviewed result is silently
accepted. This proof does not use the whole-zonogon code M2 as a local
bound: the global contents can be much larger than the window scale.

Fix D, v_i=(1,i-1), and an actual full marked tiling of the fixed
zonogon with contents N_i. Fix a known Jordan window W, diameter<=cL,
whose ONE rectifiable boundary has length<=cL, L>=1. A fixed-width
neighborhood of its closure is in the full tiled domain. The window,
directions, contents and its position are fixed across the source family.
All coordinates of vertices and canonical heights under discussion are
bounded in absolute value by R>=2. The bound R need not be O(L).

Select the full rank curves with ranks divisible by an integer r>=2.
Their whole-tile skeleton is exactly the global rank mesh, restricted
locally. A designated set of rare tile types is fixed. Suppose each
source has at most S rare whole tiles meeting the fixed constant-width
enlargement of W. Boundary tile contacts are counted, not ignored.

**LW1.** There is a code of length

    O_(D,c)(L²/r + S r² + rL + r² + log(R+2))          (LW)

which fixes the local skeleton, the discarded information, and the
complete lifted boundaries of all remaining RM1 Jordan disks. Every
remaining disk lies in a global selected face F whose whole closure
and incident tiles are clean. Its fine residual chains and two ports
are exactly the RM1 ones. Knowing their fillings and this code recovers
the original restriction to W. Their arbitrary boundary-compatible
fillings glue to the SAME full exterior of any one reference in the
code class. There is no matching permutation or per-tile log R cost.

The number of relevant interior selected faces is
O_(D,c)((L/r+1)²); the aggregate RM1 perimeter bound in each such
face is unchanged. The statement permits an arbitrary fixed D.
It does not assume or prove a lower-dimensional entropy theorem.

## 1. Uniform local rank ranges

On each of the finitely many physical tile types, the affine lift
has a fixed bounded derivative. Integrating along segments in the
CONVEX full zonogon gives an extrinsic Lipschitz constant G_D for
every height coordinate, independent of contents and filling.
The diameter of any fixed-width enlargement of W is O_c(L+1),
even when W itself is ragged. Therefore at most O_(D,c)(L+1)
integer or half-integer levels of each color can meet it.
Among them at most O_(D,c)(L/r+1) have selected ranks.

Any skeleton tile meeting that enlargement is an intersection
between one such selected full curve and another locally relevant
full curve. Distinct full curves meet at most once, and same-color
curves never meet. Thus there are

    O_(D,c)((L/r+1)(L+1))=O_(D,c)(L²/r+L+1)

such skeleton tiles. This uses local rank ranges, not N_i=O(L).
It also counts selected/selected crossings; duplicate traversal
can only change the fixed constant.

## 2. A boundary trace with one absolute lift anchor

Fix a strip about the known curve partial W of width several times
the largest tile diameter. Its possible integer tile origins have
cardinality O_(D,c)(L+1). To check this without a convexity assumption,
sample an arclength parametrization of that ONE connected curve at
unit spacings. Its bounded-width tube is covered by O(cL+1) fixed
radius disks, each containing only boundedly many integer origins.

At each possible origin record which of the binom(D,2) tile types
is present. This finite alphabet recovers every tile in the strip,
including all tangencies and vertex contacts. The union of tiles
meeting the curve is connected through shared vertices: follow the
continuous curve through successive tiles. Hence its tile-edge graph
is connected, and thicker parts can be attached by the same rule.
Use a deterministic connected tile trace containing the curve.
One canonical integer height at a chosen trace vertex costs
O_D(log(R+2)) bits. Integrating the known colored edge increments
along a deterministic spanning tree recovers all trace lifts.
Integrability is supplied by the actual source tiling. No independently
chosen rank anchor is charged at each boundary contact.

All coordinate positions of the trace tiles are already specified
by the fixed possible-origin list. A chosen anchor index costs
O(log(L+2)) bits, absorbed in O(L+1); its physical coordinate need
not be transmitted once that index is known. The absolute height
anchor is the sole log R term.

## 3. Coding interior skeleton pieces without pairing their exits

Cut a selected full curve at its passages through the recorded
boundary strip. Every component in the remaining interior has
entry and exit tiles in that strip. There is no closed component,
since the original full de Bruijn curve is a simple proper arc.
All component starts in its fixed orientation are therefore known
from the strip's tile geometry and lifts. They have a deterministic
order, for example by the physical edge coordinates followed by
color and rank. Tangencies never create an unrecorded start;
components supported in the strip are already recorded.

Start at its known color-i edge midpoint and traverse the component.
For each next crossing record only the other color j. The next
midpoint displacement is +v_j for j>i and -v_j for j<i, using
the normal-increasing orientation of the i curve. Thus the tile,
next edge, and all its height coordinates are recovered from the
previous midpoint and lift. Stop at the recorded boundary strip,
using a fixed terminator if needed. There are O(L+1) starts:
each is a contact through an edge of one of O(L+1) recorded tiles.
Their terminators have that same total cost.

The total number of crossing letters is bounded in section1 by
O(L²/r+L+1). Every tile may be traversed by at most two selected
curves. No exit permutation is needed: its location and rank are
determined by the traversed letters. A curve may leave and reenter
W many times; its separate local pieces are coded separately from
their known starts. Their global matching outside W is not used
to reconstruct a local tile or its lift. This proves the skeleton
code with O(L²/r+L+1+log(R+2)) bits.

## 4. Interior global faces, the boundary fringe and rare flags

Retain only global selected faces whose closure, and the fixed
tile-star margin, lie inside W. Discard all others that have tiles
meeting W. By RM1 every face has diameter O_D(r). A face meeting
W but not retained therefore lies within an O_D(r)-tube of partial W.
The one-curve arclength argument, now at spacing r, bounds its
possible integer tile origins by O_(D,c)(rL+r²). Record the full
finite tile alphabet in this deterministic fringe. Its code has
that same size and includes the initial boundary trace.

The locally coded selected arcs determine all retained faces:
a face enclosed strictly inside W cannot connect to the exterior
without crossing its recorded selected boundary. It is an actual
global selected face, not an artificial component obtained by
cutting one at partial W. Only O(L/r+1) selected full curves meet
W; any retained face is a cell of that subarrangement, since all
other selected curves have a constant side sign on W. The total
number is at most the full subarrangement's
1+m+binom(m,2)=O((L/r+1)²), independently of oscillations at
the window boundary. Boundary-cut cells are already discarded.

Mark a retained face bad if its closure meets a rare whole tile.
Any such tile is inside the fixed enlargement already included
in S. A tile contains at most two selected arcs and hence meets
at most four selected faces. Thus at most4S faces are bad.
Record one flag for every retained face. This costs
O((L/r+1)²), absorbed in LW. By RM1 each bad face has
O_D(r²) residual tiles and diameter O_D(r). The skeleton code
fixes the bad faces' physical positions first. The fixed finite
alphabet in their O_D(r²) possible origin boxes therefore records
all bad residual tiles with O_D(Sr²) bits. There is no separate
O(log R) coordinate cost per bad face or per tile.

If L is comparable to or below r, the deterministic fringe and
the O(r²) allowance can cover the whole window. The same bound
still holds; no positive number of retained disks is asserted.

## 5. Complete boundaries, recovery and one fixed exterior

In a retained good face, delete the skeleton tiles and take the
RM1 biconnected tile blocks. Their boundaries and disk geometry
are determined by the already fixed skeleton. Each boundary edge
has a known adjacent skeleton tile: two nonskeleton tiles sharing
an edge belong to the same selected face and the same block.
Thus their complete integer boundary heights and every fine
rank label are also known. The full boundary trace/skeleton lifts
are consistent because they came from one actual tiling.

The closure of a good F meets no rare tile at all, including a
tile outside a residual block incident at an edge or a vertex.
The retained margin keeps its closed stars inside the full tiling.
Hence the exact closed-face cleanliness needed in a separate
clean coarsening lemma is available. It has not been inferred
from S being small without discarding bad faces.

All unknown original tiles in W are now in those good disks.
Their fillings together with the finite code recover the
original restriction. Fix one actual full representative of
the code class. Replacing any good disk by a filling with
the same complete boundary leaves that representative's
entire exterior fixed. The pieces are Jordan disks with
disjoint interiors, possibly sharing fixed boundary vertices,
so replacements glue independently and are recovered by
restriction. The original full boundary and all colored
edge increments are preserved. This is an actual full tiling,
not a collection of abstract curve pieces requiring an
unrecorded outside matching.

If rare types have zero boundary minor flux in a good disk,
their absence is preserved in every replacement, by the
nonnegative tile-count identity. That conditional statement
does not declare arbitrary designated rare types absent
in alternative fillings. LW1's code and upper recovery
itself do not need such a declaration.

Combining the counts in sections2–4 proves LW. Summing over
a finite collection of windows retains the actual separate
rP+r² fringe charges and the anchors; no arbitrary number
of windows is paid for by one perimeter allowance.

## Limits and next use

This supplies local information loss even when the full
zonogon's contents are arbitrarily large relative to L.
The whole buffered affine estimate, rare-tile count,
orientation chart, lower-dimensional recovery, strict
transfer and global finite-window assembly are separate
obligations. A hypothetical global use must condition on
the local codes jointly before choosing ONE reference;
independently maximizing different windows' code classes
would not ensure a common reference exists.

The exact RM1 premise still awaits its own repaired-packet
acceptance. Two fresh whole audits must check every local
rank, traversal, face, lift, boundary and recovery inference
before this new coding lemma can be promoted.
