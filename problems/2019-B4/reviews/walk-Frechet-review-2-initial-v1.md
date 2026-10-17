# DG1–DG4: complete initially blind whole review R2

2026-10-17 UTC. Reviewer `/root/review_2021_reasoning_j15_r2`.
Requested gpt-6.1-sol/max; independently verified effective settings
unknown. This is a recommendation to the coordinator, not promotion.

Target: the COMPLETE 15923-byte `coordinator-walk-Frechet-return-v1.md`,
SHA256 `a62416fe466f21265b6f6572ce5333f7bbe75744cb17c293ef963288b73bf8f2`,
with the 2046-byte constructor manifest SHA256
`bd895bb6d18dee9a66fa337cce0b5f7330aa1a76c34a0bc8f692022611c5012d`.
I read the entire main text, all twelve end obligations, exact accepted
relation/growth bodies and their scope authorities, and the separate
5322-byte postfreeze literature addendum. The addendum is context only;
it does not add a theorem premise or change the mathematical target.

I found no substantive defect or required author repair in DG1–DG4.
The reconstruction below includes the complete continuous incoming-set
induction, rather than inferring it from a generic distance comparison.
The 43-row companion ledger covers every one of the twelve obligations.
The full report, ledger, actual source checks and immutable fingerprint
packet must all freeze before any peer comparison. I have read no new
DG peer report/findings or later coordinator inspection. The root
constructed DG and cannot count as either independent reviewer.

## Roles and accepted scope

I constructed the older 2019 R7 positive-renewal packet and earlier NR
work, and reviewed moment, CCL, linear-output and MR material. I did NOT
construct or contribute any new
inference to DG1–DG4. My earlier roles do not independently recertify my
own R7 work. Here R7 is an exact accepted input used only for its stated
all-length root-growth/common-lambda scope and the retained numerical
enclosure. The chronological relation and count already occur in the
accepted older context/renewal bodies. No new peer DG result is a premise.

The official open target counts DISTINCT original binary strings grown
from seed 1. Its two requested root limits are not an insertion-history
count. The accepted chronological tapes record additions starting with
0; a physical left context is the reversal of its chronological tape.
There is a marked seed in the original-string interpretation. An
unmarked string can have several admissible seed marks. DG counts the
ordered chronological pairs once each; it neither identifies that count
with the unmarked count nor counts each coupling separately. The old
accepted mark-forgetting/root-growth comparison supplies the common
lambda. I did not investigate or reproduce preliminary part (a).

## DG1: every finite pair and the correct staggered strip

Let a=|u|, b=|v|, and set

    S(i,j)=H_u(i)+H_v(j),
    P_i-Q_j=S(i,j)-1/2.

Since S is integral, the free grid vertices at threshold 1/2 are exactly
S in {0,1}. Starting at S(0,0)=0, any axis step consumes precisely one
next tape letter and changes S by +1 for 0 or -1 for 1. A path which
stays in this two-level strip must therefore consume +1,-1,+1,-1,...,
and hence exactly the required alternating source, in tape order.
Conversely an actual alternating history has exactly these heights.
The parity of i+j supplies the endpoint height automatically; an extra
endpoint-balance assumption is unnecessary.

For a diagonal move, its two individual H increments are each +/-1.
If both endpoint sums lie in {0,1}, their sum is zero: an increment of
+2 or -2 cannot connect two allowed sums. At starting sum 0 take the
positive increment first, reaching 1, then the negative one. At starting
sum 1 take the negative increment first, reaching 0, then the positive
one. The chosen move can be on either tape, according to its actual
letter. Both tape orders and all other coupling vertices remain intact.
Repeating for every diagonal gives an axis history. The signs here are
the H_u,H_v signs; the reflected Q sign is not inadvertently used.

The empty word has the singleton walk at its prescribed initial value.
With one tape empty there are only axis steps and the same proof works.
With both empty the only pair has cost 1/2 and is admitted. Thus no
positive-length convention excludes an endpoint of the claimed domain.
Omitting either reflection or half offset changes the strip and is not
an alternative definition being assumed.

## DG2: a full reconstruction at the closed threshold

The definition uses continuous, coordinatewise nondecreasing matchings
with the two fixed endpoints, allowing waiting. It permits neither
backtracking nor jumping over a vertex. Linear interpolation of a
discrete coupled move stays in its cell; P-Q is affine on that segment,
so its absolute value is at most the larger endpoint absolute value.
This proves continuous <= discrete directly in the present setting.

