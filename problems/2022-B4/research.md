# 2022 B4 research log

Status: initial research pass completed 2026-10-16; no full solution claimed.
Two partial proof drafts are **candidate proof - unverified**. No independent
reviews have been completed, and no novelty claim is made.

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
   extends the analytic control to every integer d without using preliminary
   (a). No computation is a premise of the proof. A density-zero exceptional
   set can still contain positive integers; that is the exact unresolved gap.
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

- Obtain two independent adversarial reviews of the partial candidates,
  one reconstructing the finite lifting and density proof. Keep both
  initial reports blind to each other's conclusions. See issues.md.
- Investigate whether a nonperiodic avoiding path can have a nonnegative
  integer quotient lift. Repeated abstract cycles alone are insufficient.
- Explore stronger arithmetic constraints on an eventually constant
  nonzero difference, keeping this within (b) rather than redoing trapping.
- Investigate an explicit quantitative tail bound in terms of the size of
  an initial integer. Current density counting has no pointwise guarantee.
- Further literature verification may locate a later resolution or an
  existing form of the partial density argument. Search failure is not
  evidence that no such work exists.
