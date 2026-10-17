# A possible dimension induction for uniform dilation recovery

2026-10-17 UTC. **Research program with unresolved proof obligations.**
This is not a proof of H, PR, uniform D-direction recovery or the
official limits. It records a new route while its geometric pieces
and three-direction input receive their required reviews. No computation
or CAS was used. Do not promote a sketch or similarly named hypothesis
to a theorem.

## 1. The proposed induction target is stronger than the balanced limit

For fixed D,C define GE_D,C(r) to consist of Jordan tile disks with
complete colored boundaries and lifts, perimeter at most Cr, and a
fixed exterior in a full marked D-direction zonogon having at most Cr
tracks of each color. Every filling must glue to that SAME exterior.
All directions are fixed cyclicly ordered integer directions; deleting
inactive curves and marked deformations have to retain the full lift.

The desired statement is

    max(0, log2 Z(B)-liminf_(M->infinity) M^-2 log2 Z(MB))
       <=eta_D,C(r) r^2,       eta_D,C(r)->0.             (UR_D)

It is not the exact finite inequality Z(MB)>=Z(B)^(M^2).
UR_3 is the substantive target of the rank-mesh/CKP supplement, whose
two whole audits reconstructed LC3 but require a separate Jordan-window
scope repair before whole-packet acceptance. UR_2 is the unique-grid
endpoint. No UR_D for D>=4 is assumed proved.

There is a useful precise consequence if UR_D is eventually established.
Take B to be the full balanced content-r zonogon, so Z(B)=B_D(r).
It gives

    liminf_M log2 B_D(Mr)/(Mr)^2
       >=log2 B_D(r)/r^2-eta_D,C(r).

The separately accepted remainder injection/padding then passes an
all-large-multiples lower count to every integer scale, with this fixed
r chosen BEFORE the final scale tends to infinity. Choosing r along
a limsup sequence and then letting r grow would prove H_D. Thus
uniform recovery for arbitrary small full-exterior disks is a natural
inductive target; knowing H_(D-1) only for balanced polygons is too weak.
Even H_D for all D would still need the accepted direction-coarsening
comparison's exact scope to reach the official growing-direction limit.
Equality/existence alone must not be reported as a numerical evaluation.

## 2. Why a one-pair reduction may suffice at each induction step

The current clean-lifting theorem is written for D4 with one merged
pair and two singleton groups. Its actual no-return argument uses
only that every OTHER group is singleton. With exactly one merged
pair and D-2 singleton groups, an exit from a clean selected face
must cross one of those fixed singleton barriers; a return must
restore its sign and cross that same coarse curve again. This
suggests an all-D ONE-PAIR lemma with the same exact boundary-port
and dilation conclusions. It requires a full new statement and audit;
it is not already accepted by renaming D4.

An induction could merge only one pair at a time. The resulting
(D-1)-direction disk is then handled by UR_(D-1), which would already
allow arbitrary profiles. It would not be necessary to assert the
currently unsupported simultaneous several-nonsingleton-group port
theorem. If the tangent has several zero minors, choosing ONE pair
is enough for a dimension reduction; additional degeneracy remains
inside the lower-dimensional UR hypothesis. A zero row can instead
be removed by declaring all its incident tile types rare.

The new orientation-chart candidate OC1--OC3 explains how antiparallel
row directions might first be made positive and consecutive. It
preserves actual counts, complete ranks and a common affine offset.
Its finite charts and the standard-coordinate return need their own
two audits. Applying different charts in different windows still
requires precise source/window and seam accounting.

## 3. Strict windows can compare upper counts to dilated insertion
without an explicit entropy formula

For ONE fixed strict rational tangent and matching canonical frame,
accepted ST compares a near-affine source-family upper count to C_m,
and inserts C_k/B_J fillings into any compatible actual reference.
The canonical entropy exists at all integer sizes by A5. Hence the
same canonical term can be used for the original upper bound and
the dilated-reference lower bound. The inserted interiors need not
remain nearly affine; their complete exterior is fixed, and only
the count is needed. This is the same advantage used in UR_3's
compactness contradiction.

For an actual reference with affine error epsilon L, integer dilation
has affine error M epsilon L at scale ML, with exactly matching lifted
boundary and exterior. Thus upper and lower ST can be compared at
the SAME positive epsilon. The two side factors1+O(sqrt(epsilon))
and1-O(sqrt(epsilon)), plus a finite-alphabet strip cost, give an
O(sqrt(epsilon)) normalized loss when the canonical density is bounded.
No continuity of an unknown D-direction entropy density is required
if the same fixed rational frame is used on both sides.

The missing point is not the comparison for a fixed rational tangent.
It is a denominator-safe uniform version on compact sets of STRICT
real tangents, and then a finite actual-window assembly.

## 4. A concrete way to seek denominator-safe strict uniformity

Let K be a compact strict tangent set, ||J||<=G and every ordered
minor at least rho>0, with VJ=I. A finite cover should permit fixed
rational physical directions u0,v0 in each chart's common positive
cone, with uniformly positive J_i u0,J_i v0 and det(u0,v0)>0.
Approximate J by rational J' in the affine space VJ'=I. Choose a
common denominator q so J'(q u0),J'(q v0) are integral. The A4
event words then have these contents and period q in physical units.

