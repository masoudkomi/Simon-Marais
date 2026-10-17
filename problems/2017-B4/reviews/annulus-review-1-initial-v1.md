# Blind whole reconstruction of annulus A1--A5

2026-10-17 UTC. Reviewer `review_2021_reasoning_j15_r2`, fresh
nonconstructor. I did not construct the annulus packet. No peer annulus
report, issue ledger or findings were read before this report and its
companion records were frozen. Requested gpt-6.1-sol/max; independent
effective-setting readback unavailable. No enumeration or CAS was used.

## Disposition

The principal geometric construction works once the rank-range condition
from A1 is explicitly retained in A2. A1, the range-corrected A2 proof,
the strictly positive winding criterion A3, digital comparability and
bounded trimming A4, and the exact block-gluing limit A5 all admit the
independent reconstructions below. I found one statement-level issue:
A2 says that I(h) is an ideal but does not explicitly require its
heights to be in the available rank box. With an absent inner color,
its empty rank interval does not supply that missing lower bound. The
literal set formula erases a negative coordinate. An exact small inner
patch in a large outer zonogon demonstrates the failure.

If the author intends I(h) to be a partially defined symbol whose
domain is, by A1, already the rank box, that convention excludes the
example. That interpretation should be made explicit in the standalone
A2 statement. The mathematically necessary condition is

    0<=a_i<=b_i<=N_i for every color i.                    (R)

It also puts every intermediate positive-path boundary height in that
box. This is a localized statement repair, not a counterexample to A3:
the six winding tests in A3 independently imply the required range.
I recommend resolving AR1-01 before promoting unqualified A2. I do not
recommend accepting an arbitrary-window extension, a boundary-stratum
theorem, H or the full 2017 problem.

Input candidate SHA256:
`020d3f6408f9423b83ac2d5633d3e508a7468a16ebe6db673879fca2af1ff610`.
The worklog, sources and constructor freeze are also included in the
metadata validation. No candidate, shared status or frozen older report
was edited.

## 1. Word order, positive planar shellings and A1

Rank occurrences within each color, with initial total order by color
and rank. An inversion is a pair of initially ordered labels that occur
in the opposite order. For p<=q, at the first mismatching position move
q's desired next label left through the intervening current labels. Each
such label must be smaller in initial order: otherwise the move would
remove an inversion required by the current lower word but absent from
q. Same-color ranks cannot be crossed because both words preserve that
rank order. Each swap therefore adds an inversion that q requires.
Iteration gives the claimed chain within the interval.

For i<j, swapping ij to ji raises the physical path at the sole
intermediate integer x position, by j-i>0, and raises it pointwise
throughout the intervening x interval. The region added is the positive
ij parallelogram. All previously added interiors lie below the current
path, so new interiors are disjoint. This proves actual planar shelling
of the weak lens. Every edge has integer endpoints and x displacement
one, so no integer vertex can occur strictly inside an edge. There is
no folded abstract surface or unnoticed partial-edge subdivision.

For the common-comparison poset P0, an inverted pair of p0 is forced
in both endpoint orders; a noninverted pair of q0 is also forced in
both. All remaining pairs are precisely the optional inversions in
Inv(q0) minus Inv(p0). Thus its linear extensions are exactly the
weak-order interval. Same-color ranks are forced by P0. The intersection
of the two total orders is transitive, so no separate transitive-closure
assumption is missing.

For h **in the rank box**, its initial rank set I(h) is the prefix of
an extension if and only if it is an ideal. Necessity is immediate.
For sufficiency, list I(h) in p0 order and then its complement in p0
order. All predecessor relations from the complement into I(h) are
excluded by ideality. Every prefix of the resulting list is then a
valid extension prefix.

Fix colors i<j, write s=h_i, and let b_p(k) count j's before the kth
i. Inversion inclusion gives `b_p0(k)<=b_q0(k)`. A selected i_s forces
all j's through b_p0(s) to be selected. Conversely, an unselected
i_(s+1) cannot be forced before a selected j; this is exactly
`h_j<=b_q0(s+1)`. The integer vertical slice of the closed projected
weak lens is therefore

    b_p0(s)<=h_j<=b_q0(s+1).

The conventions at s=0,N_i correctly include the vertical beginning
and ending boundary segments. Identical projected paths give just that
path; shared vertices or edges present no exception. Testing all six
pairs checks every cross-color comparison of P0, with internal rank
prefixes already imposed. A1 is correct with its stated rank-box domain.

## 2. AR1-01: A2 must preserve the rank-box domain

