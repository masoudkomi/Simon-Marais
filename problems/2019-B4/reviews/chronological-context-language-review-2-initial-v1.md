# Fresh initially blind WHOLE CCL audit R2

2026-10-17 UTC. Reviewer `review_2021_reasoning_j15_r2`.
Requested gpt-6.1-sol/max; verified effective-setting readback unavailable.
This is a nonconstructor recommendation, not coordinator promotion.

**Recommendation:** no substantive defect found in the exact CCL
statement. I reconstructed the complete exact regular slice, every
last-pair routing branch, every pumping decomposition and the final
closure inference. The27-row ledger covers all15 constructor obligations.
No required author repair was identified. A second complete initially
blind whole audit and coordinator reconciliation remain necessary for
promotion. Nothing here determines the official growth constant.

Target:6235 bytes, SHA256
`6d9446e4bb4fb81457eb8882b498c073353eaf93a546e8b56007a0adf0e613da`.
Constructor manifest: SHA256
`38fb9ca9e5db47d97c18cbfc6fd5f52283b8896e0f8637dd802da4c532d56e8c`.
The complete candidate, sources and15-obligation JSON were read.
The current submission has three artifacts, not a separate worklog or
mathematical program. No author code was executed.

## Independence and earlier work

I authored the earlier2019 NR1–NR4 return packet and previously audited
the moment-tail work. Those are different accepted results: their
nonregularity, strict spectral-gap and cap conclusions do not imply the
NEW CCL assertion. They are not silently used as an independent proof
of it. I did not construct, suggest or repair this new four-run slice
or context-free pumping argument. Root constructed CCL. No new CCL
peer report, findings or later root inspection was read before this
COMPLETE initial freeze; no substantive finding was sent before it.

The old chronological routing dictionary and physical reversal are
checked directly below. The new mathematical proof can be read solely
from C's explicit definition; it does not need a theorem about least
histories, forbidden factors, cap automata or growth constants. Older
own packets and all earlier frozen bytes remain unchanged.

## 1. Official scope and the exact language

The [official2019 B4(b)](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-paper-b_1.pdf)
asks for the lower and upper exponential rates of DISTINCT generated
binary strings. A choice sequence of ends is a history, not a distinct
string. Only part(b) is under investigation. No preliminary proof was
reproduced or used as a substitute for the open problem.

Starting with marked seed1, the successive added bits are0,1,0,1,... .
For any finite history h over{L,R}, let u be the bits routed to L in
chronological order and v those routed to R in chronological order.
Then |u|+|v|=|h|, and the corresponding marked physical word is

    reverse(u) 1 v.

Conversely, any partition of a finite alternating source prefix into
two order-preserving subsequences is exactly such a history. Both
directions hold also at odd source lengths and at length0, where the
pair is(empty,empty). This verifies the all-length definition, rather
than confusing it with the older even-step context classes C_k.

C is a SET of pairs: multiple interleavings for one pair do not create
multiple elements. L_C serializes those pairs as u#v. The new symbol#
is outside the binary alphabet, and # itself belongs to L_C. That
empty-pair boundary causes no exception because the regular slice
requires four strictly positive runs. Partial reversal of a component
is not asserted to preserve context-freeness. Forgetting the marked
seed is not treated as an injective encoding either.

## 2. The regular slice and the forced prefix

In the candidate's notation each plus repeats its displayed two-letter
block one or more times. Therefore

    R=(00)+(11)+#(11)+(00)+

is regular and has the unique form

    0^A 1^B # 1^C 0^D,

where A,B,C,D are positive even integers. The separator and changes of
binary letter make all four exponents unambiguous. Put t=min(A,C).

Consider reading the two prescribed tapes from the heads, while the
next source symbols are01. For each of the first t-1 pairs, v still
begins with an unread1 when the0 is required, so that0 must come from
u. After that0, u still has an unread initial0 because the pair number
is strictly below A. Hence1 must come from v. Induction gives t-1
cross-tape pairs and an even source time before the t-th pair.

