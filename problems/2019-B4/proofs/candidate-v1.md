# 2019 B4(b): partial proof, version 1

**candidate proof - unverified.** Written 2026-10-16. No independent
adversarial review has yet been completed. This is partial progress on the
explicitly open part (b); the exact growth constant is not determined here.
Only the coordinator may promote any result after the required two audits.

The definitions of \(B_n\) and \(b_n\) are those of the official paper. A
history records left/right choices, whereas a word is counted only once,
regardless of how many histories produce it. This distinction is used
throughout.

The published contextual bounds are
\(\phi\le\liminf b_n^{1/n}\le\limsup b_n^{1/n}\le\psi\), where
\(\phi=(1+\sqrt5)/2\) and \(\psi\) is the real root greater than 1 of
\(x^3-x^2-x-1\). These are attributed to the official 2019 solution notes,
pp. 10–12; this investigation does not reprove part (a).

## 1. Marked contexts and existence of the growth rate

For \(k\ge0\), let \(\mathcal C_k\) be the set of pairs \((l,r)\) of binary
words obtained by making \(2k\) legal additions around an unchanged, marked
central seed \(1\). Thus the resulting word is \(l1r\), and
\(|l|+|r|=2k\). Let \(C_k=|\mathcal C_k|\). In particular,
\(\mathcal C_0=\{(\epsilon,\epsilon)\}\) and \(C_0=1\).

**Lemma 1.** For all \(k,j\ge0\),
\[
b_{2k+1}\le C_k\le(2k+1)b_{2k+1},\qquad
C_{k+j}\le C_k C_j.\tag{1}
\]

*Candidate proof.* The map \((l,r)\mapsto l1r\) is onto \(B_{2k+1}\).
For a fixed output word and fixed \(|l|\), the pair \((l,r)\) is uniquely
determined, so every fibre has at most \(2k+1\) members. This proves the
first two inequalities, without identifying different marked positions.

Split a history of \(2(k+j)\) moves after its first \(2k\) moves. The first
block gives a context \((l_1,r_1)\in\mathcal C_k\). The second block starts
from an odd-length word, so its sequence of added bits is again
\(0,1,0,1,\ldots\), exactly as from the seed. It therefore gives a context
\((l_2,r_2)\in\mathcal C_j\). The final context is
\[
(l_2l_1,r_1r_2).
\]
Conversely, this composition is possible for every pair of contexts in the
two sets. In particular the composition map is onto \(\mathcal C_{k+j}\),
which proves the last inequality. Injectivity is neither claimed nor needed.
\(\square\)

**Theorem 2 (partial answer to (b)).** A finite real number \(\lambda\) exists
such that
\[
\lim_{n\to\infty}b_n^{1/n}=\lambda,
\qquad
\lambda=\inf_{k\ge1} C_k^{1/(2k)}.\tag{2}
\]

*Candidate proof.* Put \(a_k=\log C_k\). These are finite, nonnegative
numbers and \(a_{k+j}\le a_k+a_j\). For any fixed \(r\ge1\), write
\(k=qr+s\), where \(0\le s<r\). Repeated application gives
\[
a_k\le q a_r+a_s.
\]
After division by \(k\) and passage to the upper limit, the bounded finite
set of possible \(a_s\)'s contributes zero, yielding
\(\limsup a_k/k\le a_r/r\). Since this holds for each \(r\), and
\(a_k/k\ge\inf_r a_r/r\), the limit equals \(\inf_r a_r/r\). This is the
elementary subadditivity argument; no additional theorem hypotheses are
being suppressed.

The first two bounds in (1) show
\[
0\le\log C_k-\log b_{2k+1}\le\log(2k+1).
\]
Dividing by \(2k\) makes the right side tend to zero. Also
\(b_n\le2^{n-1}\), since there are \(2^{n-1}\) histories. Consequently
replacing exponent denominator \(2k\) by \(2k+1\) changes the limiting
logarithmic rate by zero. Hence the odd-length roots converge to the value
in (2).

Appending the next mandated bit is an injective map \(B_n\to B_{n+1}\),
so \(b_n\le b_{n+1}\). In particular
\(b_{2k+1}\le b_{2k+2}\le b_{2k+3}\). Taking logs, dividing by \(2k+2\),
and using the odd-length limit proves convergence along even lengths too.
\(\square\)

## 2. Seed substitution and lower approximants

For \(k\ge1\) and \(0\le p\le2k\), define
\[
\mathcal C_{k,p}=\{(l,r)\in\mathcal C_k:|l|=p\},
\qquad M_k=\max_p|\mathcal C_{k,p}|.
\]

**Lemma 3.** For every \(k\ge1\),
\[
M_k^{1/(2k)}\le\lambda\le C_k^{1/(2k)},\qquad
\frac{C_k^{1/(2k)}}{M_k^{1/(2k)}}\le(2k+1)^{1/(2k)}.\tag{3}
\]
Thus finite context counts give converging lower and upper enclosures,
although these have not yet identified a closed form for \(\lambda\).

