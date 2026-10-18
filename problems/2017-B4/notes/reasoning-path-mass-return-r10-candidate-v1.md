# Actual schedule multiplicities and the history-pressure obstruction

2026-10-18 UTC. **Candidate proof - unverified.** Constructor B,
`/root/review_2022_complexity_r2`. Requested inherited `gpt-6.1-sol/max`;
independent effective-setting readback unavailable. Root assigned the
scalar-value research target and supplied NO NEW proof inference.
TWO OTHER initially blind ENTIRE WHOLE audits and full coordinator
reconciliation are required. B is excluded from those reviews.

This is a quantitative obstruction for ACTUAL official2017 arrangements,
not an abstract integer count model. It does not evaluate the official
constant, improve PM9's upper bound, supply a matching lower bound,
prove two-sided computability, refute a published random-sorting theorem
or establish a new typical geometry. No novelty or annual solution.

## Significance and exact remaining issue

Uniform reduced sorting histories are a natural primary-literature route
to the geometry of large reversal networks. They are not uniform rhombus
tilings: a tiling is one COMMUTATION CLASS of histories. The earlier
research record already warns of this distinction using small examples.
Here two explicit all-size actual families prove that the multiplicity
spread has leading order `(1/2)n² ln n`, larger than the entire quadratic
entropy under study. The corresponding fixed-temperature multiplicity
pressure has an explicitly evaluable but uninformative leading limit.
Even a coupling tending to zero like a sufficiently large constant
divided by ln n still changes the quadratic free energy.

This pinpoints a genuine missing inference in a tempting route: a
uniform, subquadratic correction from histories to tilings is impossible.
An argument controlling multiplicities on a sufficiently large family
of actual classes could still work. The examples below are individual
classes, so they do NOT prove that the two probability measures have
different typical events or limit shapes. That typical-multiplicity
problem remains open here.

## 0. Official count, accepted inputs and proposed claims

Let `n>=2`, `N=n(n-1)/2`, and `s_i` exchange positions i and i+1.
A reversal word is a sequence of N such adjacent transpositions taking
`1,...,n` to `n,...,1`, applied in the written order. It is reduced
because the target has N inversions. Two words are commutation equivalent
when connected by exchanges of adjacent generators s_i,s_j with
`|i-j|>1`. A braid `s_i s_(i+1) s_i <-> s_(i+1) s_i s_(i+1)` does NOT
identify two classes in this quotient.

Write `A_n` for this finite set of classes and `C(n)=|A_n|`. The accepted
marked dictionary identifies it with the exact official unit-sided fixed
regular2n-gon tilings. There is no rotation/reflection quotient, extra
n! boundary-label factor, arbitrary insertion history or metric drawing
count. For `A in A_n`, let `m(A)` be the number of distinct reversal
WORDS in A, and put

    W_n=sum_(A in A_n) m(A),   m_max(n)=max_A m(A).

All these are actual positive finite integers. W_n is auxiliary and
is NOT the official C(n).

Only the following accepted mathematical inputs are used:

* The exact marked commutation-class dictionary, as in current DC and
  PM9, and the elementary Coxeter commutation rule above.
* PM9C's all-size actual bound, for its fixed constant H>1,

      C(n)<=H^(N-1), n>=2.                            (0.1)

  The current complete PM9 body and MD/JSON were freshly read. This
  does not construct or re-audit its old local-geometry premises.
* For the final comparison to the official limit only, accepted G2/G3
  gives `L=lim_n log2 C(n)/n²`. Its exact setting is full balanced
  counts at ALL integer sizes for each FIXED D, followed by D growing;
  no uniform fixed-D rate or numerical value is imported. B's older
  all-D construction is disclosed, not independently self-recertified.

All new logarithms below are NATURAL. Thus `ln C(n)/n² -> L ln2`.
The statements not mentioning L require only (0.1), not the global
existence theorem or an effective finite count algorithm.

