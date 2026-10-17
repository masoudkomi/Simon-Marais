# Initial independent whole audit R2: rank disks and uniform three-direction recovery

2026-10-17 UTC. Reviewer /root/review_2022_complexity_r2 did not construct
either target. Requested gpt-6.1-sol/max; independent effective-setting
readback unavailable. This full report, per-claim ledger and source
checks are frozen before reading any peer rank-mesh or UR3 findings.

Targets:

- rank-mesh-reasoning-r1-candidate-v1.md, SHA-256
  e0f2e55e62aabe5547120f4fc72c506c3f680844a90aa98ece7147d404178d27;
- rank-mesh-reasoning-r1-UR3-v1.md, SHA-256
  40ad9b252b6c34f5dee5c8cd3eedea8e8feeabb0cec1497b224bf5c32ba58aab;
- their complete freeze-v1.json, SHA-256
  7173ee9db5d7990af60ca0731a301d9017691e42f9c741efce1e81a7d90de747.

**Finding:** the core disk/port construction, special D4 clean lifting,
GE3 reduction, LC3 import and proposed uniform recovery reconstruct in
their stated substantive settings. I found one scope defect in the
auxiliary window-boundary loss sentence in RM1a: a perimeter bound alone
does not imply its O(rL+r^2) tube/loss for arbitrary rectifiable windows.
A connected Jordan-boundary qualification, or an appropriate boundary
component/tube hypothesis, must be stated. An exact family below refutes
the literal perimeter-only assertion. This issue is separate from
UR3's explicitly Jordan class and does not refute the core rank-disk
lemmas or the proposed LC3/UR3 argument.

I request a versioned author scope repair for that sentence and its uses.
Only the coordinator decides its disposition and any scoped acceptance.
This review is not a promotion, an entropy-rate evaluation, a proof of H,
or a novelty claim. No computation, enumeration or CAS was used.

## 1. Inputs and full-arrangement quantifiers

I read both complete candidates, obligations, worklog, source record,
source JSON and manifest. The official 2017 B4 domain and the accepted
integer tiling/marked-arrangement dictionary are the background.
The source is an actual two-dimensional full zonogon tiling, with fixed
D, integer contents 0<=N_i<=cL, canonical lift and all crossing ranks.
The repeated references to an outer disk require a genuine tiled disk;
a degenerate one-direction segment is not an implicit new disk case.
Zero-content colors inside a genuine two-dimensional instance are allowed.

The coordinator's program and clean-lens packet are leads and warnings,
not silently accepted premises. In particular the number S of designated
rare tiles is supplied as input; the packet does not derive a small S
from affine flatness. No annulus, CUT, strict-transfer or remainder
theorem is used as a premise. I reconstructed the new packet on that
basis rather than substituting one of those other results.

Select exactly ranks divisible by r in every color, r>=2. There are
m=O_D,c(L/r) selected proper arcs. Adding them successively cuts disk
cells by single proper arcs: leaving and revisiting an earlier sign
cell would restore an earlier arc's sign and hence cross it twice.
Thus selected cells are disks at the arrangement-curve level, with at
most 1+m+binom(m,2) cells. This argument includes parallel same-color
arcs and does not by itself identify the residual whole-tile domains.

## 2. RM1: whole tiles, pinches, ports and size bounds

An unselected tile contains no selected midpoint arc and its interior
lies in one selected cell. For a fixed cell F let K_F be its retained
whole tiles, and G_F their edge graph. If a bounded face of G_F were
not an original tile, a tile across a boundary edge on that face's
side could not be a retained neighbor: two non-skeleton neighbors
sharing an edge are not separated by a selected arc and belong to
the same K_F. It must be a skeleton tile. A selected arc through it
can be followed to the original exterior without meeting G_F:
it traverses only skeleton tiles, crosses their selected-rank edges
at midpoints and never passes a vertex. This contradicts enclosure
by the bounded face. Thus all bounded faces are original tile faces.