At the t-th pair, taking a1 from u becomes a potential alternative if
u's final initial0 has just been consumed. It cannot be ignored. The
candidate retains this branch, and its three cases exhaust A<C,A>C
and A=C.

### A<C

The t-th pair is the A-th. Its0 must be u's last initial0, while v has
at least three initial1s immediately before this pair: C-A+1>=3.
If its1 is taken from v, u and v both begin with1 at the next required0;
v retains C-A>=2 such1s. If instead its1 is taken from u, then B-1>=1
left1 remains and v still begins with1. Again neither tape can supply
the next0. The tapes are not exhausted in either case. Thus no full
legal routing exists.

### A>C

The t-th pair is the C-th. Its0 must come from u, which has at least
three initial0s immediately before the pair, and its1 must be v's last
initial1. The residual u has A-C>=2 initial0s before any later1, and v
contains only D>=2 zeros. Either tape may supply the next0, but after
that one symbol both heads are still0. No1 is accessible. A routing
that momentarily consumes one further0 therefore still cannot finish.

### A=C

The final initial0 comes from u. Taking the following1 from u leaves
B-1>=1 left1 and at least one right1, so the next0 is impossible.
Consequently this1 must come from v and exhaust its initial run.
Exactly A complete pairs have been consumed. The unread tapes are
now precisely1^B and0^D at an even source time. There is no hidden
phase switch or unused initial symbol.

These arguments use ordinary head access and the prescribed finite
words. Equal global symbol counts alone would not establish them.

## 3. Tail, odd endpoints and constructive sufficiency

From unread tapes(1^B,0^D), each complete01 pair must route0 to the
second tape and1 to the first, as long as both are nonempty.

If B>D, after D pairs only left1s remain and the next source symbol
is0, so completion fails. If B<D, after B pairs only D-B zeros remain.
The difference is positive and even, hence at least2. Taking its first0
still leaves a required1 with no available tape1. The one-extra-zero
ending allowed by an odd alternating source prefix is therefore not
available. Equivalently, all four even exponents already force the
total source length even. No odd-length prefix can consume these
four runs exactly.

As an adversarial boundary check, removing the even-tail condition
really would invalidate that last inference: tapes0011 and11000 are
legally produced by two LR pairs, two RL pairs and a final R move.
They have B=2,D=3. This is outside R, so is not a counterexample to
the stated slice. It confirms that an unrestricted positive-run
version should not be silently substituted.

If A=C and B=D, the explicit ordinary history

    (LR)^A (RL)^B

