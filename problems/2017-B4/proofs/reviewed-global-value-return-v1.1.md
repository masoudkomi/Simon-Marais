# Accepted global-value-return: exact coordinator scope

2026-10-17 UTC. **Proved, independently reviewed scoped partial result.**

V1 proves a finite invariant injection on the original orientation-distinguished full-reversal commutation classes, recording projected class, each original internal class and weak gap compositions of its fixed per-rank port lists. The kth-to-kth matching and original-label event poset recover the entire class. Summing gives C(n)<=B(m_1,...,m_D) product_i W_(m_i)(n-m_i), and balancing the degree-vector bound gives the explicit product of C(m_i) binom(n-1,m_i-1)^m_i. Invalid abstract records may be overcounted; no simultaneous realization or factorial choice is asserted. The actual prefix section gives the lower bound B<=C.

Using the already accepted ALL-integer global limits, V2 proves 0<=L-ell_D<=h2(1/D)+L/D<=h2(1/D)+U/D, U=324757/500000, with D fixed before the side-length limit. The new improvement uses U<1 and does not evaluate L or supply an effective fixed-D convergence rate. It does not circularly reprove the older global theorem used as a premise.

V3 is EXPLICITLY CONDITIONAL. Additional effective hypothesis E, a uniform computable rational bound on the balanced positive finite excess tending to zero at fixed D, supplies computable lower approximants increasing to ell_D and then L. Additional R, effective fixed-D upper approximants, yields a computable two-sided value by a terminating interval-width test. NEITHER E NOR R is proved for the actual tilings. Qualitative accepted geometric recovery is not called effective.

V4 is an ABSTRACT computable increasing integer sequence with the all-size floor-replication inequality and even zero balanced positive deficit, whose normalized logarithmic limit is noncomputable. Its direct halting-set/base-four construction disproves only the implication from those weak numerical properties to an effective value. It is not an actual tiling, GE/SFT construction or proof of noncomputability of L.

Constructor: review_2017_coarsening_r1. Fresh initially blind WHOLE nonconstructor reviewers: coordinator root and review_2022_complexity_r2, through40/48 checks covering all40 author obligations. Root's older global strategy contribution and reviewer2's older G1-G3 construction are disclosed; the separately accepted older global theorem is a premise, not independently recertified own work. Root read the COMPLETE candidate, constructor obligations/ledger/worklog/failed routes/source records, BOTH full reports, ALL ledgers and BOTH source checks. No substantive defect or required repair remained after reconciliation.

Exact official marked/orientation counts, the accepted complete DC/global/U scopes and fixed-D order are preserved. Primary Dallant/SoCG passages are bounded historical context, not new best-bound claims. The directly read Hochman-Meyerovitch strong-irreducibility theorem is not applied: an exact finite-alphabet lattice SFT identification and its mixing hypothesis are absent. The optional unread Specker scan is not a theorem premise; V4 is proved directly. No mathematical program, enumeration, old numerical certificate replay, CAS or author rerun was used. No exact value, actual computability/noncomputability, full annual solution or novelty is claimed.

The COMPLETE frozen mathematical submission follows as a byte-identical suffix. Its historical unverified label records submission status; this header and acceptance record state the current exact scope.

---

# Retaining internal classes in direction coarsening, and the effective-value gap

2026-10-17 UTC. **Candidate proof - unverified.**

Constructor: /root/review_2017_coarsening_r1. Requested model/reasoning:
gpt-6.1-sol/max; verified effective-setting readback unavailable. Two OTHER
fresh initially blind whole auditors are required before promotion. This
packet does not determine the common numerical value in official 2017 B4,
assert its computability, or claim novelty. No mathematical program,
enumeration, CAS, certificate replay or numerical experiment was run.

## 0. Domain, accepted inputs and proposed statements

The [official 2017 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-2_1.pdf),
p.2 B4, asks for the liminf and limsup of log2 C(n)/n², for every integer
n>=2. We retain its fixed-polygon, orientation-distinguished convention,
as clarified by the official notes and the accepted marked dictionary.
C(n) counts full reversal wiring words on n initially boundary-ordered
strands modulo commuting disjoint adjacent swaps. It does not count
individual reduced words or quotient by rotations/reflections. Define
C(1)=1 solely for auxiliary blocks of size one.

The exact accepted logical inputs are:

* **DC:** proofs/reviewed-direction-coarsening-v1.1.md. For consecutive
  initial color blocks of positive sizes m_1,...,m_D, sum n, smoothing
  equal-color crossings defines a projection to the full block-reversal
  commutation classes B(m_1,...,m_D), with a section. Its canonical
  directed rank tracks, ordered ports/neighbor bits, forced matching and
  event-poset reconstruction give an invariant injective code. DC also
  supplies coordinatewise monotonicity of the full B counts.
* **G1–G3:** proofs/reviewed-allD-global-v1.1.md, in its accepted scope
  relative to its ten exact local interfaces. For each fixed D>=2, the
  full balanced limit k_D=lim_p p^(-2) log2 B_D(p) exists at ALL integer
  p, where B_D(p)=B(p,...,p), and ell_D=k_D/D². The official scalar limit
  L=lim_n n^(-2)log2 C(n) exists, ell_D<=L, and ell_D->L. G1's uniform
  dilation deficit is stated below only on its actual GE class. There
  is no imported effective convergence rate, general variational
  formula, sufficient-profile theorem or global chart assertion.
* **U:** proofs/reviewed-concavity-v1.1.md supplies the accepted strict
  upper bound L<U=324757/500000=0.649514. Its source certificate is not
  replayed. Its historical construction-stage labels are superseded by
  that document's acceptance header.

The new proposed results are as follows. All logarithms are base two.

**V1 (finite internal-class code).** For an integer m>=1, a>=0 and a full
m-strand reversal commutation class A, smooth ALL its crossings. Name
the resulting noncrossing rank tracks r=1,...,m. Let k_r(A) be the number
of crossing ports on track r. Define the finite positive integer

    W_m(a)=sum_(A in C(m)) product_(r=1)^m binom(a+k_r(A),k_r(A)).

Here A in C(m) means that A ranges over the set counted by C(m), not
over reduced words. Then for every partition above, including D=1,2,

    B(m_1,...,m_D) <= C(n)
      <= B(m_1,...,m_D) product_i W_(m_i)(n-m_i)           (V1a)
      <= B(m_1,...,m_D)
           product_i [C(m_i) binom(n-1,m_i-1)^(m_i)].     (V1b)

The weighted expression is a finite structural upper bound; no limit
or closed evaluation of W_m(a) is asserted.

**V2 (sharper fixed-D direction error).** For every fixed D>=3,

    ell_D <= L <= [D/(D-1)] [ell_D+h_2(1/D)],             (V2a)
    0 <= L-ell_D <= h_2(1/D)+U/D.                       (V2b)

In particular the explicit additive 1/D in the accepted DC2/G3 error
can be replaced by U/D, using the separately accepted bound U<1.
This is control of the subsequent direction limit D->infinity. It
does not give a rate for p->infinity in any one fixed D.

**V3 (conditional effective-value bridge).** A computable one-sided
balanced deficit envelope, explicitly specified in section3, would
make ell_D uniformly left semicomputable and L left semicomputable.
If one ALSO has uniformly computable upper approximants converging to
each ell_D, L is computable. Neither extra effective hypothesis is
established here. Effective upper control of the accepted deficit alone
does not supply the upper approximants.

**V4 (exact abstract obstruction to a rate inference).** There is a
computable nondecreasing positive integer sequence A(n), bounded by
2^(n²/3), such that

    A(m)>=A(l)^(floor(m/l)²) for all positive integers m,l,
    lim_n log2 A(n)/n² exists and is not computable,
    max(0,log2 A(r)-liminf_M M^(-2)log2 A(Mr))=0 for EVERY r.

This is an abstract count sequence, not a tiling construction, not a
counterexample to the accepted geometric theorems, and not a proof that
the actual L is noncomputable.

## 1. The finite internal-class code

### 1.1 Restrict before smoothing

Take a representative full reversal wiring diagram T on n labels.
Fix one of the initial consecutive blocks i. Delete all original
strands whose labels are outside that block, keeping the crossings
of the remaining original strands. Compress the vertical positions
only to read an adjacent-swap word on m_i strands.

At an internal crossing the two original strands were adjacent in the
full current order, so they are adjacent after the other strands are
deleted. Every internal label pair crosses exactly once, and their
final order is reversed. The restriction therefore has binom(m_i,2)
events and is a reduced full reversal word. Call its class A_i.

