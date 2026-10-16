# Independent adversarial review 1: 2018 B4

Initial report completed 2026-10-16. Reviewer did not construct this candidate, did not read another review report or conclusion, and did not communicate with another reviewer. This report includes a complete independent reconstruction. No proof, issue-log, integration, or shared-file edits were made.

Reviewed snapshot: `proof.md`, **candidate proof - unverified**, version **1.0**, dated 2026-10-16; SHA-256 **`5a90732b2696559176d02b6a695e1743fbc4406158a76c0185d9e06c17b06e83`**. Hash verified before reading and again in the independent computation. Line references below refer to this snapshot. Requested agent settings: `gpt-6.1-sol`, reasoning `max`; an independent effective-setting readback was unavailable. Account-wide usage monitoring belongs to the coordinator; no separately billed API was used.

**Verdict: accepted conditional on the other independent review and coordinator integration.** I found no substantive mathematical error, unproved inference, or domain mismatch. The candidate gives the full literal enumeration for every positive integer pair. It reproduces an existing published formula; it is not evidence of a new research result. The reason for the competition's historical open label remains unresolved. This report does not promote the repository's overall proof status.

## Issues and limits

| ID | Severity | Location | Finding / disposition |
|---|---|---|---|
| R1-2018-01 | Informational; historical issue remains open | `proof.md:5`, `statement.md`, `references.md` | The published general formula and the paper's open label coexist. I independently verified both. The mathematical literal enumeration is complete, but a claim to have newly solved an unsolved research problem would not follow. The candidate already makes the necessary distinction, so no mathematical repair is required. |
| R1-2018-02 | Informational; convention checked | `proof.md:22`, `94-95`, `110` | Treating the binomial terms as polynomials is legitimate even where the coefficient-expansion cutoff would omit a term: every retained upper argument is nonnegative, and a nonnegative integer below the lower argument gives a zero falling factorial. No extension to negative upper arguments is used. No repair required. |

No blocking issues were found. The other bibliography cross-checks are not premises of the elementary proof; this audit independently checked the two published formulas actually cited in its opening and reconstructed its symmetric-function context directly.

## Official-statement fidelity

I extracted B4 only from `.cache/official/2018-paper_b.pdf`, page 2, and independently rendered and visually inspected that page. The cached paper hash is `fa26d31d056dfcb5f782209c20ee0c59f20717cdc48ef195c2099582037aa704`, matching the source record. I also opened the [official online paper](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2018-paper-b_1.pdf). The source has positive integer parameters, two rows of length `mn`, alphabet `1,...,m`, exactly `2n` occurrences of each symbol, weak row order, and strict top-to-bottom column order. It asks for the cardinality without specifying a product formula, positivity, or a fixed number of summands independent of `m`. The candidate preserves each condition and quantifier.

Only the general enumeration was researched. The known `m=5` case was not independently solved, expanded, or computationally investigated in this review. Its comparison in the candidate is treated as attributed preliminary context. No other competition problem was investigated.

## Complete independent reconstruction

1. Fix positive integers `m,n`, and put `L=mn`, which is at least 1. Discard the strict column condition temporarily. Once the top row multiplicities `a_1,...,a_m` are fixed, sorting fixes the top row, and sorting the residual multiplicities `2n-a_1,...,2n-a_m` fixes the bottom row. Thus the unconstrained equal-length row pairs are counted by the number `c_L` of integer vectors with `0<=a_k<=2n` and sum `L`. The valid matrices form a subset of exactly this set; no labeling or row permutation factor is missing.

2. For a bad row pair `(U,V)`, let `i` be its first column with `U_i>=V_i`. Splice the prefix of `V` through `i` to the suffix of `U` beginning at `i`, and the prefix of `U` ending at `i-1` to the suffix of `V` beginning at `i+1`. The resulting row lengths are `i+(L-i+1)=L+1` and `(i-1)+(L-i)=L-1`. Each original entry is used exactly once, so every symbol's combined multiplicity is preserved. Each piece is sorted. At the first new junction `V_i<=U_i`. If the other junction is present, first failure gives `U_{i-1}<V_{i-1}`, and the order of `V` gives `V_{i-1}<=V_{i+1}`. Thus both new rows are sorted. If `i=1` or `i=L`, the missing pieces impose no junction condition.

