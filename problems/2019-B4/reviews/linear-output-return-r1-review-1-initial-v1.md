# Fresh initially blind WHOLE linear-output audit R1

2026-10-17 UTC. Reviewer `review_2021_reasoning_j15_r2`.
Requested gpt-6.1-sol/max; effective-setting readback unavailable.
This is a nonconstructor recommendation, not coordinator promotion.

**Recommendation:** no substantive defect found in LO1–LO6 or the
stated conditional rational-series argument. I reconstructed the full
chain and all28 obligations, including every overlap intersection and
J0, both recoverable injections, the generating-series shifts and
analytic cancellation, the internal forcing-block proof and the exact
limits of its weighted conclusion. The44-check ledger records the
individual inferences. No required author repair was identified. The
exact growth constant, another unambiguous presentation and ordinary
growth-sensitivity remain unresolved. A second complete fresh whole
audit and coordinator reconciliation are still required for promotion.

Target:17270 bytes, SHA256
`b1bec632971326a661a4188135ce23d40f0fdcc6a121197aefe10d2237f6e1fa`.
Constructor freeze:3511 bytes, SHA256
`b1728d67d1101e3c9207fc935919c0cc4bf7c148f3af3220344729e5554b2deb`.
The complete main,28-obligation MD, worklog, source-audit MD, sources
JSON and constructor self-check were read. Scripts/input-validation
are administrative provenance; author code is not executed. The
self-check is not one of the required independent reviews.

## Independence and source boundaries

I authored the earlier2019 NR1–NR4 return, previously audited the
moment-tail work, and have just independently reviewed CCL's different
separator language. Those roles are explicit. I did not construct,
suggest or repair NEW LO grammar/overlap/weighted arguments. Root
supplied the grammar and literature lead, and C constructed this
packet; neither is counted as an independent reviewer. No new peer
linear-output findings/report or later root inspection was read before
this COMPLETE initial freeze. No substantive finding was sent before it.

The only accepted mathematical input is the actual output growth
limit b_n^(1/n)->lambda with lambda<2. The complete accepted proof.md
and its acceptance were reread; older certificates are accepted inputs,
not rerun. Other declared context files are fingerprinted with their
actual read scopes distinguished in the source record. Neither my old
NR conclusion nor the newly accepted CCL assertion is an LO premise.

The full2007 primary article text was freshly read through its public
viewer, including all definitions and theorem hypotheses used for the
source comparison. No entire external proof is claimed newly
independently established. The2005 source was available only through
its primary publisher-indexed abstract; no unread full theorem is used.

## 1. Exact original-output grammar and small parity levels

The [official2019 B4(b)](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-paper-b_1.pdf)
counts DISTINCT unmarked binary strings generated from seed1 by the
prescribed alternating0/1 additions at either end. It asks the lower
and upper exponential rates. A history, marked context or separator
pair is not an official output. This review concerns part(b) only;
no preliminary proof is researched or reproduced.

Let O_k=B intersect{0,1}^(2k+1), E_(k+1)=B intersect{0,1}^(2k+2).
The grammar is

    O -> 1 | 1E | E1,
    E -> 0O | O0.

For both directions, induct on output length. Every even output is
an odd output with its last mandated0 at an end; these are exactly
the two E productions. Every nonseed odd output has its last
mandated1 at an end of an even output; these are exactly the two
nonterminal O productions. Seed1 is the only stopping rule. Conversely
each such production implements that legal last addition. There is
no extra empty word, mark or side-order convention. In particular

    O_0={1}, E_1={01,10}.

Each nonterminal production adds exactly one terminal and has one
remaining variable. There are no chains or epsilon rules. From
either parity start both variables are reachable and productive,
and the dependency graph is O<->E. Thus each parity-start grammar
has the claimed reduced, linear and strong-connectivity properties.
B=O union E is also a linear context-free language, for example by
adjoining a union start. No assertion that this new union start is
itself part of the same strong component is needed or used.

The grammar derivation chooses outermost LAST additions first. Its
emission order is not the forward chronological source tape used in
CCL. The grammar's own two productions at every state are sufficient
for all constructions below.

## 2. Nonregularity of the actual outputs and the occurrence clause

Every O_k word has k zeros and k+1 ones, while every E_(k+1) word
has k+1 of each. These are necessary counts, not a sufficiency test
for arbitrary words. Intersecting with0*1* therefore gives at most

    {0^r1^(r+1):r>=0} for O,
    {0^r1^r:r>=1} for E.

