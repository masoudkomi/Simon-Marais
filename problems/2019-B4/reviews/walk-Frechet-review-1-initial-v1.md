# DG1–DG4 walk–Fréchet bridge: complete initially blind whole R1

2026-10-17 UTC. Reviewer `/root/review_2022_complexity_r2`.
Requested gpt-6.1-sol/max; independent effective-setting readback
unavailable. **Initial nonconstructor whole audit, not promotion.**

I find no substantive scoped defect in DG1, DG2, DG3 or DG4. The
closed-threshold continuous converse requires the supplied reachable-
interval and grid-vertex induction; the generic additive-edge bound
would not suffice. The balanced counting proof uses independent swapped
bidegree choices with fixed recoverable cuts, giving the required square.
The exact probability statement counts word pairs once, not their
couplings. All 12 whole obligations are covered by 40 ledger checks.
No mathematical code, enumeration, sample, CAS, certificate or author
program was used.

## 1. Independence, exact target and read boundaries

Root constructed the NEW 2019 DG bridge and is excluded from both
independent reviewer slots. I did not contribute to this new candidate.
I previously reviewed the moment/NR/linear-output/R7 results and just
completed the independent MR audit. Those roles are disclosed; neither
my previous verdict nor unaccepted MR/short-joining reasoning is a new
premise here. I have not read any other NEW DG peer report, issue ledger
or finding before freezing this entire initial packet. This is the
2019 walk packet, unrelated to the similarly named 2017 geodesic claims.

Exact target relative to `problems/2019-B4/`:
`notes/coordinator-walk-Frechet-return-v1.md`, 15923bytes, SHA256
`a62416fe466f21265b6f6572ce5333f7bbe75744cb17c293ef963288b73bf8f2`.
Exact manifest: `notes/coordinator-walk-Frechet-manifest-v1.json`,
2046bytes, SHA256
`bd895bb6d18dee9a66fa337cce0b5f7330aa1a76c34a0bc8f692022611c5012d`.

The entire main was read, including all four proofs, source/worklog
limits and 12 inline obligations, together with its manifest. Accepted
chronological model, physical-left reversal, growth existence and R7
scope were checked against the unchanged accepted bodies/acceptance
records. The immediately preceding whole MR audit had read those
complete bodies; their operative model/growth sections were reread here.
This is not a claim of a second fresh whole audit of R7 itself.

The entire postfreeze literature addendum was read as context only.
Its paper is not a new DG premise and its theorem proofs are not
silently assumed. The unrelated critical-code research note was not
read as part of DG. Actual primary read scopes appear in the separate
source record. Every old frozen byte remains preserved.

## 2. Actual relation, official scope and distance conventions

The official open part concerns distinct output strings and their
lower/upper root-growth limits. Histories of alternating added bits
are not counted as distinct outputs. The accepted canonical count c_n
instead counts each marked chronological tape pair once, with c0=1.
The tapes (u,v) belong to R precisely when an ordered shuffle gives
the alternating phase-zero source 0101... . Physical conversion reverses
the left chronological tape; it is not reversed in the current matching
or concatenation arguments. Accepted comparison gives the common
root growth lambda for c_n and original b_n.

For a binary word w let H_w start at zero with increment +1 on 0,
-1 on 1. For tape lengths a,b define indexed vertices

    P_i=H_u(i), Q_j=1/2-H_v(j).

A discrete coupling uses index increments (1,0),(0,1),(1,1), endpoints
(0,0),(a,b), and maximum absolute scalar difference at its vertices.
These are indexed visits: repeated geometric values are not deleted or
identified. A continuous matching is a continuous coordinatewise
nondecreasing path between the same parameter endpoints, permitting
waiting and forbidding backtracking or jumps. Its coordinates are
continuous nondecreasing surjections to the two parameter intervals.
Empty tapes are one-point constant curves, with degenerate parameter
intervals. No weak or Hausdorff matching is substituted.

