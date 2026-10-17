# Reviewed closed rank-matched collars and rational frame entropy

**Proved, independently reviewed partial results A1-A5**, accepted
exposition v1.2, 2026-10-17 UTC. This register accepts the author's FULL
v1.1 replacement after two fresh initially blind WHOLE nonconstructor
audits of v1, a substantive author repair, and BOTH independent targeted
reaudits. The coordinator read both full original reports/ledgers,
complete replacement and repair, and both full targeted reports/issues/
sources, then verified the immutable records. No substantive issue remains
in the repaired stated scope. Frozen v1, its counterexample, both initial
reports and the full v1.1 repair remain unchanged.

AR1-01 was a real standalone-domain defect: ideality of literal prefix
sets could erase a negative height of an absent inner color. The exact
counterexample is preserved below. The repaired A2 explicitly requires
ALL color ranks within the available box, including absent colors; A3
first derives that box by winding, then proves ideality. Both reauditors
reconstructed the correction. Reviewer2 explicitly acknowledges the
initial missed omission without overwriting the original report.
ANN2-N1/N2's strict-nesting and complete conditional-scope clarifications
were also checked by both. Only this acceptance header is new; the full
frozen v1.1 mathematical body below is unchanged, and its historical
candidate/pending labels are superseded by this scoped register.

Accepted: global outer-poset rank-prefix criterion; exact fixed-boundary
annulus injection for actual nested comparable Jordan lenses satisfying
the explicit all-color range and ideals; a common-affine positive-minor
buffer test; rational strict flat digital frames with fixed phases and
bounded corner trims; the all-scale entropy limit of THESE receiving
frames. Constants can depend on the fixed strict slope. Arbitrary cut
windows, zero-minor uniformity, global profile recovery and the full
balanced-zonogon hypothesis H remain outside this acceptance. No full
2017 solution or novelty is claimed. See ../reviews/annulus-acceptance.md.

---

# A closed rank-matched collar at a strictly positive rational D4 slope

2026-10-17 UTC. **Candidate proof - unverified, version 1.1.** Constructor:
`review_2017_coarsening_r1`, in a separate construction assignment after
freezing all assigned reviews. Requested `gpt-6.1-sol` / `max`; effective
settings have no verified readback. Two fresh independent nonconstructor
whole audits are required. No proof of hypothesis(H), no full2017
solution and no novelty are claimed.

This complete versioned copy repairs the standalone rank-domain omission
AR1-01 identified by the first fresh whole audit, and makes the second
audit's ANN2-N1/N2 geometric and scope clarifications explicit. Both
complete initial reports and ledgers were read only after their freezes.
The frozen v1 and all initial reports remain unchanged. Both targeted
independent re-audits and coordinator reconciliation are required; this
author copy does not close a reviewer issue or promote the result.

The principal results below are A1--A5: a global rank-prefix criterion,
an exact tiled annulus, a quantitative strictly-positive collar test,
rational flat boundary frames, and a boundary-preserving local entropy
limit. They are narrower than an extension theorem for arbitrary cut
windows or all boundary strata. They do close the four sides and corners
for the explicitly specified two-path lens boundaries.

## 0. Geometry, word convention and the precise advance

Fix v_i=(1,i-1), i1,2,3,4, and let V have these columns. A positive
edge of color i has displacement v_i and lift e_i. All tilings are
face-to-face tilings by the six positive ij parallelograms. Heights a
are integer vertex lifts with Va=x. A word with N_i occurrences of
color i is ranked internally: its k-th occurrence is label(i,k).
Initial labels are ordered by color, then rank. Weak order means
inclusion of cross-color inversion sets.

Two words p<=q with the same content define a weak lens: the closed
physical region between their positive-edge paths. In the main annulus
theorem both boundaries are Jordan lenses, meaning the paths meet only
at their common endpoints. Weak lenses with additional common pieces
are allowed in the later entropy gluing statement; their open lobes
are tiled independently with the prescribed lifted boundary.

For completeness, inversion inclusion gives an adjacent-swap chain.
At the first position where p and q differ, move q's desired next label
leftward across the intervening labels of p. Each crossed label must
be smaller in the initial order: the opposite comparison would remove
an inversion already present in p, contrary to inclusion. Each move is
therefore inversion-creating; same-color labels are never crossed.
Repeat. Swapping ij to ji for i<j adds the positive ij tile above the
old path. Its interior is disjoint from every previously swept region.
Thus a chain actually tiles the weak lens in the plane. This is a
degree-one shelling, not a possibly folded projection of an abstract
surface. Unit horizontal edge displacement prevents a hidden vertex
strictly inside an edge.

