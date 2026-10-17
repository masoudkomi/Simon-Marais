# Independent whole initial audit: orientation charts R1

2026-10-17 UTC. Reviewer `review_2017_coarsening_r1`; requested
gpt-6.1-sol/max, effective readback unavailable. This initial report,
issue ledger and source/integrity records are frozen before any peer
orientation-chart conclusion is read. No candidate is edited here.

Target: `coordinator-orientation-charts-candidate-v1.md`, SHA256
a64eea09f6cab7ba86f158cc685ab20d35742c4d8dbfc3dfb60260a3b7ada552;
freeze SHA256
338a50e977061e29a379cf311273d5d8edada01ebf86891aa80d4afa74cd1da0.
I did not construct OC1-OC3. My earlier fixed-D/rank-mesh work named
an orientation obligation, but did not supply this proof. The accepted
fixed-D background is disclosed as prior work and checked in its exact
scope; it does not make this review an independent audit of that older
packet. I reconstruct every substantive OC inference below.

**Disposition:** no substantive defect found within the stated finite
chart, full-tiling and tangent-matrix scope. I recommend scoped acceptance
after the other fresh whole audit and coordinator reconciliation. This
is not promotion, a global-chart theorem, entropy recovery, H, PR or a
solution of the official limits.

## 1. Official domain and exact inputs

The official2017 Paper B, page2 B4, was directly checked. It asks for
both limiting extremal rates of n^-2 log2 C(n), n>=2. All of this
B4 is open scope. The candidate proves only local structural statements
that could support a later rate argument; it does not claim to evaluate
either rate. Counts remain marked in a fixed polygon. No symmetry
quotient, reduced-word count or arbitrary packing is substituted.

The precise algebraic input is D>=2, V columns v_i=(1,i-1),
VJ=I2 and every ordered row minor Delta_ij>=0. VJ=I implies rankJ=2.
No strict lower bound on every row/minor is assumed. Zero rows and
antiparallel endpoint rows must therefore be included; rationality is
not required. The actual tiling input of OC2 is a full marked balanced
zonogon with content p in every color. For positive p this is a genuine
two-dimensional disk. If an empty p=0 convention is allowed, the
tiling/lift bijection is the trivial one-point case; degree arguments
are used only for the genuine disk.

## 2. OC1: weak angles and the finite cyclic cut

Let f be the first nonzero row. Rotate the axes for this angle argument
so its angle is0. For each later nonzero row the determinant condition
with row f puts its angle uniquely in[0,pi]. A pair of such angles
theta_i>theta_j has negative sine of the difference, unless it is
exactly(pi,0). Thus any angular inversion is an antiparallel endpoint
inversion.

Suppose such an inverted pair occurs. A row of angle strictly between0
and pi cannot occur before, between or after that pair: in each case
its ordered determinant with one of the endpoint rows is negative.
All nonzero rows would therefore point at0 or pi, giving rank1,
contrary to VJ=I. So nonzero angles are weakly increasing in[0,pi].
This also checks the possible endpoint degeneracy rather than silently
assuming the angles are already in an open semicircle.

Rank2 supplies a positive angular gap between successive nonzero rows.
Let their original indices be a<k; any indices between them have zero
rows. In particular2<=k<=D. Cyclically list k,...,D,1,...,k-1
and negate the prefix that moved to the end. The nonzero angles become

    theta_k,...,theta_last, pi, ...,theta_a+pi.

The first shifted angle is theta_f+pi=pi, and theta_last<=pi,
so they stay weakly increasing. Their span is
pi-(theta_k-theta_a)<pi. They lie inside an open half-plane.
Any two ordered nonzero rows consequently have angular difference
in[0,pi), so all ordered minors stay nonnegative and zero minor means
positive parallelism. Equal directions are consecutive among nonzero
rows. Original opposite endpoint directions, if present, merge at
the cyclic junction, rather than leave a hidden antiparallel pair.
Interposed zero rows do not affect this order and need no positivity.

There are exactly the possible indices k=2,...,D, a finite D-1 family.
An open half-plane of row covectors has a nonempty open strict positive
dual cone. Choose two independent physical vectors in that cone; all
nonzero chart rows evaluate positively on both. Here these are the
signed/reordered rows, as the text's phrase “in the chosen chart”
specifies. The positivity margin can tend to zero; the candidate
correctly asserts no uniform nonzero-row or angular-gap bound.

## 3. OC2: actual geometry, labels, offsets and ranks

Write b=p sum_(i<k)v_i and let S be the diagonal signs, followed
by the stated cyclic permutation. Before permutation the new height
is a'=S a+p sigma, where sigma_i=1 exactly for flipped colors.
The physical coordinate is x'=x-b and V'=V S. Direct substitution
gives V'a'=Va-b=x', including the constant on every flipped color.

The interval identity[-pv_i,0]=[0,pv_i]-pv_i shows that the new
zonogon is the original one translated by-b. Every tile is exactly
the old tile translated; its lift now uses the opposite orientation
on a flipped color. The inverse restores x and a at every point,
so this is an actual marked tiling bijection, not a map only of slope
matrices or of local ports. Complete boundary words and fine labels
are recoverable.

In particular an old rank r level a_i=r-1/2 becomes

    p-a_i=(p+1-r)-1/2.

Thus a flipped color's rank is exactly p+1-r; endpoint order and both
occurrences reverse together. There is no independent choice of rank
matching. The common balanced content is what permits the same p
in these formulas.

