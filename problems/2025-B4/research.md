# 2025 B4 research log

Status: initial investigation completed 2026-10-16; no full solution claimed. All new elementary arguments remain **candidate proof - unverified**, version P2025-v1 in proof.md. No independent reviews yet.

Launch request recorded by coordinator: gpt-6.1-sol, max reasoning. An independent readback of effective model/reasoning settings was unavailable. This is requested-setting evidence only. Weekly telemetry is monitored centrally by the coordinator; the supplied launch checkpoint was 2% total weekly used, with a 90% cutoff and reset 2026-10-23 08:46:27 UTC. No separately billed API was used.

## Statement checks

The cached official paper page 2 was read directly with pypdf. It specifies integers x,y,n,q with n,q>=2, so negative bases, negative roots and x=-1,0,1 must be handled. Official solutions page 20 identifies Nagell-Ljunggren. Its known tuples use the number of terms in the n slot; Paper B uses degree. The correct translation is m=n+1. Exact substitution gives degree 4 at x=3, degree 3 at x=7, and degree 2 at x=18,-19. The square roots also have negative signs in the official integer domain.

The preliminary solution pages were not investigated or reproduced. Degree 3 with odd q>=3 is excluded from the perfect-power search. General boundary/sign reductions apply to (b) and are recorded without reconstructing the preliminary proof.

## Approaches and results

### 1. Literature reduction and present-day status

Primary sources were searched and read on 2026-10-16; details and cautions are in references.md and computations/literature-audit.md. Bennett-Levin (2015) is particularly useful because its domain includes negative x and y. Its Proposition 1 restricts an unfamiliar nontrivial identity to odd q>=3, least prime divisor of m at least 5, |x|>=10^4, and a prime divisor of x congruent to 1 modulo q. Its Theorem 1 gives Omega(m)<=3, counting multiplicity. These are published imports, not project-original proofs; the full cited proofs have not received this project's independent audits.

Therefore any additional nontrivial identity would have even official degree n. For positive x the original Bugeaud-Mihailescu (2007) Theorem 1 has stronger least-prime bound 29, gives m prime for q=3, and m=q when q|m. Its Omega(m)<=4 is superseded by Bennett-Levin. The positive-domain scope must be retained. Their Theorem 2 is a reduction for proving absence of positive solutions via prime m; it does not allow replacing the m in every existing solution by a prime.

Recent primary publications found are a 2026 conditional class-number result and a 2026 paper for m=5,q=3 only. The latter's all-integer statement is false as printed: x=-1,y=1 gives (-2)/(-2)=1=1^3, a boundary pair that it omits. Its printed Case 2 coefficient also fails an exact symbolic check. This does not refute a repaired restricted theorem, but this paper is not used as a verified proof. A December 2025 unreviewed preprint claims a full positive solution via an abc bound; a false algebraic equality in its supporting argument was identified. No independently verified general resolution was located. This search result is not a proof that no such publication exists.

### 2. Boundary families, signs and elementary restrictions

P2025-v1 C1 gives all |x|<=1 families, including y=0 exactly at x=-1 and odd n. For |x|>=2 the sum has magnitude greater than 1; its sign is negative exactly when x<=-2 and n is odd. C2 records gcd identities and fully stated LTE hypotheses. In particular an odd prime dividing both x-1 and m must occur in m to an exponent divisible by q. When m is an odd prime, this excludes x=1 modulo m. C3 excludes nontrivial even powers for degree 2 by placing the sum between successive squares. These arguments are unreviewed partial candidates, not a complete answer or novelty claims.

### 3. Cyclotomic and block factorization

For x!=1, G_m(x) is the product of Phi_d(x) over divisors d>1 of m. P2025-v1 C4 gives a safe block factorization with its exact gcd. Treating these factors as automatically coprime fails: for the known (b) square identity x=7,m=4, G_2(7)=8 and G_2(49)=50 share gcd 2, although their product is 20^2. The shared primes tied to m require valuation bookkeeping, which is central in the published reductions.

Replacing negative x by -x-1 is valid for degree 2 only. For degree 4, G_5(2)=31 whereas G_5(-3)=61. Thus a positive-base theorem cannot be transferred by that substitution in general.

### 4. Exact finite search and counterexample tests

The reproducible script computations/investigate.py completed 2<=|x|<=10,000 and 2<=n<=128, screening 2,539,746 pairs. Degree 3 odd q>=3 was excluded; degree 3 uses a square screen and checks only even exponents. For all other pairs, an exact FLINT perfect-power test and SymPy maximal exponent identify every possible q>=2, since |y|>=2. No y-bound is imposed. All hits are checked by exact substitution. Only the six signed quadruples in proof.md were found. This is evidence on this finite rectangle, not evidence that the unrestricted conjecture has been proved.

The elementary formulas were also counterexample-tested for -100<=x<=100, 2<=n<=100, with odd primes through 19. An independent exact-root enumeration cross-checks the perfect-power method for 2<=|x|<=25, 2<=n<=16, with preliminary odd exponents excluded. Exact counts, versions, timings, parameters and script hash are in initial-results.json; the console transcript is initial-run.log.

### 5. Why straightforward extensions stop

Fixed finite congruence obstructions cannot rule out the entire remaining region: if L is the lcm of their moduli, choosing x=0 modulo L and y=1 modulo L makes G_m(x)=y^q modulo every such modulus for all m,q. This is only a statement about that limited method, not about integer solutions. Local valuations cut many residue classes but leave others. The nearest-square argument in C3 does not extend to arbitrary q and m, and the known x=3 degree-four square already blocks a blanket between-powers assertion.

The main unresolved prime-m cases require more than these elementary restrictions. Bounded searches do not supply a bound on x,m or q; the literature's simultaneous Runge and cyclotomic arguments must not be abbreviated into an unsupported finiteness assertion.

## Next steps

1. Obtain two independent blind adversarial audits of P2025-v1 if the coordinator wishes to promote these partial lemmas; one reviewer must reconstruct all four claims. Any substantive repair needs re-review.
2. Verify the full theorem and integer-domain hypotheses of Chen-Mihailescu 2026 before using its abstract-level class-number restriction. The diagonal case and class-number-divisible cases remain potential obstructions.
3. Audit the published negative-base reductions and references behind Bennett-Levin Proposition 1 before narrowing them further. Preserve the distinction between established theorems and original project arguments.
4. Pursue a targeted new idea for prime m and odd q, rather than repeatedly enlarging the finite rectangle. Any further computation should have explicit parameters and monitored cutoff.

All third-party full PDFs remain in the ignored local .cache/literature/2025/ cache; only citations, cache paths and hashes are stored in the year directory. The coordinator authorized this cache relocation. No commit or push was made by this owner.
