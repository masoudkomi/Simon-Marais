# A two-route discount pays an infeasible row and bounds actual class pressure

2026-10-18 UTC. **Candidate proof - unverified.** C,
`/root/review_2017_coarsening_r1`, is the sole NEW constructor and is
EXCLUDED from both required OTHER initially blind ENTIRE WHOLE audits.
Root supplied the general counting target, no new proof inference.
Requested inherited gpt-6.1-sol/max; verified effective-setting readback
is unavailable. This is a proposed stricter upper certificate and a
weighted moment for actual classes, not the exact official value,
an effective all-scale upper modulus R, a matching lower bound, an
annual solution, external validation or a priority claim.

## Significance and precise proposed claims

The official2017 problem concerns tilings of a fixed regular unit-sided
2N-gon. Under the accepted marked-arrangement dictionary, the tilings
are commutation classes, not reduced reversal words before quotienting.
An actual cutpath inserts the next canonical pseudoline. The accepted
PM9 bound is obtained by combining two moments. Here we retain BOTH
routes of an actual diamond and distinguish the loss at degree two
from the loss at degree at least five. The resulting two-step gain
pays an entire slightly infeasible degree-four row. This supplies
a direct smaller base and then a pressure estimate on actual classes.
It does not presume that formal degree sequences are arrangements.

Fix the exact rational constants

    lambda=2109/1000,
    m=2lambda/(lambda^2-1)=4218000/3447881,
    v=lambda/m=(lambda^2-1)/2=3447881/2000000,
    G=lambda*m^(3/4).

For integer j>=0 put

    sigma_j=(2+j/v)/(lambda*m^j),
    chi=sigma_2,
    s0=sqrt(sigma_0), s3=sqrt(sigma_3), s=max(s0,s3),
    mu=1/[2(v+1)],
    dstar=2mu*min(1-s, v*mu*(1-s0)),
    a=1-dstar, z=a^(-1/2), xi=z/chi.

All these constants are fixed BEFORE choosing a size, arrangement or
path. Sections2 and5 prove 0<a<1, chi>1 and xi>1. In an actual simple
marked arrangement A of n>=2 pseudolines, let c_F(p) count forward
tail vertices of outdegree four on a complete cutpath p. Let c_R(p)
count reverse tail vertices of reverse outdegree four, equivalently
forward head vertices of indegree four. Set c(p)=c_F(p)+c_R(p).
Terminal degree zero is never a row or a penalty.

**PR11A (actual two-route weighted discount).** The normalized exit
measure at a degree-four vertex satisfies, after EVERY prefix,

    E[D(next vertex)*D(following vertex) | prefix]<=a<1,       (A)

where D is the explicit symmetric vertex discount in Section3.
This holds in either orientation, includes unbounded cells, and sums
the full continuation of a bad intermediate vertex of arbitrary degree.

**PR11B (paid row and absolute path moment).** For EVERY actual A and
EVERY n>=2,

    sum_(complete p in A) xi^(c(p)/2)<=G^n,
    #complete cutpaths of A<=G^n.                            (B)

The raw degree-four row has mass chi>1. It is normalized before ANY
flow argument; the final reward z pays chi because chi^2*a<1.

**PR11C (strict comparison to current PM9).** With H EXACTLY the
currently accepted PM9 base,

    ln(H/G)>701/8206000>0.                                  (C)

This is a hand rational/logarithm comparison, not an optimizer or a
new decimal approximation. In particular it is a strict improvement
over H, not merely over the earlier feasible-family optimum K.

**PR11D (actual class pressure and official upper bound).** Canonical
deletion gives each actual marked N-line class T a UNIQUE chain
T_2,...,T_N and insertion paths p_j in T_j, j=2,...,N-1. Define

    D_N(T)=sum_(j=2)^(N-1) c(T_j,p_j),
    E_N=N(N-1)/2-1.

Then for EVERY N>=2 and every real h>=0,

    sum_(actual classes T of size N) xi^(D_N(T)/2)<=G^(E_N), (D1)
    #{T:D_N(T)>=h}<=G^(E_N)*xi^(-h/2),                      (D2)
    log2 C(N)<=E_N*log2 G,
    limsup_N log2 C(N)/N^2 <=(1/2)log2 G
               <(1/2)log2 H.                              (D3)

