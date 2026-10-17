# CUT1/CUT2: second independent whole initial audit

2026-10-17 UTC. Frozen initial report, completed before reading any other CUT
review, issue ledger or conclusion. Reviewer: review_2022_complexity_r2,
not a constructor. Requested settings: gpt-6.1-sol / max; no independent
effective-setting readback is available. The candidate remains unverified
pending the coordinator's reconciliation of both reviews.

Audited target: notes/coordinator-lens-cutting-candidate-v1.md, SHA-256
1937c12d4cf9c9e2d7b4f713566a77e1b32e1a88ea0c55f09ae7e43870b8482f.
I read the whole candidate, its freeze, the accepted DG1/conditional DG2
exposition and acceptance, AGENTS.md, and the 2017 statement. I checked the
primary plane-arc input again. I did not read a peer CUT report or finding.
No computation, enumeration, CAS, candidate edit, shared edit or Git operation
is a mathematical premise of this audit.

## Decision and precise scope

I find no substantive defect in CUT1 or CUT2 under their stated fixed-data,
whole-neighborhood, genuine full-tiling, and coordinate-range hypotheses.
Below I reconstruct every step, including the sign argument for comparability,
the one-sided distance-to-graph conversion, and the existence of an actual
nonempty Jordan lens. These are essential; simply invoking a partial-cube
graph or drawing approximate sides would not establish CUT1.

The result is a fixed-D conditional cutting lemma and an upper bound on
recovery fibers. It neither inserts arbitrary replacements nor closes a
closed-annulus or entropy-recovery argument. It does not prove the two
official limits. In particular the constants are not uniform as a common
positive margin tends to zero, and CUT2 explicitly charges unbounded global
coordinate ranges. I recommend the coordinator accept only this scope if the
other independent audit agrees and no new substantive objection remains.

## 1. Domain, lift, and dependencies

The official open problem counts marked tilings in a fixed regular 2n-gon;
it asks for both normalized logarithmic growth limits. The present finite-D
integer zonogon has vectors v_i=(1,i-1). It is an intermediate model, not an
identification of its scale parameter L with the official n.

The full tiling is a genuine two-dimensional tiled disk. Its de Bruijn
dictionary and canonical lift a are explicit background hypotheses of the
accepted DG1 exposition. In particular Va(x)=x, positive edges add e_i, and
the lift is affine on each tile. The lift is single valued on an actual
physical vertex even though the unrestricted map V:Z^D -> Z^2 has a kernel.
There is no inference from equal physical endpoints to equal arbitrary
integer height vectors.

DG1 gives an actual positive graph path between coordinate-ordered vertices.
DG2 bounds every point of that path by M_V(K ell+3E) from its starting target
sample, where M_V=sum_i ||v_i||. DG2 does not require an affine estimate along
the path; endpoint lifts already give the bound. The whole target buffer
ensures that the resulting path lies in the permitted region. Hence using
DG2 here does not reason circularly from confinement to the affine estimate.

The accepted disk-to-plane argument is relevant to DG1: radial extensions
create no new crossings, and exterior cells attach to single existing
boundary-vertex cells. The primary arc lemma allows parallel pairs and
supplies a dual path crossing each arc at most once. No outside shortcut or
projective every-pair-crosses hypothesis is imported into CUT.

The identities VJ=I and Vc=0 are used at physical sample points and in
DG2. Positivity J_i u,J_i v >= kappa implies
u_x=sum_i J_i u >0 and v_x=sum_i J_i v >0. Independence and det(u,v)>0
then put the slope of u strictly below that of v. Zero rows and
antiparallel rows cannot satisfy this common-positive-direction hypothesis.
Other row minors may vanish; CUT never divides by them.

## 2. Equal meshes and shared corners

