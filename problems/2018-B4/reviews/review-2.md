# Independent adversarial review 2: 2018 B4

Initial audit completed and saved on **2026-10-16**. Reviewer: fresh agent `/root/review_2018_r2`, which did not construct the candidate. Requested launch settings: **gpt-6.1-sol / max**. No independent readback of effective model or reasoning settings was available; requested and verified settings are not conflated.

Audited artifact: `problems/2018-B4/proof.md`, **candidate proof - unverified, version 1.0**, SHA-256 **`5a90732b2696559176d02b6a695e1743fbc4406158a76c0185d9e06c17b06e83`**. The hash matched before inspection. Line numbers below refer to this exact version.

**Independent verdict:** I found no substantive mathematical objection to the explicit enumeration or the optional polynomial consequence. The elementary argument gives the full literal general cardinality requested by B4, subject to the stated positive-integer domain. Its formula reproduces published work. This is one reviewer's assessment, not promotion to repository status **proved, independently reviewed**; only the coordinator may combine both independent audits and resolve all issues.

## Independence, scope and source fidelity

Before saving this initial report I did **not** read `reviews/review-1.md`, any review-1 asset, review-queue conclusions, other reviewer messages, the author's computation scripts, or the author's computation outputs. I read the assigned candidate, `AGENTS.md`, `statement.md`, and `references.md`; consulted the official PDF and the cited primary texts; and designed separate exact computations. All writes were confined to this report and `review-2-assets/`. No proof, shared file, issue log, commit, push, dependency installation, paid API, or subagent was used.

The cached official paper's SHA-256 is `fa26d31d056dfcb5f782209c20ee0c59f20717cdc48ef195c2099582037aa704`. I extracted B4 from page 2, independently rendered its region to `review-2-assets/official-b4.png`, and visually checked it. The dimensions are exactly \(2\times mn\); both parameters are positive integers; each symbol in \(\{1,\ldots,m\}\) occurs \(2n\) times in the whole matrix; both rows are weakly increasing; the first entry of every column is strictly smaller than the second. The final request is cardinality determination without a further restriction on the answer's form. The normalization and candidate match these conditions. The paper's as-issued open label and known preliminary target are visible on the same page. [Official Paper B, p. 2](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2018-paper-b_1.pdf).

No separate research on the known \(m=5\) case was done. Candidate line 106 was treated solely as its attributed consistency comparison; no preliminary-case derivation or separate numerical test was made. No other competition problem was investigated.

## Full reconstruction and inference audit

Write \(L=mn\). Ignore column inequalities temporarily, keeping both rows sorted and the total content fixed. This gives \(\mathcal R\). Its good elements are exactly the required matrices. For a bad element, let \(i\) be the first position with \(U_i\ge V_i\). Move the prefix \(V_1,\ldots,V_i\) in front of the suffix \(U_i,\ldots,U_L\) to make \(P\), and concatenate the remaining prefix of \(U\) and suffix of \(V\) to make \(Q\). The lengths become \(L+1,L-1\); every occurrence of every symbol appears once among the outputs. At the only new junction of \(P\), \(V_i\le U_i\). At the only new junction of \(Q\), when both pieces exist, first failure gives \(U_{i-1}<V_{i-1}\le V_{i+1}\). Thus the map lands in \(\mathcal S\).

Conversely, for sorted \((P,Q)\) of these lengths, select the first \(i<L\) with \(Q_i\ge P_i\), or set \(i=L\) if none exists. Splitting at that position as in (3) makes rows of length \(L\). The \(U\) junction is ordered because \(Q_{i-1}<P_{i-1}\le P_{i+1}\); the \(V\) junction, if present, is ordered because \(P_i\le Q_i\). For \(j<i\), the recovered columns satisfy \(U_j=Q_j<P_j=V_j\). At \(i\), \(U_i=P_{i+1}\ge P_i=V_i\), so its first failure is exactly the selected \(i\). This also shows the two constructions recover each other's split point and all pieces. At \(i=1\), the absent prefixes impose no condition. At \(i=L\), the inverse has \(U=(Q_1,\ldots,Q_{L-1},P_{L+1})\), \(V=(P_1,\ldots,P_L)\), and both monotonicity and failure remain valid. At \(L=1\), \(Q\) is empty, the default is \(i=1\), and the inverse is \(U=(P_2),V=(P_1)\); this is bad since \(P_1\le P_2\). There is no missing endpoint assumption.