3. To invert an arbitrary sorted pair `(P,Q)` of lengths `L+1,L-1`, choose the first `i<L` with `Q_i>=P_i`, or choose `i=L` if no such index exists. Form `U` by taking `Q_1,...,Q_{i-1}` followed by `P_{i+1},...,P_{L+1}`, and form `V` by taking `P_1,...,P_i` followed by `Q_i,...,Q_{L-1}`. The lengths are both `L`, and the content is unchanged. If `i>1`, minimality gives `Q_{i-1}<P_{i-1}<=P_{i+1}`, so `U` is sorted at its only new junction. If `i<L`, the choice gives `P_i<=Q_i`, so `V` is sorted at its junction. For `j<i`, the new columns satisfy `U_j=Q_j<P_j=V_j`. At `i`, they satisfy `U_i=P_{i+1}>=P_i=V_i`. Hence `i` is exactly the first failure.

4. Starting from the forward splice, all `j<i` satisfy `Q_j=U_j<V_j=P_j`; if `i<L`, at `i` one has `Q_i=V_{i+1}>=V_i=P_i`. The inverse therefore chooses the same `i`. If the forward failure was at `L`, all possible inverse test indices precede it, so the default chooses `L`. In the other direction, step 3 establishes the first failure, and direct concatenation recovers `P,Q`. These maps are mutually inverse on the prescribed-content sets. For `L=1`, `Q` is empty, the default index is 1, and the maps simply send a bad pair `(U_1,V_1)` to `(V_1,U_1)` and back. No undefined comparison is needed.

5. The unequal-length row pairs are counted by `c_{L+1}`, using their first-row multiplicities just as in step 1. Therefore the desired count is `c_L-c_{L+1}`. Complementing each component, `a_k -> 2n-a_k`, preserves the bounds and changes the sum to `2mn-t=2L-t`; it carries sum `L+1` to `L-1`. Consequently the count is `c_L-c_{L-1}`. This works even when a composition set is empty. It establishes the counting identity without any representation-theoretic assumption.

6. The polynomial with coefficients `c_t` is `C(x)=(1+x+...+x^(2n))^m`. Thus `c_L-c_{L-1}` is the coefficient of `x^L` in `(1-x)C(x)`. For `m>=2`, the finite geometric-series identity yields `(1-x^(2n+1))^m/(1-x)^(m-1)`. Expand the numerator by the ordinary binomial theorem. The coefficient at degree `r>=0` in `(1-x)^(-(m-1))` counts weak compositions of `r` into `m-1` parts and equals `binom(r+m-2,m-2)`. Terms with `r<0` do not occur. This gives (5) with `r=mn-(2n+1)j`. These are formal power series over the integers, so there is no convergence condition, and only finitely many terms contribute at the chosen degree.

7. If `r>=0` and `2j>=m`, then `j>=1` and `(2n+1)j=2nj+j>=mn+j>mn`, a contradiction. Hence all contributing indices obey `j<=floor((m-1)/2)`. For every index in this larger fixed range, `m-2j>=1`, and its upper binomial argument is `(m-2j)n+m-j-2>=m-j-1>=0`. If such an index has `r<0`, that argument is `r+m-2<=m-3`, so its binomial coefficient vanishes under the candidate's stated convention. Extending the sum by these zero terms produces exactly equation (1), with ordinary binomial coefficients throughout.

8. The excluded algebraic case `m=1` has alphabet consisting of one symbol, so no strict column exists, and the count is zero for every positive `n`. For `m=2` the sum is the single `binom(2n,0)=1`; sorting and strictness also force all smaller symbols into the top row and all larger symbols into the bottom. The `m=3,4` simplifications in lines 102-103 follow by substitution and cancellation. Nothing in steps 1-7 requires `n>1`; hence `n=1` is covered. The displayed `n=1` formula follows by substituting `n=1`, and the finite value list is only evidence.

9. For fixed `m>=3`, each summand in (1) agrees on all positive integer `n` with its falling-factorial polynomial divided by `(m-2)!`; this remains true when the nonnegative upper argument is smaller than `m-2`, because one of those factors is zero. Its degree is at most `m-2`, and its leading coefficient is the candidate's stated multiple of `T`. The full alternating sum over `0<=j<=m` annihilates the polynomial `(m-2j)^(m-2)`: applying a finite difference lowers the degree, so its `m`th finite difference is zero. For paired indices, the sign calculation is `(-1)^(m-j)(-(m-2j))^(m-2)=(-1)^j(m-2j)^(m-2)`. If `m` is even, the central base is zero and its exponent is positive. Thus the full sum is `2T`; `T=0`, and the degree is at most `m-3`. This proves exactly the optional bound, not a stronger degree or positivity claim.

