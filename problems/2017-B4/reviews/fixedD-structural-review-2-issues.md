# Fixed-D structural review 2: blind initial issue ledger

2026-10-17 UTC. Frozen before reading any peer fixed-D structural report, issue ledger, or conclusion. Both candidate hashes are in the joint report and freeze manifest.

## FD2-01: substantive qualification required

Affected location: profile-reduction-v1.md, Section 4, lines 163--169.

Claim challenged: nearby vector-height boundary words with fixed color counts admit uniform weak-order padding within \(O_D(\epsilon L)\), with \(O_D(\epsilon L^2)\) area.

Exact counterexample, \(D=3,M\ge2,L=3M\):

\[
w_0=1^M2_1 3^M2_2\cdots2_M,\quad
w_A=2_1 1^M3^M2_2\cdots2_M,\quad
w_B=1^M3^M2_1 2_2\cdots2_M.
\]

All counts equal M. Every prefix color-count coordinate differs from the reference by at most one; the physical y-error is at most one. The exact join is \(3^M2_1 1^M2_2\cdots2_M\), because the inversions \(1_a>2_1\) and \(2_1>3_c\) force all \(1_a>3_c\). Its prefix-M vector error is M, physical y-error \(2M\), and its added band area is \(2M^2+2M\). Taking \(\epsilon=1/L\) contradicts both claimed bounds under the height-only hypothesis. Equally, for fixed epsilon these examples occur at arbitrarily large L and retain a join excursion \(L/3\), so a D-only constant times epsilon cannot control them uniformly as epsilon tends to zero.

The structural labelled-envelope lemma is not contradicted: the rank \(2_1\) moves M positions. The periodic bounded-gap conversion is also not contradicted, but its constant depends on gap bound G.

Required author action: explicitly retain a ranked-label displacement assumption, or a fixed periodic reference with bounded gaps and G-dependent constants. Do not assert a D-only consequence for arbitrary height-close words or for degenerating slope strata. Proof author handles the repair. Status: **open, substantive scope correction; do not promote this consequence unchanged**.

This is not a counterexample to (H), the full EAI program, or the structural weak-order theorem.

## Other substantive attack points

| ID | Location | Attack point | Initial disposition |
|---|---|---|---|
| FD2-02 | Structural Section 1 | Integer deformation may add non-simple arcs or change the marked count | Closed by reconstruction. Strict \(\ell_i\) monotonicity excludes closed arcs; fixed intersection sign and alternating endpoints force one crossing per ranked pair. Swap shellings and crossing orders preserve the commutation class and frame. |
| FD2-03 | Structural Sections 1--2 | Primitive edges, local records, or boundary cut cells may introduce extra packings | Closed. Integer x-displacement one excludes interior integer subdivision; nonoverlap and face incidence remain local constraints. Boundary data are prescribed, not discarded. |
| FD2-04 | Structural Section 2 | Lift may depend on a path; compactness may lose boundary or minor constraints | Closed. Tile boundaries and simple connectivity define the lift. Uniform gradient bounds and the distribution determinant identity pass all ordered minor signs to uniform limits. |
| FD2-05 | Structural Section 2 | K may be unbounded despite bounded minors; integral identities may be lost | Closed. Cauchy--Binet plus the displayed row identity bounds every entry. Each ij tile contributes one to its minor integral; common trace/cutoffs preserve the identity. |
| FD2-06 | Structural Section 3 | Wrong tile origins, overlap, average gradient, or unit-octagon coordinates | Closed. Both reversal sequences and origins check; the exact common interior points and all four regular coefficients check. The negative minor is \(-1/4\) in the integer case and has the stated general sign. |
| FD2-07 | Structural Section 4 | The union-closure may fail coclosure or leave the shuffle interval | Closed. The path-straddling proof gives coclosure. Every edge increases color, so no same-color inversion appears and chains have at most \(D-1\) edges. |
| FD2-08 | Structural Section 4 | The \(2(D-1)r\) displacement bound or meet duality may fail | Closed. New U-edges span at most \(2r\) in reference positions; old edges decrease position. D-bounded closure chains control new comparisons; reversal/rank renaming is antitone and preserves displacement. |
| FD2-09 | Structural Section 5 | Padding injectivity or recording varying boundaries may cost factorial factors | Closed under the labelled/gap hypotheses. Fixed boundaries recover by restriction. A color word of length \(O(L)\) has \(O_D(L)\) bits; ranks introduce no extra choices. Height-only extension is the distinct open issue FD2-01. |
| FD2-10 | Structural Section 6 | Zero rows, parallel/antiparallel rows, coincident grids, or triples | Closed. Omit zero rows, choose generic phases, use rank two for bounded cells. Only nonparallel pairs produce faces and then their minors are positive. |
| FD2-11 | Structural Section 6 | Degree one plus positive faces may still permit edge/vertex self-identification | Closed by explicit local reconstruction. Positive adjacent sectors make the map open at edges/vertices; a self-identification would yield two preimages of a nearby regular value, contradicting degree one. |
| FD2-12 | Structural Section 6 | Rationality and periodicity may fail on boundary strata | Closed for the local plane construction. Clearing denominators gives periods; \(VJP=P\). This does not prove fixed-frame recovery. |
| FD2-13 | Structural Section 6 | Gaussian-type perturbation may have the wrong minor sign | Closed. Off-diagonal exponent exceeds diagonal exponent by \(2(j-i)(\ell-k)>0\); Cauchy--Binet gives strict minors, and positive-determinant right normalization preserves them. |
| FD2-14 | Profile Section 1 | Compact profile identity may imply an invalid all-scale lower bound | Closed for P1 only. Upper semicontinuity and finite-cover counting prove the maximum identity. PR is an additional sufficient property, not established or equated with (H). |
| FD2-15 | Profile Sections 1--2 | Abstract oscillation example or skeleton entropy estimate may fail | Closed. The derivative is positive, logarithmic increments are \(O(p)\), and integer phases approach both extrema. Fixed-mesh skeleton cost is subquadratic; it supplies upper fibers only. |
| FD2-16 | Source theorem use | Free-window/SFT theorem may silently fill the prescribed polygon | Closed. Primary definitions and Theorems A--B checked; the candidate explicitly does not assume the required uniform filling or boundary transfer. |

## Open program obligations, not repaired theorems

EAI and its all-scale application remain unproved and are correctly labelled as a program. A formal recovery theorem would still require compatible corner offsets, color ranks, fixed phases and boundary selection, uniform scales/losses, zero-density and parallel-row strata, and all-scale transfer to the original full frame. These are not closed by the present audit or by the valid P1 identity. No exact 2017 exponent follows.
