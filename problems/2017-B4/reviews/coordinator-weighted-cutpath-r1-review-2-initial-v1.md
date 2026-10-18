# WC1–WC3 independent ENTIRE WHOLE initial review2

2026-10-18 UTC. Reviewer B, `/root/review_2022_complexity_r2`.
Requested inherited gpt-6.1-sol/max; independent effective readback
unavailable. Root is sole NEW constructor and excluded. B supplied no
NEW WC proof inference or repair. This ENTIRE initial is frozen without
ANY corresponding C NEW WC finding, report, ledger, source, code or
metadata/hash access. Only2017 B4 is investigated.

## Whole disposition and target

WC1–WC3 PASS in the stated domain and with the explicitly attributed
published combinatorial inputs. I found no substantive proof defect,
counterexample or required author repair. ALL40 obligations have separate
independent dispositions in the ledger. The complete graph-weight proof,
its local-integer certificate, every rational logarithm comparison and
the marked-count transfer reconstruct by hand. Five closed notes in
the issue record preserve the source and scope boundaries. This is not
coordinator acceptance, an external validation or a priority finding.

Exact main: `notes/coordinator-weighted-cutpath-r1-candidate-v1.md`,
12695B,SHA256f77d09e57a7462faaf6d48077c6815b9d33ffa722470596a947b9f46c4205928.
Exact ten-file constructor freeze: `notes/coordinator-weighted-cutpath-r1-freeze-v1.json`,
2672B,SHA2562ff11ebea88c684a2d86be972ae6f937ec5aec95040904eb27fc5c392ad7b4d4.
ALL ten files were read, including the complete administrative source,
sources/limits, failed routes,40 author dispositions and every JSON.
The author program was READ, never executed. An initially clipped combined
display of its source was reissued separately and read completely.

B's older2017 roles include global-recovery construction and various
independent local/global reviews. They do not independently recertify
those accepted inputs or this NEW weighted proof. No older global
recovery, entropy existence, periodic realization or effective-rate
theorem is a mathematical premise here. The accepted concavity upper
bound and authority were read fully as an old source/convention check;
its computational certificate was not opened as a new premise or rerun.
No C corresponding WC material was inventoried or accessed.

## 1. Actual official count and published geometric imports

The official target is n>=2, fixed regular2n-gon of unit sides,
unit-sided quadrilateral tilings, with log2 C(n)/n^2 lower/upper limits.
The official B4 notes identify the intended sequence, distinguish the
two hexagon tilings, and point to arrangements/commutation classes.
Felsner–Valtr Section1 fixes the marked arrangement convention, its
natural boundary labeling, and the fixed zonotopal-tiling representation.
No factorial labeling multiplier, rotation/reflection quotient or reduced
word count is introduced. The source equivalence is an ATTRIBUTED
dictionary, not a newly reconstructed foundation proof. In this convention
C(n)=B_n and B_2=1, as already checked in accepted project authority.

Fresh original Dallantv2 reading confirms: arrangements are simple,
one crossing per pair, marked north, opposite south, with orientation-
and north-preserving isomorphisms. Their original directed dual is a
finite DAG, and its complete north-to-south paths are cutpaths. Each
crosses every separating pseudoline once: its side sign changes only
on crossing that line and directed edges always change away from the
north side. Hence each complete path takes exactly n edges/exits.

At a nonterminal cell, degree1 gives one UNIQUE exit; degree>=2 gives
two EXTREME exits plus an INTEGER d>=0 middle exits. A degree2 cell
has d0 but is not unique. The statistics are actual graph statistics:
u counts unique exits TAKEN, k counts middle exits TAKEN, and m sums
ALL available middle exits of every visited nonterminal tail cell,
including untaken ones. A terminal contributes no outgoing count.

The opposite description uses the SAME path in reverse, in the rotated
arrangement with old south now north. Published middle-to-bounded-unique
correspondence implies k<=u' and k'<=u, since u includes all unique exits.
It is not necessary or correct to identify k with ALL of u'. Thus

    T=k+k'<=U=u+u'.