For finite polygonal curves the closed-threshold existence formulation
agrees with the usual minimum/infimum convention. One can check
attainment directly: straighten feasible path portions inside convex
cells, take a sequence of feasible costs decreasing to the infimum,
and choose one of the finitely many monotone cell/edge itineraries
along a subsequence. Its finitely many gate points have a compact
subsequence limit. The limit endpoints preserve coordinate order;
closed free spaces and straight segments in the common cells give a
path at the limiting cost. Repeated corner gates or zero segments
cause no difficulty. Thus no strict-versus-closed loophole is hidden
when the candidate says minimum cost. The exact polygonal free-space
definition is also stated in the primary JoCG source.

## 3. DG1: the height strip is equivalent to the legal shuffle

At index (i,j) the difference is

    P_i-Q_j=H_u(i)+H_v(j)-1/2.

The total height after i+j consumed source letters is zero at even
time and one at odd time. Therefore every legal history gives an AXIS
path through vertices with H_u(i)+H_v(j) in {0,1}, exactly the closed
distance condition abs(P_i-Q_j)<=1/2.

Conversely an axis path consumes every tape letter in order. Its
height starts at zero and changes by +1 or -1 at each move. If it
stays in {0,1}, the changes are forced to be +1,-1,+1,-1,... .
Thus it reads the actual alternating source starting with zero.
The terminal parity/height relation is a consequence of this process,
not an extra assumption on the pair. The count concerns existence
of a history, not the number of such paths.

Suppose a discrete coupling has a diagonal move between allowed
vertices. The sum of its two height increments is -2,0 or +2.
Allowed endpoints force it to be zero; the two increments are opposite.
At initial height zero use the positive increment first, reaching one;
at initial height one use the negative increment first, reaching zero.
The second increment returns to the allowed terminal height. This
refines each diagonal to two legal axis moves, preserving tape order.
Conversely every axis history is an allowed discrete coupling. DG1
therefore holds for all finite tapes without assuming equal lengths.

If one tape is empty only the other index changes, so the same proof
applies directly. If both are empty, the initial/final vertex pair has
cost exactly one half and represents the unique empty context. The
offset and reflection are essential: using H_v without the minus sign
or omitting one half changes the admitted relation.

## 4. DG2 forward direction and exact cell geometry

Given a discrete coupling of cost at most one half, linearly interpolate
each axis or diagonal index move. Within that cell segment P-Q is
affine in the interpolation parameter, so its absolute value is at
most the maximum of the two endpoint values. The concatenated path
is a continuous monotone matching at the same cost. This proves the
ordinary continuous<=discrete direction without importing an algorithm.

For the converse, every grid-edge difference is an affine function
with slope +1 or -1 and half-integer endpoint values. At threshold
one half, the interval endpoints solving P-Q=+/-1/2 have integer
edge parameters. Intersecting with [0,1] therefore gives exactly a
whole edge, one endpoint, or the empty set. A proper positive-length
subinterval with a nongrid endpoint cannot occur.

In a cell the difference has form d+s*epsilon-t*eta, with d a
half-integer and epsilon,eta in {+1,-1}. Intersecting its two affine
inequalities with the cell square gives a closed convex free set.
Hence a straight segment between free points remains free; if its
endpoints are coordinatewise ordered, the segment is also monotone.
This uses the actual half-integer offset/unit slopes at the closed
threshold. It is not a statement about arbitrary curves or all costs.

## 5. Exact incoming sets and closed-corner induction

Order cells so left/bottom predecessor cells have been processed.
The reachable left-edge set L and bottom-edge set B are global
reachable subsets, with a reachable shared corner included in either
incident incoming set by convention. On the outer axes, a monotone
path cannot leave and later return to the axis. Whole-edge/point/empty
free sets therefore initialize closed reachable sets whose nonempty
minimum is a grid endpoint, zero or one.

For the right edge there are three cases.

1. If B is nonempty, any right-edge free point can be joined to a
   chosen B point by a monotone straight segment: the first coordinate
   rises to one and the second from zero to its target. Thus every
   free right-edge point is reachable through this cell.
