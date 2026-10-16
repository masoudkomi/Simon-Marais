# Initial blind issue log: concavity review 2

This log was completed independently with the full report before seeing any
peer reviewer conclusion or constructor script/output. It concerns only the
frozen concavity candidate, SHA-256
`07dc9766e56eca4ec3359289a537072d47e6f5ce6b48129538552f54899728fc`.

## CR2-01: start the literal zone bound in its nontrivial size range

**Severity:** nonblocking expository clarification for the asymptotic C1.
**Status:** mathematically discharged in this review; author wording
recommendation remains available to the coordinator.

The imported edge-count statement \(5.5n-5\) cannot literally apply at
\(n=1\): the one-line arrangement has two visited cells with total boundary
incidence count 2, whereas the expression is 0.5. The candidate starts its
illustrative logarithm sum at 1 without noting a finite-size exception.
The weakened necessary inequality used by the candidate does hold at that
size, but it should not be justified by that stronger small-size formula.

The actual claim is asymptotic and the official problem starts at \(n=2\).
Initialize the recurrence at \(B_2=1\) and sum only \(j\ge2\), or absorb
all finitely many sizes into a constant. The proof and exponent are
unaffected. This is not a counterexample to C1 or to the entropy bound.
No repair has been made to the author's proof by this reviewer.

## CR2-02: pruned encoding trees may have no blue successor

**Severity:** source wording caution, not an open candidate objection.
**Status:** resolved by independent reconstruction in report Section 2.

In the older Felsner--Valtr tree exposition, after restricting to paths with
exactly \(k\) red edges, the stated property of exactly one blue successor
need not survive pruning. For example, a root-to-leaf path required to use
all \(h\) red edges cannot retain a blue first step. The valid property is
at most one blue successor. The leaf-count recurrence remains an upper
bound with that weaker property, as reconstructed in this review.

Allowing zero-sized blocks in the same argument also proves the class bound
when \(m<n-U\), so this caution does not restore the extra hypothesis
removed in Dallant v2. The published Lemma 3 imported by the candidate has
the correct hypotheses and bound; no substantive missing source condition
was found.

## Required audit challenges with no issue found

All six integer constraints and the polynomial tuple count; entropy at
\(k=0,N\) and \(N=0\); continuity at \(a=\mu=0\) and \(b=0\);
joint concavity; averaging two triples while bounding the minimum;
monotonicity in \(\mu\); the endpoint derivative test on \([0,1/4]\);
both exact tangent gradients; signs and interval-division directions;
uniform strict slack before taking a supremum; the insertion triangular
sum; the official marked-tiling dictionary; and the absence of a limit
existence claim all passed the independent reconstruction.

No substantive issue remains open in review 2. Promotion, originality
assessment, integration, and any author edits remain the coordinator's
responsibility.
