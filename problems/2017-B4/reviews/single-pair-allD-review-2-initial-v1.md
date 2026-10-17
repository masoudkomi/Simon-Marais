# Initial independent whole audit R2: one merged pair for fixed D

2026-10-17 UTC. Reviewer /root/review_2022_complexity_r2 did not
construct this extension. Requested gpt-6.1-sol/max; independent
effective-setting readback unavailable. This full initial report,
per-inference ledger and source checks are frozen before any
peer single-pair-allD findings are read.

Target: complete coordinator-single-pair-allD-candidate-v1.md,
SHA-256 c0d51d61f110cf5a190344403d346940b06b95a6d1880c6c725d241c92c397b4,
with complete freeze-v1.json,
2714227e14b516d260a1c9d1c8cdef5ae7b9071ea8b9b9c7140b65b6ead520db.

**Finding:** SP1--SP3 reconstruct as the stated implication from
the exact RM1 disk/port background, for a single consecutive
merged pair and arbitrary fixed D>=3. I found no substantive
objection or needed mathematical repair. In particular the
singletons' number need not equal two, all integer dilations
have the same exact count bijection, and the reduced disk has
an actual small fixed full exterior. This review does not
silently promote the pending rank-mesh packet or infer
general lower-direction recovery from a type label.
Only the coordinator decides acceptance after both audits.

No simultaneous multiple-nonsingleton theorem, H, PR,
UR_D, all-D entropy induction, global assembly, official
limit or novelty is claimed. No mathematical computation,
enumeration or CAS was used.

## 1. Exact conditional background and the closed-face restriction

The [official 2017 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-2_1.pdf),
page2, B4, concerns fixed polygon tilings and both normalized
logarithmic limits. This note gives structural finite-D
interfaces only. All B4 is authorized; no other problem
or preliminary equation is investigated.

The accepted full marked dictionary is the complete
reviewed-fixedD-structural-v1.2.md and its acceptance.
The additional general-D RM1 statements are explicitly
conditional background in this candidate, not silently
accepted from an unreviewed theorem. The frozen v1
rank-mesh main packet still had an auxiliary arbitrary-window
scope issue at construction. That issue is not a premise
of SP1--SP3. A versioned repair arrived during this audit;
it will receive a separate targeted review after this
initial freeze, without altering these records.

Precisely the assumed RM1 data are: a full standard
zonogon tiling with canonical lift a; rank-r selected
arcs; selected cells F; residual biconnected Jordan
tile disks C; at most D(r-1) unselected full arcs
through F; and one consecutive residual fine chain
with two complete boundary ports in its one block.
The skeleton, fine rank labels and boundary heights
are retained. I reread RM1's exact construction and
the dimension program, while preserving their statuses.

Only colors k,k+1 are merged, 1<=k<D, with all other
D-2 groups singleton. Every forbidden tile has that
one pair type. The entire closed selected face is
disjoint from every forbidden whole tile, not merely
the interior of C. The face is interior to the full
tiled disk so its closed stars have full neighborhoods.
These hypotheses are indispensable to the following
closed embeddings and sign argument. No estimate
for an arbitrary window or for a small positive
number of forbidden events is used.

Empty residual cells contribute no disk. Every actual
C here contains tile cycles, hence positive area.
D=3 leaves one singleton group and a two-direction
coarse tiling; the arguments below still apply.
Constants may depend on fixed D, not on an unbounded
dimension or on the large source scale L.

## 2. Full deformation and connected limiting fibers

Let g(i) be the coarse group index, w_g=(1,g-1), and use

    v_i(t)=(1,t(i-1)+(1-t)(g(i)-1)).

For i<j and t>0 the determinant is

    t(j-i)+(1-t)(g(j)-g(i))>0.

At t=0 it vanishes only for the merged pair and is
positive on every other pair. The map F_t=V_t a
is continuous and affine on source tiles. Its
positive face determinants and complete convex
boundary of degree one give a full tiling
homeomorphism for every t>0. At edges, incident
positive tiles lie on opposite sides; at vertices,
the full cyclic ray order is preserved. Thus the
regular-point degree argument does not overlook
singular edge or vertex identifications.

