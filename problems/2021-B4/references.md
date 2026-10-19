# 2021 B4 references and published status

10:48 Brisbane update: [R24A--C](reviews/reasoning-deep-return-r24-acceptance.md) is **proved, independently reviewed scoped partial result** after B/C OTHER whole32 audits and root full64 reconciliation. In the retained actual negative frameIII, every d>=3 has t=1 and full gcd(f,H12)=X-s; t>=2 is confined to d2 with a9=a10=0 and full H11/H10 gcds X/X². Residual sectors, full degree20 and the annual question remain open. No new external theorem or priority claim. Earlier dated snapshots remain historical.

## Official starting sources

- [Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf), B4 on page 2.
- [Official solutions](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-solutions.pdf).

The official solutions identify the Casas-Alvero connection and discuss known
degree families. That discussion is attributed historical context. No
preliminary part (a) proof is reproduced in this research packet.

## Current-literature audit

Checked 2026-10-16. This is a bounded audit, not proof that no other publication
exists. No accepted general solution was verified. The current situation is a
general proof claim with independent validation unresolved in these sources.

| Primary source | Verified content and scope | Status / caution |
|---|---|---|
| [Graf von Bothmer, Labs, Schicho, van de Woestijne, *The Casas-Alvero conjecture for infinitely many degrees*](https://doi.org/10.1016/j.jalgebra.2007.06.017), J. Algebra 316 (2007), 224-230; [arXiv math/0605090](https://arxiv.org/abs/math/0605090) | Characteristic zero, common factors with derivatives; covers prime-power degrees and twice prime powers. Hence applicable to the stronger contest hypothesis. | Published work; attributed context only. |
| [Castryck, Laterveer, Ounaies, *Constraints on counterexamples ... and a verification in degree 12*](https://arxiv.org/abs/1208.5404), Math. Comp. 83 (2014), 3017-3037 | Theorems 3-5: transfer from algebraically closed characteristic p using Hasse derivatives; 5p^k, 6p^k, 7p^k outside explicit bad-prime lists, plus degree 12. For degree 5 the bad primes are 2,3,7,11,131,193,599,3541,8009. | Published. Its original discussion identifies 20 as the next open degree. Rational witnesses are stronger than its common-root hypothesis. |
| [Ghosh, *Proof of the Casas-Alvero conjecture*, arXiv:2501.09272v2](https://arxiv.org/abs/2501.09272v2), [full HTML](https://arxiv.org/html/2501.09272v2) | Theorem A claims every degree >=3 over any characteristic-zero field, using nonconstant gcds with Hasse derivatives. If valid, it implies all contest degrees >=2. ArXiv gives v1 2025-01-16, v2 2026-03-21 and comment "Major revisions". No withdrawal or journal reference appears there. | Active preprint claim, not accepted as a result in this packet. Its HTML displays internal date 2026-08-24 despite March version metadata. A focused second pass identified three inferences requiring specialized justification; see the source-audit note below. Neither the objections nor the theorem have been independently validated in this packet. |
| [Marashdeh, *A descent-set obstruction for the Casas-Alvero conjecture*, arXiv:2608.14726v1](https://arxiv.org/abs/2608.14726v1), [HTML](https://arxiv.org/html/2608.14726v1), 2026-08-12 | Introduction explicitly says Ghosh's work has not been independently verified and therefore treats the conjecture as open. It studies support/scenario reductions, not a full proof. | Preprint. Reports smallest open degree 20. No new result here relies on its theorem. |
| [Gasull, *A Primer on Resultants and Their Applications*](https://doi.org/10.1007/s44425-026-00047-6), Matematica Contemporanea, 2026-05-28, sec. 3.4 | Describes complex Casas-Alvero as open, reporting 24 as smallest open degree. | Published survey; its frontier disagrees with the August preprint and the degree-family audit. Do not use 24 as an established frontier. |
| [Battiston, *The Casas-Alvero conjecture*, arXiv:1511.04932v2](https://arxiv.org/abs/1511.04932v2) | Withdrawn 2015-11-19; author identifies a crucial error on the last page, pointed out by Joseph Schicho. | Withdrawn claim, unusable as proof. |
| [Dobrowolski, *Casas-Alvero Conjecture is true*, arXiv:1705.01704v2](https://arxiv.org/abs/1705.01704v2) | Withdrawn 2017-05-07; author says Jacob Tsimerman found an irreparable error. | Withdrawn claim, unusable as proof. |
| [Ghosh, *A finiteness result towards the Casas-Alvero Conjecture*, arXiv:2402.18717v3](https://arxiv.org/abs/2402.18717v3) | Fixed-degree arithmetic scheme finiteness is distinct from emptiness; it does not by itself settle the contest question. V3 2025-01-14, comment "Submitted version". | [Author's university page](https://sites.math.washington.edu/~soham13/) lists it as to appear in American Journal of Mathematics, and the [journal's accepted-paper list](https://math.jhu.edu/~ajm/) lists it 2026-04-07. This acceptance concerns the finiteness paper, not the universal-proof claim. |

Queries included exact arXiv identifiers; "Casas Alvero rational common roots
rational coefficients conjecture rational roots all degrees"; "2501.09272 error
gap critique"; "Proof of the Casas-Alvero conjecture Ghosh Journal"; and
"Casas-Alvero degree 20 24". Secondary search results were used only to locate
primary records. A social-media claim of a further degree-20 type restriction
was not treated as a theorem or reproduced.

## Focused second pass, 2026-10-16

The Ghosh v2 source-use audit is in
`notes/ghosh-full-context-audit-v1.md`. It reconstructs the dependency chain,
checks applicability to the exact rational-witness contest statement, and
identifies the coefficient descent after (4.23) as an invalid general
Artinian-ring inference. The local determinantal model and the two additional
queries are **candidate objections**, with specialized repair unresolved and
two independent audits still needed. No counterexample to the specialized
lemma or the Casas-Alvero conjecture is claimed. The accepted finiteness paper
is kept distinct from the universal proof claim.

Additional primary sources read in this pass:

| Source | Verified content / use | Limits |
|---|---|---|
| [Draisma and de Jong, *On the Casas-Alvero conjecture*](https://www.ems-ph.org/journals/newsletter/pdf/2011-06-80.pdf), EMS Newsletter 80 (2011), 29-33 | Proposition 6, printed pp. 31-32 (PDF pages 33-34, one-based), rules out exactly two distinct chosen common witness roots and attributes the observation to Draisma and Knopper. CLO §1.2 defines the covering-set invariant type; its Proposition 7 gives type>=2. This is the recycled-root result needed in the rational/Eisenstein note. | Distinct recycled roots are not the full root set. The later degree-family statement in this newsletter was corrected by CLO; it is not used here. |
| [Massri, *The Casas-Alvero conjecture for three recycled roots in degree 20*, arXiv:1806.09561v6](https://arxiv.org/abs/1806.09561v6), [full HTML](https://arxiv.org/html/1806.09561v6), 2023-08-25 | Theorem 7.10 claims degree-20 exclusion with three recycled roots via 3^17 one-parameter scenario/resultant cases. Remark 7.4 separately reports 6680 surviving binary mod-19 patterns, matching the small exact necessary-pattern calculation saved here. | Active v6 preprint, with earlier v2/v3/v5 marked withdrawn in the version history. No journal acceptance or full computation certificate was verified here. The treatment of degenerate parameter values and saturation, and the complete resultant computation, still need audit before use as a validated exclusion. |

The coordinator cached Massri v6 at
`.cache/literature/2021/massri-1806.09561v6.pdf` and owns its central retrieval
manifest entry. No full third-party paper was placed in the tracked year
directory. The local candidate Eisenstein restriction and its source-by-source
hypothesis map are in `notes/rational-witness-p-plus-one-v1.md`.
