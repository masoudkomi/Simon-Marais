# 2022 B4(b): independent adversarial review 1

Initial report completed 2026-10-16. Reviewer R1 independently reconstructed
the whole argument. No other review report or another reviewer's conclusions
were read before this report was completed. No proof file or shared issue log
was edited. Requested launch settings: `gpt-6.1-sol`, reasoning `max`.
Effective settings: no verified readback available.

## Verdict

- **proof.md v1, P1-P4:** no substantive mathematical defect found in this
  audit. These are partial results only. This is one review, not a promotion
  to the repository's independently reviewed status.
- **proof-extension-v2.md:** a substantive, repairable gap blocks acceptance
  of the density proof as written. The assertion that its initial-state bound
  `K(d)` works after every surviving prefix is false. The local arbitrary-
  difference control argument passes this audit; the claimed density theorem
  is not refuted by the counterexample below.
- Nothing reviewed establishes a universal positive answer, a counterexample
  to the official question, or a two-dimensional density theorem.

## Frozen inputs and official fidelity

The reviewed proof hashes, verified before the audit and again by the evidence
script, are:

| File | SHA-256 |
| --- | --- |
| `proof.md` v1 | `8b35be18bb70f81b623f78e7dd1a148478c698c1f5ad32e4097def92ff75aed3` |
| `proof-extension-v2.md` | `b41aff3fcfadd33f80fdec80570d5b2f61807a5b9e16a28becacefaa237743ed` |

I read the cached original official Paper B, visually inspected its page 2,
and checked the relevant official solution-note statement. The PDF sources
are the original primary sources, not the normalized statement alone:

- [Official Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2022-paper-b.pdf),
  page 2; cache `.cache/official/2022-paper_b.pdf`, SHA-256
  `33b15241e89b2e4db54f78d3a565ee01afe357ade786f8bb7602c0b7e89e4519`.
- [Official solution notes](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2022-solutions.pdf),
  B4 begins on printed page 16; the invariant-strip conclusion is explicitly
  stated on printed page 19. Cache `.cache/official/2022-solutions.pdf`, SHA-256
  `3e1670aef22b83cd2be13d027728ebed119072011e4150d7c3aa8dba3101295f`.

Both candidates use the correct positive integer domain, inclusive initial
product threshold 600, simultaneous old-pair updates, and nonnegative
equality time (including time 0). The invariant strip is used only as
attributed established context for v1. I did not reconstruct or reproduce
the preliminary proof. Attribution of the official recurrence and strip is
separated from the candidates' contributions; novelty remains unestablished.
No claim about the current literature's completeness follows from this review.

## R1-2022-01: initial bound cannot be reused after arbitrary prefixes

**Severity:** substantive; must repair and re-review the extension's counting
step. **Location:** `proof-extension-v2.md` lines 73-77, especially 74-75.

The analytic argument in lines 24-69 supplies a path bound for states whose
current difference is the specified initial `d`. It does not bound the path
length from every state reachable after an arbitrary surviving prefix. The
fixed initial difference is generally no longer the current difference.

This is a false intermediate assertion, not only an omitted explanation.
For `d=-1`, the possible `D(-1,r)` are `{-2,-1,0,1,2}`, so the displayed
definition gives `K(-1)=3`. Consider the admissible initial pair `(599,600)`:

| Time | a | b | d=a-b | r=b mod 60 | e=floor(b/60) mod 10 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 0 | 599 | 600 | -1 | 0 | 0 |
| 1 | 659 | 657 | 2 | 57 | 0 |
| 2 | 723 | 720 | 3 | 0 | 2 |
| 3 | 795 | 792 | 3 | 12 | 3 |

Its first three controls `(0,0,2)` form a surviving block of precisely
`K(-1)` steps. From state `(3,12)`, **no** abstract continuation hits equality
in at most three more steps. An elementary exhaustive description verifies
this without assuming an integer lift of an infinite walk:

1. The next difference is 3. The next residue can only be a multiple of 6.
2. From `(3,s)` with `s` a multiple of 6, the next difference belongs to
   `{2,3,4,5}`. The value 2 occurs only for `s=30` or `s=36`; then the
   ensuing residue is 3 modulo 6.
3. For each `h` in `{3,4,5}` and every residue `u`, `D(h,u)>=h-2>0`.
   For `h=2`, equality in one update occurs only at `u=58` or `u=59`,
   neither of which is 3 modulo 6. Thus the third further update cannot hit.

