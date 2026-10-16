# Uniform remainder equations for further J=16 digits

2026-10-16 UTC. **Candidate proof - unverified.** New co-constructor:
`owner_2021_hensel`. This work cannot count as either independent audit of
the coordinator's combined leading/digit argument. It is a partial
necessary-condition investigation for 2021 B4(b), not a degree-20 proof
or the annual classification, and no novelty is claimed.

Requested launch settings: `gpt-6.1-sol`, reasoning `max`. The worker
inherited the parent model/settings. Effective-setting readback is not
available. The source code records requested and verified-setting status
separately.

## Inputs and scope

The reviewed [rational witness register](coordinator-three-rational-witnesses-reviewed-v1.1.md)
accepts T1--T3 and their frozen proof. In particular T1 says that a
nontrivial rational degree-20 counterexample cannot have all derivative
witnesses covered by at most three distinct rational roots. T2 gives,
in the specified J=16 normalization,

    f = X^2 (X-1) (X-u) (X-v) g,

where the complete rational root set is `{0,1,u,v}`, the nonzero small
roots `u,v` are distinct with positive integral 19-adic valuations, and
the residual `g` is Eisenstein of degree 15. These facts are accepted
dependencies; they are not independently reviewed again here.

The coordinator's leading constraints, 768 leading branches and restored
840396 full label/residue/minimum-valuation branches are **unverified**
construction inputs. The combined L1--L3 proof was subsequently frozen
as `coordinator-J16-coupled-digit-candidate-v1.md`, SHA-256
`2fa8c3ad1ccea46350c7d8ae76d9463b332e2be636e48f48dbcbff7cad85c801`.
The old second-digit certificate stream is compared to the new formula
only as a constructor cross-check. Agreement does not supply an
independent audit of either construction.

## A pruning consequence of accepted T1

Fix a full assignment of all selected normalized derivative conditions
of indices `j=2,...,18` to `1,0,u,v`, with center assignments encoded by
the canonical mask. The derivative orders are `20-j`. The first
derivative already uses `0` and the derivative of order 19 already uses
`1` in the normalization. If the full assignment never uses `u`, all
19 derivative conditions are therefore witnessed by the set `{0,1,v}`.
This contradicts T1. The same applies if it never uses `v`.

Consequently a full family whose `U_mask=0` or `V_mask=0` cannot
specialize to an actual counterexample. This applies even when an unused
formal variable is still required to be a root by the other equations:
the other three values already cover all derivative witnesses.

This does **not** justify removing any residue pair with `U=V`. Distinct
19-adic numbers can agree to arbitrarily many finite digits. No finite
coincidence of residues is discarded in this construction.

## Exact equations without dividing by u-v

Put `p=19`, `q=p^nu`, `u=qU`, `v=qV`, where `nu` is 1 or 2 on the
candidate leading cover. At least one of `U,V` is a unit. For each
fixed full derivative assignment define integer polynomials recursively:

    a_0=1, a_1=-1,
    a_j=-sum_(h<j) binom(j,h) a_h w_j^(j-h),       2<=j<=18,

where `w_j` is `1,0,u,v` according to the assignment. Then

    f = X^20 - 20 X^19
        + sum_(j=2)^18 binom(20,j) a_j X^(20-j).

This full recurrence is exact and uses no division. Let

    beta_j = binom(20,j)/19,      2<=j<=18,
    Ptilde = f(1)/19 = -1+sum beta_j a_j,
    F=f/X^2.

The coefficients of `F`, in ascending degree, are

    c_(e+2)=19 beta_(18-e) a_(18-e),     0<=e<=16,
    c_19=-20, c_20=1.

Divide `F` by the monic quadratic `X^2-sX+t`, with `s=u+v`, `t=uv`,
and call its remainder `R_1 X+R_0`. Monic division has integer
polynomial coefficients. In an actual T2 example the displayed
factorization gives `Ptilde=R_0=R_1=0` exactly. Neither the construction
nor these conditions divide by `u-v`.

Define the normalized necessary equations

    E_0 = Ptilde/q,
    E_1 = R_0/(19 q beta_18),
    E_2 = R_1/(19 q),                         beta_18=10.

Their coefficients lie in `Z_(19)[U,V]` whenever the leading constant
prerequisites `q|Ptilde(0,0),a_17(0,0),a_18(0,0)` hold. The leading
construction checks those prerequisites for every retained `nu`.

For a direct verification put `S=U+V`, `T=UV`, `h_0=0`, `h_1=1`, and

    h_e=S h_(e-1)-T h_(e-2),       k_e=-T h_(e-1).