This restriction is well defined on full commutation classes. An
original allowed commutation exchanges two events on disjoint current
position intervals. If neither or only one event survives, the two
restricted words coincide. If both survive in the same block, their
four labels are distinct and ordered in disjoint adjacent pairs in
the restricted list. Their restricted generators therefore commute.
These are all possibilities for this fixed block. Thus A_i does not
depend on a chosen full sweep representative. There is no extra
choice of internal labels: their initial boundary order is retained.

### 1.2 What an internal class already records

In a reversal class A on m strands, smooth every crossing using the
order-preserving, noncrossing smoothing. The resulting directed tracks
are named by rank r=1,...,m. At a former crossing between the current
ranks j and j+1 there is a port on each track. Give its port the symbol
+ on j and - on j+1. Thus a symbol indicates the adjacent same-color
rank on which its partner lies. End ranks have only their available
neighbor symbol.

The directed symbol list on every rank track is an invariant of A.
Indeed an allowed word commutation uses generators at indices j,k
with |j-k|>1. The two events use disjoint rank pairs; interchanging
them changes no order on any one rank track and no symbol. In
particular k_r(A), the length of this list, is invariant and

    sum_(r=1)^m k_r(A)=2 binom(m,2)=m(m-1).              (1)

No arbitrary linear extension of all internal events is selected.
The port lists are per-track orders, which are exactly the data used
in DC's canonical code.

Now smooth the equal-color crossings of T to obtain its projected
block-reversal class P(T). Within any one color, smoothing preserves
current order, so the smoothed rank r is fixed along its whole track.
Deleting other colors does not change this same-color order. Therefore
the full directed list of equal-color port symbols on track (i,r),
after one forgets all retained other-color vertices, is EXACTLY the
list supplied by A_i in the preceding paragraph. This identification
includes the first/last portions of the tracks and all repeated
contacts between the same neighboring ranks.

### 1.3 Only the port placements remain

Fix a projected class Q counted by B(m_1,...,m_D), and fix A_1,...,A_D.
In Q, each track of color i crosses every other-color track exactly
once. There are n-m_i such tracks. Its retained vertices have a
canonical directed order and are named by the identities of their
two projected tracks. Consequently track (i,r) has exactly

    g_i=n-m_i+1                                           (2)

canonical gaps, including its two endpoint gaps (one gap if n=m_i).
This number does not depend on r or on the class Q.

Distribute the k_r(A_i) ports among these ordered gaps, recording
only their nonnegative counts. Fill the gaps, in their directed order,
with the already known symbol list from A_i. The number of possible
gap-count lists is the weak-composition number

    binom(k_r(A_i)+g_i-1,k_r(A_i))
       =binom(n-m_i+k_r(A_i),k_r(A_i)).                 (3)

Multiple ports within a single gap require no further permutation:
their relative order is the fixed order in that track's symbol list.
They may be separated by arbitrarily small geometric distances in a
representative; metric positions are not data in a commutation class.

This recovers DC's entire decorated projected diagram. For clarity,
its reconstruction is as follows. For each neighboring pair of
same-color ranks, list all ports pointing toward the other rank.
The kth such port on one track pairs with the kth on the other. In
an actual monotone diagram both endpoints of one contact have the
same sweep time; the contact orders on the two tracks agree. Thus
matching is forced even when there are multiple contacts. Cross-route
at restored internal contacts and retain the original routing at
retained other-color crossings. Following the initial labels then
recovers every original strand and its event order. The event poset
generated by these strand orders determines the original commutation
class: linear extensions differ by swaps of incomparable events,
which use disjoint current label pairs and hence commute.

The accepted DC proof establishes invariance of this complete
decorated diagram under original commutations, not merely invariance
of Q. Our gap counts are part of that decoration. Section1.1 also
establishes invariance of the added internal class records A_i.
Their combination is therefore a well-defined injective code on
original commutation classes. It records neither a hidden global
event order nor planar metric coordinates. Some choices of A_i and
gap counts can be inconsistent with Q; counting such invalid codes
only enlarges the upper bound. No assertion that arbitrary internal
and projected classes admit a simultaneous lifting is used.

For each Q, summing (3) over each internal class independently bounds
its fiber by product_i W_(m_i)(n-m_i). There are B(m_1,...,m_D) choices
for Q. The lower bound is the accepted DC section. This proves (V1a).

### 1.4 A discrete log-concavity simplification

For a>=0 an integer put F_a(k)=binom(a+k,k), k>=0. For u>=v+2,

    F_a(u-1)F_a(v+1) / [F_a(u)F_a(v)]
      = [u/(a+u)] [(a+v+1)/(v+1)] >=1,                 (4)