**R10A (actual extremal multiplicities).** There is a class `R_n` with
`m(R_n)=1` for every n>=2. There is also an explicit class `O_n` with

    m(O_(2a)) >= (a!)^a ((a-1)!)^a,
    m(O_(2a+1)) >= (a!)^(2a+1).                       (0.2)

For every n>=4, with `c0=1+ln4`,

    N(ln n-c0) <= ln m_max(n) <= N ln(n-1),
    lim_n ln m_max(n)/(n² ln n)=1/2.                 (0.3)

**R10B (sharp uniform normalization obstruction).** For every n>=2,

    inf_(b>0) max_(A in A_n) |ln m(A)-ln b|
       =(1/2)ln m_max(n).                            (0.4)

Consequently the left side divided by n² ln n tends to1/4. No sequence
of common normalizing constants can make all class multiplicities
uniformly accurate to `exp(o(n² ln n))`, in particular to `exp(O(n²))`.
This does not forbid an unknown average normalizer W_n/C(n).

**R10C (actual measure and entropy consequences).** Let U_n be uniform
on A_n and let Q_n be the image in A_n of a uniform reversal WORD. Then

    U_n(A)=1/C(n), Q_n(A)=m(A)/W_n,
    lim_n ln[U_n(R_n)/Q_n(R_n)]/(n² ln n)=1/2.        (0.5)

The likelihood oscillation over classes is exactly ln m_max(n).
Moreover, if `Ent(Q_n)=-sum_A Q_n(A) ln Q_n(A)`,

    ln W_n=Ent(Q_n)+sum_A Q_n(A)ln m(A),
    0<=Ent(Q_n)<=ln C(n)<= (N-1)ln H,
    lim_n [sum Q_n ln m]/(n² ln n)=1/2.              (0.6)

This is a pointwise obstruction and leading conditional-entropy
calculation, not a total-variation or typical-event separation theorem.

**R10D (fully evaluated leading history pressure).** For real tau put

    Z_n(tau)=sum_(A in A_n) m(A)^tau.

Then for EVERY fixed real tau,

    lim_n ln Z_n(tau)/(n² ln n)=max(tau,0)/2.        (0.7)

In particular Z_n(0)=C(n) and Z_n(1)=W_n, but the leading pressure
in (0.7) erases the quadratic coefficient requested in2017. It is
not a characterization that evaluates L.

**R10E (a real vanishing-coupling boundary).** For all n>=2 and real tau,

    |ln Z_n(tau)-ln C(n)|<=|tau| N ln(n-1).          (0.8)

For any real sequence tau_n with `|tau_n| ln n ->0`, accepted scalar
existence therefore gives `ln Z_n(tau_n)/n² -> L ln2`. Conversely,
for EVERY fixed alpha>ln H and `tau_n=alpha/ln n`,

    liminf_n ln Z_n(tau_n)/n² >=alpha/2
       > (ln H)/2 >=L ln2.                          (0.9)

Thus even tau_n->0 is insufficient to preserve the quadratic free
energy. The finite-alpha pressure limit/distribution and L remain
unevaluated. No necessity assertion for every negative sequence or
every coefficient alpha is made.

## 1. One actual rigid class at every size

For auxiliary recursion only let `w_0,w_1` be empty words. For n>=2 set

    p_n=(1,2,...,n-1,n-2,...,1),
    w_n=p_n followed by (1+w_(n-2)),                 (1.1)

where1+word adds1 to every generator index. The descending part of
p_2 is empty. The first sweep1,...,n-1 moves label1 to position n,
leaving the middle labels2,...,n in increasing order. The return sweep
n-2,...,1 moves label n to position1. Its resulting list is

    n,2,3,...,n-1,1.

The shifted recursive word acts only on positions2,...,n-1 and reverses
that increasing middle list by induction. Therefore w_n reverses all
n labels. Its length satisfies

    len(w_n)=2n-3+(n-2)(n-3)/2=N.

It is reduced: any adjacent swap changes the inversion number by1
in absolute value, and reaching N inversions in N steps permits no
inversion-decreasing step. In particular it defines an actual marked
arrangement/class and hence an actual tiling under the accepted dictionary.

