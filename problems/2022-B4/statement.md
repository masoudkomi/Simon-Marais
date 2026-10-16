# 2022 B4: Integer recurrence and equality

## Official source and scope

- [Official Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2022-paper-b.pdf), page 2.
- [Official solution notes](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2022-solutions.pdf).
- Inventory checked 2026-10-16. The following is a mathematical normalization; the official PDF is authoritative.
- Current published solution status must be checked separately from the paper's as-issued openness.

## Mathematical statement

Let \(a_0,b_0\) be positive integers with \(a_0b_0\ge600\). For every \(n\ge0\), define
\[
a_{n+1}=a_n+2\left\lfloor\frac{b_n}{20}\right\rfloor,\qquad
b_{n+1}=b_n+3\left\lfloor\frac{a_n}{30}\right\rfloor.
\]

**Open target, B4(b) only:** decide whether there must be an \(n\ge0\) with \(a_n=b_n\).

Only (b) was designated open. Both updates use the old pair \((a_n,b_n)\), not an in-place sequential update.

## Fidelity checklist

Before claiming a proof, compare every hypothesis, quantifier, domain, convention, boundary case and conclusion with the original PDF. A result for the preliminary part or a restricted domain is not a full solution of the open part.
