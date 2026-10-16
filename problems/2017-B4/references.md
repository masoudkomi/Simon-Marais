# 2017 B4 references and published status

Verification date: **2026-10-16**. This is a bounded literature audit, not a proof that no unpublished or unindexed solution exists.

## Official sources

- [Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-2_1.pdf), p. 2, B4. Entire B4 was explicitly open as issued; there is no preliminary part.
- [Official preliminary solution notes](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-solutions-preliminary_1.pdf), p. 12. These identify the intended count with A006245 and give the then-known interval \(0.1887\) to \(0.6571\), citing Felsner–Valtr. They give background, not exact values of the requested rates.
- [Official 2017 problem index](https://www.simonmarais.org/20171.html), checked for a later linked solution document. The listed notes remain titled preliminary.

Read-only local cache hashes:

```text
.cache/official/2017-paper_b.pdf
69d7cf84128c2464d962136ed613808b6c7a7b07122cfba9c06b5adf775e2a68
.cache/official/2017-solutions.pdf
c272a72239ef4c2ccd54df0702140179e0a9b85f5a9028c87d485841eb1a2c12
```

## Primary mathematical literature

1. Fernando Cortés Kühnast, Justin Dallant, Stefan Felsner, Manfred Scheucher, **An Improved Lower Bound on the Number of Pseudoline Arrangements**, SoCG 2024, article 43, [DOI 10.4230/LIPIcs.SoCG.2024.43](https://doi.org/10.4230/LIPIcs.SoCG.2024.43), [published PDF](https://drops.dagstuhl.de/storage/00lipics/lipics-vol293-socg2024/LIPIcs.SoCG.2024.43/LIPIcs.SoCG.2024.43.pdf), [full version arXiv:2402.13107](https://arxiv.org/abs/2402.13107). Published 2024-06-06. Theorem 1: \(B_n\ge 2^{c n^2-O(n\log n)}\) for some \(c>0.2721\). Here \(B_n\) counts simple arrangements of \(n\) pseudolines, with a marked unbounded north-cell, up to orientation-preserving plane homeomorphisms preserving that cell. Page 2 explicitly says equality of liminf and limsup is open. Its Table 1 is the source of the published exact counts through \(n=16\) used in our script. Section 4, Lemma 5 gives a recursive amplification rule. The patch counts are computer assisted; they were not independently rerun in this pass.

2. Justin Dallant, **Improved Bound on the Number of Pseudoline Arrangements via the Zone Theorem**, [arXiv:2502.20909v2](https://arxiv.org/abs/2502.20909v2), [PDF](https://arxiv.org/pdf/2502.20909v2), revised 2025-03-07. Same simple marked arrangement convention, explicitly stated on p. 1. The paper establishes \(c^+<0.6496\); p. 2 still calls existence of the normalized limit open. The upper argument counts cutpaths (ways to insert a new pseudoline) and combines their two directional encodings with the zone theorem, then certifies an optimization bound. A footnote says changing to unmarked/projective arrangements changes only lower-order factors. Version 2 corrects an unnecessary hypothesis in Lemma 3; use v2. The introduction contains an apparent repeated old constant in the historical paragraph, so do not copy that paragraph as a reliable history table. No independent audit of the optimization certificate was performed here.

3. Günter Rote, **NumPSLA — An experimental research tool for pseudoline arrangements and order types**, [arXiv:2503.02336](https://arxiv.org/abs/2503.02336), [PDF](https://arxiv.org/pdf/2503.02336), 2025. Section 2 fixes the x-monotone/marked convention and numbers strands by their order at the left. Appendix E.5 repeats the interval \(0.2721\le c^-\le c^+\le0.6496\), reports counts known through 16, and documents severe variance in random insertion-tree estimates. Appendix F provides an insertion enumerator. This is an independent primary consistency check on the convention and bounds; our small script was written separately and does not copy that implementation.

4. Hugh Denoncourt, Dana C. Ernst, Dustin Story, **On the number of commutation classes of the longest element in the symmetric group**, Open Problem Journal 4 (2016), [arXiv:1602.08328](https://arxiv.org/abs/1602.08328). This is the overview explicitly recommended by the official notes. It gives the equivalent algebraic formulation and references the tiling correspondence. We use it as a dictionary reference, not a current-status authority.

5. Stefan Felsner and Pavel Valtr, **Coding and Counting Arrangements of Pseudolines**, Discrete & Computational Geometry 46(3) (2011), [DOI 10.1007/s00454-011-9366-4](https://doi.org/10.1007/s00454-011-9366-4), [author-hosted PDF](https://page.math.tu-berlin.de/~felsner/Paper/new-pla.pdf). Directly inspected Sections 1 and 4. Section 1 describes zonotopal tilings, local crossing sequences and their equivalence to marked arrangements. Section 4 reproduces MacMahon's product \(PP(i,j,k)\) and the injection \(B_{3m}\ge PP(m,m,m) B_m^3\). Its asymptotic lower coefficient is \(\tfrac34\log_2 3-1\approx0.1887218755\). These are historical, attributed results; the bounds have been improved. Our rational product script checks finite values without reproving the product or injection.

6. Günter Rote, **Enumeration and Counting of Pseudoline Arrangements**, Oswinfest, 2026-03-28, [author-hosted slides](https://page.mi.fu-berlin.de/rote/Papers/slides/Oswinfest-2026-Enumeration%2Band%2BCounting%2Bof%2BPseudoline%2BArrangements.pdf). Current-year primary corroboration of the exact table through \(n=16\) and lower-bound lineage. The visible upper-bound slide retains the old \(0.6571\), so it is not used to supersede the 2025 paper.

## Current status supported by this audit

Let \(c^-\) and \(c^+\) denote the official liminf and limsup. The strongest primary bounds located are
\[
0.2721<c^-\le c^+<0.6496.
\]
The strict lower inequality follows from the positive slack in the 2024 theorem, after its \(O(n\log n)\) term vanishes upon division by \(n^2\). These are attributed published results, **not** independently reviewed proofs produced by this project. The exact constants, and even \(c^-=c^+\), remain open in the latest directly inspected research statements. We found no later resolution in the targeted search through the verification date. Do not upgrade that negative search to an unconditional present-day claim.

Queries included `Simon Marais 2017 B4 rhombus tilings limsup liminf solution`, `number of pseudoline arrangements 2025 2026`, `number commutation classes longest element asymptotic limit exists`, `pseudoline arrangements 0.6496 2026`, and `pseudoline arrangements 0.2721 2026`. The 2026 affine higher-Bruhat paper [arXiv:2604.24573](https://arxiv.org/abs/2604.24573) was checked at abstract level as a possible false lead; its abstract concerns poset structure, not this asymptotic enumeration problem.
