# Blind whole audit of the fixed-D structural packet

2026-10-16 UTC. Reviewer: `review_2021_reasoning_j15_r2`, in a fresh
nonconstructor assignment. This is an initial independent report; no
other new fixed-D structural review, issue ledger or conclusion was read.
The reviewer did not construct either note. Requested setting:
`gpt-6.1-sol`, reasoning `max`; no independent effective-setting readback
is available. Only this report's assigned prefix is edited.

## Recommendation and exact scope

I find no unresolved substantive objection to the partial structural
lemmas or the compact-profile identity, with the definitions and
qualifications in the frozen packet. I independently reconstructed the
dictionary, compactness and minor argument, both nonconvex examples,
weak-order bounds, monotone padding, rational multigrid realization and
rational density, and the upper entropy maximum. The proofs below make
explicit a few standard intermediate steps; none changes a hypothesis
or repairs a counterexample.

This recommendation does **not** certify a formal annulus theorem, an
implication from an already precise EAI_D hypothesis, profile recovery,
(H), or a full 2017 solution. EAI_D is a research target with unresolved
window, phase, corner and stratum definitions. Its intended recovery
application is a program, as the note explicitly says. The open items in
the issue ledger retain that distinction. Only the coordinator may
promote the audited partial results after the other blind audit.

The fixed input hashes supplied by the coordinator are:

- Structural note: `c776e81d0fd44c0e8042ddc00a0d949966cdc106ba9b7e67486dc4d14a1b7d87`.
- Profile note: `973e8d7da034082b4416100d51650798ec3eb90e75cfd44106b5810dd9ec7e8d`.
- Source record: `e33ef844964e5cdfa0420696c2ee08ab90600ac766b9d7aa3667e8776c7ac3c0`.

The separate input-validation and freeze records check these bytes,
dependency hashes and the preservation of my older frozen packets. No
candidate file was edited. No mathematical enumeration, CAS, numerical
experiment or finite-search certificate was used.

## 1. Domain, marked count and dependency boundary

The [official 2017 B4 statement](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-2_1.pdf)
asks for the lower and upper limits of `log_2 C(n)/n^2`, for integer
`n>=2`, for the full tiling count in the given regular polygon. The
[official notes, p. 12](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-solutions-preliminary_1.pdf)
identify commutation classes and give `C(3)=2, C(4)=8`. This is the
established marked-frame dictionary, with no rotation/reflection quotient
and no extra labeling factorial.

I read the accepted coarsening statement and its reviewed exposition,
not another new structural review. They establish the full block count
`B(m_1,...,m_D)` and the conditional transfer from (H). They expressly do
not establish (H). Here `D` is fixed, `p` is a positive integer, and
`B_D(p)=B(p,...,p)`. Dividing a normalized logarithm by the fixed number
`D^2` changes neither existence nor the recovery issue. The trivial
two-direction case is included in the structural construction; the
nontrivial conditional transfer uses unbounded fixed `D>=3`.

## 2. Integer parallelograms and oriented curves

Put `v_i=(1,i-1)` and `Z_p=sum_i[0,pv_i]`. All ordered determinants
`det(v_i,v_j)=j-i`, for `i<j`, are positive. An inversion-creating
adjacent swap replaces a path segment `v_i,v_j` by `v_j,v_i`. Both are
graphs over the same x interval and the latter is strictly higher in
its interior. Thus successive positive swaps add disjoint parallelogram
shells. Their initial and final paths are exactly the lower and upper
boundaries of `Z_p`; a reduced block reversal fills the intervening
region. Commuting disjoint swaps changes the shelling order only.

For the converse, draw each color-i de Bruijn curve between midpoints
of opposite i-edges in a tile. Its local displacement is `+/-v_j` in
an ij tile. Choose the sign making `ell_i=det(v_i,x)` strictly increase.
The same choice continues across a shared i-edge, so every component is
a proper simple arc. It cannot close or return to an earlier point,
since ell_i strictly increases. Its only possible endpoints are the
two color-i boundary side intervals, one at each extreme ell_i value.
There are exactly p arcs of that color.

