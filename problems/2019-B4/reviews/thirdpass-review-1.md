# 2019 B4(b), third pass: independent adversarial review R1

Initial blind report, completed 2026-10-16 UTC (2026-10-17 Brisbane).
Reviewer: `review_2019_thirdpass_r1`, a fresh nonconstructor agent.
Requested launch settings: `gpt-6.1-sol`, `max`. An independent effective-setting
readback was unavailable; the requested settings are not represented as verified
effective settings.

**Review disposition: no unresolved substantive mathematical objection found.**
I recommend that the coordinator consider the stated *partial* results for
acceptance after the required independent R2 audit and integration. This report
does not promote the candidate, determine the exact growth constant, establish
novelty, or certify that no later published solution exists.

This initial report was completed without reading any third-pass peer review,
peer conclusion, shared issue/status narrative, `research.md`, or shared
literature triage. The permitted second-pass acceptance register was read to
identify established inputs. I did not construct the candidate. My first
verifier was written and run for D=3 and D=7 before I inspected any third-pass
author program or raw mathematical data. I have edited only files beginning
`problems/2019-B4/reviews/thirdpass-review-1`; I made no author repair, promotion,
Git commit, push, or shared-file edit.

## Frozen target and source fidelity

The audited mathematical body is
`notes/thirdpass-bounded-separation-v1.md`, SHA-256
`3364e8c6cf23ba3ecb250f13a5873732c108b6904a68126f52f5d7234eb916d4`.
Its checkpoint is `notes/thirdpass-checkpoint-v1.md`, SHA-256
`9f7492716a68357e866279fb9b073212e7256fac18919c87ea06d43a4c548166`.

The complete 70-file author manifest has SHA-256
`ed672a1a68874ea44c2c4752dad7f1f7ef5e27e496ed4cf40d4f633cc2364b6b`.
Every one of its 70 byte counts and hashes matched before computation and
again after the mathematical/source audit. The two complete readbacks are
`thirdpass-review-1-before-freeze.json` and
`thirdpass-review-1-after-freeze.json`; both record `all_match: true`.
The manifest deliberately excludes itself and the companion 70-line hash list.
The latter was also inspected; its observed SHA-256 is
`c5833172df57dcad65572b19640807ff70b7e5c8ef49c4183566a099304b4475`.

The decisive author data hashes also match the assignment:

| Input | SHA-256 |
| --- | --- |
| `computations/thirdpass-delay7-exact.json` | `24cd54122c24fe3e13e0cbd9a4b698275e77f4b2dedec39b0dfe67b045985c56` |
| `computations/thirdpass-crosscheck15.json` | `42d142c6a3db0cb33b13b2b46a3a01772a06e002d41794725898f068e70cbecc` |
| Accepted 143-factor input `secondpass-full-obstruction24-v2.json` | `48ee03a0f7be101763ca7132a68925bcd51a5ceb030ccfbf86dab96fda315d59` |

I read the [official paper](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-paper-b_1.pdf),
page 2, and checked the definition of B and the target in (b): positive string
length n; seed 1; alternating required additions beginning with 0; and counts
of distinct resulting strings. No preliminary proof in (a) was reproduced or
investigated as a target. The four-move replacement is attributed to the
[official solution notes](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-solutions_1.pdf),
as in the accepted register. No other contest problem was investigated.

The accepted inputs I checked in the register and mathematical texts are the
marked-context growth identification, factorial canonical histories, upper
witnesses for minimal bad factors, factor-freeness, cross-bifix-freeness, and
the renewal argument. The old numerical enclosure remains an accepted input;
I do not describe this review as a new exhaustive derivation of its lower
certificate. The rigid/staircase results were read as established context,
not substituted for a theorem about all minimal factors.

## Reconstruction of the complete mathematical chain

### 1. Histories, contexts, lexicographic order, and the original sequence

Write h in {L,R}^n and let pi(h)=(u,v), where position t, numbered from zero,
writes t mod 2 onto its selected chronological tape. The actual output string
is reverse(u) 1 v. Thus every marked context has at least one history, and
every original string has at least one marked context. Fixing a seed position
in the output fixes both context tapes. Consequently the context count c_n
satisfies

    b_(n+1) <= c_n <= (n+1) b_(n+1).

