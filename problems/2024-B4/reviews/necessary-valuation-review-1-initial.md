# Whole initial audit R1: necessary valuation for a whole Kasami divisor

2026-10-17 UTC. Reviewer `review_2022_complexity_r2`. **Independent review of a candidate proof; no promotion.** No substantive objection found. The result under audit is only

\[
q=2^k,\ k\ge2,\ d=q^2-q+1,\ n\ge3\text{ odd},\quad
\phi_d\mid\phi_n\Longrightarrow v_2(n-1)=k.
\]

The complete 3446-byte candidate, all eleven obligation entries, sources, constructor manifest and its administrative freeze script were read. The complete exact accepted CP body and acceptance scope were read. This report and its separate inference ledger/source record freeze before any new peer NV findings are read. Root constructed NV; I did not contribute to it. I previously reviewed the 2024 structural, divisor and generalized Kasami packets. That context is disclosed; none of those reviews constructs this local valuation argument. Requested settings are `gpt-6.1-sol`/`max`; independent effective-setting readback is unavailable.

## Official and dependency scope

The official 2024 Paper B, page 2, part (b), asks for odd positive integer exponents admitting the stated coefficientwise factorization modulo two with two nonconstant integer-polynomial factors. NV is a necessary condition for one particular WHOLE polynomial divisor. It does not classify reducibility, individual extension-field factors, or the full family of exponents. It does not reproduce preliminary part (a).

Accepted CP1 supplies precisely the bridge used here. For odd indices at least three, write

\[
G_j(x)=x^j+(x+1)^j=g_j(x^2+x),\qquad \deg g_j=(j-1)/2.
\]

Then whole divisibility \(\phi_d\mid\phi_n\) over \(\mathbb F_2\) is equivalent to \(g_n=H\circ g_d\) for a polynomial \(H\in\mathbb F_2[T]\). This includes multiplicities. I checked the exact body's invariant-ring/free-module reduction, cancellation of the same diagonal factor, monic composition expansion, and homogenization scope. The cover has basis \(1,s,t,st\), so divisibility descends rather than merely holding after an arbitrary extension. The monic expansion in powers of \(g_d\) forces the coefficients of positive residual powers to vanish. The homogeneous degree argument does not discard a factor at infinity. These are the accepted CP1 assertions, not a new proof claim about arbitrary factors. CP2 and CP3 are read context, not needed premises of NV.

Degree comparison in CP1 gives

\[
\deg H=(n-1)/(d-1)\in\mathbb Z_{>0},\qquad d-1=q(q-1).
\]

Consequently \(n\ge d\), \(q-1\mid n-1\), and \(s=v_2(n-1)\ge k\). These three consequences are all used, and their integer scope is valid. In particular \(n=3\) cannot satisfy the NV hypothesis, while \(n=1\) is outside CP1 and NV.

## The local order preserved by composition

For odd \(j\ge3\), \(G_j(0)=1\). In characteristic two,

\[
G_j'(x)=x^{j-1}+(x+1)^{j-1},\qquad G_j'(0)=1.
\]

The composition identity, first evaluated and then differentiated at zero, gives \(H(1)=1\) and \(H'(1)=1\). Hence \(H(T)+1=(T+1)Q(T)\), where differentiation at one gives \(Q(1)=H'(1)=1\). At any extension-field point \(\alpha\) with \(G_d(\alpha)=1\), the substitution \(Q(G_d(x))\) has nonzero constant term in the local coordinate \(z=x-\alpha\). It is a unit in \(\mathbb F_q[[z]]\). Thus

\[
\operatorname{ord}_{\alpha}(G_n+1)
=\operatorname{ord}_{\alpha}(G_d+1).
\]

This is an exact multiplicity statement, not only equality of root sets. No assertion that \(H\) is everywhere unramified or globally separable is used. Its derivative at the single value one suffices. Nonzero polynomials remain nonzero under extension of the coefficient field.

## Exact Kasami multiplicity

Since \(q\ge4\), choose \(\alpha\in\mathbb F_q\setminus\mathbb F_2\) and put \(b=\alpha+1\). Both \(\alpha,b\) are nonzero, \(\alpha+b=1\), and their powers of exponent \(q-1\) are one. For \(a=\alpha\) or \(b\),

