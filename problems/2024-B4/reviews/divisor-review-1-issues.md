# Initial issue ledger: divisor review 1

2026-10-17 UTC. Candidate SHA256
`48d2ca76b3492584b38d8798650e078c7c9771fea97bae8db4d7cd51b21e2fc4`.
Fresh whole nonconstructor audit, blind to the other divisor reviewer through
the initial freeze. **Unresolved substantive issues: 0. Requested repairs: 0.**
The rows below record challenged inferences and their resolution during this
audit, rather than pretend that no adversarial questions arose.

| Check | Potential failure | Resolution in initial audit | State |
|---|---|---|---|
| DR1-01 | Characteristic-two determinant four might vanish, destroying injectivity. | It is an integer exponent determinant; distinct leading exponent vectors are distinct over Z. Largest leading monomial cannot cancel. | Passed |
| DR1-02 | Extra actual divisibility might appear after invariant substitution. | T is integral over the injective normal subring S; the actual quotient belongs to Frac(S), hence to S. This concerns whole divisors only. | Passed |
| DR1-03 | Localization could discard a q=0 component. | Both A_2 and A_4 are prime and avoid q. Clearing a power of q gives exact saturation in S. The two Laurent quotient descriptions are isomorphisms. | Passed |
| DR1-04 | The C7 witness might miss positive even m with arbitrarily large 2-adic valuation. | k=m-2^(v-1) is allowed; the first three coefficients of B are 1,1,0, and t<3*2^v. The selected coefficient is exactly one for every v>=1. | Passed |
| DR1-05 | Different terms in the F7 expansion might cancel the witness in b. | The summand at k has exactly b^k times a series independent of b. Each fixed z coefficient has only finitely many contributing k. | Passed |
| DR1-06 | C11 might treat parameter sections as an existential choice. | The two b parities are disjoint. Vanishing is the conjunction of both sections; linear span retains exactly that condition for every numerator. | Passed |
| DR1-07 | Closure/output data might have been inferred from bounded index scans. | Independent fixed-certificate arithmetic checked 48 actual columns, all 15 entire subspaces and all 30 entire image-space equalities, plus outputs and quotient congruence. No n scan or CAS was run. | Passed |
| DR1-08 | Leading zeros, empty word, or reversed binary direction might add indices. | General invariant uses least significant bit first. All finite accepted words are 0010*, each representing four; empty word and zero strings reject. | Passed |
| DR1-09 | The cited irreducibility theorem might assert only an absolute component or have exceptional small t. | The actual thesis theorem asserts absolute irreducibility for all t>3, t=3 mod4; both7 and11 qualify. Definitions and rehomogenization match. | Passed |
| DR1-10 | A common absolute component could exist despite base-field whole-divisor exclusion. | Each fixed polynomial is absolutely irreducible; whole divisibility descends along a field extension by injectivity of the quotient module. | Passed |
| DR1-11 | Distinct-degree sums might cancel modulo a homogeneous divisor, especially the zero sum. | Its principal ideal is graded. Every distinct homogeneous component must be divisible. The all-zero case has the required vacuous condition. | Passed |
| DR1-12 | Effective recurrence theory might require simple, nondegenerate, or nonzero roots here. | The general statements used have no such restriction. The field is finitely generated and the monic recurrence explicit. Root0 with the prescribed index-zero convention still satisfies its factor. | Passed |
| DR1-13 | General methods or existing irreducibility might be misrepresented as new. | The packet attributes JMW, Derksen and Adamczewski--Bell and states no priority claim. The explicit singleton identification remains separately proved. | Passed |
| DR1-14 | Fixed-divisor exclusions might be presented as a full B4(b) classification. | Scope is expressly limited; self cases have unit cofactor, other factors remain possible, and official n1/n3 are excluded separately. | Passed |

The finite certificate input was copied with its source hash asserted. Its
independent check completed under a ten-second external timeout, child PID
76805, return code0, reaped. All complete vector sets and operator outputs
are frozen with this review. The computation verifies a finite algebraic
certificate for the general invariant; it is not empirical evidence from an
index range.

Recommendation: accept only the stated partial criteria and consequences
after the coordinator has reconciled both fresh blind audits. The reviewer
does not promote the candidate or close the full annual problem.
