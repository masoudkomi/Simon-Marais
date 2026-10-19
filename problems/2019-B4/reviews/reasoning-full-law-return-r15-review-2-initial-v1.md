# FL15: independent whole review 2, initially blind

2026-10-18 UTC. Reviewer `/root`; NEW constructor
`/root/review_2017_coarsening_r1` is excluded. This is the ENTIRE initial
review of all 48 obligations and all four proposed assertions, not an
audit of one lemma. No corresponding NEW review-1 findings, files,
actual inventory, hashes or metadata have been accessed. Findings stay
sealed until both whole reviews have completed their full payload and
manifest MODEL readbacks and separate documentary verification, followed
by explicit coordinator release. No author repair has been supplied by
this reviewer. Historical accepted-input construction/review roles are
disclosed below and do not make root a NEW FL15 constructor.

**Initial disposition: no substantive defect found within FL15A--D.**
This is a proposed acceptance of a partial result only. The annual
question, the full-law bound at every positive density, exact growth,
renewal-regime selection and priority remain open. The second OTHER
whole review and coordinator reconciliation are still required. All
mathematical checks below are by hand; documentary code cannot certify
them.

## 1. Exact target and research significance

The six-file author packet is bound by its freeze manifest, 2055 bytes,
SHA256 `9d65c7cf66efa14925fc15ef081aec846157db3c853ea0744b09afd165e1cbfb`.
Its candidate is 33314 bytes, SHA256
`38a770fac7bdc044b672038353a8b2140899f1607f86a0bcc1cfb2f33c077ab8`.
I read the ENTIRE candidate, source record, documentary program,
baseline, metadata and manifest. I did not execute the author's program
or any historical mathematical/certificate/freezer program.

The official open part concerns distinct alternating-end output words.
A full-law upper count must therefore control all actual outputs and
use their own denominator. The proposed result supplies an exponential
tail near a sharp quadratic viable-area ceiling. This is relevant to
understanding synchronization and renewal obstructions, but the covered
density range is too high to decide the surviving critical-mean branch.
The edge-incidence and finite-entropy methods connect the question to
occupation measures and constrained walks. They are standard methods;
this review establishes neither novelty nor an imported random-walk law.

The objects are distinct: histories, actual chronological pairs, physical
words and legal seed marks. Let X=(u,v), a=|u|, b=|v|, N=a+b; R_N is
the distinct actual pair class and c_N its cardinality. V is the UNION
of vertices belonging to some complete legal history, not the number
of histories. Q is the number of height matches with sum 0 or 1,
including endpoints. A viable vertex necessarily satisfies that test,
so V<=Q. No sufficiency is used except in the explicitly constructed
alternating sharp witness.

## 2. Independent reconstruction of the finite geometry

For a tape of length l, let E(h) count undirected crossings of the edge
{h,h+1}, D(h)=E(h-1)+E(h), and e(h)=1_(h=0)+1_(h=terminal).
Counting the two incident steps of every interior time and the one
incident step at each endpoint gives 2L(h)=D(h)+e(h). Coincident
endpoints contribute twice at their common height. An empty tape has
D=0, e(0)=2 and L(0)=1, so the same identity holds. The masses are
sum E=l, sum D=2l and sum e=2.

Expanding Q bilinearly gives a quarter of four terms. The D_u/e_v
term is at most (2a)(2)/4=a; the e_u/D_v term is at most b; the
endpoint/endpoint term is at most 1. Thus the entire endpoint error is
at most N+1. An edge pair with lower heights h,k contributes through
the four sums r,r+1,r+1,r+2, r=h+k. The exact number in {0,1} is 3
for r=-1,0; 1 for r=-2,1; and zero otherwise. Therefore

    Q <= 3ab/4+N+1 <= 3N²/16+N+1.

Both inequalities apply to arbitrary binary tapes at the Q level, with
no reachability assumption. They cover N=0 and either empty tape.

