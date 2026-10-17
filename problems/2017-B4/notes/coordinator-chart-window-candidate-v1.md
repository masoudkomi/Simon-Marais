# Fixed target windows and exact pullbacks under a local chart

2026-10-17 UTC. **Candidate proof - unverified**, coordinator root.
Two fresh initially blind nonconstructor whole audits are required.
This proves geometric and coding interfaces only. It is not a local
entropy theorem, UR4, H, PR or an official limit. No mathematical
computation or CAS was used; no novelty is claimed.

The explicit dependency is the accepted finite orientation packet
`proofs/reviewed-orientation-charts-v1.1.md`, SHA-256
d15ed547defaffc617ffc6faf6df683c8473ecd9077be63e52d02bbb4edb4ca8,
with its full-balanced-tiling, rank, lift and affine-offset hypotheses.
The marked dictionary and fixed local lattice alphabet are the accepted
background. No unproved strict, rank-mesh or global program is a premise.

## Fixed data and exact affine formulas

Fix D and the original standard physical columns v_i=(1,i-1).
Let T range over actual full BALANCED marked tilings of content p,
with canonical lift a_T and V a_T(x)=x. Fix one matrix J with
VJ=I and all ordered row minors nonnegative. Choose one of OC1's
valid cyclic cuts k for THIS J, and use that same cut for the whole
local family. Write S for the signed permutation taking the original
list to k,...,D,1,...,k-1, with the moved prefix negated. Let sigma
be the correspondingly permuted indicator of the flipped coordinates.
Put

    b0=p sum_(i<k) v_i,  x'=x-b0,
    a'_T(x')=S a_T(x)+p sigma,
    J'=S J,  V'=the signed/reordered physical matrix,
    W_i=(1,i-1) in the NEW slots, A=WJ'.

The complete orientation theorem gives an actual homeomorphism

    F_T(x)=W a'_T(x-b0)

from the original full zonogon to the full standard balanced zonogon.
The notation F_T uses ORIGINAL x, so its source translation is already
included. The map and inverse have constants independent of T,p.
The matrix A is invertible and has uniform inverse bounds for bounded
J, including zero minors. Different physical windows may choose different
cuts; no simultaneous global chart for a nonaffine profile is assumed.

Suppose on a source region a_T(x)=Jx+c+e_T(x), Vc=0,
with the SAME J,c for every source representative. Define

    c'=J'b0+S c+p sigma, b=Wc'-A b0,
    J*=J'A^(-1), c*=c'-J*Wc'.

These data are fixed across the family. Direct substitution gives

    V'c'=0, Wc*=0,
    F_T(x)=A x+b+W S e_T(x),                         (CW0)
    a'_T(x-b0)=J*F_T(x)+c*+(I-J*W)S e_T(x).         (CW0')

All norms below can be Euclidean, after fixed-D conversions from an
infinity-norm source error. If |e_T|<=E, let delta=||W|| E.

## CW1. One fixed target core and its whole buffer really exist

Let Q be a closed Jordan parallelogram in the source tiled domain,
and assume the stated error bound on all of Q. Put P=AQ+b.
For each T,

    P eroded by any distance >delta subset F_T(int Q),
    F_T(Q) subset P+closed_ball(0,delta).             (CW1)

In particular, a fixed target parallelogram and its required whole
neighborhood can be used for EVERY T whenever that neighborhood is
inside the stated erosion of P. Its transformed lift satisfies the
common affine estimate CW0' there. Hausdorff closeness alone is not
being used to infer inclusion for arbitrary Jordan curves.

Proof. The outer inclusion is immediate pointwise from CW0. For an
interior y at distance>delta from partial P, the boundary homotopy

    H_s(z)=Az+b+s(F_T(z)-Az-b), z in partial Q,
    0<=s<=1,

never reaches y: |Az+b-y|>delta and the perturbation is at most
delta. Its winding number is therefore the affine boundary's1.
Since F_T is a full homeomorphism, F_T(partial Q) is a Jordan
curve bounding F_T(int Q); its winding1 puts y in that interior.
Boundary points of the strict erosion follow by the same argument
at their positive margin. This proves the assertion and ensures
the full target neighborhood, rather than merely its four corners,
is covered. CW0' gives its affine estimate with one common c*.

