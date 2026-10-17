# AF1/AF2: fresh initially blind WHOLE review R1

2026-10-17 UTC. Reviewer `/root/review_2022_complexity_r2`. Requested
gpt-6.1-sol/max; independently verified effective settings unavailable.

**Finding:** the complete AF1 transport lemma and AF2 application survive
this audit in their written scopes. All ten constructor obligations and
the entire six-file packet have been covered. I find no substantive
defect and request no author repair. This is one independent whole
initial review, not coordinator promotion. No new AF peer report,
ledger, source record, manifest or finding has been read before this
freeze. The original growth value remains undetermined by this result.

The target main is 8849 bytes, SHA256
`a0cc010860ee21155239421bef44e95e3ce2cec84be6796a9e067b39afcf4372`;
the1705-byte constructor freeze has SHA256
`114dabe97999c84e37687c3e88b7e8f65080f93ac3477ab708e99712d0ffcbb5`.
Its five recorded companions/main plus that freeze are the six-file
packet; there are not six rows inside the manifest. Exact names are in
the new reviewer manifest. The other records are the ten obligations,
source/failures, worklog and integrity JSON. All were read completely.

## 1. Independence and exact mathematical object

Root constructed AF1/AF2 and is excluded from its independent reviewer
count. I did not construct or contribute to this new proof. My older
roles include whole reviews of 2019 NR, R7, linear-output, monotone-ratio
and walk/Fréchet packets. Those earlier reviews are disclosed background,
not new proof authority. I did not construct the accepted second-pass
rigidity theorem. This audit freshly reconstructs its needed proof after
reading its complete unchanged body and exact acceptance scopes.

The original official2019 B4(b) counts DISTINCT generated binary strings
and asks for their two root growth rates, for all positive integer
lengths. I checked its actual official statement. No preliminary (a)
argument is solved or reproduced here. The new candidate concerns a
particular context monoid that arises in this research, not equality of
all histories producing one unmarked final string.

Let X={A,B,C,D}, and let alpha:X*→{0,1}*×{0,1}* send the letters to

    A=(01,epsilon), B=(0,1), C=(1,0), D=(epsilon,01).

The operation in the target is componentwise concatenation and the
identity is (epsilon,epsilon). M0 is the image of alpha, with its actual
induced monoid structure. Each letter groups TWO consecutive moves
of the alternating phase-zero source: LL, LR, RL, RR respectively.
Every block consumes exactly two source bits, so the next block again
starts at phase zero. This is why alpha is an ordinary monoid
homomorphism. Arbitrary odd histories would require a phase action;
ordinary pair concatenation on those is not assumed. Chronological left
tape order also remains distinct from its reversal in the final output.
One must not turn this auxiliary equality relation into an assertion
about the original unmarked-string count.

Every alpha(w) has total tape length2|w|. Thus equality of images forces
equal X lengths. In particular the only word representing the identity
is epsilon. This homogeneity is about the FIXED alphabet X; a proposed
auxiliary alphabet can include identity elements or variable-length
encodings, which AF1 must handle rather than forbid.

## 2. The accepted rigid premise is exactly strong enough

I read the entire unchanged `secondpass-rigidity-obstructions.md`, the
accepted second-pass register, full acceptance MD/JSON and issue snapshot.
I also read complete canonical-renewal, staircase/pumping and checkpoint2
texts to check the linked accepted scope. Their original candidate
labels are historical; the unchanged mathematical bodies are governed
by the later acceptance register. The numerical certificates and old
enumeration scripts were not rerun. No finite check is needed for AF.

For p,q>=1 set U_q=01(10)^q01, V_p=01(10)^p01. The two accepted blocked
histories are

    K=A C A^(q-1) B B D^(p-1) C D,
    H=D B D^(p-1) C C A^(q-1) B A.

Both have length p+q+4. Their left/right concatenations are U_q,V_p,
including p=1 or q=1 when the indicated powers vanish. I reconstructed
the proof that these are ALL histories, not merely two examples:

* Both tape heads initially are0, and the next source pair is01. The
  first blocked letter can only be A or D; B/C would need an initial1.
