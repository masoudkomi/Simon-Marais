# FL1/CL1/OB1: second independent whole initial audit

2026-10-17 UTC. Initially blind nonconstructor review by
review_2022_complexity_r2. Requested model/reasoning: gpt-6.1-sol / max.
Independently verified effective settings are unavailable.

Target: notes/coordinator-stratum-clean-lens-candidate-v1.md, SHA-256
aa4c79b1fb3136ecd3e7c5ab845733697cca925ba8203b2988fba5c9a793bd95.
I read the whole candidate and freeze, all six frozen constructor
artifacts, AGENTS.md, the official-domain normalization, and the relevant
accepted integer dictionary and DC1 exposition. No peer clean-strata
report, issue ledger or conclusion was read before this report, its
ledger/source checks and hash manifest were frozen.

I find no substantive defect in the stated FL1, CL1, or OB1. In
particular OB1 is a valid prescribed-boundary obstruction, not merely
a failure of an algorithm or a finite search's absence of lifts. The
hand proof stands alone. The candidate proves neither a general
rare-crossing reinsertion theorem nor stratum recovery, EAI, PR, H,
or either official entropy rate.

## 1. Official scope and elementary tiling inputs

The official 2017 B4 count is for marked tilings of a fixed regular
2n-gon, n>=2, and asks for both normalized logarithmic growth limits.
The present packet works in the fixed-D integer deformation
v_i=(1,i-1). It is a partial structural argument; its large window
scale L is not silently the official number of directions.

The accepted integer dictionary uses actual edge-to-edge unit
parallelograms, with affine canonical lift. On a type ij tile, i<j,
write x=x_*+s v_i+t v_j. The nonconstant lift coordinates are a_i=s+
constant, a_j=t+constant. Therefore

    det(grad a_i,grad a_j)=1/(j-i),

and the tile's physical area is j-i. Every other ordered row-pair
minor vanishes on that tile. The explicit inverse two-by-two matrix
also bounds all coordinate gradients by a fixed G_D. Across common
edges these affine lifts agree, so the lift is globally Lipschitz.
These statements apply to cut windows inside the actual tiling.

Positive adjacent swaps between distinct fine colors generate weak
order on ranked words of fixed content; same-color ranks never reverse.
Their commutation classes are the actual marked tilings. The accepted
full-zonogon dictionary gives this input, and its local lens version
can be obtained by fixing a lower shell from the sorted word to p and
an upper shell from q to the block reversal. Glue them to a tiling of
the actual Jordan lens. De Bruijn arcs and the full dictionary recover
the same fixed shells and middle class. Conversely a middle positive
swap shell fills the actual region between p and q; unit positive
x increments and positive determinants prevent overlapping shells.
Thus the local use is not a claim that arbitrary abstract projected
surfaces tile a prescribed plane region.

## 2. FL1: reconstructing the exact boundary identity

Set b_i=J_i x+c_i and e_i=a_i-b_i. Give the Jordan Lipschitz boundary
the positive orientation. For Lipschitz functions the planar Stokes
identity gives

    integral_Omega det(grad a_i,grad a_j)
      = integral_boundary a_i da_j,

and the same statement for b. In this setting one may first integrate
on the finitely many whole or cut tiles and cancel common-edge terms;
the weak Green formula or a Lipschitz approximation supplies the
possibly nonpolygonal outer boundary. No differentiability of a across
tile edges is assumed.

Subtract and expand:

    a_i da_j-b_i db_j = e_i da_j+b_i de_j.

The integral of d(b_i e_j) around the closed boundary is zero, so
integral b_i de_j=-integral e_j db_i. This proves exactly the candidate's
identity, including the minus sign in its second term:

    integral_Omega [det(grad a_i,grad a_j)-det(J_i,J_j)]
      = integral_boundary [e_i da_j-e_j db_i].

Along a boundary parametrized by arclength, a_j has derivative bounded
by G_D almost everywhere, and b_i by ||J_i||. Since |e_i|,|e_j|<=epsilon L
on the entire boundary and its length is at most C L, the absolute
discrepancy is at most
C(G_D+||J||)epsilon L^2, after choosing a consistent row norm.
There is no missing interior closeness hypothesis: only boundary
error is used by this null-Lagrangian identity.

The window may meet many tiles partially. For each type ij tile T its
contribution is area(T intersect Omega)/(j-i), a number in [0,1].
It is one for a whole contained tile and zero for a disjoint tile.
Only tiles meeting the boundary can make the fractional count differ
from either the whole-tile or the intersecting-tile count.