Both inclusions reverse constructively. Starting with1, the legal
two-step wrap w->0w1 gives each odd word0^r1^(r+1). Prepending0 to
the odd word0^(r-1)1^r gives the even word0^r1^r. These include r0
for O and r1 for E with no empty official word.

For any regular pumping length P>=1, the word0^P1^(P+1) in the
first slice has every pumping segment within its first P symbols
consisting of a positive number of zeros. Pumping down changes
the required difference of counts. This contradicts the bounded
prefix form of the regular pumping lemma. The same proof with
0^P1^P treats the even slice. A DFA pigeonhole among its first P
transitions supplies exactly that bounded-prefix version. Regular
intersection then proves O and E nonregular. If B were regular,
its odd-length restriction O would be regular; thus B is nonregular
too. These nonregular slices themselves have rational word series
z/(1-z²) and z²/(1-z²), illustrating why no nonrationality follows.

For the additional occurrence condition, fix any finite binary word
w and either initial variable T. Nonterminal emissions alternate
1,0,... from O and0,1,... from E. Greedily selecting each successive
required letter embeds w into a sufficiently long alternating
prefix. At those selected steps choose the left-emitting production,
and at every other step choose the right-emitting one. The sentential
form is then

    w U v,

with a variable U still present. Left emissions accumulate in forward
order adjacent before U; right emissions accumulate after U and never
separate letters of w. Complete U to a nonempty terminal word. The
result contains w as a PROPER contiguous factor. The empty w is
included by the initial form T and a nonempty completion.

This proves more than the required occurrence assertion for words
of either start language. It verifies the actual extra linear
occurrence clause, rather than treating graph strong connectivity
alone as sufficient. It does not imply that all binary words of
the SAME length are outputs: a containing output may be longer.
The construction supplies no unambiguity.

## 3. Exact derivation counts and their exponential ambiguity

A derivation of a length-n word has exactly n-1 nonterminal steps
and one final O->1 step. The state after n-1 steps allows that
stop exactly for the appropriate parity start: O for odd n and E
for even n. Each step has two independent orientation choices.
Consequently the rightmost-derivation totals are

    4^k from O at length2k+1,
    2*4^k from E at length2k+2.

These count production sequences, not distinct strings. Linearity
means there is only one variable to rewrite, so no spurious rewrite
ordering multiplies a derivation count. They are finite since each
nonterminal step adds a letter.

Eliminating E for two consecutive steps gives

    P(w)=10w, Q(w)=1w0, R(w)=0w1, S(w)=w01.

All four are legal distinct two-production choices and injective
maps on word sets. For w_k=(10)^k1, k>=1, Q cannot be outermost
because it ends0 and R cannot because it begins0. Both P and S
strip to the SAME w_(k-1), and they are different production pairs.
The seed w0=1 has one derivation. Therefore, exactly,

    d_O(w_k)=2*d_O(w_(k-1))=2^k.

No other outer forms or derivative parse orders have been missed.

The derivation equations over ordinary counting coefficients are

    A_der=z+2z E_der, E_der=2z A_der.

They give A_der=z/(1-4z²), E_der=2z²/(1-4z²), and

    A_der+E_der=z/(1-2z).

Thus total multiplicity at length n is2^(n-1). Since the number
of DISTINCT outputs is b_n and its accepted nth root tends to
lambda<2, the mean multiplicity has nth root tending to2/lambda>1.
There is a genuine exponential loss, not just ambiguity at101.
It defeats a subexponential-ambiguity transfer for THIS grammar.
It does not prove inherent ambiguity of B or exclude a different
unambiguous linear grammar.

## 4. All six intersections and the endpoint J0

Let a_k=|O_k| and e_(k+1)=|E_(k+1)|. Define the DISTINCT parameters

    I_k=#{t of length2k : t0,0t both in O_k},
    J_k=#{(u,v) in O_k² : 10u=v01}.

For J, u determines v; this is not an independent pair multiplicity.
The four odd images have total nominal size4a_k. Their complete
intersection classification is:

| Pair | Exact relation or disjointness | Count |
|---|---|---|
| P,Q | 10u=1v0 iff0u=v0 iff u=t0,v=0t | I_k |
| P,R | Different first letters1,0 | 0 |
| P,S | 10u=v01 | J_k |
| Q,R | Different first letters1,0 | 0 |
| Q,S | Different last letters0,1 | 0 |
| R,S | 0u1=v01 iff0u=v0 iff u=t0,v=0t | I_k |

