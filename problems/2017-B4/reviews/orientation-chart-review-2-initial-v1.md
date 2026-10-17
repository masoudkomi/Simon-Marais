# Initial independent whole audit R2: finite orientation charts

2026-10-17 UTC. Reviewer /root/review_2022_complexity_r2 did not construct
the target. Requested gpt-6.1-sol/max; independent effective-setting
readback unavailable. This full report, per-claim ledger and source
checks are frozen before reading peer orientation-chart findings.

The target is the complete coordinator-orientation-charts-candidate-v1.md,
SHA-256 a64eea09f6cab7ba86f158cc685ab20d35742c4d8dbfc3dfb60260a3b7ada552,
with complete freeze-v1.json,
338a50e977061e29a379cf311273d5d8edada01ebf86891aa80d4afa74cd1da0.
I read the official domain, the entire accepted fixed-D structural
dependency and its precise acceptance, not just the new note's summary.

**Finding:** OC1--OC3 and the D=4 type corollary reconstruct in their
stated scope. I found no substantive objection or required mathematical
repair. Zero rows, antiparallel endpoint rows, all rank transformations,
full tiling injectivity, uniform deformation constants, the affine
offset and Cauchy--Binet nondegeneracy all survive the checks below.
This is not a promotion. No H, PR, entropy recovery, common chart for
an arbitrary nonaffine profile, or official limit conclusion follows.
No mathematical computation, enumeration or CAS was used.

## 1. Exact hypotheses and dependencies

The [official 2017 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-2_1.pdf),
page 2, B4, concerns marked tilings in the fixed regular polygon and
both asymptotic normalized logarithmic limits. This packet establishes
finite-D interfaces, rather than evaluating those limits. The full
B4 is in scope; no other problem was investigated.

Fix D>=2, v_i=(1,i-1), V=[v_1 ... v_D], and a real D-by-2 matrix J
satisfying VJ=I and all ordered row minors nonnegative.
In particular J has rank two; a zero matrix or a one-dimensional
row span is impossible. Zero individual rows and zero minors are
allowed and must not be removed by a hidden strictness assumption.
Since

    1=det(VJ)=sum_(i<j) (j-i) det(J_i,J_j),

at least one ordered row minor is positive. The count/deformation
claims concern actual full balanced marked zonogon tilings with
positive integer content p in every color. They do not assert a
new count theorem for arbitrary incomplete windows, arbitrary
unmarked packings, or a degenerate point called a full tiled disk.

The accepted dependency is reviewed-fixedD-structural-v1.2.md,
SHA-256 421dc271ed65831e3aa70057a0d74c4d999ba8249dfa2b99066dfdc298f86868,
and its exact acceptance. It supplies the canonical integer lift,
full ranked de Bruijn arrangement, count dictionary and fixed
boundary interpretation. Its separate unproved EAI/PR/H targets,
and the later rank-mesh program, are not premises.
Below I reconstruct the new deformation explicitly rather than
letting that accepted dictionary stand in for a missing proof.

## 2. OC1: weak angles, endpoint inversions and choice of cut

Let f be the first nonzero row. Measure row angles from J_f using
the positive orientation; this is only an angle-coordinate choice
and does not change the physical vectors V in later formulas.
For every later nonzero row J_i, det(J_f,J_i)>=0 puts its
angle theta_i in [0,pi]. All earlier rows are zero.

If i<j are nonzero and theta_i>theta_j, their difference lies
in (0,pi]. A difference strictly below pi would give
sin(theta_j-theta_i)<0, contrary to the minor condition.
The only possible inversion would therefore be theta_i=pi
and theta_j=0.

Such an endpoint inversion cannot coexist with a row of angle
strictly between zero and pi anywhere in the list. If that row
is before i, its minor with the later angle-zero row is negative.
If it is after i, including between i and j, its minor with
the earlier angle-pi row is negative. Thus every nonzero
row would have one of the two endpoint angles, making the
row span one-dimensional. Rank two rules this out.
Consequently the nonzero angles are weakly increasing.

