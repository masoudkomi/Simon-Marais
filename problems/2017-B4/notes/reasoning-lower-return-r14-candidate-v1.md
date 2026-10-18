# A positive-entropy family with only linear canonical degree-four cost

2026-10-18 UTC. **Candidate proof - unverified.** Sole NEW constructor C,
`/root/review_2017_coarsening_r1`; requested inherited gpt-6.1-sol/max,
independent effective-setting readback unavailable. Root supplied only a
generic research target, no NEW inference. TWO OTHER initially blind
ENTIRE WHOLE audits and coordinator reconciliation are required; C is
excluded. Only official2017 B4 is investigated.

The new assertion concerns ACTUAL marked commutation classes, not a
formal degree profile or reduced-word multiplicity. It constructs
quadratically exponentially many classes on which R11's OLD degree-four
cost is only linear. R12 previously disproved uniform positive cost
density with one actual class per size; here the low-cost sector itself
has positive entropy. The numerical global lower bound below is weaker
than published bounds and is NOT claimed as an improved scalar estimate.
No claim controls R12's joint directional cost J, proves saturation of an
upper bound, evaluates the official scalar, gives effective upper R,
solves the annual problem or establishes publication priority.

## 0. Exact objects, imports and claims

Let A_N be the marked arrangement classes counted by official C(N), for
a FIXED regular unit-sided2N-gon, N>=2. Labels are fixed by the north
exterior convention. Rotations/reflections and sorting-word histories
are not divided in or multiplied in. The accepted marked-arrangement/
tiling dictionary and largest-label insertion fiber are used literally.

Use the COMPLETE current accepted R11 and R12 bodies and EACH current
acceptance MD/JSON. C constructed those older results; this is accepted
input, not independent self-recertification. In an n-line parent and
its canonical insertion cutpath p, write

    c(p)=#{forward tails with outdegree4}
          +#{forward heads with indegree4}.

The second term is the reverse degree-four-tail count. Source indegree0
and sink outdegree0 contribute nothing. On the ONE canonical deletion
chain n=2,...,N-1 put D_N=sum c(p_n), as in R11/R12. These actual costs
are well defined on classes. The new proof needs their definition and
R12's directly proved hereditary tangent-fan graph, not a hypothetical
uniform random flow, average-zone theorem or unknown counting limit.

For positive integers a,b,c let PP(a,b,c) denote the number of consistent
three-bundle partial classes with bundle sizes a,b,c and FIXED input
block order C,B,A/output order A,B,C, preserving member order within each
color: different colors cross once and same colors do not cross. The equivalent boxed
plane partitions/hexagon tilings and MacMahon product are classical;
the precise published statement in Felsner--Valtr Section4 is an
attributed counting input. No new claim of discovering that construction
or auditing MacMahon's original book proof is made.

Proposed claims:

**LF14A (actual guarded injection).** For every a,b,c>=1, there is a
well-defined injection of those PP(a,b,c) partial classes into actual
marked full arrangements on N=a+b+c+2 lines. Same-color completions are
fixed hereditary tangent fans, and two explicitly placed guards protect
EVERY C insertion after any larger C labels have been deleted.

**LF14B (uniform cost in this entire family).** Every image class has

    c(p_n)<=4 at EVERY canonical insertion n>=2,
    D_N<=4(N-2).                                         (B)

This assertion covers all choices of the three-bundle core and all
canonical prefixes, not just a typical filling or one chosen path.

**LF14C (positive entropy of the low-cost sector).** For every N>=5,
put p=floor((N-2)/3), r=N-2-3p in{0,1,2}. There is an image family F_N
with EXACT cardinality PP(p,p,p+r), satisfying(B), and

    lim_N log2|F_N|/N² = alpha,
    alpha=(1/2)log2(3)-2/3>0.                            (C)