For X_m=((01)^m,(01)^m), N=4m, first assigning all left letters then
all right letters is legal: each has even length and returns the source
to phase zero. The two height profiles visit 0 exactly m+1 times and
1 exactly m times, giving Q=3m²+4m+1. Both-odd coordinate vertices
fail the necessary height test. Every other vertex has a complete
legal witness: for two even coordinates use whole 01 loops before
and after the vertex; for one odd coordinate use all preceding loops,
then its next 0, then its available next 1 and the remaining loops.
That next 1 exists because the tape length is even and the coordinate
is odd. This also handles boundary coordinates. Consequently V=Q,
including m=0, and both upper bounds are attained along N=4m. The
leading constant 3/16 is sharp; no every-N equality is asserted.

## 3. Independent reconstruction of localization and the full count

For a,b>0 normalize the two edge-count vectors to p and q. These are
deterministic empirical vectors of one pair. Taking their product is
bilinear algebra, not an independence assumption about random actual
tapes. Define tau as product mass outside h+k in {-1,0}. The kernel
there loses at least 2, so Q<=ab(3-2tau)/4+N+1.

The complementary mass is sum_k q_k(p_(-k-1)+p_(-k)). A finite weighted
average cannot exceed every bracket, so some adjacent p-edge pair
carries mass >=1-tau. Swapping tapes supplies an adjacent q-edge pair
with the same lower bound. The choices coexist because they concern
the two fixed tapes separately. They need not themselves define an
actual replacement pair or an admissible contraction.

Fix 0<rho<1/2 and eta>3/16-rho/8, with Delta the positive difference.
For every integer N>=max(2,ceil(2/Delta)), (N+1)/N²<=2/N<=Delta.
The high-Q event therefore has

    Q-N-1 >= (3/16-rho/8)N² > 0.

This first excludes empty tapes. It also justifies the otherwise
dangerous denominator substitution:

    tau <= 3/2-2(Q-N-1)/(ab)
         <= 3/2-8(Q-N-1)/N² <= rho.

Both tapes thus admit fixed adjacent-edge intervals with, in total,
at most rho N outside steps. There is no extra factor 2: their separate
costs are rho a and rho b.

For a fixed split and two absolute intervals, specify all m outside
positions among the N tape slots and all their bits, costing
binom(N,m) and 2^m. Between these positions each tape has blocks on a
three-vertex path. From any fixed vertex, a pair of steps has at most
two words (from the center one chooses an endpoint and returns; from
an endpoint one goes to the center and chooses an endpoint). A final
single step costs at most two. Thus a length-l block has at most
2^ceil(l/2) words. A start outside the three vertices supplies zero,
not a new free height. Earlier bits determine every subsequent start.

There are at most m+2 nonempty inside blocks across the two tapes.
Their lengths sum to N-m; hence the sum of their ceiling exponents
is at most (N-m+m+2)/2=N/2+1. The fixed-description cost is therefore
at most 2^(N/2+1+m). This reasoning tolerates adjacent exceptions,
empty blocks, a split at an exception and overcounting descriptions.

Each chosen interval contains a used edge, since its inside fraction
is positive. Every used lower edge height lies in [-N,N-1]; the loose
interval-start range [-N-1,N+1] has 2N+3 labels and covers all choices
needed by localization. Pay (2N+3)² and N+1 splits. Every actual high-Q
pair lies in this raw-word superset, giving

    count <= 2(N+1)(2N+3)² 2^(N/2)
                      sum_(m<=floor(rho N)) binom(N,m)2^m.

For x=rho/(1-rho)<1 and m<=rho N, x^m>=x^(rho N). The binomial
theorem gives the unweighted tail <=x^(-rho N)(1+x)^N=exp(Nh(rho)).
Multiplying by 2^(rho N) bounds its weighted version. This proves the
claimed base g(rho)=sqrt(2) exp(h(rho)+rho log 2), with every descriptor
paid. No actual-output decoder, independence law or injective reduction
is needed: this is explicitly an upper superset. Divide only now by
the accepted all-N actual bound c_N>=lambda^N. V's tail is a subset
of Q's tail, so it inherits the same result.

## 4. Explicit exponential gap and mark forgetting

