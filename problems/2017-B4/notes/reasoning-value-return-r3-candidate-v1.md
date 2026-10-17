# Ordered contact heaps and a smaller direction-entropy error

2026-10-17 UTC. **Candidate proof - unverified.** Constructor
`/root/review_2021_reasoning_j15_r2`. Requested gpt-6.1-sol/max;
independently verified effective settings unknown. TWO OTHER fresh
initially blind WHOLE nonconstructor audits are required. Only the
coordinator may promote the exact result after reconciliation.

This is a finite weighted-count refinement and a new proposed constraint
on the unknown direction entropies. It does not determine the official
2017 value, prove computability or an effective side-length convergence
rate, or assert novelty. No mathematical program, CAS, enumeration,
numerical optimization, old certificate replay or author rerun was used.

## 0. Official objects, exact accepted premises and attribution

The official count C(n), n>=2, is the count of tilings in the fixed
regular 2n-gon, with orientations distinguished. Use the accepted marked
dictionary: C(n) is the number of full-reversal adjacent-swap words on
n boundary-ordered labels MODULO commutations of disjoint swaps. We
never substitute the number of individual words or sweep histories.
C(1)=1 is auxiliary. Empty original polygons and n=0 are excluded.

For D consecutive NONEMPTY initial color blocks of sizes m_i, sum n,
write B(m_1,...,m_D) for full block reversal with internal color order
preserved. Every sum over internal A below is over the ACTUAL C(m)
commutation classes, each once. All logarithms are base two.

The complete accepted bodies and scope/acceptance records were read:

* **DC:** `proofs/reviewed-direction-coarsening-v1.1.md`. Equal-color
  smoothing defines the canonical projected class Q. Directed projected
  rank tracks and gaps are invariant. Complete ordered contact ports,
  forced neighbor kth matching and original-strand orders recover the
  original commutation class. A section gives B<=C. Invalid abstract
  records may be overcounted for an upper bound.
* **G:** `proofs/reviewed-allD-global-v1.1.md`. At EACH fixed D>=2,
  k_D=lim_p p^-2 log B(p,...,p) exists at ALL integers p, and
  ell_D=k_D/D^2. The official scalar limit L exists, ell_D<=L and
  ell_D->L. Its exact GE theorem and ten local interfaces retain their
  accepted scopes. No effective p-modulus, variational formula, mixing
  theorem, arbitrary-profile realization or uniform growing-D assertion
  is imported. Its elementary two-color grid is unique.
* **V and OP:** the COMPLETE accepted global-value-return v1.1 and r2
  v1.1 bodies. The internal restriction class A_i fixes the WHOLE ordered
  list of contacts on each smoothed same-color rank. OP1 forces the two
  ends of every erased contact to have the SAME canonical external gap
  index. The stronger common-prefix SET condition remains necessary
  only. The accepted code and its order information are not discarded.
* **U:** `proofs/reviewed-concavity-v1.1.md`, solely for the separately
  accepted L<U=324757/500000. Its old numerical certificate is not run.

I constructed the older all-D strict LOCAL packet and reviewed the new
global G assembly and several older local packets. Those roles do not
independently recertify their accepted proofs. I did not construct the
accepted V/OP returns. The present heap code, alternating-chain count
and entropy consequence are a NEW construction requiring other auditors.
The coordinator's broad research assignment supplied none of these new
proof inferences. Older candidate/review/accepted bytes remain intact.

Heaps for commutation classes, finite-poset order polynomials and
projection-to-generalized-partitions are established literature. The
source packet records actual primary passages of Destainville–Mosseri–
Bailly and Stanley, and the precise heap exposition read. Their general
framework is attributed, not claimed new. The needed finite special
bijection and all new inequalities are proved below without importing an
unchecked arbitrary-codimension theorem. This also avoids using a source
count of maximal walks as a count of tilings.

## 1. Definitions and complete proposed statements

Put F_a(k)=binom(a+k,k) for integers a,k>=0. For an internal class A
on m>=1 labels, its contact events are the occurrences of generators
s_1,...,s_(m-1). Name an event by (r,l), the lth occurrence of s_r;
occurrences of the same generator never commute past each other.
Let x_r(A) be their number, and put x_0=x_m=0. Define the finite
poset P_A by ordering two events as in a representative whenever their
generator indices differ by at most one, and taking transitive closure.
Its size is K_m=binom(m,2). It is empty for m=1.

Write

    Omega_A(a+1)=#{f:P_A->{0,...,a}: e<=e' implies f(e)<=f(e')},
    H_m(a)=sum_(A in C(m)) Omega_A(a+1).                 (1)

