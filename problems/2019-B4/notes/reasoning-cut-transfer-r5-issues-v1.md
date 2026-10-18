# Constructor issues and adversarial checks — BT1–BT4

2026-10-18 UTC. **Candidate proof - unverified.** This is the author's
issue/check record, not either required independent whole audit.
No external verification or absence-of-error assertion is made.

| Item | Disposition before freeze |
|---|---|
| I1 — A terminal tape piece is not generally a terminal HISTORY block | Choose the history cut before its first selected letter and retain ALL later other-tape moves. The remaining history really is terminal; the prefix is actual. |
| I2 — An initial tape piece may be preceded by other-tape moves | Include those moves in the initial history block. The suffix phase is determined by ell+m; complement both suffix words when odd. |
| I3 — Usual submultiplicative direction is insufficient | Explicitly use accepted R7's strict consecutive ratio bound to control c_p/c_n. Reversing ordinary submultiplicativity would be false reasoning. |
| I4 — Independent walk sampling would change the measure | The middle path counts are upper bounds inside an injective encoding of DISTINCT actual contexts, with an actual prefix or suffix. |
| I5 — Constant selected words have unbounded range | Give a separate avoid-bb argument for the other word; do not subsume them under a fixed height range. |
| I6 — Composed output is not uniform | Exact pushforward k/(c_n c_m) is retained. Harmonic identity is under independent inputs, while A is the uniform-output mean. |
| I7 — A bare height-zero vertex is not feasible | J counts only prefix-AND-suffix actual cut vertices, then drops feasibility only for an upper bound. |
| I8 — Cut shift may run beyond a tape | Such a signed distance contributes no candidate. Words are exact suffixes/prefixes, never cyclic factors. |
| I9 — Tail constants count indicators, not merely the event of one contact | At each distance sum both signed indicators separately; the same union-sum bound controls their expectation. |
| I10 — Size bias can magnify rare large fibres | No positive-defect converse or bound on E_x k is inferred from bounded A. |
| I11 — New residual theorem could be mistaken for regime selection | Delta=0 is an explicit hypothesis in divergence and finite-mu quantiles. No estimate rules out U. |
| I12 — A guard counterexample could be overgeneralized | BT4 concerns the exact (0,1) separator with fixed first/last windows and maximum-run-one restriction, not arbitrary markers. |

## Additional whole checks performed by hand

The path-vector inequalities include m=0, ell=1, reduced actual range,
both starting phases and both tapes. Their rational comparisons use only
lambda>7/4. For ell>n and any empty tape the relevant end event is false.
The four-end union implicit in alternative cuts is distinct from the
four selected height intervals in the range-three count.

For words of length at most four, either their range is at most three
or they are constant. Therefore the residual U has no displacement
of absolute value at most four. This agrees with all small-degree cases;
it is not needed to improve a constant or infer a large-degree result.

At n=0 or m=0 the map has one cut, A=1 and J=U=0. The lower bound
A-1-M may be negative and remains a valid lower bound, not a claimed
positive expectation in those cases. The bound for z^J requires
z>1 and z^2 alpha<1 before summing; no endpoint equality is included.

The harmonic lower-tail inequality applies to real thresholds as well
as the integer values actually used. D_n=floor(sqrt(A_n)) is chosen
only under A_n->infinity, and D_n=floor(sqrt(n)) only in the finite
critical argument. Empty terms at n=0 do not enter a limit.

The separator restriction has N-2w-3 choices, with at least two
when N>=2w+5. Every tape is long enough for both end windows, even
if the windows are allowed to overlap in other possible inputs.
The rarity statement concerns the listed subfamily only.

## Open research issues, not assumed premises

U is not bounded in mean, in probability or by a deterministic detector.
There is no classification of the remaining nonconstant large-range
transfers, no all-range end estimate, no pressure regularity theorem,
no selection of delta or mu, and no exact lambda. Those gaps are retained
in the main and failed-route log. Both OTHER whole audits must reconstruct
all56 obligations and every companion; root alone can promote a result.
