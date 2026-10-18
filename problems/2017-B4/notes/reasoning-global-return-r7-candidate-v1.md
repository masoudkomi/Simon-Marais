# Boundary-rank completion, pinned plane-window mass, and finite periodic recognition

2026-10-18 UTC. **Candidate proof - unverified.** Constructor C,
`/root/review_2017_coarsening_r1`. Requested inherited gpt-6.1-sol/max;
independently verified effective settings unavailable. TWO OTHER initially
blind ENTIRE WHOLE nonconstructor audits and coordinator reconciliation
are required. No numerical value, upper hypothesis R, two-sided entropy
computability, full annual answer or priority is claimed.

The new deductions concern ACTUAL tilings, whole complete-boundary
fibres and finite global-pattern recognition. They do not assert that
arbitrary local decorations extend, or identify free plane entropy with
the balanced count. The latter identification is already disproved by
accepted PM4. The official2017 question remains the normalized marked
regular-polygon count, with logarithm base2; no other contest problem or
preliminary proof is investigated.

## 0. Exact model, inputs and proposed conclusions

Fix D>=2 and v_i=(1,i-1), V=[v_1 ... v_D]. Write

    Z_N=sum_i[0,N_i v_i], Omega=Z_(1,...,1), Z_p=p Omega.

An integer plane tiling means the actual edge-to-edge tilings X_D of
R² by integer translates of P_ij=[0,v_i]+[0,v_j], i<j, from PM1.
Some colors may be absent. Its integer vertex lift a, affine on each
tile, satisfies Va(x)=x after one integer anchor. Absolute heights may
be negative. A complete disk boundary specifies its physical Jordan
polygon, oriented colored edges and all inherited integer heights.
Z_D(B) counts actual fillings of that one disk/boundary, not anchors,
outside tilings or insertion histories. B(N_1,...,N_D) is the full
marked zonogon count, and B_D(p)=B(p,...,p).

The exact accepted inputs used are:

* PM1's finite origin-bit model, global decoding and proper once-only
  tracks; PM2 in its FULL finite-angle repair. That construction retains
  precisely the finite track set meeting the patch and has contents
  N_i equal to the number of retained tracks of color i. One exterior
  works for EVERY filling of the same complete boundary.
* The actual convex-window Jordan crop and boundary-trace conditioning
  proved in PM3, without its compact-strict entropy conclusion.
* The componentwise fixed-belt padding in accepted G section1. It retains
  the old tile set, ranks and one exterior for every filling. Zero old
  contents are allowed. The integer/full deformation dictionary is used
  only for actual full zonogons.
* Accepted G gives the ALL-integer limit

      k_D=lim_(p->infinity) p^-2 log2 B_D(p).

  The separately accepted EC and PUS statements are starting context,
  not inverted or strengthened in the proof below. GR realizes one
  admissible full profile, not exponentially many fillings.

