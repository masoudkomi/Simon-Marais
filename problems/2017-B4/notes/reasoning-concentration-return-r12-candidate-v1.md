# Directional flow imbalance costs actual class entropy

18 October2026 UTC. **Candidate proof - unverified.** C,
`/root/review_2017_coarsening_r1`, is the sole NEW constructor and is
EXCLUDED from TWO required OTHER initially blind ENTIRE WHOLE audits.
Root supplied the generic research target, no new proof inference.
Requested inherited gpt-6.1-sol/max; effective-setting readback unavailable.
Only official2017 B4 is investigated. No exact value, improved global
base, matching lower bound, effective upper modulus, annual solution or
publication priority is claimed.

## 0. What is new and what is imported

The exact official objects are classes of tilings of a FIXED regular
unit-sided2N-gon, equivalently the accepted simple marked pseudoline
arrangement classes. Rotations, reflections, reduced words before the
commutation quotient and arbitrary insertion schedules are not substituted.

Use the COMPLETE accepted R11 proof and current MDJSON authority. C
constructed that older result; this is an accepted-input role, not an
independent recertification. The new step uses the TWO directional
subprobability estimates retained in its proof, not only its scalar
moment conclusion. An arithmetic-mean identity keeps the actual
forward/reverse imbalance discarded by Cauchy. It gives a new structural
class pressure and entropy-sector loss. A concrete actual arrangement
family proves this new cost is not controlled by the old degree-four
cost and refutes a positive-density premise for that old cost.

Fix R11's constants, once and for all:

    lambda=2109/1000, m=4218000/3447881,
    v=3447881/2000000, G=lambda*m^(3/4).

In the exact notation of that accepted proof,

    sigma_j=(2+j/v)/(lambda*m^j), chi=sigma_2,
    s0=sqrt(sigma_0), s3=sqrt(sigma_3), s=max(s0,s3),
    mu=1/[2(v+1)],
    dstar=2mu*min(1-s,v*mu*(1-s0)), a=1-dstar,
    z=a^(-1/2), xi=z/chi>1.

R11 proves v>1,0<a<1,z>1 and xi>1. No parameter is optimized or changed
here. In every actual n-line arrangement,n>=2, write P(p),Q(p) for
R11's POSITIVE normalized forward and reversed exit probabilities on
the SAME complete n-edge cutpaths. At a nonunique cell with j middles,
the probabilities are

    each extreme: v/(2v+j), each middle:1/(2v+j);

a unique exit has probability1. Thus P and Q separately sum to1.
Let c_F,c_R be the old forward/reverse degree-four-tail counts, and
c=c_F+c_R. Terminal zero degrees are not rows. R11 defines the SAME
symmetric positive discount R(p) in both directions. Its Section4,
equations(13)-(16), gives the following operative accepted inputs:

    X(p)=P(p)*R(p)*z^c_F(p),
    Y(p)=Q(p)*R(p)*z^c_R(p),
    sum_p X(p)<=1, sum_p Y(p)<=1,                         (I1)
    sqrt(X(p)Y(p))>=G^(-n)*xi^(c(p)/2).                 (I2)

These estimates already include the actual diamond geometry, correct
normalization of the infeasible raw row and exact chi payment. They
hold for every arrangement and every complete path, without independence
of reconvergent prefixes. We do not derive a new flow from the final
R11 tail count alone. The whole accepted body/current MDJSON were
freshly read before applying(I1)-(I2).

Define a new REAL statistic on an actual cutpath:

    T(p)=ln[X(p)/Y(p)]
        =ln[P(p)/Q(p)]+(c_F(p)-c_R(p))*ln z.             (5)

The common R cancels exactly. T is a log ratio of the two weighted
flows; these flows are not asserted to have equal total mass. No
time-reversal theorem, stationarity, uniform-path law or stochastic
independence is assumed. Positivity makes every logarithm finite.

Proposed claims:

**CI12A.** For every actual arrangement and every n>=2,

    sum_p xi^(c(p)/2)*cosh(T(p)/2)<=G^n.                 (6)

