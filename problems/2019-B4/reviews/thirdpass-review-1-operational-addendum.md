# R1 operational addendum after initial report freeze

2026-10-16 UTC, immediately after the 17:34:59 initial freeze. This addendum
does not change the initially blind mathematical findings or the report's
SHA-256 `0ceec50769c77f656f7765a2ea309921d893eb3a0e0be1045ef9255d5e4d953a`.
No peer third-pass review conclusion has been read before this addendum.

The `compare` mode explicitly imports the author's monitor only after the
independent construction. Python's source loader wrote or refreshed the
ignored cache

    problems/2019-B4/computations/__pycache__/thirdpass-delay-automaton.cpython-315.pyc

Its observed modification time is `2026-10-16T17:23:55.723556+00:00`, within
the recorded comparison job. This is an operational exception to the
initial report's literal claim that all writes were confined to the
reviewer's filename prefix. All intentional research-artifact edits were
confined to that prefix, and every one of the 70 frozen author source/data
files is unchanged. The exception neither supplied the independent initial
verifier nor changes any proof, state transition, vector, or result.

I did not remove or overwrite the cache afterward, since its pre-review
existence was not recorded and it may have been a pre-existing shared cache.
Future reproductions should run the saved comparison with bytecode writes
disabled, for example by launching its supervisor with

    PYTHONDONTWRITEBYTECODE=1 python3 problems/2019-B4/reviews/thirdpass-review-1-run.py compare 60 compare

The initially frozen report and all verifier versions remain byte-for-byte
unchanged. The original review manifest, SHA-256
`3733b86d1dea6cd3cb28e0342e73e4ee9fbf664bd6df911b75d4e866eb5ee3b6`,
and its hash list are retained as `thirdpass-review-1-manifest-initial.json`
and `thirdpass-review-1-sha256-initial.txt`. The current manifest additionally
includes this addendum and the two original freeze artifacts. No mathematical
repair or re-review is requested because of this cache side effect.