The only NEW public theorem import is the periodic polygon construction
of de Tiliere, Theorem4.4 in [math/0403324](https://arxiv.org/pdf/math/0403324).
Its actual operative geometry is used below with equal-length polygon
sides. The source's finite-angle setting is retained. No probability,
mixing, density, variational or entropy assertion is imported from it.

Set the explicit loose integers

    w_D=32(D+1), C_D=2D w_D=64D(D+1),
    H_D=10^6(D+1)^8,
    J_D=128 D^6 H_D^2(2D+3)^2.                         (0)

The proposed results are:

**R7A (boundary-range completion).** For an actual positive-area Jordan
tile disk B in a plane tiling, set

    w_i(B)=max_boundary a_i-min_boundary a_i.

These are nonnegative integers. There is one actual full Z_N exterior
for its entire boundary fibre with N_i<=w_i(B). Consequently

    Z_D(B)<=B(w_1(B),...,w_D(B)).                       (1)

The w_D in(0) is a scalar geometric constant; w_i(B) in(1) are contents.
Their distinct notation/arguments will be retained.

**R7B (full tilings extend to the plane).** Every full integer zonogon
tiling has an integer plane extension preserving its physical tiles and
their one chosen lift anchor. There is no small-collar or density claim.

For integer p>=1 and 0<=delta<=1, define F_D(p,delta) as follows. Count
distinct tile restrictions to the OPEN interior of Z_p which have an
actual plane representative and an integer vertex lift a satisfying

    ||a(x)-p h_b(x/p)||_infinity<=delta p
                          for EVERY x in boundary Z_p.       (2)

A tile belongs to the restriction when its interior meets that open
polygon. h_b is the WHOLE canonical marked boundary lift. Existence of
one integer lift is required; lifts and exteriors are not counted.

**R7C (actual full-boundary mass stability).** With

    Q=ceil((1+2delta)p+C_D),

one has the finite comparison

    B_D(p)<=F_D(p,delta)
      <=2^[H_D(p+1)] (3p+C_D+1)^D B_D(Q).              (3)

In fact F_D(p,0)=B_D(p). For every fixed delta in[0,1],

    k_D<=liminf_p p^-2 log2 F_D(p,delta)
       <=limsup_p p^-2 log2 F_D(p,delta)
       <=(1+2delta)^2 k_D.                            (4)

Thus for ANY sequence delta_p in[0,1] tending to0,

    p^-2 log2 F_D(p,delta_p)->k_D.                     (5)

This retains the entire boundary lift, not one averaged tile-density
vector. It uses actual whole-boundary families, including all weak/zero
slope strata, without a compact-strict hypothesis.

**R7D (bounded periodic realization of actual finite patterns).** Every
finite PM1 origin-bit pattern supported in the integer square[-s,s]^2,
s>=1, which has an actual global realization has one whose two rectangular
integer periods are both m, for some positive integer

    m<=J_D(s+1)^2.                                    (6)

The periodic realization retains all specified bits, including zeros,
after ONE integer physical translation. This is a realization theorem
for patterns ALREADY known to have a global realization, not a statement
that every locally legal finite block extends.

**R7E (finite recognition and pinned counts).** Global extendability of
a finite PM1 origin-bit pattern is decidable by a terminating finite
periodic search using(6). For rational delta in[0,1], F_D(p,delta) is
therefore uniformly computable in D,p,delta. No proposed search or count
has been executed in this packet.

**R7F (exact remaining limit).** These finite-model and mass comparisons
do NOT supply an EVERY-scale upper certificate for k_D. In particular
(4)--(5) and finite computability do not provide upper hypothesis R or
an effective convergence rate. The new positive bridges remove a rank
content loss and a finite plane-language recognition issue; a compatible
finite mass upper envelope for the LIMIT remains missing.

Root supplied the broad assignment, not the new track-range, torus,
period-bound, pattern-recognition or mass arguments. C's older PM/GR/OP
authorship and other old review roles are separately accepted input
roles, not independent self-recertification of those old results.
The periodic extension principle is published, not claimed new.

## 1. Scalar height monotonicity and distinct track levels

On a tile with colors j,k the affine lift has only rows j,k nonzero.
For any color i,

    directional derivative of a_i along v_i
       =1 if i is one of j,k, and0 otherwise.          (7)

This uses the actual edge increments, not a convex mixture of vector
profiles. The lift is continuous and locally piecewise affine. Every
bounded segment meets finitely many tiles; if it runs along an edge,
the same affine edge restriction holds. Therefore a_i is nondecreasing
on EVERY line parallel to v_i. The coordinate gradients also have norm
at most D: on an ij tile, an active row has norm ||v_j||/|j-i|<=D,
and absent rows vanish. Hence each a_i is globally D-Lipschitz.

A global color-i train track joins midpoints of opposite i edges.
Their a_i coordinates are both k+1/2 for one integer k; passing the
tile changes only the other color coordinate. Thus the same k labels
the whole track. PM1 proves that q_i(x)=det(v_i,x) is strictly increasing
along its chosen orientation, with increment at least1 per tile,
tending to both infinities. The track is consequently a proper graph
over q_i, meeting every v_i-parallel line exactly once.

Two different color-i tracks cannot have the same level k+1/2. If
they did, take their distinct intersection points with one such
parallel line. The scalar a_i is nondecreasing along it. Moreover it
is strictly increasing on a small interval through either intersection:
the point is either inside an i tile, where(7) equals1, or at the
midpoint of an i edge, where the restriction along that edge equals1.
Two separated equal values are therefore impossible. The level map
from global i tracks to the integers k is injective. Multiple excursions
of ONE track through a disk are not counted as different tracks.

For an actual finite Jordan tile disk B, any point in it lies between
the two boundary endpoints of the component of its v_i-parallel line
inside B. Scalar monotonicity bounds its a_i value by those boundary
values. Thus min/max over the entire disk are already attained on its
boundary. On boundary edges a_i is affine with integer endpoint values,
so both extrema and their difference w_i(B) are integers.

Each i track meeting B has its half-integer level strictly between
these two integer extrema. At most w_i(B) distinct levels are available.
The exact same-track conclusion in repaired PM2 therefore gives

    N_i=#{global i tracks meeting B}<=w_i(B).          (8)

No rank displacement, reference gap bound, phase estimate or separate
height choice on different sides was used.

## 2. One exterior for the entire fibre: proof of R7A

Apply PM2 once to one actual plane representative of B. Its marked
patch survives after one integer physical translation and one integer
lift rebase. The completed contents are exactly the track numbers in(8).
Keep that ONE exterior as the filling varies. A replacement with the
same physical/colored/lifted boundary glues to a genuine full tiling,
and restriction recovers it, as in the accepted complete-fibre proof.

Pad this full Z_N componentwise to Z_(w_1(B),...,w_D(B)) using the fixed
positive belts. By(8) every requested padding amount is nonnegative.
Each belt depends only on the old complete full boundary, not the
interior filling. Composing these two injections proves(1). At least
two colors have positive content because B has positive area. Absent
colors w_i(B)=0 cause no extra track, collapsed tile or independent
offset. The range is invariant under the one rebase, so negative
original ranks cause no exception.

This is stronger than charging contents only by half the boundary
length, but it remains specific to an actual plane patch. It is not a
sufficient test for a formal decoration or an arbitrary coarse insertion.
The old OB1 and profile nonconvexity counterexamples are not contradicted.

## 3. Symmetric belts give an actual plane extension

The accepted positive belt adds [0,v_i] to Z_N without moving any old
physical tile. There is a negative counterpart: centrally reflect the
old zonogon/tiling, apply the positive belt, then reflect back. Its new
domain is Z_N+[-v_i,0], and it also retains every old physical tile.
The boundary side receiving the new belt is now the negative-v_i visible
side. All vertices remain integer, all tiles remain allowed translates
of P_ij, and the old one-anchor lift remains fixed; the new canonical
outer-corner anchor need not coincide with it.

Start from any full Z_N tiling. For every color add one positive and
one negative belt, and repeat. After m rounds the domain is

    Z_(N+2m*1)-m sum_i v_i
       = Z_N+sum_i[-m v_i,m v_i].                     (9)

The tilings are nested as physical tile sets and agree on every old
tile and its anchored heights. The centrally symmetric polygon
sum_i[-v_i,v_i] contains a neighborhood of0 for D>=2. Domains(9)
therefore exhaust R². Fixed tile types have positive area and bounded
diameter, so only finitely many retained tiles can meet a compact set.
Their union is an actual edge-to-edge integer plane tiling. The common
old anchor gives its global integer lift. This proves R7B without
claiming that one zonogon tiles the plane at density one.

In particular each full balanced tiling supplies a restriction counted
by F_D(p,0). Distinct full tilings give distinct restrictions. Hence
the first inequality of(3) holds for every delta>=0.

## 4. Whole-boundary conditioning and the finite mass bound

Here are explicit crop bounds, avoiding any perimeter-only assertion for
a set with uncharged holes. Tile diameter is at most d_D=2D. The perimeter
of Omega is at most2D². For each integer p choose

    W_p=p Omega+[-4D,4D]^2+xi,

where a fixed small rational xi avoids all integer support lines parallel
to these finitely many side directions. One choice is xi=(1/M,1/M²)
with integer M>100D². A primitive integral side normal n has
0<|n dot xi|<1, so no boundary side passes through an integer vertex or
coincides with a candidate tile edge. This choice works for every p.
W_p contains Z_p plus a tile margin, and its perimeter is at most

    2D²p+32D.

For a representative plane tiling take all tiles whose interiors meet
the interior of W_p and fill bounded complementary holes. The accepted
PM3 crop argument gives an actual Jordan tile disk P. Its support
contains W_p, lies within distance2D of W_p, and its outer boundary is
one polygon in that fixed-width tube. Filling bounded holes removes
boundary components rather than charging an unbounded family of them.
All boundary points of P are within Euclidean distance w_D of boundary
Z_p. In particular P includes every tile of the counted restriction.

Record the origin/type presence bits in the radius20(D+1) neighborhood
of boundary W_p. This determines the outer support of the union of
intersecting tiles, its hole-filled support P and its complete colored
boundary: inside W_p the support is full, and every choice affecting
the outside boundary is in that trace. A unit-arclength sample of the
boundary has at most2D²p+32D+2 points. Disks of radius20(D+1)+1 about
them cover all relevant origins. Each has at most(40D+45)^2 lattice
points, with at most binom(D,2) type bits per origin. For D>=2 their
product is bounded by H_D(p+1) with H_D in(0). This is a finite trace
bound, not an independent coordinate code for every interior tile.

Choose one witness and one such trace for every restriction counted by
F_D(p,delta). For a boundary point y of P choose a closest point y0 on
boundary Z_p. By the D-Lipschitz bound, (2) and 0<=p h_b,i<=p,

    -delta p-Dw_D<=a_i(y)<=p+delta p+Dw_D.

Consequently

    w_i(P)<=p+2delta p+C_D<=Q.                        (10)

Condition jointly on the trace and the integer height at ONE fixed
boundary vertex of its known polygon P. The latter has at most
(3p+C_D+1)^D possible values, since delta<=1 and the displayed range
holds there. This single anchor and the complete colored boundary
determine every boundary height. No unbounded common offset or phase
is charged independently on different sides.

Within each joint class, restrictions inject into complete-boundary
fillings of this SAME physical P. R7A and padding(10) give one injection
of that entire class into B_D(Q). There are at most
2^[H_D(p+1)](3p+C_D+1)^D classes. Multiplication proves(3), including
p=1 and zero ambient contents in intermediate completions.

At delta0 there is a stronger exact observation. Along the interior of
a canonical color-i side, the boundary height derivative in direction
v_i is e_i and every other height coordinate is the integer0 or p.
That side cannot meet the interior of a tile. A tile not containing i
has directional a_i derivative0, contradicting the required1. In an
i,j tile, a line parallel to v_i through its interior has a_j strictly
between its two consecutive integer ranks, contradicting the prescribed
integer a_j value. Thus the side lies in the tile skeleton. Only i edges
can contain an open part of it, and their unit subdivisions join the
integer polygon corners. All polygon sides are therefore actual tile
boundaries. Their interiors are filled by an actual full marked tiling
of Z_p, and the restriction determines precisely that tiling. With R7B,

    F_D(p,0)=B_D(p).                                  (11)

This exact equality is not offered as a new numerical approximation
scheme; it explains why zero tolerance alone does not settle upper R.

## 5. Consequences for actual pinned-window entropy

The number F_D(p,delta) is positive and finite: there are only finitely
many integer-origin candidate tiles capable of meeting the bounded
polygon, and R7B supplies at least one. Taking logarithms in(3), the
extra trace/anchor terms divided by p² tend to0 uniformly for delta
in[0,1]. At fixed delta, Q/p tends to1+2delta. Since the accepted k_D
limit holds at ALL integer sizes, including this subsequence Q,

    p^-2 log2 B_D(Q)
      =(Q/p)^2[Q^-2 log2 B_D(Q)] ->(1+2delta)^2 k_D.

The lower term in(3) tends to k_D. This proves(4). If delta=delta_p
tends to0, the same comparison has Q/p->1 and proves(5). No uniform
rate of convergence in p is extracted from the existence of k_D.

This is a true mass comparison for full-boundary pinned PLANE patterns,
not just approximation of one height profile. It requires no strict
minor, positive-row lower bound or convex interpolation. It also does
not count arbitrary local-rule blocks or ignore whether they have global
plane representatives. Recognition of those representatives is addressed
separately next.

## 6. Periodic integer realization, with an explicit finite period bound

First take any actual plane patch P. PM2 completes it into Z_N, up to
one integer translation and one common lift rebase. Pad to balanced
Z_p, p>=max_i N_i. Use the accepted full deformation dictionary to
replace v_i by the unit vector u_i=v_i/||v_i||, with the same cyclic
order. This is an actual full rhombus tiling of the convex polygon

    Q_p=sum_i[0,p u_i],

whose D pairs of opposite sides ALL have length p. The marked old patch
has its induced geometric image; its original coordinates are restored
after deformation back.

Apply de Tiliere Theorem4.4 and its finite side-strip construction to
Q_p. Only its original side directions are used; each added rhombus has
side length p. Subdivide each such rhombus into its p-by-p unit grid.
Shared sides have identical unit subdivisions. The result is an actual
periodic unit-rhombus plane tiling using only the u_i, retaining the
entire original full tiled Q_p. This uses equal-length sides, not an
unsupported assertion about arbitrary parallelograms with unequal edges.

For a quantitative period bound, the operative construction has three
boundary chains and their translation-matched inverses. At D>=4 their
step counts are

    1+(D-3)(D-2)/2, D-2, 1.

For D4 the finite strip construction has its single strip; the same
displayed chains and bound apply. At D2,3 a parallelogram/centrally
symmetric hexagon already supplies the periodic base. The standard
hexagon period vectors are sums of two of the three chain displacements.
In every case they may be chosen as integer combinations of p u_i
with total absolute coefficient at most2D². No collar area tending to
zero is asserted or needed by this finite recognition argument.

The corresponding translations have actual edge paths along those
two boundary chains. After unit subdivision their lift increments are
the SAME signed sums of p e_i. This path statement is essential:
an expression for the physical period vector alone would not bound its
integer lift when D>2.

It remains essential to justify the periodic deformation back to v_i.
Let P0,Q0 be these two independent periods in the unit-rhombus plane,
and let a be its integer lift anchored at a vertex. Its period increments
A=a(x+P0)-a(x), B=a(x+Q0)-a(x) are constant integer vectors: the colored
cochain is translation invariant and the graph is connected. The map

    g(x)=V a(x)

is affine on every tile. It sends its edges to the v_i edges and all
tile determinants are positive. The cyclic order of the 2D rays +/-u_i
is exactly that of +/-v_i. Thus the map is a local homeomorphism on
tile interiors, shared edges AND complete vertex fans. This is a
full-star assertion, not merely positivity on separate faces.

Put P'=VA,Q'=VB. To check that these periods do not collapse, write
g(x)=A0 x+r(x), where A0 maps P0 to P' and Q0 to Q' and r is periodic.
For one period parallelogram F, Green's identity gives

    integral_F det Dg=det(P',Q').                     (12)

Indeed the linear terms involving Dr have zero periodic integral,
and integral det Dr=0 by opposite-boundary cancellation. One can apply
this directly on a finite triangulation of the periodic PL map, or
first approximate r by smooth periodic functions. The left side is
strictly positive because every tile Jacobian is positive. Hence P',Q'
are independent with the correct orientation.

The descended map from the source torus to R²/(ZP'+ZQ') is a local
homeomorphism between compact tori. On fundamental cycles it sends the
basis P0,Q0 to the defining basis P',Q', so its topological degree is1.
Its positive covering degree is consequently1; it is a homeomorphism.
Lifting proves that g gives an actual whole-plane tiling. Its vertices
are integer, its tiles are exactly the allowed P_ij, and the marked old
patch is restored up to the single original integer translation. The
target periods P',Q' are integer because A,B are integer.

The source period coefficient bound shows that each coordinate of P'
or Q' has absolute value at most2D³p. Thus the positive integer

    m=det(P',Q')<=32D^6 p².                          (13)

The loose constant absorbs the elementary determinant bound. For an
integer matrix with columns P',Q', its adjugate identity implies
m Z² is contained in ZP'+ZQ'. Thus the integer bit tiling is periodic
under BOTH (m,0) and(0,m), even if its smaller natural cell is skew.

Now suppose the finite input pattern is supported in[-s,s]^2. Every
candidate tile from those sites lies in[-L,L]^2 for L=s+2D+1. Crop an
actual witness plane around that square with the same fixed tile margin
as before. Its boundary has at most4H_D(L+1) edges, by the identical
arclength/finite-candidate estimate used in section4 (the square's
perimeter8L+32D obeys the same loose bound). PM2 therefore needs at
most2H_D(L+1) tracks. Pad to the fixed integer

    p=2H_D(L+1).

All specified candidate supports lie in the marked patch. Positive
bits survive as their old tiles. Negative bits survive too: a forbidden
candidate tile has its whole interior covered there by the retained
old tiles, so activating it would create an interior overlap. Merely
copying the old positive bits without this support margin would not
justify negative-bit preservation.

Combine(13) with s+2D+2<=(2D+3)(s+1). The rectangular period is at most

    32D^6 [2H_D(s+2D+2)]² <=J_D(s+1)².

Translate back by the one integer marked-patch translation. Periods are
unchanged, all specified bits are in their original physical locations,
and(6) follows. This proves R7D in the actual finite-angle source domain.

## 7. Finite global-pattern decision and pinned-count computation

The PM1 local rules have a finite alphabet of binom(D,2) bits per
integer site and a finite computable rational scope. For a given input
pattern in[-s,s]^2 enumerate every integer m with
1<=m<=J_D(s+1)², and every m-by-m periodic bit array. Check the finite
rules with periodic substitutions and check the input pattern. A rule
retains all its geometric terms even if several site variables become
the same after periodic substitution; self-overlap and coverage are not
discarded by aliasing those variables.

A passing array decodes by PM1 to an actual periodic plane tiling, so
it is a sound positive witness. If the input had ANY plane witness,
R7D provides one in this finite list. Failure of the entire list is
therefore a sound negative decision. The search is finite, uniform and
terminating, albeit far from practical. This is not a claim that local
legality alone suffices. An alternative unbounded dovetail between
periodic witnesses and failed finite-buffer extensions would also work
by compactness, but is not needed once(6) is proved.

To compute F_D(p,delta) for rational delta, list the finitely many
candidate tiles whose interiors meet the open rational polygon Z_p.
Every proposed restriction is a finite assignment of presence/absence
bits to those candidates. Use the preceding decision to retain exactly
the globally realizable assignments, deduplicating identical actual
tile sets rather than counting witnesses. If the finite-pattern convention
requires a whole symbol at each assigned site, first enumerate all
completions of the finitely many unassigned type bits at those sites
and take the finite disjunction. This does not add witness multiplicity.

For each retained restriction the tiles meeting the convex open polygon
are connected through whole edges: a generic path inside the polygon
crosses only full shared edges. Their actual cochain gives a unique
relative integer lift after one vertex anchor. One may take a convenient
integer a0 satisfying Va0=x0, since v_1,v_2 generate Z². Every other
integer anchored lift differs by an integer z in ker V. Condition(2)
at the origin gives a finite box of possible z coordinates. Its boundary
inequalities are decidable exactly: both the interpolated height and
h_b are affine between the finitely many rational intersections of
polygon sides and tile edges, so coordinate maxima occur at those
endpoints. Test the finite z list, and count the restriction once if
one works. No outside witness contributes extra multiplicity.

This terminates uniformly and proves R7E. It supplies actual computable
finite global pattern counts, not merely local-rule upper counts. No
periodic array, rule compiler or count was evaluated in this work.

## 8. The remaining upper-R gap and the significance of the new bridge

The positive conclusions retain ENTIRE complete-boundary mass. R7A
replaces a perimeter content bound by an exact height-range bound.
R7C proves full-boundary stability of exponential plane-window counts
without strict-slope restrictions. R7D--E remove a genuine global-language
recognition issue using a bounded periodic witness. Neither proposition
is a generic free-SFT or abstract computability implication.

Nevertheless (3) compares a finite count with another finite balanced
count; the accepted limit in(4) has no effective p threshold. It does
not prove k_D<=p^-2 log2 F_D(p,delta)+a computably vanishing error for
EVERY p. At delta0 the finite values are exactly the old balanced
counts, by(11), so merely computing them cannot close that gap.

Periodization can add a constant-factor collar. It proves finite-pattern
recognition, not density-one replication, entropy-density preservation,
or a boundary-compatible subadditive partition of large Z_p. Arbitrary
full zonogons cannot be declared to pack themselves at density one.
The actual PM4 free-entropy gap survives, even with matching limiting
tile composition. Imposing the WHOLE boundary, as here, repairs that
particular loss of information but not an EVERY-finite-scale upper
inequality for the limiting mass.

An actual next upper bridge still needs such a finite mass envelope
retaining the prescribed global profile, or an appropriate compatible
subadditivity/realization theorem. Accepted EC gives lower certificates,
PUS gives the original-plane strict local recovery, and GR gives full
reference shapes. None is inverted or relabelled as the missing upper
statement. No claim that the remaining theorem is impossible is made.
All official numerical values, upper R, two-sided computability and
the full annual answer remain open in this packet.
