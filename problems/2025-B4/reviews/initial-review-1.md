# 2025 B4(b): initial independent adversarial review R1

Review completed independently on 2026-10-17 (Australia/Brisbane; UTC date 2026-10-16). This reviewer did not construct P2025-v1 and did not read another review, the shared issue log, or shared status logs. The author's research log was used only for the requested construction-history/source audit. This initial report was completed without another reviewer's conclusions.

**Verdict:** I recommend accepting **C1-C4 as correct elementary partial results** on the frozen input below. I found no substantive gap or counterexample in those four arguments. This is a reviewer recommendation, not a promotion. There is no full classification proof in this candidate, and no unrestricted classification is established by this review.

Frozen candidate: `problems/2025-B4/proof.md`, P2025-v1, SHA-256 `c422139567ee3e2f4eafd852c9a3f5fac73cb6c8e0bfdf9e2c9c5311a9348b0d`. The same hash was checked initially and after the audit. Other input and output hashes are in `initial-review-1-manifest.json` and `initial-review-1-sha256.txt`.

The launch request was gpt-6.1-sol with max reasoning. No independent effective-setting readback was available; this records requested settings only. Authoritative account telemetry read during this review was 8% used in the 10,080-minute weekly window, reset Unix time 1792745187, below the 90% total-used cutoff. No separately billed API was used.

## Official fidelity and scope

I directly extracted the part-(b) text on page 2 of [official Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2025_paper_b.pdf). It asks for integer quadruples `(x,y,n,q)` satisfying `x^n+...+x+1=y^q`, with `n,q>=2`. Thus neither positivity of x,y nor primality of q is available. The term count is `m=n+1>=3`. The candidate preserves all these conventions.

I read only the part-(b) unsolved-part remark on page 20 of the [official solutions](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2025solutions.pdf), not the preliminary proof. Its listed exponent slot is a term count and requires subtracting one to get the paper's degree. The candidate's `(3,±11,4,2)`, `(7,±20,3,2)`, `(18,7,2,3)`, `(-19,7,2,3)` have the correct official indexing and signs. Their identities were checked independently. They are attributed examples, not a proved exhaustive list.

The candidate's conclusions are explicitly partial. No preliminary degree-3 odd-q argument is reproduced here. The finite solution search excludes that slice.

## Independent reconstruction of every claim

### C1: boundary families, magnitude and signs

At x=0 the sum is 1. Its integer qth roots are 1, and also -1 exactly for even q. At x=-1 the alternating sum is 1 for even degree n and 0 for odd n; the qth roots of 0 consist only of 0. These yield exactly families 1-3, including every sign of y that is possible there.

At x=1 the sum is `n+1=m>=3`. Hence any integer root has absolute value a>=2 and satisfies `m=a^q`. For odd q the root must be a; for even q both a and -a work. Conversely every family-4 parameter gives n>=2 and the required identity. In particular this does not accidentally include n=1 or x=1,y=±1.

For x>=2 the first three terms already exceed 1 and all terms are positive. Write x=-a with a>=2. The finite geometric identity gives `(a^m+1)/(a+1)` for odd m and `-(a^m-1)/(a+1)` for even m. When m is odd it is at least `a^2-a+1>=3`; when m is even, m>=4 and `a^m-1>a+1`, so the sum is below -1. Thus no nonboundary base yields y=-1,0,1. The negative case is exactly x<=-2 and odd n, and an integer negative power then requires q odd and y<=-2. The remaining sign assertions follow from the parity of q. No domain gap found.

### C2: gcds and LTE, including signed bases

As integer polynomial identities, `G_m(x)=1+xH(x)` and `G_m(x)=m+(x-1)K(x)`. Therefore the two gcd identities hold without dividing by x or x-1. In particular x=0, x=1, and the zero sum at x=-1 with even m cause no exception: gcds are taken nonnegative and the polynomial identities remain valid.

For the valuation assertions |x|>=2 makes `x-1`, `x+1`, `x^m-1`, and `G_m(x)` nonzero whenever they are used. Valuation of a negative integer means valuation of its absolute value. If an odd prime p divides x-1, p does not divide x. To reconstruct the cited LTE step, write `m=p^t u` with p not dividing u. Binomial expansion of `z^u-1` about z=1 shows its valuation equals `v_p(z-1)`. For the p-power step, if `v_p(z-1)=h>=1`, the first term of `(1+(z-1))^p-1` has valuation h+1 and every later term has larger valuation, since p>=3. Iterating gives `v_p(x^m-1)=v_p(x-1)+v_p(m)`, including negative x. Dividing the nonzero product identity `(x-1)G_m(x)=x^m-1` at the valuation level gives the claimed formula.

