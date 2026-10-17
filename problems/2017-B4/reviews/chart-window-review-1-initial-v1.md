# Independent whole initial audit of CW0–CW4

2026-10-17 UTC. Reviewer `review_2021_reasoning_j15_r2`; requested
`gpt-6.1-sol` / `max`, verified effective settings unavailable.

**Recommendation:** no substantive defect found in the stated
CW0–CW4 geometric/coding interfaces. The fixed target margins,
whole-buffer error hypothesis, anchored lift, complete boundary and
one common actual reference are necessary hypotheses and are all
retained. This report does not accept an entropy estimate, UR4,
H, PR, a global chart or an official limit.

I did not construct or contribute to this candidate. My earlier D4
strict candidate is a separate result and is not used in this audit.
The entire initial report, per-claim ledger and source checks were
completed before reading any peer CW report or receiving its findings.
No mathematical program, enumeration, CAS, Git operation, shared-file
edit, external contact, charge or subagent was used. The accompanying
program checks record integrity only.

## Full target and accepted dependency boundary

Candidate `notes/coordinator-chart-window-candidate-v1.md`, 11284 bytes,
SHA-256 `c272eabf4d5efcd2d0f8075d68b010ec00a48e824bdec81e563f6402a7568e0b`;
five-record freeze SHA-256
`f9708bcba4de2c877420e162336a8a8775c3a72e30c98eb2b03fef7e540e6a19`.
I read the complete candidate and freeze, the complete accepted
orientation-charts exposition and its acceptance statement, the full
accepted marked-dictionary exposition, and the official local statement.

The substantive imported result is OC1–OC3 in
`proofs/reviewed-orientation-charts-v1.1.md`, SHA-256
`d15ed547defaffc617ffc6faf6df683c8473ecd9077be63e52d02bbb4edb4ca8`.
It is accepted for finite tangent-dependent reorientation and exact
full BALANCED marked tiling/lift transformations, including all ranks,
actual global homeomorphisms and uniform fixed-D bilipschitz bounds.
Its determinant bound allows zero row minors. Its D4 stratum corollary
is not substituted for an all-D entropy theorem. No accepted or
candidate rank-mesh, strict, annulus, cutting, local-window or global
assembly result is needed by CW0–CW4.

Fix p and an actual full balanced tiling T, with its canonical lift
a_T in [0,p]^D, V a_T(x)=x, and standard original vectors. The
matrix J and offset c are fixed across the local family, with VJ=I
and Vc=0. A valid OC1 cut is selected for this J and remains fixed
across that family. Different windows may use different cuts only
in CW4's separate construction from one fixed actual reference.

## CW0: translations, signs and the common affine offset

Let S be the signed permutation and sigma the permuted flipped-prefix
indicator. Then V'S=V and

    p V' sigma=−b0,  b0=p sum_(i<k) v_i.

The formula a'_T(x−b0)=S a_T(x)+p sigma is exactly the OC2
reorientation of the physical polygon translated by −b0. It retains
all ranks; its entries are p−a_i on flipped coordinates, not −a_i
without the content correction. The target direction replacement is
F_T(x)=W a'_T(x−b0), where x is the ORIGINAL physical point.
There is no additional unrecorded translation in this notation.

Substituting a_T(x)=Jx+c+e_T(x) and J'=SJ gives

    a'_T(x−b0)=J'(x−b0)+c'+S e_T(x),
    c'=J'b0+Sc+p sigma.

Since V'J'=I, V'c'=b0+Vc−b0=0. For A=WJ', OC3 supplies
det A>0; its weighted Cauchy–Binet lower bound remains positive
at zero minors, and bounded J gives uniform bounds for A and A^{-1}
over the finite cuts. With b=Wc'−Ab0, direct multiplication yields

    F_T(x)=Ax+b+WS e_T(x).

Setting J*=J'A^{-1} and c*=c'−J*Wc' gives WJ*=I and Wc*=0.
Subtracting J*F_T(x)+c* from the lifted equality gives exactly
(I−J*W)S e_T(x). This verifies both CW0 formulas, their signs and
all constant terms. The same p,J,c,cut give the SAME b,c',c* for
every representative. No corner-dependent offset is chosen. Since
S is an isometry in Euclidean norms, |F_T(x)−Ax−b|<=delta with
delta=||W||E; fixed-D norm conversions cover an original infinity
norm error. These are estimates on the stated source region only.

