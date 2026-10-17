# Near-flat positive-path lens extraction

2026-10-17 UTC. **Candidate proof - unverified.** Constructor: coordinator.
This packet requires two fresh independent nonconstructor whole audits.
It uses accepted DG1/DG2 (reviewed-directed-geodesics-v1.1.md), not the
unreviewed annulus candidate. It does not prove EAI, PR, H or any official
entropy rate. No enumeration or CAS is a premise.

## CUT1: a buffered affine parallelogram has an actual inner lens

Fix D, v_i=(1,i-1), V=[v_1 ... v_D], and a genuine full marked zonogon
tiling with canonical lift a, interpolated affinely on each tile. Assume
the standard de Bruijn dictionary used by DG1: rank-threshold curves are
simple, same-color curves disjoint, and each different-color pair meets
at most once. All tile diameters are bounded at fixed D.

Fix VJ=I, Vc=0 and two independent vectors u,v with det(u,v)>0 and

    0<kappa<=J_i u,J_i v<=K  for all i.

These data are fixed before epsilon and L. Strict positivity of every
row minor is NOT required for this cutting claim; the two common
positive directions are required. Since VJ=I, u_x=sum_i J_i u>0 and
v_x=sum_i J_i v>0. Let

    P_L=x0+{s u+t v:0<=s,t<=L}.

Suppose the whole C sqrt(epsilon)L neighborhood of P_L is inside the
full tiling and the interpolated lift there satisfies

    ||a(x)-Jx-c||_infinity<=C1 epsilon L,

for fixed C1, sufficiently small 0<epsilon<=epsilon0 and sufficiently
large L>=L0(epsilon). Constants C,epsilon0,L0 may depend on the fixed
D,J,u,v,kappa,K,C1. In particular C is chosen sufficiently large for
the DG2 bands and the bounded tile-to-vertex allowance.

**CUT1.** There are two positive tiling-edge paths p<=q, from a common
vertex A to a common vertex B, disjoint except at their endpoints,
whose enclosed Jordan lens Omega is tiled by the original tiling and

    P_L minus its C2 sqrt(epsilon)L boundary band is contained in Omega,
    Omega is contained in the C2 sqrt(epsilon)L neighborhood of P_L.

Their total edge lengths are O(L); their global lift is the restriction
of a, without relabeling, so their common content is a(B)-a(A).
The paths and the selection rule may depend on the input tiling.
The symmetric difference between P_L and Omega has area
O(sqrt(epsilon)L^2+L). The harmless L term accommodates tile rounding.

Here P_L minus its boundary band means the inner parallel set of the
parallelogram. The statement does not require Omega to be contained in
P_L itself. A version contained in a prescribed outer window follows
by starting with a slightly inset parallelogram and retaining the stated
whole-neighborhood buffer.

### Four sides with genuinely shared corner vertices

At each of the four straight corners choose one vertex of a tile
containing it, by a deterministic tie rule, and use that SAME vertex for
the two incident sides. Its lift error relative to the straight corner
is at most E=C1 epsilon L+C0, where C0 is fixed by tile diameter and J.

Subdivide each u-side and v-side into equal steps ell=L/N, choosing
N of order epsilon^(-1/2). For small epsilon and large L, both meshes
satisfy kappa ell>=2E. Choose vertices at the interior sample points
by the same rule. DG1 joins consecutive vertices by positive paths;
DG2 confines them to a band R=O(sqrt(epsilon)L) about that side.
A deterministic shortest-positive-path tie rule is available because
the full tiling graph is finite. Enlarging C ensures all these paths
and their sample tiles lie in the hypothesis region.

Concatenate the u-side followed by the v-side to obtain the lower
candidate path, and the v-side followed by the u-side for the upper.
Each concatenation has the same chosen starting and ending vertex.
Every nonempty edge advances x by one, so each path is simple and
x-monotone. Along each side its lift increments telescope. Therefore
each whole path has O(L) edges: its length is the sum of its coordinate
increments, and J and the endpoint errors are bounded.

### Intersections occur only near the two extreme corners

The straight lower and upper boundary chains of P_L are x-monotone
piecewise linear graphs. Their vertical separation at abscissa x is
bounded below by

    c0 min(x-x_left,x_right-x,L),

with c0>0 depending only on u,v. Each constructed path is within
distance R of its respective straight chain, apart from the bounded
corner displacement already included in R. Since those chains have
fixed bounded slopes, this implies vertical graph error at most C3 R
at every abscissa common to their x-ranges. Thus an intersection of
the two constructed paths is within O(R) of one of the two extreme
corners. Their intersections are tiling vertices or shared tiling edges;
there are no transversal crossings in edge interiors.

