# The guarded low-degree construction has vanishing joint-low-cost entropy

2026-10-19 UTC. **Candidate proof - unverified.** Sole NEW constructor C, /root/review_2017_coarsening_r1, is excluded from the TWO OTHER initially blind ENTIRE whole audits required before coordinator promotion. Root supplied the generic research target only, no new inference. Requested inherited gpt-6.1-sol/max; independent effective backend readback unavailable.

This is a proposed joint-sector MASS statement for the ENTIRE accepted LF14 guarded construction, allowing ALL positive parameter splits. It is not another single-class witness. Small directional cost forces its first canonical fan block to be sublinear; a direct row code then makes its number of cores subquadratic in logarithm. Conversely the whole balanced positive-entropy LF14 family pays positive quadratic directional cost despite its linear old degree cost. This closes a specific failed route to simultaneous low-D/low-J mass. It does NOT bound the corresponding sector in ALL arrangements, give a new global numerical rate, evaluate the scalar, or solve official2017 B4. Publication overlap/priority are OPEN.

## 1. Exact actual objects and accepted inputs

Official C(N) counts tilings of a FIXED regular unit-sided 2N-gon, N>=2. Use the separately accepted marked simple-pseudoline dictionary, with its fixed north marking and canonical labels determined by the exterior south-to-north order. Actual marked commutation classes, not reduced words, arbitrary histories or symmetry quotients, are counted. The whole official2017 B4 is open; no preliminary or neighboring problem is researched.

I freshly read COMPLETE current accepted PR11, CI12, LF14 and JC15 bodies and EACH current authority MD/JSON. I constructed older PR11/CI12/LF14 and reviewed older JC15; this is use of separately accepted inputs, not a new independent self-certification of those older proofs. NEW R16 is my construction; root did not supply a new step.

Keep the SAME fixed PR11 constants v,z,xi,G and actual normalized forward/reverse probabilities P,Q. In particular 1<v<7/4 and z>1. If c_F,c_R count the two orientations' degree-four tails on one actual insertion path p, CI12 defines

    T(p)=ln(P(p)/Q(p))+(c_F(p)-c_R(p))*ln z.

On ONE largest-label canonical deletion chain define

    D_N=sum c_F+c_R,
    J_N=sum ln cosh(T(p_n)/2),
    S_N=sum |T(p_n)|,     n=2,...,N-1.

All summands of J_N are nonnegative. CI12 proves, for every actual class,

    S_N/2-(N-2)ln2 <= J_N <= S_N/2.                 (I1)

No equal-mass, stationarity, independence or uniform-path interpretation is imposed on P,Q.

For each a,b,c>=1, accepted LF14 gives a fixed marked injection

    iota_(a,b,c): PP(a,b,c) -> A_(a+b+c+2).           (I2)

Here PP denotes fixed-boundary three-bundle classes, equivalently plane partitions in an a by b by c box. Same-color completions are the SPECIFIED hereditary tangent fans and there are the SPECIFIED two guards. This is exactly that construction, not arbitrary local completions. Write F(a,b,c) for its image. The following accepted facts are indispensable:

* Its first a+1 canonical labels are the A fan, including Aguard. Deleting every larger label leaves exactly that marked tangent fan, independently of the active core.
* Every image class has D_N<=4(N-2), including every canonical prefix.
* The map is injective on CORE CLASSES, so |F(a,b,c)|=PP(a,b,c), not the number of wiring-word representatives.
* For N>=5, p=floor((N-2)/3), r=N-2-3p, the balanced family F(p,p,p+r) has logarithmic rate alpha=(1/2)log2(3)-2/3>0.

CI12's exact tangent-fan calculation, at size k>=2, gives

    S_fan(k)=((k-2)(k-1)/2)ln2+(k-2)ln v
       -sum_(n=2)^(k-1) ln(n-2+2v)+1_(k>=5)ln z.   (I3)

This uses its ACTUAL first extreme exit and subsequent unique forward exits, together with the actual reversed probabilities. It is not an externally assigned path statistic. LF14's A phase matches precisely this marked fan and deletion order.

JC15 is context: its one actual family has D quadratic and J/S subquadratic. It supplies no positive-entropy simultaneous-small-cost family and no uniform joint-cost theorem. No JC15 conclusion is needed in the new estimates.

## 2. Proposed complete statements

All logarithms not labelled log2 are natural. Put

    kappa=(ln2)/4,
    B_N=(kappa+ln2)*N+(N/2)*ln(N+2v),    N>=5.