The notation Omega is the classical WEAK order polynomial, with the
argument shifted by one. The count definition (1), including a=0 and
the empty poset, is sufficient for all proofs here. No unrestricted
infinite-volume pressure or polynomial equation for L is inferred.

Choose a set of internal RANK TRACKS

    I_(2t)={1,3,...,2t-1},                    t>=1,
    I_(2t+1)={2,4,...,2t},                    t>=0.

Thus q_m=|I_m|=floor(m/2). Every neighboring pair r,r+1 contains
EXACTLY one selected rank. Set

    k_r(A)=x_(r-1)(A)+x_r(A),
    T_m(a)=sum_(A in C(m)) product_(r in I_m) F_a(k_r(A)),
    T_1(a)=1.                                           (2)

The accepted old one-sided weight is

    V_m(a)=sum_(A in C(m)) product_(r=1)^(m-1) F_a(x_r(A)).

**HC1 (exact finite heap capacity and invariant upper code).** H_m(a)
is EXACTLY the actual commutation-class count

    H_m(a)=B(1,...,1,a)      (m singleton blocks, a>0),
    H_m(0)=C(m).                                        (3)

Here the a=0 block is omitted. Equivalently the target permutation on
m+a labels has final list m+1,...,m+a,m,m-1,...,1. For EVERY consecutive
positive block partition,

    B(m_1,...,m_D)<=C(n)
       <=B(m_1,...,m_D) product_i H_(m_i)(n-m_i).        (4)

This is an upper bound on fibers over a general Q, not an equality
for every such fiber or a sufficient common-prefix gluing theorem.

**HC2 (alternating chains, weighted SUM and finite closed bounds).**
For all m>=1,a>=0,

    C(m)<=H_m(a)<=T_m(a)<=V_m(a).                        (5)

If a>0, H_m(a)<T_m(a) for m>=4, whereas H_m=T_m for m<=3.
If a>0 and m>=3, T_m(a)<V_m(a). These are finite comparisons of
actual-class weighted SUMS; they do not choose a typical class.

For m>=2 put d_m=m-1 if m is even, and d_m=m if m is odd. Then

    T_m(a)<=C(m) F_a(d_m)^(q_m).                         (6)

Use the value one for m=1. For a partition in (4), put

    S=sum_i binom(m_i,2),
    E_*=sum_i floor(m_i/2)(n-m_i+1),
    J_*=1 if S=0, and binom(E_*+S-1,S) if S>0.

There is the separate convenient global upper bound

    C(n)<=B(m_1,...,m_D) [product_i C(m_i)] J_*.         (7)

It counts contact placements on about half the internal rank tracks,
with all internal classes and mixed-neighbor orders retained.

**HC3 (new direction-entropy constraint).** For EVERY fixed D>=2,

    g_D=(1/2)h_2(1/D),
    0<=L-ell_D<=g_D+L/D<=g_D+U/D,
    L<=[D/(D-1)](ell_D+g_D).                           (8)

The accepted OP error uses
f_D=(1-1/(2D))h_2(1/(2D-1)). Here

    g_D<f_D for EVERY D>=2,
    D(f_D-g_D)->1/2.                                   (9)

The leading logarithmic order remains (log2 D)/(2D); it is NOT halved
again. This improves the lower-order direction error. Neither the fixed-D
values ell_D nor L are evaluated, and the effective E/R gap stays open.

## 2. The actual commutation heap and its contact orders

Take one representative word of A. The stated generating relations for
P_A all go forward in that word, so they have no cycle. They do not
depend on the representative: a commutation exchanges only two indices
at distance greater than one. It changes neither the order of two
noncommuting events nor the occurrence number of one generator. Event
names and the transitive closure are therefore class invariant.

Every representative is a linear extension of P_A. Conversely linear
extensions of a finite poset are connected by swapping adjacent
incomparable elements. One direct proof brings the first desired element
to the front through preceding incomparable elements, then inducts on
the remaining elements. In P_A, incomparable events have generator
indices differing by MORE than one. Their generators commute, so every
such extension gives a representative of the SAME A. There is no braid
move, change of internal class, new event labeling or count of all linear
extensions being substituted for C(m).

After smoothing all internal events, an event s_r is incident to rank
tracks r and r+1. The directed list of its contact IDs on rank r contains
exactly the events of indices r-1,r, in their representative order.
Every pair on that list has index difference at most one and is therefore
comparable. Conversely each generating relation of P_A is an order on a
shared rank track: indices r,r share both, and indices r,r+1 share rank
r+1. Thus P_A is exactly the transitive closure of these directed
rank-track contact orders. This identifies the order used in (1) with
the actual internal data of V/OP, rather than an unrelated word poset.

