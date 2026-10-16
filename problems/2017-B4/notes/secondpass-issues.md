# Second-pass candidate and experiment issue log

All proposed arguments below are **candidate proof - unverified**. No author-created verdict is an independent review, and no result is promoted here.

| ID | Candidate / location | Issue requiring audit | Evidence / author handling | Status |
|---|---|---|---|---|
| SP-M1-1 | MacMahon M1 | Direction of Jensen and the logarithmic singularity at the first unit cell | Convex f_c, integrable corner, mean x+y=i+j-1 stated explicitly; 2600 finite exact integer checks passed | Await two independent audits |
| SP-M1-2 | MacMahon M1 | Symmetric maximization must cover all simplex boundary and mixed concave/convex cases | Boundary identity, at most one coordinate above u at an interior maximum, and one-variable J argument supplied | Await two independent audits |
| SP-M2-1 | Adaptive ternary M2 | Upper bound applies only to the specified tree construction family | Exact telescoping; tree/leaf-choice overhead at most exp(O(n log n)); no global C(n) upper claim | Scope stated; await audits |
| SP-M3-1 | Unequal recursion M3 | Recurrence must hold for all large n, not just a sparse subsequence | This is an explicit hypothesis; floors and padding need an independent geometric injection | Await audits |
| SP-F1-1 | Completion-fiber F1 | Converse must retain the embedded outside graph, designated face and correct port order | Rotation system plus outer circle argument supplied; empty slots and disconnected interiors explicitly flagged | Main topological audit point |
| SP-F1-2 | Completion-fiber F1 | Complete signotope correspondence is an attributed ingredient, not proved from finite matches | Forward completion is described independently; full finite sets from first-pass oracle used only as evidence | Await audits |
| SP-F2-1 | Constraint factorization F2 | Components must be defined using every four-set constraint after fixed bits are inserted | Component adjacency described; no independent-variable assumption on arbitrary triples | Await audits |
| SP-F3-1 | Patch gluing F3 | Scalar counts cannot replace full boundary pairing; a strand cannot enter a patch repeatedly under the stated lemma | Connected-arc intersection and full paired ports are hypotheses; four-strand equal-size/equal-crossing counterexample saved | Scope stated; await audits |
| SP-G1-1 | Periodic limit G1 | Integer seam phases and boundary-preserving product injection | Rational offsets and integer translations explicit; limit is for Q(L,H), never C(n) | Await audits |
| SP-G2-1 | Four-bundle certificate G2 | Bundle completion cannot preserve the old parallel pairing | Repaired in v1 before freeze: fixed tail reversal is specified, separate from F3; child connectivity fixed across all choices | Await audits |
| SP-G2-2 | Four-bundle certificate G2 | Every finite count used in an unrestricted lower bound requires algorithm audit | Q(3,3) computed from complete exact boundary word; small general words and six MacMahon tests cross-checked | G2 remains candidate |
| SP-COMP-1 | Four-bundle L=4 | Preset memo cap reached; no exact count obtained | Child PID19103 exited1 after12.62s at50000 states; stdout and job metadata retained; completed L<=3 values survive | Incomplete, excluded from every bound |
| SP-STATUS-1 | All packets | Novelty and current global rates | No novelty claim; no improvement on published0.2721/0.6496 claimed; prior literature status retained | Limitation acknowledged |

Reviewers must not read each other's initial conclusions. One reviewer must reconstruct the relevant entire packet. The coordinator owns review assignment and any promotion.
