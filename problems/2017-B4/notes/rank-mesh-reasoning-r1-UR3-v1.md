# A proposed uniform three-direction recovery for globally extendable disks

2026-10-17 UTC. **Candidate proof - unverified.** Constructor
`review_2017_coarsening_r1`. This is a proposed corollary of published
Cohn--Kenyon--Propp, with a new explicit boundary-class reduction and
compactness/gluing argument. It is not a new variational-principle method
or a direct statement of their theorem. Two fresh independent whole audits
must check the imported quantifiers and every construction below. No
MacMahon balanced-hexagon estimate is used. No H or full2017 solution.

## 1. The precise class and target

Use standard unit-lozenge directions, three vectors in cyclic order in
one open half-plane. Fix C0. A member B of GE3_C0(r) is a Jordan
tile disk with a complete prescribed colored boundary and scalar height,
perimeter at most C0 r, which embeds with a fixed exterior tiling in a
full three-direction zonogon having at most C0 r curves in each color.
The scalar height is normalized at one fixed vertex. Translations and
one constant height shift are immaterial. Every filling of B glues to
the same exterior, not just a selected subset of its fillings.

The companion rank-mesh candidate explains why its actual coarse disks
have this property: remove inactive full curves, then deform the three
remaining ordered directions to standard lozenges. The globally extendable
condition is retained explicitly. Diameter and perimeter alone do not
supply it for an arbitrary ragged boundary.

Let Z(B) be its exact tiling count, and let M B denote integer dilation
with each boundary edge replaced by M unit edges of the same color.
Dilating one reference filling and filling each enlarged lozenge by its
uniform M-by-M array shows Z(M B)>=1. Define

    Delta(B)=max(0, log2 Z(B)
                   -liminf_(M->infinity) M^-2 log2 Z(M B)).

**Proposed UR3-GE.** For each fixed C0 there is eta_C0(r)->0 such that

    Delta(B)<=eta_C0(r) r^2 for every B in GE3_C0(r).       (U1)

This includes all complete paired boundaries in this class, not only
balanced hexagons or an affine boundary. No exact inequality
Z(M B)>=Z(B)^(M^2) is asserted. No explicit convergence rate is obtained.

## 2. Primary theorem import, with its boundary hypotheses

