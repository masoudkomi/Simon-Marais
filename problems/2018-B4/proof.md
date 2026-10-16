# 2018 B4: an explicit general enumeration

**candidate proof - unverified**, version 1.0, 2026-10-16.

This is a reproduction and elementary derivation of a **published formula**, not a claim of a new research result. Hering and Howard, Proposition 3.2, directly contains the result after substituting equal weights. Ottaviani, Theorem 40, also records the equal-weight formula and attributes it to Howe. Full references and the discrepancy with the competition's as-issued open label are in `references.md`. The proof below is self-contained and does not require representation theory or those theorems as black boxes.

Two independent adversarial audits, including one complete reconstruction, are pending. Only the coordinator may change the proof status.

## 1. Statement and explicit answer

For the official set of matrices in `statement.md`, let \(F(m,n)=|A(m,n)|\). For all positive integers \(m,n\), the proposed answer is

\[
F(1,n)=0,
\qquad
F(m,n)=\sum_{j=0}^{\lfloor(m-1)/2\rfloor}
(-1)^j\binom mj
\binom{(m-2j)n+m-j-2}{m-2}
\quad(m\ge2).                                      \tag{1}
\]

Here \(\binom ab=0\) for integers \(0\le a<b\), and otherwise it has its usual factorial meaning. Every upper argument in (1) is nonnegative: since \(m-2j\ge1\), it is at least \(m-j-1\ge0\). Thus (1) does not silently use binomial coefficients at negative upper arguments.

The number of summands is \(\lfloor(m-1)/2\rfloor+1\), independent of \(n\). This is an explicit sum of ordinary binomial coefficients, rather than just a coefficient-extraction restatement of the counting problem.

## 2. A content-preserving reflection bijection

Put \(L=mn\). Let \(\mathcal R\) be the set of pairs \((U,V)\) of weakly increasing rows of length \(L\), with exactly \(2n\) occurrences of each symbol in their union. A pair is good if \(U_i<V_i\) for every \(1\le i\le L\). These good pairs are exactly the required matrices. Call the other pairs bad.

Let \(\mathcal S\) be the set of weakly increasing row pairs \((P,Q)\) of respective lengths \(L+1\) and \(L-1\), again with the prescribed combined content. There is a bijection from the bad pairs in \(\mathcal R\) to \(\mathcal S\).

For a bad pair, choose its first failure index
\[
i=\min\{j:U_j\ge V_j\}.
\]
Define
\[
P=(V_1,\ldots,V_i,U_i,\ldots,U_L),\qquad
Q=(U_1,\ldots,U_{i-1},V_{i+1},\ldots,V_L).       \tag{2}
\]
The row \(P\) is weakly increasing because \(V_i\le U_i\). The only possible new junction in \(Q\), when both pieces are nonempty, satisfies
\[
U_{i-1}<V_{i-1}\le V_{i+1}.
\]
The lengths and the combined content have the required values. Empty pieces when \(i=1\) or \(i=L\) cause no additional condition.

For the inverse, take any \((P,Q)\in\mathcal S\). Choose the first index \(i\in\{1,\ldots,L-1\}\) for which \(Q_i\ge P_i\), if such an index exists, and choose \(i=L\) otherwise. Set
\[
U=(Q_1,\ldots,Q_{i-1},P_{i+1},\ldots,P_{L+1}),\qquad
V=(P_1,\ldots,P_i,Q_i,\ldots,Q_{L-1}).          \tag{3}
\]
The new junction in \(U\), when present, is weakly increasing since
\(Q_{i-1}<P_{i-1}\le P_{i+1}\). The new junction in \(V\), when present, is weakly increasing by the choice \(P_i\le Q_i\). Both lengths are \(L\), and the combined content is preserved. For \(j<i\), (3) gives \(U_j=Q_j<P_j=V_j\), whereas at \(i\) it gives \(U_i=P_{i+1}\ge P_i=V_i\). Thus \(i\) is its first failure index.

The two constructions are inverse. Indeed, starting from (2), one has \(Q_j=U_j<V_j=P_j\) for \(j<i\), and, if \(i<L\), \(Q_i=V_{i+1}\ge V_i=P_i\). Therefore the inverse selects precisely \(i\); if \(i=L\), it selects the prescribed default. Conversely, the preceding first-failure calculation for (3) ensures that (2) reconstructs the given \((P,Q)\). This proves the bijection, including its endpoint cases.

