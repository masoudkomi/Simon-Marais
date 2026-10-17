# Full rank-mesh v1.1 repair ledger

2026-10-17 UTC. **Candidate proof - unverified.** Author repair, not
independent acceptance. Requested gpt-6.1-sol/max; effective readback
unavailable. Both initial whole audits were frozen before their complete
reports, ledgers and source checks were read. This full main-copy repair
requires both original auditors' affected reaudits and coordinator
resolution. All original candidate, supplement and review bytes remain
unchanged.

## Shared substantive issue RMR1-01 / RM2-01

The v1 helper asserted that a rectifiable window of perimeter O(L)
has only O_D(rL+r²) tiles in selected faces touching its boundary.
That literal domain allowed many tiny holes, so the assertion was
false. Connectedness of the window does not repair the assertion;
the single boundary curve is the relevant property. This is a
substantive scope repair, not merely the author's preferred wording.

Both independently supplied exact counterexamples are preserved here.

**R1 counterexample.** Take the D2 full grid with v1=(1,0),v2=(1,1),
N1=N2=L even, r=2. There are Θ(L²) interior selected cells, each
containing a retained odd/odd tile. At an interior point of that tile
remove a closed round disk of radius L^-3, one in every such cell.
For large L the holes are disjoint and avoid the selected curves.
The outer parallelogram has perimeter2L(1+sqrt(2)); total hole
perimeter is Θ(L²)*2πL^-3=O(1/L). The resulting connected window
therefore has perimeter O(L). Every one of the chosen selected faces
touches a hole boundary, so the prescribed operation discards Θ(L²)
residual tiles at fixed r=2, against the claimed O(L). This also
refutes the old lower-order conclusion. Its holes intersect retained
tiles, which the next example deliberately avoids.

**R2 strengthened counterexample.** In the same even-N full grid and
r=2, an interior selected cell in rank coordinates is

    2s-1/2<a1<2s+3/2, 2t-1/2<a2<2t+3/2.

The retained tile is[2s,2s+1]×[2t,2t+1]. Put a physical circular
hole of radius1/(10N) at rank coordinates(2s+5/4,2t+1/2), in a
skeleton tile strictly inside that cell and away from the whole
retained tile. Do this in Θ(N²) interior cells. The holes are disjoint
with fixed positive separation. The window is connected, all those
retained tiles remain fully inside it, and total boundary length is
O(N)+Θ(N²)*2π/(10N)=O(N). But every chosen cell meets the boundary,
so discarding boundary cells still loses Θ(N²) retained tiles rather
than O(2N+4). This rules out repairing the old sentence by counting
only fully contained retained tiles. Both are analytic families, not
enumerated examples or counterexamples to H.

**Versioned repair.** The full v1.1 main copy expressly requires W
to be the bounded interior of one rectifiable Jordan curve of length P.
If a selected face's closure meets that curve, every tile in it lies
within distance C_D r of the curve by RM1. For rho=C_D r, an
arclength mesh of at most ceil(P/rho)+1 centers has radius2rho disks
covering the rho-tube. Its area is O_D(rP+r²). Original tile areas
are at least1, so disjoint interiors give that same tile-count bound.
For P=O(L), at fixed r the loss is lower order than L².

For an actual finite list of such Jordan windows, the v1.1 text keeps
the sum O_D(r ΣP_j+M r²). There is no assertion that the number M
is bounded, or that this total is lower order without checking the
actual scales. It makes no new arbitrary multiply connected-window
theorem and does not import a perimeter bound as a substitute for
this sum. The two counterexamples have many boundary components and
are outside the repaired domain.

## Editorial N1: general-D alphabet

The phrase “six finite tile types” was appropriate for D4 but occurred
inside an RM1a argument stated for general fixed D. The full copy now
says binom(D,2) finite tile types. Its constants were already allowed
to depend on D; no encoding bound or proof changes.

## All affected uses and unchanged supplement

The RM1a single-window paragraph is replaced in full. The RM2 reference
to discarding original outer-boundary faces now explicitly invokes the
full zonogon's one rectifiable Jordan polygon boundary and its
O_D,c(L) perimeter. The final limitations retain the Jordan hypothesis
and the actual r ΣP_j+M r² total. These are all substantive uses of
that helper in the main candidate; the exact diff is saved.

RM1's biconnected disks, the whole-zonogon skeleton/rare-face code,
closed cleanliness and special D4 lifting, zero-row reduction, GE3
exterior construction and component aggregation are unchanged. No
generalized multi-merged-group statement is introduced. The count S
remains an input, and no chart, profile, PR, H or global entropy
assembly is added by this repair.

The full UR3 supplement remains byte-identical at SHA256
40ad9b252b6c34f5dee5c8cd3eedea8e8feeabb0cec1497b224bf5c32ba58aab.
Its GE3 disks are expressly Jordan, and its mesh-boundary loss uses
the one connected boundary of B_j. LC3's limiting triangles and actual
Jordan cores are likewise unaffected. Both initial reviewers found
no independent analytic gap within those hypotheses. That finding
does not authorize the author to promote the packet or remove its
review gate.

No other claim is changed. The complete v1.1 is supplied for both
affected reaudits; this ledger records a proposed repair disposition,
while the original issue records remain frozen and open pending the
reviewers and coordinator.