Fix D,J,u,v,kappa,K,C1 before epsilon and L. For a corner or interior
sample x, choose a vertex w of one tile containing x. Since the lift is
affine on a tile, |a(w)-a(x)|_infinity <=1, with a harmless bounded
allowance if a different local recording convention is used. Its physical
distance is bounded by the fixed maximum tile diameter. Thus
|a(w)-(Jx+c)|_infinity <= E=C1 epsilon L+C0.
The same chosen corner vertex must serve both adjacent sides. This prevents
an unmatched corner rank offset; the candidate explicitly makes that choice.

Here is one concrete way to make the equal-step choice in the note. Choose
A >= max(1,4C1/kappa), shrink epsilon0 so that
1/(A sqrt(epsilon))>=2, and set
N=floor(1/(A sqrt(epsilon))). Then
A sqrt(epsilon)L <= ell=L/N <=2A sqrt(epsilon)L.
After increasing L0(epsilon) to ensure
L >=4C0/(kappa A sqrt(epsilon)), one has kappa ell>=2E.
For the first contribution, 2C1 epsilon L <=
(kappa A/2) sqrt(epsilon)L when epsilon<=1; the constant contribution
uses the displayed lower bound on L. The same N works for both side
parameters because both u and v obey the same kappa,K bounds.

Every consecutive sample pair has nonnegative coordinate lift difference.
DG1 supplies a positive path; DG2 gives
R <= M_V(2KA sqrt(epsilon)L+3C1 epsilon L+3C0),
which is B sqrt(epsilon)L after enlarging the scale threshold. B depends
only on the fixed data. Choose the hypothesis buffer constant C larger than
this bound and the tile-sampling allowance. The closed neighborhood of the
entire target P_L then contains every sample tile and constructed path.
An endpoint-only buffer would not suffice; it is not the hypothesis used.

The graph is finite, so a deterministic lexicographic choice among its
shortest positive paths exists. Concatenating the lower u-side then v-side,
and upper v-side then u-side, gives paths with exactly shared extreme
vertices. All edges have x increment one. They cannot self-intersect,
and their lengths telescope to the difference in x coordinates of the
common endpoints. This is O(L), including the bounded endpoint sampling
allowance. A zero increment on an individual very short mesh segment
causes no problem; the full extreme vertices are distinct for small
epsilon and large L.

## 3. Straight-chain gap and vertical graph error

Translate x_left to zero. Put U=L u_x, W=L v_x and let alpha<beta be
the two slopes. Direct subtraction of the two broken linear chains gives
the exact gap

    (beta-alpha) min(x,U,W,U+W-x),  0<=x<=U+W.

Since u_x,v_x>0 are fixed, this bounds below
c0 min(x,U+W-x,L) for fixed c0>0, including the central plateau and
the case U=W.

Each constructed path point is within R of its assigned straight boundary
chain. The note needs only this one-sided distance estimate. Let f be that
straight graph and let M bound its two absolute slopes. For a path point
(x,g(x)) in the common x-domain, choose a straight-chain point
(x',f(x')) at distance at most R. Then
|g(x)-f(x)| <= R+M|x-x'| <=(1+M)R.
Thus a reverse Hausdorff estimate is not missing. The endpoints' x-domains
differ from those of the straight chains only by the bounded tile-vertex
sampling distance, and these exceptional portions already lie in extreme
corner boxes. A positive path is a graph at every intermediate real x
because every edge has positive x increment.

If the two candidate graphs meet at an x in the common domain, the straight
gap there is at most 2(1+M)R. Choose epsilon0 smaller so that R/L is less
than a fixed sufficiently small constant. The exact gap formula then
forces x to lie within a fixed multiple of R of one of the two extreme
corners. The short exceptional endpoint domains satisfy the same conclusion.
All contacts are confined to these two disjoint boxes. There is a nonempty
central abscissa slab of strict upper/lower separation.

## 4. Trimming produces a nonempty actual Jordan lens

