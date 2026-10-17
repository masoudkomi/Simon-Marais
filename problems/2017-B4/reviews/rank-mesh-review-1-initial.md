# Rank mesh and UR3: independent whole initial audit R1

2026-10-17 UTC. Reviewer `review_2021_reasoning_j15_r2`.
Requested gpt-6.1-sol / max; no independent effective-setting readback.
This report is a recommendation, not coordinator promotion.

## Identity, independence, and disposition

The audited main candidate is
`notes/rank-mesh-reasoning-r1-candidate-v1.md`, SHA-256
`e0f2e55e62aabe5547120f4fc72c506c3f680844a90aa98ece7147d404178d27`.
The audited analytic supplement is
`notes/rank-mesh-reasoning-r1-UR3-v1.md`, SHA-256
`40ad9b252b6c34f5dee5c8cd3eedea8e8feeabb0cec1497b224bf5c32ba58aab`.
Their complete freeze has SHA-256
`7173ee9db5d7990af60ca0731a301d9017691e42f9c741efce1e81a7d90de747`.

I did not construct these results or contribute their disk adaptation.
Both whole texts, the obligations, worklog and source packet were read
before this report. I read no other new rank-mesh/UR3 review or findings.
The preceding strict-transfer audit was completely frozen before I opened
this packet; it is not used as a premise here.

**One standalone domain repair is required:** the RM1a assertion for an
unspecified rectifiable window, main lines 173-178, is false if windows
with arbitrarily many boundary components are allowed. RMR1-01 below
gives a full hand counterexample, including failure at fixed r. Requiring
a Jordan window, or accounting for the number of boundary components,
repairs that particular interface. The author should supply a versioned
full statement; this reviewer has not edited the candidate.

Separately, the RM1 disk/port construction, skeleton and rare-cell code,
restricted D4 RM2 lifting, RM2a, and RM3 aggregation withstand this audit
in their stated scopes. I also reconstructed the analytic supplement:
the quantified CKP import supplies LC3 for the strengthened triangular
class used here, and the subsequent UR3-GE contradiction has no separate
substantive gap found in this audit. In particular I do not recommend
leaving LC3 accepted merely on the basis of pointwise convergence for
one boundary; the uniform extraction is explained explicitly in Sections
9-12 below. The counterexample to the window helper does not apply to
UR3's expressly Jordan disks.

The whole packet should not be accepted without resolving RMR1-01.
No H, full official entropy rate, general multiple-nonsingleton lifting,
or orientation reduction is established by these local results.

## 1. RMR1-01: perimeter alone does not control a perforated window's tube

Main lines 173-178 assert that a rectifiable window of perimeter O(L)
has additional rank-face deletion loss O_D(rL+r^2), lower order at fixed r.
No Jordan or bounded-boundary-component condition is included there.
A connected window with many small holes is a counterexample.

Take D=2, v_1=(1,0), v_2=(1,1), N_1=N_2=L with L an even integer,
and the unique full parallelogram grid tiling. Fix r=2. Selecting the
even rank curves leaves Theta(L^2) interior selected faces; each such
face contains its one odd/odd unselected tile. Choose a point strictly
inside that tile in every one of these interior faces and remove a
closed round disk of radius L^-3 around it. The disks are disjoint and
stay away from the selected curves for sufficiently large L.

Let the window be the interior of the outer parallelogram minus all
these tiny disks. It is connected and has a finite rectifiable boundary.
Its outer perimeter is 2L(1+sqrt(2)), and the total hole perimeter is
Theta(L^2)*2pi L^-3=O(1/L). Its perimeter is therefore O(L), exactly
as in the written helper. But every one of the Theta(L^2) interior
selected faces touches a hole boundary. Discarding all boundary-touching
faces removes Theta(L^2) residual tiles, whereas the claimed bound at
r=2 is O(L). The r-tube itself has quadratic area in this example.
This is not a computation, a multiple-window charge, or an exotic tiling;
it is one perforated connected planar window in a fixed two-color grid.

For one connected rectifiable boundary curve, the familiar tube estimate
does give O(rP+r^2), with P its length. For b separate boundary curves,
the direct bound is O(rP+b r^2), before exploiting any overlap. Thus a
Jordan-window hypothesis or an explicit component term is needed.
If “window” was intended to mean Jordan throughout, that intention must
be stated at this new assertion. The later GE3 and UR3 disks already
are Jordan and do not invoke this missing generality.

## 2. Full arrangement and curve-level cells

