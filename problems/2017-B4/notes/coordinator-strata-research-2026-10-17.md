# Boundary-stratum ideas for the fixed-D recovery problem

2026-10-17 UTC. **Research leads, unverified; no theorem promoted.**
Coordinator's reasoning sent to the annulus constructor. These ideas do
not establish EAI, profile recovery, (H), or the official limit. Any
substantive lemma would need a frozen proof and two independent audits.

## Orientation charts

Nonnegative ordered minors do not ensure all nonzero J_i have a common
strictly positive direction: the extreme rows may be antiparallel.
For example rank-two rows can have opposite first and last directions.
A possible remedy is to choose a generic physical u, orient each nonzero
row by sign(J_i u), flip its height coordinate and physical edge vector
together, and cyclically reorder colors. The signs should have at most
one cut along the cyclically ordered directions. The transformed physical
edge vectors should still lie in an open halfplane. This is a change of
zonogon root/orientation, not a convex perturbation of a profile.

The exact handling of zero rows, rank offsets and chart boundaries needs
proof. Nothing here licenses applying a positive-margin theorem to a
zero-margin row without a separate argument.

## Parallel-row merging as a possible extraction step

After a valid orientation chart, suppose rows in a consecutive group
satisfy J_i=c_i gamma, c_i>0. Define

    J_group = sum_i J_i,
    v_group = (sum_i c_i v_i)/(sum_i c_i).

Then the formal identity V'J'=VJ=I holds. The new projection differs
from the old one by zero on the exact affine gradient. On an
epsilon L-near affine patch, its position error is therefore
O(epsilon L), up to an absolute lift translation. Distinct projective
row groups should give positive pair minors in the reduced model.

The global tiling interpretation matters. Smoothing two nonconsecutive
colors in an arbitrary isolated reduced word can produce a nonreduced
word: the color pattern ABA and a full three-label reversal give a
double crossing after the equal-color event erases. Thus arbitrary
local smoothing is not automatically a smaller-direction zonogon.

Consecutive physical bundles in a full zonogon are different: the
accepted coarsening projection is reduced globally. One possible local
strategy is to restrict that global projection while recording its
boundary ranks, then use the near-affine projection identity. Whether
the needed local fibers and boundary domains have the right controlled
geometry must be proved.

When a pair minor is small, the number of its pair-type tiles in a
near-affine window should be small after a precise local flux estimate.
If S=O(epsilon L^2) such crossings are deleted, a local version of the
ordered-port injection suggests an entropy cost

    O(h2(epsilon)L^2)+O(L log L),

rather than a factor L per port. Initial boundary labels and colors
need to be recorded at subquadratic cost. This estimate is only a
proposed adaptation: local unmatched ports and the actual projected
window must be specified. No finite word count proves it unrestricted.

## Zero-row deletion

A near-flat zero coordinate has only O(epsilon L) curves crossing the
window if the boundary trace gives the required monotone oscillation
bound. Deleting that family changes O(epsilon L^2) tiles, since each
such curve crosses at most O(L) other curves at fixed D. An insertion
path in the projected tiling graph has bounded degree at fixed D;
encoding O(epsilon L) paths of length O(L), plus boundary ports,
suggests O(epsilon L^2)+O(epsilon L log L) bits.

This is an upper fiber-encoding idea. The number of boundary crossings
and restriction to suitable lens windows must be justified. Arbitrary
wiggly windows cannot be assumed to intersect each curve only twice.

## The insertion gap remains

Even if extraction to a reduced strictly positive model is proved,
an arbitrary replacement core need not accept the original fine
colors and rare crossings. Preserving an old port code does not
guarantee that code remains valid after the coarse arrangement changes.
That would be an invalid sufficiency inference.

A possible repair is to move rare within-group inversions into a
boundary band. Near-flat boundary prefix discrepancies might bound
their rank displacement by O(epsilon L), so the fixed-D weak-order
envelope lemma could supply thin sorting bands. All boundary words,
corner offsets, phase choices and recoverability still need to fit
one construction. A small crossing count alone does not provide a
thin sorting depth: one strand can have a large rank displacement.

The annulus constructor is developing an exact ideal/pairwise-projection
criterion for strictly positive lenses. This note records possible
extensions and their obstructions; it does not assume that criterion
or any future stratum repair is already proved.

