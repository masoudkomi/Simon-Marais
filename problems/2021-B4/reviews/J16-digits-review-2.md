# R2 whole independent audit: rational J=16 exclusion L1--L4

2026-10-16 UTC. **Initial blind audit complete; no unresolved substantive
objection.** I recommend that the coordinator accept L1--L4 in their exact
rational scope after integrating the other required fresh whole audit.
This report does not itself promote the candidate.

Requested settings were `gpt-6.1-sol` / `max`; verified effective-setting
readback is unavailable. I did not construct any portion of the candidate,
and have not read another J16 reviewer's reports, code, data or conclusions.
The coordinator and owner are both treated as co-constructors. No shared
issue/status file or unrelated proof was read. No Git operation, shared
file edit, subagent, native CAS, installation, charge or separately billed
API was used.

## Exact scope and accepted inputs

The annual target is 2021 B4(b), whose hypothesis is a polynomial in Q[x]
with a possibly different **rational** common root for each derivative
order 1,...,d-1. This audit establishes only the proposed impossibility of
the J=16 branch of a nontrivial degree 20 example in the accepted 19-adic
normalization. It does not establish the entire degree 20 case or classify
all degrees. It does not apply to arbitrary complex recycled roots, and
does not assume that every root of f is rational. No preliminary part(a)
is solved or reproduced.

Explicit accepted inputs are the reviewed rational normalization, the
reviewed Newton width-one and long-edge results, the accepted 772-mask
register, and T1--T2 in
`notes/coordinator-three-rational-witnesses-reviewed-v1.1.md`. In particular
T2 supplies a double 0, simple 1,u,v, the exact rational root set {0,1,u,v},
positive integer valuations for u,v, and the Eisenstein degree 15 residual
factor. T1 states that every covering set of rational recycled roots has
at least four distinct members. Those accepted results are not replaced
by their constructors' old candidate status annotations. I independently
regenerated the ordinary binary-mask recursion and the complete 772-mask
list, including all 88 J16 masks, and checked it against the designated
accepted register. I did not rerun the earlier 1,493,024-family T1 proof.

The published normalization and root constraints remain attributed to
Castryck--Laterveer--Ounaïes, arXiv:1208.5404, as specified in the accepted
register. No independent validation of Massri's complex-witness theorem
or novelty claim is supplied here.

## Independence and reconstruction

Before opening any constructor code, manifest or finite data, I wrote
`J16-digits-review-2-independent-derivation.md`, the full independent
leading/continuation program and an external process supervisor. Their
predata freeze is timestamped 2026-10-16T17:01:22Z. The unchanged mathematical
program has SHA-256
`428a574119ea2dbbe33700654cb8fe6b48ed9e5ca1a9609e23c1669c6ee9dc86`;
the derivation has SHA-256
`ef3c998723c3eb08b66c5b6d48138c73b34577a4a7d70dffb273b6dcedcb7cff`.
The complete independent traversal was launched before the constructor
serialization comparison was designed. The later adapter imports only
this frozen reviewer module; it imports no constructor or peer module.

The frozen derivation reconstructs the whole argument. The key checks are:

1. Ordinary Hasse coefficients give the exact division-free recurrence
   `a_j=-sum_(h<j) binom(j,h)a_h w_j^(j-h)` from
   `binom(20-h,20-j)binom(20,h)=binom(20,j)binom(j,h)`.
   Every actual canonical full assignment is therefore covered.
2. Multiplying the exact T2 factorization yields the stated c2,c3,c4
   identities. Different small-root valuations give two width-one edges
   with lower exponents 2,3<19 and force both H2,H3 to use 1. In sole-center
   cases the valuations are equal; the integral initial form is
   `T²(T-Ubar)(T-Vbar)`. Its ordinary Hasse values give exactly the
   candidate's ratios, without assuming distinct reduced roots.
3. `q0=Ptilde(0,0)` is nonzero for every mask. An actual minimum valuation
   nu obeys `19^nu|q0`. All 84 bound 1 masks and 4 bound 2 masks are retained
   for their permitted nu until exact constant prerequisites remove them.
   The root-sum identity and the constant/linear coefficient expansion give
   the three leading affine rows. Inactive labels do not change those
   rows and are fully restored afterward.
4. Monic division of `F=f/Z²` by
   `Z²-(u+v)Z+uv` gives R0+R1Z over Z[u,v]. The homogeneous degree bounds
   prove integrality of
   `E=(Ptilde/q,R0/(19q*10),R1/(19q))` over Z_(19). The two exceptional
   coefficients c19=-20,c20=1 also satisfy the bounds and are included.
   No division by u-v occurs. Modulo 19 the equations are affine, with
   constant Jacobian M exactly as claimed.
