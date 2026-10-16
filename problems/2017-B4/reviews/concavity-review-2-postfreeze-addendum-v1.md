# Post-freeze arithmetic comparison: concavity review 2

The independent initial full report, issues, source checks and N=96
certificate were frozen before this comparison. Initial freeze SHA-256:
`aa69df336924f90c3ccfa139e6d487105083939df7be0be90c7fd53ec9e184a2`.
Those eight frozen artifacts were rehashed and verified unchanged.
No peer reviewer conclusion was read during this subsequent comparison.

Only after the initial freeze did I read the constructor's script,
certificate and job record. Their hashes matched the construction manifest:

```text
deep-literature-r2-concavity-certificate.py
f26e2b9aabe20dc01457e6b7e4a4ce6e168f3a8be046db5965b7fc69d725e03b
deep-literature-r2-concavity-certificate.json
8b5222a9240d6d6dd8126ccaaff8a2585523f1914e8e4b2932b6ae07fa14714f
deep-literature-r2-concavity-job.json
21c53e4f74eaee9d39f47cc0dd0523265f375b73ea241b03dee2bf90a57a2a30
```

The constructor uses rational `Fraction` arithmetic for its asserted
inequalities and reserves floats for diagnostics. Its log summation, next
power in the geometric tail, positive-numerator interval divisions, tangent
value and derivative combinations, and factor of 1/2 match the independently
derived formulas. I found no hidden floating-point premise or source-path
substitution.

The separate comparison script imports only my own already-frozen log
routine under `-B`, switches its in-memory term count to 80, and recomputes
all five intervals. It never executes the constructor's code. It verifies:

* exact equality of each recomputed 80-term lower and upper endpoint with
  the saved constructor endpoint;
* exact containment of my blind 96-term intervals in those 80-term intervals;
* exact equality of the constructor's derived value, slope and quarter-point
  endpoints with the recomputed rational expressions;
* the strict scalar inequalities and the objective-to-limsup factor of 1/2.

All 17 exact comparisons passed. This is finite verification evidence;
the unrestricted mathematical argument remains the analytic reconstruction
in the initial report.

Reproducible command:

```text
/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -B -u problems/2017-B4/reviews/concavity-review-2-postfreeze-compare.py
```

The comparison supervisor recorded an external 30-second cap, child PID
`65145`, start `2026-10-16T21:23:38.019176+00:00`, exit code 0, successful
reaping, no timeout, and about 0.084 s elapsed. Exact comparison results,
stdout/stderr, parameters and job status are preserved under the reviewer
prefix. No constructor artifact or original blind artifact was overwritten.

The review verdict is unchanged: no substantive unresolved objection to C1
was found. The nonblocking finite-size clarification and resolved older
tree-wording caution are preserved in the initial issue log. This addendum
does not promote the candidate or establish originality or a full B4
solution.