Injectivity makes the listed parameter counts the cardinalities of
the intersections. Each triple of the four images contains a
disjoint pair, so all triple and quadruple intersections are empty.
Ordinary set inclusion-exclusion therefore gives

    a_(k+1)=4a_k-2I_k-J_k.

The even set is0O_k union O_k0. Its intersection is the same
0u=v0 parameter set, hence e_(k+1)=2a_k-I_k.

At k0, O0={1}, so I0=0. But10*1=1*01, so J0=1, not0.
The first recurrence thus gives a1=3, exactly the three distinct
images011,101,110;101 is the duplicated P/S image. This is an
essential endpoint check, not a table extrapolation.

For k>=1, equality10u=v01 forces u=t01,v=10t with |t|=2k-1,
and conversely those two memberships give a J pair. At k0 those
fixed ends overlap in101, so a negative-length middle parameter
would be invalid. The candidate explicitly excludes that rewrite
at k0 while retaining J0 in both recurrence and series.

## 5. Injections, failed closure and the correct entropy scale

The maps t->t0 and(u,v)->u inject I_k and J_k parameters into
O_k, proving both upper bounds by a_k.

For any DISTINCT w in O_k, set u=w01=S(w) and v=10w=P(w).
Then10u=v01 and both belong to O_(k+1). Recover w by deleting01
from u, so J_(k+1)>=a_k.

For I, put t=10w1, of length2k+4=2(k+2). Directly,

    t0=10w10=Q(R(w)),
    0t=010w1=R(P(w)).

Both are in O_(k+2), and deleting prefix10 and suffix1 recovers w.
Thus I_(k+2)>=a_k. No marked position or selected derivation needs
to be recovered; these are injective maps of actual word sets.

For k>=2 the bounds a_(k-2)<=I_k<=a_k and
a_(k-1)<=J_k<=a_k squeeze their2k-th roots to lambda, since the
known roots of a_j use length2j+1 and all shifts are fixed. This
is the stated SINGLE-word scale: J may be represented by one u of
length2k+1 or by its middle t of length2k-1. It is not a claim of
rate lambda under concatenated pair length4k+2. The displayed
series explicitly use the index length2k. The k0 exception is finite
and does not change a radius. Both overlap types retain the full
output entropy in this precise scale, not a lower-entropy remainder.

The suggested closure J_k=a_(k-1) is refuted without a scan.
Take t=01110. Both ends are0, whereas every nonseed odd official
output has a last-added1 at an end. Thus t is not in O2. Yet

    R(1)=011, R(R(1))=00111,
    Q(R(R(1)))=1001110=10t;
    Q(1)=110, Q(Q(1))=11100,
    R(Q(Q(1)))=0111001=t01.

The middle-word J3 set already contains every O2 word by the
general injection, and contains this additional t. Hence J3>=a2+1.
Nothing in this counterexample rules out every other finite closure.

## 6. Formal shifts, analytic evaluation and the canceled pole

With A,E,I,J defined by the displayed exponents in the candidate,
multiply the even recurrence by z^(2k+2) and sum, obtaining

    E(z)=2z A(z)-z² I(z).

For the odd recurrence multiply by z^(2k+3). Its left side is
A(z)-a0*z=A(z)-z. Hence

    (1-4z²)A(z)=z-z³(2I(z)+J(z)).

All arithmetic is in ordinary integer/rational formal power series,
not modulo2. The coefficient and injection bounds show that A,I,J
all have radius1/lambda, including their zero parity coefficients.
The accepted strict inequality lambda<2 places1/2 strictly INSIDE
all three disks. Thus evaluation is analytic and absolutely convergent,
not a formal substitution at an unknown boundary. It gives

    0=1/2-(1/8)(2I(1/2)+J(1/2)),
    2I(1/2)+J(1/2)=4.

This checks every factor z,z²,z³ and the initial terms I0,J0.
The numerator cancels the apparent pole1/2 of1/(1-4z²).
It does not identify the true radius1/lambda, evaluate lambda,
or make the unspecified I,J rational or algebraic.

## 7. The forcing block and every weighted-bound quantifier

Fix ANY nonempty binary pattern f=f1...fm, m>=1, and L=2m.
From either state the next L nonterminal emissions alternate.
Greedily choosing the j-th required letter takes at most2j steps,
so the pattern is a subsequence of those L emissions. Choose one
such subsequence once for each start state T. At its positions emit
left and at all others emit right. This gives one fixed orientation
block h_T of length L with left projection EXACTLY f.

