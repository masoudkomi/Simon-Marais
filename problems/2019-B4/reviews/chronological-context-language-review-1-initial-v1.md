# Chronological context serialization: whole initial review 1

2026-10-17 UTC. Reviewer `/root/review_2017_coarsening_r1`, nonconstructor
of CCL. Requested gpt-6.1-sol/max; verified effective readback unavailable.
I have read no new peer CCL report, findings or coordinator reconciliation.
This complete initial is frozen before the separately assigned original
output-language counting investigation begins.

**Finding:** no substantive mathematical objection found. All fifteen
obligations pass. The conclusion is exactly that

\[
 L_C=\{u\#v:(u,v)\text{ is a chronological routing of a finite prefix
 of }0101\ldots\}
\]

is not context-free. It is not a conclusion about physical binary output
words, canonical histories, other encodings, a counting series or the
exact growth constant. Only the coordinator may promote this scope after
both blind whole audits and reconciliation.

Exact candidate:6235bytes,
SHA256`6d9446e4bb4fb81457eb8882b498c073353eaf93a546e8b56007a0adf0e613da`.
Exact author manifest:
SHA256`38fb9ca9e5db47d97c18cbfc6fd5f52283b8896e0f8637dd802da4c532d56e8c`.
I read the ENTIRE candidate, fifteen-obligation record, sources and
manifest. No mathematical program, CAS, scan, author rerun or finite-table
inference was used. The source/integrity record states exact earlier
input read limits rather than claiming fresh whole re-audits of them.

## Domain and chronological dictionary

The official 2019 B4(b) counts DISTINCT generated binary words from
seed1, under alternating additions0,1,0,1,... at either end. Its open
target is the lower/upper exponential growth of these word counts.
This CCL candidate is a restricted structural result, not that count.

A chronological history sends each successive source bit to one of two
tapes and appends it in time order. If the first tape records left
additions and the second right additions, the physical final word is
\(\operatorname{rev}(u)1v\), retaining a marked seed. This proves the
dictionary directly, in both directions, for any finite source prefix;
there are no other moves or tape constraints. Zero moves give
\((\epsilon,\epsilon)\) and serialization `#`. Its presence has no
effect on the positive-run slice below. The equality relation between
different histories and their canonical representatives is irrelevant
to this dictionary, so none of the old witness/cap theorems is needed
to prove the new slice.

## Reconstructing the ENTIRE exact slice

