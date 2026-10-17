# 2022 B4(b): arithmetic reasoning checkpoint

2026-10-16 UTC. All new deductions below are **candidate proof -
unverified** or explicitly failed leads. Nothing in this note promotes a
result. The universal equality question remains unresolved.

## Assignment and provenance

Worker owns only the `notes/arithmetic-reasoning-*` and optional
`computations/arithmetic-reasoning-*` prefixes. No shared proof, reference,
issue-log, Git, or coordinator-owned file was edited. No subagent was
spawned. Requested settings are `gpt-6.1-sol`, `max`; effective-setting
readback was unavailable. Latest coordinator-supplied telemetry during
this pass was 17% total weekly used, at 2026-10-16 21:52 UTC, with the same
reset previously reported as Unix 1792745187. This is a relayed readback,
not a fresh worker-side account-wide telemetry call.

Inputs read: `AGENTS.md`, the year's normalized official statement,
`proofs/reviewed-partials-v1.md`, `proofs/reviewed-density-v3.md`, their
acceptance, `notes/rational-base-lead-v1.md`, and
`notes/deep-literature-coordinator-v1.md`. Preliminary part (a) was used
only as attributed strip context. No preliminary solution was constructed
or reproduced.

## Main successful direction, pending audits

The frozen candidate is
`arithmetic-reasoning-complexity-candidate-v1.md`, SHA-256
`e9c24e96982d1d2a74aa97cb5fd045a3319f37c69316fbada884eeec0a0412d3`.
Its exact claim is a rational-lift dichotomy: an infinite strip-controller
path with rational \(10\)-adic lift either has an ultimately periodic
full state, or its correction word has lower factor-complexity slope at
least \(\log10/\log(11/10)\). Identical correction factors give
\(10^L\mid v(Q_m-Q_n)\) after clearing the fixed denominator \(v\).
The real growth identity makes a nonzero difference too small for this
divisibility if the repeated factor occurs too early. A bounded rational
lift lies in a fixed discrete lattice and a finite deterministic state
space, so it is ultimately periodic.

The ordinary positive integer application audits the small-quotient
exception explicitly. Bounded coordinates would eventually be fixed and
give product at most \(29\cdot19=551\), incompatible with the official
product condition and nondecreasing coordinates.

Two explicit two-step avoiding loops at difference 1 have correction
words \((0,0)\) and \((-1,1)\). Mechanical binary coding of these loops
gives nonperiodic avoiding paths with factor complexity at most \(L+3\).
The candidate consequently forces their unique \(10\)-adic lifts to be
irrational. This excludes an explicit uncountable structured family of
infinite avoiding controllers. It does not exclude high-complexity
avoiding paths.

After freezing, a focused literature search located Dubickas's original
2009 complexity bound and its exact divisibility-versus-growth proof for
scalar ceiling iteration. The separate
`arithmetic-reasoning-complexity-attribution-v1.md` supplies the citation
and precise scope. The candidate is an adaptation of that known method
to signed rational controller lifts, not a new complexity technique. Both
the mathematical candidate and this attribution must accompany audits.

## A separate exact reduction: an eventually constant nonzero difference

This is an unreviewed structural reduction, not an exclusion theorem.
Suppose an actual orbit in the strip has \(d_n=d\ne0\) for all sufficiently
large \(n\). At every such step,

\[
2\left\lfloor\frac r{20}\right\rfloor
=3\left\lfloor\frac{r+d}{30}\right\rfloor.
\]

The first floor is in \(\{0,1,2\}\). Coprimality of 2 and 3 forces
both floors to be zero. Hence the only possible residues lie in

\[
J_d=[\max(0,-d),\min(19,29-d)]\cap\mathbb Z.
\tag{R1}
\]