Every consecutive pair of indices in p_n differs by1. If the recursive
part is nonempty, its first index is2 whereas p_n ends with1; the
same property holds inside it by induction. Thus every adjacent pair
in the ENTIRE word has index difference1. No two adjacent letters
commute. The word is therefore an isolated vertex of the graph whose
edges are allowed commutations: a sequence leaving it would need a
first such edge. Its commutation class R_n has exactly one word.

For n2 this is(1), for n3 it is(1,2,1). The bases are included by the
same reasoning. No braid move is allowed as a way to escape this
commutation class. No classification of ALL singleton classes is claimed.

## 2. A layered actual reversal with many histories in ONE class

For phases t=1,...,n, let layer t consist of ALL generators s_j such
that `1<=j<n` and `j=t mod2`. Apply the layers in increasing phase
order, choosing any fixed order inside each layer initially. Within
one layer indices differ by at least2, so all its generators commute.

Here is a direct proof that the resulting word reverses the labels.
At phase1 a particle initially in an odd position moves right, unless
it is at the right boundary; a particle in an even position moves left.
After a right move, the parity of its new position agrees with the
next phase, so it moves right again if there is a wire to its right.
After a left move it is similarly the right endpoint of the next
active edge, and moves left again. At an endpoint a particle waits
ONE phase before reversing its direction. There is no two-particle
assumption in this description: each phase is a disjoint matching of
positions, hence this is its exact action on each particle.

If the initial position i is odd, it takes n-i moves to the right
endpoint, waits one phase, then takes i-1 moves left in the n-phase
time interval. Its final position is `n-(i-1)=n+1-i`. If i=n is odd,
the first segment has length0 and the initial waiting phase is included.
If i is even, it takes i-1 moves left, waits one phase, then takes
n-i moves right. Its final position is `1+(n-i)=n+1-i`.
The remaining travel never requires a second reflection before the
last phase. Thus every label ends at its reverse position.

For n=2a there are a odd phases of size a and a even phases of size
a-1, with total `a²+a(a-1)=N`. For n=2a+1 every one of the n phases
has size a, with total `na=N`. Empty even phases at n2 are harmless.
So this reversal word is reduced, not a longer sorting history.

Permute the letters independently within each layer. Every resulting
word remains in the same commutation class O_n and represents the same
reversal. The number of choices is the product of layer factorials.
They are DISTINCT words: layer lengths and their fixed positions in
the full word recover the permutation chosen in each layer, even when
the same generator reappears in a later layer. This proves (0.2).
It is a lower bound for one class, not an exact formula for its entire
size; commutations across layer boundaries may add further words.

For n>=4 every layer has size s_t>=n/4 and sum_t s_t=N. For any
integer s>=1, monotonicity of ln x on[1,s] gives

    ln(s!)>=integral_1^s ln x dx>=s ln s-s.

Consequently, writing J_n for the product in (0.2),

    ln J_n>=sum_t s_t(ln(n/4)-1)
            =N(ln n-c0), c0=1+ln4.                 (2.1)

The upper bound `m(A)<=(n-1)^N` simply counts ALL sequences of N
generator indices, including invalid ones. It applies to every class
and gives the other half of (0.3). Divide by n² ln n, using
`N/n²->1/2` and `ln(n-1)/ln n->1`, to prove its sharp limit.
No Stirling expansion, hook formula, enumerator or binomial table is
needed. Both examples are actual families for unbounded n.

## 3. The normalization and measure obstructions

Let `D_n=ln m_max(n)`. The finite set of logarithmic multiplicities
lies in[0,D_n] and contains BOTH endpoints by Section1 and the attained
maximum. For any real x,

    D_n<=|x|+|D_n-x|<=2 max_A |ln m(A)-x|.

Taking x=D_n/2 makes every distance at most D_n/2. Set x=ln b to
obtain the EXACT minimax identity (0.4). Section2 gives its limiting
coefficient1/4. In particular no b_n can bound all multiplicity errors
by any fixed constant times n², nor by o(n² ln n), as n grows.
This is not the false assertion that the aggregate identity
`C(n)=W_n/[W_n/C(n)]` has no average normalizer; that identity is true
but its unknown denominator is the missing information.