2. If B is empty and L is nonempty, a target (1,t) is reachable
   precisely when it is free and t>=min L. Sufficiency uses the
   free included point (0,min L) and cell convexity. Necessity follows
   because a monotone path reaching the target must enter from L
   (or its included corner) and cannot lower its second coordinate.
3. If both are empty there is no reachable right-edge point through
   the cell. A route that lies on a boundary still enters via an
   incoming edge/corner; no exceptional shared-corner route is omitted.

The formulas for the top edge are obtained by exchanging L and B.
The free output set is whole/point/empty, intersected with [0,1],
[min L,1] or the empty set as appropriate. Thus every nonempty
outgoing reachable set is closed and has minimum zero or one again.
This inductively justifies the actual interval data, rather than merely
propagating nonempty flags and losing the entry height.

Strengthen the induction: every globally reachable GRID vertex already
has a free axis history. Outer-axis vertices have this property by
the initialization. For a reachable output vertex the formulas choose
an included MINIMUM incoming point, which is a grid vertex with an
already constructed axis history. A monotone segment from that point
to the output vertex is either an identity segment, a single grid edge,
or the cell's lower-left-to-upper-right diagonal. A grid edge is free
by convexity. The diagonal's endpoints are free, so Section3 supplies
the two-step free axis refinement. Append that segment/refinement to
the incoming history. This proves the strengthened induction.

Consequently a continuous path reaching (a,b) yields an axis history
there, proving the converse and DG2. The proof retains single free
points and equality, rather than approximating them away. If a or b
is zero there are no cells: the cost along each remaining affine edge
is bounded by its endpoint maximum, so continuous and discrete
conditions coincide directly. Both-empty cost is one half as above.

A tempting but invalid shortcut is to round every free interior point
up/right. For example the single cell for u=v=0 has difference
-1/2+s+t; some interior points are free but the upper-right corner
is not. This is an analytic counterexample to that REJECTED shortcut,
not to DG2. The submitted incoming-set induction does not use it.

## 6. DG3: fixed bidegrees, independent square and balanced rate

Let M_(a,b) count actual pairs of those tape lengths. Tape swap is a
bijection, so M_(a,b)=M_(b,a). For two fixed bidegrees with EVEN
total lengths, chronological concatenation

    ((u,v),(u',v')) -> (u u',v v')

is admitted because each source block starts at phase zero. The known
first tape lengths a,b recover the first pair by prefix cuts and the
second pair by the remaining suffixes, even when a or b is zero.
Thus the map is injective at fixed bidegrees. It need not be injective
over an unlabelled union of all bidegrees, and no such assertion is used.

Taking balanced lengths m,n gives D_(m+n)>=D_m D_n. The history
(LR)^m supplies tapes 0^m,1^m, so D_m>=1. For m=0 the same empty
convention gives D0=1, although all root/supremum formulas use m>=1.

Since c_(2k)=sum_(a=0)^(2k)M_(a,2k-a), choose a fixed maximizing
bidegree (a,b), a+b=2k, with size at least c_(2k)/(2k+1). Choose
its member and a member of the SWAPPED bidegree independently. They
have equal cardinalities by tape swap; their product therefore has
the SQUARE cardinality, not merely the size of a single diagonal
choice of a pair and its own swap. Fixed cuts recover both choices
from the balanced output of tape length 2k. Therefore

    [c_(2k)/(2k+1)]² <= D_(2k) <= c_(4k).

Taking 1/(4k) powers, the lower bound becomes
c_(2k)^(1/(2k))/(2k+1)^(1/(2k)), tending to lambda. The upper
bound tends to lambda too. Hence D_(2k)^(1/(4k))->lambda.

For odd m=2k+1 append zero to the first tape and one to the second.
The previous total length4k is even, so the two appended source
letters have the required phase. Removing the last letter from each
tape recovers the input, so D_(2k+1)>=D_(2k). Raising to
1/(4k+2) preserves the lower limit lambda, since the old exponent
ratio 4k/(4k+2) tends to one. Together with D_(2k+1)<=c_(4k+2)
this proves the ALL-m balanced limit.

