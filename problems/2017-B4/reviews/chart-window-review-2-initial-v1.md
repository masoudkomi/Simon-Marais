# CW0–CW4 whole independent audit R2

2026-10-17 UTC. Initial nonconstructor adversarial whole audit, frozen
before reading any peer chart-window report, issues or conclusions.
Reviewer: /root/review_2022_complexity_r2. Requested model/reasoning:
gpt-6.1-sol/max; an independent effective-setting readback is unavailable.

Target: notes/coordinator-chart-window-candidate-v1.md, SHA-256
c272eabf4d5efcd2d0f8075d68b010ec00a48e824bdec81e563f6402a7568e0b,
11284 bytes. Author freeze: coordinator-chart-window-freeze-v1.json,
SHA-256 f9708bcba4de2c877420e162336a8a8775c3a72e30c98eb2b03fef7e540e6a19.
I read the whole target, the whole exact accepted orientation exposition,
its acceptance scope, the whole accepted fixed-D structural exposition,
AGENTS.md, the marked official statement and reference metadata. This
report does not use the local-code, uniform-strict, rank-mesh or entropy
program as a premise.

Disposition: no substantive objection found to the stated interfaces.
The whole argument survives the attempts below. This is a recommendation
about these scoped claims, not promotion and not a solution of 2017 B4.
The coordinator must compare two complete independent audits and decide.

## Domain and exact accepted input

The official problem concerns fixed-polygon rhombus counts and their
normalized liminf and limsup for all integers n>=2. The fixed-D balanced
integer zonogon is an attributed count-preserving normalization of part
of that program, not the official varying-direction polygon silently
identified with one local window. I checked B4 on the official Paper B,
page2. Nothing here establishes either requested rate or their equality.

The input is an actual full balanced marked tiling, D>=2 and positive
integer content p, with canonical lift a, Va=x and all heights in [0,p].
These are the orientation theorem's hypotheses; the packet's explicit
dependency imports them. A degenerate zero-area object or an arbitrary
standalone patch with no full extension is not an admissible input.
The fixed row matrix J satisfies VJ=I and all ordered minors >=0.
One valid cut k is chosen for this J and held fixed across the family.
The source offset c and p are also common across that family.

Accepted OC2/OC3 give an exact marked bijection of FULL tilings in both
directions. They do not require every row minor to be positive. Every
individual tile still has positive source and target physical determinant
because both ordered physical vector lists do. The finite tile-type
derivative bounds and the full convex zonogons make the deformation and
its inverse globally bilipschitz, uniformly in p and the filling.
For bounded J the Cauchy–Binet determinant bound gives uniform A inverse
bounds even when some tangent rows or minors vanish. I reconstructed
these hypotheses from the exact accepted text, rather than supposing a
local affine approximation itself supplies a full inverse.

## CW0: translations, offsets and both identities

Let S be the signed permutation of lift coordinates. It is orthogonal,
V'S=V, and the new-slot indicator sigma has ones exactly at the flipped
coordinates. With b0=p sum_(i<k) v_i,

    V'(p sigma)=-b0.

This sign is essential. Starting at an ORIGINAL point x gives

    a'(x-b0)=S a(x)+p sigma
             =J'x+S c+p sigma+S e(x)
             =J'(x-b0)+c'+S e(x),
    c'=J'b0+S c+p sigma.

