# Strong Fermat-Catalan primary-source audit 1: blind reconstruction v1

Status: **candidate source audit - unverified by a second auditor**. This is one independent adversarial review, not a promotion or a coordinator acceptance decision. The intended nontrivial theorem has not been reconstructed as a valid proof here. No counterexample to that intended nontrivial theorem is claimed.

## Independence, scope, settings and source identity

- Reviewer: `/root/review_2025_strongfc_r1`, assigned a fresh whole-source reconstruction. No proof construction role and no other Strong FC reviewer report read.
- Before freezing this file, read only the assigned source manifest, `AGENTS.md`, the PDF skill, the official-domain normalization in `problems/2025-B4/statement.md`, and the primary preprint. In particular, `notes/deep-literature-r1-report-v1.md` was **not** read before the blind file and issue list were completed. A later comparison, if performed, belongs in a separate file.
- The assignment supplied generic audit topics (including integrality, norms, modules and exponent boundaries), and the locating manifest named Lemma 5 on pp.8-9. Neither supplied an earlier reviewer's substantive conclusion; this prior guidance is disclosed rather than claiming no prior information about where to inspect.
- Requested launch settings: `gpt-6.1-sol`, reasoning `max`, as supplied in the coordinator assignment. Verified effective model/reasoning readback: **unavailable**. These are distinct records.
- Scope: 2025 B4(b), specifically possible relevance of the claimed theorem to signed integer geometric sums. No investigation or reproduction of preliminary part (a).
- Primary source: Preda Mihailescu, *The strong Fermat-Catalan Equation*, arXiv:2509.18275v1, submitted 2025-09-22. Cached PDF title page says “Version 1.0 September 24, 2025.”
- Source URL: <https://arxiv.org/abs/2509.18275v1>; PDF <https://arxiv.org/pdf/2509.18275v1>.
- Exact audited local bytes: `.cache/literature/deep-literature-r1/2025-mihailescu-strong-fermat-catalan-v1.pdf`, 424143 bytes, SHA-256 `daba36d8971a346d4cd40d0b823f787034c4a11b67e76258beeb7574e6fe2669`.
- All ten PDF pages were extracted and visually inspected. PDF page numbers and printed page numbers coincide, 1 through 10. All locators below refer to these bytes.
- The arXiv metadata page was checked on 2026-10-16. Its v1 submission date agrees with the cached PDF margin. The experimental HTML at the v1 URL displayed a different internal date, “August 24, 2026”; I did not substitute that rendering for the hashed PDF. This discrepancy requires a separate source-version check before treating HTML/PDF variants as interchangeable.
- Authoritative account-wide weekly telemetry at 2026-10-16 21:28:56 UTC: 15% total used, 10080-minute window, reset `1792745187`. The assigned cutoff is 90% total, with integration/review reserve; no new weekly window was spent into.

## Outcome and exact remaining barriers

The outline is to construct Jacobi generators from a hypothetical solution, factor certain rational integers through differences of their conjugates, prove a universal congruence ideal is trivial (Lemma 5), deduce every prime dividing `XY(X+Y)` except `q` is `1 mod q` (Lemma 6 and Proposition 1), then apply this to the unavoidable prime 2.

I cannot validate the two central implications, even after granting the customary cyclotomic/Jacobi machinery and correcting several evident notation errors:

1. **Lemma 5, PDF pp.8-9:** from `beta(t1) | chi` and `beta(t2) | chi`, the proof passes to `beta(t1) beta(t2) | chi`. It supplies no coprimality or valuation argument. For every non-norm positive `t`, the characteristic-ideal valuations actually exhibit the precise obstruction to the asserted integrality of `chi / beta(t)`; see SF1-01 below. A missing integral divisibility statement is essential before Kronecker's theorem can be used.
2. **Lemma 6, PDF p.9:** complete splitting of a prime of `Q(zeta_p)` in `Q(zeta_p,zeta_q)` is converted to complete splitting of the rational prime in `Q(zeta_q)`. The stated decomposition-group implication is not valid in a direct product. The explicit unramified example `(p,q,r)=(5,3,2)` disproves that implication as a general number-field assertion. It is not a solution of the Diophantine equation; additional information about these special Jacobi differences would be needed.

Additional upstream defects are material: the printed universal ideal is an intersection where the proof uses a common divisor; norm group-ring elements have not been excluded; the `p=5`, weight-2 construction yields only the norm; the sign argument in Lemma 4 is not generally the stated positive sign; and the case `e=1` loses a factor of `p^k` in the passage to differences. These are recorded separately rather than used as a vague aggregate reason to reject a result.

Thus the appropriate research status, pending the coordinator's two-audit process, is **unverified preprint claim, not available as an established exclusion theorem for 2025 B4(b)**. The audit neither proves the intended theorem nor constructs a nontrivial counterexample to it.

## Domain audit before reconstruction

Write the preprint variables as `X,Y,Z` to avoid confusing them with the official geometric-sum variables. The intended claim from the abstract is

`(X^p+Y^p)/(X+Y) = p^e Z^q`,