A fourth further update can hit: the successive abstract states
`(3,12), (3,30), (2,33), (1,30), (0,33)` are feasible, with controls
`(3,0,9,0)`. Thus the minimum abstract hitting length at the reached state
is 4, greater than the claimed reusable bound 3. All 1-, 2-, and 3-step
continuations were also independently enumerated as finite evidence in the
accompanying script.

**Required author action:** supply a finite bound valid uniformly over every
state reachable from the fixed initial difference, and redo the block count
with that bound. One possible route to check is a uniform bound on all
reachable differences, then maximize the local path bound on that finite
set. For example, the formula for `D` suggests investigating the elementary
estimate `|D(d,r)| <= 0.9|d|+2.9` and a bound depending on
`max(|d_initial|,29)`. The author must state and justify the repair; this
review does not alter or accept a repaired proof. Alternatively, a rigorous
nonuniform counting argument would also need to replace the present claim.

The displayed survival upper bound might hold for other reasons, but it does
not follow from the false per-prefix assertion. Density one itself remains
plausible and is not disproved here.

## Reconstruction of v1 and checks of each substantive step

### P1: quotient dynamics and finite lifting

Writing `b=60q+r` and `a=60q+r+d` gives
`floor(b/20)=3q+floor(r/20)` and
`floor(a/30)=2q+floor((r+d)/30)`. Hence `d'=D(d,r)` and
`b'=66q+r+c(d,r)` exactly, including negative `d` and negative floor
arguments. Reducing `66q` modulo 60 gives `6e`, so the ten controls give
exactly the ten residues of the required class modulo 6. They are abstract
choices, not ten successors of a fixed actual integer pair.

The common-shift identity follows from integral translations in both floor
arguments. For the shift `60*10^m*z`, the shift at time `i<=m` is
`60*11^i*10^(m-i)*z`; it is still divisible by 60. Consequently the states
through time `m` and the controls before time `m` are unchanged, while the
time-`m` quotient shifts by `11^m*z`. Its ten residues modulo 10 are all
different. Beginning with `m=0`, each class for a length-`m` word therefore
has exactly one of its ten refinements realizing a chosen next control.
This reconstructs the bijection for every finite word length, including the
base case. The exact modulus is `10^N` for `q` and `60*10^N` for `b` with
the prescribed initial residue.

Every such finite congruence class has arbitrarily large ordinary positive
representatives meeting both positivity and the product condition. Following
the actual recurrence then retains positivity. This does not lift an infinite
control word to an ordinary integer; the candidates correctly distinguish
that missing implication.

### P2: strip path and density

The established invariance hypothesis is applicable: for every abstract
strip state there are arbitrarily large admissible representatives. For a
positive ensuing difference `h`, the unique available residue in 30-35 gives
`31<=s+h<=58`, so `D(h,s)=h-1`. The endpoints `h=1,23` are included. For
`-13<=h<=-1`, the residue in 20-25 gives `7<=s+h<=24`, so
`D(h,s)=h+2`. An odd negative value can first reach 1, then 0; the maximum
is eight further steps from -13. Including the unconstrained first update,
24 steps suffice from every strip state. Controls needed at the final
equality step may be chosen arbitrarily; padding a hit to length 24 keeps
the history classified as hit, even if equality is later lost.

Unlike the extension's `K(d)`, the constant 24 is valid after every surviving
prefix, because the same established invariant strip contains all reachable
states. Each prefix has `10^24` equally numerous refinements modulo the
larger modulus, at least one of which hits. Iterating this finite count
gives the stated survival fraction. Equal frequency follows from the
congruence-class bijection; no probabilistic independence of actual orbits
is needed.

For each fixed block count the finite-time survivor set is periodic modulo
`60*10^(24t)`, after discarding finitely many inadmissible small `b`. The
never-hit set lies in every such survivor set, so its upper natural density
is bounded by `(1-10^-24)^t` for every integer `t`. Letting `t` tend to
infinity gives upper density zero; lower density is nonnegative, hence the
ordinary natural density is zero. The admissible domain on each fixed line
is cofinite among positive integers. The complement consequently has density
one, as claimed. The case `d=0` hits at time 0.

### P3: arbitrarily long finite delay