At a crossing of colors `i<j`, the oriented directions are `+v_j` and
`-v_i`; their determinant is positive. The local sign is therefore the
same at every crossing of the same pair of arcs. Proper simple arcs in
a disk have algebraic intersection zero or absolute value one,
according to the cyclic order of their four endpoints. The color side
intervals occur in alternating order for distinct colors. Each such
pair consequently crosses exactly once. Same-color curves are disjoint
by their construction. The boundary ranks and all crossing orders are
the marked bundle arrangement used by the accepted wiring dictionary.

The remaining standard dictionary step is the topological sweep of this
bundle arrangement and the event-poset description of commutations.
It is within the accepted marked wiring equivalence, rather than a
new assumption about stretchability. In particular, no straight-line
realization of arbitrary pseudolines is needed. Conversely the swept
word recovers the same tile corners by its prefix color counts.

There is no hidden T-junction model here: the note imposes face-to-face
incidence. Every allowed edge has x displacement one and integer
endpoints, hence no integer vertex lies in its relative interior. The
integer deformation preserves the combinatorial count; it does not
replace it by arbitrary packings or by periodic tilings.

## 3. Finite encoding, lifts and compact K_D

For fixed D, only finitely many integer-origin prototiles can meet a
specified unit square. Recording their types and relative origins gives
a finite alphabet. A bounded neighborhood suffices to check that any
recorded tile is recorded consistently in all squares it meets, that
interiors cover exactly once, and that intersections are allowed full
faces. The designated polygon and outside-empty constraints impose the
boundary. This establishes a finite-range coding, without any claim
that its specified boundary has negligible cost.

Lift each oriented i-edge by `e_i`. A tile's lifted boundary sums to
zero. Because the full tiled polygon is a disk, all closed cellular
paths are generated by face boundaries, so the lift based at zero is
well-defined. On an ij tile it is affine. Its projection by V is the
physical position. Crossing a color-i curve changes the i-coordinate
by one; the p ordered curves of that color give the vertex bounds
`0<=a_i<=p`. These bounds also control absolute height offsets, rather
than only gradients.

Solving the two equations for an ij tile gives

    J_i=(j-1,-1)/(j-i),   J_j=(-(i-1),1)/(j-i),
    J_r=0 otherwise.

The only nonzero ordered row minor is `Delta_ij=1/(j-i)>0`.
There is a common finite derivative bound depending on D. On the convex
polygon, integration along segments gives a common Lipschitz bound,
including across tile boundaries. After normalization all profiles lie
on the same compact domain, have the same boundary trace, and take
values in `[0,1]^D`. Arzela--Ascoli therefore gives compact uniform
closure `X_D`.

For Lipschitz coordinate functions the distributional identity

    det(grad f,grad g)=div(f partial_2 g,-f partial_1 g)

is valid by approximation, or directly by weak derivatives. If `f_n`
converges uniformly and the derivatives of `g_n` are uniformly bounded,
then `f_n grad g_n` converges to `f grad g` in distributions, after taking
a weak-* derivative subsequence. The limit derivative is forced by the
uniform function limit. This proves weak convergence of the minors.
Each limiting minor is an L-infinity function and a nonnegative
distribution, so it is nonnegative almost everywhere. Also `V grad h=I`
passes to the limit. Thus membership in K_D is a valid necessary
condition. No sufficiency for non-affine profiles is inferred.

To check compactness of K_D, write `J_i=(a_i,b_i)`. Cauchy--Binet gives

    1=det(VJ)=sum_(i<j)(j-i)Delta_ij.

All ordered minors are nonnegative, so each is bounded. Taking
determinants against the two rows of `VJ=I` gives, with antisymmetric
Delta notation,

    sum_k (k-1)Delta_ik=a_i,
    sum_k Delta_ik=-b_i.

This bounds every entry; the defining equalities and inequalities are
closed. Rank two and at least one strictly positive minor follow from
the same identity. They remain true on boundary strata.

