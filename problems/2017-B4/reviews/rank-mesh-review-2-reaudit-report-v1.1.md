# Targeted independent rank-mesh reaudit R2, repair v1.1

2026-10-17 UTC. Reviewer /root/review_2022_complexity_r2, the original
independent whole R2 auditor, did not construct or repair the proof.
Requested gpt-6.1-sol/max; effective-setting readback unavailable.
The original whole report and ledger remain byte-for-byte frozen.

Targets:

- full main candidate v1.1, SHA-256
  f6c1681ae288b37d2e845e31ca1ef4503d659c9669ec6801266f3564de771ee3;
- full repair ledger v1.1,
  f9d637f76ee320d022dd481b836b04b584cf392bc5acf130106326701c94767d;
- complete eight-artifact freeze-v1.1.json,
  0273dd67122b549dbf7b9cf6dab57f6671aab52ed793e942524c1bd69718bb14;
- unchanged complete UR3 supplement,
  40ad9b252b6c34f5dee5c8cd3eedea8e8feeabb0cec1497b224bf5c32ba58aab.

**Disposition:** RM2-01 is resolved for the narrowed v1.1 Jordan-window
statement and its affected uses. The independently found R1 issue
RMR1-01 has the same resolution. N1's general-D alphabet correction
is valid. I found no new substantive objection in the affected
arguments. The original unrestricted v1 sentence remains false;
neither its history nor either exact counterexample is withdrawn.
This is a reviewer recommendation, not coordinator promotion.
Both original auditors' targeted reaudits and root reconciliation
remain required.

## 1. Full reading and exact change boundary

After both original initially blind whole audits had frozen, I read
both complete original reports, full issue ledgers and source checks.
My own report had already identified RM2-01 independently and was
frozen before any R1 finding was read. R1 separately noted the
editorial N1 alphabet phrase; I did not list N1 in my original
ledger. This new record acknowledges it without changing that ledger.
No other reviewer's new targeted reaudit findings were read before
this targeted report was frozen.

I read the full v1.1 replacement, entire repair ledger, exact diff,
new worklog/source record and complete unchanged UR3 supplement.
The actual full-copy diff was independently reconstructed with
difflib and matched the saved patch exactly. This was administrative
byte/line comparison, not mathematical computation.

The actual edits are confined to:

1. version/date and repair-scope notice;
2. six tile types changed to binom(D,2);
3. the full RM1a window helper replaced by a one-Jordan-curve
   estimate and actual summed cost;
4. the RM2 outer-boundary use explicitly identified as the
   full zonogon's Jordan polygon;
5. final limitations retaining that domain and sum.

No hidden proof replacement occurred in RM1, the main whole-zonogon
code, closed coarsening/lifting, RM2a, GE3, aggregation or analytic
supplement. The unchanged supplement is checked by its exact hash.
No SP, OC, strict-transfer, annulus, local-window or later recovery
packet is a new premise of this repair.

## 2. Both exact counterexamples remain visible

The original false claim allowed a connected rectifiable window
with arbitrarily many boundary components and asserted
O_D(rL+r^2) loss from perimeter O(L) alone.

R1's family uses the actual D2 grid with v1=(1,0),v2=(1,1),
N1=N2=L even and r=2. Each of Theta(L^2) interior selected cells
contains a retained odd/odd tile. Remove one radius L^-3
round hole centered strictly inside that tile in every such cell.
The outer perimeter is 2L(1+sqrt(2)); the holes add O(1/L).
The window is connected and has perimeter O(L), but the
prescribed boundary-cell discard removes Theta(L^2) residual
tiles. The holes intersect retained tiles in this first example.

My stronger RM2-01 family uses the same full grid with even N
and r=2. A selected cell in rank coordinates is

    2s-1/2<a1<2s+3/2,     2t-1/2<a2<2t+3/2,

and its retained tile is

    [2s,2s+1] times [2t,2t+1].

Put one physical circular hole of radius1/(10N) at rank
coordinates (2s+5/4,2t+1/2), in Theta(N^2) interior cells.
Its a1 coordinate lies in the neighboring even-rank skeleton
tile, with margin1/4 from the retained tile. Since
V^(-1) has first row(1,-1), the physical distance to
that a1 boundary is1/(4sqrt(2)); the chosen holes
are strictly smaller for all sufficiently large N.
They stay inside the selected cell and away from the whole
retained tile. Their centers have fixed positive separation,
so the holes are disjoint.