The maps converge uniformly on the compact full
source disk to F0. For y in its image and
e_t=sup|F_t-F0|>0, consider

    K_t=F_t^(-1)(Z_t intersect closed_ball(y,2e_t)).

The target cap is compact, convex and nonempty.
Its inverse under the homeomorphism is compact
and connected. Every point of F0^(-1)(y) belongs
to K_t. Conversely, for any x_t in K_t,

    |F0(x_t)-y|<=3e_t.

Compactness gives a Hausdorff-convergent subsequence;
its limit is exactly the fiber, since it both
contains the fixed fiber and is contained in it.
A Hausdorff limit of nonempty compact connected
sets is connected. If e_t=0 at a positive t,
F0 is itself that homeomorphism and the assertion
is immediate. This proves connected fibers,
including boundary fibers, rather than presuming
it from an informal collapse.

## 3. Closed clean stars, Jordan embedding and the actual coarse tiling

Every point in the closed clean face, and in
particular every point of closed C, has no
forbidden incident tile. Its positive faces remain
nondegenerate at t=0. Distinct outgoing rays can
coalesce only at the consecutive pair directions
or their negatives. If both such rays occur,
their intervening fan sector would be the
forbidden pair tile; no other direction lies
between them. That sector has been excluded.
All remaining cyclic sectors stay positive.
Hence F0 is a local homeomorphism there,
including along edges and at the closed vertices.

A fiber through such a point has that point
isolated. Since the full fiber is connected,
it is a singleton. Thus F0 is injective on
closed C, and compactness makes its restriction
an embedding. The image Cbar is a genuine
Jordan tile disk. The same reasoning applies
on all of closed F, not only C, so references
below to a visit through F mean its embedded
image F0(F) with its unique fine preimages.

To check the coarse ambient tiling, an open
overlap of two positive limiting faces would
persist for small t>0, which is impossible.
Compact preimage limits give surjectivity onto
the limiting convex zonogon. The finite union
of positive closed faces must cover it: any
open gap could not be covered by the finite
collection of collapsed line segments.

Nor can a collapsed segment enter a positive
face interior. There the positive face gives
a local homeomorphism and an isolated fiber
point; connected fibers rule out any distinct
collapsed preimage. This also supplies a precise
justification for the candidate's persistence
observation at such a contact.

All image vertices are integer, and each
coarse edge has horizontal displacement one.
No image vertex can lie strictly inside a
coarse unit edge. Nonzero partial edge
overlaps are also impossible for integer
endpoints with those unit horizontal intervals.
Thus the positive limiting faces make a
face-to-face full coarse tiling, with collapsed
faces in its edge skeleton. The count and
curve arguments have an actual geometric
ambient tiling, not an abstract diagram.

## 4. SP1: singleton barriers and exactly one visit for every active curve

A singleton fine coordinate remains the
same coarse coordinate under coarsening.
Its global rank curve is the image of the
same fine full curve, with its rank and two
sides unchanged. It only crosses positive
faces, so no deleted pair event changes
its identity. RM1 therefore already gives
one residual fine chain and two ports if
that singleton curve meets Cbar.

A merged-group coarse curve can change
fine identity only in a collapsed forbidden
region. On a forbidden-free region it
follows one original fine color and rank.
Equivalently the coarse height is a_k+a_(k+1);
along a fine chain the other pair coordinate
is constant until a forbidden crossing.
There are no such crossings in closed F.

Such a curve cannot depart F through a
selected same-group barrier. A different
fine color would require a forbidden pair
tile; its own fine color cannot cross
itself or another curve of that color.
A coincidence along a same coarse rank
would not give a new crossing or exit:
the clean embedding preserves the distinct
fine preimages, and an interior active
chain cannot be the selected boundary arc.
No triple curve crossing at a cell corner
creates a bypass in the actual full tiling.

Therefore every departure crosses a
selected singleton barrier. Suppose there
is a later return to the same F.
Inside F the sign relative to that very
singleton proper curve is the original
one. Restoring it after the departure
requires a second crossing of the same
entire coarse singleton curve. A proper
arc cannot go around the barrier through
the disk exterior and then continue:
the coarse arrangement stays in the full
disk until its terminal boundary endpoint.
Different-color coarse curves cross only
once, so the return is impossible.