Each pair of the p color-i and p color-j curves crosses once, so a full
tiling has exactly p squared ij tiles. Its ij minor integrates to
`p^2`, because tile area and nonzero minor are reciprocal. The normalized
integral is one. The boundary null-Lagrangian identity yields the same
answer. Uniform derivative bounds prevent a boundary concentration
problem when passing these integrals to limits.

## 4. Same-frame nonconvexity, including the regular octagon

Both displayed words are valid six-swap reversals of 1234. In the first,
the 12 crossing has prefix 4; in the second, the 34 crossing has prefix
2. Thus the designated tile origins are `(1,3)` and `(1,1)` in the
integer geometry. Each tile has center `(2,7/2)`. The two normalized
lifts have identical full zonogon boundary data and affine gradients
J12 and J34 on a common open neighborhood.

Their averaged rows are exactly the four rows in the note. In
particular, `det((1/2,-1/2),(-1,1/2))=-1/4`. The minor-closure lemma
therefore excludes the averaged profile from X_4. Dilation by any
positive integer and subdivision of every enlarged tile into its same
pair-type grid preserve the normalized original lift exactly. These
are admissible profiles even under a definition using arbitrarily fine
tilings. Neither a change of frame nor an unmatched boundary was used.

For the regular octagon, subtracting v4 from `(1/2,5/4)` and solving in
the basis `(v1,v2)` gives the two coefficients printed in the note.
Subtracting v2 and solving in `(v3,v4)` gives its other two coefficients.
All are strictly between zero and one. The row-1 dual covector on a
12 tile is `(v2_y,-v2_x)/det(v1,v2)` and the row-4 covector on a 34
tile is `(-v3_y,v3_x)/det(v3,v4)`. Their averaged determinant is

    -det(v2,v3)/(4 det(v1,v2) det(v3,v4))<0.

This independently checks the exact square-root example and the stated
general sign. It refutes convexity of these same-frame profiles, not
(H) or a variational theory on a nonconvex admissible set. It does not
say that all nonconvexity causes entropy-limit failure.

## 5. Weak-order join, meet and the displacement bound

Label each occurrence by color and increasing within-color rank.
Inversion pairs are pairs in increasing initial label order. A
permutation inversion set is closed and coclosed on every three labels.
Conversely those two properties make the oriented complete comparison
graph have no directed triangle, hence be a total order. This
characterization includes intermediate labels of the same color.

Take U to be the union of the family's inversion sets and take its
transitive closure S along increasing labels. If `a<c` is realized by
a U path and b lies between them, either b is a path vertex or it lies
inside one edge. In the latter case, coclosure in the original
inversion set containing that edge attaches b to the prefix or suffix.
This proves coclosure of S; closure is automatic. Every U edge strictly
increases color, so the same holds on paths, no same-color inversion
arises, and every path has at most D-1 edges. S is the least inversion
set containing U and is therefore the join inside the shuffle interval.

Let `t(a)=pos_w0(a)`. If `(a,b)` is a U inversion absent from w0,
then `t(a)<t(b)`, but some word w has b before a. The assumed displacement
bound gives `0<t(b)-t(a)<=2r`. If a U edge already belongs to w0, its
increment of t is negative. Adding increments along a path shows that
any newly created inversion has reference gap at most
`R=2(D-1)r`. Every old w0 inversion is retained because w0 is in the
family. Thus comparisons at reference gap greater than R are unchanged.
For a label initially at position t, all labels below t-R still precede
it and all labels above t+R still follow it. This bounds its new
position between t-R and t+R; the conclusion is R, not an extra factor
of two.

Reverse each word and replace each within-color rank by its reverse
rank. This preserves the increasing internal order in the newly named
shuffle, complements cross-color inversions up to the fixed renaming,
and sends positions to `N+1-position`. It is the required order-reversing
involution and preserves all relative displacement bounds. The meet
bound follows from the join bound. Zero r, missing colors, a singleton
family and repeated family elements cause no exception. Keeping D
fixed is essential to the path-length estimate.