with nonzero coprime integers, `p>3`, distinct **odd** primes `p,q`, and `e=0 or 1`. The proof's Assumption 1 on PDF p.3 imposes `X > |Y| >= 1`; Section 3 on p.7 explicitly speaks of a nontrivial solution. The abstract, Equation (2), Theorem 1, and proof assumption do not give fully identical formulations:

- Equation (2), PDF p.1, says distinct primes but does not repeat that `q` is odd. The abstract and final parity argument do require odd `q`. If Equation (2) were read literally to include `q=2`, the already established official example corresponding to `(X,Y,Z;p,q,e)=(3,-1,11;5,2,0)` contradicts it. This is attributed boundary context, not a new treatment of preliminary part (a), and is not a counterexample to the intended odd-`q` claim.
- Theorem 1 on p.2 says no integer solutions of (2), while (2) excludes only zero variables. For any allowed distinct odd primes, `X=Y=1`, `Z=1`, `e=0` is a literal counterexample to that unrestricted wording. Simultaneous sign change gives `X=Y=-1` too. These are trivial cases, excluded by the intended nontrivial assumption; they do not refute the intended theorem.
- The displayed quotient requires `X+Y != 0`. Interpreting it instead as the polynomial continuation at `X+Y=0` introduces further boundary cases. The proof does not authorize that extension.
- Swapping `X,Y` and changing both signs preserves the quotient, whose degree is `p-1`. After excluding equal absolute values and zero variables, this does justify `X>|Y|>=1`. It does not justify discarding the equal-absolute-value cases without first recording them.
- The equation plus `gcd(X,Y,Z)=1` forces `gcd(X,Y)=1`: a prime dividing both `X,Y` divides the homogeneous numerator of degree `p-1`, and hence `Z` (also at `p`, since `p-1-e>0`). Conversely a prime dividing one of `X,Y` and `Z` would divide the other variable. Thus the pairwise coprimality used later can be recovered.
- For odd `p`, the quotient is positive whenever it is defined. With odd `q`, `Z>0`. The intended nontrivial normalized domain has `Z>1`; this matters for injectivity of the beta map. For `e=0`, the absolute values of the cyclotomic factors are at least `X-|Y|>=1` and not all equal to 1. For `e=1`, `p|X+Y` gives `X >= (p+1)/2`, and the elementary bound `(X^p+Y^p)/(X+Y) >= X^(p-1)/2 > p` shows `Z>1` there as well.

## Whole proof reconstruction and inference audit

### A. Rational gcds, valuations and characteristic ideals (PDF pp.2-4)

For odd `p` and `s=X+Y`, the polynomial expansion is

`(X^p+(s-X)^p)/s = p X^(p-1) - binom(p,2) X^(p-2) s + ... + s^(p-1)`.

Consequently the gcd with `s` divides `p`. If `p|s` and `p` does not divide `XY`, the valuation of the quotient is exactly 1. If `p` does not divide `s`, the quotient is a unit modulo `p`. This recovers `e=1 iff p|s`, `p` not dividing `Z`, and `gcd(Z,XY(X+Y))=1`.

The printed proof of Fact 1 has an extra division by `s` in its last expression; Fact 1's general wording also fails to require odd `p`, needed for the polynomial quotient in that form. Neither issue blocks the intended `p>3` case after correction. Remark 2 incorrectly starts with gcd equal to 1 even when `e=1`, and writes `Z^p` where `Z^q` is relevant. The conclusion `gcd(Z,XY(X+Y))=1` remains recoverable by the preceding valuation argument. The Barlow-Abel factorization (4) follows by distributing prime valuations between `s` and the quotient. It provides context for the weaker Fermat-Catalan equation but is not needed for the later contradiction.

Set `F=Q(zeta_p)`, `lambda=1-zeta_p`, and initially set

`a=(Y+zeta_p X)/lambda^e`, `A=(a,Z)`.

This initial `a` is distinguished from the redefined, unnormalized `alpha=Y+zeta_p X` in Definition 3. Its norm is `Z^q`.

Lemma 1, points 1-3, can be reconstructed. Integrality of `a` is clear when `e=0` and follows from `p|X+Y` when `e=1`. Any common prime of two conjugates of `a` would lie over `p`, because subtracting their unnormalized numerators gives a unit multiple of `lambda X`, and an analogous linear combination gives a unit multiple of `lambda Y`. But `a` is a unit at `lambda`: for `e=0`, reduce `X+Y` modulo `lambda`; for `e=1`, use `a=(X+Y)/lambda-X`, with `v_lambda((X+Y)/lambda)>=p-2`. This excludes that prime. Several printed linear combinations on p.4 interchange the letters `X,Y`; the two requisite combinations themselves are elementary and available.

Every prime in `(a)` has exponent divisible by `q`, because its conjugate ideals are pairwise coprime and their product is `(Z^q)`. The gcd ideal `(a,Z)` therefore has exactly one `q`th of each exponent in `(a)`. Thus `A^q=(a)` and `Norm(A)=(Z)`. This ideal-valuation argument also avoids the printed unexplained simplification of a longer gcd ideal to `(a,Z^q/a)`.

For `e=0`, expansion gives