The old bounded-displacement meet/join lemma concerns a one-dimensional
band. It does not by itself close a collar. Here all color-rank
comparisons are enforced together by one poset. A closed-loop winding
test then certifies its prefix constraints, including corners. No
inference from mere prefix-height discrepancy to label displacement
is used below. In particular the constants are not asserted uniform
as a slope approaches a zero-minor stratum.

## A1. Exact prefix criterion for one whole outer frame

Fix outer words p0<=q0 of content N. Define a poset P0 on all ranked
labels by the comparisons on which p0 and q0 agree. This is the
intersection of their two total orders and is therefore transitive.

**Claim A1.** A shuffle w belongs to[p0,q0] exactly when it is a
linear extension of P0. An integer vector h with0<=h_i<=N_i is the
prefix count of such an extension exactly when

    I(h)={(i,k):1<=k<=h_i}, defined for 0<=h_i<=N_i,

is an ideal of P0. Its rank-box domain is part of the assertion; the
set formula alone is not a substitute for the coordinate bounds.
Equivalently, for every i<j the point(h_i,h_j)
belongs to the closed two-color weak lens between the i,j subwords
of p0 and q0.

For the first assertion, an inversion of p0 is forced in both orders,
and a noninversion of q0 is forced in both. The other pairs are exactly
the unconstrained comparisons. This is precisely inversion inclusion.
The same-color comparisons are always forced. For the second assertion,
a prefix is necessarily an ideal. Conversely concatenate the restriction
of p0 to I(h) with its restriction to the complement. The ideal
condition ensures that this is still a linear extension of P0.

Here is an explicit check of the geometric equivalence, including grid
vertices on the two-color boundary. Let b_p(k) be the number of j's
before the k-th i in a two-color word, and put b_p(0)=0,
b_p(N_i+1)=N_j. Since p0<=q0, b_p0(k)<=b_q0(k). At h_i=s the
closed projected lens has exactly the integer vertical range

    b_p0(s) <= h_j <= b_q0(s+1).                       (1)

If the lower inequality fails, an unselected j is forced before a
selected i in both words. If the upper fails, an unselected i is
forced before a selected j. Those are exactly the two ways for I(h)
to violate a cross-color ideal relation. The conventions handle s0
and s=N_i. Thus the test is global, has no free strand permutation,
and fixes the identities of all boundary ranks.

## A2. Exact absorption and an actual closed tiled annulus

**Claim A2.** Suppose p0<=q0 bound a Jordan outer lens Omega0.
An actual tiled inner Jordan lens Omega has boundary words p<=q,
starts at integer height a and ends at b=a+m, and lies strictly inside
Omega0 in physical space. The outer frame starts at height zero, and
the available color-i ranks are 1,...,N_i. Explicitly require

    0<=a_i<=b_i<=N_i for every i.                       (R)

Identify the inner color-i ranks with the consecutive global ranks
a_i+1,...,b_i. Empty inner colors m_i=0 are allowed; their a_i=b_i
still must satisfy (R). Every boundary height h is coordinatewise
between a and b, hence lies in the domain of I. Assume every such
I(h) is an ideal in P0. Then Omega0 minus the interior of Omega has a
parallelogram tiling matching the complete inner and outer lifted
boundaries. It can be chosen from the inner boundary alone. Consequently
insertion of different inner tilings with that boundary is injective.

For an outer frame based at an arbitrary integer height z0, use the
relative condition z0_i<=a_i<=b_i<=z0_i+N_i and the ideals
I(h-z0). The global ranks are z0_i+1,...,z0_i+N_i. Rebase physical
coordinates by Vz0 and heights by z0; the proof below is then exactly
the zero-based statement. This is a fixed rank translation, not a free
change of the assigned inner offset.

The initial and final prefix sets I(a),I(b) are ideals. By (R), their
actual coordinate counts are exactly a,b, with no coordinate truncated
by the set formula. Let A be the p0 order restricted to I(a), and
B the p0 order restricted to the
complement of I(b). The two full words

    w_lower=A p B,       w_upper=A q B