## CW1: the fixed core and complete target buffer

For Q a nondegenerate closed source parallelogram, the pointwise
estimate immediately gives F_T(Q) contained in P+B_delta, with
P=AQ+b. For y in the strict erosion of P, its distance to every
point Az+b on the affine boundary exceeds delta. The boundary
homotopy Az+b+s(F_T(z)−Az−b) therefore avoids y for all s.
The affine boundary has winding number one, because det A>0 and
y is inside P. Thus F_T(partial Q) also winds once about y.
The accepted full homeomorphism makes that image a Jordan curve
bounding F_T(int Q). Consequently the entire strict eroded set,
not merely selected corners or a nearby boundary, lies inside it.

This uses the error on all of Q (in particular its boundary) and
the exact pointwise boundary correspondence. A bare Hausdorff
comparison of arbitrary Jordan curves would not give this conclusion.
A prescribed target parallelogram PLUS its entire required neighborhood
can be fixed for every T whenever that whole set lies in the stated
strict erosion. The margin hypothesis is an input, not something
deduced from four corner tests. CW0' consequently controls the lift
with one common c* on that complete target buffer.

For y=F_T(x) with x in Q, multiplying y−b=Ax+WS e_T(x)
by A^{-1} proves CW1' with error ||A^{-1}||delta. It is used
only on the actual image. In particular a target tile patch contained
in the common core has its whole reference pullback in the controlled
source region. No claim F_T(Q)=AQ+b or unchanged image shape occurs.
The possibility that Q touches the original polygon boundary does not
invalidate the winding proof: its Euclidean interior is inside the
full polygon interior and the compact chosen core has a strict margin.

## CW2: entire source tiles, the anchor and upper-count injection

A source tile meeting Q0 lies entirely within its d_tile-neighborhood:
choose a point of intersection with Q0 and use the maximum whole-tile
diameter. By hypothesis that entire neighborhood is in Q and has the
same affine estimate. Hence every point of that source tile has image
in A(Q0+B_dtile)+b+B_delta, which is explicitly contained in Pplus.
The chart maps it to one entire target tile. Recording ALL target
tiles meeting Pplus therefore includes all tiles needed to reconstruct
the source restriction. There is no error caused by recording only
target tile interiors or only tiles contained in Pplus.

The union of recorded tiles has a connected edge graph. Indeed every
tile meets the connected convex Pplus, and Pplus is covered by those
tiles, so their union is connected. For a finite tile complex its
one-skeleton is then connected; a vertex-only contact still joins
the edge graph. The prescribed colored increments and one canonical
lift anchor determine the lift at every vertex of that graph. Closed
loops are consistent because the record comes from an actual full
target tiling. One need not assume an arbitrary colored physical
patch has a uniquely normalized canonical lift without an anchor.

The anchor vertex is deterministically chosen from the recorded
geometry; only its height vector is additional information. Its
integer coordinates lie in [0,p]^D for the full balanced target.
There are at most (p+1)^D choices, bounded by
2^{O_D(log(R+2))} when R>=max(2,p). No separate coordinate or
unbounded local translation is concealed in this code.

From that anchored target lift, first apply V' to recover the
reoriented physical positions, then reverse S, the p−a_i corrections,
labels and fixed translation b0. This recovers every represented
original tile, its physical shape and complete fine rank. Filtering
by the known Q0 recovers exactly the requested source restriction.
Some recorded target tiles may correspond to additional source tiles;
that does not affect the filter or injection.

Choosing one full representative of each distinct source restriction
before mapping is legitimate. Two chosen representatives with the
same target record and anchor recover the same source restriction.
There is no requirement that every extension of one source restriction
have the same target restriction. This establishes precisely CW2's
one-sided count bound, rather than an equality of window counts.
The additional whole-buffer assumption for a later theorem remains
explicit and is not supplied by this counting argument alone.

## CW3: exact boundary pullback and fixed fine exterior