`a/(X+Y) = 1 - [X/(X+Y)] lambda + O(lambda^2)`.

Here the rational exponent of `zeta_p` must mean its residue modulo `p`, since `p` does not divide `X+Y`; it is not an arbitrary rational power in a larger field. The normalized element satisfying the stated congruence is

`a' = zeta_p^(-X/(X+Y)) a`,

with a **minus** sign. Equation (9) on p.4 prints a plus sign; its own final congruence has `a` congruent to `(X+Y) zeta_p^(+X/(X+Y))`. Equation (8) for `a/bar(a)` is otherwise correct. When `t` kills the root of unity, this sign error disappears from `a'^t=a^t`, but it needs correction before using the unrestricted beta formula.

### B. Stickelberger elements, weights and generators (PDF pp.5-6)

The spectral idempotents (5) and `vartheta=(1/p) sum c sigma_c^(-1)` are standard in `Z_p[G]` and `Q[G]`, respectively. Formula (11) expresses the only potentially nonintegral `p`-adic component and is consistent with reduction modulo `p`. No later central inference needs (11).

The Stickelberger annihilation theorem cited to Washington, section 15.1, applies to the ideal class group of this cyclotomic field. It makes `A^theta` principal for integral Stickelberger `theta`. It does not by itself say that an arbitrary generator has rational product with its complex conjugate. That additional property comes from the Gauss/Jacobi construction, not merely from principality.

The coefficient formula in (12) does give positive integral Fueter elements satisfying `psi_n+j psi_n=N`, where `N=sum sigma` is the norm element. However, the associated lattice assertions are not literally valid:

- A positive nonzero `psi_n` cannot belong to `(1-j)I`, because its plus part is `N`, whereas an element of `(1-j)I` has plus part zero. Thus these `psi_n` are not a basis of the anti-invariant module named on p.5.
- Equation (14) cannot represent **every** element of `I` by the listed `(p-1)/2` elements. Each of those `psi_n` has zero coefficient at `sigma_1` by the displayed floor formula. Every linear combination has that coefficient zero. But `N=vartheta(1+j)` belongs to `I` and has coefficient 1 there. A corrected description must include the norm direction (and accurately specify the lattice).
- Negative group-ring coefficients give fractional ideals and potentially nonintegral generators. Statements on p.5 that all `C^theta` and their generators are integral for arbitrary `theta in I` need this qualification. The positive elements selected later avoid that particular defect only if their two pieces are positive too.

For the later argument it is enough to define relative weight by the group-ring relation `theta+j theta=varsigma(theta) N`. This yields `beta(theta) bar(beta(theta))=Z^varsigma(theta)` for suitably normalized Jacobi generators. The formula remains compatible with positive `theta`. The fixed-weight positive set `J_k` in (16) is not a submodule: it does not contain zero and is not closed under addition. It can be used as a set, but calling it a module does not establish its asserted decompositions.

Fact 2's explicit cancellation `phi(psi_1+sigma_c psi_2)=0`, or `2 psi_j` when one value is zero, is valid. It constructs a positive relative-weight-2 element. It does **not** establish that the element has a nonzero anti-invariant component. Indeed at `p=5` the constructed element is `N`, and in fact `J_1={N}`; an exact hand derivation is given below under SF1-04. This matters because Lemma 6 chooses `t in J_1`, and Lemma 5 later requires a power of `a^t` to be nonrational.

### C. Jacobi normalization and beta map (PDF p.6 to p.7, (17)-(22))

The intended classical construction is as follows. A prime dividing `Z` splits completely in `F`: at a prime above it dividing `Y+zeta_p X`, the residue of `zeta_p` equals the rational residue `-Y/X`, and has order `p`; `p` does not divide `Z`. Thus such rational primes are `1 mod p`. One can use order-`p` characters over those prime residue fields to form Jacobi sums, multiply them according to the Stickelberger exponent and the prime factorization of `A`, and normalize their sign to obtain generators with rational complex norm and congruence `1 mod lambda^2`.

For the usual nontrivial pair of order-`p` characters, the negative Jacobi sum has that congruence: expanding the characters modulo `lambda^2`, the constant term is the negative of the number of nonzero summands, congruent to 1 modulo `p`, and the two first-moment sums of discrete logarithms vanish modulo `p`. This is compatible with the standard Jacobi congruence cited as (17). The footnote on p.6 discusses a Gauss sum and only a prime-ideal congruence; that footnote alone does not supply the full Jacobi-generator theorem or its precise scope for every element of the ideal.

The uniqueness argument does correctly use Kronecker **when** two generators have the same rational complex norm: their quotient is a unit all of whose complex conjugates have absolute value 1. A root of unity is then the only ambiguity, and congruence `1 mod lambda^2` removes it for `p>3`. This gives multiplication and Galois equivariance of a consistently normalized generator map. These classical ingredients are reasonable conditional input here; I did not obtain the complete cited Washington and Iwasawa originals, so this is not a bibliographic verification of their exact formulations.

The printed intermediate formula (18) is not compatible with the preceding ideals. It has

`a^((1-j)theta) = eta' beta^p`

