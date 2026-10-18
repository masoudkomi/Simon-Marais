from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re

ROOT=Path.cwd()
BASE='problems/2025-B4/reviews/'
P='reasoning-return-r9-review-1-reaudit-v1.1-'
assert not list((ROOT/BASE).glob(P+'*')), 'Refuse existing review prefix'
now=datetime.now(timezone.utc).isoformat()
def rec(path):
    b=(ROOT/path).read_bytes()
    return dict(path=path,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def walk(obj):
    if isinstance(obj,dict):
        if isinstance(obj.get('path'),str) and isinstance(obj.get('bytes'),int) and isinstance(obj.get('sha256'),str): yield obj
        for v in obj.values(): yield from walk(v)
    elif isinstance(obj,list):
        for v in obj: yield from walk(v)
inputs=[
 'problems/2025-B4/notes/reasoning-return-r9-freeze-v1.1.json',
 'problems/2025-B4/notes/reasoning-return-r9-baseline-v1.1.json',
 'problems/2025-B4/reviews/reasoning-return-r9-review-1-manifest-v1.json',
 'problems/2025-B4/reviews/reasoning-return-r9-review-1-integrity-v1.json',
 'problems/2025-B4/reviews/reasoning-return-r9-review-2-manifest-v1.json',
]
declared=[]
for f in inputs:
    declared.append(rec(f))
    declared.extend(walk(json.loads((ROOT/f).read_text())))
unique={}
for r in declared:
    actual=rec(r['path'])
    assert all(actual[k]==r[k] for k in ('path','bytes','sha256')), (r,actual)
    if r['path'] in unique: assert unique[r['path']]==actual
    unique[r['path']]=actual
old=(ROOT/'problems/2025-B4/notes/reasoning-return-r9-candidate-v1.md').read_text()
new=(ROOT/'problems/2025-B4/notes/reasoning-return-r9-candidate-v1.1.md').read_text()
def seg(t,a,b=None):
    x=t.split(a,1)[1]
    return x if b is None else x.split(b,1)[0]
unchanged={
 'complete_sections1_to3':seg(old,'## 1.','## 4.')==seg(new,'## 1.','## 4.'),
 'complete_sections5_to6':seg(old,'## 5.','## 7.')==seg(new,'## 5.','## 7.'),
 'complete_section8':seg(old,'## 8.')==seg(new,'## 8.'),
 'complete_cofactor_paragraph':seg(old,'A safe replacement is elementary.','## 5.')==seg(new,'A safe replacement is elementary.','## 5.'),
}
assert all(unchanged.values()),unchanged
ob=(ROOT/'problems/2025-B4/notes/reasoning-return-r9-obligations-v1.1.md').read_text()
assert [int(x)for x in re.findall(r'^\| (\d+) \|',ob,re.M)]==list(range(1,57))
summary=hashlib.sha256(json.dumps([unique[k]for k in sorted(unique)],sort_keys=True,separators=(',',':')).encode()).hexdigest()
report='''# OTHER whole affected reaudit R1: complete R9 v1.1

2026-10-18 UTC. Reviewer /root; constructor C /root/review_2017_coarsening_r1.
ENTIRE affected WHOLE reaudit, all56 obligations. The original initially
blind whole R1 remains immutable. This new complete packet is frozen
BEFORE opening or hashing ANY NEW B R9 v1.1 affected-reaudit finding,
source record, ledger, issue file or metadata. Both original whole initials
were already frozen and have now been fully read; that authorized original
comparison is distinct from the pending new affected peer review.

Verdict: R9R1-01 is resolved in the FULL v1.1. The independently found same
R9R2-01 radius issue is resolved too. The R9R2-N3 generator-quantifier
qualification is explicit throughout. I found no new substantive defect or
required repair in the stated R9A–F scopes after reconstructing all56 rows.
Acceptance still requires B's separate whole affected reaudit and root's
complete reconciliation; this report itself does not promote the candidate.

## 1. Radius repair, including both endpoints

The fourteen independent rows are e1+H e2 and e3,...,e15. Adding v=e1
gives rank15. Orthogonality to the fourteen rows says w1=-H w2 and
w3=...=w15=0. For an INTEGER vector with |w1|<=R<H, integrality forces
w2=0 and hence w1=0. This proves equation(16) for EVERY real0<R<H.
It does not assert a nonzero vector when R<1. At H2,d17,R1/2 the closed
integer cube is exactly {0}; v1.1 expressly preserves and acknowledges
the countercertificate to the old sentence.

For1<=R<H the unit vector e16 lies in both kernels and the box, even at
the closed lower endpoint R1. For the perturbed added row e1+ej, with
j>=16, the old equations first force w1=w2=0, so the added equation
forces wj=0. There is an alternate k>=16,k!=j since d>=17; ek is in
that perturbed kernel and has sup norm1. Every nonzero-unit assertion
now carries1<=R<H, including failed-route summaries. For R<1 the same
perturbed integer boxes are zero-only. At R=H the vector(-H,1,0,...,0)
lies in S' and outside S, so the strict upper endpoint is necessary.
For integer H>1,1<sqrt(H)<H retains the intended arbitrarily large
counterexample family. No actual Jacobi signature is inferred from it.

## 2. Generator quantifier repair

For a0=1+c zeta,c=2p², the binomial coefficients at degrees p-2 and
p-1 of a0^p are p(p-1)c^(p-2)/2 and p c^(p-1). Their ratio equality
would require c=(p-1)/2, which is false. A degree<=p polynomial evaluated
at zeta reduces its degree-p constant term since zeta^p=1. If it were
linear, its remaining degree2,...,p-1 coefficients would be a common
multiple of Phi_p; the displayed two would agree. Thus the CHOSEN
number a0^p is nonlinear. This is a statement about that number, not
every generator of (a0)^p. A unit multiple can change linearity.

The explicit diagnostic zeta²(2+zeta) is nonlinear: subtracting an
arbitrary linear polynomial leaves a nonzero polynomial of degree3,
less than p-1 for p>=37, so it cannot vanish at zeta. Yet zeta² is a
unit and its ideal equals(2+zeta). This diagnostic supplies no alternative
generator of the SPECIFIC ideal A0^p. The overview, section7 title,
coefficient proof, unit discussion, final model conclusion, obligations43–44
and failed-route ledger all now retain exactly this distinction. No
ideal-level no-linear-generator theorem has been inserted.

## 3. Complete unchanged R9A–B reconstruction

I reread the COMPLETE repaired main, complete56-row obligation file,
all repair/source/failure/worklog/diff companions and all administrative
metadata and freezer source without running the author's program.
The complete sections1–3,5–6,8 and the full cofactor paragraph are also
independently byte-compared to the original mathematical text. They
are unchanged, but their mathematical scopes were checked again.

The t_h basis uses the single integral Phi_p relation and symmetric
coefficients; t0=-2 sum t_h eliminates the constant without halving an
integral lattice. The folded k0 entries have magnitude<=2. At k1,
four negative contributions total[-8,0], and t0 elimination contributes
a common[0,8], giving[-8,8], including collisions. Expanding both real
coordinates gives U=2q m² and V<=2m². The binary-image count is at
most(16U+1)^V. q>=32 and m<=16q give the strict collision inequality;
2^32>8192*32³+1 and the cubic growth ratio stays below2. p>=937 is
sufficient, not an optimized prime threshold. The nonzero difference
has coordinates in{-1,0,1}; independence of1,zeta over Kplus makes
some ell nonzero. All embeddings satisfy sum|ell|<=4q m².

For actual phases, the accepted R8 tails give |sigma delta|<=4A
|X|^(-1-1/p). The nonzero integral real norm gives the stated
(4A)^(p/(p+1)) bound. That branch remains conditional. If delta=0,
the nonzero formal radical combination has at most2q m active
functions. Its general Wronskian cost uses T*=(p-2)n*(n*-1)/2+n*-1,
never the old sparse support. Clearing the first coefficient by p^t t!
and the retained accepted tail argument give the HUGE bound(10).
No short-vector claim removes that branch or improves a published
unconditional height theorem.

## 4. Complete arithmetic and cofactor reconstruction

The characteristic ideal is the accepted signed e0 ideal, with pairwise
coprime conjugates and normY>1. G_p(X) is odd for either parity and
either sign. The matched half-weight Jacobi products have the correct
ideal, all conjugate modulus sqrtY and lambda² normalization. Only a
quotient of generators of the SAME ideal is automatically a unit;
Kronecker and common normalization then remove its root of unity.
This proves the displayed multiplicative/equivariant normalization,
beta_N=Y and the needed k1/k3 p-th-power identity, retaining F0 and
p not dividing X-1. It is not a new generalized e1 theorem.

The safe avoidance replacement chooses r+1 columns with a nonzero
augmented determinant. Signed r-minors annihilate the original r rows
and their contraction with b is that nonzero determinant. Each minor
has magnitude<=r!B^r by the determinant expansion. The empty minor1
handles r0. This remains a large-minor avoidance bound, not the
unsupported ordinary-first-minimum replacement.

Two half-supports each have m entries; disjointness is equivalent to
sumN. M1 nonzero excludes N. At an overlapping conjugate prime the
three valuations of b1,b2,Y are e,e,e; thus b1b2-Y has valuation e,
not2e. A denominator D coprime toY leaves chi valuation e, so the
quotient chi/(b1b2) has valuation-e. Each separate divisibility is
valid, whereas product divisibility fails. Equal complex moduli do
not make a number with a finite pole into an integral unit.

For psi(1,1) in the DIRECT convention, M1=1/8. Theta=2 sigma2 psi+
4jpsi has coefficients0,2,4,6, complement6N,F0,M1=-3/8, and the
correct source J3 domain. sigma2 u=u² modulo2 for ALL u in O gives
beta_Theta=(sigma2 b)²(jb)^4 congruentY^4=1 modulo2. Every conjugate
has that residue; the even nonzero w' makes each equality ideal a
NONZERO subset of(2), with the stated ideal-divisibility direction.
The two signed homogeneous maps preserve the argument. The only
norm shift to complement2N subtracts2N; an index with psi1 and
sigma2psi0 produces coefficient-2. No original-weight or infinity
phase bridge follows.

The explicit model has positive odd norm(c^p+1)/(c+1)>1 and a0=1
modulo lambda². A common conjugate-ideal prime would divide c or
zeta^a-zeta^b, each impossible; zeta=-1/c in the prime field has
orderp, so every relevant prime splits completely. For the accepted
original-weight pair, b_i=a0^psi_i has the required ideal, normalization
and all-embedding modulus sqrtZ. Since a0=1 modulo2, beta is1 at
every conjugate modulo2, and w'2 gives equality ideal EXACTLY(2).
The same overlap prime gives a genuine product-division pole. This
uses genuine numbers but supplies no actual linear characteristic
p-th-power generator or solution; the quantifier correction above
is essential.

## 5. Sources, independence and exact recommendation

The original whole R1 fresh source reading and accepted-input limits
remain historical, as recorded in its immutable source audit. This
affected audit imports NO new primary theorem; it reads the full new
source/diff/repair record. Reading B's original source report is not
represented as freshly reading its primary PDFs. The current v4 ideal
argument remains distinguished from the2021 v1 carry argument. The
overlap inference is challenged in its exposed scope; no final source
nonexistence theorem is declared false. The separate subsequent Runge
packet and root's later exploratory quotient note are NOT premises.

Root's OLD UW/source/R6/R8 roles are disclosed and do not become new
self-certification. Root constructed none of the NEW R9A–F inference.
The original blind R1 froze before B's original findings; this complete
affected R1 now freezes before ANY NEW B affected findings or metadata.
No mathematical code, scan, CAS, author-program rerun or new native child
was used. Integrity checks compare files only. Requested inherited
gpt-6.1-sol/max is distinct from unavailable effective readback.

Recommendation: accept only the scoped R9A–F partial mathematics once
the OTHER complete affected audit agrees and full reconciliation resolves
all issues. Annual2025 classification, actual evaluated nonvanishing,
useful unconditional height improvement, all-generator ideal exclusion,
and novelty are NOT established. All old bytes and findings survive.
'''
rows=[
'Official signed diagonal domain retained, with degreep-1 and e0/Ypositive imports.',
'Exact R8 accepted input and old constructor/reviewer roles retained; no recertification.',
'Actual transported signature rows retained, m representatives, two real coordinates.',
'Integral t_h basis reconstructed from the unique Phi_p relation without dividing by2.',
't0=-2 sum t_h and folded multiplication hold with coincident indices.',
'k0 expanded entries bounded by2, including t0.',
'k1 negative[-8,0] and common[0,8] correction give magnitude8.',
'U2qm² and at most V2m² hold after expanding both real coordinates.',
'Strict binary-image collision yields a nonzero{-1,0,1} integral vector.',
'q32 base, cubic doubling, ceiling endpoint and sufficient prime937 verified.',
'Each embedding sum|ell|<=4qm²; independence of1,zeta makes some ell nonzero.',
'Actual nonzero-delta real norm gives exponentp/(p+1), conditional only.',
'Dense active-function count2qm retained, not the sparse cofactor count.',
'Canonical distinct radicals and general Wronskian give the displayed T*.',
'p^t t! integral witness and large zero-branch bound retained.',
'No unconditional useful improvement follows from the conditional branch.',
'Accepted actual ideal, coprime conjugates and normY>1 stay in signed e0 scope.',
'Oddness of G_p(X) checked for both parities and signs.',
'Matched half Jacobi products have integral ideal, sqrtY moduli and normalization.',
'Same-ideal quotient is a unit; Kronecker and lambda² normalization give uniqueness.',
'Equivariance/multiplicativity and beta_N=Y hold in generated group.',
'k1/k3 exact p-th powers retain F0 and the signed local congruence.',
'Ranks14/15 and exact S/S-prime equations reconstructed.',
'Equality holds for EVERY0<R<H; nonzero unit witnesses ONLY1<=R<H.',
'Perturbed extra coordinate vanishes for0<R<H; alternate unit ONLY1<=R<H.',
'Generic rational counterexample is not an actual Jacobi realization.',
'Augmented determinant and signed minors prove avoidance bound, including r0.',
'Half-support disjointness iff sumN; M1nonzero excludes that case.',
'Chosen overlap prime gives valuations e,e,e in b1,b2,Y.',
'Difference valuation exactlye; separate divisibilities do not multiply.',
'Quotient has pole-e; complex normone does not imply integral unit.',
'DIRECT inverse-index psi(1,1) has M1=1/8.',
'Theta positive coefficients< p, complement6N, sourceJ3 scope retained.',
'FTheta0 and M1Theta=-3/8 give freeness and exclude norm reduction.',
'sigma2u=u² modulo2 valid for all O, no splitting assumption.',
'Normalized actual product gives Y^4=1 modulo2 at every conjugate.',
'Even nonzero w-prime gives nonzero intersection subset(2), correct direction.',
'Signed homogeneous maps retain conjugate ideal and e0 scope.',
'Unique norm shift Theta-2N has coefficient-2; no original-weight/phase bridge.',
'Model norm, normalization, coprimality and complete splitting proved without scan.',
'Model half generators carry stated ideal/modulus/normalization for an accepted pair.',
'Original-weight equality ideal exactly(2) and overlap pole both retained.',
'Chosen a0^p coefficient comparison proves only that NUMBER nonlinear.',
'No suitable actual linear characteristic generator supplied; others unchecked.',
'Currentv4 and2021v1 proof versions remain distinguished.',
'Product-step objection does not refute final source nonexistence theorem.',
'Avoidance source scope retained; no unread quantitative theorem imported.',
'Annual/actual-zero/useful-height/novelty gaps remain explicit.',
'H2,d17,R1/2 zero-only countercertificate preserved and acknowledged.',
'Equation16 proof requires only0<R<H and integer w2.',
'Closed R1 contains all required unit vectors; d17 provides alternate index.',
'At R=H,(-H,1,0,...) lies in S-prime outside S.',
'H>1 gives1<sqrtH<H; unaffected blocks and full-minor proof unchanged.',
'Overview, detailed proof and final model conclusion all concern CHOSEN generator.',
'zeta²(2+zeta) diagnostic nonlinear yet same ideal, no A0^p conclusion.',
'Old initials preserved, both affected audits required; separate Runge not premise.'
]
assert len(rows)==56
ledger='# Whole affected ledger R1, R9 v1.1\n\n2026-10-18 UTC. All56 reconstructed; no open issue.\n\n| ID | Disposition and reconstruction |\n|---|---|\n'+''.join(f'| {i:02} | PASS scoped: {v} |\n'for i,v in enumerate(rows,1))
issues='''# Affected R1 issue disposition, R9 v1.1

2026-10-18 UTC. No new substantive issue or required author repair.

* R9R1-01 and original peer R9R2-01: RESOLVED. Equality remains for
  every0<R<H; every nonzero/unit assertion now requires1<=R<H. The
  R<1 countercertificate, R1 closed endpoint, alternate perturbed unit,
  valid sqrtH choice and R=H failure are explicit and correct.
* Original R9R2-N3: RESOLVED as a retained scope qualification. Only
  the chosen a0^p is nonlinear; all other ideal generators remain
  unchecked. The unit diagnostic and all overview/conclusion claims agree.
* Scope retained: actual evaluated-zero branch unresolved; large dense
  support bound not a useful unconditional improvement; generic rational
  examples not actual Jacobi systems; weight6 not original weight; no
  final source theorem refutation, annual classification or novelty claim.

This ENTIRE affected R1 freezes before any NEW B affected R9 metadata
or findings. Both original whole initials were already frozen and fully
read. B's new whole affected audit and root reconciliation are required.
'''
sources='''# Source and complete-read record: R9 v1.1 affected R1

2026-10-18 UTC. Root directly read the COMPLETE25036B main v1.1, ALL56
obligations, complete7172B repair ledger,8675B source ledger,5694B failed
routes,7142B worklog,21556B full five-file diff,9349B author freezer source
(READ, not run),7962B baseline,1498B metadata,610B input validation and
3132B constructor freeze. Final complete main/ledger reread was also
returned without truncation. Original R1 and original B R2 reports,
ALL48+48 rows, issues, sources and metadata were fully read after both
original initials froze. B's original report section8 was reread separately
after a globally truncated display. No missing segment supports a claim.

No new external primary result is imported for the repair. Root's original
R1 source audit records its actual direct official2025, R8/R6 and current
v4 operative sections, v1 section4.3.4, Fukshansky theorem/sharpness/height
scope, and exact reading limits. Those are historical direct reads, not a
claim of a fresh whole-paper read here. The elementary threshold and unit
diagnostic are fully rederived in this report. Reading B's original source
ledger does not turn its additional full-v4 read into a root whole-v4 read.

Accepted R8/R6 scopes and original role disclosures remain unchanged.
Current2025v4 differs from2021v1; the source inference criticism remains
local. No purchased source, restricted-access bypass, paper upload,
contact, new download or mathematical computation occurred. The later
Runge and root exploratory quotient records are not repair premises.
No NEW B R9 affected-reaudit file, source, finding or metadata was read
or hashed before this ENTIRE packet freeze.
'''
log='''# Root affected-re-audit worklog, R9 v1.1

2026-10-18 UTC. Read complete frozen constructor and ALL companions,
reconstructed both radius thresholds, every perturbed box, closed endpoints,
the chosen-number coefficient proof and unit diagnostic. Rechecked the
complete unaffected coefficient/norm/Wronskian/ideal/weight/model arguments
and every one of56 obligations. Independently compare complete unchanged
mathematical text blocks; validate declared immutable byte/SHA records.

All computations in this freezer are administrative text/JSON integrity,
not mathematical testing. No author freezer or CAS program is run. All
old bytes are preserved; new writes use only this fresh assigned prefix.
Root is OTHER for new R9 but has disclosed old UW/source/R6/R8 roles.
Original whole initials may now be compared; NEW B affected R9 findings
and metadata remain unread until this ENTIRE initial is frozen.

Both root/A Runge and root/B R12 initials froze separately; neither is
used to repair this argument. Requested gpt-6.1-sol/max is recorded apart
from unavailable effective readback. Latest authoritative root weekly
read5%TOTAL at00:53:20UTC, reset1792874445,90%TOTAL ceiling with reserve
under explicit new-window authorization. Workers continue independently.
'''
def out(suffix,data):
    path=BASE+P+suffix
    if not isinstance(data,str): data=json.dumps(data,indent=2,ensure_ascii=False)+'\n'
    with(ROOT/path).open('x')as f:f.write(data)
    return rec(path)
payloads=[out('initial-v1.md',report),out('ledger-v1.md',ledger),out('issues-v1.md',issues),out('source-audit-v1.md',sources),out('worklog-v1.md',log)]
# Include the actual one-shot code in the frozen review; never execute author code.
payloads.append(out('freeze-v1.py',Path(__file__).read_text()))
for r in declared:
    assert all(rec(r['path'])[k]==r[k]for k in ('path','bytes','sha256'))
payloads.append(out('integrity-v1.json',dict(verified_at_utc=now,administrative_only=True,record_occurrences=len(declared),unique_paths=len(unique),summary_sha256=summary,inputs=[rec(f)for f in inputs],unchanged_complete_mathematical_text_blocks=unchanged,all56_obligation_ids_in_order=True,all_old_records_match_before_after=True,ANY_NEW_B_affected_R9_findings_or_metadata_read_or_hashed=False)))
manifest=out('manifest-v1.json',dict(frozen_at_utc=now,status='ENTIRE OTHER WHOLE affected R1 complete; scoped PASS, reconciliation pending',reviewer='/root',constructor='/root/review_2017_coarsening_r1',target=rec('problems/2025-B4/notes/reasoning-return-r9-candidate-v1.1.md'),constructor_freeze=rec(inputs[0]),whole_obligations_reconstructed=56,original48_retained=True,affected_additional_checks=8,resolved_original_issues=['R9R1-01','R9R2-01'],resolved_scope_note='R9R2-N3 chosen generator only',open_substantive_issues=0,required_author_repairs=0,ENTIRE_packet_before_ANY_NEW_peer_affected_findings_or_metadata=True,original_whole_initials_already_frozen_before_comparison=True,another_OTHER_whole_affected_audit_and_root_reconciliation_required=True,requested_model='gpt-6.1-sol',requested_reasoning='max',effective_setting_readback=None,artifacts=payloads))
for r in payloads: assert rec(r['path'])==r
print(json.dumps(dict(manifest=manifest,report=payloads[0],ledger=payloads[1],input_occurrences=len(declared),unique_paths=len(unique),summary_sha256=summary,all_postverified=True),indent=2))