For odd x and even `m=2^t u`, u odd and t>=1, the odd-u factor has no extra factor of 2. Factor `x^(2^t)-1` into `x-1`, `x+1`, and the factors `x^(2^j)+1` for 1<=j<t. Since every odd square is 1 modulo 8, each latter factor has 2-adic valuation 1. This proves the stated two-adic formula after subtracting `v_2(x-1)`, also for negative x. For even x the sum is 1 modulo 2; for odd x its parity is m's parity. Finally an actual nonboundary solution has `v_p(G_m(x))=q*v_p(y)`, so the valuation divisibility requirement is valid for composite q as well. No unstated LTE hypothesis remains.

### C3: degree two and even exponents

The substitution x -> -x-1 preserves `x^2+x+1`. If x is neither 0 nor -1, `t=max(x,-x-1)` is an integer >=1 and has the same polynomial value. The gaps from t^2 and to `(t+1)^2` are t+1 and t, respectively, both strictly positive. Therefore the value is not an integer square. Every even power `y^q=(y^(q/2))^2` is a square for arbitrary signed integer y and even q>=2. The two remaining bases give 1 and exactly y=±1. No boundary or parity exception found.

### C4: exponent reduction, block factors and zero factors

For each prime ell dividing q, `Y=y^(q/ell)` is an integer, including negative and zero y, and `Y^ell=y^q`. No assumption that q itself is prime is introduced.

For positive r,s, expansion of `G_r(x)G_s(x^r)` enumerates every exponent i+rj from 0 to rs-1 once. Interpret `G_1=1`, as the same finite-sum definition prescribes. Let `E_s(T)=(G_s(T)-s)/(T-1)` in Z[T]. Then

`G_s(x^r)-s=(x-1)G_r(x)E_s(x^r)`.

This is an identity, not division by a possibly zero number, and gives the gcd formula for every integer x. If `G_r(x)=0`, the only relevant integer possibility is x=-1 and even r; then x^r=1 and `G_s(x^r)=s`, so both gcds equal s. The cases r=1, s=1, x=0 and x=1 also satisfy the formula directly. There is no hidden zero-gcd convention or cancelled zero factor.

For |x|>=2 neither block factor vanishes, including r=1 or s=1. If their gcd is 1, each prime dividing one factor does not divide the other. Its exponent in the product is therefore its exponent in that factor, and is a multiple of q. Unique factorization proves that each **absolute value** is a qth power; a unit factor is `1=1^q`. The absolute-value wording correctly avoids an unjustified signed-factor assertion when q is even. The candidate does not infer coprimality of arbitrary cyclotomic factors. No gap found.

## Primary-source theorem and source-error audits

### Bennett-Levin 2015