because the numerator minus denominator after cross multiplication
is a(u-v-1)>=0. All denominators in (4) are positive. This includes
a=0, when every F_0(k)=1.

For any nonnegative integer tuple k_1,...,k_m of sum m(m-1), replace
two entries u>=v+2 by u-1,v+1. This does not decrease product F_a(k_r)
and strictly decreases sum k_r². Repetition terminates with all
entries differing by at most one. Their mean is the integer m-1, so
every final entry equals m-1. Applying this to (1) gives

    product_r binom(a+k_r(A),k_r(A))
        <=binom(a+m-1,m-1)^m.                          (5)

Summing (5) over the C(m) classes and setting a=n-m proves (V1b).
When m=1 the one list is empty and both sides of (5) are one.

All endpoint conventions are explicit. D=1 gives B(n)=1 and
W_n(0)=C(n), so (V1a) is equality. If D=n and every m_i=1, all
W_1(n-1)=1 and B(1,...,1)=C(n), again equality. The natural n=1
auxiliary extension also gives equality with binom(0,0)=1. Empty
blocks and n=0 are not part of the statement. No assertion that
(V1b) is pointwise smaller than the old DC1 finite bound for every
finite partition is made.

## 2. Normalize at fixed D, then increase D

Fix D>=3. For large n take m_i in{p,p+1}, p=floor(n/D), summing to n.
Accepted coordinatewise monotonicity gives

    B_D(p)<=B(m_1,...,m_D)<=B_D(p+1).

G2, with the normalization ratios (Dp/n)² and (D(p+1)/n)² both
tending to one, therefore gives

    n^(-2)log2 B(m_1,...,m_D) ->ell_D.                  (6)

Each m_i->infinity and m_i/n->1/D. The accepted official limit gives

    n^(-2)sum_i log2 C(m_i)
      =sum_i (m_i/n)² [log2 C(m_i)/m_i²] ->L/D.        (7)

For N>=1 and 0<=k<=N the elementary binomial entropy inequality is
log2 binom(N,k)<=N h_2(k/N), including its zero endpoints. Thus

    n^(-2)sum_i m_i log2 binom(n-1,m_i-1)
      <=[(n-1)/n] sum_i (m_i/n) h_2((m_i-1)/(n-1))
       ->h_2(1/D).                                    (8)

Take the limsup of the upper bound (V1b), using (6)–(8) and
n^(-2)log2 C(n)->L. It follows that

    0<=L-ell_D<=h_2(1/D)+L/D.                           (9)

The left inequality follows already from B<=C. Rearranging (9) is
legal since D>1 and gives (V2a). Substituting the separate accepted
L<U gives (V2b), even with strict inequality on its last upper bound.
Since U<1, the stated additive direction error is strictly smaller
than the older h_2(1/D)+1/D bound. The dominant order remains
O((log D)/D). This supplies no new numerical upper bound on L by
itself, because ell_D is unevaluated.

There is no exchange of the D and n or p limits. In particular one
cannot choose D=D(n) in this proof and use G2 as if it supplied a
uniform side-length threshold. The new finite inequality holds at
all finite partitions, but the passage (6)–(8) is at a fixed D.

## 3. A precise conditional computability bridge

### 3.1 Exact finite counts are computable in principle

For fixed D,p the block-reversal permutation on Dp labels has
K=binom(D,2)p² inversions. Enumerate the finitely many adjacent-swap
words of length K, retain those with the prescribed target
permutation, and form the finite graph joining words differing by
one adjacent commutation of disjoint generators. The number of
components is B_D(p). A retained K-letter word is reduced because
its target permutation has exactly K inversions. The same finite
procedure for a full reversal computes C(n). This is a terminating
algorithm argument, not a proposed efficient scan or a scan performed
here. It asserts no practical time bound.

The base-two logarithm of a positive integer is uniformly computable.
For example dyadic lower bounds for log2 N /r² can be found by
comparing the integers N^(2^t) and 2^(j r²). Equality is resolved by
the same integer comparison. We may therefore choose uniformly
computable dyadic d(D,r,t) with

    d(D,r,t)<=a_D(r):=r^(-2)log2 B_D(r),
    0<=a_D(r)-d(D,r,t)<2^(-t),                          (10)

and d nondecreasing in t. No logarithm oracle is assumed.