If this block appears internally in a complete derivation, write its
starting form u T v. After the block the form is u f U v' with a
pending variable. Earlier terminals are outside this already adjacent
f. Later rewrites occur only inside U, so they cannot insert between
its letters. Consequently the final terminal output contains f
contiguously. The assertion holds for any surrounding derivation,
not merely for a block at the beginning. It is unaffected by the
reverse chronological order of actual official additions.

A length-n derivation has exactly n-1 nonterminal choices. Partition
them into q=floor((n-1)/L) complete L-blocks and a remainder r.
Since L is EVEN, each complete block begins in the same state T
as the initial one, independent of orientation choices. Every
derivation with f-avoiding output must avoid its h_T at each of
these blocks. At most2^L-1 choices per block and2^r for the remainder
give exactly the asserted upper bound

    D_n^f <=(2^L-1)^q 2^r.

This is necessary-only filtering, so other forbidden patterns or
dependencies can only reduce the count. A stop O->1 does not occur
inside these n-1 prescribed nonterminal steps. Appropriate initial
parity ensures the final O stop. For q0, n1 or patterns longer than
the output, the bound still holds; m0 is explicitly outside scope.

Taking limsup nth roots gives at most
alpha_f=(2^(2m)-1)^(1/(2m))<2. The statement does not require
existence of an avoiding-growth LIMIT. Each distinct avoiding word
has at least one counted derivation, so the same numerical upper
bound holds for word counts. It is a bound below2, however, not
below lambda. The ambiguity calculated above prevents an automatic
transfer to ordinary growth-sensitivity for this presentation.
No such stronger conclusion is claimed.

## 8. Primary hypotheses and the conditional rational-series route

In the primary [Ceccherini–Silberstein article,2007](https://scispace.com/pdf/growth-and-ergodicity-of-context-free-languages-ii-the-4xfrjcv85s.pdf),
Definitions1.1/1.4 include the occurrence requirement, Theorems1.2/1.5
require an unambiguous presentation, and §5 counts rightmost
derivations. The solo author, electronic2006 and print2007 dates are
correct. That unweighted theorem cannot be applied to this ambiguous
grammar. LO6 has its own proof. The paper uses cumulative lengths;
summing the displayed exact-level bounds gives the same exponential
upper rate since alpha_f>1, without a distinct-word transfer.
The [2005 primary abstract](https://www.sciencedirect.com/science/article/pii/S0196885805000321)
concerns the unambiguous subclass; its full theorem is not imported.

Finally suppose B has a FINITE PROPER UNAMBIGUOUS linear grammar,
as the candidate explicitly hypothesizes rather than constructs.
Reduce it first. If a reachable variable had two derivations of one
terminal word, extending through a fixed reachable outer context
would give two start derivations of the same word. Thus all relevant
auxiliary variables are unambiguous. Different productions for one
variable yield disjoint word contributions, and insertion into a
fixed terminal context is injective. Each production i->u j v
therefore contributes exactly z^(|u|+|v|)F_j, while terminal
productions contribute their corresponding monomials.

There are finitely many variables and rules, so the system over
ordinary counting coefficients is F=t+M(z)F. Properness requires
|u|+|v|>=1 for nonterminal productions; hence M(0)=0 and
det(Id-M)(0)=1. The inverse exists formally and has rational entries
over Q(z), giving the stated rational DISTINCT-word series under
the actual unambiguity hypothesis. With ambiguity, the same equations
instead count derivations, as this grammar demonstrates exactly.
No such alternative unambiguous presentation is supplied or inferred.

## Scope and disposition

The packet gives exact output-language and overlap results, explicit
exponential ambiguity of one grammar, and a weighted avoidance bound.
It proves original-output nonregularity without claiming inherent
ambiguity or generating-series nonrationality. All failed shortcuts
remain explicit: raw two-state path counting counts derivations,
J_k=a_(k-1) is false, the overlap terms have full entropy,1/2 is a
canceled apparent pole, and a bound below2 is not a bound below
lambda. The exact lambda, a closed overlap system, ordinary
growth-sensitivity and a possible other presentation remain open.

No mathematical program, CAS, enumeration, automaton scan, native
certificate replay or author rerun was used. The one failed-closure
example was checked by its displayed legal operations, not a search.
Source browsing and metadata hashes are separate from mathematical
proof. The complete report,44-row ledger, actual source record and
input/older integrity freeze before findings are shared. I recommend
acceptance only of these scoped statements after both complete whole
audits and root reconciliation; no annual value, new enclosure or
novelty is promoted here.
