# Unattended execution permissions

User requested a preflight to avoid research stopping for routine permission prompts.

## Already authorized and tested

- Intended remote is https://github.com/masoudkomi/Simon-Marais.git; branch codex/smmc-b4-research.
- Initial commit and push succeeded using existing Git credentials. No default-branch merge, force push, deletion, credential changes, or separately billed API access is authorized.
- Public official-paper download script was run with scoped network approval; 18 PDFs were fetched into the ignored workspace cache and hashed. Public literature can be researched with web tools. The existing approved curl -L --fail prefix is available for needed public PDF downloads.
- All research artifacts and computations stay inside the writable workspace. No global software installation or GUI automation is needed for the planned mathematical work.
- The user approved the dependency setup while present. A workspace-local `.venv/` now contains SymPy, mpmath, SciPy and Matplotlib; scientific/PDF imports and smoke checks passed. Exact inspected versions are pinned in `requirements-research.txt`. The existing scoped pip-install prefix applies to this local environment; no broad interpreter or shell approval was requested.
- The user explicitly approved preventing idle sleep for 12 hours. `caffeinate -i -t 43200` is running as PID 5398 (exec session 57629); `pmset -g assertions` verified the idle-sleep assertion. It began shortly before 2026-10-16 09:26 UTC (19:26 Brisbane) and expires approximately 2026-10-16 21:26 UTC (07:26 Brisbane on 17 October). Display sleep is allowed; lid closure is not prevented. Terminate the assertion if research ends early.
- Coordinator plus at most three workers; slot reassignment and fresh independent reviews are authorized. Workers must not commit or push.

## Avoid avoidable prompts

Use the installed bundled scientific/PDF dependencies, exact standard-library code, and web tools. Route any unexpected permission need to the coordinator. Do not attempt writes outside the workspace, install global packages, change security settings, create paid API sessions, or seek broad shell/interpreter approvals. Do not bypass an actual approval denial. Keep useful work progressing in allowed areas while an unrelated request is unresolved.

Existing credentials can still expire and the computer/network can become unavailable; these are external execution blockers, not permissions that can be guaranteed in advance. Preserve local commits and exact restart state if this occurs.