Here is an exact diagnostic for the standalone statement. Take the
outer content `(10,10,10,10)`, p0 the ascending block word and q0 its
block reversal. Their physical lens is the convex zonogon Z_10 and is
Jordan. Their common-comparison poset is just the four separate chains
of same-color ranks: there are no forced cross-color comparisons.

Use an inner **single type-13 tile**, with words p=13 and q=31 and
content `m=(1,0,1,0)`. Place its initial physical vertex at `(16,24)`.
Its four assigned heights are

    a=(7,-2,7,4),
    a+e1=(8,-2,7,4),
    a+e3=(7,-2,8,4),
    b=(8,-2,8,4).

These are legitimate integer lifts: `V(1,-2,1,0)=0`, and a differs
from `(4,4,4,4)` by three times that kernel vector. The physical
vertices are `(16,24),(17,24),(17,26),(18,26)`. The whole inner tile
lies strictly inside Z_10. Indeed every point also has a representative
`(4,4,4,4)+alpha e1+beta e3`, with alpha,beta in [0,1], strictly inside
the coefficient cube [0,10]^4. A surjective linear map sends a small
open neighborhood of each such representative into an open neighborhood
inside the zonogon. Compactness of the tile gives positive distance
from its outer boundary.

All four sets given by the literal formula I(h) are ideals of P0:
their color counts are respectively `(7,0,7,4),(8,0,7,4),
(7,0,8,4),(8,0,8,4)`. The active inner ranks are valid global rank 8
of colors 1 and 3. The intervals for absent colors 2 and 4 are empty,
so the instruction to identify inner ranks with global ranks imposes
no lower bound for color 2. Thus this boundary case is not repaired
merely by saying that the active ranks must exist.

Nevertheless the prescribed negative color-2 height cannot extend to
the outer frame. Every full outer tiling has its color-2 height in
[0,10], by the ten ordered boundary-to-boundary color-2 de Bruijn
curves and the boundary lift based at zero. Equivalently, these are
the only globally available rank levels. There is no annulus matching
the assigned inner boundary.

The displayed A2 construction exposes the precise failure: restricting
p0 to I(a) ends at height `(7,0,7,4)`, not a. Its physical endpoint is
`(18,26)`, not the designated initial vertex `(16,24)`. The proposed
word A p B consequently places a different inner patch. Ideality alone
cannot recover the coordinate discarded by the set formula.

This does not invalidate A1, which explicitly assumes its range, or
an interpretation of A2 explicitly carrying that domain forward. The
repair is to add (R), or explicitly declare that using I(h) in A2
includes h belonging to the domain `[0,N] intersect Z^4`. Retaining
empty inner colors then causes no difficulty. The issue ledger leaves
that statement correction to the author/coordinator.

## 3. A2 reconstructed with the necessary range

Assume (R) and the ideal tests. Then I(a) and I(b) really have the
coordinate counts a,b. The restriction A of p0 to I(a) ends at Va,
and the restriction B to the complement of I(b) begins after Vb.
Every prefix of A is an ideal, since I(a) is an ideal and p0 is a
linear extension. Every prefix through the middle p or q is an ideal
by hypothesis. Appending B preserves the extension because any
predecessor remaining outside I(b) occurs earlier in p0's restriction.

Hence both A p B and A q B lie in the full outer interval. Their
middle comparison follows from p<=q with the same rank shift. Outer
lower and upper shellings therefore exist. They fill exactly the
regions below A p B and above A q B respectively. The remaining
positive-area region is the designated inner lens, with its given
tiling. Pointwise order makes interiors disjoint and fills all of
Omega0. This is a genuine tiled annulus with possible common pieces
in the two cut bands; it does not require each cut band itself to be
a Jordan lens.

The entry seam A has all its x coordinates at or before the inner
left endpoint, since each edge increases x by one. B lies at or
after the right endpoint. Neither passes through the inner interior.
Their coincident portions are matched in height, not just in physical
space. The construction leaves no corner sector unfilled. It also
determines every boundary edge's color rank, so there is no later
strand-permutation choice.

For fixed a,p,q, choose all shellings before the interior is varied.
Restriction to the fixed designated physical core recovers each input
tiling, proving injectivity. For varying codes with O(L) letters and
O(L)-sized integer a, there are only polynomially many offsets and
exponentially-in-O(L) many word pairs. Length bookkeeping adds a
polynomial factor. Given one code and one output, its core tiling is
determined by restriction. The total fiber bound is consequently
2^O(L). This is a counting injection/fiber bound, rather than an
assumption about entropy of an unconstrained annulus.

## 4. A3: winding, all six projections and rank offsets

