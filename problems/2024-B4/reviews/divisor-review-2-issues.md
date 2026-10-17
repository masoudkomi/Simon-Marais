# Fixed phi7/phi11 criteria: initial blind issue ledger 2

2026-10-17 UTC. No peer divisor report, issue ledger or conclusion
was read before this ledger and the full whole audit were frozen.

## Substantive issues

None found. The complete proof and necessary finite certificate
were independently reconstructed. This is a reviewer conclusion,
not coordinator promotion or an absolute-certainty claim.

## Attack ledger

| ID | Attack point | Initial disposition |
|---|---|---|
| DIV2-01 | General \(T/(G)\) need not be a domain | \(G\) is irreducible in the polynomial UFD, hence prime; its quotient embeds in its fraction field. |
| DIV2-02 | Repeated/zero recurrence roots or \(0^0\) may invalidate the source application | Shift-product annihilation is valid with multiplicity; the zero-root sequence \(1,0,0,\ldots\) is annihilated by the shift. Derksen does not impose nondegeneracy at input. |
| DIV2-03 | Automaticity/effectiveness may require an unavailable hypothesis | The explicit function field is finitely generated over \(\mathbb F_2\), and recurrence/initial values are effective. The original Theorems 1.10/4.14 apply. |
| DIV2-04 | Invariant generating recurrence or \(P_2,P_4\) may have wrong terms | Even-part extraction from \(E/E^2\) and direct coefficient comparison give the displayed polynomials. |
| DIV2-05 | Leading determinant 4 vanishes in characteristic two | It is an integer exponent determinant; image leading monomials are distinct over the integer exponent lattice. |
| DIV2-06 | Actual divisibility may fail to descend | Squared monic quartics make \(T\) integral over embedded normal \(S\); the actual quotient lies in \(\operatorname{Frac}(S)\), hence in \(S\). |
| DIV2-07 | A divisor may be composite or vanish on localization | \(A_2\) is linear prime; \(A_4\) is primitive linear in \(u\), irreducible and prime; neither divides \(q\). |
| DIV2-08 | The \(q=0\) locus may hide an extra whole divisibility | Clearing powers of \(q\) and prime saturation contract the ideal exactly; both localized quotient isomorphisms are explicit. |
| DIV2-09 | Parameter specialization may lose polynomial information | The normalized parameter \(b\) remains transcendental in \(\mathbb F_2[q,q^{-1},b]\); no finite evaluation is used. |
| DIV2-10 | The C7 witness may omit high \(v_2(m)\) or small endpoints | The unrestricted \(m=2^vs\) construction works for every \(v\geq1,s\) odd, including \(v=1\); \(m=0\) gives exactly the sole zero \(j=2\). |
| DIV2-11 | C7 coefficient cancellation across parameter powers | Each selected \(b^k\) occurs in exactly its own summand; the explicit coefficient is one. |
| DIV2-12 | Cartier maps may leave the 12-dimensional space | Product exponents are \(z\leq7,b\leq4\); each section returns \(z\leq3,b\leq2\). No negative exponents occur. |
| DIV2-13 | The two parameter sections may be wrongly treated as alternatives | Even/odd parameter supports are disjoint; vanishing is a conjunction, represented by the span of both section images. |
| DIV2-14 | A correct-looking table may conceal a false transition | Independent six-shift maps, Gaussian normal forms and complete finite vector sets checked all 48 columns, all 15 subspaces and all 30 equalities. |
| DIV2-15 | Output mask may ignore a nonconstant parameter term | \(K(0,b)=1\); all three constant-\(z\) bits 0--2 are checked on every vector. |
| DIV2-16 | Quotient language, digit order or leading zeros may be wrong | Every state output and successor class checks; the exact LSB language is \(0010^*\), hence index four only, with empty word rejecting. |
| DIV2-17 | Source irreducibility may be only affine or APN nonexceptionality | Original affine definition and theorem hypotheses checked; nonzero \(z=0\) specialization preserves degree and excludes a lost \(z\) component. |
| DIV2-18 | Extension fields may introduce a fixed whole divisibility absent over \(\mathbb F_2\) | Scalar extension of \(T/(G)\) is faithful on the underlying \(\mathbb F_2\)-vector space. Absolute irreducibility then gives the common-component gcd conclusion. |
| DIV2-19 | Finite sums may cancel different homogeneous components | The degrees \(n-3\) are distinct and nonzero; homogeneous principal ideals are graded. Zero/empty sums satisfy the vacuous condition. |
| DIV2-20 | \(n=1,3\) or self cases may be miscounted as reducible | \(n=1\) has zero numerator and is impossible with nonconstant factors in a domain; \(\phi_3=1\); self cofactors at 7 and 11 are units. |
| DIV2-21 | Older scans or unpublished priority may be an unspoken premise | Neither scan nor unverified structural result is needed; general automaticity and irreducibility are attributed, and novelty/exhaustive literature absence are unclaimed. |

## Exact finite job

Reviewer child PID 77847, external timeout five seconds, return code zero,
elapsed 0.04090591595740989 seconds including launch; completed and reaped.
All checkpoints, complete certificate output, source code, immutable job
record and completion record are preserved under divisor-review-2-.

No larger BFS, index scan, routine tests, native CAS, source-paper
redistribution, candidate repair or Git operation was performed.