There is exactly one lexicographically least history for each context, since
the histories of a fixed context form a nonempty finite set of fixed length.
It follows that counting canonical histories counts c_n, not the 2^n raw
histories and not b_(n+1) directly. The polynomial fibre bound identifies
their exponential rates. The accepted marked-context proof establishes the
existence of the original rate lambda. Equivalently, factoriality below gives
submultiplicativity of c_n and the same identification. The shift from n
moves to n+1 bits causes no asymptotic change. At n=0 there is one empty
history, one marked context and the length-one string 1; no b_0 is introduced.

If a factor is replaced by a smaller equal-context factor, both chronological
tape substrings agree at the actual starting phase. Changing that phase
complements both tapes, so equality is phase invariant. The whole history
strictly decreases in lexicographic order. Hence canonical histories form a
factorial language K, and K=Avoid(F), where F consists of minimal
noncanonical factors. F is anti-factorial: no one of its words is a proper
factor of another.

For f in F, a smaller equal-context history g cannot share f's first letter:
cancelling it would contradict canonicity of the proper suffix, with the
phase change handled by complementation. Thus f starts R and g starts L.
If the paths met at an internal common vertex, the two proper prefixes would
have the same tape prefixes, but g's prefix would be smaller. This contradicts
minimality. Their left-coordinate difference changes by at most one per
layer, so it remains strictly positive internally and returns to zero only
at the endpoint. This reconstructs the upper-witness input without assuming
that the context has only two histories. The last-letter restrictions and
the minimum length four have no exceptional length-one or empty-tape case.

I also reconstructed the accepted no-overlap argument, since renewal later
depends on it. If ab and bc were minimal bad factors with a,b,c nonempty,
embed their upper witnesses independently in abc. Their order is strict in
opposite directions at the ends of b, so the two legal grid paths meet
internally. Splice the second witness's beginning of b to the first
witness's end of b. This makes b noncanonical, contrary to its being a
proper factor of ab. For an overlap of length one the required change of
order is itself impossible in one step. Therefore every subset F_D inherits
the full set's lack of proper suffix-prefix overlaps.

### 2. The envelope restriction is valid, including factor endpoints

For two paths in one fixed legal tape grid, their difference in left
coordinates changes by at most one at a source-time step. Their order can
therefore change only through a common vertex. The pointwise lower envelope
is a legal path obtained by splicing at such vertices. The source time is
also the sum of consumed coordinates, so at a splice there is no hidden
phase or pending-bit disagreement. The upper envelope is legal for the same
reason.

Let h be any D-bubble, with a strictly upper witness P whose separation is
at most D. It is noncanonical because P starts L while h starts R. Select
a shortest noncanonical factor f of h. Its upper witness Q exists by the
minimal-factor result just reconstructed. Embed Q into h by following h
outside that factor; phase invariance makes this a legal path for the
complete fixed tape pair of h.

Outside f, Q=h and P>=h, so min(P,Q)=h. On each internal layer of f, both
P and Q are strictly above h. Thus min(P,Q) is strictly above h there and
has height at most P-h<=D. At both endpoints of f it agrees with h. Its
restriction is a legal bounded upper witness for f. This argument also
applies when f shares either or both endpoints of h. It does not require
P and Q to be distinct or require Q's original height to be bounded.

Therefore every D-bubble contains a member of the intrinsically defined
F_D subset F. Conversely every member of F_D is a D-bubble. This proves

    K_D = Avoid(F_D),       MF(K_D)=F_D.

For the minimal-forbidden assertion, anti-factoriality of F ensures that
every proper factor of a member of F_D avoids F_D; any minimal rejection
must contain one of those members and hence must equal it. In particular
the monitor's minimal exclusions are true minimal obstructions, rather
than a larger collection of artificial sound exclusions. This is the
substantive role of the envelope lemma.

### 3. Queue invariant, source parity, and truncation direction

At positive separation d, g has consumed d extra bits from the left tape
and h has consumed d extra bits from the right tape. The two FIFO queues
u,v contain precisely these unmatched bits in tape order. Before a step,
xor them with that step's mandated source bit. The present bit becomes 0.
The next phase then complements every surviving bit.

My independent implementation derives the cases by processing h's bit
event, then g's bit event, with queue heads at the low bits of integers:

