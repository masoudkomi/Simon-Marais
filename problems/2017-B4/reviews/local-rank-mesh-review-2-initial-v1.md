# Initial independent whole audit R2: local rank-mesh coding

2026-10-17 UTC. Reviewer /root/review_2022_complexity_r2 did not
construct LW1. Requested gpt-6.1-sol/max; independent effective-setting
readback unavailable. This full report, inference ledger and source
checks are frozen before peer local-rank-mesh findings are read.

Target: complete coordinator-local-rank-mesh-candidate-v1.md,
SHA-256 09c206718f1acecb9f23ae9bdb54122a4e9a9420b4549326413a664cb44230c5;
complete freeze-v1.json,
a3e76f8d6dcb6a2db900e810aa75c076b4b479235e95e6bbe021a85799fdc781.

**Finding:** LW1 reconstructs with its exact conditional RM1
background and the stated fixed-window, complete-lift and
coordinate-range hypotheses. I found no substantive objection
or mathematical repair requirement. The new local count does
not assume global N_i=O(L), and neither the single height anchor
nor interior component traversal introduces an unrecorded
rank/exit matching factor.

This is a reviewer recommendation only. It does not accept
an unreviewed dependency by its name or promote the result.
No lower-dimensional entropy theorem, H, PR, UR4, global
assembly, official limit or novelty is established.
No mathematical computation, enumeration or CAS was used.

## 1. Exact domain and conditional dependency

The [official 2017 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-2_1.pdf),
page2, B4, concerns marked fixed-polygon tilings and both
normalized logarithmic limits. LW1 supplies local information
loss only. No other problem or preliminary equation is investigated.

The source is one actual full marked tiling of a fixed convex
zonogon, with fixed contents, position, integer directions
v_i=(1,i-1) and canonical height. Different sources may have
different interiors and outside arrangements, but share the
fixed global domain. The known W is a bounded Jordan window
with diameter and ONE rectifiable boundary length at most cL,
L>=1, and a tiled fixed-width neighborhood.
The absolute range R>=2 is a separate datum and may be
arbitrarily larger than L. The assertion is for fixed D.

The exact RM1 disk/port/diameter conclusions from the full
repaired rank-mesh candidate are explicitly conditional
premises in frozen LW1. My prior whole RM1 audit and
targeted scope reaudit are separate records; they do not
silently change this packet's stated dependency status.
The accepted full marked dictionary and finite tile/lift
facts were read in their exact fixed-D scope.
Global M2 is not a local premise.

The selected ranks are the same global multiples of r,
r>=2, rather than a locally reset selection.
The designated rare tile types are fixed, with at most S
rare whole tiles meeting the stated constant-width
enlargement. Contacts are included. S supplies no
unrestricted conclusion about later alternative fillings.

## 2. Extrinsic height ranges and the local crossing bound

There are finitely many tile gradients at fixed D.
On a tile of type i<j, its only nonzero coordinate rows are

    ((j-1),-1)/(j-i),      (-(i-1),1)/(j-i).

Thus every coordinate has one finite Lipschitz bound G_D.
For two points in the full convex zonogon, integrate
along their straight segment through its affine tile
pieces. This proves an extrinsic global bound independent
of all contents and the particular filling. No intrinsic
short path inside a ragged W is assumed.

A fixed-width enlargement has diameter O_c(L+1).
Intersecting it with the full domain does not enlarge
this diameter; the straight-segment bound still applies
to its points even if the segment leaves the enlargement.
At most O_D,c(L+1) integer or half-integer levels of each
height can meet it, and at most O_D,c(L/r+1) selected ones.

When a whole tile meets the local set but its crossing
center lies just outside, increase the fixed width once
by the maximum tile diameter. This changes only fixed
constants and puts both crossing curves in the same
local rank-range estimate. A skeleton tile has at least
one selected curve and one other curve; different full
curves meet at most once, same-color curves never do.
Consequently the number of relevant skeleton tiles is at most

    O_D,c((L/r+1)(L+1))
       =O_D,c(L^2/r+L+1).

This argument uses the actual local levels. A very long
global curve may have huge total crossing count, but
only these locally relevant crossings are charged.
No bound on N_i relative to L has entered.

## 3. One boundary trace and one absolute height anchor

For any fixed width B, cover the B-neighborhood of
Gamma=boundary W by unit-arclength samples and fixed
radius disks. There are O_c(L+1) samples, and each
disk contains only O_D(1) possible integer origins.
Increasing B by the maximum tile diameter includes
origins of every tile meeting the chosen strip.
Recording the finite type-presence mask therefore
costs O_D,c(L+1) bits.

