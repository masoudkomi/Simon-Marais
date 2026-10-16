# First-order four-witness projection: a documented limitation

2026-10-16 UTC. **Computational evidence; unverified exploratory reduction.**
This is not a mask exclusion or a proof of the four-witness case. It uses
the separately accepted T2 for J=16: multiplicity 2 at zero and rational
small roots u,v, both with positive integral 19-adic valuation.

There are 5,794,470 assignments of noncenter equations to 0,U,V across
the 88 masks. Requiring both U,V and identifying their swap leaves
2,843,039. Blind exact bivariate elimination at that scale is not justified
without a stronger reduction. This first-order test makes a smaller projection.

For each mask let a_j^0 be the exact integer coefficient recursion with
all noncenter choices zero. At a noncenter position, modulo 19^2,

    a_j = -j*a_(j-1)^0*w_j,

because all higher powers of w_j vanish modulo 19^2. Only positions
where a_(j-1)^0 is a unit matter at first order. There are 11,316
projected label assignments in total. Write u=19*u1,v=19*v1 and

    a_j = a_j^0 + 19*(A_j*u1+B_j*v1) mod 19^2.

Let q0=f_(0,0)(1)/19. Its valuation bounds min(v19(u),v19(v)) from above:
all nonconstant terms of the integral polynomial f_(u,v)(1)/19 have
valuation at least that minimum. Here q0 is nonzero for each mask;
84 masks give bound 1 and four give bound 2.

Two necessary linear constraints on residues u1,v1 are checked:

    q0/19 + sum_j (binom(20,j)/19)*(A_j*u1+B_j*v1) = 0 mod19,
    a_18^0/19 + A_18*u1+B_18*v1 = 0 mod19.

The first lifts the divided center-root equation one order. The second
uses v19(c_2)=1+v19(u)+v19(v)>=3, hence 19^2 divides a_18.
When v19(q0)=1, the pair (u1,v1)=(0,0) is forbidden. It is retained as
necessary excess when that bound is 2. The test permits residue-zero
u1 or v1 and does not assume distinct leading residues.

All 361 residue pairs were tested for every projected assignment.
**Every one of the 88 masks survives.** No mask, lift or rational
counterexample is thereby established. Second-order constraints or a
different structural argument are needed; repeating this same projection
at a larger enumeration cap would not answer that need.

Script: `computations/coordinator-J16-linear-projection-v1.py`, SHA-256
`db576a4964fae433062536feb7e6538ecbe1b7805bc4416214f740c987f0760f`.
Result: `computations/coordinator-J16-linear-projection-v1-result.json`,
SHA-256 `ab337f4be8191d75e9996633698749cd4292777b5cd3df27b606bd68caf53b56`.
Dedicated child PID 35969 completed in 1.037 seconds under an explicit
30-second timeout, exit 0, reaped. Exact parameters and output are saved;
no native CAS, global process kill, or paid API was used. The formulas
and their possible use in a proof would need independent mathematical audits.
