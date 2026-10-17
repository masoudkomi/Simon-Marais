# 2022 B4 research log

## Current reviewed arithmetic result

The rational-lift complexity obstruction is **proved, independently
reviewed (partial result)** after two fresh blind whole analytic audits.
A rational Z10 controller lift is eventually periodic in full state or
has correction-factor complexity lower slope log10/log(11/10). Every
admissible actual integer orbit has the latter lower bound. Explicit
mechanical avoiding paths have irrational lifts, while every finite prefix
has positive integer lifts. See proofs/reviewed-arithmetic-complexity-v1.1.md
and reviews/arithmetic-complexity-acceptance.md/json. The mechanism adapts
Dubickas2009, Theorem3/Section4. No novelty or universal equality result
is claimed. Arbitrary high-complexity integer avoiding paths remain open.
Earlier checkpoint text below is historical.

Status: initial research pass and first repair checkpoint completed
2026-10-16; no full solution claimed. Two independent blind initial audits
found no substantive defect in v1 P1-P4 and found a blocking uniformity error
in v2's repeated-block count. Frozen v1/v2 and the review reports are preserved.
The separate v3 repair is **candidate proof - unverified**, awaiting both
affected-argument re-audits. No author promotion or novelty claim is made.

Requested agent settings: `gpt-6.1-sol`, `max` reasoning. The coordinator
reported no independent effective-setting readback; these are requested
settings, not verified effective settings. Only this year directory was
edited; no worker commits, pushes, installs, or subagents were used.

## Statement checks

Checked the cached official paper with pypdf 6.10.0 and the live primary PDF
on 2026-10-16. The variables are positive integers, the product threshold
is inclusive at 600, updates are simultaneous, and n=0 is allowed. The
paper identifies (b) as open as issued. Part (a) was not investigated or
reproduced; its established invariant strip is attributed context only.

## Approaches and results

1. **Exact finite search, evidence only.** All 246,278 admissible starts in
   `1<=a,b<=500` hit equality within 3,204 steps; the maximum is at (399,7).
   All 369,180 admissible starts with `1<=b<=10000` and `-13<=a-b<=23`
   hit, maximum 3,173 at (3735,3712). All 10,000 seeded pairs of up to
   256 bits hit: one capped at 5,000 was continued exactly and first hit
   at 5,119. All 20,000 seeded starts of up to 1024 bits already within
   the strip hit, maximum 3,056. See computations/README.md for parameters,
   commands, output hashes, exact records, and limitations. These searches
   neither prove the universal statement nor rule out rare exceptions.
2. **Congruence obstruction attempt.** `a mod2` and `b mod3` are invariant.
   A diagonal value with both residues always exists by CRT. For a linear
   expression `u*a+v*b mod m` to be invariant for all allowed starts,
   varying the two floor quotients independently forces `m|2u` and
   `m|3v`; these universal linear congruences add no incompatible equality
   condition. This does not exclude nonlinear or orbit-specific obstructions.
3. **Residue/carry quotient.** With `b=60q+r`, equations (1)-(2) in proof.md
   give a finite state `(d,r)` and a ten-valued control `q mod10`. The
   graph on the established strip has 2,220 vertices and 22,200 controlled
   edges. Removing d=0 leaves many cyclic components; 2,112 vertices admit
   arbitrarily long abstract avoiding walks. Thus merely finding graph
   cycles cannot answer (b). Every finite path has an exact integer lift,
   but an infinite path gives a nested congruence condition, potentially
   only a 10-adic integer rather than an ordinary positive integer.
4. **Candidate density theorem.** The control can choose the next residue
   in a six-integer interval. Residues 30,...,35 lower a positive ensuing
   difference; residues 20,...,25 raise a negative ensuing difference.
   A finite lifting/counting argument gives a candidate natural-density-one
   hitting result on every fixed line `(a,b)=(b+d,b)`. The first draft in
   proof.md restricts d to the established strip; proof-extension-v2.md
   attempted the extension to every integer d, but its initial-only path
   bound cannot be reused after arbitrary prefixes. Both independent audits
   supplied counterexamples to that intermediate assertion. The standalone
   proof-extension-v3.md repairs the count using a uniform auxiliary radius
   M=max(abs(initial difference),29) and fixed K=M+1 at every reached state.
   It does not use or re-prove preliminary (a). No computation is a premise
   of the analytic repair. A density-zero exceptional set can still contain
   positive integers; that is the exact unresolved gap. See repair-v3-notes.md
   and issues.md for the failed version, repair, evidence and review status.
5. **Arbitrary finite delay.** The explicit family
   `b0=60*10^N*t+r, a0=b0+1` (`N,t>=1`, `0<=r<=19`) has difference 1
   through time N, by an exact formula in P3. This blocks any universal
   fixed-step equality bound, including for starts already in the strip.
   It is not a counterexample; the later behavior is not determined here.
6. **Periodic and affine-periodic attempt.** P4 gives a candidate proof
   that an ultimately periodic full state `(d,b mod60)` cannot occur for
   an admissible orbit: after one period the quotient would obey
   `x'=(11^p*x+H)/10^p`; integrality for all repetitions forces a fixed
   quotient and hence a forbidden stationary original pair. This rules out
   the direct periodic lift of graph cycles. It does not exclude periodic
   differences with nonperiodic residues, or nonperiodic avoiding paths.
7. **Random-walk heuristics.** The organizer report attributes experiments
   to Chris Tuffley and describes random-walk-like differences. This is
   useful motivation only; no independence, normality of digits, or
   stochastic recurrence theorem has been assumed for an individual orbit.

## Next steps

- Obtain both independent affected-argument re-audits of v3 Sections 3-6,
  including reconstruction of the uniform finite lifting/counting proof.
  Both blind initial reports are already complete and immutable. Only the
  coordinator may promote any partial result after resolving objections.
- Investigate whether a nonperiodic avoiding path can have a nonnegative
  integer quotient lift. Repeated abstract cycles alone are insufficient.
- Explore stronger arithmetic constraints on an eventually constant
  nonzero difference, keeping this within (b) rather than redoing trapping.
- Investigate an explicit quantitative tail bound in terms of the size of
  an initial integer. Current density counting has no pointwise guarantee.
- Further literature verification may locate a later resolution or an
  existing form of the partial density argument. Search failure is not
  evidence that no such work exists.
# Coordinator acceptance update, 2026-10-16

The v3 fixed-offset density theorem and supplementary v1 partial claims are now **proved, independently reviewed (partial results)**. Both blind initial audits accepted v1 and independently found the genuine v2 uniformity error. The author supplied a separate v3 repair; both independent re-audits fully reconstructed it and closed the objections. See proof.md, proofs/reviewed-density-v3.md and reviews/acceptance.md. V2 remains a preserved failed proof version. Historical owner-stage pending-audit notices below are superseded by this update. The full universal equality question and novelty remain unresolved.