The biconnected decomposition is essential. Each tile four-cycle is
in one block, and two tile cycles sharing an edge are in the same
block. A block containing tile cycles has a simple outer cycle;
a repeated outer-face vertex would be a cut vertex. Its bounded
faces cannot hide another block or an unfilled region. More explicitly,
the original tile incident on the inside of any such face-boundary
edge has its four-cycle in that same block, since it shares the edge.
The face is consequently that tile. The filled block is a genuine
Jordan disk. Splitting at cut vertices duplicates vertices, not tiles
or edges, and does not assume edge connectivity alone removes a pinch.

Every unselected full arc meets F in at most one interval by the same
sign argument. Its skeleton crossing tiles can only be at the entry
and exit selected boundaries of that interval. All intervening tiles
form one consecutive retained chain, sharing opposite edges of its
color. Their tile cycles are therefore in one block. If nonempty,
the chain has exactly two boundary ports; empty chains contribute none.
Every retained boundary edge is such a port: an edge of a selected
rank would have skeleton tiles on both sides and could not adjoin a
retained tile. This proves the aggregate, not per-block, perimeter
bound 2n_F.

There are at most r-1 unselected ranks of a color between consecutive
selected ranks, also in either end tail. Hence

    n_F<=D(r-1),
    sum_(blocks in F) boundary_edges<=2n_F,
    number_of_retained_tiles<=binom(n_F,2).

The last assertion counts crossings of pairs of residual arcs, each
pair at most once. Every height coordinate ranges over an interval
of length at most r in F, including outer-boundary cells and colors
with no selected rank. From x=Va,
diam(F)<=r sum_i ||v_i||. These metric and perimeter estimates check.
There is no unspecified thickening or rank pairing in the disk class.

## 3. RM1a: finite skeleton code and rare-face loss

A selected color-i arc crosses at most sum_(j!=i)N_j=O_D,c(L)
tiles. Thus its whole-tile skeleton has O_D,c(L^2/r+L) tiles.
The proposed finite-word code is sufficient. Its start edge and
rank are predetermined by N and the selected label. Traversing
the i-arc in increasing det(v_i,x), a j crossing displaces the
next i-edge midpoint by +v_j for j>i and -v_j for j<i.
The other-color crossing word therefore recovers every tile's
geometry. Starting coordinates of the lift are known on the
outer boundary; the j coordinate starts at 0 or N_j and changes
by one with the recorded orientation. Thus the same code recovers
all crossing ranks and integer lifts. It does not need log L
coordinate choices at every tile. Double recording of a
selected/selected tile only enlarges this valid upper code.

A tile is cut by at most its two incident selected arcs, so its
closed tile meets at most four selected cells. Selected arcs never
pass vertices, so no extra cells appear merely by vertex contact.
At most 4S faces are marked by S rare tiles. The RM1 tile bound
then gives O_D(Sr^2) retained tiles in all such faces.

After the skeleton code, one bit per known selected face costs
O(L^2/r^2+L/r+1), absorbed into the stated total. The marked
complement domains are now fixed. Their possible tile origins
belong to the domain and a bounded tube about its boundary.
A reference filling by K tiles bounds its perimeter and component
count by O_D(K), while each tile has area bounded below.
Thus those known domains have O_D(K) possible local records,
not an independent coordinate factor per filling. Taking
K=O_D(Sr^2) proves the O_D,c(L^2/r+Sr^2+L+1) bit bound.

Good block boundaries and lifts are fixed after conditioning.
Arbitrary fine fillings glue to the fixed exterior. They cannot
create a new selected-level track inside a block: all such
ports are absent on the fixed boundary, so it would have to be
closed, impossible for an oriented de Bruijn track. A zero
boundary flux for a rare pair similarly forces zero rare events
in every filling, because each relevant tile contributes the
same nonnegative unit to that boundary integral.
These are valid whole-tiling facts, not consequences of a
small numerical rare count alone.

