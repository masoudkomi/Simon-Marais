# 2019 B4(b): second-pass checkpoint 2

2026-10-16. Status of every new mathematical result remains
**candidate proof - unverified**. Frozen checkpoint-1 files are unchanged.
The accepted proof is unchanged. The exact growth constant is still unknown.

## Main new outcomes

The candidate arguments now establish an exact canonical renewal identity,
an infinite rigid collision family, failure of all finite context-equation
presentations on the current generators, infinitely many bounded-run
obstruction shapes, and strict non-sharpness of every finite forbidden-factor
upper approximation. The full arguments are in:

- `secondpass-canonical-renewal.md` (checkpoint 1): no-overlap theorem,
  `C(z)=1/(1-2z+F(z))`, `F(R)=2R-1`, `F'(R)<=2`, and a tail bound.
- `secondpass-rigidity-obstructions.md` (checkpoint 1): exactly two histories
  for the two-parameter family and the resulting finite-rule obstruction;
  failed fixed-window scheduling and range-only tests.
- `secondpass-staircases-and-pumping.md` (new): the closed staircase family,
  its forced-choice proof, failure of finite run-parity base models, and
  strictness of finite factor-avoidance upper bounds.

Two independent adversarial reviewer agents are still required for all of
these claims. The author has not served as an independent reviewer.

## Stronger candidate enclosure from 24-move obstruction data

The new fully enumerated obstruction counts extend those at checkpoint 1:

```
f_21=20, f_22=14, f_23=40, f_24=42.
```

There are 143 minimal bad factors in total through 24 moves. The targeted
enumerator fixes only the universally proved prefix `RR` and suffix `LL`,
successively excludes shorter minimal bad factors, and tests each surviving
complete candidate by exact grid dynamic programming. The complete corrected
run is `computations/secondpass-full-obstruction24-v2.json`.

The initial 20,000-node probe was deliberately stopped at its cap in length
21, after less than 0.1 seconds, and is honestly marked incomplete. After
inspecting it, the explicit cap was raised to one million nodes per length,
with a sixty-second child timeout. The corrected full run completed all
four requested layers in 4.01 seconds, visiting at most 500538 nodes at
one length and testing 74645 complete candidates in that layer. No larger
full-history or context-count enumeration was attempted.

Let

```
P_24(x)=x^4+x^12+2x^14+3x^16+2x^17+4x^18+8x^19+6x^20
        +20x^21+14x^22+40x^23+42x^24.
```

The general tail argument already written at checkpoint 1 applies with
`N=24`. The exact certificate in `computations/secondpass-renewal24.json`
verifies the two negative signs for

```
E_24(x)=1-(48/25)x+sum(n<=24) ((25-n)/25) f_n x^n
```

at `x=100000/176521` and `x=3/5`. Convexity and the accepted bound `R<3/5`
therefore give the new **unreviewed candidate** lower bound

```
lambda > 1.76521.
```

There is also a scalar upper certificate, independent of a large DFA matrix.
The finite set of 143 words is checked directly to be factor-free and
non-overlapping. Its avoiding language consequently has generating function

```
1/D_24(x),        D_24(x)=1-2x+P_24(x).
```

For completeness, the radius `r` of this finite avoiding-language series
is the first positive zero of `D_24`. Its counts `d_n` are submultiplicative,
because cutting an avoiding word gives two avoiding words. Thus
`d_n>=rho^n`, where `rho=lim d_n^(1/n)`; the series diverges at `r=1/rho`.
The formal generating-function identity implies `D_24(r)=0`, whereas
`D_24(x)>0` for `x<r`.

The exact certificate checks at

```
x=100000000/183516197
```

that `D_24(x)>0` and `D_24'(x)<0`. Since `D_24''>=0`, its derivative is
negative throughout `[0,x]`; hence `D_24` has no zero there. It follows
that `r>x` and `rho<183516197/100000000`. Every generated word has a
canonical history avoiding this finite set, so

