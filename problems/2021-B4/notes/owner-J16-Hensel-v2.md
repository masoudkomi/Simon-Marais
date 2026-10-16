# Bounded extension eliminates the remaining J=16 digit cover

2026-10-16 UTC. **Candidate proof - unverified.** Constructor:
`owner_2021_hensel`, as a new co-constructor. No independent review
credit is claimed. This note concerns only 2021 B4(b), the J=16 case
of a possible nontrivial rational degree-20 example. It does not solve
degree 20 or the full annual classification, and no novelty is claimed.

Requested model/reasoning: `gpt-6.1-sol` / `max`; effective-setting
readback unavailable. The account-wide weekly usage was 11% total used,
reset `1792745187`, before and after the precision-four run. The
90% total-used stop threshold and review/integration reserve are retained.

## Fixed inputs and structural budget

This extension uses the exact integrality, monic quadratic remainder and
constant-Jacobian derivation in the frozen
[v1 note](owner-J16-Hensel-v1.md), SHA-256
`990661fa1cb7c173efa406437d6c9481edf80861a64609a73ec4f5b077c5b9dc`.
Its 53-artifact manifest is `owner-J16-Hensel-v1-manifest.json`, SHA-256
`2f5eec6a98e0ff8c264259a508868c3d0e5f5befa8de833a9434dfd7fc069f6a`.
All v1 files remain unchanged. In particular the previously fixed v1
precision-four run was not relabeled as a longer run.

The v1 exact post-check preserves the full state and matrix for every
one of the 90 surviving nodes, with SHA-256
`6eee254cd548d78c68c02348945fac4b42dffeea78f7c622da23019561c27f0b`.
Each 3-by-2 matrix has a nonzero 2-by-2 minor, so its rank is 2 over
`F_19`. The matrix is fixed by the full derivative family and remains
the Jacobian modulo 19 for every later digit of the same two roots.
Every consistent next-digit system therefore has exactly one child.
It follows by induction that no future layer can have more than 90
nodes. This is a structural bound, independent of a runtime estimate
or a successful short computation.

On that bound the coordinator explicitly authorized a **new v2** run
to a fixed target precision 8, a stricter cap of 90 nodes per level and
a 30-second external child timeout. The run stops earlier if a layer
is empty. No cap or target is raised during this run.

## Exact finite extension

The source `computations/owner-J16-Hensel-v2.py` checks the frozen
source and state hashes before loading any v1 helper. This is explicit
constructor reuse, not an independent implementation or review. For
each input pair `(U,V)` at precision `k=4,...,7`, it also performs a
new **untruncated integer** construction:

1. Rebuild every normalized derivative coefficient by Horner evaluation
   of the full integer recurrence.
2. Form every coefficient of `F=f/X^2`, including `c19=-20,c20=1`.
3. Compute its exact remainder by Horner evaluation in
   `Z[X]/(X^2-(u+v)X+uv)`.
4. Form the exact rational numbers
   `E=(f(1)/(19q), R0/(19q*10), R1/(19q))`, `q=19^nu`.
5. Verify these values and all coefficient residues against the frozen
   v1 modular evaluator at the required modulus `19^(k+1)`.
6. Solve the affine next-digit system with the fixed matrix, and
   independently enumerate all 361 possible digit pairs to check its
   complete solution list.

Every state records its full family key, all exact integer coefficients,
exact remainders and normalized fractions, modular residuals, fixed
matrix, affine constants, rank, reduced augmented rows, digits and
children. A checkpoint is flushed every 10 nodes and at each layer end.
The cap is asserted at every layer and after every child insertion.

The deliberately limited benchmark processes only the first 90-node
layer. Its child PID 51229 finished, exit 0 and reaped, in 0.102156
seconds supervisor time, with 0.041568 seconds worker time, under
30 seconds. It retained 14 nodes at precision five and is explicitly
labeled incomplete for the precision-eight traversal. At the measured
rate the structurally bounded maximum of 360 node lifts projected
less than 0.2 worker seconds, which justified starting the separate
full run under its 30-second timeout.

