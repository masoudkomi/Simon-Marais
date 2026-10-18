#!/usr/bin/env python3
"""Exclusive text assembly for the full R19 author correction; no math execution."""
from pathlib import Path
import difflib
import json

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "problems/2021-B4/notes"
P = "reasoning-center-return-r19-"


def old(suffix):
    return (BASE / (P + suffix)).read_text()


def new(suffix, text):
    with (BASE / (P + suffix)).open("x", encoding="utf-8") as stream:
        stream.write(text)


def once(text, before, after):
    if text.count(before) != 1:
        raise ValueError("expected exactly one literal text match")
    return text.replace(before, after, 1)


main = old("candidate-v1.md")
main = once(main, "## 0. Exact domain and accepted authority", """Version1.1 is a FULL author replacement after BOTH original whole
initials completed. Reviewer B identified required correction R19R2-01:
the v1 introduction incorrectly transferred an Eisenstein assertion
from a scaled carrier to the original carrier by translation alone.
That sentence is withdrawn; the precise normalized theorem and its
original-coordinate consequences are stated and proved below. All
v1 and original review bytes remain immutable. Root's original whole
initial missed this introductory overstatement; its coordinator
reconciliation preserves that fact. BOTH affected whole reaudits are
required before any promotion. This version is still UNVERIFIED.

## 0. Exact domain and accepted authority""")
main = once(main, """Moreover the actual degree14 carrier has a degree2 factor over Q2
whose translate is 2-Eisenstein. This is a necessary arithmetic
obstruction for the ENTIRE frame II, not an exclusion of that frame.
Frame III and the other actual EC/m3 branches remain unresolved.""", """Moreover the SCALED carrier G(Z)=s^(-14)g(sZ) has a monic
degree2 factor P over Z2 for which P(T+1) is 2-Eisenstein.
The corresponding monic factor E(X)=s^2 P(X/s) of the ORIGINAL
carrier lies over Q2 and defines a ramified quadratic field. Its
translate E(T+s) has constant valuation 2v2(s)+1<0, so it is NOT
an integral Eisenstein polynomial. The original carrier roots in
this pair satisfy v2(alpha-s)=v2(s)+1/2. These are necessary
arithmetic properties for the ENTIRE frame II, not an exclusion of
that frame. Frame III and the other actual EC/m3 branches remain
unresolved.""")
main = once(main, """self-certification. No NEW R19 peer review exists or was consulted.""", """self-certification. In the original v1 construction no NEW R19
peer review existed or was consulted. After BOTH original whole
initials froze and root explicitly released them, this repair read
both full mathematical reports, all64+64 dispositions, issue logs,
source MD/JSON and worklogs. B's scaling objection and hand prototype
are retained in Section8 and the repair ledger. They prompted this
author correction; they are not concealed as new author discovery.
The original generic research assignment supplied no new proof step.
The present repair uses the reviewer-identified coordinate formula;
root relayed the objection and required both affected reaudits.""")
main = once(main, """satisfy v2(alpha-s)=v2(s)+1/2. The other twelve roots of G are
integral and reduce to0. This local factor is not a rational global
factor, and none of its roots is promoted to a rational common witness.""", """satisfy v2(alpha-s)=v2(s)+1/2. Their monic original-coordinate
factor is E(X)=s^2 P(X/s), irreducible of degree2 over Q2. It
defines the SAME root field as P; this field has ramification index2.
Writing P(T+1)=T^2+bT+c and M=v2(s)<0, one has the exact identities

    E(T+s)=T^2+s b T+s^2 c,
    v2(s^2 c)=2M+1<0,
    s^(-2) E(s(T+1))=P(T+1).                       (C-original)

Thus the Eisenstein assertion concerns the normalized P(T+1),
not the original-coordinate translate E(T+s). In fact no Q2
translation of this constructed monic E is integral. The other
twelve roots of G are integral and reduce to0. This local factor
is not a rational global factor, and none of its roots is promoted
to a rational common witness.""")
main = once(main, "## 6. The degree2 carrier factor is forced and 2-Eisenstein", "## 6. The normalized degree2 factor is forced and 2-Eisenstein")
main = once(main, """The other monic factor Q is integral. Each of its roots is integral
and reduces to0 because Qbar=Z^12. Returning to g via alpha=s z
proves all assertions of R19C. The quadratic root field is ramified
at2, as also witnessed directly by the half-integral valuation.""", """The other monic factor Q is integral. Each of its roots is integral
and reduces to0 because Qbar=Z^12. Returning to g via alpha=s z
gives v(alpha-s)=M+1/2, where M=v(s)<0. The corresponding exact
factorization over Q2, in ORIGINAL coordinates, is

    g(X)=E(X) Q_original(X),
    E(X)=s^2 P(X/s), Q_original(X)=s^12 Q(X/s).

These two original-coordinate factors are monic, but integral
coefficients are NOT asserted. Since s is a nonzero rational
number, substitution X=sZ preserves irreducibility over Q2 and
Q2(alpha)=Q2(z)=Q2(z-1). The field has degree2 and contains
an element z-1 of valuation1/2, hence is ramified with index2.
For the index assertion, distinct valuation classes modulo Z give
linearly independent elements over Q2, by the unique-smallest-term
argument. There are at least two classes, and at most the field
degree2, so the index is exactly2.

Put P(T+1)=T^2+bT+c as above. Direct substitution gives

    E(T+s)=s^2 P(1+T/s)=T^2+s b T+s^2 c.           (20)

The constant term in (20) has valuation 2M+1. As M is a negative
INTEGER, 2M+1<=-1. Therefore (20) is not in Z2[T] and cannot
be called 2-Eisenstein. Rescaling as well as translating gives
the exact identity s^(-2)E(s(T+1))=P(T+1), which IS integral
and 2-Eisenstein. No invariance under nonunit scaling is used.

More strongly, let a be ANY element of Q2. For either root alpha
of E put t=z-1; then

    alpha-a=s(t+1-a/s).

The term 1-a/s lies in Q2 and has integral valuation, or is0
and has infinite valuation. It can never have valuation1/2.
The unequal-valuation sum rule gives

    v(alpha-a)=M+min(1/2,v(1-a/s))<=M+1/2<0.        (21)

If E(T+a) were monic integral, all its roots would be integral
by Section1, contradicting (21). Thus NO Q2 translation makes
this constructed monic E integral. This assertion concerns E,
not unknown other possible local factors of g. The ramified
quadratic field and root distances persist under the change of
coordinates; integral Eisenstein coefficients do not. This proves
the exact normalized and original-coordinate versions of R19C.""")
main = once(main, """carrier value v(G(1))=1. These do not assume a2-adic depth cap,""", """carrier value v(G(1))=1. Its quadratic factor P is integral
and has an Eisenstein translate only in the NORMALIZED coordinate
used here. The constructed original monic E has a ramified degree2
root field and satisfies (20),(21), not an integral-translate claim.
These conclusions do not assume a2-adic depth cap,""")
main += """

## 8. Required correction R19R2-01 and its sharp counterexample

The original v1 introduction said that the actual degree14 carrier
has a quadratic factor whose translate is 2-Eisenstein. The formal
v1 Section6 had established that assertion only for the SCALED
G and its integral factor P. Dropping this scale was incorrect.
Reviewer B identified the issue and supplied the following exact
hand prototype, retained here with attribution:

    P(Z)=(Z-1)^2-2, s=1/2,
    P(T+1)=T^2-2,
    E(X)=s^2 P(X/s)=X^2-X-1/4,
    E(T+1/2)=T^2-1/2.

The normalized translate is 2-Eisenstein; the last polynomial is
not integral. This is a counterexample to the omitted scaling
inference, NOT an actual degree20 polynomial satisfying (S),(W)
or an example contradicting the original Casas--Alvero question.
No numerical scan or algebra system produced this prototype.

The repaired claims retain the entire R19A exclusion and R19B
inequality, the normalized factorization and P(T+1) Eisenstein
property, the local quadratic field with ramification index2, and
the original root displacement M+1/2. The unscaled integral
Eisenstein assertion is withdrawn and explicitly replaced by the
negative constant valuation and nonintegrality in (20),(21).
Nothing here excludes frame II or III, forces an actual new
rational common zero, makes g globally reducible, or solves the
remaining degree20/annual problem. BOTH original reviewers must
reconstruct the full affected argument in fresh independent
reaudits before coordinator promotion. No old file was edited.
"""
new("candidate-v1.1.md", main)
new("diff-v1-to-v1.1.patch", "".join(difflib.unified_diff(
    old("candidate-v1.md").splitlines(keepends=True), main.splitlines(keepends=True),
    fromfile=P+"candidate-v1.md", tofile=P+"candidate-v1.1.md")))