### 3.2 What an effective deficit envelope would supply

For each D>=3 choose the computable integer C_D=D(D+1). With
v_i=(1,i-1), the full balanced zonogon has perimeter
2r sum_i||v_i||<=C_D r and contents r<=C_D r. Its empty exterior
makes it an actual member of GE_(D,C_D)(r), with the same boundary
for every filling; the perimeter bound uses ||(1,i-1)||<=i.
G1's notation is

    Lambda_D(B)=liminf_M M^(-2)log2 Z_D(MB),
    Delta_D(B)=max(0,log2 Z_D(B)-Lambda_D(B)),
    eta_D(r)=sup_(B in GE_(D,C_D)(r)) Delta_D(B)/r² ->0.

For this full boundary B_r, G2 along ALL multiples of the fixed r
gives exactly

    Lambda_D(B_r)=r² k_D,
    Delta_D(B_r)/r²=max(0,a_D(r)-k_D)<=eta_D(r).         (11)

Introduce the following EXTRA hypothesis, not a conclusion of the
accepted qualitative convergence theorem or of this packet:

**(E)** There is one total algorithm producing rational epsilon(D,r)
for every D>=3,r>=1 such that

    epsilon(D,r)>=max(0,a_D(r)-k_D),
    epsilon(D,r)>=0,  epsilon(D,r)->0 for each fixed D.  (12)

A uniformly computable rational upper envelope of eta_D(r) tending
to zero would imply (E), by (11). The weaker balanced form (12) is
all that the following argument needs. No rate of the convergence
of epsilon itself is required for this one-sided assertion.

By (10),(12), each

    b(D,s)=D^(-2) max(0,max_(1<=r<=s)
                         [d(D,r,s)-epsilon(D,r)])      (13)

is a computable rational <=ell_D. It is nondecreasing in s. For a
fixed D, a_D(r)->k_D and epsilon(D,r)->0; first choose a large fixed
r and then let s>=r grow in (10). This proves b(D,s)->ell_D.
Thus (E) makes ell_D uniformly left semicomputable. Since all
ell_D<=L and ell_D->L, the computable nondecreasing sequence

    max_(3<=D<=s) b(D,s), s>=3,

is <=L and tends to L. This proves the first conditional part of V3.

The upper envelope in (12) bounds finite a_D(r) from ABOVE RELATIVE
to k_D, so rearrangement gives a LOWER bound for k_D. It supplies no
corresponding computable upper sequence for k_D. Reversing this
inequality would be an error. Section4 shows that even an identically
zero analogous deficit can coexist with a noncomputable limit.

### 3.3 A second, sufficient effective hypothesis

In addition to (E), suppose:

**(R)** A total algorithm outputs rational u(D,s)>=ell_D for every
D>=3,s>=1, with u(D,s)->ell_D at each fixed D.

Then L is computable. Here are all choices in an approximation
algorithm, without assuming a hidden convergence modulus. Given a
positive rational accuracy delta, choose j>=2 so

    (j+3)/2^j <delta/4,  and set D=2^j.                 (14)

For x=1/D, the elementary bound
-(1-x)ln(1-x)<=x gives h_2(1/D)<=(j+2)/D, using ln2>1/2.
Hence even the OLD accepted G3 error obeys

    0<=L-ell_D<=h_2(1/D)+1/D<=(j+3)/2^j.               (15)

The smaller error from V2 could be used, but is unnecessary for
this conditional reduction. Compute b(D,s),u(D,s) until their
gap is less than delta/4. The search halts because both converge
to ell_D and b(D,s)<=ell_D<=u(D,s). We have the verified interval

    b(D,s)<=L<=u(D,s)+(j+3)/2^j                         (16)

of width less than delta/2. Its rational midpoint approximates L
within delta. The search uses no assumed p-convergence rate.

Neither (E) nor (R) is proved here. Computability of every finite
B_D(r), existence of k_D, and the computable D-error alone do not
provide the needed two-sided pair of effective approximants. A
separate verified free-boundary/SFT entropy identification might
furnish some upper bounds, but has not been supplied. The lattice
SFT computability theorems of Hochman–Meyerovitch have hypotheses
distinct from fixed zonogon counts; see the source checks.

## 4. Exact obstruction to extracting an effective rate by analogy

