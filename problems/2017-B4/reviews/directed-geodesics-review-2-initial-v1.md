# Blind whole audit of DG1 and DG2

2026-10-17 UTC. Reviewer: `review_2021_reasoning_j15_r2`. This is a
fresh independent nonconstructor audit. I did not construct DG1/DG2 or
contribute their disk adaptation, and I read no peer DG review or findings
before this report, issue ledger and source record were frozen. Requested
gpt-6.1-sol/max; effective-setting readback is unavailable. No enumeration,
CAS or mathematical computation was used.

## Recommendation and boundary of the conclusion

I find no unresolved substantive objection to DG1 or the precise
conditional DG2, including their stated buffer and positive-margin
restrictions. The disk-to-plane dual graph identification, curve signs
and zero-coordinate cases check out. The geometric scale statement is
valid with fixed affine-error constants, fixed kappa,K and a sufficiently
large scale depending on epsilon. The proof below gives an explicit order
of choices and the vertex-choice additive error.

This is a recommendation for these limited lemmas only. It supplies no
closed annulus, corner/phase matching, profile recovery or hypothesis H.
The separate fixed-D envelope repair is not imported as a premise or
audited here. No promotion is made by this reviewer.

Frozen candidate input:
`problems/2017-B4/notes/coordinator-directed-geodesics-candidate-v1.md`,
SHA256 `0fe9e72b07d12d7a5e417e14a56fec06191ea7f76a9f8787ea533cdd9824bcb6`.
The associated freeze JSON and byte checks are recorded separately.

## 1. Primary lemma and matching hypotheses

