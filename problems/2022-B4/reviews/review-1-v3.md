# 2022 B4(b): R1 independent re-audit of version 3

Completed 2026-10-16. This is a separate affected-argument re-audit; the
initial report is preserved. I did not read any other re-audit report or
receive another re-auditor's conclusions before completing this report.
Requested launch settings: `gpt-6.1-sol`, reasoning `max`. Effective settings:
no verified readback available.

## Verdict and resolution of the original objection

**R1-2022-01 is resolved for version 3.** I independently reconstructed the
whole standalone fixed-offset density theorem, including all dependencies
and its density limit, and found no remaining substantive mathematical
objection. The repaired radius applies to every reachable abstract state;
the consequent single block length applies after every surviving prefix.
This is precisely the quantifier missing from v2.

This is one reviewer's acceptance of the repaired partial argument, not a
coordinator promotion or a claim of absolute certainty. The theorem states
density one on each fixed offset. It does not answer the official question
for every admissible start, prove the exceptional set empty, or establish a
two-dimensional density theorem. V2's proof remains defective as a historical
version; v3 is the repaired proof reviewed here.

## Frozen inputs, scope and fidelity

The reviewed `proof-extension-v3.md` has SHA-256
`0238f99a93b0ba1076484db1c16b173efcc02be4410e859f2c5bafc55f0f2a3f`.
The initial `reviews/review-1.md` has SHA-256
`6f7f8fa9ce0bcc08ed0738f2db587ad2ef1e0c5f269d9aac975033c8cfe29e60`.
Both hashes were checked before the re-audit and again at the evidence
checkpoint. The unchanged v1 and v2 proof hashes, and the unchanged cached
official PDF hashes, are recorded in the separate evidence output.

Official fidelity was checked against the original Paper B page 2 during
the initial audit, including visual inspection; its cached contents and
hash are unchanged. V3 retains the positive integer domain, inclusive
initial product threshold 600, simultaneous updates using the old pair,
and equality at an arbitrary nonnegative time, including time 0. Fixing
an arbitrary integer offset is explicitly a restriction of the universal
question for this partial theorem. On that line the official admissibility
conditions exclude only finitely many positive `b`.

V3 does not use the established preliminary trapping theorem. Its auxiliary
radius is an initial-data-dependent bound used for part (b), with no claim
of eventual entry into the official fixed narrow strip. The published
recurrence and hypotheses are attributed, and novelty of the candidate
contribution is not asserted. This audit adds no current-literature claim.

## Reconstruction of the repaired proof

### 1. Quotient state and control availability

Keep the original offset `delta` fixed throughout. At any state, write
`b=60q+r`, `a=60q+r+d`, with `0<=r<60`. The floor translations give
`floor(b/20)=3q+floor(r/20)` and
`floor(a/30)=2q+floor((r+d)/30)`, hence exactly
`d'=D(d,r)` and `b'=66q+r+c(d,r)`. In particular the next difference
is independent of the quotient control. Since `66q` is congruent to
`6(q mod 10)` modulo 60, the ten controls yield exactly the ten available
next residues of the prescribed class modulo 6, with no repetitions.
Each of the chosen six-consecutive-residue intervals therefore contains
one available residue. These statements apply also to negative floor
arguments; no truncation-toward-zero convention is used.

A fixed actual integer start still has only its actual successor. Abstract
choice is used below solely to identify finitely many congruence classes
that hit, as justified by the finite lifting argument.

### 2. Exact remainders and one radius for every prefix

Let `u=r+d-30*floor((r+d)/30)` and
`v=r-20*floor(r/20)`. The definition of the floor gives
`0<=u<=29`, even for negative `r+d`, and `0<=v<=19`. Direct algebra gives

```text
10D = 10d + 20floor(r/20) - 30floor((r+d)/30)
    = 10d + (r-v) - (r+d-u)
    = 9d + u-v.
```

Since `-19<=u-v<=29`, the claimed inequality
`10|D|<=9|d|+29` follows. It is a uniform bound for every integer `d`
and every allowed residue. With `M=max(|delta|,29)`, one has
`(9M+29)/10<=M`. Thus `|d|<=M` implies `|D(d,r)|<=M` for every residue.
Starting from `d_0=delta`, induction closes this radius under every finite
abstract control sequence, as well as every actual orbit.

