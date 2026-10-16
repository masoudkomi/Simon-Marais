# A resultant obstruction for the remaining exponent pairs

**proved, independently reviewed**, version 1.0, 2026-10-16.

Constructed by the 2023 B4(b) research owner. The coordinator accepted this argument after two fresh, initially blind adversarial audits, each reconstructing the full proof. No substantive mathematical objection or repair was outstanding. See ../reviews/acceptance.md. Novelty is not established. The frozen constructor draft remains ../notes/candidate-resultant-v0.1.md; this version changes status annotations only.

Requested agent settings: `gpt-6.1-sol`, `max`. No independent effective-setting readback was available to this owner.

## Claimed classification and published input

For every fixed nonsquare positive integer \(N\), the proposed answer to **2023 B4(b) only** is

\[
(a,b)=(k,k)\quad(k\geq1),
\qquad (a,b)=(k,2k)\text{ or }(2k,k)\quad(k\geq1\text{ odd}).
\tag{C}
\]

The official statement allows a real witness of either sign. It does not assume that \(N\) is squarefree. The argument below uses only \(N\in\mathbb Z\), \(N\geq2\), and \(\sqrt N\notin\mathbb Q\).

The following established preliminary facts are used as attributed context, without reproducing the proof of part (a): the [official solution notes](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2023solutions.pdf), B4, pp. 14–16, give the diagonal family; establish that an off-diagonal witness must be negative and the exponents must have opposite parity; and settle the case in which one exponent is 1, with only the off-diagonal possibilities \((1,2),(2,1)\). The new proposed argument is the exclusion of **all remaining coprime even/odd exponent pairs with the odd exponent at least 3**. The published results are not claimed as new work.

## 1. Correct gcd reduction and the real quadratic parameters

Suppose there is an off-diagonal witness. By the published input it is negative and the two exponents have opposite parity. Let \(d=\gcd(a,b)\). Then \(d\) is odd. Put \(x=r^d<0\) and denote the reduced even exponent by \(e\) and the reduced odd exponent by \(o\). Thus

\[
\gcd(e,o)=1,
\quad x^e+\sqrt N\in\mathbb Q,
\quad x^o+\sqrt N\in\mathbb Q.
\tag{1}
\]

The witness is nonzero, since \(\sqrt N\) is irrational. Bézout's identity applied to \(e,o\) therefore implies \(x\in K=\mathbb Q(\sqrt N)\). Let \(x'\) be the nontrivial conjugate. Conjugating (1) gives

\[
(x')^e-x^e=(x')^o-x^o=2\sqrt N.
\tag{2}
\]

