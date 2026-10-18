# OTHER initially blind WHOLE WO1--WO4 review R2

2026-10-18 UTC. Reviewer C, `/root/review_2017_coarsening_r1`.
Requested inherited `gpt-6.1-sol/max`; independent effective-setting
readback unavailable. This is an adversarial reconstruction of the
ENTIRE NEW root submission, ALL48 obligations and all11 frozen files.
It is not promotion and does not replace the second OTHER whole audit
or coordinator reconciliation.

**Initial verdict:** no substantive mathematical defect found in the
stated scopes. **48/48 obligations PASS**, zero required repairs and
zero advisory changes. Three interpretation notes below are CLOSED by
the candidate's existing explicit qualifications. In particular WO4
is conditional, and no actual low-cost mass bound has been proved.
No exact annual value or optimum over actual arrangements is certified.

## Independence, immutable target and old roles

The entire author freeze is
`notes/coordinator-weighted-optimum-r2-freeze-v1.json`,2906B,
SHA256 e8c60dd823a4e88c0b7d9cd5eb820f13c2791ca69b00317195c806faf51e30ec.
The main is14252B,
SHA256 ca09c36677badac6649775d2ade78a4f5af90fcbdafd0648a6bf8541e835e533.
All11 author files, all48 obligations, checks, failures, sources, log,
administrative code and ALL metadata were read in full. Constructor
code was NOT run. Its declared input fingerprints and the complete
current WC accepted input are independently checked by review-only
administrative code. The immediate OWN parent is C's ENTIRE2019CT
constructor freeze, a metadata link only and NOT a WO mathematical premise.

Root alone constructed NEW WO and is excluded. C did not construct
or contribute a new parameter, proof or optimization inference. C was
the older WC WHOLE R1 reviewer and has older2017 construction/review
roles (including annulus/profile/rank inputs), which are accepted-input
context, not a new independent recertification of those old proofs.
Only WC's current accepted exact scope is operative here. No NEW B WO
review file, ledger, source, log, code, hash, metadata or finding was
opened or computed before this ENTIRE initial checkpoint. Parent supplied
B's completion identity only; it supplied no mathematical verdict.

The assigned review prefix was confirmed unused. No old/shared/cache/Git
file was changed, no mathematical executable, optimizer, scan, CAS or
author certificate replay ran, and no subagent was spawned.

## 1. Official count and exact accepted geometry

The official2017 B4 and its own notes were freshly checked at B4 only:
integer n>=2, fixed regular2n-gon of side1, quadrilaterals of side1,
and log2 C(n)/n². The notes' intended count and marked-arrangement
dictionary agree with the complete accepted WC body. The fixed polygon
is not quotiented again by rotations or reflections. No n! factor,
reduced-word multiplicity or count of insertion histories enters.

I read the COMPLETE accepted WC1--WC3 body, current MD/JSON authority,
and both original WC source records. Their literal accepted-copy suffix
is checked administratively. The operative necessary geometry is

```
U=u+u',       T=k+k'<=U,
Z=m+m'-U<=3n/2.                                               (A)
```

All statistics concern one actual complete path and its rotated reverse.
The m statistic counts EVERY available middle exit, not only the exit
taken; cells with two exits have d=0 and are NONunique. Every path
has n steps, so u counts exactly its unique tail cells, and n-u its
nonunique tail cells. The reverse uses the same complete path set.

Fresh primary inspection confirms the relevant model and attributed
interfaces. Dallant's original v2 defines simple marked arrangements,
directed cutpaths and the six statistics; Section2 gives the rotation
and weakened zone comparison. Felsner--Valtr supplies fixed labels,
orientation, zonotopal correspondence and canonical insertion. Exact
read limits are in the source record. The older sharp-zone and complete
representation foundations remain attributed accepted inputs, not a
claim that this review independently reproved every source foundation.
No entropy-limit theorem, free-boundary variational identity, LP optimizer
or possible local-degree realization is needed by the new proof.

## 2. Reconstructing the exact family optimum

Write L=MV with L,M,V>1 and require, for every INTEGER d>=0,

```
2+d/V<=L M^d.                                                 (B)
```

The d=0 inequality forces L>=2. At d=1, multiplying by L and using
V=L/M gives `2L+M<=L²M`, equivalently

```
M>=f1(L)=2L/(L²-1).
```

At d=2 it gives `L²M²-2M-2L>=0`. Its positive root is

```
f2(L)=(1+sqrt(1+2L³))/L²,
```

