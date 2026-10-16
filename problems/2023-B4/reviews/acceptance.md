# Coordinator acceptance: 2023 B4(b)

Date: 2026-10-16. Status: **proved, independently reviewed**.

For each fixed nonsquare positive integer N, the full classification is all diagonal pairs and (d,2d),(2d,d) for positive odd d. The proof uses the explicitly attributed official preliminary restrictions, then excludes every remaining coprime even/odd exponent pair by a general resultant/denominator argument and a real inequality. The preliminary part (a) has not been re-solved or reproduced. Novelty and prior-publication status are not established; see notes/coordinator-literature-audit.md.

Both fresh independent agents audited the same frozen constructor v0.1, SHA-256 `77d209d6a35ebf96a72d5d3a29f9f23d8f7456adae01d1572c180cf842c05365`. Neither constructed the proof; both initial reports were completed blind to the other's conclusions. Each independently reconstructed the entire argument, checked original official domains and published inputs, and attacked degree drops, all resultant identities, arithmetic branches, signs, denominators and sufficiency. Neither found a substantive mathematical gap. Both suggested only optional exposition expansions, supplied in their reports. No mathematical repair or re-review was required.

- [R1 report](review-1.md), SHA-256 `26688996c215bf7980b51f30abf854006038e0c694a18ed60227021f3e52d3b9`: full reconstruction; separate standard-library Sylvester evidence and 138,369 bounded modular cases.
- [R2 report](review-2.md), SHA-256 `85b2ed3916eca1b25b0867e854a81978bb4a62305e0fde428b449d5d1ce739a3`: full reconstruction; independent CAS checks, degree-specialization tests, and 4,278 bounded integer cases.

The coordinator read both full reports, verified their hashes and the frozen candidate hash, checked their acceptance conditions and issue disposition, and reproduced the constructor's saved computation with exact stdout equality and no stderr. Computations supplement the unrestricted argument; neither agreement nor finite tests are its proof.

The accepted copy proofs/reviewed-v1.md changes only status annotations and the audit-trail heading from the frozen draft; its mathematical argument is unchanged. Issue rows C01-C03 are closed. L01 remains an attribution/novelty question, not an unresolved mathematical gap. Acceptance makes no absolute-certainty or priority claim.