For an actual original T over projected Q, let f(e) be the common gap
index of the two ends of the internal contact e; OP1 supplies its
equality. Along each directed projected track the number of already
crossed external tracks is nondecreasing. Hence f is nondecreasing on
every rank-track list and therefore on P_A. Its values lie in 0,...,a,
where a=n-m for this block.

Knowing Q, A and this f locates both ends of every contact in named
canonical gaps. Within each track A already supplies the complete ordered
ID list, including contacts to BOTH neighbors and several contacts with
the same gap index. Filling those lists gives the full accepted DC port
decoration. Its forced matching and original-strand event orders recover
the original class. Opposite neighbor contacts in a gap do not acquire
an extra shuffle or factorial factor. Abstract f can violate other Q
constraints; that causes overcounting only.

This gives an invariant injective record on original classes consisting
of Q and (A_i,f_i) for all blocks. Summing over ACTUAL internal A_i and
their finite isotone maps gives (4)'s upper bound. The lower bound is
the accepted DC section. This proves the coding part of HC1.

## 3. Exact realization for one exterior parallel bundle

For a>0, color the first m labels with one provisional color A and
the last a labels with a color B. The full two-color block-reversal
class Q_(m,a) is unique: its tiling is the m-by-a parallelogram grid.
Every A-rank track crosses the B tracks in the same order B_1,...,B_a.
All prefix sets and all corresponding gap indices agree across A ranks.

Now distinguish the m A labels, allowing their full internal reversal,
but continue to forbid B–B crossings. The resulting actual count is
B(1,...,1,a). Internal restriction and common contact gap indices give
an injective map from these classes to the pairs (A,f) in (1), by
section 2. There is no B internal class to record.

Every such (A,f) is realizable. Since f is weakly isotone, choose a
linear extension of P_A which reads its f values in nondecreasing order:
first order equal-value subposets arbitrarily, then concatenate the
levels. No relation points from a larger value to a smaller one, so
this is indeed an extension and gives a representative of A.

Begin with the current list

    A_1 ... A_m B_1 ... B_a.

At stage j=0,...,a, perform all internal A events whose f value is j,
in the just-chosen order. Immediately before stage j, the current list
has the form

    B_1 ... B_j [the contiguous current A block] B_(j+1) ... B_a.

This holds initially. Internal A swaps do not change this form. If j<a,
bubble B_(j+1), the first unprocessed B label, left across the ENTIRE A
block, with its m successive adjacent swaps, and stop immediately after
B_j. The form then holds for j+1. No B labels are crossed with each
other, and the current A order is unchanged by the completed bubble.

The restriction of the full word to A is the chosen representative
of A, so the final A order is reversed. Each A–B pair crosses exactly
once; no B–B pair crosses. The total length is K_m+ma, exactly the
inversion number of the prescribed final permutation, so the word is
reduced and gives an actual class counted by B(1,...,1,a).

At an internal contact of stage j, EVERY smoothed A-rank track has
already crossed exactly B_1,...,B_j. Thus its common canonical gap
index is the prescribed f(e)=j. The internal record is also the chosen
A. The preceding injectivity shows that choices of extension inside
one level lead to the SAME class, and that different (A,f) give distinct
classes. This establishes surjectivity onto the record set and (3).

At a=0, every event has the single value 0, and this construction is
just a representative of A; hence H_m(0)=C(m). At m=1 the heap is
empty and the two-color grid is unique, so H_1(a)=1 for all a>=0.
At a=1 all m+1 original labels are distinguished, and (3) specializes
to H_m(1)=C(m+1). None of these observations extrapolates from a test.

This exact special realization does NOT extend to arbitrary projected
Q. The accepted OP small example with an internal block of size two
and two outside singleton colors has only two allowed contact gaps,
while H_2(2)=3. That counterexample remains intact. The staged proof
works because Q_(m,a) is the fixed two-color grid, not because necessary
prefix-set equalities have become sufficient in general.

## 4. Alternate tracks give a disjoint chain partition

Each event between neighboring ranks r,r+1 has exactly one end in I_m.
Assign the event to that selected rank. Its assigned list is a chain
of length k_r(A)=x_(r-1)+x_r. These chains are disjoint and partition
ALL K_m events, including both signs of contacts on a selected track.
In particular

    sum_(r in I_m) k_r(A)=K_m.                         (10)