This argument uses a singleton identity
for the departure barrier; it does not
use that there are exactly two singleton
groups. It works with one or any larger
fixed number D-2. It would fail if the
barrier itself belonged to another merged
group and could change fine identity
outside F, which is why that extension
is not claimed.

The one visit through F has constant fine
identity. RM1 makes its retained tiles
one consecutive chain in one residual
block, with exactly two ports if nonempty.
Because clean Cbar has unique preimages,
there is no additional coarse visit to
Cbar unrelated to that fine chain.
Distinct active coarse curves yield
distinct unselected fine chains in F.
Hence their number is at most D(r-1).
This proves the whole SP1 port assertion.

## 5. SP2: arbitrary coarse fillings and fine rank recovery

Fix the full coarse exterior, the complete
Cbar boundary lift, all port ranks and
their original fine labels. An arbitrary
coarse filling with that boundary glues
to the exterior as an actual full tiling.
There are exactly the same two boundary
ports for each active coarse rank as in
the reference. No new active level can
have no port: it would be an internal
closed de Bruijn track, impossible in
the full arrangement. Two transverse
ports give one chain between them.

SP1 assigns the same fine color and
fine rank to both ports of each such
chain. Label the entire replacement
chain accordingly. Each face crosses
different coarse groups; since only
a consecutive pair was merged, its
two fine colors are distinct and
ordered in the original list.
Every resulting fine parallelogram
has positive determinant.

Assign increments +/-e_i to its oriented
edges. Opposite edges have the same
chain label, so the lifted increment
around every face is zero. Simple
connectivity of the Jordan disk makes
the integral path independent.
Fixing one boundary vertex lift fixes
all heights. The complete boundary
increments agree exactly with the
original fine boundary, so the
physical boundary is the original
Jordan curve of C, not a translated
or independently phased approximation.

On each replacement face the map to
fine coordinates is affine and positive.
Triangulating the faces gives positive
oriented triangles. At an interior
vertex their positive sectors have a
positive integer local winding degree.
The whole Jordan boundary has degree
one inside C and zero outside.
Two preimages, or a branch of degree
greater than one, would give at least
two regular preimages; an interior
image on the target boundary would
produce exterior regular preimages.
Both contradict these degrees.
Thus the integrated map is an actual
fine tiling homeomorphism. Convexity
of C is not being assumed here.

Every fine rank is recovered as well.
The integrated coordinate a_i has its
prescribed value at each port; its
half-integer level is constant along
the labeled chain. Hence the chain
has the original fine rank, rather
than a freely permuted name.
Coarsening returns the chosen
coarse filling, so this construction
is injective.

For the converse, the reference fine
C contains no forbidden tile. Green's
boundary identity gives

    integral_C det(grad a_k,grad a_(k+1))
      = integral_boundaryC a_k d a_(k+1)=0.

Every possible fine filling with the
same complete boundary has the same
integral. A tile of type(k,k+1)
contributes one and all others zero,
so the nonnegative total counts
forbidden tiles and forces their
absence in every filling.

Glue such a filling to the original
fine exterior. The outside incident
stars remain clean by the full
closed-F hypothesis, and the inside
has just been shown clean. Global
coarsening therefore embeds its
entire closed boundary and sends it
to exactly the fixed Cbar boundary.
The positive faces fill Cbar and
recover the inverse coarse filling.
This proves surjectivity and the
exact whole-count equality. Merely
forbidding tiles in the interior of
the reference without its closed
star condition would not supply
this inverse argument.

## 6. Every positive integer dilation

Dilate the original full fine
reference by M>=1 and subdivide
each enlarged tile into its M-by-M
grid. Canonical lifts scale by M;
every old port gives M ports at
the prescribed consecutive ranks.
An original rank r0 has copies
M(r0-1)+1,...,Mr0.
These assignments are fixed before
the replacement fillings vary.

In each enlarged tile the parallel
copies enter and leave opposite
edges in the same order. They
concatenate along the original
chain, so each reference copy
still has exactly two ports on
the dilated disk. Coarsening
commutes with the linear dilation
and grid subdivision, giving
exactly M Cbar.