**CI12B.** On ONE fixed largest-label deletion chain of each actual
N-line class tau, let p_n be the canonical insertion path in its
n-line parent, n=2,...,N-1. Define

    D_N=sum_n c(p_n),
    J_N=sum_n ln cosh(T(p_n)/2),
    S_N=sum_n |T(p_n)|,
    E_N=N(N-1)/2-1.

For every N>=2, empty sums at N2,

    sum_tau xi^(D_N(tau)/2)*exp(J_N(tau))<=G^E_N,        (7)
    sum_tau xi^(D_N(tau)/2)*exp(S_N(tau)/2)
                    <=2^(N-2)*G^E_N.                  (8)

In particular the actual sectors J_N>=h*N^2 or S_N>=s*N^2 lose,
respectively, at least h/ln2 or s/(2ln2) in their entropy upper bound,
relative to (ln G)/(2ln2). This is an ABSOLUTE count statement; a
uniform-class concentration claim requires its stated normalization.

**CI12C.** For every probability law pi on the actual N-line classes,

    Ent(pi)+E_pi[J_N+(ln xi)*D_N/2]<=E_N*ln G.           (9)

Entropy Ent uses natural logarithms. In particular if the ACTUAL
counts asymptotically saturate the R11 upper rate, then under their
uniform laws S_N/N^2 and D_N/N^2 tend to0 in mean and probability.
Saturation is an EXPLICIT hypothesis, not an established fact.

**CI12D.** There is an explicit hereditary family tau_N of ACTUAL
simple marked straight-line arrangements for which

    D_N(tau_N)=1 for N>=5,
    S_N(tau_N)/N^2 -> (ln2)/2,
    J_N(tau_N)/N^2 -> (ln2)/4.                          (10)

Thus no uniform assertion D_N>=epsilon*N^2 for every class can hold
for fixed epsilon>0. Nor can S_N<=A*D_N+o(N^2) hold uniformly over
actual classes for a fixed A. The new cost detects real configurations
missed by the old cost. This family has ONE class per size; it is not
claimed to carry all or a positive fraction of total class entropy.

## 1. The retained arithmetic-mean identity

For any positive x,y, with t=ln(x/y),

    sqrt(xy)*cosh(t/2)=(x+y)/2.                         (11)

Indeed cosh u=(e^u+e^(-u))/2. Applying(11) path by path and summing(I1)
gives

    sum_p sqrt(X(p)Y(p))*cosh(T(p)/2)<=1.

Each cosh is positive. Substitute the POINTWISE lower bound(I2) in
this inequality and multiply by G^n. This proves(6). It does not
multiply unrelated moment upper bounds in an unjustified direction;
it retains the same path set and actual X,Y on each path.

Taking cosh>=1 recovers R11's path moment, but(6) also penalizes an
imbalanced path even when c=0. The new input is not a theorem about
arbitrary externally assigned T values; T MUST be the actual flow ratio
(5) in the R11 proof. Changing the drawing or a commuting-word
representative does not change graph degrees, extreme/middle exits,
P,Q,c_F,c_R, or the ratio. It is well defined on the marked parent and
its insertion path. Reversing the same arrangement/path changes T's
sign and leaves cosh(T/2) unchanged. A different global deletion order
is not asserted to leave J_N,S_N unchanged.

## 2. Transfer to exact classes, with every factor accounted for

The accepted canonical extension fiber associates each child class
with its UNIQUE largest-label parent and one complete cutpath in that
parent. Begin with the one N2 class. Repeated deletion supplies ONE
chain per class. There is no sum over alternative histories or words.

Put w(p)=xi^(c(p)/2)*cosh(T(p)/2), and let

    Z_N=sum_tau xi^(D_N/2)*exp(J_N).

For each actual parent tau on n labels, the extensions have weight
xi^(D_n(tau)/2)*exp(J_n(tau))*w(p). Applying(6) inside EACH parent gives

    Z_(n+1)<=G^n*Z_n, Z_2=1.

