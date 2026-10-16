# Deeper rational-base literature and a signed-digit coding lead

2026-10-16 UTC. Literature checkpoint and **candidate mathematical lead —
unverified**. The coordinator constructed the deductions below; they have
not received the two independent audits required for promotion. The accepted
fixed-offset density-one theorem remains partial. No proof of universal
equality is claimed, and preliminary part (a) is not investigated.

## What was actually read

Akiyama, Frougny and Sakarovitch, *Powers of rationals modulo 1 and rational
base number systems*, Israel J. Math. 168 (2008), 53–91,
[author manuscript](https://perso.telecom-paristech.fr/jsaka/PUB/Files/RBNS-rev.pdf):
the introduction, the full statement and proof of Proposition 13 (§3.3,
manuscript p12), and the hypotheses of the restricted-fractional-part results
were inspected. Proposition 13 normalizes a finite signed digit alphabet
containing the usual digits by a finite **right** transducer. Its transition
is q*z+d=p*z_next+a. This is a useful existing construction, rather than a
new transducer technique. The restricted-interval application in Theorems
3/49 requires p>=2q−1. For p/q=11/10 this fails: 11<19. It supplies no
universal equality conclusion here.

Andrieu, Eliahou and Vivion, *A Normality Conjecture on Rational Base Number
Systems*, [arXiv:2510.11723v2](https://arxiv.org/abs/2510.11723v2), 7 April
2026: the introduction, Conjectures 1.2/1.6 and Theorem 1.7 were inspected.
The proposed normality of minimal/maximal words and of scalar ceiling-map
orbits is still conjectural in this source. No all-integer normality theorem
was found there. Even a valid theorem for ceil(11*x/10) would require a
separate correspondence with this contest recurrence. The previously saved
(599,600) example disproves the simplest identification.

Rigo and Stipulanti, *Automatic sequences: from rational bases to trees*,
DMTCS 24:1 (2022), #25, [journal record](https://dmtcs.episciences.org/en/articles/9725),
[full PDF](https://dmtcs.episciences.org/en/articles/8455/download), also
[arXiv:2102.10828v5](https://arxiv.org/abs/2102.10828v5): the relevant tree
definitions and §4, especially Theorem 20 and Corollary 21, were read.
An already p/q-automatic sequence is a coding of a fixed point of a
q-block substitution with image length p. Establishing automaticity is a
hypothesis, not a consequence of noticing bounded residues. The paper's
periodic labeled-tree signature is a precise possible target for a future
coding proof. Its rational-base integer language is not a regular language.
The journal PDF is marked CC-BY 4.0; it is nevertheless kept in local cache.

Akiyama, Marsault and Sakarovitch,
[*Auto-similarity in rational base number systems*, arXiv:1305.6757v1](https://arxiv.org/abs/1305.6757v1),
was located as a further original source. Only its abstract/metadata were
checked in this pass. No detailed theorem from it is imported.

These searches did not locate an exact earlier solution of the simultaneous
recurrence. That bounded search finding does not establish absence from the
literature or originality of the deductions below. Johan Meyer's explicit
2022 proposer credit and its first-person origin story are documented in
`sources/problem-provenance.md`; committee membership is not used to guess
other setters. No person was contacted.

## A finite signed alphabet for the actual quotient

Use the accepted quotient identities from
`../proofs/reviewed-partials-v1.md`, with Q denoting its quotient q:

    b=60Q+r, 0<=r<60, d=a-b,
    c=3*floor((r+d)/30),
    b_next=66Q+r+c, r_next=b_next mod60,
    Q_next=(11Q+h)/10, h=(r+c-r_next)/6.

For this coding question only, we use the attributed eventual strip
−13<=d<=23 as established context, without proving it. Write t=Q mod10
and s=6t+r+c. Then

    h = 10*floor(s/60)-t.                                  (C1)

Within the strip, c belongs to {−3,0,3,6}, and −3<=s<=119.
If floor(s/60)=−1 then t=0, since r+c>=−3. This gives h=−10.
If the floor is 0 then −9<=h<=0; if it is 1 then 1<=h<=10.
Thus the actual correction alphabet is contained in

    D={−10,−9,...,10}.                                    (C2)

This sharpening of a bounded-error identity is a candidate deduction, not
a new research claim about rational-base systems. The negative digits are
essential: (a,b)=(599,600) gives Q=10,r=0,d=−1,c=−3,
r_next=57,h=−10,Q_next=10, whereas ceil(11Q/10)=11.

Define a finite word's value, with digits ordered from most significant
to least significant, by appending d via V -> (11V+d)/10. If sigma(Q0)
is the canonical 11/10 representation of Q0, repeated substitution in the
actual recurrence gives the exact finite identity

    value(sigma(Q0) h0 ... h_(N−1)) = Q_N.                 (C3)

Here each finite prefix represents the corresponding nonnegative integer
quotient. This records the actual state-dependent corrections, rather than
replacing them by scalar ceiling digits. It does not identify the sequence
of h's with the canonical representation of one fixed ordinary integer.

## Reusing the published right normalizer

In Proposition 13 take p=11,q=10,e=max D=10,f=min D=−10.
Its accessible carry bounds become

    z_max=floor((e-p)/(p-q))+1=0,
    z_min=ceil((f+1)/(p-q))−1=−10.

Thus its normalizer has eleven accessible carry states −10,...,0, with

    10z+d = 11z_next+a,   0<=a<=10,
    z_next=floor((10z+d)/11).                             (C4)

The candidate code verifies closure and reachability of all eleven states
using exact integers. The initial carry is 0 and the input is read from its
least significant end. The source final-output rule allows nonnegative
final carries; among these states that means 0. Correct handling of the
canonical initial prefix and final carry is essential when constructing a
product language. The finite checks below confirm final carry 0 for their
actual integer examples; they are not a general infinite-language proof.

The proposed next research step is a product of the known (d,r,t) control
with this published finite normalizer, treating the canonical initial
prefix as an explicit boundary condition. Before computing that product,
one must specify which direction is read, how unknown higher quotient
digits are represented, and exactly which finite or infinite paths
correspond to ordinary integer starts. Right normalization of successively
longer finite words need not give a causal forward conjugacy. A finite
state graph can also have nonperiodic infinite paths; strongly connected
components alone would not force an ultimately periodic full residue
state. The accepted no-periodic-state result therefore does not close the
ordinary-integer exceptional-set gap.

## Bounded exact evidence and review boundary

`../computations/deep-literature-coordinator-signed-digits-v1.py` enumerates
all 37*60*10=22,200 strip/controller states, checks (C1)/(C2) and the actual
simultaneous recurrence at two positive representatives per state, and
checks each one-step finite-word normalization. It independently evaluates
word values using Fraction arithmetic. It also checks all 231 transitions
of (C4), their closure/reachability, and four explicitly listed 40-step
integer examples. These are complete finite checks at their stated sizes.

The external supervisor gave PID60127 a 30-second cap; it exited0 after
4.243244 seconds and was reaped. Source, output, empty stderr, job record,
source retrieval metadata and this note are hashed in the companion
manifest. No long search, native CAS, new dependency or charge was used.
All candidate identities and their source application remain unverified
until two independent reviewers have reconstructed the mathematics.

The universal question remains: can a nonperiodic avoiding path correspond
to an ordinary positive integer start? Neither density one, finite lifting,
this normalizer, nor the cited normality conjectures answer it.