after saying `(a^theta)=A^(p theta)=b(theta)^p`. The characteristic exponent is `q`, not `p`. Even changing `p` to `q` does not fix the missing `(1-j)` on the beta side: the left ideal is `A^(q(1-j)theta)` while `beta^q` generates `A^(q theta)`. A compatible ratio formula would involve `(beta/bar(beta))^q`. This is more than an unambiguous one-letter substitution in (18).

For positive `t` of relative weight `2k` with `phi(t)=0`, the needed equation (20) can nevertheless be reconstructed for `e=0` from the normalized generators: `(beta(t)^q)=(a^t)` and both have equal rational complex norm, so the quotient is a root of unity. Since the augmentation of `t` is `k(p-1)`, the corrected normalization of `a` gives `a^t=1 mod lambda^2`; the same is true for `beta(t)^q`. The root of unity is therefore 1. For `e=1`, the initial characteristic number satisfies `a=-X+(X+Y)/lambda=-X mod lambda^2` because `p>3`; raising the rational leading term to augmentation `k(p-1)` again gives 1 modulo `lambda^2`. The same uniqueness argument establishes `beta(t)^q=a^t` there as well, conditional on the normalized Jacobi-generator input. This reconstructs the restricted identity in both cases without relying on (18). The assertion `beta(theta)^q=a'^theta` for arbitrary `theta` in Lemma 2 also needs a sign when the relative weight is odd. Its injectivity can instead be proved from ideals: `A` and its conjugates are proper, pairwise coprime, and `A^theta=(1)` forces all coefficients of `theta` to vanish. Properness fails in the omitted `Z=1` boundary cases.

For `t in J_k`, (21) gives

`lambda^t=s(t) p^k`, with `s(t)=+1 or -1`.

This follows because `lambda^t` is real, its complex norm is `p^(2k)`, and `phi(t)=0`; it does **not** force its sign positive. With the unnormalized `alpha=Y+zeta_p X` introduced in Definition 3, the intended relation becomes

`beta(t)^q = s(t)^e alpha^t / p^(e k)`.

Consequently acting by `sigma-1` yields

`beta(t)^(q(sigma-1)) = alpha^(t(sigma-1))`,

not (22) as printed, which omits the exponent `q` on the beta side. For differences rather than ratios the actual consequence is

`beta(t)^q - sigma(beta(t))^q = s(t)^e p^(-e k) [alpha^t-sigma(alpha^t)]`.

That denominator cannot be discarded at primes over `p` in the `e=1` case.

### D. Rational congruences and difference ideals (PDF pp.7-8, Lemmas 3-4)

Lemma 3 for the unnormalized `Psi_t=alpha^t` is recoverable: modulo `X`, `Y`, and `X+Y` it takes the rational values `Y^(k(p-1))`, `X^(k(p-1))`, and `s(t) p^k Y^(k(p-1))`, respectively. These three rational ideals are pairwise coprime in the normalized domain, so their product divides every conjugate difference. This is a valid statement for integral positive `t`.

For Definition 4 one must distinguish rings. `delta_c=beta-xi_q^c sigma(beta)` lies in `O(L)` for `L=Q(zeta_p,zeta_q)`. Only `delta_0` is already in `O(F)`. Thus `D_c=(w',delta_c)` are naturally `O(L)` ideals, with `D_0` extended from `F`; taking contractions or extensions should be explicit in statements involving a prime of `F`. Here `w'=w/q^v_q(w)` removes `q` and not `p`.

The distinct `D_a,D_b` are coprime: subtracting the two deltas shows a common prime away from `q` would divide both `beta` and `sigma(beta)`, whereas a prime of `(w')` cannot divide them because `gcd(w,Z)=1` and each beta divides a power of `Z`. This works with `a=0` too, by the same subtraction, without a new exceptional case. If the product of the deltas is divisible by `(w')`, unique ideal factorization then yields `product D_c=(w')` including multiplicities. This product argument is fine **conditional on** that divisibility.

For `e=0`, it follows directly from Lemma 3. For `e=1`, the product of deltas is the last displayed expression in the previous subsection, with a denominator `p^k`. Lemma 3 alone proves the required divisibility away from `p`; it does not prove it at primes over `p`. The proof's equality `product delta_c=Psi_t-sigma(Psi_t)` on p.8 is not the right equality for `e=1`. The local certificate below shows that the claimed divisibility can lose one uniformizer power even with a permitted non-norm `t`; the current `e=1` argument cannot just cancel that denominator.

More basically, Definition 4 prints

`D = intersection_(sigma in G) D_0(sigma)`.

The subsequent argument treats `D` as the ideal imposing *all* congruences. In the conventional ideal divisibility order that common divisor is the **sum** of the ideals, not their intersection. In valuation language an intersection takes maxima, while simultaneous congruences from all `D_0` require minima. Also the printed index set includes `sigma=1` even though the initial definition excludes it; extending the definition naturally gives `D_0(1)=(w')` and makes the displayed intersection equal to `(w')`. The proof cannot use its stated interpretation with this literal definition. Even on the charitable replacement by a sum over nonidentity `sigma`, the following issues persist.