The endpoint `M=29` is allowed; strict contraction is unnecessary. For
example, `d=29,r=0` gives `D=29`, consistent with the needed non-strict
invariance. Neither this boundary case nor arbitrarily large positive or
negative `delta` invalidates the finite uniform radius.

Crucially, `M` continues to refer to the original offset, not to the current
difference. Every state after any surviving prefix lies in the same radius.
This repairs the original quantifier defect without assuming the desired
equality behavior of any individual orbit.

### 3. A single hitting bound from all states in that radius

At any current state in the radius, the first update produces
`h=D(d,r)` with `|h|<=M`. If `h=0`, a hit occurs in one step. Otherwise
the first control can choose the ensuing residue in the sign-dependent
interval, because of the ten available residues. All subsequent choices
use the next difference in the same way; that difference is known before
the residue control is chosen.

For positive `h`, taking the residue in 30-35 makes the next difference
at most `h-1`. At `h=1`, the floor is exactly 1 and the result is 0. For
`h>=2`, the lower bound `9h/10-3/2` is positive, including `h=2`, where
it is `3/10`. Thus positive integer differences strictly decrease without
crossing below zero and terminate within `h<=M` further updates.

For negative `h=-k`, taking the residue in 20-25 gives an increase of at
least 2, because the floor is at most zero. Directly, `k=1,2,3` give
the next differences `1,0,-1`. For `k>=4`, the strict inequality
`floor(x)>x-1` gives
`D(-k,s)<-9k/10+3<0`; at the smallest case `k=4` this upper bound is
`-3/5`. Therefore a value with magnitude at least 4 remains negative
while increasing by at least 2. The value -3 maps to -1. Eventually -2
or -1 is reached and requires at most two more updates to hit zero.

This does not require preservation of parity: after at most
`floor((k-1)/2)` increases that remain negative, the final small-negative
case must have been reached. Adding at most two final updates gives
`ceil(k/2)+1`. For `k<=M` and `M>=29`, this is at most
`ceil(M/2)+1<=M`. The small cases `k=1,2,3` and endpoint `k=4` are
included, rather than inferred from an invalid large-`k` bound.

Including the first update that produced `h` gives the fixed
`K=M+1` for every state in the radius, hence after every surviving prefix
from the fixed original offset. This bound is deliberately loose. If the
current difference is already zero, the history has already hit; no
surviving prefix of that kind enters the counting step. The theorem's
`delta=0` case is immediate at time 0.

### 4. Finite lifting and exact class moduli

The common-shift identity holds by integral translation in each floor.
It is legitimate to evaluate the same algebraic formula on arbitrary
integers for this purpose; actual representatives counted in the theorem
are taken large enough to meet the official domain. Starting with common
shift `60*10^m*z`, its shift after `i<=m` steps is
`60*11^i*10^(m-i)*z`. Thus the states through time `m`, and controls
before time `m`, agree, while `q_m` changes by `11^m*z`.

For the fixed original offset and fixed initial residue, begin with the
single class modulo 1 for a word of length zero. A class modulo `10^m`
has ten refinements modulo `10^(m+1)`. The displayed shift preserves
the existing word and its terminal state, while the ten refinements give
every next control exactly once because 11 is coprime to 10. Induction
therefore gives the claimed bijection between length-`N` control words
and classes of `q_0 mod 10^N`. For `b_0` the modulus is exactly
`60*10^N` with the specified initial residue.

The same shift identity shows the histories through time `N` are constant
on each such class. Every finite class has arbitrarily large positive
representatives with `b_0+delta>0` and product at least 600. Their actual
recurrence remains positive. No assertion about ordinary positive integer
lifts of infinite control words is required or justified; v3 makes none.

### 5. Repeated-block count with the repaired quantifier

For fixed `N`, each class counted by `A_N` determines a surviving history
through time `N`, including the initial time. The state at its endpoint
is in the same radius `M`. Its hitting word of length at most the same
fixed `K` may be padded to length `K`; once a history has hit, later loss
of equality does not put it back in the survivor set.