### Open issue RM2-01: perimeter alone does not control all window boundaries

The following auxiliary sentence of RM1a requires an explicit domain
qualification: a rectifiable window of perimeter O(L) is said to
incur additional loss O_D(rL+r^2) when faces meeting its boundary
are discarded. This follows for one rectifiable Jordan boundary,
and is the usual tube estimate for the intended simple windows.
It is false if rectifiable window means an arbitrary bounded region
with rectifiable boundary and only the stated perimeter bound.

Here is a counterexample entirely inside an actual full grid tiling.
Take D=2, v1=(1,0), v2=(1,1), N1=N2=N, L=N, and r=2.
The full zonogon is tiled by its forced N-by-N type12 grid.
Selected ranks are the even ranks. Skeleton tiles have at least
one even rank; each interior selected cell contains a whole
odd/odd retained tile. There are Theta(N^2) such cells.

In rank coordinates, an interior selected cell can be written

    2s-1/2<a1<2s+3/2, 2t-1/2<a2<2t+3/2.

Its retained odd/odd tile occupies
[2s,2s+1] times [2t,2t+1]. Choose a small physical circular
hole centered at the point with rank coordinates
(2s+5/4,2t+1/2), of radius 1/(10N). For large N it lies
strictly inside that selected cell and in a skeleton tile,
away from the entire retained odd/odd tile. Make one such
hole in each of a quadratic number of interior cells.
All holes are disjoint and separated by a fixed distance.

Let the window be the large grid parallelogram minus these
open holes. It is connected, bounded and has rectifiable
boundary of total length

    O(N)+Theta(N^2)*2pi/(10N)=O(N).

All retained odd/odd tiles remain fully inside the window,
because the holes were placed only in the skeleton.
Nevertheless the boundary meets every one of those
selected cells. The prescribed boundary-discard operation
therefore loses Theta(N^2) retained tiles, whereas
rL+r^2=2N+4 is only O(N). This is an analytic family,
not a numerical probe. The same example is within the
stated zero-content-color allowance at D=4, or can be
placed in a large type12 block of a full four-color tiling.

The repair should restrict this auxiliary claim to Jordan
windows or to windows with a controlled connected boundary/tube.
With b boundary components a safe general tube bound keeps
an additional O(br^2) term, with the appropriate geometric
hypotheses on their rectifiable curves. Perimeter alone
does not bound b. The main whole-zonogon skeleton estimate
and the explicitly Jordan GE3 argument do not use this
false generalization. The author should state the intended
window class and check all references to its additional loss.

## 4. RM2: global coarsening and embedding of a clean closed disk

Move fine vectors continuously to consecutive-group vectors,
with first coordinate one and positive ordered determinants
before equality. At a positive parameter the affine-on-tile
map has positive determinants and maps the outer boundary
once around the convex target zonogon. Degree one gives
one preimage for every regular image point: positive
tile-interior preimages cannot overlap or leave a hole.
The cyclic fan at an edge or vertex supplies local degree
one there as well. Thus these maps are homeomorphisms
of the full disks.

I checked the connected-fiber limit rather than assuming
monotonicity of a collapse. If epsilon_t is the uniform
distance between F_t and F0, then

    F_t^-1(Z_t intersect closed_ball(y,2epsilon_t))

is compact and connected, since the image set is convex.
It contains every point of F0^-1(y). Every Hausdorff
limit lies in that fiber, because the distance of its
F0 image from y is at most 3epsilon_t. Hence it converges
to exactly that fiber, which is connected. If epsilon_t=0
for a positive parameter, F0 is already a homeomorphism.