and its other root is negative for L>=2. Thus EVERY feasible triple
has `M>=max(f1,f2)`; this is a necessary envelope, not an asserted
sufficient characterization of all feasible triples.

The polynomial P(L)=L⁴-2L³-1 has derivative2L²(2L-3)>0 on L>=2.
Its values P(2)=-1 and P(9/4)=473/256>0 put its unique >2 root ell
strictly between these numbers. Direct substitution in
F_L(M)=L²M²-2M-2L yields

```
F_L(f1)=-2L P(L)/(L²-1)².                                    (C)
```

Because F_L has one positive root and is negative between zero and
that root, f1>f2 on[2,ell), f1=f2 at ell, and f1<f2 for L>ell.
This direction is correct; reversing it would reverse the minimization.

The root bound ell<9/4<sqrt7 and ell<9/4<1+sqrt2 is exact:
81/16<7 and25/16<2. Thus `M*=2ell/(ell²-1)>1`; also M*<ell
because ell²-1>2. Hence `V*=ell/M*>1` and L=ell is in the
required OPEN parameter domain.

At these parameters the d1/d2 inequalities bind. If
`g_d=(2+d/V*)/(M*)^d`, then g1=g2=ell and

```
g_(d+1)/g_d=[1+1/(2V*+d)]/M*.
```

This ratio is strictly decreasing in the INTEGER d and equals1 at d1.
Consequently g_d<ell for EVERY d>=3, while g0=2<ell. Thus the
intersection is really feasible for ALL degrees, not just the first
two binding ones or a tested finite range.

For the objective K=L M^(3/4), the first branch's logarithmic derivative
is `(L²-7)/(4L(L²-1))`, strictly negative through ell. For the second
branch M=f2(L), implicit differentiation gives

```
M'=(1-LM²)/(L²M-1),
d(log(L M^(3/4)))/dL=(5L-2M)/(4LM(L²M-1)).                   (D)
```

Here L²M-1=sqrt(1+2L³)>0. Independently, F_L(L)=L⁴-4L>0 for
L>=2, whereas F_L(0)<0 and there is one positive root. Therefore
M<L, and the last derivative is positive on the ENTIRE unbounded
second branch. This remains true where f2<1: it is used there solely
as a necessary lower bound; actual feasible M>1 has not been dropped.

The necessary lower envelope decreases strictly to the feasible
intersection and increases strictly after it. Therefore its minimum
is K*=ell(M*)^(3/4). Every actual feasible objective is at least this
value; equality forces L=ell, then M=M*, then V=V*. This establishes
both existence and uniqueness without compactness of an open feasible
set or assuming the remainder of the envelope feasible. WO1 passes.

## 3. Strict comparison and exact upper transfer

I rederived the hand integer comparison rather than running a root
finder. At L0=527/250,

```
P(L0)=[27*527³-250⁴]/250⁴
      =45,555,941/3,906,250,000>0.
```

The integers527³=146,363,183, its product by27=3,951,805,941 and
250⁴=3,906,250,000 give exactly that gap. Thus L0>ell, and strict
increase of the necessary second envelope plus the old feasible triple
proves K*<L0(49/40)^(3/4). No new decimal approximation is required.

The old <0.648 hand certificate was also reconstructed from the accepted
body rather than rerun: its odd log truncations give
ln(L0/2)<527/10000 and ln(49/40)<203/1000, while ln2>842/1215.
The remaining strict comparison is
`4099/20000 <(37/125)*(842/1215)` with positive integer gap544375.
Thus half-log2 K* is strictly below the old exact half-log2 certificate,
and that certificate is strictly below81/125. No numerical optimizer,
decimal logarithm or old executable supplies any inference.

For the NEW optimal parameters, give each original unique exit weight1,
each extreme exit weight1/(ell M*^d), and each middle exit an additional
factor1/V*. The outgoing row sum is sigma_d<=1. Unfold the finite DAG
into its finite tree of prefixes. At each prefix, child weight sum is
at most the prefix weight. Hence sum W<=1, retaining reconvergent paths
as separate leaves. The reversed graph gives sum W'<=1 indexed by the
SAME paths. The exact products are

```
W=ell^(-(n-u)) M*^(-m) V*^(-k),
W'=ell^(-(n-u')) M*^(-m') V*^(-k').
```

Using ell=M*V* and(A),

```
sqrt(WW')=ell^-n M*^(-Z/2) V*^((U-T)/2)>=K*^-n.              (E)
```

