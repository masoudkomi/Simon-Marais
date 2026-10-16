# 2020 B4(b): initial independent adversarial review R2

**Initial report frozen, 2026-10-16 UTC / 2026-10-17 Australia/Brisbane.**

**Verdict: accept the frozen package as a correct, explicitly partial argument, relying on the published theorem statements identified below.** I found no substantive mathematical defect requiring repair in P1-P6 or in the square-descent application. This is one reviewer's verdict, not promotion to `proved, independently reviewed`, and not a solution of the unrestricted classification in B4(b).

## Identity, independence, and scope

The reviewed file is `problems/2020-B4/proofs/partial-v1.md`, SHA-256
`f53945e49bd626847e52a61f7e39e96defd2ae44900f9d235c2c14e720f41525`.
It was checked unchanged both before the audit and on recovery. The manifest freezes exact file hashes.

I did not construct this candidate. I reconstructed P1-P6 from the candidate and official-domain normalization before reading the author's references and computation notes. I did not read any other reviewer's report, conclusions, issue log, source extracts, or shared progress/status files. An initial directory inventory exposed review filenames only. Later readings were limited to the author's statement, references, computation README, residual script and selected computation outputs, together with official and published mathematical sources.

The task is B4(b) only. The [official Paper B, page 2](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2020-paper-b_1.pdf) has precisely the domain n >= 2, a regular polygon on n^2-n+1 vertices, and n chosen distinct vertices with all unordered pairwise Euclidean distances different. The local official PDF text and a rendered B4 crop agree. I did not solve or reproduce the preliminary construction. Singer's prime-power existence is used only as attributed context from the official discussion; its proof was not audited here.

Requested launch settings: `gpt-6.1-sol`, reasoning `max`. Verified effective-setting readback: unavailable. Authoritative telemetry during the audit was 10% and then 12% total weekly used, reset `1792745187`; the latter was obtained at approximately 16:48:33 UTC. No separately billed API or purchase was used.

## Complete reconstruction of the internal arguments

### P1: geometry, difference sets, and the boundary

Put q=n-1, k=q+1, v=q^2+q+1. Since q(q+1) is even, v is odd. Every nonzero residue difference has a unique undirected representative r in {1,...,(v-1)/2}. Its chord length is 2R sin(pi r/v), where R>0. All arguments of sine lie strictly between 0 and pi/2; hence these lengths are strictly increasing. Equality of two chord lengths is therefore equivalent to equality of residue differences up to sign, with no accidental equality between different separations.

If two ordered differences from D are equal, either they come from different unordered pairs, which would repeat a distance, or from a pair and its reversal. In the latter case their common nonzero difference would satisfy 2r=0 modulo v, impossible because v is odd. Thus tautness gives k(k-1)=v-1 distinct nonzero ordered differences and so exactly one representation of each nonzero residue. Conversely, a repeated distance lets us orient the two pairs to get an equal ordered difference, contradicting the difference-set property. This proves both directions, rather than merely a packing bound.

At n=2, v=3 and a two-element set has exactly one unordered pair, so it works. The candidate explicitly includes this boundary and does not apply the nondegenerate plane correspondence at q=1. The positive-exponent prime-power convention would otherwise omit this valid case. The equivalence is also stated in the [official solution discussion, page 27](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2020-solutions_1.pdf); no preliminary proof is needed for it.

**Disposition: valid for the full official domain.**

### P2: the precise cyclic-plane correspondence

Assume q>=2. In the development of D, the lines D+t have size q+1. For t nonzero, points in D intersect (D+t) are in bijection with ordered pairs a,b in D satisfying a-b=t, so this intersection has size exactly one. Translating this statement proves that any two differently indexed lines meet once. They cannot be equal, since their intersection size would then be q+1>1. Thus the development really has v distinct lines.

For distinct points x,y, their unique ordered representation x-y=a-b gives the line D+(x-a)=D+(y-b). Conversely, any line through x,y supplies such a representation, so the line is unique. Each point x lies on exactly the q+1 lines indexed by x-d with d in D. These incidences establish the two uniqueness axioms and uniform point/line degrees without assuming a plane in advance.

Nondegeneracy is not omitted. Pick distinct A,B on L and P outside L; such P exists because v>q+1. The lines L,AP,BP have distinct pairwise intersections A,B,P and no common intersection. Inclusion-exclusion gives union size 3(q+1)-3=3q. There is a point outside the union because v-3q=(q-1)^2>0. Such a Q gives four points with no three collinear. At q=2 the complement has exactly one point, still sufficient.