Total boundary length is

    O(N)+Theta(N^2)*2pi/(10N)=O(N).

Every selected cell meets a hole boundary, yet every
designated retained tile remains fully contained in the
window. The prescribed discard still loses Theta(N^2)
whole retained tiles, rather than O(2N+4).
Taking the interior of the outer polygon and removing
closed holes instead of open ones changes no boundary
length or selected-cell conclusion. Thus an open/closed
window convention cannot remove the counterexample.

Both analytic families are reproduced in the author's
repair ledger with their parameters and their different
strengths. The skeleton-only-hole example is not replaced
by the weaker retained-tile-hole example. In particular
the repair is not merely an interpretation that counts
only tiles wholly inside the window.

These windows have many boundary components, so they
are excluded by the new one-Jordan-boundary hypothesis.
They remain exact counterexamples to frozen v1, not to H,
RM1's full-disk geometry or the repaired scoped helper.

## 3. Direct arclength tube proof and whole-tile loss

Let Gamma be one rectifiable Jordan curve of length P,
the boundary of the repaired window. It has a unit-speed
arclength parametrization on[0,P], with endpoints identified.
For rho=C_D r>0, sample at arclength gaps at most rho.
At most ceil(P/rho)+1 sample points suffice.
Every curve point is at Euclidean distance at most rho
from one sample, and every point at distance at most rho
from Gamma is consequently within2rho of a sample.
Thus the rho-tube is covered by those radius2rho disks:

    area(tube_rho Gamma)
      <=4pi rho^2(ceil(P/rho)+1)
      <=4pi(P rho+2rho^2)
      =O_D(rP+r^2).

The extra rho^2 term is necessary when P is small
relative to rho. A tiny Jordan window is therefore
covered without an unstated lower bound P>=rho.
Arbitrary nonconvexity, narrow necks and self-approach
do not affect this arclength argument. No smoothness,
bounded curvature or reach hypothesis is needed.

If a selected face's closure meets Gamma, choose such
a contact point. RM1's diameter bound is
r sum_i||v_i||, also for end tails and boundary cells.
Every whole retained tile in that face is therefore
contained in a tube with rho a fixed D-dependent
multiple of r. Closure contacts and tangencies are
included. If one also records incident skeleton
tiles, their fixed D-dependent diameter is absorbed
in that multiple since r>=2; skeleton loss is already
accounted for separately.

All original standard integer tiles have area j-i>=1
and disjoint interiors. Hence the number of these
whole discarded tiles is at most the area of the
covering tube. This proves the new O_D(rP+r^2)
whole-tile bound directly, with no missing lattice
origin or independent boundary-component factor.

For P=O(L), fixing r before L tends to infinity gives

    (rP+r^2)/L^2=O(r/L+r^2/L^2)->0.

No lower-order conclusion for an arbitrary r(L)
is asserted. The estimate remains a valid upper
bound even for r larger than the frame scale,
when it may simply exceed the total tile count.
The limit order is the same as in the original
mesh program.

## 4. Actual multiple-window and boundary-component costs

For an actual finite list of Jordan windows with
lengths P_1,...,P_M, applying the preceding bound
separately and summing gives

    O_D(r sum_j P_j+M r^2).

Overlap can reduce the discarded union; it cannot
invalidate this safe upper bound. M may depend on
the large scale. The repaired text does not call
this lower order without checking the displayed
sum at those actual scales. In particular total
perimeter O(L) alone does not remove M r^2.

For comparison, if a boundary has b separate
rectifiable Jordan components, the same individual
curve covers would yield O_D(rP+b r^2). This
explains exactly what the old counterexamples
were missing: b=Theta(N^2), so the quadratic
component term cannot be suppressed. The repaired
candidate does not assert a new theorem for every
arbitrary multiply connected rectifiable region;
it deliberately states one curve and the actual
sum for explicitly listed Jordan windows.

No unbounded number of physical windows is
charged to a single frame allowance. The final
limitations repeat the same domain and cost,
so the repair is not undone at the eventual
aggregation interface.

## 5. RM2's outer-boundary use and the main local code

The only direct invocation of the helper in RM2
discards selected faces touching the full outer
zonogon. For a genuine full tiled disk its
boundary is one convex Jordan polygon, and

    perimeter(Z_N)=2 sum_i N_i||v_i||
                 =O_D,c(L).