For `n<N`, the leading term is divisible by 60, while `0<=r<=19` and
`1<=r+1<=20` make the two residual floor terms zero. The increments are
equal, and the leading term is multiplied by `11/10`. Induction gives the
displayed formula through time `N`, including its endpoint. The smallest
permitted initial `b` is 600, so the domain and product threshold hold.
Difference 1 throughout this arbitrary finite interval precludes a uniform
finite upper bound on first-hit times, even if some starts never hit. No
conclusion after that interval or about an infinite avoidance orbit follows.

### P4: ultimately periodic full states

The quotient update is exact because
`r_n+c(d_n,r_n)-r_(n+1)` is divisible by 6. If the full state is eventually
`p`-periodic, the integers `h_n` are `p`-periodic as well. On a fixed phase,
composition yields `x_(j+1)=(11^p*x_j+H)/10^p` with integer
`H=sum_(i=0)^(p-1) 11^(p-1-i)*10^i*h_i`. The displayed iterated identity
is correct. Reducing it modulo `B^j` gives
`B^j | A^j*((A-B)*x_0+H)`; coprimality removes `A^j`. Since `B>1`,
divisibility by every `B^j` forces that single fixed integer to vanish.
Thus the quotients at the chosen phase are constant, and periodicity of
the residues and differences makes the original pair repeat exactly.

Both coordinates of a positive orbit are nondecreasing. Exact repetition
forces each intervening increment to be zero, which implies `a<30` and
`b<20`. Positivity bounds their product by 551. The product at the chosen
phase is at least its initial value 600, a contradiction. The transient,
period 1, and the inclusive threshold 600 cause no exception. This excludes
ultimate periodicity of the full `(d,r)` state only; periodicity of `d`
alone is not excluded.

## Extension's local estimates and boundary audit

The positive rule's floor bounds hold for every integer `h>0`: at `h=1`
the next difference is zero, and for `h>=2` it lies between a positive
lower bound `0.9h-1.5` and `h-1`. The smallest lower-bound case `h=2`
is positive. Thus repeated positive control terminates in at most `h`
further steps.

For `h=-k`, the floor argument is less than 1, giving an increase of at
least 2. The direct cases `k=1,2,3` are 1, 0, -1. For `k>=4`, the strict
floor inequality gives a strictly negative result; the endpoint `k=4`
has upper bound -0.6. Hence the difference remains negative while its
magnitude decreases until -2 or -1, then reaches 0 or 1, with 1 mapping
to 0. The bound `ceil(k/2)+1` is valid, albeit loose in some even cases.
The initial 60-residue maximum is a valid local path bound. The defect
occurs only when reusing that initial bound after arbitrary prefixes.

There are no additional cited-theorem hypotheses beyond the established
strip fact. The proofs otherwise use floor identities, coprime integer
divisibility, finite residue counts, monotonicity, and elementary density
inequalities, all reconstructed above.

## Reproducible finite evidence and checkpoint

All computations below are finite evidence. They neither prove universal
equality nor supply an infinite positive integer lift.

Run from the repository root:

```text
.venv/bin/python problems/2022-B4/reviews/review-1-evidence.py
```

Files owned by this review:

- `review-1-evidence.py`: exact standard-library integer and rational checks;
  supervisor launches a dedicated subprocess with a 40-second timeout.
- `review-1-evidence-job.json`: exact executable/command, child PID, working
  directory, timeout, elapsed time, return code and log path.
- `review-1-evidence-output.txt`: incremental checkpoints and exact outputs.

The initial run completed in under one second, return code 0. It checked
72,300 quotient updates; 4,200 shifted-state comparisons; 1,080 complete
finite lifting bijections for lengths 1-3; all 2,220 strip states under the
stated control policy; arbitrary-difference local bounds for 2,005 test
differences and paths for 12,060 initial states; 480 finite delay instances;
and 480 exact affine-identity instances. Independent reverse breadth-first
search on the strip graph gave maximum abstract minimum hitting distance
12, consistent with the analytic 24-step upper bound. The counterexample's
continuation layers contain 10, 40, 70, and 90 states at lengths 1-4;
equality first becomes possible in the fourth layer.

All commands finished. No CAS jobs are outstanding, no unrelated process
was stopped, no dependency was installed, and no commit or push was made.
The temporary rendered official source page was removed after visual
inspection, so a full third-party page is not left for accidental tracking.
The substantive objection is ready for coordinator issue-log integration and
author repair. R1's initial audit is complete before any comparison with R2.