The elementary inequality -(1-rho)log(1-rho)<=rho follows from the
nonnegative derivative -log(1-rho) of rho+(1-rho)log(1-rho). At rho=1/32,
h(rho)+rho log2 <=(1+6log2)/32. Adding log(sqrt2) gives
log g <=(1+22log2)/32. Thus g<=g0=(e 2^22)^(1/32).
The factorial-series proof of e<3 is strict, and
3^15=(3^4)^3 3^3>2^18 2^4=2^22. Hence e2^22<3^16 and g0<sqrt3.
Also 3<49/16 proves sqrt3<7/4. The freshly read accepted lower enclosure
1.76522347<lambda supplies lambda>7/4 without a new certificate or a
preliminary-part proof. Therefore g0/lambda<1.

The density threshold is exactly 3/16-(1/32)/8=47/256. Eta must be
fixed and strictly greater than that value; equality is not covered by
this certificate. Its all-integer-N starting threshold is explicit and
finite. If eta exceeds the pointwise ceiling asymptotically, an empty
event causes no problem. No optimized threshold is asserted.

For the physical-word event, use EXISTENCE of some legal marked seed
with the property. Its cardinality is at most that of bad chronological
pairs, because forgetting a mark is a map onto the existential event.
The accepted fibre bound c_N<= (floor(N/2)+1)b_(N+1) then gives the
stated extra factor. One must apply min(1,...) to the resulting bound
if desired; multiplying the untruncated marked bound is safe. This
does not say every 1 is legal, all marks agree or consecutive ratios
have a limit.

## 5. ALL48 obligation dispositions

Each row was checked against the ENTIRE candidate and reconstruction
above. PASS means the stated, restricted obligation, not an annual
solution or independent verification of the author's private read acts.

| ID | Initial whole-review disposition |
|---|---|
| FL15-01 | PASS. Official seed/parity, distinct words and all integer lengths; only open (b). |
| FL15-02 | PASS. Histories witness reachability; pairs and forgotten marks are not interchanged. |
| FL15-03 | PASS. V is the union over complete histories, retaining the suffix condition. |
| FL15-04 | PASS. Both endpoint time vertices and height sign convention are retained. |
| FL15-05 | PASS. Source-prefix height 0/1 proves only V<=Q. |
| FL15-06 | PASS with literal reading qualification: author's complete-read declaration is preserved, not independently observed. Root fresh whole-read R7/AT plus each authority, AR/AU current authorities and CT erratum; historical whole AR/AU reads are not relabelled fresh here. CT is not a final-proof premise. |
| FL15-07 | PASS. Fresh whole R7 body and EACH acceptance MD/JSON support c_N>=lambda^N and the exact mark polynomial. |
| FL15-08 | PASS. Accepted (b) lower enclosure is >7/4>sqrt3; no old numerical certificate or preliminary proof replay. |
| FL15-09 | PASS. E counts BOTH crossing directions; one count per step. |
| FL15-10 | PASS. Both endpoint contributions remain, including coincident endpoints. |
| FL15-11 | PASS. Empty-tape e(0)=2 gives the correct unit local time; N=0 is included. |
| FL15-12 | PASS. All four bilinear terms occur with factor 1/4. |
| FL15-13 | PASS. Cross and endpoint errors are <=a,b,1 respectively. |
| FL15-14 | PASS. The four endpoint sums yield exactly the printed 3/1/0 kernel. |
| FL15-15 | PASS. Total edge mass is ab; ab<=N²/4 has the correct upper-bound direction. |
| FL15-16 | PASS. Sharp witness has an explicit legal phase-zero full schedule, even at m=0. |
| FL15-17 | PASS. The next 1 after one odd coordinate exists; all permitted vertices have full prefix/suffix witnesses. |
| FL15-18 | PASS. Visits m+1,m give 3m²+4m+1, saturating both bounds for N=4m. |
| FL15-19 | PASS. Normalize only nonempty tapes; empirical products introduce no stochastic law. |
| FL15-20 | PASS. Outside {-1,0} kernel is <=1, so the loss is at least 2 tau. |
| FL15-21 | PASS. Finite averaging supplies the u adjacent-edge interval. |
| FL15-22 | PASS. Symmetry supplies v independently; no phase-compatible replacement pair is asserted. |
| FL15-23 | PASS. Strict rho/eta/Delta domains ensure a positive localization threshold. |
| FL15-24 | PASS. The displayed all-N bound pays N+1 uniformly, including floor/ceiling endpoints. |
| FL15-25 | PASS. Positivity is established before nonempty normalization or division. |
| FL15-26 | PASS. The sign of Q-N-1 validates replacing ab by N²/4. |
| FL15-27 | PASS. Outside counts sum to rho(a+b), with no lost factor 2. |
| FL15-28 | PASS. Positive inside mass forces a used edge; 2N+3 absolute labels are a safe overcount. |
| FL15-29 | PASS. N+1 splits retain all pair coordinates; no seed mark is silently forgotten. |
| FL15-30 | PASS. Every exceptional slot is paid through binom(N,m). |
| FL15-31 | PASS. All exceptional bits cost 2^m and determine later block starts. |
| FL15-32 | PASS. The two-step/one-step three-vertex argument covers every fixed start and block length. |
| FL15-33 | PASS. At most m+2 nonempty inside blocks across two tapes, including degenerate placements. |
| FL15-34 | PASS. Summed ceiling exponents <=N/2+1; odd block lengths do not evade the cost. |
| FL15-35 | PASS. Descriptor multiplicity is harmless in an upper union; no injectivity claim. |
| FL15-36 | PASS. x^m inequality is correctly directed for 0<x<1 and covers floor(rho N). |
| FL15-37 | PASS. The 2^m weight is fully paid by 2^(rho N). |
| FL15-38 | PASS. The raw superset contains the ENTIRE actual high-Q event. |
| FL15-39 | PASS. Uniform DISTINCT pair probabilities use actual c_N, not histories or 2^N. |
| FL15-40 | PASS. High V is a subset of high Q; no converse enters. |
| FL15-41 | PASS. The entropy inequality gives the claimed exact g0 exponent. |
| FL15-42 | PASS. Integer-power and factorial-series comparisons prove the strict gap by hand. |
| FL15-43 | PASS. 47/256 is exact and its lower endpoint remains strict. |
| FL15-44 | PASS. Eta is fixed before the limit and N threshold; no uniform eta->0 inference. |
| FL15-45 | PASS. Physical event is existential over actual legal marks, with the correct polynomial loss. |
| FL15-46 | PASS. AR's rare subclass and AU's lower constructions lie outside any claimed universal small-density upper law. |
| FL15-47 | PASS. AT's existing mean<=1/6 is stronger than the weak new mean corollary; no regime selection is claimed. |
| FL15-48 | PASS. All six author files, code and metadata read; seven failures and literal source limits retained; TWO OTHER whole audits still required. |