Define the set of ACTUAL classes

    U_N = union_(a,b,c>=1, a+b+c=N-2) F(a,b,c).

Different parameter images may overlap; this is a SET union, never a disjointness assertion. For h>=0 define the integer

    A_N(h)=min(N-4, floor sqrt((h+B_N)/kappa)).

**JM16A (uniform joint cost on every parameter image).** Every tau in F(a,b,c), N=a+b+c+2, satisfies

    D_N(tau)<=4(N-2),
    J_N(tau)>=kappa*a^2-B_N.                           (A)

The lower bound is harmless when negative and includes a=1.

**JM16B (finite and asymptotic joint-low mass in the whole union).** For EVERY N>=5 and EVERY real h>=0,

    #{tau in U_N:J_N(tau)<=h}
       <=N^2 * 2^[ min(N*A_N(h), (N-2)^2/4) ].         (B)

Every tau in this union already has the displayed linear D bound. Thus (B) bounds an ACTUAL simultaneous low-D/low-J sector of the WHOLE union, not a separately selected one-cost witness.

For EVERY sequence h_N>=0 with h_N=o(N^2),

    log2 max(1,#{tau in U_N:J_N(tau)<=h_N})=o(N^2).     (C)

More quantitatively, for each fixed epsilon>=0,

    limsup_N N^-2 log2 max(1,#{tau in U_N:
                              J_N(tau)<=epsilon*N^2})
       <= min(1/4, 2 sqrt(epsilon/ln2)).                (D)

In particular the bound tends to zero with the directional-cost tolerance. No unknown C(N) denominator occurs in any statement.

**JM16C (the whole counted balanced family is outside small joint cost).** Uniformly over tau in F(p,p,p+r),

    liminf_N inf_tau J_N(tau)/N^2 >= ln2/36,
    D_N(tau)<=4(N-2),                                 (E)

while this family's quadratic count entropy is the accepted alpha. Equivalently, for EVERY fixed epsilon<ln2/36 the WHOLE balanced family has J_N>epsilon*N^2 at all sufficiently large N. No exclusion at the endpoint epsilon=ln2/36 is asserted. This is not a uniform-law claim on all A_N.

## 3. Proof of JM16A: keep the actual initial fan

Fix a,b,c and an image class tau. Its first a+1 labels are exactly the inherited A fan by (I2). Every parent/path in the initial part n=2,...,a of its ONE canonical chain is therefore the CI12 tangent-fan parent/path, with the SAME marking, same actual full cell boundaries, same normalized P,Q and asymmetric z tilt. Later labels do not remain as phantom boundary edges after canonical deletion. Consequently

    J_N(tau)>=J_fan(a+1).                              (1)

This is just omission of nonnegative later summands, not an assumed cancellation, gluing theorem or comparison under a changed deletion order.

Use (I1) at size k=a+1 and then (I3):

    J_fan(a+1)
      >=kappa*a*(a-1)+(a-1)(ln v)/2
          -(1/2)sum_(n=2)^a ln(n-2+2v)
          -(a-1)ln2+(1/2)1_(a>=4)ln z.                (2)

At a=1 every sum and extra factor is empty, so (2) equals zero. For all a>=1 the v and z terms are nonnegative. There are a-1 logarithms; each is at most ln(a+2v). Thus

    J_N(tau)>=kappa*a^2-kappa*a-(a-1)ln2
                                -((a-1)/2)ln(a+2v).   (3)

Since a<=N and ln(a+2v)<=ln(N+2v), the total subtracted error is at most B_N. This proves the J lower bound in (A). Its D bound is exactly the accepted LF14 uniform statement, not newly inferred from a local degree picture. Both are true on the SAME actual class. B_N=O(N ln(N+1)), hence B_N/N^2 tends to zero.

It would be invalid to multiply full sums over alternative deletion histories or to divide by symmetry factors here. The fixed LF14 labeling makes (1) a literal initial segment of the existing chain; there is precisely one such segment for each image class.

## 4. Proof of JM16B: an actual core count, not word multiplicity

A plane partition in the a by b by c box is an a by b array of heights in {0,...,c}, weakly decreasing along each row and column. Ignore the column conditions temporarily. A single row is a weakly decreasing sequence of b integers in {0,...,c}. It is uniquely determined by its multiplicities, b nonnegative total entries in c+1 value bins. The elementary stars-and-bars bijection gives

    #possible rows=binom(b+c,b).

