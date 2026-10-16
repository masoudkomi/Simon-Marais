# Independent adversarial audit R2: fixed-factor family v1

Initial report completed 2026-10-16. Reviewer recommendation: **accept the
stated partial family; no substantive mathematical objection found.** This
is one independent audit, not a coordinator promotion and not a full
solution of B4(b).

## Independence, scope, and frozen inputs

I did not construct this proof. I reconstructed the complete argument
without reading another review, another reviewer's evidence, the
constructor's computational output, or the repository's status conclusions.
I did not import, read, or execute the constructor's certificate program.
The manifest's files were read by my program solely to compare their raw
hashes and byte lengths. All nine manifest entries match.

The audited proof is `proofs/fixed-factor-family-v1.md`, SHA-256
`1a1a8e6513d175cc075e13c6353371a9ece47e0c37d6781b16999a3544f9e376`.
The manifest SHA-256 is
`6c44cfe97734ccaf74062f62e92d52758be1c338787c1667a7b238e4c8d4542d`.
Requested reviewer settings were gpt-6.1-sol / max reasoning. There is no
verified effective-setting readback. No subagents, installations, commits,
or pushes were used.

I visually inspected the complete relevant official page, cached at
`.cache/official/2024-paper_b.pdf` (SHA-256
`1401f21218ad4c387c4d537ed8fd7de119b376cba52957ef788c772dc5ab4ddc`),
and saved my own rendering as `family-review-2-official-page2.png`.
Only B4(b) was audited. It asks for all odd positive n with the stated
coefficientwise congruence and two integer factors nonconstant modulo 2.
The claimed contribution is narrower: divisibility by phi_13 at
n=(64*16^m+1)/5 for m>=0, producing two nonconstant factors only for m>=1.
Neither a full classification nor a novelty claim is justified or made.

## Whole-argument reconstruction and inference audit

1. **Formal generating function, with multiplicities.** Work in the
   polynomial ring over F2 and its formal power-series ring. Set
   w=x+y+z. Direct expansion of the four indexed factors gives
   E(t)=(1+xt)(1+yt)(1+zt)(1+wt)=1+Qt^2+Rt^3+Dt^4, with Q,R,D as
   displayed in the proof. I independently checked this expansion over
   GF(2). Treating the four entries as a list is necessary and sufficient;
   coinciding values after specialization do not change the product rule.
   E(0)=1, so all inverses used exist formally. The logarithmic derivative
   is an identity obtained by the product rule, without dividing by any
   list entry. In characteristic two E'=Rt^2. Expanding each
   a/(1+at) and multiplying by t therefore gives
   sum_(n>=1) f_n t^n=Rt^3/E. This is coefficientwise, not a statement
   about functions on a finite field. Because R is a nonzero polynomial,
   f_n/R for n>=3 is the uniquely specified coefficient of E^(-1).

2. **Parity extraction and independent invariant variables.** Since
   E^2=1+Q^2t^4+R^2t^6+D^2t^8 has only even powers, the even part of
   E/E^2 is exactly (1+Qt^2+Dt^4)/E^2. For n=2j+3 one needs
   the coefficient t^(2j) of E^(-1), so replacing t^2 by s gives
   formula (3) with the correct index. Defining P_j in independent
   q,u,d and then substituting (Q,R^2,D) is legitimate coefficient by
   coefficient because the denominators have constant coefficient 1.
   The denominator recurrence independently gives P_0 through P_5,
   including A=P_5=q^5+qd^2+ud. I also checked directly against the
   original f_13 that R*A(Q,R^2,D)=f_13. Weight(q,u,d)=(2,6,4)
   makes P_j homogeneous of weight 2j; this follows either from the
   recurrence or the denominator expansion. No assumption that every
   factor belongs to this invariant subring is present or needed.

3. **The localized divisor and normalized coefficients.** Inverting q,d
   is a legitimate intermediate computation. In U/(A), the coefficient
   d of u is a unit, so eliminating u gives exactly
   F2[q,q^(-1),d,d^(-1)], with no extra relation. With b=d/q^2 this
   becomes F2[q,q^(-1),b,b^(-1)]. Here d=q^2b and
   u=q^3(b+b^(-1)). Substituting s=z/q gives numerator 1+z+bz^2
   and denominator K=1+z^2+(b+b^(-1))z^3+b^2z^4. Consequently
   its j-th coefficient is q^(-j)P_j in the quotient. I checked both
   substitutions exactly after clearing their Laurent denominators.
   Coefficients of F are in Lambda=F2[b,b^(-1)], which injects into
   E=F2(b). Vanishing proved in E therefore also means vanishing in
   the localized quotient; q is an independent invertible variable.