* After A the left head is1 and the right tape begins01. Taking D next
  would leave both heads1 at the next mandated0. Hence C is forced.
  The tapes are now 0(10)^(q-1)01 and1(10)^p01.
* While the first exponent is positive, a B would again leave both
  heads1 at a zero step. The next q-1 letters are A. The remaining
  left tape is001 and the right is1(10)^p01, forcing B.
* Now the tapes are01 and(10)^p01. A would empty the left tape while
  the right begins1 at the next zero step, so a second B is forced.
  They become1 and0(10)^(p-1)01.
* A C before the last right001 would exhaust the left1 and leave a
  right1 at a zero step. Thus p-1 D's are forced. The final tapes1,001
  force C then D. The resulting history is exactly K.
* Exchanging the two tapes exchanges A/D, B/C and p/q, giving exactly
  H in the other first-letter branch. These two branches exhaust the
  possibilities. The endpoint p=1 or q=1 simply skips a loop; no
  unsuccessful branch becomes available there.

K begins A and ends D; H begins D and ends A. Suppose a PROPER
contiguous X factor of one has another X prehistory for its image.
Replacing it in the full word preserves the image, since alpha is a
homomorphism, and changes the word by free-word cancellation. The
replacement has the same length. At least one of the original endpoints
is untouched, so the resulting word cannot be the OTHER full history,
which differs at both endpoints. This would be a third history, a
contradiction. The empty factor has only epsilon as prehistory by total
length. Thus proper-factor uniqueness has exactly the form required
for a bounded-rule obstruction on X, with no parity mismatch.

This fixed-X obstruction was already accepted. The old register
expressly withheld the auxiliary-generator extension; the new candidate
does not rewrite history by calling the old result a discovery or its
scope qualification a defect.

## 3. AF1 in both directions, with all substitutions typed

Suppose a monoid M is generated by finite X and is isomorphic to a
finite monoid presentation N=<Y|R>. Let beta:Y*→N be the quotient map
and fix an isomorphism phi:N→M. Write alpha:X*→M for the chosen
generating map. For each y choose p_y∈X* with alpha(p_y)=phi(beta(y));
for each x choose q_x∈Y* with phi(beta(q_x))=alpha(x). Surjectivity and
generation give these finite choices. They extend to homomorphisms
p:Y*→X* and q:X*→Y*. In particular

    alpha p=phi beta,       phi beta q=alpha.

No identity on free words is asserted for pq or qp. Empty words may
occur in either family, and the lemma asks for existence, not an
algorithm computing them.

Take the finite X-equation set

    S={(p(u),p(v)):(u,v)∈R} union {(x,p(q_x)):x∈X}.

For the first type, beta(u)=beta(v) implies alpha(p(u))=alpha(p(v)).
For the second type the displayed substitution identities give
alpha(p(q_x))=alpha(x). Therefore all S equations are sound, and their
generated congruence is contained in ker(alpha). This does not assume
R's written sides have equal literal lengths or that Y's symbols have
nonidentity images.

