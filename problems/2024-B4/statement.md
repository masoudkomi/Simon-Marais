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

## Fidelity check, 2026-10-16

The cached official Paper B, page 2, was text-extracted and visually inspected. The normalization above matches part (b), including positive odd n, integer polynomials, and the definition of constant modulo 2. No change of domain to polynomial functions is permitted.

For n=1 the numerator is the zero polynomial. Zero is constant modulo 2; moreover the polynomial ring over F2 is an integral domain, so the prescribed product cannot be zero when both g and h are nonconstant. Thus n=1 is excluded. For n=3 the quotient by the three prescribed linear factors is 1, so n=3 is also excluded. These elementary boundary deductions are recorded as candidate proof - unverified until the required independent audits.

For odd n>=3, write phi_n=f_n/((x+y)(y+z)(z+x)) in F2[x,y,z]. The target is precisely a product of two nonconstant polynomials over F2. An F2 factorization lifts coefficientwise to integer polynomials. For n>=5 this is the usual reducibility question for the nonzero homogeneous polynomial phi_n of degree n-3. Neither a factorization only over an extension field nor an APN classification suffices.

## Fidelity checklist

Before claiming a proof, compare every hypothesis, quantifier, domain, convention, boundary case and conclusion with the original PDF. A result for the preliminary part or a restricted domain is not a full solution of the open part.