5. At every k>=1, the polynomial Taylor expansion gives the complete
   next-digit condition `M*d=-E/19^k mod19`. This works at rank 0,1,2,
   with no nonsingularity assumption and no close-root pruning. T1 removes
   only assignments omitting a required small-root label, after all old
   second-digit records have been compared.

The remaining 15 roots can be ramified and nonrational. Their valuations
enter only through the accepted T2 factorization and long-edge separation.
The integers nu,U,V refer solely to the rational small roots. An absent
center bit denotes a failed center equation only for the actual canonical
mask; formal families are not asserted to satisfy extra nonvanishing
conditions. This is sufficient for complete necessary coverage.

## Independent exact evaluator and complete exhaustion

For E precision 19^r, the checker evaluates every normalized coefficient
modulo `q*19^r`. It omits a noncenter power w^e only when
`nu*e>=nu+r`, which makes that term zero at the stated modulus. Center
positions keep the full binomial sum. It then constructs the actual
coefficients of F, including -20 and 1, modulo `D=19q19^r`.

Its remainder evaluation is direct Horner in the monic quadratic quotient:

    (R0,R1) <- (c_e-u*v*R1, R0+(u+v)*R1) mod D.

After traversing all 19 coefficients, exact residue division by 19q and
unit inversion of 10 give the second and third E coordinates. Ptilde/q is
computed separately. This does not reuse the constructor's scaled
homogeneous-remainder recursion. Every generated child is additionally
reevaluated at its new precision.

The leading cover independently contains 70 masks,768 projected branches
(756 at nu=1 and 12 at nu=2), and 840396 full keys. Every allowed label and
valuation case is covered once. The code tests all 361 leading residue
pairs wherever constant prerequisites hold. It permits zero coordinates
in both-center cases and equal residues everywhere before justified
filters; the full calculation happens to retain neither type of leading
point. There is no finite root-inequality filter at later stages.

The independent finite-field solver uses a nonzero two-row minor when
rank 2, one nonzero row plus its entire affine line when rank 1, and all 361
points when rank 0. Every one of 692 encountered matrices was independently
validated by enumerating all 361 digit pairs and comparing every nonempty
fiber. Algebraic pivot solving with explicit consistency checks proves
empty-fiber completeness as well. This is complete validated linear
algebra, not a representative sampling of matrices or systems.

| Input precision | Parents | Children | Relevant outcomes |
|---:|---:|---:|---|
|1|840396|361194|58 masks after the next digit and T1|
|2|361194|2026|Every 249356 rank 1 node is inconsistent;31 masks remain|
|3|2026|90|All matrices rank 2;8 masks remain|
|4|90|14|76 inconsistent; only 55584 and 58480 remain|
|5|14|0|All 14 inconsistent; precision 6 is empty|

Before T1, the first next-digit test has 125346 consistent parents:
112222 rank 2 and 13124 rank 1. The other counts are 373610 inconsistent
rank 2 and 341440 inconsistent rank 1. T1 deletes 14248 assignments,
including 384 consistent rank 2 parents, giving
`111838+19*13124=361194` children. Thus the candidate's L2 and L3 mask
counts, all singular fibers, and the T1 correction are independently
reproduced. The surviving precision 4 mask counts are 2,36,4,36,6,2,2,2
at 51495,55584,56407,58480,58898,59703,62251,89160 respectively.

For **all 104** late states (90 at precision 4 and 14 at precision 5), the
frozen independent code also rebuilds every coefficient as an untruncated
integer by Horner evaluation and recomputes the exact monic remainder
and rational E vector. These agree with the modular evaluator. It brute
forces all 361 digits for each state. All 104 matrices have rank 2, so the
90-node upper bound for every later level follows structurally from the
constant Jacobian. The metadata check additionally evaluates all 1976
selected ordinary Hasse equations directly from the ordinary c_i values,
including the fixed order 1 and 19 witnesses.

For each matrix the independent cofactor vector
`lambda=(det(m1,m2),det(m2,m0),det(m0,m1)) mod19` is nonzero and has
`lambda^t M=0`. Every failed late node has nonzero `lambda^t c`, with
c=E/19^k. All 76 failures at precision 4 and 14 at precision 5 have this
explicit obstruction; exactly 14 precision 4 rows have zero obstruction
and their unique children are precisely the next input set. This verifies
the whole 90→14→0 certificate chain and every obstruction.

