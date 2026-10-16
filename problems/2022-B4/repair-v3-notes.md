# 2022 B4(b): constructor repair notes, 2026-10-16

Status: **candidate proof - unverified**. These are author repair notes,
not an independent review and not a coordinator promotion.

## Acknowledged error and preserved versions

The v2 local hitting-path estimates were valid, but I incorrectly treated
their initial-state bound K(d_initial) as reusable after every surviving
prefix. The current difference can change. Both reviewers supplied actual
admissible prefixes showing that the claimed conditional block bound fails:

- R1: (599,600) reaches (795,792), state (3,12), after three avoiding
  steps. The v2 initial bound is 3, but four further abstract steps are
  needed.
- R2: (25,24), with product exactly 600, reaches (33,27), state (6,27),
  after four avoiding steps. The v2 initial bound is 4, but five further
  abstract steps are needed.

These refute v2's repeated-block premise. They do not refute the fixed-
offset density claim. V2 is retained unchanged as a failed proof version.
Neither reviewer found a substantive defect in v1 P1-P4, but the author
has not promoted any status; that decision belongs to the coordinator.

## Constructor repair

The new standalone `proof-extension-v3.md` reconstructs all needed steps.
With exact integer floor remainders u=(r+d) mod30 and v=r mod20,
`10D(d,r)=9d+u-v`, where `0<=u<=29`, `0<=v<=19`, including negative
r+d. Thus `|D|<=(9|d|+29)/10`. For fixed initial difference delta,
`M=max(|delta|,29)` bounds every reachable difference, under every
finite control word. The same analytic sign policy then has at most
M further updates after its first update, giving the fixed uniform
`K=M+1` from every reached state.

This makes the conditional loss factor `1-10^(-K)` valid at every block
boundary. The lifting bijection and periodic-class density argument are
reconstructed in full in v3. The auxiliary radius depends on the initial
difference and is used only in this equality-density proof; no narrow
eventual trapping claim or preliminary (a) proof is reproduced.

The repair is mathematical, not computational. The finite checks below
are supporting evidence and are not premises of an unrestricted theorem.

## Frozen fingerprints

| Object | SHA-256 |
|---|---|
| proof.md v1 | 8b35be18bb70f81b623f78e7dd1a148478c698c1f5ad32e4097def92ff75aed3 |
| proof-extension-v2.md | b41aff3fcfadd33f80fdec80570d5b2f61807a5b9e16a28becacefaa237743ed |
| proof-extension-v3.md | 0238f99a93b0ba1076484db1c16b173efcc02be4410e859f2c5bafc55f0f2a3f |
| reviews/review-1.md | 6f7f8fa9ce0bcc08ed0738f2db587ad2ef1e0c5f269d9aac975033c8cfe29e60 |
| reviews/review-2.md | 1fe554ad4e5c77a1cad18a739a05b7ad1ceba4a8bce0beee91d6d34eedefbc04 |

V1, v2 and both initial review reports were fingerprinted before and after
the evidence run and stayed unchanged. V3 is a separate file. The reports
and their evidence files were read only; no reviewer-owned file was edited.

## Reproducible finite evidence

Run from `/Users/uqmkamga/Documents/ChatGPT/Website`:

```sh
.venv/bin/python -u problems/2022-B4/computations/v3_repair_evidence.py --tag v3-repair
```

This exact run generated `computations/v3-repair-job.json` and
`computations/v3-repair-output.txt`. The standard-library supervisor
launched a dedicated child, PID 12143, with a 40-second timeout and
incremental checkpoints. It completed with return code 0 in 0.778 seconds;
no cleanup signal was needed and no job remains outstanding. A rerun
must use a fresh `--tag` to preserve the initial output files.

Python was 3.12.14. No package, native CAS, API, network access, installation,
or unrelated process was involved. Exact finite checks covered:

- 1,200,060 remainder-identity and numerical-bound instances for
  -10000<=d<=10000, 0<=r<60;
- every state in radii 29,30,60,100,333 (66,540 state/radius instances),
  checking the invariant radius and the analytic policy length against K;
- both actual reviewer prefixes, their old local bounds, and minimum
  further abstract hitting lengths 4 and 5 by finite BFS;
- 147 complete lifting bijections of lengths 1-3, over 54,390 quotient
  classes, including large positive and negative fixed differences.

The maximum observed policy lengths in those radii were 28,28,35,40,52,
respectively, below the analytic bounds 30,31,61,101,334. These measured
maxima are not substituted for the analytic uniform bound.

## Re-review request and unresolved full question

Both independent reviewers must re-audit the repair, especially v3
Sections 3-6. The required question is whether the same K is valid at
every prefix and whether the lifting/counting argument then proves the
stated fixed-offset density conclusion. Keep the earlier initial reports
immutable and record affected-argument re-review separately.

The never-hit set can have natural density zero and still be nonempty.
No individual exceptional integer has been excluded by the density proof,
and no universal equality answer or two-dimensional density result is
claimed. The full B4(b) question remains unresolved in this work.