\[
(a+z)^d=(a+z)(a^q+z^q)^{q-1}.
\]

Terms on the right have degrees \(iq\) and \(iq+1\). Since \(q\ge4\), through degree \(q+1\) only \(0,1,q,q+1\) occur. The coefficient associated with \(i=1\) is \(q-1=1\) in characteristic two. Summing the two expressions gives the following coefficients of \(G_d(\alpha+z)\):

| Degree | Coefficient and reason |
| --- | --- |
| 0 | \(\alpha^d+b^d=\alpha+b=1\), since \(d\equiv1\pmod{q-1}\). |
| 1 | \(\alpha^{d-1}+b^{d-1}=1+1=0\). |
| \(q\) | \(\alpha^{d-q}+b^{d-q}=0\), since \(d-q=(q-1)^2\). |
| \(q+1\) | \(\alpha^{d-q-1}+b^{d-q-1}=\alpha^{-1}+b^{-1}=1/(\alpha b)\ne0\), since \(d-q-1=q(q-2)\equiv-1\pmod{q-1}\). |

Adding one cancels the constant coefficient and does not affect the last coefficient. There are no omitted lower degrees. Therefore

\[
\operatorname{ord}_{\alpha}(G_d+1)=q+1.
\]

The calculation works at every point of \(\mathbb F_q\setminus\mathbb F_2\); only one is needed. There is no sampling argument. In particular the smallest permitted value \(q=4\) causes no collision of the displayed degrees, and \(2q>q+1\) still holds.

## The larger valuation contradicts that multiplicity

Assume \(s>k\) and write \(n=1+2^s h\) with positive odd \(h\). For either \(a=\alpha,b\),

\[
(a+z)^n=(a+z)(a^{2^s}+z^{2^s})^h.
\]

Every nonconstant degree occurring is of the form \(i2^s\) or \(i2^s+1\). Hence no degree strictly between one and \(2^s\) occurs. The constant coefficient of \(G_n(\alpha+z)\) is one because \(q-1\mid n-1\). Its coefficient at degree one is \(\alpha^{n-1}+b^{n-1}=1+1=0\). Adding one cancels its constant coefficient as well. It follows that

\[
\operatorname{ord}_{\alpha}(G_n+1)\ge2^s\ge2q>q+1.
\]

This proof never assumes \(\alpha^{2^s}=\alpha\), which would generally require an extra divisibility relation between \(k\) and \(s\). Only Frobenius in the polynomial identity is needed. Nor must the coefficient at degree \(2^s\) be shown nonzero; the stated lower bound is sufficient. The order is finite: \(G_n\) has degree \(n-1\) and leading coefficient one for odd \(n\ge3\), so \(G_n+1\) is not the zero polynomial.

The lower bound contradicts the exact order preserved by \(H'(1)=1\). Since degree comparison already gave \(s\ge k\), the only remaining possibility is \(s=k\). This reconstructs every mathematical step in NV.

## Boundary and counterexample challenges

The restriction \(k\ge2\) is essential. For \(q=2\), \(d=3\), and the quotient \(\phi_3\) is the unit. It divides \(\phi_5\), whereas \(v_2(5-1)=2\ne1\). This explicit excluded-domain counterexample agrees with the lack of an \(\alpha\notin\mathbb F_2\). It is not a counterexample to NV as stated.

At \(n=d\), \(H=T\) and \(v_2(d-1)=k\), so equality and a unit cofactor are covered. Repeated factors, inseparability at other values, and extension-field evaluation do not defeat the local unit argument. A single irreducible Kasami component need not imply the CP1 composition identity; the candidate explicitly retains the whole-divisor hypothesis. The conclusion only fixes a valuation. It does not force the complete sufficient progression, and it does not claim a new Diophantine or APN classification. The older exact \(\phi_{13}\) criterion is consistent context for \(q=4\), not a premise of this proof.

No mathematical computation, enumeration, CAS or constructor rerun was used. Administrative hashing verifies integrity only. The separate ledger records 23 inference checks covering all eleven constructor obligations. No repair is requested on this audit; acceptance still belongs to the coordinator after the other independent whole audit.