The exact fiber gives equality before the inequality. An injection
version would still suffice for this upper bound. Iteration over
n=2,...,N-1 gives(7), since that sum of n is E_N. Every factor is
counted once along a canonical chain, irrespective of how many reduced
words realize its class.

For every real t,

    |t|/2-ln2 <= ln cosh(t/2) <= |t|/2.                 (12)

This follows from e^|u|/2<=cosh u<=e^|u|. There are N-2 insertion
steps, so

    S_N/2-(N-2)ln2<=J_N<=S_N/2.                        (13)

Exponentiating the left inequality, multiplying by the positive class
weight and summing(7) proves(8). The only loss is2^(N-2), subquadratic
on the logarithmic scale; it is not a repeated factorial or a diagram
multiplicity. At N2 both sides equal1 and(13) is an empty identity.

More generally, for all real d,h,s>=0,

    #{tau:D_N>=d,J_N>=h}<=G^E_N*xi^(-d/2)*e^(-h),      (14)
    #{tau:D_N>=d,S_N>=s}
           <=2^(N-2)*G^E_N*xi^(-d/2)*e^(-s/2).        (15)

These follow by restricting a positive sum and using the lower bound
on every retained summand. No law on uniformly random classes is
silently substituted for the flow probabilities P,Q.

Taking d=0 and h=hbar*N^2 in(14), or s=sbar*N^2 in(15), for any fixed
hbar,sbar>=0 (distinct from the old discount s0), yields

    limsup N^(-2)log2 #{tau:J_N>=hbar*N^2}
               <=(ln G)/(2ln2)-hbar/ln2,
    limsup N^(-2)log2 #{tau:S_N>=sbar*N^2}
               <=(ln G)/(2ln2)-sbar/(2ln2).             (16)

Here log0=-infinity. If an upper expression is negative, the integer
counts are eventually zero. These are structural entropy losses of
actual sectors. They are not a numerical evaluation of the full count.

## 3. Finite entropy budget and the exact concentration condition

Let a_tau=xi^(D_N(tau)/2)*exp(J_N(tau)), which is positive for every
actual class. For any probability law pi, Jensen's inequality for ln
on its positive support gives

    sum_tau pi_tau*ln[a_tau/pi_tau]
       <=ln[sum_(pi_tau>0) a_tau]
       <=ln Z_N<=E_N*ln G.

The left side is Ent(pi)+E_pi[J_N+(ln xi)D_N/2], proving(9), with the
usual zero-probability terms omitted. This is an elementary finite
entropy inequality, not an imported infinite-volume variational identity.

For the uniform law on the C(N) actual classes it reads

    E_unif[J_N+(ln xi)D_N/2]<=E_N*ln G-ln C(N).          (17)

Both costs are nonnegative. Consequently, IF a sequence of these
actual counts satisfies

    E_N*ln G-ln C(N)=o(N^2),                            (18)

then E_unif J_N/N^2 and E_unif D_N/N^2 tend to0. Equation(13) also gives
E_unif S_N/N^2->0, since(N-2)/N^2->0. Markov's elementary inequality
then gives convergence to0 in uniform-class probability. The fixed
ln xi>0 is small but positive, which is enough for this implication.

Condition(18) is precisely upper-rate saturation. It is NOT known,
not supplied by the separate existence of the scalar limit, and not
assumed in any unconditional count statement(6)-(17). Without it, the
correct uniform probability consequence of(15), for example, is only

    Pr_unif{S_N>=s}<=min(1,
         2^(N-2)*G^E_N*e^(-s/2)/C(N)).                 (19)

A proved count lower bound could be inserted in this displayed formula;
an unknown denominator cannot be discarded. The new mechanism reduces
the possible entropy of imbalanced classes; showing that the remaining
balanced classes themselves lose positive entropy is the genuinely
missing global step. It is not proved below or by R11.

For completeness, any individual class also satisfies the pointwise
constraint

    J_N+(ln xi)D_N/2<=E_N*ln G,
    S_N+(ln xi)D_N<=2E_N*ln G+2(N-2)ln2.               (20)

