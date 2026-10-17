# The unmarked linear language: exact overlaps and an ambiguity barrier

2026-10-17 UTC. **Candidate proof - unverified.** Constructor
`/root/review_2017_coarsening_r1`; requested gpt-6.1-sol/max, effective
readback unavailable. The coordinator supplied the exact two-state grammar
as a research lead. The new overlap identities, injections, regular slice
and explicit weighted-pattern argument below are reconstructed here.
Two OTHER fresh initially blind whole nonconstructor audits are required.
No exact growth value, inherent ambiguity, full annual solution or novelty
is claimed. This is 2019 B4(b) only, not a new preliminary-bound proof.

## Scope, notation and complete statements

Use the ORIGINAL unmarked binary output language B from seed1. Let O_k
be its length2k+1 words, k>=0, and E_(k+1) its length2k+2 words. Put

    a_k=|O_k|=b_(2k+1),     e_(k+1)=|E_(k+1)|=b_(2k+2).

Write O and E for the unions of the odd and even levels. The accepted
earlier project theorem establishes b_n^(1/n)->lambda and lambda<2.
That existence/strict bound is used only in the growth comparisons and
analytic normalization below. It is not reproved, and no old finite
certificate is rerun. No chronological separator language or canonical
history language is identified with B.

**LO1 (exact linear grammar).** The terminal languages of

    O -> 1 | 1E | E1,          E -> 0O | O0               (1)

are exactly O and E above. This grammar is reduced, linear, chain-free
and epsilon-free. Its nonterminal dependency graph is strongly connected.

**LO2 (unmarked nonregularity and occurrence condition).** B, O and E
are not regular. In fact

    O intersect 0*1* = {0^r 1^(r+1) : r>=0},
    E intersect 0*1* = {0^r 1^r : r>=1}.                 (2)

Every finite binary word occurs in a nonterminal sentential form from
EITHER O or E. Consequently every binary word is a proper factor of a
terminal word from either state. This verifies the extra occurrence
condition in the primary linear-ergodicity definition; it does not turn
the grammar into an unambiguous one.

**LO3 (exact derivation counts).** If d_O(w) and d_E(w) count rightmost
derivations in (1), then

    sum_(w in O_k) d_O(w)=4^k,
    sum_(w in E_(k+1)) d_E(w)=2*4^k,
    d_O((10)^k1)=2^k.                                  (3)

The combined weighted series is z/(1-2z), with coefficient2^(n-1).
It counts derivations, not distinct output words. The mean multiplicity
at length n has exponential rate2/lambda>1, using only accepted lambda<2.

For k>=0 define two DISTINCT-WORD overlap counts

    I_k = #{t in {0,1}^(2k) : t0 and 0t both in O_k},
    J_k = #{(u,v) in O_k x O_k : 10u=v01}.               (4)

Each u in J determines v, so this is not an independent pair multiplicity.

**LO4 (exact overlap recurrence, all endpoints).** One has

    a_0=1, I_0=0, J_0=1,
    e_(k+1)=2a_k-I_k,
    a_(k+1)=4a_k-2I_k-J_k,                 EVERY k>=0.  (5)

There are only three possible pairwise intersections of the four odd
images, and no triple intersections. In particular J_0 is NOT zero.

**LO5 (the overlaps retain the entire output entropy).** For all k>=0,

    I_k<=a_k, J_k<=a_k,
    I_(k+2)>=a_k, J_(k+1)>=a_k.                         (6)

Both inequalities on the right come from explicit recoverable maps.
Consequently both overlap families have exponential rate lambda, in
their ordinary word-length scale. They cannot be declared lower-entropy
error terms. For

    A(z)=sum a_k z^(2k+1),
    E(z)=sum e_(k+1) z^(2k+2),
    I(z)=sum I_k z^(2k), J(z)=sum J_k z^(2k),

the exact formal identities are

    E(z)=2z A(z)-z² I(z),
    (1-4z²)A(z)=z-z³(2I(z)+J(z)).                      (7)

The three series A,I,J have radius1/lambda. Since accepted lambda<2,
they are analytic at z=1/2 and

    2I(1/2)+J(1/2)=4.                                 (8)

This is a normalization/cancellation identity, NOT an equation evaluating
lambda. A finite counterexample below also disproves the tempting
closure J_k=a_(k-1) for k>=1.

