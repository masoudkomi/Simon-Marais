# Frozen issue dispositions at coordinator acceptance

# Concavity audit 1 issue log

Initial blind log, 2026-10-16 UTC. Candidate SHA-256:
`07dc9766e56eca4ec3359289a537072d47e6f5ce6b48129538552f54899728fc`.
This log was completed without viewing the other concavity review.

**Open substantive objections: none.** This is an audit disposition;
promotion remains exclusively the coordinator's responsibility.

| ID | Concern tested | Disposition and evidence |
|---|---|---|
| R1-01 | Wrong geometric count or quotient convention | Resolved. Official notes p. 12 and FV pp. 1--3 identify the intended fixed-boundary count with marked simple arrangements. Boundary order and orientation are fixed. |
| R1-02 | Hidden `n-u<=m` restriction in the cutpath lemma | Resolved. Dallant v2 Lemma 3 explicitly removes it. Independent reconstruction of the FV transversal/tree bound with empty color classes covers `m<n-u`. |
| R1-03 | Reverse uniques treated as exactly reverse middles | Resolved. The candidate only uses `k<=u'`, `k'<=u`; it does not assume equality and includes unbounded-cell exits. |
| R1-04 | Zone theorem used on a non-simple extension or wrong edge convention | Resolved for the official domain. A cutpath inserts one generic crossing with each old line; the edge incidence conversion removes `2(n+1)+2n`. Both lower and upper old-cell incidences are counted. See R1-N1 for the unnecessary `n=1` wording. |
| R1-05 | Integer zero endpoints lost in the number of classes | Resolved. Every variable is in `[0,n]`; `(n+1)^6` counts zero tuples safely. No positivity-only interpretation of `N^6` is imported. |
| R1-06 | `m=0`, `k=0`, or `n-u=0` invalidates entropy | Resolved. The zero-exponent convention and deterministic all-unique encoding give the correct endpoint bounds; the continuous formula gives `f=0` at `u=1`. |
| R1-07 | Separate concavity incorrectly used as joint concavity | Resolved. Both exact terms are concave perspectives in their two arguments. Affine composition in `b=1-u-a` gives joint concavity. Explicit bounds verify continuity of both perspective terms at the corners. |
| R1-08 | An asymmetric tuple could exceed the symmetric reduction | Resolved. Swapping triples preserves the linear domain. `min<=mean<=f(average)` gives an upper bound for every feasible pair, and the averaged cross and zone constraints are retained. |
| R1-09 | Saturating `mu` violates feasibility or reverses monotonicity | Resolved. `mu_max=min(1,u+3/4)` is at least each allowed `a`, and `f` is nondecreasing in `mu`, including endpoints. |
| R1-10 | Low-`u` maximum need not have `a=u` | Resolved. `f_a` decreases with `a`, and at the maximal allowed `a=u` it is nonnegative because `3/4-(5/2)u>=0` on `[0,1/4]`. |
| R1-11 | Derivative formula, sign, or negative tangent displacement mishandled | Resolved. Direct differentiation reproduces the exact logarithm argument and rational terms. Independent rational intervals give positive slope below `1/5000`; negative displacement only lowers the tangent. |
| R1-12 | High-`u` tangent bound valid only locally | Resolved. The function is jointly concave on the whole triangle, so its interior tangent is a global upper supporting plane. `f_a>0`, `a<=u`, and negative gradient sum give the stated bound. |
| R1-13 | Rational log tail or interval division direction invalid | Resolved. Independent Mercator enclosures with 96 terms verify all inequalities. Independent reconstruction of the candidate's 80-term atanh endpoints agrees with the frozen exact JSON. |
| R1-14 | Strict pointwise bound gives no uniform strict supremum | Resolved. The exact rational `A_hi=max(Phi_hi+Phi'_hi/25,F0_hi)` is uniformly valid and strictly less than `324757/250000`; saved positive slack is about `3.2238458e-6`. |
| R1-15 | Wrong recurrence, overcounted insertion histories, or lost factor `1/2` | Resolved. FV pp. 3--4 gives canonical deletion/insertion, and `sum j=n(n-1)/2` yields the required factor. `O(n log n)/n^2` vanishes. |
| R1-N1 | Source's stronger edge count if read as including `n=1` | Nonblocking scope clarification. The literal `5.5n-5` edge bound fails for one line. C1 is unaffected: the official domain and the reconstructed iteration start at `n=2`, while `gamma1=1` and the relaxed tuple inequality hold directly. An author may explicitly write `n>=2` at candidate lines 47--49 for clarity. No repair is needed for the claimed asymptotic result. |

Computational searches are evidence only. The proof checks above use analytic
arguments plus finite exact rational certificates for explicit constants.
No finding from a peer review was used to close any entry.


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
