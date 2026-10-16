# 2023 B4 references and published status

## Official starting sources

- [Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2023_paper_b.pdf), B4 on page 2.
- [Official solutions](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2023solutions.pdf).

Official solutions (pp. 14-16) solve (a), yielding a=b. For (b) they additionally exhibit (1,2) and (2,1), and reduce any further possibilities to opposite-parity exponents both greater than 1. This is not a complete solution of (b).

## Primary-source audit, 2026-10-16

- [Current official 2023 download index](https://www.simonmarais.org/20231.html), reached from the current official home page. It still links the Paper B and solution-note PDFs above. This checks source provenance; it is not a statement that no later solution exists elsewhere.
- Michael Giudici and Anthony Henderson, **The 2023 Simon Marais Mathematics Competition**, *Gazette of the Australian Mathematical Society* 51(2), May 2024, pp. 97–99, especially p. 98. [Primary issue PDF](https://austms.org.au/wp-content/uploads/2025/02/May24-512.pdf), [issue landing page](https://austms.org.au/publications/gazette/gazette512/). The report treats this B4(b) as open and describes partial contestant progress. The indexed PDF text was accessible through search; opening the whole PDF through the web reader failed because its 11,384,008-byte content exceeded that reader's limit, and the landing page was not accessible through that reader. This is dated primary evidence of status in May 2024, not proof of status in October 2026.
- [Forretrio, Simon Marais 23B4 revisited + comments on official solution](https://www.forretrio.com/2023/11/), post dated 18 November 2023. The author's own text explicitly admits a gap. Treat it only as a failed-approach lead. In particular its unrestricted multiple-lifting assertion does not preserve negative real witnesses through even roots, and its small-index discussion does not establish an unrestricted exponent bound. The article also overlaps small-exponent trace/recurrence ideas, so the coordinator's restricted draft is not claimed as novel. Search-indexed text was available; a later direct web-reader open returned a cache miss.
- [AoPS 2023 contest printable collection](https://artofproblemsolving.com/downloads/printable_post_collections/3630984) was located, but the printable collection contains statements rather than an additional B4(b) proof. No other competition problem in it was investigated.

Targeted searches on 2026-10-16 included the exact queries:

    "Simon Marais" "2023" "B4" solution
    "2023" "B4" "sqrt" "rational" Marais
    "Marais" "rational" "nonsquare" "2023"
    "Marais" "rational" "non-square" "B4"
    "Simon Marais 23B4"
    "r^a" "r^b" "sqrt{n}" "Marais"
    "2023" "B4" site:simonmarais.org open
    "Simon Marais" "2023" "B4" resultant
    "Simon Marais" "2023" "B4" solved
    "The 2023 Simon Marais Mathematics Competition" "Gazette"

Some queries were repeated with source exclusions to reduce contest-paper mirrors. Results supplied official material, the diary and the Gazette report. No complete published classification was located in this bounded search. **Current absence of a published solution has not been established.** Do not claim novelty from these search results.

## Theorem inputs of candidate v0.1

The candidate supplies its own proof of the coprime-index Lucas resultant. It uses only standard Sylvester-resultant identities (integral coefficients, vanishing at a common finite root, scaling, multiplicativity, and evaluation against a linear factor), with the relevant degrees and specialization issues stated in the proof. No primitive-divisor theorem is cited or applied. The computations use SymPy 1.14.0 as evidence and are independently checked against direct Sylvester determinants in eight numeric instances, up to a sign that has no mathematical effect on the proof.