Let
\(R=(00)^+(11)^+\#(11)^+(00)^+\). This is regular, and every word in
it has a UNIQUE representation

\[
 0^A1^B\#1^C0^D,
 \qquad A,B,C,D\text{ positive even integers}.          \tag{1}
\]

Let the unread tapes be \(u=0^A1^B\), \(v=1^C0^D\).
Every word in R has even total tape length; a successful finite source
prefix therefore consists of complete01 pairs. Put \(m=\min(A,C)\).

For the first \(m-1\) source pairs, routing is forced to be LR. More
explicitly, before pair \(j+1\), with \(0\le j\le m-2\), the right
head is1, so its source0 must go left. The left initial zero run has
at least two letters before that move and hence still has a zero
after it, so the following source1 must go right. This proves the
induction and isolates the genuinely exceptional pair \(m\), instead
of incorrectly asserting that it too is automatically LR.

* If \(A<C\), before pair A the left tape has its last initial zero
  and the right tape has \(C-A+1\ge3\) initial ones. Its zero is
  forced left. If the following one goes right, at least two right
  initial ones remain and the left head is1. If it goes left, at
  least one of the \(B\ge2\) left ones remains and the right head
  is1. In either case the next required zero is unavailable. Remaining
  tapes are nonempty, so stopping here cannot be a successful routing.
* If \(A>C\), before pair C the left initial zero run has
  \(A-C+1\ge3\) letters. Its zero goes left and its one must go
  right, consuming the last initial right one. Both heads are now
  zero, with at least two zeros on EACH tape: \(A-C\ge2\) and
  \(D\ge2\). After any next zero, both unread heads are still
  zero, so the next required one is inaccessible. Consuming one
  additional zero does not rescue this branch.
* If \(A=C\), the final zero of the first stage must go left. If
  its one also goes left, a left one remains because \(B\ge2\),
  while the pending right head is still its last initial one.
  The next zero is unavailable. Thus this one must go right. Exactly
  A source pairs have been consumed, and the unread tapes are
  \(1^B,0^D\), at an even source time.

Only the last case survives. Each following complete pair must now be
RL: zero from the second tape, one from the first. If \(B=D\), it
finishes. If \(B<D\), after B complete pairs only \(D-B\ge2\)
right zeros remain. One zero can be taken but the next one cannot.
If \(B>D\), after D pairs the next required zero has no source.
The positive even differences exclude a one-extra-zero completion;
also the total length in (1) already excludes an odd successful prefix.
Thus necessity is exactly \(A=C\) and \(B=D\).

Conversely, if these equalities hold, the explicit history
\((LR)^A(RL)^B\) realizes the pair: the first A01 pairs give
\(0^A,1^A\), and the next B pairs append \(1^B,0^B\).
Consequently

\[
 L_C\cap R
 =S:=\{0^{2a}1^{2b}\#1^{2a}0^{2b}:a,b\ge1\}.        \tag{2}
\]

This is an equality for arbitrary run lengths, not a subfamily or
observed finite pattern. The even/positive restrictions were used where
stated and are not silently dropped. For example unequal suffix counts
can end at an odd source time without these restrictions, so a proof for
arbitrary four runs could not be substituted for this exact slice.

## Pumping: all decompositions, including the central separator

Assume S is context-free and let P>=1 be a context-free pumping length.
Take

\[
 w=0^{2P}1^{2P}\#1^{2P}0^{2P}\in S.
\]

Consider ANY decomposition \(w=uvxyz\) with \(|vxy|\le P\) and
\(|vy|>0\), as in the pumping lemma. Number its binary blocks1,2,3,4.
The equal-exponent matching pairs are(1,3) and(2,4), despite the
different letters in each matching pair. Between either matching pair
lies a full intervening binary block of length2P, as well as the
separator. A window of length at most P cannot intersect both members
of EITHER matching pair.

If v or y contains the unique separator, the pumped word
\(uv^2xy^2z\) has at least two separators and is not in S. Otherwise
the separator remains unique, even if it lies in the unpumped x.
At least one binary symbol is added. If the result has an incorrect
four-run order or an odd run length, it is outside S already. If it
retains the form (1), the original nonempty runs remain in order and
no deletion has occurred. Choose a block whose exponent increased.
Its matching block is disjoint from the ENTIRE pumping window and
cannot have increased; thus one required equality fails. A window
crossing the separator can affect blocks2 and3, but these match blocks4
and1 respectively, neither of which it can reach. This case is covered,
not omitted. Every decomposition therefore fails at pumping exponent2.

The quantifiers are stronger than needed: for this one w, for EVERY
permitted decomposition, there is the SAME failed exponent2. This
contradicts the pumping lemma and proves S is not context-free.

The finite-word pumping fact used here can be reconstructed from a
Chomsky-normal-form parse tree. With finitely many nonterminals, a
sufficiently tall tree has a repeated nonterminal within a bounded
bottom portion of a longest branch. The yield of that portion has a
uniform bounded length; expanding the segment between its repeats gives
v and y, at least one nonempty, and repetition or removal preserves a
valid derivation. This is the usual |vxy| and |vy| version, with both
substrings pumped together. The candidate does not use a regular-language
pumping property in its place or assume an unambiguous grammar.

## Regular intersection and encoding scope

Context-free languages are closed under intersection with a regular
language. One direct construction annotates each grammar nonterminal
with the start and end states of a finite DFA. For each binary grammar
production, sum over the intermediate DFA state; for a terminal
production, retain precisely its actual DFA transition. A new start
symbol selects a final accepting state. Induction on derivation trees
gives exactly the original language intersected with the DFA language.
Ambiguity is immaterial. Applying this to R, if L_C were context-free
then S in (2) would be context-free, a contradiction. Hence CCL holds.

The cited constrained-shuffle context defines an input TUPLE of strings,
whose number is not fixed, and a fixed regular target. Its hardness
statement is not needed for this proof and says nothing here about
fixed-two-tape hardness. Likewise a physical output uses reversal of
one tape and forgets the marked seed. Neither a partial reversal nor
forgetting this mark can be assumed to transfer non-context-freeness.
The proof therefore makes no claim about the original output language,
canonical histories, other useful encodings, rationality/algebraicity
of generating series, or an exact growth value. Non-context-freeness
alone would not establish those conclusions. No repair requested for
the submitted scope; coordinator reconciliation remains required.