Lemma 4(3) first takes a prime `R|D` and reduces `Tr(beta)/(p-1)` modulo `R`. Modular division by `p-1` is not justified when the residue characteristic divides `p-1`, particularly at 2, the prime used in the conclusion. A trace average is not automatically an element of the local ring. At an unramified prime, a reconstruction could instead use the Frobenius in the decomposition group: equality of all conjugates of beta modulo `R` implies its residue belongs to the rational residue field. That repairs this particular residue-field step without division by `p-1`; it does not repair the later arguments.

The sign need not be the printed positive one. The paper itself permits `s(t)=-1`. For example, at `p=7`, `psi_2` has support `{3,5,6}` in the `sigma_c^(-1)` coordinates and `phi(psi_2)=0`. Thus `t=2 psi_2` is in `J_1`. The factors of `lambda^psi_2` have arguments adding to `pi/2`, and its absolute value is `sqrt(7)`; hence `lambda^t=-7`. For `e=0`, modulo `X+Y` the value of `Psi_t` is therefore `-7 Y^6`, while `Norm(alpha)` is `+7 Y^6`. Lemma 3 says each is rational modulo `X+Y`, not that they are the same rational residue. The sign argument on p.8 asserts that equality without establishing it.

More generally, away from `p q`, comparison of the correct `q`th-power congruences with `Z^(qk)` gives the sign `s(t)^e` for `w=X` or `Y`, and `s(t)^(e+1)` for `w=X+Y`, not a universal `+1`. A sign can coincide modulo small primes, especially 2. Consequently this is a defect in the full claimed congruence; it is not on its own a disproof of a possible argument restricted to 2.

The proof then works only modulo individual prime ideals, but concludes that the whole ideal, with full multiplicities, is G-invariant and equal to a rational principal ideal `(D)`. G-invariance of the radical is not a proof about higher valuations. At an unramified rational prime a genuinely invariant ideal does have a rational exponent, but an invariant ideal at a ramified prime need not be generated by a rational integer: `(lambda)` in `F` is a basic counterexample. The `e=1` case admits primes over `p` in `w'`, so this distinction is relevant. Additional prime-power and ramification work is missing before the integral equation in Lemma 5 is available as written.

### E. Lemma 5 and the integral obstruction (PDF p.8 bottom to p.9 top)

Temporarily grant a correctly defined rational ideal `(D)`, full congruence `beta(t)=Z^k mod D`, and a decomposition `t=t1+t2` with integral positive pieces of relative weight `k`. Put `b_i=beta(t_i)` and `b=b_1 b_2`. The classical generator norms give `b_i bar(b_i)=Z^k`. Then

`b-Z^k = D chi = b_1 (b_2-bar(b_1))`.

Since `D` is coprime to `Z` and each `b_i` divides a power of `Z`, cancellation gives `b_1|chi`. Interchanging the two pieces gives `b_2|chi`. These deductions are individually legitimate under the granted integrality hypotheses. The next line, claiming `chi=b_1 b_2 chi'` with `chi' in Z[zeta_p]`, is the unsupported step. Neither common divisibility nor the rational complex norms supplies product divisibility.

There is an exact ideal-valuation obstruction in the paper's own setup. Write

`t=sum n_c sigma_c^(-1)`, so `n_c+n_(p-c)=2k`.

At any prime `P` belonging to the proper ideal `sigma_c^(-1)(A)`, let its exponent there be `m>0`. Pairwise coprimality of the conjugate characteristic ideals and their product `(Z)` imply

`v_P(b)=m n_c`, `v_P(Z^k)=m k`, `v_P(D)=0`.

If `n_c>k`, unequal valuations force

`v_P(chi)=v_P(b-Z^k)=m k < m n_c=v_P(b)`.

Therefore `chi/b` is nonintegral at `P`. For any non-norm `t`, a coefficient differs from `k`, and the pair-sum identity provides a coefficient greater than `k`. Thus the precise claimed integrality fails at such a characteristic prime under the hypothetical-solution structure. This pinpoints the missing step without searching for a Diophantine solution or treating a generic arithmetic example as one.

Nor can one simply add the assumption that `b_1,b_2` are coprime while keeping a useful positive non-norm `t`. Write the coefficients of `t_i` as `a_c,b_c`, with `a_c+a_(p-c)=b_c+b_(p-c)=k`. Disjoint positive supports require `a_c b_c=0` for every `c`. Any `0<a_c<k` would make both `a_c,a_(p-c)` positive and force both corresponding `b` coefficients to zero, impossible. Hence every `a_c` is 0 or `k`, the other coefficients are complementary, and `t=kN`. This loses the later nonrationality.

A small generic algebra model makes the same distinction transparent: in `Z[i]`, let `b_1=b_2=2+i`, `Z=5`, `k=1`, `D=2`. Then `b=3+4i`, `b-Z=2(-1+2i)`, and `chi=-1+2i=i(2+i)` is divisible by both `b_i` but not their product. Both norms are 5 and `D` is coprime to the generators. The norm-one element `Z/b=(3-4i)/5` is not integral. This is **not** a counterexample to the Strong FC equation, nor an example in its cyclotomic field; it isolates the invalid algebraic rule and the integral hypothesis needed by Kronecker.