## Full artifact audit

After freezing the independent mathematical code, I opened the constructor
sources and data to design a serialization adapter. All four manifests
match their supplied hashes and entry counts 12,46,53,14; their union
contains 113 unique artifacts. Every entry passes its exact byte count
and SHA-256 check, and all are unchanged after the full audit. The
independent source and initial mathematical notes are unchanged too.

The adapter compares the complete leading branch sets, active/inactive
positions, q0 bounds, prerequisite-adjusted test counts, every saved
leading example's reduced equations, and every full key. It matches all
**1203616** v1 certificate records to the independent key/fiber stream,
recomputes every coefficient vector, residual, matrix and complete digit
list, checks every recorded augmented row space, and binds each output
node to its parent fiber. It checks 21627 distinct recorded augmented
row spaces, caching only exact repeats of all matrix/constant/record data.
No input record, coefficient vector or node fiber is sampled.

It also checks all 90 v1 exact post-check records, all 104 v2 exact records,
and all 104 obstruction records against the frozen independent construction.
Every saved integer coefficient, remainder, normalized fraction, minor,
constant, digit and child agrees. The late chain and root-label swap
closure agree. The supplemental metadata check matches all full result
histograms, per-mask visit/child counts, masks, precision targets and caps.

The two original plain streams are independently reproduced exactly:

- Rows: `b0ab2fd44f64015b0ae1caa954c3dad76be44c02833cec62d79c2df6c1f3dacb`.
- Coefficients: `dfe2ca43528f5e55c68a642f61838343b0a09bc6690afe153643c04ff574e49f`.

For the second hash the original serialization represents fixed a1 as −1,
where the modular checker stores its congruent nonnegative residue. The
adapter explicitly restores that fixed −1 representative before hashing;
no other coefficient normalization is changed.

The issue log records every substantive challenge, the harmless leading
test-counter convention, and the reviewer's failed first adapter benchmark.
The latter failed before mathematical comparison because it selected a
historical accepted-register field rather than the combined 772-mask field.
The failed source, PID, command, output and error are preserved. No
constructor repair or candidate artifact change was necessary.

## Reproduction, monitored budget and conclusion

Python 3.15.0 and the standard library suffice. From the repository root:

    python3 -u problems/2021-B4/reviews/J16-digits-review-2-runner.py problems/2021-B4/reviews/J16-digits-review-2-independent.py benchmark 60 --benchmark
    python3 -u problems/2021-B4/reviews/J16-digits-review-2-runner.py problems/2021-B4/reviews/J16-digits-review-2-independent.py full 300
    python3 -u problems/2021-B4/reviews/J16-digits-review-2-runner.py problems/2021-B4/reviews/J16-digits-review-2-artifact-audit.py artifact-benchmark 60 --benchmark
    python3 -u problems/2021-B4/reviews/J16-digits-review-2-runner.py problems/2021-B4/reviews/J16-digits-review-2-artifact-audit.py artifact-full 300
    python3 -u problems/2021-B4/reviews/J16-digits-review-2-runner.py problems/2021-B4/reviews/J16-digits-review-2-metadata-audit.py metadata 30

The independent 8192-node benchmark PID 53695 completed in 3.537s including
the complete leading enumeration. The full independent child PID 53793
completed in 40.731s under 300s. The successful artifact benchmark PID 55196
completed in 2.424s; the full artifact child PID 55388 completed in 76.518s
under 300s. All completed exit 0 and were reaped; all checkpoints and exact
commands are saved. The failed first adapter PID 55033 was also reaped.
No timeout occurred, no cap was raised, and no unrelated process was
terminated. Final metadata child PID 56017 completed exit 0 and was reaped
in 2.958s under 30s. Both benchmark outputs remain explicitly incomplete.

Authoritative account-wide weekly telemetry was 12% total used before the
run and 13% during integration, with unchanged reset 1792745187 and the
90% total-used stop threshold. No new weekly window was automatically used.

The mathematical conclusion follows from complete necessary coverage:
an actual rational J16 pair defines a compatible 19-adic path through
every precision, whereas this exact finite cover is empty at precision 6.
The computation is finite evidence; its use in the unrestricted rational
J16 statement is justified by the reconstructed coverage and Taylor
argument. Subject to the stated accepted inputs, no unresolved substantive
objection to L1--L4 remains. If promoted by the coordinator after both
audits, all 88 J16 masks are removed and 684 necessary masks remain in
the other J classes. No further classification claim is made.
