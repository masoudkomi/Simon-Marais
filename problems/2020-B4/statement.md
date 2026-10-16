# 2020 B4: Taut integers and cyclic difference sets

## Official source and scope

- [Official Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2020-paper-b_1.pdf), page 2.
- [Official solution notes](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2020-solutions_1.pdf).
- Inventory checked 2026-10-16. The following is a mathematical normalization; the official PDF is authoritative.
- Current published solution status must be checked separately from the paper's as-issued openness.
- Official page 2 was checked by text extraction and visual rendering on 2026-10-16. The displayed normalization below matches B4(b); no preliminary proof is reproduced here.

## Mathematical statement

For an integer \(n\ge2\), take a regular polygon with \(n^2-n+1\) vertices. Call \(n\) taut if a set of \(n\) vertices can be chosen such that all \(\binom n2\) Euclidean pairwise distances are different.

**Open target, B4(b) only:** determine exactly which integers \(n\ge2\) are taut.

Only (b) was designated open.

## Boundary and parameter convention

Write \(q=n-1\), \(k=n=q+1\), and \(v=q^2+q+1\). Difference-set literature calls \(q\), rather than \(n\), the **order**. The case \(n=2\), \(q=1\), is taut: two vertices of a triangle have only one pairwise distance. Under the convention that a prime power is \(p^a\) with \(a\ge1\), the expected classification is therefore

\[
\{2\}\;\cup\;\{p^a+1:p\text{ prime},\ a\ge1\}.
\]

This is a conjectural unrestricted classification, not a result of this project. The official discussion's informal converse needs the \(n=2\) exception under that convention. A nondegenerate projective plane has order at least 2; its equivalence with tautness is applied only when \(n\ge3\).

## Fidelity checklist

Before claiming a proof, compare every hypothesis, quantifier, domain, convention, boundary case and conclusion with the original PDF. A result for the preliminary part or a restricted domain is not a full solution of the open part.