Dallant's actual upper/lower-edge count on all visited cells is
4n+m+m'-u-u'. Its Lemma5, from the attributed sharp pseudoline zone
theorem, yields the weakened consequence

    m+m'-U<=3n/2,                                  (G)

for the n>=2 source convention. The n1 finite exception is not used.
This is an actual path constraint, not sufficiency of a six-variable
polytope. The original older sharp zone proof is not freshly certified;
the explicit published Dallant theorem/interface is imported. The
original Pinchasi manuscript open failed and its body remains unread.

Finally Felsner–Valtr's canonical deletion of the boundary-labeled new
pseudoline gives B_(n+1)<=gamma_n B_n; their actual insertion paragraph
and Dallant's same recurrence were freshly read. These geometric
inputs are published methods, not part of a new novelty claim.

## 2. Reconstructing the substochastic bound on the ORIGINAL graph

Assume L,M,V>1,L=MV, and2+d/V<=LM^d for every integer d>=0.
Give a unique edge weight1. At a cell with d middle exits give each
of its two extremes weight1/(LM^d), and every middle weight
1/(LM^d V). The outgoing sum is(2+d/V)/(LM^d)<=1, including d0.
These are weights on the original graph, depending only on the current
tail and exit type. No pruned encoding tree or eventual path-class
conditioning is involved.

Here is an independent finite-DAG verification of the mass bound.
For each vertex v let F(v) be the total product weight of complete
suffix paths to south. Put F(south)=1 and put0 at any other terminal.
In reverse topological order, F(v)=sum_(v,w)w(v,w)F(w)<=1 whenever
all successor F(w)<=1. Thus F(north)<=1. Reconvergent prefixes are
still distinct paths in this finite sum; no identification of prefixes
is used. This is equivalent to the author's full prefix-tree argument,
not a missing extra combinatorial premise.

For a complete path p the number of nonunique tail cells is n-u.
Each pays one L denominator, all its d values sum to m, and a
selected middle pays the extra V denominator. Therefore

    W(p)=L^(-(n-u)) M^(-m) V^(-k),
    sum_p W(p)<=1.                                (F)

Repeat the identical construction on the reverse description. It is
another actual original directed dual. Reversal is a bijection of
complete paths, so its mass bound can be indexed on precisely the
same set p:

    W'(p)=L^(-(n-u')) M^(-m') V^(-k'),
    sum_p W'(p)<=1.

