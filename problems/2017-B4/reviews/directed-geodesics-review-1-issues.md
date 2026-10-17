# Directed-geodesics whole audit 1: initial issue ledger

2026-10-17 UTC. Initial blind ledger, jointly frozen with the complete report
and source checks. No peer directed-geodesics conclusions were read.

## Substantive issues

None found in DG1 or the explicit DG2 estimate under the intended
two-dimensional marked-tiling hypotheses. This is a review conclusion rather
than coordinator acceptance or a claim of absolute certainty.

## DG-R1-N1: make disk domain and lift normalization explicit

- Classification: nonblocking precision clarification.
- Candidate locations: lines 26--32, 42--46, and 64--65.
- Observation: the radial proof chooses an interior point of \(Z\), and the
  initial-segment sizes are literally \(a_i\) only for the conventional
  normalization \(a(0)=0\).
- Intended sufficient hypotheses: nonnegative integer \(m_i\), at least two
  active directions, a genuine edge-to-edge two-dimensional tiling, and the
  marked lift normalized at \(0\).
- Boundary challenge: one active direction gives a segment with no interior
  point. Zero colors are otherwise harmless. An integer kernel translation
  of the lift changes the literal size assertion but changes neither lift
  differences nor DG1's conclusion.
- Recommended author action: state the domain and normalization in one
  sentence. A one-dimensional extension, if desired, needs a separate
  elementary sentence rather than the radial construction.
- Current disposition: clarification recommended; no mathematical
  counterexample in the stated disk setting; author owns any edit.

## DG-R1-N2: expose asymptotic constants and the joint scale threshold

- Classification: nonblocking quantifier clarification.
- Candidate locations: lines 100--107.
- Observation: the exact inequality at lines 91--96 is valid. Its
  square-root application fixes more data than the compact subscript
  \(O_{D,J}\) displays: the positive margin \(\kappa\), upper bound \(K\),
  direction \(u\), and the original affine-error constant are fixed.
- Sufficient explicit version: for \(0<\varepsilon\leq1\), let
  \(E\leq C\varepsilon L+C_0\), choose
  \(A\geq\max\{1,4C/\kappa\}\), set
  \(\ell=A\sqrt\varepsilon L\), and require
  \(L\geq4C_0/(\kappa A\sqrt\varepsilon)\).
  Then \(\kappa\ell\geq2E\) and the asserted band is a fixed constant
  times \(\sqrt\varepsilon L\).
- Buffer scope: the entire target segment must have that buffer from the
  complement of a prescribed region. An endpoint-only margin is
  insufficient for an arbitrary region.
- Boundary challenge: there is no uniform extension as \(\kappa\downarrow0\)
  in this proof. When the sampling term is nonzero, the required scale
  grows as \(\varepsilon\downarrow0\). The choice \(\varepsilon=0\)
  requires separate treatment of sampling.
- Recommended author action: display the fixed-data dependence and one
  sufficient joint threshold. The candidate already excludes zero-margin
  strata and states that an adequate buffer is needed.
- Current disposition: clarification recommended; no counterexample to the
  exact DG2 claim; author owns any edit.

## Audited challenges that did not become issues

The primary theorem permits disjoint curves. Radial rays do not cross or create
an exterior shortcut. Boundary endpoint intervals contain exactly one tiling
vertex, including collinear subdivision vertices. The color-threshold argument
identifies signs with lift ranks; graph distance then implies positive
orientation. Edge interiors satisfy the same DG2 bound. Equality in the mesh
condition and a zero-length sampled path are valid boundary cases.

No annulus, entropy-recovery, profile-mixing, or full-exponent inference has been
accepted here. Those stronger conclusions are expressly absent from the
candidate, rather than an outstanding defect in a claimed proof.