```
lambda < 1.83516197.
```

The candidate enclosure is therefore

```
1.76521 < lambda < 1.83516197.                    [unreviewed]
```

Only the exact rational signs in the certificate are used. The numerical
roots shown there are explicitly evidence, not the proof. The old accepted
enclosure and proof remain the repository's accepted result until the
coordinator receives and accepts the required two independent audits.

## Search correction preserved

The historical v1 targeted enumerator required suffix `RLL` rather than
only `LL`. It was recognized as an unjustified restriction before its
counts were used by any mathematical argument. Its source and output are
retained, with the explicit warning in
`secondpass-full-obstruction-v1-warning.md`; they are not complete counts
of the full obstruction language. The corrected v2 above allows arbitrary
final L-run length. Checkpoint-1 data are unaffected, as they came from
the independent exhaustive history generator.

## Current run-compression hypothesis and its obstructions

All 143 minimal bad factors through length 24 compress, by replacing every
odd run length with one and every even run length with two, to a minimal
bad factor whose runs are at most two. All fourteen such bounded-run
factors through length 26 have exactly two full histories for their tape
contexts in the exact grid count. These are finite observations only.

The candidate strategy is to characterize all such rigid bounded-run
factors and then derive exactly which even inflations remain minimal.
This would produce an explicit weighted grammar for `F(z)`, allowing a
real evaluation of the renewal root rather than another count enclosure.
No unrestricted compression theorem has been proved.

The finite test `secondpass-parity-model.py` examines 1791 states. For each
of the fourteen known bounded-run factors, it identifies run positions
whose individual increase by two preserves minimality and tests every
zero-or-two combination at those positions. For the 24-move staircase,
ten positions individually permit an increase, but many simultaneous
increases fail: inflating adjacent `R,L` runs can create `RRLL`. All 592
failed simultaneous combinations of individually allowed positions contain
`RRLL`; no simultaneous-inflation failure
without it was found. This is evidence for a guarded inflation model,
not proof that arbitrary larger inflations work independently.

The staircase family has unboundedly many bounded-run shapes, so a finite
list of bases cannot suffice even if the inflation conjecture is true.
The quadratic staircase lengths suggest investigating a continued fraction
or another recursive excursion series. No recurrence, rationality,
algebraicity or nonrationality has been established from these data.

## Literature checked during this stage

Xiaoyu He, Emily Huang, Ihyun Nam and Rishubh Thaper,
[*Shuffle Squares and Reverse Shuffle Squares*](https://arxiv.org/abs/2109.12455),
v2, 2023-11-19, was read through its primary arXiv HTML on 2026-10-16.
Its shuffle-square methods use tableaux and non-nesting matchings; its
large-alphabet asymptotic theorem does not apply to counting the distinct
two-tape partitions of our fixed alternating source. Its binary results
also concern a different enumeration. No theorem from it is used in the
candidate proofs here, and no full third-party paper was committed.

The earlier rational-trace/linear-language literature checks remain in
checkpoint 1. They give no permission to assume unambiguity of the
displayed linear grammar or rationality of the desired counting series.

## Operational state

Runtime versions were checked as Python 3.12.14 and SymPy 1.14.0; only the
small exact characteristic-polynomial calculation used SymPy. All other
scripts use the standard library. Every numerical or symbolic child used an explicit sixty-second timeout,
recorded PID, exact command, completion status and incremental log. Every
job has completed; there is no lingering computational process. The
initial capped searches are saved as incomplete, and the rejected v1
restriction is preserved explicitly. No dependency was installed, no
separately billed API used, and no worker commit or push made.

Coordinator telemetry was last reported at 5% total weekly use during this
pass; the coordinator retains telemetry, review, integration and Git ownership.
Requested model/reasoning settings remain `gpt-6.1-sol`, `max`, without an
independent effective-setting readback.