Every word in a class maps to that class, so the two finite probability
measures have the exact formulas in (0.5). For the rigid class,

    ln[U_n(R_n)/Q_n(R_n)]=ln W_n-ln C(n).

Section2 and (0.1) imply, for n>=4,

    N(ln n-c0)-(N-1)ln H
       <= ln W_n-ln C(n) <= N ln(n-1).              (3.1)

The last inequality uses `W_n<=C(n)(n-1)^N`. The two sides divided
by n² ln n tend to1/2, proving (0.5). Also

    ln(Q_n(A)/U_n(A))=ln m(A)+ln C(n)-ln W_n.

Its maximum-minus-minimum is exactly D_n. Thus a uniform likelihood
comparison with only exp(O(n²)) loss in BOTH directions is impossible.
The explicit event here is the single class{R_n}. Its probability
can tend to zero under BOTH measures. We do not infer noncontiguity,
a total-variation lower bound or a difference of typical geometries.

The entropy identity is equally exact and finite:

    Ent(Q_n)=sum_A [m(A)/W_n] ln[W_n/m(A)]
             =ln W_n-sum_A Q_n(A)ln m(A).

Nonnegativity follows because each probability is at most1.
For the upper bound, `-ln x<=1/x-1` for x>0 gives
`sum_A Q_n(A)ln[C(n)Q_n(A)]>=0`; hence Ent(Q_n)<=ln C(n).
The elementary logarithm inequality follows by minimizing y-1-ln y
at y=1 and then taking y=1/x, so no external entropy theorem is imported.
Combining this bound with (3.1) and `ln m<=N ln(n-1)` squeezes
`sum Q_n ln m/(n² ln n)` to1/2, proving (0.6).

Most leading `n² ln n` history entropy is therefore scheduling entropy
WITHIN a class. Its remaining O(n²) part still contains the unknown
official count information; it is not evaluated by this calculation.

## 4. The entire fixed-real-parameter leading pressure

Every multiplicity is positive, so Z_n(tau) is defined for every real
tau, including negative tau. For fixed tau>0, Section2 and (0.1) give

    tau N(ln n-c0) <= ln Z_n(tau)
        <=ln C(n)+tau N ln(n-1)
        <=(N-1)ln H+tau N ln(n-1).                 (4.1)

Divide by n² ln n to get tau/2. At tau0, Z_n(0)=C(n), whose logarithm
is between0 and (N-1)ln H, so its same normalization tends to0.
For tau<0, `m(A)^tau<=1`, while the rigid class contributes exactly1.
Thus `1<=Z_n(tau)<=C(n)`, giving the limit0. These exhaust the real
parameter domain and prove (0.7) without a limiting interchange.

The function in (0.7) has a kink at0. Its left/right derivatives are
0 and1/2, but neither derivative is the official L. No derivative of
a finite sum is interchanged with a limit. Knowledge of this leading
pressure, even at every fixed tau, has removed the O(n²) term at tau0
by dividing by the larger n² ln n scale. The statement is an evaluated
obstruction, not an unevaluated renaming of the original limit.

## 5. Vanishing parameters do not automatically fix the problem

For tau>=0 the termwise bounds on m give

    C(n)<=Z_n(tau)<=C(n) exp[tau N ln(n-1)].

For tau<=0 their order is reversed in the appropriate way:

    C(n) exp[tau N ln(n-1)]<=Z_n(tau)<=C(n).

Together these prove (0.8) for every finite n>=2. They include n2,
where ln(n-1)=0 and the unique class has multiplicity1.
If `|tau_n|ln n->0`, (0.8) divided by n² tends to zero, so the accepted
official limit gives the first R10E conclusion.

Now fix alpha>ln H, without letting it depend on n. The term from
O_n alone and (2.1) give at tau_n=alpha/ln n,

    ln Z_n(tau_n)/n²
       >=alpha (N/n²)(1-c0/ln n) ->alpha/2.