The new physical angles are phi_k,...,phi_D,phi_1+pi,...,
phi_(k-1)+pi, with phi_i=arctan(i-1). They are strictly increasing
and span pi-(phi_k-phi_(k-1))<pi. Therefore every reordered
physical pair determinant is positive. This assertion concerns the
original strictly ordered physical vectors, independently of zero
rows of J. Signed/permuted J' satisfies V'J'=VJ=I. The tangent
row order is exactly OC1's, so its nonzero parallel groups are positive.

The full polygon's boundary has its usual ascending/reversed color
order when rooted at the new initial corner. It has not been treated
as the old boundary word rooted at the old vertex. Nor does this
operation make one chart valid at every point of an arbitrary profile.

For completeness, if originally a(x)=Jx+c+e(x), the same source
translation gives a single c'=S(c+Jb)+p sigma and error S e,
then the same index permutation. If Vc=0 then V'c'=0. Thus the
reorientation also retains one common offset rather than reset offsets
at different sides. OC3 starts from exactly this type of common data.

## 4. OC3: positive full deformation and uniform bilipschitz bounds

For the new ordered columns let W_i=(1,i-1). The canonical lift maps
the source to y=W a'. On a source tile ij this is the affine map
with derivative W_ij(V'_ij)^-1, with strictly positive determinant.
The source full boundary maps once, with its consecutive color order,
around the convex target zonogon.

At a regular target point outside all image edges, the winding degree
is1 inside that polygon and0 outside. Every face preimage has positive
sign. Hence a regular interior point has exactly one preimage and an
exterior point none. This excludes interior tile overlap or missing
open regions. At a vertex the incident source edge rays occur once
in their cyclic order among the signed physical directions; replacement
preserves that strict cyclic order. Their fan therefore has local
winding1, not a hidden multiple winding. The same check at edges gives
local homeomorphisms. Boundary injectivity follows from the convex
cyclic polygon. A nonunique remaining preimage would force two nearby
regular preimages. Compactness now gives a full homeomorphism.

The map preserves face-to-face incidence and colors. Replacing W by
V' reverses it on every tile. Thus it preserves the exact full tiling
count and complete boundary data. It does not assert that a partial
physical window becomes a canonical parallelogram or zonogon frame.

There are finitely many pairs ij. Both W_ij(V'_ij)^-1 and its
inverse V'_ij(W_ij)^-1 have norms bounded by a constant for fixed
D,cut. Source and target full domains are convex. Restrict a segment
in either to its finitely many tile pieces and integrate those derivative
bounds; edge coincidences follow by continuity. This gives global
Lipschitz bounds in both directions. They do not depend on p or the
tiling. A maximum over the finite cuts gives constants depending only
on D if desired.

## 5. Transformed slope, affine error and nondegeneracy

Set A=WJ'. By Cauchy--Binet,

    det A=sum_(i<j) det(w_i,w_j) Delta'_ij>0.

All coefficients are positive, all Delta'_ij nonnegative, and rankJ'=2
gives at least one positive minor. Therefore J*=J'A^-1 is well
defined and WJ*=I. Right multiplication gives each ordered minor
Delta*_ij=Delta'_ij/det A. Zero rows, zero minors and positive
parallelism are preserved exactly. The strict positive dual cone is
also preserved: if J'_i u>0, then J*_i(Au)>0. No argument depends
on Euclidean angles being preserved by a nonorthogonal map.

Given a'=J'x'+c'+e, direct substitution yields
y=Ax'+Wc'+We. Consequently

    a'-[J*(y-Wc')+c']=(I-J*W)e.

This is an exact algebraic identity at each point of the actual image,
with c*=c'-J*Wc' and Wc*=0. The error bound is its operator norm
times E. The actual source constraint also implies V'e=0, but the
identity does not need a stronger independently chosen error gauge.
There is only one c' and one target c*, so corners, ranks and ports
are not assigned unrelated phases. This pointwise statement assumes
no derivative chain rule for a possibly oscillating approximate profile.

Finally1=det(V'J')=sum det(v'_i,v'_j)Delta'_ij. The summands
are nonnegative weights summing to1. Thus det A is their weighted
average of the fixed positive ratios

    det(w_i,w_j)/det(v'_i,v'_j).

The minimum and maximum of those ratios are valid bounds, including
when many row minors vanish. If||J||<=G, signing/permutation preserves
the Euclidean operator bound, so ||A|| is bounded. For a2-by2 matrix,
the adjugate formula and the positive determinant lower bound control
||A^-1||. They then control J* and I-J*W in terms of D,G,
uniformly over the finite cuts. This is determinant nondegeneracy,
not a uniform positive lower bound on each row or each minor.

## 6. D4 type conclusion and limits

Rank2 gives at least two distinct nonzero positive directions, and
there are at most four rows. Four groups means four nonzero singleton
rows; their ordered angles differ strictly by less than pi, so every
minor is positive. Three groups allow exactly three or four nonzero
rows. The former gives one zero and three singleton groups; the
latter gives one adjacent positive merged pair and two singletons.
Two groups can have different multiplicities and zero rows. Deleting
zero labels only for that grouping description must retain those
original labels for later geometry, as stated.

This is a type classification, not an entropy statement for any of
the types. In particular the deformation identity gives closeness on
the actual image only. It supplies no canonical window shape, seam
matching, rare-tile count, common chart across macro regions, PR, H
or rate value. Those explicit exclusions are material and survive this
audit. No hypothesis of a new analytic literature theorem is imported.

No mathematical enumeration, CAS or finite experiment was used. All
calculations above are exact. Administrative code only verifies frozen
files and serializes this report. The complete ledger/source record
is frozen before any peer finding is received. The coordinator retains
promotion authority after the second fresh whole reconstruction.
