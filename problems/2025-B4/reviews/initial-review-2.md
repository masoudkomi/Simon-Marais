# Independent initial review R2 of P2025-v1

**Review completed blind on 2026-10-17 Australia/Brisbane (2026-10-16 UTC).** This is an adversarial reconstruction and source audit of the partial candidate only. It is not a proof of the unrestricted 2025 B4(b) classification and does not promote any result.

## Frozen input and independence

- Candidate: `problems/2025-B4/proof.md`, P2025-v1, SHA-256 `c422139567ee3e2f4eafd852c9a3f5fac73cb6c8e0bfdf9e2c9c5311a9348b0d`. The hash matched before reconstruction and again at completion.
- I did not construct this candidate. I read no other review conclusions, other reviewers' source notes, shared issue log, or shared progress/status file. The primary 24-page Chen-Mihailescu PDF happened to have an `initial-review-1-` cache filename; only its actual PDF content was used.
- I reconstructed C1-C4 from the candidate before consulting the author's `research.md` for the imported restrictions referenced by `references.md`. That author-log read was after the independent mathematical reconstruction. It was not used to establish any elementary inference.
- Requested launch settings supplied by the coordinator: `gpt-6.1-sol`, reasoning `max`. Independent effective-setting readback: unavailable. These are requested settings, not verified runtime settings.
- Authoritative usage tool readings at entry and after the source audit: 9% total weekly used, window 10080 minutes, reset Unix `1792745187`; the project cutoff is 90%. No billed API, purchase, subscription, or access bypass was used.
- Ownership: only `problems/2025-B4/reviews/initial-review-2*` and my ignored cache artifacts were written. The candidate and author files were unchanged. No commit or push was made.

## Overall finding

I found no substantive mathematical objection to C1-C4. Each is valid as a partial reduction over the official integer domain, after interpreting valuations of negative integers as valuations of their absolute values. The conclusion of the complete classification remains conjectural as the candidate explicitly states.

The literature audit is substantially careful about domains and necessary-versus-sufficient conditions. Its Chen-Mihailescu entry should now be updated from the abstract lead to the full theorem, including its printed small-prime negative-base exception. This is a source-documentation repair, not a dependency failure of C1-C4. The Son and Wang objections below concern the printed statements or displayed arguments; they do not disprove the corresponding restricted nonexistence or abc conjectures.

## Official B4(b) fidelity

I checked the original [Paper B, page 2](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2025_paper_b.pdf), and only the open-part remark on [solution page 20](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2025solutions.pdf). B4(b) has integer variables `(x,y,n,q)`, `n,q>=2`, and a polynomial of degree `n`. Thus `m=n+1>=3` is the term count; the quotient formula is used only where its denominator is nonzero. Boundary `x=-1,0,1` and both signs of `y` belong to the official domain. The solution remark's exponent slot uses the literature term count. The candidate translates its known examples correctly. I did not investigate or reproduce the preliminary argument.

## Full independent reconstruction

### C1: boundary families, magnitude, signs

For `x=0`, the polynomial is 1, so the integer roots are `y=1` and also `y=-1` for even `q`. For `x=-1`, the alternating sum is 1 when `m` is odd (`n` even), and 0 when `m` is even (`n` odd); the claimed roots follow, including `y=0` for every allowed exponent in the latter case. For `x=1`, the value is `m>=3`. Writing its positive integer root as `a` forces `a>=2`, `m=a^q`, and `n=a^q-1`; a negative root occurs exactly for even `q`. This parameterization automatically meets `n>=2`.

For `x>=2`, the value is positive and at least `1+x+x^2>1`. For `x=-a<=-2`, multiplying the polynomial by `x-1` gives the candidate's two rational expressions without any division by zero. Odd `m>=3` gives at least `(a^3+1)/(a+1)=a^2-a+1>=3`. Even `m>=4` gives magnitude `(a^m-1)/(a+1)>1`, since `a^4-1>a+1`. The even case has negative sign, the odd case positive sign. Hence all solutions with `y=0,1,-1` were already included, and every remaining solution has `|y|>=2`. A negative value requires odd `q` and negative `y`; a positive value has the signs stated in the candidate. No parity or sign case is omitted.

