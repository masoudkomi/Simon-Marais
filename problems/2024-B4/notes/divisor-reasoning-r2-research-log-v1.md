# Divisor reasoning R2: construction log

2026-10-17 UTC. Constructor `review_2021_reasoning_j15_r2`. Status:
**candidate proof - unverified**. Requested gpt-6.1-sol/max; independent
effective readback unavailable. All older J15, 2024 structural and 2017
blind-review artifacts remain untouched. No peer 2017 structural audit
was read. No shared status, Git action or spawning occurred.

## Inputs and research order

Read current AGENTS.md, official-normalized 2024 statement, accepted
whole-phi13 criterion and acceptance, the coordinator's unverified
small-divisor note and its finite graph JSON, earlier literature notes,
and the earlier unverified structural candidate. First checked primary
gcd/divisibility literature, including the 2012/2016 Delgado--Janwa
papers. Then constructed the new coefficient argument, checked further
function-field/zero-set sources, and completed a static exact phi11
certificate. The older scan below 8192 was read as part of the input
record but is not used as a premise.

## Successful reasoning

1. The accepted integral/normal ring bridge applies to any whole formal
   divisor, not specifically P5. For A2 and A4, primality plus localization
   saturation at q produce exact single-parameter series. The candidate
   gives the full hypotheses, avoiding accidental loss at q=0.
2. For phi7, denominator `(1+z+z^2)^2+bz^3` expands by b degree. The
   maximum possible b coefficient detects j=0,1 modulo 3 and j=3m+2
   when m is odd. For positive even m=2^v s, choosing b exponent
   `m-2^(v-1)` and using Frobenius exposes a coefficient equal to one.
   The only remaining zero is j=2. This is an analytic proof at every
   index and uses no automatic graph.
3. For phi11, the finite 15-state graph already suggested by the
   coordinator is enough once the universal conjunctive section invariant
   is proved and every transition is checked. The new checker rebuilds
   polynomial support maps and complete subspace vector sets; it imports
   no old constructor code or operator columns. It checks all 30 edges,
   outputs and quotient classes. The exact language is `0010*`, least
   significant bit first, hence canonical index four only.
4. The source's absolute irreducibility for n=7 and 11 converts the
   whole-divisor exclusions into an exact gcd/common-absolute-component
   result. Grading also gives the finite nonhomogeneous odd-sum
   consequence (17). Neither supplies a new reducible exponent.
5. The function-field recurrence reduction for any fixed F2-irreducible
   G coprime to R is a direct attributed application of Derksen. The
   general existence/effectiveness of automatic zero sets is published;
   it does not remove the unbounded search over possible factors in the
   whole contest problem.

## Approaches considered but not used as proof

- Finite b specializations for phi11 impose only residue conditions on
  an index and cannot establish a polynomial-parameter zero. They were
  considered analytically, not used to infer an infinite criterion.
- Leading b degree in the phi11 series proves nonvanishing immediately
  at indices 3m and 3m+2. At 3m+1, the leading coefficient is m+1 modulo
  two; when m is odd it cancels. A next-coefficient calculation detects
  m=3 modulo four but leaves further cancellations. I did not assert a
  general leading-degree formula or turn these fragments into an
  unsupported valuation induction. The exact finite certificate closes
  that remaining proof instead.
- A possible larger-symmetry/Dickson-polynomial route for phi7 was
  considered as intuition and abandoned once the short parameter
  coefficient proof was available. No new invariant-theory theorem is
  asserted or needed.
- Published APN nonexceptionality is not whole F2 irreducibility. Nor
  does existence of one absolute F2 component classify the other factors.
- A title containing 'divisibility criterion' did not by itself supply
  the fixed divisor sought: the Caullery paper addresses degree 4e
  exceptional APN polynomials. Its source scope is recorded separately.

## Exact computation actually required

One fixed finite symbolic certificate was checked. There was no index
scan, search expansion, factorization or native CAS. Exact command:

    .venv/bin/python problems/2024-B4/notes/divisor-reasoning-r2-phi11-run-v1.py

The harness started child PID 75264 at
2026-10-17T00:21:37.727404+00:00 with an explicit five-second timeout.
It finished with code zero in 0.04884912498528138 seconds. Incremental
stdout confirms 48 operator columns, 30 transitions, outputs and the
five-class quotient. The output keeps all complete finite vector sets.
The static table is provenance-attributed to the coordinator probe;
this construction is not an independent review of itself.

The certificate and new checker are proof-supporting finite algebra,
not empirical validation of an unrestricted pattern. The independent
reviews must reconstruct them afresh. Metadata freezing and hashing are
the only other computations. No separately billed API or native process
cleanup was used.

## Status and budget

No result is promoted by this constructor. Both new criteria, the
gcd extension and the graded-sum corollary require two fresh blind
nonconstructor audits, one of the whole packet. The coordinator alone
may promote. This is a finished fixed-divisor construction, not the
full B4(b) solution.

Latest authoritative account-wide telemetry in this assignment: 19%
total used in the 10080-minute codex window, reset Unix 1792745187.
The 90%-total cutoff and review/integration reserve remain in force;
no new weekly window was entered.