4. **Coefficient selection and the denominator change.** For C_r with
   stride 16, coefficient convolution proves
   C_r(H(z)G(z^16))=C_r(H(z))G(z). For any fixed output coefficient,
   the required convolution is finite. The operator is E-linear and
   never takes roots or raises arbitrary coefficients to powers.
   Frobenius gives K(z,b)^16=K(z^16,b^16); applying the preceding
   formula to P*K^15/K(z^16,b^16) proves (8). For deg P<=3,
   deg_z(P*K^15)<=63, so only selected degrees 0 through 3 can occur.
   E need not be perfect, and the substitution b -> b^16 need not be
   surjective. Neither fact obstructs this argument.

5. **All three symbolic Cartier identities.** I independently verified
   (9), (10), and (11) as complete polynomial identities, not by plugging
   in parameter values. Specifically, write

       H=b*K=b+b*z^2+(b^2+1)*z^3+b^3*z^4.

   Then b^15*C_r(P*K^15)=C_r(P*H^15), since C_r is E-linear.
   I used SymPy's ordinary multivariate `Poly` arithmetic over GF(2)
   to raise H to the fifteenth power and select all z exponents in the
   appropriate residue class. I compared the resulting full polynomials
   with b^15 times the displayed right sides. This differs from the
   constructor's Laurent-monomial-set program and does not use its saved
   evidence. H^15 has 361 terms and z-degree 60. The selected numerators
   for (9), (10), (11) have respectively 49, 24, 25 terms; each has
   z-degree 3 and no constant term. Every remainder is zero. The saved
   JSON includes every selected coefficient, represented by all b
   exponents after clearing b^15. I also checked the polynomial
   Frobenius identity independently. These finite exact computations
   check the universal formal identities; they alone are not the
   justification for arbitrary m.

6. **The changing span and unrestricted induction.** Identity (9)
   places C_5F in V(b^16). For any c=b^(16^k), (10) and (11) remain
   valid on substituting b=c, as they are Laurent-polynomial identities.
   If the input numerator is alpha*z+beta*(z^2+c*z^3), the output is

       (alpha*L(c)+beta*M(c))*z
       +(alpha*L(c)+beta*J(c))*(z^2+c^16*z^3).

   Alpha and beta remain unchanged outside coefficient selection;
   Frobenius applies to K, not to those scalar multipliers. All the
   displayed coefficients lie in E, even when they do not belong to
   the smaller field F2(c). Thus C_6 V(c) is contained in V(c^16)
   with the correct coefficient field. Every such series has constant
   coefficient zero, since K(0,c)=1. Induction consequently gives zero
   constant coefficient in C_6^m C_5F for every integer m>=0.

7. **Hexadecimal index and direction of composition.** C_5 first
   retains exponents 16a+5. Applying C_6 to this output retains original
   exponents 16(16a+6)+5. Iterating yields
   16^(m+1)a+j_m with j_m=5+6*16+...+6*16^m. Thus the operator order
   in the proof is correct: digits are removed from the least significant
   end. The geometric sum gives j_m=(32*16^m-7)/5 and
   2j_m+3=(64*16^m+1)/5. The empty sum at m=0 gives j_0=5 and n_0=13.
   These equalities establish vanishing at all the asserted indices,
   with no finite bound on m. My separate recurrence checks for j=5
   and 101 are explicitly only finite evidence and are unnecessary
   to this unrestricted inference.

8. **Descent from the localization.** The key saturation argument is
   sound. In F2[q,d][u], the coefficients d and q(q^4+d^2) of A
   are coprime: the only possible irreducible divisor of d is d,
   and setting d=0 in the other coefficient leaves q^5. Hence A
   is primitive. Over F2(q,d), A has degree one in u and is
   irreducible. Gauss's lemma applies over the UFD F2[q,d], so A
   is irreducible in S=F2[q,u,d]. Polynomial rings over a field are
   UFDs, making this irreducible element prime. Its positive u-degree
   prevents it from dividing the nonzero u-degree-zero polynomials
   q and d. Membership P_j in A*U therefore clears to divisibility
   of q^a d^b P_j by A in S; primality forces A|P_j. This recovers
   a genuine polynomial identity in S, including loci q=0 or d=0.
   An identity known only after numerical specialization would not
   suffice; the proof does not make that error.