I read the actual original-author [Arroyo--McQuillan--Richter--Salazar
PDF](https://www.ifisica.uaslp.mx/~gsalazar/RESEARCH/levi.pdf), dated
2015-11-20, Section 2 on printed pp. 4--5. Their arrangement of arcs
permits disjoint pairs, unlike the projective pseudoline arrangement used
in their separate enlargement theorem. Lemma 2.2 gives a dual path
crossing each arc at most once. Its complete short induction proof was
read. DG1 uses that lemma, not the stronger projective theorem.

The candidate's finite set of extended de Bruijn curves meets the lemma's
requirements: each is a simple proper plane arc separating the plane;
distinct curves either are disjoint or have exactly one crossing; and
the representative points lie off every arc. Same-color parallel pairs
are expressly allowed by the source. Intersections at tile centers are
ordinary crossings, with no triple crossings. The source only supplies
a path in its plane dual; its transfer to the finite tiling requires
the separate checks below.

The background is the explicitly assumed marked zonogon/de Bruijn
dictionary and canonical lift, not the unreviewed or repaired envelope
packet. A tiled zonogon is a genuine two-dimensional polygon with a
common interior point. Empty direction classes may be omitted, provided
the remaining polygon is still two-dimensional. If all active directions
were parallel, there would be no disk tiling or interior point to which
this argument applies. In the project's positive m_i setting this
degeneracy does not arise.

## 2. Extending the disk curves without new intersections

Choose o in the interior of the convex zonogon. For each boundary
midpoint e where a curve ends, append the ray

    {o+t(e-o): t>=1}.

Convexity and interiority imply that each ray meets the polygon exactly
in its initial boundary point. The map from the polygon boundary to
radial directions about o is a cyclic-order-preserving homeomorphism.
Consequently distinct endpoints have distinct ray directions, even if
their tiling edges lie on the same straight side. Their exterior rays
do not intersect one another and cannot meet any of the original disk
arcs. Appending rays creates no new crossing, self-intersection or
identification of endpoints.

Each original de Bruijn curve is a simple compact arc with two distinct
boundary endpoints. The joined curve is therefore a proper embedding of
the real line. Both ends go to infinity on different rays, and every
compact set meets only a compact portion of it. Its one-point
compactification is a Jordan curve in the sphere, so its complement in
the plane has two sides. This checks the source separation premise
directly, rather than using a finite arc that would fail to separate
the plane.

## 3. Exact identification of plane cells with tiling vertices

Inside each parallelogram the two midpoint arcs cross at the center.
The complement has four sectors, with exactly one tile vertex assigned
to each. Across a tiling edge the sectors on the same side of its
midpoint connect and have the same common endpoint. Around a tiling
vertex, its incident sectors join in its connected star. A vertex lies
on no midpoint arc. Thus inside the disk every complementary cell is
the sector union belonging to one tiling vertex. This assignment cannot
connect different vertices: every possible sector transition across an
edge retains its assigned endpoint, and a tile center is removed by
the curves.

It remains to check infinity, where a generic finite-disk dual would
otherwise introduce a single outside vertex and shortcuts. The radial
rays cut the exterior into sectors. Consecutive curve endpoints on the
boundary are the midpoints of two consecutive **unit tiling edges**.
The boundary arc between them contains exactly one tiling vertex,
including when the sides are collinear across that vertex. The exterior
sector between the corresponding rays is homeomorphic to that boundary
arc times a radial interval. It attaches precisely to this one vertex's
inside cell. It cannot meet a second boundary interval without crossing
a ray. Therefore it merely makes an existing boundary-vertex cell
unbounded: it neither creates a new cell nor merges two cells.

The identification also holds on edges, not only vertices. A component
of a de Bruijn curve between consecutive tile-center crossings passes
through exactly one tiling-edge midpoint. Its two incident cells belong
to that edge's endpoints. An unbounded initial/final component passes
through the corresponding boundary-edge midpoint, and its two incident
unbounded cells belong to that boundary edge's endpoints. Every tiling
edge occurs exactly once in this description. There are no extra dual
edges at the artificial polygon boundary, since it is not part of the
extended arrangement. Hence the plane dual graph is precisely the
tiling vertex-edge graph. In particular, a plane-dual path that wanders
outside the polygon translates to available boundary edges, rather
than a new outside shortcut.

## 4. Color signs, nested sets and the distance formula

For each color, number its disjoint curves by their rank along its
initial boundary side. All those curves separate the base corner with
lift zero from the opposite corner whose i-coordinate is m_i. Declare
the latter side positive. Disjoint proper curves with these two common
opposite-side points have nested positive half-planes, in the boundary
rank order. Their positive-sign sets at any disk cell are therefore
initial rank segments (after choosing the consistent rank convention).

The number of positive signs at a vertex is its lift coordinate a_i.
One can check this without assuming the distance formula: at the base
vertex the number is zero. A color-i tiling edge crosses one color-i
mid-curve and no other curve; traversing it as +v_i moves from the
negative side to the positive side. Along the initial boundary path
this is exactly rank increment. Local consistency through an ij tile
preserves the convention, and the lift based at zero has the same edge
increments. Connectivity of the tiled polygon graph gives equality
everywhere. Edges of other colors leave that count unchanged.

Thus for cells x,y precisely

    |a_i(y)-a_i(x)|

color-i curves separate them: it is the size of the symmetric difference
of two nested initial segments. Counting just the number of different
signs without nesting would not suffice; the same two corners and
noncrossing same-color curves provide the needed nesting.

Apply the primary lemma to points in the corresponding plane cells.
Its dual path crosses every curve at most once. It crosses every
separating curve, since a curve separates the plane into its two sides.
It crosses no nonseparating curve: a transverse path returning to the
same side would need an even number of crossings, whereas at most one
is allowed. Its length is consequently the total number of separating
curves, namely the asserted L1 sum. Conversely every tiling edge changes
one lift coordinate by one in absolute value, so every graph path has
at least that many edges. This proves equality of graph distance.

If all endpoint differences are nonnegative, each separating curve is
crossed from its negative side to its positive side. Every edge is
therefore +v_i. If a coordinate difference is zero, that color has no
separating curves and the shortest path uses no edges of that color.
If x=y the empty path is the appropriate shortest positive path. No
strict positivity of the endpoint differences is needed in DG1.

## 5. DG2: endpoint order and the displayed constant

Set

    e_k=a(w_k)-(Jx_k+c),  ||e_k||_infinity<=E.

Then for every color i,

    a_i(w_(k+1))-a_i(w_k)=ell J_i u+e_(k+1,i)-e_(k,i)
       lies in [kappa ell-2E, K ell+2E].

The stated threshold makes every increment nonnegative, so DG1 applies
to each successive pair. Equality in the threshold can give some zero
increments; DG1 already covers them. A repeated consecutive vertex
gives an empty subpath. The assumption kappa>0 excludes u=0 in any
nontrivial step. No assumption that every gradient lies in K_D is needed
for this conditional linear estimate.

For any point z on a positive subpath, use affine interpolation of the
lift on its edges. Each coordinate of `a(z)-a(w_k)` lies in
`[0,K ell+2E]`. Since `Va(z)=z`,

    ||z-w_k||_2 <= sum_i ||v_i||_2 (K ell+2E)
                = M_V(K ell+2E).

Also `VJ=I` and `Vc=0` give

    w_k-x_k=V e_k,  ||w_k-x_k||_2<=M_V E.

Adding proves exactly

    ||z-x_k||_2<=M_V(K ell+3E).

This also bounds distance to the full target segment, since x_k is a
point of it. Linear interpolation on an edge cannot enlarge the
coordinate bounds or the norm bound. Both the combinatorial length
and the Euclidean edge length telescope: the former is the sum of
coordinate increments, and the latter is the same sum weighted by
`||v_i||_2`. Every nonempty positive edge has physical x displacement
one. A concatenation has no directed cycle and is x-monotone, apart
from irrelevant empty subpaths.

The kernel condition on c is essential to the displayed reference-point
bound and is present in the statement. Without it an extra `||Vc||`
term would be needed. Likewise the direction lower bound is a genuine
margin hypothesis, not a conclusion from affine closeness.

## 6. Choosing vertices, scales and a genuine buffer

Here is a precise interpretation of the note's asymptotic paragraph.
Suppose on the relevant region the continuously interpolated lift has
uniform error at most `C epsilon L` from a fixed affine map Jx+c.
For x_k inside a tile, choose any of that tile's vertices w_k. On a
unit ij parallelogram the only varying lift coordinates are its two
unit tile parameters, so

    ||a(w_k)-a(x_k)||_infinity<=1.

Therefore E may be `C epsilon L+1`. If the error hypothesis is instead
given only at nearby vertices, comparison of Jw_k with Jx_k adds at
most the fixed tile diameter times the relevant norm of J. This is
the candidate's harmless `O_(D,J)(1)` term. An appropriate tile-scale
buffer is then needed to ensure the chosen vertex is among the vertices
where the hypothesis holds. The statement constructs paths in the
full tiling, so it does not assume that all tile vertices of a cut
window lie in that window.

For example take `ell=sqrt(epsilon)L`, with kappa,K and C fixed.
If `sqrt(epsilon)<=kappa/(4C)` when C>0 and

    L>=4 C_0/(kappa sqrt(epsilon)),

where C_0 is the additive vertex-choice error, then
`2(C epsilon L+C_0)<=kappa ell`. Enlarging the threshold also handles
unit tile size and any rounding of the sampling interval. The estimate
becomes `O_(D,J,u,C,kappa,K)(sqrt(epsilon)L)`. In the candidate the
direction bounds and affine-error constants are fixed, so its shorter
constant notation is consistent. This is not a uniform bound as kappa
tends to zero or as the affine-error constant grows.

One can even keep the band constant independent of those fixed values:
choose `ell=sqrt(epsilon)L/K`, then make epsilon small and L large
enough that `E<=kappa ell/2`. The exact formula gives
`R<=M_V(K+3kappa/2)ell<=5M_V sqrt(epsilon)L/2`. The necessary
epsilon and scale thresholds still depend on C,C_0,kappa,K. Thus the
candidate's band notation does not remove its fixed-margin restriction.

For confinement one needs the entire R-neighborhood of the sampled
target segment to lie in the permitted region, with
`R>=M_V(K ell+3E)`, as well as the vertex-choice allowance if needed.
The proved distance band then keeps all subpaths there. A buffer only
at some vertices, or only at the sides away from a corner, would not
imply that assertion. The note explicitly requires a buffer and only
claims paths in the full tiling before imposing it. It does not supply
an arbitrary boundary-to-boundary path in an unbuffered subwindow.

No exact prescribed final corner, paired boundary word or phase is
chosen by this argument. If a desired long segment has a nonintegral
number of nominal steps, its step length can be slightly adjusted by
choosing the integer number first, or its final short part can be left
outside this local lemma. Neither option is an annulus construction.

## 7. Adversarial checks and disposition

I specifically checked parallel same-color arcs, collinear unit boundary
edges, boundary cells at infinity, possible extra dual edges, zero
coordinate differences, equality in the ordering threshold, repeated
vertices, the projection of c, vertex selection near a cut boundary,
fixed versus vanishing direction margin and the order of epsilon and
large-scale choices. No counterexample to DG1 or conditional DG2 was
found. No statement about an arbitrary planar graph or unrestricted
near-flat collars is used.

DG1 and DG2 pass this whole independent audit under their explicit
background and stated restrictions. The issue ledger records no open
substantive objection. Closed compatible side systems, corner offsets,
phases, zero-margin strata, recoverable inserted interiors, EAI, PR and
H remain outside the proved claim. A second fresh blind audit and the
coordinator's decision are still required for any project promotion.
