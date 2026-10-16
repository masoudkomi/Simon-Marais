# 2018 B4: Monotone matrix enumeration

## Official source and scope

- [Official Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2018-paper-b_1.pdf), page 2.
- [Official solution notes](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2018-solutions_1.pdf).
- Inventory and full B4 text checked 2026-10-16, including visual inspection of page 2 rendered from the cached official PDF. The following is a mathematical normalization; the official PDF is authoritative.
- Current published solution status must be checked separately from the paper's as-issued openness.

## Mathematical statement

Let \(m,n\) be positive integers. Let \(A(m,n)\) consist of \(2\times mn\) matrices with entries in \(\{1,\ldots,m\}\), such that:
- every symbol occurs exactly \(2n\) times in the whole matrix;
- each row is weakly increasing;
- \(M_{1j}<M_{2j}\) in each column \(j\).

Determine \(|A(m,n)|\) for all \(m,n\). The general problem was designated open; the known case \(m=5\) was a preliminary target. The current authorized research target is only the general open portion. The known \(m=5\) expression is used only as a comparison.

The paper literally asks for the cardinality and gives no further requirement such as a product formula, a sum without alternating signs, a polynomial with manifestly positive coefficients, or a fixed number of terms independent of both parameters. Its open label is therefore in tension with a published general binomial-sum formula; see `references.md`. Do not silently impose an additional requirement or claim a novel solution.

## Exact source checks

- Cached paper: `.cache/official/2018-paper_b.pdf`; SHA-256 `fa26d31d056dfcb5f782209c20ee0c59f20717cdc48ef195c2099582037aa704`.
- Cached solutions: `.cache/official/2018-solutions.pdf`; SHA-256 `b19562352d09bf6fbb43974339b82c2a59c0d2276eb69f357a752772ce0f83cb`.
- The dimensions are visually confirmed to be \(2\times mn\), not \(2n\times m\) or any other shape. Both parameters are positive integers. The strict inequality is down columns; rows are weakly increasing. Every one of the \(m\) symbols occurs exactly \(2n\) times. There is no hidden restriction \(m\ge3\).
- `computations/official-statement.png` preserves the rendered page. No other problem on that page was investigated.

## Fidelity checklist

Before claiming a proof, compare every hypothesis, quantifier, domain, convention, boundary case and conclusion with the original PDF. A result for the preliminary part or a restricted domain is not a full solution of the open part.
