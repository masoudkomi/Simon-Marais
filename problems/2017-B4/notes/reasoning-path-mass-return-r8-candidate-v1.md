# Adjacent middle exits force enough weighted escape

2026-10-18 UTC. **Candidate proof - unverified.** C alone constructs
NEW PM8A--PM8E. Root supplied the general research target, with no new
proof inference. C is EXCLUDED from both required independent audits.
TWO OTHER initially blind ENTIRE WHOLE audits and complete coordinator
reconciliation must precede promotion. Requested inherited
gpt-6.1-sol/max; effective-setting readback independently unavailable.

## Significance and exact proposed result

The official2017 question concerns the quadratic logarithmic growth of
unit-rhombus tilings of the fixed regular2n-gon, n>=2. The accepted
marked-arrangement dictionary reduces an upper estimate to counting
directed cutpaths in actual simple pseudoline arrangements. The accepted
WO theorem optimizes one local weight family and penalizes certain
degrees; its further improvement remains conditional on bounding the
absolute number of low-penalty paths. This submission proposes such a
bound using a local diamond of the ACTUAL arrangement dual, followed by
an adapted finite weighted-flow argument. No arbitrary degree sequence
or unconstrained directed graph is substituted for an arrangement.

Let ell>2 be the unique root of ell^4-2ell^3-1=0 and set

    M=2ell/(ell^2-1), V=ell/M, K=ell M^(3/4),
    sigma_d=(2+d/V)/(ell M^d),
    rho=max(sigma_0,sigma_3), 0<rho<1.

These are exactly the accepted WO constants. The explicit new constants
below are independent of n and of the actual arrangement:

    L0=19/9, M0=171/140, V0=140/81=L0/M0,
    K0=L0 M0^(3/4), chi=61880/61731>1,
    delta=min(1, ln(K/K0)/ln chi),
    kappa=1/[4(V+1)^2], a=1-kappa/2,
    eta=(delta/8) log2(1/a),
    J0=K0 chi^(delta/2),
    J1=K a^(delta/16), J2=K rho^(eta/2),
    J=max(J0,J1,J2).

The proof below establishes 1<K0<K, delta>0, 0<a<1, eta>0 and
J<K, without evaluating a decimal or using a mathematical executable.

Proposed **PM8A**: at every outdegree4 cell of an actual marked wiring
dual, the normalized WO forward measure has probability at least kappa
of visiting a penalized vertex within its next two steps. A penalized
vertex has forward outdegree2 or>=5, or reverse outdegree2 or>=5,
with the terminal zero degree excluded in each orientation.

Proposed **PM8B**: greedily disjoint two-step trials at outdegree4
vertices satisfy an exact finite-flow exponential moment. It yields an
absolute count, at most J1^n in each orientation, for paths with many
outdegree4 visits in that orientation and fewer than eta*n penalties.
There is no independence or uniform-path-probability assumption.

Proposed **PM8C**: a separate explicit rational tilt gives an absolute
count at most J0^n for paths with at most delta*n outdegree4 visits
across both orientations. This tilt violates its raw d2 row inequality;
dividing exactly those rows by chi accounts for that violation.

Proposed **PM8D**: EVERY actual arrangement of EVERY integer n>=2 has

    #complete cutpaths <=J0^n+2 J1^n+J2^n <=4 J^n,       (1)

where J<K. In particular the accepted WO4 low-cost premise holds with
a fixed positive eta, a fixed base below K and a threshold uniform over
all actual arrangements at all later sizes.

Proposed **PM8E**: for the exact official fixed-polygon count C(N),

    limsup_(N->infinity) log2 C(N)/N^2
        <=(1/2)log2 J <(1/2)log2 K.                  (2)

This is a proposed strict improvement of the accepted algebraic upper
bound, with no asserted decimal improvement, exact value, matching
lower bound, effective all-scale upper R, annual solution or priority.
The separately accepted limit-existence theorem is not needed here.