are linear extensions of P0: inside the middle piece every prefix is
an ideal by hypothesis, and in A and B the ideal condition together
with p0's order ensures the same. Therefore

    p0 <= w_lower <= w_upper <= q0.                    (2)

The middle inequality is p<=q with the fixed rank shifts. Choose any
fixed adjacent-swap chain for the first and last comparisons. They
tile the lower band p0--w_lower and upper band w_upper--q0. Between
w_lower and w_upper the paths coincide along A and B, and their
remaining region is exactly the given inner lens. Retain its actual
tiling. The three pieces have disjoint interiors by the pointwise
ordering of the swept paths. Their union is Omega0.

This constructs a genuine annulus around Omega: the two bands meet
along the fixed entry and exit seams A,B. Their positive x directions
put A entirely before the inner left endpoint and B entirely after
the inner right endpoint, so neither seam enters the inner interior.
There is no missing corner cap. The two seams are an explicit cut of
the annulus into the two shellable bands. Every seam edge has the
same global color rank on both sides by its prefix height.

For a fixed inner boundary choose A,B and the padding chains once,
before varying the inner tiling. Restriction to the designated core
then recovers the original tiling exactly. This gives injectivity
without a matching factor, a crossing-order factor or a label factorial.

If the inner boundary itself varies but has at most cL letters on
each side and relative integer heights of magnitude at most cL, the data
(a,p,q) have at most

    (2cL+1)^4 * 4^(2cL)

possibilities, up to an additional polynomial factor for a length
convention. A fixed boundary code recovers the inner region and hence
its tiling from the output. Thus the same map on such a family has
fibers2^(O_c(L)), even if distinct boundary codes yield the same final
outer tiling. This is an actual entropy transfer estimate.

## A3. Six closed projections give a quantitative positive-slope collar

Let J be a4-by-2 matrix with VJ=I and every ordered row minor
Delta_ij=det(J_i,J_j)>0. Set

    M_ij=(J_i;J_j),
    sigma(J)=min_(i<j) least_singular_value(M_ij)>0.

The proof below does not require J rational. Rationality is used for
the canonical frames of A4.

**Claim A3.** Retain the outer Jordan frame, actual inner Jordan
lens, comparable words and assigned integer lifts of A2. Do not yet
assume (R), boundary ideality or strict nesting; use the containment
and vertex-distance hypothesis below. Normalize the outer starting
height to zero. Let a0(x) be the outer
boundary lift, and h(x) the assigned inner boundary lift, in common
physical and integer-height coordinates. Suppose for some c in ker V,

    ||a0(x)-Jx-c||_infinity <= E0 on the outer boundary,
    ||h(x)-Jx-c||_infinity <= E1 on inner boundary vertices.

If the inner lens is contained in Omega0 and its boundary vertices
have physical distance at least t from the outer boundary, where

    sigma(J)*t > sqrt(2)*(E0+E1),                     (3)

then both (R) and every ideal condition in A2 hold. Hence there is a closed
rank-matched tiled annulus and the stated injection.

The containment and positive vertex distance imply the strict nesting
needed in A2 in this exact geometry. Every boundary edge has integer
endpoints and horizontal displacement one. On each interval [k,k+1]
containing an inner edge, that edge and each outer boundary path are
affine graphs. At its two endpoints the inner vertex lies strictly
between the outer graphs, by containment and positive distance. Both
affine gap functions are therefore positive on the entire interval.
No interior edge contact is possible. The whole closed inner lens is
strictly inside the outer Jordan domain; compactness gives positive
separation. This argument does not claim that its minimum distance
everywhere equals the vertex bound t. The winding proof below tests
the boundary vertices, for which the stated bound is exactly available.

Fix an inner boundary vertex x and a color pair i<j. Let gamma be
the counterclockwise physical outer boundary and let gamma_ij be its
lift projected to coordinates i,j. The affine loop M_ij*gamma+c_ij
has winding one around every point in its interior, since det M_ij>0.
The point h_ij(x) is within sqrt(2)E1 of M_ij*x+c_ij, whose distance
from the affine boundary is at least sigma(J)*t. Thus h_ij(x) lies
inside that affine image and has distance greater than sqrt(2)E0
from its boundary. The straight homotopy from the affine boundary
loop to gamma_ij stays within sqrt(2)E0 of the former. It never passes
through h_ij(x), so gamma_ij also has winding one about that point.