For either row-length pair, choosing the first-row multiplicities \(a_1,\ldots,a_m\) with \(0\le a_k\le2n\) uniquely determines **both** sorted rows, the second having multiplicities \(2n-a_k\). Hence \(|\mathcal R|=c_L\) and \(|\mathcal S|=c_{L+1}\). The bad-pair bijection gives \(F=c_L-c_{L+1}\). Complementing all multiplicities takes sum \(L+1\) to \(2mn-(L+1)=L-1\), so \(c_{L+1}=c_{L-1}\). Thus

\[
F=[x^L](1-x)(1+x+\cdots+x^{2n})^m
 =[x^L](1-x^{2n+1})^m(1-x)^{-(m-1)}.
\]

For \(m\ge2\), expansion gives (5). Put \(r=mn-(2n+1)j\). A contributing index has \(r\ge0\). Since \(n\ge1\), this implies \(2j<m\). In the proposed extended range \(j\le\lfloor(m-1)/2\rfloor\), the upper argument \(N=r+m-2=(m-2j)n+m-j-2\) satisfies \(N\ge m-j-1\ge0\). If \(r<0\), then \(N\le m-3<m-2\), so its ordinary binomial term is zero under the declared convention. This proves precisely (1), without a generalized binomial at a negative upper argument. When \(m=1\), every entry is 1 and no column can be strict, establishing the separate answer.

| Candidate location | Adversarial check and disposition |
| --- | --- |
| Lines 11-24, (1) | Full positive-integer domain and ordinary-binomial convention match the official problem. Number of terms is independent of \(n\). Upper-argument bound is correct. |
| Lines 28-30 | \(\mathcal R\) fixes combined content, not content per row. Good pairs impose the exact required strict inequality. \(\mathcal S\)'s longer row is the first row, consistent with the map and count. |
| Lines 32-45, (2) | First failure exists for every bad pair; junction checks, lengths, total content and both empty-piece cases are valid. Equality \(U_i=V_i\) is correctly classified as bad. |
| Lines 47-55, (3) | First-choice/default rule is exhaustive. All needed inequalities and both inverse identities hold, including \(i=1\), \(i=L\), and \(L=1\), as reconstructed above. |
| Lines 59-73, (4) | Multiplicity parametrization and complement symmetry are bijections. Both subtraction signs and the change from \(c_{L+1}\) to \(c_{L-1}\) are correct. |
| Lines 75-76 | Kostka shape/content and the two-row Jacobi-Trudi determinant agree with this count. This contextual identity is not needed as an unproved step in the elementary argument. |
| Lines 80-92, (5) | Formal-series use is valid. The factor \(1-x\) takes exactly \(c_L-c_{L-1}\); the denominator exponent and lower binomial argument are \(m-1\) and \(m-2\), respectively. Weak-composition expansion has a positive number of factors. |
| Lines 94-97 | Truncation, extension by zero and \(m=1\) are valid. No \(n=0\) case is claimed or needed. |
| Lines 101-105 | \(m=2\) gives the unique possible matrix. The \(m=3,4\) simplifications and the \(n=1\) substitution are correct. Separate tests exclude \(m=5\) and verify the remaining listed \(n=1\) values. |
| Line 106 | Attributed preliminary-case context only; not used to establish the general formula and not separately researched in this audit. |
| Lines 110-114 | Polynomial consequence is valid for \(m\ge3\). Even where \(0\le N<m-2\), the falling-factorial polynomial has a zero factor, agreeing with the stated binomial convention at every allowed integer \(n\). The full finite difference vanishes, and pairing \(j\) with \(m-j\) preserves signs because \((-1)^{m-j}(-1)^{m-2}=(-1)^j\). For even \(m\ge4\), the unpaired middle term is zero. Thus the full sum is \(2T\), and the degree is at most \(m-3\). The excluded \(m=2\) would not satisfy this argument. |

## Primary theorem and attribution audit

I downloaded fresh primary PDFs into my own asset directory, rather than using any other reviewer's files, and visually inspected the relevant theorem pages. Verification date: **2026-10-16**.