* h=L must consume a leading 0 from u; h=R appends 0 to v.
* g=L appends 0 to u; g=R must consume a leading 0 from v.
* Complement the remaining queues for the next step and then enforce
  1<=d<=D, or recognize a return at d=0.

This yields exactly the candidate's four move pairs. R/L raises d and
appends 0 to both queues; R/R rotates the right queue after checking its
head; L/L does the symmetric operation on the left queue; L/R consumes
both leading zeros. At d=1 the last case empties both queues and certifies
a return. There is no zero return on any other pair. Lengths remain equal
and no queue symbol may be skipped. No cyclic-rotation or multiplicity-only
compression is assumed.

On a divergence h=R, g=L at any source phase a, the newly pending bits are
a on both tapes. Normalization with the next phase gives (1,1), irrespective
of a. New competitors are therefore spawned at every R with exactly that
state. The set S after a prefix is the union of all possible positive-height
competitor segments that have started at such divergences, have not yet
returned, and have kept height at most D at every layer. This statement
follows inductively from the event updates. If any branch returns, its
factor has equal tapes and a smaller history; rejection is sound. Every
D-bubble follows a tracked branch until its first return; rejection is
complete for D-bubbles.

Discarding a branch when its height would exceed D can miss other
noncanonical factors. It cannot create a false rejection. This is the
correct direction for K subset K_D and the upper bound. The stronger
identification with Avoid(F_D) uses the envelope lemma, not an unjustified
reversal of this truncation argument.

There are finitely many queue pairs of each length 1,...,D, so the powerset
monitor is finite for every integer D>=1. The reachable construction has a
rejecting sink conceptually. The author's exact signature refinement keeps
that sink separate and stabilizes only when all targets respect the blocks;
the quotient therefore preserves the whole language. An aborted state-cap
construction would not have supplied that conclusion. All data used here
are marked complete, and I independently finished both required builds.

The small-cap boundary is harmless: D=1 has two raw states and one accepting
quotient state with both letters looping, so F_1 is empty. The candidate's
phrase about excluding infinitely many bad histories must retain its
"in general" qualification; it is not a universal nontriviality assertion
for D=1. D=2 has six raw states and four quotient states. The empty word,
one-letter words, all-left/all-right words and departures at either source
parity cause no special failure.

### 4. Matrix and minimal-forbidden recognizers

The adjacency convention is A[i,j]=the number of letters taking state i
to j. Both letters count even if they have the same target; for example
the displayed D=3 state 8 has two transitions to state 4. For n-letter
words the count is e_start^T A^n 1. This gives the formal rational series
e_start^T (I-zA)^(-1)1, since the finite matrix inverse has constant term I.
My forward row-vector counts and the backward column-vector iteration for
the certificate use this same orientation independently.

For a factorial language, it suffices to check the proper prefix and proper
suffix of length n-1 to test whether all proper factors are admitted. A
product monitor can therefore track the complete prefix and the prefix
with its first letter dropped. It enters its accepting terminal only at
the first rejection of the former, provided the latter still accepts;
the terminal allows no subsequent letters. Thus the full proper prefix
was admitted and the proper suffix is admitted. Conversely every minimal
forbidden word reaches that terminal. This establishes the product's
language, rather than merely fitting its coefficient sequence.

### 5. Formal renewal and convergence, with no full-language regularity leak

Because F_D subset F, it is anti-factorial and has no proper
suffix-prefix overlaps. Append a letter to a K_D-word. A first forbidden
factor must end at the new letter and is unique. Conversely, a K_D-prefix
concatenated with f in F_D has no earlier forbidden crossing: any crossing
would give a forbidden suffix-prefix overlap. This is the same renewal
bijection as for full F, and proves

    a_(D,n) = 2 a_(D,n-1) - sum_j f_(D,j) a_(D,n-j),
    A_D(z) = 1/(1-2z+F_D(z)).

This is coefficientwise formal algebra. An infinite regular F_D creates no
infinite sum in a fixed coefficient, since the alphabet and length are
finite. Because A_D(z) is rational with constant term 1, its formal inverse
is rational and F_D(z) is rational. This does not imply rationality of the
coefficientwise limit F(z).