On the other hand PM9 gives `L ln2<=ln H/2`. This proves the strict
comparison (0.9). Thus a parameter tending to0 at this specified rate
can already shift the quadratic free energy by a positive amount.
For positive sequences with tau_n ln n->infinity, the same lower
bound even forces ln Z_n(tau_n)/n²->infinity. Nothing parallel is
asserted for all negative sequences.

We have not proved existence/evaluation of the limit at a general
fixed alpha/ln n, a finite-alpha phase transition, or a way to compute
L from these inequalities. The sufficient o(1/ln n) scale is not
claimed a sharp iff for every possible sequence or model property.

## 6. What the primary literature does and does not supply

The [Felsner--Valtr original marked/wiring/zonotopal discussion](https://page.math.tu-berlin.de/~felsner/Paper/new-pla.pdf) and the
accepted project dictionary identify the official objects. Their
cutpath construction counts extensions of a fixed parent, not uniform
sorting histories. [Dallant's v2](https://arxiv.org/pdf/2502.20909v2) has the same marked definition. Its
Section3 high-cutpath construction does not by itself control the
population of parents; its finite computational count was NOT rerun
or used as a new premise. The average/small-zone proposals in its
Section4 remain proposals, not hypotheses silently assumed here.

The [original Angel--Holroyd--Romik--Virag paper](https://arxiv.org/pdf/math/0609538) defines the uniform law
on ALL sorting words. [Dauvergne's Archimedean theorem](https://arxiv.org/pdf/1802.08934v4) uses this same
uniform sorting-network law. I read their definitions/operative theorem
statements, not the entire deep limit proofs, which are not imported.
Their theorems are not refuted or applied to uniform classes here.
The exact pushforward law Q_n was derived directly in Section3.

Even a class event must be distinguished from a time-parametrized
trajectory event: commuting disjoint swaps changes the intermediate
time-slice permutation. For example the first layer(1,3) versus(3,1)
on four wires has different states after its first swap, while its
class is unchanged. No canonical geometric representative or class
limit shape is furnished by a word law without further work.

The layered reversal is the standard odd/even matching construction;
rigid words and schedule multiplicities are elementary established
objects. The proposed asymptotic/measure consequences are proved
explicitly, but their published originality has NOT been established.
No unread external counting formula, source program, hook-length theorem,
large-deviation theorem, statistical-mechanics analogy or full-paper
audit supplies a missing proof step.

## 7. Remaining scalar-value gap and honest failed routes

The new conclusions are obstructions, not an upper/lower match.
The exact current all-D theorem supplies scalar existence; PM9 supplies
the strict upper H. The lower bound and numerical value remain as
before. A class of enormous history multiplicity is still just ONE
tiling and supplies no quadratic lower bound for the number of classes.

One possible remaining route would control the distribution of
`ln m(A)-N ln n` at scale n² on a sufficiently large collection of
ACTUAL classes, with the correct measure and both count inequalities.
The extremal examples do not supply that typical control. The entropy
identity and Z_n are not claimed as an effective characterization of L:
evaluating the needed quadratic remainder is precisely what is missing.

Also unproved here: a uniform exponent improvement from compatible
multi-strand insertions, typical-family prevalence of high-cutpath
parents, an average-zone conjecture, fixed-boundary/free-window entropy
equality, effective upper R or a uniform D-dependent convergence rate.
Earlier accepted free/balanced entropy gaps and lower-only certificates
are preserved. No formal model or periodic patch is substituted for
the official full count. Full failures, obligations/checks, source
read limits, worklog, administrative code and compact immutable
metadata accompany this candidate; TWO OTHER whole audits remain required.

No mathematical executable, enumeration, table, CAS, optimizer, source/
author/old certificate replay, paid API, charge, contact, cache change,
access bypass or worker Git operation supplied this proof. All arguments
are hand constructions and finite inequalities. New metadata code only
preserves exact files/labels; it does not establish the mathematics.