## 6. What geometric padding does and does not establish

In the integer geometry every word vertex has x equal to its prefix
length. Moving each occurrence by at most R changes a prefix count of
each color by at most R. The y discrepancy is therefore at most
`sum_i(i-1)R=O_D(R)`; the lift discrepancy is also bounded by a
D-dependent constant times R. The path envelope bound is consequently
pointwise as asserted.

A comparable pair in the weak order admits a chain of adjacent
inversion-creating swaps. Its positive shells tile the strip between
the two physical graph paths. Applying this below and above an already
tiled patch supplies the claimed padding whenever the paths have the
same endpoints and color counts. A length O(L) strip of height O_D(r)
has area O_D(rL). Restricting to a fixed inner domain recovers the
original tiling. If inner paths vary, their O(L)-letter words, endpoint
and rank data have only O_D(L) bits at fixed D, apart from harmless
logarithmic coordinate bookkeeping. There is no factorial choice of
strand matching in this construction.

For a fixed periodic reference word with all active colors of bounded
gap, an error of at most r in prefix counts traps the kth occurrence
between reference occurrences k-r and k+r. Bounded gaps give
O(r+1) position error, with constants depending on that reference
period; endpoints are handled by clamping the ranks. This is not a
uniform constant over arbitrary periods or over a disappearing active
color. The note's use is at a fixed local periodic background.

These results concern comparable monotone sides with fixed flux. They
do not independently close a four-sided annulus, identify ranks at
corners or control a zero-density color's offset. The candidate keeps
these as separate obligations, correctly.

## 7. Multigrid construction, including degenerate strata

Let J be rational in K_D. Omit a zero row. Choose phases outside the
countable bad sets for coincident parallel lines or triple crossings.
Rationality is needed for periods, not for the initial existence of
generic phases. Two independent rows exist. Their strips already bound
all grid cells. In fact if x,y belong to one cell, every coordinate of
`J(x-y)` has absolute value less than one, so `x-y=VJ(x-y)` gives a
cell-diameter bound depending only on V. Parallel or oppositely parallel
row families do not invalidate boundedness.

Give a cell its vector of strip indices k. Crossing an oriented line
changes precisely one k_i by one. At an ij intersection the four cells
have the four heights of a unit ij square. The standard planar dual
complex has one such quadrilateral face, mapped by k -> Vk to the
desired nondegenerate parallelogram. The cyclic orientation of the grid
crossing is determined by `det(J_i,J_j)>0`, as is the target orientation
by `det(v_i,v_j)>0`. All dual faces therefore map with positive local
degree. Pairs with zero minor are parallel and have no crossing after
the phase choice; no degenerate face is inserted.

Here is the degree-one argument in more detail. Embed the abstract dual
using a point inside each convex grid cell and arcs across each common
grid edge. Its faces are bounded topological disks. Extend the map on
each face to an orientation-preserving parametrization of its image
parallelogram. For a cell representative x, strip indexing gives
`k=Jx-theta+O(1)`, so `Vk=x-Vtheta+O_D(1)`. Bounded primal/dual cell
diameters extend this bound throughout all faces. The resulting plane
map F is a bounded distance from the identity. It is proper and the
straight homotopy to the identity stays proper, so its degree is one.

For a target point off the image of the dual one-skeleton, properness
and local finiteness leave finitely many preimages. Each lies in a face
and has local degree +1. The sum is one, hence exactly one face covers
the point. This proves both coverage and nonoverlap of face interiors.
It also rules out unintended crossings of image edges: the two incident
positive faces occupy opposite sides of each edge and would create an
overlap near such a crossing. Around a dual vertex the positive face
angles give positive integer winding; degree one forces one winding
and excludes distinct interior vertices with the same image. The result
is a genuine face-to-face plane tiling, rather than just a formal
multicover. Primitive integer edges provide the same no-T-junction
check as before.