Consequently V'c'=b0+Vc-b0=0. Multiplication by W gives

    F_T(x)=W a'(x-b0)
           =A x+[W c'-A b0]+W S e(x)
           =A x+b+W S e(x).

Equivalently b=W S c+p W sigma. This second expression confirms that
no source translation was accidentally included twice in F_T.
Everything other than e is fixed across the common source family.

Set J*=J'A^-1 and c*=c'-J*Wc'. Since WJ*=I, Wc*=0.
Substitution into J*F_T+c* yields J'x+S c+p sigma+J*W S e.
The difference from a'(x-b0) is exactly (I-J*W)S e. This proves
CW0' with one common target offset, not separate offsets chosen at
different corners or at different target points.

After the stated fixed-D conversion to Euclidean error, S preserves its
norm. Thus delta=||W||E bounds the physical displacement in CW0, while
||I-J*W||E is the target lift error. The latter applies at the actual
image point y=F_T(x). Zero row/minor cases do not invalidate either
identity or the inverse A. Constants may depend on fixed D and the
bounded matrix class; no small positive-minor lower bound is introduced.

## CW1: genuine inclusion and full buffer control

For a closed nondegenerate parallelogram Q in the source full domain,
its image under the full homeomorphism has boundary F_T(partial Q).
Its interior is the image of int Q. The affine image P=AQ+b has
positive orientation because det A>0.

Take y in P with dist(y,partial P)>delta. At every z in partial Q
the straight-line boundary homotopy

    A z+b+s(F_T(z)-A z-b)

stays at positive distance from y: the affine distance exceeds delta,
and the perturbation has norm <=delta. Its winding number is therefore
unchanged from the affine boundary, namely one. The simple closed image
boundary has winding one precisely in its bounded interior. This proves
y lies in F_T(int Q). It is a degree/winding argument using the full
homeomorphism, not an inference from boundary Hausdorff distance alone.

For a closed erosion at distance t>delta, every point still has this
positive margin, including that erosion's own boundary. The outer
inclusion follows directly pointwise from CW0. The argument permits
E=0 and boundary contact between Q and the full zonogon; int Q still
lies in the full polygon's interior. If the erosion is empty or too
small for the desired buffered frame, the assertion is empty and its
later explicit margin hypothesis fails. The packet does not guarantee
nonempty cores for arbitrary E or arbitrary small Q.

The whole chosen target neighborhood must be a subset of this fixed
erosion. It then lies in every F_T(int Q), and CW0' holds at ALL its
points by pulling back through each full homeomorphism. Checking only
four corners would not suffice, but that weaker condition is not used.
For y in F_T(Q), write y=A x+b+d, |d|<=delta. Then

    x-A^-1(y-b)=-A^-1 d,

which proves CW1' with constant ||A^-1||delta. In particular, if a
closed actual target patch is wholly inside the common core, its entire
reference inverse lies inside the controlled source region. No equality
between the nonlinear image of Q and P is needed.

## CW2: all tiles, one anchor and a real injection

If a source tile meets Q0, choose an intersection point. Every other
point of that tile is within d_tile of it, so the WHOLE source tile
lies in Q0+closed_ball(0,d_tile). The assumed neighborhood inclusion
puts its whole lift error under control. CW0 and the Pplus margin
then put its whole image tile inside Pplus. The chart maps actual tiles
to whole corresponding target tiles, not just to nearby subsets.

The target record contains all target tiles meeting the fixed Pplus.
It therefore includes the image of every source tile needed for the
Q0 restriction. It may also contain extra target tiles whose full
inverse is outside the controlled Q; this causes no difficulty.
Their exact inverse comes from the full tiling correspondence and
does not require a local affine estimate. Only the guaranteed images
of the needed source tiles use the margin calculation.

The recorded tiles form a connected finite complex. Indeed Pplus is
connected and covered by these tiles, and each recorded tile meets it.
The union is connected. In a face-to-face polygonal complex, the
one-skeleton of each tile is connected and tile intersections are
edges or vertices, so the union's edge graph is connected too.
Vertex-only contacts are sufficient for that graph statement and
do not require an edge-sharing dual graph.

Choose a vertex deterministically from the recorded physical geometry,
for example lexicographically. On each oriented target edge, color i
changes the canonical lift by +/-e_i. Starting from the one anchor
and following a graph spanning tree reconstructs all canonical heights.
Path consistency follows because the record and anchor come from an
actual full tiling. The absolute target vertex positions are already
part of the fixed-window record, so the chosen vertex index/location
does not incur an additional unbounded parameter.

Each coordinate of this integer anchor lies in [0,p]; there are at
most (p+1)^D choices. R>=max(2,p) therefore pays for it with
O_D(log(R+2)) bits. The estimate retains this cost and never uses
p=O(window size) or R=O(window size). The known fixed p also determines
the sign-reversal constants and source translation. A family with
varying unknown p would need different data and is not this statement.

At every reconstructed target vertex with height a', reverse OC3:
x'=V'a'. Reverse the signed permutation, recover a=S^-1(a'-p sigma),
and put x=x'+b0=Va. This reconstructs complete source tiles, colors,
physical positions and fine ranks. Restrict by intersection with the
known Q0. All source tiles meeting it were included; extra reconstructed
tiles are simply discarded by this test.

To define the counting injection, select ONE full representative for
each distinct source restriction, and send it to its target restriction
and anchor. Equality of those two records forces equality of all
recovered source tiles, hence equality of source restrictions. The
map need not be independent of every possible extension of a source
patch. This proves the asserted upper bound. It is neither equality of
two unrestricted local counts nor an arbitrary extension theorem.

## CW3: the old region is fixed by its boundary and exterior

Fix an actual full source T and its full target image. Omega is a
Jordan union of whole target tiles, with its CLOSED disk contained
in F_T(int Q). The reference inverse C_T is a Jordan union of whole
source tiles contained in int Q. This uses the actual tilewise full
homeomorphism, including boundary edges and vertices.

For an arbitrary proposed target filling, the complete boundary must
match the old Omega in its actual physical positions, colors, canonical
heights and ranks. Glue it to the unchanged full target exterior.
This is a full marked tiling of the same balanced target zonogon.
All edge incidences match; in the integer model a unit horizontal
edge has no hidden interior lattice vertex. Apply the exact FULL
inverse of OC3/OC2 to this newly completed full tiling.

Omega is strictly inside the full target polygon, so its complement
there is a connected annular exterior, including the original outer
boundary normalization. On that exterior the colored edges and
normalization are unchanged. Canonical integration therefore gives the
old heights everywhere on the exterior, including Omega's boundary.
The inverse positions V'a', sign changes and b0 consequently agree
with the old inverse there. The original fine exterior is fixed.

