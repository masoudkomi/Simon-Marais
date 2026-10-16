# 2021 B4: Rational Casas-Alvero degrees

## Official source and scope

- [Official Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf), page 2.
- [Official solution notes](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-solutions.pdf).
- Inventory checked 2026-10-16. The following is a mathematical normalization; the official PDF is authoritative.
- Current published solution status must be checked separately from the paper's as-issued openness.
- B4 and the part (b) question were checked against the cached official Paper B
  by `pypdf` extraction on 2026-10-16. The part (b) wording asks:
  "For which integers d >= 2 does the conclusion of part (a) hold?"

## Mathematical statement

Let \(p\in\mathbb Q[x]\) have degree \(d\). Suppose that, for each integer \(k\) with \(1\le k\le d-1\), there is \(r_k\in\mathbb Q\) such that
\[
p(r_k)=p^{(k)}(r_k)=0.
\]
The root \(r_k\) is allowed to depend on \(k\).

**Open target, B4(b) only:** determine all \(d\ge2\) for which every such polynomial satisfies \(p(x)=c(ax+b)^d\) for some \(a,b,c\in\mathbb Q\).

Only (b) was designated open.

The conclusion is equivalently a nonzero rational scalar times the d-th power
of a rational linear polynomial. Since deg(p)=d, the scalar and the linear
coefficient are nonzero. Having a nonconstant gcd in Q[x] is a weaker
hypothesis: the common roots need not be rational. These formulations are
not treated as equivalent in the research packet.

## Fidelity checklist

Before claiming a proof, compare every hypothesis, quantifier, domain, convention, boundary case and conclusion with the original PDF. A result for the preliminary part or a restricted domain is not a full solution of the open part.