The tiling's lifted height k differs from J times its physical position
by a bounded amount, since both the grid parameter and its image differ
by a bounded amount. Thus the asserted affine asymptotics follow.
Choose a full-rank integer period lattice with `JP` integral; a common
denominator of J supplies one. Translation by a period shifts cell
indices by JP and physical vertices by `VJP=P`. It preserves phases,
the entire grid and the dual tiling. This proves periodicity on strata
with zero rows or parallel families as well.

The argument establishes a local plane background at each rational
slope. It supplies neither the prescribed full zonogon frame nor a
uniform annulus transfer to it.

## 8. Rational density without global convexity

For rows i<j and columns k<l, the off-diagonal exponent in the
2-by-2 minor of M_eta exceeds the diagonal exponent by
`2(j-i)(l-k)>0`. Since `0<eta<1`, the minor is strictly positive.
The matrix tends to the identity as eta tends to zero. Cauchy--Binet
then makes every ordered minor of `M_eta J` strictly positive: all
terms are nonnegative and at least one original J minor is positive.

Put `A=VM_eta J`. It tends to I, so for sufficiently small eta it is
invertible with positive determinant. Right multiplication by A inverse
restores `VJ_eta=I` and multiplies all minors by `1/det A>0`.
Consequently J_eta lies in the strictly positive stratum and tends to
J. The affine solution space `VJ=I` is rational and nonempty and has a
rational parametrization by a rational particular solution and a
rational nullspace basis. Rational points are dense in it. Approximating
J_eta closely inside that space preserves all strict minor inequalities.

This proves the asserted rational density. It is a pointwise operation
on a single gradient. Applying it to all gradients of a non-affine
profile need not yield an integrable gradient field or the original
boundary trace, so it cannot be silently used as global regularization.
The candidate expressly avoids that inference.

## 9. Upper semicontinuity and the exact maximum identity

The finite alphabet gives a direct finite quadratic upper bound at
fixed D, consistent with the accepted arrangement bound. Also there is
always at least one full tiling. Thus L_plus is finite and nonnegative.
For each h define the local ball limsup as in the note, with log zero
equal to negative infinity.