Then the remainder of `X^e` at the actual `u,v` is
`q^(e-1)h_e X + q^e k_e`, for `e>=1`. In the formulas below the
`a_j` are evaluated at `(qU,qV)`:

    E_0=(-1+sum beta_j a_j)/q,

    E_1=a_18/q
       + beta_18^(-1) sum_(e=2)^16
             beta_(18-e) a_(18-e) q^(e-1) k_e
       + beta_18^(-1) sum_(e=17)^18
             c_(e+2) (q^(e-1)/19) k_e,

    E_2=beta_17 a_17/q
       + sum_(e=2)^16 beta_(18-e) a_(18-e) q^(e-2) h_e
       + sum_(e=17)^18 c_(e+2) (q^(e-2)/19) h_e.

The quotients `q^r/19` in the last terms are exact integers. Those
terms have valuation at least 15 in `E_1` and at least 14 in `E_2`
for `nu>=1`. The code nevertheless includes the two unit coefficients
explicitly, and the exact integer division cross-check retains them.

Every nonconstant monomial in `a_j(qU,qV)` has a factor `q`. The
three leading constant prerequisites therefore make the displayed
divisions by `q` integral. Every other displayed summand is integral
over `Z_(19)` because `beta_18=10` is a 19-adic unit. This proves the
claimed integrality without assuming an exact root at a test residue.

## One Jacobian for every subsequent digit

Write `a_j^0=a_j(0,0)` and let `A_j,B_j` be the coefficients of `u,v`
in the unscaled integer polynomial `a_j`, reduced modulo 19. Terms of
degree at least two in `a_j(qU,qV)/q` have a coefficient divisible
by 19. At a center index,

    A_j=-sum_(h<j) binom(j,h) A_h                 modulo19,

and similarly for `B_j`. At a noncenter index labeled `u`, the linear
coefficient is `A_j=-j*a_(j-1)^0`, `B_j=0`; the roles swap for label
`v`, and both are zero for label `0`. This reconstruction uses the
complete assignment and does not rely on active-label compression.

Let `C4=beta_16*a_16^0 mod19`. Reducing the three exact equations gives
the affine system

    E_0 = Ptilde(0,0)/q + sum beta_j (A_j U+B_j V),
    E_1 = a_18^0/q + A_18 U+B_18 V,
    E_2 = beta_17*a_17^0/q
          +(beta_17 A_17+C4)U+(beta_17 B_17+C4)V       modulo19.

All terms of parameter degree at least two carry a factor 19. The
Jacobian of `E=(E_0,E_1,E_2)` modulo 19 is therefore the constant matrix

    M = [sum beta_j A_j,       sum beta_j B_j]
        [A_18,                B_18             ]
        [beta_17 A_17+C4,     beta_17 B_17+C4 ].

Suppose the current pair satisfies `E(U,V)=0 mod19^k`, `k>=1`.
For the next digits `dU,dV` in `F_19`, polynomial expansion over
`Z_(19)` gives

    E(U+19^k*dU,V+19^k*dV)
       =E(U,V)+19^k M*(dU,dV)^t        modulo19^(k+1).

Terms quadratic in the changes have valuation at least `2k>=k+1`.
Thus the complete next-digit fiber is the affine linear system
`M*(dU,dV)^t=-E(U,V)/19^k mod19`. Gaussian elimination returns all its
solutions. A consistent rank-2 system has one, a consistent rank-1
system has 19, and a rank-0 system has 361. Inconsistency has none.
The implementation supports all ranks, even though only ranks 1 and 2
were present in the old second-digit data.

All returned digits preserve the nonzero minimum-valuation residue.
No unit condition is added to a variable whose leading residue was
zero; it may have larger actual valuation. No inequality of finite
`U,V` representatives is imposed. Hence the procedure does not remove
distinct roots merely because they are 19-adically close.

## Exact computation and current limits

`computations/owner-J16-Hensel-v1.py` is a new constructor implementation
using Python's standard library. It imports no mathematical helper from
the previous constructor. It reads the leading branch cover and expands
each inactive label in the same recorded order, then compares every
first next-digit key, residual, matrix rank and consistency flag against
the previous second-digit certificate stream.

For each node at precision `k`, the `a_j` are evaluated modulo
`19^(nu+k+1)`. At a noncenter index the recurrence can omit precisely
the powers `w^e` with `nu*e>=nu+k+1`. This threshold follows from
`19^nu|w` and the integrality of every earlier coefficient. The code
then evaluates the exact scaled-remainder formulas modulo `19^(k+1)`.
The recorded certificate includes the key, coefficient modulus, all
19 coefficient residues, all three residuals, the matrix, its reduced
augmented rows, any T1 pruning reason, and every next-digit solution.
The output node stream is separately hashed and compressed.

The fixed exploratory target is `E=0 mod19^4`, with **at most one
million nodes at each level** and a single dedicated full-run child
timeout of 300 seconds. If the next level would cross the cap, the code
closes its artifacts, marks the traversal incomplete and stops; it does
not raise the cap. A timeout kills only the recorded child PID and
reaps it. This is a fixed precision calculation, not a height search
or a proof that a surviving residue lifts indefinitely or rationally.

