# Code scope and reproducibility record

2026-10-18 UTC. **Candidate proof - unverified.** There is NO mathematical program for CN1--CN3: no generation of histories, ruler words, reachable vertices, canonical factors, matrices, automata, large tables, floating-point constants or CAS expressions, and no old certificate replay. All formulas and the h=3 arithmetic in the main/checks files were obtained and checked by hand.

The only new executable is `reasoning-cut-number-r3-validate-v1.py`. It is an administrative byte/SHA-256/JSON validator, confined in its WRITES to this assigned new prefix. It binds necessary accepted inputs, checks agreement with their acceptance records, verifies the immediate parent whole-review manifest, records compact metadata counts, and freezes the NEW payload files. It does not inspect mathematical example data or call an external process, network service, package or mathematical library.

Administrative commands, run from `/Users/uqmkamga/Documents/ChatGPT/Website`:

```
python3 problems/2019-B4/notes/reasoning-cut-number-r3-validate-v1.py --baseline
python3 problems/2019-B4/notes/reasoning-cut-number-r3-validate-v1.py --freeze
python3 problems/2019-B4/notes/reasoning-cut-number-r3-validate-v1.py --verify
```

The first creates only the new baseline and refuses an existing output. The second revalidates inputs and emits the new integrity report and freeze; it refuses overwrites. The third is read-only and must pass after full generated-metadata readback. The exact command output is retained by the tool transcript and the metadata files. No long native operation, timeout, child PID, incomplete mathematical run or cleanup exists. `rg` searches and ordinary `cat`/`sed` reads are source discovery/readback, not mathematical enumeration.

The script's own bytes are frozen as a payload. Its administrative validation is not an independent mathematical review. TWO OTHER initially blind ENTIRE WHOLE audits remain required.