## 6. Closed adversarial issue log

These are checks made in the initial whole audit, not post-peer repairs.
No issue remains open against FL15A--D as written.

1. **Viability versus height matches.** Potentially fatal if Q=V were
   used globally. Closed: only V<=Q is used; sufficiency is proved for
   the sharp witness and nowhere else. The inherited ruler-mountain
   counterexample is explicitly preserved.
2. **Endpoint loss, including empty tapes.** Closed by the exact
   2L=D+e identity with endpoint mass 2 and the a+b+1 bound.
3. **Sharpness could supply only prefixes.** Closed by explicit
   remaining-loop schedules in the one-odd-coordinate cases; even tape
   length guarantees the next 1. Both-odd vertices are prohibited.
4. **Wrong denominator direction in stability.** Closed because
   Q-N-1 is proved strictly positive BEFORE ab is replaced.
5. **Separate mass localizations might need gluing.** Closed: they
   describe fixed tapes for an upper count; no new actual pair is built.
6. **Exceptional locations or restarts might be free.** Closed: every
   location and bit is paid, starts are determined by earlier bits and
   both tapes' m+2 blocks are included. The bound survives empty blocks.
7. **Raw words mistaken for uniform actual paths.** Closed: raw words
   are only a superset; the actual accepted c_N lower bound enters only
   after the count. The argument has no probabilistic independence step.
8. **Physical marks might be treated intrinsically.** Closed: the event
   is existential, the fibre bound is used in the correct direction and
   no legal-mark equality or consecutive-ratio transfer is asserted.
9. **Near-ceiling tail overstated as critical-regime progress.** Closed:
   the author explicitly notes AT's stronger mean<=1/6 and the untouched
   eta<=47/256 range. All three renewal alternatives remain unselected.
