# 2020 B4 research log


The FULL SQ15 v1.1 integral-domain version is now independently reviewed after BOTH OTHER affected whole60 audits and complete120-disposition reconciliation. It proves actual endpoint rigidity, integral norm2 class-order restrictions and actual conjugate/orbit costs. The original false fractional extension and root miss remain preserved. The separate SQ14D/E hold was subsequently lifted by the full correction and both repair reviews below; full annual classification is open. [Acceptance](reviews/reasoning-class-return-sq15-acceptance.md).


The FULL corrected SQ14 INTEGRAL-domain theorem is now independently reviewed after BOTH OTHER affected whole76 audits and complete152-disposition reconciliation. Only the NEW accepted v1.2 copy governs D/E use; the old false fractional wording, historical hold and both original review misses remain preserved. Fractional TD/Gamma are unchanged. No numerical class quotient/full norm-q cancellation or annual answer follows. [Corrected acceptance](reviews/reasoning-arithmetic-return-r14-repair-v1.1-acceptance.md).

## Research significance and connections

Opening overview updated 2026-10-18. Choosing the maximum possible collection
of distinct polygonal distances is equivalent, after setting \(q=n-1\), to
constructing a cyclic planar difference set of order \(q\). The associated
incidence structure is a projective plane with a cyclic group acting
regularly on its points. Thus this short geometry question asks for the
cyclic Prime Power Conjecture, with the separate boundary case \(n=2\).
The conjecture for arbitrary projective planes has broader scope.