## 1. Exact accepted inputs and counting model

I read the COMPLETE accepted WC and WO bodies, COMPLETE current MD/JSON
authorities, old operative source records and failed routes. The inputs
are reviewed-weighted-cutpath-r1-v1.1.md,15914B,SHA
93c08b0a43426c972bd6a0042c7e496cb08a106873c931f0231901e9f425f14b,
and reviewed-weighted-optimum-r2-v1.1.md,18824B,SHA
dcc12d2989e5ab657960498179e2585e62ad35ffb1989a4bca72fef8fb953f9a.
Their separately accepted marked dictionary, rotation/zone inequalities
and canonical insertion keep those exact scopes and source-read limits.
C was an OTHER reviewer of the older WC/WO, not their constructor;
this new construction cannot independently recertify its own claims.

Use an actual simple marked arrangement of n pseudolines, represented
as a wiring diagram: continuous x-monotone wires, every pair crossing
transversely exactly once, and no triple crossing. A harmless choice of
representation separates crossing abscissae. North and south are fixed.
The directed dual orients every edge from the north side of its wire to
the south side. A complete cutpath has exactly n steps. It is a path in
this ORIGINAL graph, not a commutation history or a pruned encoding.

For a cell v write o(v),i(v) for its forward outdegree and indegree.
If o=1 its exit is unique. If o=d+2>=2, the two ends of its linearly
ordered lower boundary are extreme exits and its d other exits are
middle exits. The rotated arrangement reverses all dual edges and uses
the upper boundary in place of the lower boundary. We always compare
the SAME complete paths in the two directions.

For a path p=(v_0,...,v_n), v_0=north and v_n=south, let u,u' count
unique exits, k,k' taken middle exits, and m,m' ALL available middles
at its tail vertices in the two respective orientations. The exact
accepted geometric input is

    T=k+k'<=U=u+u', Z=m+m'-U<=3n/2.                 (3)

For any L,Mbar,Vbar>1 with L=Mbar Vbar, assign RAW weights1 to unique
exits, 1/(L Mbar^d) to each extreme, and 1/(L Mbar^d Vbar) to each
middle at a nonunique cell. The outgoing row sum is

    tau_d=(2+d/Vbar)/(L Mbar^d).