For example one can place b identical marks and c separators in a binary string of length b+c, so the count is at most 2^(b+c). Choosing all a rows independently is an UPPER bound: the column conditions can only remove arrays. Therefore, for EVERY positive a,b,c,

    PP(a,b,c)<=binom(b+c,b)^a<=2^[a(b+c)].              (4)

No MacMahon product evaluation is required for (4). The accepted boxed-height/core correspondence and LF14's injectivity transfer this bound to the number of ACTUAL image classes. A reduced word cannot contribute another copy.

If J_N(tau)<=h, (A) implies a^2<=(h+B_N)/kappa, hence a<=A_N(h). For each a there are fewer than N possible positive b,c with b+c=N-a-2, and there are fewer than N possible a values. Images for different splits need not be disjoint. The elementary UNION upper bound, (4), and

    a(b+c)=a(N-a-2)<=N*A_N(h),
    a(N-a-2)<=((N-2)/2)^2

give precisely (B). The second inequality is completion of a square and holds at every allowed integer a. No formal degree profile or unproved count factor is introduced.

For h_N=o(N^2),

    A_N(h_N)/N
       <=sqrt[(h_N/N^2+B_N/N^2)/kappa] ->0.

Taking logarithms of (B), with max(1,count) to handle an empty sector, proves (C). Its leading right side is nonnegative, so the max does not change this implication.

For h=epsilon*N^2, the same bound gives

    limsup A_N(h)/N<=sqrt(epsilon/kappa)
                             =2sqrt(epsilon/ln2).

The other exponent in (B) has limit 1/4 after division by N^2, while 2log2 N/N^2 tends to zero. This proves (D), including epsilon=0. A vanishing tolerance h_N/N^2 and a fixed tolerance epsilon are kept separate; neither is claimed uniform in N without the displayed finite bound.

## 5. Proof of JM16C and its exact meaning

In the balanced LF14 construction a=p and N=3p+r+2 with r in {0,1,2}. Hence p/N tends to 1/3. Applying (A) to EVERY core gives

    inf_tau J_N(tau)/N^2
       >=kappa*(p/N)^2-B_N/N^2 ->kappa/9=ln2/36.

This proves the stated liminf, for ALL integers N>=5, not only a subsequence. It implies the strict-epsilon exclusion by the definition of liminf. LF14 already proves the whole family's exact cardinality PP(p,p,p+r), count entropy alpha>0, and D<=4(N-2). Thus the proposed conclusion concerns quadratically exponentially many ACTUAL classes with simultaneously small old degree cost and positive directional cost.

In particular the existing positive-entropy low-D family does not yield positive-entropy joint-low mass by simply reusing its cardinality. Allowing ALL parameter splits does not repair that route: (C) says that the genuinely low-J part of that union has zero quadratic count entropy. This does not say that the full official joint-low sector has zero entropy; U_N is only this explicitly guarded fixed-fan union.

There is no probability normalization by an unknown C(N). Even the exact entropy alpha is below the published full lower bounds. No matching global lower, improved global upper, upper-rate saturation, effective upper approximation, exact scalar value or annual conclusion follows.

## 6. Failed routes and precise remaining inference

Constructor issue log: no known mathematical defect in JM16A--C after these hand checks, which are not independent audits. The unproved global implication identified below is deliberately outside the claims, not silently marked resolved.