For the reverse inclusion take alpha(w)=alpha(w'). Injectivity of phi
gives beta(q(w))=beta(q(w')). Equality in the monoid presentation is
equivalent to a FINITE chain of elementary R replacements, in either
direction, inside arbitrary left/right Y contexts. This characterization
follows directly because such finite chains themselves form the least
congruence containing R. Apply p to every step. A step
a u b→a v b becomes p(a)p(u)p(b)→p(a)p(v)p(b), an S replacement; if
its sides collapse to identical X words it can be omitted. Empty
contexts and empty relation sides remain valid under a monoid map.
Thus p(q(w)) and p(q(w')) are S-congruent.

Replacing each x in w by p(q_x), one occurrence at a time, gives
w≡p(q(w)) modulo S, and similarly w'≡p(q(w')). The steps are finite
even if some p(q_x) are empty; the intended occurrences can be tracked
as the original finite letter list. Concatenating these three finite
derivations proves w≡w'. Hence ker(alpha) is exactly generated by S.
This establishes AF1 on arbitrary finite generating sets, including
empty/trivial cases, without a word-problem oracle, group inverses or
a theorem about group normal closures.

## 4. AF2: any finite presentation would give the impossible first step

If M0 had any finite monoid presentation, AF1 would produce a finite
set S of sound X equations generating its equality relation. If S is
empty, its congruence is literal equality and already fails on H,K.
Otherwise let M be the maximum length of any side of an S equation.
Choose positive p,q with p+q+4>M. Each sound X equation preserves
length, since alpha has the total-length homogeneity checked above.
In particular an equation with an empty side has both sides epsilon
and changes nothing.

Consider a finite S derivation from H, and remove its trivial initial
steps. Its first genuinely changing step must match a side of length
at most M, therefore a PROPER factor of the ORIGINAL H. Soundness
would replace it by another word with the same alpha image, whereas
that factor has a unique prehistory. Its replacement is consequently
the identical word, contrary to the chosen genuine change. Arbitrary
left/right contexts and either orientation of every relation are covered
by the maximum over BOTH sides. There is no way to grow an intermediate
word before the first step; the argument already blocks that step.
Therefore H is isolated in the S congruence but alpha(H)=alpha(K) and
H≠K, a contradiction.

The quantifiers are correct: the finite alphabet, all equations and
the substitutions are fixed FIRST; p,q are then chosen beyond the
resulting finite M. Auxiliary generators that expand to very long
X words merely increase this finite M. An alphabet or a rule set
allowed to depend without bound on p,q would not be one finite
presentation. Thus M0 is not finitely presented on ANY finite alphabet.

For a finite complete rewriting system presenting the SAME monoid,
forgetting rule orientations gives a finite monoid presentation; its
termination/confluence cannot escape this contradiction. Here the
usual finite-system convention includes a finite alphabet. A trace
monoid on finite alphabet Y has only finitely many prescribed commuting
letter equations and is finitely presented. Any isomorphism with M0
would give a prohibited finite presentation. Both stated consequences
follow; no normal-form or growth conclusion is appended.

## 5. Stronger interpretations fail, rather than the candidate

The image M0 is already a submonoid of the product of two binary free
monoids by its definition. That ambient monoid has a finite presentation:
use l_0,l_1,r_0,r_1 and the four equations l_i r_j=r_j l_i. Commuting
all left letters before all right letters gives the unique pair of
component words, so this is the actual direct product. Thus the
candidate's SAME-monoid restriction is essential: non-finite presentation
does not obstruct an embedding into a finitely presented ambient monoid.
This is a direct scope check, not a new candidate claim needed by AF.

Likewise M0's relation is directly recognized by a finite one-state
word-labeled two-tape device with the four generator pairs as loops.
Such a device counts paths with collisions H,K, and therefore is not
automatically a finite presentation, an unambiguous counting model or
a rational generating series for DISTINCT outputs. This illustrates
why the candidate's rational-relation/transducer firewall is correct.
It claims neither absence of regular cross-sections nor nonrationality
or nonalgebraicity of the growth series/value.

The general transport proof is classical monoid Tietze machinery and
is properly attributed. The actual primary source definitions were
checked within the limits recorded separately. Proposition9.2's outside
proof is not needed: the finite-chain/substitution proof above supplies
the entire lemma. No claim about source complexity bounds or general
decidability is imported. No mathematical computation was run.

## 6. Completion, preservation and remaining authority

The whole initial issue ledger records all AF-01 through AF-10 plus
fourteen additional challenges. All are resolved within the written
proof; no substantive objection remains in this audit. Exact constructor
inputs and the old acceptance's14 artifact-path-to-SHA entries are
independently checked using their actual older schema. The preceding
own HC review and its preservation inventory remain immutable; metadata
verification is administrative and not an independent mathematical
certificate. Only this previously unused assigned prefix is written.

No new peer AF finding was read, no author program/certificate was
executed, and no old/shared/cache/Git byte, job or setting was changed.
No spawn, charge, contact or access bypass occurred. Direct weekly
telemetry was51% TOTAL at2026-10-17 16:29:42UTC, same reset1792745187,
with the90% TOTAL ceiling and integration reserve. The candidate needs
the other whole audit and coordinator reconciliation before promotion;
it supplies no full2019 answer, lambda value, defect or novelty claim.