Fix one actual full reference T. The target disk Omega is a Jordan
union of its whole target tiles compactly inside F_T(int Q). The
reference chart homeomorphism carries it back to an actual Jordan
union C_T of original whole tiles. Its entire boundary, vertex stars,
colors and heights are inherited; no partial-tile approximation is
made.

Any target filling with the same complete boundary can be glued to
the unchanged full target exterior. The result is an actual full
balanced tiling with the same marked outer polygon. Applying the
exact inverse OC3 and OC2 to this FULL tiling yields an actual
original full tiling. On the unchanged exterior, target lift
increments and the full outer normalization are unchanged. This
exterior is connected: Omega is an interior Jordan disk in a full
convex disk. Its canonical lift is therefore the old one, including
on partial Omega. The inverse physical positions and labels there
are exactly the reference positions and labels.

The complete lifted boundary of Omega consequently pulls back to
exactly partial C_T, with its original fine ranks. The new inverse
homeomorphism places the new fine faces inside that same Jordan
boundary; it cannot overlap the unchanged exterior or take an
excursion outside it. Thus the fine replacement region and its
full exterior are fixed across all choices. Its interior point map
need not agree with the old reference inverse map, and no such
agreement or retained affine approximation is assumed.

The full chart is invertible. Applying it to the reconstructed fine
tiling recovers the chosen target filling. Therefore distinct target
fillings give distinct fine patches. This is the asserted recoverable
injection; no general extension theorem for arbitrary incomplete
source windows has been invoked.

## CW4: exact integer dilation and coexistence of local charts

For the M-by-M uniform subdivision of each enlarged reference tile,
the canonical lift satisfies a_MT(Mx)=M a_T(x) on each face by
affine interpolation, and the formulas agree on shared edges. The
outer normalization is also the scaled normalization. Reorientation
now uses content Mp and translation Mb0. Therefore

    F_MT(Mx)=W[S M a_T(x)+Mp sigma]=M F_T(x)

for every point, not merely lattice vertices or boundary points.
The target preimage of M Omega in the fixed dilated reference is
exactly M C_T. Each boundary edge is replaced by M colored unit
edges with its consecutive fixed ranks, including the reversed
rank order specified by Mp−a_i for flipped colors. There is no
fresh port matching. Applying CW3 at this scale inserts EVERY
complete-boundary target filling of M Omega into that exact fixed
fine dilation and leaves the same scaled fine exterior.

For finitely many source windows with disjoint interiors, each compact
pullback C_alpha lies strictly inside its own source window. The
pullbacks are therefore disjoint, even if window boundaries touch.
This remains true after dilation. Each local chart is applied to
the SAME original reference T, and CW3 returns a fine patch matching
its inherited complete boundary. Such fine patches can be glued to
T, or their dilates to MT, independently along these disjoint fixed
boundaries. Each result is an actual tiling in the original plane.

Restriction to each fixed fine patch recovers that local choice;
its fixed boundary lift allows its forward local chart to recover
the corresponding target patch. Distinct tuples yield distinct
tilings. The global chart maps need not commute, because they are
not the maps being simultaneously glued: their fine outputs are.
Choosing different global reference representatives for different
local code classes would lose this proof, and the candidate explicitly
prohibits that step without first fixing a common representative.

## Adversarial cases and disposition

I tried to break the signs by omitting b0 or the p sigma term;
both exact corrections are required and present. I checked zero
minors, strict erosion endpoints, source tiles touching Q0 only at
a vertex, target records joined only at a vertex, anchor ambiguity,
multiple full extensions of one source restriction, a changing inverse
map inside the new patch, exterior height normalization, M-subdivision
rank reversal, touching source-window boundaries and noncommuting
charts. The preceding reconstruction resolves these cases under the
written hypotheses. In particular fixed target-window existence and
full buffers are conditional on explicit margins, while shape equality
and preservation of the new interior affine estimate are not claimed.

All 24 claim-level checks in the separate ledger pass. No author
repair is requested. The result remains candidate-unverified pending
the other fresh whole audit and coordinator reconciliation; this report
does not promote it. Only geometric/coding interfaces are established.
Selection and coding of global windows, entropy inputs and the order
of global parameters remain separate obligations. The integrity freeze
also confirms preservation of all 30 older own packets.
