# 2018 B4: Monotone matrix enumeration

## Official source and scope

- [Official Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2018-paper-b_1.pdf), page 2.
- [Official solution notes](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2018-solutions_1.pdf).
- Inventory checked 2026-10-16. The following is a mathematical normalization; the official PDF is authoritative.
- Current published solution status must be checked separately from the paper's as-issued openness.

## Mathematical statement

Let \(m,n\) be positive integers. Let \(A(m,n)\) consist of \(2\times mn\) matrices with entries in \(\{1,\ldots,m\}\), such that:
- every symbol occurs exactly \(2n\) times in the whole matrix;
- each row is weakly increasing;
- \(M_{1j}<M_{2j}\) in each column \(j\).

Determine \(|A(m,n)|\) for all \(m,n\). The general problem was designated open; the known case \(m=5\) was a preliminary target.

## Fidelity checklist

Before claiming a proof, compare every hypothesis, quantifier, domain, convention, boundary case and conclusion with the original PDF. A result for the preliminary part or a restricted domain is not a full solution of the open part.
