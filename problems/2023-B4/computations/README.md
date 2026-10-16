# 2023 B4(b) computations

All computations are **finite evidence, never proof of the unrestricted statement**. Date: 2026-10-16. Working directory for commands: repository root.

## Completed exact run

Source: `resultant_checks.py`. Output: `resultant_checks.stdout.txt`. Dependencies: Python 3.12.14 stdlib and SymPy 1.14.0 in the existing project `.venv`; no installation was performed. Exact command:

```sh
.venv/bin/python problems/2023-B4/computations/resultant_checks.py > problems/2023-B4/computations/resultant_checks.stdout.txt
```

Exit status: 0. Runtime reported by the command tool: about 1.72 seconds. The run checks:

- 28 resultant weighted-degree and constant-in-N identities, all coprime even/odd index pairs with 4<=e<=18 and 3<=o<e;
- 80 coprime-index unit Lucas resultants with e<=30;
- eight exact numeric comparisons with direct Sylvester determinants, up to overall sign;
- both trace/norm algebraic identities in the coordinator's (4,3) draft;
- every reduced 0<D<1 with denominator at most 300 (27,397 traces), using all positive rational P branches of (4,3) and (6,5), finding no integer-N hit.

The last search found 51 positive rational (6,5) branches; their derived rational N values are printed exactly in stdout. There is no numerical tolerance or random seed. These finite bounds do not exclude larger denominators or exponents and are not used as a logical replacement for the proposed proof.

## Preserved failed run

`resultant_checks.failed-v0.1.py`, `resultant_checks.failed-v0.1.stdout.txt`, and `failure-notes.md` preserve the initial failed finite-search discriminant calculation, its assertion failure, exact invocation and repair. The corrected discriminant is not an ingredient of the general proof. The successful rerun is separate.

## Other commands and outcomes

The owner read the official PDFs with `pypdf.PdfReader`, extracting the B4(b) statement and the official B4(b) discussion. An initial paper-heading lookup for the string `Problem B4` failed (`ValueError: substring not found`); the PDF uses `B4.`. This was a parsing issue, not a mathematical result. A subsequent extraction found the correct fixed-N, real-witness quantifier.

Exploratory exact commands generated the (6,5) resultant and checked its weighted degree before the reusable script was written. The decisive examples, general finite checks and direct algebra tests are all reproducible in the saved script. No unmonitored or incomplete computational search remains running.