The shared starting vertex belongs to the initial contact box, and the
shared terminal vertex belongs to the final box. Take the common vertex
with greatest x in the first box and the common vertex with least x in the
second. They are in this order on both paths. Between them there is no
other common vertex: any such vertex would lie in a contact box, violating
the chosen extremality. There is also no common edge, since that would
give common vertices. Edge interiors cannot cross transversally in an
embedded edge-to-edge tiling. Consequently the retained paths are
disjoint except at their endpoints.

Their order on the strict central slab is lower/upper. Since their graphs
are continuous and cannot meet elsewhere, the same order holds throughout
the open retained x-range. Their union is a simple polygonal Jordan
curve. It encloses a nonempty region because of the strict central slab;
this is stronger than merely asserting that all intersections are near
corners. The discarded start and end portions lie in their corresponding
corner boxes.

Every original tile has an interior disjoint from this boundary, which is
a union of original tile edges. The original full tiling covers the region.
Thus the region is a union of whole original tiles, without projected
overlap, missing faces, or an abstract-surface realization assumption.

For outer containment, both retained boundary graphs lie in the R-neighborhood
of P_L, a convex set, so the whole Jordan region also lies there. For inner
containment, take a point at distance delta from every side of P_L, with
delta a sufficiently large fixed multiple of R. Its x-coordinate is
farther than the trimmed corner-box widths from either extreme. Its vertical
separations from the two straight graphs exceed the graph errors, with
constants depending only on the two fixed slopes. Hence it lies strictly
between the retained graphs. This proves inclusion of the fixed inner
parallel set, rather than inclusion of just a central vertical segment.
For small epsilon that parallel set is nonempty.

The possible symmetric difference is contained in fixed-width O(R)
side strips and O(R)-sized corner boxes. Their area is
O(LR+R^2+L), the last term allowing discrete boundary rounding.
Since epsilon<=1 and R=O(sqrt(epsilon)L), this is
O(sqrt(epsilon)L^2+L). Constants depend on the fixed shape and margin.
There is no assertion that the entire output lies inside the unbuffered
P_L; the candidate expressly allows a controlled outward extension.

## 5. Exact common ranked content and weak order

The trimmed common vertices A,B each have one canonical full-tiling lift.
Both retained paths have coordinate increments
a_i(B)-a_i(A)>=0. They traverse exactly the same consecutive color-i
rank labels. Coordinate ranges are therefore inherited from actual
vertices in the full marked tiling; there is no inference from truncated
formal ideals of height vectors outside the rank box.

For any color-i threshold, a positive path can cross it at most once:
a_i increases by one on an i-edge and is constant on other edges.
For thresholds strictly between a_i(A) and a_i(B), it crosses once on
each boundary; every other threshold crosses neither. These intersections
are transverse crossings of edge interiors, not intersections at boundary
vertices.

Restrict a full threshold curve to the Jordan disk. For a threshold
crossing the boundary twice, it has exactly one arc in the disk joining
those crossings. A further component would require more boundary crossings
or an entire bounded closed curve. The original full curve is simple and
proper, so the latter is impossible. A curve with zero boundary crossings
has no component inside: it cannot be trapped in the compact disk without
being closed or ending there. The retained arcs therefore all join the
lower boundary to the upper boundary, and the inherited one-crossing
and same-color noncrossing properties remain valid.

The crossing sign deserves an explicit check. Orient each color-i arc
from lower to upper. At its crossing with a positive i-edge this orientation
has positive determinant with v_i. This orientation remains consistent
along the de Bruijn track: within an ij tile it is +v_j for i<j, and
-v_j for j<i. At an ij tile with i<j the two oriented tangents are
+v_j for color i and -v_i for color j, so their determinant is
det(v_i,v_j)>0. Every possible retained pair crossing has this same sign.

A pair crosses at most once. Endpoint alternation in the Jordan disk
therefore changes its order only in the positive direction; calibrating
the sign on one ij tile gives lower order ij and upper order ji, for i<j.
If already ji on the lower boundary, an additional crossing would have
the opposite sign, so cannot occur. A noncrossing pair keeps its order.
Same-color ranks keep their order. It follows for all ranked labels,
not just total color counts, that Inv(p) is a subset of Inv(q).
This does not rely on an unspecified global vertical sweep.

