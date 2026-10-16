# 2021 B4 computations

All runs below used the existing project `.venv/bin/python`, Python 3.12.14 on
macOS 26.7 arm64. Research scripts use the standard library only; no dependencies
were installed. Official PDF extraction used installed pypdf 6.10.0. SymPy
1.14.0 was available but is not required by the saved search scripts. Full
dependency context is pinned by the coordinator's requirements-research.txt.

From repository root, exact invocations on 2026-10-16:

```sh
.venv/bin/python problems/2021-B4/computations/sparse_witness_search.py > problems/2021-B4/computations/sparse-witness-output.jsonl
.venv/bin/python problems/2021-B4/computations/sparse_witness_search.py --degrees 20 24 --primes 2 3 5 7 11 > problems/2021-B4/computations/finite-field-examples.jsonl
.venv/bin/python problems/2021-B4/computations/two_support_compatibility.py > problems/2021-B4/computations/two-support-output.jsonl
```

| Run | Complete scope | Exact outcome / limits |
|---|---|---|
| sparse-witness-output.jsonl | d=20,24,28,30; <=3 nonzero lower coefficients; nonzero witnesses in {-2,-1,1,2}; gcd-one/reflection filters | No examples. 544616 tuples visited, 237112 reconstructed after filters. Finite integer box only, not a general rational-height bound. |
| finite-field-examples.jsonl | d=20,24; primes2,3,5,7,11; seeks first example per case | Every case finds one. `search_complete=false` denotes deliberate stop at the first verified example, not a timeout. All derivative and polynomial evaluations checked exactly mod p. These are not Q counterexamples. |
| two-support-output.jsonl | Every pair1<=a<b<=d-2 for d=20,24,28,30 | 153,231,325,378 exact necessary-ratio comparisons; none equal. No assertion for unscanned d. Derivation is candidate proof-unverified in notes/two-support.md. |

No incomplete long run is hidden. The real/integer sparse searches completed
within about 2.4 seconds total on this host; the finite-field example run and
two-support comparisons each completed in under one second. Output includes
per-run measured durations where relevant. Computations are evidence, never
proof of an unrestricted statement.