Before the full run, 12 deterministic cases covering the available
`nu` and low-center flag types passed comparison with
untruncated integer construction and monic division. The same cases
passed finite-difference Jacobian checks at precisions 1, 2 and 3 and
brute-force comparison of all 361 affine digit pairs. Full integer
coefficients, remainders and exact fractions are preserved in the
self-test artifact. These are constructor checks, not review credit.

The deliberately incomplete 8192-initial-node benchmark (child PID
47539) finished in 0.557891 seconds of worker time, exit 0, under a
60-second external timeout. All 8192 prior stream rows matched. It
generated 2666 precision-2 nodes after T1 removed 128 input assignments;
2730 parents were consistent before the T1 removal. This gives no
complete-cover mask exclusion. The measured rate projected about
57 seconds for the first full level, so the predeclared full run was
started with PID 47605 under the unchanged 300-second timeout.

Commands from the repository root:

    python3 -u problems/2021-B4/computations/owner-J16-Hensel-v1.py --benchmark
    python3 -u problems/2021-B4/computations/owner-J16-Hensel-v1.py

Python executable: `/usr/local/bin/python3`. No CAS, dependency install,
paid API, charge, third-party paper copy, Git commit, push, shared-file
edit, promotion or subagent was used by this worker. Weekly account-wide
telemetry was 11% total used at the beginning of this task, with reset
`1792745187`; the stop threshold remains 90% total weekly usage.

The full child PID 47605 completed, exit 0 and reaped, in 80.909070
seconds supervisor time (80.769892 seconds worker time) under the
unchanged 300-second timeout. Every one of the 840396 previous digit
records matched exactly, including all rank/consistency counts. There
were no zero leading residues for either variable in the actual input
cover, although the equations and implementation allow that case.

The complete finite results are:

| Input precision | Input nodes | Output precision | Output nodes | Masks remaining |
|---|---:|---|---:|---:|
| 1 | 840396 | 2 | 361194 | 58 |
| 2 | 361194 | 3 | 2026 | 31 |
| 3 | 2026 | 4 | 90 | 8 |

The first level visits all input assignments before applying the T1
pruning, so it can compare the entire previous stream. T1 removes 14248
assignments, 384 of which had a consistent rank-2 next-digit system.
Before this pruning the old counts are reproduced exactly: 112222
consistent rank-2 parents, 13124 consistent rank-1 parents, 373610
inconsistent rank-2 parents and 341440 inconsistent rank-1 parents.
The retained precision-2 nodes are `111838+19*13124=361194`.

At the second lifting level every one of the 249356 rank-1 nodes is
inconsistent, as are 109812 rank-2 nodes; 2026 rank-2 nodes remain.
At the third lifting level all 2026 nodes have rank 2; 1936 are
inconsistent and 90 remain. The final masks and node counts are:

| Center mask | Precision-4 nodes |
|---:|---:|
| 51495 | 2 |
| 55584 | 36 |
| 56407 | 4 |
| 58480 | 36 |
| 58898 | 6 |
| 59703 | 2 |
| 62251 | 2 |
| 89160 | 2 |

Conditional on the complete unverified leading cover and all arguments
here, this would exclude 80 of the 88 original J=16 masks, including
50 additional exclusions beyond the previous second-digit test. The
combined 772-mask necessary cover would contain 692 rather than 742
masks. These are **candidate consequences**, not accepted counts.
The 90 surviving states are residue approximations only.

A separate exact constructor post-check
`owner-J16-Hensel-v1-postcheck.py` rebuilds all 90 states by untruncated
integer Horner derivative evaluation, followed by two-state Horner
evaluation in `Z[X]/(X^2-(u+v)X+uv)`. All exact `E` values vanish
modulo `19^4`. The result stores every integer coefficient, exact
remainder and normalized fraction, family key, matrix and all three
2-by-2 minors. Every matrix has a nonzero minor, hence rank 2. Every
state's root-label swap is present. The post-check child PID 50878
finished, exit 0 and reaped, in 0.072300 supervisor seconds under its
30-second timeout. This is co-construction verification only.

All 90 final matrices have rank 2, and the matrix depends only on the
fixed family, not on later root digits. Thus at most one child can ever
arise from each of these 90 states at each subsequent precision. This
gives a structural bound of 90 nodes per future level, independent of
observed runtime. The coordinator has authorized a **separate v2**
extension to a fixed precision 8 with this bound and a 30-second child
timeout. The v1 precision target and all frozen v1 artifacts are kept
unchanged.

The v1 artifact manifest is
`owner-J16-Hensel-v1-manifest.json` in this notes directory. It includes
all same-prefix source, result, job, self-test, coefficient/certificate
and node streams, including the incomplete benchmark. Python was
3.15.0, with no third-party dependency. Weekly telemetry was rechecked
after the full run and remained at 11% total used, reset `1792745187`.

All new claims remain candidate and require two fresh independent
adversarial audits, including a reconstruction of the whole mathematical
coverage argument and exact finite streams. No reviewer work was read
and no reviewer was contacted by this constructor.