There must be a strictly positive angular gap between two
successive nonzero rows. Otherwise all nonzero rows would
point the same way and again span only a line. Let h<k
be the original indices on either side of such a gap;
all intervening rows are zero and k>=2.
After keeping the suffix and negating the prefix, the
nonzero angles in the reordered list are

    theta_k,...,theta_last,theta_f+pi,...,theta_h+pi.

The join is weakly ordered because theta_last<=pi=theta_f+pi.
The full angular width is

    theta_h+pi-theta_k=pi-(theta_k-theta_h)<pi.

Thus a slightly larger angular interval of width pi contains
every nonzero direction in its interior. This supplies a
common open half-plane, including the cases where the old
list used both endpoint directions. Old antiparallel endpoints
can now have the same positive direction at the join; they
do not remain antiparallel.

All ordered row minors in the reoriented list are nonnegative,
since differences of weakly ordered angles lie in [0,pi).
Equal directions are positive parallelism, and equal values
are consecutive among nonzero rows. Interposed zero rows
do not create an inversion or a distinct group.
The choice k lies in {2,...,D}; although it depends on J,
there are only D-1 possibilities. No continuum of chart
orientations is introduced.

To justify the last OC1 assertion, the finite nonzero row set
in an open half-plane has a column vector u with J'_i u>0
for each such row. Finitely many strict inequalities remain
true on a neighborhood of u, so choose v there independent
of u. This proves the two positive directions. It does not
give a uniform cone margin when a gap or row degenerates.
The candidate explicitly avoids that stronger assertion.

## 3. OC2: translated polygons, canonical lifts and exact ranks

Fix k and let S be the diagonal sign matrix: -1 on the prefix
i<k and +1 on the suffix. First make the change before
permuting, then apply the same fixed cyclic permutation to
columns, rows, labels and ranks. Directly,

    a'_i=a_i                 for i>=k,
    a'_i=p-a_i               for i<k,
    v'_i=epsilon_i v_i,
    x'=x-p sum_(i<k) v_i,
    V'a'=Va-p sum_(i<k)v_i=x'.

This includes the constant p on every flipped coordinate:
merely replacing a_i by -a_i would move the canonical initial
corner and lose the rank interval. The new coordinates
remain between zero and p at vertices.
For an original color-i edge of rank r, whose endpoints
have a_i=r-1,r, flipping gives endpoints p-r+1,p-r.
In the new positive edge orientation its rank is therefore
p-r+1. Equivalently the level r-1/2 is sent to
(p-r+1)-1/2. This supplies the exact recoverable fine rank,
not only an unranked color.

