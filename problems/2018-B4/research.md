# 2018 B4 research log

Status as of 2026-10-16: **proved, independently reviewed** for all positive \(m,n\), reproducing a published formula. No novel full solution is claimed. Candidate v1.0 is preserved unchanged under proofs/; two fresh blind audits, both with complete reconstruction and exact falsification checks, found no substantive gap. The coordinator integrated them in reviews/acceptance.md. Author review requests later in this initial log are retained as history and have now been completed.

Requested worker settings: `model=gpt-6.1-sol`, `reasoning_effort=max`. Independent effective-setting readback was not available, so these are requested settings only. The coordinator monitors the shared weekly telemetry and reserves review/integration capacity. No separately billed API was used.

## Statement checks

The cached official paper's page 2 was rendered and inspected visually. The problem is exactly the stated two-row, weak-row, strict-column, equal-content problem, for every positive integral \(m,n\). In particular \(m=1\) is not excluded. No additional notion of acceptable explicit expression appears in the wording. `statement.md` records hashes, sources and the distinction between the general authorized target and the known \(m=5\) comparison.

## Approaches and results

### A. Tableaux and the two-row determinant

The objects are semistandard tableaux with shape \((mn,mn)\) and weight \((2n)^m\), hence their number is the Kostka number \(K_{(mn,mn),(2n)^m}\). The two-row Jacobi-Trudi expression is \(h_{mn}^2-h_{mn+1}h_{mn-1}\). Taking the equal-content coefficient reduces the count to the difference of two adjacent coefficients of \((1+x+\cdots+x^{2n})^m\).

This is a standard method, not a new theorem. A bare Kostka label or coefficient expression would not by itself be presented as a research resolution. Expanding the bounded-composition generating function does, however, give a finite sum of ordinary binomial coefficients with a number of terms depending only on \(m\). The author independently derived that sum before locating its direct prior publication.

### B. Elementary first-failure reflection

To remove reliance on external symmetric-function theorems, the author constructed the content-preserving reflection described in `proof.md`: from the first non-strict column, exchange suitable row pieces and obtain arbitrary weakly increasing rows of lengths \(mn+1\) and \(mn-1\). The explicit inverse chooses the first index where the shorter row's entry is at least the longer row's entry, using the last index as a default. Endpoint cases are written out.

This supplies a proposed self-contained proof of the central coefficient difference and then of
\[
F(1,n)=0,\qquad
F(m,n)=\sum_{j=0}^{\lfloor(m-1)/2\rfloor}(-1)^j\binom mj
\binom{(m-2j)n+m-j-2}{m-2}\quad(m\ge2).
\]
The upper binomial arguments are nonnegative throughout the fixed range; negative-exponent contributions are represented by ordinary zero binomial coefficients. This convention matters especially when \(n\) is small and \(m\) is large.

### C. Ballot inequalities and exact dynamic programming

Let \(a_k\) be the count of symbol \(k\) in the top row and \(S_k=a_1+\cdots+a_k\). With \(S_0=0\), the exact strict-column criterion is
\[
0\le a_k\le2n,\quad S_m=mn,\quad S_{k-1}+S_k\ge2nk\quad(1\le k\le m).
\]
Necessity: every bottom entry at most \(k\) needs a top entry less than \(k\); their counts are \(2nk-S_k\) and \(S_{k-1}\). Sufficiency: for a bottom entry \(k\) at column \(j\), we have \(j\le2nk-S_k\le S_{k-1}\), so the top entry there is less than \(k\). Thus no equality case is lost. The endpoint inequalities force \(a_1=2n\) and \(a_m=0\).

The script uses this criterion in a dynamic program with state \(S_k\), separately from the composition convolution and formula. It can also be viewed as counting lattice points in a polytope scaled by \(n\). For \(m\ge3\), after removing the forced endpoint variables and the sum equation, the expected dimension is \(m-3\); the choice \(a_2=\cdots=a_{m-1}=n\) has strict slack in the remaining inequalities. A claim of Ehrhart polynomiality based only on dimension would be insufficient without an integral-vertex argument. The explicit sum already proves polynomiality, so no unverified integrality theorem is needed.

### D. Representation/integral route

The same count is the multiplicity of the trivial representation in a tensor product of \(m\) spin-\(n\) representations of \(SU(2)\). Primary papers listed in `references.md` give integral and coefficient-difference formulas for this multiplicity. This route confirmed the count's place in standard literature and provided a published numerical table. It was not needed for the elementary proof and was not pursued into asymptotic analysis, since the authorized target is exact enumeration.

### E. Literature status and exact obstruction to an originality claim

Hering-Howard Proposition 3.2 (2014) directly states the needed two-row Kostka subset sum; grouping subsets of equal size gives the proposed binomial formula. Ottaviani Theorem 40 (2013) records the same equal-weight expression and attributes it to Howe (1988). The candidate consequently has **no claimed mathematical novelty**. It answers the literal general counting request if independently validated, while the historical reason for the competition's open label is unresolved.

Hering-Howard also discuss the separate desire for formulas with positive coefficients. That is not in B4's official wording. Expanding the candidate for \(m\le10\) gives positive rational coefficients, but that observation is finite evidence and is not a proof of positivity for all \(m\), nor is positivity being substituted as this project's target.

### F. Checks completed and non-results

`computations/exact_count.py` uses only Python's standard library. All counts and polynomial arithmetic are exact. The preserved output shows agreement of the formula, prefix-inequality dynamic program and bounded-composition convolution in 400 cases \(1\le m,n\le20\). Direct row construction and both directions of the reflection map were exhaustively checked in 21 cases \(1\le m\le7,1\le n\le3\), covering 81,135 bad row pairs. The official \(m=5\) formula agrees for \(1\le n\le100\). These checks are evidence only.

No unmonitored large search was launched. No run was abandoned or timed out. No A1-A4 or B1-B3 was investigated. The apparent "open problem" was not treated as permission to claim a new discovery after finding a standard formula.

## Next steps

1. Coordinator freezes v1.0/hash, then commissions two fresh adversarial reviewers with blind initial reports; one reconstructs every step.
2. Ask reviewers to audit the exact official statement, reflection junctions and inverse, binomial zero conventions, \(m=1,2\), \(n=1\), the optional polynomial corollary and primary-source specialization.
3. If needed, the author repairs only affected arguments and records a new version; reviewers recheck those repairs.
4. Preserve the historical discrepancy without inventing a stricter open problem. A further authoritative clarification could explain the intended target, but it is not necessary to verify the literal count formula.
