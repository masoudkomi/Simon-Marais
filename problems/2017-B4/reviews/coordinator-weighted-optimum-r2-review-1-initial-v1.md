# WO1–WO4: initially blind whole review 1

18 October 2026 UTC. Reviewer B, `/root/review_2022_complexity_r2`.
Requested inherited **gpt-6.1-sol/max**; independent effective-setting
readback is unavailable. This is an **initial independent review**, not
coordinator acceptance. The submitted proof remains **candidate proof -
unverified** until both OTHER whole audits and reconciliation finish.

## Whole finding and independence

I reconstructed the ENTIRE new WO1–WO4 argument and ALL48 constructor
obligations, rather than checking only its endpoints or old WC proof.
All48 pass within the stated scopes. I found **zero substantive defects,
zero required repairs and zero unresolved mathematical issues**. Six
closed scope notes in the issue record preserve the limits I challenged.
In particular WO4 remains conditional on its unproved uniform low-cost
hypothesis; the weighted moment does not establish that hypothesis.

Root alone constructed the NEW proof and is excluded. I supplied no new
construction inference before or after the author freeze. My preparation
was confined to the accepted WC input and primary source passages. I was
the older WC whole reviewer2, not its constructor. That historical role
and other old 2017 input roles are disclosed; accepted old authority is
not fresh self-certification or a substitute for this whole audit.

No corresponding NEW other-reviewer WO report, finding, ledger, source,
code, hash or metadata was read before this ENTIRE initial checkpoint.
Only the reserved new review1 prefix is written. No author repair, old
file, shared file, Git or cache mutation occurred. All mathematics here
is by hand; no degree/parameter scan, optimizer, CAS, routine test,
author/source algorithm or old mathematical/freezer replay was run.

The exact target is the complete eleven-file author packet, whose main
has14252 bytes, SHA256
`ca09c36677badac6649775d2ade78a4f5af90fcbdafd0648a6bf8541e835e533`,
and freeze has2906 bytes, SHA256
`e8c60dd823a4e88c0b7d9cd5eb820f13c2791ca69b00317195c806faf51e30ec`.
Every component was read in full, including obligations, hand checks,
failures, source/log records and all code/generated metadata. The
constructor code was read, not executed. My NEW code is metadata-only.

## Exact target and accepted interfaces

The official domain is integer n>=2 and tilings in the fixed regular
unit-side2n-gon, with log2 count divided by n². The intended orientation
convention is fixed by the official examples and marked arrangement
dictionary. There is no factorial line-label factor, rotation quotient,
unmarked-arrangement replacement or count of insertion histories.

The COMPLETE accepted WC body15914B/SHA256
`93c08b0a43426c972bd6a0042c7e496cb08a106873c931f0231901e9f425f14b`,
its complete current MD/JSON authority and old source MD/JSON were read.
Its original candidate is an exact accepted-copy suffix. Its102 declared
fingerprint occurrences/49 paths are bound compactly, without a
historical inventory replay. Its old rational feasible triple and exact
logarithm certificate are operative accepted inputs, not new numerics.

The geometry is explicitly attributed: actual simple MARKED arrangements,
the directed dual graph, n exits per complete path, the SAME path rotated
by180 degrees, T=k+k'<=U=u+u', and
Z=m+m'−u−u'<=3n/2. The m counts include ALL available middle exits at
visited nonterminal cells, including exits not taken. A unique exit is
separate from a nonunique cell with d0, which has TWO extreme exits.

Fresh Dallant source inspection confirms these definitions, the insertion
interface, rotation and zone comparison. Fresh Felsner–Valtr passages
give the marked labels, fixed zonotopal representation and canonical
deletion/insertion. The older sharp-zone original proof and complete
representation-equivalence foundations remain attributed, not freshly
reproved. My source record gives the actual fresh read ranges. None of
the new optimization or renormalization is imported from an unread
external theorem or from a source optimization program.

## WO1: necessary constraints, feasible intersection and global optimum

Substitute V=L/M into(F). At d0 the inequality is2<=L, so every
feasible point has L>=2. At d1 multiply by L>0 to get
2L+M<=L²M, exactly M>=f1(L)=2L/(L²−1). The denominator is positive
throughout the necessary L-domain. At d2 the exact condition is
L²M²−2M−2L>=0. Its roots are
(1±sqrt(1+2L³))/L². Only the plus root f2 is positive, so for M>0
the condition is exactly M>=f2(L). No positive branch was dropped.

For P(L)=L⁴−2L³−1, P'(L)=2L²(2L−3)>0 on[2,infinity).
P2=−1, while P(9/4)=473/256>0. The intermediate-value theorem
and strict monotonicity therefore give exactly one ell in(2,9/4).
Since81/16<7 and5/4<sqrt2, ell<sqrt7 and ell<1+sqrt2.