No feasibility of these raw rows is required for the following
PATHWISE algebra. If W,W' are their two products, (3) gives

    sqrt(W W')
       =L^-n Mbar^(-Z/2) Vbar^((U-T)/2)
       >=[L Mbar^(3/4)]^-n.                       (4)

Both inequalities have the correct sign also when Z is negative.
We will separately ensure row sums<=1 before invoking finite flow.

At the WO constants, sigma_1=sigma_2=1 and all other nonunique rows
have sigma_d<=rho<1. Normalize each such row by its own sigma_d. Call
the resulting two complete-path weights P(p),Q(p). Unique rows have
weight1. Every nonterminal normalized row sums exactly1. In particular

    sum_p P(p)<=1, sum_p Q(p)<=1,
    sqrt(P(p)Q(p))>=K^-n rho^(-b(p)/2)>=K^-n,        (5)

where b(p) counts nonunique d0 and d>=3 visits in BOTH orientations.
The accepted WO3 also gives, for every real h>=0,

    #{p:b(p)>=h}<=K^n rho^(h/2).                  (6)

These are absolute counts and two weighted measures, not probabilities
under uniform sampling from all actual paths. All constants are fixed
before choosing the arrangement, n or a path.

## 2. Elementary actual wiring geometry, including unbounded cells

The published Felsner--Valtr rotation lemma identifies a taken middle
with a BOUNDED reversed-unique successor; its unbounded qualification
matters. Here is a direct local derivation of the precise form needed.
The rest of this section makes the new diamond interface explicit.

Write wire j as y=f_j(x). At a cell C let S be the wires above C and
T the wires below C. Its vertical section is

    max_(j in T) f_j(x) < y < min_(j in S) f_j(x),   (7)

with missing maxima/minima interpreted as infinities. Each cross-order
condition f_j(x)<f_k(x), j in T,k in S, holds on a half-line, because
that pair crosses once. Thus the nonempty x projection in (7) is an
interval. Its lower and upper boundaries are linearly ordered chains.
Each wire occurs at most once on either chain: after another lower
wire overtakes it, that same wire remains above it to the right and
prevents its return to the maximum. The minimum case is analogous.
Consequently distinct lower exits have distinct wire labels.

Suppose the lower edge e of color l is MIDDLE in the chain of C.
Its two endpoints have finite abscissae alpha<beta. At alpha the
preceding lower wire r meets l and lies above l for x<alpha. At beta
the following lower wire r' meets l and lies above l for x>beta.
The adjacent cell D just below e has above-set S union{l} and
below-set T minus{l}. It can exist only for alpha<x<beta: otherwise
r or r' would be above l while required to be below D<l. Throughout
that interval all old S wires are above l and all old T minus{l}
wires are below l, so D exists and has l as its entire upper chain.
It is bounded, since its projection and all its boundary functions on
the closed finite interval are bounded. In particular

    a MIDDLE edge C->D has D bounded and i(D)=1.     (8)

This proof allows C to be unbounded. Rotating the representation gives
the inverse form: if an edge is middle among the INCOMING edges of its
head, its tail is bounded and has forward outdegree1. Neither statement
claims that every unbounded unique cell corresponds to a middle.

Every bounded cell has at least one upper and one lower edge and at
least three total boundary edges. A two-edge bounded face would be a
closed lens requiring the same pair of wires to meet at both endpoints,
contrary to their unique intersection. Thus a bounded cell with i=1
has o>=2. Also a nonsouth cell has at least one lower exit. One may see
this by following a vertical ray from an interior point; all remaining
wires below it are crossed once before reaching south. Crossing an
oriented edge increases |S| by1, so every directed path terminates at
south in exactly the remaining n-|S| steps. There is no probability
loss to a nonterminal dead end in the normalized process.

At a simple crossing of two adjacent lower edges of C, simplicity
gives four incident cells with four distinct sign patterns on those
two wire labels. In the dual these form an oriented diamond

                v
              /   \
             A     B
              \   /
                w

with edges v->A, v->B, A->w, B->w. At w the two indicated incoming
edges are adjacent in its upper chain: they meet at this very primal
crossing. This is an ACTUAL four-cell face of the dual, without added
edges or presumed realizability of an abstract diagram.

Take now o(v)=4 and use its two adjacent middle exits. By (8), A and
B are bounded with indegree1, hence both have outdegree>=2. If i(w)
were>=3, two adjacent incoming edges could not BOTH be extreme in its
linear upper chain. At least one would be middle. The rotated form of
(8) would force that edge's tail A or B to have outdegree1, a
contradiction. Since the diamond already gives two incoming edges,

    i(w)=2.                                      (9)

This conclusion requires no bound on the outdegrees of A and B. It
holds also if w is unbounded. The north cell cannot be w, by rank.
The reverse penalty at w is valid even if w=south, since it is then
a nonterminal cell in the REVERSE process. There is no degree-zero
penalty at a terminal. In fact o(v)=4 implies n-|S(v)|>=4 by distinct
exit labels, so at least two steps always remain when a trial starts.

## 3. A uniform two-step escape probability: PM8A

Flag a visited vertex as BAD when either of these holds:

* its positive forward outdegree is2 or>=5;
* its positive forward indegree is2 or>=5.

Outdegree0 at south and indegree0 at north are excluded. Along a
complete path the number of distinct bad vertices is at most b(p):
each flag is exactly one of the appropriate WO penalties, and a
vertex with both flags is counted twice by b but once as a vertex.

Under P, a nonunique row with d middles has probability

    extreme: 1/(2+d/V), middle: 1/[V(2+d/V)].       (10)

Thus an outdegree4 middle edge has probability

    mu=1/[2(V+1)].

At any outdegree3 or4 cell, EVERY edge has probability at least mu.
Indeed for d1 the middle probability is1/(2V+1)>mu, and the extreme
probability is still larger since V>1; for d2 its middles equal mu
and its extremes equal V*mu. Unique cells are not used in this bound.

Use the diamond from Section2 at any current outdegree4 vertex v.
If A or B is bad, take the corresponding middle edge. The first-step
probability of hitting a bad vertex is at least mu, and the second
step has total continuation probability1. If neither is bad, their
outdegrees, already>=2, must belong to{3,4}. Choose the two-edge path
v->A->w. It has probability at least mu^2, and w is bad by (9).
Therefore conditional on ANY prefix reaching v,

    P(at least one of the NEXT TWO vertices is bad | prefix)
       >=mu^2=kappa>0.                            (11)

We deliberately use the weaker kappa=mu^2. A sharper special estimate
using the extreme nature of A->w is unnecessary. No bound at arbitrary
high-degree intermediate rows is asserted: if such a row occurs, its
vertex has ALREADY supplied success. This avoids a hidden degree-
dependent probability in (11). The same statement holds for Q in the
rotated arrangement, with exactly the same constants.

## 4. Adapted disjoint trials and their exact moment: PM8B

Let c_F(p) be the number of FORWARD tail vertices of p with o=4.
Let c_R(p) be the number of REVERSE tail vertices with reverse
outdegree4, equivalently forward head vertices with i=4. Put

    c(p)=c_F(p)+c_R(p), 0<=c<=2n.

Here c counts the d2 visits, while b counts d0 and d>=3; unique
and d1 visits are counted in neither statistic.

On a P-distributed forward prefix, apply the following deterministic
rule using only its current vertex and the past. If its current vertex
has outdegree4, take the next TWO edges as one trial; resume at the
endpoint. Otherwise take one ordinary edge and repeat. Section2
guarantees that no incomplete two-edge trial is started at the end.
The rule does not inspect future c or b, nor condition on a desired
event before assigning weights.

Let t(p) be the number of trials. Each forward outdegree4 occurrence
is either a trial start or the single skipped intermediate tail within
a trial. Ordinary one-edge blocks start at other degrees. Hence

    t(p)>=c_F(p)/2.                               (12)

A trial starting at path level j is successful if v_(j+1) or v_(j+2)
is bad. Its TARGET set is exactly{j+1,j+2}. All trial target sets are
disjoint; a subsequent trial starting at j+2 has targets j+3,j+4.
Let S(p) count successful trials. Charge each success to one bad
target vertex, for example the first one in its target set. These
charges are distinct, so

    S(p)<=#visited bad vertices<=b(p).             (13)

At a trial start let Y be its success indicator. Its complete two-edge
conditional distribution has total1, and (11) gives success probability
at least kappa. Thus, with a=1-kappa/2,

    sum_(two-edge continuations s) P(s | prefix) 2^(-Y(s))
       =1-(1/2)P(Y=1 | prefix)<=a.                (14)

Unfold all graph prefixes into the finite rooted tree of this block
process. Give an ordinary block its P transition weight. Give a trial
block its two-edge P weight times2^(-Y)/a. Every outgoing block row
has total<=1, by (14); ordinary rows have total1. Induction over this
finite tree proves

    sum_(complete paths p) P(p) 2^(-S(p)) a^(-t(p))<=1. (15)

This proof retains distinct reconvergent prefixes. Blocks are just a
unique decomposition of each actual path, so no path is lost or counted
twice. It is a finite weighted-flow proof, not an independence claim,
optional-stopping shortcut or replacement by a uniform random cutpath.

Let E_F be any path family satisfying

    c_F(p)>=delta*n/2 and b(p)<eta*n.

Using (12)--(13), the factor multiplying P(p) in (15) is at least
2^(-eta*n) a^(-delta*n/4). Restricting a sum of nonnegative terms
therefore gives

    P(E_F)<=2^(eta*n) a^(delta*n/4)=a^(delta*n/8), (16)

by the chosen eta. Now apply Cauchy to this SAME path family using
(5), with Q(E_F)<=1:

    #E_F K^-n <=sum_(p in E_F) sqrt(P(p)Q(p))
       <=sqrt(P(E_F)Q(E_F))<=a^(delta*n/16).

Consequently #E_F<=J1^n. The identical reversed block argument yields
#E_R<=J1^n for the family c_R>=delta*n/2,b<eta*n. Since c>delta*n
forces one of these two directional inequalities,

    #{p:c>delta*n,b<eta*n}<=2 J1^n.               (17)

Only the final Cauchy conversion gives an ABSOLUTE count. Equation(16)
alone is a statement under the particular positive local weight P.
The total number of paths need not be close to K^n.

## 5. Explicit tilt for the complementary few-d2 family: PM8C

Set L0,M0,V0 as in the opening. All exceed1 and L0=M0 V0, so the
pathwise lower bound (4) gives sqrt(W0 W0')>=K0^-n. Their raw row sums
tau_d are NOT all at most1. Direct hand arithmetic gives

    tau_0=18/19<1, tau_1=1,
    L0 M0=361/140,
    L0 M0^2=61731/19600,
    2+2/V0=221/70,
    tau_2=61880/61731=chi>1,
    tau_3=10250800/10556001<1.                    (18)

The two gaps are chi-1=149/61731 and
1-tau_3=305201/10556001. For every integer d>=2,

    tau_(d+1)/tau_d=(2V0+d+1)/[M0(2V0+d)].        (19)

This ratio strictly decreases with d. At d2 it is

    73220/75582<1, gap2362/75582.

Thus every d>=3 row has tau_d<=tau_3<1. This verifies the entire
unbounded integer range, without a cutoff or a real-degree assertion.

Divide each outdegree4 row by chi, and leave every other row unchanged.
All rows now have sum<=1. Do this in both directions on the original
graph. The resulting complete path weights have products

    W0(p) chi^(-c_F(p)), W0'(p) chi^(-c_R(p)).

Finite-prefix flow, Cauchy and (4) therefore give

    sum_p chi^(-c(p)/2)<=K0^n.                    (20)

For c<=delta*n, every summand is at least chi^(-delta*n/2), so

    #{p:c<=delta*n}<=K0^n chi^(delta*n/2)=J0^n.   (21)

The exceptional row factor has been paid EXACTLY and locally, before
flow is invoked. One cannot simply use the infeasible raw weights in
an all-path substochastic bound.

It remains to justify K0<K, which is not a contradiction to the WO1
feasible-family optimum. The tilt in (18) is OUTSIDE that family at d2.
Let f(L)=2L/(L^2-1) and F(L)=L f(L)^(3/4). Then M0=f(L0) and
K0=F(L0), whereas K=F(ell). The polynomial defining ell is strictly
increasing for L>=2. Hand evaluation yields

    P(19/9)=(130321-123462-6561)/6561=298/6561>0.

Hence 2<ell<L0. Differentiation on this whole interval gives

    d/dL ln F(L)=(L^2-7)/[4L(L^2-1)]<0,           (22)

because L0^2=361/81<7. Every denominator is positive. Therefore
1<K0<K. The ratio ln(K/K0)/ln chi is strictly positive; our
delta is in(0,1] and satisfies delta*ln chi<=ln(K/K0). Accordingly

    J0=K0 chi^(delta/2)<=sqrt(K0 K)<K.             (23)

No floating point, root approximation or optimizer is used. In (22)
we differentiated F itself outside the feasible envelope, not an
incorrect continuation of WO's optimized envelope branch.

## 6. Uniform low-cost and complete counts: PM8D

All constants were fixed before choosing n or its arrangement. They
satisfy delta>0, 0<kappa<1, 0<a<1 and eta>0. Thus J1<K and J2<K;
(23) gives J0<K, so J<K. Also J>=J0>=K0>1.

Split the complete path set first according to c<=delta*n or c>delta*n,
and in the latter case according to b<eta*n or b>=eta*n. Equation(21)
bounds the first family by J0^n; (17) bounds the second by2 J1^n;
the accepted absolute WO3 tail (6) bounds the third by J2^n even if
we enlarge it to all paths with b>=eta*n. This proves (1), for EVERY
actual simple marked arrangement and EVERY integer n>=2. Enlarging
the third family causes harmless overcounting in an upper bound.

For the exact WO4 premise, put J_L=max(J0,J1)<K. Equations(17),(21)
give the uniform low-cost estimate

    #{p:b(p)<eta*n}<=J0^n+2 J1^n<=3 J_L^n.        (24)

Choose J_L'=sqrt(K J_L), so J_L<J_L'<K. For every integer

    n>=max(2, ceil[ln3/ln(J_L'/J_L)]),

the right side of (24) is at most (J_L')^n. This is precisely the
fixed-base, fixed-threshold, EVERY-arrangement and EVERY-later-size
WO4 hypothesis. It is not a subsequence estimate, a relative fraction
of uniform paths, or a claim that every individual path has linearly
many penalties. Few-d2 paths may have no such local density; their
absolute count was controlled by a DIFFERENT valid weight argument.

## 7. Exact official transfer: PM8E

Let gamma_n be the largest actual cutpath count. The separately accepted
canonical insertion gives B_(n+1)<=gamma_n B_n, with B2=1 and
C(n)=B_n in the fixed polygon/orientation convention. Applying (1)
for j=2,...,N-1 gives, including the empty N2 product,

    log2 B_N
       <=[N(N-1)/2-1]log2 J +2(N-2).              (25)

The factor4 per insertion contributes only2(N-2), not a quadratic
entropy term. Divide by N^2 and take limsup to obtain (2). No new
factorial, label quotient, unmarked identification, arbitrary insertion
history count or rotation quotient is introduced. The official base2
and quadratic normalization are retained. Existing equality of lower
and upper limits may be combined only under its separate authority;
this upper estimate does not calculate that common value.

## 8. Source roles, failed shortcuts and remaining boundaries

The official B4 PDF and the current exact accepted WC/WO authorities
are operative. Fresh primary reads of Felsner--Valtr covered the marked
dictionary/insertion passages and the middle/bounded-unique rotation
proof (printedp6); the exact local form (8) is also derived here.
Dallant's current paper, Section2 through Lemma7, supplies the attributed
rotation/zone framework under the same actual marked conventions.
The older original sharp-zone proof and the complete dictionary
foundations remain separately attributed, not freshly reproduced.
No full literature-priority claim is made.

The new geometric proof needs actual four-cell diamonds, boundedness
of middle successors, linear upper/lower chains and once-only wire
crossings. It cannot be inferred for arbitrary degree lists or arbitrary
directed graphs. Nor does (15) follow by treating successive trials as
independent. Prefix-dependent trials require the explicitly unfolded
block flow. Normalizing just the new raw d2 violation in Section5 is
essential; ignoring it would contradict the proved WO1 family optimum.

Searches also exposed a primary undergraduate weighted-zone manuscript,
but its operative theorem/proof was NOT read and nothing from it is
imported. No new paper is invented from search absence; no source-author
program, previous certificate, mathematical executable, routine test,
scan, numerical optimization or CAS supplied this proof. Only integrity
code accompanies the packet. No charge, contact or access bypass occurred.

The proposed improvement, its small explicit strict gap and the claimed
WO4 discharge all remain UNVERIFIED pending TWO OTHER complete blind
audits. Exact value, effective upper R, matching lower estimate, annual
solution and novelty remain outside the conclusion. The companion
obligations enumerate all substantive geometry/probability/algebra/
counting inferences; all older bytes are preserved.