To count such tiles, cover the rectifiable boundary by O(C L+1) disks
of fixed radius, by splitting its arclength into unit intervals.
Its bounded-width tube meets O_D(C L+1) lattice cells. A tile meeting
the boundary has integer origin in this tube enlarged by its bounded
diameter. For each fixed D there are finitely many tile types and
relative integer origins per cell. Thus there are O_D,C(L+1) such
tiles, including a tile merely touching at a vertex. This argument
does not need a lower bound on local boundary smoothness or a bound
on the number of tiny oscillations.

If det(J_i,J_j)=0, the affine bulk term vanishes. The nonnegative
fractional tile count is O(epsilon L^2), and the boundary discrepancy
gives O(epsilon L^2+L) intersecting tiles at large scales. For the
intended L>=1 regime the harmless constant is absorbed in L; the
preceding exact count explicitly includes L+1. Parallel row pairs
and every pair containing a zero row have zero determinant, so the
same conclusion applies. Summing finitely many such bounds costs
only a D-dependent factor.

The statement gives a count, not a location bound. Rare tiles can
remain scattered across the window. No thin-band localization or
automatic insertion theorem follows from FL1.

## 3. CL1: all comparisons, not just aggregate counts

Assume consecutive groups and an actual Jordan fine lens p<=q.
For any pair of distinct fine ranked labels, a positive swap adds its
inversion at most once. The set of pairs swapped between p and q
is exactly Inv(q) minus Inv(p), independently of the chosen chain
or commutation class. The tiling dictionary makes these the tile
events. Thus absence of a within-group tile is equivalent to absence
of every within-group pair from this inversion difference.

For each group G_g, all pairwise orders among its fine ranked labels
are then the same in p and q. Let that common full sequence be r_g.
Every w in the interval has exactly those same within-group orders:
its inversion set is between the two endpoint sets. Hence its
restriction to G_g is r_g, including the original ranks of repeated
fine colors.

Replace the kth group occurrence in a coarse word by the kth label
of r_g. This is inverse to coarsening on every fine interval word.
For labels in different consecutive groups, their natural fine-color
order agrees with their group order. Consequently every cross-group
inversion test, both at the lower and at the upper endpoint, is
exactly the corresponding coarse ranked-label test. Within-group
orders are already fixed by r_g. These observations prove both
directions of the claimed interval isomorphism, with no freedom left
to permute fine labels inside a coarse group.

The conclusion would fail for nonconsecutive groups because fine
and coarse inversion signs could disagree. Consecutiveness is
explicitly required. Zero-count colors can be omitted; if fewer
than two active groups remain, a nonempty Jordan lens with no
within-group events cannot occur. There is no unhandled
two-dimensional insertion case hidden in that degeneration.

## 4. CL1: covers, commutations, and geometry

A cover in either interval swaps adjacent labels from distinct
groups. Its expansion swaps the very same two fine ranked labels,
in increasing fine-color order. A pair of disjoint cover events
remains disjoint after expansion, and the inverse map has the same
property. Thus the induced bijection of maximal chains identifies
the equivalence relation generated by commuting disjoint swaps.
It is a bijection on commutation classes/tilings, not a count of
all shelling orders and not merely a surjection. There are no
within-group events to erase or restore.

Choose strictly increasing coarse slopes s_g and w_g=(1,s_g).
Every coarse cover is a positive-area parallelogram. The interval
therefore has its usual genuine positive shelling geometry.
An additional check is needed because coarsening can otherwise
create a touching boundary and a common tail; OB1 demonstrates that.

At a fixed integer prefix length k, an increasing coarse swap
chain raises the physical y-value of that prefix strictly exactly
when a swap changes its prefix count vector. A swap outside the
prefix changes neither; a swap straddling it adds s_h-s_g>0.
There are no negative contributions. Hence if the coarse endpoints
have the same physical vertex at k, every step leaves that prefix
vector fixed. The two coarse prefix vectors are equal. Expanding
their group counts by r_g gives equal fine prefix count vectors,
and hence the same fine physical vertex. Fine Jordan boundaries
exclude this at an interior prefix. This rules out a new coarse
contact. Between consecutive integer x-values the gaps are affine
and nonnegative; an interior zero would force zeros at both
endpoints, so there is no hidden nonvertex intersection.