I expanded the substitution independently:

    (L²−1)² F_L(f1)
      =4L⁴−4L(L²−1)−2L(L²−1)²
      =−2L⁵+4L⁴+2L=−2L P(L).

The quadratic F_L has one negative and one positive root and leading
coefficient>0. Consequently f1>f2 before ell, equality at ell and
f1<f2 after ell. This sign argument does not presume that F_L is
increasing on the whole positive half-line.

M*=f1(ell)>1 follows from ell²−2ell−1<0. Also ell²−1>3>2,
so M*<ell and V*=ell/M*>1. Thus the proposed minimizer lies in
the actual OPEN M/V domain, not its closure. The d1 and d2 equalities
hold there simultaneously.

To verify every remaining integer degree, set
g_d=(2+d/V*)/(M*)^d. The exact ratio is

    g_(d+1)/g_d=[1+1/(2V*+d)]/M*.

It strictly decreases with d. Since g1=g2=ell, the ratio at d1
is1, all ratios at integers d>=2 are<1, and g_d<ell for every
d>=3. Separately g0=2<ell. This proves ALL infinitely many
constraints, with equality exactly at d1/d2. No real-degree
extension or finite cutoff is assumed.

For any feasible point, K=L M^(3/4) is at least the necessary envelope
L max(f1,f2)^(3/4). The proof need not assert that every envelope
point satisfies all higher-degree constraints. On[2,ell], direct
differentiation gives

    d ln[L f1^(3/4)]/dL=(L²−7)/[4L(L²−1)]<0.

The strict sign holds on the WHOLE closed interval, including L2.
On[ell,infinity), write M=f2(L). From F_L(M)=0,

    L²M−1=sqrt(1+2L³)>0,
    M'=(1−LM²)/(L²M−1).

I recombined the logarithmic derivative with a common positive
denominator. Its numerator before reduction is
(1/4)L²M²+(3/4)L−M; using L²M²=2L+2M gives

    d ln[L M^(3/4)]/dL
      =(5L−2M)/[4LM(L²M−1)].

F_L(L)=L⁴−4L>0 for every L>=2, while F_L(0)<0 and the positive
root is unique. Hence f2(L)<L, so that last derivative is strictly
positive on the ENTIRE unbounded interval. It remains a valid lower
envelope even where f2(L)<1; actual feasible M is still required>1.

These strict one-sided signs and the ALL-degree feasible intersection
prove existence and the unique GLOBAL minimum in the specified family.
Equality forces L=ell, then M=M* because the objective strictly
increases in M, and finally V=V*. No compactness of an open domain,
unexamined large-L endpoint or numerical optimization is needed.

For the old certificate L0=527/250, I checked by integer expansion
527³=146363183,27·527³=3951805941 and250⁴=3906250000. Their
difference45555941 is positive, so P(L0)>0 and L0>ell. Strictly
increasing right envelope then puts the OLD feasible objective strictly
above K*, even if its M did not equal f2(L0). The accepted old exact
logarithm inequality supplies the final strict0.648 bound. No decimal
approximation to ell, M*, K* or a numerical gap is a premise.

## WO2: two measures on actual paths