**LO6 (an explicit weighted pattern bound).** Fix any nonempty binary
word f of length m and put L=2m. Let D_n^f be the TOTAL number of
derivations in (1), from the appropriate parity state, whose length-n
terminal output avoids f as a contiguous factor. Then for every n>=1,

    D_n^f <= (2^L-1)^floor((n-1)/L)
                *2^((n-1) mod L).                     (9)

Thus the weighted avoiding rate is at most(2^(2m)-1)^(1/(2m))<2.
This also bounds distinct avoiding words, but does NOT show their rate
is less than lambda. The comparison in(9) is with derivation growth2.

## 1. Exact grammar and nonregular original language

At even output length, the last addition was0, at one end of an odd
output; this is exactly either production for E. At odd length greater
than1, the last addition was1 at one end of an even output; these are
the two nonterminal productions for O. The only stopping case is seed1.
Induction on length proves BOTH inclusions between grammar words and
official outputs, for both states. There are no extra empty/length-zero
words, no marked position, and no grammar convention that changes the
count from outputs to histories.

Every production has at most one nonterminal, and every nonterminal
production adds precisely one letter. Both variables derive terminal
words and are reachable from either start, so the stated reduced/proper
and strong-connectivity assertions follow.

Every output of length2k+1 has k zeros and k+1 ones; every output of
length2k+2 has k+1 of each. This follows immediately from the mandated
added-bit sequence and is a necessary condition on words, independent
of their number of histories. It gives the necessary inclusions in(2).
For the converse odd inclusion, repeatedly use the legal two-move
operation w->0w1, starting at1. It produces0^r1^(r+1). Prepending0 to
the corresponding odd word0^(r-1)1^r produces every even word0^r1^r,
r>=1. Thus(2) is exact.

The language{0^r1^(r+1)} is not regular: if P is a regular pumping
length, choose0^P1^(P+1). Every decomposition whose pumping part ends
within its first P letters pumps a positive number of zeros only;
removing that part changes the difference between ones and zeros from1.
The analogous argument applies to{0^r1^r}. Regular intersection would
make these slices regular if O or E were regular. Finally if B were
regular, intersecting it with the regular odd-length language would
make O regular. Therefore ALL three original unmarked languages are
nonregular. This makes no assertion of nonrationality of their series:
the two displayed nonregular slices themselves have rational counting
series.

For the occurrence condition, start from either nonterminal T and fix
an arbitrary binary word w. The emitted letters along any nonterminal
derivation alternate:1,0,... from O and0,1,... from E. Any finite
binary word is a subsequence of a sufficiently long such alternating
prefix. At its chosen occurrences emit that letter to the LEFT of
the current variable; at all intervening steps emit the letter to
the RIGHT, using the other production at that state. The resulting
nonterminal sentential form is exactly

    w U v

for a state U and some terminal suffix v. Completing U to any nonempty
terminal word gives a word of the original start language containing w
as a PROPER factor. All left-emitted letters remain adjacent; sending
skipped letters right does not put them between letters of w. This
proves the asserted condition for every finite word, without an
unbounded-delay theorem. Factor universality does not imply that
words of a given length are all admitted; padding can have comparable
length to w.

## 2. Exact ambiguity, and why the two-state matrix does not count words

A complete derivation producing length n makes exactly n-1 nonterminal
productions followed by O->1. At each nonterminal step there are exactly
two orientation choices. The parity state after those steps determines
whether stopping is possible. Thus the totals from O at odd length are
2^(2k)=4^k, and from E at even length2k+2 are2^(2k+1). These are
production-sequence counts, even if their terminal strings coincide.

For an exact collision witness, let w_k=(10)^k1. At k=0, seed1 has one
derivation. Eliminate E once in (1), obtaining four TWO-STEP operations
on odd words:

    P(w)=10w, Q(w)=1w0, R(w)=0w1, S(w)=w01.             (10)

For w_k with k>=1, Q cannot be its outer operation because Q ends0,
and R cannot because R starts0. Its outer operation is either P or S.
Stripping that operation leaves w_(k-1) in both cases, and each choice
corresponds to a different pair of actual productions. Therefore
d_O(w_k)=2d_O(w_(k-1))=2^k, EXACTLY. The exhibited grammar is
exponentially ambiguous, not merely ambiguous at an isolated seed.

