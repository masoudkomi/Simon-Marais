# Initially blind WHOLE AF R2: auxiliary presentations of the even context monoid

2026-10-17 UTC. Reviewer `/root/review_2017_coarsening_r1`.
Requested gpt-6.1-sol/max; independently verified effective readback
unavailable. **Independent whole initial report, not coordinator
promotion.** I did not construct or contribute to the NEW AF1/AF2
argument. My older2019 linear-output construction and CCL review
roles are disclosed; they are not independent re-audits of those old
inputs. I did not construct the accepted secondpass rigid-family
theorem. I read no new AF peer report, ledger, finding or comparison
before freezing this complete initial packet.

Target: `notes/auxiliary-presentation-r1-candidate-v1.md`,8849 bytes,
SHA256 `a0cc010860ee21155239421bef44e95e3ce2cec84be6796a9e067b39afcf4372`.
The entire six-record submission, all10 obligations, full accepted
rigidity text, acceptance register and exact acceptance scope were
read. No constructor selfcheck was substituted for reconstruction.
No mathematical program, CAS, enumeration, source-certificate replay
or author rerun was used.

## Whole conclusion and exact boundary

I found no substantive defect in AF1, AF2 or the two stated algebraic
consequences. The argument proves the SAME even phase-zero image
monoid is not finitely presented on any finite alphabet. It correctly
uses the already accepted fixed-generator obstruction and a classical
change-of-generators lemma, rather than reporting the old obstruction
as a new theorem. No author repair is required by this initial audit.
The result gives no numerical growth improvement or annual answer.
Coordinator promotion still requires the other initially blind whole
audit and reconciliation of both complete reports and source records.

## 1. Official object versus the algebraic object actually studied

The official2019 B4(b) counts DISTINCT binary strings generated from
the seed1 by alternating which bit may be appended/prepended, and
asks for the lower and upper exponential growth limits. I read the
actual official B4 text. No part(a) proof is reconstructed here.

AF studies the image M0 of X* for X={A,B,C,D} in the direct product
of two binary free monoids, under componentwise concatenation:

    A=(01,epsilon), B=(0,1), C=(1,0), D=(epsilon,01).

This is an ordinary monoid homomorphism because one block always
consumes the same two phase-zero source bits01. After an even number
of source bits the phase resets, so concatenating two blocked histories
concatenates their chronological tape words. The empty X-word maps
to the empty pair and is the identity. No extension of this ordinary
product to arbitrary odd histories is asserted or needed. In
particular the proof need not identify M0 elements with unmarked
output strings or infer a counting presentation for those strings.

Every generator contributes total tape length2. Consequently, for
the image map pi,

    |pi(w)_left|+|pi(w)_right|=2|w|.

Thus equality in M0 implies equality of X-word lengths. In particular
no positive X-word represents the identity. This explicit length
grading will block a hidden empty-factor insertion in the application.

## 2. Reconstructing the accepted rigid input and proper-factor claim

The accepted secondpass theorem gives, for every p,q>=1, exactly
two histories of (U_q,V_p), with U_q=01(10)^q01 and
V_p=01(10)^p01:

    K=A C A^(q-1) B^2 D^(p-1) C D,
    H=D B D^(p-1) C^2 A^(q-1) B A.

I checked the forced-choice proof rather than the old finite checks.
Initially both tape heads are0 and their following bits1. The first
01 pair must therefore lie entirely on one tape: either A or D.
If A is used, the remaining heads force the next0 from the right.
Taking the following right1 would leave both heads1 before the next
required0, so its paired1 must come from the left, giving C.
Thereafter taking a left0 with a right1 too early produces the same
dead heads; the next q-1 pairs are forced A. The tapes become001
and1(10)^p01. The next B is forced by these heads. Taking A after
it would exhaust the left tape and leave a right1 at a required0,
so a second B is forced. With only the last left1 remaining, using
it too soon would again leave an initial right1 at a required0;
this forces D^(p-1), then the final C D. This is K. Exchanging
the tapes sends A to D and B to C and exchanges p,q, giving exactly
H. Empty powers when p=1 or q=1 create no exception. Direct
concatenation gives the stated target tapes for both histories.

The two X-words have length p+q+4. Their first letters A/D differ,
and their final letters D/A differ. If a PROPER contiguous factor u
of H had a different same-image prehistory v, homomorphism allows
its replacement in H. The length grading gives |u|=|v|, so the
replacement is a different full word. At least one endpoint of H
lies outside the proper factor and remains unchanged. The new word
therefore cannot be K, whose two endpoints both differ from H's.
It is not H either, hence would be a forbidden third history. The
same proof works with K and for prefixes/suffixes touching exactly
one endpoint. The empty factor has only the empty prehistory by
the grading. This validates the exact unique-factor premise used
by AF. The old acceptance explicitly covered the fixed-X equation
obstruction but withheld the auxiliary-generator conclusion; AF
addresses that withheld scope by an additional elementary lemma.