ob = old("obligations-v1.md")
ob = once(ob, "# R19 entire constructor obligations", "# R19 version1.1 ENTIRE constructor obligations")
ob = once(ob, "ALL64 must be reconstructed by each of TWO OTHER entire whole auditors.", """The original64 rows are preserved in this full replacement and
must be reconstructed together with all12 repair rows, ALL76,
by BOTH affected whole auditors. Original closed scopes are not
replaced by checking one explanatory sentence.""")
ob += """

## Full affected coordinate-repair obligations

|ID|Inference and adversarial check|Constructor disposition|
|---|---|---|
|R19-FC01|Admit the original introductory unscaled-translate assertion was not established; preserve original13, both original21 and B's issue/prototype unchanged.|Checked, version note, §8 and repair ledger.|
|R19-FC02|Keep ALL original64 domains, witness/integrality arguments, cases, frame-I exclusion and frame-II inequality; no new convenience hypotheses.|Checked, §§0--5 unchanged apart from role/history note.|
|R19-FC03|State normalized G and P separately from original g and E in introduction, formal R19C, §6 and final scope.|Checked, full replacement and exact diff.|
|R19-FC04|E=s²P(X/s), Q_original=s¹²Q(X/s) are monic Q2 factors and multiply to g with all scaling powers exact.|Checked, §6 from G=s^-14 g(sZ).|
|R19-FC05|P(T+1)=T²+bT+c has v(b)>=1, v(c)=1, including b0; this is the precise integral Eisenstein claim.|Checked, original lift proof retained in §6.|
|R19-FC06|Exact identity E(T+s)=T²+s b T+s²c has constant valuation2M+1<=-1 because M is a negative integer.|Checked, (20); b may be0.|
|R19-FC07|Only combined scaling/translation s^-2 E(s(T+1))=P(T+1) preserves the displayed normalized polynomial; translation alone does not.|Checked, (C-original),(20).|
|R19-FC08|Original roots alpha=s z have displacement M+1/2; Q2(alpha)=Q2(z), irreducible quadratic and ramification index2, without coefficient integrality.|Checked, §6 and valuation-class independence.|
|R19-FC09|For every a inQ2, v(1-a/s) integer or infinity, distinct from1/2; unequal-valuation rule gives (21), including a=s.|Checked, §6.|
|R19-FC10|No Q2 translate of the CONSTRUCTED monic E can be integral, since its translated roots have negative valuations; no assertion about other factors.|Checked, (21), Section1 monic-root lemma.|
|R19-FC11|B's P=(Z-1)²-2,s1/2 gives E=X²-X-1/4, E(T+1/2)=T²-1/2; distinguish generic counterexample from an actual(S),(W) polynomial.|Checked by hand, §8.|
|R19-FC12|Both original reviews complete/released before this author response; BOTH fresh affected whole reaudits and root reconciliation remain required; no frameII/III/annual exclusion, no mathcode or old edits.|Required entire76 freeze/readback/separate verify; no promotion.|
"""
new("obligations-v1.1.md", ob)