At the polygon level,

    sum_i[0,pv'_i]
      =sum_i[0,pv_i]-p sum_(i<k)v_i.

Every tile is the same physical parallelogram after this
translation, with its edge orientation changed on flipped
colors. The canonical new origin corresponds to the original
boundary vertex p sum_(i<k)v_i. In the new cyclic order
k,...,D,1,...,k-1 the vectors have angles

    phi_k,...,phi_D,phi_1+pi,...,phi_(k-1)+pi,
    phi_i=arctan(i-1).

Their width is pi-(phi_k-phi_(k-1))<pi and every
ordered physical determinant is positive. Hence the translated
boundary has the usual ascending and reversed chains for
those new vectors. Starting at the corresponding vertex
explains the boundary word change rather than quotienting
out a rotation or forgetting a marking.

The derivative of the flipped height is S J before the
permutation; the derivative of x'=x-constant is the identity.
With the simultaneous permutation this is exactly J', and
V'J'=I. Reversing p-a_i, the permutation and the fixed
translation recovers every original vertex, tile, label,
rank and complete boundary word. Thus the operation is
an exact bijection on full marked tilings at each p.
It does not assert any one k works for every tangent in
a varying profile.

## 4. OC3: actual standard deformation, degree and inverse

Now index the new slots by 1,...,D and set w_i=(1,i-1)
in those slots, W=[w_1 ... w_D]. These are new standard
directions; they are not the signed original vectors with
their old indices retained. Define on the reoriented full tiling

    F(x')=W a'(x').

On each tile of type i<j the map is affine, with derivative

    W_(ij) (V'_(ij))^(-1).

Its determinant is det(w_i,w_j)/det(v'_i,v'_j)>0.
The continuous canonical lift makes these formulas agree
on shared edges. Integer vertex lifts give integer target
vertices, and each tile becomes the indicated standard tile.
The boundary is mapped in its complete cyclic color order
once around the convex standard balanced zonogon.

Here are the details behind the degree argument. For a
regular point outside the finitely many image edges, the
signed preimage count is the winding degree of this boundary:
one inside the target polygon, zero outside. Every tile
interior preimage has positive sign. Hence interior
regular points have exactly one preimage and exterior
regular points have none. No target tile can protrude
outside the target polygon: its interior would supply
an exterior regular point with positive degree.

At an old interior edge the two incident positive tiles
map to opposite sides of its target edge; there is no fold.
At an interior vertex, the outgoing rays are selected from
the cyclic set {+v'_i,-v'_i}. Their replacement by
{+w_i,-w_i} preserves that complete cyclic order, since
both positive lists are strictly ordered inside half-planes.
All tile sectors retain positive angles. Their full fan
therefore gives local degree one and a local homeomorphism.
This is an argument about the closed tiling stars, not
only its faces. The corresponding partial fans at boundary
vertices respect the convex target boundary.

If two distinct interior points had the same image, their
local neighborhoods would produce at least two preimages
of nearby regular values, contradicting degree one.
An interior point cannot share a boundary image either:
its open image neighborhood would contain regular exterior
points, where degree is zero. The boundary map is already
injective by its convex cyclic order. Surjectivity follows
first for regular interior points and then by compactness
for their closure. This proves a full disk homeomorphism
and the required face-to-face tiling.

For the inverse counting map, take the canonical marked
lift of a standard tiling and replace W by V'. The same
positive determinant/cyclic boundary proof gives a full
reoriented tiling. Restoring the OC2 signs and translation
then gives the original tiling. Thus count preservation
does not depend on remembering an unrecoverable geometric
choice or on counting shelling histories.

## 5. Bilipschitz constants

For each fixed cut and pair i<j the preceding derivative
and its inverse

    V'_(ij) (W_(ij))^(-1)

are fixed finite invertible matrices. Their norms have a
finite maximum over all pairs and the D-1 cuts.
The source full zonogon and the target full zonogon are
convex. A segment in either passes through finitely many
affine pieces; integrating the derivative bound gives the
global Lipschitz estimate for F or F^(-1). Segments that
coincide with edges follow by continuity or by subdivision.
Constants depend on D and the finite cut family, and
are independent of p and the particular filling.

This reasoning uses full convex source and target polygons.
It would not justify a global inverse bound merely from
local derivatives on a holey or unspecified window.
The candidate keeps the actual full deformation, and
only afterwards restricts it to an image region.

## 6. Tangents and Cauchy--Binet nondegeneracy

For a chart chosen by OC1 set A=WJ'. All row minors
Delta_ij=det(J'_i,J'_j) are nonnegative and at least
one is positive. Since every standard minor d_ij=j-i
is strictly positive, Cauchy--Binet gives

    det A=sum_(i<j) d_ij Delta_ij>0.

Thus A is invertible and the tangent in target coordinates is

    J*=J'A^(-1),      WJ*=I.

Every row-pair determinant is multiplied by det(A^(-1)),
which is positive. Therefore zero minors, positive minors,
zero rows and positive parallelism are preserved exactly.
If u is strictly positive for all nonzero rows of J',
then Au is strictly positive for the corresponding rows
of J*, because J*_i(Au)=J'_i u. This directly preserves
the common open-half-plane property. There is no new
antiparallel direction concealed by the coordinate change.

The uniform lower bound uses more than rank two:

    1=det(V'J')=sum_(i<j) c_ij Delta_ij,
    c_ij=det(v'_i,v'_j)>0.

Let alpha_ij=c_ij Delta_ij. These weights are nonnegative
and sum to one. Hence

    det A=sum_(i<j) (d_ij/c_ij) alpha_ij

lies between the minimum and maximum of the fixed positive
ratios d_ij/c_ij. This remains true on every boundary stratum;
some or most weights may be zero. It does not require every
row minor to have a positive lower bound.
Both d_ij and c_ij are integer absolute direction differences
between one and D-1, so the weaker bounds
1/(D-1)<=det A<=D-1 are already sufficient uniformly over
the cuts.

Under ||J||<=G, sign changes and permutation preserve the
Euclidean norm (or give equivalent fixed-D bounds for
another chosen norm). Then A=WJ' is bounded in terms
of D,G. In dimension two, the adjugate formula and the
determinant lower bound give a bound for A^(-1), then
for J* and I-J*W. Thus the stated uniform norm claims
are valid. A determinant bound by itself would not control
an arbitrary unbounded matrix norm; the explicit G
qualification prevents that invalid inference.

## 7. One affine offset on the actual image region

Suppose the actual source lift has the stated approximation

    a'(x')=J'x'+c'+e(x'),    V'c'=0,    |e|<=E.

The identity V'a'=x' also implies V'e=0, although
that is not needed to derive the next algebra. Since
y=W a'=Ax'+Wc'+We and J*A=J', direct substitution gives

    a'-[J*(y-Wc')+c']=(I-J*W)e.

Writing c*=c'-J*Wc' yields

    a'=J*y+c*+(I-J*W)e,      Wc*=0.

The error norm is at most ||I-J*W|| E. The source-to-target
homeomorphism makes this an actual estimate on its image,
with a single fixed c* for the whole source region.
No corner-dependent normalization or separately chosen
port offset is introduced. The formula holds without a
derivative assumption on e.

If this is derived from an original approximation a=Jx+c,
the OC2 sign/translation operation also produces one
common c': it is obtained by expanding x=x'+p sum_(i<k)v_i
and the fixed p-a_i formula. V'c'=0 follows from
the exact lift identity. So there is no missing phase
choice between OC2 and OC3.

The estimate does not identify the image region with
a canonical parallelogram or lens. Its shape and buffer,
and any all-side rank compatibility needed by another
theorem, remain separate hypotheses. The candidate
expressly retains that distinction.

## 8. D=4 types and limits of the inference

The reoriented nonzero rows have at least two distinct
directions, since they span R^2, and at most four.
If there are four groups, all four rows are nonzero
and their angles are distinct inside an interval
of width less than pi. Every ordered row minor
is therefore strictly positive.

With three groups there are only two possibilities:
three nonzero rows and one zero row, all three
nonzero directions distinct; or four nonzero rows
with multiplicities 2,1,1. In the latter case the
parallel pair is consecutive in the nonzero order,
and there are two singleton groups. This includes
the group that may have been formed from old
antiparallel endpoint rows. Any interposed zeros
can be deleted for the reduced list while their
original labels and zero status remain recoverable.

With two groups there can be several multiplicities
and zero rows. The algebra alone supplies neither
an entropy value nor a general multiple-merged-group
port theorem. The candidate does not assert one.

These types match possible inputs to other strict
or clean-stratum lemmas, but matching a type is
not a proof of those lemmas' hypotheses, rare-tile
flux estimates, reference exteriors, global seams,
profile regularization, or recovery. In particular
the finite family of possible cuts is not a single
chart valid on every part of a nonaffine profile.
All of these scope boundaries are stated accurately.

## 9. Adversarial disposition and preservation

The whole argument was checked for first/last zero rows,
zeros between a chosen angular gap, endpoint inversions,
antiparallel endpoints, D=2, rank-two necessity, positive
versus negative parallelism, canonical starting corner,
the flipped rank r to p-r+1, the simultaneous label
permutation, full boundary injectivity, edge/vertex stars,
inverse count recovery, segment integration, zero-minor
boundary strata, determinant versus norm bounds, common
offset and actual image shape.

No counterexample or unresolved substantive inference
was found. No routine enumeration or mathematical
program was needed. The source dependency's prior
qualifications are preserved; this audit does not
resolve its EAI/PR/H targets.

Only orientation-chart-review-2-* review records are
written. The exact candidate and all earlier frozen
own records are separately fingerprinted. No Git,
candidate/shared edits, spawning, charges, outside
contact or separately billed API occurred.
No peer orientation-chart findings were read before
this full initial freeze. Coordinator acceptance
requires both independent reviews and remains
outside this reviewer's authority.

Latest authoritative weekly total usage:26% at
2026-10-17 06:35:13UTC, window10080minutes,
reset1792745187. The90% total ceiling and
integration/review reserve remain in force.
