# Blind whole reconstruction of CUT1 and CUT2

2026-10-17 UTC. Reviewer `review_2021_reasoning_j15_r2`, a fresh
nonconstructor. I did not construct the cutting packet and read no peer
CUT report, issues or findings before this whole report and companion
records froze. Requested gpt-6.1-sol/max; no independently verified
effective-setting readback. No enumeration or CAS was used.

## Disposition

CUT1 and the qualified upper-fiber statement CUT2 survive the complete
reconstruction below. I found no substantive objection or required
author repair within their written buffered, fixed-positive-direction
scope. The shared-corner choice, integer mesh, single main Jordan lens,
global rank identification, weak-order orientation, inner containment
and recovery of discarded information all admit the claimed bounds.
I recommend coordinator reconciliation of these two partial claims;
this reviewer does not promote a result. No annulus, EAI, PR, H,
all-scale fixed-frame recovery or exact 2017 entropy conclusion follows.

The input candidate has SHA256
`1937c12d4cf9c9e2d7b4f713566a77e1b32e1a88ea0c55f09ae7e43870b8482f`.
The accepted DG exposition has SHA256
`061ae1749e938aad68f1824ab5f33583a3a1c58e556bd62649309c7cb12da9aa`.
Both complete texts, the CUT freeze and the DG acceptance decision were
read. The sole external mathematical method is already accepted DG1/DG2;
the cutting argument does not use any annulus conclusion or the separate
unaccepted fixedD profile program.

## 1. Domain and exact hypotheses of DG1/DG2

The ambient object is a genuine full marked zonogon tiling with canonical
lift a, Va(x)=x. Its rank-threshold de Bruijn curves are simple proper
disk arcs; same-color arcs are disjoint and different-color pairs cross
at most once. Positive v_i edges increase exactly coordinate i by one.
These are the same explicit dictionary hypotheses as accepted DG1.
The rank-two identity VJ=I and independent u,v force a nondegenerate
two-dimensional setting. The identity's first row gives

    u_x=sum_i J_i u>0,  v_x=sum_i J_i v>0.

The positive margin is fixed before epsilon and L. In particular this
argument does not have a constant uniform as kappa tends to zero. It
does not assume every ordered minor of J is strictly positive, and none
of the steps below needs that stronger assumption. Zero rows and
antiparallel rows are excluded by the two common positive directions;
parallel rows compatible with those directions cause no cutting error.
Degenerating-stratum interpolation remains a different problem.

DG1 supplies a path in the full tiling for coordinate-ordered vertices;
it does not by itself supply a path in an arbitrary cut patch. DG2
confines such a path by its endpoint lifts, with bound
M_V(K*ell+3E), M_V=sum_i ||v_i||. The whole segment neighborhood is
therefore required. CUT assumes exactly this stronger buffered region,
so it does not infer a local path from an endpoint-only buffer.

## 2. Shared corners and a valid integer mesh

Let d_D be a fixed maximum tile diameter. Select one vertex of one tile
containing each straight sample point, with fixed tie conventions. At
each straight corner the same selected vertex is used for the two
incident sides. The four selected corners are therefore genuinely
shared, rather than merely close in physical projection or lift.

For a sample point x and selected vertex w, ||w-x||<=d_D. At sufficiently
large L the buffer contains the selected sample tiles and vertices.
The affine error at w and the bounded term J(w-x) give

    ||a(w)-(Jx+c)||_infinity <= C1*epsilon*L+C0=E,

with C0 fixed by D and J. Equivalently one can use the uniform tile
gradient bound and the interpolated lift at x. C0 can harmlessly be
enlarged to a positive constant absorbing all rounding allowances.

Here is an explicit equal-step integer choice, completing the candidate's
order-of-magnitude statement. Set

    N=ceil(epsilon^(-1/2)),  ell=L/N.

For 0<epsilon<=1, (1/2)*sqrt(epsilon)*L<=ell<=sqrt(epsilon)*L.
If C1>0, choose sqrt(epsilon)<=kappa/(8C1); if C1=0 this restriction
is unnecessary. Require also

    L>=8C0/(kappa*sqrt(epsilon)).

Then E<=kappa*sqrt(epsilon)*L/4<=kappa*ell/2. This choice works for
both u and v, including translated opposite sides, because the same
fixed lower and upper bounds kappa,K hold for their coordinate
directions. Increasing L0(epsilon) accommodates tile diameter and any
remaining fixed constants. N is an actual positive integer and every
side ends exactly at its prescribed straight corner.