ch = old("checks-v1.md")
ch = once(ch, "# R19 explicit hand checks and counterexample challenges", "# R19 version1.1 explicit hand checks and counterexample challenges")
ch += """

## Additional complete coordinate checks for R19R2-01

13. The previously derived M<0 is the valuation of rational s, so M is an
    integer, not a fractional algebraic-root valuation. Thus2M+1
    is strictly negative, including the endpoint M=-1 where it is-1.
14. The original factor E has coefficients in Q2, because P is
    over Z2 and s is nonzero rational. Its leading coefficient is
    s²*(1/s²)=1; g=E*(s¹²Q(X/s)) follows by canceling s^14.
15. Substituting T+s cancels the center but does not divide the
    root distances by s. Its constant is s²c, not c. Conversely
    substituting s(T+1) and multiplying by s^-2 gives P(T+1).
16. The quadratic field is unchanged by multiplying a root by
    nonzero s inQ2 or subtracting1. Its value group has a half-
    integral element. Distinct value classes give linearly
    independent Q2 elements, so the quadratic extension has e=2.
17. For any a inQ2, 1-a/s has valuation inZ or infinity. No equality
    with1/2 allows cancellation. Thus (21) is valid for all a,
    even a=s, a0 and negative valuations, and always gives a
    negative original-coordinate distance. This contradicts a
    hypothetical monic integral E(T+a), without assuming b is nonzero.
18. B's exact prototype has M=-1, b0,c=-2. E(T+s)=T²-1/2
    has valuation-1 in its constant. It isolates the discarded
    inference only and supplies no actual rational-witness f.

Every original check1--12 and repair check13--18 is retained in the
full operative proof. Neither a stronger irreducibility conclusion
over Q nor an exclusion of the remaining actual frames is inferred.
"""
new("checks-v1.1.md", ch)

