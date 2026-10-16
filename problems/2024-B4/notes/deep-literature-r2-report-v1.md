# Deep literature investigation: 2024 B4(b)

Checked 2026-10-16 UTC. Research worker R2; requested GPT-6.1-sol/max,
effective-setting readback unavailable. Only part (b) is investigated.
Preliminary part (a) is not solved or reproduced. Existing accepted
whole-phi13 work and shared status files are unchanged. New deductions in
this packet are **candidate proof - unverified** unless explicitly
identified as an earlier reviewed result.

## Outcome and the exact target

The search obtained a legal full original-author thesis containing the
JMW-era irreducibility proofs, including results beyond that journal
article. It did not obtain the full Janwa--Wilson 1993 chapter or Férard
2014/2017 theorem texts. Those access gaps must remain explicit. I located
no full classification of the contest's F2 reducibility problem.

For odd positive n, write

    f_n=x^n+y^n+z^n+(x+y+z)^n,
    R=(x+y)(y+z)(z+x),       phi_n=f_n/R over F2.

The [official part (b)](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc_2024_solutions.pdf),
PDF p. 15/printed p. 14, asks when f_n=Rgh modulo two, with both integer
lifts g,h nonconstant modulo two. Thus the relevant factorization is over
F2, with both factors of positive degree; no minimum degree two is
stated. Absolute reducibility over the algebraic closure is a different
condition. A nonconstant factor defined over an extension alone need not
supply an F2 factorization. The same page explicitly credits **Peter
McNamara** as proposer of B4; this is actual problem credit, not an
inference from the current committee list.

At the boundary n=1, phi_n is zero, so positive-degree factors cannot
multiply to it in the polynomial domain; at n=3, phi_n is a unit. These
cases must be handled separately from irreducibility theorems for
nonconstant phi_n. The integer lifts of F2 factors impose no additional
condition: coefficients zero or one give such lifts.

The already reviewed project result is

    whole phi13 divides phi_n  iff  n=(64*16^m+1)/5, m>=0.

At m=0 the cofactor is a unit; at m>=1 it supplies two positive-degree
F2 factors. It classifies divisibility by this entire degree-ten factor,
not every possible reducibility mechanism. The source attribution for
the n=205 example remains Hernando--McGuire (2011). No novelty is claimed
for their factor or the published APN mechanism.

## Original-author source newly obtained

