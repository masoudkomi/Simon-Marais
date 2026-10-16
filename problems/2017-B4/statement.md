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
The entire B4 was designated open. There is no separately stated preliminary part.

The paper does not separately specify quotienting by rotations/reflections. The official notes resolve the intended convention by giving \(C(3)=2\), \(C(4)=8\), and identifying OEIS A006245: tilings in a fixed polygon, with their orientations distinguished. In particular, the two tilings of the regular hexagon are counted separately. Do not use unmarked/unoriented arrangement counts, count reduced words before the commutation quotient, or count arbitrary insertion histories as \(C(n)\).

The standard dictionary uses rhombus tilings of the zonogon and simple marked pseudoline arrangements. The official notes explicitly make this identification; this first pass relies on that published identification rather than supplying a new geometric proof covering every possible interpretation of the word “tiling.”

Verified against Paper B, p. 2, lines B4, and official notes p. 12 on 2026-10-16. Cached official-file SHA-256 values are recorded in references.md.

## Fidelity checklist

Before claiming a proof, compare every hypothesis, quantifier, domain, convention, boundary case and conclusion with the original PDF. A result for the preliminary part or a restricted domain is not a full solution of the open part.
