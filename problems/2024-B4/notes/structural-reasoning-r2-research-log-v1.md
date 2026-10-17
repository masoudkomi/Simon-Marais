# Structural reasoning log: 2024 B4(b)

2026-10-16 UTC. All new deductions are **candidate proof - unverified**.
Requested gpt-6.1-sol/max; independent effective readback unavailable.
Only this task's `structural-reasoning-r2-*` notes and ignored source
cache artifacts were written. The frozen J15 review remains unchanged.

## Mathematical work retained

1. Reconstructed the Kasami specialization and coefficient-field premise
   from the full 2016 coauthor preprint. Original JW1993 remains
   inaccessible in full through the normal public routes inspected.
2. Identified a false parity implication in the later 2016 argument that
   every symmetric factor passes (1,1). An explicit symmetric-polynomial
   counterexample is in the source audit. This is a proof-inference
   objection, not a counterexample to the separately stated factorization.
3. Derived the ordinary tangent cone at P directly from
   (1+T)^(2^i ell+1), and the field degree of each absolute component
   from each uniquely assigned tangent line. This became T3.
4. Tried to use that observation for new whole-polynomial exclusions.
   If phi_n were F2-irreducible, its absolute orbit length would divide
   every d>1 dividing i, and hence would be either one or the prime p
   when i=p^a; mixed-prime i forces one. Coordinate symmetry further
   excludes the p=3 possibility, since its 3-cycles fix components but
   would require their tangent multiplicity to be divisible by three.
   The ordinary F4 point also excludes odd p when 3 does not divide n.
   These are useful elementary checks, but the global consequences
   outside the known exceptional families are subsumed by the published
   Hernando–McGuire F2-component theorem. They were not promoted as new
   exponent progress and were not used to substitute APN classification
   for polynomial reducibility.
5. Kept the individual-factor statement and analyzed the six tangent
   directions for i=3. Their two irreducible cubic cones and the action
   of coordinate permutations force the exact T4 trichotomy, including
   equal factor degrees and exclusion of a mixed absolute/norm pair.
6. Sought a low-degree obstruction independent of that global theorem.
   Substituting a general line into f_n and comparing the binary-supported
   coefficients j=1 and j=1+2^s excludes every extra line when the binary
   weight is at least three. The only original numerator lines are simple
   prescribed diagonals. This became T1.
7. Avoided a genus/Hasse bound for degree-three factors by classifying
   point-free F2 cubics through an exact count: eight coefficient choices
   and eight F8 norm forms. Combined with the F2-point pattern and the
   ordinary tangent cone, this proves the proposed factor-degree lower
   bound four, T2. This uses no enumeration program.

## Approaches deliberately not treated as conclusions

- Absolute splitting does not alone give an F2 factorization. The
  coefficient field and Frobenius orbit must be checked.
- The local point P need not lie on every global factor. Factors avoiding
  P remain an essential unresolved possibility, as the phi13 examples
  already illustrate.
- A conditional orbit-product argument is not an exponent classification.
- The 2014 Férard abstract is not a complete theorem premise. The newly
  exposed public citation-PDF URL returned no bytes; that did not remove
  the access gap.
- A speculative extension of the phi13 exponent family to larger Kasami
  divisors has no established identity in this work. No finite check or
  theorem claim was made for it.

## Exact source/inspection operations and outcomes

- Normal web searches retained in the source JSON located the existing
  full coauthor preprint and an institutional proceedings URL; the latter
  returned 404 on HTTPS and was unavailable on HTTP. Springer remained
  subscription preview, and Caltech original-chapter metadata had no file.
- The first sandboxed publisher HTML request failed with DNS resolution.
  It was retried with the required escalation and succeeded. Its output
  identified the public citation-PDF URL recorded in the source JSON.
- That exact public PDF request exited zero but produced zero bytes.
  It is not a downloaded paper and is retained as a failed attempt.
- Two read-only attempts to render the existing 2016 page through PyMuPDF
  failed because `fitz` was absent in both the project and bundled Python.
  No package was installed. The bundled Poppler renderer then succeeded:

    /Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm -f 7 -l 7 -singlefile -scale-to 1600 -png .cache/literature/deep-literature-r2/2024-delgado-janwa-1612.05997v1.pdf .cache/literature/structural-reasoning-r2-delgado-janwa-page7

  Exit zero, about 0.109 seconds; the whole page was visually inspected.
- Existing thesis PNGs were read directly. No mathematical search,
  polynomial factorization command, CAS, paid API, process cleanup or
  broad enumeration was run.

At 2026-10-16 22:17:15 UTC, authoritative account-wide weekly telemetry
reported 18% total used, 10080-minute window, reset 1792745187. The
90% total-used cutoff and integration/review reserve remain in force.
No Git, shared status, other-year proof or existing note was edited.
