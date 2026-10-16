# Literature audit, 2026-10-16

Scope: only 2025 B4(b). All literature exponents here are translated to term count m=n+1. No preliminary proof was investigated. These are source audits and finite exact checks, not a new full solution.

## Search log and access

Queries issued through web search on 2026-10-16:

- `Nagell Ljunggren equation 2025 2026 Bugeaud Mihailescu all solutions`
- `Bennett Levin Nagell Ljunggren Runge method 177 15 31 2015 DOI`
- `"Nagell-Ljunggren" "2026" solved conjecture`
- `"Nagell-Ljunggren" "2025" "conjecture"`
- `Bugeaud Mihailescu 2007 Nagell Ljunggren pdf Theorem 1 q divides n`
- `"On the Nagell-Ljunggren equation" "29" "2007"`

Primary journal/author sources are listed in ../references.md. The original official B4(b) text and solution-page-20 remark were extracted with pypdf; no preliminary proof was read for research. Initial journal access to `https://www.mscand.dk/article/download/15038/13033/34539` returned HTTP 404 via web; `https://tidsskrift.dk/math/article/view/15038` redirected to login. The current MSP journal PDF path succeeded without an access bypass. Author-posted published Bennett-Levin PDF was checked, so its main theorem is called Theorem 1, not the arXiv version's Theorem 2.

The curl downloads to the Son and UBC domains initially returned exit 6, `Could not resolve host`; authorized network retries succeeded. Public downloads were cached locally, then moved from the year directory to ignored `.cache/literature/2025/` at the coordinator's direction. The precise successful URL/hash inventory is source-manifest.json. No credentials, paid APIs or access-control bypass were used.

## Published import safeguards

Bennett-Levin's equation (1) permits |x|>1 and |y|>1. Its four displayed identities count roots with even q up to sign; for literal integer quadruples the negative square roots must also be included. Normalize y to |y| for a positive even power before comparing the displayed exceptional identities. Its quoted restrictions and main theorem are recorded in ../research.md; no full reconstruction of their proofs was attempted here.

Bugeaud-Mihailescu's equation (1) explicitly assumes x,y>1. The least-prime bound 29 and q=3 prime-term-count conclusion were read in original Theorem 1, not inferred from a search snippet. Their Theorem 2 supplies a positive-domain no-further-solutions reduction to prime term counts. It is not a direct claim that every solution already has prime term count. Full independent theorem verification remains a project review task.

## Son 2026: exact objections to the printed statement and proof

Theorem 3's all-integer claim lists only (0,1), but (-1,1) satisfies the defined quotient: (-2)/(-2)=1=1^3. This counterexample needs no theorem import. For x=1 the quotient is undefined; its polynomial continuation equals 5 and adds no cube.

In Case 2, equation (6), put rho^2=rho+1. The correct coefficient of rho in rho(a+b rho)^3 is a^3+3a^2 b+6ab^2+3b^3; the printed expression is a^3+6a^2 b+9ab^2+5b^3. At a=-1,b=1 the expression equals 2-rho, matching the omitted x=-1 solution; the printed coefficient is +1 instead of -1. Exact symbolic output is in initial-results.json. Remark 1 also incorrectly says m=5 satisfies m not congruent to 5 modulo 6. These objections prevent relying on the paper; they do not refute a narrower nontrivial nonexistence result established elsewhere.

## Wang 2025 preprint: full-solution claim not accepted

The site marks v1 unreviewed. Its Theorem 8 uses Theorem 7's claimed abc bound. In Theorem 7, equation (33), set T=zeta rad(abc)^2 and rho=1/sqrt(T). Under c=floor(T)+1, the expression sqrt(c)/rho equals T sqrt(c/T). The paper instead replaces it by sqrt(c/T), dropping the factor T. The subsequent bound (35) uses that smaller expression. This is a false equality, not a cited theorem with unverified hypotheses. Hence this argument does not establish the abc bound or its claimed positive Nagell-Ljunggren conclusion. This audit does not claim a counterexample to either conjecture.

## Status conclusion and limit

The sources inspected do not give this project an independently verified unrestricted classification. The 2026 Chen-Mihailescu abstract is conditional, and full hypotheses remain unchecked. Neither an unsuccessful search nor the flaws in specific claims prove that no valid general result exists. No claim of absolute certainty is made.