fl = old("failures-v1.md")
fl = once(fl, "# R19 failed routes and exact remaining gaps", "# R19 version1.1 failed routes and exact remaining gaps")
fl += """

11. **Required failure, not a cosmetic notation choice (R19R2-01).**
    V1's introduction omitted the scale when describing its quadratic
    factor. Integral Eisenstein coefficients are not invariant under
    the nonunit scale s. B's prototype P=(Z-1)²-2,s1/2 yields
    original E=X²-X-1/4 and E(T+s)=T²-1/2, not integral. The
    general actual formula is T²+s b T+s²c with constant valuation
    2M+1<0. Formal v1 R19C was normalized and is not contradicted;
    the explanatory original-carrier statement WAS unjustified.
    The repaired full main withdraws it, preserves local quadratic
    ramification/root distance and proves original nonintegrality.
    The prototype is not an actual counterexample to degree20 CA.

The next missing global equation still has to contradict the ACTUAL
ramified carrier in frameII, or exclude frameIII/differentEC/m3.
Correcting coordinate integrality does not supply that contradiction.
"""
new("failures-v1.1.md", fl)

new("sources-v1.1.md", """# R19 version1.1 source and review-contribution record

2026-10-18 UTC. Candidate proof - unverified. This FULL replacement
retains below the original precise primary/accepted-input read record.
Those operative inputs and their current identities are unchanged.
The historical v1 no-peer/no-future-BT statements below describe
ORIGINAL CONSTRUCTION ONLY, not the present author-repair stage.
No new external theorem, full-book audit, download or source replay
was needed for this coordinate correction. The algebra is fully
displayed in the new main. The repair's new actual reading follows.

After root explicitly confirmed BOTH complete original whole initials,
read both mathematical reports in full, ALL64+64 separate dispositions,
both issue logs, both source MD/JSON and both worklogs. Also read the
complete coordinator reconciliation MD/JSON. B identified R19R2-01,
the original-coordinate formula and the prototype; root relayed the
issue, preserved its own missed introduction qualification, and
required versioned repair/BOTH affected reaudits. These correction
contributions are attributed, not treated as original A discoveries.
A remains the original constructor and is excluded from independent
reviews. Future affected review findings remain unread until both
entire affected checkpoints and coordinator release.

Byte validation of older admin/manifest records is not a claim of
fresh mathematical or entire historical-source reading. The parent
compact bindings preserve original13/BOTH21/current operative inputs;
historical mutable research-map observations remain historical and
are not falsely required to match their current coordinator version.

---

## Original v1 source record, retained as historical evidence

""" + old("sources-v1.md"))
sj = json.loads(old("sources-v1.json"))
new("sources-v1.1.json", json.dumps({
    "date_utc": "2026-10-18", "status": "candidate proof - unverified",
    "version": "1.1 author correction R19R2-01",
    "original_primary_and_accepted_read_scope_HISTORICAL": sj,
    "new_external_theorem_import": False,
    "new_external_source_download_cache_or_replay": False,
    "original_BOTH_complete_and_released_before_peer_read": True,
    "new_FULL_mathematical_reads": [
        "reviews/reasoning-center-return-r19-review-1-report-v1.md",
        "reviews/reasoning-center-return-r19-review-1-ledger-v1.md",
        "reviews/reasoning-center-return-r19-review-1-issues-v1.md",
        "reviews/reasoning-center-return-r19-review-1-sources-v1.md/.json",
        "reviews/reasoning-center-return-r19-review-1-worklog-v1.md",
        "reviews/reasoning-center-return-r19-review-2-initial.md",
        "reviews/reasoning-center-return-r19-review-2-obligations-v1.md",
        "reviews/reasoning-center-return-r19-review-2-issues-v1.md",
        "reviews/reasoning-center-return-r19-review-2-sources-v1.md/.json",
        "reviews/reasoning-center-return-r19-review-2-worklog-v1.md",
        "reviews/reasoning-center-return-r19-coordinator-reconciliation-v1.md/.json"],
    "review_contribution": "B identified omitted scaling, E formula and prototype; root relayed/required versioned repair and acknowledged original miss",
    "new_math_hand_only": True, "all_original_bytes_preserved": True,
    "TWO_OTHER_affected_WHOLE_reaudits_required": True,
    "requested_inherited": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "effective_readback": None,
    "fresh_full_historical_external_or_peer_admin_model_read_claimed": False
}, indent=2) + "\n")