*Candidate proof.* Fix a position \(p\) attaining \(M_k\). Compose \(q\)
contexts from \(\mathcal C_{k,p}\), starting from the seed. Every generated
word has its marked seed after exactly \(qp\) left bits. From the final
word, recover the left and right context strings by cutting at this known
position. Split the left string into its fixed-length \(p\)-bit blocks,
and the right string into its fixed-length \(2k-p\)-bit blocks. These
recover the original ordered list of contexts, reversing the block order
on the left as dictated by composition. If \(p=0\) or \(p=2k\), the
corresponding empty blocks cause no ambiguity; in fact that position class
contains just the all-right or all-left context. Therefore the map from
the \(M_k^q\) lists to output words is injective. It follows that
\(b_{2kq+1}\ge M_k^q\). Let \(q\to\infty\) and use Theorem 2.
The upper bound is (2), while \(C_k\le(2k+1)M_k\) proves the ratio bound.
Since the ratio tends to one and \(\lambda\) lies between the endpoints,
both endpoints converge to \(\lambda\). \(\square\)

A second, weaker formulation does not require counting all marked
contexts: for odd \(m\) and any \(n\ge1\),
\[
b_{m+n-1}\ge b_m b_n/n.\tag{4}
\]
To see this, choose one generating history for each of the finitely many
words in \(B_n\), and partition them by the position of their seed. A class
has at least \(b_n/n\) words. Replace the seed in any word of this class by
an arbitrary member of \(B_m\). Since \(m\) is odd, every subsequent move
has the correct parity. The fixed seed position and known \(m\) recover
both input words, so the map is injective. This was the first route found
to growth existence; Theorem 2 gives the cleaner argument.

## 3. An explicit candidate upper bound below the published bound

Set \(L<R\) in lexicographic order on histories. The following replacements
preserve the final left/right context around *every* starting word:
\[
RRLL\longrightarrow LLRR,
\qquad
RRLRRLRLLRLL\longrightarrow LLRLLRLRRLRR.\tag{5}
\]
For a block whose first added bit is 0, the second pair of histories both
produce left context \(100110\) and right context \(011001\). Their
contexts agree also when the first bit is 1, by complementing every bit.
The first replacement has the same property, checked directly. Both
replacements have the same length on each side and strictly lower the
history in lexicographic order.

For any word of \(B_n\), take a lexicographically least length-\(n-1\)
history producing it. If the history contained either left-hand side in
(5), replacing that block would give a smaller history for the same word:
the actual block starts with either 0 or 1, and the equality holds in both
cases. This is impossible. Hence the number \(d_t\) of histories avoiding
both forbidden blocks satisfies
\[
b_{t+1}\le d_t.\tag{6}
\]

Build the finite suffix automaton whose states are the proper prefixes of
\(RRLL\) and \(RRLRRLRLLRLL\), including the empty word. On appending a
letter, reject if a forbidden word is completed; otherwise move to the
longest state that is a suffix of the current word. Every state is
accepting. This gives precisely the avoiding histories, by induction on
their length. In the order
\[
\epsilon,R,RR,RRL,RRLR,RRLRR,RRLRRL,RRLRRLR,
RRLRRLRL,RRLRRLRLL,RRLRRLRLLR,RRLRRLRLLRL,
\]
its adjacency matrix is the exact matrix stored in
`computations/upper-certificate-2026-10-16.json`.

Here is an integer weight vector in that state order:
\[
\begin{split}
v=(&1000000000000,837605905420,539189558215,451628358102,\\
&829914937903,525056590887,425657533878,782190797941,\\
&912301838575,838845340670,541467151750,455813677432)^T.
\end{split}
\]
Every entry is positive. With \(q=183761/100000=1.83761\), the exact
integers \(183761v_i-100000(Av)_i\) are
\[
\begin{split}
(&409458000000,342964384620,220775446615,184922881622,\\
&339815293183,214988686007,174288855158,320274236101,\\
&373549380575,343471859870,221708031750,186636581752),
\end{split}
\]
all strictly positive. Put \(q'=\max_i(Av)_i/v_i\); these inequalities
give \(q'<q\). Since \(\boldsymbol1\le v/\min_i v_i\), induction yields
\[
d_t=(A^t\boldsymbol1)_\epsilon
\le \frac{v_\epsilon}{\min_i v_i}(q')^t.
\]
Together with (6) and Theorem 2 this proves the candidate bound
\[
\boxed{\lambda<1.83761.}\tag{7}
\]
The exact finite certificate uses only the displayed integer arithmetic.
The separately reported numerical spectral radius
\(1.837605905420144\ldots\) is computational evidence, not used by this
deduction. This certificate and its mathematical applicability both still
require two independent adversarial reviews.

## 4. Finite evidence and the outstanding gap

The exhaustive computations in `computations/` give
\(C_{12}=2985943\) and \(M_{12}=395397\), with the maximum at \(p=12\).
An independent subset enumeration examines all
\(\binom{24}{12}=2704156\) histories with twelve left moves and obtains
the same fixed-position count. These are **finite computational evidence**.
If that count is accepted after independent audit, Lemma 3 gives the
candidate numerical lower estimate
\(\lambda\ge395397^{1/24}\approx1.710841292477\).
The proof of Lemma 3 is the unrestricted argument; the finite run does
not by itself establish an asymptotic theorem.

No equality between \(\lambda\) and an explicitly evaluated real number
has been established. Equations (2)–(3) describe converging enclosures but
are not being presented as a full solution of the requested determination.
The principal remaining tasks are to characterize all context collisions
or otherwise evaluate the growth constant, and to independently audit all
partial candidate arguments above.