The prefix's `10^K` refinements give all `10^K` extension words bijectively.
At least one refinement hits within the block. An already failed prefix
has no surviving refinement. Summing over classes gives exactly the
valid inequality `A_(N+K)<=(10^K-1)*A_N`. Dividing by the respective
moduli gives the stated recurrence for `p_N`. Here `p_0=1` when
`delta!=0`, and `p_0=0` when `delta=0`; in particular `p_0<=1` suffices
for `p_(tK)<=(1-10^-K)^t` for every nonnegative integer `t`.

The old R1 witness has `delta=-1`, so v3 uses `M=29,K=30`. The state
`(3,12)` after its surviving three-step prefix is in this radius and its
four-step hitting continuation is within the new bound. The proof of
uniformity covers all prefixes, not just this witness. No use of v2's
invalid bound 3 survives in the reconstructed count.

### 6. Natural density, including its quantifiers

For each fixed `N`, the finite-time survivor condition depends only on
the residue class modulo `60*10^N`. On positive integers its periodic
version has density `A_N/(60*10^N)`. Because the original offset is
fixed, positivity of the other coordinate and the product threshold
remove only finitely many small positive integers, which does not change
this density.

The never-hit set is contained in each fixed finite-time survivor set.
Its upper natural density is consequently at most `p_(tK)`, hence at most
`(1-10^-K)^t`, for every fixed `t`. The integer `K` depends on the
original offset but is finite and does not depend on `t`. These bounds
tend to zero as `t` tends to infinity. Nonnegativity of lower density
then gives natural density zero for the never-hit set. Since the
admissible domain itself is cofinite, the hitting set has natural density
one among positive integers as well as within that domain.

This uses containment for every finite time. It exchanges no infinite
intersection with density, assumes no independence of actual controls,
and obtains no conclusion about a particular exceptional sequence.
The entire argument is elementary; there is no imported theorem with
unverified additional hypotheses.

## Finite evidence and checkpoint

The analytic reconstruction above is the basis of this re-audit. The
following finite computations are evidence only, not premises of an
unrestricted mathematical statement. Run from the repository root:

```text
.venv/bin/python problems/2022-B4/reviews/review-1-v3-evidence.py
```

The separate script uses exact Python standard-library integer arithmetic.
Its supervisor records a dedicated child PID, exact command and parameters,
incremental log path, and a 45-second timeout. The run completed in 3.23
seconds with return code 0. No job remains outstanding.

- The exact remainder identity and absolute-value bound were checked in
  1,200,300 `(d,r)` samples, covering every residue for `-10000<=d<=10000`
  and four additional signed 101-digit differences. The observed extrema
  of `u-v` were -19 and 29.
- Radius closure was enumerated for every state at `M=29,30,31,100,1000`.
  Policy paths were checked for every state at `M=29,30,31,100`, with
  maximum observed path lengths 28, 28, 28 and 40, respectively, all
  below `M+1`. Sixteen additional paths began at differences `+/-10^100`.
- The positive and negative local bounds included all magnitudes 1-1000
  and `10^100`. The inequality `ceil(M/2)+1<=M` was checked for
  `29<=M<=10000`, in addition to its analytic verification above.
- There were 280 complete control-word bijection checks for lengths 0-4,
  seven initial differences, and eight residue boundary cases. The same
  runs made 3,041,976 exact shifted-state comparisons.
- Exact finite dynamic counts were obtained through `2K` for offsets
  `-30,-1,0,1,30`; the conditional block inequality was checked for all
  `0<=N<=K`. Direct enumeration of initial congruence classes independently
  matched the dynamic counts at lengths 0-3.
- Both old numerical witnesses as recorded in v3 were independently
  evaluated under the new radius; their continuations fit within 30.
  The second witness's tested policy takes six steps, which does not
  conflict with v3's claim of a shorter minimum abstract path.

Evidence files are `review-1-v3-evidence.py`,
`review-1-v3-evidence-output.txt`, and `review-1-v3-evidence-job.json`.
All proof versions and the initial report retained their frozen hashes
through the final computation checkpoint. Only this report and these
separate evidence files were written. No other re-audit was inspected,
no shared issue log or proof was edited, no dependency was installed,
and no commit, push or unrelated process termination was performed.

The coordinator may record R1-2022-01 as resolved in v3, subject to the
second independent affected-argument audit and the coordinator's promotion
decision. No further author repair is requested by R1 for this version.
