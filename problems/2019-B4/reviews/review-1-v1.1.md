# 2019 B4(b): R1 targeted attribution recheck, version 1.1

**Recheck complete, 2026-10-16. R1-E1 is resolved.** This supplements and
preserves the blind initial report `review-1.md`; it does not replace that
report or promote the candidate's status.

Reviewed objects:

```text
227cff77dc63aba6125494e6e39e3feb687fe4b8a3ff90d4392d72b4133e5a1e  proofs/candidate-v1.md
bcb05ede335a09d0d2d50f0b2b076b7ad5d408fe2557e1361dbb7b0439a3f48b  proof.md (candidate v1.1)
4f4632e7eb8ecfb7e273b035c4bfa1bfa7d70dd5fa4896f613fdb5bc96edab80  proofs/attribution-v1-to-v1.1.diff
```

I read `proofs/repair-v1.1.md` and the saved diff. I independently generated
the complete unified diff between the archived v1 and current v1.1 with
Python 3.12.14 `difflib.unified_diff`, using retained line endings and the
same source/target labels. It matches the saved diff byte for byte. The
archived file's SHA-256 matches the exact object audited in my initial R1
report.

The four diff hunks consist only of:

- the version heading and initial review-status paragraph;
- the added Section 3 attribution paragraph;
- the certificate review-status sentence;
- the final remaining-work/status annotation.

The new Section 3 paragraph explicitly credits the official 2019 solution
notes, page 11, for both the four-move `RRLL -> LLRR` relation and the method
of obtaining avoiding representatives. It identifies the additional
twelve-move relation and combined finite automaton certificate as additions
of the present investigation, with an explicit disclaimer of global
novelty. This directly and fully addresses R1-E1. The paragraph introduces
no additional mathematical claim requiring a new audit.

I verified that no mathematical definition, hypothesis, inference,
formula, integer, vector, matrix or certificate in the candidate body was
changed. The four computation source/output hashes remain:

```text
49795106e48cbb880f086f33f1b532cefc43c82ae3135834195e02a481220b1d  computations/upper_certificate.py
da9278d68e22914bfb63457459f597dcbb3aeb9de55ba0ebd9837e4db151ea03  computations/upper-certificate-2026-10-16.json
cb8c21a83f51ee2e065eebb6ee1d01617f75fefe26d5609957f892cb429a0645  computations/enumerate.py
a2b5c5e7d40afa68dc8f2704988f17fcb749da4921202ddbf533e381b06477ba  computations/enumeration-2026-10-16.json
```

The original independent R1 check script, JSON output and log also retain
the three SHA-256 values recorded in `review-1.md`. All ten version, diff,
computation and R1 evidence hash checks passed. No enumeration or matrix
calculation was repeated because its inputs and application are unchanged;
the original check script remains pinned to the originally reviewed v1.

My initial mathematical findings therefore carry over to candidate v1.1,
and no objection remains from R1. The common growth constant is still not
explicitly evaluated, so the work remains partial progress on (b). Any
issue-log closure and promotion after the two audits belong to the
coordinator. This recheck changes neither the proof nor its status, and
does not incorporate or audit any separate exploratory note.