new("repair-ledger-v1.1.md", """# R19R2-01 full versioned author response

2026-10-18 UTC. Candidate proof - unverified. Required correction
ACKNOWLEDGED. No original author13 or original reviewer21 file is
edited. The original introductory statement was unjustified, not
merely a different notation for the formal normalized theorem.

|Issue|Original defect|Full author correction|Affected obligations|
|---|---|---|---|
|R19R2-01|The introduction described an Eisenstein translate of an original-carrier quadratic; Section6 only proved it for normalized G.|Full v1.1 introduction, formal R19C, §6, §7 and new §8 distinguish G/P from g/E. P(T+1) is integral 2-Eisenstein; E(T+s) has negative constant valuation2M+1. B's prototype retained and attributed.|All64 retained; FC01--FC12 added.|

Exact original defect retained in frozen v1: the actual degree14
carrier was said to have a degree2 factor whose translate is
2-Eisenstein. The correct constructed original monic factor is
E=s²P(X/s), so E(T+s)=T²+s b T+s²c. R19B gives M=v2(s)<0
and formal R19C gives v2(c)=1; hence its constant valuation is
2M+1<=-1. It is not integral. B's P=(Z-1)²-2,s1/2 yields
E=X²-X-1/4 and E(T+1/2)=T²-1/2. That counterexample targets
the dropped scale, not any actual degree20(S),(W) polynomial.

Retained conclusions: entire actual frameI exclusion/affinepartner;
entire frameII inequality; G integral/Gbar/v(G1); unique monic
integral P/Q; P(T+1) Eisenstein; local original degree2 factor,
same ramified quadratic field and root distances M+1/2. Added
explicit coordinate proof: all Q2 translations of this constructed
monic E have a root of negative valuation, so none is integral.
This concerns the constructed E and does not classify other factors.

Every original domain, actual common-witness recursion, residue case,
coefficient sign, endpoint b0, factor-lifting proof and attribution
is present in the full replacement. Exact main diff is included.
The abstract prototype has no19-adic/CA hypotheses and is not used
as an actual f. No frameII/III/differentEC/m3/annual exclusion,
global Q factor, extra rational witness or novelty claim is added.

Original root initial did not flag the introductory scaling error;
root's coordinator record preserves that miss. Author response
does not rewrite either independent initial. BOTH original reviewers
must perform independent affected WHOLE reaudits, including all76
obligations and source/coordinate scopes, before root reconciliation.
Author A is excluded. No already accepted conclusion is presumed
for this repaired candidate. Administrative freezing is not proof.
""")
new("worklog-v1.1.md", """# R19 version1.1 author worklog

2026-10-18 UTC. Candidate proof - unverified. Only NEW assigned
R19 version1.1 paths are written; no Git/shared/old/cache mutation.

1. Root explicitly released BOTH original complete whole initials.
   A accepted B's required coordinate objection R19R2-01. Root
   relayed it and asked for full versioned repair/both affected
   reaudits, preserving all originals and root's initial miss.
2. Completed the active2025 DR6 meaningful entire13/48 constructor
   checkpoint before switching. It froze14:17:29.756496UTC,
   full final model readback and separate verify14:18:28.826882
   passed. That mathematics is not a premise of this repair.
3. Read full original R19 main, ALL64/hand checks/failures/source
   MD/JSON, old code/admin/worklog and compact metadata; full
   original root/B mathematical reports, ALL64+64 dispositions,
   issue/source MDJSON/worklogs and coordinator reconciliation.
   No fresh full historical source or peer-admin audit is claimed.
4. Checked by hand the exact unscaled monic factor, translation,
   scaled inverse substitution, root-field identity, ramification
   index and all-a-inQ2 nonintegrality. Retained b0, a=s, M=-1
   and the prototype. No math computation/scan/replay occurred.
5. Direct authoritative clock/usage at14:22:59UTC returned42%TOTAL,
   reset1792874445/10080min, ordinaryUsageAllowed=true; legacy
   and by-limit codex values agreed, account029a8928...1334ac3a.
   Only this expressly authorized current window is funded;
   ceiling90TOTAL plus integration reserve; no automatic laterweek.
6. Exclusive text-assembly code copies the full proof/old64 rows,
   replaces exact literal passages, supplies all12 repair rows,
   complete companion files and exact unified diff. No symbolic
   mathematics or certificate is evaluated by code. New admin
   verifies immutable parent/payload bytes and obligation labels.
7. Requested inherited gpt-6.1-sol/max; independent verified
   effective-setting readback unavailable. No pending approval,
   native math child, PID, incomplete run, contact, charge or
   access bypass. Other agents continue independently.

Complete all final files must be model-read, then freeze manifest
created/read fully, then a SEPARATE read-only command re-verifies
every payload/immutable protected record before handoff. Generated
metadata and final separate tool output carry exact times/identities.
BOTH fresh affected whole reaudits remain required; no promotion.
""")
new("code-log-v1.1.md", """# R19 version1.1 exact command and execution scope

All proof and prototype arithmetic was checked by hand. No math
program/CAS/table/scan/source replay was run. NEW source below
is text assembly and byte/JSON administration only.

Read-only: cat AGENTS/current assigned old main/companions, narrow
rg --files for unused v1.1 suffixes, then full old mathematical
reports/ALL128/issues/source/worklogs and reconciliation. Metadata
hashing is not mathematical model-reading of all referenced history.

Executed administrative sequence:

    python3 problems/2021-B4/notes/reasoning-center-return-r19-build-v1.1.py
    python3 problems/2021-B4/notes/reasoning-center-return-r19-admin-v1.1.py prepare
    [FULL final ALL payload model readback in bounded chunks]
    python3 problems/2021-B4/notes/reasoning-center-return-r19-admin-v1.1.py freeze
    [FULL final freeze manifest model readback]
    python3 problems/2021-B4/notes/reasoning-center-return-r19-admin-v1.1.py verify

The build source is retained in the packet. Every new text write
uses exclusive creation. It performs exact literal replacements,
JSON formatting and unified textual diff; there is no polynomial
calculation. Prepare/freeze are exclusive; verify is read-only.
Parent metadata is bound by path/bytes/SHA plus occurrence counts
and deduplicated summaries, not recopied as a growing giant inventory.
The old research-map observation is kept historical and excluded
from immutable-math guards; original proof/payload hashes are still
checked. No original admin routine is rerun as a source/certificate.

No Git/shared/old/cache write, broad cleanup, charge/contact/bypass,
pending permission or long native command. Any execution failure
must be recorded rather than silently presented as a proof failure.
""")
print("Exclusive full v1.1 text assembly complete; no mathematics executed.")