The complete-boundary recoloring,
integration and degree proof
therefore works at each such M.
The fine boundary flux is again
zero and excludes every forbidden
tile in any alternative fine
filling. Thus both directions
remain inverse, proving

    Z_fine(MC)=Z_coarse(M Cbar)

for all positive integers M,
including M=1. No relation between
M and L, no new mesh choice and
no entropy-limit interchange are
needed. In particular this is
not an assertion of a power-law
supermultiplicative count bound.

## 7. SP3: deleting inactive curves gives one actual small exterior

Delete a full coarse curve only
when it does not meet Cbar.
Its half-integer height step has
constant sign on the connected
disk, so removing it changes
every disk height by the same
fixed coordinate step or zero.
The physical disk is changed
only by the corresponding fixed
translation. This includes its
whole boundary and port ranks.

Deleting a curve from a full
marked arrangement leaves the
full marked subarrangement:
every remaining different-color
pair still crosses exactly once
and all boundary ranks retain
their order. The accepted full
dictionary supplies its genuine
zonogon tiling. One can equally
remove the curve's tile ribbon
and identify its translated
sides, with positive faces and
the smaller convex boundary.
Since the curve is inactive on
Cbar, that operation is a
translation there. Repeat it
for every inactive curve.

At most D(r-1) total curves
remain, all active in the
reference. Their content in
each coarse color is therefore
O_D(r). The full outer boundary
has twice that many unit edges,
and its physical diameter and
perimeter are O_D(r). A disk
of positive area has at least
two active coarse directions;
other zero-content groups may
remain in the notation.

The recorded translation may
depend on the large source's
global ranks, but it is fixed,
not a choice per filling.
After recentering, the reduced
canonical coordinate range is
bounded by the kept content.
Any deleted level in a coarse
color lies on one fixed side
of the connected disk, so
the local rank shift is
constant as asserted.
The fixed active list recovers
the original global names.

Every alternative Cbar filling
glues to this one reduced
reference exterior with its
same complete boundary.
Consequently the disk belongs
to the stated actual small
full-exterior class GE_(D-1),
with fixed D-dependent
constants. Perimeter or
diameter alone is not used
as a substitute for that
exterior construction.

## 8. Conditional entropy application and scope

If recovery UR_(D-1) were
proved for this exact class,
the SP2 count equalities at
all M and SP3 exterior would
transfer its deficit bound
to the fine disks. This is
a conditional implication,
not a proof of UR_(D-1)
from a balanced-zonogon
formula or H_(D-1).

For D=4 it interfaces with
the separately reviewed UR3
target subject to that
target's acceptance. For
D>4 no lower-dimensional
recovery theorem is supplied.
There is no multiple-merged
group theorem, rare-event
smallness estimate, arbitrary
window discard, orientation
chart or strict transfer
premise hidden in SP1--SP3.
The earlier erased-event
obstruction is not removed
by terminology.

## 9. Whole-audit disposition and preservation

The reconstruction challenged
global limiting fibers,
closed versus interior
cleanliness, embedded F
versus embedded C, collapsed
skeleton contacts, singleton
sign restoration for all
D-2, empty and active
levels, two actual ports,
fine rank consistency,
boundary phases, inverse
surjectivity, Green's
nonnegative tile flux,
every integer dilation,
large global rank shifts
and the fixed small
exterior. No counterexample
or unresolved substantive
inference was found.

The conclusion retains
the explicit RM1 condition;
this audit does not accept
the auxiliary arbitrary-window
claim or promote a repaired
rank-mesh version before
its own targeted reaudits.
The author handles any
future substantive repair.

Only assigned single-pair-allD-
review-2-* review records
were created. No mathematical
program, search, enumeration,
CAS, candidate/shared edit,
Git, spawning, charge,
outside contact or separately
billed API occurred.
All declared target metadata
and prior own frozen records
are checked separately.
No peer SP findings were
read before this full
initial freeze.

Authoritative weekly use
rechecked2026-10-17
06:49:12UTC was27%
total,10080-minute
window, reset1792745187,
ordinary usage allowed.
The90% total ceiling
and integration/review
reserve remain in force.
