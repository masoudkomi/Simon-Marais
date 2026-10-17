# Whole initially blind OP1–OP3 review R2

2026-10-17 UTC. Reviewer `/root/review_2022_complexity_r2`.
Requested `gpt-6.1-sol`/`max`; verified effective-setting readback is
unavailable. This COMPLETE initial report, its full inference ledger and
source/preservation records are frozen before any new OP peer report,
ledger or coordinator finding is read. Only the coordinator can promote
the candidate after both independent whole audits are reconciled.

I find no substantive defect in OP1, OP2a/b/c, the Q-dependent refinement,
OP3a/b/c or the stated auxiliary per-class obstruction. The new code
recovers the missing port ends from adjacency and retains the internal
class to fix all port orders. Its global weak-composition count has half
as many contact ends as the older code. The resulting fixed-D error has
the claimed halved leading logarithmic coefficient. It supplies neither
an effective side-length rate nor the unknown numerical entropy value.

## Submission, independence and accepted-premise boundary

The complete target is `notes/global-value-return-r2-candidate-v1.md`,
22228bytes,SHA256
`49045e601d8934cbeb282b78162a34652b3a50772df66987b3c21280936befdc`;
the eight-record manifest is `notes/global-value-return-r2-manifest-v1.json`,
3351bytes,SHA256
`05b38b4c3af797def7910863d731b72e6d747b1fd945a4167a6e994270d892e6`.
I read the complete main, all48 obligations, constructor checks/open
ledger, source checks/JSON and research/failed-route/operational log.
All new mathematical assertions are reconstructed below, not just OP3.

The new constructor is `/root/review_2017_coarsening_r1`. I did not
construct or contribute to OP1–OP3 or the auxiliary example. My older
roles include construction of the separately accepted all-D global
argument and whole R2 review of V1–V4; earlier local audits are also
part of my preserved history. These roles are disclosed. In this review
G is an exact independently accepted premise, not a new self-audit of my
own older work. Root's unused integer-grid/SFT suggestion is not an OP
premise. I read no NEW OP peer findings before completing this freeze.

All four exact accepted mathematical bodies DC,G,V,U were reread in full,
including their current headers and historical mathematical suffixes,
with their acceptance scopes. DC supplies the marked dictionary,
invariant complete port decoration, section and monotonicity. G supplies
the all-integer full balanced limits and the scalar limit at each fixed
direction count. V supplies the older internal-list/weighted-count
context, directly reconstructed here. U supplies only the separately
accepted strict bound L<324757/500000. No old numerical/cutpath certificate
is rerun or independently recertified by this new review. Transitive
local interfaces of G retain their existing accepted scopes.

## 1. Official count and projection identities

The official problem concerns every integer n>=2 and the orientation-
distinguished tilings of a fixed regular2n-gon. The official notes give
the commutation-class dictionary and, in particular, distinguish the
two hexagon tilings. There is no extra initial-label permutation, no
quotient by rotations/reflections and no count of individual reduced
words or insertion histories. C(1)=1 is an auxiliary block convention.

Partition the initially ordered labels into D consecutive nonempty
blocks of sizes m_i, with sum n. Erasing every equal-color adjacent
swap leaves the same color in every current position; all retained
position indices therefore remain legal. The retained word has exactly
the different-color inversion pairs and length K=sum_(i<j)m_i m_j.
Its final permutation reverses the blocks while preserving rank inside
each color, and its inversion length is K, proving reducedness. Each
projected track (i,r) crosses each track of a different color once and
none of its own color. These are projected rank identities, not the
original labels routed across erased contacts.

Allowed original commutations use disjoint instantaneous position
intervals and preserve the color decisions and complete DC decoration.
The projected class Q and each directed crossing list L_(i,r), named
by the other projected tracks, are invariant. The list has a_i=n-m_i
entries and canonical gaps j=0,...,a_i, including endpoint gaps. Metric
crossing times or a selected sweep are not data.

Restrict the ORIGINAL diagram to labels of color i by deleting all
other original labels. An internal crossing remains adjacent, every
internal pair crosses once and the final order is reversed, so this
is a reduced m_i-label reversal word A_i. Under an original commutation,
zero, one or two restricted events survive; two surviving events use
disjoint adjacent restricted pairs and commute. Thus A_i is itself an
invariant class, with its original initial label order fixed.