A clean closed selected face has no incident forbidden
tile, including outside tiles meeting it. Every point of
its disk blocks therefore has a full neighborhood with
no collapsed face. In the limiting fan, two equal
outgoing group rays would require an intervening
within-group tile, excluded by that hypothesis.
All remaining faces have positive determinant and the
local map is a homeomorphism. Each fiber meeting the
closed disk thus has an isolated point; a connected
fiber with an isolated point is a singleton. Compactness
then gives an embedding of the entire closed disk,
not only its open interior.

Positive coarse faces do not overlap, since an open
overlap would persist before the limit. They fill the
coarse zonogon; the remaining images have zero area.
A collapsed face cannot lie in the interior of a
positive face, again by persistence before the limit.
Integer vertices and unit horizontal edge displacement
exclude partial-edge subdivision. This gives an actual
coarse full tiling with a Jordan embedded disk.
The excluded incident tiles are precisely what prevent
the earlier erased-event boundary-identification obstruction.

## 5. RM2: the D4 two-port restriction and exact lifting

For one merged pair and two singleton groups, a singleton
coarse rank curve is the same fine rank curve and has its
one residual chain by RM1. A merged curve can change
fine identity only at a deleted within-group event.
Such an event cannot meet the good closed face. It
cannot cross a selected same-group barrier there,
since that would itself be a forbidden within-group
tile. A visit which reaches a retained tile must
therefore leave the selected face across a singleton
selected barrier. To return it must restore that
barrier's sign, crossing the same unchanged singleton
coarse rank curve twice. The full coarse arrangement
excludes this. Within its single visit the fine
identity is constant; its retained chain is one RM1
block chain, with exactly two ports.

This is not a proof for several nonsingleton groups.
A selected barrier in another merged group could change
fine identity outside the face, defeating this specific
sign argument. The packet explicitly excludes that extension.

For an arbitrary coarse filling with the same complete
boundary, glue the unchanged full coarse exterior.
The global coarse rank at every boundary port is fixed,
so each active level has the same two ports as in the
reference, with no closed track inside. Each such pair
has one assigned fine color/rank in the clean reference.
Recoloring the track by that assignment matches both
fine ports. This uses complete ranked heights, not
only a multiset of port colors.

Every coarse face crosses two different consecutive
groups, so its two assigned fine vectors have positive
determinant. Their edge increments close around each
face, and the disk is simply connected, so they
integrate to a fine physical map with exactly the
original fine Jordan boundary. Positivity and degree
one give a genuine nonoverlapping fine tiling.
Coarsening it recovers the chosen coarse filling,
so the map is injective. Conversely the boundary
integral for every forbidden pair is zero in the
clean reference; every tile contribution is nonnegative,
so every fine filling of that complete boundary has
no forbidden event. It coarsens back. Whole counts
therefore agree.

Integer dilation repeats each boundary port M times
at its consecutive multiplied ranks. The reference
dilation fixes these copies and their colors. The
same lifting argument applies at every integer M;
there is no hidden re-pairing choice.

## 6. RM2a and RM3: reductions, actual GE3 class and error sum

For a zero-row color, absence of all its incident tiles
in the full neighborhood makes its coordinate constant
on the closed disk. Deleting its tracks changes the
disk by a translation and fixed rank shift. Remaining
singleton curves retain their identities and ports.
This is a three-direction reduction for one deleted
color; no antiparallel chart is inferred.

For a two-group clean image there is only one coarse
parallelogram type, hence the geometric grid filling
is fixed. Each straight track segment in the disk
reaches its boundary; the compatible fine boundary
assigns its constant fine identity. No internal
group event permits a switch. This proves uniqueness
for that endpoint separately from the special
three-group port theorem. It is not a claim that
regions with remaining defects have zero entropy.

For the three-direction class, every active coarse
curve has at most two ports on the disk, and their
total number is O_D(r). Delete all inactive full
curves. A deleted curve is disjoint from the connected
closed disk, hence its height contribution there
is constant. The disk is translated with a fixed
rank shift, while the remaining full arrangement
supplies an actual small-zonogon exterior with
O_D(r) curves in each color.