But gamma_ij is precisely the closed loop made from the two ordered
two-color boundary paths. Their interiors do not cross. Its winding
is one exactly in their projected weak lens and zero outside (shared
boundary pieces cancel). In particular h_ij(x) is in that lens.
Each closed projected lens is contained in the rectangle
[0,N_i] times [0,N_j]. Thus winding one first forces all coordinates
of h into the available rank box. Applying this at the initial and
final inner vertices gives (R), including every absent inner color.
Only after this range check do we apply A1 to all six projected lenses
and conclude boundary ideality. The corrected A2 therefore applies.

For an outer starting height z0, set x_prime=x-Vz0 and
h_prime=h-z0. The affine offset becomes

    c_prime=c-(I-JV)z0 in ker V.

Both affine error bounds and the physical distance condition are
unchanged. The same argument gives the relative rank-box and ideal
conditions required by translated A2.

The rank offsets in a need not be zero. They are checked by these
six inequalities at once. Corners are included in the one closed
loop rather than patched separately. No assumption that the two
profiles can be convexly interpolated is made, and no admissible
interpolated gradient is needed. The actual annulus is produced by
positive tile shellings in A2, so its physical map has degree one.

For E0=O_J(1), E1=epsilon L, a physical collar of width
O_J(epsilon L+1) is sufficient. Its constant depends on sigma(J)^-1.
There is no uniform conclusion when a row minor tends to zero.

## A4. Explicit rational flat frames with exact phases and corner counts

Now assume J is rational and strictly positive as above. Its nonzero
row vectors have strictly increasing directions in an angle interval
of width less than pi: take the first row as angle0, and the positive
pair minors put all the others strictly between0 and pi in their
given order. Therefore the open cone

    C={u in R²:J_i u>0 for every i}

is nonempty. Choose two independent rational u,v in C with
det(u,v)>0 and multiply by a common integer so that

    a=Ju, b=Jv are positive integer vectors.

Then u=Va, v=Vb, and

    a_i b_j-a_j b_i=Delta_ij det(u,v)>0 for i<j.       (4)

Choose one phase vector theta with0<theta_i<1, avoiding simultaneous
crossings along the two finite segments0--a and0--b. Only finitely
many rational hyperplanes are forbidden, so a rational phase can be
chosen. Let U be the word recording, in order, the events
t a_i=k+theta_i along0<=t<=1, and define Vword similarly from b.
Their contents are exactly a and b. Use the name Vword to distinguish
this word from the physical projection matrix V.

**Claim A4.** For all integers m,n>=1,

    U^m Vword^n <= Vword^n U^m.                       (5)

Their lifted boundary stays within a constant C_J of the affine lift
Jx, and their physical boundary stays a bounded distance from the
parallelogram with sides m*u,n*v. When m=n=L is large, deleting only
bounded initial and final lobes gives a Jordan main lens whose
boundary remains within the same bounded band. This is a fixed
canonical flat outer boundary family.

To prove(5), restrict to any colors i<j. The two event sequences
are digital traces of the two boundary paths of the parallelogram
with side vectors m(a_i,a_j), n(b_i,b_j), in the coordinate plane.
Both side vectors are positive and their determinant is positive
by(4). At the k-th vertical threshold i, the lower path U^m Vword^n
has crossed no more horizontal j thresholds than the upper path
Vword^n U^m. Thus b_lower(k)<=b_upper(k) for every i rank. These
are exactly the pairwise inversion inequalities. All six pairs prove(5).
Integer endpoint coordinates preserve the same phases on translated
segments, so the words really are the displayed powers, not merely
words of matching content.

Both fixed words contain every color. Their powers and single junctions
therefore have a bounded color gap G_J, independent of L (for example
2*(length U+length Vword) suffices). Any use of the earlier bounded-gap
conversion is legitimate with this J-dependent bound. The proof of
A3 instead uses closed pair projections directly and needs no such
conversion.

On each segment the event-prefix count vector differs coordinatewise
from its straight height point by at most1. Its physical image differs
from the straight physical point by a bounded amount depending on the
fixed v_i. Moreover (I-JV)a=(I-JV)b=0, so the boundary height error
H-JVH=(I-JV)(H-straight_height) is uniformly bounded, independent
of m,n. The same holds on every interpolated edge. This proves the
flatness estimates without a global multigrid-extension assumption.