The odd-power equality implies \(x'>x\). The even-power equality implies \(|x'|>|x|\). Since \(x<0\), these force \(x'>0\). Set

\[
U=x'>V=-x>0,
\qquad D=U-V=x+x'\in\mathbb Q_{>0},
\qquad P=UV=-xx'\in\mathbb Q_{>0}.
\tag{3}
\]

Then

\[
U^e-V^e=U^o+V^o=2\sqrt N.
\tag{4}
\]

In particular \(U^e>2\sqrt N>1\), so \(U>1\). If \(e<o\), then \(U^e-V^e<U^e<U^o<U^o+V^o\), contradicting (4). Parity excludes equality, so \(e>o\). The published exponent-1 result now handles \(o=1\). Hence assume throughout the exclusion that

\[
e>o\geq3,\qquad e\text{ even},\quad o\text{ odd},\quad\gcd(e,o)=1.
\tag{5}
\]

## 2. Integer recurrence polynomials

Define \(F_j(D,P)\in\mathbb Z[D,P]\) by

\[
F_0=0,\quad F_1=1,\quad F_{j+2}=D F_{j+1}+P F_j.
\tag{6}
\]

The characteristic roots are \(U,-V\), and they are distinct because \(U+V>0\). Thus

\[
F_j(D,P)=\frac{U^j-(-V)^j}{U+V}.
\tag{7}
\]

Consequently (4) implies

\[
F_e=F_o,
\qquad (D^2+4P)F_o^2=4N.
\tag{8}
\]

All \(F_j(D,P)\) for \(j\geq1\) are positive at (3). If \(D\geq1\), then \(F_{j+1}=D F_j+P F_{j-1}>F_j\) for \(j\geq2\). Since \(e>o\geq3\), this contradicts \(F_e=F_o\). Therefore

\[
0<D<1.
\tag{9}
\]

Write \(D=p/q\) in lowest terms, where \(0<p<q\) and \(q\geq2\).

Each monomial of \(F_j\) has weight \(j-1\) under \(\operatorname{wt}(D)=1,\operatorname{wt}(P)=2\). Also

\[
\deg_P F_e=(e-2)/2=:d_e,
\quad\deg_P F_o=(o-1)/2=:d_o;
\]

the leading coefficients are \((e/2)D\) and 1 respectively. These statements follow directly by induction from (6), or from

\[
F_j(D,P)=\sum_{k=0}^{\lfloor(j-1)/2\rfloor}
\binom{j-1-k}{k}D^{j-1-2k}P^k.
\tag{10}
\]

## 3. A unit resultant for coprime indices

We claim that, up to an overall sign,

\[
\operatorname{Res}_P(F_e(D,P),F_o(D,P))
=\pm D^{(e-1)(o-1)/2}.
\tag{11}
\]

Here and below the resultant can be defined as the Sylvester determinant. Its sign will never matter.

First put \(D=1\). For each nontrivial \(o\)-th root of unity \(\zeta\), the number

\[
P_\zeta=-\frac{\zeta}{(1+\zeta)^2}
\]

is a root of \(F_o(1,P)\), by taking characteristic roots \(\zeta/(1+\zeta)\) and \(1/(1+\zeta)\). The denominator is nonzero because \(o\) is odd. Exactly \(\zeta,\zeta^{-1}\) give each such \(P_\zeta\): rearranging its defining equation gives a quadratic in \(\zeta\) with those two roots. Since \(o\) is odd, no nontrivial \(\zeta\) is self-inverse. There are therefore exactly \(d_o\) distinct roots, exhausting the roots of the monic polynomial \(F_o(1,P)\).

At such a root,

\[
F_e(1,P_\zeta)=
\frac{\zeta^e-1}{(\zeta-1)(1+\zeta)^{e-1}}.
\tag{12}
\]

The map \(\zeta\mapsto\zeta^e\) permutes the nontrivial \(o\)-th roots, since \(\gcd(e,o)=1\). Moreover \(\prod_{\zeta\ne1}(1+\zeta)=1\), by evaluating \((T^o-1)/(T-1)\) at \(T=-1\). Thus the product of (12) over **all** nontrivial \(o\)-th roots is 1. Each distinct \(P_\zeta\) occurs twice, so the product over the \(d_o\) distinct roots has square 1. Because \(F_o(1,P)\) is monic, its resultant with \(F_e(1,P)\) is \(\pm1\).

Finally substitute \(P=D^2Z\) and use \(F_j(D,D^2Z)=D^{j-1}F_j(1,Z)\). The resultant scaling rules give the power \((e-1)(o-1)/2\) in (11). This can first be calculated for nonzero indeterminate \(D\); both sides are polynomials, so it is a polynomial identity. There is no appeal to a primitive-divisor theorem.

## 4. An integer resultant and its weighted degree

Set \(\delta=e-o>0\), \(L=o(e-1)\), and define

\[
A=F_e-F_o,
\quad B=(D^2+4P)F_o^2-4N,
\quad R(D,N)=\operatorname{Res}_P(A,B)\in\mathbb Z[D,N].
\tag{13}
\]

The degrees in \(P\) are \(d_e\) and \(o\) over the rational-function field; their leading coefficients are nonzero polynomials. At an actual solution (8), the polynomials share a finite root \(P\), so

\[
R(D,N)=0.
\tag{14}
\]

The following two polynomial properties are required:

1. Every monomial \(D^iN^j\) of \(R\) satisfies \(i+2oj\leq L\).
2. Up to an overall sign,

\[
R(D,0)=\pm D^{e(o-1)}
\left[\frac e2D^\delta-2^{\delta-1}o\right].
\tag{15}
\]

For property 1, introduce an indeterminate \(t\) and change the elimination variable by \(P=t^2Z\). The usual scaling formulas for the resultant give

\[
R(tD,t^{2o}N)=t^L\operatorname{Res}_Z
\left(F_e(D,Z)-t^{-\delta}F_o(D,Z),
(D^2+4Z)F_o(D,Z)^2-4N\right).
\tag{16}
\]

The resultant on the right is a polynomial in \(t^{-\delta}\) with no positive powers of \(t\). Its coefficients do not depend on \(t\). This proves property 1. Identity (16) is over a Laurent-polynomial field, so the occurrence of negative powers is legitimate; its left side is the original polynomial.

For property 2 use multiplicativity:

\[
R(D,0)=\operatorname{Res}_P(A,D^2+4P)
\operatorname{Res}_P(A,F_o)^2.
\]

The second resultant equals that of \(F_e,F_o\), so (11) makes its square \(D^{(e-1)(o-1)}\). At \(P=-D^2/4\), the two characteristic roots coincide at \(D/2\); the recurrence gives

\[
F_j(D,-D^2/4)=j(D/2)^{j-1}.
\]

Therefore the first resultant, up to sign, is

\[
4^{d_e}A(D,-D^2/4)
=D^{o-1}\left[\frac e2D^\delta-2^{\delta-1}o\right].
\]

Multiplying proves (15). It also proves that \(R\) is a nonzero polynomial. All resultant properties used here follow from the Sylvester determinant/product over roots in characteristic zero; they are applied to polynomials in the indicated elimination variable, with polynomial coefficients, before specializing \(D,N\). No division by a specialized leading coefficient is used in (14).

## 5. The denominator divisibility

Substitute \(D=p/q\) into (14) and multiply by \(q^L\). Property 1 shows that every term involving \(N\) is an integer multiple of \(q^{2o}\), because \(N\in\mathbb Z\). Property 2 then gives

\[
q^{2o}\mid p^{e(o-1)}
\left[\frac e2p^\delta-2^{\delta-1}o q^\delta\right].
\]

Since \(p,q\) are coprime, cancel the factor \(p^{e(o-1)}\):

\[
q^{2o}\mid H:=\frac e2p^\delta-2^{\delta-1}o q^\delta.
\tag{17}
\]

All quantities in (17) are integers, since \(e\) is even and \(\delta\geq1\).

Suppose first that \(\delta<2o\). Then (17) implies \(q^\delta\mid e/2\); hence

\[
e\geq2q^\delta\geq2^{\delta+1},
\qquad o=e-\delta\geq2^{\delta+1}-\delta\geq2\delta.
\tag{18}
\]

The final inequality follows from \(2^{h+1}\geq3h\) for all positive integers \(h\), which follows by induction. In particular \(e/2=(o+\delta)/2<o\), and \(p<q\) gives

\[
0<-H<2^{\delta-1}o q^\delta.
\]

Divisibility (17) forces

\[
q^{2o-\delta}<2^{\delta-1}o,
\quad\text{thus}\quad 2^{2o-2\delta+1}<o.
\]

But (18) makes the left side at least \(2^{o+1}>o\), a contradiction.

Consequently \(\delta\geq2o\). Now the second summand in \(H\) is a multiple of \(q^{2o}\), so (17) implies

\[
q^{2o}\mid e/2,
\qquad e\geq2q^{2o}\geq2^{2o+1}.
\tag{19}
\]

## 6. The real inequality contradicts (19)

Since \(U>V>0\), (4) gives \(U^o>\sqrt N\geq\sqrt2\), so

\[
U>2^{1/(2o)}.
\]

Factoring the even-power difference in (4) and retaining its first positive term gives

\[
D U^{e-1}<U^e-V^e=U^o+V^o<2U^o.
\]

Because \(\delta\geq2o\), its consequence is

\[
\frac1q\leq D<2U^{-(\delta-1)}
<2^{1-(\delta-1)/(2o)}.
\]

Raise the resulting lower bound on \(q\) to the power \(2o\) and combine with (19):

\[
\frac e2\geq q^{2o}>2^{\delta-1-2o},
\qquad\text{hence}\qquad e>2^{e-3o}.
\tag{20}
\]

For integers \(o\geq3\), \(2^{2o+1}\geq6o\). Thus (19) gives \(e\geq6o\) and \(e\geq4\). Consequently

\[
2^{e-3o}\geq2^{e/2}\geq e,
\]

where the last inequality holds for every even integer \(e\geq4\) (again by induction). This contradicts (20). There is therefore no remaining pair (5).

## 7. Returning to the original exponents

Only the coprime pair \((e,o)=(2,1)\) remains beyond the attributed diagonal family. The original common factor \(d\) was odd, so it gives exactly \((2d,d),(d,2d)\) with \(d\) odd.

For sufficiency in this additional family, the official witness for \((2,1)\) is \(x=1/2-\sqrt N<0\). For every positive odd \(d\), its negative real \(d\)-th root exists. This root witnesses \((2d,d)\) and its reversal. This is an **odd-multiple** step; an even multiple need not preserve a negative real witness. The diagonal family is the published preliminary input already cited. This yields classification (C). Both required audits have now reconstructed and accepted the argument; the published preliminary inputs remain explicitly attributed.

## Constructor checks and audit trail

- The coordinator's \((4,3)\) draft is compatible with the proposed argument, but this constructor's check is not one of its independent reviews.
- Exact SymPy checks confirm the weighted-degree bound and the constant-in-\(N\) identity up to sign for all coprime even/odd pairs \(4\leq e\leq18,3\leq o<e\). This is finite evidence only.
- The unit-resultant calculation was checked separately for all coprime even/odd pairs through \(e=30\). This is finite evidence only.
- Pay particular attention to the resultant scaling in (16), the proof of the unit constant in (11), degree drops on specialization, the modulus \(q^{2o}\) in (17), and both branches in Section 5. These steps carry the unrestricted conclusion.
- No primitive-divisor theorem, separately billed API, or empirical search is used as a substitute for an unrestricted proof.
- Novelty and present-day publication status remain subject to a broader literature audit. A failed web search does not establish absence of a published solution.