Even without using the MacMahon evaluation, explicit independent binary
boxed-height choices give |F_N|>=2^[p(p-1)/2]. For every fixed delta>0,

    liminf_N N^-2 log2 #{tau in A_N:D_N(tau)<=delta*N²}
         >=alpha>0.                                    (C')

**LF14D (limited pressure consequence).** On this constructed family,
for EVERY fixed real t,

    lim_N N^-2 ln[sum_(tau in F_N) exp(t*D_N(tau))]
        =alpha*ln2.                                    (D)

A fixed degree-cost tilt changes its logarithm by at most O_t(N).
This refutes a subquadratic-entropy assertion for the ENTIRE low-D
sector. It does NOT prove that this sector approaches R11's upper rate,
that R12's J is small, or that no degree-based method can improve a
global upper estimate.

## 1. Elementary wiring cells and an exact interface lemma

Use x-monotone simple wiring diagrams: each wire is y=f_i(x), every pair
crosses once, no triple point, and all crossings lie in a bounded region.
Choose x=0 through no crossing. A point's above-set T consists of labels
whose wires lie above it. The north/south sets are empty/all labels.

For a fixed T, its possible x coordinates satisfy

    f_i(x)>f_j(x) for EVERY i in T,j outside T.

Each such inequality is a half-line, because that pair crosses once.
Their intersection is an interval, possibly empty. Over a feasible x,
the points with this sign set form the open vertical interval between
max outside f_j and min inside f_i. Continuous endpoints make the full
nonempty region connected. It is exactly ONE cell. This also handles
empty/all T, with an infinite endpoint.

On any fixed wire i, all other sign inequalities restrict its parameter
to an interval, again because each other wire crosses it once. Thus a
cell has at most ONE boundary edge with a given wire label. The directed
dual adds one label to T on a downward edge, and removes one on a
reverse edge. In particular a directed cutpath never revisits a cell.

Let rho be the order of wires at x0, from north to south. Precisely its
prefix sets occur on that vertical line, each in one cell. Therefore:

* a cell meets x0 iff its above-set is a rho-prefix;
* a cell containing a left point but no rho-prefix is wholly left;
* a cell containing a right point but no rho-prefix is wholly right.

These statements use actual cell connectedness; they do not merely
assert that two boundary words have compatible ranks.

Suppose on the right wires have k colors and no same-color crossings.
Their order within each color is fixed. A cell's intersection with a
color is a prefix of that fixed order, so there is at most one possible
added and one removed label per color. The one-edge-per-label result
then gives i,o<=k for a cell WHOLLY right. This alone says nothing about
a cell crossing the interface; those cells must be handled separately.

## 2. The fixed left fans and their boundary contributions

For each color take the hereditary tangent fan from accepted CI12D:
local line j is y=2^-j*x-2^-2j, with the north marking above all lines.
Put a wiring version of the fan into a left rectangle. Different colors
occupy disjoint horizontal bands throughout x<=0. Straight horizontal
tails outside the rectangle create no extra crossing. The published/
accepted wiring representation preserves its marked graph and labels.

For q local fan lines, its far-left order is q,...,1 and its interface
order is1,...,q. Its cells are empty and consecutive intervals of local
labels. From interval[u,v] the downward options add u-1 or v+1 when
present. Its indegree is at most2. A proper interface prefix[1,h],
1<=h<q, has outdegree1 (label h+1) and incoming labels among1,h.
These are literal edge-label sets, not just degree counts.

Adding local largest label q+1 follows

    empty,{q},{q-1,q},...,{1,...,q}.

Every proper nonempty intermediate set is a SUFFIX, not an interface
prefix. Thus in a global left slab the interior cells of this insertion
path remain wholly in that fan; they have i<=2,o<=2. Only its local
north/south cells can acquire exterior edges. q0/q1 have no proper
interior suffix and satisfy the same statement vacuously.

One additional interface observation will be used for two-color stages.
At a proper prefix of the current fan color, the left outgoing label is
h+1 and left incoming labels are among1,h. On the right, the current
color's possible outgoing/ingoing labels are h+1 and h. They are already
among those left labels. On the left, this proper nonempty prefix cell
lies between two wires of its own fan, inside that fan's horizontal band;
no other color supplies a left boundary edge there. With only ONE other
color on the right, gluing can add at
most one more incoming and outgoing label. Thus every such nonjunction
global cell has indegree/outdegree at most3. This union counts actual
labels; two edges with the same label cannot introduce an extra degree.
The assertion is not made for an arbitrary internal fan or for three
colors at an unprotected interface.

## 3. An explicit guarded full-reversal word

Let the global canonical blocks be

    A={1,...,a+1}, B={a+2,...,a+b+2}, C=the last c labels.

Use local labels A_1..A_(a+1),B_1..B_(b+1),C_1..C_c in increasing
canonical order. At far left, the total north-to-south order is the
decreasing global order. Resolve every same-color pair in its fixed left
tangent fan. At the interface the order is

    C_1..C_c | B_1..B_b B_(b+1) | A_1 A_2..A_(a+1).

Set Aguard=A_1 and Bguard=B_(b+1). All remaining crossings are on the
right, in four successive blocks of adjacent swaps:

1. Move Aguard UP across the whole B block, then the whole C block,
   ending at the top. Each encountered pair crosses once.
2. Move Bguard DOWN across all active A labels A_2..A_(a+1), ending
   at the bottom. It does not cross active B or C in this block.
3. In the remaining contiguous positions, place an arbitrary consistent
   partial wiring of the active blocks C,B_active,A_active, changing
   their block order to A_active,B_active,C. Their sizes are c,b,a.
   Same-color order stays fixed; each different-color pair crosses once.
4. Move Bguard UP across the C block only, stopping below active B
   and above C.

The resulting north-to-south order is

    A_1..A_(a+1) | B_1..B_(b+1) | C_1..C_c,

the reverse of the original global order. The crossing sets partition
ALL pairs: same-color fans; Aguard with B/C; Bguard with active A;
active-core pairs; and Bguard with C. No pair repeats. All swaps are
adjacent in their displayed blocks, so this is an ACTUAL simple wiring
arrangement, not an abstract ordering of nonadjacent pair events.

For a=b=c1, the pre-fan order5,4,3,2,1 becomes5,3,4,1,2 after the
two size2 fans. The guard moves give1,5,3,2,4, the two possible active
three-wire cores end1,2,3,5,4, and the last guard move ends1,2,3,4,5.
The ten distinct crossing pairs are12,34;14,13,15;24;35,25,23;45.
This hand endpoint check illustrates the prescribed word; it is not a
finite enumeration offered as proof of the general construction.

The concatenation is well defined on core commutation classes: changing
a core representative by commuting disjoint events changes the full
word by those same commutations. Conversely the full class determines
the crossing order on EACH labelled strand. Delete the guards and all
same-color crossing events from those orders. One recovers exactly the
original active core orders. Distinct core classes therefore cannot
coalesce. This proves the injection, with no word-multiplicity factor.
Canonical labels/marking are fixed throughout; the usual polygon
dictionary puts every image in A_N.

## 4. EVERY canonical insertion has at most four flags

Delete largest labels successively in the constructed full arrangement.
All A prefixes first appear, then B prefixes, then C prefixes. Left
fans restrict to exactly their hereditary local prefixes. No same-color
crossing remains on the right of ANY prefix.

### A phase

While only A labels are present the whole class is the accepted tangent
fan. Its nonnorth positive degrees are at most2. In particular every
insertion has at most four flags (in fact the old fan formula is sharper).

### B phase

Here A is full, C absent, and the new largest B crosses all old B in the
left fan, then all A on the right. Its proper left-fan suffix cells
miss the interface by Section2 and have both degrees<=2. On the right
the parent has only TWO noncrossing color orders. A wholly right cell
has both degrees<=2. An interface cell visited after the fan has old B
full and an A prefix. If that A prefix is proper nonempty, Section2's
edge-label union gives both degrees<=3. No other nonjunction interface
type can be visited, since old B is already full along this whole
right segment.

Only north, the full-old-B/empty-A junction and south remain exceptional.
They may coincide when old B is empty. Each is visited at most once.
North has indegree0 and south outdegree0, so each contributes at most
one flag; the intermediate junction contributes at most two. Thus c<=4.
This proof covers the last B being Bguard as well as every earlier B;
it does not require that guard to have existed in an earlier prefix.

### C phase

All A/B and both guards are now present. Every new C crosses its old C
fan before entering the right slab, so its proper left suffix cells
are again pure fan cells with degrees<=2. It crosses Aguard FIRST among
all right-slab wires that it crosses and Bguard LAST. Between those two crossings its
above-set contains Aguard but omits Bguard.

Any prefix of the interface order containing Aguard must contain ALL
B labels, including Bguard. Therefore EVERY intermediate right-slab
cell of this insertion is nonprefix and is wholly right. Both degrees
are at most3 by the three-color statement in Section1, for EVERY active
core. This reasoning is unchanged after any larger C labels are deleted.

Only north, the full-old-C/empty-A/B junction, and south can contribute
flags. The same1+2+1 bound gives c<=4. Old C0/C1, coincident source/
junction, and empty lists of proper suffix cells are all included.

Summing over exactly N-2 canonical insertions proves D_N<=4(N-2).
No alternative deletion schedule, extremal representative, random law
or uniform bound on ALL paths in an arbitrary arrangement is assumed.
The theorem controls precisely the canonical paths of EVERY class in
the constructed image family.

## 5. Exact family counts and its quadratic entropy

Felsner--Valtr's consistent three-bundle count is the classical product

    PP(a,b,c)=prod_(i=0)^(a-1) prod_(j=0)^(b-1)
                  prod_(k=0)^(c-1) (i+j+k+2)/(i+j+k+1).

Its hypotheses are exactly the active core's complete cross-color,
noncrossing same-color boundary pairing. The fixed fans/guard map is
injective, so its image has EXACTLY that many actual full classes.
The independent-disk completion and recursive amplification in the
literature are attributed precedents; no recursive entropy multiplier
is added to this fixed-fan family.

For N>=5 choose p,r as in LF14C. Then F_N has PP(p,p,p+r) classes and
satisfies(B), including p1 and every r0/1/2. Telescoping the k product
gives

    ln PP(p,p,p)=sum_(i,j=0)^(p-1) ln[(i+j+p+1)/(i+j+1)].

Let g_p(s)=ln[(s+p)/s]. On cells with i+j>=1 its variation across
[i,i+1]x[j,j+1] is at most2/(i+j), because |g'_p(s)|<=1/s.
There are at most i+j+1 cells on each such diagonal, hence the total
sum-versus-integral error is O(p). The one corner cell has a finite
logarithmic singularity and error O(ln(p+1)), also O(p). Consequently

    ln PP(p,p,p)=p² I+O(p),
    I=integral_0^1 integral_0^1 ln[(x+y+1)/(x+y)] dxdy.

For F(t)=(t²/2)ln t-3t²/4, F(0)=0, one has F''(t)=ln t. Direct
integration gives

    I=F(3)-3F(2)+3F(1)-F(0)=(9/2)ln3-6ln2.

Changing the third side from p to p+r, r<=2, changes the logarithm by

    sum_(i,j) ln[1+r/(i+j+p+1)]=O(p),

using ln(1+x)<=x. Since N=3p+O(1), this proves(C). Positivity follows
from3^9>2^12. Also alpha<1/6, since27<32 gives log2(3)<5/3. Thus
this sector lower bound is deliberately BELOW the published global
lower bound, and is not presented as an improved annual estimate.

There is also a self-contained weaker positive count. For indices
1<=i,j<=p with i+j<=p, independently select epsilon_(i,j) in{0,1}
and set h_(i,j)=p-i-j+epsilon_(i,j); put h0 outside that triangle.
Adjacent base heights drop by1, so arbitrary binary changes preserve
both weak row/column monotonicity; the boundary heights remain0/1 and
the maximum is at most p. These are2^[p(p-1)/2] different boxed plane
partitions. Their stepped surfaces, viewed in the(1,1,1) direction,
give different three-direction hexagon tilings with the prescribed
bundle boundary. Thus positive sector entropy does not rest solely
on evaluating the imported product. This weaker count is not substituted
for the stronger classical value in(C).

For fixed delta>0, eventually4(N-2)<=delta*N². F_N is then contained
in the stated low-D sector, proving(C'). It follows in particular that
an assertion that all such low-cost classes have only2^o(N²) members is
FALSE. The earlier one-class R12 example alone did not give this fact.

## 6. Exact pressure scope and the still open global inference

For every fixed real t, (B) implies

    e^[-4|t|(N-2)]|F_N| <= sum_F_N e^(tD_N)
                          <=e^[4|t|(N-2)]|F_N|.

Divide logarithms byN² and use(C), proving(D). In particular the fixed
R11 tilt(ln xi)/2 has no leading entropy payment on this actual family.
This says nothing about all classes' tilted pressure or an N-dependent
unbounded tilt, and does not show alpha is close to an upper rate.

R12's J/S costs were never estimated here. The protected core may have
directional flow imbalance, and its low OLD D does not imply low joint
cost. An upper argument can still seek a stronger low-D sector bound
ABOVE alpha or exploit J or other actual structure. The exact scalar
value, a better global numerical bound, effective upper approximation,
entropy saturation and the annual target remain OPEN.

Replacing the fixed tangent fans by arbitrary counted arrangements
would destroy the proved prefix-edge bounds. The historical recursive
factor B_p^3 cannot be attached to LF14C without a NEW uniform argument.
Similarly, without the two guards, a C path may visit many unprotected
interface-prefix cells whose incoming degree can be4. Those failed
inferences are preserved, not hidden by a local three-color statement.

The construction, sign-cell/interface proof, cost accounting, remainder
handling and elementary integral estimates are hand reasoning. No
mathematical program, CAS, scan, optimizer, routine test, source/author
executable or old certificate/freezer replay was used. Primary theorem
statements/proofs were read only in the literal operative scopes in the
source record. No root R13 tensor material was accessed or used. This
packet remains candidate-unverified until TWO OTHER ENTIRE WHOLE audits
and coordinator-only reconciliation.
