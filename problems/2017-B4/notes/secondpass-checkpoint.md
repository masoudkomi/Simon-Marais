# 2017 B4 second-pass checkpoint, 2026-10-16

Status: **substantive partial candidates, all unverified; no solution of the exact rates and no better global bound**. The current located published interval remains 0.2721 < liminf <= limsup < 0.6496. No original first-pass file or shared coordinator file was changed in this pass.

## Candidate packets

- `secondpass-macmahon-candidate-v1.md`: M1 proposes the sharp finite inequality M(a,b,c)^2*16^(ab+bc+ca) <= 27^(ab+bc+ca). The proof uses Jensen in the correct direction, an evaluated double integral, and a complete symmetric calculus maximum. M2 telescopes this inequality along any adaptive ternary MacMahon hierarchy, giving a precise reason unequal bundle widths cannot improve its old 0.1887218755 coefficient. M3 supplies a floor-robust weighted recursion implication conditional on a valid all-n injection. These are partial structural results; novelty is unestablished.
- `secondpass-boundary-fiber-candidate-v1.md`: F1 identifies a fixed paired-boundary patch count with a fiber of complete arrangement signs. Its forward map is elementary; its embedded-graph converse is a substantive audit target. F2 gives a finite constraint-component factorization; F3 states the exact hypotheses under which local patch counts multiply injectively. This packet retains complete boundary pairing and the marked/fixed-polygon count.
- `secondpass-periodic-grid-candidate-v1.md`: G1 uses exact seam data and two-dimensional superadditivity to obtain an entropy limit for one fixed-direction periodic patch family. It expressly does not infer existence for C(n). G2 is a small reproducible four-bundle construction certificate, conditionally yielding 0.1900060770 from the computed side 3 patch. That value is weaker than the already published 0.2721 bound. It is a test of geometry/counting/recursion, not a frontier improvement.

Each packet starts **candidate proof - unverified**. Two fresh independent adversarial reviews, one reconstructing the entire packet, are required before any promotion. No worker reviewer was launched and no author review is represented as independent.

## Completed exact computations

All use Python 3.12.14 and the standard library, with exact integers/Fraction for combinatorial or geometric quantities. Decimal logarithms are numerical evidence. Commands from the repository root:

```sh
/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 problems/2017-B4/computations/secondpass-patchcount.py --max-n 7 --timeout 90
/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 problems/2017-B4/computations/secondpass-macmahon-bound.py --cap 24 --timeout 20
/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 problems/2017-B4/computations/secondpass-fourbundle.py --max-side 4 --timeout 45
```

Every command is a driver which starts one dedicated child and saves its PID, full argv, parameters, timeout, status, return code and elapsed time to a same-prefix `-job.json`, with incremental stdout in `-output.txt`. No global process kill is used. All children have exited.

1. The boundary-cut recurrence was independently implemented from the attributed 2024 recipe. For all paired words through 7 strands, its counts agree with the proposed signotope-fiber count. At 7 there are 135135 words and 5283 canonical boundary types. Canonical dihedral/relabel forms cache equal counts; they do not quotient the counted arrangements by symmetry. The seven-strand exhaustive comparison finished in 11.04 s. Six MacMahon boundary families also agreed, including M(3,3,3)=980 and M(2,3,4)=490. The original first-pass enumerator was imported read-only with bytecode writing disabled; its SHA-256 is saved in stdout.
2. All 2600 sorted positive integer triples 1<=a<=b<=c<=24 satisfied M1 strictly using exact integer comparisons. The hyperfactorial formula used for the exact product is stated in the script. The largest numerical coefficient on this finite grid occurred at (24,24,24), 0.188576378634261. This finite check does not prove the general inequality. Runtime 0.076 s.
3. Exact rational clipping generated full boundary words for square patches of the four-line-family periodic grid. Completed counts were Q(1,1)=8, Q(2,2)=10442, Q(3,3)=4419734746. The side 3 entropy per area is 3.560145849075202. The side 4 attempt hit the 50000-state cap and exited after 12.62 s. No value for Q(4,4) is reported. Its failure trace and completed checkpoints are preserved. It was not rerun with a larger cap.

An initial through 6 version of the boundary comparison completed in 1.03 s before the through 7 run; all its substantive output is included in the larger run. The added canonical fiber cache avoids redundant comparisons and changes no mathematical recurrence.

## Concrete failures and prevented mistakes

- Replacing paired boundary data by just strand and crossing counts fails already at four strands and three crossings: explicit words have F=1 and F=2. The exact words are preserved in the boundary packet and stdout.
- Free triple orientations are not independent: a complete four-strand patch has 8 assignments, not 16. F2 retains all packet constraints.
- Arbitrary unequal/adaptive ternary MacMahon splitting cannot escape the old coefficient if M1 is correct. A better construction needs interactions beyond that precisely defined hierarchy.
- Completing a parallel bundle requires a fixed reversal tail reconnection. It cannot be described as preserving the old parallel pairing; G2 now states the distinction explicitly.
- G1's valid fixed-direction Fekete limit is not the official growing-direction limit. A proof for C(n) still needs a genuinely stronger compatible replication or entropy argument.

## Sources inspected and limits

The local cached Felsner–Valtr paper supplies attributed context for MacMahon's formula and three-bundle completion. The cached full 2024 paper supplies the boundary-cut recurrence and recursive bundle framework. Directly read sections are recorded in the candidate packets. Their URLs and hashes are in `sources/literature-retrieval.json`; this pass downloaded or redistributed no full paper and edited no source manifest.

The geometric/combinatorial lemmas and calculus argument are proposed project contributions or reconstructions, with no novelty claim. The exact counts are reproducible evidence. No separately billed API was used. Requested launch settings remain `gpt-6.1-sol`/`max`; no effective readback is available. The coordinator monitors weekly telemetry; the most recent supplied baseline for this pass was 6% total weekly used.

## Next obstruction

First review M1–M3 and the topology in F1; any repair must be by the author, followed by re-review of affected arguments. For constructive improvement, a larger patch or a different interaction family is needed. Raising the failed side 4 cap without a better state representation is not the next step. The promising computational direction is to exploit F2's constraint structure or improve cut-state canonicalization, then test again against the preserved exact oracles. The official rates remain unresolved by this work.
