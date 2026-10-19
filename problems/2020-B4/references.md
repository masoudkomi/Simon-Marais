# 2020 B4 references and published status

## Official starting sources

- [Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2020-paper-b_1.pdf), B4 on page 2.
- [Official solutions](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2020-solutions_1.pdf).

The official discussion (p. 27) connects (b) to cyclic planar difference sets and attributes prime-power existence to Singer. That existence theorem is used only as established context; its preliminary construction is not reproduced.

## Current-literature audit

Checked 2026-10-16, approximately 09:25-09:33 UTC. The latest primary paper explicitly discussing the conjecture that was checked was Alexeev-Mixon v2, revised 2026-01-16. It treats the cyclic Prime Power Conjecture as unresolved. No full resolution was identified by this search. This is a qualified literature-status assessment, not a proof that no later result exists.

The conjectural answer for the actual official domain is \(n=2\) or \(n-1\) a positive-exponent prime power. The three statements below must be kept separate:

1. The cyclic Prime Power Conjecture concerns cyclic planar difference sets, equivalently planes admitting a cyclic regular point action. This is exactly B4(b) after the boundary is handled.
2. The abelian planar-difference-set conjecture is stronger in group scope.
3. The assertion that *every* finite projective-plane order is a prime power is stronger again. B4(b) does not require arbitrary planes to be cyclic. The claim that every cyclic plane is Desarguesian is a separate stronger structural conjecture.

## Checked sources and exact uses

