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
| 2026-10-16 21:14:13 UTC | 15% | 85% | Same reset; host-delayed tool call returned; both2019audits complete and new2017reviews launched. |
| 2026-10-16 21:37:51 UTC | 16% | 84% | Same reset;2017/2019 refinements accepted; structural2021reasoning and two whole2025source audits continue. |

| 2026-10-16 approximately 21:52 UTC | 17% | 83% | Same reset; continue mathematical research with 2017, 2022 and 2024 owners. |

| 2026-10-16 22:11:06 UTC | 17% | 83% | Same reset; two new 2022 complexity audits and structural research continue. |

| 2026-10-16 22:17:35 UTC | 18% | 82% | Same reset; 2022 complexity adaptation accepted, fresh 2021 single-center audits and 2024 factor-field research continue. |

| 2026-10-17 00:22:55 UTC | 19% | 81% | Same reset; continue annulus/divisor reasoning and fresh audits, with review and integration reserve. |
| 2026-10-17 00:34:31 UTC | 20% | 80% | Same reset; continue author repair, independent geometric audits and fixed-divisor review. No stop condition. |

User clarification during the initial group: investigate only the explicitly open portion of B4. This narrows mathematical targets, not the weekly cutoff.

## Stop record

Research has not stopped at the cutoff. Record the final observed usage and actual stop reason here; never claim execution continues after it ends.

## Observed project token accounting

The user requested explicit token reporting. The 17:07 UTC snapshot records **255,675,838 total tokens**, including **242,026,752 cached input**, **11,430,007 uncached input**, and **2,219,079 output** (reasoning included). Uncached input plus output is **13,649,086**. This sums deduplicated own-thread per-response usage across the coordinator and all spawned descendants; each of the 49 recorded session totals matched its cumulative counter. It counts repeated context, not unique text. See token-usage-2026-10-16-1707.json and the newer timestamped snapshot. These are local observations during active execution, not billing or a conversion to weekly allowance. The 90% cutoff continues to use authoritative account-wide percentage telemetry. Reproduce a fresh snapshot with `.venv/bin/python tools/report_project_tokens.py --output progress/token-usage-latest.json` in this chat, or supply `--root-thread-id` for an explicit root. No prompts, account identifiers or raw logs are exported.

At **17:31:36 UTC**, the latest audit records **298,729,173 total tokens**: **283,106,816 cached input**, **13,177,156 uncached input**, and **2,445,201 output**, including reasoning. Uncached input plus output is **15,622,357**. All51 session sums matched their own cumulative counters;51 sessions are historical launches, not simultaneous agents. See `token-usage-latest.json`. In-flight unreported usage is excluded.

At **21:39:37 UTC**, the refreshed audit records **327,243,804 total**:309,796,864 cached input,14,724,214 uncached input and2,722,726 output. Output includes **1,180,857 reasoning tokens**, a subset rather than an added category. Uncached input plus output is17,446,940. All57 recorded session sums match cumulative counters; no billing or weekly conversion is inferred. The user requested greater emphasis on mathematical reasoning; Max remains the requested worker setting, with no independent effective-setting readback.

At **22:13:22 UTC**, recorded project usage was **354,246,265 total**:335,256,064 cached input,16,018,769 uncached input and2,971,432 output, including1,309,467 reasoning tokens. Uncached input plus output was18,990,201. All62 historical session sums matched cumulative counters; simultaneous capacity remains four total agents.

At **2026-10-17 00:22:56 UTC**, recorded project usage was **389,511,772 total**:367,888,512 cached input,18,354,949 uncached input and3,268,311 output, including1,460,285 reasoning tokens. Uncached input plus output was21,623,260. All62 historical session sums matched cumulative counters. This is a local recorded snapshot excluding unreported in-flight usage; it is not a bill or weekly-percentage conversion.

At **2026-10-17 00:47:50UTC**, recorded project usage was **421,191,874 total**:
398,370,944 cached input;19,252,474 uncached input;3,568,456 output,
including1,577,691 reasoning output. Uncached input plus output22,820,930.
All62 historical sums match; in-flight unreported usage excluded. This
is not billing or weekly conversion. Authoritative weekly telemetry
returned21% at approximately00:46UTC, same reset1792745187; continue
with integration reserve before90% total.

At **2026-10-17 05:47:16UTC**, authoritative account-wide usage returned **23% total used**, same reset1792745187. Continue with review/integration reserve. User authorizes an untimed owned keep-awake assertion until the90% cutoff; see permissions.md and run-state.json.

At **2026-10-17 05:49:57UTC**, recorded project token audit: **478,054,490 total**, including451,011,712 cached input,22,905,669 uncached input and4,137,109 output. Output includes1,900,963 reasoning tokens. Uncached input plus output27,042,778. All62 historicalsession sums match; in-flight unreported usage excluded. Account-wide telemetry23%at05:49:59UTC; worker direct authoritative read24%at05:51:41UTC,same reset1792745187. No weekly conversion inferred from rawtokens.

At **2026-10-17 06:14:08 UTC**, account-wide telemetry remains **25% weekly used**, 75% remaining, reset1792745187;65percentagepoints before the90% total cutoff. The **06:14:09 UTC** raw token audit records **508,517,198 total**, comprising479,825,152cachedinput,24,307,846uncachedinput and4,384,200output (including1,993,743reasoning). Uncachedinput+output28,692,046. All62historical session sums match cumulative counters. These are repeated-context counts excluding unreported in-flight work; no bill or conversion to weekly percentage is implied. [Official Codex usage guidance](https://learn.chatgpt.com/docs/pricing) distinguishes included allowance from token/credit rates and says context, reasoning, tools and caching affect usage; the account meter supplies our cutoff. [Official token category documentation](https://developers.openai.com/api/docs/guides/agents-api/observability) confirms cached input and reasoning output are subsets, not added categories. New work remains authorized, with review/integration reserve and owned untimed awake assertion active.

At **2026-10-17 06:34:05UTC**, authoritative account meter **26% total weekly used**,74%remaining,64percentagepoints before90%, same reset1792745187. Tokenaudit **06:34:06UTC**: **529,865,545total**,499,958,784cachedinput,25,343,876uncachedinput,4,562,885output including2,079,331reasoning; uncachedinput+output29,906,761. All62historical session sums match. Repeated context and unreported in-flight exclusions remain; no bill or weeklyconversion inferred. Continue authorized mathematical work and independent audits with integration reserve.

At **2026-10-17 06:59:04UTC**, authoritative account usage is **28% total weekly used**,72% remaining,62percentagepoints before90%, same reset1792745187. Local raw audit06:57:58UTC: **569,173,322total**,537,760,000cachedinput,26,602,304uncachedinput,4,811,018output including2,161,169reasoning; uncachedinput+output31,413,322. All62historical session sums match; in-flight unreported usage excluded, no bill or weekly conversion inferred. Keep-awakePID79293/session64368 verified active16:49:42Brisbane; release only at90%cutoff or actualtermination. Continue authorized reasoning/review with integration reserve.


At **2026-10-17 07:20:08UTC**, authoritative account usage is **29% total weekly used**,71%remaining,61percentagepoints before90%, same reset1792745187. Local raw audit **07:21:38UTC**: **600,459,470total**,567,800,448cachedinput,27,570,571uncachedinput,5,088,451output including2,271,758reasoning; uncachedinput+output32,659,022. All62historicalsession sums match; unreported in-flight usage excluded. These repeated-context counts are not billing or a conversion to weeklyusage. Keep-awake79293/session64368 verifiedactive17:21:38Brisbane. Continue authorized reasoning, literature work and whole independent audits with integration reserve.