Let K be a recursively enumerable, undecidable halting set, indexed
by e=0,1,...; for example e belongs when the eth program halts on
input e. The usual diagonal proof rules out a total decider: the
program that halts exactly when that putative decider predicts
nonhalting contradicts its prediction on its own index.

Define

    alpha=sum_(e in K) 4^(-(e+1)),
    alpha_n=sum_(0<=e<=n, program e halts on e within n steps)
                                            4^(-(e+1)). (17)

Each alpha_n is a computable nonnegative rational, the sequence is
nondecreasing, and alpha_n->alpha<=sum_(e>=0)4^(-(e+1))=1/3.
For convergence, fix a finite index cutoff; all halting programs below
it are eventually included, and the remaining geometric tail is
arbitrarily small when that cutoff grows.
The limit alpha is not computable. Indeed suppose it were. Having
already decided the membership of indices smaller than e, subtract
their known weights from alpha and put w_e=4^(-(e+1)). If e is in
K, the residual is >=w_e; if it is not, that residual is at most
sum_(f>e)4^(-(f+1))=w_e/3. An approximation to alpha within w_e/6
distinguishes the cases by the threshold 2w_e/3. This inductively
decides K, a contradiction. The separated base-four digit weights
avoid any binary-expansion ambiguity.

Set, for every positive integer n,

    A(n)=2^(floor(n² alpha_n)).                         (18)

This is a computable positive integer; no halting oracle is used,
since only finitely many programs are simulated for n steps in
alpha_n. It is nondecreasing, A(1)=1, and

    1<=A(n)<=2^(n²/3).

For positive m,l put k=floor(m/l). If m<l, k=0 and the replication
inequality A(m)>=A(l)^0=1 is automatic. Otherwise alpha_m>=alpha_l
and m²>=k² l², so

    floor(m² alpha_m)
      >=floor(k² l² alpha_l)
      >=k² floor(l² alpha_l).

Exponentiating proves A(m)>=A(l)^(floor(m/l)²), for ALL m,l,
including the exact square-grid inequality A(Mr)>=A(r)^(M²).
Nevertheless

    0<=alpha-log2 A(n)/n²
           <=alpha-alpha_n+1/n² ->0,                   (19)

so the quadratic entropy limit is the noncomputable alpha.
For a fixed positive r, the subsequence Mr in (19) gives

    liminf_M M^(-2)log2 A(Mr)=r² alpha.

Since log2 A(r)<=r² alpha_r<=r² alpha, the positive part of the
finite-count-minus-dilation-limit difference is ZERO at every r.
The hypothetical balanced envelope in this abstract example is
therefore the exactly computable constant zero. Its finite
normalized counts are all <=alpha and converge to it; they need not
be monotone. This supplies no upper semicomputation: such an upper
sequence, together with alpha_n, would compute alpha by a terminating
interval-width search, contrary to its proved noncomputability.

This elementary halting-set construction is a standard kind of
computability obstruction, not a claimed new recursion-theoretic
method. It establishes only that computable finite counts,
quadratic exponential bounds, monotonicity, exact quadratic
replication, and even zero balanced dilation deficit do not by
themselves imply an effective entropy value or convergence rate.
No GE disks, prescribed colored boundaries, partial-cube graph,
SFT coding or actual pseudoline arrangement family is constructed
by (18). It does not refute computability of L, establish that
the global geometric proof cannot be made effective, or replace
any missing theorem about that geometry.

## 5. Exact remaining mathematical tasks

The proposed finite V1 code and V2 consequence have complete author
proofs above but remain unverified pending two whole audits. The
conditional V3 and abstract V4 are also proposed lemmas requiring
those audits. No new numerical estimate of L is obtained because
ell_D is still unevaluated. The weighted W_m(a) retains genuine
within-block structure; estimating it sharply would require more
than the mean port count used in (5).

For an actual computability theorem one useful sufficient target
is the pair (E),(R), or a different verified two-sided finite
certificate scheme for ell_D. The accepted compactness/Vitali
argument does not presently come with an algorithm producing
those certificates. An effective realization/gluing theorem that
identifies the relevant fixed-boundary entropy with a computable
mixing model could also help, but it must preserve boundary flux,
the correct normalization, and both entropy inequalities. Neither
general free-boundary SFT entropy nor one periodic patch entropy
can be substituted for this obligation.

Failed inferences and source/read limits are preserved in the
companion worklog and source checks. All earlier construction and
review bytes are immutable. This packet is a partial value-research
checkpoint, not a complete annual solution or a priority assertion.