**C1 disposition:** passes reconstruction and boundary audit.

### C2: gcds and exact valuation hypotheses

For `x!=0`, division with integer remainder gives `G_m(x)=1 (mod x)`, proving the first gcd identity. At `x=0`, it says `gcd(1,0)=1`. For `x!=1`, evaluation at 1 gives `G_m(x)=m (mod x-1)` and the second identity follows by the Euclidean algorithm, with gcds nonnegative. At `x=1`, both sides are `gcd(m,0)=m`. This also treats `x=-1`: for even `m`, the zero sum has gcd 2 with `x-1=-2`, exactly `gcd(m,-2)`. No unspoken positive-gcd convention is needed beyond the one stated.

For completeness I reconstructed the needed odd-prime LTE identity, rather than merely accepting its name. Let `p` be odd, `p|(x-1)`, and `t=v_p(x-1)>=1`. For a positive exponent `d` coprime to `p`, `G_d(x)=d (mod p)`, so `v_p(x^d-1)=t`. For any integer `z=1+u` with `v_p(u)>=1`, the binomial expansion of `z^p-1` has first term `pu` of valuation `1+v_p(u)`. Every other term has strictly larger valuation: middle terms have at least `1+2v_p(u)`, and the last term at least `p v_p(u)>1+v_p(u)`. Iterating this step with `m=p^a d` gives `v_p(x^m-1)=t+a`. Subtracting `t` proves `v_p(G_m(x))=v_p(m)`.

All hypotheses are met: `m` is a positive integer, `p` is odd, `p|(x-1)` makes `p` coprime to `x`, and `|x|>=2` prevents `x^m-1`, `x-1`, or `G_m(x)` from vanishing. The binomial argument uses integer divisibility and applies unchanged to negative `x`.

For the 2-adic formula write `m=2^a d`, `a>=1`, `d` odd. For odd `x`, the quotients `(x^d-1)/(x-1)` and `(x^d+1)/(x+1)` are odd; hence the two valuations are `v_2(x-1)` and `v_2(x+1)`. Every further squaring contributes one from `x^{2^j d}+1`, because an odd square is 1 modulo 8 for `j>=1`. Thus

`v_2(x^m-1)=v_2(x-1)+v_2(x+1)+a-1`.

Subtracting `v_2(x-1)` gives C2. The condition `|x|>=2` excludes `x=1,-1`, so no valuation of zero is invoked. Modulo 2 the geometric sum is odd when `x` is even, and equals `m` modulo 2 when `x` is odd. For an actual nonboundary solution, `v_p(G_m)=q v_p(y)`, with finite valuations, justifying divisibility by the full exponent `q` (not only a prime divisor).

**C2 disposition:** passes reconstruction; no missing LTE sign or zero hypothesis.

### C3: official degree two and every even exponent

Direct expansion gives `x^2+x+1=(-x-1)^2+(-x-1)+1`. For every integer outside `x=0,-1`, the representative `t=max(x,-x-1)` is an integer at least 1. Subtracting neighboring squares yields

`(t^2+t+1)-t^2=t+1>0`, and `(t+1)^2-(t^2+t+1)=t>0`.

Therefore it is not a square. For every even `q>=2` and integer `y`, `y^q=(y^(q/2))^2` is a square, irrespective of the sign of `y`. The only remaining `x` give value 1 and `y=1,-1`. This is precisely the stated portion of B4(b) with official degree `n=2`; there is no degree/term-count interchange.

**C3 disposition:** passes reconstruction; the strict upper inequality is valid even at the smallest `t=1`.

### C4: exponent reduction, factorization, zero factors

