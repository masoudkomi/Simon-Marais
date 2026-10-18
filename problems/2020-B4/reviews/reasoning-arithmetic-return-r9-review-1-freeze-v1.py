#!/usr/bin/env python3
"""One-shot administrative review freeze; no mathematical executable."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import re

ROOT = Path.cwd().resolve()
P = 'problems/2020-B4/reviews/reasoning-arithmetic-return-r9-review-1-'
C = 'problems/2020-B4/notes/reasoning-arithmetic-return-r9-'
NOW = datetime.now(timezone.utc).isoformat()

def rec(path):
    data = (ROOT / path).read_bytes()
    return dict(path=path, bytes=len(data), sha256=sha256(data).hexdigest())

def write(suffix, value):
    with (ROOT / (P + suffix)).open('x', encoding='utf-8') as out:
        out.write(value if isinstance(value, str) else json.dumps(value, indent=2, ensure_ascii=False) + '\n')

freeze = json.loads((ROOT / (C + 'freeze-v1.json')).read_text())
assert rec(C + 'candidate-v1.md') == dict(path=C+'candidate-v1.md', bytes=20253, sha256='aab97b7ba5c91d17e9e82f18a58db400bcddd1afb11081917d6f12a1f31fd892')
assert rec(C + 'freeze-v1.json') == dict(path=C+'freeze-v1.json', bytes=2811, sha256='c90992cdc72cc411b8dbec2b811bbd39fb3e9e948e1559dd4e6163487a4ec5ef')
occurrences = []
for item in freeze['artifacts']:
    assert rec(item['path']) == item, item['path']
    occurrences.append(item)
occurrences.append(rec(C + 'freeze-v1.json'))
baseline = json.loads((ROOT / (C + 'baseline-v1.json')).read_text())
for item in baseline['records']:
    assert rec(item['path']) == item, item['path']
    occurrences.append(item)
# Bind precisely the old root records, without opening any NEW peer review.
for path in (
    'problems/2025-B4/reviews/reasoning-return-r9-review-1-reaudit-v1.1-manifest-v1.json',
    'problems/2017-B4/notes/coordinator-plane-recovery-r1-freeze-v1.json',
):
    occurrences.append(rec(path))
unique = {x['path']: x for x in occurrences}
ordered = [unique[p] for p in sorted(unique)]
digest = sha256(json.dumps(ordered, sort_keys=True, separators=(',', ':')).encode()).hexdigest()

write('initial-v1.md', '''# OTHER initially blind WHOLE R1: arithmetic A9A–A9F

2026-10-18 UTC. Reviewer /root. **Scoped PASS; coordinator reconciliation pending.**
This is an independent whole audit of the COMPLETE frozen C submission,
20253 bytes, SHA256 aab97b7ba5c91d17e9e82f18a58db400bcddd1afb11081917d6f12a1f31fd892,
and all nine accompanying constructor files including the freeze.
ALL56 obligations were reconstructed by hand. No substantive defect,
required repair or action advisory was identified. This is one OTHER
audit, not promotion or an annual solution. B's NEW A9 review, findings,
ledger, source files and metadata have not been read or hashed. Root has
asked B to send completion identity only until this ENTIRE packet freezes.
The frozen constructor's future R10 work is not a premise and is unread.

Root gave only the broad research assignment and supplied no new A9
inference. Root reviewed older R7/R8 and integrated accepted earlier
work; those roles do not constitute construction of this NEW A9 argument.
The accepted inputs retain their original authorship and two-OTHER review
authority. This review does not independently self-recertify old input.

## Whole reconstruction and adversarial checks

Only official2020(b) is at issue. q=n−1≥2 and prime p=q²+q+1 are EXTRA
restrictions. Every relevant prime divisor belongs to the fixed odd T;
thus q has order3, T is nonidentity and F/E is a CM quadratic extension.
The relative identity alpha times its conjugate equals a rational integer
is essential; an absolute norm would not give the trace energy. q cannot
be a square, because q=b² factors p into b²+b+1 and b²−b+1, both >1.
The n2 boundary and composite moduli remain outside all new claims.

A9A correctly attributes its bound to published Leung–Schmidt Theorem23.
I separately checked the candidate's complete prime-case reconstruction.
Tracing gives a(p−1)=p sum(c_i²)−(sum c_i)², also the pairwise squared
difference sum. With maximum coefficient multiplicity t, the unequal
pair count gives t>p−2a. Under the contrary bound p>a²+a+1, p>4a;
a2 uses the next possible prime ≥11. Subtracting the majority coefficient
preserves the cyclotomic element and leaves u<2a<p/2 nonzero entries.
Their differences from the zeros give u(p−u)≤a(p−1). Monotonicity and
the exact positive excess p−a²−a−1 at u=a+1 force u≤a.

The integral evaluation kernel really is Z times Phi_p in degree≤p−1,
so B B^−=a+lambda N with INTEGER lambda. For lambda0, augmentation
would make nonsquare a an integer square. For nonzero lambda each of
p−1 nonzero residues must be a difference of two distinct support
indices, while at most u(u−1)≤a(a−1) ordered pairs are available.
Signed coefficients or cancellation cannot create a missing difference.
This contradicts p−1>a(a−1). No positivity or fixed augmentation was
silently needed. At the planar p, every smaller positive nonsquare norm
is therefore excluded. For a hypothetical Weil factorization of normq,
one proper integer norm is nonsquare; it is forbidden. This proves only
the written semigroup indecomposability. It does not prove ordinary ring
irreducibility or qprime; the attributed existing norm8 example remains.

A9B must work for arbitrary supported exponents, and it does. Above the
support, Frobenius in T gives complete splitting and relative degree1,
so there is no valuation obstruction. Away from support and p, a is a
unit and the relative extension is unramified or trivial; successive
residue trace corrections give unit norms, also at residue2. At p the
residue of a is in odd T, so a^((|T|+1)/2) is its nonzero square root.
Hensel applies with derivative2r a p-unit. The resulting Qp element
lies in E_v and is a relative norm since its square is a. At infinity
the positive rational a is a complex-to-real norm at every place.
Cyclic Hasse now supplies a FIELD element z, with denominators allowed.

For a PRINCIPAL balanced integral ideal B=(gamma), gamma is integral;
epsilon=gamma conjugate(gamma)/a is a unit of E and the field norm of
gamma/z. The exact standalone accepted R8B lemma uses odd ORDINARY h(F)
to produce a UNIT u of norm epsilon. Dividing gamma by u preserves both
integrality and the SAME ideal, and gives exact norma. A mere norm-one
kernel statement, positivity, an even class number, or odd h(E) would
not suffice. Combining with A9A makes EVERY such proper nonsquare
balanced ideal nonprincipal in this domain, not only a chosen example.

A9C chooses any one-of-each-pair balanced ell-ideal. Its class is in
Cminus, and its order r is odd because the whole ordinary class group
has odd order. Its rth power is principal and balanced; A9B applies even
when r exceeds the exponent of ell inq. Thus the norm ell^r exists and
is nonsquare, forcing ell^r≥q. If q is not an ell-power, equality is
impossible and r>log_ell q>e_ell. The order r divides exp Cminus,
giving the stated necessary exponent bound. At h(F)1, r1 for every
choice and any compositeq has a proper prime factor ell<q: contradiction.
There is no converse or assertion that the uncomputed class number is odd.

A9D keeps the EXACT accepted sufficient tests. At non-prime-power q,
nonsquareness selects a rational prime whose entire exponent e is odd;
a=ell^e is a PROPER nonsquare supported integer. The one-prime baseline
obeys 2b0=−e sum delta_i, by the principal factorization of ell. For
odd m_i, choose 0≤a_i≤m_i−1 with 2a_i=e mod m_i. The long-interval
hypothesis places these exponents in0..e, including m_i1/a_i0. The
resulting integral balanced partial ideal has class x with2x0; odd C
forces x0. A9B then contradicts the small-norm bound. This rules out the
easy CERTIFICATE, not the full mixed class criterion or all actual D.
The full-class exponent-divisibility test implies these intervals since
each m_i divides m and each positive e_ell multiple of m is at least m_i.
For q=ell^e, the principal balanced mth power has nonsquare normell^m,
so m≥e; m|e then gives m=e. Conversely that equality gives the test.
The accepted perfect-power prime-value lemma applies before any plane
or saturation assumption and forces e a power of3, including1.

A9E starts with an ACTUAL normq character. For squarefree q, its ideal
has exactly a0/1 exponent pattern above each ell, so its ell-primary
factor is balanced of normell. Their classes lie in the SAME Cminus,
their full sum is zero, and every nonempty proper product has nonsquare
norm<q. By A9B/A9A none of these proper products is principal. This is
a minimal zero-sum sequence, with each class nonzero when q is composite.
In a minimal sequence of length t, the t partial sums up to the penultimate
one are distinct, proving t≤|Cminus|. Accepted R8C gives Cplus=jCl(E)
under odd h(F), with j injective. Division by2 in the finite odd group
decomposes C into plus/minus eigengroups, so |Cminus|=h(F)/h(E).
No abstract sequence realizes the specified prime ideals, principal full
product or actual character. Repeated-prime layers can have square norm,
so this exact minimality conclusion is deliberately restricted.

A9F is independent of class numbers and of actual existence up to its
explicit corollary. Since q has order3, |T|=3d and ell^(3d)=1 modp.
The only cube roots are1,q,q², distinct because p≥7. If 1<ell^d<p,
its ordinary value would equal one of those three residues;1 is
impossible, and q or q² would make q an ell-power. Equality ell^d=p
is impossible for the different prime ell<p. Hence ell^d≥p+1, and
|T|≥3 ceil(log_ell(p+1))>6 log_ell q since p+1>q².

For ACTUAL full M satisfying the separately assumed small upper bound,
this forces q=ell^e. Its residue order is exactly3e: a proper divisor
u of3e is ≤3e/2<2e, whereas p dividing ell^u−1 would be impossible
between0 andp. Actual M is odd and contains that subgroup. Thus its
odd index is ≤2 and must be1, proving M=<ell> and |M|3e in this
restricted situation. No universal smallness, Desarguesian structure,
composite-modulus replacement or new numerical order follows.

## Verdict and surviving mathematical gap

All56 checks pass in their written domains. The cited norm bound is
known; the new deductions are scoped applications without a priority
claim. The candidate usefully closes the tempting easy-test route to
non-prime-power existence, but the full principal product may still
involve genuinely mixed nonprincipal classes. Nothing excludes that
actual cancellation. Even class number, square partial norms and
composite-modulus gluing retain their original gaps. This review and its
byte checks are not external validation, a computation of any class
group, a new forbidden numerical order or the annual answer. A second
OTHER entire whole review and coordinator reconciliation remain required.
''')

checks = [
'Official(b) only; q≥2, extra prime planar modulus, q1 excluded.',
'Relative conjugation identity, not an absolute norm; actual sets distinguished.',
'C old construction/review roles disclosed; root supplied no NEW A9 step.',
'Accepted R8 fixed odd T contains every prime divisor; ordinary h(F) condition retained.',
'Published Theorem23 actual statement and complete operative proof read; own prime proof audited.',
'Tracing conjugation norm yields both exact signed-coefficient energy identities.',
'Unequal-pair count and sum multiplicity squares≤tp give strict t>p−2a.',
'Contrary bound implies p>4a, with nonsquare a2 prime endpoint checked.',
'Subtracting majority constant preserves alpha; u<2a<p/2 and zero-cross energy bound.',
'Monotonicity and exact excess p−a²−a−1 force u≤a.',
'Integral group-ring evaluation kernel is ZN, including integrality of lambda.',
'lambda0 augmentation gives an integer square, contradicting nonsquare a.',
'Nonzero lambda needs all p−1 differences; signed/cancelling coefficients cannot exceed u(u−1).',
'Strict planar threshold excludes every smaller positive nonsquare norm without h(F).',
'Square q factorization excludes it; Weil factorization has a proper nonsquare norm.',
'Norm8 example is attributed existing context, no ordinary irreducibility or primality inference.',
'q exactorder3 and odd T excludes−1 before existence; CM quadratic extension.',
'All support primes split completely; conjugate pairs distinct; balanced ideals exist.',
'Arbitrary supported exponents permitted; relative split norms have no valuation restriction.',
'Unramified unit norms at all other non-p places, including residue2.',
'Odd-T residue square and p-unit derivative justify Hensel at the ramified place.',
'All real places checked positive; cyclic Hasse supplies only FIELD norm.',
'For integral principal B, gamma integral and epsilon is an E-unit plus a FIELD norm.',
'Accepted standalone odd ordinary class norm-unit lemma supplies unit preserving SAME ideal.',
'Even h(F), positivity alone, h(E) parity and kernel substitutions explicitly excluded.',
'ANY balanced ell-ideal of paired exponents0/1, no favorable-choice quantifier.',
'Its ideal class belongs to minus eigengroup, distinct from stabilizer information.',
'Class order r odd, including r1, so ell^r nonsquare.',
'rth power integral principal balanced; arbitrary-exponent correction actually applies.',
'Norm theorem forces ell^r≥q for EVERY balanced choice.',
'At non-prime-powerq equality impossible and log_ell q>e_ell.',
'r divides exp Cminus, hence that exponent>every e_ell; no computed value asserted.',
'h(F)1 gives r1 and excludes compositeq; no converse or universal parity claim.',
'm_i exact odd class orders include1; full exponent m distinguished from minus exponent.',
'Nonsquare non-prime-powerq has a prime component of odd exponent and proper norm.',
'One-prime factorization gives exact 2b0=−e sumdelta, independent of other primes.',
'Odd m_i solves half-residue; interval bounds actual nonnegative exponents, including m_i1.',
'Constructed integral balanced partial ideal has2x0; odd class group forces principality.',
'Corrected generator contradicts norm bound; only sufficient long-interval test ruled out.',
'Full exponent-divisibility implies intervals because positive e multiplem≥m_i.',
'At prime power, principal mth balanced power gives m≥e; m|e yields equality.',
'Equality expCl(F)=e at primepower conversely gives THAT test only.',
'Accepted perfect-power prime-value lemma forces e powerof3 without saturation/classicality.',
'Actual squarefree character ideal decomposes into balanced prime factors in same field.',
'Every nonempty proper squarefree subproduct has supported nonsquare norm<q, nonprincipal.',
'Full sumzero and every proper sum nonzero give actual minimal zero-sum sequence.',
'Distinct partial sums prove length≤|Cminus| without an external Davenport import.',
'Accepted injective plus extension and finite odd-group divisionby2 give h(F)/h(E).',
'No abstract realization converse; square layers/even classes/composite modulus remain gaps.',
'No odd-h(F) needed for group gap; qorder3 and cube-root residues exact.',
'Ordinary ell^d belowp cannot equal1,q,q² at non-ell-powerq; equalityp also impossible.',
'Integer ceiling and strict logarithmic inequality use p+1>q², no approximation.',
'Small FULL M upper bound remains extra; no universal size assertion.',
'At primepower ordell=3e and odd index≤2 forces exact full group in restricted corollary.',
'Known subgroup may use gap without equating full M; primality essential.',
'All source/read limits, immutable bytes, no mathcode/scan/novelty/annual promotion checked.',
]
assert len(checks) == 56
write('ledger-v1.md', '# Complete independent ALL56 ledger\n\n2026-10-18 UTC. /root, OTHER WHOLE R1. Each row hand reconstructed.\n\n|ID|Result|Independent check|\n|---|---|---|\n' + ''.join(f'|{i:02d}|PASS|{s}|\n' for i,s in enumerate(checks,1)))
write('issues-v1.md', '''# Initial R1 issue log

2026-10-18 UTC. No substantive defect, required repair or action advisory
identified after whole reconstruction of ALL56 obligations.

Scope boundaries enforced: published small-norm theorem is attributed;
odd ORDINARY h(F) is essential outside A9A/F; field norm does not give
integrality; only a PRINCIPAL balanced ideal is corrected; easy sufficient
tests are not necessary for actual existence; squarefree minimality is
one-way; the full-group size upper bound is extra. Mixed class cancellation,
even class numbers, repeated square layers and composite gluing remain open.
These are retained limitations, not repairs to the submitted statement.

No NEW B A9 result or metadata was consulted before this ENTIRE freeze.
''')
write('source-audit-v1.md', '''# R1 actual source and reading limits

2026-10-18 UTC. COMPLETE new candidate, obligations, sources, failed routes,
worklog, freezer CODE (not run), baseline, metadata, validation and freeze
read. Complete accepted R8 body and header reread, including standalone
norm-unit lemma, plus-class injection and exact easy tests. Accepted R8
acceptance JSON/Markdown read completely. Accepted R7 header/domain,
complete sections R7B/R7C and R6 header/domain read; operative R5B1 lemma
read completely. No claim to fresh complete rereads of unrelated R4/R5/R6/R7
proof sections or every surveyed source. Their accepted authority and
declared fingerprints are checked, not self-recertified.

[Official2020 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2020-paper-b_1.pdf):
fresh B4 lines98–105 read; part(b) domain matches the complete local
statement. Other returned problems were not investigated. No preliminary
construction was reproduced. Full official solutions not newly audited.

[Leung–Schmidt author PDF](https://personal.ntu.edu.sg/bernhard/Publications/pub/BentFunctions.pdf):
41pages. Actual tool reading includes frontmatter/early context through495,
Corollary21/proof and adjacent context870–1120, Theorems22–23 and complete
operative proofs1121–1267, plus following context returned through1530.
The published nonsquare norm bound has the needed prime-conductor special
case. The candidate's trace/support reconstruction was separately checked.
No complete41-page audit, original Cassels read, or later table import.

[Kedlaya Hasse theorem](https://kskedlaya.org/cft/sec_ideles-cohom2.html):
fresh complete Theorem7.2.10/proof and cyclicity warning618–643 read.
This is an attributed classical field-norm theorem, with all places
checked in the candidate; its full CFT foundation is not reconstructed.

[Kedlaya local norm results](https://kskedlaya.org/cft/sec_localcomp.html):
fresh complete Propositions4.2.4–4.2.5 with proofs449–478 read. Unramified
unit surjectivity includes residue2 and the trace-correction argument.

No new PDF download/cache/hash, external mathematical code, class-group
computation, paper redistribution or paid access. C's source-ledger reading
of Duc–Schmidt and unsuccessful class.pdf decoding is recorded as C's
work, not claimed as a new root direct proof read. Neither is a premise.
''')
write('worklog-v1.md', '''# Actual R1 work and independence log

2026-10-18 UTC. Root was assigned OTHER NEW A9 WHOLE R1 after C's ENTIRE
constructor freeze. B is OTHER R2 and was expressly asked to send completion
identity only until root's ENTIRE initial freezes. No NEW B A9 material
was opened, read, hashed or used. Root's generic research assignment
contributed no new A9 inference. Older R7/R8 review and integration roles
are disclosed; this is not a self-review of those accepted inputs.

Read all ten constructor files and hand reconstructed ALL56 obligations.
Read accepted and primary material within the exact source ledger limits.
One combined display was truncated; affected accepted R8 ranges and new
metadata were reread separately. A guessed older acceptance filename and
a guessed old root freezer filename did not exist; no file was changed.
Subsequent rg discovery identified the actual records. No omitted source
read is claimed on the basis of truncation or a filename guess.

Adversarial cases included signed coefficients, a2, lambda0/nonzero,
unrestricted supported exponents, residue2, unit norma1, r1/m_i1,
ordinary versus narrow/relative class parity, exact same ideal after unit
correction, repeated square layers, distinct cube roots, strict endpoints,
known subgroup versus full M and no classicality inference. No mathematical
program, CAS, scan, certificate replay or author rerun was used. This
script only freezes text, hashes exact declared bytes and serializes JSON.

Fresh root account telemetry at2026-10-18 01:22:58UTC is8% TOTAL in the
authorized10080-minute weekly window reset1792874445, ordinary use allowed.
User authorized continued research up to90% TOTAL of this window; root
owns monitoring and keepawake. No spending into a later reset is authorized.
There is no new native child, pending permission, charge or contact.

No old constructor, old review, accepted proof, shared or Git file is
edited by this packet. Compact parent records are bound without recursively
rehashing all historical root work. The initial report, ALL56 ledger,
issues, sources, this log, code and ALL necessary metadata are completed
and frozen together before any NEW peer A9 findings or metadata.
''')
write('baseline-v1.json', dict(captured_at_utc=NOW, records=ordered, occurrences=len(occurrences), unique_paths=len(ordered), canonical_deduplicated_sha256=digest, no_recursive_historical_inventory=True))
write('metadata-v1.json', dict(status='ENTIRE initially blind OTHER WHOLE R1 complete; scoped PASS pending reconciliation', reviewer='/root', constructor='/root/review_2017_coarsening_r1', all_obligations=56, substantive_issues=0, repairs=0, advisories=0, root_supplied_new_A9_inference=False, NEW_peer_A9_findings_files_metadata_read_or_hashed=False, source_read_limits=P+'source-audit-v1.md', requested_model='gpt-6.1-sol', requested_reasoning='max', verified_effective_setting_readback=None, weekly_TOTAL_percent=8, weekly_reset=1792874445, mathematical_code_or_scan=False, promotion=False))
for item in ordered:
    assert rec(item['path']) == item, item['path']
ids = re.findall(r'^\|(\d\d)\|PASS\|', (ROOT / (P+'ledger-v1.md')).read_text(), re.M)
assert ids == [f'{i:02d}' for i in range(1,57)]
write('input-validation-v1.json', dict(validated_at_utc=NOW, declared_occurrences=len(occurrences), unique_paths=len(ordered), canonical_deduplicated_sha256=digest, exact_declared_input_bytes_match=True, all56_ledger_checks_present=True, hashes_not_mathematical_testing=True))
suffixes=['initial-v1.md','ledger-v1.md','issues-v1.md','source-audit-v1.md','worklog-v1.md','freeze-v1.py','baseline-v1.json','metadata-v1.json','input-validation-v1.json']
write('manifest-v1.json', dict(frozen_at_utc=NOW,status='ENTIRE OTHER initially blind WHOLE R1 complete; scoped PASS, reconciliation pending',reviewer='/root',constructor='/root/review_2017_coarsening_r1',target=rec(C+'candidate-v1.md'),constructor_freeze=rec(C+'freeze-v1.json'),all_obligations_reconstructed=56,substantive_issues=0,repairs_required=0,advisories=0,ENTIRE_before_ANY_NEW_peer_findings_or_files_or_metadata=True,input_summary=dict(occurrences=len(occurrences),unique_paths=len(ordered),sha256=digest),artifacts=[rec(P+s) for s in suffixes]))
print(json.dumps(dict(manifest=rec(P+'manifest-v1.json'),report=rec(P+'initial-v1.md'),all56=True,inputs=len(ordered)),indent=2))