Thus it fits the repaired helper exactly and
costs O_D,c(rL+r^2). Remaining selected faces
have closed stars inside the original full
disk, as required by the unchanged coarsening
and clean-boundary argument. This does not
charge the boundary of every residual block
using the one-window allowance.

The main whole-zonogon skeleton count and
rare-face code are unchanged. Their bad-region
encoding permits several components because
a given filling with K tiles controls both
its perimeter and component count by O_D(K).
The fixed-width local tube and possible tile
origins then have O_D(K) records. That argument
already accounts for the number of components;
it does not use the false perimeter-only
continuous-window generalization.

R1's N1 correction is simply the correct
finite number of tile types binom(D,2).
It specializes to six at D=4 and is finite
for each fixed D. The O_D encoding constants
already depend on D, so no new factor growing
with L or new uniform-in-D assertion appears.

RM3's multiple-block aggregation remains
the explicit isoperimetric calculation with
aggregate perimeter O_D(r), small-block loss
O_D(sqrt(delta)r^2) and at most O_D(1/delta)
large blocks. It is not replaced by an
unpaid collection of Jordan-window helper
applications. Its limit order and the
eta(r)/delta term remain unchanged.

## 6. Full affected UR3 and analytic-interface check

The entire UR3 supplement was reread and
is byte-identical. Its class GE3_C0(r)
requires an actual Jordan tile disk with
complete height boundary and a fixed
small full-zonogon exterior to which
every filling extends. No new general
rectifiable-window class has entered.

In the compactness contradiction each
B_j has one Jordan boundary of length
at most C0 r_j. Mesh triangles touching
it lie in an O(ell_j)-tube of that
one curve. The direct arclength proof
gives

    O(ell_j perimeter(B_j)+ell_j^2)
       =O_C0(lambda r_j^2+ell_j^2),

since ell_j=floor(lambda r_j) at
fixed positive lambda and large j.
Absorbing one lozenge diameter changes
only constants. This is precisely the
boundary loss used in UR3, with the
topology that v1's auxiliary helper
had failed to state.

The many triangular core strips are
counted by their actual lattice size:
there are O(lambda^-2) triangles and
each strip costs O(ell_j+1), yielding
O(r_j/lambda+1) at fixed lambda.
No collection term is dropped.
The resulting discarded region may
have holes or many components, but
its 3^A count uses its actual lozenge
area and a matching choice per
up-pointing triangle, not a
perimeter-only boundary estimate.

Every core Q remains an actual
Jordan block containing a fixed
triangular inset, with complete
heights fixed by its cut code.
The source limiting domains are
the same fixed triangles, not
varying ragged B_j/r_j.
The initial whole audits separately
checked the precise CKP v3
Theorem4.3 quantifiers, printed
page13 lozenge extension, refined
from-within metric, finite upper
cover/Jensen and affine-parameter
uniformity. No new source theorem
or enlarged analytic hypothesis
is part of this repair.

Scalar compactness, admissible
local tangent planes, local
height gauges and fixed exteriors
are unchanged. Integer dilation
of one reference still supplies
all exact core exteriors. For
each fixed j, M tends to infinity
only after that finite core list
is fixed; its relative core-strip
width O(1/ell_j) is already below
the chosen LC3 tolerance.
The final contradiction and
eta_C0(r)->0 argument therefore
have no newly unaccounted
multiple-window loss.

## 7. Final scoped recommendation and integrity

I recommend resolving RM2-01
and the concordant RMR1-01
for v1.1 only. N1 is corrected.
There is no new substantive
objection to the affected uses.
The original broad statement,
both complete initially blind
reports and all counterexample
parameters remain preserved.
The new ledger records this
resolution without rewriting
any historical open issue.

The repair does not prove
rare-count extraction, charts,
arbitrary profile partition,
strict transfer, balanced
remainders, H, PR or the
official limits. It imports
no new all-D lifting or
local-window coding result.
Coordinator acceptance remains
separate from this recommendation.

Only new assigned rank-mesh-
review-2-reaudit-* records were
created. No mathematical program,
enumeration, CAS, candidate/shared
edit, Git, spawning, charge,
outside contact or separately
billed API occurred.
Administrative hashing verifies
the full new author packet,
both original review manifests
and all earlier own frozen
records. New peer targeted
findings were not read before
this reaudit froze.
