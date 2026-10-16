# Independent whole-source audit 2: Strong Fermat-Catalan v1

Status: **candidate proof - unverified**. This is a blind adversarial source audit, not a promotion of a mathematical result. The specific objections below also await the coordinator's required independent review. Statements attributed to the preprint are separated from this reviewer's reconstructed repairs, valuation analysis, and counterexamples; the latter are review contributions rather than attributed published results.

Reviewer: `review_2025_strongfc_r2`. Assigned scope: 2025 B4(b), with edits confined to this review prefix. Requested settings: `gpt-6.1-sol`, `max`; verified effective-setting readback: unavailable. No model identity is inferred from the request. No subagents were spawned.

Source: Preda Mihailescu, [The strong Fermat-Catalan Equation, arXiv:2509.18275v1](https://arxiv.org/abs/2509.18275v1), submitted 2025-09-22; the PDF itself dates Version 1.0 to 2025-09-24. Ten PDF pages, printed pages 1-10. Local ignored original: `.cache/literature/deep-literature-r1/2025-mihailescu-strong-fermat-catalan-v1.pdf`; 424143 bytes; SHA-256 `daba36d8971a346d4cd40d0b823f787034c4a11b67e76258beeb7574e6fe2669`.

## Blindness and conclusion

Before this report and its blind-freeze manifest were saved, I read neither another strongFC review nor `notes/deep-literature-r1-report-v1.md`. I used the source manifest only to locate and hash the original PDF. I read all ten pages by extraction and visually inspected printed pages 2-9 to resolve notation. A later comparison, if any, belongs in a separate addendum and must not change this frozen report.

The preprint is not a usable proof of its nontrivial theorem on the evidence audited here. Even after granting the standard cyclotomic setup and repairing obvious notation errors, the argument has two independent central obstructions:

1. Lemma 5, printed pp. 8-9, infers divisibility by a product from divisibility by its factors. The factors are not proved coprime. The characteristic-ideal valuations show exactly why this step cannot be supplied in the asserted form for nonconstant `t`; see the reconstruction below.
2. Lemma 6, printed p. 9, replaces trivial intersection of a decomposition group with one direct factor by trivial projection onto that factor. The implication is false. Explicit cyclotomic examples, including one compatible with the local Weil-number norm condition at 2, demonstrate the distinction.

There is an additional problem in Definition 4/Lemma 4: an ideal intersection is used as though its prime divisors were common to every intersectand. Changing intersection to ideal sum would repair that particular definition but would not repair either central obstruction.

I found a counterexample to the *literal boundary-inclusive wording* of Theorem 1: `(x,y,z,e)=(1,1,1,0)` for any permitted primes. I found no counterexample to the intended normalized nontrivial theorem `x>|y|>=1`. The generic algebraic and field-theoretic counterexamples below are expressly not solutions of the Diophantine equation.

## Domain and normalization

Printed p. 1, equation (2), is

\[
F_p(x,y):=\frac{x^p+y^p}{x+y}=p^e z^q,
\qquad (x,y,z)\in(\mathbb Z^*)^3,\quad \gcd(x,y,z)=1,
\]

with distinct odd primes `p,q`, `p>3`, and `e in {0,1}`. The rational quotient requires `x+y != 0`; its homogeneous polynomial continuation at `x+y=0` must not be silently substituted. Theorem 1, p. 2, omits a nontriviality qualification. Section 3, p. 7, invokes a nontrivial solution. Assumption 1, p. 3, imposes `x>|y|>=1`.

For unequal absolute values, symmetry and simultaneous sign change put a primitive solution in that normalization: `F_p(-x,-y)=F_p(x,y)` because `p-1` is even. The missing equal-absolute-value cases must be excluded explicitly. In particular `x=y=1` satisfies the displayed equation with `e=0,z=1`; its gcd is 1 and its denominator is 2. This is only a boundary counterexample to the literal theorem, not an objection to the normalized target.

In the normalized domain the quotient is positive, so `z>0` because `q` is odd. Primitivity gives `gcd(x,y)=1`: a prime dividing both must also divide `z`, since its valuation on the left is at least `p-1>e`. Standard reduction modulo `x` and `y`, and the valuation at `p`, then give `gcd(z,xy(x+y))=1`. In particular `p` does not divide `z`. For coprime integers,

\[
v_p(F_p(x,y))=\begin{cases}1&p\mid x+y,\\0&p\nmid x+y,\end{cases}
\]

so `e` has its intended value. The elementary proof uses the binomial expansion when `p|x+y` and `F_p(x,y)=(x+y)^{p-1}` modulo `p` otherwise. Remark 2, p. 2, writes a gcd of 1 before removing the factor `p` in the `e=1` case; that line needs this correction, although its desired conclusion about `z` is valid.

The normalization also gives `z>1`. For `y>0`, `F_p(x,y)>x^(p-1)/2`; for `y<0`, `F_p(x,y)>=x^(p-1)`. Here `x>=2,p>=5`, and even after division by `p` the result exceeds 1. This nonunit condition is needed in the beta-map injectivity argument.

## Reconstruction of the preparatory algebra, pp. 2-7

To avoid the source's repeated `K,K'` notation, write `C=Q(zeta_p)`, `C'=Q(xi_q)`, `L=C C'`, `G=Gal(C/Q)`, `H=Gal(C'/Q)`, and `M=xy(x+y)`. The fields are linearly disjoint because their prime conductors are distinct, so `Gal(L/Q)=G' x H'`. Let `lambda=1-zeta_p`, whose unique prime above `p` has `(lambda)^(p-1)=(p)`.

1. **Fact 1 and the Barlow-Abel reduction, p. 2.** Reduction modulo `x+y` gives `F_p(x,y)=p*x^(p-1)` modulo that ideal. Together with `gcd(x,x+y)=1`, this proves the ideal gcd divides `(p)`; abelianity is unnecessary for this identity. The printed last expansion has an extra division by `s`; the corrected expansion is `F_p(x,s-x)=p*x^(p-1)+O(s)`. Over integers, the valuation statement above and coprimality away from `p` give the two factorizations in (4). Thus the asserted necessary passage from equation (1) to (2) is sound, with the same normalization and triviality caveat.

2. **Notations, p. 3, (5).** The Teichmuller idempotents are the usual orthogonal idempotents of `F_p[G]` or `Z_p[G]`, indexed modulo `p-1`. This material has no substantive later use beyond (11). The expression of conjugation as a power of an unspecified group generator is a notation omission; `j=sigma_(p-1)` is unambiguous.

3. **Characteristic number and ideal, pp. 3-4, (6)-(7).** Keep the normalized number `a=(y+zeta*x)/lambda^e` distinct from the later raw number `a0=y+zeta*x`. Then `N_C/Q(a)=z^q`, `a` is integral and prime to `p`, and its distinct conjugate ideals are coprime. For `e=1`, `v_lambda(y+zeta*x)=1` because `p|x+y` and `p` does not divide `x`; dividing by `lambda` leaves a unit at the ramified prime. For the other primes, differences of conjugates give `(x*lambda,y*lambda)`. Several occurrences of `x` and `y` are interchanged in the displayed proof, but the two required linear combinations exist. It follows valuation by valuation that

   \[
   A=(a,z),\qquad A^q=(a),\qquad N(A)=z,\qquad A^N=(z),
   \]

   where `N=sum_(sigma in G) sigma`. The conjugates of `A` are pairwise coprime and nonunit. Every rational prime `ell|z` is in fact `1 mod p`: at a prime dividing `a`, the residue of `zeta` is the rational residue `-y/x`, a primitive `p`th root because `ell != p`. Thus the supporting primes have degree 1. This extra observation checks the degree-one hypotheses of the usual Jacobi-sum construction.

4. **Phase normalization, p. 4, (8)-(9).** The ratio in (8), including the factor `-bar(zeta)` for `e=1`, is correct. In (9) the exponent has the wrong sign. If `e=0` and `r=x/(x+y)` in `F_p`, then

   \[
   a=(x+y)(1-r\lambda)+O(\lambda^2),\qquad
   \zeta^{-r}a=(x+y)+O(\lambda^2).
   \]

   Multiplication by `zeta^(+r)`, as printed in the definition of `a'`, gives first-order coefficient `-2r`, which need not vanish. The expansion at the bottom of p. 4 itself has the consistent positive exponent on the *right*. A corrected phase is a local repair, not a repair of Section 3.

5. **Stickelberger element and positive elements, p. 5, (10)-(16).** The definition `I=theta Z[G] intersect Z[G]` and class-group annihilation are standard. The `p`-adic comparison (11) follows coefficientwise from the Teichmuller lift. The floor-coefficient formula for `psi_n` gives nonnegative coefficients with `n_c+n_(p-c)=1`, hence `psi_n+j psi_n=N`. Therefore these positive `psi_n` cannot themselves belong to the module `(1-j)I` identified as `I^-` in the preceding sentence: every member of that module has zero sum with its conjugate. Nor can (14) span all of `I` using only the listed `(p-1)/2` positive elements. For example, when `p=5`, their coefficient vectors in the source's `sigma_c^-1` basis are `(0,0,1,1)` and `(0,1,0,1)`, so they cannot span `N=(1,1,1,1)`, which lies in `I` because `(1+j)theta=N`. A norm direction and a correct minus-module statement are required. The later argument can still work with the individually defined positive elements, without the false spanning assertion.

6. **Weight, Fermat map, and Fact 2, pp. 5-6.** For `theta in I`, the relative-weight identity is `theta+j theta=rho(theta)N`. For positive elements the augmentation is `rho(theta)(p-1)/2`. The map `phi(sum n_c sigma_c^-1)=sum n_c/c mod p` has `phi(sigma_d theta)=d phi(theta)`. The construction in Fact 2 does produce a positive element of relative weight 2 in `ker phi`; multiplication gives higher even weights. This does not prove it is nonconstant. The fixed-weight positive set `J_k` is not an additive submodule. The notation `I(k)` in Lemma 5 is not defined; a positive relative-weight-`k` set is presumably intended. Statements about integral beta values require positivity of the chosen pieces.

7. **Jacobi-number generators and beta, p. 6, (17)-(19).** With suitable normalized Jacobi generators one expects `(beta(theta))=A^theta` and `beta(theta) bar(beta(theta))=z^rho(theta)`. The displayed norm of `b(theta)` omits the weight. Equation (18) uses `p` where `q` belongs in the ideal-power identity and has further mismatch between its conjugation and beta exponent. It cannot be used verbatim for `p != q`. These are not merely extraction errors; the render shows them. A repair for *even positive weight and phi=0*, which is all the decisive section needs, is given next. The homomorphism and G-equivariance then follow from uniqueness of normalized generators. Injectivity uses pairwise coprime **nonunit** conjugates of `A`; the nonunit fact was not supplied in the source but follows from the normalized domain.

8. **Restricted repaired power identity, p. 7, (20)-(22).** Grant the standard normalized Jacobi generator for each positive `t in J_k`. Its complex-conjugate product is `z^(2k)`. The ideals of `a^t` and `beta(t)^q` agree. Their quotient is a unit whose product with every complex conjugate is 1, because `a^(t+j t)=N(a)^(2k)=z^(2kq)`. Kronecker's theorem therefore makes it a root of unity. It equals 1 by reduction modulo `lambda^2`: for `e=0`, each conjugate of `a` is `(x+y)` times its first-order phase, the total phase is killed by `phi(t)=0`, and the total rational power is `(x+y)^(k(p-1))=1 mod lambda^2`. For `e=1`, each conjugate of normalized `a` is `-x mod lambda^2` because `v_lambda(x+y)>=p-1` and `p>=5`; again the augmentation is `k(p-1)`. A root in `mu_(2p)` congruent to 1 modulo `lambda^2` is 1. Consequently

   \[
   \beta(t)^q=a^t=\frac{a_0^t}{(\lambda^t)^e},\qquad
   \lambda^t=s(t)p^k,\quad s(t)\in\{1,-1\}.
   \]

   The last identity follows because `(lambda^t)^2=p^(2k)` and its conjugate ratio is `(-zeta)^t=1`. For `e=0` only the first identity is needed. For `e=1`, the correct consequence of (22) is

   \[
   (\beta(t)^{\sigma-1})^q=a_0^{t(\sigma-1)},
   \]

   not the displayed identity without `q`. Cancellation of a rational denominator does not cancel the exponent `q`.

9. **Lemma 3, p. 7.** For raw `Psi_t=a0^t`, its residues modulo `x`, `y`, and `x+y` are respectively `y^(k(p-1))`, `x^(k(p-1))`, and `s(t)p^k y^(k(p-1))`. They are rational. Since these three integers are pairwise coprime, `M` divides `Psi_t-sigma(Psi_t)`. This is valid. It gives rationality of residues, not equality of the residues for different choices of `t` of the same weight.

## Definition 4 and Lemma 4, pp. 7-8

The intended factorization is `beta^q-(sigma beta)^q=product_(c=0)^(q-1)(beta-xi^c sigma beta)`. For a fixed `w in {x,y,x+y}`, let `w'=w/q^v_q(w)` and `D_c(sigma)=(w',beta-xi^c sigma beta)` in `O_L`. For `c=0` the ideal descends from `O_C`; for `c!=0` descent must not be assumed.

At primes above `w'`, beta and its conjugates are units because `gcd(z,w)=1`. Distinct `q`th roots remain distinct because those primes are not above `q`. Therefore the `D_c` for fixed `sigma` are pairwise coprime. Whenever `w'` divides `beta^q-(sigma beta)^q`, their product is `(w')` by valuations. This is immediate for `e=0` from Lemma 3. For `e=1` it is immediate away from `p`; at `p` the extra division by `p^k` must be controlled separately. The printed use of raw `Psi_t` alone does not provide that valuation control. This latter point is a request for missing justification, not a proved counterexample to the product formula. It has no bearing on the final prime `2`, which is different from `p`.

The displayed definition of bold `D` is an **intersection** of `D_0(sigma)`. In a Dedekind domain,

\[
v_R\left(\bigcap_\sigma D_0(\sigma)\right)
=\max_\sigma v_R(D_0(\sigma)),
\]

so a prime divisor of the intersection need divide only one intersectand. Lemma 4(3)'s first inference requires divisibility of every intersectand; that would use the **ideal sum**, with minimum valuations. If the identity automorphism is included as printed in the intersection, `D_0(1)=(w')` is contained in every other `D_0`, so the intersection is simply `(w')` for all `t`. Omitting the identity does not repair the max/min problem. This is a precise definition/inference defect, not a counterexample to the main Diophantine theorem.

Even after replacing the intersection by a sum, further care is needed:

- `Tr(beta)/(p-1)` cannot be reduced modulo a prime above a divisor of `p-1` without a denominator argument; that includes `r=2`, the only prime used in the final contradiction. At `r=2`, this can instead be repaired directly: equality of all conjugate residues includes `beta=bar(beta)`, and `beta bar(beta)=z^(2k)` then forces `beta=z^k` in the residue field because squaring is injective in characteristic 2.
- A G-invariant ideal need not be generated by a rational integer at the ramified prime. The prime `(lambda)` itself is a counterexample to that general assertion. Away from `p`, G-invariance does imply a rational ideal, because the extension is unramified and transitive on primes. The assertion in the paper needs a separate ramified valuation argument. For the final prime 2, that issue is absent.
- The attempt on p. 8 to identify the positive sign from `a0^t=z^(qk) mod M` does not follow from Lemma 3. For `e=0` and `w=x+y` the two residues differ by `s(t)`. This sign can actually be negative: for `p=7`, `psi_2` has support `c=3,5,6` in the inverse basis and `phi(psi_2)=5+3+6=0 mod 7`. Then `t=2psi_2 in J_1`, while `lambda^t=-7`: `lambda^psi_2` has conjugate ratio -1 and norm 7, so its square is -7. By contrast `lambda^N=7`. This is a counterexample to equality of the asserted generic residues, not a solution of (2). In characteristic 2 the sign distinction vanishes, so this is also locally repairable for the parity argument.

Thus the strongest charitable continuation is to replace the intersection by the ideal sum and focus just on the unramified factor at 2, with the repaired phase/norm identities. The remaining two obstructions persist under those concessions.

## Lemma 5, pp. 8-9: divisibility and rational exponents

Suppose `t=t1+t2 in J_k`, each piece positive of relative weight `k`, and use the repaired beta identities. Put `b_i=beta(t_i)` and `b=b1*b2=beta(t)`. Then

\[
b_i\bar b_i=z^k,\qquad b-z^k=D\chi,
\qquad (D,z)=1.
\]

The source's displayed factorization has a swapped subscript, but a valid version is

\[
b-z^k=b_1(b_2-\bar b_1)=b_2(b_1-\bar b_2).
\]

Consequently `b1|chi` and `b2|chi`. This does **not** imply `b1*b2|chi` unless the ideals `(b1)` and `(b2)` are coprime, or a different argument supplies their overlapping valuations. Neither is given. The split can even have `t1=t2`.

A generic exact illustration retaining the two norm identities and a nontrivial `D` is in `Z[i]`: take `b1=b2=1+2i`, `z^k=5`, `D=2`, and `chi=-4+2i`. Then `b=(1+2i)^2=-3+4i`, `b-5=2chi`, and `b_i bar b_i=5`. Both `b_i` divide `chi` because `chi=2i(1+2i)`. Their product does not divide `chi` because its norm is 25 whereas `N(chi)=20`. This is only a counterexample to the algebraic inference; `Q(i)` is not the paper's prime cyclotomic field and these numbers are not an equation-(2) solution.

More strongly, the **actual characteristic-ideal structure** shows why the requested extra divisibility is unavailable for nonconstant `t`. Write

\[
t=\sum_{\sigma\in G}n_\sigma\sigma,
\quad n_\sigma\ge0,
\quad n_\sigma+n_{j\sigma}=2k,
\quad \sum n_\sigma=k(p-1).
\]

If `t` is not `kN`, some `n_sigma>k`. Choose a prime `P` dividing the nonunit ideal `sigma(A)`, and let `a=v_P(sigma(A))>0`. Pairwise coprimality of the conjugates of `A` gives

\[
v_P(b)=n_\sigma a>ka=v_P(z^k).
\]

Unequal valuations in a discrete valuation ring therefore give

\[
v_P(b-z^k)=ka.
\]

Because `D` is coprime to `z`, division by `D` does not alter this valuation. Hence `v_P(chi)=ka<v_P(b)`, so `b` does **not** divide `chi`. This argument uses the intended setup rather than merely arbitrary integers. It does not assert existence of a normalized solution or refute Lemma 5's conclusion; it identifies exactly the unsupported step in the proposed contradiction.

Adding coprimality as a repair is incompatible with the intended nonrational case. If `(b1)` and `(b2)` were coprime, positivity and `t_i+j t_i=kN` force, in each conjugate pair of coefficients, one piece to have coefficients `(k,0)` and the other `(0,k)`. Thus `t=kN`. The final contradiction then disappears.

Indeed `kN` is always in `J_k`: `N in I`, `phi(N)=0`, it is positive and its relative weight is 2. For this element,

\[
\beta(kN)=z^k,\qquad a_0^{kN}=N_{C/\mathbb Q}(a_0)^k\in\mathbb Z.
\]

Consequently the claim at the top of p. 9 that `a0^(2pt)` is nonrational by Lemma 1 is false for allowed constant `t`. Pairwise coprimality implies nonrationality only when the exponent vector is nonconstant and the conjugate ideals are nonunit. The proof requires that qualification but cannot then make its product-divisibility step.

The issue is visible at the smallest permitted prime without any Diophantine search. When `p=5`, let the coefficients of `t in J_1` be `(a,b,2-b,2-a)`; positivity gives `0<=a,b<=2`. The Fermat condition is `2+2a+b=0 mod 5`. Its left side lies between 2 and 8, so `2a+b=3`, whose only allowed pair is `(1,1)`. Thus `J_1={N}`. Fact 2's specific construction also gives this element: `phi(psi_1)=1`, `phi(psi_2)=2`, so it selects `psi_1+sigma_2 psi_2=N`. Lemma 6's prescribed `t in J_1` consequently has no nonrational choice at `p=5`.

The Kronecker step itself would be valid **if** an integral `chi'` with `chi=b chi'` had been proved: `mu=1-Dchi'` would be integral and every conjugate would have modulus 1. But that integral `chi'` is precisely what the invalid divisibility step fails to produce. This is not an objection to Kronecker's theorem.

## Lemma 6 and final contradiction, p. 9

Grant for this section even the corrected version of `D=1` and the desired factorization at a rational prime `r|w'`. A prime `R` of `C` outside `D_0(sigma)` then gives a nontrivial `q`th root

\[
b=\beta/\sigma(\beta)\pmod R
\]

in the residue field of `C`. It follows that `R` splits completely in `L/C`. This first implication is sound: the residue field already contains `mu_q`, so adjoining `xi_q` does not extend it, and `r != q`.

Let `D_r` be a decomposition group in `Gal(L/Q)=G' x H'`. Complete splitting over `C` says `D_r intersect H'={1}`. Complete splitting of rational `r` in `C'/Q` would require `pr_H'(D_r)={1}`, equivalently `D_r subset G'`. The first condition does not imply the second. In field language, `C' subset L^(D_r)` requires `D_r subset Gal(L/C')=G'`, not just trivial intersection with `H'`.

A concrete counterexample uses `p=5,q=3,r=2`: Frobenius in `Q(zeta_5,xi_3)` is `(2 mod 5,2 mod 3)` and has order 4. Its generated subgroup intersects `{1} x (Z/3)^*` trivially because `ord_3(2)=2` divides `ord_5(2)=4`, but its projection onto that second factor has order 2. A prime of `Q(zeta_5)` above 2 splits in `L/C`; rational 2 is inert in `Q(xi_3)`.

The local Weil-number norm can exclude some individual patterns in that first example, so it should not be presented as satisfying all the paper's premises. There is also an example showing that the generic subgroup error is **not repaired by the local conjugate-product identity alone**: take `p=11,q=3,r=2`. Then

\[
\operatorname{ord}_{11}(2)=10,\qquad
\operatorname{ord}_3(2)=2,\qquad
D_r=\langle(2,2)\rangle.
\]

Again `D_r intersect H'={1}` but `pr_H'(D_r)=H'`. In the residue field `F_(2^10)`, choose `b` a primitive cube root. Complex conjugation on `C` equals Frobenius to the fifth power because `2^5=-1 mod 11`. Thus `bar b=b^(2^5)=b^(-1)`, so `b bar b=1`, exactly the nonzero norm condition at 2. Moreover `b^3=1`; this local residue pattern is compatible with both a cube-power identity and the conjugate-product identity. It is not claimed to arise from a global solution or even an actual global characteristic ideal. It rules out that proposed *local-only* repair.

What the argument actually gives, with `f=ord_p(r)`, is

\[
q\mid r^f-1,
\quad\text{or equivalently}\quad
\operatorname{ord}_q(r)\mid\operatorname{ord}_p(r),
\]

not `r=1 mod q`. An extra argument giving `f=1`, or directly killing the projection, would suffice; none is supplied for factors of `xy(x+y)`. The special signed Nagell-Ljunggren substitution `y=+/-1` does not itself give that missing splitting condition. For example a rational divisor of `x` can have arbitrary residue degree in `Q(zeta_p)`; reducing the raw characteristic number to a rational residue only puts a `q`th-power equation in that larger residue field.

Proposition 1 and the parity contradiction are correct **conditional on** their unproved assertion that every prime dividing `M` except `q` is `1 mod q`. One of `x,y,x+y` is even, removing `q`-powers preserves that because `q` is odd, and `2` is neither `q` nor `1 mod q`. The obstruction is establishing the prime-splitting assertion, not the final parity calculation. References and acknowledgements on p. 10 add no missing proof step.

## External theorem hypotheses and validation limits

| Ingredient | Exact hypotheses needed here | Audit result |
|---|---|---|
| Stickelberger annihilation | Cyclotomic `C`, integral element of `I`; fractional ideals allowed, and positivity for an integral generator | Applicable. Independently checked against [Sharifi, Iwasawa Theory, Theorem 4.5.6](https://www.math.ucla.edu/~sharifi/notes/iwasawa-ch04.html). The source's Washington section number was not independently verified from that book. |
| Fueter elements | Correct floor coefficients and their class-group principalization, with a correct norm direction in a spanning statement | Coefficient and conjugate-pair identities reconstructed directly; claimed `I^-` membership and full spanning fail as above. Full 1922 Fueter original was not obtained. No conclusion here depends on accepting its misquoted basis. |
| Jacobi generator of `A^t` | Primes supporting `A` prime to `p`, degree 1 over rational `ell=1 mod p`; characters of order `p`; nonzero character exponents and nonzero sum; products/inverses for general exponents | Supporting-prime hypotheses follow from the characteristic number. Existence of normalized generators is granted as the standard Gauss/Jacobi-sum principalization theorem, not fully reproved from Iwasawa's original. The central objections survive that grant. |
| `J=1 mod lambda^2` | The signed Jacobi convention with `J=-sum chi^a(u)chi^b(1-u)` and `a,b,a+b !=0 mod p`; products preserve the congruence | Direct verification in the degree-one case: modulo `lambda^2`, the constant term is `-(ell-2)=1` because `ell=1 mod p`; the linear term vanishes because the character of the product of `F_ell^*` is `chi(-1)=1` for odd `p`. This supplies the needed local congruence without treating a Gauss sum as a Jacobi sum. The PDF footnote discusses a Gauss sum, so it does not itself prove this normalization. A primary thesis, [Diophantine equations and cyclotomic fields, section 5.2](https://ediss.uni-goettingen.de/bitstream/handle/11858/00-1735-0000-0028-86F5-5/Thesis_Gottingen_Optimized.pdf?isAllowed=y&sequence=1), was consulted for the explicit Jacobi convention and the reference chain. The full Iwasawa 1975 original was not read. |
| Uniqueness up to roots of unity | Two generators of the same principal ideal, quotient an algebraic unit, equal positive rational conjugate products at every embedding | Valid by Kronecker. The generator's norm identity, rather than its ideal alone, is essential. |
| Kronecker unit theorem | Algebraic integer/unit whose every complex embedding has absolute value 1 | Applicable after integrality and all conjugate norm equalities are established. Fails to rescue Lemma 5 because the asserted integral quotient is missing. |
| Splitting/decomposition | `r != p,q`; Frobenius acts by `r` on each root of unity; residue degree in `C` is `ord_p(r)` | Valid. The source's descent from splitting over `C` to splitting over `Q` is not one of these theorems and is false as a general implication. |

The source also cites published Fermat work and surveys for context. Its proof of Section 3 does not invoke their conclusions to supply either missing implication. No reliance on authority, abstract wording, or journal status is used in this assessment.

## Exact potential relevance to 2025 B4(b)

Write the contest variable as `u`, number of terms `m=n+1`, right-hand base `v`, and exponent `Q>=2`. The open part asks for integer solutions of `S_m(u)=v^Q`; no preliminary part (a) is proved or reproduced here.

For prime term count `m=p>3`, a solution with `|u|>1` and an odd prime `q|Q`, `q != p`, would map to equation (2) via

\[
(X,Y,Z,e)=\begin{cases}
(u,-1,v^{Q/q},0),&u>1,\\
(-u,1,v^{Q/q},0),&u<-1.
\end{cases}
\]

The second line uses simultaneous sign change, preserving `F_p`. The sum is positive; because `Q/q` has the same parity as `Q` and `q` is odd, any permitted sign gives `Z>0` once the original equality holds. Primitivity is automatic from `Y=+/-1`, and `X>|Y|=1`. A prime-term perfect power has `p`-adic valuation divisible by `q`; since the quotient's `p`-valuation is 0 or 1, it must be 0. Thus the intended theorem, **if repaired and independently accepted**, would rule out this signed prime-term sector. The preprint as audited does not currently establish that exclusion.

For completeness, the same conditional bridge can apply to a prime factor `p>=5` of a composite term count: set `d=m/p`, `T=u^d`, and factor `S_m(u)=S_d(u)*Phi_p(T)`. Any common rational prime of the two factors is `p`, since `S_d(u)` divides `T-1` and `Phi_p(T)=p mod T-1`. Thus for odd prime `q|Q` distinct from `p`, every non-`p` valuation of `Phi_p(T)` is a multiple of `q`; its `p` valuation is 0 or 1. This gives `Phi_p(T)=p^e Z^q` with `|T|>1`, which normalizes to `(X,Y)=(T,-1)` or `(-T,1)`. This is a conditional reduction only, not a claimed classification or use of the unaccepted theorem.

The source excludes `p=3`, `q=2`, and the diagonal `q=p`. It does not handle term counts with no suitable prime factor or exponents with no suitable odd prime factor. The contest's `u=-1,0,1` boundary cases are outside `X>|Y|>=1` and must be handled independently in part (b). No statement of the preprint can be used to delete them. A single applicable prime divisor of a composite exponent would suffice for the conditional reduction; an exponent that is a power of 2 supplies none. No full contest solution follows even from accepting the intended restricted theorem.

## Reproduction and resources

Read-only commands: `cat AGENTS.md`; read the assigned source manifest; `shasum -a 256` on the ignored original; bundled Python `-B` with `pypdf.PdfReader` to extract all ten pages; Poppler `pdftoppm -f 2 -l 3 -r 110 -png` and `-f 4 -l 9 -r 110 -png` to `/private/tmp/strongfc-review-2-page-*`; `view_image` on pages 2-9. Source extraction was inspected in tool output and was not committed. The images are temporary derivatives, not repository deliverables. No full third-party paper or extract is added to tracked review files.

Dependencies: bundled runtime `26.1013.11914`; Python at `/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`, `pypdf`, Poppler override binaries, and built-in Python arithmetic for the small certificate script. No native CAS, long search, paid API, network purchase, access bypass, or global process cleanup was used. Poppler child session `27167` completed normally with exit code 0; the second rendering completed synchronously. The supplementary arithmetic script only checks explicitly listed finite identities and is evidence, not a proof of an unrestricted claim.

Authoritative account-wide telemetry checked during this audit: total weekly used 16%, duration 10080 minutes, reset `1792745187`, same window as the coordinator's 15% reading. Stop threshold remains 90% total used. No account identifier or credentials are saved.

Verification date: 2026-10-16 UTC (local Brisbane date 2026-10-17). A separate manifest records the exact blind-freeze time, file hashes, and later comparison boundary. Coordinator action required: arrange the independent audit needed before promoting any positive result or objection; do not adopt the preprint's theorem as an established ingredient on this review alone.
