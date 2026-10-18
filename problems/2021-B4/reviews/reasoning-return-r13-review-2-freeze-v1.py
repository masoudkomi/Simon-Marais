#!/usr/bin/env python3
"""Administrative-only initial WHOLE R2 freeze; no mathematical executable."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import re

R=Path.cwd().resolve()
P='problems/2021-B4/reviews/reasoning-return-r13-review-2-'
C='problems/2021-B4/notes/reasoning-return-r13-'
NOW=datetime.now(timezone.utc).isoformat()
def rec(p):
    b=(R/p).read_bytes()
    return dict(path=p,bytes=len(b),sha256=sha256(b).hexdigest())
def save(s,v):
    with (R/(P+s)).open('x',encoding='utf-8') as f:
        f.write(v if isinstance(v,str) else json.dumps(v,indent=2,ensure_ascii=False)+'\n')
rows=[]
def bind(x):
    assert rec(x['path'])==x,x['path']
    rows.append(x)
    return x
f=json.loads((R/(C+'freeze-v1.json')).read_text())
bind(dict(path=C+'candidate-v1.md',bytes=15806,sha256='25a871da93b7cd375e0af43c8643094463ac45ce913722805ba6958dee004148'))
bind(dict(path=C+'freeze-v1.json',bytes=4152,sha256='4d6b95b7c5b70301f227af7cce5169c8c691c01f6b287fdadacf0b337c40c656'))
for x in f['artifacts']:bind(x)
sources=json.loads((R/(C+'sources-v1.json')).read_text())
for x in sources['operative_local_authority']:
    bind(x)
    a=json.loads((R/x['path']).read_text())
    for k in ('candidate','accepted_copy'):bind(a[k])
    bind(rec(x['path'].replace('.json','.md')))
    assert (R/a['accepted_copy']['path']).read_bytes().endswith((R/a['candidate']['path']).read_bytes())
# Reconstruct the constructor's compact selected-parent validation, not its historical inventories.
validation=json.loads((R/(C+'input-validation-v1.json')).read_text())
authorrows=[]
for group in validation['groups']:
    if 'metadata' in group:
        x=group['metadata'];bind(x);authorrows.append(x)
        obj=json.loads((R/x['path']).read_text())
        selector=group.get('selector','')
        if 'artifacts[0:7]' in selector or 'artifacts[0:10]' in selector:
            for y in obj['artifacts']:bind(y);authorrows.append(y)
        elif 'acceptance Markdown' in selector:
            for y in (rec(x['path'].replace('.json','.md')),obj['candidate'],obj['accepted_copy']):
                bind(y);authorrows.append(y)
    else:
        for x in group['records']:bind(x);authorrows.append(x)
def summary(items):
    u={x['path']:x for x in items}
    ordered=[u[p] for p in sorted(u)]
    return dict(occurrences=len(items),unique_paths=len(u),sha256=sha256(json.dumps(ordered,sort_keys=True,separators=(',',':')).encode()).hexdigest()),ordered
asum,_=summary(authorrows)
assert asum['occurrences']==33 and asum['unique_paths']==32
assert asum['sha256']=='c1d4beb5b4c668bbb077bc58520926f39c0658c25be3ef17f6f97171f257906b'
bind(rec('problems/2020-B4/reviews/reasoning-arithmetic-return-r9-review-1-manifest-v1.json'))

save('initial-v1.md','''# OTHER initially blind WHOLE R2: complete R13A–R13C

2026-10-18 UTC. Reviewer /root. **Scoped PASS; reconciliation pending.**
The ENTIRE new A constructor packet, all11 files, was read. The target
main is15806B SHA25625a871da93b7cd375e0af43c8643094463ac45ce913722805ba6958dee004148.
ALL44 obligations were hand reconstructed. No substantive defect, required
author repair or action advisory was identified. B's NEW R13 review,
findings, source record, ledger and metadata remain unread/unhashed.
B was asked to send completion identity only until this ENTIRE packet
freezes. Root gave only the broad assignment, with no new R13 inference.
Older R8/R12 whole-review roles and the R5 counting clarification are
disclosed; those accepted inputs are not independently self-certified anew.

## Exact branch and whole mathematical reconstruction

Official(b) requires actual rational witnesses for every derivative of a
rational polynomial. It does not make the other roots rational or real.
The candidate is confined to the normalized degree20, J15, sole-H3,
double-origin branch with an ADDITIONAL actual rational double small s.
The four distinct rational values are0,1,r,s, with r/1 simple and0/s double;
v(r)=v(s)=nu≥1 and s/r=2 modulo19. No equality s=2r is assumed.
The rational irreducible degree14 carrier is an accepted actual factor,
not the result of treating a merely local factor as rational. D_j,
H_k and all binomial divisions are defined over Q before reduction.

The precise accepted R8 fork at m5 has essential nonzero NONUNIT center
at H10/11/12 or depths(a7,a8,a9,a10)≥(nu,2nu,3nu,4nu); its cubic case
is absent at m5. The alternatives may overlap. Its Euler polynomial is
W=h10+h12Z+h14Z²+h16Z³+h18Z⁴+Z⁵; W(r²) is zero at displacement0,
otherwise has valuation≥9nu+1. It also forces a10 nonunit. R12A applies
only under its exact SIX nonunit-even hypotheses; those must be verified
before using any of its unit conclusions. No old finite certificate was rerun.

For R13A reflect a quartic with root2 by z↦2−z. Even degree preserves
monicity, derivative nodes remain in{0,1,2}, and the even-derivative
functional at1 is unchanged. This purely field operation makes the root0
without asserting a symmetry of f. Write q=z⁴−4v z³+Cz²+Bz. The H3
condition gives that cubic coefficient; H2(q)(t)0 gives C=12vt−6t² and
q'(u)0 gives B=−4u³+12vu²−2Cu. No possibly zero variable is divided out.
The functional expands to106−208v+18C+B, hence11+v−C+B modulo19.

I independently substituted u0,1,2 and t0,1,2. The affine coefficient/
constant pairs are (1,11),(8,17),(15,16); (13,7),(15,6),(17,3);
(11,17),(8,9),(5,4). Their unique roots are respectively8,5,4;
17,11,11;14,6,3. For example8*5+17=57,15*4+16=76,13*17+7=228,
15*11+6=171,17*11+3=190,11*14+17=171,8*6+9=57 and5*3+4=19;
the first cell1*8+11=19. Every coefficient is nonzero and every root
is outside{0,1,2}. This checks all27 last-node possibilities, including
coincident nodes and zero lower coefficients, by exact hand algebra.
It is a weighted interpolation obstruction, not a quartic CA theorem.

Under T4, the actual preceding H2/H4/H6/H8 equations at r force
a18,a16,a14,a12 nonunit: their monic integral D_j equations at a point
of positive valuation have constant congruent0. T4 supplies a8,a10
nonunit, completing Q6, and a7 is nonunit. Thus accepted R12A FORCES
a6 unit and D7(1),D8(1) units. The scalar factors19 beta7/8 have
valuation1, so H13(1),H12(1) are nonzero with valuation1. Actual
rational common-root hypotheses now supply genuine noncenter witnesses
for those two orders. A unit a6 is obtained here, not assumed from T4.

Set A=a6 and P=D10(rz)/(A r⁴) over Q. T4 makes degrees0–3 integral;
the degree4 coefficient210 is1 mod19; every higher degree has excess
at leastnu. In particular a5 may be unit and still disappears. Thus
the reduction is a MONIC quartic. Exact differentiation gives
H_i(P)=binom(10,i)D_(10−i)(rz)/(A r^(4−i)), i0..4. Integrality follows
from the same coefficient bounds, and10,45,120,210 are19-units.

Divide W(r²) by19 beta10 A r⁴ BEFORE reduction. Its valuation is zero
element or at least5nu>0. The h16/h18 terms have excess≥2nu/4nu,
and the leading r^10 term has excess6nu−1>0, includingnu1. Hence only
h10,h12r²,h14r⁴ survive. Direct rational beta values9724,6630,2040
reduce to15,18,7 at indices10,8,6. Ratios are5 and3, while45≡7
and210≡1, giving the precise functional q(1)+17H2(q)(1)+3H4(q)(1)=0.
As a separate hand check, the unreflected quartic is
c+10bz+7dz²+6ez³+z⁴ with normalized coefficient residues c,b,d,e;
the surviving expression is c+10b+12d+8e+11. At root0 its linear,
quadratic and cubic coefficients convert this to11+v−C+B. No old
m7/m3 functional, division by displacement or finite depth cutoff is used.

If H10 and H11 both have actual noncenter witnesses, the H10 witness
is0 or s since H10(r)≠0. It gives w0/2 after scaling. H11 and the
forced H12/H13 noncenters give u,t,v in{0,1,2} through the exact integral
derivative identities. These are actual zero equations reduced to field
conditions, never assertions that a field root lifts. Local node1 is r,
not original center1. Multiple choices and coincident nodes are included
in the finite lemma. It contradicts the Euler functional. R13B excludes
T4 PLUS BOTH noncenters, and does not exclude T4 with an essential center.

For the full R13C fork, an R8 nonunit EC12 would make a8 nonunit;
the preceding ladder and accepted Euler estimate make the other five
Q6 coefficients nonunit. R12A would then force D8(1) unit, contradicting
that actual center. Therefore EC12 is impossible. The accepted m5 fork
now either directly gives EC10/11, or T4. Under T4, if H10 or H11 lacks
a noncenter rational common value, its required witness is1. Its constant
cannot vanish, because then0 is a noncenter common value. Its T4 depth
is≥4nu or3nu and hence meets the exact NONZERO NONUNIT EC condition.
If both have noncenters, R13B is the contradiction. This exhausts even
overlapping alternatives. When a8 is unit, T4 and nonunit EC12 are
already unavailable, so R8 supplies EC10/11 directly; Q6 is not misused.

Finally the actual irreducible rational carrier g has degree14, whereas
H10/H11 have degrees10/9. A root in common would make g divide that
derivative, impossible. All common values thus lie among0,1,r,s, and
the selected order has sole value1. Since1 is simple in f, its FULL
monic gcd is exactly X−1, over Q and after scalar extension. No stronger
R5 equal-degree argument, all-real-root theorem or quotient-CA inference
is needed for these two orders.

The diagnostic q=(z−1)^4−1 has roots0/2 and derivative nodes1; its
functional with final coefficient1 vanishes, while with coefficient3
it is2. This confirms the sharp distinction between functionals; it is
not an actual contest counterexample. The remaining EC10/EC11 cases,
full m5, m3/m4, other normalized branches, degree20 and the annual
question are not eliminated. The candidate establishes its written
scoped necessary conclusion only. Two OTHER whole audits and root
reconciliation precede acceptance; this is one of those audits.
''')
checks=[
'Actual Q polynomial and Q common witness at EVERY derivative, not all roots rational/real.',
'Exact extra actual double-s domain, degree20/J15/sole-H3, four values and multiplicities retained.',
'Equal integral nu≥1 and s/r≡2, arbitrary displacement including zero.',
'Actual rational carrier degree14 and accepted irreducibility, no local-to-rational inference.',
'D/H indexing, monic integral normalization and unit beta denominators defined over Q first.',
'Exact accepted R8/R12/R5 scopes, author and root older roles disclosed.',
'Actual m5 first break includes H2/H4/H6/H8 ladder; cubic fork absent, overlaps allowed.',
'EC is sole center plus nonzero NONUNIT constant at depth≥nu, not merely center availability.',
'Weighted quartic lemma is direct algebra, no small-degree CA import.',
'Reflection2−z preserves monicity, node sets and even functional; no f symmetry.',
'H3 node gives cubic coefficient−4v using characteristic19 unit4.',
'Second and first derivative equations give exact C/B including zero/coincident cases.',
'Functional expands106−208v+18C+B to11+v−C+B.',
'Independent substitution at u0/1/2 gives the three exact affine equations.',
'All nine nonzero coefficients and roots8,5,4,17,11,11,14,6,3 hand checked.',
'All roots outside0/1/2, covering all27 last-node choices and zero constants.',
'Earlier actual even equations force a12,a14,a16,a18 nonunit.',
'T4 gives a8,a10 nonunit, exactly completing six-even Q6.',
'T4 also gives a7 nonunit; R12A FORCES a6 and D7(1) units.',
'D7/D8 units give actual H13/H12 center nonvanishing with valuation1 and noncenter witnesses.',
'P formed over Q and its first four coefficients integral by T4.',
'Degree4 coefficient210≡1 and higher terms disappear even with unit a5.',
'Hasse differentiation/scaling exact before reduction, unit binomial scalars checked.',
'm5 Euler W has precisely h10,h12Z,h14Z²,h16Z³,h18Z⁴,Z⁵.',
'Zero displacement separate; other W-depth9nu+1 leaves excess5nu after division.',
'Later terms excess2nu/4nu and leading6nu−1 positive for allnu≥1.',
'Exact beta integers/residues9724/15,6630/18,2040/7, rational cancellations first.',
'Hasse conversion coefficients17 and3 verified, also direct coefficient expression.',
'Actual H10 noncenter0/s because value at r nonzero; scaled root0/2.',
'Actual H11/H12/H13 give derivative nodes0/1/2; local1 distinguished from center.',
'Any multiple available witnesses, coincident nodes and infinite valuations covered.',
'Finite lemma contradicts actual T4+both-noncenter branch, no lifting converse.',
'T4 with essential center not excluded by R13B.',
'At any m5, nonunit EC12 plus ladder/Euler yields all Q6 conditions.',
'R12A unit D8(1) excludes EC12 at every finite nonunit depth.',
'Complete R8 fork reduces to EC10/11 or T4, no disjointness assumption.',
'No noncenter under T4 forces center, nonzero constant and exact EC depths.',
'Both noncenters contradict R13B, hence every actual m5 break has EC10/11.',
'Unit-a8 case handled by R8 directly; R12A not applied outside Q6.',
'Rational irreducible carrier14 exceeds derivative degrees10/9; simple1 yields full gcdX−1.',
'Wrong-functional quartic diagnostic checked, not an actual rational CA lift.',
'EC10/11, fullm5/m3/m4 and other branches remain open; no height/real/quotient theorem.',
'Primary normalization and full prime5 erratum read limits kept; no novelty/external validation.',
'Complete constructor and all44/code/source/meta freeze before peer; no mathcode or promotion.',
]
assert len(checks)==44
save('ledger-v1.md','# Complete independent ALL44 ledger\n\n2026-10-18 UTC. /root OTHER WHOLE R2. Every row hand reconstructed.\n\n|ID|Result|Independent check|\n|---|---|---|\n'+''.join(f'|{i:02d}|PASS|{s}|\n' for i,s in enumerate(checks,1)))
save('issues-v1.md','''# Initial R13 R2 issues

2026-10-18 UTC. No substantive defect, author repair or action advisory
identified after ENTIRE whole reconstruction of ALL44 obligations.
Retained boundaries: actual double rational s; exact Q6 before R12A;
four-depth branch is only excluded with both actual H10/H11 noncenters;
the final Euler coefficient is3; forced EC10/11 is not itself a contradiction;
full gcd uses actual rational irreducible carrier14 and simple1. These
already-explicit limits are not requested repairs. NEW B R13 material
remains unread and unhashed before this ENTIRE initial freeze.
''')
save('source-audit-v1.md','''# Actual R13 R2 source/read scopes

2026-10-18 UTC. ALL11 constructor files read fully, including full
44 obligations, constructor hand checks/failures/log, freezer CODE not run,
source JSON, compact validation, output and freeze. Complete accepted
R12 body was read during its earlier whole R2 audit this same sustained
session; fresh header/domain/proposed claims and operative Q6 scope
reread now. Accepted R8 complete scope and operative sections0/claims/2
reread, including exact Euler estimate and full m5 fork. Accepted R5
header/domain and carrier scope read. Complete three authority JSON and
R8/R12 acceptance Markdown read. No claim to replay or fresh independent
reaudit of all old finite certificates or every unrelated R5/R8 section.

[Official2021 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf):
fresh B4 lines67–81 read, actual rational witnesses and(b) scope matched
the full local statement. No preliminary proof or other problem researched.

[CLO original author preprint](https://arxiv.org/pdf/1208.5404): served
v1,23pages. Fresh complete normalized context§3.4, Lemma17 and§3.5
equations9–13, lines898–1126, read; Proposition19/proof and unramified
remark1163–1307 read. Published method attributed. Stronger all-root-rational
or unramified hypotheses do not hold for the ramified degree14 carrier.
No whole23-page audit or computational attachment replay claimed.

[Draisma–de Jong erratum](https://math-unibe.ch/jdraisma/publications/erratumcasasalvero.pdf):
fresh complete one-page correction, all20 extracted lines read. The
prime5 exception is retained; no invalid degree20 shortcut imported.

No new download/cache or remote response hash, CAS, mathematical test,
scan, paid access, contact or third-party redistribution. NEW field
certificate and all valuation/fork steps were independently hand audited.
''')
save('worklog-v1.md','''# Actual R13 OTHER R2 work log

2026-10-18 UTC. Root completed its ENTIRE independent2020A9 R1 before
starting this ENTIRE2021R13 R2. B's R13 review was queued after its A9 R2;
B has been explicitly told to send completion IDENTITY ONLY until root
confirms this ENTIRE initial freeze. No NEW B R13 reports, findings,
ledger, sources or metadata were opened/read/hashed. Root provided no
new R13 mathematical step; older review/contribution roles are disclosed.

Read all11 frozen constructor files; used exact accepted input scopes
and fresh primary operative passages recorded in the source audit. A
guessed hand-check filename did not exist; the actual freeze identified
constructor-checks-v1.md, which was then fully read. No file was changed.
All44 obligations were independently reconstructed. All nine affine
equations and27 residuals were checked by hand, together with exact beta
ratios and a separate direct coefficient functional. This was not a
program, mask scan, old certificate replay or author rerun.

Adversarial boundaries checked: nu1, displacement0/arbitrary finite
depth, zero coefficients/infinite valuations, unit a5 and unit a8 outside
T4, forced rather than assumed a6 unit, original center/localnode1,
coincident/multiple actual witnesses, overlapping alternatives, and
rational irreducible carrier versus mere local factor. No root-lifting,
all-real, sign, height, maximum depth or quotient-CA inference appears.

Only this new assigned review prefix is written. Compact immutable
parents and exact author declarations are byte-verified, without copying
all historical inventories or claiming unrelated old proofs reread.
The complete report, ALL44 ledger, issues, source audit, this log, code
and ALL necessary metadata are written and frozen before any NEW peer
R13 material. Hashing/JSON/syntax checks are administrative, not proof.
Root's latest direct weekly reading8% TOTAL at01:22:58UTC,10080-minute
window/reset1792874445, ordinary use allowed, remains below authorized90%
TOTAL. No later-reset spending, charge, contact, native child or pending
approval. Research continues; the remaining EC10/11 cases are not solved.
''')
sm,ordered=summary(rows)
save('baseline-v1.json',dict(captured_at_utc=NOW,summary=sm,records=ordered,constructor_selected_parent_summary_reconstructed=asum,historical_rows_bound_not_recopied=True))
save('metadata-v1.json',dict(status='ENTIRE OTHER initially blind WHOLE R2 complete; scoped PASS pending reconciliation',reviewer='/root',constructor='/root/review_2021_reasoning_j15_r2',all_obligations=44,substantive_issues=0,required_repairs=0,advisories=0,root_new_R13_inference=False,NEW_peer_R13_findings_files_metadata_read_or_hashed=False,requested_model='gpt-6.1-sol',requested_reasoning='max',verified_effective_setting_readback=None,mathematical_executable_CAS_scan_or_author_rerun=False,source_read_limits=P+'source-audit-v1.md',promotion=False))
for x in ordered:assert rec(x['path'])==x
assert re.findall(r'^\|(\d\d)\|PASS\|',(R/(P+'ledger-v1.md')).read_text(),re.M)==[f'{i:02d}' for i in range(1,45)]
save('input-validation-v1.json',dict(validated_at_utc=NOW,summary=sm,all_exact_declared_inputs_match=True,all44_ledger_rows_present=True,constructor33occ32paths_summary_reconstructed=True,administrative_checks_not_mathematical_tests=True))
suffixes=['initial-v1.md','ledger-v1.md','issues-v1.md','source-audit-v1.md','worklog-v1.md','freeze-v1.py','baseline-v1.json','metadata-v1.json','input-validation-v1.json']
save('manifest-v1.json',dict(frozen_at_utc=NOW,status='ENTIRE OTHER initially blind WHOLE R2 complete; scoped PASS pending reconciliation',reviewer='/root',constructor='/root/review_2021_reasoning_j15_r2',target=rec(C+'candidate-v1.md'),constructor_freeze=rec(C+'freeze-v1.json'),all_obligations_reconstructed=44,substantive_issues=0,required_repairs=0,advisories=0,ENTIRE_before_ANY_NEW_peer_findings_files_or_metadata=True,summary=sm,artifacts=[rec(P+s) for s in suffixes]))
print(json.dumps(dict(manifest=rec(P+'manifest-v1.json'),report=rec(P+'initial-v1.md'),all44=True,summary=sm),indent=2))