Difference sets connect finite geometry, optimal difference packings, and
Fourier analysis on finite groups. Their group-ring identities turn into
cyclotomic norm equations. Arithmetic then brings in ideals, class groups
and units: solving a field norm equation is only one part of recovering an
actual integral binary difference set. [Peluse's asymptotic theorem](https://arxiv.org/abs/2003.04929)
illustrates another connection, to analytic number theory: an asymptotic count
of admissible orders can be established without excluding every exceptional
order.

The accepted [SQ16 integral even-factor/content theorem](reviews/reasoning-class-return-sq16-acceptance.md)
and [SQ17 literal source-unit diagnostic](reviews/reasoning-class-return-sq17-acceptance.md)
passed both OTHER whole audits and full reconciliation. SQ16 retains BOTH
integral scalar-balanced factors and gives exact denominator8 for every
nonidentity conjugate in the known q8 diagnostic. SQ17 gives integral
SAME-ideal counterexamples to an unqualified real-square shortcut in the
inspected author copy, together with the classical two-unit-norm-coset
criterion. Final journal wording/errata are uninspected; no full Fourier
tuple or new taut order follows. Odd-H/mixed existence and annual stay open.

Historical scope holds arose from omitted INTEGRAL qualifiers in old
SQ14/SQ15 statements. Both full corrections and affected reaudits are now
complete; only the corrected accepted copies govern those clauses. The old
false versions, root/reviewer misses and reconciliation records remain
preserved. Full mixed-order/annual classification remains open.


The new [SQ14A–E low-square result](reviews/reasoning-arithmetic-return-r14-acceptance.md)
is **proved, independently reviewed scoped partial result** after root/C
TWO OTHER ENTIRE WHOLE64/64 and full128-disposition reconciliation.
Constructor B excluded. Exact square lift/orbit moments force rationality
when s>=2a;unit squaring on SAME I² gives low ordinary principality
without odd class number. Actual refined boxes inject under2a<=s;
ordinary boxes require2a²<=s. Specified prime-ideal orders and mixed
leastprime<=7 give new necessary class restrictions. The full mixed
norm-q case,new class evaluation,annual classification and priority
remain open/unclaimed;actual T-stability is retained where needed.

The reviewed results now include [A9 arithmetic obstructions](reviews/reasoning-arithmetic-return-r9-acceptance.md) and [R10 actual mixed-norm realization](reviews/reasoning-arithmetic-return-r10-acceptance.md), each accepted after two OTHER initially blind whole audits and reconciliation. R10 realizes actual integral Weil atoms in its specified odd-class fixed fields. Its exact weighted lift has binary defect Phi3(N)/p−1: the correct norm residue does not force the required equality N=q0. Thus genuine class cancellation is compatible with those necessary conditions; the finite conductor-size and full character-tuple gaps remain open. These results give no new taut order, numerical exclusion or unrestricted classification. See the [current dashboard](../../progress/dashboard.md), [references](references.md), and [review register](reviews/README.md).

Status: 2026-10-16. **No full solution claimed.** P1–P6 and the attributed square-descent application are proved, independently reviewed partial results after two blind full reconstructions; see reviews/acceptance.md. Earlier candidate labels below are historical. Requested worker settings: `model=gpt-6.1-sol`, `reasoning_effort=max`; no independent effective-setting readback was available.

2026-10-18 current advance: [A11A–E](reviews/reasoning-arithmetic-return-r11-acceptance.md)
has passed both OTHER whole audits and full reconciliation. Signed
primary-ideal relations yield exponential subset-sum restrictions; an
actual small generated subgroup would force a principal norm EXACTLYq
and an actual configuration via the full integral binary lift. No new
q meets that arithmetic hypothesis here, so the annual classification
remains open.


2026-10-18 further advance: [TD1–TD5](reviews/reasoning-Todd-return-r12-acceptance.md)
has passed root/A TWO OTHER initially blind ENTIRE WHOLE72/72 audits
and complete reconciliation. The canonical refined ideal class retains
the even-class unit obstruction, and gives the COMPLETE exact-q finite
box plus precise actual conjugation-cube and mixed-slice counts. Actual
whole-primary minimality holds even with square blocks. No new q has
its canonical offset/box or small-H condition evaluated; no automatic
unit correction, composite assembler, annual answer or priority follows.


2026-10-18 current: [L13A–D](reviews/reasoning-arithmetic-return-r13-acceptance.md) accepted after root/A OTHER ENTIRE WHOLE64/64 audits and full reconciliation. Every ACTUAL prime-layer sequence is minimal; nonsquarefree fields have unconditional2^omega(q) distinct labels and actual extra Omega(q)-omega(q)-1 prefixes. Classical Davenport restrictions retain unit defect and exact norm/ideal domains. No new class-group evaluation, finite-q realization, numerical taut order or annual answer. Old A9 theorem/warning preserved; actual integral complement supplies the new inference.

## Statement checks

Official B4(b), page 2, was checked by extraction and visual rendering. It asks for all taut integers n>=2, with Euclidean distances among n selected vertices of an (n²-n+1)-gon. Part (a) is excluded from this work. The order/cardinality change q=n-1 is essential, as is the n=2 exception. See statement.md, source-check.json, and the cropped official B4 render.

## Approaches and results

### 1. Chord geometry and extremal counting

Exact signed differences replace floating-point chord lengths. The number of ordered pairs equals the number of nonzero residues, so distinct distances force a perfect cyclic difference set. Partial-v1 P1 reconstructs the official reduction and checks n=2 explicitly. This gives a precise problem identification rather than a solution. For q>=2 the cyclic-plane correspondence is written in both directions in P2; arbitrary projective planes are not silently assumed cyclic.

The conjectural classification is {2} union {p^a+1:a>=1}. Prime-power sufficiency is attributed published context only. No construction or proof of the excluded preliminary case is reproduced.

### 2. Incidence matrices / Bruck-Ryser

A taut set yields the incidence matrix of a cyclic plane; its row inner products are q on the diagonal in excess of the all-ones matrix. Bruck-Ryser applies when q is congruent to 1 or 2 modulo 4: every prime congruent to 3 modulo 4 must have even valuation in q. The theorem is only necessary. In particular q=10 passes because 10=1²+3², even though the cyclic quotient obstruction below excludes it. Thus Bruck-Ryser cannot classify tautness.

### 3. Quotient occupancy and character sums

For d|v, exact occupancies satisfy the autocorrelation equations in partial-v1 P4. At d=3 this gives q=x²-xy+y², hence every prime congruent to 2 modulo 3 has even valuation in q when q=1 mod 3. The elementary derivation and the weaker infinite exclusion n=11 mod 12 are in P5. This is recorded as a reconstruction of a weaker known necessary restriction, with no novelty claim.

The quotient computation excludes q=10 and 55 at the level of occupancy vectors, but admits vectors for q=28,52,91,100, all non-prime-powers. For example (13,19,21) meets all quotient modulo 3 equations at q=52. Such a vector is not a taut set. Fourier magnitudes |A(zeta)|²=q encode the same correlations; no valid step here forces prime-power q from those identities alone. Lifting a relaxed occupancy solution to a 0-1 difference set is the missing obstruction.

### 4. Multiplier groups and exact orbits

The standard First Multiplier Theorem makes prime divisors of q multipliers; gcd(q,v)=1. The sum-zero translation in P3 makes all multipliers fix D. Therefore D is a union of their orbits. This is stronger than the raw distance formulation, but does not itself settle the conjecture.

The full group generated by prime divisors of q can be small even for non-prime-power q: at 1944 it has 1872 elements (<=1945), and at 2435 it has 435 (<=2436). Thus a proposed universal proof by showing |M|>q+1 for every non-prime-power q is false. Orbit cardinalities exclude these two examples; the arithmetic formula in P6 avoids materializing millions of residues. At q=2304, orbit cardinalities do permit size 2305, demonstrating a further limitation.

### 5. Bounded exact search and imported nonexistence filters

All scripts use Python 3.12.14 and its standard library. Full invocations and exact JSON/stdout are in computations/README.md. No run reached its budget limit.

| n | q | v | Exact finite outcome | DFS calls |
|---:|---:|---:|---|---:|
|2|1|3|Witness {0,1}|1|
|5|4|21|Witness {0,1,4,14,16}|18|
|7|6|43|Normalized search exhausted, no witness|4386|
|9|8|73|Witness {0,1,3,7,15,31,36,54,63}|201|
|10|9|91|Witness {0,1,3,9,27,49,56,61,77,81}|29848|

Every witness was rechecked by enumerating all ordered differences. Prime q cases were not researched; these finite examples address the boundary and composite orders beyond the preliminary prime case.

A first pass over 2<=q<=5000 skipped 711 prime-power orders as established context. In its stated test order it excluded 1462 by Bruck-Ryser, 979 by the even-order theorem, 416 by Wilbrink's 3-divisibility condition, 1070 by the nonsquare quadratic-residue test, 357 by the multiplier-group bound, and 1 by explicit orbit-size subset sum. The only remaining non-prime-power orders were 1944,2304,2435. These counts are disjoint bookkeeping for this implementation, not intrinsic mathematical categories.

Residual exact diagnostics:

- q=1944: v=577*6553, multiplier orbit lengths 1,117,144,1872. Size 1945 is impossible. Gordon's Arasu inequality also excludes it, e.g. p=577,h=6553,m=2,s=117,o=16.
- q=2435: v=5931661 is prime; nonzero multiplier orbits all have size 435. Neither 2436 nor 2435 is divisible by 435, so adding or omitting the singleton0 cannot give size 2436. This reproduces a case already present in Gordon's 1994 tables and treated in his 2020/2022 paper.
- q=2304: orbit-size subset sum passes and the selected Arasu tests give no exclusion. The published square-descent theorem reduces 2304=48² to 48; Wilbrink then excludes 48 because 3|48 but 9 does not divide 48. This is an attributed consequence, not a new proof of those theorems.

Accordingly the local work reproduces known obstructions in a modest finite range; it does not improve the much larger published range. The general classification remains open in the checked literature. The safe imported bound q<2e10 is kept separate from our q<=5000 computation.

### Preserved failures and nonclaims

- Distances sampled in floating point were deliberately not used as proof; exact cyclic separations suffice.
- Raw exhaustive search is not proposed for large orders: v grows quadratically and subset search grows combinatorially. The only exhaustion in this pass was n=7; positive runs stop at the first witness.
- Bruck-Ryser, quotient moments, group-size bounds, and orbit-size subset sums all have explicit surviving cases. Their converses are not used.
- Neither Singer's existence theorem nor the cyclic-plane correspondence proves that all planes or all cyclic planes are Desarguesian.
- No literature search, asymptotic density theorem, or finite verification proves the unrestricted PPC.

## Next steps

Checkpoint and free the worker slot so every annual problem receives initial investigation. The coordinator should arrange the two queued independent reviews if the partial package is retained. Review priorities are exact statement/boundary fidelity, P2's plane converse, P5's norm argument, P6's arithmetic orbit formula, and all imported theorem hypotheses.

Further 2020 work should start from the actual remaining cyclic PPC rather than rerunning known small ranges. If pursued later, a precise target is strengthening the lifting obstruction for quotient occupancies or orbit unions that pass the cardinality test. No plausible complete proof or counterexample has emerged in this pass.