A weakly increasing list of k values in 0,...,a has exactly F_a(k)
possibilities. Restricting an isotone f to the selected chains is
injective, because every event appears once. Forgetting comparabilities
BETWEEN chains therefore gives

    Omega_A(a+1)<=product_(r in I_m) F_a(k_r(A)).        (11)

Sum (11) over actual A to get H_m<=T_m. Constant maps, or the actual
one-bundle section, give H_m>=C(m). This proves the first part of (5).

There is a genuine retained order constraint beyond the chain product.
Every generator s_r occurs in a full reversal: otherwise the set of
labels on the first r positions never changes, contrary to the final
reversal. For even m>=4, events of indices 1 and 2 are in different
selected chains (ranks 1 and 3), but are comparable in P_A. For odd
m>=5 use indices 2 and 3, in selected chains 2 and 4. Choose one such
ordered pair e<e'. Put the constant value a on the chain containing e
and 0 on the chain containing e', and 0 on every other chain. If a>0
this is increasing within each selected chain but violates f(e)<=f(e').
Consequently (11) is STRICT for every A in these ranges, giving H<T
after summation. For m<=3 there is at most one selected chain, so it
is the entire heap, and equality H=T holds.

To compare with the old OP SUM, note that the selected degrees k_r
group all x_1,...,x_(m-1) into disjoint singletons or neighboring pairs.
For nonnegative u,v,

    F_a(u+v)<=F_a(u)F_a(v).                            (12)

Indeed F_a(k+1)/F_a(k)=(a+k+1)/(k+1) decreases with k; multiply v
successive ratios starting at u and compare with those starting at 0.
The inequality is strict when a,u,v are all positive. Full reversal
uses every generator; for m>=3 at least one grouped pair has two
positive x values. Applying (12) to each group proves T_m<=V_m,
strict for a>0,m>=3, exactly as asserted. This changes the record,
rather than assuming internal degree vectors are atypical or unbalanced.

The empty m=1 heap and a=0 give equality throughout (5). For m=2,
H=T=V=a+1. For m=3 the two internal classes both have a three-event
chain, giving H=T=2 binom(a+3,3). This is a hand endpoint identity,
not an enumerated certificate or an asymptotic assertion.

## 5. Two finite upper bounds without losing reconstruction

The discrete log-concavity used in the accepted OP proof gives, for
u>=v+2 and a>=0,

    F_a(u-1)F_a(v+1)/[F_a(u)F_a(v)]
      =[u/(a+u)] [(a+v+1)/(v+1)]>=1,                 (13)

since cross multiplication leaves a(u-v-1)>=0. Denominators are
positive, including a=0. Balance the q_m selected degrees in (10).
Their mean is the integer d_m: K_(2t)=t(2t-1) and
K_(2t+1)=t(2t+1). Successive balancing terminates by decreasing the
sum of their squares and never decreases the product. It ends at
all degrees d_m. Therefore each product in (2) is at most
F_a(d_m)^q_m. Summing proves (6), including all odd m. No assertion
that the balanced tuple is realized or has typical weighted mass is used.

There is also a direct invariant sparse code proving (7). Fix Q and
all internal A_i. Record the gap counts of the already ordered contact
ID list on ONLY the selected tracks of each color. There are E_* named
gaps, endpoint gaps included, and exactly S recorded contacts, since
each internal contact occurs on exactly one selected track. The total
record is a weak composition of S into E_* parts. The individual track
totals are fixed by A_i, but forgetting these totals only enlarges the
possible arrays to binom(E_*+S-1,S).

Fill selected-track gaps with their fixed lists. For each contact put
its unrecorded partner in the SAME gap index on its neighboring track,
using OP1. A_i supplies the merged order of all its contacts on that
unselected track. This reconstructs every port, including contacts to
two different selected neighbors in a single gap; no ordering choice
remains. Any violation of monotonic gap order, common prefix sets or
other realization constraints is rejected, not assigned extra multiplicity.
The accepted DC recovery is injective. These gap counts are a subrecord
of an invariant full decoration, so this is a code on COMMUTATION
CLASSES, not a choice of representatives.

Multiply by B(m_1,...,m_D) and by the number product_i C(m_i) of
internal records to obtain (7). If S>0 then some m_i>=2, hence some
q_m>=1 and E_*>=1; the binomial is defined. If S=0 there are no
recorded contacts and one empty record, so J_*=1 is defined separately.

For D=1, a_1=0 and (4) is equality C(n)=B(n)H_n(0); the coarser
composition relaxation (7) need not be equality. If every m_i=1,
S=E_*=0, all H,T,V factors are one and B(1,...,1)=C(n), again equality.
The auxiliary n=1 convention has the same empty record. No empty
positive color block or binomial with a negative top is used.

## 6. The new scalar inequality, with the limits in their proper order

Fix D>=2 and take balanced positive m_i in {floor(n/D),ceil(n/D)}.
Then accepted coordinatewise monotonicity and the ALL-integer G2 limit
give

    n^-2 log B(m_1,...,m_D)->ell_D.                    (14)

The separately accepted official limit applied to each m_i gives

    n^-2 sum_i log C(m_i)->L/D.                        (15)

Let delta_i be 0 or 1 according to the parity of m_i. The exact identities

    S=(sum_i m_i^2-n)/2,
    E_*=[n^2-sum_i m_i^2+n
                 -sum_i delta_i(n-m_i+1)]/2,
    E_*+S=[n^2-sum_i delta_i(n-m_i+1)]/2               (16)

follow from q_m=(m-delta)/2. At fixed D their correction term is O_D(n).
Since sum_i m_i^2/n^2->1/D, it follows that

    S/n^2->1/(2D),
    E_*/n^2->(1-1/D)/2,
    (E_*+S-1)/n^2->1/2,
    S/(E_*+S-1)->1/D.                                 (17)

For sufficiently large n, S>0 and E_*>=1. The elementary entropy
inequality log binom(M,s)<=M h_2(s/M), 0<=s<=M, applies to
M=E_*+S-1 and s=S. It follows either from the binomial theorem at
probability s/M or directly at s=0,M, with h_2(0)=h_2(1)=0. From
(17) and continuity,

    limsup_n n^-2 log J_* <=(1/2)h_2(1/D)=g_D.         (18)

Take logarithms in (7), use (14),(15),(18) and the known limit L:

    L<=ell_D+L/D+g_D.

The lower bound ell_D<=L is accepted DC/G. Rearrangement is legal for
D>1 and proves (8); replacing L by its separate upper bound U in the
error is also legal. Nothing in this proof uses D=D(n), a rate in p,
or exchanges the direction and side-length limits.

For completeness compare with OP. Put p=1/D and use the accepted
entropy identity

    f_D=h_2(p)-h_2(p/2)+p.

Their difference is

    f_D-g_D=G(p):=(1/2)h_2(p)-h_2(p/2)+p.

It extends continuously to G(0)=G(1)=0, and for 0<p<1,

    G''(p)=[1/(2 ln(2) p)]
                      [1/(1-p/2)-1/(1-p)]<0.         (19)

Strict concavity and the two endpoint values give G(p)>0. Finally
h_2(p)=p log2(1/p)+p log2(e)+o(p); this follows from
-ln(1-p)/p->1. Substitution gives G(p)/p->1/2, proving (9).
Thus the new error is strictly smaller at every fixed D, with a
1/(2D)+o(1/D) improvement, not another halving of the logarithmic term.

## 7. What is gained, and the exact remaining gap

The finite hierarchy H_m<=T_m<=V_m keeps the actual weighted SUM over
internal classes and exposes an order constraint the independent + port
product had forgotten. H_m has an actual tiling interpretation; its
proof does not convert insertion histories into distinct counts by
assumption. Between different selected chains genuine comparabilities
remain, so the explicit chain bound is still an upper relaxation.

No quadratic-size gain follows merely because H<T is strict at every
finite m,a. Its logarithmic difference might be subquadratic along the
parameters of interest; that has not been proved either way. Likewise
the necessary common-prefix condition for Q still removes additional
records whose aggregate weighted mass is unevaluated. A useful next
task is to bound the SUM of those order-constrained capacities jointly
with projected Q at quadratic scale, not to maximize one old degree
vector or to assume every abstract map lifts through arbitrary Q.

The new explicit D-error concerns the OUTER direction limit only. Each
ell_D still lacks the two effective fixed-D approximation inputs E/R
specified in accepted V3. The abstract V4 obstruction remains a warning
about those weak numerical premises, not a statement that actual L is
noncomputable. No exact SFT/mixing identification or compatible-boundary
variational theorem has been proved here. Published partition/heaps
methods motivate the finite proof, not an imported value formula.

The full candidate, 40 obligations, failed routes, source checks, research
log and immutable metadata accompany this submission. No old byte or
shared file was edited. This proposed partial result awaits TWO OTHER
fresh initially blind WHOLE audits and coordinator reconciliation; the
official common numerical value remains unresolved.
