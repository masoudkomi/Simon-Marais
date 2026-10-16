# 2020 B4 computations

All recorded runs completed on 2026-10-16 with Python 3.12.14, using the standard library only. No package installation, separately billed API, or floating-point geometry was used. Runtime seconds in logs are measurements; all mathematical comparisons use exact integers. All claims remain finite evidence pending independent audit.

Run from repository root `/Users/uqmkamga/Documents/ChatGPT/Website`:

```sh
.venv/bin/python problems/2020-B4/computations/exact_search.py small --seconds 10 --max-nodes 2000000 --output-prefix problems/2020-B4/computations/small-search
.venv/bin/python problems/2020-B4/computations/exact_search.py filters --bound 5000 --output-prefix problems/2020-B4/computations/filters-q5000
.venv/bin/python problems/2020-B4/computations/exact_search.py orbits --output-prefix problems/2020-B4/computations/orbit-examples
.venv/bin/python problems/2020-B4/computations/residual_orders.py
.venv/bin/python problems/2020-B4/computations/quotient_counts.py
.venv/bin/python problems/2020-B4/computations/verify_outputs.py
```

Each command saves JSON and identical `.stdout` text alongside the script. Existing output names capture the initial run; copy them to a new version before rerunning if preservation is needed. Recorded timestamps and measured times will differ on rerun.

`verify_outputs.py` checks witnesses again by unordered separations (rather than the ordered-difference counter used in the search), compares arithmetic orbit histograms with explicitly enumerated small orbits, checks bookkeeping totals and all saved quotient vectors, and records file hashes. These are consistency checks by the author; they do not count as independent adversarial audits.

## Direct search

`small` searches n=2,5,7,9,10 only, with a 10-second / 2,000,000-call bound per case. It normalizes 0,1 into the set, then recursively enumerates increasing subsets while rejecting repeated undirected cyclic separations. Completeness of this normalization is candidate P3. A timeout/node-limit status is explicitly different from exhaustive nonexistence. No recorded small run was incomplete. Exact outcomes and DFS calls are in `small-search.json`; n=7 exhausted after 4386 calls. Each positive result has a full ordered-difference multiplicity check.

The prime-order preliminary case is not constructed or reproved. The selected positive examples concern q=1 and composite prime powers 4,8,9.

## Imported necessary-condition filters

`filters` covers every integer2<=q<=5000. It skips prime powers as published context and tests, in order: Bruck-Ryser, Jungnickel-Vedder's even-order condition, Wilbrink's 3-divisibility condition, Mann's quadratic-residue condition for nonsquare q, and the multiplier-size bound. The exception q=4 is skipped as a prime power before that bound is applied. The generated subgroup is stopped once q+2 distinct elements have been seen: this already proves its order exceeds q+1, without needing its full order.

For a complete subgroup small enough to pass that bound, an explicit orbit-size subset sum is additionally tested only for q<=500. The three residual values 1944,2304,2435 mean **not decided by this pass**, not potential new counterexamples to published results. Theorem sources and their hypotheses are in references.md. There is no attempt to rerun Gordon's twenty-billion verification.

## Arithmetic orbit diagnostics

`residual_orders.py` computes histograms by divisors of v rather than allocating all v residues; candidate P6 gives the formula. Exact bounded subset sums handle multiplicities with binary splitting. It also implements Gordon 2020/2022 Theorem 3 for each prime p dividing v exactly once and each prime multiplier m dividing q. Here h=v/p, gcd(p,h)=1, s=ord_h(m), and o=ord_p(m^s). It checks **nonnegative** a,b satisfying

\[
q+1=ao+b,\quad b(b-1)\le h-1,\quad ao(o-1)\le p-1,
\]

also requiring b<=h. Including zero counts avoids an unsafe application of the paper's word "positive". If o<=1 the test is skipped. The convention ord_1(m)=1 is used. No exclusion is inferred if the test yields no nontrivial multiplier.

The separate published square descent q=m² => an order-m planar set in a subgroup is not implemented as a hidden local search; its use at 2304=48² is explicit in research.md and partial-v1.

## Quotient counts

`quotient_counts.py` enumerates all nonnegative triples (a,b,c) with sumq+1 and squared sumq+v/3 for q=10,28,52,55,91,100. It asserts the equivalent cross-correlation and Eisenstein-norm equalities for every reported vector. These vectors are occupancies modulo 3, **not vertex sets**. Having such vectors is not sufficient for tautness.

## Official PDF check

The cached official files were read with bundled Python/pypdf 6.10.0 and page 2 was visually inspected after rendering with bundled Poppler `pdftoppm`. The tracked crop contains B4 only. Reproduce the render with:

```sh
pdftoppm -f 2 -l 2 -scale-to 1800 -x 100 -y 1370 -W 1110 -H 340 -png -singlefile .cache/official/2020-paper_b.pdf problems/2020-B4/computations/pdf-check/official-b4
```

`source-check.json` records SHA-256 hashes and the B4(b) source check. The source PDFs are maintained by the coordinator in the shared ignored official cache; this worker did not alter them.