Every strictly upper witness for a length-n word has height at most
min(number of L,number of R)<=floor(n/2). Thus all members of F of length
at most 2D+1 are already in F_D, and a_(D,n)=c_n for n<=2D+1. This uses
no upper bound on the number of witnesses.

The positive counts of each factorial K_D are submultiplicative, by the
injective split of an admitted word into its prefix and suffix. The usual
subadditive argument for their logarithms gives

    rho_D = lim_n a_(D,n)^(1/n) = inf_n a_(D,n)^(1/n).

Since K subset K_D and K_(D+1) subset K_D, rho_D>=lambda and the sequence
is nonincreasing. For any fixed n, D>=floor(n/2) gives
rho_D<=c_n^(1/n). Taking the nonincreasing limit in D and then infimum in
n gives exactly lambda. No exchange of an unjustified analytic limit and
radius of convergence is involved. The assertion is nonincreasing
convergence; no strict inequality between every pair of consecutive caps
is needed or proved by inclusion alone.

The weak displayed lower enclosure also has the stated direction:
rho_D<=c_(2D)^(1/(2D)), while the accepted marked-position injection gives
lambda>=(c_(2D)/(2D+1))^(1/(2D)). Dividing the first inequality by
(2D+1)^(1/(2D)) proves the claimed lower endpoint. It does not improve
the accepted numerical lower bound at the computed caps.

### 6. The entire D=3 grammar, not a finite prefix fit

My initial integer-queue construction gave exactly 19 raw accepting states
and nine accepting quotient states. Independent Hopcroft refinement,
followed by canonical BFS ordering, reproduced every entry of the displayed
nine-state table. The minimal-forbidden product had 23 states including
its initial and terminal states, exactly matching the saved product.

I built a separate word-path NFA for

    RRLL | RRLRRLRL (RRLRL | LRLRL | LRLRRLRL)* LRLL.

The reachable product with my minimal-forbidden DFA has 31 states. I checked
acceptance equality at every product state and closure under both letters,
including the dead case. This is a complete finite language-equivalence
check. An additional independent deterministic prefix-trie parser has
21 states, and its complete product also has 31 states with equal
acceptance throughout. No regex package, author checker import or bounded
word sample is used in either equivalence argument.

Unambiguity follows directly: the three loops form a prefix code. The
R-starting loop is separate from the L-starting ones; the latter differ at
their fifth letters. The terminal word LRLL is separate from both
L-starting loops at the fourth letter. Hence every long-branch word has a
unique succession of loops followed by its terminal. The short branch
differs from the long prefix at letter four. Lengths are 4 for the short
word, 8+4 for the long branch without loops, and 5,5,8 for its loops. Thus

    F_3(z)=z^4 + z^12/(1-2z^5-z^8).

Substitution in renewal gives the candidate's rational A_3(z). I checked
the polynomial identity exactly using integer coefficients. As an
additional finite check, the formula's first 101 coefficients match the
minimal-forbidden DFA. The unrestricted series identity rests on the
complete language equivalence and unambiguity, not these 101 terms.

All runs in the grammar have length at most two, including concatenation
boundaries. The language is infinite since loops may repeat. It is a proper
subset of F: the independently checked length-14 factors
`RRLRRLRLLLLRLL` and `RRLRRRRLRLLRLL` both require minimum separation four.
The use of RRLL retains its official attribution.

### 7. Exact D=7 weighted-norm bound

My independent integer-queue/Hopcroft implementation finished the entire
D=7 build: 20,377 raw states, 11,662 accepting quotient states, maximum
57 active queue states. It constructed v=A^200 1 using exact integers
before I inspected the author vector. Every entry was positive. After
opening the author data I checked every vector entry under the complete
BFS state isomorphism, not just the extremal entries or a numerical
eigenvalue. I also regenerated the author's raw queue subsets and verified
every raw state and transition against the independent bit encoding.

With p=1834856083 and q=1000000000, all 11,662 signs

    p v_i - q (A v)_i > 0

hold. The minimum is exactly

    2474277709610765473517281655170069565260566278840834.

The minimum vector entry is exactly

    28992044787669162084686071274960499944391494615090998.

Set alpha=max_i (Av)_i/v_i. The finite positive vector and all strict row
signs give alpha<p/q. For the weighted sup norm, nonnegativity gives
||A||_v=alpha. More concretely, 1<=v/min(v), so

    a_(7,n) = (A^n 1)_start
            <= [v_start/min(v)] alpha^n.