If `chi'` really were integral, then `mu=1-D chi'` would be integral and `mu bar(mu)=1`; all its complex embeddings would have absolute value 1 because this is a CM Galois field. Kronecker would correctly show `mu` is a root of unity. The obstruction is before this valid application, not a defect in Kronecker's theorem.

The next line on p.9 claims `beta(t)^(2pq)=alpha^(2tp)` is nonrational by Lemma 1. Even after restoring the rational `p` denominator for `e=1`, Lemma 1 only gives that nonrationality if `t` is not a multiple of `N` (and `A` is proper). The allowed set contains `kN`: `phi(N)=0`, `N` is positive and has relative weight 2. For such `t`, `beta(t)=Z^k` and the relevant power is rational. Its universal congruence ideal contains all of `(w')`, rather than supporting a contradiction. The source explicitly invokes `kN in J_k` in Lemma 4, so this is not a hypothetical element excluded elsewhere.

The final sentence claiming that `D=1` avoids the same contradiction because its congruence is void does not cure the algebra: the integral identity `b-Z^k=D chi` also exists when `D=1`. The failed product-divisibility step does not become true when `D!=1` or false when `D=1`.

### F. Lemma 6, Proposition 1 and parity (PDF p.9)

Suppose, despite the above gaps, one knew that a prime of `F` dividing a nonzero-index `D_a` splits completely in `L/F`. This relative splitting conclusion is understandable: in its residue field, the nonzero ratio `beta/sigma(beta)` equals `xi_q^a` with `a!=0`, so it contains a primitive `q`th root; excluding `q` ensures that root retains order `q`. Ring extensions and the relevant prime should still be specified.

The next conclusion is not supplied by relative splitting. With `Gal(L/Q)=G' x H'` and decomposition group `E`, relative splitting says `E intersection H'={1}`. The containment `L^E superset Q(zeta_q)` used on p.9 would instead require `E subset G'`. A subgroup of a direct product can have trivial intersection with one factor but project nontrivially to it.

Exact countermodel to this group/field inference: take `p=5,q=3,r=2`. The orders of 2 modulo 5 and 3 are 4 and 2. A prime over 2 of `F=Q(zeta_5)` has residue field `F_16`, containing the primitive cube roots; it splits completely in `L=Q(zeta_15)` over `F`, since the relative residue degree is `lcm(4,2)/4=1`. Nevertheless 2 is inert in `Q(zeta_3)` and `2 != 1 mod 3`. Its decomposition group in `G' x H'` is generated by `(sigma_2,tau_2)`, has order 4, intersects `H'` trivially, and is not contained in `G'`. All primes here are unramified. This disproves the asserted inference on its own stated number-field premises, without presuming a solution of the original equation.

The valid numerical consequence of relative splitting at `r != p q` is only

`ord_q(r) divides ord_p(r)`.

The paper needs the stronger `ord_q(r)=1`. Some extra hypothesis, such as already knowing complete splitting of `r` in `F`, could imply it, but none is proved for primes dividing `X,Y,X+Y`. Such an extra hypothesis would in particular exclude the parity prime 2 for every `p>3`. A new argument using the specialized Jacobi data would be needed; the stated decomposition-group sentence is not that argument.

If the much stronger Proposition 1 were valid, the concluding parity contradiction would be valid: a factor among `X,Y,X+Y` is even; removing powers of the odd prime `q` does not remove that factor 2; and 2 is neither `q` nor `1 mod q`. No further issue in this final elementary implication repairs the preceding barriers.

## Consolidated issue ledger (single-reviewer, not promoted)

| ID | Locator | Kind | Candidate finding and needed resolution |
|---|---|---|---|
| SF1-01 | p.8, Lemma 5, line introducing `chi'` | Substantive integral-divisibility gap | Individual divisibilities do not imply product divisibility. The non-norm coefficient valuation above prevents integrality of `chi/beta(t)` at a characteristic prime. A different argument is needed. |
| SF1-02 | p.9, Lemma 6, decomposition-group sentence | Substantive group/field inference gap | `E intersection H'=1` does not imply `E subset G'`; `(5,3,2)` is an exact countermodel to the inference, not the Diophantine theorem. Need additional specialized information implying absolute splitting. |
| SF1-03 | p.7, Definition 4; p.8, Lemma 4(3) | Definition and ideal-multiplicity gap | Intersection is used as a gcd; identity automorphism has inconsistent scope; prime-level invariance is promoted to a rational integer ideal without multiplicities or ramification. Must define rings and common ideal, then establish prime-power congruences. |
| SF1-04 | p.5 (12)-(16), p.6 Fact 2, p.9 Lemma 5 and Lemma 6 | Norm direction and small-prime boundary | Fueters are not the stated anti-invariant basis, (14) misses `N`, `J_k` contains `kN`, and `J_1={N}` for `p=5`. The nonrationality assertion and small-weight selection need a non-norm construction plus a valid argument for it. |
| SF1-05 | p.7 (22), p.8 product of deltas | Exponent and `e=1` denominator gap | Correct difference is `s^e p^(-ek)(Psi-sigma Psi)`. The `p=11` local certificate below loses one uniformizer power in the claimed product identity. Reinsert `q` in (22), then replace the incorrect local statement. |
| SF1-06 | p.8, proof of Lemma 4(3), sign paragraph | Sign and local-ring qualification | Rationality modulo `w` does not equate the two rational residues. At `p=7,t=2psi_2`, `lambda^t=-7`. Trace division by `p-1` is also unjustified at residue characteristic 2. Some sign/residue steps can be repaired, but not as written. |
| SF1-07 | p.4 (9), p.6 (18)-(20) | Normalization / inconsistent intermediate formula | (9) needs the opposite sign; (18) has both wrong characteristic exponent and unmatched relative part. The restricted `e=0` relation (20) can be derived anew from normalized generators; `e=1` and arbitrary-weight claims require a precise normalization theorem. |
| SF1-08 | p.1 (2), p.2 Theorem 1, p.3 Assumption 1 | Literal statement-domain counterexamples | `q` odd and nontriviality must be explicit. `X=Y=Z=1,e=0` contradicts literal unrestricted wording. The known `q=2` example is outside the intended claim. No nontrivial odd-`q` counterexample found or asserted. |