The outer physical Jordan loop is its lower word forward followed by
the upper word backward, and is counterclockwise. For each i<j,
the positive determinant of M_ij preserves that orientation. If x is
inside and distance at least t from the physical boundary, then
`M_ij x+c_ij` is inside the affine image and its boundary distance is
at least `sigma(J)t`. The displacement of h_ij(x) is at most
sqrt(2)E1. Condition (3) therefore puts h_ij(x) in the same interior
component and more than sqrt(2)E0 from the affine boundary. This
argument works even when the Jordan lens is nonconvex: the entire
ball below the distance to the boundary stays in the interior.

The outer boundary lift differs from the affine loop by at most
sqrt(2)E0 in this projection. The straight pointwise homotopy avoids
h_ij(x). Winding is thus unchanged and equals one. A projected loop
of two ordered E/N paths has positive unit winding in each open
lobe, zero outside, with coincident path pieces cancelling. It has
no negatively oriented lobe. Collapsed steps of the other two colors
do not affect that loop. Hence h_ij(x) lies in the projected lens.

All six projections give the A1 comparisons. They also give the
missing rank-range condition: each projected lens is contained in
`[0,N_i] times [0,N_j]`. In fact winding one places the point off its
boundary. Thus every h_i is in the available interval, and A3 may use
the range-corrected A2 proof without an additional hypothesis. Corners
a,b are among the tested inner boundary vertices. Their possibly
nonzero rank offsets are checked by the same six tests.

The constants are correct: vector infinity error E becomes at most
sqrt(2)E in a two-coordinate Euclidean projection, and the least
singular value multiplies physical boundary distance from below.
There is no use of convex admissible profiles or an interpolated
gradient. The homotopy is only a boundary-loop winding calculation;
actual tiles are supplied by the shellings.

When using a frame translated by physical Vz and height z, apply A1
to **relative** heights h-z and rebase physical coordinates by Vz.
The corresponding affine offset is
`c'=c-(I-JV)z`, still in ker V. Its affine error is exactly the same.
This is a rank translation, not a permutation or a new free phase.

The stated collar is a sufficient distance condition for a chosen
outer frame satisfying its hypotheses. It does not by itself assert
that a fixed-shape parallelogram can surround every differently shaped
lens with only that small area overhead. The candidate's final open
cut-window interface must retain this distinction.

## 5. A4: positive directions, digital words and comparability

All row vectors are nonzero. Relative to the first row, every other
row angle is in (0,pi), and positive pair minors order those angles
strictly. Their total angular spread is less than pi. The common
strictly positive dual cone C is therefore a nonempty open cone.
It contains independent rational u,v with det(u,v)>0. Scaling by a
common integer clears all denominators of Ju,Jv, producing positive
integer vectors a,b. The displayed two-by-two determinant identity
follows from multiplication by the two-column matrix (u,v).

Choose rational phases in (0,1)^4 outside the finitely many hyperplanes
for simultaneous events on 0--a or 0--b. Each coordinate has exactly
a_i or b_i events and no endpoint event. Integer translations of a
segment preserve all phases, so repeated segments give exactly U^m
and Vword^n.

For each pair i<j the projected side vectors a_ij,b_ij have positive
coordinates and positive determinant. The continuous chain first
m a_ij then n b_ij is below the reverse chain at every common first
coordinate. At the kth i threshold, that coordinate is the same
`k-1+theta_i` for both chains. The common j threshold set is likewise
unchanged by their integer translations. The lower chain has therefore
passed no more j thresholds. This proves the b_lower(k)<=b_upper(k)
inequality for every ranked i, with no rounding reversal. All six
pairs give the full weak-order comparison for every m,n>=1. Zero
remainder powers in A5 are handled by the empty word.

Along one side, event-prefix counts differ from the straight height
point by at most one coordinatewise. During an event edge, associate
the same event time to both endpoint counts; both still differ by
at most one, and linear interpolation preserves that bound. Applying
V gives a fixed physical error. Applying I-JV gives a fixed affine
lift error because that operator annihilates a and b. Translated sides
and their junctions satisfy the same bounds. No full-plane multigrid
extension is used.

Both words contain every color, so their powers and the one switch
between word types have a fixed bounded color gap. Its constant depends
on the chosen rational slope/frame and is not uniform on a limiting
zero-minor stratum. The present A3 proof does not need a height-to-label
displacement conversion at all.

## 6. Bounded lobes, common-vertex heights and phases

Write alpha<beta for the physical slopes of u,v, and let X be the
full horizontal span for equal powers L. The straight-chain vertical
gap is

    (beta-alpha) min(x, L u_x, L v_x, X-x).

Both u_x,v_x are positive. Thus it has the asserted lower bound by
a positive constant times min(x,X-x,L). Fixed Hausdorff error from
the digital chains implies fixed vertical graph error as well, since
all physical edge slopes are between zero and three. For large L,
common digital vertices are consequently confined to two fixed-width
end boxes. Positive unit x displacement bounds the number of letters
in either such box, not just its area.