If `h'` tends to h, then for all sufficiently close h',
`B_(epsilon/2)(h')` is contained in `B_epsilon(h)`. The infimum defining
s_plus(h') is at most the limsup count on the smaller ball and hence at
most the limsup on the larger ball. Taking the upper limit in h', then
the infimum in epsilon, proves upper semicontinuity, including extended
values. Every local count is at most the full count, so s_plus<=L_plus.

If every s_plus(h) were strictly below L_plus, for each h there would
be a ball with local limsup strictly below some c_h<L_plus. A finite
cover by those balls exists. The full count is at most the finite sum
of their counts. Its logarithmic limsup is bounded by the largest of
finitely many c_h, still strictly below L_plus: a contradiction. This
gives equality and a maximizer. Alternatively upper semicontinuity and
compactness supply attainment. Convexity, differentiability of entropy,
or uniqueness is not used.

Profile recovery at just one maximizer, for every epsilon and all large
scales in the liminf sense, makes L_minus at least L_plus and proves
(H). The reverse implication from (H) to that fixed maximizer recovery
is not asserted. The identity alone contains no liminf information.

The abstract one-profile example is correct. For
`G(x)=x^2(1+sin(log x)/4)`,

    G'(x)=x[2+(2 sin(log x)+cos(log x))/4]>0,

because the oscillatory numerator has absolute value at most sqrt(5).
The floor changes successive differences by a bounded amount, so
`floor G(p+1)-floor G(p)=O(p)` and the counts are nondecreasing. Choosing
integers near `exp(2 pi k+t)` realizes every limiting logarithmic phase.
The normalized logarithm has lower limit 3/4 and upper limit 5/4.
There is one compact profile and an upper semicontinuous entropy
maximum throughout. This is an abstract insufficiency example, not a
tiling construction.

## 10. Source check and the intended lower recovery

The [Balister--Bollobas--Quas author manuscript](https://web.uvic.ca/~aquas/papers/paper15.pdf)
defines N(Lambda) from restrictions of global subshift configurations.
Theorem A applies to bounded convex windows with growing inradius;
Theorem B additionally requires strong irreducibility, defined by a
uniform filling distance. Neither theorem specifies the zonogon lift
used here. The candidate's source distinction is accurate. I checked
definitions and theorem statements on printed pp. 1--4, not the full
proofs of those published results.

For fixed physical mesh delta p, a bounded-width tile skeleton uses
O_D(p/delta) lattice cells; at fixed delta its description is o(p^2).
Fixing it separates interior boundary fibers. A box of side L has at
most exponential-in-O_D(L^2) record patterns. These are legitimate
upper bounds. They do not identify different fibers or make their
interiors insertable in an unrelated frame.

The proposed recovery architecture is coherent, but remains conditional
on more than the currently informal wording of a target. Differentiability
of h* supplies affine approximations on small windows at almost every
point; a finite disjoint selection can leave arbitrarily small area.
Global uniform approximation must be chosen much smaller than the
selected window sizes to make actual local lifts near the same affine
maps. A mesh skeleton fixes the absolute boundary traces, or those
offsets must be recorded at subquadratic cost. Those orders of choices
are possible at this upper-estimate stage.

At a fixed rational background, a rigorously defined family of windows
whose opposite boundary collars match under the background's period
translations can be replicated. Copy an L block in a large M block,
fill leftover strips by the reference tiling, and obtain
`N(M)>=N(L)^floor(M/L)^2` after the appropriate period units and collar
corrections. Finite alphabet bounds then give the corresponding fixed
family entropy limit. This elementary argument requires those matching
collars and commensurate window definitions; the phrase 'periodic
boundary' alone is not a general boundary-gluing theorem.

There is also no basic obstacle to an all-scale reference profile:
dilate one finite tiling and subdivide each tile, then add the bounded
number of remaining strands per color by the monotone boundary strips.
For `p=kq+r`, `0<=r<q`, this costs width O_D(q), so the normalized
profile error tends to zero as p grows, with q fixed. This produces a
reference, not many tilings.

The essential missing inference is entropy-preserving transfer from
each high-count actual local fiber to one of those reproducible families
and back into the all-scale reference. Precisely it must specify common
window shapes and collars, rational period choice, absolute lift offset,
phase compatibility between extraction and insertion, recoverability,
and error bounds with the necessary uniformity over the finite local
collection. The zero/parallel strata require either their own transfer
or a proved entropy approximation within the fixed global frame. The
note acknowledges all these obligations and calls its argument a
reduction/program, not a completed implication theorem. My recommendation
does not promote them by treating an informal target as an established
hypothesis.

The stated zero-density obstruction is real even with `Va=x` enforced.
For example, at a pure 12 slope with D>=3, add an integer multiple of
`(1,-2,1,0,...)` to an independent inner lift. This vector lies in ker V
and raises its color-3 coordinate while leaving its physical embedding
unchanged. Outer and inner boundaries have no color-3 edges. A proposed
interpolating annulus would have no possible endpoints for its color-3
curves; they cannot close because ell_3 increases along them. Hence no
such exact label-preserving annulus exists. Its scaled offset can be
arbitrarily small relative to the diameter. This validates the warning
against arbitrary near-flat collar interpolation. It does not refute
EAI_D with genuinely compatible data and explicitly controlled repair.

## 11. Initial disposition

The exact partial claims pass this independent whole reconstruction.
The finite-range model, rational background and upper entropy maximum
are not substitutes for the full fixed-boundary count. The nonconvexity
example prevents a specific invalid regularization shortcut; it leaves
nonconvex or stratified approaches open. The bounded weak-order
envelopes control sides, leaving the two-dimensional flux and phase
problem visible rather than solved.

No proof of H or of either requested 2017 numerical limit has been
audited into existence by this packet. The unresolved research items
are carried as explicit open targets, not false theorems or newly
discovered counterexamples to H. The separate issue log marks no
blocking objection to the limited partial-results recommendation.