## 6. CUT2: what the finite alphabet records

The inputs are distinct restrictions to P_L. Choosing one full-tiling
representative for each such restriction avoids trying to count the
arbitrarily many possible completions outside P_L. Apply the deterministic
extraction to that representative. Output tiles outside P_L are harmless
for an upper bound on fibers.

At fixed D a local lattice alphabet can be made concrete as follows:
in each integer unit cell, record the types and relative integer origins
of all tiles meeting that cell. All origins lie within a fixed neighborhood,
and there are finitely many types and relative origins. Hence this is
a finite presence-bit alphabet. A consistent assignment coming from an
actual tiling specifies all relevant tiles. Boundary contact conventions
may be fixed once; enlarging the recorded strip by a fixed number of cells
handles those conventions without changing its order of size.

The fixed inner parallel set is contained in Omega. An original tile
relevant to P_L but not recovered from the output Omega tiling cannot
meet that deep core in its interior, since Omega is a union of whole
original tiles. It therefore meets the deterministic strip near the
boundary of P_L, with a tile-diameter allowance for a record straddling
the boundary. This strip, including its fixed rounding halo, has
O(sqrt(epsilon)L^2+L) integer cells. A constant number of bits per cell
suffices. There is no need to encode an entire outside completion.

The two boundary words have O(L) letters. Given an endpoint location and
its lift, these words locate the whole boundary and identify all rank
offsets. They cost O(L) bits, with at most a logarithmic length/tie code.
For positions and heights in an O(L) box the endpoint code costs
O_D(log L) bits. In a general global frame it costs the logarithm of the
actual coordinate ranges. A translation with an arbitrarily large kernel
rank offset cannot be assigned a uniform O(log L) cost. The note explicitly
retains this qualification, so it does not repeat that false uniformity.

Given the same output lens tiling, boundary/endpoint code, and strip
record, every tile record in P_L is determined: it either belongs to
the output or is read from the strip. Thus the distinct input restrictions
agree. This proves the upper fiber bound
2^{O_fixed-data(sqrt(epsilon)L^2+L)} for the stated bounded ranges, or
the same bound times the explicit coordinate-range factor in general.
There is no factorial rank matching cost and no assumption of arbitrary
replacement-patch insertion.

## 7. Adversarial boundary checks and excluded conclusions

I challenged the common-corner choice, small equal mesh with integer N,
large sampling error, reversed relative side lengths, U=W, endpoint
domain shifts, contact along an edge, multiple corner contacts, absence
of a central main lobe, and loss of ranked content through projection.
The explicit constructions above handle them under the written small-error,
large-scale order of quantifiers. Epsilon=0 is not claimed; L0(epsilon)
may diverge. Constants may deteriorate with kappa, det(u,v), the two
positive x-components, or the fixed matrix J.

I also challenged a full curve reentering the lens, a curve entirely
inside it, negative crossing orientation, an exterior shortcut from DG1,
cut tiles in the discarded strip, arbitrary global rank translations,
and completion multiplicities. These require the proper-curve,
actual-full-tiling, buffer, and coordinate-range hypotheses; the candidate
has those hypotheses and the proof uses them.

No closed annulus is a premise. In particular I did not import an annulus
review outcome into this audit. CUT2 is an information-loss estimate;
an entropy lower bound requires an additional insertion/transfer theorem.
The stated unreviewed annulus interface is conditional, not a proof of
that missing step. Zero/antiparallel-row strata, arbitrary-D annulus
extension, EAI, PR, H and original-zonogon all-scale recovery remain open
in this packet. Novelty is expressly unestablished.

The accompanying issue ledger records the checked concerns and their
disposition. The freeze manifest fixes this full initial report, the
ledger, source checks, inputs, and integrity checks before peer comparison.