Translation preserves membership incidence and acts regularly on the v points and the v distinct lines, so the resulting group is a cyclic collineation group.

For the converse, an action on points must mean an action by collineations; an arbitrary labeling of points would be useless. The candidate's final paragraph explicitly supplies that qualification. The standard finite-plane counts can also be reconstructed: projection from a point P outside a line L bijects L's q+1 points with the lines through P; these lines partition all other points into q points each, giving 1+q(q+1)=v points, and the dual argument gives v lines. Let H be a line stabilizer in the regular point group G. No nonidentity element of H fixes any point, so the H-orbits within the line all have size |H|. Consequently |H| divides q+1; also |H| divides |G|=v. Since v=q(q+1)+1, their gcd is one, so H is trivial. A line's G-orbit consequently comprises all lines exactly once. Identify G additively with the cyclic point coordinates and call one line D. For each nonzero g, the unique line containing g and 0 supplies a representation g=a-b in D. Any other representation gives another such translate, so it is the same representation.

This establishes the cyclic, regular-collineation case only. It neither makes arbitrary projective planes cyclic nor makes cyclic planes Desarguesian. [Alexeev-Mixon v2, section 4, pages 6-7](https://arxiv.org/pdf/2510.19804v2) was checked both textually and visually: its definitions and separate Desarguesian conjecture agree with that distinction. Its existence construction is not reproduced here.

**Disposition: valid with the collineation qualification already present in the frozen text.**

### P3: two valid, different normalizations

There is an ordered difference equal to 1, say a-b=1. Subtracting b from all elements leaves the difference multiset unchanged and includes both 0 and 1. Sorting this translated set gives an increasing-subset representative. Therefore restricting a direct existence search in this way loses no case. It does not assert one representative per equivalence class.

For the second normalization, k=q+1 is invertible modulo v because v-qk=1; explicitly, -q is its inverse. Hence S+kc=0 has exactly one solution c. A multiplier remains a multiplier after any translation: replacing D by D+c changes the translate term from h to h+(t-1)c. On the sum-zero representative, summing tD=D+h gives t*0=0+kh. Invertibility of k forces h=0. This applies to every numerical multiplier on the same uniquely normalized set, so simultaneity is justified.

For the import, [Gordon (1994), Theorem 2, page 2](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v1i1r6/pdf/) gives divisor multipliers for a planar abelian difference set. The candidate uses only the prime-divisor consequence. The ambient group is cyclic, hence abelian; the order is q=k-1, not k or v; lambda=1; and gcd(q,v)=1. In the general prime formulation, p>lambda holds automatically for every prime p. The q=1 boundary has no prime divisors, so this assertion is vacuous there. I checked the published statement, not Hall's original proof. The invariant-translate conclusion in this package is separately proved by the sum argument, so it does not require reconstructing the broader McFarland-Rice theorem.

**Disposition: valid. No multiplier converse or unjustified prime-power assumption is used.**

### P4: quotient counts and the character identity

For a positive divisor d of v, each quotient residue class contains h=v/d residues of the original cyclic group. The sum of the a_i is k. In the zero class, the ordered pairs counted by sum a_i^2 consist of k diagonal pairs and h-1 nonzero differences, each represented once. Thus the count is k+h-1=q+h. For nonzero quotient class r, all h residues lying over it are nonzero, and each has one representation. Their count is the correlation sum a_i a_(i-r)=h. This verifies the zero-class correction and all multiplicities.

There is no exception at d=1: its only equation is k^2=q+v, which holds. At d=v the occupancies are 0 or 1, giving sum a_i^2=k=q+1 and every nonzero correlation equal to 1.

In the cyclic polynomial ring, the coefficient at residue zero of A(X)A(X^-1) is k, and all other coefficients are 1. The displayed group-ring identity follows because its right side has coefficient q+1=k at zero. Evaluating at any nontrivial vth root kills the geometric sum. Since the coefficients are real integers and zeta^-1 is the complex conjugate of zeta, this gives |A(zeta)|^2=q. Primitivity is not needed. These are necessary identities, not sufficient existence tests.

**Disposition: valid, including diagonal, d=1, and d=v cases.**

### P5: the elementary norm obstruction

When q=1 mod 3, v=0 mod 3. P4 with d=3 gives a+b+c=q+1, a^2+b^2+c^2=q+v/3 and ab+bc+ca=v/3. Subtracting yields q=a^2+b^2+c^2-ab-bc-ca. Substitution x=a-c, y=b-c expands exactly to x^2-xy+y^2, with no assumption that x or y is positive.

For p=2, the only pair modulo 2 on which the form vanishes is (0,0). For an odd prime p=2 mod 3, if y is zero modulo p then x is zero too. Otherwise t=x/y satisfies t^2-t+1=0. It follows that (-t)^3=1. Also -t cannot equal 1: t=-1 would make the quadratic equal to 3, and p is not 3. Thus the multiplicative group of the field of p elements would have an element of order 3 although 3 does not divide p-1, a contradiction. This proves p divides both x and y whenever it divides the form.

After dividing x,y by p the form is divided by p^2. Repeating terminates because the form equals positive q, so x=y=0 is impossible; every such prime has an even valuation. Values x=0 or y=0 cause no omitted division: the argument branches before forming a ratio. The prime 3 is not claimed to obey this restriction.

For q=10 mod 12, q=1 mod 3 and q=2 mod 4, so its 2-adic valuation is exactly one. Hence this entire progression is excluded, equivalently n=11 mod 12. The q=1 case remains allowed. The example q=10=1^2+3^2 indeed passes the usual sum-of-two-squares necessary condition, so the candidate's comparison does not reverse Bruck-Ryser or assert sufficiency. The norm obstruction is weaker than the imported general even-order restrictions and is not presented as original.

**Disposition: valid as a necessary obstruction only.**

### P6: arithmetic orbit lengths and bounded multiplicities

For a positive divisor d of v, x with gcd(x,v)=v/d is uniquely represented by x=(v/d)u with u a unit modulo d. There are phi(d) such residues. Multiplication by M preserves the stratum and corresponds to multiplication by the image of M in the units modulo d. For a unit u, tu=t'u modulo d is equivalent to t=t' modulo d, so the image acts freely on this stratum. Every orbit therefore has size |M mod d|, and the number of orbits is phi(d)/|M mod d|.

At d=1 the unit group is the trivial group, represented arithmetically by the unique residue 0; the stratum is exactly {0}, with one orbit of length one. This handles the only zero-coordinate case. For d>1 the argument never cancels a nonunit: u is a unit by the stratum definition. M can be trivial and can be a proper known subgroup of the full multiplier group; the assertion remains necessary.

P3 makes D invariant under M. Hence D is a disjoint union of M-orbits. For each d one may select between zero and the available number of orbits of that length; summing the sizes must give k. This is a bounded subset sum, rather than an unbounded coin problem. Nothing in it checks differences within or between chosen orbits. Passing this test establishes no difference set, as the candidate explicitly states. The residual program uses exact integer arithmetic for mathematical decisions; timing/metadata are separate.

**Disposition: valid.**

## Square descent and imported-theorem scope

[Gordon (1994), Theorem 6, page 3](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v1i1r6/pdf/) gives a planar set of order m in a subgroup from square order m^2; it attributes the result to Jungnickel-Vedder. The same page's Theorem 8 attributes to Wilbrink the restriction that an order divisible by 3 is either 3 or a multiple of 9. Both statements were visually checked in the independently downloaded publisher PDF.

The present G is cyclic and therefore abelian. A subgroup remains cyclic and abelian, so square descent preserves exactly the group scope needed for the next import. At q=2304=48^2, descent would give order 48. Its 3-adic valuation is one and it is not 3, contradicting Wilbrink's restriction. This excludes B4 cardinality n=2305, not n=2304. No application at m=1 or a nonintegral square root is made.

The primary [Wilbrink publisher abstract](https://www.sciencedirect.com/science/article/pii/0097316585900287) independently supports the p=3 consequence for an abelian regular plane group. The primary [Jungnickel-Vedder publisher abstract](https://www.sciencedirect.com/science/article/pii/S0195669884800281) confirms its abelian setting and even-order result, but does not itself state square descent. Its square-descent statement was checked through Gordon's explicit attribution, not through an inspected original theorem page. Attempts at the original full PDFs returned HTTP 403. I did not bypass that restriction.

Thus the square-descent **application and hypotheses** are reconstructed; the original square-descent, multiplier, and Wilbrink **proofs** are not independently reconstructed in this review. Gordon is a directly checked published restatement in a primary research paper, not the original proof source for those older theorems. The candidate already describes these as published imports and does not claim to prove them. This disclosed dependency is not a mathematical correction request.

## Independent finite evidence and ancillary zero cases

The saved command is:

```sh
.venv/bin/python -u problems/2020-B4/reviews/initial-review-2-run.py
```

The runner records the exact executable, child script hash, job parameters and PID, applies a 90-second subprocess timeout, preserves incremental stdout checkpoints, and reaps only its own child. Child PID 38854 completed with exit 0 and no timeout, 16:07:20.634122 to 16:07:21.741592 UTC; wall time 1.107090584 seconds. Python was 3.12.14 with the standard library only. The check script imports no project module and does not rerun or modify the author's outputs.

The meaningful finite checks were:

- Coprimality and the explicit inverse identity for every 1<=q<=5000.
- 240 quotient-contraction cases on deterministic arbitrary subsets at q=6,10,12,28,55. This tests ordered-pair/occupancy contraction without constructing a preliminary example or searching for a taut set.
- All 581528 residue pairs for the 29 primes equal to 2 mod 3 through 257, and all nonzero form values in the integer box [-50,50]^2; no counterexample to the local norm obstruction appeared.
- Independent equality between occupancy enumeration and norm-based reconstruction for all 67 orders q=1 mod 3 through 199, including empty solution sets at q=10 and 55. These are occupancies, not vertex witnesses.
- Direct generator-action orbit enumeration on every odd modulus 3..171, compared stratum by stratum with P6, including the zero singleton.
- Independent subgroup generation separately modulo each divisor and plain-set bounded subset-sum dynamic programming for q=1944,2304,2435. All saved histograms and decisions matched. The respective size tests fail, pass, fail. This is particularly useful evidence against confusing the successful 2304 size test with existence.
- Independent arithmetic for all ancillary Arasu rows saved at those three orders, using nonnegative counts, including h=1. All matched.

For the ancillary import only, [Gordon's small-lambda preprint v1, Theorem 3, page 3](https://arxiv.org/pdf/2007.07292) assumes G=Z_p times H with gcd(p,|H|)=1 and chooses s to kill the action on H. The residual program applies this only to primes dividing v exactly once, takes cyclic H of order h=v/p, uses ord_h(m), and correctly has ord_1(m)=1. The source prints "positive" counts, but the counting proof requires allowing b=0. The implementation explicitly uses nonnegative counts and skips o<=1, so it makes the safe necessary test.

I independently reconstructed that counting extension: singleton-singleton ordered differences lie in {0} times (H minus {0}), while internal ordered differences from the a nontrivial orbits lie in (Z_p minus {0}) times {0}. Their budgets give exactly the two inequalities with a,b>=0. The model p=7,h=1,k=3,o=3 retains (a,b)=(1,0); it must not be discarded solely by the source's word "positive". This is a resolved source-wording risk, not an unresolved error in the candidate or code. The preprint's cyclic multiplier bound also has the explicit (21,5,1) exception; this review has not extended that theorem outside its stated scope.

All computations above are finite evidence. They neither prove the unrestricted Prime Power Conjecture nor replace the analytic reconstruction. I did not independently certify every author's search witness, the entire q<=5000 filter pass, or all large published verification ranges; those are not silently covered by this verdict on the frozen partial package.

## Issues, limitations, and recovery provenance

There are no unresolved substantive objections to the frozen P1-P6 or square-descent application. The separate issue-disposition JSON records the boundary, collineation, multiplier, quotient-zero, inert-prime and ancillary-zero risks and why each is already resolved. No proof repair or change of conclusion is requested.

The remaining limitations are source-proof access (as above), the deliberate partial scope, and lack of effective-model-setting readback. A search did not establish that no later paper exists; this review makes no fresh strongest-current-bound claim.

The audit was interrupted by an optional PDF rendering operation, not a mathematical computation. The operation emitted repeated Fontconfig cache errors. Its tool session was 86629; the subsequent sandboxed process query failed, and the escalated read-only query returned `aborted by user after 2340.2s`, without a PID or process result. On recovery, the expected optional PNGs already existed and I visually inspected the relevant Gordon small-lambda and Alexeev-Mixon pages. The coordinator later reported `Unknown process id 86629` from a targeted Ctrl-C attempt. That establishes no active tool session at that time; it is not verified OS-process cleanup. No global cleanup was attempted, and no renderer completion exit code is invented. The exact recovery checkpoint is preserved separately.

The full downloaded papers remain in ignored `.cache/`, with retrieval URLs and hashes recorded. No redistribution licence was established, so no full paper is proposed for Git. No proof/source/shared-status file was edited, no commit or push was made, and no result status was promoted by this reviewer. This initial report was frozen without seeing another reviewer's conclusions.