The starting object is an actual two-dimensional full marked zonogon
tiling, with absent colors allowed. Its proper ranked de Bruijn arcs,
same-color disjointness, different-color single crossings, absence of
triple crossings and fixed endpoints are explicit input hypotheses.
They are not inferred from a locally incomplete wiring patch.

For the selected rank-multiple arcs, add curves successively. A new
curve cannot visit one previously constructed cell twice: the two visits
would have the same separating-sign vector, requiring some previously
crossed arc to be crossed again. Hence its intersections with a cell
form at most one proper arc. Cutting a disk by such arcs preserves
disk cells. The cell count is at most 1+m+binom(m,2), including parallel
selected pairs which do not cross.

For any one selected cell, the selected signs fix one gap between
successive selected ranks of each color. Each gap, including the two
outer tails and colors with no selected rank, has at most r-1 unselected
arcs. Thus n_F<=D(r-1). The continuous height coordinate a_i has range
at most r in the cell: its bounding selected levels differ by r, and
the endpoint tails are no larger. Since x=Va(x), the diameter is at
most r sum_i ||v_i||. A cell touching the original outer boundary causes
no missing metric or rank case.

## 3. RM1: residual holes, pinches, blocks and ports

An unselected tile has no selected midpoint arc through its interior.
Two unselected tiles sharing an edge cannot be separated by a selected
arc across that edge: a selected-rank edge would put both incident tiles
in the skeleton. Hence adjacent unselected tiles belong to the same
selected cell.

Suppose the residual edge graph G_F had a bounded non-tile face. An
edge on that face has a skeleton tile on its non-residual side, because
an unselected neighbor would be in the same K_F. The skeleton tile's
interior and center lie in this graph face. Its selected arc runs to
the original outer boundary while avoiding G_F: it travels through
skeleton interiors, crosses only selected-color edges with skeleton
tiles on both sides, and never visits a vertex. It can continue past
its outer endpoint into the exterior. This contradicts the bounded
face. Thus every bounded G_F face is an original tile face.

Now take a biconnected block containing tile cycles. Its outer face is
a simple cycle; a repeated boundary vertex would separate its incident
sectors and be a cut vertex. A bounded face of this block cannot contain
an unfilled hole of G_F. Nor can a hanging block fill such a face: the
portion between its attachment and the block's cycle would be a bounded
non-tile face of G_F. Therefore the cycle encloses exactly the block's
own tile faces, giving a Jordan disk. Two tile cycles sharing an edge
belong to the same block, and a tile cycle cannot split between blocks.
This handles actual vertex pinches without declaring the whole K_F
to be a Jordan domain.

Follow one unselected full arc through F. It visits F only once.
Skeleton tiles on this visit can occur only where its other crossing
arc is selected, namely at entry or exit. All intermediate tiles are
one consecutive residual chain, joined across opposite edges of its
color, hence belong to one block. If nonempty, the chain has exactly
two boundary ports, including when one end is at the original boundary.
Every block boundary edge is such a port: an adjoining residual tile
would share its cycle block. Consequently the aggregate perimeter over
all blocks is at most 2n_F, rather than that quantity for each block.
Each residual tile is a crossing of two of these n_F arcs, with no pair
repeated, so the aggregate tile count is at most binom(n_F,2).

The no-selected-arc case is included: F is the whole original disk and
these are the usual full-grid bounds. A zero-area original object is
not the closed outer disk used by this proof; the local theorems are
conditional on the actual disk input. Empty residual cells give no patch.

## 4. RM1a: skeleton decoding and rare-cell conditioning

There are O_D,c(L/r) selected arcs. Each crosses exactly sum_(j!=i)N_j
other arcs, so the selected tiles total O_D,c(L^2/r+L). A fixed ordered
list of their crossing-color words is an adequate finite-alphabet code.
Its starting edge and midpoint are fixed by the outer content, color
and rank. Orient an i-arc by increasing det(v_i,x). Crossing color j
then changes its midpoint by +v_j if j>i and -v_j if j<i. This recovers
the actual tile position, not merely its combinatorial type. The other
height coordinates begin at 0 or N_j at that fixed endpoint and change
by one with the recorded crossings. They therefore recover the crossing
rank and every tile's lifted vertices as well. Duplicated recordings of
selected/selected tiles do not increase the asymptotic cost or create
an unrecorded pairing choice.

A whole rare tile meets at most four selected faces, including closure
contacts. A selected arc does not run through a tile vertex or along
an edge, so additional faces cannot touch a rare tile only at a vertex
without also being one of its at most four curve-cut sectors. Hence
at most 4S faces are bad. Their residual tiles total O_D(Sr^2).

