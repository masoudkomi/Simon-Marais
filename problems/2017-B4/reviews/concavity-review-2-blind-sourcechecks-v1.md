# Blind source checks for concavity review 2

Verified 2026-10-16 UTC / 2026-10-17 Brisbane. Source material was inspected
independently of all peer review reports. No new full third-party paper was
added to tracked files. The original sources below were already cached in
ignored `.cache/`; hashes were recomputed. Only review-prefix documents
and calculation artifacts were authored.

## Dallant v2: primary class bound and domain

Justin Dallant, *Improved Bound on the Number of Pseudoline Arrangements via
the Zone Theorem*, [arXiv:2502.20909v2](https://arxiv.org/abs/2502.20909v2),
[original PDF](https://arxiv.org/pdf/2502.20909v2), revised 2025-03-07.

Cache:
`.cache/literature/deep-literature-r2/2017-dallant-zone-2502.20909v2.pdf`.
SHA-256:
`9ae4886f8b1fce91c6ae8e86c577c5690d0f2ef10355a6524235f95a18dfa03b`.

Checks:

* p. 1: simple Euclidean pseudoline arrangements, a distinguished unbounded
  north cell, orientation-preserving plane homeomorphisms preserving the
  mark. This agrees with the count used in the candidate.
* pp. 3-4: all exits and six path parameters have the meanings used in the
  candidate. Rotation reverses a path for encoding; it does not identify
  tilings modulo rotation.
* p. 5, Lemma 3: \(k\le m\) and \(k\le n-U\) suffice. The older extra
  condition \(n-U\le m\) has been removed in v2. The arXiv version record
  expressly identifies this correction. The independent tree argument in
  the report also checks it without relying on a path-independent set of
  all available middle colors.
* p. 5, Theorem 4 and Lemma 5: the imported zone complexity bound leads to
  the required visited-cell incidence bound in the nontrivial size range.
  Counting below and above gives the candidate's necessary zone inequality.
  Discarding its negative additive constant enlarges the domain safely.
  The small \(n=1\) wording exception is explicitly logged as CR2-01.
* pp. 5-6, Lemma 6: both directional class bounds and all integer
  constraints match. The reviewer uses \((n+1)^6\), avoiding ambiguity
  about whether the paper's \(\mathbb N\) includes zero.
* p. 6, Lemma 7 and program P: the entropy relaxation matches exactly.
  The reviewer independently derived the binomial bound and treated the
  zero denominator separately. The branch-and-bound LP implementation on
  later pages is not required by this candidate and was not used as a
  proof certificate.
* p. 3, Section 2: the marked insertion recurrence is explicitly imported.

The zone theorem itself is an attributed external input; this review
audits its application and Dallant's stated hypotheses, and does not claim
to reprove the tight zone theorem. Its leading constant is not changed by
the proposed concavity proof. The reconstructed new contribution is the
analytic bound on Dallant's necessary entropy domain.

## Felsner--Valtr: dictionary, labeling, insertion and encoding

Stefan Felsner and Pavel Valtr, *Coding and Counting Arrangements of
Pseudolines*, Discrete & Computational Geometry 46 (2011), 405-416,
[DOI](https://doi.org/10.1007/s00454-011-9366-4),
[author-hosted PDF](https://page.math.tu-berlin.de/~felsner/Paper/new-pla.pdf).

Existing cache:
`.cache/literature/2017/cited-7f7251133b0c4ebc.pdf`.
SHA-256:
`9f68329a62318b355cde668eabb9a05073ce755becfdd81dc5a6a15f9db68c26`.
This was identified by its actual title/text, rather than by filename.
The web PDF and cache were cross-checked at the relevant displayed text.

Checks:

* pp. 1-2: the north mark induces orientations on the curves; marked
  isomorphisms preserve these. With the mark fixed, this is consistent
  with the plane orientation convention made explicit by Dallant.
* p. 2: the lines are labeled canonically from a boundary traversal. The
  fixed cyclic order and chosen orientation do not introduce \(n!\)
  arbitrary labelings.
* pp. 2-3, Section 1: regular \(2n\)-gon with fixed clockwise vertex order
  and distinguished highest vertex; prescribed rhombus directions; the
  tiling is a normalized drawing of the dual of a simple marked
  arrangement. Individual tilings are not taken modulo a polygon symmetry.
* pp. 3-4, equation (1): deleting canonical line \(n+1\) and recording one
  cutpath gives the stated recurrence. No collection of all insertion
  histories is substituted for the arrangement count.
* pp. 5-10, Sections 2-3: middle-once encoding and the refined red/blue
  tree mechanism provide the source context for Dallant Lemma 3. The report
  gives its own leaf-count induction, using at most one blue successor and
  allowing empty blocks. This resolves the pruned-tree wording caution
  CR2-02 and verifies the \(m<n-U\) case.

I do not rely on this older paper's assertion of a single limiting
constant, nor on its Maple maximum or numerical upper-bound rounding.

## Official 2017 B4

[Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-2_1.pdf),
p. 2, B4;
[official preliminary notes](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-solutions-preliminary_1.pdf),
p. 12, B4 only.

Cache/hash pairs:

```text
.cache/official/2017-paper_b.pdf
69d7cf84128c2464d962136ed613808b6c7a7b07122cfba9c06b5adf775e2a68
.cache/official/2017-solutions.pdf
c272a72239ef4c2ccd54df0702140179e0a9b85f5a9028c87d485841eb1a2c12
```

The problem's domains are integers \(n\ge2\), regular polygons with
\(2n\) unit sides, and unit-sided quadrilateral tiles. It asks for both
liminf and limsup of \(n^{-2}\log_2 C(n)\). The notes identify A006245,
give \(1,1,2,8,\ldots\), and refer directly to Felsner--Valtr. This is
the official evidence for the intended tiling convention. C1 is progress
on the upper rate only and does not claim to answer both requested limits.
No other annual problem was investigated in this review.

## Extraction and visual checks

The bundled Python 3 runtime with `pypdf` was used read-only for actual
PDF extraction; existing extracted Dallant text was also read and then
cross-checked against the PDF. No mathematical claim rests solely on an
OCR artifact. The bundled Poppler renderer generated temporary PNGs under
`/private/tmp/concavity-review-2-*`; viewed pages were Dallant 5-6,
Felsner--Valtr 2-3, and official notes 12. These confirmed the displayed
formulas, subscripts, inequalities, polygon orientation, and source labels.

Representative command, with page range adjusted for the other sources:

```text
/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm -f 5 -l 6 -scale-to 1600 -png .cache/literature/deep-literature-r2/2017-dallant-zone-2502.20909v2.pdf /private/tmp/concavity-review-2-dallant
```

The exact arithmetic calculation has no dependencies beyond Python's
standard library and reads no constructor script or data. Its complete
run command, timeout, PID, incremental checkpoints and exit/reaping
record are preserved alongside the report. No literature originality
claim or unbounded current-status search is included.
