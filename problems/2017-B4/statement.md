# 2017 B4: Rhombus tiling growth

## Official source and scope

- [Official Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-2_1.pdf), page 2.
- [Official solution notes](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-solutions-preliminary_1.pdf).
- Inventory checked 2026-10-16. The following is a mathematical normalization; the official PDF is authoritative.
- Current published solution status must be checked separately from the paper's as-issued openness.

## Mathematical statement

For each integer \(n\ge2\), let \(C(n)\) be the number of tilings of a regular \(2n\)-gon with side length 1 using quadrilaterals whose four sides all have length 1. Determine both
\[
\liminf_{n\to\infty}\frac{\log_2 C(n)}{n^2}
\quad\text{and}\quad
\limsup_{n\to\infty}\frac{\log_2 C(n)}{n^2}.
\]
The entire B4 was designated open. The paper does not separately specify quotienting tilings by rotations/reflections; verify the intended fixed-polygon counting convention against the official notes.

## Fidelity checklist

Before claiming a proof, compare every hypothesis, quantifier, domain, convention, boundary case and conclusion with the original PDF. A result for the preliminary part or a restricted domain is not a full solution of the open part.
