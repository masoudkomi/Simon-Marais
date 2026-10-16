# 2021 B4 proof register

No candidate full solution has been proposed. The lemmas below are a research
reduction, not a classification of degrees.

Every future proof begins as **candidate proof - unverified**. Distinguish published reproductions from original results. Do not relabel until two independent adversarial audits, a reconstruction and all repairs are complete.

## Accepted rational-witness restriction in degree p+1

**Proved, independently reviewed (partial result).** In the attributed p+1
normalization of a hypothetical nontrivial rational-witness polynomial,
with odd prime p, double root at0 and simple center at1, the first nonzero
coefficient c_m at0 must satisfy v_p(c_m)>=2. The residual-factor
Eisenstein argument uses the published two-recycled-root obstruction;
it does not assume all roots rational. Both fresh blind reviewers
reconstructed all inputs and the proof. The exact degree20 necessary
filter has6680 congruence patterns,3043 excluded,3637 remaining.
These counts do not solve degree20. See [accepted proof](notes/rational-witness-p-plus-one-reviewed-v1.2.md)
and [acceptance](reviews/witness-acceptance.md). Novelty is unestablished.
The later Newton packet, original reductions below, and source objections
remain outside this acceptance.

## V1, 2026-10-16: integral witnesses and a local obstruction

Status: **candidate proof - unverified**. Author: 2021 research owner. The
normalization is elementary and related to the official solution's
normalization; novelty is not claimed. Two independent adversarial audits,
including reconstruction, are requested through the coordinator.

Write H_k(f)=f^(k)/k! over Q, equivalently
H_k(sum c_j x^j)=sum_(j>=k) binom(j,k)c_j x^(j-k).

**Lemma 1 (integral normalized witness tuple).** If a nontrivial counterexample
to B4(b) exists in degree d, one exists in the form

    f(x)=x^d + sum_(j=1)^(d-2) c_j x^j in Z[x],

with integer witnesses s_k, s_(d-1)=0, and gcd(s_1,...,s_(d-1))=1.

Proof. Translate the shared root of the linear derivative of order d-1 to zero
and divide by the leading coefficient. This gives a monic rational polynomial
g with g(0)=0 and coefficient of x^(d-1) zero. Its transformed witnesses t_k
are rational. If they are all zero, g(0)=H_1(g)(0)=...=H_(d-1)(g)(0)=0
forces g=x^d, contrary to nontriviality. Otherwise choose a positive integer D
clearing all t_k denominators, let h be the positive gcd of the integers D t_k,
and put lambda=h/D. Then f(x)=lambda^(-d)g(lambda x) has integer witnesses
s_k=t_k/lambda of gcd one, with s_(d-1)=0. Let c_d=1. Descending from k=d-1
to k=1, the equation H_k(f)(s_k)=0 gives

    c_k = -sum_(j=k+1)^d binom(j,k)c_j s_k^(j-k).

Thus all c_k are integers. The constant coefficient is zero because f(0)=0.
Affine changes with nonzero rational slope preserve common-root equalities and
nontriviality. This proves the stated reduction. End candidate proof.

**Lemma 2 (Fp rational-witness obstruction).** Fix d>=2. Suppose for some prime
p every monic F in F_p[x] of degree d, with F(0)=0 and coefficient of x^(d-1)
zero, that has a common F_p-root with every H_k(F), 1<=k<d, equals x^d.
Then B4(b)'s conclusion holds in degree d.

Proof. A rational counterexample would give the polynomial and witnesses of
Lemma 1. Reduction modulo p preserves monicity, degree, zero constant and
x^(d-1) coefficients, and all Hasse evaluations because their coefficients are
integers. By hypothesis its reduction is x^d. But f(s_k)=0 then gives
s_k^d=0 mod p for every k, so p divides every s_k, contrary to their gcd one.
End candidate proof.

This lemma is only a sufficient criterion. It uses F_p-rational shared roots,
not all roots in the algebraic closure. Ordinary formal derivatives must not
replace Hasse derivatives in small characteristic. No prime has been found
that satisfies this criterion in a new degree.

**Lemma 3 (explicit failure of many local tests).** In F_p[x], for
1<=m<=d-2, F=x^d-x^m satisfies the centered common F_p-root conditions if
p divides binom(d,m)-1. It is nontrivial because it has distinct roots 0 and 1.

Proof. At k=m, H_m(F)(1)=binom(d,m)-1. For k!=m, 1<=k<d,
H_k(F)(0)=0, and F(0)=F(1)=0. Its x^(d-1) coefficient is zero by the bound
m<=d-2. End candidate proof.

This is an elementary reproduction of a known bad-prime mechanism, attributed
in Marashdeh's introduction to Schaub-Spivakovsky/de Frutos Marin. It is not a
counterexample over Q. Exact examples for d=20 and 24, p=2,3,5,7,11 are saved
in computations/finite-field-examples.jsonl and directly verified by the script.
