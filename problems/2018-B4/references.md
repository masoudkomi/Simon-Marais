# 2018 B4 references and published status

Verification date: **2026-10-16**. Only B4 was investigated.

## Official record

- [Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2018-paper-b_1.pdf), page 2. The normalized statement in `statement.md` was verified against its rendered page, including dimensions, strictness and positive-integer quantifiers. The paper explicitly designated the general determination open.
- [Official solutions](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2018-solutions_1.pdf), pp. 16-17. They give \((5n^2+5n+2)/2\) for \(m=5\), relate the problem to torus quotients of Grassmannians, and point to [OEIS A060854](https://oeis.org/A060854) for related combinatorics. That OEIS sequence concerns rectangular standard tableaux, so it is not itself the desired equal-content count.
- [Official 2018 competition page](https://www.simonmarais.org/20181.html) was inspected for a current update. No correction of B4 was located in this bounded search. This is not evidence that no correction exists elsewhere.

## Direct prior formula: Hering and Howard

Milena Hering and Benjamin J. Howard, *The ring of evenly weighted points on the projective line*, **Mathematische Zeitschrift 277** (2014), 691-708, [DOI](https://doi.org/10.1007/s00209-013-1272-4). Primary full text: [author preprint v2](https://arxiv.org/pdf/1211.3941v2), [arXiv record](https://arxiv.org/abs/1211.3941), [accepted manuscript](https://www.pure.ed.ac.uk/ws/files/16949586/The_ring_of_evenly_weighted_points_on_the_projective_line.pdf), [author's publication list](https://webhomes.maths.ed.ac.uk/~mhering/publications.html).

**Proposition 3.2**, preprint pp. 6-7, assumes a positive integral weight vector \(w\) of even total weight. It counts tableaux of shape \((|w|/2,|w|/2)\) and content \(w\), and gives their bounded-composition difference and explicit subset sum.

For B4, set the number of weights to \(m\) and \(w=(2n,\ldots,2n)\). The total weight is \(2mn\), hence even, and the required shape is exactly \((mn,mn)\). A subset of size \(j\) has weight \(2nj\); its allowed condition becomes \(j<m/2\). Grouping equal-sized subsets gives precisely equation (1) of `proof.md`. This establishes direct prior availability for the literal enumeration, with \(m=1,2\) handled separately in the elementary proof. The preprint record dates v2 to 2014-01-19, before the competition. The author list confirms the 2014 journal publication.

## Equal-weight formula: Ottaviani and attribution to Howe

Giorgio Ottaviani, *Five Lectures on Projective Invariants*, **Rendiconti del Seminario Matematico 71** (2013), 119-194. Primary [journal PDF](https://seminariomatematico.polito.it/rendiconti/71-1/119.pdf), [author preprint](https://arxiv.org/abs/1305.2749), [university publication record](https://flore.unifi.it/handle/2158/1038825).

**Theorem 40**, journal p. 186 (PDF page 68), gives the equal-weight invariant dimension as
\[
\sum_{j=0}^{\lfloor(d-1)/2\rfloor}(-1)^j\binom dj
\binom{k(d/2-j)+d-2-j}{d-2}.
\]
Its parity convention requires even \(k\) when \(d\) is odd; \(d=m,k=2n\) meets that requirement for all B4 parameters. The theorem attributes the result to Roger Howe, *The classical groups and invariants of binary forms*, Proc. Sympos. Pure Math. **48** (1988), 133-166, section 5.4.2.3. Howe's original text has **not** been inspected here; that earlier attribution is reported through the verified Ottaviani source, not claimed as independently verified.

## Other primary cross-checks

- Christopher J. Brooks, Abraham Martin del Campo and Frank Sottile, *Galois groups of Schubert problems of lines are at least alternating*, [arXiv:1207.4280](https://arxiv.org/abs/1207.4280), [PDF](https://arxiv.org/pdf/1207.4280), section 3.3, equation (3.2): an integral expression for two-row Kostka counts as trivial-representation multiplicities. This supports the representation-theoretic route, not a new counting theorem here.
- Thomas L. Curtright, Thomas S. Van Kortryk and Cosmas K. Zachos, *Spin multiplicities*, [arXiv:1607.05849](https://arxiv.org/abs/1607.05849), [PDF](https://arxiv.org/pdf/1607.05849), equations (10)-(11) and singlet table. Set their number of factors to \(m\), their spin to B4's \(n\), and their final spin to 0. Their table for factor counts 1-10 agrees with the table produced independently in `computations/exact_count-output.txt`.

## Status interpretation and limits

The known subset/binomial formulas directly answer the literal general cardinality request. The candidate is therefore a **published-result reproduction**, not a claimed new solution of a still-open research problem. It remains unreviewed in this repository. The reason the 2018 competition designated this exact formulation open has not been established. A desired stronger form, such as manifest positivity of polynomial coefficients, would be an additional question absent from its wording; it must not be substituted silently.

Representative search queries: `"Simon Marais" "2018" "B4" solution matrices`; `"Simon Marais" "Kostka"`; `"Kostka" "mn" "2n" "formula"`; `"tensor product" "SU(2)" "multiplicities" "explicit formula"`; `"Hilbert function" "invariants" "points on" "line" binomial formula`; `"The ring of evenly weighted points on the projective line"`; `"2018" "B4" "Howe" Marais`; `"Simon Marais" "Hering"`; `"Simon Marais" "Ottaviani"`. Search results were used for discovery; theorem claims above rely on the primary texts actually inspected. No absence-of-literature conclusion is drawn.
