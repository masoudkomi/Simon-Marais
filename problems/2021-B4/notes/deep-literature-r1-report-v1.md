# Deep literature checkpoint: 2021 B4(b)

Status: literature investigation, not a candidate full proof. Verified on 2026-10-16 UTC. Researcher requested gpt-6.1-sol/max; effective settings could not be read back. This work began after the separate J16 review was frozen. It changes no proof or review packet.

The search found no verified original theorem that settles **all rational-witness degree-20 polynomials**. This is a bounded literature finding, not a proof that no such theorem exists. The strongest relevant earlier claim located is Massri's exclusion of three recycled complex roots. That materially subsumes a rational three-value-cover exclusion; it does not subsume the complete rational degree-20 problem or the new J16-specific partial exclusion.

## Hypotheses that must stay separate

For the contest, f belongs to Q[x] and, for each 1<=j<d, some **rational** a_j satisfies f(a_j)=f^(j)(a_j)=0. The chosen values can vary with j. Three nearby statements have different hypotheses:

| Version | Roots required rational? | Relation to contest |
|---|---|---|
| Classical complex Casas-Alvero | No; shared roots may be arbitrary complex numbers | A valid classical exclusion implies the contest exclusion in that degree |
| Rational coefficients and nonconstant gcds over Q | No rational linear factor is required in each gcd | Also weaker hypotheses than the contest; not equivalent to having rational witnesses |
| All polynomial roots rational | Every root, including unused ones | Stronger assumptions; its exclusion alone does not settle the contest |
| At most three recycled values | Only a covering set for derivative conditions has size <=3 | Restricts the number of chosen common values, not the total root count |

## Original theorem map and the degree-20 trap