Reverse tail cells include the old sink and exclude the old source;
the published primed statistics already make that shift. Both path
lengths are n, so no n+1 exponent is lost. Opposite marking here
does not count a second arrangement in B_n. No independence of the
two measures, symmetry of individual statistics, or equality of their
outgoing sums is assumed. Cauchy–Schwarz on this common finite set gives

    sum_p sqrt(W(p)W'(p))<=1.                      (C)

Set U=u+u',T=k+k'. Since V>1 and T<=U,

 sqrt(WW')=L^(-n+U/2) M^(-(m+m')/2) V^(-T/2)
          >=L^(-n)(L/V)^(U/2)M^(-(m+m')/2)
           =L^(-n)M^(-(m+m'-U)/2)
          >=L^(-n)M^(-3n/4)=K^(-n),              (P)

where K=LM^(3/4) and the final comparison uses M>1 and(G).
Both inequality directions are correct, even if m+m'-U<0. Sum the
LOWER bound(P) over all paths and combine with the UPPER bound(C):
number of paths<=K^n. This is WC1. There is no six-tuple class count,
polynomial prefactor, invalid product of upper estimates, entropy
relaxation sufficiency or arbitrary-graph realization claim.

## 3. All INTEGER local degrees and exact constants

For L=527/250,M=49/40, V=L/M=2108/1225, we have L>M>1,V>1.
At d0, L-2=27/250>0. At d1 the exact quantities are

    LM=25823/10000, 2+1/V=5441/2108,
    25823*2108-5441*10000=24884>0.

At d2 they are

    LM^2=1265327/400000, 2+2/V=3333/1054,
    1265327*1054-3333*400000=454658>0.

For g_d=(2+d/V)/M^d, direct division gives
g_(d+1)/g_d=(2V+d+1)/[M(2V+d)]. The pre-M ratio is
1+1/(2V+d), strictly decreasing. At d2 it is7891/6666,
and49*6666-40*7891=10994>0 proves M exceeds it. Thus g_d
strictly decreases for every integer d>=2; g_2<L proves all such
degrees. Along with d0/1 this verifies the full unbounded local
condition. No finite degree cap, numerical optimization or real-d
claim is involved. Actual local degrees are integers, precisely the
property the new proof exploits beyond the old relaxation.

## 4. Strict logarithm certificate reconstructed by hand

Integrate the finite identity for1/(1+t): truncations after t^2 or
t^4 in the integrand leave negative remainders. Thus for0<t<1,

 ln(1+t)<t-t^2/2+t^3/3,
 ln(1+t)<t-t^2/2+t^3/3-t^4/4+t^5/5.

At t=27/500 the first polynomial is19722933/375000000, strictly
less than527/10000 by cross-product difference39567. At t=9/40
the second is103914999/512000000, strictly less than203/1000
by difference21001. Both positive t values lie in the required
interval. Independently, integrating2/(1-s^2) to1/3 and retaining
three positive terms yields ln2>2/3+2/81+2/1215=842/1215.
All remainders are strictly signed, without a numerical logarithm.

Since L/2=527/500 and M=49/40,

 ln(L/2)+(3/4)ln M
    <527/10000+(3/4)(203/1000)=4099/20000
    <(37/125)(842/1215)<(37/125)ln2.

The middle strict comparison has exact gap544375 between the
cross products31154*20000 and4099*151875. All denominators
are positive. Divide by positive ln2 and restore the L/2 factor:
log2 K<1+37/125=162/125. This is WC2, proved entirely by the
displayed symbolic bounds and finite hand arithmetic. The final
strict gap is independent of n.

## 5. Correct marked transfer and upper exponent

For every j>=2, WC1 and the published insertion recurrence yield
B_(j+1)<=K^j B_j. Start B_2=1 and telescope:

 log2 B_n<=[sum_(j=2)^(n-1)j]log2K
          =[n(n-1)/2-1]log2K.

At n2 both sides are0; no zone theorem at n1 is needed. A fixed
larger source starting index would add only a constant. Use the exact
attributed C(n)=B_n dictionary, divide by n^2 and take limsup. This
gives

 limsup log2 C(n)/n^2
   <=(1/2)log2L+(3/8)log2M<81/125=0.648.

That is WC3, an upper bound only. No matching lower bound or exact
common value follows. Older qualitative equality or new effective
upper hypotheses R are not premises; this argument does not supply
a profile-sensitive two-sided rate or a uniform effective modulus.
The historical old bound is not numerically optimized or replayed.

## 6. Adversarial findings and read limitations

I challenged the original-versus-pruned graph, d0 classification,
available-versus-taken middle counts, reverse-marking path identity,
source/sink shift, reconvergent prefixes, possible mass loss, both
monotonic inequality signs, negative zone defect, all local degrees,
every rational numerator, strict logarithm direction, n2 initialization
and the marked dictionary. These challenges close with the arguments
above and the exact original source passages. No counterexample or
substantive missing inference was found; no reviewer repair is supplied.

The sharp older zone proof and full foundations of the arrangement-
tiling equivalence are ATTRIBUTED imports. Original Dallant's explicit
interface and Felsner–Valtr's operative definitions/rotation/insertion
passages were freshly checked. The original Pinchasi body could not
be opened and is not falsely claimed read. The unrelated high-symmetry
entropy paper is context only, not a free/fixed-boundary premise or
a source-wide theorem refutation. Priority is unresolved.

All ten constructor files, ALL40 obligations, exact old authority,
sources/read limits, code and compact metadata are covered in the
entire initial. Neither the author's nor a source's mathematical
program was run. No C corresponding WC file or finding was read or
hashed before the full freeze. Send completion identity ONLY until
BOTH entire initials are confirmed. Coordinator alone may promote
after reading and reconciling both complete independent packets.