Finally, for each fixed positive m, supermultiplicativity gives
D_(jm)>=D_m^j. The already proved all-m limit implies
D_m^(1/(2m))<=lambda. Those same quantities tend to lambda, so
their supremum is lambda. No reversed Fekete inequality or unjustified
all-bidegree concatenation injection is invoked. This proves DG3
without asserting a positive or polynomially controlled fraction of
all contexts lies in the balanced bidegree.

## 7. DG4: exact random-pair probability and rate

There are 2^m binary words for each tape and hence 4^m independent
uniform pairs. The first walk is H_u. Reflection of the independent
second unit walk, followed by the fixed one-half shift, preserves its
uniform simple-walk law and independence. The word-to-walk maps are
bijections. DG1 says precisely that D_m of these pairs satisfy the
discrete event; DG2 identifies that same event continuously at this
specific threshold. Thus

    pi_m=D_m/4^m,
    pi_m^(1/m)=D_m^(1/m)/4 ->lambda²/4.

Each D_m>=1, so pi_m>0 and logarithms are legitimate. Continuity of
log at the positive limit yields
-lim(log pi_m)/m=log4-2log lambda=2log(2/lambda).
The already accepted strict bounds L<lambda<U<2 give
2log(2/U)<rate<2log(2/L), because this function decreases in lambda.
This does not sharpen their numerical content.

Every context pair is counted exactly once, regardless of how many
legal axis or diagonal couplings realize it. No probability of an
infinite matching pair, conditional endpoint distribution, sampler,
generic random-walk law or original b-ratio theorem is imported.

## 8. Source hypotheses and postfreeze literature firewall

I read the primary Eiter–Mannila mathematical text Sections1–5 through
the references. Its indexed coupling and nondecreasing-surjection
definitions and continuous<=discrete comparison are the relevant
classical attribution. Its additive longest-edge bound cannot give
the exact closed-threshold converse. No incidental metric/stuttering
assertion, extraction typo or external algorithm is a proof premise.

The primary JoCG2025 deposit was checked for its actual definition and
free-space formulation, and Section4's strict long-edge hypothesis.
Its stated condition is edge length GREATER than2delta. Our edges
have length1 and delta=1/2, so equality fails that hypothesis. No
generic simplification, approximation or algorithmic counting theorem
fills DG2 or the growth transfer.

The postfreeze ECCC2026 addendum is CONTEXT, not a changed candidate
or a theorem input. Its interval-chain/cumulative-sum relation is prior
methodological context. Actual Definition4.1 uses axis-only increments,
with walks starting at zero; our offset and diagonal refinement are
separate. The actual Lemma4.3 threshold n^(1/4-epsilon) is at least
(2/3)ln n, and Lemma4.7 assumes Delta>=2log n. Direct substitution
of a fixed threshold1/2 or1 into those hypotheses is invalid. The
growing-threshold bounds can at most bound a larger event; they do
not evaluate this exact fixed-threshold exponential rate. I do not
claim a full new proof audit of the ECCC paper or its probability
foundations. The separate source record gives the actual partial
read scope and chronology without a priority assertion.

## 9. Preservation and disposition

No substantive issue or author repair is requested. All four NEW
claims are reconstructed, including the continuous incoming-interval
and grid-vertex proof, empty tapes, fixed-bidegree independent square,
all-m limit/supremum and exact finite probability. Existing accepted
model/growth statements remain attributed premises, not a new claim
that MR or joining has been accepted by implication.

Only NEW `problems/2019-B4/reviews/walk-Frechet-review-1-*` files
are written. Exact input/candidate/source-context hashes and the older
own preservation chain are frozen after the entire report, ledger and
source record exist and before NEW peer findings. No mathematical
program, certificate or source algorithm is executed. Root must still
reconcile two independent whole audits before promotion. No exact
lambda, positive defect, grammar, annual evaluation or novelty follows.