The record can use a deterministic connected trace.
For clarity, take the tiles meeting a fixed-width
tube about Gamma, using a slightly larger origin
list to record them. The tube is path connected.
If it is clipped by the known convex full zonogon,
it is still path connected: a point in the clipped
tube joins a nearest Gamma point by a segment in
both the zonogon and that tube. Following such
paths through finitely many tiles shows that the
chosen tiles' edge graph is connected through
shared vertices. The thinner set of tiles meeting
Gamma is connected for the same reason.
Extra mask entries outside the chosen trace do
not require additional height anchors.

This also handles tangencies, curves following
tile edges, repeated nearby boundary approaches,
and infinitely many geometric contacts inside
a finite tile strip. The strip is made of whole
tiles, so these do not create infinitely many
component starts.

Choose one trace vertex by a deterministic rule.
Its D integer height coordinates in the absolute
R range cost O_D(log(R+2)) bits. A deterministic
spanning tree of the known colored edge graph
recovers all other trace lifts by +/-e_i increments.
The trace need not itself be simply connected:
integrability is supplied by the actual full
source lift, so all known cycles are consistent.

The possible origins and hence physical positions
are already specified by the fixed window's list.
An anchor index has O(log(L+2)) cost, absorbed by
O(L+1); no absolute physical coordinate must be
transmitted per boundary contact. This is exactly
why there is one log R term rather than
O(L log R).

## 4. Interior selected pieces: starts, traversal and exits

The boundary trace separates the interior part
of W from its exterior. Every selected full
curve that enters a complementary interior
component has its entry and exit in the trace.
Its full endpoints are on the original outer
zonogon, outside W, and a full de Bruijn curve
is a proper simple arc. There can be no closed
local curve component with no recorded start.
The fixed tiled neighborhood excludes an
endpoint hidden inside W.

All oriented starts are read from trace edges,
their midpoint curves and their recovered
absolute heights. The latter decide whether
the global rank is divisible by r.
An unrecorded adjacent region is classified
as inside or outside by the fixed W; since
the trace covers Gamma it cannot connect
the two without crossing that trace.
No global outside continuation is needed
for this local decision.

There are at most O(L+1) starts, since each
uses an edge of O(L+1) recorded tiles.
Order them deterministically. From a
known color-i edge midpoint, read each
next crossing color j. The normal-
increasing orientation displaces the
opposite midpoint by +v_j for j>i
and -v_j for j<i. It determines the
whole parallelogram and its next
edge. Starting from known endpoint
lifts, the same +/-e_j update gives
all new lifted vertices and the
other crossing rank.

Stop when the walk reaches the
recorded trace. A terminator symbol
if used costs one fixed-alphabet
letter per component. Its actual
exit location and rank have already
been determined by the letters.
There is no separate permutation
of exits, component-length logarithm,
or independent rank anchor.

A selected curve can leave and
reenter W many times; its local
pieces are treated separately
from their known starts. Each
skeleton tile is traversed at
most twice, once for each
possible selected incident
curve. Thus total letters are
O_D,c(L^2/r+L+1), from Section2.
The entire locally relevant
selected skeleton, including
all its lifts, is recovered.
Every local skeleton component
is attached to the boundary
trace by at least one such
curve piece, so no floating
height offset remains.

## 5. Global interior faces and their number

Retain only a global selected
face whose closure plus the
fixed tile-star margin lies
inside W. If a face has a
tile meeting W but fails this
test, either its closure
crosses Gamma or it comes
within the fixed margin of
Gamma. RM1 diameter O_D(r)
then places its entire local
residual tile set in a
C_D r tube. The fixed
margin and tile diameters
are absorbed since r>=2.

A retained face is genuinely
global. Its selected boundary
is all recorded inside W,
so a path to the global
exterior cannot bypass it
through an unrecorded
outside component. A cell
artificially capped by the
window boundary is not
retained and is in the
recorded fringe.

Only m=O_D,c(L/r+1)
selected full curves
can meet W. Consider
their full subarrangement,
not just their possibly
many pieces in W.
Every selected curve
not meeting W has a
constant side on the
connected W. Distinct
retained global faces
therefore cannot acquire
different signs from an
unseen outside curve.
Cells of the subarrangement
have distinct sign vectors:
successive proper single-
crossing cuts create the
two signs without duplicate
cells. Consequently the
retained faces inject into
its at most

    1+m+binom(m,2)

cells. Equivalently all
boundary arcs of a wholly
interior face belong to
that subarrangement.
The bound is
O_D,c((L/r+1)^2),
independent of how often
the known Jordan window
oscillates across a curve.
Counting arbitrary local
boundary-cut pieces by
that formula instead
would not be justified.

## 6. The deterministic fringe and rare-face data

Sample Gamma at arclength
spacing proportional to r.
Its C_D r tube is covered
by O_c(L/r+1) disks of
radius O_D(r). Each has
O_D(r^2) integer origins,
since r>=2. Thus a fixed
possible-origin list for
the entire fringe has
size O_D,c(rL+r^2).
Its full finite type
mask records all discarded
boundary-face tiles and
the original boundary
trace. This is a direct
one-curve origin count,
not the false perimeter-
only assertion for many
tiny holes.

