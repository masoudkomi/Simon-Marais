# 2017 B4 issue log

No candidate proof is currently under review. The following are research limitations and counting traps, not objections to an accepted project proof.

| ID | Version / location | Objection | Severity | Repair / evidence | Re-review | Status |
|---|---|---|---|---|---|---|
| 17-01 | statement.md / dictionary | The literal statement does not separately spell out edge-to-edge or symmetry conventions. | Domain fidelity | Official notes identify A006245 and give C(3)=2; fixed-polygon orientation convention recovered. Independent geometric dictionary proof is not supplied. | Required for any new geometric proof | Intended count identified; geometric audit deferred |
| 17-02 | references.md / current status | A negative literature search cannot establish universal absence of a later solution. | Status qualification | 2024 and 2025 primary papers explicitly retain the open problem; targeted 2026 searches found no resolution. Wording is restricted to latest inspected sources. | Recheck on substantial resumption | Acknowledged limitation |
| 17-03 | computations/enumerate_small.py | Reduced words, commutation classes, unmarked arrangements and insertion histories give different counts. | Counting correctness | Full strand-order quotient used; n<=6 complete signature sets cross-checked against one-change patterns; no symmetry quotient. | Any future enumerator change | Finite checks passed; unrestricted dictionary remains attributed |
| 17-04 | computations / n=7 | n=7 was checked only by the one-change predicate, not by exhaustive reduced words. | Computational coverage | Output explicitly says not_run for reduced words; predicate count 24698 matches published data. | Independent algorithm if needed | Honest bounded coverage |
| 17-05 | research.md / convergence approaches | Fekete's lemma at linear normalization does not establish a quadratic entropy limit. | Substantive gap in a tempting approach | No quadratic replication/gluing theorem was found; no candidate proof asserted. | Any later existence argument | Open obstruction |
| 17-06 | literature bounds | Computer-assisted patch/optimization certificates have not been rerun or adversarially audited by this project. | Verification scope | Bounds are attributed to their authors and kept separate from project proofs. | Needed if attempting a self-contained reproduction | Acknowledged limitation |

## Second-pass independent review, 2026-10-16 UTC

Both fresh initially blind full reconstructions support M1-M3, F1-F3 and G1 with stated precision requests. G2 remains unverified: both identify uncovered boundary fourfold crossings left nonsimple by the frozen v1 instructions. The author is preparing new versioned repairs; both reviewers must re-audit affected arguments before acceptance. No improved global bound or official entropy limit is claimed.

| ID | Issue | Disposition |
|---|---|---|
| 2017-SP-G2 | R1-G2-01 / R2-G2-1: fixed local simple resolutions needed at every uncovered multiple crossing before tail completion | Open; author repair active, both re-audits pending |
| 2017-SP-SOURCE | Direct Felsner-Weil Theorems7-8 citation for rank-three signotopes | Both independently verify original author source; citation repair pending |
| 2017-SP-PRECISION | G1 remainder strips, F1 regular neighborhood/empty slots, F3 proper transverse ports and empty case, M2 leaf model | Reconstructed by both; author clarifications and affected checks pending |
