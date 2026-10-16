# 2018 B4 computations

`exact_count.py` is a deterministic, exact, standard-library-only evidence script. `exact_count-output.txt` preserves its output on 2026-10-16. No finite run proves unrestricted validity.

Runtime: **CPython 3.12.14** (bundled runtime 26.1013.11914); `collections`, `fractions`, `math`, and `platform` are standard-library modules. No packages were installed. No separately billed API was used.

Run from the repository root:

```sh
/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 problems/2018-B4/computations/exact_count.py
```

The script compares three implementations over the full 20-by-20 parameter grid: an explicit binomial sum, direct dynamic programming on the strict-column prefix constraints, and exact generating-polynomial convolution. It also exhaustively constructs sorted rows and checks the reflection bijection and its inverse for \(m\le7,n\le3\). The published \(m=5\) expression is a consistency check only. Rational polynomial coefficients are formed by exact multiplication, without numerical fitting.

`official-statement.png` was rendered read-only from the coordinator's cached source using:

```sh
pdftoppm -f 2 -singlefile -scale-to 1600 -x 130 -y 1150 -W 900 -H 420 -png .cache/official/2018-paper_b.pdf problems/2018-B4/computations/official-statement
```

The complete B4 section was inspected visually. The tracked rendering includes B4 and its source footer only; the original full-page rendering is retained in the ignored coordinator QA cache. Other problems on the source page were not investigated. Source URLs, hashes, and verification date are recorded in `../statement.md`; the coordinator owns the shared source cache and manifest.