The weighted equations are valid as derivation equations:

    A_der=z+2z E_der,   E_der=2z A_der.

They give A_der=z/(1-4z²), E_der=2z²/(1-4z²), and their sum is
z/(1-2z). Equating either equation with DISTINCT-word generating
functions would count overlaps twice. Moreover, accepted b_n^(1/n)
->lambda<2 gives

    (2^(n-1)/b_n)^(1/n) -> 2/lambda >1.

So the mean ambiguity, not only its maximum, has an exponential loss
relative to terminal words. A subexponential-ambiguity entropy transfer
cannot be applied to THIS presentation. Exponential ambiguity of one
grammar does not prove the language inherently ambiguous or rule out
some other unambiguous linear grammar.

## 3. Exact distinct-word overlap identities and the short endpoint

Eliminating E as a SET union gives

    O_(k+1)=P(O_k) union Q(O_k) union R(O_k) union S(O_k).

Each map in(10) is injective. P and R have incompatible first letters;
Q and R likewise; Q and S have incompatible last letters. The remaining
intersections are exactly:

* P(u)=Q(v) iff10u=1v0 iff0u=v0. This is equivalent to
  u=t0,v=0t with both in O_k, and is counted by I_k.
* R(u)=S(v) iff0u1=v01 iff0u=v0, giving the SAME parameter set I_k.
* P(u)=S(v) iff10u=v01, counted by J_k as DEFINED, at every k.

No triple intersection is possible, because every triple contains one
of the three disjoint pairs already listed. Inclusion-exclusion now
gives a_(k+1)=4a_k-2I_k-J_k. Likewise
E_(k+1)=0O_k union O_k0 has intersection0u=v0, giving2a_k-I_k.

The endpoints matter. O_0={1}, so I_0=0 but J_0=1 because101=101
with u=v=1. One must NOT rewrite J_k using a middle word of length
2k-1 at k=0. For k>=1 that rewrite is legitimate:

    J_k = #{t in {0,1}^(2k-1): 10t and t01 in O_k}.     (11)

Indeed any u ending01 has u=t01 and equality forces v=10t; the word
u has length2k+1>=3. At k=0 the overlap of the fixed prefix10 and
suffix01 creates the separate solution above. This completes every
endpoint in(5), with no computation.

## 4. Recoverable injections and a failed finite closure

The upper bounds I_k,J_k<=a_k follow by the injective maps t->t0
and(u,v)->u. For any w in O_k, define

    u=w01=S(w),   v=10w=P(w).

Both belong to O_(k+1), and10u=v01. Recovering w from u proves
J_(k+1)>=a_k. For I, set

    t=10w1.

It has length2(k+2), and

    t0=10w10=Q(R(w)),
    0t=010w1=R(P(w)).                                  (12)

Both belong to O_(k+2). Deleting the fixed prefix10 and suffix1 of
t recovers w, proving I_(k+2)>=a_k. These are injections of DISTINCT
word sets, not choices of derivations or marked fibers.

Using the accepted odd-level growth limit, for k>=2,

    a_(k-2)<=I_k<=a_k,    a_(k-1)<=J_k<=a_k.

Taking (2k)-th roots gives rate lambda for both overlap sequences.
Changing between denominators2k and2k+1 has no effect. The power-series
radii of A,I,J are thus all1/lambda, by the root formula for series
with nonnegative coefficients. This is an actual entropy obstruction
to declaring the overlaps smaller-order corrections; it does not prove
that no finite alternative description exists.

The tempting equality J_k=a_(k-1) would require every t in(11) to
belong to O_(k-1). It is false. Take t=01110. Both ends are0, so it
is NOT in O_2: any nonseed odd output has an outer added1 at an end.
Nevertheless

    10t=1001110=Q(R(R(1))),
    t01=0111001=R(Q(Q(1))).                             (13)

Both are in O_3. Together with the general injection from O_2 into
the t-set in(11), this yields J_3>=a_2+1. This is one exact symbolic
counterexample to a proposed closure, not a larger prefix table. No
claim that the extra set can never have a simpler description follows.

