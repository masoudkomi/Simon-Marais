# Unattended execution permissions

User requested a preflight to avoid research stopping for routine permission prompts.

## Public literature authorization, 2026-10-16

The user explicitly authorizes search, access, download and local caching of all publicly available mathematics papers and supporting materials needed for the project, without asking each time. Prefer primary papers and author-posted versions. No purchases, paid subscriptions, access bypass or charges are authorized. Ask before any charge. Full third-party papers stay in ignored `.cache/` unless a redistribution licence has been verified; GitHub receives citations, source links, hashes and research notes.

Four full-paper review-evidence PDFs from earlier checkpoints were moved intact into `.cache/literature/2018/` and removed from the current branch tree. Their original review commands map to the new local paths in `sources/literature-cache.json`; the review reports and proof hashes remain unchanged. Earlier pushed commits still contain those copies. History has not been rewritten, consistent with the no-force-push instruction. All four downloaded 2025 papers now follow the same ignored-cache convention; their URLs, paths and hashes are in that year's computations/source-manifest.json. The current Git index contains no full-paper PDFs.

## Already authorized and tested

- Intended remote is https://github.com/masoudkomi/Simon-Marais.git; branch codex/smmc-b4-research.
- Initial commit and push succeeded using existing Git credentials. No default-branch merge, force push, deletion, credential changes, or separately billed API access is authorized.
- Public official-paper download script was run with scoped network approval; 18 PDFs were fetched into the ignored workspace cache and hashed. Public literature can be researched with web tools. The existing approved curl -L --fail prefix is available for needed public PDF downloads.
- All research artifacts and computations stay inside the writable workspace. No global software installation or GUI automation is needed for the planned mathematical work.
- The user approved the dependency setup while present. A workspace-local `.venv/` now contains SymPy, mpmath, SciPy and Matplotlib; scientific/PDF imports and smoke checks passed. Exact inspected versions are pinned in `requirements-research.txt`. The existing scoped pip-install prefix applies to this local environment; no broad interpreter or shell approval was requested.
- The initial authorized12-hour `caffeinate -i -t 43200`, PID5398/session57629, began about09:26UTC. The earlier assertion had been checked with `pmset`; at the end of its window the coordinator sent targeted Ctrl-C to its own session, which exited1 at about21:27UTC. No extension occurred without a new user instruction.
- The user then explicitly instructed “Extend for another12hours.” A new `caffeinate -i -t 43200` launched successfully at approximately2026-10-16 21:28:10UTC (07:28BrisbaneOct17), owned exec session14140. Its nominal end is2026-10-17 09:28:10UTC (19:28BrisbaneOct17). The new OS PID was not separately queried. Display sleep remains allowed, lid closure is not prevented, and the owned process should be terminated if research ends early.
- Coordinator plus at most three workers; slot reassignment and fresh independent reviews are authorized. Workers must not commit or push.

## Avoid avoidable prompts

Use the installed bundled scientific/PDF dependencies, exact standard-library code, and web tools. Route any unexpected permission need to the coordinator. Do not attempt writes outside the workspace, install global packages, change security settings, create paid API sessions, or seek broad shell/interpreter approvals. Do not bypass an actual approval denial. Keep useful work progressing in allowed areas while an unrelated request is unresolved.

For subsequent unattended Git saves, issue `git add`, `git commit`, and **plain `git push origin codex/smmc-b4-research`** as separate commands matching their existing approved prefixes. Do not prepend environment-variable assignments or combine extra shell operations in an escalated command: those forms can prevent prefix matching. Existing credential-helper authentication has worked. A later needed exact-algebra package, python-flint 0.9.0, installed successfully under the same project-local pip scope; no global install or broad interpreter approval was used.

Existing credentials can still expire and the computer/network can become unavailable; these are external execution blockers, not permissions that can be guaranteed in advance. Preserve local commits and exact restart state if this occurs.

## Keep awake until the authorized budget cutoff, 2026-10-17

The user explicitly requested idle-sleep prevention until 90% of weekly usage. The coordinator launched untimed `caffeinate -i`, owned exec session **64368**, PID **79293**. The former timed session14140 was stopped by targeted Ctrl-C (exit130). `pmset -g assertions` verified `PreventUserIdleSystemSleep=1`, PID79293, and “caffeinate asserting forever” at **2026-10-17 15:47:07 Australia/Brisbane**. This readback returned after a long host-side tool/approval delay; worker research checkpoints continued meanwhile. The display may sleep; lid closure is not prevented. At the90% total weekly cutoff or actual research termination, stop only this owned assertion, preferably via session64368. Do not leave it running after stopping the project. No paid API use or new-week spending is authorized.
