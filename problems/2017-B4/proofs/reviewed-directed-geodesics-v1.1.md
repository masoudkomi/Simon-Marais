# Directed geodesics and near-flat side paths

2026-10-17 UTC. **Proved, independently reviewed partial results: DG1 and conditional DG2.**
Constructor: coordinator. Both fresh initially blind nonconstructor whole
audits and their issue ledgers were fully read before coordinator acceptance.
The frozen v1 is preserved. This exposition adds only the explicit domain,
lift normalization and fixed-data scale clarifications reconstructed by both
audits; see reviews/directed-geodesics-acceptance.md/json. No closed annulus,
entropy recovery, hypothesis (H), novelty or full solution is claimed.
No enumeration or CAS is a premise.

## Precise primary input

Arroyo, McQuillan, Richter and Salazar, *Levi's Lemma, pseudolinear drawings
of K_n, and empty triangles*, author preprint dated 2015-11-20,
[full author PDF](https://www.ifisica.uaslp.mx/~gsalazar/RESEARCH/levi.pdf),
Section 2, printed pp. 4–5, Lemma 2.2. The complete definition, lemma and
proof were read on 2026-10-17 UTC. Their finite arrangements of proper
plane arcs allow nonintersecting parallel pairs; any intersection is a
single crossing. The lemma supplies a dual cell path crossing each arc
at most once. This broader arc result, rather than the projective
every-pair-crosses enlargement theorem, is the needed input.

Its finite-disk application below passed both independent whole audits.
This is an adaptation of a published method, not a new partial-cube theorem. No
external annulus theorem is assumed and no full PDF is redistributed.

## DG1: coordinate-ordered vertices have a positive path

Use fixed D, vectors v_i=(1,i-1), and the zonogon Z=sum_i[0,m_i v_i].
Assume the established marked tiling/de Bruijn dictionary: its
edge-to-edge parallelogram tiling has m_i color-i curves; different-color
pairs cross once, same-color pairs do not; each vertex has canonical
lift a in Z^D with Va(x)=x, where V has columns v_i. A positive edge
v_i increments a_i by one. These are explicit background hypotheses,
not an import of the other unreviewed fixedD structural packet.
Require nonnegative integer m_i with at least two active directions, so Z
is a genuine two-dimensional tiled disk; normalize the marked lift a(0)=0.
Empty colors may be omitted. The one-active-direction segment case is
outside this radial disk proof. In DG2, error E and mesh ell are nonnegative.

**DG1.** For tiling vertices x,y, their graph distance is

    sum_i |a_i(y)-a_i(x)|.

If every coordinate difference is nonnegative, some shortest path uses
only positive v_i edges.

Draw the curves across opposite tile edges, with crossings at tile
centers and ends inside boundary edges. Extend every end radially
outside the convex zonogon from a common interior point. Different
ends have different directions; their exterior rays are disjoint and
create no crossings. Each resulting full curve is a proper simple
copy of R and separates the plane. Thus the cited arc lemma applies.

The extended plane dual graph is the tiling-vertex graph. Within a
tile the mid-arcs have four sectors, one for each vertex. Across an
edge these sectors join by the common endpoint; around a vertex they
form its connected star. Hence inside cells correspond to vertices,
with adjacency across tiling edges. Each exterior wedge between
consecutive radial ends attaches to the boundary arc between those
ends. That arc contains one boundary vertex and no other curve end.
It therefore continues one existing vertex cell, creating neither
another cell nor an identification of distinct cells. Exterior ray
segments yield the same boundary-edge adjacencies already present.
This checks that the plane dual path gives no unavailable shortcut.

Apply Lemma 2.2 to points in the cells for x,y. A path crossing each
curve at most once crosses exactly the separating curves. A
nonseparating curve would need an even positive number of crossings,
and a separating curve must be crossed at least once. Within each
color, disjoint curves are ordered and the side-sign sets are nested
initial segments, with sizes a_i. Thus exactly |a_i(y)-a_i(x)|
color-i curves separate the cells. Every edge crosses one curve,
proving the distance formula. If all differences are nonnegative,
all crossings increase the associated rank coordinate; these are
precisely positive v_i edges. No convex profile mixing is used.

Both the disk-to-plane cell identification and the nested-sign/lift
identification are substantive audit targets, not consequences inferred
from an arbitrary graph being planar.

## DG2: localization near a strictly positive affine direction

Let J be D-by-2 with VJ=I, and c in R^D with Vc=0. Fix u such that

    0<kappa<=J_i u<=K for all i.

Suppose vertices w_0,...,w_N satisfy, for x_k=x_0+k ell u,

    |a(w_k)-(J x_k+c)|_infinity <= E,
    kappa ell >= 2E.

Then successive lift increments are nonnegative, and at most K ell+2E
in each coordinate. DG1 supplies positive-edge paths through those
vertices. Put M_V=sum_i ||v_i||_2. Each point z on the k-th subpath
satisfies

    ||z-x_k||_2 <= M_V (K ell+3E).

Indeed Va(w_k)=w_k, VJ=I and Vc=0 give
||w_k-x_k||_2<=M_V E. Along the positive subpath each lift coordinate
lies between its endpoint values, giving the remaining bound. Linear
interpolation on an edge preserves it. Thus the path is in this
distance band around the target segment. Its length telescopes in
the lift, and its physical first coordinate increases on every edge.

For a region of diameter L with uniform affine lift error O(epsilon L),
one can choose ell of order sqrt(epsilon)L at sufficiently large scales,
with fixed kappa,K. Vertices w_k can be chosen in tiles containing x_k:
tile diameter is bounded at fixed D, so the error gains only an O_D,J(1)
term, which must be included in E and the scale threshold. The bound is
then an O(sqrt(epsilon)L) side band, with D,J,u,kappa,K and the affine
error constant fixed. For example let 0<epsilon<=1 and
E<=C epsilon L+C0. Choose A>=max(1,4C/kappa), set
ell=A sqrt(epsilon)L and require L>=4C0/(kappa A sqrt(epsilon)).
Then kappa ell>=2E and the exact DG2 bound has the stated order.
This is not uniform as kappa tends to zero. The sqrt choice does not
assert an epsilon=0 conclusion in the presence of a sampling error.
The closed neighborhood of the ENTIRE target segment of radius
M_V(K ell+3E) must lie in the permitted region to ensure confinement.
An endpoint-only buffer does not suffice. DG2 otherwise constructs paths
in the full tiling.

## Remaining extension gap

Paths for different sides need not yet form a compatible simple closed
boundary. Shared endpoints, color counts, corner rank offsets, phases,
and recovery of every inserted interior remain separate obligations.
Zero-margin boundary strata are excluded by the positive kappa
hypothesis. A weak-order band lemma might help after compatible
boundaries exist; no closed-annulus theorem follows just from these
side paths. Neither EAI, profile recovery, (H), numerical frontier
progress nor the full 2017 problem is asserted. The accepted scope is DG1 and conditional DG2 only.
