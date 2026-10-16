# 2024 B4 computations

All computations here are exact GF(2) calculations. They provide finite evidence/certificates, not a general classification. No multivariate irreducibility claims are made by the sparse arithmetic script.

## Invariant probe

Command from the repository root:

```sh
.venv/bin/python -u problems/2024-B4/computations/invariant_probe.py > problems/2024-B4/computations/invariant-probe-output.txt
```

Dependency: Python 3.12.14 standard library only. Existing project dependencies SymPy 1.14.0 etc. are not needed by this script. Completed normally; exact elapsed runtime was not instrumented. No random search.

- `invariant_probe.py`: set-based sparse arithmetic in characteristic two; direct Frobenius powering and exact polynomial division; independent invariant recurrence.
- `invariant-probe-output.txt`: exact completed run output.
- `n205-certificate.json`: all exponents of both factors in x,y,z, and both formal invariant factors. A term is a tuple of nonnegative exponents with coefficient one; all omitted coefficients are zero. Multiplication is over F2. The finite identity is phi_205=phi_13 B.
- Odd n=3,5,...,65: direct construction and recurrence match exactly.
- Fixed-divisor scan odd n=3,5,...,1025: phi_13 divides in the formal invariant ring only at 13 and 205. This does not search every possible factor or prove irreducibility for other n.

## Official source rendering

The bundled Poppler executable was used, with no installation:

```sh
/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm -f 2 -singlefile -scale-to 1500 -png .cache/official/2024-paper_b.pdf problems/2024-B4/computations/source-checks/2024-b4-statement
/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm -f 17 -singlefile -scale-to 1500 -png .cache/official/2024-solutions.pdf problems/2024-B4/computations/source-checks/2024-b4-context
```

Both output images were inspected on 2026-10-16 for exact B4(b) wording and the published partial-result list. Other problems appearing on the source page were outside research scope.

## Launched follow-up

```sh
.venv/bin/python -c 'import sys;sys.path.insert(0,"problems/2024-B4/computations");import invariant_probe as p; hs=p.invariant_powers(3277); a=hs[13]; c,r=p.divrem(hs[3277],a); print("n3277", "divides",not r,"remterms",len(r),"cofactor",len(c))'
```

Completed normally, exact stdout:

```text
n3277 divides True remterms 0 cofactor 34414
```

This tests only the speculative next exponent (4^7+1)/5. The cofactor was calculated by exact formal division, and remainder zero was checked. The cofactor was not saved in this follow-up command; rerunning the displayed command reconstructs it. No unrestricted family follows from these three exponents.

## FLINT factor probe

The coordinator installed python-flint 0.9.0 centrally after this worker's initial checkpoint. `flint_probe.py` first factors a small product and explicitly multiplies the result back, then performs the same check for a fixed bounded list of exponents. Its source records the exact list. Official API checked at https://python-flint.readthedocs.io/en/latest/fmpz_mod_mpoly.html on 2026-10-16.

```sh
.venv/bin/python -u problems/2024-B4/computations/flint_probe.py > problems/2024-B4/computations/flint-bounded-output.txt 2> problems/2024-B4/computations/flint-bounded-stderr.txt
```

The output and JSON preserve exact factors/multiplicities. A CAS report that a factor is irreducible remains computational evidence here unless independently justified. Each equality is checked by exact multiplication; a factorization with at least two positive-degree factors certifies the requested finite reducibility identity regardless of irreducibility status.

Initial run output: n9 has degrees 3+3; n57 has degrees 27+27; n205 has degrees 10+192, all multiplicity 1. Other sampled n=5,7,13,21,25,29,41,45 produced one factor. The first run completed factorizations but failed at final JSON serialization with `TypeError: Object of type fmpz is not JSON serializable`. Converting FLINT exponents/degrees/term tuples to Python integers repaired serialization.

An initial rerun, exec session 39778, was still inside the native n205 factorization at this worker's handoff and is recorded as **incomplete**. Its stdout/stderr are `flint-probe-output.txt` / `flint-probe-stderr.txt`; no complete output artifact is attributed to that rerun. The coordinator was asked to handle targeted cleanup. Ctrl-C on the plain exec stdin did not stop it; sandbox denied `ps -Ao pid,etime,command` with `operation not permitted`. No other Python process was targeted.

The final script avoids repeating n205 and isolates every other factorization in a child process with a 30-second timeout, saving exact factors immediately after each n. Its bounded run (exec session 6447) completed all ten sampled small exponents, wrote `flint-factor-certificates.json`, and has an empty stderr file. It uses the displayed bounded-output command. n205 remains fully covered by the independent completed sparse certificate, which is the reproducible evidence used for that exponent.

Coordinator cleanup: the retained rerun stderr ends in `KeyboardInterrupt` at the native factor call. A scoped OS process inspection found no matching `flint_probe.py` process. The worker-local exec session 39778 was not accessible from the coordinator (`Unknown process id`), so no exit code is invented. No global Python kill was issued. The interrupted rerun remains excluded from completed evidence; use the bounded final script and completed sparse certificate instead.

## Symbolic Cartier-family certificate v1

**Candidate proof - unverified.** This supports the separately versioned
`../proofs/fixed-factor-family-v1.md`; it does not determine all qualifying
exponents. The coefficient ring is GF(2)[b,b^-1], with b an indeterminate.
No numeric parameter sampling or factorization oracle is used.

```sh
.venv/bin/python -u problems/2024-B4/computations/cartier_family_certificate_v1.py
```

The retained run was launched from a Python subprocess supervisor with
`Popen`, `wait(timeout=30)`, and targeted `kill()` only on timeout. It
completed normally without a kill: PID 12474, return code 0, elapsed
0.181595375 seconds. Standard output was flushed at checkpoints and
saved as `cartier-family-output-v1.txt`; stderr is the empty
`cartier-family-stderr-v1.txt`. The full command, timeout, interpreter
version and completion status are in `cartier-family-run-v1.json`.
Dependencies: Python 3.12.14 standard library only; no native CAS.

`cartier_family_certificate_v1.py` constructs K^15 in two independent
multiplication schedules and compares their full 361-term monomial
sets. It then checks the three claimed numerator identities in the
symbolic Laurent-polynomial ring. The outputs have 49,24,25 terms;
all three differences are zero. `cartier-family-certificate-v1.json`
stores K, K^15, all output monomials, L/M/J exponent lists and all
selected coefficients. A pair [i,a] denotes the monomial z^i*b^a
with coefficient one; omitted monomials have coefficient zero.

These are finite certificates of exact identities in an indeterminate,
so each displayed identity is valid for the formal parameter, not only
at checked values. The unbounded m claim additionally requires the
span induction and localization descent written in the proof; those
steps await the two independent mathematical audits.

The script also computes the normalized series directly up to j=1637
and checks its zero coefficients at (m,j,n)=(0,5,13),(1,101,205),
(2,1637,3277). Those three checks are explicitly finite evidence and
are not a proof of the unrestricted family. It constructs no full
large cofactor and runs no growing native factorization.