### Exact `p=5` hand certificate for SF1-04

Use the coefficient order `sigma_1^(-1),...,sigma_4^(-1)`. The formulas give

`psi_1=(0,0,1,1)`, `psi_2=(0,1,0,1)`, `N=(1,1,1,1)`.

Their Fermat values are 1 and 2 modulo 5, respectively; Fact 2 chooses `c=2` and `psi_1+sigma_2 psi_2=N`. To see all of `J_1`, write an integral Stickelberger element in the corrected rank-3 description `t=aN+b psi_1+c psi_2`. Relative weight 2 gives `2a+b+c=2`. Positivity gives `a>=0`, `a+c>=0`, `a+b>=0`, `a+b+c>=0`, and pair sums 2 give `a<=2`. The Fermat condition is `b+2c=0 mod5`.

- `a=0`: `b+c=2`, `b,c>=0`, and `b+2c=2+c` is 2, 3 or 4 modulo 5.
- `a=1`: `b+c=0`, `-1<=c<=1`, and `b+2c=c`, so only `b=c=0` works.
- `a=2`: `b+c=-2`, `-2<=b,c<=0`, and `b+2c=-2+c` is -4, -3 or -2 modulo 5.

Thus `t=N`. The corrected integral description follows directly without an index assumption: every `theta=vartheta u` with `u in Z[G]` satisfies `theta+j theta=augmentation(u) N`, so its integer coefficients satisfy `n_1+n_4=n_2+n_3`. Conversely every integral vector satisfying that relation is `n_1 N+(n_3-n_1) psi_1+(n_2-n_1) psi_2`, and all three displayed generators belong to `I`. This proves the exact lattice used in the certificate.

### Exact local `p=11` certificate for SF1-05

This is a calculation of an inference under a hypothetical `e=1` solution, not a constructed solution. At `p=11`, let `t=psi_1+psi_2`. The supports in the paper's inverse-automorphism coordinates are `{6,7,8,9,10}` and `{4,5,8,9,10}`. Their Fermat values are `32=10 mod11` and `34=1 mod11`. Hence `t in J_1`. On the other hand

`M=sum n_c c=40+36=76=10 mod11`.

Put `s=X+Y` and `h=v_lambda(s)=10 v_11(s)>=10`. For the **initial**, normalized characteristic number, its conjugate indexed by `c` is `-X+s/(1-zeta^(1/c))`. Thus

`a^t=(-X)^10 [1-(s/X) B + terms of valuation at least 2(h-1)]`,

where `B=sum n_c/(1-zeta^(1/c))`. Since `1-zeta^(1/c)=(1/c)lambda+O(lambda^2)`, the leading coefficient of `B` is `M/lambda`, so `v_lambda(B)=-1`. For any nonidentity `sigma_d`, the leading coefficient of `B-sigma_d(B)` is `(1-1/d)M/lambda`, still nonzero modulo 11. It follows that

`v_lambda(a^t-sigma_d(a^t))=h-1`.

The reconstructed identity `beta(t)^q=a^t` makes this the valuation of `product_c delta_c`. In the extension by `zeta_q`, which is unramified at 11, the other deltas are units at a prime over `lambda`: `beta` and all its conjugates are `1 mod lambda^2`, whereas `1-xi_q^c` is a unit there when `c!=0` and `q!=11`. Therefore the product of the capped ideals `(w',delta_c)` has valuation `h-1`, while `(w')` for `w=X+Y` has valuation `h`. The claimed equality in Lemma 4(2) is not a consequence of the correct formulas; its local version would require a substantive replacement. This certificate is algebraic and uses no numerical Diophantine search.

## Exact relevance to 2025 B4(b), conditional on a valid replacement proof

