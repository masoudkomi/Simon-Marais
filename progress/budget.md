# Weekly budget

## Authorized cutoff

Stop at **90% total used** of the user's weekly subscription allowance. Do not spend 90% of the remaining allowance. Do not use separately billed API access. Preserve room for reviews, final integration, commits and push. Begin wind-down conservatively before the ceiling; do not infer precise future costs from context length.

## Baseline

- Source: Codex desktop `get_usage_limits`, account-wide `rateLimitsByLimitId.codex.primary`.
- Client date: 2026-10-16, Australia/Brisbane.
- Latest pre-launch observation: **0% used**, **100% remaining**, at the precision returned by the tool.
- Window duration: **10,080 minutes (seven days)**.
- Reset Unix timestamp: **1792745187**.
- Reset: **2026-10-23 08:46:27 UTC**, or **2026-10-23 18:46:27 Australia/Brisbane**.
- Plan type was returned as `unknown`; this does not make a reported zero equivalent to unavailable telemetry.
- No numeric token estimate is substituted for weekly usage. Reporting granularity/lag is unknown.

Recheck before launching each group, during sustained work, before expensive computation, and at wind-down. Account for active workers and possible telemetry lag. If a reset occurs, stop and record it; another week's allowance is not automatically authorized.

## Observation log

| Observation | Weekly used | Remaining | Action |
|---|---:|---:|---|
| 2026-10-16 prerequisite checks | 0% | 100% | No sustained mathematical research launched while scope/repository were unresolved. |
| 2026-10-16 repository verified, before initial owner group | 0% | 100% | Initial research authorized; reserve review and integration capacity. |
| 2026-10-16 after initial research and permission preflight | 1% | 99% | Telemetry increased; same weekly reset. Continue with reserved review capacity. |
| 2026-10-16 09:52:05 UTC | 2% | 98% | Same reset; initial passes and reviews continue. |
| 2026-10-16 10:00:57 UTC | 2% | 98% | Eight initial checkpoints, last owner plus two independent full-candidate reviews active. |

User clarification during the initial group: investigate only the explicitly open portion of B4. This narrows mathematical targets, not the weekly cutoff.

## Stop record

Research has not stopped at the cutoff. Record the final observed usage and actual stop reason here; never claim execution continues after it ends.