All substantive steps were reconstructed. No omitted step resisted reconstruction.

## Line-by-line inference audit

| Candidate lines | Audit |
|---|---|
| 11-24 | Formula covers exactly the positive domain; every used upper binomial argument is nonnegative. Fixed summation bound is independent of `n`, as claimed. |
| 28-30 | Sets match official matrices after adding or dropping exactly the strict-column condition. Unequal lengths are nonnegative because `L>=1`. |
| 32-45 | First failure exists for every bad pair; both junction inequalities, lengths, and exact content preservation checked. |
| 47-55 | Inverse is defined on every proposed target; both junctions, true first failure, both compositions, `i=1`, `i=L`, and `L=1` checked. |
| 59-73 | Top-row multiplicities determine both sorted rows; reflection subtraction and complement symmetry have the asserted orientations. |
| 75-76 | Shape and content give the stated two-row Kostka count. If `h_r` is the weight-generating sum over sorted length-`r` rows, the same content-preserving bijection proves that the weight sum over valid two-row tableaux is `h_L^2-h_(L+1)h_(L-1)`. Thus the contextual Jacobi-Trudi instance is consistent without relying on it as an external black box. |
| 80-92 | Formal power-series manipulation, coefficient shift by `(1-x)`, geometric-series expansion, and binomial coefficient all checked. |
| 94-97 | Strict inequality in the cutoff, added-zero terms, and the separate `m=1` case checked explicitly. |
| 101-105 | Boundary computations and `n=1` substitution checked; finite values independently tested except the deliberately excluded preliminary parameter. |
| 106 | Attributed preliminary comparison only; not independently rederived here. |
| 110-114 | Polynomial interpretation including zero-binomial cases, leading coefficient, finite-difference annihilation, sign pairing, and even central term checked. |

## Primary-source audit and historical interpretation

