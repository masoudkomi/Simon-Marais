# Annulus A1--A5: initial blind issue ledger 2

2026-10-17 UTC. No peer annulus report, issue ledger or conclusion
was read before the complete report and this ledger were frozen.

## Substantive issues

None found in the explicit A1--A5 statements under their hypotheses.
This is a reviewer conclusion; it is not coordinator promotion or an
absolute-certainty claim.

## ANN2-N1: explain vertex separation versus strict containment

- Classification: nonblocking proof-detail clarification.
- Location: A3, lines 169--175, invoking A2.
- Question tested: A2 assumes strict physical nesting, while A3 states
  containment and a positive distance for boundary vertices. Could an
  inner edge contact the outer boundary between its vertices?
- Resolution: all boundary vertices have integral first coordinate and
  all edges have horizontal displacement one. On an interval
  \((n,n+1)\) both boundaries are straight. A contact of
  nonparallel edges crosses the boundary and violates containment;
  collinear contact makes the unit edge and its endpoints common,
  violating positive vertex distance. Integral-abscissa contacts are
  vertex contacts. Thus strict nesting follows in this exact model.
- Recommended author action: add this short justification, or simply
  retain strict physical containment explicitly in A3.
- Status: reconstructed and nonblocking; no counterexample.

## ANN2-N2: keep the conditional transfer hypotheses in the summary

- Classification: nonblocking scope clarification.
- Location: summary after A5, lines 345--350.
- Observation: “any family of near-flat lens patches” is correctly
  conditional on A2--A4: actual two-path lenses, fixed common slope and
  affine offset, compatible integer frame, physical containment and
  the quantitative buffer. Rational frame choices are fixed.
- What is not proved: constructing a thin surrounding canonical frame
  around an arbitrary shaped lens, extracting a lens from a general
  cut window, uniformity near a zero minor, or transfer with an
  arbitrary independently prescribed offset at each corner.
- Recommended author action: add “satisfying the above nesting,
  common-affine and buffer hypotheses” to the summary.
- Status: nonblocking; the formal claims and remaining-interface section
  already keep those restrictions.

## Complete attack ledger

| ID | Claim attacked | Initial disposition |
|---|---|---|
| ANN2-01 | Comparable words may lack a positive swap chain | Reconstructed first-difference algorithm; all crossed labels are smaller, and same-color ranks never cross. |
| ANN2-02 | Abstract shellings may fold or overlap | Closed by pointwise increasing physical paths; newly swept regions are above the previous path and have disjoint interiors. Primitive integral edges exclude T-junctions. |
| ANN2-03 | Common-comparison poset may have too many extensions | Pairwise forced inversions/noninversions characterize the interval exactly. |
| ANN2-04 | Prefix ideal test or closed two-color range may fail at endpoints | Exact range is \(b_{p_0}(s)\leq h_j\leq b_{q_0}(s+1)\), including both sentinels and missing colors. |
| ANN2-05 | Independent side constraints may miss global corner ranks | All six pair constraints characterize one ideal in one poset; the global ranks and range are fixed. |
| ANN2-06 | Entry/exit seams may penetrate the inner lens | All entry abscissae precede the inner start and all exit abscissae follow its end; their lifts agree exactly. |
| ANN2-07 | Annulus padding may depend on a chosen core filling | Fixed boundary fixes seams and chains; restriction recovers every filling. Varying boundary codes give \(2^{O(L)}\) fibers. |
| ANN2-08 | Winding may fail for self-touching projected loops | Ordered two-color paths have positive weak-lens lobes; shared pieces cancel. The test point avoids the loop throughout the homotopy. |
| ANN2-09 | Singular values or affine offsets may be ignored | Explicit \(\sigma(J)t>\sqrt2(E_0+E_1)\) controls every pair; one common affine offset is used. Constants are slope-dependent. |
| ANN2-10 | Common positive cone may be empty | Strict row-minor signs put all row angles in one ordered interval of width less than \(\pi\); its positive dot-product cone is open and nonempty. |
| ANN2-11 | Digital phases may reverse continuous word order | Shared thresholds are monotone functions of continuous vertical height; the exact two-color gap formula proves every inversion inequality. |
| ANN2-12 | Powers may silently reset phase or corner ranks | Integer height side vectors preserve the one phase on every translated segment. |
| ANN2-13 | Common physical vertices may have distinct lifts | Each swap at a prefix strictly increases its physical height; equality at that prefix forces equality of the full lift. |
| ANN2-14 | End-lobe deletion may discard unbounded entropy | Contacts occur only in two fixed boxes; finitely many integer origins give a uniformly bounded end factor. |
| ANN2-15 | Integer rounding may permit independent corner offsets | One global rounded integer vector fixes every corner; its physical and kernel errors are bounded and included in the buffer. |
| ANN2-16 | Block gluing may overlap or swap same-color labels | Regions are successive monotone bands. Local labels are the canonical next ranks after a fixed prefix, not persistent block labels. |
| ANN2-17 | Remainders may give a subsequence-only entropy result | Mixed-size block comparisons have fixed fillings; \(C_L\geq C_\ell^{\lfloor L/\ell\rfloor^2}\) holds for every integer \(L\). |
| ANN2-18 | Local entropy might be substituted for full (H) | The exact \(C_L\) family is retained and distinguished from the full balanced count; arbitrary cutting and boundary strata remain open. |
| ANN2-19 | Kernel-shift obstruction may contradict A3 | It violates the required growing buffer and global rank range. It is a valid obstruction only to the overstrong assigned-lift version. |

No accepted dependency on the separate DG candidate, free-boundary entropy
theorem, unqualified height-to-displacement bound or convex profile mixing
was found. All substantive repairs, if another audit identifies one, remain
the author's responsibility.
