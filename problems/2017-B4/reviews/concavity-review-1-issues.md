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