The coarse boundary is therefore Jordan as claimed under the
clean hypothesis. Given any coarse replacement tiling of that
exact boundary, expand its class. The resulting fine class fills
the original fine lens with its exact boundary words p and q.
This is genuine insertion in the clean case. If boundaries vary,
the sequences r_g must be included: all group totals together do
not determine them. With O(L) labels, recording their fine colors
and fixed same-color ranks costs O_D(L) bits.

## 5. OB1: complete hand reconstruction

Take p=1243 and q=4312 with one label per color. Their inversion sets are

    Inv(p)={(3,4)},
    Inv(q)={(3,4),(2,4),(1,4),(2,3),(1,3)}.

Thus p<=q, with four new inversions. From p the only allowed adjacent
increasing swap is 24: swapping 12 would create an inversion absent
from q. After that step the word is 1423, with choices 14 or 23.
Those events have disjoint labels and disjoint adjacent positions,
so they commute. Either order reaches 4132 after both. Its only
remaining allowed step is 13, giving q. There are exactly two
maximal chains and exactly one commutation class.

This argument is exhaustive without a search: every possible next
cover at each of the few displayed words has been checked against
Inv(q), and a positive chain cannot undo an excluded inversion.

Merge 2,3 into B, keeping A={1} and C={4}. The endpoints become
ABCB and CBAB. Their common last B edge is a tail. Remove it to
obtain the ABC-to-CBA hexagon, with one occurrence of each of
the three coarse labels. Its only reduced reversal chains are

    BC, AC, AB;       AB, AC, BC.

They are different commutation classes, since each of the three
events shares a label with each of the other two, so none of
their adjacent events commute. This proves exactly two coarse
tilings, not just two chosen examples.

Erase the single internal fine event 23. Both fine chains then
give BC,AC,AB. The missing coarse tiling contains the path BACB.
There is no fine interval word above that coarse word. If its
first B is fine label 2, then 2 precedes 1, an inversion absent
from q. If that B is label 3, the retained inversion (3,4)
requires 4 before 3, whereas BACB puts 3 before 1 before 4.
This is a strict cycle. Those are the only assignments of the
first B, so the obstruction is complete.

For actual geometry use slopes 0,1,2,3. The fine lower prefix
y-values at x=0,1,2,3,4 are 0,0,1,4,6; the upper values are
0,3,5,5,6. Their gaps at the three interior vertices are 3,4,1.
The fine boundary is a genuine Jordan lens, filled by the explicit
four positive tile shells above. With any strictly ordered
coarse A,B,C slopes, the common tail is real and the remaining
three-color hexagon has the two stated fillings. The counterexample
is therefore an actual local prescribed-boundary lifting failure.
It does not falsely require that the coarsened full boundary
remain strict Jordan after a forbidden event collapses.

DC1's surjectivity for the full sorted/reversed boundary uses
a separate fixed prefix of internal reversals. That prefix
cannot be inserted here while keeping p and q. Thus OB1 does
not contradict the accepted global statement.

## 6. Computational provenance and limits

I read, hashed, but did not run the constructor's six frozen
artifacts. The targeted script located a five-label example
with a common initial edge. Its stdout records 1837 tested
intervals when it stopped, approximately 0.0667 seconds in
the script's own timer. The external process record gives
PID 77136, timeout 10 seconds, normal exit, elapsed
0.13698101043701172 seconds, and reaped=true. These timings
describe different scopes and are consistent.

Deleting the common prefix gives the four-label hand proof
above. No property of untested intervals, script correctness,
finite absence, or search exhaustiveness over larger inputs
is a premise of OB1. No new enumeration or CAS was performed
for this audit.

## 7. What remains unresolved

FL1 controls the number of rare tiles; CL1 inserts exactly
when the forbidden count is zero; OB1 shows that merely
deleting rare crossings does not extend CL1. These are
compatible, restricted conclusions. A small number of rare
tiles can be spread among many macroscopic cells. At a fixed
microscopic cell side l, discarding cells meeting those
tiles costs O(epsilon l^2 L^2) in the bulk, with boundary
rounding terms, but a global epsilon L lift error need not
be small compared with l. The two scales cannot be silently
exchanged.

The packet does not provide a crossing-routing theorem,
an annulus for altered fine boundaries, an arbitrary-D
zero-minor recovery theorem, EAI, PR, H, or a full official
solution. No novelty conclusion is warranted by this audit.
The companion issue ledger has no open substantive entry;
the coordinator alone decides acceptance after both audits.
