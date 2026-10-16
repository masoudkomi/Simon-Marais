# 2020 B4 issue log

P1–P6 and the attributed square-descent application are **proved, independently reviewed (partial results)**. Both complete blind audits found no substantive gap. The unrestricted classification remains unresolved.

| ID | Issue | Disposition after both audits | Status |
|---|---|---|---|
| 2020-01 | q=1 and official n=2 boundary | Both reconstructed P1 and retained n=2 outside positive-exponent prime-power terminology. | Resolved |
| 2020-02 | Published order q versus official n and table cardinality k | Both checked conservative q<2e10 ⇒ 3≤n≤2e10, with n=2 separate; published large computation not rerun. | Resolved with disclosed scope |
| 2020-03 | Source says positive orbit counts | Both reconstructed the necessary inequality with a,b≥0; existing code allows zeros. The saved q=8 witness demonstrates b=0. | Resolved source wording |
| 2020-04 | All internal reductions and orbit formulas | Both full independent reconstructions, including q=2 nondegeneracy and d=1,v quotient cases, found no gap. | Resolved |
| 2020-05 | Original imported proofs inaccessible | Exact Gordon 1994 restatements and primary abstracts checked; original proofs remain unaudited. No access or full-original-proof claim. | Disclosed dependency |
| 2020-06 | Necessary finite tests versus classification | Both preserve necessary-only and finite-range labels; no existence inference from a passing test. | Resolved |
| R1-2020-C1 | Gordon preprint/publisher theorem numbering | notes/reviewed-source-clarifications-v1.md explicitly identifies arXiv v1 Theorems 3/4 versus publisher 2/3. | Editorial correction resolved |
| R1-2020-C2 | Put collineation hypothesis earlier | Accepted register explicitly states it throughout P2; frozen proof already specifies it in its closing paragraph. | Exposition clarified |

No substantive repair was required. The full reports, immutable manifests and acceptance record preserve the checked scope and source limitations. The initial issue log is retained below for provenance; its pending statuses are historical.

## Original pre-review entries

# 2020 B4 issue log

Partial-v1 is queued for independent review. No full-solution candidate exists.

| ID | Version / location | Objection | Severity | Repair / evidence | Re-review | Status |
|---|---|---|---|---|---|---|
| 2020-01 | Official discussion / statement boundary | The informal prime-power converse omits q=1 under positive-exponent convention; n=2 is in the official domain. | Scope | statement.md and P1 explicitly retain n=2. | Pending two independent audits | Owner repair recorded; unverified |
| 2020-02 | Published finite range | Literature uses q for order, official problem uses n=q+1; small-lambda table labels k. | Scope | Conservative imported range q<2e10, hence n<=2e10; no endpoint overclaim. | Pending source audit | Open for review |
| 2020-03 | Gordon Theorem 3 / residual_orders.py | Statement says positive a,b, although orbit counts may be zero. | Hypothesis | Code tests all nonnegative a,b (and b<=h), a conservative superset of positive solutions; no exclusion from omitting a zero case. | Pending independent computational audit | Open for review |
| 2020-04 | proofs/partial-v1.md P1-P6 | Reduction, plane converse, quotient norm and arithmetic orbit formula require independent reconstruction. | Substantive | Exact domains and q=1 exception written explicitly. | Two blind initial reports not yet obtained | Unverified |
| 2020-05 | Source access | Singer original and several older original proofs were not fully retrievable. | Attribution | Access limitations stated in references.md; precise imported statements checked in accessible primary research papers. No direct-original-audit claim. | Pending reviewer assessment | Open |
| 2020-06 | Computational evidence | Finite filters and occupancy vectors are necessary tests, not unrestricted classification or existence witnesses. | Scope | Every output has explicit range/status; research.md records survivors and failures. | Pending independent audit | Unverified |