This comes from its single summand in(7) and then(13). It gives a uniform
quadratic envelope for the actual directional imbalance, not the looser
bound obtained by multiplying arbitrary O(n)-degree row probabilities.

## 4. An actual hereditary arrangement and its complete directed dual

For n>=2 take the n straight lines

    L_j: y=t_j*x-t_j^2, t_j=2^(-j), j=1,...,n.         (21)

Mark the cell above every line as north. Its opposite below every line
is south. These are ACTUAL Euclidean arrangements, not merely possible
degree sequences. Each pair crosses at

    (x,y)=(t_j+t_k,t_j*t_k).

No three concur: equality of the intersections with a fixed L_j would
give t_k=t_l. In fact the pair sums are distinct by their two distinct
binary digits, although simplicity only needs the preceding argument.

The labels j in(21) are exactly the canonical labels in Felsner-Valtr's
left-boundary convention. Choose a vertical upward curve at any x0<0.
All line intersections are to its right. Since t1>t2>...>tn>0 and
t*x0-t^2 strictly decreases with t>0, the curve meets lines1,...,n from
south to north in increasing j. Thus adding line n+1 inserts the
canonical largest label, and deleting it leaves EXACTLY the same marked
family on the first n labels. The hereditary deletion chain is real.

Describe a cell by T, the set of lines lying ABOVE its points. For fixed
(x,y), the condition t*x-t^2>y is an interval condition on real t,
because the quadratic is strictly concave in t. Hence the nonempty sets
T are consecutive intervals [a,b] of the labels (decreasing t order
still preserves intervals); T=empty is the north cell.

EVERY such interval occurs. For a<b, at the intersection of its endpoint
lines the intervening lines have greater y-value, and the exterior lines
have smaller value: the difference is

    (t_j*x-t_j^2)-t_a*t_b=-(t_j-t_a)(t_j-t_b).

Move y a sufficiently small amount downward. Then exactly all lines
in[a,b] are above the chosen point. For singleton[a,a], use x=2t_a,
y=t_a^2-epsilon with epsilon smaller than all positive squared distances
(t_j-t_a)^2. The full interval is included in the same endpoint proof.
Each sign region is an intersection of open halfplanes, hence convex
and connected, so it is ONE cell, not several cells with the same T.

Two such cells are adjacent exactly when their sets differ by one
element. The necessity is immediate when crossing an arrangement edge.
For sufficiency, choose an interior point in each of the two sign
regions. Along their connecting segment every common strict inequality
remains strict; the one differing line is crossed at a point on no
other line. Thus the cells share an edge. Orienting north to south
adds one label to T. We have the COMPLETE directed dual graph:

    empty -> each singleton [a,a];
    [a,b] -> [a-1,b] if a>1;
    [a,b] -> [a,b+1] if b<n.

The full interval[1,n] is south. North has outdegree n. Every other
cell has outdegree at most2. A singleton has indegree1; every interval
of length at least2 has indegree2. Thus the reverse positive degrees
are at most2, with all zero endpoint rows handled exactly as in R11.

A complete cutpath starts at one singleton and then grows its interval
at either end. Equivalently in reverse, successively remove its left
or right endpoint until one singleton remains. There are EXACTLY n-1
binary choices and then one unique edge to north. Therefore

    #complete cutpaths=2^(n-1).                         (22)

These are actual cutpaths, not reduced reversal words or arbitrary
arrangement histories. Each increasing sign rank gives n steps.

## 5. The exact new cost on that family

Since the only possible forward degree-four tail is north when n=4,
and no reverse degree is four, EVERY complete cutpath in this parent has

    c_F=1_{n=4}, c_R=0.                                (23)

On inserting line n+1 of(21), follow that line from left to right. It
starts above all old lines and crosses them in order n,n-1,...,1, since
their intersection x-values with it are t_(n+1)+t_n, then
t_(n+1)+t_(n-1), and so on. Thus it follows the specific boundary path

    empty,[n,n],[n-1,n],...,[1,n].