For m=n=L the two straight physical boundary chains have a vertical
gap bounded below by a positive constant times
min(x,X_end-x,L), with constants depending only on u,v. The bounded
digital errors therefore allow common vertices only within bounded
distance of the two extreme corners. Comparable words have the same
height at a common physical vertex: along an increasing-swap chain,
a swap across that prefix strictly increases its y coordinate, whereas
every other swap leaves its prefix height unchanged. Equal y values
therefore imply no change of prefix height.

Choose the last common vertex near the initial corner and the first
common vertex near the final corner. Between these vertices the two
paths are disjoint except at their ends, and remain comparable after
restricting labels. They bound the asserted Jordan lens. Discarded
lobes are confined to two bounded physical boxes, have bounded tile
count and affect logarithmic tiling counts by only O_J(1).

**Affine-offset and phase alignment.** The preceding family starts
at height0. For a desired physical corner x0 and affine offset c in
ker V, choose an integer vector z nearest Jx0+c coordinatewise.
Then Vz is within O_V(1) of x0 and

    (I-JV)z is within O_J(1) of c.

Translate the frame physically by Vz and its heights by z. Its boundary
now approximates Jx+c within a bounded error, using the same fixed
phase words. Thus arbitrary macroscopic offsets do not require a
permutation of ranks or a new phase continuum: integer rounding fixes
the ranks, and only a bounded geometric corner adjustment is needed.
The A3 collar absorbs that bounded adjustment. For inner cores of a
fixed boundary fiber, all these choices are fixed before varying the core.

## A5. A genuine local entropy limit for these exact boundary frames

Let C_L be the number of tilings of the whole weak lens bounded by
U^L Vword^L and Vword^L U^L, with its prescribed lifted boundary.
The bounded extra end lobes are included. C_L>=1 by a swap chain.
Its support has diameter O_J(L), and the finite integer prototile
alphabet bounds C_L<=2^(K_J L²). This bound follows by recording
which of6 tile types occurs at each possible integer tile origin in
an O_J(L)-box; no free-boundary entropy theorem is used.

**Claim A5.** The limit

    lim_(L->infinity) L^-2 log2 C_L
       =sup_(l>=1) l^-2 log2 C_l                      (6)

exists. The Jordan main-lens counts have the same limit.

Fix l and write L=k*l+r,0<=r<l. Regard U^L as k blocks U^l plus
one U^r remainder, and similarly for Vword^L. Bubble the U blocks
past the Vword blocks. A crossing of a length-l block of each type
is exactly a translated weak lens of size l, by(5). Every mixed-size
remainder crossing is also a comparable-word lens and admits a fixed
swap filling. Each successive block replacement raises the current
physical path; its added region has disjoint interior from all earlier
regions. Consequently the k² size-l regions are actual disjoint
geometric patches with exactly matching translated boundary words.
Independent choices of their C_l fillings recover by restriction, so

    C_L >= C_l^(floor(L/l)²).                         (7)

There is no assumption that arbitrary zonogons pack at density one.
These regions are the explicit bands of a fixed block-swap shelling.
The exact seam heights are the sums of the a,b block counts. Shared
same-color ranks are therefore already matched, and no crossing-order
factor is suppressed.

Dividing(7) by L² in the logarithm and sending L to infinity gives
liminf>=l^-2 log2 C_l for every fixed l. Taking the supremum, and
using the reverse limsup bound by that same supremum, proves(6).
The removed bounded end lobes multiply C_L by a uniformly bounded
factor, so their logarithmic effect is O_J(1) and the main-lens
entropy limit is identical.

A2--A4 therefore give a conditional transfer with all frame data
retained. Fix a rational J with all ordered minors strictly positive,
one common affine offset c, one phase choice, and a receiving canonical
integer frame. The inner patches must be actual Jordan two-path lenses
with comparable boundary words and their assigned integer lifts. They
must be physically contained in that frame and satisfy the common-affine
error bounds and quantitative buffer inequality in A3. These hypotheses
give the rank box and ideals before the closed annulus is constructed.
If A2 is used directly, its rank box and ideal hypotheses must instead
be supplied explicitly.

For a fixed inner boundary this transfer is injective. For varying
boundary codes of O(L) letters and O(L) relative integer offsets it
loses at most O(L) bits. A5 gives an actual all-scale local boundary
entropy limit for the receiving family. This does not itself construct
a thin surrounding canonical frame for an arbitrarily shaped lens or
bound its relative area overhead. No independent corner offset, free
phase change, or uniform zero-minor limit is included.