The known skeleton fixes all complement domains, and a bad/not-bad bit
per face costs O(L^2/r^2+L/r+1). A fixed reference filling bounds the
number of possible tile origins in the bad domains plus a fixed-width
boundary allowance by O_D(the number of reference tiles): cover the
allowance by bounded neighborhoods of those reference tiles. A presence
mask for the finitely many types then costs O_D(Sr^2) bits. No independent
logarithmic coordinate is needed per tile. For general D the alphabet
has binom(D,2) types; the text's phrase “six” is literally the D=4
specialization and should be adjusted editorially (N1 in the ledger).

After conditioning, each residual Jordan block has its complete geometry
and boundary heights fixed. These are geometric components separated by
the fixed removed skeleton, so another filling does not change the
block domains at a vertex pinch. Arbitrary fillings glue with the fixed
exterior. A new selected-level component cannot be born inside: there
are no selected-rank ports on its boundary, and a full de Bruijn track
cannot be closed. When a prohibited pair has zero lifted boundary flux,
its count stays zero in every filling. The core conditioning estimate

    O_D,c(L^2/r+S r^2+L+1)

is justified. It is the subsequent arbitrary-window helper, not this
estimate, that needs RMR1-01's domain repair.

## 5. RM2: global degeneration and embedding of a clean closed disk

For positive deformation parameter before group equality, keep all fine
directions strictly ordered. Each tile map is orientation preserving,
and the full outer boundary maps once around the corresponding convex
zonogon. Positive local degrees and the cyclic fan order give a local
homeomorphism at edges and vertices as well. The degree-one boundary
then rules out overlaps and gives a full-disk homeomorphism F_t.

The connected-fiber argument for F_0 is valid. Let e_t=sup|F_t-F_0|.
For a nonempty fiber above y, the compact set

    F_t^-1(Z_t intersect closed_ball(y,2e_t))

is connected, contains the whole fiber, and every Hausdorff limit of
these sets lies in that fiber by uniform convergence. Compactness of
the fixed source disk gives a subsequential limit, which is exactly the
fiber and is connected. If e_t=0 there is already a homeomorphism.

The closed selected face in RM2 avoids every forbidden tile, including
incident tiles outside the chosen disk. Therefore every point of C has
a full forbidden-free star. Its limiting tile faces retain positive
determinants. Two outgoing rays could merge into the same group ray only
if an intervening fan sector contained a within-group tile, excluded
by the closed-star condition. Thus F_0 is locally a homeomorphism at
every point of C. A connected fiber with an isolated point is a singleton.
It follows that F_0 embeds the entire compact C, including boundary and
vertices; its image boundary is Jordan.

Positive coarse faces cannot overlap, since a positive interior overlap
would persist for t>0. Images of collapsed faces cannot enter a positive
coarse face's interior for the same reason. Surjectivity follows by a
compact preimage limit from Z_t to Z_0. Primitive unit-horizontal integer
edges exclude a vertex or partial-edge subdivision in an edge interior.
The limiting positive faces consequently form the actual full coarse
tiling used by the port argument.

## 6. RM2: the restricted two-port theorem and exact lifting

In D4 with one merged pair and two singleton groups, a merged coarse
curve can change fine identity only at a deleted within-pair event.
Inside the closed clean F no such event exists, so a visit there is
one fine residual chain. It cannot exit through a selected same-group
barrier: that would require either a same-color crossing or an incident
within-group event. An exit must cross a selected singleton barrier.
To return to the same F the sign of that very singleton curve would
have to be restored, contradicting the single-crossing full coarse
arrangement. This proves a single visit and hence two ports in one block.
Singleton curves retain their original fine identities and RM1's ports.
The proof really uses singleton barriers and is not a general
multiple-nonsingleton-group theorem.

For any alternative coarse filling of the fixed complete Jordan boundary,
glue to the unchanged full coarse exterior. Each relevant rank curve has
the same two boundary ports, and no extra closed component. Its reference
ports therefore assign one fine color and rank consistently to that
entire interior track. Every coarse face uses different consecutive
groups, so its assigned fine vectors have positive determinant. Fine
edge increments close around every face and, by simple connectivity,
around every loop. Integrating gives the original fine Jordan boundary.
Positive faces and boundary degree one give an actual fine filling.
Coarsening it recovers the original replacement, proving injectivity.

