# 2019 B4(b): exact finite computations

Date: 2026-10-16. Runtime: bundled Python 3.12.14, standard library only;
no third-party dependencies and no separately billed API.
All outputs are **finite computational evidence**. Their role in candidate
unrestricted arguments is explained separately in `../proof.md`.

Run from `/Users/uqmkamga/Documents/ChatGPT/Website`:

```sh
/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 problems/2019-B4/computations/enumerate.py --max-n 25 --max-t 24 --deletion-audit 14 --fixed-split 24,12 > problems/2019-B4/computations/enumeration-2026-10-16.json
/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 problems/2019-B4/computations/upper_certificate.py > problems/2019-B4/computations/upper-certificate-2026-10-16.json
/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 problems/2019-B4/computations/explore.py > problems/2019-B4/computations/exploration-2026-10-16.json
```

The first script:

- generates sets of distinct words, packed as integers with an externally
  known length, through length 25;
- independently tests every binary word through length 14 by interval
  deletion recursion;
- generates marked contexts through 24 moves, retaining their left length;
- reinserts the seed and compares with every available unmarked count;
- independently enumerates all 2704156 twelve-element subsets of 24 source
  positions, obtaining 395397 distinct fixed-position contexts.

The second script checks both replacements at both possible first bits,
constructs the complete suffix-avoidance matrix, and verifies all twelve
strict integer inequalities for the fixed rational candidate upper bound
183761/100000. Its floating-point eigenvalue estimate is displayed as
evidence only and is not used for the inequalities.

The third script reproduces the short greedy-deletion counterexample and
the first additional 12-move relation among `RRLL`-avoiding histories.

All three runs completed. No larger run, interrupted search or extrapolated
term is reported. The final unmarked count is 1417222, the final total
marked count is 2985943, and the final maximum fixed-position count is
395397. Full intermediate rows appear in the JSON output.

SHA-256 of the first two scripts and outputs immediately after the runs:

```
cb8c21a83f51ee2e065eebb6ee1d01617f75fefe26d5609957f892cb429a0645  enumerate.py
49795106e48cbb880f086f33f1b532cefc43c82ae3135834195e02a481220b1d  upper_certificate.py
a2b5c5e7d40afa68dc8f2704988f17fcb749da4921202ddbf533e381b06477ba  enumeration-2026-10-16.json
da9278d68e22914bfb63457459f597dcbb3aeb9de55ba0ebd9837e4db151ea03  upper-certificate-2026-10-16.json
```