## An exact obstruction to omitting the rank box

The rank-box condition in A2 is necessary even for an inner color
that does not occur. This finite example, supplied by the first fresh
whole reviewer, diagnoses the literal v1 statement. Take outer content
N=(10,10,10,10), with ascending color blocks for p0 and descending
color blocks for q0. The physical lens is the convex zonogon Z_10;
P0 consists of the four independent same-color chains.

Take the single inner type-13 tile, with lower word 13 and upper
word 31, assigned start and end heights

    a=(7,-2,7,4),  b=(8,-2,8,4).

Its physical vertices are (16,24),(17,24),(17,26),(18,26). The
whole tile is strictly inside Z_10: it also has coefficient representatives
(4,4,4,4)+alpha e1+beta e3 with 0<=alpha,beta<=1, all in the
interior of the coefficient cube [0,10]^4. Surjectivity of V sends
small open coefficient neighborhoods to physical neighborhoods, so
compactness gives positive distance to the zonogon boundary.

Every set given by the literal formula for I at these four heights
is an ideal of P0, since it merely truncates the negative color-2
coordinate to an empty prefix. Active color-1 and color-3 ranks are
valid rank 8; the absent color-2 interval is empty and imposes no
lower bound by itself. Nevertheless no full outer tiling has color-2
height -2 relative to its prescribed boundary base. The proposed entry
seam from the truncated ideal would end at height (7,0,7,4), physically
(18,26), instead of the assigned start (16,24). This is an actual
failed rank assignment, not a failure of the corrected shelling proof.
Condition (R) excludes it. A3 already excludes it by its winding test.

## An exact obstruction to omitting the phase/buffer condition

Physical nesting and an O(epsilon L) height error are not enough if
the collar is only O(1) thick. Let k=(1,-2,1,0), so Vk=0. In a large
canonical frame of A4, fix a sufficiently large integer s depending
only on J and place an inner lens of size L-2s translated by s(a+b).
The constant s makes the inner main lens strictly nested despite the
bounded digital boundary errors. It has a bounded-width surrounding
band; all its tilings have a valid lift h.
Replace the assigned inner lift by h+M*k, where M grows but M=o(L).
This is still a lift of exactly the same physical patch, and its
deviation from the same affine slope is O_J(M+1).

At its initial vertex the second height coordinate relative to the
outer starting rank is s(a_2+b_2)+O_J(1)-2M, negative for large M.
The bounded term is just the main-lens corner trimming. Every outer
lifted path uses ranks0,...,N_2, so this boundary assignment cannot
extend to the prescribed outer lifted frame. In ideal language it
fails even the rank-range condition. Thus this is a precise obstruction
for assigned boundary/color ranks, not a counterexample to geometric
unlabelled patch insertion after arbitrary relabeling. It does not
refute the A3 repaired theorem: (3) requires a collar of order M here.
The same issue explains why height offsets and phase data must be
checked globally rather than ignored at the four corners.

## Remaining interfaces; no proof of H

The statements above start with an actual inner two-path lens. To use
them for every nearly affine cut window one must still construct such
a lens after discarding only a thin boundary band, and account for
the discarded information. The coordinator's separate directed-geodesic
results and cutting candidate may supply parts of that interface, but
neither is a premise of this repair.
The original A1--A5 construction preceded the fresh annulus audits;
this v1.1 author copy uses their complete frozen reports to repair
AR1-01 and to state ANN2-N1/N2 explicitly. Neither initial report was
altered and both targeted re-audits remain required.

For a thin discarded band of area delta L², a fixed finite-alphabet
encoding would cost O(delta L²+L) bits, once the required controlled
cutting operation is proved. The statement here does not assert that
operation for an arbitrary window. Non-strict slopes are another
unresolved interface: sigma(J) tends to zero, and zero rows or parallel
row groups cannot be covered by pretending this constant is uniform.
Global profile recovery with the original zonogon boundary remains
unproved. Convex averaging of profiles is not used as a repair.

The local limit A5 is deliberately distinguished from hypothesis(H)
for the FULL balanced zonogon count. It is a receiving entropy family,
not a substitution for the full count. A complete implication to(H)
still needs the cutting/stratified extension and recovery argument,
followed by two fresh whole audits. Every new assertion in this note
remains candidate-unverified pending those audits.