Fully smoothing A_i makes noncrossing rank tracks. At generator s_r
put + on rank r and - on rank r+1. A commutation exchanges disjoint
rank pairs, leaving all per-rank lists and counts x_r invariant. Hence

    sum_(r=1)^(m_i-1) x_r(A_i)=binom(m_i,2).

The lth + on r and lth - on r+1 are the same internal event. Their
ID(r,l) is canonical, and the FULL A_i lists include the interleaving
of contacts toward both neighbors. Deleting other colors does not
change current same-color rank, so these are exactly the erased-contact
lists along projected (i,r) after forgetting retained vertices. Replacing
A_i by only its counts would lose essential order information.

## 2. OP1 reconstructed with projected identities

Fix an actual erased event between current neighboring ranks r,r+1
in color i. Its two labels are adjacent in the FULL current list.
Omitting all preceding equal-color events preserves every current
color position, so the projected tracks at those two positions are
precisely (i,r),(i,r+1), also adjacent in the full projected list.

Let t be any other-color PROJECTED track. Initially t lies on the same
side of both compared tracks because color i was one consecutive
initial block. At the contact time t again lies on the same side of
both because they are adjacent. Each pair crosses at most once in the
reduced projected word, so crossing before this instant is equivalent
to reversal of its initial relative side. The two indicators therefore
agree for this t. Applying this to every other-color t proves equality
of the full crossed-track SETS, not just their cardinalities.

The cardinality equals the count of preceding retained vertices on
the relevant track, namely its canonical gap index. Both contact ends
therefore have the SAME index. This conclusion is expressed in
canonical Q data, making the representative instant only a proof device.
It would not apply to arbitrary nonconsecutive colors, repeated pair
crossings or arbitrary local recolorings. Equality of prefix SETS
does not require the two directed crossing orders to be identical.

## 3. The complete one-sided code is injective on classes

For neighboring ranks define D_(i,r)(Q) as those j for which the two
length-j prefix SETS of their Q crossing lists agree, and b_(i,r) as
its cardinality. Every actual contact has its index in this set by
OP1. Both endpoints occur, but give one index when a_i=0; hence
1<=b<=a_i+1, and b>=2 only when a_i>0. Prefix agreement is necessary
only and is not a realization/gluing theorem.

Fix Q and the WHOLE A_i. On rank r<m_i there are x_r ordered +
contact IDs. Allocate them among the b allowed gaps in their given
order. Weak compositions count these allocations by

    binom(b+x_r-1,x_r)=F_(b-1)(x_r),
    F_c(x)=binom(c+x,x).

Repeated contacts in a gap and x_r=0 are included, with no contact
permutation. For every + ID put its - partner on rank r+1 at the
same gap index. Then use each FULL internal A_i per-rank list to order
all its contacts, including opposite signs in one gap. Actual records
have nondecreasing assigned indices along these lists. Invalid abstract
records are discarded and do not create an additional choice.

The entire DC decoration is now known: Q, every ordered port list in
each canonical gap, all neighbor signs and the forced kth-to-kth
pairing. Cross-routing restored contacts and keeping through-routing
at retained crossings recovers every ORIGINAL labeled strand and its
ordered crossing partners. These per-strand orders generate an event
poset. All representatives are linear extensions. Adjacent incomparable
events share no original label and, when consecutive in a valid word,
use disjoint position intervals, so exchanging them is an allowed
commutation and stays valid. Connectivity of linear extensions proves
that the original class is uniquely determined. No matching factorial,
hidden global event order or planar metric parameter remains.

All recorded parts are invariant under original commutations: Q and
its DC gap decoration, A_i, and the subset of + gap counts. Thus this
is an injection on classes, not a code of chosen words. It yields

    C(n)<=sum_Q product_i V_(m_i)(b_(i,1)(Q)-1,...),
    V_m(c_1,...,c_(m-1))=sum_A product_r F_(c_r)(x_r(A)).

Since b-1<=a_i and F_c(x) is nondecreasing in c, the upper OP2a bound
follows. The lower B<=C uses the actual DC section, prefixing fixed
internal reversals. No simultaneous realization of all abstract upper
records or arbitrary pairs (Q,A_i) is asserted.