If the prime `ell` divides `q`, the integer `q/ell` is positive and `Y=y^(q/ell)` is an integer with `Y^ell=y^q`. This preserves negative values when they can occur; it assumes no positive root convention.

For all positive `r,s`, the products of monomials in `G_r(x)G_s(x^r)` have exponents `i+rj`, `0<=i<r`, `0<=j<s`, which enumerate `0,...,rs-1` uniquely. Thus the polynomial identity is universal. Also `G_s(T)-s=(T-1)H(T)` for an integer polynomial `H`, so

`G_s(x^r)-s=(x-1)G_r(x)H(x^r)`.

The Euclidean gcd identity therefore gives `gcd(G_r(x),G_s(x^r))=gcd(G_r(x),s)`. This derivation did not divide by `G_r` and remains valid at `G_r=0`: then `x^r=1`, the second factor is `s`, and both gcds are `s`. For example, `x=-1`, even `r` gives exactly this case. When the second factor is zero instead, e.g. `x=-1`, odd `r`, even `s`, the same congruence proof works. The endpoints `r=1` or `s=1` are valid with `G_1=1`.

For `|x|>=2`, `G_r(x)` cannot vanish: for `r=1` it is 1, otherwise its quotient representation has nonzero numerator; the same reasoning applies to `G_s(x^r)` since `|x^r|>=2`. If these nonzero factors are coprime, every prime divides at most one, so its valuation in that factor is the valuation in their product. A `q`th power product makes each such valuation a multiple of `q`. Unique prime factorization then makes each absolute value a `q`th power, including the value 1. This is deliberately an absolute-value conclusion and does not assume unjustified signs or coprimality of arbitrary cyclotomic factors.

**C4 disposition:** passes reconstruction, including zero-factor gcds outside the final nonboundary application. Defining `G_k` explicitly for every positive `k` would be a harmless notation clarification, since `r,s` can be 1 or 2; it is not a substantive gap.

## Conjectural classification and exact examples

The candidate labels its full answer as conjectural and attributes it to the integer Nagell-Ljunggren conjecture. This is the correct logical status. The displayed patterns represent six signed official-domain quadruples: two signs at the two square identities and a single positive root at each cube identity. Exact Horner substitution confirms sums 121, 400, 343, 343 at degrees 4, 3, 2, 2 respectively, including `x=-19`. No assertion of completeness follows from those checks or from C1-C4.

## Independent source audit

The source manifest records byte hashes of each local primary PDF used, and a separate provider-extraction hash for Wang, whose direct cache download returned HTTP 403. Full third-party source text and page images remain only in ignored `.cache/`. Original sources are linked below. Published theorem proofs were not reconstructed in full; this audit checks their statements, domains, and the logic of the proposed imports.

### Bennett-Levin 2015