Multiplying the exact coefficient identities by the displayed powers
of z gives(7). Since lambda<2, all of A,I,J converge absolutely in a
neighborhood of z=1/2. Evaluation there gives(8). The apparent weighted
pole1/2 of1/(1-4z²) is canceled; it cannot be used to assert that the
distinct-word growth is2. The overlap series remain unspecified at
their actual boundary1/lambda. Equation(8) does not evaluate that boundary.

## 5. An explicit weighted avoidance bound

Fix f=f_1...f_m, m>=1, and L=2m. From EITHER state, the next L
emitted letters alternate and contain f as a subsequence: greedily
choose its j-th letter no later than position2j. Choose one such
subsequence once for that initial state. At those m positions take
the left-emitting production, and at every other position the
right-emitting production. This defines a specific orientation block
h_T in{left,right}^L. The left terminal projection of this entire
block is EXACTLY f.

If h_T occurs at any point of a complete derivation whose current
state is T, then f is a contiguous factor of the final word. To check
this, write the current sentential form u T v. After the block it is
u f U v' for some U,v'. Later productions operate inside U and
cannot break or insert letters between the already adjacent letters
of f. Earlier outer productions lie outside u f. Thus every derivation
whose output avoids f must avoid that orientation block at that state.

Partition its n-1 nonterminal choices into q=floor((n-1)/L) disjoint
blocks of length L and a remainder r. Since L is even, every full
block starts in the SAME parity state as the initial one. Among the
2^L possible orientation blocks, at least the specified h_T is forbidden.
There are at most(2^L-1)^q choices for the full blocks and2^r for the
remainder, proving(9), also when q=0 or n=1. Every allowed sequence
of the required parity ends with O->1; imposing further avoidance can
only reduce this bound. No unambiguity is used, because derivations
are what is being counted in(9).

Taking n-th roots gives the stated rate strictly below2. Distinct
avoiding words are at most D_n^f, but the comparison needed to obtain
ordinary growth-sensitivity would be a strict bound below lambda, not
below2. Such a comparison is NOT obtained here. In particular this
does not convert the literature's weighted theorem into its unweighted
one for the present grammar.

## 6. Primary literature, a conditional count route, and remaining gap

The full primary article **Tullio Ceccherini--Silberstein ALONE**, *Growth
and ergodicity of context-free languages II: the linear case*, Trans.
AMS359(2007),605--618, electronically2006, was read via a public viewer.
Its unweighted Theorems1.2/1.5 assume an unambiguous linear presentation;
its §5 instead weights by derivation multiplicity. Neither supplies an
unweighted count for(1). The earlier 2005 *On the growth of linear
languages* was checked at primary publisher-abstract level only; no
unread full theorem is imported. Full source roles, exact reading and
failed public retrievals are in the separate source record.

There is a precise conditional route worth retaining. If B has a
FINITE PROPER UNAMBIGUOUS linear grammar, then its DISTINCT-word
counting series is rational. For such a reduced grammar, auxiliary
nonterminals are unambiguous too: two derivations of a word at one
reachable variable would extend through a fixed outer context to two
derivations from the start. Writing F_i(z) for the counting series
of the variables, each production i->u j v contributes
z^(|u|+|v|)F_j, and each terminal production contributes its monomial.
Unambiguity makes those contributions disjoint, so

    F=t+M(z)F,     F=(Id-M(z))^(-1)t.                  (14)

Properness here explicitly requires |u|+|v|>=1, so M(0)=0. The finite
inverse has rational entries by determinants, proving the conditional
statement. For an ambiguous grammar the same equations describe
DERIVATIONS instead, and(3) is an exact counterexample to treating that
series as the distinct-word series. No such unambiguous presentation
of B is supplied, and its existence is not inferred from linearity.

What remains unresolved is a finite recoverable description of the
overlaps I,J, or another presentation that controls ambiguity at the
ordinary output entropy. Nonregularity does not prove inherent
ambiguity, and nonregularity of canonical histories does not rule out
every other unambiguous linear presentation. The new recurrence is
exact but not closed: both overlap types retain the entire lambda
entropy, and even the first proposed simplification(11) fails at(13).
No rational/algebraic counting series or algebraic/transcendental lambda
is proved. No exact annual value or new numerical enclosure is given.
All failed inferences are retained; two other fresh whole audits are
required before any scoped promotion.