For consecutive samples, their actual lift difference in each
coordinate lies in [kappa*ell-2E,K*ell+2E], hence is nonnegative.
DG1 supplies a positive path, even if a particular coordinate increment
is zero. DG2 places every point of the subpath within

    R=M_V(K*ell+3E)=O_fixed(sqrt(epsilon)*L)

of its initial straight sample and therefore of its straight side.
No affine error along the unknown path is assumed to prove this bound:
coordinate monotonicity between its endpoint lifts gives it. Thus there
is no circular buffer argument. Choose the hypothesis constant C larger
than all fixed band and sample-tile constants; the constructed paths
then lie inside the region where the hypothesis is supplied.

A finite full tiling graph admits a deterministic tie rule among its
positive shortest paths. Concatenating the u-side then v-side, and the
v-side then u-side, gives two paths with the same chosen extreme corner
vertices. Every nonempty edge increases physical x by exactly one, so
each concatenation is simple and x-monotone. In fact its number of
edges is precisely the difference of its endpoint x coordinates,
L*(u_x+v_x)+O_D(1), and is O(L). Telescoping lift increments gives the
same conclusion. Empty subpaths, if any, create no exception.

## 3. All intersections lie in separated extreme-corner boxes

Put alpha=u_y/u_x and beta=v_y/v_x. Since det(u,v)>0 and both x
components are positive, alpha<beta. The straight lower chain is u
then v, and the upper is v then u. With s=x-x_left and
X=L*(u_x+v_x), their exact vertical separation is

    (beta-alpha)*min(s,L*u_x,L*v_x,X-s).

This equals the linear opening near either extreme corner and a
positive plateau, when present, between the two bends. It is at least

    c0*min(s,X-s,L)

for a fixed c0>0, for example
c0=(beta-alpha)*min(1,u_x,v_x). No separation between arbitrary curved
paths was presumed in deriving this estimate.

Let M=max(|alpha|,|beta|). If a point (x,y) on a constructed path is
within Euclidean distance R of the corresponding straight chain at
abscissa t, then |x-t|<=R and

    |y-f(x)|<=(1+M)*R

at a common abscissa. Linear endpoint extensions of f handle the
O(1)-shifted actual endpoint x ranges; those extra pieces are already
in the corner allowance. This is a graph error estimate derived from
the one-sided distance band, not an unjustified Hausdorff converse.

At an intersection, the straight-chain gap is at most twice this graph
error. The displayed gap estimate forces s=O(R) or X-s=O(R), once
epsilon is small enough that R is a small fixed fraction of L. Bounded
slopes and the R-band then place the entire intersection in the
corresponding O(R) Euclidean corner box. This includes common edges.
The boxes and a nonempty central x slab are disjoint after decreasing
epsilon0 depending on the fixed data.

The paths lie in a face-to-face tiling graph. They cannot cross
transversally inside edge interiors, or partly overlap primitive edges
without sharing their endpoints. All vertices are integral and an edge
has unit x displacement, so it has no other integer point in its
interior. Intersections are precisely common vertices or full common
edges.

## 4. Selecting one Jordan lens and checking both containments

The common initial selected vertex belongs to the initial corner box,
and the common final selected vertex to the final one. Choose A as the
last common vertex in the first box and B as the first in the second.
One deterministic implementation separates the common vertices by the
central x slab and uses the maximum initial and minimum final x. The
strictly increasing x coordinate puts these selections in the same
order along both paths. They are distinct, because there is a nonempty
central slab between their boxes.

There is no other common vertex between A and B: all common vertices
belong to one of those two boxes and the extremal choices exclude both
possibilities. A common retained edge would give another common vertex,
so it is excluded as well. The retained paths form a simple closed
polygon, hence a Jordan lens. On the central slab the first path is
strictly below the second by the graph-gap estimate. Their continuous
graph difference cannot change sign without another common point, so
this is the lower/upper order throughout the open retained x range.
Tangencies, shared pieces and small lobes removed near the original
extreme corners therefore cause no disconnected retained lens.