Comparability is crucial to identifying heights at a common physical
vertex. At a fixed integer x prefix position, each inversion swap
either leaves that prefix vector alone or replaces one color by a
larger color, strictly raising its physical y coordinate. If the two
endpoint paths have equal y there, none of those changes can have
occurred in a comparison chain. Their prefix height vectors are the
same. A kernel relation between physical edge vectors therefore causes
no rank ambiguity at a common vertex of these comparable paths.

Select the last common vertex in the initial box and the first in
the final box. They have equal height in both words. Restricting to
the intervening common label set preserves inversion inclusion and
internal ranks. Between them there are no further common vertices.
Distinct unit positive edges cannot have an isolated nonvertex contact
without crossing; any coincident edge has integer endpoints. Thus the
two remaining paths form a Jordan lens. The discarded weak lobes have
uniformly bounded support and tile counts. Empty pieces and shared
edges count as forced zero-area pieces, not new interiors.

For the count comparison, lobes separated by a pinch point cannot
exchange tile interiors: a positive-area parallelogram straddling that
x coordinate would have a positive vertical section there, contrary
to the zero lens gap. The prescribed common lift heights match at
each pinch. Tilings consequently factor over open lobes. The bounded
end pieces change logarithmic counts by only a uniform O_J(1).

For offset alignment, if `z-(Jx0+c)` is coordinatewise bounded by
rounding, applying V gives the bounded physical corner error.
Applying I-JV gives
`(I-JV)z-c=(I-JV)(z-Jx0-c)`, also bounded. Translation therefore
has exactly the claimed affine offset control. Fixed inner-boundary
fibers use one chosen z and phase before varying interiors. This does
not license independently changing the assigned rank offset of an
already fixed inner core.

## 7. A5: exact block gluing and the all-scale limit

C_L is finite and at least one. Its support is in a fixed-J O(L)
box, and the six integer-origin tile-presence bits at possible integer
origins bound its count by 2^O_J(L^2). No free-window entropy theorem
enters. The weak-lens convention already specifies independent open
lobes with their full lifted boundary.

Write L=kl+r. Treat U^L and Vword^L as k full l blocks and a possible
remainder block of each type. Each adjacent block interchange is
comparable by A4, including mixed lengths; if r=0 that block is absent.
Bubble all U blocks past the V blocks. Each replacement raises the
current path and its positive-area band is disjoint from all earlier
bands. There are exactly k squared full/full crossings. Their bands
are physical translations of the size-l weak lens, with seam lifts
equal to the corresponding accumulated a,b block contents. Color-rank
identities are consequently fixed even though a block interchange can
change which occurrence falls in a named word block.

Fill mixed remainder bands once. Choose independently one of C_l
fillings in each full/full band. These are actual disjoint physical
patches, and edge incidence matches along their prescribed seam paths.
Restriction recovers all choices. Hence

    C_L>=C_l^(floor(L/l)^2).

This does not presume density-one packing of arbitrary zonogons. As
an additional consistency check, the complete band area is exactly
L squared det(u,v): the internal area contributions of the U and V
words cancel between the two boundary orders. Thus full/full bands
have the correct geometric area scaling as well as disjointness.

For fixed l, division by L squared and passage to liminf gives the
lower bound by l^(-2)log2 C_l. Taking the supremum over l and using
the tautological upper bound of each normalized term by that same
finite supremum proves the claimed equality and convergence at **all**
integer L. The uniformly bounded end-lobe factor gives the identical
limit for the main Jordan lenses.

## 8. Retained obstruction and final scope

The candidate's growing kernel-offset example is valid: its physical
core remains unchanged while the assigned color-2 starting rank drops
below zero in an outer frame based at zero. Its affine error grows
like M and its physical collar remains bounded, so A3's strict distance
inequality eventually fails. It is a counterexample to omitting rank/
buffer compatibility, not to the winding criterion. AR1-01 explains
why the standalone A2 wording must also retain that very rank range,
including an inner color with no edges.

Subject to resolving that localized statement issue, this is a genuine
closed rank-matched collar for the specified buffered lens data and a
real all-scale entropy limit for one receiving family. It is not an
extraction theorem for arbitrary near-flat cut windows. In particular,
neither a thin discarded band nor small relative area overhead for an
arbitrary lens shape has been supplied just by surrounding it with a
large fixed-shape canonical parallelogram. Non-strict slope strata and
global recovery of the original balanced zonogon frame remain open.
DG is not used as an accepted dependency. No H or full-solution claim
is accepted by this audit.
