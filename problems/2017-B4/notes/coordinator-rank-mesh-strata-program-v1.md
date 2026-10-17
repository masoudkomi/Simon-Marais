# Rank-mesh route for degenerate slopes: research program

2026-10-17 UTC. **Unverified research program, not a proof of H.**
Coordinator's reasoning after the exact OB1 local lifting obstruction.
No published theorem is imported beyond its checked scope. The assertions
below need complete hypotheses and independent audits before promotion.

FL1 in coordinator-stratum-clean-lens-candidate-v1 suggests O(epsilon L^2)
rare tile events for zero row minors in an epsilon-near-affine window.
CL1 gives exact lifting if all within-group events are absent. OB1 shows
that arbitrary replacement after even one such event erases is invalid.

## Use a mesh of selected rank curves, rather than large physical cells

In a full marked arrangement with O(L) curves in each fixed color, select
every r-th curve in each color. The selected arrangement has O_D(L/r)
curves, hence O_D((L/r)^2+L/r+1) cells. Record the tiles crossed by
selected curves: each selected curve crosses O_D(L) others, so this
skeleton costs O_D(L^2/r+L) finite-alphabet bits, before any local
boundary labels.

A cell of the selected arrangement has each canonical rank coordinate
in an interval of length at most r. Any vertex in its dual patch is
therefore physically within O_D(r) of any other, by x=Va. An unselected
proper curve cannot visit the same selected cell twice: leaving it
changes a selected-curve sign, which cannot change back because that
pair crosses at most once. Its intersection with the cell is one arc.

These facts suggest actual disk patches of diameter O_D(r), boundary
length O_D(r), and at most O_D(r^2) tiles, with each residual ranked
strand entering/exiting once. A precise thickening of midpoint-curve
cell boundaries into fixed original tile bands is still needed. Possible
pinches, selected-curve intersections, cells at the original boundary,
rank shifts and degenerate small cells must be included.

If S rare tiles are present, discard every selected cell touching one
of them as well as the mesh skeleton. Each discarded cell has O_D(r^2)
tiles, so the loss would be

    O_D(L^2/r + S r^2 + L).

For S=O(epsilon L^2+L), first fix r and epsilon, then let L grow.
Afterwards take r of order epsilon^(-1/3), giving O(epsilon^(1/3)L^2)
plus lower-order terms. This order is legitimate only after exact cell
and skeleton bounds are proved. It does not rely on global epsilon L
height error giving a microscopic affine approximation in each cell.

This differs from an invalid macroscopic-cell argument: a rare tile in
every large physical box can destroy that argument, but a rank cell
has an r-controlled number of strands and r is fixed before L grows.

## Clean disk lifting may extend CL1 beyond two-path lenses

A good cell has no forbidden within-parallel-group tile and no tile
involving a zero row. Its residual fine curves in any one consecutive
group have no crossing. After global consecutive-bundle coarsening,
the coarse cell is a subpatch of a genuine coarser tiling.

If every residual coarse rank curve has exactly two boundary ports,
the fine color assigned to each such curve should be determined by the
fixed boundary. An arbitrary coarse replacement with that same complete
boundary cannot permute the ports: equal coarse rank means the same
threshold, and two ports leave only one possible pair. Recolor its
tracks using the fine boundary assignments. Each face then uses two
different consecutive groups and has positive fine determinant.
The fine edge-vector sum closes around every tile and the disk is
simply connected, so the fine physical map is defined. If the fixed
fine boundary is Jordan, positivity of every face and degree one should
prove a genuine fine tiling. This is a possible clean-disk lifting
theorem, not yet a proved extension of the two-path CL1.

The boundary-port condition is essential. An arbitrary wiggly window
can meet a threshold curve repeatedly and does not have this property.
Global coarsening can also identify boundary points if removed tiles
were outside the chosen patch. A complete rank-cell construction must
show exactly which boundary is retained to avoid those issues.

Zero rows disappear from a good patch only if all their incident tiles
have been removed. A zero-color edge cannot bound a remaining interior
tile unless that tile also uses that color. This supports deletion
there, but the precise patch boundary and constant rank offsets still
must be fixed.

## The lower-direction entropy theorem that would be needed

For D=4, parallel-group merging reduces a degenerate nonzero slope to
at most three distinct row directions. A route through the known
three-direction lozenge/dimer variational principle might then handle
the good cells. It is NOT sufficient to cite balanced-hexagon MacMahon
counts. One needs an all-boundary, uniform finite-size recovery statement.

A useful precise target UR_s(r) is: for all admissible clean disk
boundaries B of diameter and perimeter <=C r and bounded rank range,
let T(B) be the exact tiling count and delta_M B its integer-dilated
boundary with every colored edge replaced by M same-color unit edges.
Require a uniform error eta_s(r)->0 such that

    liminf_(M->infinity) M^-2 log2 T(delta_M B)
       >= log2 T(B)-eta_s(r) r^2.

This is an additive uniform r^2 error, not an asserted exact
T(delta_M B)>=T(B)^(M^2). Very small-area cells may use their elementary
area entropy bound. There are only O((L/r)^2) rank cells, so the uniform
error would sum to o(L^2). Ragged boundaries, possible pinches and the
chosen port condition must be matched to the actual primary theorem.

For s=3, the original Cohn--Kenyon--Propp variational principle is a
plausible source, but its full hypotheses, boundary class and uniformity
must be checked and any derived compactness/continuity corollary proved.
For general s this is a stronger induction target than the original
balanced-zonogon H_s. Neither UR_s nor that induction is currently proved
by the project.

## Why this could help all-scale insertion

One finite high-entropy family can be conditioned on its skeleton,
bad cells and all paired boundary data. The remaining good-cell choices
are independent exact fibers. Integer dilation of that skeleton gives
a fixed large reference tiling; in each good cell, insert independently
many fine tilings lifted from its <=s direction coarse cell. Restriction
would recover all choices. Losses would be the recorded skeleton/bad
area and UR_s errors. An explicit balanced-zonogon remainder padding
would then be needed for arbitrary target p, not just multiples.

The strict-slope region would use the separately audited CUT/annulus
route; the rank mesh handles only the degenerate part. Orientation
charts for antiparallel extreme rows, consecutive grouping, source
uniformity, actual clean disk construction and the global error budget
are all missing. This note does not close any of them by terminology.
