# Initially blind WHOLE linear-output review R2

2026-10-17 UTC. Reviewer `review_2022_complexity_r2`; requested
gpt-6.1-sol/max, independently verified effective setting unavailable.
**No substantive objection found in the scoped LO1--LO6 or conditional
rational-series argument.** This is one independent whole audit, not
coordinator acceptance. Fifty inference checks cover all28 constructor
obligations. The exact growth constant remains unevaluated.

Target: COMPLETE `notes/linear-output-return-r1-candidate-v1.md`,
17,270bytes, SHA256
`b1bec632971326a661a4188135ce23d40f0fdcc6a121197aefe10d2237f6e1fa`;
constructor freeze3,511bytes, SHA256
`b1728d67d1101e3c9207fc935919c0cc4bf7c148f3af3220344729e5554b2deb`.
I read the entire main, all28 obligations, complete source audit,
worklog, self-check and source JSON. All eight frozen artifacts are
fingerprinted administratively; hashing is not mathematical evidence.

I did not construct this packet or supply its grammar/source leads.
The constructor is `review_2017_coarsening_r1`; root supplied those
leads and is conservatively excluded as an independent reviewer.
I previously audited the older 2019 moment and nonregularity-return
packets. Those roles give knowledge of accepted inputs, not authorship
of LO1--LO6. I have not read another new linear-output review, findings
or conclusions before freezing this complete report, ledger and source
record. The older accepted NR report is not a premise for the new
unmarked-word claims. My intervening 2020 r4 construction is separately
frozen and unchanged.

No mathematical program, finite enumeration, scan, CAS, certificate
replay or constructor rerun was used. All checks below are symbolic.
Only the assigned new review prefix is written. No candidate, old
review, shared file, Git state or cache is changed.

## Domain and accepted premise

The official2019 B4(b) counts DISTINCT binary outputs from seed1,
adding0 at either end at odd length and1 at either end at even
length. No other words are admitted. It asks for the limiting root
rates, not a number of histories. I reopened the actual official
PDF, page2 B4, and the complete local statement. Part(a) is not
investigated or reproved here.

I reread the COMPLETE accepted `proof.md`, including its marked-fiber
growth proof, and its acceptance record. The mathematical premise
needed by this candidate is precisely

\[
b_n^{1/n}\longrightarrow\lambda<2.
\]

The distinction between the original words and marked contexts is
preserved. The accepted proof's surjection has at most n marked
positions above a length-n word; its submultiplicative context counts
give the odd-level limit, and monotone adjacent lengths give the
all-length one. The existing strict upper certificate is accepted
input; I read its written inference and did not rerun its arithmetic
or old finite counts. Other accepted second/third-pass and NR registers
were checked for scope. Their canonical languages are never substituted
for the present original outputs.

## LO1--LO2: exact grammar and original-word nonregularity

Let \(O_k=B_{2k+1}\) and \(E_{k+1}=B_{2k+2}\). Removing the
last official addition from an even output removes a0 from one end
and leaves an odd output. Removing it from a nonseed odd output
removes a1 and leaves an even output. Conversely either wrapping is
one legal official addition. Induction on length therefore gives
exactly the two state languages of

\[
O\to1\mid1E\mid E1,\qquad E\to0O\mid O0.
\]

The seed is the only terminal production, and there is no empty
word. Every nonterminal production adds one symbol, hence the
grammar is linear, chain-free and epsilon-free. Each variable is
reachable and productive, and the dependency graph has both
directions between O and E. For a formal single start language B one
may take the disjoint parity union of the two starts; the candidate
does not claim that starting only at O produces even words. Its
combined counts are defined explicitly by parity.

The mandated symbol totals are k zeros/k+1 ones at odd length and
k+1 of each at even length. Within the regular slice \(0^*1^*\),
this is necessary for the displayed forms. It is sufficient there:
the legal two-move wrap \(w\mapsto0w1\) repeatedly gives
\(0^r1^{r+1}\) from seed1, including r=0, while prepending0 to
\(0^{r-1}1^r\) gives every \(0^r1^r\), r>=1. Thus both
slice equalities are exact, not guesses from a few words.

For the odd slice, a regular pumping length P applied to
\(0^P1^{P+1}\) has a nonempty pumping segment entirely among
the initial zeros. Pumping it out violates the symbol difference.
The same argument applies to \(0^P1^P\) for the even slice.
Regular intersection would preserve regularity, so O and E are
nonregular. A regular B would have regular odd-length restriction O,
also impossible. This proves nonregularity of the actual unmarked
outputs. It does not imply inherent ambiguity or nonrationality of
their counting series.

