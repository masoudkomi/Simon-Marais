# 2017 B4 computations

All runs below completed on 2026-10-16 using **Python 3.12.14**, standard library only. There are no third-party dependencies or random choices. A finite computation does not establish an asymptotic theorem.

From the repository root:

```sh
/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 problems/2017-B4/computations/enumerate_small.py > problems/2017-B4/computations/enumerate_small-output.txt
/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 problems/2017-B4/computations/macmahon_check.py > problems/2017-B4/computations/macmahon_check-output.txt
```

`enumerate_small.py` enumerates all reduced adjacent-swap words to reversal for n=2,...,6, stores the complete crossing orders along strands, and independently searches the one-change triple-sign predicate through n=7. It compares the entire signature sets through 6. A 45-second watchdog applies to each individual search; exceeding it raises an error rather than returning an incomplete count. All configured searches finished. The n=7 reduced-word enumeration was deliberately not attempted. The final table through n=16 is explicitly transcribed published data from SoCG 2024 Table 1, not newly computed tiling counts; only its logarithms are evaluated here. n=1 is the conventional empty-network extension used in that literature and is outside the official n>=2 domain.

`macmahon_check.py` evaluates MacMahon's product as reproduced in Felsner–Valtr, Section 4, using exact `fractions.Fraction` arithmetic. The product's third index is telescoped. Its integral denominator is checked for every configured m in {1,2,3,4,8,16}. This is an exact arithmetic reproduction of a published formula, not a proof of the formula or of the gluing injection. Decimal logarithms and coefficient displays are numerical evidence.

The full stdout files preserve the multiplicity histograms and extension-count ranges. There were no incomplete computational runs. The first enumerator was run once interactively before adding the extension-count table, then rerun to save the final stdout. No larger search was left running.