The small four-label example is exact by hand. The projected word
23212 takes 1234 through1324,1342,1432,4132 to4312. A2 crosses B,C;
A1 crosses C,B. Their prefix sets agree only at0,2. Their single
internal contact can therefore occur only at those two indices.
Prefixing s1 or appending s3 gives length6 full reversals, respectively
at gap0 or gap2, and smoothing gives the same Q. DC distinguishes
these records. The refined upper bound is2 and both are realized,
so this one fiber has exactly2 classes, compared with uniform bound3.
This is a standalone finite hand proof, not an enumeration or evidence
that general common-prefix conditions are sufficient.

## 4. Closed finite bounds and all empty conventions

For u>=v+2 and a>=0, direct factorial cancellation gives

    F_a(u-1)F_a(v+1)/(F_a(u)F_a(v))
       =[u/(a+u)]*[(a+v+1)/(v+1)]>=1,

since the numerator difference after cross multiplication is
a(u-v-1)>=0. Denominators are positive, including a=0, where all
F_0=1. Balancing coordinates by this move preserves their total,
does not decrease the product and strictly decreases the sum of
squares. The m-1 coordinates have total m(m-1)/2 and mean m/2.
For m=2t the relaxed maximum has all entries t; for m=2t+1 it has
t entries t and t entries t+1. Realizability of the maximizing tuple
is not needed. Summing over C(m) classes gives OP2b with exactly

    J_(2t)=F_a(t)^(2t-1),
    J_(2t+1)=[F_a(t)F_a(t+1)]^t,
    J_1=1.

For OP2c, the total number of + ports is
S=sum_i binom(m_i,2). There are
E_+=sum_i(m_i-1)(n-m_i+1) named host gaps, only on tracks r<m_i.
For fixed Q,A_i, all actual arrays of gap counts sum to S. Dropping
their individual x_r constraints gives at most
binom(E_++S-1,S) arrays. Each actual array reconstructs the full
decoration by the preceding argument. Multiplication by product C(m_i)
and B gives OP2c. If S>0, some m_i>=2 and E_+>=1, so the binomial
has valid nonnegative arguments. If S=0, all m_i=1 and E_+=0, with
one empty record; H is separately1 rather than an undefined binomial.

D1 gives a=0,B(n)=1,V_n(0)=C(n), so the sharp weighted bound is
equality. All singleton blocks also give equality B=C with empty
products. For m2, x1=1 and V2(a)=a+1. Auxiliary n1 has one empty
block record, while empty blocks,D0,n0 are excluded. The weaker
J/global bounds are not required to be equalities at D1.

For old all-port degrees, k_r=x_(r-1)+x_r with x0=xm=0. On every
r<m, F_a(k_r)>=F_a(x_r), and the final rank factor is at least1.
Thus V_m(a)<=W_m(a), per class and after summing. At m2,a>0 it is
strictly a+1<(a+1)^2. No distribution of degree vectors is assumed.

## 5. OP3 normalization and limit order

Fix an integer D>=2 and take balanced nonempty m_i in{p,p+1},
p=floor(n/D), for all sufficiently large n. Coordinate monotonicity
gives B_D(p)<=B(m_1,...,m_D)<=B_D(p+1). The exact accepted ALL-integer
balanced limit, with (Dp/n)^2 and (D(p+1)/n)^2 tending to1, yields
n^-2 log B(m_i)->ell_D. The accepted scalar limit gives separately

    n^-2 sum_i log C(m_i)
      =sum_i(m_i/n)^2[log C(m_i)/m_i^2]->L/D.

For D2 this uses the unique full two-direction grid and k2=ell2=0;
no hidden D>=3 restriction survives in G. All m_i tend to infinity,
so the auxiliary finite C1 convention does not affect this limit.

Expanding the finite gap count gives exactly

    E_+=n^2-sum_i m_i^2+(2-D)n-D.

At this fixed D, therefore,

    S/n^2->1/(2D), E_+/n^2->1-1/D,
    (E_++S-1)/n^2->1-1/(2D),
    S/(E_++S-1)->1/(2D-1).