Conversely the fixed lifted fine boundary has zero flux for each
within-group pair. On a tile its height-minor integral is 1 for that
pair and 0 for the other types. Green's identity therefore makes the
number of prohibited tiles zero in every fine filling. Coarsening is
again an embedded clean filling and reverses the construction. Thus
the complete fine and coarse counts agree in this restricted situation.

Under integer dilation each port becomes M ports at consecutive ranks.
Both occurrences inherit the same fine-color assignment. The same
argument applies after dilation; it does not assert the much stronger
inequality Z(MC)>=Z(C)^(M^2).

Deleting a zero-row color acts by a fixed translation on a closed disk
with no incident tiles of that color; the remaining three singleton
tracks retain their ports. With only two compatible positive direction
groups, the coarse grid is fixed, and each of its straight track
segments has its fine identity prescribed by its boundary endpoints.
The compatible fine filling is unique. The unproved antiparallel
orientation reduction is explicitly outside these conclusions.

## 7. RM3: the actual GE3 class and per-face aggregation

Delete every inactive full coarse curve. Its height-step contribution
is constant on the connected disk, so the disk changes only by a
translation and fixed rank shift. There are at most n_F active curves,
by the two-port theorem. Their remaining full arrangement supplies a
fixed exterior in an O_D(r)-strand three-direction zonogon. Deforming
its three ordered directions to standard lozenges is a positive
full-disk homeomorphism and preserves words and counts. Every disk
filling glues to that same exterior.

The scalar height on the resulting convex ambient zonogon is globally
Lipschitz, by integrating its three bounded tile gradients along a
straight segment. This supplies a uniform extrinsic bound even for a
ragged disk with a long intrinsic detour. The actual disks therefore
belong to GE3_C0(r) for one fixed C0; diameter and perimeter alone
would not have supplied this fact.

Aggregate perimeter in one selected F is O_D(r), and area is O_D(r^2).
For blocks of area A_B<delta r^2, isoperimetry gives

    A_B<=sqrt(delta) r sqrt(A_B)
        <=sqrt(delta) r perimeter(B)/(2sqrt(pi)).

Their total area is O_D(sqrt(delta)r^2). There are O_D(1/delta)
remaining blocks, so a uniform per-disk deficit eta(r)r^2 contributes
O_D(eta(r)r^2/delta) there. Summing over the actual O(L^2/r^2+L/r+1)
faces and taking L to infinity at fixed r,delta yields the stated
O_D(sqrt(delta)+eta(r)/delta) normalized loss. Choosing
delta=eta(r)^(2/3) for positive small eta gives O_D(eta(r)^(1/3)).
If eta is zero, no positive deficit needs paying. The estimate does
not pretend that one selected face supplies only one substantial block.

## 8. The scalar compactness and cut-core geometry in UR3

Every B filling extends to a fixed convex ambient zonogon of diameter
O_C0(r); normalized heights have one uniform bound and Lipschitz constant.
An ordinary Lipschitz extension to a common box is used only for
compactness, not declared admissible outside the ambient region.
Sampling on a gamma mesh and quantizing values gives a cover with
log2 N(gamma)=O_C0(gamma^-2 log(2/gamma)). With gamma=1/log(r+2),
this logarithm is o(r^2). On a retained open triangle the gradient
constraint survives uniform limits because its admissible set P is
closed and convex.

For a triangular lattice mesh of side ell, all crossing tiles lie in
a fixed-width neighborhood of total line length O(r^2/ell+r).
Their finite-alphabet masks and all relevant integer heights cost
O((r^2/ell+r)log(r+2)). For ell comparable to a fixed lambda r this
is o(r^2). Heights, not just geometry, are recorded, so no phase or
boundary-height fiber remains free.

In a triangle lying wholly inside B, a sufficiently deep fixed inset
meets only unremoved tiles. Generic interior paths connect their tile
cycles through edges; points at contact vertices are covered by the
closures of these cycles. They lie in one biconnected block Q. A
removed tile reaches across the triangle boundary through its own
interior, excluding a residual hole by the same escape argument as RM1.
Thus Q is Jordan and contains the fixed inset. All other blocks and
all omissions lie in a bounded-width triangle strip. Its lattice-edge
count bounds both omitted area and perimeter by O(ell+1), uniformly
in the reference tiling. This proves U2 without assuming the entire
residual tile set is connected.

The known crossing tiles and triangle lines determine Q's physical
domain. Every boundary vertex is on a recorded band or a mesh line,
so its height is fixed by the code. Each alternative Q filling extends
by the chosen reference outside Q to an admissible height on the
whole triangle. Under integer dilation it has the same property.