## 3. AF1 with all maps and both congruence inclusions

Let M be generated by a finite alphabet X via e_X:X*->M, and let
theta:Y*/cong(R)->M be an isomorphism for a finite presentation
with Y,R finite. For every y choose p_y in X* with image theta(y),
and for every x choose q_x in Y* with theta(q_x)=e_X(x).
Surjectivity supplies all choices, including identity-representing
generators and empty words. Extending gives free-monoid maps
p:Y*->X* and q:X*->Y*. They are not claimed to be inverse on
free words. The actual identities are the evaluation identities
e_X p=theta e_Y and theta e_Y q=e_X.

Form the finite set

    S=p(R) union{(x,p(q_x)):x in X}.

Both types of equations are sound in M by those evaluation
identities. Since actual equality is a monoid congruence containing
S, the S-congruence is contained in actual equality.

For the converse, e_X(w)=e_X(w') implies q(w) and q(w') are
equal modulo R. The congruence generated by R is exactly the
relation of FINITE contextual replacements using R in either
direction: finite replacement chains form a congruence containing
R, and every congruence containing R contains every such chain.
This also gives a direct proof of that definition-level fact.
For a step alpha u delta -> alpha v delta, applying p gives
p(alpha)p(u)p(delta) -> p(alpha)p(v)p(delta), a valid contextual
step by p(R). If both images coincide, it is a stationary step
that may be omitted. This works for erasing maps, empty contexts,
empty u/v and reversed equations. It does not require p to be
injective or contexts to be nonempty.

Finally the x equations, substituted letter by letter and using
congruence closure, give w congruent to p(q(w)) for EVERY finite
w, including the empty word. They give the analogous statement
for w'. Concatenating those two chains with the transported
R-chain proves w congruent to w' modulo S. This is the reverse
inclusion and completes AF1. No decision procedure for equality
or for choosing p,q, no group inverses, and no computability
hypothesis are concealed in this existential proof.

## 4. AF2 and attempted evasions

Suppose any finite presentation on any finite auxiliary alphabet
presented the SAME M0. AF1 would yield a finite sound equation
set S on the fixed alphabet X. If S is empty, distinct H,K are
not connected. Otherwise let m be the largest length of ANY side
of any equation in S and choose p,q>=1 with p+q+4>m. These
parameters may be chosen after the fixed finite presentation;
the presentation is not permitted to change with them.

Every sound S equation is length preserving by the grading in
Section1, including all transported equations even if the original
Y presentation was nonhomogeneous. Thus an empty side is paired
only with the empty side, which has no effect. If a derivation
from H changed its word for the first time, it would replace a
factor of length at most m, strictly shorter than H. Unique
prehistory of that proper factor forces the replacement to be
the identical X-word. This contradicts the definition of a first
change. Arbitrarily many stationary steps or uses of equations
in reverse cannot help. H is therefore isolated under S, although
K is a distinct same-image word. This contradicts AF1's equality
of congruences and proves AF2 on EVERY finite generating alphabet.

I checked possible evasion by a new identity generator, different
word lengths on Y, empty insertion/deletion rules, taking a very
long auxiliary codeword, or a derivation that changes length before
using a large relation. AF1 produces only finitely many fixed
X-equations and each is sound, so the same grading and maximum
length obstruction apply to all these cases. An embedding in a
different monoid is outside the hypotheses and is correctly not
excluded. In fact the given M0 already lives in a direct product
of free monoids; the claim is intrinsically about presentations
of M0 itself, not the complexity of the ambient container.

## 5. Consequences, source scope and limits

A finite complete rewriting system that presents M0 provides a
finite set of equations after forgetting orientation. Regardless
of termination/confluence details, its presented congruence would
be a finite monoid presentation, contrary to AF2. A trace monoid
on finite alphabet Z has finitely many letter-commutation
equations, one for each declared independent pair. Hence it is
finitely presented; an abstract monoid isomorphism with M0 would
provide a forbidden finite presentation. These consequences
apply to the SAME abstract monoid; no encoding or ambient
embedding conclusion is substituted for that hypothesis.

Vaccaro's author-posted2010 survey was inspected at the actual
monoid congruence/finite-derivation definitions and Section9
generator-elimination context. Its scope does include monoids;
the group adaptation is explicitly separated. The survey points
outside itself for the general Tietze equivalence theorem. Neither
the candidate nor this audit imports that unread proof: AF1 is
fully established above by finite substitutions. Classical
attribution is appropriate, and no novelty claim is justified.

Non-finite presentation alone says nothing decisive about
regular cross-sections, rational two-tape relations, transducers,
finite weighted counting models, rational/algebraic growth, the
renewal defect or the exact growth value. The candidate explicitly
withholds all these assertions and the official annual question.
Old finite certificates and failed experiments play no proof role
and were not rerun. Full issue/source/integrity companions freeze
this initial verdict before any new AF peer comparison. No
substantive defect or required author repair is recorded.