The occurrence condition is also correct in its stronger stated
form. Starting from either state, the symbols emitted on successive
nonterminal productions alternate. Any binary word w is a subsequence
of a sufficiently long alternating prefix. At its selected occurrences
emit left, and send every skipped symbol right. In a sentential form
\(uTv\), a left emission appends to u immediately before T, while
a right emission goes after T. Hence the selected letters become one
contiguous left block w, yielding \(wUv'\), not merely a scattered
subsequence of the terminal result. Complete U to a nonempty word.
Then w is a proper factor, from each starting state. This verifies
the extra source occurrence condition without asserting unambiguity
or admitting every word at its own length.

## LO3: derivations are not terminal words

A derivation of a length-n terminal word uses exactly n-1
nonterminal productions, each with two left/right choices, followed
by O->1. Odd n uses start O and even n uses start E. Alternation
ensures that every such orientation sequence reaches O at the
required stopping time. Thus the total is \(2^{n-1}\), or
\(4^k\) and \(2\cdot4^k\) at the stated levels. Distinct
production sequences may have the same terminal string.

For \(w_k=(10)^k1\), the only possible two-step outer operations
are \(P(w)=10w\) and \(S(w)=w01\): the alternatives
\(Q(w)=1w0\) and \(R(w)=0w1\) have a wrong endpoint.
Stripping P or S from \(w_k\) gives precisely \(w_{k-1}\).
Both choices are legal and are different production sequences.
With the seed multiplicity1, induction gives exactly \(2^k\),
not merely a lower bound on ambiguity.

The two-state equations consequently give
\(A_{\rm der}=z/(1-4z^2)\),
\(E_{\rm der}=2z^2/(1-4z^2)\), and combined
\(z/(1-2z)\). These count derivations. Dividing the coefficient
\(2^{n-1}\) by the actual \(b_n\) and taking nth roots gives
\(2/\lambda>1\). Thus even mean multiplicity is exponential.
The presentation cannot be assigned a subexponential ambiguity loss.
This is not a proof that every grammar for B is ambiguous.

## LO4: all intersections and the short J endpoint

Each of P,Q,R,S is an injective actual legal two-move operation on
odd outputs. The union of their images is exactly \(O_{k+1}\).
I reconstructed all six intersections separately:

- P/R and Q/R have incompatible initial bits; Q/S have incompatible
  final bits. All three are empty.
- \(P(u)=Q(v)\) reduces to \(0u=v0\). This forces
  \(u=t0,v=0t\), uniquely, and gives \(I_k\).
- \(R(u)=S(v)\) reduces to the identical equation and gives a
  second intersection of size \(I_k\).
- \(P(u)=S(v)\) is precisely \(10u=v01\), so it gives
  \(J_k\) in the candidate's ordered-pair definition.

Every triple contains one of the three empty pairs. Thus there are
no higher intersections to restore, and ordinary inclusion-exclusion
gives \(a_{k+1}=4a_k-2I_k-J_k\). The even image union
\(0O_k\cup O_k0\) has the same uniquely parameterized overlap
\(0u=v0\), yielding \(e_{k+1}=2a_k-I_k\).

At k=0, \(O_0=\{1\}\), the empty t does not pass the I-test,
and \(10\cdot1=1\cdot01\) does pass the J-test. Hence
\(I_0=0,J_0=1\). For k>=1 only, the J-equation forces
\(u=t01,v=10t\) with \(|t|=2k-1\). At k=0 those prescribed
ends overlap, so the middle-word formula is invalid. The candidate
retains that exceptional overlap and loses no shortest output.

## LO5: recoverable overlaps, full entropy and failed closure

The upper bounds project I to \(t0\in O_k\) and J to its
first component \(u\in O_k\); in the latter case the equation
uniquely determines v even at k=0. For every \(w\in O_k\),
\((u,v)=(w01,10w)\) is a J-overlap at level k+1 and recovers
w from u. For I, choose \(t=10w1\), of length2(k+2). Then

\[
t0=10w10=Q(R(w)),\qquad 0t=010w1=R(P(w)).
\]

They belong to \(O_{k+2}\); deleting the fixed decorations
recovers w. These are injections of word sets, with the exact
one-level J and two-level I shifts. No history multiplicity is
inserted into their count.

It follows for k>=2 that
\(a_{k-2}\le I_k\le a_k\) and
\(a_{k-1}\le J_k\le a_k\). The accepted odd-level limit,
with exponent denominators compared to2k, squeezes both roots to
\(\lambda\). The nonnegative power series A,I,J all therefore
have radius \(1/\lambda\), despite their parity-zero coefficients.
In particular the overlaps are not lower-entropy corrections.

The proposed shortcut \(J_k=a_{k-1}\) is indeed disproved by the
specific hand witness t=01110. An odd nonseed output must start or
end in its outer added1, so t is not in \(O_2\). Yet

\[
10t=Q(R(R(1)))=1001110,\qquad
t01=R(Q(Q(1)))=0111001.
\]

Both are in \(O_3\). The general J injection realizes the
whole \(O_2\) as middle words, and this is one additional middle
word outside it. Hence \(J_3\ge a_2+1\). This is an exact
counterexample to the attempted closure, not a numerical table or a
counterexample to the candidate's retained claims.

Multiplying the two coefficient recurrences by their specified
powers gives exactly

\[
E=2zA-z^2I,\qquad
(1-4z^2)A=z-z^3(2I+J).
\]

The seed term is z, and the factor on the overlap series is z^3,
including their k=0 coefficients. Since \(\lambda<2\), each
of A,I,J is analytic in a neighborhood of1/2. Substitution there
gives \(2I(1/2)+J(1/2)=4\). The zero denominator in a weighted
matrix calculation is canceled; this equation neither identifies
the actual singularity \(1/\lambda\) nor evaluates it.

## LO6: the all-n weighted bound

For a nonempty binary pattern f of length m, greedy selection
places its jth letter by position2j in either phase of alternating
emissions. Fix the resulting positions within L=2m. Send exactly
those m letters left and all remaining letters right. This gives
one specific orientation block \(h_T\) for each possible current
state T. Its left projection is exactly f.

Crucially the block works at an arbitrary interior point of a
derivation, not merely at its start. From \(uTv\), it produces
\(ufUv'\). Later substitutions inside U cannot split the already
adjacent letters of f; previous outer context is outside that block.
Every f-avoiding terminal derivation therefore avoids \(h_T\) at
any aligned occurrence with state T.

Partition the n-1 choices into q full L-blocks and remainder r.
L is even, so all those block starts have the initial state. At
least one of the \(2^L\) choices is forbidden in every block,
independently of the preceding outer context. At most
\((2^L-1)^q2^r\) orientation sequences remain. When q=0,
including n=1, this is the trivial count bound; no zero-length
production or invalid final state is introduced. This proves the
claimed inequality for every n>=1.

Taking limsup nth roots gives the weighted avoiding rate at most
\(\beta_m=(2^{2m}-1)^{1/(2m)}<2\). A distinct avoiding word
has at least one such derivation, so its count is also bounded, but
this gives no generic strict comparison with \(\lambda\) for
every pattern. In particular \(\beta_m\to2\) as m grows.
The comparison supplied is with derivation growth2. A special short
pattern may admit a stronger comparison using other bounds; that
would not establish the universal ordinary growth-sensitivity
assertion excluded by the candidate.

## Conditional rationality and primary theorem boundary

The conditional finite unambiguous linear route is correct. In a
reduced such grammar, a reachable variable's two derivations of
one terminal word would extend through the same fixed outer context
to two start derivations. Hence each variable is unambiguous. Within
one production, adjoining fixed terminal prefixes/suffixes is injective;
across productions the contributions are disjoint by unambiguity.
Their length series therefore satisfy \(F=t+M(z)F\). The stipulated
positive terminal length on every nonterminal production gives
\(M(0)=0\), so the finite matrix inverse exists formally and has
rational entries by the determinant formula. An ambiguous grammar
instead gives derivation series, as LO3 exhibits. No such unambiguous
presentation of B is supplied by the conditional argument.

I checked the actual2007 primary definitions and relevant proof
passages, not just its abstract. Definition1.1 includes the extra
occurrence condition; Theorems1.2/1.5 require unambiguity. Section5
defines weights by rightmost derivation counts. The current grammar's
same-word multiplicities prevent an unweighted import. The paper
uses cumulative lengths, whereas the candidate uses exact lengths:
the former has rate2 for these full derivation counts as well, and
the explicit bound above also bounds cumulative avoidance at rate
at most \(\beta_m>1\). Thus this convention difference does not
create a hidden word-count conclusion. No external growth theorem
is needed to prove LO1--LO6.

The2005 lead was checked at a primary publisher-indexed abstract
and against the2007 paper's own discussion. No unread full theorem
is used. Source retrieval limits, solo authorship and electronic/
print dates are recorded separately. I do not claim a new full
external-paper proof audit or a newly retrieved binary hash.

The complete scoped argument passes this initially blind audit.
Root must still reconcile the other independent whole report before
any promotion. The overlap hierarchy is not closed, ordinary
growth-sensitivity is not established, another unambiguous grammar
is neither constructed nor excluded, and the official exact limit
remains unknown. No novelty or new numerical enclosure follows.