- **Singer (1938).** James Singer, *A theorem in finite projective geometry and some applications to number theory*, Transactions AMS 43, 377-385, [DOI](https://doi.org/10.1090/S0002-9947-1938-1501951-4). The AMS PDF and landing page returned HTTP 403 in the browser tool. Original full text was **not** independently retrieved. Prime-power existence is checked as an attributed theorem in the official discussion and in Peluse and Alexeev-Mixon; no claim of a direct Singer proof audit is made.
- **Gordon (1994).** Daniel M. Gordon, *The prime power conjecture is true for n < 2,000,000*, Electronic Journal of Combinatorics 1, R6, [publisher page](https://doi.org/10.37236/1186), [full PDF](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v1i1r6/pdf/). Full text checked: Theorem 2 supplies divisor multipliers for planar abelian difference sets; Theorem 3 supplies a common invariant translate; Theorem 4 bounds multiplier-group order by \(q+1\), with the \(q=4\) exception. Theorem 5(2) is the quadratic-nonresidue obstruction for nonsquare \(q\). Theorems 6-8 state square descent, the even-order restriction, and the 3-divisibility restriction. The published finite verification concerns difference-set **order** \(q\), not B4's cardinality \(n=q+1\).
- **Baumert-Gordon (2003/2004).** Leonard D. Baumert and Daniel M. Gordon, *On the existence of cyclic difference sets with small parameters*, [arXiv:math/0304502](https://arxiv.org/abs/math/0304502), [PDF](https://arxiv.org/pdf/math/0304502). The abstract explicitly reports no cyclic planes at non-prime-power orders through \(2\cdot10^9\). This supersedes the smaller cyclic range one might infer from the official 2020 notes.
- **Gordon (online 2020; issue 2022).** *On difference sets with small lambda*, Journal of Algebraic Combinatorics 55, 109-115, [publisher DOI](https://doi.org/10.1007/s10801-020-00992-x), [arXiv:2007.07292](https://arxiv.org/abs/2007.07292), [full preprint](https://arxiv.org/pdf/2007.07292). Publisher confirms online publication 2020-11-21 and February 2022 issue. Abstract reports PPC through order \(2\cdot10^{10}\); section 3 and Table 2 were checked. We safely state the verified cyclic consequence for \(2\le q<2\cdot10^{10}\), hence \(3\le n\le2\cdot10^{10}\), since the table labels its bound by \(k=q+1\). Theorem 3 is the Arasu orbit-count inequality used in residual_orders.py; Theorem 4 gives the cyclic multiplier bound with exceptional parameters \((21,5,1)\). No claim that our code reran this enormous search is made.
- **Peluse (2021; preprint v2 2023).** Sarah Peluse, *An asymptotic version of the prime power conjecture for perfect difference sets*, Math. Ann. 380, 1387-1425, [arXiv:2003.04929](https://arxiv.org/abs/2003.04929), [PDF](https://arxiv.org/pdf/2003.04929). Theorem 1.2 counts admissible cyclic orders up to \(N\) asymptotically as \(N/\log N\); this does not exclude every exceptional order. Theorem 2.1 restates Mann's quadratic-residue condition when the order is not a square. The multiplier explanation in section 2 was checked. The introduction's two-billion citation is an older lower bound, not evidence that Gordon's later twenty-billion result is wrong.
- **Alexeev-Mixon (2025; v2 2026).** Boris Alexeev and Dustin G. Mixon, *Forbidden Sidon subsets of perfect difference sets, featuring a human-assisted proof*, [arXiv:2510.19804v2](https://arxiv.org/abs/2510.19804v2), [PDF](https://arxiv.org/pdf/2510.19804v2). Section 4, pp. 6-7, distinguishes arbitrary planes, cyclic planes, and Desarguesian cyclic planes and treats the cyclic PPC as conjectural. Its Sidon-extension counterexamples resolve a different question; they do not classify taut integers. Its smaller stated computational lower bound is not used as a best-known claim.
- **Bruck-Ryser (1949).** R. H. Bruck and H. J. Ryser, *The nonexistence of certain finite projective planes*, Canadian Journal of Mathematics 1, 88-93, [DOI](https://doi.org/10.4153/CJM-1949-009-2), [publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/2A2E0D91C8E872232A01C7519F14D705/S0008414X00028686a.pdf/the-nonexistence-of-certain-finite-projective-planes.pdf). Theorem 1 was checked: if \(q\equiv1,2\pmod4\), an odd valuation at a prime \(3\pmod4\) excludes a plane. It is a necessary condition only and applies to tautness through the plane construction for \(q\ge2\).
- **Jungnickel-Vedder (1984).** *On the geometry of planar difference sets*, European J. Combinatorics 5, 143-148, [publisher record](https://doi.org/10.1016/S0195-6698(84)80028-1). Primary abstract checked for the even-order restriction \(q>4\Rightarrow8\mid q\). Square descent's precise statement was checked in Gordon (1994), Theorem 6, which attributes it to this paper; original full text was not audited here.
- **Wilbrink (1985).** H. A. Wilbrink, *A note on planar difference sets*, JCT A 38, 94-95, [publisher record](https://doi.org/10.1016/0097-3165(85)90028-7). Primary abstract checked: when prime \(p=2\) or 3 divides the abelian-plane order exactly once, the order is \(p\). The \(p=3\) consequence used by the script is also Gordon (1994), Theorem 8.
- **Xiang-Chen (1995).** *On the size of the multiplier groups of cyclic difference sets*, JCT A 69, 168-169, [publisher record](https://doi.org/10.1016/0097-3165(95)90113-2). Primary abstract and bibliographic metadata checked; the exact bound and exception used here are taken from Gordon (2020/2022), Theorem 4. Original proof not audited here.

## Dated search log

All queries below were run 2026-10-16 with the web search tool. Only primary papers/publisher or author pages support mathematical assertions; search discovery pages were not treated as proofs.

| Approx. UTC | Query / action | Outcome and limitation |
|---|---|---|
| 09:25 | `cyclic planar difference sets prime power conjecture 2026 Gordon 2024` | Found Gordon's small-lambda paper and the later cyclic verification. |
| 09:25 | `Singer 1938 theorem finite projective geometry cyclic difference set original paper` | Bibliography confirmed; AMS full-text access blocked. |
| 09:25 | `Daniel Gordon 1994 cyclic planar difference sets prime power conjecture` | Found original EJC paper; retrieved publisher PDF by following its download link. |
| 09:26 | `"cyclic" "prime power conjecture" "2025"` and `"prime power conjecture" "2026" difference sets` | Found Alexeev-Mixon and other related work; no complete PPC solution identified. |
| 09:26 | `Bruck Ryser 1949 nonexistence certain finite projective planes pdf original` | Retrieved primary publisher theorem statement. |
| 09:27 | `"cyclic planar difference" "prime power" "2024" conjecture` and `"prime power conjecture" "2025" "difference sets" Gordon` | No additional complete classification identified. |
| 09:28-09:32 | Opened arXiv papers, Gordon's author publication list, Springer DOI, EJC publisher PDF | Checked scope, dates, parameter conventions and exact theorem hypotheses above. Author-site legacy PDF URLs returned 404; stable arXiv/publisher versions were used. |
| 09:31-09:33 | `"On the geometry of planar difference sets"`, `"A note on planar difference sets"`, and exact multiplier-paper title | Primary publisher abstracts checked; imported full theorem scope cross-checked in Gordon. |

Verification is time-stamped; a search not finding a paper cannot establish nonexistence of a paper.


19 October 2026, 10:11 Brisbane: AR19: classical unit-index/ramification context from Lemmermeyer arXiv1202.5777v1 Section2; quadratic Gauss/orthogonality/Kronecker operative proofs in Reed author-hosted kummer.pdf. Exact read limits, no source-absence/priority claim, and explicit quadratic repair are recorded in the accepted packet.
