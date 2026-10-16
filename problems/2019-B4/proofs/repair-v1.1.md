# 2019 B4(b): attribution repair, version 1.1

Date: 2026-10-16. Author: `owner_2019`.

Status: **candidate proof - unverified**. No author promotion, commit or
push. The exact growth constant remains undetermined.

Both blind initial audits are complete in `reviews/review-1.md` and
`reviews/review-2.md`. The author read them only after the coordinator
confirmed their independent completion. Both report no substantive
mathematical gap and independently reproduce the context counts and exact
certificate. R1-E1 requests a minor attribution clarification; R2 requests
no mathematical repair.

## Repair made

Section 3 of `proof.md` now explicitly credits the official 2019 solution
notes, page 11, for the four-move `RRLL -> LLRR` relation and the method of
obtaining avoiding representatives. It distinguishes the present
investigation's additional twelve-move relation and combined finite
automaton certificate, and disclaims a global-novelty assertion.

The other proof changes are confined to version and review-status
annotations: the heading, opening paragraph, certificate review-status
sentence, and final remaining-work sentence. No definition, mathematical
hypothesis, inference, formula, numerical value, vector, matrix or
certificate changed. The coordinator's separate two-tape exploratory note
has not been incorporated into this repair.

The v1 issue-log entries are retained as the initial audit-request record.
A new `2019-R1-E1` author-repair entry records the attribution change and
pending reviewer recheck. The author has not closed reviewer issues.

## Exact objects

```text
227cff77dc63aba6125494e6e39e3feb687fe4b8a3ff90d4392d72b4133e5a1e  proofs/candidate-v1.md (exact reviewed version 1)
bcb05ede335a09d0d2d50f0b2b076b7ad5d408fe2557e1361dbb7b0439a3f48b  proof.md (candidate version 1.1)
4f4632e7eb8ecfb7e273b035c4bfa1bfa7d70dd5fa4896f613fdb5bc96edab80  proofs/attribution-v1-to-v1.1.diff
```

The archive was created as an exact byte copy before editing and checked
against the coordinator-supplied v1 hash. The diff was generated with
Python 3.12.14 `difflib.unified_diff`; its whole contents are the attribution
paragraph and the version/review-status annotations described above.

The following mathematical scripts and evidence outputs retain their
pre-review SHA-256 values:

```text
49795106e48cbb880f086f33f1b532cefc43c82ae3135834195e02a481220b1d  computations/upper_certificate.py
da9278d68e22914bfb63457459f597dcbb3aeb9de55ba0ebd9837e4db151ea03  computations/upper-certificate-2026-10-16.json
cb8c21a83f51ee2e065eebb6ee1d01617f75fefe26d5609957f892cb429a0645  computations/enumerate.py
a2b5c5e7d40afa68dc8f2704988f17fcb749da4921202ddbf533e381b06477ba  computations/enumeration-2026-10-16.json

```

No enumeration or matrix run was repeated because neither computation nor
its mathematical application changed. The archived source hash, preserved
computation hashes, and exact text diff are the relevant checks for this
attribution-only revision. The coordinator should obtain R1's targeted
recheck against the new proof hash before considering issue closure or
status promotion.

`git diff --check -- problems/2019-B4` completed with exit code zero after
the repair. Reviewer files and the separate exploratory note were not edited.