The weights are a fixed assignment on the ORIGINAL directed graph:
unique1, each extreme1/[ell(M*)^d], and each middle
1/[ell(M*)^d V*]. Their nonunique row sum is sigma_d<=1.
Unfolding the finite graph into its tree of directed prefixes counts
every path separately even when prefixes reconverge. Each node sends
at most its received mass, so sum W<=1. The rotated assignment gives
sum W'<=1 on the SAME complete path set. Independence is neither true
nor required; Cauchy–Schwarz gives sum sqrt(WW')<=1.

Exactly n−u nonterminal visits are nonunique, their d-values sum to m,
and k middle exits are actually taken. This gives the stated products.
Combining them and using ell=M*V* yields exactly

    sqrt(WW')=ell^(-n) (M*)^(-Z/2) (V*)^((U−T)/2).

Because U−T>=0 and V*>1 the last factor is>=1. Because Z<=3n/2
and M*>1 the middle factor is>=(M*)^(-3n/4). This direction is
unchanged when Z<0. Thus each summand is bounded BELOW by(K*)^(-n),
and Cauchy gives the asserted UPPER number of paths.

Canonical deletion/insertion gives B_(n+1)<=gamma_n B_n with B2=1.
The exact sum j=2,...,n−1 is n(n−1)/2−1, including the empty sum at
n2. Dividing by n² and the fixed-polygon dictionary gives half the
base2 path logarithm as claimed. It is a limsup upper bound; no
existence theorem for the limit or exact entropy value is imported.

## WO3: normalized rows, both orientations and the tail

Every sigma_d is positive. Unique rows have sum1; d1/d2 have sum1;
d0 has sigma0=2/ell<1; and all d>=3 have
sigma_d<=sigma3<1 by the same infinite decreasing-ratio argument.
Therefore rho=max(sigma0,sigma3) is a FIXED number strictly between
zero and one, independent of n, arrangement or path.

Dividing every outgoing weight of a nonunique cell by that cell's
sigma_d is another fixed graph assignment with row sum1. Its path
product is exactly W/S, not a change to the path set or a future-
dependent probability. The rotated assignment similarly gives W'/S'.
The prefix-tree argument still gives both sums<=1 in the presence of
mergers, unreachable cells or a terminal sink. Equality is unnecessary.

b(p) counts nonbinding nonunique visits in BOTH orientations of the
SAME path, not just the forward statistic. There are n tail visits
per orientation, so0<=b<=2n. A d0 cell has two exits and does
contribute; a unique exit does not. All binding/unique factors in S S'
are1 and each other factor is<=rho. Thus

    S S'<=rho^b,
    sqrt[WW'/(S S')] >= (K*)^(-n) rho^(-b/2).

Division reverses the relevant comparison exactly as needed because
all quantities are positive. Applying Cauchy to the two normalized
measures proves the unconditional weighted sum(W).

For any real h>=0, restricting to b>=h gives a contribution at least
rho^(-h/2) times that subfamily's cardinality. This proves(T).
h0 recovers the ordinary bound; nonintegral h needs no rounding;
h>2n gives an empty tail and a valid inequality. If EVERY path has
b>=eta n, the asserted entire-count corollary follows. That is an
extra condition, not something established by a local strict row.

The estimate is an ABSOLUTE count relative to(K*)^n. Dividing it
by the actual path count would require a lower bound on that count;
none is supplied. It is not a uniform-random-path probability or a
positive-cost density theorem. Formal lists of locally binding degrees
do not supply an actual arrangement or establish global tightness.

## WO4: exact conditional quantifiers and insertion loss

The hypothesis is one fixed eta>0, one0<J<K* and one sufficiently
large-size threshold valid for EVERY actual simple marked arrangement
at each later n. It does not permit an arrangement-dependent J, a
single subsequence or a formal graph relaxation. The main explicitly
does NOT prove this hypothesis.

Under it the disjoint split b<eta n/b>=eta n gives
gamma_n<=J^n+[K*rho^(eta/2)]^n<=2K_new^n.
Both terms defining K_new are positive and strictly below K*, since
eta>0 and0<rho<1. The inequality remains logically valid even for
parameters whose antecedent could be impossible; no implicit claim of
their realization is made. A fixed finite initial B_N and each factor2
contribute only O(n) to log B_n. The j-sum contributes
(n²/2+O(n))log K_new, yielding precisely half-log K_new in limsup.

There is no unproved step from WO3 to(LC). That actual geometric
low-cost count, broader weight families, and additional correlations
remain open directions. The family minimum is not a lower bound on
actual gamma_n or the annual value, and does not establish uniform R,
a matching lower estimate or a new decimal/numeric annual answer.

## Preservation and delivery boundary

The immediate own immutable parent is the complete2020 R13 constructor
freeze6630B/SHA256
`eba097f9c6bffc2549fef51ef74b99962b16affa86a7dcaf9679bab95ad8adbe`
and its ten payloads. It binds719 own paths transitively. It is
unrelated preservation ancestry, NOT a mathematical premise here.
Necessary accepted WC and author packet fingerprints are checked;
the author's unrelated root R17 ancestry is bound by its declared
metadata, not recursively replayed as a mathematical input.

All sources/read limits, all48 per-inference ledger rows, six closed
notes, worklog and NEW metadata-only code accompany this report.
Generated metadata is read in FULL, followed by a SEPARATE read-only
postverification before handoff. Initial handoff is IDENTITY ONLY until
root confirms both ENTIRE initially blind checkpoints. No peer findings
or promotion are inferred from hashes or this single report.

Latest direct clock/get_usage_limits same-awaited-batch measurement:
2026-10-18 11:41:34UTC,31%TOTAL weekly,10080minutes,
reset1792874445,ordinaryUsageAllowed=true, legacy/by-limit agree,
account label029a8928…1334ac3a. Only the human-authorized current
window through90%TOTAL with integration reserve is used; no automatic
later-reset spending. No stop condition has been reached.