I read and visually checked [Hering and Howard, Proposition 3.2](https://arxiv.org/pdf/1211.3941v2), PDF pages 6-7, including its proof. It counts semistandard tableaux of shape `(|w|/2,|w|/2)` and content `w`, assuming an integral nonnegative weight vector with even total. The candidate's positive weights meet these hypotheses. With source-vector length `m` and `w=(2n,...,2n)`, total weight is `2mn`. A subset of size `j` has weight `2nj`, the subset condition is `j<m/2`, and the upper argument becomes `(m-2j)n+m-j-2`. There are `binom(m,j)` subsets of that size. This is exactly (1) for `m>=2`; the elementary proof independently handles `m=1`. No stability, genericity, characteristic, or asymptotic requirement is needed for this purely combinatorial proposition. The [arXiv record](https://arxiv.org/abs/1211.3941) dates v2 to 2014-01-19, and the [author's publication list](https://webhomes.maths.ed.ac.uk/~mhering/publications.html) confirms the 2014 journal publication. Thus prior availability is independently supported.

I also visually checked [Ottaviani, Theorem 40](https://seminariomatematico.polito.it/rendiconti/71-1/119.pdf), journal page 186 / PDF page 68. Setting `d=m,k=2n` in its displayed formula gives (1). Its explanatory parity condition for odd `d` requires even `k`, which is satisfied. For odd `d`, the degree is `k/2` with weight vector `2^d`, hence individual weight `k`; for even `d`, degree `k` with weight `1^d` again gives individual weight `k`. The theorem attributes its proof to Howe section 5.4.2.3. I did not inspect Howe's original text, so that attribution remains mediated through Ottaviani, as the candidate correctly says.

The official as-issued PDF labels the general problem open. My bounded check of the [2018 official competition page](https://www.simonmarais.org/20181.html) did not locate an explanation or correction. This does not establish that none exists. The formula answers the paper's literal request, while the historical motivation for its open label is unresolved. No extra requested property should be inferred from that label.

## Independent falsification attempts

The script `review-1-assets/independent_audit.py` was constructed and run before reading any author computation; I did not import or read `computations/exact_count.py` or its output. It uses Python **3.12.14**, standard library only. The direct counter appends an actual column `(a,b)` with `a<b`, both entries at least their predecessors in their rows, and consumes the two symbol multiplicities. Memoization merges identical residual states. This counts the official objects directly, without using the bounded-composition difference or a tableaux-counting recurrence.

Results are preserved exactly in `review-1-assets/independent-audit-results.json`:

- **32** parameter pairs completed and agreed exactly with (1): `n=1` with `m in {1,2,3,4,6,7,8,9,10}`; `n in {2,3,4}` with `m in {1,2,3,4,6,7}`; and `(8,2),(4,5),(4,10),(4,20),(6,5)`. Examples outside the preliminary case are `F(7,4)=2661`, `F(8,2)=1085`, and `F(6,5)=671`. The `n=1` counts at the tested `m` match the candidate list.
- Exhaustive forward and inverse tests over alphabets of sizes **1-4** and lengths **1-6** checked **12,871** bad equal-length row pairs and **12,871** unequal-length target pairs. Every test preserved each symbol's content, row order and lengths; both compositions were the identity. For alphabet size at least 2, every first-failure position `1,...,L` occurred. These tests include arbitrary contents to attack the local splice claim; they do not assert a new enumeration problem.
- The coefficient cutoff and added-zero convention passed **257,100** index checks for `2<=m<=100`, `1<=n<=50`, excluding `m=5`; **3,662** terms added by the fixed summation range were zero as claimed. For example, `m=7,n=1,j=3` is retained by (1) but omitted by (5), and its coefficient is `binom(3,5)=0`.
- The exact integer leading-coefficient cancellation `T=0` passed for `3<=m<=100`, excluding `m=5`.

All planned cases finished in **0.579594 seconds** under a 45-second / one-million-states-per-case cap. No incomplete or failed run occurred. These computations are finite evidence; the unrestricted conclusion rests on the reconstruction above.

## Reproducibility and saved evidence

Working directory for every command was `/Users/uqmkamga/Documents/ChatGPT/Website`. Relevant successful commands were:

```text
shasum -a 256 problems/2018-B4/proof.md
shasum -a 256 .cache/official/2018-paper_b.pdf .cache/official/2018-solutions.pdf
.venv/bin/python --version
.venv/bin/python problems/2018-B4/reviews/review-1-assets/independent_audit.py
pdftoppm -f 2 -l 2 -scale-to 1800 -singlefile -png .cache/official/2018-paper_b.pdf problems/2018-B4/reviews/review-1-assets/official-page-2
curl -L --fail --silent --show-error https://arxiv.org/pdf/1211.3941v2 -o problems/2018-B4/reviews/review-1-assets/hering-howard-v2.pdf
curl -L --fail --silent --show-error https://seminariomatematico.polito.it/rendiconti/71-1/119.pdf -o problems/2018-B4/reviews/review-1-assets/ottaviani.pdf
pdftoppm -f 6 -l 7 -scale-to 1800 -png problems/2018-B4/reviews/review-1-assets/hering-howard-v2.pdf problems/2018-B4/reviews/review-1-assets/hering-howard
pdftoppm -f 68 -l 68 -scale-to 1800 -singlefile -png problems/2018-B4/reviews/review-1-assets/ottaviani.pdf problems/2018-B4/reviews/review-1-assets/ottaviani-theorem-40
```

Saved checksums:

| Artifact | SHA-256 |
|---|---|
| Independent script | `13e6698bd941e99692eb3968f5e8d8b33b54d54ac847bb181f39f08c6909834f` |
| Hering-Howard v2 PDF | `4d03468322f4886c092aa263d88b98c593aacc2106f340049a36ec4b398ab360` |
| Ottaviani journal PDF | `8e6e11d3105670a7b6fa00df0a3e8665770001276e64bd776e10f58f70812cb4` |

Web-tool screenshots of the three theorem pages returned internal errors. Local downloads and Poppler renders succeeded and were visually inspected instead. A supplementary pypdf extraction attempt for the Ottaviani page emitted malformed-object warnings and did not match the small-caps heading; no conclusion relied on that extraction. The preserved page rendering and direct PDF inspection resolved this tooling limitation. No dependency installation or external-directory write was performed.