writes0^A1^B to the first tape and1^A0^B to the second. It has source
length2(A+B), with the correct0 phase at the start of the second block.
This proves sufficiency for EVERY allowed A,B, not just for a tested
family. Necessity and sufficiency give exactly

    L_C intersect R
       ={0^(2a)1^(2b)#1^(2a)0^(2b) : a,b>=1}.       (S)

The variables a,b are independent. No string/history multiplicity,
canonicality or reversal theorem enters(S).

## 4. Pumping reconstruction for every decomposition

Assume S context-free. In the finite-word pumping lemma there is a
single integer P>=1 such that each sufficiently long word in S has
SOME factorization w=uvxyz satisfying |vxy|<=P, |vy|>0 and
uv^i x y^i z in S for EVERY integer i>=0. To contradict this, we
must defeat EVERY permitted factorization of our selected word; one
convenient factorization or one failed routing would not suffice.

Choose

    w=0^(2P)1^(2P)#1^(2P)0^(2P).

It belongs to S with a=b=P, and its length8P+1 exceeds P. Number
its four binary blocks1,2,3,4. The matched pairs are(1,3) and(2,4),
although the two central blocks2,3 use the same binary letter.

Any contiguous window vxy of length at most P misses at least one
block in each matched pair. Between blocks1 and3 lies the entire
block2 of length2P and the separator. Between blocks2 and4 lies the
entire block3 of length2P and the separator. In particular, a window
across# can touch the two central1 blocks but cannot thereby touch
either one's matched counterpart. This also handles P=1.

Fix ANY eligible decomposition. Use i=2 throughout:

* If v or y contains#, then repeating it produces at least two#
  symbols. The pumped word is not even in R.
* Otherwise the unique# is unpumped: it can lie outside the window
  or in x. Because |vy|>0, at least one pumped binary substring is
  nonempty and increases some binary block. A pumped substring that
  crosses a0-to1 transition on the left, or a1-to0 transition on the
  right, produces a forbidden reversed transition when repeated; in
  that event the word leaves R. If the required run order is retained,
  each nonempty pumped substring lies within one of the original
  four blocks, so its letters increase that same block's exponent.
* If a retained run length becomes odd, the word leaves R already.
  Otherwise choose ANY enlarged block. Its matched block is absent
  from the whole vxy window, hence from both pumped substrings. Its
  exponent is unchanged. The required equality for this pair fails.

The second bullet explicitly includes# in x with one pump on each
side: these can enlarge both central1 blocks, but those are different
matched pairs. Their untouched outer partners give the contradiction.
Empty v or empty y is permitted, but both cannot be empty. No case is
lost when x is empty, a substring meets a run boundary, or pumping
breaks more than one condition. Pumping upward cannot erase the
original positive runs or move the unique separator to a different
component. Thus every eligible decomposition fails at the SAME i=2.
This is stronger than the needed quantifier and proves S not
context-free.

## 5. Closure and source hypotheses

If L_C were context-free, its intersection with the regular R would
be context-free. The precise closure can be checked by taking a PDA
for L_C and a DFA for R: simulate both in the finite control, keeping
the DFA state unchanged on PDA epsilon moves, and require acceptance
by both. This is regular-intersection closure, not an assumption that
arbitrary intersections of two CFLs are CFLs. It contradicts(S), hence
L_C is not context-free.

The standard pumping and regular-intersection statements were freshly
checked in [Michael Sipser's MIT18.404J Lecture5, slides2–5](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/18c8cd00b14d48dc5865f3bdc41abd76_MIT18_404f20_lec5.pdf).
The proof uses their ordinary finite-word forms; it requires neither
ambiguity restrictions nor determinism of the PDA. The pumping
notation above translates the notes' notation without moving the
unpumped middle or dropping the bounded-window condition.

The candidate's [Amarilli–Paperman ICALP2018 paper](https://paperman.name/data/publi/10.4230.LIPIcs.ICALP.2018.115.pdf)
was freshly inspected at §2's shuffle definitions and §3's
Theorem3.6 statement and proof sketch. Its input tuple can have a
variable number of strings. Its hardness assertion is context only;
it neither proves the present fixed-two-tape assertion nor implies
hardness for the official enumeration. CCL's symbolic proof stands
without that complexity theorem. No external source about growth,
algebraicity, canonical histories or their grammars is imported.

## 6. Scope and recommendation

This establishes the proposed obstruction for exactly the separator
serialization of chronological pairs. It does not identify L_C with
canonical histories or official unmarked binary strings. It does not
show non-context-freeness after partial reversal, rule out every
encoding or grammar, prove a nonrational/nonalgebraic series, or
evaluate lambda. The earlier numerical enclosure and official open
growth determination are unchanged. There is no novelty or full
annual-solution claim.

All new inferences were reconstructed symbolically for arbitrary
finite exponents. No mathematical program, CAS, routing scan, finite
table, constructor rerun or enlarged automaton was used. Only reading,
ordinary source browsing and administrative fingerprint/JSON checks
occurred. The separate integrity records freeze this report, the
per-inference ledger, actual source scopes and input/older packet
hashes. I recommend acceptance of CCL in this precise partial scope
if the other complete whole audit and root reconciliation agree.