The source is [Cohn--Kenyon--Propp, arXiv:math/0008220v3](https://arxiv.org/pdf/math/0008220v3),
especially Sections1.6 and4, Theorem4.3 and Corollary4.2. Its limiting
domain is a fixed piecewise smooth simple closed curve, without cusps;
lattice regions are simply connected, approximate from within, and
their normalized boundary heights approximate admissible boundary data.
The theorem counts height neighborhoods; compactness yields total
entropy. Printed page13 explicitly extends all results to unit lozenges.
Only fixed triangular limiting domains are imported here. Source entropy
units must be converted consistently to log2 per physical area; no
numerical value is used. The varying ragged B are not substituted as
a compact family of smooth limiting domains.

Write P for the compact triangle of admissible scalar-height gradients,
and sigma3 for the continuous concave lozenge entropy density, in those
consistent units. For an affine admissible height p on a fixed triangle
T, the entropy integral is area(T)*sigma3(grad p). It is maximal
among heights with boundary p: concavity and the boundary determination
of the average gradient give Jensen's inequality. This observation also
covers slopes on the boundary of P, where the density vanishes.

The local consequence needed below is spelled out to expose the exact
uniformity obligation. It is derived next rather than silently read into
a slogan about a thermodynamic limit.

## 3. LC3: a fixed-triangle comparison

Let T be a unit equilateral triangle, in either lattice orientation.
For every kappa>0 there exist tau>0 and n0, uniformly over admissible
affine p with its constant normalized in a bounded interval, such that:

* Q is a tileable Jordan lattice disk contained in nT and containing
  the inset of nT at distance tau n from its sides;
* its complete normalized boundary height is within tau of p in the
  lifted boundary approximation metric;
* all its fillings have a common fixed-exterior extension to admissible
  heights on nT, whose normalized boundary heights are within tau of p;
* n>=n0.

Then

    |n^-2 log2 Z(Q)-area(T)*sigma3(grad p)|<=kappa.        (LC3)

The inset condition is deliberately stronger than a bare Hausdorff
distance between two boundary sets. It supplies the O(tau) missing-area
bound needed in the theorem's triangular proof, including nonconvex Q.
The fixed-exterior condition will come from a reference tiling, so this
claim does not assume arbitrary height data extend across an annulus.

For one fixed p, the lower bound follows by applying the quantitative
height-neighborhood theorem to p itself, with Q approximating T from
within. Boundary distance plus the fixed affine error gives exactly the
lifted approximation hypothesis. Constants can be multiplied by fixed
Lipschitz bounds without changing the conclusion.

The source's refined from-within metric also refers to restrictions of
every limiting admissible height. This is satisfied here, not omitted:
every h in AH(T,p) has a uniform global Lipschitz bound on the convex
triangle. Every point of the inner boundary of Q is O(tau) from the
outer triangle boundary. Comparing h and p there via that outer boundary
gives |h-p|=O(tau), uniformly over h. The actual boundary data of Q
are therefore within O(tau) of every such restriction. The stronger
inset condition also bounds the missing area by O(tau).

For the upper bound, extend each Q height using the fixed exterior to
T and normalize. These functions have one uniform Lipschitz bound and
bounded values. As tau tends to zero, every subsequential limit is an
admissible height on T with boundary p: the gradient constraint is closed
and convex, and the boundary values converge. Thus for small tau their
extensions lie near the compact set AH(T,p). For each h in that set,
the quantitative source theorem gives an upper bound on the count in
a sufficiently small neighborhood of h by its entropy integral plus an
arbitrarily small kappa error, for sufficiently large n. These open
neighborhoods cover AH(T,p); take a finite subcover. The exterior choice
does not identify distinct Q fillings. The sum of finitely many such
count bounds has normalized logarithm at most the largest entropy plus
o(1). Jensen bounds that largest entropy by the affine value. This
proves the upper bound.

The sufficiently-large-n bound here is uniform over Q meeting the chosen
approximation tolerance for a fixed h. This is the quantified reading
of Theorem4.3 used: its proof first chooses a finite mesh for the fixed
target h and then uses the local triangular estimate; Q enters only
through approximation tolerance and the excluded boundary area. A review
must verify this reading, rather than replace it by a pointwise theorem
for one predetermined Q sequence. A finite subcover makes the n threshold
uniform for the fixed p.

Finally take a finite cover of the compact affine-parameter set. At each
p0, shrink its comparison tolerance so nearby p have nearby sigma3 values
by continuity, and their boundary errors relative to p0 still fit the
chosen tolerance. Finitely many such neighborhoods give a single tau and
n0 for all p. This includes frozen slopes; it uses continuity at those
slopes and makes no positive-slope lower bound uniform by division.

This is the only analytic source interface. If its precise theorem
quantifiers or stated lozenge extension fail the audit, (U1) is to be
retained only as conditional on LC3; no general entropy theorem can be
substituted without a new complete source check.

## 4. Why scalar profiles have the compactness needed here

On a lozenge, a scalar height has one of three fixed gradients. On a
convex full zonogon its continuous extension is therefore globally
G-Lipschitz, for one absolute G: integrate along the straight segment.
Every B filling glues to the fixed small-zonogon exterior, so this applies
to every filling, even when B itself has narrow necks. The full zonogon
has diameter O_C0(r), and its height range is O_C0(r).

After translating and dividing positions and heights by r, extend these
scalar functions from their convex ambient zonogons to a common fixed
box by the elementary Lipschitz extension formula. The extension outside
the ambient zonogon need not be an admissible lozenge profile; only its
uniform Lipschitz bound and bounded range are used there. On any open
triangle eventually lying in B it is admissible. The gradient constraint
P survives uniform limits on such a triangle because P is closed and
convex.

This family has a finite sup-norm gamma cover with
log2 N(gamma)=O_C0(gamma^-2 log(2/gamma)). To see the bound, use a
gamma-scale square mesh of the common box and quantize the function
values to a constant multiple of gamma; Lipschitz continuity controls
the error between mesh vertices. It is also sequentially compact.
No convergence of the boundaries B/r to a Jordan curve is needed.

## 5. Actual triangular cores and their recorded cuts

Fix a triangular lattice mesh with side ell, inside the O(r) box.
Its total internal line length is O_C0(r^2/ell+r). For one reference
tiling, record every lozenge whose interior crosses a mesh line. There
are O_C0(r^2/ell+r) such tiles, since their possible positions lie
in a bounded-width tube around those fixed lines. A finite-alphabet
bitmask of those positions records their exact geometry.

Also record scalar heights at all lattice vertices on the cut bands
and mesh lines. There are O_C0(r^2/ell+r) such vertices and each has
O(r) possible values after the fixed normalization. The additional
code length is O_C0((r^2/ell+r) log(r+2)). This intentionally generous
bound is sufficient: ell is a fixed positive fraction of r before r
goes to infinity, so the code is o(r^2). No coordinate or phase data
are left unconditioned.

For a closed mesh triangle T_ell lying wholly inside B, remove its
recorded crossing tiles and consider all tiles contained in it. Ignore
contacts where a mesh line merely follows a tile edge; no tile is
removed just for such a contact. Split its residual edge graph into
biconnected tile blocks as in RM1. There is one block Q containing
the inset of T_ell at a fixed distance c1 from its sides. Indeed every
tile meeting that inset is wholly inside the triangle and not removed;
generic paths inside the convex inset connect its tiles across edges.
No cut tile can make a hole, since its interior connects across the
triangle's boundary to the exterior while avoiding every retained tile.
The same plane-graph argument gives a Jordan Q.

The omitted parts lie in a fixed-width boundary strip. Thus

    T_(ell,-c1) subset Q subset T_ell,
    area(T_ell minus Q)=O(ell+1),
    perimeter(Q)=O(ell+1),
    distance_Hausdorff(boundaries Q,T_ell)=O(1).           (U2)

The constants are independent of the reference tiling. Bounds on the
strip's lattice sites give the perimeter bound even for a jagged Q.
All other blocks are in that strip and may be discarded. The cut code
determines the region Q and its complete boundary heights, so the same
Q is available for every member of the conditioned family. Every filling
of Q extends to admissible heights on T_ell by the fixed reference
exterior. Integer dilation of the reference gives the identical extension
property for M Q in M T_ell.

## 6. Compactness contradiction proving uniform recovery

Suppose (U1) fails for a fixed C0. Then some a>0 and r_j->infinity
have disks B_j with Delta(B_j)>=a r_j^2. Let gamma_j=1/log(r_j+2).
Partition their tilings by the compact profile cover of Section4. Its
logarithmic size is o(r_j^2). Choose a largest fiber, and one actual
extended normalized height h_j in it. All heights in the fiber differ
from h_j by O(gamma_j). Pass to a subsequence on which h_j converges
uniformly to a Lipschitz h in the fixed box. Therefore every height
in the chosen fiber converges uniformly to the same h.

Fix kappa>0 and let tau,n0 be the uniform LC3 constants. For a small
epsilon>0, differentiability almost everywhere and the standard finite-mesh
approximation of a Lipschitz function give a triangular mesh of normalized
side lambda, with lambda<=epsilon, on which all but an epsilon fraction
of the box's area lies in triangles where h is within tau lambda/10
of an affine function. Choose lambda sufficiently small for this fixed
h,tau,epsilon. This step concerns a single limiting scalar function;
it assumes no uniform differentiability modulus for the whole class.

Take ell_j=floor(lambda r_j), and use its lattice mesh. Mesh rounding
changes normalized positions by O(1/r_j). There are only O_C0(lambda^-2)
triangles. Pass to a further subsequence so the list lying wholly inside
B_j stabilizes. On any retained triangle h is an admissible limit, so
the affine approximation may be chosen with gradient in P. For large j,
all heights of the fiber, and its selected reference, are within
tau ell_j/3 of the corresponding plane on that triangle.

Discard triangles meeting the boundary of B_j, and triangles failing the
affine test. The first type lies in an O(ell_j)-tube about a curve of
length at most C0 r_j; its area is O_C0(lambda r_j^2+ell_j^2).
The second type costs O_C0(epsilon r_j^2). A further fixed-width
mesh strip costs O_C0(r_j/lambda+1). These estimates allow thin necks,
pinches in a limiting boundary and disconnected limiting interiors.

Within the chosen profile fiber, condition on the cut geometry and
heights of Section5, taking a largest subfiber. Its additional logarithmic
loss is o(r_j^2), at fixed lambda. Let T0_j be one filling in that
subfiber. In each retained triangle form the actual Jordan core Q_j,t
from T0_j. Every subfiber filling restricts to a filling of those fixed
cores plus a filling of the discarded region. The latter has
O_C0((epsilon+lambda)r_j^2+r_j/lambda+1) lozenges.
A regular lozenge region with A lozenges has at most3^A fillings:
each up-pointing unit triangle has at most three matching neighbors.
Consequently

    log2 Z(B_j) <= sum_t log2 Z(Q_j,t)
                  + O_C0((epsilon+lambda)r_j^2)
                  + o_j(r_j^2).                         (U3)

The cores and their boundary heights satisfy LC3 for large j: (U2)
gives the inset and lifted geometric error, the fiber gives near-planarity,
and the fixed reference supplies the extension. Here n=ell_j. Let
E_j,t be the planar entropy density times the area of that mesh triangle.
Then

    log2 Z(Q_j,t)<=E_j,t+kappa ell_j^2.                   (U4)

For each fixed j, dilate T0_j to M B_j. Keep its exterior to all
M Q_j,t fixed, and insert independently arbitrary fillings in those
disjoint dilated cores. Their complete colored boundaries and heights
match exactly; restriction recovers every choice. Hence

    Z(M B_j)>=product_t Z(M Q_j,t).

Applying the lower LC3 estimate with n=M ell_j gives, for all sufficiently
large M and for every core in this finite list,

    M^-2 log2 Z(M Q_j,t)>=E_j,t-kappa ell_j^2.             (U5)

No uniformity in M across infinitely many j is needed: M tends to
infinity with j fixed in the definition of Delta. Combining (U3)--(U5)
and summing ell_j^2 over O(lambda^-2) triangles yields

    Delta(B_j)/r_j^2 <= O_C0(kappa+epsilon+lambda)+o_j(1).

Choose kappa and epsilon sufficiently small relative to a, with
lambda<=epsilon as above, then let j grow. This contradicts the assumed
positive deficit. The supremum of those normalized deficits therefore
tends to zero, proving the proposed uniform eta_C0(r). All orders of
limits are explicit: compactness in r, a fixed mesh for the limiting
height, r sufficiently large, and only then M->infinity at each fixed r.

## 7. What this does and does not settle

The proposed proof addresses the exact lower-direction class produced
by the clean rank disks, including nonaffine and ragged complete boundaries.
The elementary skeleton and dilation gluing preserve those boundaries.
It does not infer uniformity just because there are finitely many
boundaries for each fixed r; that observation alone would say nothing
about eta(r)->0.

The analytic audit target is LC3's quantitative import and its upper
compact-cover step, including the explicit lozenge adaptation and entropy
normalization. The geometric targets are the biconnected triangle core,
the code fixing complete boundary data, admissible affine slopes on
retained triangles, and the ability to extend every filling using the
small-zonogon exterior. If any fails, the precise conditional theorem
and remaining gap must be retained rather than promoting (U1).

No result for D>=4 general full boundary entropy is imported from this
three-direction argument. The original orientation, rare-flux, macro-window,
stratum and global-profile assembly obligations remain as recorded in the
companion candidate. The official full 2017 limits are not computed.