The new full inverse takes the fixed boundary of Omega to exactly
the old partial C_T. That simple closed polygon bounds the same
bounded Jordan disk C_T. The new inverse is a full homeomorphism and
Omega is an interior disk, so its image occupies that disk, rather
than wandering outside it or overlapping the fixed exterior.
The new interior inverse need not agree pointwise with the old
F_T^-1; no step assumes it does. This distinction resolves the
main potential false inference in a naive local pullback argument.

The forward full chart recovers each target filling from its inverse
source filling, so different choices remain different. A boundary
height anchor is inherited here from the one fixed full reference;
it is not independently chosen for each proposed filling.
Interior affine approximations are only for the reference/interface;
the replacement interior is allowed to be arbitrarily nonflat.

## CW4: every integer scale and independent local charts

On a tile enlarged by integer M, the M-by-M grid uses the same unit
physical edge vectors and the same lifted edge increments. Its affine
lift equals M a_T(x) at Mx throughout that enlarged tile, not just at
its corners. Across shared tile edges these formulas agree. The
canonical full boundary normalization is also scaled, giving

    a_MT(Mx)=M a_T(x)

on the whole reference polygon. This is an actual full content-Mp
tiling, with no residue restriction on M>=1.

Its reorientation has translation Mb0 and constant Mp sigma. Hence

    F_MT(Mx)
      =W[S a_MT(Mx)+Mp sigma]
      =M W[S a_T(x)+p sigma]
      =M F_T(x).

The target reference is exactly the M-grid subdivision of the old
target reference. Thus M Omega is a union of its whole tiles, and
its reference inverse is exactly M C_T. Applying CW3 to THIS full
dilated reference proves insertion into that exact original-domain
dilation for every positive integer M. This does not choose unrelated
nearby source windows at different scales.

An old unit boundary edge with lift coordinate interval [r-1,r]
becomes M unit edges with coordinate intervals from M(r-1) to Mr.
Their ranks are consecutive and predetermined. For flipped colors
the reversal s -> Mp-s+1 gives exactly the reversed consecutive
block prescribed by the scaled p-a_i formula. There is no independent
permutation of new ports or matching choice.

For several windows, all the reference patches C_alpha are obtained
from ONE actual fine T. Each lies strictly inside its own Q_alpha.
Since the Q_alpha interiors are disjoint, these closed patches are
pairwise disjoint, and remain so after multiplying by M. Each local
chart inverse supplies a filling of its own fixed fine patch with
the SAME complete boundary. Gluing all these fillings to the single
fine exterior gives a valid full tiling independently of whether
the global chart maps agree elsewhere.

For recovery, restrict the final fine tiling to each fixed C_alpha,
use its inherited boundary lift, and apply that alpha's forward
chart. Other disjoint changes cannot alter this local lift: its
boundary heights and the exterior normalization are fixed. Thus
the tuple of target choices is recovered, proving a product injection.
This works for the same exact M-dilation. No simultaneous global
affine chart for a nonaffine profile is needed. Picking incompatible
reference exteriors separately would invalidate the argument, but
the packet explicitly requires one common reference.

## Adversarial boundaries, failed objections and scope

I specifically tried: a lost p sigma or b0 sign; zero tangent rows;
an erosion too small to exist; mere boundary closeness with a thin
or wrongly enclosed image; a tile touching Q0 only at one vertex;
a target patch connected only through tile vertices; an unbounded p
hidden in a window-size code; multiple extensions of one source
restriction; a replacement with a different interior inverse; edge
subdivision and flipped ranks at M=1 and arbitrary M; and incompatible
global chart maps for adjacent windows. The exact formulas, positive
margin, full-tile records, explicit anchor, representative selection,
full inverse, exact grid lift and one-reference requirements respectively
dispose of these attempts. No mathematical enumeration or CAS was used.

None of the hypotheses supplies a target buffered frame when its
margin is absent. The lemmas do not assert a canonical image shape,
uniform entropy for varying tangents, a global discard code, admissible
window selection, an all-profile assembly theorem or an official
limiting count. They also do not remove log R from an upper code or
allow different conditioned reference exteriors to be multiplied.
The final paragraph of the target correctly keeps those obligations
separate. Exact OC and dictionary inputs suffice; no rank-mesh, DG,
CUT, strict-transfer, LW, US, H or UR4 conclusion has been imported.

Twenty separate inference records accompany this full report. All
five declared author-freeze rows and the exact target/freeze hashes
were checked. Earlier own frozen records are verified and preserved
by the accompanying integrity file. Only this assigned review prefix
was written; there were no candidate, shared or Git edits. Latest
direct account telemetry during this audit was 29% total weekly used,
10080-minute window, reset1792745187, ordinary usage allowed; the
90%-total ceiling and integration reserve remain in force.
