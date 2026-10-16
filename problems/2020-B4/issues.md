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