## 3. Reduction to bounded compositions

For an integer \(t\), let
\[
c_t=\#\{(a_1,\ldots,a_m)\in\mathbb Z^m:
0\le a_k\le2n,\ a_1+\cdots+a_m=t\}.
\]
We set \(c_t=0\) when no such vector exists. A pair of weakly increasing rows with prescribed combined content is uniquely determined by the multiplicity vector of its first row. Consequently
\[
|\mathcal R|=c_L,\qquad |\mathcal S|=c_{L+1}.
\]
The reflection bijection gives
\[
F(m,n)=c_L-c_{L+1}=c_L-c_{L-1}.                 \tag{4}
\]
The second equality follows from the bijection
\((a_1,\ldots,a_m)\mapsto(2n-a_1,\ldots,2n-a_m)\), which changes a sum \(L+1\) into \(L-1\).

This also identifies the familiar symmetric-function route: these matrices are the semistandard tableaux counted by
\(K_{(mn,mn),(2n,\ldots,2n)}\). The two-row Jacobi-Trudi expression \(h_L^2-h_{L+1}h_{L-1}\) gives (4). That identity is context only; the bijection above establishes (4) without invoking it.

## 4. Evaluation as a binomial sum

Assume \(m\ge2\). In formal power series,
\[
\sum_t c_t x^t=(1+x+\cdots+x^{2n})^m
=\frac{(1-x^{2n+1})^m}{(1-x)^m}.
\]
Therefore (4) is
\[
[x^L]\frac{(1-x^{2n+1})^m}{(1-x)^{m-1}}
=\sum_{\substack{0\le j\le m\\(2n+1)j\le L}}
(-1)^j\binom mj
\binom{L-(2n+1)j+m-2}{m-2}.                    \tag{5}
\]
Here the expansion \((1-x)^{-(m-1)}=\sum_{r\ge0}\binom{r+m-2}{m-2}x^r\) follows, for example, by multiplying \(m-1\) geometric series and counting weak compositions of \(r\). All coefficient manipulations involve finitely many terms at the selected degree.

If \((2n+1)j\le mn\), then \(2j<m\), so every nonzero term of (5) has
\(j\le\lfloor(m-1)/2\rfloor\). Conversely, for an index in this latter range that violates \((2n+1)j\le mn\), its upper binomial argument in (1) lies between \(0\) and \(m-3\); its term is therefore zero. We may extend (5) to exactly the range in (1). This proves the proposed formula for all \(m\ge2,n\ge1\).

For \(m=1\), every matrix entry would be 1, so every column fails its strict inequality. Thus \(F(1,n)=0\), completing all positive \(m,n\).

## 5. Boundary and published-case comparisons

- For \(m=2\), (1) has the single term \(\binom{2n}{0}=1\). Directly, the top row must contain all the 1s and the bottom row all the 2s.
- For \(m=3\), it gives \((3n+1)-3n=1\).
- For \(m=4\), it gives \(\binom{4n+2}{2}-4\binom{2n+1}{2}=2n+1\).
- The boundary \(n=1\) is included in every step and gives the explicit specialization
  \(\sum_{j=0}^{\lfloor(m-1)/2\rfloor}(-1)^j\binom mj\binom{2m-3j-2}{m-2}\) for \(m\ge2\). The first values for \(m=1,\ldots,10\) are \(0,1,1,3,6,15,36,91,232,603\); these finite values are computational checks, not the proof of the specialization.
- As a consistency check only, for \(m=5\), (1) simplifies to the official value \((5n^2+5n+2)/2\). No new result is claimed for this already known preliminary case.

## 6. Optional polynomial consequence

For fixed \(m\ge3\), (1) is a polynomial in \(n\) of degree at most \(m-3\). Each binomial term is a polynomial of degree at most \(m-2\). Its coefficient at \(n^{m-2}\), apart from the positive factor \(1/(m-2)!\), sums to
\[
T=\sum_{j=0}^{\lfloor(m-1)/2\rfloor}(-1)^j\binom mj(m-2j)^{m-2}.
\]
The full sum over \(0\le j\le m\) is zero: it is an \(m\)-th finite difference of a polynomial in \(j\) of degree \(m-2\). Terms at \(j\) and \(m-j\) are equal. When \(m\) is even, the middle term is zero because \(m-2\ge1\). Thus the full sum is \(2T\), so \(T=0\), proving the stated degree bound. This consequence is part of the candidate and remains subject to the same reviews.
