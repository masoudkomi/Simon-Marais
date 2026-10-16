# Deeper literature and prior-method attribution for 2023 B4(b)

2026-10-16 UTC. Literature checkpoint; no change to the already reviewed
classification or its frozen proof. Novelty remains unestablished. Only
part (b), with real witnesses of either sign, is investigated.

## Exact problem and historical evidence

The [official statement](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2023_paper_b.pdf)
and [official notes](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2023solutions.pdf)
are the controlling sources. The project has an independently reviewed
classification: diagonal pairs (k,k), and (k,2k)/(2k,k) for odd positive k.
The proof explicitly supplies the unrestricted resultant obstruction rather
than assuming an exponent search cutoff. Its novelty was not established
by the mathematical reviews.

The full Giudici–Henderson organizer report, Gazette 51(2), May2024,
printed pp97–99, was read from the normally downloaded
[primary issue PDF](https://austms.org.au/wp-content/uploads/2024/06/512.pdf).
It corroborates the historical open designation and partial contestant
progress. This supersedes the earlier access limitation in references.md:
the full issue is now cached locally. It neither gives an individual B4
setter credit nor proves the absence of a later solution.

The author-posted [Forretrio November2023 discussion](https://www.forretrio.com/2023/11/)
explicitly acknowledges a gap. Its recurrence ideas are relevant prior
approach evidence, not a valid complete proof. The real negative-witness
domain prevents unrestricted lifting through even roots. No inference of
novelty follows from finding only incomplete public attempts.

## Generalized Fibonacci resultants: important method prior art

Flórez, Higuita and Ramírez, *The resultant, the discriminant, and the
derivative of generalized Fibonacci polynomials*, Journal of Integer
Sequences22 (2019), Article19.4.4,
[original journal PDF](https://cs.uwaterloo.ca/journals/JIS/VOL22/Florez/florez23.pdf),
also [arXiv:1808.01264](https://arxiv.org/abs/1808.01264). The full28-page
paper is cached; Theorem1, the global hypotheses at §3.1, its proof in §4,
and the reference chain were read. The family F0=0,F1=1,
F_n=dF_(n−1)+gF_(n−2) includes the recurrence used in our proof.
Crucially, the paper assumes gcd(d,g)=1 and deg(g)<deg(d). Directly
eliminating P with d=D constant and g=P fails the degree hypothesis.
The authors themselves separate the opposite degree range in their closing
discussion. Thus Theorem1 is not directly imported for that specialization.
This is a scope limitation, not an objection to their theorem.

The paper nevertheless supplies clear prior art for the resultant method
and the coprime-index phenomenon. A reciprocal-variable transformation
could connect a standard Fibonacci specialization to our unit-resultant
lemma, but it would require explicit degree and leading-coefficient
bookkeeping. The project's existing self-contained roots-of-unity proof
already provides that lemma without importing an unchecked specialization.
It should be described as a proved instance of an established method,
rather than as an invention of generalized-Fibonacci resultants.

Stéphane R. Louboutin, *Resultants of Chebyshev Polynomials: A Short Proof*,
Canadian Mathematical Bulletin56(3) (2013),602–605,
[original full PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/307773230FE1D9B72A312B7B4EEB6BB0/S0008439500003593a.pdf/resultants-of-chebyshev-polynomials-a-short-proof.pdf),
[DOI10.4153/CMB-2012-002-1](https://doi.org/10.4153/CMB-2012-002-1), published
electronically in2012. All four pages were read. Lemma2 uses cyclotomic
associates to calculate resultants, and Theorem4 gives the second-kind
coprime-index resultant. This is close prior art for the roots-of-unity
product technique in our lemma. Its cited antecedent is Jacobs, Rayes and
Trevisan, CMB54 (2011),288–296; its cyclotomic chain includes Apostol1970
and Louboutin1997. These antecedents were located bibliographically, not
independently read in full here. No theorem from them is silently imported.

This source comparison supports attribution of the mechanism. It does not
show that the contest's entire signed exponent classification, especially
the weighted elimination and denominator contradiction, already appears in
either paper. No such exact match was located in this bounded search.

## Nearby finiteness results do not replace the needed exclusion

Dujella and Tichy, *Diophantine equations for second order recursive
sequences of polynomials*,
[author-posted13-page manuscript](https://web.math.pmf.unizg.hr/~duje/pdf/dutichy.pdf),
was found by following the recursive-polynomial literature. The introduction,
Theorems1–2 and the definitions in §2 were read. With a fixed nonzero
integer B, G_(n+1)(x)=xG_n(x)+BG_(n−1)(x). Theorem2 gives finiteness of
integer solutions of G_n(x)=G_m(y), for fixed distinct m,n>=3; the quoted
Bilu–Tichy criterion concerns rational solutions with a bounded denominator.
These conclusions do not assert emptiness, bound all varying exponent pairs,
or supply an unrestricted denominator bound for the contest's rational D,P.
The full proof of this finiteness theorem was not reconstructed in this pass.

The exact mismatch matters: our contradiction uses N integral and a rational
trace D=p/q with 0<D<1, then proves q^(2o) divides a specific nonzero integer
before applying a real inequality. Replacing that denominator argument by
fixed-index finiteness would leave the central gap. Likewise a primitive
divisor theorem for integral Lucas/Lehmer parameters needs its integrality
hypotheses checked before use; none is needed by the accepted proof.

## Search record, source limits, and next mathematical action

In addition to the earlier exact contest queries in references.md, this
pass searched the exact contest/year/B4 with “solved”, “resultant”, and
later dates; powers with a shared irrational coefficient in quadratic
fields; coprime-index generalized-Fibonacci resultants; and rational
solutions of equal recursive polynomials. Technical conclusions above use
primary author or journal sources. Search snippets led to sources, not to
new unrestricted theorem claims.

The important next action is a careful exposition and novelty comparison of
the already reviewed classification, with the established resultant method
properly attributed. More low-exponent searches would not improve its
unrestricted proof. The individual contest proposer remains unknown; report
authorship, the2026 committee roster, and topic resemblance are insufficient.
No one was contacted. Source hashes, retrieval/read scope and queries are
saved in the companion manifest. Full PDFs remain in ignored local cache;
no charge or access bypass occurred.