Changing the three ordered directions continuously to
standard unit lozenges preserves all ordered positive
determinants and gives the same degree-one
homeomorphism. Complete boundary words/ranks and
tile counts remain fixed. Every alternative filling
glues to the same exterior. Thus each resulting
Jordan disk really lies in GE3_C0(r), for a fixed
D-dependent C0. This is stronger than an arbitrary
ragged disk of bounded diameter and perimeter.
Its scalar height extends to a uniformly Lipschitz
height on a convex ambient domain of diameter O(r).

Several disk blocks may come from one face. The
aggregation uses the correct aggregate perimeter
O_D(r). For area a<delta r^2, isoperimetry gives

    a<=sqrt(delta) r sqrt(a)
       <=sqrt(delta) r perimeter/(2sqrt(pi)).

The sum of small-block areas is O_D(sqrt(delta)r^2).
At most O_D(1/delta) blocks of area at least
delta r^2 remain. An error eta(r)r^2 per substantial
block therefore sums to O_D(eta(r)r^2/delta).
Over O_D(L^2/r^2+L/r+1) faces this gives the stated
normalized O_D(sqrt(delta)+eta(r)/delta), after
L grows with r,delta fixed. For positive small eta,
delta=eta^(2/3) gives O_D(eta^(1/3)); eta=0 can
be handled with an arbitrary small delta and then
letting it decrease. Fine/coarse tile-area constants
are fixed. No one-error-per-face shortcut is used.

## 7. Primary CKP import: LC3's exact quantifiers

I directly read the corrected arXiv v3 source's
approximation definitions in section1.6, relevant
analytic setup, Proposition3.2 and the complete
statements/proofs in section4. Theorem4.3 is stated
for any simply connected lattice R satisfying the
chosen approximation tolerance to one fixed limiting
domain and height data, with sufficiently large n.
Its proof first fixes a finite mesh for the target
height, then the boundary tolerance and local
triangle estimates. It is not merely convergence
for one preselected region sequence. Printed page13
explicitly extends the results to unit lozenges.
The import may therefore be used at that fixed-triangle
quantitative level, with consistent entropy units.
The entire 49-page analytic derivation is an
attributed theorem, not newly reproved here.

The refined from-within metric really does require
closeness to restrictions of every admissible
limiting height, not only matching boundary values
on nearby geometric points. LC3 supplies it: if Q
contains the tau-inset of T, each point of its
inner boundary is O(tau) from the outer boundary.
For h in AH(T,p), both h and affine p have a
uniform global Lipschitz bound on convex T and
agree on its boundary. Thus |h-p|=O(tau)
there, uniformly over h. Adding the Q boundary
error gives the required refined height approximation.
The inset also bounds missing area by O(tau).
Triangle corners have positive angles and are
not the excluded cusps.

For fixed p, applying the quantitative height-neighborhood
estimate to p gives LC3's lower bound on the total count.
For the upper bound, use the stipulated fixed exterior
to extend every Q filling to T. These extensions have
one Lipschitz and value bound. As tau decreases to zero,
any subsequential limit is admissible with boundary p.
Closed convex gradient constraint and boundary
convergence justify this compactness assertion.
Thus the extensions eventually lie in any chosen
open neighborhood of compact AH(T,p).

For each h in that compact set choose a sufficiently
small source height neighborhood whose count has
entropy at most its integral plus the chosen error.
Finitely many cover AH(T,p); choose a common boundary
tolerance and maximum n threshold. Extension is
injective on Q fillings, and restriction to Q puts
each one in a corresponding source neighborhood.
The finite sum costs only o(n^2) bits. Concavity
and the boundary-determined average gradient give

    integral_T sigma3(grad h)
       <=area(T)sigma3(grad p)

by Jensen. This includes boundary slopes, where
the density is zero; there is no division by a
positive density or a minor.