There is no issue from defining the continuous distance by a minimum,
where the 1994 source writes an infimum. For completeness, if a+b>0,
compress simultaneous pauses and parameterize any such monotone path by
s=x+y in [0,a+b]. This is well-defined: equal sums along a monotone
path imply identical coordinates. Its coordinates are 1-Lipschitz,
nondecreasing, and sum to s. A uniformly convergent subsequence of
paths with costs approaching the infimum preserves these properties,
endpoints and the limiting cost, by continuity of the polygonal curves.
Thus the infimum is attained. The zero-length case is a single point.
This is the usual elementary compactness underlying the classical
minimum convention; it is not an extra restriction or a repair to DG.

On each grid edge, the scalar difference starts at a half-integer and
changes by exactly +1 or -1. Intersection with [-1/2,1/2] therefore
gives the whole edge, one endpoint, or the empty set. In particular a
nonempty proper interval with a nongrid endpoint cannot occur. Each
cell's free set is convex, because the difference there is affine and
the two threshold inequalities are halfplanes. These are separate facts:
cell convexity alone would not imply the integral edge endpoints.

Use local coordinates on a cell [0,1]^2, with incoming reachable sets L
on its left edge and B on its bottom edge. Here reachable means from the
global origin, not just membership in the cell's free set. On an outer
axis a path cannot jump a missing piece; successive free edges are
whole/point/empty. Their reachable pieces are closed intervals whose
minimum, when they are nonempty, is a grid endpoint.

For completeness the exact outgoing formulas are:

    right = free_right,                         if B is nonempty;
    right = free_right intersect [min L,1],    if B empty, L nonempty;
    right = empty,                             if both empty;

    top   = free_top,                           if L is nonempty;
    top   = free_top intersect [min B,1],      if L empty, B nonempty;
    top   = empty,                             if both empty.

If B is nonempty, take its attained minimum (s0,0). Every point (1,t)
on the free right edge is coordinatewise later, so its straight segment
from (s0,0) is monotone and free. If only L is nonempty, a right point
(1,t) can be reached precisely when t>=min L; the straight segment from
(0,min L) proves sufficiency, while monotonicity proves necessity. The
top formulas follow by exchanging x and y. With no incoming point there
is no way to enter. A reachable shared corner belongs to its incoming
edge, including the degenerate singleton case, and is not silently lost.

These formulas do compute GLOBAL reachability. A monotone path arriving
at the cell's right or top side has entered its closed cell through its
left or bottom side, or starts at a common corner already on that side.
It cannot enter from a point strictly to the right or above and return.
A route along a grid line is assigned to the adjacent closed cell; a
right-bottom or top-left corner is contained in the appropriate incoming
edge. Processing cells after their left and bottom predecessors therefore
has no circular dependency or missing outside route.

The free edge is whole/point/empty and the only cut level is 0 or 1.
Consequently each outgoing set is again a closed interval, empty set or
point, and its attained minimum is 0 or 1. The induction is valid even
if an allowed cell touches the already reached set at one vertex only.

Strengthen it by retaining an AXIS history for every reachable GRID
vertex. The formulas choose an incoming minimum which is itself a grid
vertex. From that vertex to a reachable output grid vertex, the monotone
segment is constant, lies along one free edge, or joins the cell's
lower-left to upper-right corners. An anti-diagonal cannot be selected,
because the segment is coordinatewise nondecreasing. In the diagonal
case DG1 refines it to an allowed two-edge route. All selected incoming
vertices already have axis histories by predecessor/outer-axis
induction. This gives an axis history to every reachable output grid
vertex and, finally, to (a,b). It does not round an arbitrary free
interior point to a possibly forbidden upper-right corner.

If one tape is empty the rectangle has no cells. The one-dimensional
linear edge has its maximum absolute difference at an endpoint, so the
continuous condition equals the discrete condition there. Both-empty
was checked above. Thus the argument includes equality at 1/2, point
pinches, boundary-only paths, singletons, and all zero dimensions.
No long-edge theorem or equality at other thresholds was imported.

## DG3: fixed cuts, a genuine square, and every tape length

Swapping tapes gives an actual bijection M_(a,b)=M_(b,a). Take pairs
of bidegrees (a,b) and (c,d), with a+b and c+d both even. Concatenating
the two first tapes and the two second tapes admits the concatenation
of their histories. The second block starts at phase 0 because the
first block's total length is even. For FIXED bidegrees, cutting after
a and b letters recovers both input pairs. Thus the concatenation is
injective at those cuts, including cuts of length zero. Forgetting the
first block's lengths would invalidate that recovery; DG does not do so.