1. Combining LF14's low-D count with JC15's low-J witness by “gluing” is unjustified. Their markings, canonical parents and COMPLETE cell boundaries must survive each insertion. No independent-core gluing has been proved. The new argument instead examines the existing LF14 object and shows its actual initial fan already costs J.
2. Cancelling directional contributions across a later core would not lower J: J is a SUM of ln cosh of the individual insertion imbalances, all nonnegative. Only the components within one T(p_n) can cancel. The initial A insertions precede the core on the canonical chain and cannot be cancelled by it. This is the reason (1) is valid.
3. Choosing a=o(N) does make the initial-fan obstruction subquadratic, but the SAME construction then loses quadratic count entropy by (4). The proof counts all remaining b,c possibilities. It does not assume they are bounded, balanced or independently realizable outside LF14.
4. Replacing the fixed fan with arbitrary counted arrangements, relabeling a later color as the first without tracking the new chain, or attaching an extra recursive count destroys the exact accepted interface argument. None is used.
5. There is a precise one-parent test of that missing hereditary step. In CI12's n-line interval graph, n>=3, start at any interior singleton k in {2,...,n-1}. Grow its interval within [2,n-1] until it equals [2,n-1], add one endpoint1 or n, then take the last unique edge. The north exit is middle; exactly n-2 later rows have two extreme exits and one is unique. Hence P=2^[-(n-2)]/(n-2+2v), while the SAME parent's reverse probability is Q=2^[-(n-1)] on every path. Its actual c_F=1_(n4),c_R=0 and T=ln[2/(n-2+2v)]+1_(n4)ln z=O(ln n). This is a legitimate cutpath and therefore an actual child by the accepted fiber, with bounded degree flags and small imbalance for this ONE insertion. It is not the next canonical fan insertion, whose first exit is extreme. Repeating the argument would require the changed child to have the required parent structure; that has not been proved. This one-parent observation is not an all-scale low-joint-cost mass construction.
6. The PR11 pathwise raw-weight comparison retains additional nonnegative zone and unique/middle slack before its final scalar bound. Retaining that slack formally alone neither proves an actual uniform joint D/J lower bound nor estimates the missing full-model sector. No new result is asserted from this route.
7. Primary literature gives stacking methods for making a SINGLE parent have many cutpaths and separate bundle-completion methods for class lower bounds. Those interfaces do not control our canonical J on all prefixes. No source computation, optimizer, path-count certificate, average-zone conjecture or arbitrary decoration realization is imported.

The remaining global task is actual geometric/count control of classes OUTSIDE U_N with simultaneously low canonical D and J, or a different complete constructive family carrying such mass. This packet provides a rigorous restriction on one real route; it does not claim that this route exhausts arrangements or that no alternative mechanism can work.

## 7. ALL32 natural constructor obligations

These are hand constructor checks, NOT independent reviews. Every claim remains unverified pending TWO OTHER ENTIRE whole audits.

| ID | Constructor hand disposition |
|---|---|
| JM16-O01 | CHECKED. Whole official2017 fixed polygon and actual marked commutation classes; no neighboring/preliminary research. |
| JM16-O02 | CHECKED. FULL current JC15/PR11/CI12/LF14 bodies and EACH current MDJSON read; old author/reviewer roles disclosed. |
| JM16-O03 | CHECKED. Root supplied no NEW inference; C is sole constructor and excluded from both audits. |
| JM16-O04 | CHECKED. SAME fixed PR11 flows/constants, actual T including z tilt, and original D/J chain definitions retained. |
| JM16-O05 | CHECKED. LF14 first block is a+1 including Aguard, not a; all larger labels deleted before its fan parents. |
| JM16-O06 | CHECKED. Full marked fan class and canonical paths match CI12, not merely local cell degrees. |
| JM16-O07 | CHECKED. Later J summands are nonnegative; no cancellation across insertion times is used. |
| JM16-O08 | CHECKED. CI12 S_fan and J>=S/2-(k-2)ln2 yield equation(2) with a-1 insertions. |
| JM16-O09 | CHECKED. a1/k2 has empty sums and zero fan cost; no unsupported small-size asymptotic. |
| JM16-O10 | CHECKED. v>1 and z>1 permit dropping only positive terms in the lower bound. |
| JM16-O11 | CHECKED. Each log is <=ln(a+2v); exact finite lower bound(3) holds uniformly. |
| JM16-O12 | CHECKED. B_N dominates every subtracted error and is O(Nln(N+1)) independently of a,b,c/core. |
| JM16-O13 | CHECKED. LF14 D<=4(N-2) applies to SAME classes; no new unprotected-interface inference. |
| JM16-O14 | CHECKED. U_N is the SET union over all positive splits with a+b+c=N-2, N>=5. |
| JM16-O15 | CHECKED. A_N(h) is defined for all real h>=0, integer/clamped at N-4. |
| JM16-O16 | CHECKED. J<=h forces a<=A_N(h) by the positive kappa, without an inverse implication. |
| JM16-O17 | CHECKED. One monotone row has exactly binom(b+c,b) choices by explicit multiplicity/binary encoding. |
| JM16-O18 | CHECKED. Ignoring column constraints gives an UPPER bound; PP<=2^[a(b+c)]. |
| JM16-O19 | CHECKED. Boxed arrays correspond to core CLASSES and LF14 injection gives actual image counts; no word multiplicity. |
| JM16-O20 | CHECKED. Fewer than N² parameter choices and possible overlapping images handled by union upper bound only. |
| JM16-O21 | CHECKED. Both finite exponent bounds use a(N-a-2); completed square is valid at every integer split. |
| JM16-O22 | CHECKED. Finite bound(B) includes empty count and nonnegative exponent; max1 convention harmless. |
| JM16-O23 | CHECKED. h_N=o(N²) and B_N=o(N²) force A_N/N->0, proving the ENTIRE-union entropy conclusion. |
| JM16-O24 | CHECKED. Fixed epsilon bound(D) follows with both limits and epsilon0 included; no unstated uniform convergence. |
| JM16-O25 | CHECKED. Balanced p/N->1/3 covers all r0/1/2 and every N>=5. |
| JM16-O26 | CHECKED. Uniform bound across ALL balanced cores gives liminf>=ln2/36; only strict epsilon below it is excluded. |
| JM16-O27 | CHECKED. Positive balanced count entropy alpha is exactly attributed LF14, not a new numerical global estimate. |
| JM16-O28 | CHECKED. This is joint-sector count control within U_N; full-model sector, probabilities and unknown C(N) denominator remain unclaimed. |
| JM16-O29 | CHECKED. The one-parent interval path has n-2 binary rows, exact P/Q=2/(n-2+2v), the isolated n4 tilt, and no proved hereditary continuation; JC15/gluing/fan replacements do not close that gap. |
| JM16-O30 | CHECKED. Primary reads, computation/version/read limits and published overlap are explicit; no unread source theorem imported. |
| JM16-O31 | CHECKED. No mathematical program/CAS/scan/optimizer/test/old/source/author executable or certificate replay; documentary checks only. |
| JM16-O32 | CHECKED. Complete failures/issues/source/log/code/ALLmetadata, compact parent binding, final MODEL readbacks and SEPARATE verification precede handoff. |