Since c_n<=a_(7,n), taking roots yields

    lambda <= alpha < 1834856083/1000000000.

This proves the candidate strict upper bound, subject to the reviewed
interpretation of the monitor above. No irreducibility, primitivity,
simple dominant eigenvalue, approximate row extremum, or floating-point
eigenvalue is required. My exact maximum ratio and positive rational gap
to p/q are also saved in `thirdpass-review-1-provenance.json`. Earlier
floating extremum-index displays are not inputs to this argument.

## Independent finite evidence and adversarial cases

The finite evidence supports the exact finite certificates; the preceding
unrestricted reconstruction establishes their application to (b).

| Check | Completed scope and result |
| --- | --- |
| Author freeze | All 70 manifest entries match before and after |
| Independent D=3 build | 19 raw / 9 quotient; all transitions match |
| Independent D=7 build | 20,377 raw / 11,662 quotient; all transitions match |
| Residual-state semantics | All raw subsets match the independent integer encoding; all 22 D=3 and 3,782 D=7 distinct queue pairs match |
| Exact vectors | Every one of 9 D=3 and 11,662 D=7 entries equals independent A^200 1 |
| Counts | All saved D=3 lengths 0-30 and D=7 lengths 0-80 match independent forward path counts |
| Grammar equivalence | All 31 product states; second complete trie equivalence also passes |
| D=7 certificate | All 11,662 strict row signs, exact positive-vector minimum and slack minimum |
| Actual-tape grid test | All 65,535 histories of lengths 0-15, caps 3 and 7, agree with monitors |
| Original string sets | At every move length 0-15, direct legal insertion sets equal the unmarked contexts from the history enumeration |
| Known obstruction list | Every one of the 143 accepted factors through length 24 has independently verified noncanonicity, canonical proper prefix/suffix, tapes, smaller history, minimum witness width and cap-3-through-7 acceptance |

The grid program uses actual fixed tape prefixes and legal source-parity
edges, merging competitors by their consumed grid vertex. It shares no
residual-queue code with the monitor. For obstruction widths it instead
minimizes the maximum positive separation over all legal strictly upper
paths, with endpoint separation zero. Thus it searches all witnesses,
including contexts with more than two histories.

The independently computed context counts at move lengths 14 and 15 are
6,858 and 12,600, while the original length-15 and length-16 string counts
are 3,383 and 6,177. The D=3 monitor admits 6,860 and 12,608 histories;
D=7 admits 6,858 and 12,600. These differences show that the checker did
not silently identify strings, contexts, and raw histories. The D=7
agreement through length 15 also matches the general 2D+1 layer result.

Among the 143 accepted factors the exact minimum-width distribution is

    width 2: 1, 3: 8, 4: 97, 5: 15,
          6: 16, 7: 1, 8: 4, 9: 1.

For example `RRLRRRRRRLRLLLLLLLLRLL`, length 22, requires width eight and
is still admitted at cap seven. This is a concrete strict-approximation
example. I checked every supplied factor; I did not perform a fresh full
length-24 exhaustion and do not claim the finite list's completeness as
a new enumeration result. Its completeness was an accepted input.

The four length-19 minimal factors with three complete histories are

    RRLRRLRLLLRRLRLLRLL
    RRLRRLRLLRRRLRLLRLL
    RRLRRLRLRRLRLLLLRLL
    RRLRRRRLRLLRLRLLRLL.

Their minimality and minimum widths pass the same checks as the other
139. Thus the false universal two-history rigidity conjecture was neither
used in the proof nor baked into the checker. Other adversarial cases
covered in the reconstruction and small exhaustive test include odd
factor locations, odd factor lengths, empty histories/tapes, a first
return exactly at a factor endpoint, simultaneous equal-target letters,
missing rejecting transitions, all-right continuations, the universal
D=1 language, and the distinction between nonincreasing and strictly
decreasing growth approximants.

## Primary literature and theorem-hypothesis audit

The candidate proves its problem-specific transition, envelope and growth
arguments directly. No unchecked literature theorem is needed to fill a
gap. I checked the following primary source claims at the indicated level,
and retained the limitations of the frozen literature note.