In particular, D_(m+n)>=D_m D_n, since balanced blocks have even totals.
The history (LR)^m yields the pair (0^m,1^m), so D_m>=1 for m>=0 and
D_0=1. This proves both asserted finite statements, including zero.

At total length 2k, partition the c_(2k) actual distinct contexts into
2k+1 bidegrees. One class, say (a,b), b=2k-a, has size
N>=c_(2k)/(2k+1). Its swapped class has the SAME size N. Choose one
member of each class INDEPENDENTLY. Concatenation with its fixed cuts
gives N^2 different balanced pairs with each tape length a+b=2k. This
is the full square, not merely N pairs obtained by swapping the same
input. It follows that

    [c_(2k)/(2k+1)]^2 <= D_(2k) <= c_(4k).

The upper inequality is just subset inclusion at total 4k. Taking
1/(4k)-th powers, the lower expression is
c_(2k)^(1/(2k))/(2k+1)^(1/(2k)), tending to lambda. The upper expression
also tends to lambda by accepted all-length context growth. Hence the
balanced limit holds along even tape lengths.

For m=2k+1, append a 0 to the first tape and a 1 to the second tape by
a final LR source block. The preceding total is 4k, so this extension
has the required phase. Removing the final letter from each tape is
an inverse on the image, including k=0. Thus D_(2k+1)>=D_(2k), while
D_(2k+1)<=c_(4k+2). The lower 1/(4k+2)-th root is the already convergent
even root raised to 4k/(4k+2); the upper root tends to lambda. This
proves the limit for ALL m, rather than only a subsequence.

Finally fix m>=1 and repeat a balanced block j times. The injection
gives D_(jm)>=D_m^j. The all-m limit along jm implies
lambda>=D_m^(1/(2m)). Conversely these quantities themselves tend to
lambda as m increases, so their supremum equals lambda. No reversed
Fekete inequality or total-context supermultiplicativity is presumed.
Nothing here estimates the proportion of all contexts which is balanced.

## DG4: actual random pairs, not coupling multiplicities

Independent uniform simple walks of m steps have 4^m equally likely
ordered increment pairs. Encoding the first by u, and encoding the
REFLECTED second by v, is a bijection: Q=1/2-H_v is still a uniform
simple walk from 1/2 and remains independent of H_u. DG1 says that
exactly D_m of those pairs have the required event, once each regardless
of the number of their legal couplings. DG2 permits the continuous
wording for the same finite event. Hence pi_m=D_m/4^m exactly.

DG3 now gives pi_m^(1/m)->lambda^2/4. Since D_m>=1, logarithms are
defined, and

    -(log pi_m)/m = log 4 - (log D_m)/m
                 -> 2 log(2/lambda).

The old enclosure is strict and lambda<2, so the rate is positive. Its
displayed bounds have the correct reversed order because this expression
decreases with lambda. There is no new numerical computation, exact
evaluation of lambda, event about an infinite pair, or defect conclusion.

## Sources, limitations and disposition

Actual source reads and precise exclusions are in the companion source
checks. I freshly inspected the full Eiter–Mannila mathematical article,
the stated JoCG definition/early long-edge passages, and the complete
relevant Section 4 of the postfreeze ECCC context paper. The generic
distance inequality is attributed; DG2's converse is reconstructed above.
The strict long-edge condition fails at unit length and delta=1/2.
The postfreeze ECCC material remains methodological context only, with
its exact convention and hypothesis limits recorded separately.

The mathematical reconstruction was by hand. No mathematical program,
CAS, scan, sampler, author-script rerun or finite extrapolation was used.
Administrative SHA/JSON validation is only provenance evidence. Public
source viewers needed no native download, cache write or stalled native
retrieval; no binary source hash was invented. No shared file, old byte,
Git state, other worker job or access setting was changed.

I recommend the EXACT DG1–DG4 partial statements for coordinator
reconciliation with the other independently frozen whole audit. I do
not promote them. The exact common growth constant, a closed pressure
equation evaluating it, the actual renewal defect, original consecutive
ratios, a full annual solution, and any priority claim remain outside
this recommendation. All 58 older own packets are checked unchanged
in the companion integrity freeze.
