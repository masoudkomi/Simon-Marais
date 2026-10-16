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