The full child PID 51403 finished, exit 0 and reaped, in 0.093897
supervisor seconds (0.036470 worker seconds) under the unchanged
30-second timeout. Its complete layers were:

| Input precision | Input states | Consistent | Inconsistent | Output precision |
|---|---:|---:|---:|---|
| 4 | 90 | 14 | 76 | 5 |
| 5 | 14 | 0 | 14 | 6 |

At precision five only masks `55584` and `58480` remain. At precision
six the layer is empty. Thus there are no later nodes to investigate,
and the run correctly stops before the predeclared target eight.
Every system in these two levels has rank 2. No timeout, cap change,
height search or close-root pruning occurred.

The full exact certificate stream contains 104 records, SHA-256
`e5f4ebc407434d8337d108e95807140887f00eab8cc7ced06d26341405124c94`.
The result JSON is SHA-256
`b86b4a92a3eebc8b032d82e6329bc74e4ded8fa1afc84a0ad4515d0b3b608a91`.

## Small explicit inconsistency certificates

The separate constructor post-check
`owner-J16-Hensel-v2-obstructions.py` verifies the exact chain of input
keys and children as `90 -> 14 -> 0`. For matrix rows `m_0,m_1,m_2`
it saves

    lambda=(det(m_1,m_2), det(m_2,m_0), det(m_0,m_1)) mod19.

Rank 2 makes `lambda` nonzero, and direct scalar products check
`lambda^t M=0`. If `c=E(U,V)/19^k mod19`, the digit equation is
`M*d=-c`. Its inconsistency is certified by the nonzero scalar
`lambda^t c mod19`. All 76 failures at input precision four and all
14 failures at input precision five have such a nonzero scalar.
Exactly the 14 passing rows have scalar zero. Every matrix, constant,
left-kernel vector, obstruction, digit and child is saved in
`owner-J16-Hensel-v2-obstructions-result.json`. This fixed 104-row
post-check is constructor validation, not an adversarial audit.

## Candidate mathematical consequence and review gate

An actual rational J=16 counterexample supplies a full derivative
assignment. The coordinator's candidate leading cover places its
minimum valuation and leading residues among the finite input branches.
Accepted T1 excludes the assignments omitting either small root. The
v1 integrality and Taylor argument force every remaining actual pair
to follow one of the enumerated affine digit paths at each precision.
The exact polynomial roots impose `E=0`, so such a pair must have a
path through precision six. The complete finite construction finds no
such path.

**Proposed L4:** conditional on the accepted normalization/T1--T2 inputs,
the as-yet unreviewed leading coverage and the uniform-remainder
argument, J=16 is impossible for a nontrivial rational degree-20
counterexample. This would remove all 88 original J=16 masks and leave
684 candidate masks in the other J classes. These numbers and L4 are
**not accepted** until the required two independent adversarial audits
reconstruct the whole argument, verify all finite inputs and outputs,
and resolve any substantive issue. Computations here are exact finite
evidence; they do not alone prove an unrestricted mathematical claim.

All v1 and v2 constructions are co-authored work for review-independence
purposes. This constructor has not read a review or messaged a reviewer.
The coordinator alone can promote the candidate after both audits.
No Git commit, push, shared-file edit, paid API, native CAS, dependency
install, charge, external message or subagent was used by this worker.
Python 3.15.0 and the standard library suffice.

Commands from the repository root:

    python3 -u problems/2021-B4/computations/owner-J16-Hensel-v2.py --benchmark
    python3 -u problems/2021-B4/computations/owner-J16-Hensel-v2.py
    python3 -u problems/2021-B4/computations/owner-J16-Hensel-v2-obstructions.py

The v2 artifact manifest is `owner-J16-Hensel-v2-manifest.json` in this
notes directory. It includes the separate incomplete benchmark, all
exact node certificates, both job records and the obstruction packet.

For dependency precision: L1--L2 supply the leading cover. The old L3
second-digit formulas are cross-check material; the new uniform `E`
construction independently computes all the necessary digits from that
leading cover. Its logical coverage argument does not require treating
the previous scalar second-digit identities as an additional axiom.