**Hering-Howard.** Proposition 3.2, preprint pp. 6-7, has even total weight and counts two-row semistandard tableaux by content; its subset sum is the candidate's formula after setting the source's number of weights to \(m\), \(w=(2n,\ldots,2n)\). These weights are positive integers, their total is \(2mn\), and the shape is \((mn,mn)\). A subset of size \(j\) has weight \(2nj\); its strict bound is \(j<m/2\). Grouping subsets gives \(\binom mj\), with upper argument exactly \((m-2j)n+m-j-2\). The source's tableau convention on p. 4 matches strict columns and weak rows. The separate \(m=1\) answer needs no specialization with lower binomial argument \(-1\). The arXiv history dates v2 to 2014-01-19, and the author's publication list confirms the 2014 journal reference. [Primary preprint](https://arxiv.org/pdf/1211.3941v2), [version history](https://arxiv.org/abs/1211.3941), [author publication list](https://webhomes.maths.ed.ac.uk/~mhering/publications.html).

**Ottaviani.** Theorem 40, journal p. 186 / PDF page 68, gives the displayed equal-weight sum. Setting \(d=m,k=2n\) yields exactly (1). For even \(d\), its degree is \(k\) with polarization \(1^d\); for odd \(d\), it explicitly requires even \(k\), and uses degree \(k/2\) with polarization \(2^d\). Thus both parities give content \((2n)^m\), with no factor-of-two discrepancy. Theorem 28's proof, journal p. 173, identifies the relevant multigraded invariant dimension with semistandard tableaux, so this is the ordered-point count needed here. Theorem 40 cites Howe [28], section 5.4.2.3, and the bibliography identifies that 1988 work. I have not inspected Howe directly; attribution through Ottaviani is the appropriate claim. The journal PDF's first page verifies volume 71 (2013), pp. 119-194. [Primary journal PDF](https://seminariomatematico.polito.it/rendiconti/71-1/119.pdf).

Consequently the candidate's literal formula was available before the competition. The official paper nevertheless explicitly labels the general request open. The candidate correctly separates a published-result reproduction from a new contribution. This audit establishes the discrepancy, not its cause. The bounded check of the linked official 2018 page found no explanation; it does not establish that none exists elsewhere or that a stronger intended problem was open. An extra positivity or product-form requirement must not be silently added.

## Independent exact evidence and limits

`review-2-assets/review2_exact.py` implements a direct column-by-column enumeration. Its state contains the remaining total multiplicity of every symbol and the previous top/bottom entries. It appends every allowed strict column, maintains weak rows, and consumes the exact combined content. Every complete sequence is one literal matrix; no coefficient difference or published representation formula is used in that counting routine. A separate implementation of (1) supplies comparison values.

All **28** tested parameter pairs passed: \(m\in\{1,2,3,4,6,7,8\}\), \(n=1,2,3\), plus \((2,20),(3,15),(4,10),(6,5),(7,4),(9,1),(10,1)\). Representative counts are \(F(6,1..3)=(15,65,175)\), \(F(7,1..3)=(36,260,981)\), \(F(8,1..3)=(91,1085,5719)\), and \(F(10,1)=603\). Every case completed below the explicit cap of 500,000 memo states; the largest used 317,140.

A second exhaustive check ranges over **every** sorted row pair for alphabets of size 1 through 4 and lengths \(L=1\) through 6, with arbitrary combined contents. It found 12,871 bad source pairs and 12,871 target pairs, and checked both compositions of the maps, equality of sets, lengths, monotonicity and combined content. This includes 20 \(L=1\) incidences, 10,236 first failures at \(i=1\), and 592 at \(i=L\); these endpoint counts may overlap. Exact leading-coefficient sums vanished for \(m=3..40\), excluding the preliminary \(m=5\) case. The full run completed in about 1.52 seconds. The script and exact output are saved; all finite computations are evidence, not proof of unrestricted claims.

There were no incomplete computational runs, counterexamples, or unresolved substantive objections. Web screenshot fetches and a DOI resolver lookup failed, so the cited theorem checks used successfully downloaded primary PDFs and local Poppler renderings instead. Details, file hashes, commands, dependency versions and these retrieval limits are recorded in `review-2-assets/README.md`.

## Issue disposition

- **Substantive mathematical issues found:** none.
- **Required proof repairs from this audit:** none.
- **Retained limitation:** this is verification of a full literal enumeration already contained in the cited published formulas; it does not explain or settle an unstated stronger interpretation of the historical open label.
- **Repository action:** coordinator must combine this independently completed report with the other independent audit, re-review any affected repair, and decide status. This reviewer makes no status promotion.