Finally the affine gradient set P is compact and
the normalized constant parameter is bounded.
Apply the fixed-p comparison at finitely many
centers, shrink their tolerances to cover nearby
planes, and use continuity of sigma3 to compare
their affine entropy values. This gives one tau,n0
for the compact affine family. I found no missing
uniformity in this source step. Entropy per domino,
lozenge and physical area and natural/base2 logs
differ by fixed constants; sigma3 must and can be
defined in one consistent log2-per-physical-area
normalization throughout. No numerical density
is imported with an unstated conversion.

## 8. UR3: compact profiles, actual triangle cores and codes

Every GE3 filling extends to the same convex
O(r)-diameter zonogon. Bounded local scalar
gradients integrate along straight segments there,
so the normalized heights have a common global
Lipschitz and range bound. A scalar Lipschitz
extension to a common fixed box supplies compactness
without claiming admissibility outside the ambient
zonogon. On a triangle eventually contained in B,
the closed convex gradient set P passes to uniform
limits by weak-* compactness.

The gamma-scale mesh and quantized values give a
sup-norm cover with logarithm
O_C0(gamma^-2 log(2/gamma)). At gamma=1/log(r+2)
this is o(r^2). Choosing the largest profile fiber
therefore loses only o(r^2) entropy; an actual
reference height in it has a uniformly convergent
subsequence, and every filling in that fiber has
the same limiting profile.

For a fixed triangular mesh of side ell, the
crossing tiles lie in a fixed-width tube about
O(r^2/ell+r) mesh length. A finite local mask
records them in that order of bits. Scalar
heights on all cut-band/mesh vertices have
O(r) possible values after normalization,
costing O((r^2/ell+r)log(r+2)) more bits.
At ell a fixed positive fraction of r this
is o(r^2). Both geometry and the complete
height phase are conditioned on, not just
the positions of cuts.

Inside a closed mesh triangle wholly within B,
all tiles meeting a sufficiently deep fixed
inset are retained whole tiles. Generic paths
inside the convex inset cross tile edges and
connect these tiles; their cycles belong to
one biconnected block Q. A removed crossing
tile has an interior path to the triangle
exterior, so the same no-hole argument gives
a Jordan Q. All omitted components lie in
the fixed-width strip. Its lattice sites
bound Q's area loss and perimeter by O(ell+1).
This proves U2, including the fixed inset.

The cut code determines Q independently of
which remaining internal tiling is chosen.
The retained physical region is exactly
the triangle minus the known crossing tiles;
vertex-pinch components of that fixed filled
region are intrinsic, not hidden choices
of the internal edge graph. Every boundary
edge of the main component adjoins a cut
tile or the mesh boundary. Its height
vertices are in the recorded cut band.
Thus every member of a conditioned fiber
has the same complete Q boundary.
Keeping the reference exterior extends
every Q filling to the whole triangle;
integer reference dilation does the same
for M Q in M T.

## 9. UR3: the contradiction and all orders of limits

Assume a positive deficit a r_j^2 along r_j to
infinity. After the subquadratic profile cover,
choose an actual reference height h_j converging
uniformly on the fixed box to h.
Fix kappa and the uniform LC3 tolerance tau.
For this one h, differentiability almost
everywhere gives a sufficiently fine mesh
of normalized side lambda<=epsilon on which
all but an epsilon area fraction is within
a sufficiently small multiple of tau lambda
of an affine plane. No family-uniform
differentiability modulus is asserted.

Take ell_j=floor(lambda r_j). Mesh rounding
is O_lambda(1/r_j) in normalized coordinates.
There are finitely many mesh triangles, so
a subsequence stabilizes the list contained
in B_j. On the interiors of retained limit
triangles h has gradient in P. The flatness
planes can be chosen with slopes in P:
one may use differentiability points, or
project the slope of a close plane to the
average gradient of h on the triangle.
The boundary integral bounds that slope
change by a constant times its height error
divided by lambda. Choosing the initial
flatness tolerance smaller absorbs this
fixed constant. Thus no inadmissible
interpolant slope is smuggled into LC3.