The critical proposed estimate is that event-path DIGITAL ERROR,
not period length, is uniformly O_D,G(1). At event time t, each
coordinate is the relevant floor of J'tu0 plus one fixed phase,
so its discrepancy from the straight lift is bounded by1. Applying
V and I-J'V keeps the physical and affine boundary errors bounded
independently of q. Positive minor and direction margins on K would
then put the end-contact lobes in uniformly bounded physical boxes.
This must be proved using the actual event paths and common phase;
it cannot be replaced by a bound proportional to the word period.

Use the physical frame span q m as the scale. A floor or ceiling in
m costs O(q) physical width, which only changes the sufficiently-large
scale threshold. The supporting-line margin, CUT band and A3 inequality
can be written in physical units with constants controlled by rho,G
and the finite u0,v0 choices. The denominator should affect L0, not
force the allowable approximation epsilon to shrink faster than the
rational approximation error.

For a fixed desired loss one could then choose epsilon FIRST, take a
finite sufficiently fine rational net of K SECOND, and take the maximum
of its finitely many period-dependent scale thresholds THIRD. This
avoids the invalid inference that density of rational slopes alone
gives uniform entropy transfer: arbitrary shrinking radii around rational
slopes might fail to cover irrational slopes. Establishing the uniform
geometric constants is an explicit obligation, not a completed theorem.

The all-D versions of A1--A5/CUT/ST would also need complete proofs.
Their pair-projection arguments suggest replacing six projections by
binom(D,2), but no such replacement is accepted without checking every
rank range, common offset, lobe, code and whole-buffer hypothesis.

## 5. Boundary windows, rare tiles and an order of parameters

Suppose a window is close to an exact boundary tangent J0. After a
valid orientation chart, choose a positive-parallel row pair with
zero minor, or a zero row. The exact Green identity FL1 bounds the
number S of its rare tile types by O(epsilon L^2+L+1), provided the
whole required affine/boundary hypotheses really hold. The boundary
term must be retained before taking L to infinity.

Select every r0-th track and keep the whole-tile skeleton. Conditioning
on it, bad faces and their fillings costs

    O_D(L^2/r0+S r0^2+L+1).

Additional loss along ONE Jordan window is O_D(r0 L+r0^2). For a
finite collection, sum its actual perimeters and component terms;
the false perimeter-only arbitrary-perforated-window claim is not used.
Clean disk boundaries and ranks are now fixed. An all-D one-pair
lemma would coarsen those disks into GE_(D-1), preserving complete
counts before and after dilation. UR_(D-1), with the per-face
small-block/large-block aggregation, would give an error tending to
zero as r0 grows.

The legitimate parameter order is: fix the finite macroscopic window
construction and target loss; choose r0 large using UR_(D-1); choose
epsilon small enough that epsilon r0^2 is small; then send the actual
window scale to infinity. Later send M to infinity at each fixed
original boundary. One must not choose r0 growing with L and suppress
the L r0^2 boundary term without a new estimate.

Near, but not exactly on, a boundary tangent one needs a finite cover
by neighborhoods of exact strata with these controlled choices. A
compactness or adaptive-neighborhood argument has to be written. Simply
declaring every small minor zero would change the actual tile set.

## 6. Global compactness/assembly still to prove

For GE_D disks, every filling extends to its own fixed small full
zonogon, so the full VECTOR lifts have a uniform extrinsic Lipschitz
bound. Extend to a common box only for compactness. A finite profile
cover has subquadratic logarithmic size, just as in the scalar UR3
argument. Its limit is a vector lift with Va=x. The needed minor
closure is ALREADY supplied by accepted fixedD structural Section2:
det(grad f,grad g)=partial_1(f partial_2 g)-partial_2(f partial_1 g)
in distributions; uniform convergence and bounded derivatives preserve
the nonnegative minors. K_D is compact by Cauchy--Binet and the
explicit row reconstruction from those minors. This applies on each
fixed interior region eventually present in the varying domains.
It does not assert sufficiency of K_D for arbitrary profiles or its
convexity, and no new proof of that accepted closure is proposed here.

At differentiability points, choose disjoint small matching windows
with the necessary whole buffers. Their tangent determines a strict
chart or one boundary reduction. A finite Vitali-type selection could
cover all but a prescribed small area, with expanded buffers disjoint
after paying their relative boundary strips. Actual cut geometry,
complete heights and discarded tiles must be coded before any
independent insertion. A single finite chosen window family permits
the sum of perimeter costs to be made lower order in the large scale.

Coordinate deformations vary with a filling. The image of an old
physical window is not automatically one fixed new parallelogram.
The common affine error gives proximity to the fixed linear image,
and bilipschitz constants control perimeters, but a precise boundary
code or fixed inner-core construction is still needed. This is a
material seam/shape issue, not settled by the chart algebra alone.

After all upper fibers are fixed, select ONE actual reference filling.
Its integer dilation fixes the exterior of every chosen core. The
lower choices (strict canonical insertions or inductive clean-disk
insertions) must be disjoint, preserve every original fine boundary,
and be recoverable by restriction. The desired summed inequality is

    log2 Z(B_j)
      <=liminf_M M^-2 log2 Z(M B_j)+o(r_j^2)

along any hypothetical positive-deficit sequence. Proving all listed
interfaces would yield UR_D by contradiction. At present the uniform
strict, all-D single-pair and vector-window assembly interfaces remain
unproved. This note is a detailed route for further reasoning, not
a replacement for those proofs or their independent audits.