There is NO factor per word, history, reflection, rotation, permutation
of deletion order or boundary labelling. D_N uses one fixed canonical
deletion order; it is not asserted invariant under changing that order.
These are absolute sums and tail COUNTS, not uniform-class probabilities.

## 1. Accepted inputs, exact objects and attribution

Use actual simple marked arrangements: a north unbounded cell, the
opposite south cell, one transverse intersection per pair of wires,
no triple intersections. The directed dual orients edges north to south.
Every complete cutpath has n steps, and no nonsouth cell is a dead end.
At a cell of outdegree j+2>=2 there are j middle exits and two extremes;
outdegree one is unique, NOT the j=0 nonunique case. Reverse orientation
means rotating the SAME arrangement and reversing the SAME paths.

The indispensable accepted inputs are current WC, WO, PM8 and PM9,
with their exact current MD/JSON authorities. Their complete bodies
and authorities were freshly read for this packet. C's older PM8
authorship and WC/WO/PM9 review roles are disclosed as accepted-input
roles; this is not an independent recertification of C's old theorem.
R10 was also completely read to avoid its demonstrated word/class
normalization error; it is context, not a premise of (A)--(D3).

For one actual path let u,u' be unique exits, k,k' middle exits TAKEN,
and q,q' ALL available middle exits in the two directions. Accepted WC
uses the published rotation/zone constraints

    k+k'<=u+u',  q+q'-u-u'<=3n/2.                           (1)