* [Mohri, section 4.3](https://cs.nyu.edu/~mohri/pub/edit.pdf): the delay
  definition bounds all paths; Theorem 1 proves termination/equivalence
  under that hypothesis using residual strings. I inspected the theorem
  and proof and rendered PDF page 14. The unrestricted B4 relation has
  not been placed under those hypotheses. The candidate instead imposes
  a cap and proves a separate hierarchy; this is an appropriate use of
  the general technique.
* [Frougny-Sakarovitch, STACS 1991](https://link.springer.com/chapter/10.1007/BFb0020787):
  the publisher abstract confirms the bounded-delay synchronization
  lineage. I did not obtain its full text or the 1993 journal paper.
  Endpoint length delay and bounded residual path separation must not
  be conflated. Their bibliography supplies prior context, not a proof
  that the full canonical language is regular.
* [Béal-Carton](https://www.numdam.org/item/ITA_2000__34_2_139_0.pdf):
  section 3 requires strong connectivity and constant integer transmission
  rate on cycles. Section 4 requires additional care without transitivity.
  I read those hypotheses and visually inspected PDF page 8. Neither a
  global synchronization theorem nor irreducibility is imported into
  the B4 norm certificate.
* [Béal et al., forbidden words](https://igm.univ-mlv.fr/~beal/Recherche/Publications/fialgo.pdf):
  the primary indexed abstract concerns minimal forbidden words of a
  *factorial regular* language, and the
  [publisher record](https://journals.sagepub.com/doi/pdf/10.3233/FUN-2003-561-208?download=true)
  plus author bibliography support the 2003 citation. Direct full-file
  web retrieval timed out twice. The B4 product construction's own proof
  supplies the needed language equality; I do not claim a full-text
  theorem audit of the inaccessible paper.
* [Huschenbett-Kuske-Zetzsche](https://eiche.theoinf.tu-ilmenau.de/kuske/Publications/HusKZ14.pdf):
  their queue-action equality is equality of transformations on every
  initial queue; their normal forms use read/write projections and overlap
  width. I read the defining equivalence and Theorems 4.1/5.3. It is a
  distinct equivalence from equality of these generated context tapes.
  The candidate correctly leaves a transfer of that normal form as an
  unproved research direction.
* [Buzzi](https://arxiv.org/pdf/math/0305164): I read the constraint
  definitions, the QFT strict-entropy condition, and Lemmas 10-11 with
  their proofs, and rendered PDF page 3. Minimal-forbidden entropy can
  be strictly smaller than constraint entropy; even small follower
  entropy does not supply the desired maximum-entropy conclusions.
  Thus finite obstruction data alone do not establish QFT, meromorphy
  or an exponential tail. The candidate imports none of these conclusions.
* [Aiswarya-Manuel-Sunny](https://drops.dagstuhl.de/storage/00lipics/lipics-vol297-icalp2024/LIPIcs.ICALP.2024.125/LIPIcs.ICALP.2024.125.pdf):
  the bounded-delay/diameter discussion concerns rational relations and
  transducer distances. I checked that discussion and the relation
  definitions. A B4 rationality identification would still require proof;
  this is not a distinct-context enumeration theorem.
* The Guibas-Odlyzko DOI redirect was inaccessible in my tool. No full-text
  claim from it is used. The renewal bijection above is independently
  reconstructed, so this access limitation creates no mathematical gap.

I also read the relevant primary
[Henderson-Warnaar report](https://austms.org.au/wp-content/uploads/2025/02/Mar20-471.pdf),
printed pages 39-41. It corroborates the historical open designation of
B4(b) and the committee-leadership handover, but does not identify an
individual B4 proposer. This audit is not a fresh exhaustive search for
every later solution; global novelty and present universal openness
remain unestablished.

All six previously cached full PDFs match their saved hashes and byte
counts in my read-only verification. Their original URLs, hashes,
retrieval timestamps and the exact level of my reading are recorded in
`thirdpass-review-1-provenance.json`. No full paper was copied into this
review directory or committed. The web screenshot facility was unavailable;
the PDF skill fallback used the bundled `pdftoppm` 26.05.0 on three selected
cached pages, visually inspected the resulting images, then removed only
those three current-review temporary renders. No charge, subscription,
access bypass, external message or separately billed API was used.

## Reproduction, time limits, retained versions and disposition

Working directory for every command:

    /Users/uqmkamga/Documents/ChatGPT/Website

The standard-library verifier uses system Python 3.15.0 on macOS 26.7
arm64. It needs no SymPy or other CAS. Exact commands are saved in each
job JSON; the mathematical jobs were launched as follows:

```text
python3 problems/2019-B4/reviews/thirdpass-review-1-run.py before 20 freeze --label before
python3 problems/2019-B4/reviews/thirdpass-review-1-run.py benchmark-d3 20 build --delay 3 --cap 40000
python3 problems/2019-B4/reviews/thirdpass-review-1-run.py full-d7 180 build --delay 7 --cap 40000
python3 problems/2019-B4/reviews/thirdpass-review-1-run.py compare 60 compare
python3 problems/2019-B4/reviews/thirdpass-review-1-run.py grammar 20 grammar
python3 problems/2019-B4/reviews/thirdpass-review-1-run.py factors 30 factors
python3 problems/2019-B4/reviews/thirdpass-review-1-run.py benchmark-small 20 small --maxn 8
python3 problems/2019-B4/reviews/thirdpass-review-1-run.py full-small 180 small --maxn 15
python3 problems/2019-B4/reviews/thirdpass-review-1-run.py boundary-d1 20 build --delay 1 --cap 1000
python3 problems/2019-B4/reviews/thirdpass-review-1-run.py boundary-d2 20 build --delay 2 --cap 1000
python3 problems/2019-B4/reviews/thirdpass-review-1-run.py after 20 freeze --label after
python3 problems/2019-B4/reviews/thirdpass-review-1-run.py provenance 20 provenance
```

The supervisor records exact arguments, child PID, external deadline,
exit status, elapsed wall time and reaping, with stdout/stderr retained.
The initial D=7 full child was PID 58326, capped at 180 seconds and reaped
successfully after 4.259 seconds; its internal build/count calculation
took 3.814 seconds. The D=3 benchmark completed first. The independent
small-history benchmark through eight moves completed before the full
15-move job, whose child was reaped after 1.365 seconds. The author-comparison
child was reaped after 2.762 seconds. Every job completed with exit zero;
no timeout, incomplete state build, unrecorded native CAS operation or
remaining child was encountered. No D=8 build was attempted. The benchmark
integer rows remain in its separate stdout log; the stable small-result
JSON contains the final length-15 run.

Verifier versions are retained separately:

| Version | Role | SHA-256 |
| --- | --- | --- |
| `thirdpass-review-1-check-initial.py` | Written before author source/data; independent D=3 and D=7 builds | `4c6af7c1ecc67e31fd6c804a53fb843c4e1f534c738c91cce5573f35fa9eafa7` |
| `thirdpass-review-1-check-v2.py` | Added source/data comparisons, complete grammar products, factor audits and small grid enumeration | `96f43261b94db394061ddecd1fb0ebcf03923dbaa42d0a7b1e7ce5a99cc5036a` |
| `thirdpass-review-1-check.py` | Adds read-only provenance/hash and exact norm-maximum records | `7a2b7792cee8fae365a4805652fd9e4179bf3bf1102dfb02c35e14cc3e06157d` |

The initial independent build source is preserved byte-for-byte; later
comparison code does not retroactively turn the first computations into
author-code runs. In `compare`, the author monitor is explicitly imported
only to compare *all* its raw states with the already independently
computed monitor. The other modes do not import author mathematical code.

Authoritative account-wide weekly telemetry was available: 13% total used
at the initial check and 14% at the later check, duration 10,080 minutes,
same reset `1792745187`. This is total weekly use, not a fraction of the
remaining allowance. No new weekly window was entered; both values are
below the 90% cutoff with integration capacity left.

Open substantive issues: **none found in this initial audit**. The separate
`thirdpass-review-1-issues.md` records scope qualifications without inventing
repair requests. No author repair or re-review is currently requested by R1.
The coordinator still needs the independent R2 report and its own integration
decision. If accepted, the new status should cover the stated hierarchy,
exact D=3 language/series and the strict upper bound as partial results only.
The exact official growth value, full F(z), high-separation entropy estimates
and global novelty remain unresolved.
