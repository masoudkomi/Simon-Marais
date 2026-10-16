# 2025 B4: Integer geometric sums that are perfect powers

## Official source and scope

- [Official Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2025_paper_b.pdf), page 2.
- [Official solution notes](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2025solutions.pdf).
- Inventory checked 2026-10-16. The following is a mathematical normalization; the official PDF is authoritative.
- Current published solution status must be checked separately from the paper's as-issued openness.
- The cached Paper B and the part-(b) remark on solution page 20 were read directly with pypdf on 2026-10-16. SHA-256: Paper B `c6d1d0c47c84521da836e766201224c84cae7c481449f28c72df842caa8e2893`; solutions `46872f990326e1a0f484f02ce863b3341178a299622041768f4964a5cafd2e5e`.

## Mathematical statement

**Open target, B4(b) only:** determine all integer quadruples \((x,y,n,q)\), with \(n,q\ge2\), satisfying
\[
x^n+x^{n-1}+\cdots+x+1=y^q.
\]

Only (b) was designated open. The domain includes \(x=-1,0,1\), negative \(x,y\), even and odd \(n,q\). The degree of the sum is \(n\); its number of terms is \(n+1\).

## Indexing audit

The official solution notes' four known nontrivial identities use the number of terms in the exponent slot. Translation to this paper's degree convention is mandatory:

| x | y in the printed identity | Literature term count m | Official degree n=m-1 | q | Exact sum |
|---|---|---|---|---|---|
| 3 | 11 | 5 | 4 | 2 | 121 |
| 7 | 20 | 4 | 3 | 2 | 400 |
| 18 | 7 | 3 | 2 | 3 | 343 |
| -19 | 7 | 3 | 2 | 3 | 343 |

For the two even exponents, the negative values y=-11 and y=-20 give additional signed quadruples. These are attributed known examples, not a new unrestricted classification. No preliminary proof is reproduced.

## Fidelity checklist

Before claiming a proof, compare every hypothesis, quantifier, domain, convention, boundary case and conclusion with the original PDF. A result for the preliminary part or a restricted domain is not a full solution of the open part.