The official target is `S_n(x)=1+x+...+x^n=y^Q` for integer `x,y`, `n,Q>=2`; put `m=n+1`. For **prime term count** `m=p>3`, and an odd prime divisor `q` of `Q` with `q!=p`, set `Z=|y|^(Q/q)`. For `|x|>1`, `S_(p-1)(x)>0` and the equation would map to the intended nontrivial source domain as follows:

- `x>1`: `(X,Y)=(x,-1)`;
- `x<-1`: `(X,Y)=(-x,1)`, obtained by simultaneous sign change from `(x,-1)`.

Then `(X^p+Y^p)/(X+Y)=S_(p-1)(x)=Z^q`, so `e=0`; the `p`-adic valuation argument also precludes `p|x-1` for such a perfect power. Coprimality is automatic from `Y=+1 or -1`, and `X>|Y|=1` holds. A validated theorem would therefore exclude this **signed prime-term, off-diagonal, odd-prime-factor sector**. The present source audit does not make that exclusion available as a proved result.

The mapping does not cover `p=3`, exponent prime `q=2`, diagonal `q=p`, or cases where every prime divisor of `Q` lies in `{2,p}`. It does not by itself classify composite term counts `m`; passing from their cyclotomic factors to the theorem would require additional coprimality and valuation reductions. The official boundary values `x=-1,0,1`, and the associated `y=0,+1,-1` possibilities when applicable, must be retained separately. The source proof's nontrivial assumption cannot delete them from the official statement. Negative `y` is also retained whenever `Q` is even; using `|y|` in the reduction preserves rather than classifies those signs.

No published/theorem status is inferred from the title, author, abstract, preprint posting, or the fact that this mapping would be strong. Conversely, the size of its implied classification is not itself a mathematical objection.

## External theorem hypotheses and verification limits

| Input | What is needed here | Audit treatment |
|---|---|---|
| Cyclotomic ramification and roots of unity | `p` odd, `F=Q(zeta_p)`, `(p)=(lambda)^(p-1)` up to ideals; roots of unity `+-zeta_p^a` | Standard facts, applied with correct field and `p>3`. Distinguish invariant ideals from rational ideals at the ramified prime. |
| Stickelberger annihilation, source [Wa] 15.1 | Integral Stickelberger action on the class group; fractional versus positive integral ideals | Compatible with this field. Does not alone provide rational-norm generators or the false basis claim. Complete cited original not retrieved in this audit. |
| Fueter generators, source [Fu] and [Mi2] | The explicit positive coefficient identities and correct integral lattice | Explicit floor identities independently checked; printed lattice assertions fail their own coefficient test. Full original not independently retrieved. |
| Jacobi/Gauss generator construction, [Wa], [Iw] | Proper characteristic ideals away from `p`, normalized Weil generators, sign convention, multiplication and Galois compatibility | Character-sum normalization and ideal logic reconstructed conditionally, including the restricted even-weight relation in both cases. The footnote's Gauss congruence is insufficient as a full theorem statement. Complete originals not retrieved. |
| Kronecker unit theorem | Algebraic integer with every complex conjugate of absolute value 1 | Correct if `chi'` is integral. The main proof does not establish that hypothesis. Norm-one rational/fractional elements are insufficient. |
| Decomposition groups in a compositum | Correct restriction maps and containment/intersection distinction | Independently audited; the implication used in Lemma 6 has the explicit unramified countermodel above. |
| Ribenboim/Barlow-Abel, source [Ri] | Pairwise coprimality and rational valuations for Equation (1) | Reconstructed by valuation splitting; contextual, not used to repair the core proof. |
| [BMS], [GQ], [W], [WT], [Mo], [MFHMP] | Background, terminology, bibliography | No substantive theorem from these is invoked in the displayed contradiction; no inference borrowed from them. |

## Reproduction and operations record

Read-only commands used the bundled Python 3 runtime at `/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`, its `pypdf` package, system `shasum`, and bundled Poppler `pdftoppm`. The essential extraction command was `PdfReader(source).pages[i].extract_text(extraction_mode="layout")`, run in page batches 1-4, 5-7 and 8-10; the output was checked against all page renderings. The source SHA-256 was rechecked with `shasum -a 256`.

Rendering command: `pdftoppm -r 110 -f 1 -l 10 -png .cache/literature/deep-literature-r1/2025-mihailescu-strong-fermat-catalan-v1.pdf /private/tmp/strongfc-review-1-page`. It completed with exit 0, but emitted extensive fontconfig cache warnings; the resulting ten PNGs were legible and inspected. A process listing was requested only to identify this renderer during the warning-heavy run; no process was killed and no other owner's job was touched. The render session was `77930` and was reaped with `write_stdin` after completion. No native CAS or Diophantine search was launched. The exact small examples and valuations above are mathematical certificates, not numerical evidence for an unrestricted assertion.

No source paper is copied into a tracked file. No credentials, messages to external people, charges, separately billed APIs, Git commits or pushes were used by this reviewer. Only the assigned `strongfc-review-1*` review files were authored. The source PDF remains in ignored `.cache/`.

Blind analysis complete; freeze time and file hashes are in the companion `strongfc-review-1-blind-manifest-v1.json`. Any subsequent audit of the older proposed concerns must not overwrite this blind report.
