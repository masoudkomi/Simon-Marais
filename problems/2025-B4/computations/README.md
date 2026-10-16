# 2025 B4 computations

**Finite evidence only.** No unrestricted theorem is established by these computations. The preliminary degree-three, odd-exponent equation is excluded.

From the repository root, reproduce with:

```sh
.venv/bin/python -u problems/2025-B4/computations/investigate.py --max-abs-x 10000 --max-degree 128 --max-seconds 120 --output initial-results.json > problems/2025-B4/computations/initial-run.log
```

Runtime used Python 3.12.14, SymPy 1.14.0 and python-flint 0.9.0 from the coordinator's existing environment; no dependencies were installed. The final run took less than 8 seconds. Every thousand completed absolute bases produce a checkpoint. A time-limited run records an incomplete status and the last completed absolute base; no unfinished range is described as complete.

The final run completed all 2,539,746 pairs with 2<=|x|<=10,000 and 2<=degree<=128. FLINT screens exact perfect powers; SymPy gives their maximal exponent, whose divisors enumerate all possible q>=2. Roots are unbounded. Positive sums give both signs for even q and only the positive root for odd q; negative sums allow negative roots and odd q only. Degree 3 first screens squares and enumerates even q only, avoiding a separate investigation of the preliminary odd-q slice. Every reported quadruple is verified by exact substitution.

The six reported signed quadruples are (-19,7,2,3), (3,-11,4,2), (3,11,4,2), (7,-20,3,2), (7,20,3,2), and (18,7,2,3). No other hit occurred in this finite range. This does not prove there are no further integer solutions.

`initial-results.json` is the full final machine-readable record: parameters, timestamps, dependency versions, SHA-256 of the script, search counts, exact hits, lemma counterexample-test counts, an independent exact-root cross-check over 720 smaller pairs, and the Son source counterexample/algebra audit. `initial-run.log` is its exact console transcript. The same finite search was run during script development before adding the independent cross-check and then before adding the boundary-source audit: interim observed elapsed times were 7.003762s and 7.436599s, with the same range, pair count and hits. Those interim full files were replaced by the final run; their summary is recorded here rather than pretending the old complete logs were retained.

`source-manifest.json` gives public source URLs, file sizes, SHA-256 hashes and ignored local cache paths. Full papers must remain outside Git unless redistribution permission is verified. `literature-audit.md` contains dated search queries, source applicability checks and rejected printed inferences. No credentials or authentication data are stored.