At any y in F_T(Q), the exact same formula also gives

    |F_T^(-1)(y)-A^(-1)(y-b)|<=||A^(-1)|| delta.      (CW1')

Thus an actual target tile patch inside that common target core has
its entire original-reference pullback in the controlled source
region. Uniform bilipschitz constants are additionally available
from OC3; no shape equality F_T(Q)=AQ+b is asserted.

## CW2. A local upper-count encoding survives the chart change

Let Q0 be a fixed closed convex source parallelogram. All source
tiles meeting Q0 are contained in its d_tile-neighborhood, where
d_tile is the maximum physical tile diameter. Assume that this
neighborhood is inside Q and has the bound |e_T|<=E. Choose a
fixed convex target parallelogram Pplus, contained in every full
target zonogon, such that

    A(Q0+closed_ball(0,d_tile))+b
                         +closed_ball(0,delta) subset Pplus.

The left side need not be a parallelogram; its inclusion is an
explicit margin hypothesis. Give Pplus the whole target buffer
needed by a separate theorem using CW1 in a larger source Q.
Record a target restriction as ALL target tiles meeting Pplus.
Also record one canonical target-lift anchor at a deterministically
chosen vertex in that restriction. Take R>=max(2,p) bounding the relevant original positions and heights.
That anchor has O_D(log(R+2)) bits.

Then the source restriction to Q0 is recovered from this target
record and anchor. Consequently, choosing one full representative
for each distinct source restriction gives the upper-count bound

    number(source Q0 restrictions)
      <=number(target Pplus restrictions) * 2^O_D(log(R+2)). (CW2)

This is a local injection with an explicitly retained anchor,
not an equality of arbitrary source and target window counts.

Proof. Every point of a source tile meeting Q0 lies in the stated
source neighborhood. CW0 and the margin imply its ENTIRE image
tile is in Pplus. Thus all such source tiles are represented in
the recorded target patch. Because Pplus is connected and actually
tiled, the union of its intersecting tiles has a connected tile-edge
graph (possible vertex-only contacts still connect the graph).
Colored increments and one anchor determine the target canonical
lift on that graph. Reverse OC3's direction replacement using V',
then reverse the fixed OC2 signs, p-a_i, label permutation and
translation. This reconstructs the physical source position,
fine color, rank and shape of every represented source tile.
Filter them by intersection with the known Q0.

One need not infer the inverse from the target physical coordinates
alone; the single lift anchor is material. The anchor vertex itself
is deterministic from the known target geometry, so its location
does not acquire a separately unbounded code. Its integer height
coordinates lie in[0,p], making the stated bound valid. Distinct
source restrictions cannot have the same target record and anchor,
since the described recovery would give the same source tiles.
If one source restriction has several full representatives, choose
one before mapping; no well-definedness across all extensions is
needed for this injection.

## CW3. Pull back replacements to the EXACT original boundary

Fix ONE actual full reference T. Let Omega be any Jordan union of
whole target tiles in F_T(int Q), with COMPLETE boundary colors and
canonical lift inherited from F_T(T). Its reference pullback

    C_T=F_T^(-1)(Omega)

is an actual Jordan union of whole original tiles inside int Q.
Every target filling of Omega with the SAME complete boundary
pulls back to a fine filling of the SAME C_T with its original
complete boundary, leaving the full fine exterior fixed. Distinct
target choices remain distinct. No claim that a newly filled target
patch has the old interior affine approximation is made or needed.

Proof. The reference full homeomorphism gives the claimed disk
and boundary, including edge/vertex stars. Glue a proposed target
filling to the unchanged full target exterior. This is an actual
full target tiling with the original full marked boundary. Apply
the exact inverse of OC3 and OC2 to that FULL tiling. It gives
an actual full original tiling. On the exterior of Omega the
canonical lift is the old one: its boundary normalization and
connected exterior fix the same height. Hence inverse tile
positions and lifts there agree with T. The boundary of Omega
has the same complete height, so its inverse boundary is exactly
partial C_T. The inverse full homeomorphism puts the replacement
inside that Jordan boundary, with no overlap or excursion outside.
Applying the forward chart reconstructs the chosen target filling,
which proves the injection and recoverability.

This argument keeps the old pullback REGION fixed through the
boundary and exterior. It does not assume the new filling's
interior inverse map agrees pointwise with the old F_T^(-1).

## CW4. Integer dilation commutes, and several charts can coexist

Dilate the ONE original reference T by a positive integer M,
subdividing every enlarged tile by its M-by-M grid. Denote this
full reference MT. On every enlarged tile its canonical lift is
exactly a_MT(Mx)=M a_T(x), including its affine interpolation.
Reorientation uses content Mp and source translation Mb0. Thus

    F_MT(Mx)=M F_T(x)                                 (CW4)

as an exact identity, not an asymptotic estimate. In particular
the pullback of M Omega in the reference is exactly M C_T.
Every boundary-compatible target filling of M Omega therefore
inserts into the EXACT M-dilation of the original C_T, with the
same fixed dilated fine exterior. Its complete ranked port data
are inherited from subdivided colored boundary edges, with no
new permutation choice. Here each edge has M consecutive ranks;
no independent rank matching is chosen.

For a finite family of source windows Q_alpha with disjoint
interiors and cores strictly inside them, choose potentially
different cuts k_alpha and target disks Omega_alpha, all from
the SAME fine reference T. CW1 can guarantee each pullback
C_alpha lies inside its own source window. The C_alpha are
therefore disjoint. After dilation the M C_alpha remain disjoint.
Use CW3 separately to obtain a fine replacement in each one,
and glue them to T (or MT) along their fixed complete boundaries.
This gives a product injection, recovered by restricting to the
fixed C_alpha (or M C_alpha) and then applying each local chart.

There is no need for a single chart to orient all windows or
for the independently chosen global chart maps to commute.
Each is used only to construct a fine patch with the SAME
boundary as its reference patch. Those are the actual objects
glued in the original physical plane. One may not choose the
reference separately for different globally conditioned code
classes unless a common representative has first been fixed.

## Limits of these interfaces

The fixed target margins, full buffers, anchor ranges and one
reference are explicit hypotheses. To use these lemmas in a
global count, one still needs disjoint window selection, a
code for discarded regions, strict/degenerate local entropy
estimates and a complete order of all parameters. They do
not follow merely from finite charts or bilipschitz constants.
No arbitrary input-window image is called canonical, no entropy
formula is imported, and no H/PR/UR4 or official rate is proved.