For ANY positive L,M,V>1 with L=MV, assign RAW weight1 at a unique
exit, 1/(L*M^j) at each extreme in a j-middle nonunique row, and
1/(L*M^j*V) at each middle. Even if some raw row is infeasible,
the purely PATHWISE algebra gives

    sqrt(W(p)*W'(p))
       =L^(-n)*M^[-(q+q'-u-u')/2]*V^[(u+u'-k-k')/2]
       >=[L*M^(3/4)]^(-n).                                (2)

Both signs in (1) are used correctly since M,V>1; a negative zone
defect causes no exception. Equation(2) is not a claim that RAW
weights have total mass at most one.

The other precise accepted PM8 geometry is as follows. Every middle
successor is BOUNDED and has indegree one, even if its parent is
unbounded. Such a successor has outdegree at least two: a bounded
face has at least three sides. The two adjacent middles of an
outdegree-four vertex form an actual diamond v0->A,B->w with
indegree(w)=2. PM8's proof uses cell sign sets, linear upper/lower
boundary chains and the fact that every pair of wires crosses once.
It does not use the false converse for unbounded unique cells.

One NEW useful consequence is that A->w and B->w are EXTREME exits.
If either were middle, the accepted middle-successor implication would
give indegree(w)=1, contradicting two. They cannot be unique exits
since A and B have outdegree at least two. Their distinct first edges
make the two routes disjoint events, despite their common endpoint.
At least two steps remain: outdegree four gives four distinct available
wire labels not yet crossed. No terminal trial is incomplete.

The original Felsner--Valtr paper was freshly read in its operative
marked/wiring/tiling/insertion and middle/rotation passages. The exact
parent-fiber statement says cutpaths count the extensions obtained by
adding the canonical largest label. Dallant's operative Section2
through Lemma7 was freshly read for (1). Their deeper representation
and original sharp-zone foundations retain separately attributed
accepted scopes, not a fresh reconstruction here. Search, source
read limits and the unused later computational/theorem sections are
recorded in the source companion. No primary theorem is imported
from an abstract, a heuristic or a uniform-WORD law.

## 2. A rational point with just ONE infeasible row

The displayed lambda,m,v satisfy lambda=m*v and all exceed one.
Also

    17/10<v<7/4, m>6/5, lambda^2<89/20.                    (3)

For the last two comparisons the exact positive integer gaps are

    5*4218000-6*3447881=402714,
    89*1000000-20*4447881=42380.

The v comparisons are immediate from 3400000<3447881<3500000.
At j=0, sigma_0=2/lambda. At j=1, the definition of m gives
sigma_1=1 EXACTLY. At j=2, elementary simplification gives

    chi=(lambda^4-1)/(2lambda^3)
       =1+22483332161/18761162058000,
    1<chi<801/800.                                        (4)

Here lambda^3=9380581029/10^9 and
lambda^4=19783645390161/10^12. Subtracting twice the former and
one gives the positive numerator22483332161/10^12. The upper
comparison in(4) has exact gap

    18761162058000-800*22483332161=774496329200>0.

At j=3 write y=lambda^2. Direct simplification gives

    sigma_3=(y^3-3y+2)/(4y^2)
           =(y-3/y+2/y^2)/4.                              (5)

This function is strictly increasing for y>1: its derivative is
(y^3+3y-4)/(4y^3)>0. Hence (3) and y<89/20 give

    0<sigma_3<614169/633680<97/100,                        (6)

where 97*633680-100*614169=50060>0. Also
sigma_0=2000/2109<97/100. For EVERY integer j>=3,

    sigma_(j+1)/sigma_j=(2v+j+1)/[m*(2v+j)]
          <(37/32)/(6/5)=185/192<1,                       (7)

since 2v+j>32/5 and this ratio decreases with j. Thus all j>=3
rows are at most sigma_3<1. There is no truncation, large-degree
assumption or real-degree claim. The ONLY infeasible raw row is j=2.

## 3. Two categories of loss and the actual diamond discount

For every vertex x define

    D(x)=s0^[1_{o(x)=2}+1_{i(x)=2}]
           *s3^[1_{o(x)>=5}+1_{i(x)>=5}].                  (8)

Here i,o are positive indegree/outdegree when present; zero at north
or south triggers no indicator. Set

    R(p)=product_(x along p) D(x)=s0^b0(p)*s3^b3(p),       (9)

where b0,b3 count the indicated flags across BOTH orientations.
A vertex with two flags is counted twice; no unproved injection of
bad vertices into one directional statistic is needed. All factors
lie in(0,1], so R(p)>0. The SAME R belongs to p and its reverse.

Normalize EVERY raw outgoing row by its own positive sigma_j;
unique rows remain one. Call the full forward and reverse products
P(p),Q(p). Every nonterminal row now sums EXACTLY to one, including
the row whose raw sum is chi>1. The normalized nonunique probabilities
are

    extreme: v/(2v+j), middle: 1/(2v+j).                  (10)

In particular a degree-four middle has probability mu. At a degree
three or four vertex every extreme has probability at least v*mu.

At a degree-four trial vertex v0 use its actual two-middle diamond
v0->A,B->w. If A is bad (outdegree2 or>=5), then i(A)=1 and
D(A)<=s. Its WHOLE second-step continuation has total probability
one, so its conditional expected target discount is at most s.
This remains true with unbounded second-step degrees; the success
is already paid at A. If A is good, o(A) is three or four, D(A)=1,
and its extreme edge to w has probability at least v*mu. Since
i(w)=2, D(w)<=s0, regardless of other flags. Therefore

    E[D(A)D(next) | first middle to A]
       <=1-min(1-s, v*mu*(1-s0)).                         (11)

The SAME bound holds for B. Their first-edge probabilities are each
mu, on disjoint continuations. All other first-edge continuations
have target discount at most one. Thus the conditional two-step
row obeys (A) with exactly the a defined above. This is why BOTH
routes and the degree-two bottom matter. Rotation gives precisely
the same statement for Q with the same symmetric D.

Since 0<mu<1/4 and the minimum in dstar lies in(0,1), we have
0<dstar<1/2 and 0<a<1. No future c,b0,b3 or final event is used
to choose transitions, and no independence of trials is asserted.

## 4. Finite adapted block flow and exact payment of chi

Scan a complete path under P. At a degree-four current vertex take
the next TWO edges as a trial; otherwise take one ordinary edge.
This depends only on the current prefix. Let t be the number of
trials. Each degree-four tail is either a trial start or one skipped
intermediate tail, so c_F<=2t. The targets of a trial starting at
level j are {j+1,j+2}; these sets are disjoint. A subsequent trial
may start at j+2, but its targets are then j+3,j+4.

Unfold all prefixes, even when the underlying graph reconverges.
Give an ordinary block its P probability. Give a trial continuation
its two-edge P probability times D(target1)D(target2)/a. By(A),
every block row has total at most one. Finite leaf induction yields

    sum_p P(p)*R_trial(p)*a^(-t(p))<=1,                   (12)

where R_trial is the product of D over ONLY trial targets. Because
all D<=1 and targets are distinct, the full R(p)<=R_trial(p).
This also pays the initial north vertex, omitted from all targets;
its additional discount is harmless. Since z=a^(-1/2)>1,
z^c_F<=a^(-t). Consequently

    sum_p P(p)*R(p)*z^c_F(p)<=1.                          (13)

The reversed proof gives sum Q*R*z^c_R<=1. These are actual full
path sums, not expectations under uniform cutpaths. Finite Cauchy
on the SAME path set gives

    sum_p sqrt(P(p)Q(p))*R(p)*z^(c(p)/2)<=1.              (14)

Let S,S' be the products of raw row sums in the two directions.
The exhaustive row bounds of Section2 give

    S(p)S'(p)<=chi^c(p)*sigma_0^b0(p)*sigma_3^b3(p)
                 =chi^c(p)*R(p)^2.                       (15)

Unique and j=1 rows contribute one; j=2 contributes chi; j=0
contributes sigma_0; every j>=3 contributes at most sigma_3.
Since P=W/S and Q=W'/S', equations(2),(15) imply

    sqrt(PQ)*R*z^(c/2)
       >=G^(-n)*(z/chi)^(c/2).                            (16)

Thus (14) proves the first inequality in(B), once xi=z/chi>1 is
checked. Nothing drops the chi loss. No flow bound was applied to
the infeasible RAW weights, nor was a raw positive moment multiplied
in an unjustified direction. Both directions normalize the same
row types and compare the same paths.

## 5. Hand slack proves xi>1 at the chosen rational point

From(6), s<197/200, because97/100<38809/40000=(197/200)^2.
Also s0<39/40, since

    2109*1521-3200000=7789>0.

Equations(3) give mu>2/11 and v*mu>17/55. Therefore

    1-s>3/200,  v*mu*(1-s0)>17/2200,
    min(1-s,v*mu*(1-s0))>17/2200,
    dstar> (4/11)*(17/2200)=17/6050.                      (17)

The minimum comparison is legitimate since3/200>17/2200.
On the other hand(4) gives

    chi^2-1<1601/640000<17/6050,

where17*640000-1601*6050=1193950>0. Put e=chi^2-1>0.
Then e<dstar, and

    chi^2*a=(1+e)(1-dstar)
           =1+e-dstar-e*dstar<1.                         (18)

Equivalently z/chi>1. Hence the moment in(B) bounds the unweighted
path count too. All bounds are fixed, explicit and valid at EVERY
arrangement/size; no asymptotic row approximation is used.

## 6. Strict comparison with the CURRENT PM9 H

Use old parameters ONLY in this section: ell>2 solves
P(x)=x^4-2x^3-1=0; old K=F(ell), K0=F(19/9), where

    F(x)=x*[2x/(x^2-1)]^(3/4),
    Ctilt(x)=(x^4-1)/(2x^3).

Old chi0=Ctilt(19/9)=61880/61731, and Ctilt(ell)=1.
Write A=ln(K/K0)>0, B=ln chi0>0, r=sqrt(rho_old),
kappa=1/[4(V_old+1)^2], q=-ln[1-kappa(1-r)]. The EXACT accepted
PM9 base satisfies

    ln(K/H)=A*q/(2B+q).                                  (19)

No new interpolation limit is taken. For x>=2, P is strictly
increasing. Direct evaluations are

    P(21/10)=-739/10000<0,
    P(2107/1000)=869337601/10^12>0.

Thus21/10<ell<2107/1000<lambda<19/9. On the ENTIRE interval
[21/10,19/9], set

    f(x)=-(ln F)'=(7-x^2)/[4x(x^2-1)],
    g'(x)=(ln Ctilt)'=(x^4+3)/[x(x^4-1)].

All denominators are positive. Endpoint bounds give

    1/12 <1854/21280<=f(x)<=2590/28644<1/11.               (20)

The integer gaps are12*1854-21280=968 and28644-11*2590=154.
Also19<x^4<20 and x<=19/9 imply
g'(x)>198/361>1/2. Therefore integral comparisons give

    A/B=[integral_ell^(19/9) f]/[integral_ell^(19/9) g']
          <2/11,                                         (21)
    ln(K/G)=integral_ell^lambda f
          >(lambda-ell)/12>1/6000.                       (22)

To bound q, old V_old=(ell^2-1)/2>17/10 gives kappa<1/28:
4(V_old+1)^2>729/25>28. Formula(5) also holds at x=ell.
The bounds ell^2>441/100 and ell^4<20 give

    sigma_3(old)>
       (441/100-100/147+1/10)/4=56297/58800
       >1521/1600=(39/40)^2,

the last cross-product gap being640400>0. Since rho_old is at
least sigma_3(old), r>39/40. Hence

    0<kappa(1-r)<1/1120,
    q<1/1119,                                            (23)

using -ln(1-t)<t/(1-t), obtained by integrating1/(1-s) on[0,t].
From(19),(21),(23),

    ln(K/H)<(A/B)*q/2<1/12309.                           (24)

Subtract (24) from (22). Since
1/6000-1/12309=701/8206000, this proves(C). Every comparison is
strict before taking n to infinity. The new base lies outside WO1's
feasible raw-row family (chi>1); there is no contradiction to WO1.

## 7. Canonical actual-class pressure and official transfer

Let A_N be the exact marked classes counted by C(N). The canonical
labels are determined by the north-boundary order. Deleting the
largest label N leaves a marked class on N-1 labels; conversely a
cutpath in that parent inserts N in its fixed boundary slot. The
published fiber statement is exact. Repeating produces ONE chain
per class; it does not produce all possible insertion schedules.

Let Z_N=sum_(T in A_N) xi^(D_N(T)/2). At N=2 there is a single
class, D_2=0 and Z_2=1. For any parent T in A_n, the extensions
have exponent D_n(T)+c(T,p). Apply(B) inside EACH actual parent:

    Z_(n+1)=sum_(T in A_n) xi^(D_n(T)/2)
                     *sum_(p in T) xi^(c(T,p)/2)
             <=G^n*Z_n.                                 (25)

If one uses only the accepted insertion injection, the equality in
(25) can be weakened to <= and every conclusion still follows.
The exact fiber version shows directly that no class is counted
with reduced-word multiplicity or variable boundary labels. Summing
n=2,...,N-1 gives(D1), with an empty product at N=2. Restricting a
nonnegative weighted sum to D_N>=h gives(D2). Because xi>1,
C(N)<=Z_N, yielding(D3). There is no prefactor four or any other
factor repeated at every insertion.

The statistic is geometrically intrinsic to the marked class and
the chosen canonical deletion order: graph degrees and insertion
paths are invariant under the allowed marked isomorphisms and
commuting disjoint swaps. Changing a reduced-word representative
does not add histories. A different deletion order need not give
the same D_N; we make no such claim. The moment cannot be divided
by an unknown C(N) and called an exponentially small probability
without a corresponding count lower bound. The exact scalar value,
typical mass, matching lower construction and effective upper R
remain open here.

## 8. Failed routes, source limits and checkpoint boundary

Simply doubling the old success probability would lose the sharper
degree-two discount. Discarding chi would apply flow to an infeasible
row. Multiplying two separate absolute moments in the wrong direction
would not prove a path bound. Ignoring a bad high-degree successor's
other continuations would introduce an unbounded-degree error. These
routes are replaced by(11)--(18), which pay every factor explicitly.
No extremal or typical arrangement is asserted to attain G.

Current R10 proves that a common pointwise scalar correction from
word multiplicities to classes has an n^2*ln n obstruction. Nothing
here makes that correction. Nor does the positive class statistic
evaluate L, imply a variational identity, furnish an upper convergence
modulus, prove average-zone conjectures, or change the accepted
global existence theorem. All claims retain their exact scopes.

All new algebra, finite flow and comparisons were done by hand.
No mathematical executable, CAS, optimizer, routine scan/test, source
program, author/old certificate/freezer replay or native child was
used. The separate administrative program only fingerprints inputs,
checks documentary labels and binds the complete packet. It has no
mathematical arithmetic beyond counting labels. No charges, contact,
cache edits, access bypass, worker Git or shared-file writes occurred.
Both OTHER whole audits must freeze with ALL64 separate dispositions,
sources, code and ALLmetadata before peer findings; only coordinator
reconciliation can promote any result.
