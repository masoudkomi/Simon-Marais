"""Text-only author repair builder; creates new full versions, never edits v1.

This does not evaluate a mathematical expression, scan parameters, or rerun
an earlier program. The exact replacements and unified diff are preserved.
"""

from datetime import datetime, timezone
import difflib
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2020-B4/notes/reasoning-return-r4-"
NOW = datetime.now(timezone.utc).isoformat()


def read(suffix):
    return (ROOT / (PREFIX + suffix)).read_text()


def replace_once(text, old, new):
    assert text.count(old) == 1, old
    return text.replace(old, new, 1)


def write_new(suffix, text):
    with (ROOT / (PREFIX + suffix)).open("x") as stream:
        stream.write(text)


def fingerprint(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


main_old = read("candidate-v1.md")
main = replace_once(main_old, """2026-10-17 UTC. **Candidate proof - unverified.** Constructor:
`review_2022_complexity_r2`. Requested `gpt-6.1-sol` with `max`
reasoning; independent effective-setting readback unavailable. No part of
this new packet has been independently reviewed. Two fresh nonconstructor
whole audits and coordinator reconciliation are required before promotion.
""", """2026-10-17 UTC. **Candidate proof - unverified, full replacement v1.1.**
Constructor `review_2022_complexity_r2`; requested `gpt-6.1-sol` with `max`
reasoning, independent effective-setting readback unavailable. Both
initially blind nonconstructor WHOLE v1 audits are frozen and preserved.
Reviewer2 correctly found substantive auxiliary error R4R2-01: the author
falsely called the last moment congruence essential. Reviewer1's initial
report missed that assertion. This replacement corrects it, proves the
last row automatic and the earlier rows sufficient, and keeps the entire
valid full E2 iff. Both reviewers must re-audit the affected arguments
before coordinator acceptance. Neither old report is retroactively edited.
""")
main = replace_once(main, r"""The final equation is essential; the first congruences alone are
not a sufficient test. The index \(m\) here is the **order** of
the multiplicative subgroup. Its usual cyclotomic index is \(L\),
so source notation using the index must not be substituted blindly.
""", r"""The final congruence is AUTOMATIC for every actual size-\(k\) subset
of \(\mathbb F_\ell\), before imposing any earlier congruence. It is
included in E2 to display the full target moment sequence. For these
prescribed \(D_\epsilon\), the earlier even-index congruences alone
are already sufficient; the proof below also establishes this shorter
criterion. Redundancy does not change the final target value from
\(-1\) to zero. The index \(m\) here is the **order** of the
multiplicative subgroup. Its usual cyclotomic index is \(L\), so
source notation using the index must not be substituted blindly.
""")
insert_before = r"""When \(L>2\), the first interior congruence \(t=2\) yields
"""
new_moment_proof = r"""**Automatic final row and sufficient interior list (R4R2-01 repair).**
For ANY actual subset \(A\subset\mathbb F_\ell\) of size \(k\)
with \(k(k-1)=\ell-1\), Fermat's theorem gives

\[
\sum_{a,b\in A}(a-b)^{\ell-1}
  =\#\{(a,b)\in A^2:a\ne b\}
  =k(k-1)=-1\quad\text{in }\mathbb F_\ell.             \tag{E2a}
\]

The diagonal contributes zero and every off-diagonal field summand is
one. In particular \(B_L\equiv-1\pmod\ell\) holds for the actual
\(D_\epsilon\), independently of every preceding test. There is also
a direct check of its formula: for \(1\le i\le L-1\),

\[
\binom{\ell-1}{im}\equiv(-1)^{im}\pmod\ell,
\qquad (-1)^i(-1)^{im}=1
\]

because \(m\) is odd. Thus

\[
B_L\equiv2mk+m^2(L-1)
      =(m+1)\ell-1\equiv-1\pmod\ell.                 \tag{E2b}
\]

The intermediate integer identity uses the exact definitions of
\(k,L,\ell\); no earlier moment equation is used.

For completeness, sufficiency can be recovered WITHOUT using the last
moment at all. Suppose the interior equations \(B_t=0\) for even
\(2\le t<L\) hold. E3/E4 and odd-pair cancellation give all positive
moment equalities at \(1\le j\le\ell-2\), and the constant moments
are already equal. Also \(\mu(0)=\nu(0)=k\) EXACTLY for the actual
subset. Delete this known zero coordinate. The remaining square matrix

\[
(z^j)_{0\le j\le\ell-2,\ z\in\mathbb F_\ell^\times}
\]

is invertible: a polynomial of degree at most \(\ell-2\) with all
\(\ell-1\) distinct nonzero roots is zero. Consequently the count
vectors agree modulo \(\ell\) at each nonzero residue, and the same
bound \(0\le\mu(z)\le k<\ell\) lifts the count to the integer one.
Necessity of the interior equations follows from an actual difference
set as before. Therefore E2 is equivalent to its interior list alone,
including an empty interior list when \(L=2\). This is a correction
of the false v1 necessity/insufficiency assertion, not an unproved
new external import. The full-matrix proof and full E2 list above remain
valid with the redundant last row retained.

"""
main = replace_once(main, insert_before, new_moment_proof + insert_before)
main = replace_once(main, """candidate partial claims until two fresh whole audits have completed.
""", """candidate partial claims pending BOTH affected v1.1 re-audits and
coordinator reconciliation; both original whole initials stay preserved.
""")
main = replace_once(main, """theorems. Passing a shortened list of moments, an orbit-size subset
sum, or a real norm identity is not promoted to existence. No full
taut classification, cyclic prime-power conjecture, numerical answer
or new published cutoff follows from this packet.
""", """theorems. For the prescribed shapes here the interior E2 list IS
sufficient, because the omitted final row is automatic and the actual
zero count is known, as proved above. A different shortened moment
list, an orbit-size subset sum, or a real norm identity is not promoted
to existence without a valid reconstruction argument of its own. No
full taut classification, cyclic prime-power conjecture, numerical
answer or new published cutoff follows from this packet.
""")

oblig_old = read("obligations-v1.md")
oblig = replace_once(oblig_old, """All references are to the complete `reasoning-return-r4-candidate-v1.md`.
""", """All references are now to the FULL `reasoning-return-r4-candidate-v1.1.md`.
Both original whole audits and the v1 bytes are preserved. Reviewer2's
R4R2-01 was a real author error, not a stylistic issue; the revised rows
and the eight repair obligations below require BOTH affected re-audits.
""")
oblig = replace_once(oblig, """self-checks and requests for two fresh independent nonconstructor
whole audits, not an independent review or coordinator acceptance.
""", """self-checks and requests for BOTH affected nonconstructor v1.1 re-audits,
not an independent review or coordinator acceptance.
""")
oblig = replace_once(oblig,
    "|R4-O28|Odd moments and the full last index.|Ordered-pair reversal cancels every odd moment in odd characteristic. Even t range2..L includes j=ell-1; its target is -1, not0.|",
    "|R4-O28|Odd moments and the automatic final index.|Ordered-pair reversal cancels every odd moment in odd characteristic. The final target is -1, not0; E2a/Fermat and E2b/binomial proofs show that this row is AUTOMATIC before earlier tests.|")
oblig = replace_once(oblig,
    "|R4-O30|All moments imply residue-by-residue equality.|The square Vandermonde evaluation matrix at ALL ell field elements is invertible. Degree at most ell-1 root-count proof includes the separate constant row. A truncated list alone would not justify this step.|",
    "|R4-O30|Full and reduced matrix recovery.|The ALL-field matrix with degrees0..ell-1 is invertible as before. For the shorter list, the actual known mu(0)=nu(0)=k permits deletion of that coordinate; degrees0..ell-2 at ALL ell-1 nonzero residues give a second square invertible matrix. No unjustified general shortened-list warning remains.|")
oblig = replace_once(oblig,
    "|R4-O32|Sufficiency and necessity are both established only for these fixed shapes.|E2 enumerates all nonautomatic moments, so it is an iff for D_epsilon. It is not an iff for a general cyclic set or for existence at arbitrary q with small multiplier group.|",
    "|R4-O32|Both directions and redundant-row qualification for actual fixed shapes.|The INTERIOR E2 rows cover all nonautomatic moments; its final row is redundant. Both the full E2 system and its interior list alone are iff tests for these prescribed D_epsilon. This does not classify a general cyclic set or arbitrary q with a smaller multiplier group.|")
oblig = replace_once(oblig, """- Obtain two initially blind whole independent audits of this exact
  frozen packet. The author's self-checks above do not count as either.
""", """- Preserve both complete initially blind whole v1 audits, and obtain
  BOTH affected v1.1 re-audits before coordinator acceptance. The
  author's correction does not count as either independent re-audit.
""")
oblig += """
## Explicit repair obligations

|ID|Repair inference or preservation check|Author disposition, pending independent review|
|---|---|---|
|R4-R01|Acknowledge the exact false auxiliary claim and both initial dispositions.|R4R2-01 is accepted as a real author error. Original v1, root R1 pass/miss and C R2 finding remain frozen. No retrospective edit.|
|R4-R02|Automatic last moment for ANY actual size-k subset.|Every off-diagonal nonzero field difference has power ell-1 equal1; diagonal contributes0; k(k-1)=ell-1. No interior equation or difference-set conclusion assumed.|
|R4-R03|Independent signed-binomial calculation.|binom(ell-1,im)=(-1)^(im) mod ell, m odd; all L-1 interior sign-corrected summands are1; 2mk+m²(L-1)=(m+1)ell-1.|
|R4-R04|Interior moments and constant row cover all degrees0..ell-2.|Nonmultiples of m and odd powers are automatic; remaining even multiples have t<L; constant k² agrees by parameters.|
|R4-R05|The zero coordinate is actually known and the reduced matrix is square.|mu0=nu0=k EXACTLY, since D is a subset; after subtracting this coordinate there are ell-1 columns and degrees0..ell-2; polynomial root count proves invertibility.|
|R4-R06|Exact integer lifting, L2 and final target value.|The same small coefficient bound gives integer1; L2 allows an empty interior list, but final target remains-1. E5 still requires L>2. No preliminary construction researched.|
|R4-R07|All affected explanations corrected and mathematical core preserved.|Main preamble/E2 explanation/redundancy proof/closing warning and O28/O30/O32 corrected. Entire R4A-D body, actual q4 counterexample, E1-E5 formulas/full iff and all exact prior premises retained.|
|R4-R08|Full replacement, exact diff, old-byte preservation and review status.|New versioned complete files only; both full reports/ledgers/sources read; input/source/own hashes checked; both affected re-audits required, no promotion or full classification.|
"""

source_old = read("source-checks-v1.md")
source_header = """**Candidate proof - unverified, full versioned source record v1.1.**

2026-10-17 UTC. R4R2-01 author repair. The COMPLETE original candidate,
all36 obligations, both whole v1 reports, both full inference/issue
ledgers and both source-check records were read after the separate2022
R5 construction froze. The issue is an elementary internal error, not
an objection to Cohen, Hall, Xia or an old accepted premise. The final
moment is automatic; interior sufficiency is proved by the actual known
zero coordinate and the nonzero-residue Vandermonde. No new external
theorem, source proof audit, mathematical computation or scan is used.

The complete ORIGINAL source audit follows as a byte-identical suffix.
Its source visits describe the original construction pass, not fresh
visits repeated by this repair. All those exact hypotheses, imports,
cache fingerprints and limitations remain unchanged. Both independent
affected v1.1 re-audits are still required. The companion new JSON
distinguishes the original source reads from the current full repair
reads and hashes both original whole audits without altering them.

---

"""
source = source_header + source_old

worklog_old = read("worklog-v1.md")
worklog_header = """**Candidate proof - unverified, full versioned worklog v1.1.**

# Author repair of R4R2-01

2026-10-17 UTC. Only new versioned reasoning-return-r4-* files are
written. Original v1 and both independent whole initials stay unchanged.
After the COMPLETE2022 R5 proof/42-obligation/source/log/failure freeze,
the author read BOTH full2020 R4 whole reports, their complete ledgers
and source checks, plus the original full proof and ancillary records.
Root R1 missed the auxiliary error; C R2 identified it correctly. The
author accepts responsibility for the false necessity/insufficiency claim.

The correction is substantive but localized. Every actual size-k subset
already has final difference moment k(k-1)=-1 mod ell by Fermat. The
separate signed-binomial formula gives the same identity. The interior
E2 equations plus automatic lower moments and the EXACT zero count
give an invertible evaluation matrix on F_ell^*. Thus that interior
list is sufficient. Full E2 and R4A-D remain valid, and the final target
does not change from-1 to0. All original claims outside this correction,
including E5's L>2 boundary, stay within the same scope.

Created: full replacement candidate-v1.1, complete revised obligations
with36 original/eight repair rows, complete versioned source audit/JSON,
this complete log, detailed repair ledger, exact unified diff, text-only
builder and metadata-only freeze/check records. The old source audit
and old worklog follow in the new records as explicit HISTORICAL suffixes,
so old chronological statements are not represented as current verdicts.

Text editing is reproduced by:

    python3 problems/2020-B4/notes/reasoning-return-r4-build-repair-v1.1.py

The builder performs exact asserted text replacements and a unified diff;
it does not evaluate the binomial system, run tests, use CAS, scan orders
or rerun an old author program. The new freeze script verifies known
hashes, metadata, suffixes, unchanged proof segments and obligation labels.
Those operations are administrative, not mathematical evidence.

No promotion is made. Root and C must BOTH re-audit the affected complete
v1.1 argument and scope before coordinator reconciliation. No claim
about nonsaturated orders, solving the unbounded interior system,
novelty or the official full taut classification is added. The queued
fresh blind2021 R6 R2 starts only after this COMPLETE repair checkpoint;
no new R6 report, ledger or findings have been opened.

## Preserved original construction log (historical)

---

"""
worklog = worklog_header + worklog_old

old_sources = json.loads(read("sources-v1.json"))
sources = dict(old_sources)
sources["original_v1_recorded_at_utc"] = sources["recorded_at_utc"]
sources["recorded_at_utc"] = NOW
sources["status"] = "candidate proof - unverified; full R4R2-01 author repair source record v1.1"
sources["original_v1_direct_full_reads_preserved_unchanged"] = sources.pop(
    "direct_full_local_document_or_register_reads")
sources["actual_primary_read_scopes_are_original_v1_visits_not_fresh_repair_claims"] = True
sources["new_R4E_symbolic_moment_proof"] = (
    "Full original iff retained; added elementary automatic-last-row Fermat/binomial proofs "
    "and sufficient-interior-list nonzero-residue Vandermonde, no external import")
sources["repair_issue"] = "R4R2-01"
sources["author_acknowledges_false_v1_essential_insufficient_assertion"] = True
sources["root_initial_miss_and_C_initial_finding_preserved"] = True
sources["full_repair_reads"] = [fingerprint(path) for path in (
    PREFIX + "candidate-v1.md", PREFIX + "obligations-v1.md",
    PREFIX + "source-checks-v1.md", PREFIX + "worklog-v1.md",
    PREFIX + "sources-v1.json", PREFIX + "freeze-v1.json",
    "problems/2020-B4/reviews/reasoning-return-r4-review-1-initial-v1.md",
    "problems/2020-B4/reviews/reasoning-return-r4-review-1-issues-v1.json",
    "problems/2020-B4/reviews/reasoning-return-r4-review-1-source-checks-v1.md",
    "problems/2020-B4/reviews/reasoning-return-r4-review-2-initial-v1.md",
    "problems/2020-B4/reviews/reasoning-return-r4-review-2-issues-v1.md",
    "problems/2020-B4/reviews/reasoning-return-r4-review-2-source-checks-v1.md",
)]
sources["required_affected_reauditors"] = ["coordinator root", "review_2017_coarsening_r1"]
sources["independent_issue_resolution_or_coordinator_promotion_claimed"] = False
sources["new_external_theorem_or_fresh_full_external_proof_imported"] = False
sources["direct_weekly_telemetry"] = {
    "at_utc": "2026-10-17T12:46:26+00:00",
    "source": "direct account-wide Codex usage tool paired with UTC clock",
    "total_used_percent": 39, "window_duration_minutes": 10080,
    "resets_at_unix": 1792745187, "ordinary_usage_allowed": True,
    "total_used_cutoff_percent": 90, "integration_reserve": True,
}
sources_text = json.dumps(sources, indent=2, ensure_ascii=False) + "\n"

replacements = [
    ("candidate-v1.md", "candidate-v1.1.md", main_old, main),
    ("obligations-v1.md", "obligations-v1.1.md", oblig_old, oblig),
    ("source-checks-v1.md", "source-checks-v1.1.md", source_old, source),
    ("worklog-v1.md", "worklog-v1.1.md", worklog_old, worklog),
    ("sources-v1.json", "sources-v1.1.json", read("sources-v1.json"), sources_text),
]
for _, target, _, _ in replacements:
    assert not (ROOT / (PREFIX + target)).exists(), target
assert not (ROOT / (PREFIX + "repair-v1.1.diff")).exists()
for _, target, _, content in replacements:
    write_new(target, content)
diff = "".join("".join(difflib.unified_diff(
    old.splitlines(keepends=True), new.splitlines(keepends=True),
    fromfile=PREFIX + before, tofile=PREFIX + after))
    for before, after, old, new in replacements)
write_new("repair-v1.1.diff", diff)
print(json.dumps({"text_only_no_mathematical_program": True,
                  "new_files": [fingerprint(PREFIX + after)
                                for _, after, _, _ in replacements]
                  + [fingerprint(PREFIX + "repair-v1.1.diff")]},
                 indent=2, ensure_ascii=False))
