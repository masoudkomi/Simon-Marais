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


At **2026-10-17 10:40:46UTC**, authoritative account-wide usage is **30% total weekly used**,70%remaining,60percentagepoints before90%, same reset1792745187. The **10:40:58UTC** raw audit records **633,764,611total**,598,377,216cachedinput,30,019,555uncachedinput,5,367,840output including2,387,494reasoning; uncached+output35,387,395. All62historical session sums match across3941distinct responses. Recorded repeated-context counts exclude unreported in-flight usage; no billing or weekly conversion implied. Owned keep-awake79293/session64368 verified20:40:58Brisbane. Continue authorized research and independent audits with integration reserve.


At **2026-10-17 11:01:58UTC**, account meter **32%TOTAL weekly used**,68%remaining,58percentagepoints before90%, same reset1792745187. Raw **663,335,337total**:626,944,256cachedinput,30,803,866uncachedinput,5,587,215output including2,475,639reasoning; uncached+output36,391,081. All62historicalsession sums match across4091responses. Unreported in-flight usage excluded; no billing/weekly conversion. Continue reasoning and reviews with integration reserve.


At **2026-10-17 11:13:51UTC**, raw project audit **681,140,577total**:643,996,160cachedinput,31,442,524uncachedinput,5,701,893output including2,518,391reasoning; uncached+output37,144,417.62historicalsession sums match across4176responses. Direct account meter32%TOTAL at11:11:51UTC, same reset1792745187;58percentagepoints before90%. No billing/weekly conversion. Continue reasoning/reviews with integration reserve.


At **2026-10-17 11:23:13UTC**, account-wide meter **33%TOTAL used**,67%remaining,57percentagepoints before90%;same reset1792745187. Raw11:23:11UTC audit **692,855,018total**,654,942,464cachedinput,32,115,273uncachedinput,5,797,281output including2,570,849reasoning; uncached+output37,912,554.62historicalsession sums match across4236responses. Repeatedcontextcounts exclude unreported in-flight work; no billing/weeklyconversion. Owned keepawake verified21:23:11Brisbane. Continue reasoning/review with integration reserve.


At2026-10-17 11:44:10UTC, directaccountmeter35%TOTALweeklyused/65%remaining,55percentagepointsbefore90%;reset1792745187unchanged. Raw11:44:42UTC projectaudit727,699,511total,687,901,952cachedinput,33,763,570uncachedinput,6,033,989output including2,656,326reasoning;uncached+output39,797,559.62sessions4399responses,allrecordedsumsmatch. No bill/weeklyconversion. Ownedawakeverified21:44:11Brisbane. Research/reviewcontinues.


Current12:03UTCtransition:36%TOTALweeklyused,64%remaining,54ppbefore90%,samereset1792745187. Raw12:02:35UTC753,899,483total,712,634,112cachedinput,35,041,697uncachedinput,6,223,674outputincluding2,738,377reasoning;uncached+output41,265,371.62sessions/4519responses,allsumsmatch. No bill/weeklyconversion. Researchandreviewcontinuewithreserve.


12:14UTC transition:36%TOTALweeklyused,64%remaining,54ppbefore90%;same reset1792745187. Raw12:12:42UTC767,693,674total,725,832,704cachedinput,35,519,697uncachedinput,6,341,273output including2,780,168reasoning;uncached+output41,860,970.62sessions/4586responses,all sums match. Not a bill/weeklyconversion. Research continues.


12:30UTC transition:37%TOTALweeklyused,63%remaining,53ppbefore90%;same reset1792745187. Raw12:29:08UTC787,359,028total,744,739,968cachedinput,36,120,727uncachedinput,6,498,333output including2,853,610reasoning;uncached+output42,619,060.62sessions/4683responses,all sums match. Not a bill/weeklyconversion. Owned awake verified22:25:48Brisbane. Research continues.


12:52UTC checkpoint:39%TOTALweekly used,61%remaining,51ppbefore90%,samereset1792745187. Raw12:52:11UTC816,309,618total:771,828,736cachedinput,37,744,122uncachedinput,6,736,760output including2,956,346reasoning;uncached+output44,480,882.62historicalsessions/4831responses,allsumsmatch. Not a bill or weeklyconversion. Ownedawakeverified22:52:11Brisbane. Continue reasoning/review with reserve.


13:09UTC checkpoint: directaccountmeter40%TOTALweekly used/60%remaining,50ppbefore90%,reset1792745187. Raw13:09:25UTC848,458,187total:802,819,584cachedinput,38,717,948uncachedinput,6,920,655output including3,029,830reasoning;uncached+output45,638,603.62sessions4964responses,allsumsmatch. No bill or weeklyconversion. OwnedawakePID79293/session64368 lastverified22:52:11Brisbane; continue until90%TOTAL withreview/integrationreserve.


13:25UTC checkpoint: direct accountmeter41%TOTALweekly used/59%remaining,49ppbefore90%, reset1792745187. Raw13:24:54UTC864,439,418total:818,011,904cachedinput,39,380,110uncachedinput,7,047,404output including3,067,235reasoning;uncached+output46,427,514.62sessions5044responses,allrecordedsumsmatch. No bill or weeklyconversion. Continue with review/integrationreserve and targetedownedawakecleanupat90%oractualend.


13:44UTC checkpoint:42%TOTALweeklyused/58%remaining,48ppbefore90%,reset1792745187unchanged. Raw13:44:34UTC889,687,784total:841,892,736cachedinput,40,609,444uncachedinput,7,185,604output including3,136,190reasoning;uncached+output47,795,048.62sessions5150responses,allrecordedsumsmatch. No bill/weeklyconversion. Ownedawakeverified23:44:21Brisbane;continuewithreserve.


2026-10-17 14:15:57UTC: authoritative accountmeter43%TOTALweeklyused,57%remaining,47ppbefore90%TOTAL. Reset1792745187 unchanged. Raw snapshot14:10:12UTC917896364total,868704512cachedinput,41813767uncachedinput,7378085output including3210188reasoning;uncached+output49191852. All62session sums match;5296deduplicatedresponses. Notabillorweeklyconversion. Ownedawakeverified00:15:57Brisbane. See status-2026-10-17-1416.md.


2026-10-17 14:39:13UTC: direct accountmeter45%TOTALweeklyused/55%remaining,45ppbefore90%,reset1792745187unchanged. Raw14:39:31UTC966583508total including914768000cachedinput,44132888uncachedinput,7682620output including3308645reasoning;uncached+output51815508.62sessions/5517responses,allrecordedsumsmatch. No bill/weeklyconversion. Seven new scoped packets accepted;two full annual answers unchanged. See status-2026-10-17-1440.md. Research continues with integration reserve.


2026-10-17 15:00:09UTC: direct meter46%TOTALweekly/54%remaining/44ppbefore90%,same reset1792745187. Raw991254322total,938481024cachedinput,44899583uncachedinput,7873715output including3412126reasoning;uncached+output52773298.62sessions/5615responses,allsumsmatch. No bill or weeklyconversion. OwnedawakePID79293 verified01:00:09Brisbane,assertingforever. See status-2026-10-17-1501.md;research continues.