I read equation (1), Proposition 1, Theorem 1 and their surrounding discussion on printed pages 15-17 in the [author-posted published PDF](https://personal.math.ubc.ca/~bennett/BeLe-Mona-2015.pdf). Its domain is integer `|x|,|y|>1`, term count `m>2`, `q>=2`. After identifying the even-root sign copies with its displayed known identities, Proposition 1 restricts any further solution to odd `q>=3`, least prime factor of `m` at least 5, `|x|>=10^4`, and a prime divisor of `x` congruent to 1 modulo `q`. Theorem 1 asserts `omega(m)<=Omega(m)<=3` for solutions, counting multiplicity in `Omega`. This is a necessary bound; it excludes `Omega(m)>=4`, and does not solve the range `Omega(m)<=3`. Its discussion explicitly warns that making the term count prime is not automatically without loss. Negative bases are included. The elementary part of its proof initially leaves a special `(m,q)=(p^5,5)` case, which the published proof removes using an earlier cited result; the final theorem has no such exception. The author's translated claims preserve these distinctions. I did not re-audit the cited chain behind Proposition 1.

### Bugeaud-Mihailescu 2007

The [primary journal PDF](https://journals.msp.org/mscand/article/download/659/658), printed pages 177-179, defines equation (1) with `x,y>1`, `m>2`, `q>=2`. Theorem NL lists solved conditions `q=2`, `3|m`, `4|m`, or `q=3` and `m!=5 (mod 6)`, outside its three positive exceptions. Theorem 1 imposes least prime factor of `m>=29` and `Omega(m)<=4` on further positive solutions; additionally `m` is prime for `q=3`, and `q|m` implies `m=q`. These restrictions cannot be imported to negative `x`. Nor does the Omega bound classify its permitted range. Theorem 2 is a sufficiency reduction for proving nonexistence: eliminating further positive prime-term-count equations for odd primes `p,q`, `p>=5`, would eliminate further positive general solutions. Read with the displayed known `p=5,q=2` and `p=3,q=3` exceptions, it is not an assertion that every original solution has prime term count. The author's domain and quantifier-direction cautions are correct. I checked these statements and relevant proof context, not every external theorem used in their proof.

### Son 2026

I read all five pages of the [journal paper](https://math.colgate.edu/~integers/aa44/aa44.pdf), including its introduction, unit normalization, all three proof cases, and final conclusion. Theorem 3 and Remark 1 explicitly claim an all-integer result for `m=5,q=3`. The omitted pair `x=-1,y=1` satisfies its defined quotient. This refutes that literal statement only. Remark 1 incorrectly invokes condition (iv) at term count 5; the author-audit wording is a paraphrase of this mistaken invocation.

Independently, in `rho^2=rho+1`, the rho coefficient of `rho(a+b rho)^3` is `a^3+3a^2 b+6ab^2+3b^3`. The printed Case 2 equation (6) uses the different Case 1 coefficient. At `a=-1,b=1`, the actual product is `2-rho`, corresponding to the omitted boundary solution, while the printed coefficient is 1. Equation (7) and the modular elimination subsequently use the erroneous equations, so this is a gap in the printed argument, not merely an unused typo. It does not refute nontrivial nonexistence established by a repaired or different argument. The candidate does not rely on this paper.

### Chen-Mihailescu 2026: full statement supersedes abstract-only lead

I checked the complete 24-page [public journal PDF](https://camath.fudan.edu.cn/cambcn/ch/reader/create_pdf.aspx?file_no=47B208&flag=1), particularly printed pages 389-392, 405-407, 410-411. In the intended nontrivial domain `|x|,|y|>1`, equation (1.3) has distinct odd primes `p,q`, `p>=5`, and `e=1` exactly when `x=1 (mod p)`, otherwise `e=0`. Theorem 1.2 assumes `q` does not divide the minus class number `h_p^-` and excludes solutions outside its six signed known exceptions **except possibly when `p<29` and `x<0`**. Its footnote explains the positive-base origin of a bound used in the proof. Theorem 1.1 separately quotes the `e=1` exclusion. Subsequent work treats `e=0`, `q!=p`; it does not cover the diagonal or class-number-divisible cases. The class number is the minus quotient for `Q(zeta_p)`, not an unspecified class number. Nontriviality is inherited from the opening domain and repeated in the setup; the theorem is unsafe as a literal statement about boundary `x,y`. The abstract omits the printed small-prime negative exception. This verifies a conditional restricted import, not its whole proof or an unrestricted solution.

### Wang 2025 v1

I read the full relevant Theorem 7 induction and Theorem 8 application in the [original v1 HTML](https://www.preprints.org/manuscript/202512.0286/v1) and provider-extracted [v1 PDF](https://www.preprints.org/manuscript/202512.0286/v1/download). The source labels v1 unreviewed; Theorem 8 concerns positive variables and depends explicitly on Theorem 7. Set `T=zeta rad(abc)^2` in its induction, so `rho=1/sqrt(T)`. At `c=floor(T)+1`, the term `sqrt(c)/rho` is `sqrt(cT)=T sqrt(c/T)`. Equation (33) replaces it by `sqrt(c/T)`, dropping `T`. The subsequent equation (35) uses that smaller value to force a contradiction. Restoring `T` removes that inference; there is no justification elsewhere in the displayed induction for the strengthened bound. The error prevents accepting this proof, and therefore its dependent positive classification, on the supplied argument. It is not a counterexample to either theorem's conjectural conclusion. Theorem 8's preliminary use of the 29 bound must also be understood only for a hypothetical additional solution; its text does not explicitly say so. No negative-base conclusion is claimed there.

## Exact finite evidence, reproducibility, and limits

`initial-review-2-checks.py` is independent standard-library Python code, not a rerun or import of the author's 2.5-million-pair code. `initial-review-2-run.py` launches a dedicated child with an explicit 45-second timeout, records its PID and parameters, and saves flushed checkpoint output. It completed without failed assertions or a timeout. The child PID, command, elapsed time and exit code are in `initial-review-2-job.json`; results and complete incremental output are in the correspondingly named JSON and log files.

| Check | Finite scope | Completed evidence |
|---|---|---|
| Boundary roots | `x=-1,0,1`, degree 2-32, exponent 2-12, integer roots -40 to 40 | 1,023 triples agree with C1 |
| Signs and gcds | integer `x=-120,...,120`, term count 3-72 | 16,660 nonboundary signs; 16,870 gcd pairs |
| LTE | same nonboundary range; odd primes through 43 | 18,410 odd-prime and 4,130 two-adic checks |
| Degree-two squares | integer `x=-2000,...,2000` | 4,001 checks, only `x=-1,0` squares |
| Block products/gcds | integer `x=-80,...,80`, `r,s=1,...,12`, `rs>=3` | 22,701 pairs; 106 zero-factor cases |
| Independent power enumeration | `2<=|x|<=60`, degree 2-20, every possible exponent via exact integer roots, no y bound | 2,242 pairs; 96,523 exact-root tests; exactly six signed known quadruples |
| Reduction and factor powers | all hits above, every prime dividing each exponent, every block divisor | 6 exponent reductions; 8 coprime factor-power checks |
| Son coefficient | pair arithmetic in `Z[rho]`, `a,b=-10,...,10` | 441 checks plus exact boundary witness |
| Wang substitution | exact squared quantities at `T=36,40,144,10000` | missing factor confirmed; identity diagnostics only |

The nontrivial power enumeration skips official degree 3 with odd exponent. No preliminary proof was reconstructed or brute-forced. All evidence is finite. In particular, the small power scan supplies neither a bound on unrestricted variables nor a proof of the final conjecture. Wang's numerical samples are tests of an algebraic substitution, not claimed abc triples satisfying the preprint's contradictory assumptions.

## Issue dispositions and requested author-side follow-up

| ID | Affected item | Finding | Disposition |
|---|---|---|---|
| R2-2025-01 | C1-C4 | No substantive gap after complete independent reconstruction | No proof repair requested; coordinator controls any later status change |
| R2-2025-02 | `references.md` item 4; `computations/literature-audit.md` final paragraph; author next steps | Abstract-only Chen-Mihailescu entry lacks the now-available full-theorem exception | Update with full source, exact class-number condition, distinct-prime/nontrivial domain, and possible `p<29,x<0` exception before any application |
| R2-2025-03 | C4 notation | `G_r,G_s` include indices 1 or 2 although the opening working term count is >=3 | Optional clarification `G_k` defined for every positive k; no change of mathematical conclusion |
| R2-2025-04 | Full classification | Neither finite computations nor imported necessary conditions give completeness | Existing conjectural/unresolved labels are required and already correct |
| R2-2025-05 | Son/Wang audit | Printed statement/argument objections independently confirmed in context | Keep narrow conclusions; do not turn these into refutations of broader conjectures |

I did not inspect or alter the shared issue log. This report is the reviewer-owned issue record for coordinator integration. Any substantive later alteration of the candidate or application of the new literature needs its own affected-argument review. This completes R2's blind initial audit.
