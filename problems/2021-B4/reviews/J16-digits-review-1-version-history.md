# R1 source version and metadata history

All mathematical audit runs passed. Exact commands, source hashes, PIDs,
timeouts and outputs are in the five job records. No candidate source
was changed and no peer conclusion was read.

- `verifier-initial-v0.py` is the exact source used for the first 8192-case
  benchmark and saved before constructor serialization/data were opened.
  The current verifier adds result statistics, constructor serialization
  hashing and an independent determinant-based affine check. It changes
  the displayed leading-test count to count only cases after the stated
  constant prerequisites; the separate pre-prerequisite count is retained.
- `tree-precomparison-v0.txt` is the exact arbitrary-precision evaluator
  saved before owner source/data. An assertion's missing parentheses were
  fixed before any execution; all evaluator formulas were unchanged.
- `tree-audit-benchmark-v0.py` is the exact source for the extension
  benchmark. The complete-run source removes one unused local comprehension
  that created irrelevant dictionary keys; it changes no checked value.
- The final metadata archiver's first invocation,
  `.venv/bin/python problems/2021-B4/reviews/J16-digits-review-1-freeze.py`,
  stopped at its hash assertion before writing any archived source or
  manifest. Its reverse reconstruction had omitted the original `totals`
  and `passed` counter lines, producing hash
  `65edefa6f3efe8a68c6f143582562e32e6f812a3f886941aca079e7efcfd902a`
  instead of required
  `b53811a0f4a7c30c5492e662a9e496e3ba6263a36eb6c0138c7f6141fbd2ac8d`.
  Restoring those two original counter updates repaired the metadata
  reconstruction. This did not rerun or change any mathematical audit.

The original R1 benchmark is deliberately incomplete. Its per-mask
`next_extra_excluded` and `next_all_excluded` fields are provisional
unvisited-mask bookkeeping and have no exclusion credit. Only the complete
full-run outputs support the report's finite exclusions.