Local additive height constants may be
recentered at one known boundary point of
each triangle core before using LC3.
This is only a gauge change for the count;
the recorded absolute height is restored
for gluing. It ensures the normalized
constant parameter lies in a common
bounded interval independently of lambda.
For large j, uniform convergence of the
whole fiber then gives the stated
tau ell_j-scale approximation to those
admissible planes.

Because B_j is explicitly Jordan with
perimeter O(r_j), its boundary triangles
lie in an O(ell_j)-tube of one rectifiable
curve and cost O(lambda r_j^2+ell_j^2).
Unlike the auxiliary RM1a sentence, this
use has the needed topology. Failed-flatness
triangles cost O(epsilon r_j^2), and the
fixed-width mesh strips cost O(r_j/lambda+1).
Conditioning on cuts and heights loses
only o_j(r_j^2) bits.

Restriction into the fixed Q_j,t cores
and the discarded region is injective.
A region with A lozenges has at most3^A
tilings by recording the partner of each
up-pointing unit triangle. This does not
require its discarded region to be
simply connected. It gives U3, including
the profile and cut-code losses.
Upper LC3 gives

    log2 Z(Q_j,t)<=E_j,t+kappa ell_j^2.

For each fixed j, dilate its one reference
and keep the exterior of all M Q_j,t
unchanged. Exact complete boundaries
make insertions independent and
recoverable by restriction. Thus

    Z(M B_j)>=product_t Z(M Q_j,t).

LC3 applies at n=M ell_j with the same
relative approximation: a fixed-width
original core strip becomes an M-width
strip, but its relative width is
O(1/ell_j), already below tau for large j.
It need not decrease with M. The actual
quantitative LC3, uniform over those
approximating Q, is what justifies the
lower comparison. For each fixed j the
finite list admits a common sufficiently
large M threshold. No threshold uniform
over all j is required.

The lower estimates give U5. Since
sum_t ell_j^2=O_C0(r_j^2), combining
them with U3/U4 gives

    Delta(B_j)/r_j^2
       <=O_C0(kappa+epsilon+lambda)+o_j(1).

Choose kappa and epsilon small relative
to a, lambda<=epsilon for the limiting
height, then j large, and only then take
M to infinity with each j fixed.
This contradicts the presumed positive
deficit. It establishes the proposed
uniform eta_C0(r) tending to zero
for this globally extendable Jordan
class, subject to the two-review
promotion gate. No exact supermultiplicative
Z(MB)>=Z(B)^(M^2) is used.

## 10. Disposition and limits

All principal RM1/RM2/RM2a/RM3 and LC3/UR3
inferences were reconstructed above. The
primary source supports the needed fixed-triangle
quantitative reading and explicitly supports
lozenges. It is not used as a theorem for
varying ragged limiting domains. The local
gauges, fixed exteriors, block aggregation,
complete heights and orders of limits are
material and must be retained.

RM2-01 remains open: the auxiliary
rectifiable-window perimeter-only loss
requires a versioned scope correction.
Its counterexample does not alter the
explicitly Jordan UR3 class. The author
should repair that claim and check
affected obligations; the original
candidate and this report must remain
unchanged. Both independent targeted
reaudits and coordinator reconciliation
are required for a substantive repair.

Rare-count extraction, antiparallel
orientation, macroscopic window selection,
summed boundary costs, strict transfer,
balanced remainders and global recovery
remain separate. No H or official full
2017 limit is proved here. No mathematical
program, enumeration, CAS, candidate/shared
edit, Git, contact, charge or separately
billed API occurred. Latest root-authoritative
weekly total was25% at06:09:36 UTC,
reset1792745187, with90% total ceiling
and review/integration reserve.