Both inequality directions are correct because M*,V*>1. In particular
negative Z makes the lower bound easier, not false. Same-path Cauchy
bounds sum sqrt(WW') by1, giving the actual path upper bound K*^n.
This is the needed lower bound per term followed by upper bound on
their sum; it is not multiplication of two path-count upper estimates.

Canonical deletion gives B_(n+1)<=gamma_n B_n. Since B2=1,
log2 B_n<=[n(n-1)/2-1]log2 K*, including the empty sum at n2.
The accepted fixed-polygon dictionary transfers it to the official
limsup with the factor1/2. Any fixed larger starting index changes only
lower-order terms. No entropy existence or matching lower bound is a
new premise. This proves precisely the asserted WO2 upper improvement.

## 4. Loss normalization, the weighted count and its quantifiers

All sigma_d are positive. Sigma1=sigma2=1, sigma0<1, and the monotone
ratio above makes sigma_d<=sigma3<1 for EVERY d>=3. Thus
`rho=max(sigma0,sigma3)` is a fixed number strictly between0 and1.
The candidate correctly excludes unique rows from b, and counts visits
to nonunique d0 or d>=3 rows in BOTH path orientations; hence0<=b<=2n.
The same original cell is allowed to contribute once in each orientation.

Divide each nonunique cell's fixed outgoing weights by that cell's
positive sigma_d. This is a local fixed graph assignment, independent
of which complete path will later be followed. Let S be the product
of these row sums along a path, unique rows contributing1. Normalized
path weight is EXACTLY W/S, not an approximate pathwise probability.
The prefix-tree proof gives sum W/S<=1, even with unreachable cells,
reconvergent prefixes, a terminal sink or lost mass. Likewise for W'/S'.

Same-path Cauchy therefore gives

```
sum_p sqrt(WW'/(SS'))<=1.
```

Every costly row contributes sigma<=rho and every other row contributes1,
so `SS'<=rho^b`. Inverting positive products and combining with(E)
gives termwise lower bound `K*^-n rho^(-b/2)`. Hence

```
sum_p rho^(-b(p)/2)<=K*^n.                                    (F)
```

For ANY real h>=0, restricting(F) to b>=h gives the asserted absolute
tail count `K*^n rho^(h/2)`; h0, noninteger h and h>2n cause no
exception. It is NOT a tail probability under the uniform actual path
law: the number of all paths can be far below K*^n. An all-path positive
cost density yields the stated bound IF that extra density holds.
No such density or main-mass assertion is hidden in WO3.

## 5. Conditional low-cost improvement

Assume LC exactly as stated, uniformly over all actual n-arrangements
for all sufficiently large n, with eta>0 and0<J<K*. Split the SAME
actual path set at b<eta n and b>=eta n. Its sizes are bounded by
J^n and[K* rho^(eta/2)]^n respectively. Both bases are<K*, so their
sum is at most2K_new^n with K_new<K*. This is a valid conditional
statement even if some choices of LC parameters would make LC
impossible; no existence of such parameters is asserted.

The factor2 contributes at most one bit per insertion. Summing over
all sufficiently large insertion sizes therefore adds O(n), not O(n²),
whereas summing the j log2 K_new terms contributes n²/2+O(n).
A finite initial B_N has no leading contribution. This proves WO4
as an explicitly CONDITIONAL implication. Its missing premise is a
bound on ACTUAL low-cost output paths, not local formal degrees or
random independent visits.

## 6. Closed interpretation notes and verdict boundaries

**N1 (closed):** unique optimum means unique within the precise
exponential-toll family(B). It supplies no lower bound on actual path
counts or official entropy and no arrangement attaining equality.
The candidate states these limits in its significance and Sections4/7.

**N2 (closed):** (F) and its tail are absolute counts relative to the
certificate base. They do not give uniform path probabilities, positive
cost density or LC. The candidate makes all three distinctions explicitly.

**N3 (closed):** actual simple marked geometry, rotation and weakened
zone interface are published/accepted inputs with bounded source reads.
The exact optimization and normalization are reconstructed here, while
the older sharp-zone original and full equivalence foundations are not
misrepresented as freshly fully proved. No fresh source gap is required
to make the new extension conditional on anything beyond accepted WC.

No substantive issue, required repair or advisory wording change remains
in this independent initial. The precise claims WO1, WO2, WO3 and
CONDITIONAL WO4 pass. All historical bytes and the entire first report
remain immutable. Root must read both full OTHER packets before any
promotion; this initial alone certifies neither annual completion nor
external validation, priority or the actual low-cost geometric bridge.