9. **Nonvanishing, actual degrees, and the official congruence.** Both
   factors in P_j=A B_m can be taken homogeneous, since multiplying
   each weight component of B_m by the nonzero homogeneous A cannot
   cancel a component of another weight. Substitution now gives
   phi_n=phi_13*B_m(Q,R^2,D) in the actual polynomial ring over F2,
   before any numerical evaluation. For odd n>1 the coefficient
   x^(n-1)y in f_n is n modulo 2, hence 1, so f_n and phi_n are
   nonzero. Phi_n is homogeneous of degree n-3. Phi_13 is thus
   nonzero homogeneous of degree 10; the product identity forces
   the substituted B_m to be nonzero. Because the substitutions
   have total degrees 2,6,4, a surviving homogeneous component has
   actual degree n-13. This does not require the substitution map
   on the invariant ring to be injective. For m>=1, n>=205, so
   both factor degrees are positive (10 and at least 192). Lifting
   F2 coefficients to 0 or 1 gives integer polynomials g,h, each
   nonconstant modulo 2, and multiplying by R gives exactly the
   coefficientwise congruence required in B4(b). The exponent is
   integral because 16=1 and 64=-1 modulo 5; it is odd and positive.

## Adversarial cases and limitations

- Repeated entries among x,y,z,w, and specializations where R=0, do not
  undermine the formal identity. Cancellation by R is performed only
  in the polynomial integral domain, never after specialization.
- Special loci Q=0 or D=0 cannot invalidate the conclusion: q and d
  are eliminated from denominators before substitution. Primality is
  precisely what prevents a factor supported on these loci from
  disappearing during localization.
- The rational coefficient field can be imperfect. The explicit
  coefficient-selection definition and its linearity avoid any hidden
  extraction of sixteenth roots.
- At m=0 the second factor is 1. The family argument therefore does
  not assert that n=13 satisfies the official two-nonconstant-factor
  condition. No classification of n=13, n=1, or exponents outside the
  asserted family is inferred by this audit.
- The result supplies factors defined over F2 and hence valid integer
  lifts. It does not use a factorization over an extension field,
  absolute irreducibility, APN classification, or a pointwise equality
  on F2^3.
- No counterexample, omitted boundary within m>=0, or substantive gap
  was found in this audit. No repair is requested for the mathematics.

## Attribution audit

I checked [Hernando--McGuire, arXiv:0903.2016v4, Section 6, printed
page 18](https://arxiv.org/pdf/0903.2016) directly on 2026-10-16.
It reports the n=205 factorization over F2 and prints a degree-ten
affine factor. My independent transcription of its 42 monomials
equals A(Q,R^2,D) at z=1 exactly. Thus the stated identification
with the affine form of phi_13 is supported independently of the
constructor's n205 certificate. This is attribution verification,
not an external theorem used in the proof above.

I also checked [Férard's 2014 publisher
abstract](https://www.aimsciences.org/article/doi/10.3934/amc.2014.8.497)
on 2026-10-16. In the t=5 modulo 8 setting it discusses a phi_13
divisibility criterion and also announces an infinite family. The
abstract does not identify the exponents of that family. I have not
read or audited the full theorem and make no claim that the current
formula is new or different. The proof's explicit caveat and its
independence from that theorem are appropriate. Its exact relation to
the published family remains an attribution task, not a missing
premise of this proof.

## Reproduction, failures, and checkpoint

From the repository root:

```sh
.venv/bin/python -u problems/2024-B4/reviews/family-review-2-run.py
```

The supervisor invokes `family-review-2-check.py` in a dedicated child
with a 30-second timeout, records its PID before waiting, writes flushed
checkpoints, and would kill only that child on timeout. The final run
used PID 14517, Python 3.12.14, and SymPy 1.14.0; it returned 0 in
0.497 seconds with empty stderr. The exact run record, standard output,
standard error, and complete symbolic coefficient data are the
`family-review-2-run.json`, `family-review-2-stdout.txt`,
`family-review-2-stderr.txt`, and `family-review-2-check.json` files.
The scripts require only the existing virtual environment and SymPy.

One initial harness run (PID 14299) stopped at a misleading direct
SymPy `Poly.diff` comparison: over GF(2), its nested representation
retained leading zero layers, despite identical monomial coefficient
dictionaries. Reconstructing a canonical Poly from the differentiated
expression resolves that harness issue. This was not a counterexample
to E'=Rt^2. The initial script and its failing output, stderr, run
record, and partial JSON are retained with the `family-review-2-attempt1-`
prefix; the archived script is historical and is not the reproduction
entry point. The final script additionally checks the published
degree-ten factor. No mathematical check in the final run failed.

`pdftotext` was unavailable (exit 127); direct page rendering with
`pdftoppm -f 2 -singlefile -scale-to 1800 -png` and visual inspection
succeeded. A web screenshot attempt for the arXiv page was unavailable;
the primary PDF's parsed Section 6 supplied the attribution check.

The authoritative account-wide weekly telemetry at 2026-10-16
10:35:26 UTC reported `rateLimitsByLimitId.codex.primary.usedPercent=4`,
`windowDurationMins=10080`, and `resetsAt=1792745187`. This is total
weekly usage, well below the 90% stopping threshold. No separately
billed API was used.

This completes my blind initial audit. Only the coordinator may combine
it with the second independent audit, resolve any other objections, and
promote the result's status.