Mark a retained face bad
when its closure meets
a rare whole tile. Such
a tile meets W, hence
is among the S allowed
in the stated enlargement,
even if part of it lies
outside a residual block.
No widened count of
far-away rare tiles is
being assumed.

A whole tile is cut by
at most its two selected
mid-arcs, which never
run through its vertices.
It meets at most four
selected faces, including
closure contacts. At
most4S retained faces
are therefore bad.
Their flags cost
O((L/r+1)^2) bits.

The skeleton already
fixes each face position.
Its diameter O_D(r)
gives an O_D(r)-sized
known origin box with
O_D(r^2) possibilities.
The finite type mask
of its bad residual
tiles costs O_D(r^2);
over bad faces this
is O_D(Sr^2).
No box position or
absolute coordinate
is separately encoded
per face or tile.

For r>=2,L>=1,
the flags and skeleton
linear terms are
absorbed by
L^2/r+rL+r^2.
Adding all records
gives exactly

    O_D,c(L^2/r+Sr^2+rL+r^2+log(R+2)).

If r is comparable
to or larger than
the window diameter,
the same deterministic
fringe may cover the
whole window; the
r^2 allowance pays
for it. No nonempty
retained family or
unproved asymptotic
choice r(L) is
asserted.

## 7. Fixed lifted disks and independent recovery

After the skeleton
is fixed, the
physical residual
regions in retained
global faces are
fixed. Splitting
their intrinsic
vertex pinches
gives the RM1
Jordan blocks;
unknown internal
edges do not
change those
physical block
domains.

Every boundary
edge of a residual
block has a known
skeleton tile on
its other side.
If it had another
nonskeleton tile,
the two sharing
tile cycles would
lie in the same
face and block.
Original outer
boundary edges
cannot occur for
these retained
interior faces.
Hence the adjacent
skeleton fixes
every complete
boundary height
and fine rank
from the one
trace anchor.
The same argument
handles cut-vertex
contacts without
inventing a new
port pairing.

Good F has no
rare tile meeting
its whole closure,
including incident
outside-block
tiles at a vertex.
Its margin puts
closed stars in
the tiled domain.
This is the
actual closed-face
cleanliness needed
by a separate
clean coarsening
theorem.

Every unknown
original tile
relevant to W
is now in a
good disk; all
other geometry
was recorded.
The code and
those disk
fillings recover
the original
restriction.
If lifts inside
discarded regions
are also desired,
the recovered
whole local
tile graph is
connected through
the original W
trace and its
fixed boundary
data, so its
known colored
increments recover
them consistently.
No new absolute
height choices
are introduced.

Choose ONE actual
full representative
from a code class.
All its good
disk boundaries
are the fixed
ones. Any boundary-
compatible fillings
replace disjoint
Jordan interiors,
possibly sharing
fixed vertices,
and glue to that
representative's
same complete
exterior. Restriction
recovers every
choice. Outside
matchings are
already those of
this actual full
tiling, not new
data to be guessed.

Arbitrary designated
rare types need
not remain absent
in these replacements.
The candidate
correctly asserts
that stronger
absence only when
zero boundary
minor flux gives
a nonnegative
tile-count identity.
This does not
affect LW1's
source upper code
or the assertion
that arbitrary
valid fillings
glue. It would
be wrong to
claim the latter
always stay in
the original
rare-count source
family; that is
not asserted.

## 8. Whole-audit disposition and scope

The reconstruction
checked local
versus global
rank counts,
extrinsic convex
Lipschitz bounds,
connected whole-tile
boundary trace,
one absolute
anchor, tangencies,
known oriented
starts, finite
terminators, no
exit matching,
actual global
faces, unseen
curve signs,
oscillatory Jordan
boundaries,
whole rare-tile
contacts, disk
pinches, complete
ranked boundaries
and one reference
exterior.

No real
counterexample or
substantive gap
was found under
the stated
conditional RM1
interfaces.
Global contents
remain unrestricted
relative to L;
the explicit
log R cost
is not silently
discarded.

Multiple windows
must pay their
actual separate
fringes and
anchors. Joint
conditioning must
precede selecting
one reference.
No entropy from
independently chosen
largest fibers or
unpaid global
assembly follows.
All lower-direction,
chart, affine,
rare-count and
recovery statements
remain separate.

Only new assigned
local-rank-mesh-
review-2-* records
were created.
No mathematical
program, routine
tests, enumeration,
CAS, candidate/shared
edit, Git, spawning,
charge, outside
contact or separately
billed API occurred.
All frozen target
and earlier own
records are
fingerprinted.
No peer LW
findings were
read before
initial freeze.

Latest direct
weekly telemetry:
28% total used
at2026-10-17
07:03:17UTC,
window10080minutes,
reset1792745187.
The90% total
ceiling and
review/integration
reserve remain.