## 9. LC3: exact primary input and its uniform reading

I directly inspected the exact v3 primary source, including its
from-within approximation definition, complete Theorem 4.3 proof,
triangular Corollary 4.2 and printed-page-13 lozenge statement. I have
not claimed an independent reconstruction of the full external analytic
proof. The source check identifies the imported result and its limits.

The relevant quantified input is a fixed-target height-neighborhood
estimate: after fixing a smooth limiting domain, admissible target h
and a desired entropy tolerance, an approximation tolerance and a
sufficient lattice scale work for the inner regions satisfying the
specified approximation. The fixed target here is a triangle, never
the varying ragged B/r.

This is supported by the proof's parameter order, not inferred just
from the phrase “a thermodynamic limit.” Fix h and a target tolerance.
Its finite triangular approximation is chosen first. The local estimates
on that finite mesh have finitely many scale thresholds. The region
enters through its boundary-height approximation and the area omitted
near the limiting boundary. For LC3's regions, the inset condition
bounds that omitted area uniformly; no jagged part can enter the
interior mesh. Taking the maximum of the finite thresholds gives one
n0 for these approximating Q. This is a uniform-in-Q statement for
the fixed target, not convergence only for a predetermined list of Q.

The strengthened LC3 hypotheses verify the source metric. Because
Q/n contains the tau-inset and lies inside T, every point of its
boundary is O(tau) from the outer triangle boundary. Every admissible
h with boundary p is globally Lipschitz on convex T. At an inner boundary
point x and a nearest outer point y,

    |h(x)-p(x)|<=|h(x)-h(y)|+|p(y)-p(x)|=O(tau).

Combining this with the actual boundary's tau error verifies the
approximation of the restrictions of every such h, uniformly. The
area difference is O(tau); it also converts normalization by the
actual region area into the displayed n^2/area(T) convention.

For fixed affine p, the lower bound is the fixed-target estimate at
h=p; the near-p set is a subset of all Q fillings. For the upper
bound the fixed exterior extends each filling to a height on T with
one uniform Lipschitz bound. As tau decreases, every subsequential
limit has boundary p and gradient in P, hence belongs to compact
AH(T,p). Thus these extensions lie uniformly near that compact set
for sufficiently small tau. Choose source upper-count neighborhoods
of its members and a finite subcover. Take the minimum input tolerance
and maximum scale threshold for this finite list. Counting a finite
union adds only o(n^2) to its logarithm. Restriction from extended
heights does not identify two different Q fillings.

For any h in AH(T,p), the boundary fixes its mean gradient to grad p.
Concavity of sigma3 gives

    integral_T sigma3(grad h)<=area(T)sigma3(grad p).

This supplies the required common upper value. Continuity of sigma3
and a finite cover of the compact affine-slope parameter set make
the tolerances and n0 uniform over p. Heights may be recentered at
one vertex; this keeps affine constants bounded and does not change
tiling counts. Frozen slopes are included by continuity and the same
compact argument, with no division by a slope margin. The density
is consistently defined in log2 per physical area; no numeric density
value or unchecked conversion coefficient is used elsewhere.

These steps establish LC3 for the precise strengthened class used in
the supplement. In particular this audit does not import the source
as a direct theorem about all varying GE3 boundaries, nor use a
balanced-hexagon formula to replace the source obligation.

## 10. Admissible planes and the moving triangular mesh

Choose the largest profile fiber and one actual height h_j in it.
Compactness gives a uniformly convergent subsequence h_j to h; all
heights in the fiber converge to the same h because its radius tends
to zero. Fix kappa, then the uniform LC3 tolerance, and choose a
sufficiently fine mesh for this one limiting Lipschitz h.

The admissible-plane assertion can be checked through actual tangent
planes. Outside a set of arbitrarily small area, differentiability
has a common small approximation radius. A small mesh triangle meeting
that good set lies uniformly near a tangent plane at one of its
interior good points. For a retained triangle, h is admissible in its
interior, so that tangent has gradient in P. A discarded exceptional
area controls the triangles with no such good point. Choosing the
initial approximation tolerance with a fixed safety factor supplies
the tau lambda/10 error in the text. One need not project an arbitrary
inadmissible mesh interpolant into P without justification.