In particular \(c=0\), so
\(b'=b+6\lfloor b/60\rfloor\). The residue \(\rho=b\bmod6\) is
constant. For the ordinary integer \(B=(b-\rho)/6\),

\[
B'=B+\left\lfloor\frac B{10}\right\rfloor
=\left\lfloor\frac{11B}{10}\right\rfloor,
\qquad
B\bmod10\in T_{d,\rho}:=
\{t\in\{0,1,2,3\}:6t+\rho\in J_d\}.
\tag{R2}
\]

Conversely, a scalar orbit satisfying (R2), with
\(b=6B+\rho\) and \(a=b+d\), gives an actual constant-difference
orbit as long as its starts have the official positivity and product
hypotheses. This follows by substituting the zero floors from (R1) into
the simultaneous recurrence.

There is an exact scalar translation here, specific to this restricted
situation. For any integer \(B\), put \(X=B-9\). Since a multiple of
\(1/10\) has only the ten possible fractional parts,

\[
\left\lfloor\frac{11B}{10}\right\rfloor-9
=\left\lfloor\frac{11X}{10}+\frac9{10}\right\rfloor
=\left\lceil\frac{11X}{10}\right\rceil.
\tag{R3}
\]

Thus eventual constant nonzero difference requires a positive scalar
ceiling orbit eventually confined to residues \(\{1,2,3,4\}\pmod{10}\),
or a smaller interval subset determined by \(d,\rho\). To see positivity
at an admissible constant-difference phase, if \(B\le9\), then
\(b=6B+\rho<60\), so \(r=b\) and (R1) gives \(b\le19\),
\(a=b+d\le29\). This would force \(ab\le551\), a contradiction.
Therefore \(B\ge10\) and \(X\ge1\).

No proof was found that this scalar residue confinement is impossible.
The published scalar normality conjecture would exclude it but cannot
be used as a theorem. The complexity bound does not exclude arbitrary
four-letter high-complexity words. This exact restricted conjugacy must
not be confused with the false identification of the general contest
quotient \(Q=\lfloor b/60\rfloor\) with a scalar ceiling orbit.

## Failed or incomplete approaches kept for the next pass

1. The real and \(10\)-adic expansions of the signed correction series
   cannot simply be equated. For an ordinary rational lift they give the
   real asymptotic growth constant and an inverse-limit initial value in
   different convergence settings. A sign bound on the real sum alone
   does not rule out an integer \(10\)-adic limit.
2. A finite avoiding controller has many nonperiodic paths. The two
   explicit loops already support arbitrary binary concatenations.
   Finite state space supplies no universal linear upper bound on the
   factor complexity of those individual paths.
3. Matching a finite controller prefix to a positive integer start at
   every depth gives only the \(10\)-adic inverse-limit lift. It does
   not make that lift an ordinary positive integer. The mechanical loop
   family is a proposed explicit irrational-lift illustration of the
   difference, pending audits.
4. The existing right normalizer was not used. A causal forward
   conjugacy, and the source's domain for arbitrary signed finite words,
   remain separate issues; this note does not assume either.
5. Eventual constant difference has a useful exact scalar reduction
   (R1)-(R3), but replacing the general recurrence by that reduction would
   discard all paths with changing differences.

## Computation, commands, and source read scopes

No orbit enumeration, CAS operation, native long-running child, new
dependency, or mathematical computation was used as a premise. The only
numerical calculation was a displayed decimal for a proved logarithmic
constant. A standard-library Python command computed it and fingerprinted
the frozen candidate:

```text
python3 -c 'import hashlib,json,math,pathlib; p=pathlib.Path("problems/2022-B4/notes/arithmetic-reasoning-complexity-candidate-v1.md"); print(json.dumps({"path":str(p),"sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"kappa":math.log(10)/math.log(1.1),"alpha":math.log(1.1)/math.log(10),"bytes":p.stat().st_size},indent=2))'
```

It exited 0 immediately and printed:

```json
{
  "path": "problems/2022-B4/notes/arithmetic-reasoning-complexity-candidate-v1.md",
  "sha256": "e9c24e96982d1d2a74aa97cb5fd045a3319f37c69316fbada884eeec0a0412d3",
  "kappa": 24.15885792809679,
  "alpha": 0.04139268515822507,
  "bytes": 12810
}
```

Here `alpha` in the command means the reciprocal logarithmic slope,
not the independent irrational rotation parameter in the candidate.
No Python module outside the standard library was imported.

Read-only source searches used `rg --files`, `cat`, and `ls` to locate
the existing statements and cached literature metadata. Web searches
were `"rational base" "minimal words" "complexity"`,
`"rational base" "factor complexity"`,
`"Dubickas" "On integer sequences generated by linear maps" pdf`, and
`site:mif.vu.lt dubickas linear maps 2009`. Technical claims were checked
against the primary arXiv paper's introduction and the original publisher
PDF, not search snippets or third-party descriptions. Complete source
URLs, theorem pages, retrieval date, and scope are in the attribution
supplement. No full third-party PDF was downloaded by this worker.

## Handoff

The coordinator was sent the frozen path and hash, the mathematical
scope and bounded-orbit audit, the attribution discovery, and the exact
remaining gap. Two fresh independent adversarial reviewer agents must
audit the candidate before any status change; one must reconstruct the
whole argument. The worker made no Git commit or push.