I checked published pages 15-17, including page-16 rendering, in the [author-posted published PDF](https://personal.math.ubc.ca/~bennett/BeLe-Mona-2015.pdf). Equation (1) assumes integer |x|,|y|>1, term count m>2 and q>=2. Proposition 1 applies outside the four known identities: q is odd >=3; the least prime divisor of m is >=5; |x|>=10^4; and x has a prime divisor congruent to 1 modulo q. Known even-power identities must first include both signs of y, as the author explicitly notes.

Published Theorem 1 says every solution satisfies `omega(m)<=Omega(m)<=3`, counting multiplicity. This is a **necessary condition**, not a classification of the cases Omega(m)<=3. It includes signed bases. The unfamiliar-solution restrictions imply odd m and even official degree n, without settling that remaining region. The cached arXiv first two pages confirm its main theorem is numbered 2. The author's statement-level translation and attribution are correct; I did not reconstruct the entire published proof.

### Bugeaud-Mihailescu 2007

I checked original pages 177-179 and rendered page 178 in the [primary journal PDF](https://journals.msp.org/mscand/article/download/659/658). Equation (1) requires x,y>1, m>2, q>=2. Theorem NL's exhaustive restricted cases are q=2, 3|m, 4|m, or q=3 with m not congruent to 5 modulo 6.

Theorem 1 applies to solutions outside the three positive known identities. It asserts least prime divisor of m >=29, Omega(m)<=4, primality of m if q=3, and m=q if q divides m. These are necessary restrictions in that positive domain. Theorem 2 is a sufficiency reduction for proving absence of additional positive solutions: it suffices to exclude prime term counts p>=5 for all odd primes q. It does **not** assert that every solution has prime term count. The paper's prime p and q need not be distinct in this reduction. The author's translations correctly retain the positive-base restriction and the direction of this reduction. I did not reconstruct the complete published proof.

### Son 2026: narrowly verified printed errors

I read the complete five-page [original journal paper](https://math.colgate.edu/~integers/aa44/aa44.pdf), including Theorem 3/Remark 1 and all three proof cases, and rendered equation (6). The all-integer statement omits the defined quotient solution x=-1,y=1. Independently, arithmetic in `Z[rho]`, `rho^2=rho+1`, gives rho coefficient `a^3+3a^2*b+6a*b^2+3b^3` in `rho(a+b*rho)^3`, not equation (6)'s coefficient. At a=-1,b=1 the actual element is `2-rho`, consistent with the omitted solution. Remark 1 invokes a condition requiring term count not congruent to 5 modulo 6, which term count 5 fails. These are verified errors in the printed statement/argument. They neither refute a repaired nontrivial nonexistence theorem nor supply an unrestricted classification.

### Wang 2025 v1: supporting argument not accepted

I read [the original v1 full text](https://www.preprints.org/manuscript/202512.0286/v1), including all of Theorem 7's induction and Theorem 8's application; the site labels v1 unreviewed. In equation (33), put `T=zeta*rad(abc)^2` and use the previously defined `rho=1/sqrt(T)` and `c=floor(T)+1`. Then `sqrt(c)/rho=T*sqrt(c/T)`, whereas the printed equality has `sqrt(c/T)`. The following inequality (35) uses the smaller expression, so the error affects the contradiction. Theorem 8 explicitly depends on Theorem 7 and claims a positive-domain classification. This particular proof is not established by the displayed argument. This audit supplies no counterexample to its claimed abc bound, no disproof of Nagell-Ljunggren, and no negative-base theorem. A direct curl request returned HTTP 403; I used the accessible public web rendering and preserved normalized extraction, without attempting to bypass that response.

### Chen-Mihailescu 2026: public full statement found, with exceptions

I found the journal's explicit [public full-text PDF link](https://camath.fudan.edu.cn/cambcn/ch/reader/create_pdf.aspx?file_no=47B208&flag=1), rather than relying on [the publisher abstract](https://link.springer.com/article/10.1007/s11401-026-0018-7). Pages 389-391 define `(x^p-1)/(x-1)=p^e*y^q`, with e=1 when x is 1 modulo p, otherwise 0, and work with nontrivial integer solutions, odd primes p>=5, q!=p, and `q` not dividing `h_p^-`. Theorem 1.2 excludes solutions outside the signed known set **except possibly some with p<29 and x<0**. Its footnote explains the positive-x premise behind the imported 29 bound. Section 1.2 explicitly retains q!=p and reduces to e=0 using the cited e=1 result. Therefore neither the diagonal p=q case nor the stated negative-base exceptions may be silently removed. This is a checked theorem-statement/domain audit, not independent verification of all 24 pages of proof. The author's abstract-only treatment was appropriately cautious; any upgrade must include this exception and these premises.

## Independent exact evidence and preserved limitations

Command: `.venv/bin/python -u problems/2025-B4/reviews/initial-review-1-run.py`. The supervisor launched child PID 30856 with a hard 60-second timeout, preserved parameters/PID in `initial-review-1-job.json`, and wrote incremental checkpoints to `initial-review-1-child.log`. It completed with exit code 0 in about 1.02 seconds. Dependency: Python 3.12.14 standard library only; neither FLINT nor SymPy was used. The root test is an independent integer binary search.

Results in `initial-review-1-evidence.json`:

- 158,112 boundary quadruples checked; 915 preliminary-slice tuples deliberately skipped.
- 15,054 polynomial/gcd pairs; 14,820 nonboundary sign pairs; 15,366 odd-prime LTE checks; 3,666 two-adic LTE checks.
- 1,999 degree-two nonsquare checks, including negative bases.
- 15,975 block factor/gcd triples, including 161 cases with a zero factor, plus 1,066 signed exponent-reduction checks.
- 3,658 pairs with 2<=|x|<=60 and 2<=n<=32, testing every possible q>=2 by exact roots, except degree 3 with odd q. There were 246,447 exact root tests and precisely the six signed known examples.
- 625 exact quadratic-ring coefficient checks independently confirm the Son algebra discrepancy. The Wang equality was also checked with exact squared rational quantities; it differs by factor T before squaring, not merely notation.

These computations are finite evidence, not proofs of unrestricted assertions. The unrestricted conclusions in C1-C4 rest on the reconstructions above. I inspected the author's original search script and its finite-range claims but did not rerun its 2.5-million-pair rectangle. No failure or partial download is described as complete. Source-download attempts and hashes, including preserved incomplete Chen transfers and the Wang HTTP failure, are recorded in the manifest and cache job files.

## Reviewer issue register and recommendation

| R1 item | Severity | Disposition |
|---|---|---|
| C1-C4 proof correctness | None found | Recommend acceptance of these partial lemmas on the frozen hash, subject to the separate second review and coordinator decision. |
| Integer domains and official degree/term indexing | None found | Both signs of square roots and all x=-1,0,1 families are retained. |
| Imported restrictions versus solved ranges | None found | Omega bounds and positive-only restrictions are correctly treated as necessary conditions/imported context. |
| R1-2025-source-1: Chen full-text exception | Informational source update | Newly located primary statement retains p<29,x<0 exceptions and q!=p; author should include them if replacing the current abstract-only lead. No change to C1-C4 is required. |
| Son/Wang rejected arguments | None found in the narrow objections | Rejection is limited to the identified printed statement/inference, not a claim that either broader conjecture has been disproved. |

No candidate edit, promotion, commit, push, global process termination, purchase, or access-control bypass was performed by this reviewer.