Its first edge is an EXTREME of the n north exits. The ordered upper
envelope has all n lines as edges, and its two end labels1,n are the
two extremes; the complete interval graph also identifies them. Every
subsequent forward step of this path is unique. Hence

    P(p_n)=v/(n-2+2v).

In the reverse direction every interval of length>=2 has two extremes
with normalized probability1/2 for each; the final singleton step is
unique. There are n-1 binary reverse steps. In fact Q is uniform on
ALL cutpaths in this parent, and for the selected path

    Q(p_n)=2^(-(n-1)).

The common R cancels from T by(5), so exactly

    T(p_n)=(n-1)ln2+ln v-ln(n-2+2v)+1_{n=4}ln z.       (24)

All these values are nonnegative. At n2 the un-tilted ratio equals1;
its ratio at n+1 to its value at n is

    2(n-2+2v)/(n-1+2v)>1,

because n>=2 and v>1. The extra n4 tilt is positive. Therefore absolute
values introduce no hidden sign change in summing(24).

For the actual hereditary class tau_N on N lines, equations(23)-(24)
give, for N>=2,

    D_N(tau_N)=1_{N>=5},
    S_N(tau_N)=((N-2)(N-1)/2)ln2+(N-2)ln v
          -sum_(n=2)^(N-1) ln(n-2+2v)+1_{N>=5}ln z.   (25)

The logarithmic sum is O(N ln(N+1)): its terms are positive and at most
ln(N+1), using the accepted v<7/4. It is nonnegative and subquadratic.
Thus S_N/N^2->ln2/2. From(13), the difference between J_N and S_N/2
is at most(N-2)ln2; hence J_N/N^2->ln2/4. This proves(10), including
all small sizes and the exact bounded old cost. No enumeration supplied
the graph, probabilities, path count or limiting constants.

This actual family disproves an all-class positive-density D hypothesis.
It also makes S_N/(D_N+1) unbounded quadratically, so a uniform
S_N<=A D_N+o(N^2) assertion is false. In contrast, the new J-sector
bound(16) supplies a loss arbitrarily close to a quarter-bit-per-N² at
this limiting cost: for every epsilon>0 this family eventually has
J_N>=[(ln2)/4-epsilon]N². That observation concerns the sector bound;
the family itself has just one selected class per size and is not
claimed to have entropy one quarter or to exhaust low-D mass.

## 6. Genuine remaining inference and attribution

The global upper bound still follows from dropping nonnegative costs,
and remains R11's G. To improve it using(7), one needs actual information
that the near-balanced, small-J/small-D classes cannot carry entropy
arbitrarily close to that rate. Neither the existence of the scalar
limit, a formal feasible row profile, the explicit family(21), nor a
pressure identity proves such information. No total-mass or all-class
imbalance-density theorem is asserted. The new theorem is the joint
actual-class pressure, its exact entropy-budget implication, and the
actual independent-cost obstruction(10).

The arithmetic-mean/cosh and finite entropy inequalities are standard
elementary identities, fully proved here; no new-method claim is made.
Primary Felsner-Valtr was freshly read in exact marked-definition,
canonical-label, cutpath/fiber and degree/middle passages. Their deeper
dictionary foundations and R11's actual diamond/zone results retain
their separate accepted authority, not a fresh self-review by C. The
parabolic-tangent example is constructed and counted directly; no
claim that the underlying arrangement type or such examples are new
to the literature is made. No identification with the published
bubblesort example or its marking is used.

Root has no NEW construction contribution. All FR10 corresponding NEW
peer files/inventories/hashes/metadata remain unaccessed while its audits
are active. The prior R21 findings were released only after explicit
BOTH confirmation. No old/shared/Git/cache bytes, downloaded source,
mathematical code, routine scan, optimizer or test is involved.

The complete obligations/constructor checks/issues/failures/sourceMDJSON/
worklog/code record and compact integrity packet accompany this main.
It remains unverified until TWO OTHER ENTIRE WHOLE auditors independently
reconstruct EVERY step, freeze all metadata before peer access, and root
alone reconciles/promotes. Internal review is not external validation or
absolute certainty. The original annual value and effective upper
approximation remain open.