The binomial theorem at t=s/M gives
log binom(M,s)<=M h2(s/M), with endpoints by continuity. Apply it
to M=E_++S-1,s=S; the large balanced sizes are valid and finite
empty cases were defined separately. We obtain

    limsup n^-2 log H<=f_D,
    f_D=(1-1/(2D))h2(1/(2D-1)).

Taking limsups in the finite OP2c inequality and using the two limits
above yields L<=ell_D+L/D+f_D. The lower ell_D<=L is already supplied
by DC/G. Since D>1, rearrangement gives

    0<=L-ell_D<=f_D+L/D<=f_D+U/D,
    L<=D/(D-1)*(ell_D+f_D).

The numerical U substitution is a separate accepted theorem, not a
source abstract or a new certificate. The common-prefix refinement and
J-bound may improve finite estimates but were not assigned an unproved
asymptotic distribution.

Put p=1/D. Expanding binary entropy proves the exact identity

    f_D=h2(p)-h2(p/2)+p.

Strict concavity of h2 against the chord from0 to1/2 gives
h2(p/2)>p for0<p<1, in particular every D>=2. Thus
f_D<h2(1/D). Since h2(p)=p log2(1/p)+O(p), the identity gives

    f_D=(log2 D)/(2D)+O(1/D),
    D f_D/log2 D->1/2.

Adding L/D or U/D has no effect on that leading logarithmic coefficient.
All n limits were at one fixed D. There is no D=D(n) substitution,
uniform side threshold, modulus for ell_D or interchange of limits.

## 6. The auxiliary old-Jensen obstruction is an actual class

Let m=2t>=2, O=s1s3...s_(m-1), E=s2s4...s_(m-2). For one OE layer
the position permutation is the cycle
(1,3,...,m-1,m,m-2,...,2). Entries t places apart sum to m+1,
so (OE)^t reverses all original positions. Its length
t(t+t-1)=binom(m,2) is the inversion length, proving reducedness.
Each generator occurs exactly t times in this actual class A_*.

Thus its old smoothed port degrees are t at the two ends and m at
the m-2 interior ranks. Its old placement product and Jensen relaxation
are

    R=F_a(t)^2 F_a(m)^(m-2),
    J_old=F_a(m-1)^m.

The old discrete-concavity argument gives R<=J_old. Monotonicity then
gives

    1<=J_old/R<=[F_a(m)/F_a(t)]^2
                <=F_a(m)^2<=2^(2(a+m)).

This also covers m2,a0. At a=O(m), including a~(D-1)m for fixed D,
the logarithmic gap is O(m). A uniform improvement of the OLD per-class
bound by 2^(-delta m^2), delta>0, is therefore impossible on these
actual even classes. This makes no lower-exponent claim for the
weighted SUM relative to C(m)J_old: one class may have negligible
weighted mass. It is not an obstruction to other distributional
improvements or to the new one-sided removal of redundant ends.

## Verdict and retained open problems

The 52-check ledger covers all48 author obligations and additional
source/independence boundaries. I found no missing partner/order factor,
representative-dependent code, invalid empty binomial, asymptotic scaling
error or unsupported consequence in the submitted assertions. No author
repair is requested. This remains an initially blind reviewer finding,
not coordinator promotion or an absolute-certainty claim.

The common-prefix conditions need not be sufficient, their quadratic-
scale weighted distribution is unevaluated, and V3's E/R remain extra
hypotheses. Qualitative G and a computable D error do not imply an
effective finite-p rate or computability of L. The official numerical
value and any priority claim remain unresolved. No SFT/mixing/variational
theorem was applied.

Only new assigned review-prefix records were written. No mathematical
program, enumeration, CAS, certificate replay, constructor rerun, old
artifact/shared/Git edit, download, charge, contact, bypass or spawning
occurred. The existing constructor download interruption remains an
honestly recorded operational event, with no missing PDF/hash/PID
success inferred by this review. All prior own frozen packets are
preserved by the separate integrity record. Its hashes establish bytes,
not proof. Latest direct account-wide usage was44% TOTAL weekly at
2026-10-17 14:30:35UTC,reset1792745187, with the90% TOTAL ceiling and
integration reserve retained.