All retained boundary points are in a fixed multiple of the R
neighborhood of the straight parallelogram boundary. Since P_L is
convex, its enlarged convex set P_L+B_(C'R) contains the entire Jordan
lens, proving the outer containment. For the inner containment, choose
C2 large enough that the inner parallel set at distance C2*R misses the
two corner boxes and lies in the retained x range. At any such
abscissa its points are vertically farther than the graph-error bound
from either straight boundary chain, and hence lie between the two
retained graphs. This proves the inner containment directly, including
the side bends. Equivalently the connected inner parallel set avoids
the retained boundary and has a central point inside.

The missing end slivers are in O(R) corner boxes; elsewhere the
symmetric difference is in O(R) boundary bands. Perimeter is O(L), so
the area difference is O(L*R+R^2), with an additional O(L) harmless
unit-cell/tile rounding allowance. Since R=O(sqrt(epsilon)*L) and
epsilon<=1, this is O(sqrt(epsilon)*L^2+L). Constants may be absorbed
into the candidate's fixed C2, epsilon0 and L0. No assertion that this
lens is contained in P_L is needed. Insetting P_L can provide that
different version only while retaining its whole-neighborhood buffer.

The lens is a union of original tiles. Its boundary consists of tiling
edges, so no original tile interior is cut by that boundary. Jordan
separation puts the interior of each tile on one side; tiles inside
give the exact original tiling of the region. No abstract surface or
new packing is substituted.

## 5. Common global ranks and the direction of every pair reversal

Both retained paths run from the same actual vertex A to the same
actual vertex B. The ambient canonical lift assigns a unique vector
to either vertex, independent of the path used. Their common content
is exactly a(B)-a(A). This avoids the false implication that equal
physical endpoints alone force equal integer height vectors when V
has a nontrivial kernel.

A positive path crosses a color-i threshold curve precisely when it
traverses a v_i edge. Its i coordinate increases monotonically by one
on each such edge, so it crosses once exactly the ranks
a_i(A)+1,...,a_i(B), and crosses no other color-i curve. Crossings of
curves with boundary edges are at interior edge points, not at A, B or
any other tiling vertex.

Every retained full curve therefore meets the lens boundary exactly
twice, once on each path. Its portion in the lens is one connecting
proper arc: another component would require additional boundary
crossings or a closed component of the original simple proper curve.
A curve with no retained rank cannot have a bounded component in the
lens for the same reason. The ambient buffer keeps global curve ends
outside. Different-color retained arcs cross at most once; same-color
arcs do not cross. A crossing is at the center of an original ij tile
and cannot lie on the lens's tiling-edge boundary.

Here is an explicit orientation check for the crucial pair-order claim.
Orient a color-i curve so det(v_i,x) increases along it. At a positive
color-i boundary edge it crosses toward the left side of that oriented
edge. On the lower path this is into the lens, and on the upper it is
out. Thus every retained arc is oriented from the lower to upper
boundary. At an ij tile, i<j, the oriented tangents can be chosen as
+v_j and -v_i, with

    det(v_j,-v_i)=det(v_i,v_j)=j-i>0.

For two proper arcs oriented from the lower to upper boundary of a
disk, this positive crossing has i before j on the lower boundary and
j before i on the upper. The reverse endpoint ordering would have
negative algebraic intersection. Since there is at most one crossing,
it cannot be canceled by another crossing. Without a crossing their
relative endpoint order is unchanged. Consequently every changed
cross-color pair adds an inversion ij->ji, and an existing lower
inversion is retained. Same-color rank order is fixed on both paths.
This proves Inv(p) subset Inv(q), with exact global rank labels.

This argument is intrinsic to the retained disk and the original
curves. It does not assume a generic vertical sweep through an
arbitrary nonconvex tile patch, convexity of the profile space, or a
positive lower bound on all pair minors of J.

## 6. Finite strip encoding really recovers the input restriction

For fixed D, there are finitely many tile types and a uniform diameter
bound. A tile meeting a unit lattice cell has an integer origin in a
fixed finite set of offsets from that cell. The record of all incident
types and relative origins is therefore a finite alphabet. For this
upper counting argument one only needs records from actual tilings;
no free-boundary entropy theorem or unproved filling property is used.

Choose one full-tiling representative for each distinct input
restriction to P_L before applying CUT1. This defines an extraction
even though different full extensions could choose different outside
paths or canonical offsets. There are only finitely many physical
restrictions at fixed P_L in this local alphabet. A choice of one
representative does not inflate the number of input restrictions.

Put delta=C2*sqrt(epsilon)*L, enlarging C2 by all fixed geometric
constants from the preceding reconstruction. A tile whose data affect
P_L but cannot be recovered from the retained lens must meet the
delta boundary band of P_L, enlarged by at most the tile diameter.
Indeed every point of the inner parallel set lies in the lens. A tile
with a point farther inside than delta+d_D lies entirely on its inner
side and is an original lens tile. For local records, add the fixed
alphabet-neighborhood and unit-cell allowance as necessary. One can
take the deterministic set of relevant cells near the boundary with
width delta+O_D(1); no tiling-dependent discarded-region mask is needed.

This cell set has O(L*delta+delta^2+L) cells, uniformly in translation
of the parallelogram. This follows by covering it with the same strip
enlarged by a unit-cell diameter; its area is perimeter times width
plus a quadratic corner term. It is
O_fixed(sqrt(epsilon)*L^2+L). Recording one symbol per such cell costs
at most that many bits times a D-dependent alphabet constant. Relevant
tiles crossing P_L are contained in its bounded tile collar, available
under the hypothesis buffer at the chosen scale.

The lens output supplies every tile away from this strip. The strip
record supplies every remaining original local record relevant to P_L.
The fact that the lens may also contain tiles outside P_L causes no
loss: the reconstruction restricts the placed lens to P_L and combines
it with the original strip record.

If lens outputs are stored without their absolute placement, the two
boundary color words and one endpoint physical coordinate place the
entire boundary, since each color determines its edge vector. One
endpoint lift fixes the global rank offsets on every boundary edge.
Word lengths are O(L), giving O_D(L) bits including their lengths and
finite conventions. If physical and lifted coordinates range in an
O(L) box, their integer coordinates cost O_D(log L) bits. With arbitrary
global translations or lift offsets the explicit logarithms of their
coordinate ranges must be retained, exactly as the candidate cautions.
The exponential bound as stated is conditional on these bounded
coordinate ranges; there is no uniform O(log L) encoding of arbitrary
integers. Ranks within each color are forced, so no factorial matching
factor appears.

For a fixed lens output and identical auxiliary boundary, placement,
rank and strip records, two original restrictions agree at every
relevant cell of P_L. Thus the auxiliary code is injective on an output
fiber. Counting its possible values proves

    fiber size <= 2^O_fixed(sqrt(epsilon)*L^2+L)

under the stated coordinate-range qualification. This is an upper
fiber estimate. It permits no conclusion that an arbitrary different
tiling of that lens can be inserted into a chosen original outer
frame, much less into all large original zonogons.

## 7. Adversarial boundary cases and remaining scope

The exact mesh handles noninteger L and all positive sufficiently small
epsilon, with a joint L0(epsilon); no epsilon=0 statement is inferred
through tile rounding. The shared sample vertices prevent separate
corner rank offsets. Positive x edges rule out retracing or self-crossing
within a concatenation. All contacts between the two paths, including
shared edges and multiple small lobes, are removed by the last/first
intersection construction. The central positive separation prevents
A=B or an empty main lens.

Zero coordinate increments on individual mesh pieces are allowed by
DG1. Missing ambient colors would make the strictly positive long
affine approximation impossible at sufficiently small epsilon; the
claimed result need not treat such an empty-hypothesis instance as a
new stratum theorem. Parallel nonzero affine rows require no pairwise
margin in CUT1. A fixed near-parallel u,v with tiny det(u,v)>0 is
allowed only with data-dependent constants and epsilon0, not uniformly
as its opening vanishes. Arbitrary translations and large global ranks
retain their explicit coordinate cost in CUT2.

The accepted DG hypotheses were matched, the integer mesh and graph
estimates reconstructed, and all rank/pair/strip inferences checked
without computation. The candidate correctly leaves annular matching,
strict-slope transfer using any separate annulus theorem, excluded
strata, quantified profile recovery and all-scale remainder gluing open.
Its mention of a D=4 annulus candidate is a future interface only, and
I used no annulus assertion as a proof premise. Novelty remains
unestablished.

## 8. Source, integrity and operational provenance

The primary Arroyo--McQuillan--Richter--Salazar author text, Section 2,
printed pp.4-5, complete arrangement definition and Lemma2.2 proof,
was read directly in my preceding DG whole audit. The accepted DG
exposition and coordinator decision now supply that dependency. In
particular the source allows nonintersecting parallel arc pairs; the
disk adaptation is the accepted DG argument, not a generic claim that
all planar graphs have this metric. No new external theorem is needed
for CUT1/CUT2 beyond the stated dictionary and accepted DG.

The full candidate and accepted exposition, both freeze/decision
records and the current protocol were read. No peer CUT findings were
read. The current candidate, accepted dependencies and all seven older
own packets are fingerprinted and reverified unchanged in the
companion one-time metadata freeze. No candidate/shared-status edit,
Git action, spawning, paid API, contact, access bypass, new PDF download,
enumeration or CAS occurred. Metadata hashing is administrative only.
Fresh authoritative task-transition telemetry returned 20% total
weekly used, 10080-minute window, reset1792745187; the 90%-total ceiling
and integration reserve remain in force.