Choose the last common vertex in the initial O(R) corner region and
the first common vertex in the final O(R) corner region. When epsilon
is small, these two corner regions are disjoint and an abscissa slab
between them has strict lower/upper separation. Hence the two selected
vertices are in their stated order along both positive paths. Between
them there is no common vertex or edge. The retained paths form a
Jordan lens; the upper one is above the lower one throughout its open
x-range. Its physical boundary differs from the straight parallelogram
boundary only in the O(R) side bands and corner boxes. This proves
the stated inner/outer containment, and integrating these bounded graph
errors gives symmetric-difference area O(L R+R^2+L).

The lift at a common vertex is the SAME canonical full-tiling lift
from either path. Thus the retained paths have exactly the same ranked
content, not merely the same physical endpoints. No assumption that
physical projection is injective on every integer height vector is used.

### Why the retained boundary words are comparable

Every retained positive path crosses a fixed color-i rank-threshold
curve at most once: a_i increases from its common starting value to
its common ending value. Exactly the threshold curves with ranks
a_i(A)+1,...,a_i(B) cross each retained path once. All other curves
cross neither path.

A retained curve inside the Jordan lens therefore has one connected
arc joining the lower boundary to the upper boundary. It cannot have
a second component: such a component would require another boundary
crossing or a bounded closed component of the original simple proper
curve. The latter is impossible. Two retained different-color arcs
cross at most once by the full-tiling dictionary; same-color arcs
do not cross. Their sole possible crossing has the positive ij tile
orientation. Consequently a pair of ranked labels changes its order
between the lower and upper path only from ij to ji for i<j.
All pairs already inverted on the lower path remain inverted above.
Thus the lower word p and upper word q satisfy Inv(p) subset Inv(q).

This can also be read directly at the sole ij crossing: the lower
two-edge boundary of its positive parallelogram is ij and the upper
one is ji. Endpoint alternation in the disk identifies the same
order reversal without a generic vertical sweep of the entire tiling.
Fixed rank labels on both paths are supplied by the canonical lift.
Every tile inside Omega is an original tile, and its boundary matches
the paths exactly; no projection of an abstract surface is being
asserted to tile the plane.

## CUT2: the discarded information has a boundary-strip encoding

Consider a family of restrictions of full integer-parallelogram tilings
to P_L, under the same fixed data and error bound. Use a fixed finite
local lattice alphabet at D: tile origins and types in a bounded
neighborhood determine the local tiling record. Choose one full-tiling
representative for each distinct restriction before applying CUT1.

The inner lens contains the fixed inner parallel set of P_L at distance
C2 sqrt(epsilon)L. Any original tile not recovered by restriction from
the inner lens meets a deterministic boundary strip of P_L of thickness
C2 sqrt(epsilon)L plus the maximum tile diameter. This strip has
O(sqrt(epsilon)L^2+L) integer cells. Record the original alphabet on
these cells. This recovers the original restriction even if the output
lens extends outside P_L, since its retained tiles plus that strip
record contain every tile whose record is relevant to P_L.

Also record the two boundary color words (O(L) letters), one endpoint's
integer lift and physical location, and a finite tie/length convention.
If input heights and positions lie in an O(L) box, these coordinates
cost O_D(log L) bits. More generally retain their explicit logarithmic
coordinate-range cost; there is no uniform O(log L) assertion for an
arbitrarily translated global frame. Global canonical rank offsets do
not acquire a factorial matching cost.

Therefore for bounded coordinate ranges the extraction has fibers at
most

    2^{O_D,fixed-data(sqrt(epsilon)L^2+L)}.

The recorded inner boundary identifies the physical subregion in the
output. Different input restrictions with identical output lens tiling,
identical boundary data and identical strip record agree everywhere in
P_L. This is an upper fiber statement; it is not by itself a theorem
that an arbitrary replacement patch can be inserted into an original
fixed outer boundary.

## Interfaces still open

Combining CUT1 with a VALID independently reviewed annulus theorem could
supply strict-slope patch transfer. The annulus candidate remains a
separate dependency requiring its own audits. Its current written
scope is D=4; an arbitrary fixed-D extension must be stated and audited.

Zero rows, antiparallel extreme rows and parallel-row groups require
separate treatment. The common-positive-direction hypothesis already
excludes zero rows and antiparallel pairs. No sigma bound uniform near
a zero minor is inferred from CUT1. No local-to-global variational
recovery, original-zonogon all-scale remainder argument, H or full
official solution is claimed by this packet. Novelty is unestablished.
