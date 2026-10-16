# Simon Marais annual B4 research

This repository records a sustained investigation of the Simon Marais Mathematics Competition's annual **B4 open problems**. It covers the nine verified official problems from **2017 through 2025**. The user has deferred 2026; no missing statement is invented and no other competition problem is substituted.

**Only the open portion is in scope:** the entire 2017 problem; the general 2018 enumeration, excluding research on its already known m=5 case; and **B4(b) only in every year 2019-2025**. Preliminary part (a) is excluded. See the [direct official-paper scope audit](sources/open-scope-audit.md). Whether an originally open problem has subsequently been solved is a separate, dated literature question.

**Current stage:** all nine years have initial research checkpoints; research and reviews continue. The **2023(b) full exponent classification is proved, independently reviewed**, using attributed preliminary inputs and a project-developed unrestricted resultant argument; see [proof](problems/2023-B4/proofs/reviewed-v1.md) and [audits](problems/2023-B4/reviews/acceptance.md). Its novelty remains unestablished. The general **2018 enumeration has a proved, independently reviewed reproduction of an earlier published formula**; see [proof](problems/2018-B4/proof.md) and [audits](problems/2018-B4/reviews/acceptance.md). Reviewed partial results now include [2017 counting and gluing lemmas](problems/2017-B4/reviews/secondpass-acceptance.md), [2019 renewal, rigidity and certified 1.76521<lambda<1.83516197](problems/2019-B4/reviews/secondpass-acceptance.md), [2022 density-one hitting on each fixed-difference line](problems/2022-B4/reviews/acceptance.md), [2021 valuation restrictions and the complex degree20 three-value-cover exclusion](problems/2021-B4/reviews/three-complex-acceptance.md), [the exact 2024 criterion for the whole divisor phi13](problems/2024-B4/reviews/criterion-acceptance.md), and [2025 elementary integer-domain reductions](problems/2025-B4/reviews/acceptance.md). Their full questions remain unresolved; other candidates remain explicitly unverified. A published solution to a preliminary part does not resolve the annual open part.

- [Dashboard](progress/dashboard.md): per-problem status, results, obstructions, next steps and reviews.
- [Budget and telemetry](progress/budget.md): observed weekly usage and reset boundary.
- [Restart instructions](progress/restart.md): how to resume safely.
- [Research and review protocol](AGENTS.md).
- [Source manifest](sources/official.json): verified official annual pages, Paper B and solution URLs.
- [Environment and computations](progress/environment.md).

Each `problems/<year>-B4/` directory contains `statement.md`, `references.md`, `research.md`, `proof.md`, `issues.md`, `reviews/`, and `computations/`. Statements are mathematical normalizations of the linked official papers, not a claim that old descriptions of openness establish present-day status. Literature searches must be dated and primary sources verified.

## Acceptance labels

Use **observation**, **conjecture**, **computational evidence**, **partial result**, **candidate proof - unverified**, **failed argument**, or **proved, independently reviewed** precisely. The last label requires a complete self-contained proof, two independent adversarial audits, an independent reconstruction, and no unresolved substantive objection. Published reproductions and original contributions remain separately attributed.

## Source retrieval

Run `python3 tools/fetch_official.py` to cache the nine official Paper B and solution PDFs and record SHA-256 hashes in `sources/retrieval.json`. Downloads are cached under ignored `.cache/official/`; work on B4 only. Original papers include other problems, which are outside the investigation. The official source manifest and B4-specific notes are tracked. Python with `pypdf` is needed only for optional PDF text inspection; mathematical scripts should use exact standard-library arithmetic where practical.

Public mathematical literature may be accessed and cached without repeated permission requests. Prefer primary papers and author-posted versions; full papers stay locally in ignored `.cache/literature/`, with citations, links, hashes and notes saved here. Public access does not establish redistribution permission. Full third-party papers require a verified redistribution licence before inclusion. No paid access or charges are authorized. See [permissions and cache migration](progress/permissions.md) and [local literature mapping](sources/literature-cache.json).