Gary M. McGuire,
[Absolutely irreducible curves with applications to combinatorics and coding theory](https://thesis.caltech.edu/4053/),
Caltech PhD thesis (1995), DOI 10.7907/1CZ2-6S05,
[public full PDF](https://thesis.caltech.edu/4053/01/McGuire_gm_1995.pdf),
97 scanned pages, was downloaded normally and cached. The inspected
pages include the introduction, all needed preliminary propositions,
Chapter 2's definitions and full proofs through Theorem 8, and the later
factor-field proposition. Printed p. 2 expressly says Theorem 2.1 and
Section 2.4 through Theorem 7 are to appear with Janwa and Wilson in the
Journal of Algebra; Theorem 8 onward are thesis results absent from that
paper. This is an original-author parallel version, not a claim to have
read the inaccessible journal PDF. The correct journal citation is
J. Algebra 178(2) (1995), 665--676,
[DOI 10.1006/jabr.1995.1372](https://doi.org/10.1006/jabr.1995.1372).
The year is 1995; some later citations/search phrases use 1996.

The polynomial g_t on printed pp. 15--16 is exactly the homogeneous
phi_t above, with the same characteristic two and the affine form z=1.
Here `t=2^i*ell+1`, `i>=1`, `ell` odd. The following are literal
mathematical hypotheses from the full text, paraphrased here.

| Source location | Hypotheses | Conclusion relevant to (b) |
|---|---|---|
| Theorem 2.1', printed pp. 19--20, PDF pp. 24--25 | t>3 and t congruent 3 modulo 4 | phi_t is absolutely irreducible; therefore it has no two positive-degree F2 factors |
| Theorem 6, printed pp. 22--23, PDF pp. 27--28 | t>13, t congruent 5 modulo 8, and the maximal binary cyclic code B_ell has no word of weight four; here ell=(t-1)/4 | Absolute irreducibility |
| Theorem 7, printed pp. 23--24, PDF pp. 28--29, within Section 2.4 | i>=2, ell>1 odd, B_ell has no word of weight four, and gcd(ell,2^i-1)=1 | Absolute irreducibility |
| Thesis Theorem 8, printed pp. 24--26, PDF pp. 29--31 | t=2^i*(2^(i+1)-1)+1, i>=1 | Absolute irreducibility; this excludes 7,29,121,497,... from the reducible set |

B_ell here consists of binary polynomials of degree below ell vanishing
at a chosen primitive ell-th root of unity. That code condition is
substantive. The text preceding Theorem 6 gives sufficient arithmetic
conditions for it, including ell prime congruent plus or minus three
modulo eight, and more generally that minus one or three is a power of
two modulo ell. The full original conditions cannot be replaced merely
by “t congruent 5 modulo 8”. Theorem 6's small t=21 subcase invokes the
earlier Janwa--Wilson result, while its later cases use the displayed
intersection bound. A future reconstruction should preserve that source
dependency.

The proof mechanism is useful for current research: express singular
coordinates as ell-th roots of unity, use the first two nonzero local
homogeneous terms to exclude shared components at most singularities,
and compare the remaining intersection multiplicity with Bézout's total
degree product. Proposition A, printed pp. 9--10, requires coprime
successive local terms and a single tangent direction; omitting that
second premise invalidates its local conclusion. Theorem 8 controls the
remaining off-diagonal points through the coprime finite-field degrees
i and i+1. These are genuine exclusion methods for part (b), although
this packet is not an independent audit of the thesis proofs.

Proposition B, printed pp. 10--11, distinguishes a nonsingular rational
point from a singular one and explicitly assumes base-field
irreducibility for its stronger parts. Proposition 9, printed p. 29,
likewise **assumes** phi_t irreducible over F2 before constraining the
number r of conjugate absolute factors to divide
`gcd(t-3,2^i-2)`. For t congruent 5 modulo 8 this leaves r=1 or 2.
It cannot be used to establish the missing F2-irreducibility assumption.
This is the same logical caveat needed for Hernando--McGuire Theorem 15.

## Kasami factors: precise fields and a conditional usable deduction

The full author [Delgado--Janwa preprint, arXiv:1612.05997v1](https://arxiv.org/pdf/1612.05997v1),
2016-12-18, Section 3, equations (5)--(6), states the Janwa--Wilson
Kasami decomposition for `t=2^(2k)-2^k+1`: the affine phi_t is a product
of distinct absolute factors P_alpha of degree `2^k+1`, indexed by
`alpha in F_(2^k) minus F2`, with coefficients in F_(2^k) and
`P_alpha(x,0)=(x+alpha)^(2^k+1)`. Equation (6) explicitly groups
Frobenius-conjugate factors into F2 polynomials. This is a full theorem
statement in an author paper, but the original 1993 proof remains unread.

A precise conditional deduction is saved in
[the orbit lead](deep-literature-r2-kasami-orbit-lead-v1.md): given that
decomposition, each Frobenius orbit of alpha contributes one irreducible
F2 factor of degree `(orbit size)*(2^k+1)`. The smallest nontrivial case
k=2 has a single orbit, explaining how phi13 can be irreducible over F2
while splitting into two absolute quintics over F4. For k>=3, the number
of nontrivial field elements exceeds k, so there is more than one orbit
and an F2 factorization. The original-theorem source check and the
descent proof need independent review before promotion. This discussion
does not reproduce the preliminary Gold construction.

The [Caltech Janwa--Wilson 1993 record](https://authors.library.caltech.edu/records/wcxdz-pkj80)
is metadata-only. Its
[Springer chapter page](https://link.springer.com/chapter/10.1007/3-540-56686-4_43)
explicitly labels the content subscription preview; the full chapter was
not obtained. Its electronic online dates in 2005 do not replace the
1993 publication year. No login, payment or hidden access route was used.

## Férard: what remains unverified

The primary [2014 publisher page](https://www.aimsciences.org/article/doi/10.3934/amc.2014.8.497)
offers an abstract about t congruent 5 modulo 8 and a relation between
failure of absolute irreducibility and whole-phi13 divisibility. It does
not expose the full qualifying premises in the accessible text. Taken
without qualifications, its wording would include t=5, where the
degree-ten factor cannot divide the degree-two quotient, so an abstract
cannot be used as the universal theorem. The repository's earlier
conditional “t>13” slice is still a conditional lead, not verified
original literature.

The [GAATI publication list](https://gaati.org/publications/fr/) identifies
HAL hal-01779804 for the 2014 paper. The normal HAL API exposed an
open-access flag but no `fileMain`; a normal `/document` route returned
404 in the earlier access check. Publisher PDF navigation required access;
author-homepage and record requests returned errors or anti-bot pages.
These were not bypassed. The flag alone is not a downloaded full text.

The sequel, [Cryptography and Communications 9 (2017), 749--767](https://doi.org/10.1007/s12095-017-0213-1),
is associated with HAL hal-03417811. The public HAL API, cached in this
pass, reports `openAccess_bool=false` and no `fileMain`. Its abstract
mentions a sufficiently large odd part of t-1 with exclusions, but the
threshold and full excluded forms remain unread; no usable theorem is
claimed from it. The distinct 2017 Contemporary Mathematics paper,
[DOI 10.1090/conm/686/13777](https://doi.org/10.1090/conm/686/13777),
HAL hal-03417866, concerns perturbed Kasami functions and was identified
through references, not verified in full. These are separate papers.

A forward citation, Delgado--Janwa,
[Congressus Numerantium 232 (2019)](https://combinatorialpress.com/article/cn/Volume%20232/vol-232-paper%204.pdf),
was downloaded and all ten scanned pages inspected. Its PDF jumps from
printed p. 102 to p. 104 and ends at p. 111 despite advertising pp. 101--112.
Thus it is not a complete proof source as supplied. Its reproduced
Kasami decomposition, transversal-intersection result for perturbed
polynomials, and four finite Magma examples do not verify Férard's full
premise or classify the pure monomials in part (b). The incomplete scan
is an access limitation, not a mathematical counterexample to the paper.

## Concrete next mathematics and limits

1. Use the original-author thesis to attach fully qualified excluded
   exponent families to part (b), with new reviews if any new project
   deduction is promoted. In particular, inspect the thesis-only family
   rather than treating the 2011 APN classification as whole-polynomial
   irreducibility.
2. Complete the Kasami source/descent audit in the separate conditional
   note. The F2 orbit factors are the right objects for the contest;
   finding absolute factors alone is insufficient.
3. Obtain a normal legal full Férard text if it becomes available. If the
   proposed t>13,5-modulo-8 premise is verified, combine it with the already
   reviewed whole-phi13 criterion. Until then, no complete residue-class
   classification follows.
4. For remaining exponents, study singularity incidence and Frobenius
   orbits of components, not only the existence of an F2-defined absolute
   component. The 2011 exceptional-APN result proves a weaker property
   than F2 irreducibility of the entire phi_n.

The [search/source manifest](deep-literature-r2-search-sources-v1.json)
records exact URLs, hashes, read scope, versions and failed routes.
Scanned-source page fingerprints are cached with the PDFs; all full
third-party material remains ignored under `.cache/`. No other-year
setter inference, preliminary proof, Git action, paid access, author
contact or access bypass occurred. The latest authoritative weekly usage
was 15% total in the 10080-minute window, reset 1792745187; 90% total cutoff.