At fixed normalized mesh lambda, ell_j=floor(lambda r_j) perturbs
coordinates by O(1/r_j). There are finitely many triangle indices;
take a subsequence on which the wholly-contained list stabilizes.
Every compact subset of a retained limiting triangle is then inside
B_j for large j, proving the admissible-limit assertion just used.
The fiber error divided by the fixed lambda tends to zero. Thus all
heights in the selected fiber, and its reference, are near the same
admissible plane on each retained triangle at the required physical
scale ell_j.

When LC3 is applied to one triangle, subtract its reference vertex
height for that local comparison. Counts and fixed-boundary insertions
are unaffected, and the affine constant after division by ell_j is
uniformly bounded. Original absolute cut heights remain in the code;
this analytical recentering introduces no new gluing choice.

## 11. Boundary losses, fiber upper count, and dilation lower count

The B_j boundary is explicitly a single Jordan curve of length at
most C0 r_j. Its O(ell_j) tube therefore has area
O_C0(lambda r_j^2+ell_j^2). This valid one-curve estimate is precisely
why RMR1-01's perforated-window counterexample does not affect UR3.
Failed-flatness triangles cost O(epsilon r_j^2); a bounded-width mesh
strip costs O(r_j/lambda+1). The code is subquadratic at fixed lambda.

After conditioning on cut geometry and heights, all cores Q_j,t and
their complete boundaries are fixed. The remaining reference region
has the displayed O((epsilon+lambda)r_j^2+r_j/lambda+1) lozenge count.
For any finite tileable lozenge region with A lozenges, each up-pointing
triangle chooses one of at most three matching neighbors, so its count
is at most 3^A even if this discarded region has several components
or holes. Largest-fiber inequalities therefore give U3, including both
subquadratic code losses.

The LC3 upper bound gives log2 Z(Q_j,t)<=E_j,t+kappa ell_j^2. The
reference filling, including the exterior of all cores, has an exact
integer dilation to M B_j. Arbitrary fillings of the disjoint M Q_j,t
can be inserted independently because their colored edges and heights
match exactly. Thus Z(M B_j)>=product_t Z(M Q_j,t). Applying LC3's
lower bound with n=M ell_j gives U5. Its boundary and inset errors
scale homogeneously, and a sufficiently large j already makes the
fixed inset error small relative to ell_j.

For each fixed j there are only finitely many cores. Taking M to
infinity after fixing j is exactly the order in Delta(B_j); the
finite sum of liminf bounds suffices. No uniform M threshold across
infinitely many j is required.

## 12. UR3-GE contradiction and its limits

Suppose normalized deficits stay above a>0 along r_j to infinity.
The previous upper and lower estimates give

    Delta(B_j)/r_j^2<=O_C0(kappa+epsilon+lambda)+o_j(1).

The sum of ell_j^2 over the finitely many mesh triangles is O(r_j^2).
Choose kappa and epsilon small relative to a, then lambda<=epsilon
small enough for the fixed limiting h. Take j large, and only then
the M liminf at each fixed j as above. This contradicts a positive
deficit. Bounded total entropy makes the normalized supremum finite,
so the absence of such a sequence gives eta_C0(r) tending to zero.
Finiteness of the number of boundaries at each fixed r alone is not
used to deduce this convergence.

All GE3 inputs are retained: complete Jordan boundary and height,
fixed small full exterior, and every filling extending to that exterior.
No varying-domain smoothness is presumed for B_j/r_j, and no
all-D entropy theorem is inferred. The result still leaves rare-flux
estimates, orientation charts, macro windows, all-scale balanced
remainders and the official H/global recovery argument outside this
packet. Those omissions are stated targets, not silently accepted
theorems.

## 13. Review freeze and required repair

RMR1-01 should be resolved by a full versioned author statement and
both reviewers' affected re-audits. The original helper and this
counterexample must remain preserved. N1 is only the general-D alphabet
wording correction. The other scoped deductions have no additional
substantive objection found in this whole audit, including LC3/UR3-GE.
The coordinator alone decides what can be promoted after reconciliation.

No mathematical computation, enumeration, CAS, search program, package
installation, Git operation, shared-file edit, spawning, charge or
external contact occurred. Only `reviews/rank-mesh-review-1-*` files
were written. Public tools read the exact primary PDF; I make no claim
of independently hashing a downloaded PDF binary in this task. All
thirteen constructor/input records and earlier own packets are checked
unchanged by the administrative freeze. Latest coordinator telemetry
reported 25% total weekly used, reset 1792745187; cutoff 90% total with
reserve. The complete report, issue ledger, source checks and manifest
are frozen before this substantive objection is reported or compared.
