# 2019 B4(b): third-pass frozen checkpoint v1

2026-10-16 UTC. **All new mathematical claims: candidate proof - unverified.**
No new theorem is promoted, exact growth remains undetermined, and novelty
is unknown. The accepted second-pass results are not changed.

Author: `owner_2019_structure3`. Requested settings: `gpt-6.1-sol`, `max`.
Independent effective-setting readback unavailable. Scope: open part (b)
only. No further agent was spawned and no worker commit or push was made.

## Frozen core

- `thirdpass-bounded-separation-v1.md`: envelope lemma, exact bounded-queue
  monitor, nested regular subsets of full minimal obstructions,
  convergence to lambda, explicit delay-three grammar/series, and an exact
  candidate upper bound `lambda<1.834856083`.
- `thirdpass-literature.md`: substantive primary literature searches,
  applicability/hypothesis checks, research directions and careful limits
  on possible-setter attribution.
- `thirdpass-literature-sources.json`: six public full PDFs cached only
  under ignored `.cache/2019-B4-thirdpass/`, with original URLs, retrieval
  timestamps, hashes, byte counts and redistribution-licence status.
- `thirdpass-v1-manifest.json` and `thirdpass-v1-sha256.txt`: exact hashes
  of all frozen third-pass notes, complete data, source versions, logs
  and job records. The manifest excludes itself and its companion hash
  list, to avoid a self-reference.

The central complete data are
`computations/thirdpass-delay7-exact.json`,
`thirdpass-crosscheck15.json`, `thirdpass-minimal3.json` and
`thirdpass-regex3.json`. The independent-implementation crosscheck is an
author check, **not** one of the required independent reviewer agents.
It checks all 65,535 histories through length 15 at caps three and four,
minimum witness widths of all 143 accepted length-at-most-24 factors,
and every row of the rational delay-seven certificate.

## Computation budget and dependencies

Every potentially nontrivial mathematical job used
`computations/thirdpass-run.py`, which launches one dedicated child,
records its PID/parameters and externally waits at most the specified
30 or 60 seconds; a timed-out child would be targeted, killed and reaped.
No job here timed out and no child remains active. The longest complete
job took 8.93 seconds. No delay-eight build or length-28 brute-force
extension was attempted. Node/state caps are recorded in each job and
result JSON.

System `python3`: 3.15.0. Project `.venv/bin/python`: 3.12.14.
SymPy 1.14.0 in the existing project environment was used only for the
small delay-three and delay-four exact rational matrix solves. All other
new calculations use the standard library. No dependency was installed.
The source and outputs of two failed initial symbolic launches (no SymPy
in system or bundled Python) are preserved.

Early exploratory `thirdpass-delay3.json` through `thirdpass-delay7.json`
used the original source, now preserved exactly as
`thirdpass-delay-automaton-v1.py`, SHA-256
`b8f6aa765c4863b34ecc0b9826a8983a25fb1a08629cacae054b4ef52be5ceda`.
Only their displayed Collatz extremum-index selection used floating
point; the automata and integer vectors did not. The source was then
corrected to use exact fractions before the definitive delay-seven run.
The final bound checks **all** strict integer inequalities and is
independent of row-index selection. No earlier display is used as a
rigorous certificate.

## Author audit and reviewer focus

I found no unresolved mathematical objection in my self-audit. The parts
requiring the closest independent reconstruction are:

1. The path-envelope argument restricting a bounded witness to a true
   minimal noncanonical factor. It is what makes the regular obstruction
   sets actual subsets of full `F`, rather than merely sound rules.
2. The exact residual-queue invariant, including phase complementation,
   arbitrary factor-start locations, first divergence and first return.
3. The DFA quotient and proper-prefix/proper-suffix product construction;
   the complete delay-three language equality should be checked from
   transitions, rather than finite coefficient agreement.
4. The orientation of the saved adjacency matrix and positive-vector
   inequalities. No irreducibility assumption is needed for the norm
   estimate, and both letters must be counted if their target agrees.
5. The convergence proof via factorial submultiplicativity and equality
   of each fixed length layer once the cap is sufficiently large.

Two fresh independent initially blind adversarial audits are required;
at least one must reconstruct the full argument. The coordinator owns
review scheduling, issue-log integration and any status promotion.

## Unresolved target and next research step

No explicit exact evaluation of lambda is given. Its accepted lower bound
remains `1.76521`; the new upper bound is a candidate until audited. A
literature-informed next step is to replace literal unbounded queue words
by a proven overlap-width description, or prove an entropy bound for
high-separation minimal obstructions. The generic bounded-buffer and
minimal-forbidden-DFA techniques are published prior art. None of the
checked primary sources identifies the individual 2019 B4 setter.