1. Graf von Bothmer, Labs, Schicho and van de Woestijne, [*The Casas-Alvero conjecture for infinitely many degrees*](https://arxiv.org/abs/math/0605090), J. Algebra 316 (2007), 224–230. Theorem 1.1 gives the classical characteristic-zero assertion for d=p^k and d=2p^k. Degree20 is in neither family. The local cached v2 is seven pages; the theorem, positive-characteristic Hasse formulation, and transfer argument were read, not inferred from the title.

2. Castryck, Laterveer and Ounaïes (CLO), [*Constraints on counterexamples ... and a verification in degree 12*](https://arxiv.org/abs/1208.5404), Math. Comp. 83 (2014), 3017–3037. In the cached 23-page version, Theorem3 (p4) requires nonexistence over **algebraic closure F_p**, using Hasse derivatives, before transferring degree m to mp^k. Theorem4 (p5) supplies bad-prime lists for m=5,6,7; paragraph1.7 gives bad primes3,5,7 for m=4. Thus 20=4·5 uses a bad prime, and 20=5·2² also uses a bad prime. Theorem5 proves degree12, not20. Proposition19 (pp15–16) requires **all** roots rational; the following remark extends that hypothesis to a number field unramified at p. Neither is a rational-witness theorem. Its Newton sums include unused roots, where integral valuations cannot be assumed from rational witnesses alone. Paragraph3.6 also distinguishes a matching scenario from the lexicographically minimal scenario, a useful warning for finite-cover reductions.

3. Draisma and de Jong's June2011 Newsletter article originally appeared to cover20. Their own [August2011 erratum](https://math-unibe.ch/jdraisma/publications/erratumcasasalvero.pdf), one page, explicitly adds p=5 to the excluded primes for base degree4 and retracts the degree20 conclusion. This is the original correction, rather than an inferred discrepancy in later degree lists. Their separate Proposition6 (printed pp31–32 of the original article) excludes two recycled values and is unaffected by the stated erratum.

4. Massri, [arXiv:1806.09561v6](https://arxiv.org/abs/1806.09561v6), 2023-08-25, Theorem7.10 ([full text](https://arxiv.org/html/1806.09561v6#S7.Thmtheorem7.10)), states a degree20 exclusion for witnesses in {0,1,y}, with y complex. The proof enumerates ternary Abel–Gontcharoff scenarios. Theorem7.9 separately excludes multiplicity>=11 in degree20. These are restricted classical claims, not a complete degree20 theorem. The active version is not marked withdrawn, although earlier versions are; no journal acceptance was verified. A [2024 SSRN posting](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4935880) is an author posting, not evidence of refereeing. The project's reviewed three-value result should be attributed as an independent restricted reproduction, without claiming to validate Massri's entire computation.

## Deeper bibliography results

Rosa María de Frutos Marín, *Perspectivas aritméticas para la Conjetura de Casas-Alvero*, Valladolid doctoral thesis, 2013, advisor Antonio Campillo. The [primary university PDF](https://uvadoc.uva.es/bitstream/handle/10324/3602/tesis367-130927.pdf?sequence=1), printed p29, Corollary2.3.4, treats every two-element lower support {i,j}; the introduction explains the centered normalization with zero vicelíder and constant coefficients. The source's indexed full-text extract gives 1<=i<j<=n−2 and a binomial discriminant argument. Therefore arbitrary **centered trinomials** were already treated, substantially predating our finite scans. Direct downloads and opens repeatedly timed out, including one escalated network retry; no successful full thesis cache or full independent proof audit is claimed. The theorem statement, normalization and exact locator were verified from indexed primary-source text. This is a concrete novelty risk and a priority source to retrieve fully before any new few-term theorem is proposed.

Schaub and Spivakovsky, [*A note on the Casas-Alvero Conjecture*, arXiv:2312.08742v7](https://arxiv.org/abs/2312.08742v7), 2025-02-11, five pages, Theorem5: each of the top three resultants is outside the radical generated by the others. This is nonredundancy, not the full regular-sequence/height assertion. The added-in-press paragraph endorses Ghosh's claimed proof; an endorsement is distinct from a supplied audit. A related journal record, *On the Casas-Alvero Conjecture*, J. Commut. Algebra17(2),199–202 (2025), DOI[10.1216/jca.2025.17.199](https://doi.org/10.1216/jca.2025.17.199), was located through bibliographic records, but the publisher full text was inaccessible in this pass. Its exact relationship to v7 is not asserted as verified.

Their [*A description of and an upper bound on the set of bad primes*, arXiv:2411.13967v1](https://arxiv.org/abs/2411.13967v1), Theorem3.1, identifies bad primes by gcds of maximal minors in finitely many explicit Macaulay matrices. Corollary3.2's finite upper bound is **conditional on CA in that degree already holding in characteristic zero**. It is not a shortcut to proving that assertion. All points here are over algebraic closures. In degree6 the displayed construction has1365 columns and2751 rows, before scenario multiplicity; importing it wholesale at degree20 is not a bounded next computation. A more focused use could certify a low-degree cluster obstruction, provided its witness field and degeneration are explicitly matched.

The earlier paper [*On the set of bad primes in the study of Casas-Alvero Conjecture*](https://doi.org/10.1007/s40687-024-00444-z), Research in the Mathematical Sciences11,31 (2024), provides a **non-exhaustive** list. Its publication was verified on the primary publisher page. Bad-prime witnesses do not exclude rational lifts, and the absence of a prime from a non-exhaustive list does not make it good.

## Current proof claims, acceptance, and contradictory frontier reports

Ghosh's [arXiv:2501.09272v2](https://arxiv.org/abs/2501.09272v2), TheoremA, claims the unrestricted characteristic-zero conjecture; a valid proof would settle the rational-witness variant too. It remains an active preprint in the checked arXiv record, with major revisions, no verified journal reference or withdrawal. The separate [finiteness paper, arXiv:2402.18717v3](https://arxiv.org/abs/2402.18717v3), is listed as accepted by the American Journal of Mathematics and by the author's [current page](https://ghosh-soham.github.io/). Fixed-degree finiteness is not emptiness. No new broad refutation is made here; the project's already reviewed narrow source objections retain their original scope.

Marashdeh's [arXiv:2608.14726v1](https://arxiv.org/abs/2608.14726v1), introduction, expressly treats the general claim as unverified and reports20 as the first open classical degree. His support/scenario reductions and MacMahon determinant interpretation suggest compact exact certificates, but do not assert all rational-witness20 is solved.

Gasull's published [2026 resultant survey](https://doi.org/10.1007/s44425-026-00047-6), section3.4, reports24. Its cited reference19 is the **2011 Draisma–de Jong article**, not a new degree20 proof; its own Proposition7 only treats degrees4,5. The source trail therefore does not validate20. The old article's erratum gives a plausible explanation for the inherited frontier error, but that explanation remains an inference rather than an author-confirmed correction. Social-media/aggregator claims discovered in search were not used as mathematical or acceptance evidence.

## Setter and committee attribution

The supplied `/committees.html` path was inaccessible. The official [about-us page](https://www.simonmarais.org/aboutus.html) currently labels its problem committee **2026**. Its members must not be retrospectively called the 2021 setters. The 2021 official B4 solution and targeted searches for explicit proposal credits did not establish an individual author. Neither Casas-Alvero's authorship of the research conjecture nor a current committee member's research interests establishes who selected/wrote the contest problem. No one was contacted.

## Actionable conclusions

- Keep rational-witness20 and the all-roots-rational theorem separate in every theorem/novelty description. The verified J16 result remains a partial exclusion; this search found no validated source subsuming it as a complete rational degree20 theorem.
- Attribute the complex three-value-cover target to Massri before describing the project's independent certificate.
- Retrieve and check de Frutos' Corollary2.3.4 before spending on further centered-trinomial scans. Investigate four-term supports only with a precise novelty comparison against the thesis and Marashdeh.
- Use bad-prime matrices or descent-set determinants on a selected small cluster/scenario with explicit finite bounds; do not treat their general constructions as a feasible all-degree computation.

Search details, access failures and cached source hashes are recorded in the companion `deep-literature-r1-search-log-v1.json` and `deep-literature-r1-sources-v1.json`. No full solution is asserted.
