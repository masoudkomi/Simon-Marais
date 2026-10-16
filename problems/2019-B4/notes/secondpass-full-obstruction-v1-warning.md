# Historical restricted probe: v1 is not a full obstruction enumeration

2026-10-16. The runs saved as
`computations/secondpass-full-obstruction-initial*` and
`computations/secondpass-full-obstruction24*` used the preserved source
`computations/secondpass-full-obstruction-probe-v1.py`.

That source unnecessarily fixed the final three history letters `RLL`.
The proved general restriction is only the final `LL`; a final run of
three or more L's was not excluded by a theorem. Consequently the v1
output's completed layers are complete only for that restricted suffix
class, regardless of their generic `complete` fields. They must not be
used as complete coefficients of the full obstruction series. Their
individual context-collision witnesses remain valid finite evidence.

This was noticed before any mathematical result used those counts. The
current `secondpass-full-obstruction-probe.py` fixes only `LL`, and its
separately named v2 jobs/outputs supersede the v1 counts. The exact original
source and outputs are retained to make the failure and correction
reproducible. Frozen checkpoint-1 counts came from the independent fully
exhaustive 20-move generator and are unaffected. The bounded-run core probe
is also unaffected, since in its class a final `LL` must be preceded by R.
