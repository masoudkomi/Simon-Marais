# 2024 B4: Polynomial factorization modulo two

## Official source and scope

- [Official Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf), page 2.
- [Official solution notes](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc_2024_solutions.pdf).
- Inventory checked 2026-10-16. The following is a mathematical normalization; the official PDF is authoritative.
- Current published solution status must be checked separately from the paper's as-issued openness.

## Mathematical statement

For odd positive integers \(n\), define
\[
f_n(x,y,z)=x^n+y^n+z^n+(x+y+z)^n.
\]
**Open target, B4(b) only:** determine all odd positive integers \(n\) for which
\[
f_n\equiv(x+y)(y+z)(z+x)\,g\,h\pmod2
\]
with \(g,h\in\mathbb Z[x,y,z]\), both nonconstant modulo 2.

Only (b) was designated open. Congruence means coefficientwise congruence, not equality of the induced functions on \(\mathbb F_2^3\). A polynomial is constant modulo 2 when congruent to a constant polynomial. Check \(n=1\) and the zero-polynomial convention explicitly.

## Fidelity checklist

Before claiming a proof, compare every hypothesis, quantifier, domain, convention, boundary case and conclusion with the original PDF. A result for the preliminary part or a restricted domain is not a full solution of the open part.