10. **Literature or reading overstated.** Closed with the literal source
    boundary in this report and source JSON. Neither external source
    supplies a theorem premise. Root does not claim fresh whole AR/AU/CT,
    a full Asselah probability proof or a full context-free-language
    proof chain. The author's own read declaration is not independently
    observable from its fingerprint.

## 7. Failed approaches and source-hypothesis audit

All seven author failed routes remain failures, superseded routes or
open questions. I checked the unequal alternating countermechanism by
hand: ((01)^(2m),(01)^m) has N=6m and V=Q=6m²+6m+1 via the same
phase-correct schedules. With O=m+1, NO-O²=5m²+4m-1 is strictly
smaller. It cannot replace the edge-kernel bound. The intermediate CT
packing route is not invoked by the final proof; I neither execute nor
recertify its old quantitative marker construction here. Increasing
ranges, every-density localization and a full unambiguous grammar
remain unresolved; no raw-walk LDP fills their missing inference.

Fresh primary returned text read in this audit:

* Official 2019 Paper B: complete B4 setup lines 63--73 and open (b)
  81--87. No preliminary proof or other problem investigated.
* Asselah arXiv 0801.3918v1: definitions 19--75, Proposition 1.5
  STATEMENT 193--225 and complete operative Section 4 opening 774--875,
  including (4.1)--(4.5). A returned middle gap before this operative
  block is not claimed read. Source main LDPs concern independent walks
  in dimension >=5; Proposition 1.5 uses dimension >=3 and infinite
  horizon/capacity. None is a law for this actual one-dimensional
  finite language. Its full probability-proof chain was not read.
* Ceccherini--Silberstein, DOI 10.1090/S0002-9947-06-03958-4:
  definitions 51--85, Theorem 1.2 STATEMENT 94--95 and COMPLETE Section
  5 definitions/Proposition 5.1 supplied proof 515--556. That short
  proof refers back to Theorem 1.5; its full proof and the entire
  fourteen pages were not audited. Unweighted growth sensitivity needs
  unambiguity; the ambiguous version weights derivations. No full
  actual grammar or inherent-ambiguity conclusion is imported.

Fresh COMPLETE accepted R7 and AT bodies and EACH acceptance MD/JSON
were read. R7's renewal sum c_N R^N=sum_(j=0)^N u_j with u_0=1 gives
the all-N lower bound; no finite count certificate was run. AT's
operative V/Q and mean alternatives were read as the comparison
boundary. Fresh EACH current AR and AU authority MD/JSON plus CT's
complete presentation-erratum MD/JSON were read. Historical complete
AR/AU reads are disclosed as historical; no fresh complete AR/AU/CT
read or foundational re-audit is claimed. Root's old AT/R7 review and
older moment contribution are accepted-input roles, not NEW authorship.
No full third-party paper, binary retrieval hash or licence verification
is fabricated; this audit used returned public text, not a new download.

## 8. Documentary preservation and handoff

The new five-file reviewer packet consists of this ENTIRE initial,
literal sources, a NEW documentary-only program, baseline and manifest.
The baseline binds the exact six-file author target, necessary accepted
guards and root's immediate own CR11 whole1 packet. Old recursive
ancestry remains transitively bound, not recopied or replayed. Author
declared guard rows are checked read-only by their literal path/size/SHA;
no current mutable map is substituted for a dated snapshot.

Only this assigned NEW prefix is written. No mathematical program,
CAS, scan, optimizer, routine test, old author/source/freezer/certificate
replay, peer access, Git operation, cache change or shared-proof mutation
occurs in preparing this sealed review. Root retains independent
coordinator duties outside the sealed prefix; those do not inspect the
corresponding NEW peer. Requested worker settings and independent
backend confirmation are not conflated. Existing local logging of the
coordinator's effort is not relabelled as an independently confirmed
backend value.

Last direct account observation at 23:52:57 UTC was 73% TOTAL used,
reset 1792874445, ordinary use allowed. Only that authorized window up
to 90% TOTAL with integration/review reserve is used. Owned keepawake
remains active. Full final payload MODEL readbacks, then full manifest
MODEL readback and SEPARATE read-only verification precede any peer
access and the administrative handoff. After explicit BOTH release the
coordinator must read BOTH complete reports and reconcile ALL 96 rows
before promotion. This initial report is immutable after sealing.