## 8. Literal sources, worklog and checkpoint boundary

Fresh [official2017 PaperB](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-2_1.pdf) B4 lines48--57 was checked. The four accepted bodies and EACH current MDJSON were read completely in separate bounded outputs. One later combined source display clipped Dallant's introductory context; that clipped introductory text is NOT claimed read. All accepted-authority text was returned intact.

Fresh [Felsner--Valtr author copy](https://page.math.tu-berlin.de/~felsner/Paper/new-pla.pdf) reads covered marked definitions30--48, labels101--105, representation106--142, complete insertion statement148--164, and COMPLETE Section4 count/completion634--694. Their fixed three-bundle/boxed-tiling interface matches LF14; its recursive completion factor is NOT transferred to our cost-controlled construction. The new upper count(4) is independently proved, not a new MacMahon theorem or a new representation-foundation proof.

Fresh [Dallant v2](https://arxiv.org/pdf/2502.20909v2) reads included operative Section2 context119--450, complete Section3 construction697--746 and Section4 conjecture discussion747--775. Returned optimizer passages511--696 were read only as context and not executed or imported. The source distinguishes many cutpaths in one parent from class growth and leaves its average/minimum-zone improvements conjectural. Neither that numerical certificate nor those conjectures supply our new result. Original sharp-zone foundations, Knuth's book, MacMahon's original book, full-paper audits and literature nonoverlap are not newly certified.

Worklog: narrow assigned-prefix unused check; FULL four accepted proofs/EACH authorities; official and primary discovery/operative reads; joint-low witness attempts and failed marking/gluing analysis; exact initial-fan lower bound; row-count union bound and all tolerance/endpoints; balanced family conclusion; whole32 ledger and documentary-only compact checkpoint. The immediate OWN parent is the frozen ET12 whole1 manifest; its necessary guards are bound by summary rather than recursively expanded. ET12 findings were released only after root's explicit BOTH confirmation at02:18-era; no corresponding NEW ET12 peer files were needed. Root's unrelated R13 tensor extension and R26 exploration were NOT accessed.

All mathematics was by hand. No computation beyond documentary path/byte/SHA/JSON/label checks, no source/author/old helper replay, no child, native browser, stalled approval, cache/download/old/shared/Git mutation, paid access, contact or bypass occurred. Source binary hashes are null: public text was read without a binary download or redistribution. Publication priority is OPEN.

Direct account-wide meter at2026-10-19 02:20:32UTC was81% TOTAL, ordinary allowed,10080minutes, reset1792874445; legacy and limit-id agreed. Only that explicitly authorized window through90% TOTAL is used, with review/integration reserve and no automatic later-window spending. Root owns awake/shared budget. Final ALL4 payload MODEL readbacks, manifest MODEL readback, then a SEPARATE read-only documentary verification are required before handoff. This five-file packet stays candidate-unverified until TWO OTHER whole audits and coordinator reconciliation.
