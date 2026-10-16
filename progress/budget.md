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
| 2026-10-16 10:08:30 UTC | 3% | 97% | All nine initial passes complete; 2023 audits integrated; further independent audits active. Same reset. |
| 2026-10-16 10:42:59 UTC | 5% | 95% | Same reset; reviewed partials integrated, focused research and fresh reviews continue. |
| 2026-10-16 14:53:40 UTC | 7% | 93% | Host tool delay returned; workers saved deeper checkpoints; fresh audits and integration continue. Same reset. |

| 2026-10-16 15:13:21 UTC | 7% | 93% | Same reset; deeper 2019 and 2021 partial results accepted; fresh 2017 audit and separate degeneration audits continue. |

| 2026-10-16 15:40:02 UTC | 9% | 91% | Same reset; degeneration partial result accepted, fresh full three-witness audit launched; 2017/2020/2025 reviews continue. |

| 2026-10-16 16:02:11 UTC | 10% | 90% | Same reset; rational witness and 2025 partial audits accepted; repaired 2017 re-audits and 2020 R2 continue. |
| 2026-10-16 16:27:04 UTC | 11% | 89% | Same reset; narrow source audits integrated; complex extension audits active. |
| 2026-10-16 16:49:44 UTC | 12% | 88% | Same reset; complex C20 accepted, entire rational J=16 candidate sent for fresh full audits. No stop condition. |

| 2026-10-16 approximately 17:10 UTC | 13% | 87% | Same reset; deeper literature work across all years added alongside research and review. |
| 2026-10-16 17:24:59 UTC | 14% | 86% | Same reset; J16 accepted, literature reports and two fresh blind 2019 reviews continue. |

User clarification during the initial group: investigate only the explicitly open portion of B4. This narrows mathematical targets, not the weekly cutoff.

## Stop record

Research has not stopped at the cutoff. Record the final observed usage and actual stop reason here; never claim execution continues after it ends.

## Observed project token accounting

The user requested explicit token reporting. The 17:07 UTC snapshot records **255,675,838 total tokens**, including **242,026,752 cached input**, **11,430,007 uncached input**, and **2,219,079 output** (reasoning included). Uncached input plus output is **13,649,086**. This sums deduplicated own-thread per-response usage across the coordinator and all spawned descendants; each of the 49 recorded session totals matched its cumulative counter. It counts repeated context, not unique text. See token-usage-2026-10-16-1707.json and the newer timestamped snapshot. These are local observations during active execution, not billing or a conversion to weekly allowance. The 90% cutoff continues to use authoritative account-wide percentage telemetry. Reproduce a fresh snapshot with `.venv/bin/python tools/report_project_tokens.py --output progress/token-usage-latest.json` in this chat, or supply `--root-thread-id` for an explicit root. No prompts, account identifiers or raw logs are exported.

At **17:31:36 UTC**, the latest audit records **298,729,173 total tokens**: **283,106,816 cached input**, **13,177,156 uncached input**, and **2,445,201 output**, including reasoning. Uncached input plus output is **15,622,357**. All51 session sums matched their own cumulative counters;51 sessions are historical launches, not simultaneous agents. See `token-usage-latest.json`. In-flight unreported usage is excluded.
