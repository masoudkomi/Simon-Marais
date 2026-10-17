# Fixed phi7/phi11 criteria: initial source checks 2

2026-10-17 UTC. Completed before peer divisor comparison.

## Official domain and accepted project dependency

[Official 2024 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf),
p. 2, B4(b), gives positive odd \(n\), coefficientwise congruence,
integer polynomials and two factors nonconstant modulo two. Zero is
constant modulo two. Only the open part (b) is audited.

Local statement SHA-256:
60244f7752634772adb434efbdb41a63fb02029dc3be4238f3718c6e5ec84e5f.
AGENTS.md SHA-256:
28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff.

Read the coordinator's criterion-acceptance.md and the accepted
zero-automaton-criterion-reviewed-v1.1.md. The latter's Sections 1,
3 and 5 give the exact identity, conjunctive invariant and normal
ring descent needed here; those were reconstructed again in this
audit. Its separate 48-state phi13 certificate was not rerun.

- Accepted criterion:
  362f2541b2bb1ab1e22ba768b41d55e7282f08631b0ad39522682244d213f226.
- Acceptance record:
  526aaca33ea562ee2641a7fbd8ad891b46308f224c1cf0656eb841c29c34217d.

The accepted theorem does not cover the old small-divisor probes.
The candidate restates and separately proves its new criteria.

## Actual irreducibility premise

[Gary M. McGuire, Caltech thesis, 1995](https://thesis.caltech.edu/4053/01/McGuire_gm_1995.pdf),
*Absolutely irreducible curves with applications to combinatorics
and coding theory*, Theorem 2.1', printed pp. 19--20.

The original cached author PDF was inspected as page images.
The affine definition on printed p. 16 is exactly
\(\phi_t(X,Y,1)\); the theorem states absolute irreducibility
for \(t>3,\ t\equiv3\pmod4\). Both 7 and 11 qualify.
The complete printed proof on pp. 19--20 was read, as were
the definition/context on pp. 15--16. The broader thesis and
every auxiliary result are not represented as newly re-proved.
This is the attributed Janwa--McGuire--Wilson input.

Existing ignored cached PDF:
.cache/literature/deep-literature-r2/2024-mcguire-thesis-1995.pdf.
SHA-256 rechecked:
d8e8e62d873c5ec69e2fd40473a9aee257bb8d4994cb5ffc1a42cb70f8bcbd24.

The candidate's rehomogenization and faithful scalar-extension
arguments were independently checked. The source is not being
substituted by an APN-function nonexceptionality theorem.
No new full-paper file was saved or redistributed.

## Effective automatic zero sets: hypotheses verified

[Harm Derksen, arXiv:math/0510583v1](https://arxiv.org/pdf/math/0510583v1),
Theorems 1.10 and 4.14, and the effective-comparison argument
on printed p. 25, were checked directly. The former treats
an explicit recurrence over a field finitely generated over
\(\mathbb F_p\); the latter gives automaticity for a
positive-characteristic recurrence. The candidate's field
and recurrence satisfy those conditions, including possible
zero or repeated roots. No simple/nondegenerate hypothesis
is added to the input statement.

[Adamczewski--Bell, arXiv:1205.4091v1](https://arxiv.org/pdf/1205.4091v1),
Theorems 1.4--1.5 on printed pp. 5--7, were checked as
published context: algebraic power series in positive
characteristic have automatic, effectively determinable zero
coefficient sets. They are not needed for the explicit
fixed phi11 certificate. Neither complete long paper was
independently re-proved.

These sources justify attributing the general method.
They do not identify either singleton zero set without
the new coefficient/certificate argument.

## Earlier gcd statements and bounded attribution

[Delgado--Janwa, arXiv:1207.5528v1](https://arxiv.org/pdf/1207.5528v1),
Lemma 1 on printed p. 5, states gcd results for specified
Gold, Kasami--Welch and Welch families, including distinct
Welch degrees. Its statements, decomposition premises and
short proof were read. It does not assert fixed phi7 or
phi11 divisibility for arbitrary odd indices.

[Delgado--Janwa, arXiv:1602.02576v1](https://arxiv.org/pdf/1602.02576v1),
Theorem 10 and its surrounding scope, were checked. One
designated factor has Gold exponent \(2^k+1\). Neither
7 nor 11 has that form. It supplies relevant selected
exclusions, not the two unrestricted fixed-divisor
criteria. No preliminary construction or whole APN
classification was used.

The public author-uploaded text of
[Caullery's divisibility paper](https://www.researchgate.net/publication/280793382_A_divisibility_criterion_for_exceptional_APN_functions)
was opened; its stated degree-\(4e\) exceptional-APN scope
matches the candidate's title disambiguation. It is not a
theorem premise here. The WCC 2022 public source was also
opened as supplemental context; no later theorem from it
is relied upon.

The complete Férard texts and the 1993 Janwa--Wilson
chapter remain outside this review's read scope. The
constructor's reported failed public routes are not
turned into mathematical evidence or a priority claim.
This audit does not certify exhaustive literature
absence. No purchase, charge, account contact, proxy
or access bypass was used.

## Certificate independence and exact operations

Read the candidate's static certificate, checker and harness.
The reviewer's new checker uses the six direct monomial shifts
of the derived denominator and canonical Gaussian elimination,
with complete vector sets as an additional transition check.
It hard-codes the proposed table as certificate data and
imports no constructor implementation. Only after constructing
its maps and states does it compare results with frozen
constructor records.

The necessary fixed certificate check is not a coefficient
scan: exactly 48 columns, 15 full subspaces, 30 transitions,
outputs and quotient classes are checked. No new states
are searched. The exact command is

    .venv/bin/python problems/2024-B4/reviews/divisor-review-2-run-v1.py

Child PID 77847; external timeout five seconds; return code
zero; completed and reaped in 0.04090591595740989 seconds
including launch. The independent scripts, start/completion
records, incremental stdout, empty stderr and full finite
output are included in this review's hash manifest.
Create-new output files preserve the run; reproducing it
requires a separate version/prefix.

No mathematical computation was used for C7, saturation,
integral descent, source scope, gcd or grading. No larger
BFS, coefficient-index scan, routine sample tests, native
CAS or unrelated process termination occurred.

All candidate-manifest records and the twenty-eight earlier
files frozen by this reviewer are integrity-checked.
No peer divisor findings were read. Only the assigned
divisor-review-2 prefix was written; no constructor,
shared-source, Git or earlier review state was changed.

Requested gpt-6.1-sol / max; verified effective readback
unavailable. Weekly total used before this audit: 20%,
reset 1792745187; the completion manifest records the fresh
check. The cutoff is 90% total used with an integration
reserve. No separately billed API was used.
