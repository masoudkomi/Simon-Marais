**Candidate proof - unverified.**

# Full rational-base fibers and the ordinary A/B obstruction

2026-10-17 UTC. Constructor `review_2022_complexity_r2`; requested
`gpt-6.1-sol` with `max` reasoning. No independent effective-setting
readback is available. The coordinator supplied the bounded-correction
lead in `coordinator-AB-bounded-correction-rigidity-v1.md` and is a
contributor to this construction, not an independent reviewer. The
constructor also authored the older accepted R0–R3/S1–S2 packet and
reviewed the separately constructed R4 packet. None of those roles is
represented as an independent audit of this new argument. Two OTHER
fresh initially blind whole audits are needed before any acceptance.

This is a restricted mathematical advance toward 2022 B4(b), not a
solution of that question. No infinite positive ordinary A/B lift is
constructed or excluded. No novelty claim is made. The rational-base
definitions and extremal-path mechanism are classical
Akiyama–Frougny–Sakarovitch (AFS); the specialized proofs below are
included in full. There is no mathematical computation, enumeration,
CAS, certificate replay, or separately billed API in this construction.

## 0. Official domain, exact input, and conclusions

The official question has positive ordinary integers, simultaneous
updates

    a_(n+1)=a_n+2 floor(b_n/20),
    b_(n+1)=b_n+3 floor(a_n/30),
    a_0 b_0>=600,

and asks whether equality must occur. Only part(b) is investigated.
The established trapping result from part(a) is attributed background;
it is not proved or studied here.

The exact accepted restricted input is the A/B loop family at controller
state(d,r)=(1,0). Write beta=11/10, gamma=121/100, and

    10Q_(n+1)=11Q_n+h_n,
    (h_(2j),h_(2j+1))=(-w_j,w_j),   w_j in{0,1},
    X_j=Q_(2j),
    100X_(j+1)=121X_j-w_j.                         (0.1)

An A block has w=0 and requires X=0 mod100; a B block has w=1 and
requires X=81 mod100. Both intermediate integer steps and the
controller return were established in the accepted R1/R4 bodies.
An infinite positive ordinary lift gives the admissible contest start
(60X_0+1,60X_0) and avoids equality. This is only a restricted family.
The accepted stopped map on positive integers is

    F(x)=121x/100          on x=0 mod100,
    F(x)=(121x-1)/100      on x=81 mod100,
    STOP                  otherwise.              (0.2)

Accepted R4 E1/E2 gives at least nine full-alphabet expansions under a
positive ordinary lift; V1–V4 proves valuation and finite-shadow results,
while preserving the missing ordinary-integer infinite-lift bridge.
R5 neither assumes a no-ninefold theorem nor fills that bridge by
compactness. In particular a source upper bound of eleven, or the
proposed improvement to ten below, still permits nine.

The proposed new results are:

* **F5A:** in a Josephus base beta=(q+1)/q, q>=2, every positive real
  has at most q admissible expansions, using the full alphabet0,...,q
  and a single fixed radix convention. This proposed endpoint refinement
  of the general AFS estimate needs independent review.
* **F5B:** after a sufficiently long common prefix level, every fiber
  of size s>=2 consists of s consecutive integer prefix values. Its
  largest path is a ceiling orbit with digits0,...,q-s+1. Consequently
  existence of an r-fold fiber, 2<=r<=q, is equivalent to an actual
  positive ordinary ceiling orbit staying in an explicit residue set.
* **F5C:** a hypothetical positive A/B lift forces exactly NINE global
  expansions, not merely nine bounded translates. It also forces an
  exact eight-point fiber of the ordinary ceiling growth map. The new
  step matches an arbitrary expansion to one common integer index;
  the coordinator's carry lemma alone did not supply that match.
* **F5D:** the unrestricted binary shadow series has a full interval
  as its REAL image, whereas its10-adic image has two-prime separated
  cylinders. Positive ordinary membership in the latter is exactly the
  still-open A/B lift problem.
* **F5E:** positive ordinary A/B lifts have both letters infinitely
  often and give a strict fractional-part necessary condition. The
  interval condition alone is not used as a binary-coding converse.

## 1. One representation convention and finite-prefix facts

For Sections1–3 fix an integer q>=2, p=q+1, beta=p/q, and
A={0,...,q}. For a finite word read from left to right set

    val(a_1...a_k)=(1/q) sum_(i=1)^k a_i beta^(k-i).

Let L be the finite canonical representations of nonnegative integers,
with zero represented by the empty word, and allow leading zeros by
using0^*L. This is the AFS modified-division convention with1/q weights;
it is not the usual greedy beta expansion on digits0,...,floor(beta).
Let W consist of infinite words a=a_1a_2... every finite prefix of
which lies in0^*L. Put

    rho(a)=(1/q) sum_(i>=1) a_i beta^(-i),
    N_k(a)=val(a_1...a_k),  N_0=0.

Every N_k is an ordinary nonnegative integer and

    qN_(k+1)=pN_k+a_(k+1).                         (1.1)

The finite assertions used later can be proved directly. Given N>0,
modified division qN=pN'+a with0<=a<p has N'=floor(qN/p)<N, so
iteration terminates. Reversing the remainders gives its canonical
word, whose earlier prefixes are integers. For an integer-prefix path,
the last digit is uniquely a=qN modp; the preceding value is then
(qN-a)/p. Iteration proves uniqueness at any FIXED word length, allowing
leading zeros. Appending any digit in A which makes(1.1) integral
therefore gives a word in0^*L. The least allowed digit is

    d_min(N)=q ceil(pN/q)-pN in{0,...,q-1};        (1.2)

such a digit always exists, so every finite admissible word has an
infinite continuation. The largest digit is in{1,...,q}; when N=0 modq
the two choices are0 andq, and otherwise the only choice lies in1,...,q-1.

We also specify global radix placement, instead of changing it separately
for different representations. A global expansion of a finite real V>=0
is an indexed digit sequence (a_i)_(i in Z), with a_i in A and a_i=0 for
all sufficiently large i, satisfying

    V=(1/q) sum_(i in Z) a_i beta^i,

and such that the finite prefixes read downward from any sufficiently
large zero index lie in0^*L. Writing extra leading zeros does not create
a different indexed sequence or a different expansion. Translation of
EVERY index by -M sends the entire fiber at V bijectively to the fiber
at beta^(-M)V. This translation preserves every finite prefix word and
its admissibility. A digit at index0 has weight1/q. Thus, if

    0<beta^(-M)V<1/q,                              (1.3)

ALL expansions of the scaled value have zero digits at indices>=0.
After those zeros they are precisely root words in W, with index-i
corresponding to a_i. This ONE common normalization covers arbitrary
finite integer parts, not just a previously selected finite family.
The expansion0^infinity is the sole representation of zero, since all
weights and digits are nonnegative. A shift of the indexed nonzero
digits changes the value by a power of beta and is not counted as an
extra expansion of the original fixed value.

## 2. F5A: the strict prefix window gives at most q expansions

For a in W and every k>=0,

    beta^k rho(a)=N_k(a)+T_k(a),
    T_k(a)=(1/q) sum_(j>=1) a_(k+j) beta^(-j).

The geometric sum bounds0<=T_k<=q. Equality T_k=q is impossible:
it would require all later digits to equal q. Starting with the integer
N_k, such a tail obeys

    q(N_(n+1)+q)=p(N_n+q).

For every m>=1 this would make q^m divide the fixed positive integer
N_k+q, since gcd(p,q)=1. Hence the correct endpoint statement is

    0<=T_k<q,
    beta^k rho(a)-q<N_k(a)<=beta^k rho(a).          (2.1)

This is the full tail value, not merely its fractional part. The lower
endpoint for N_k is OPEN, including when beta^k rho(a) is an integer.
An interval (x-q,x] contains exactly q ordinary integers for every real x.

If q+1 distinct words had the same rho value, select a common finite
level k after every pair has separated. Fixed-length uniqueness makes
their q+1 prefix integer values distinct. All of them would belong to
the interval in(2.1), a contradiction. This also excludes infinite
fibers, by selecting q+1 members. Thus each root fiber has size at mostq.
The common normalization(1.3) gives the same bound for every positive
real with arbitrary global radix placement. For q=2 the bound is two;
the zero fiber has size one. No q=1 claim is needed here.

For q10 this is a proposed upper bound TEN. AFS Proposition37, as
stated with integer k>(q-1)/(p-q), gives eleven at11/10; its separate
Corollary38 gives two only when p>=2q-1. Nothing here attributes a
no-ninefold theorem to either result. The refinement follows from
keeping the strict endpoint in the classical tail window and is not
claimed to be new in the literature.

## 3. F5B: complete fiber shape and exact ordinary residue obstruction

### 3.1 Ordered levels and absence of holes in a fiber

At level k the admissible prefix values, in lexicographic order, are
exactly0,1,...,G_k-1, where G_0=1 and G_(k+1)=ceil(beta G_k).
Here is a direct reconstruction rather than a source import. Children
of the integer N have the values

    ceil(pN/q),...,floor((pN+q)/q).

For consecutive parents N,N+1 the next interval starts exactly one
integer after the preceding interval ends, because

    ceil(p(N+1)/q)=floor(pN/q)+2
                 =floor((pN+q)/q)+1.

This identity uses p=q+1 and the fact that the fractional part of pN/q
is j/q with0<=j<=q-1. The first interval starts at zero, and the last
ends at ceil(beta G_k)-1. Induction gives the assertion and its stated
recurrence. Each prefix value has one prefix word at that fixed level.

Order is also preserved under continuation. If two parent values differ
by at least1, the difference of the next numerators is at least
p-q=1, even using the most unfavorable digit choices. Their next values
are integers, so their order stays strict. At the first differing digit
from one parent the child order is its digit order. Thus fixed-length
lexicographic order is integer-value order. Taking the limits

    rho(a)=lim_k beta^(-k)N_k(a)

shows that rho is nondecreasing on infinite lexicographic order. It is
not asserted to be strictly increasing: its nontrivial fibers are the
subject of this section.

Fix V>0 and a root fiber E(V) of size s. By F5A, s<=q. At any level,
the prefix values attained by this fiber form an interval of integers.
Indeed every intermediate integer prefix is admissible by the level
description above, and has an infinite continuation. Its word lies
between the two bounding fiber words. Nondecreasing evaluation forces
the same value V. This proves the absence of holes; it does not identify
distinct infinite words merely because they share a finite prefix.

Choose one level N after all s words have pairwise separated. At EVERY
later level there are exactly s distinct prefix values, still consecutive.
Increase N further so that the least is positive, using(2.1). Let
H_n be the largest and L_n=H_n-s+1 the least at level N+n. The largest
word remains largest under continuation. If its next digit is d_n and
the least word's digit is e_n, then

    q(H_(n+1)-L_(n+1))
      =p(H_n-L_n)+d_n-e_n,
    e_n-d_n=s-1.                                  (3.1)

If s>=2, this implies

    0<=d_n<=q-s+1<=q-1,
    H_(n+1)=ceil(beta H_n).                        (3.2)

All s paths are EXACTLY H_n-c for0<=c<=s-1, and their next digits
are d_n+c. The least is maximal, the largest minimal, and the middle
s-2 paths, when present, have digits1,...,q-1 and are unary paths.
These are statements after a common finite level; no uniform choice
of that level over different real fibers is claimed.

### 3.2 Existence equivalence, with every quantifier on ordinary integers

For any fixed2<=r<=q the following three statements are equivalent:

    (i) Some positive real has at least r admissible global expansions.
    (ii) Some positive ORDINARY integer H_0 has the ceiling orbit
         H_(n+1)=ceil(beta H_n) with EVERY digit
         d_n=qH_(n+1)-pH_n in{0,...,q-r+1}.
    (iii) Some positive ORDINARY ceiling orbit stays for ALL n>=0 in
          S_r={0,r-1,r,...,q-1} modulo q.           (3.3)

To prove(i)=>(ii), apply one common radix normalization and the fiber
description above. Its actual size s satisfies r<=s<=q; the largest
positive prefix orbit has digits at most q-s+1<=q-r+1. The finite
discarded prefix is allowed to depend on that actual fiber.

For(ii)=>(i), first go forward until H_n>r-1, which is possible because
H_(n+1)>=beta H_n and H_0>0. Relabel that point as time0. For each
c=0,...,r-1 define positive ordinary integers Z_n^(c)=H_n-c. Exactly,

    qZ_(n+1)^(c)=pZ_n^(c)+(d_n+c),
    0<=d_n+c<=q.

Begin with each Z_0's canonical finite word and append its indicated
digits. Every prefix is integral and canonical by Section1. The real
growth coefficient C_H=lim beta^(-n)H_n exists, since its digits are
bounded, and C_H>=H_0>0. The unscaled real evaluation of each seeded
expansion is

    H_0-c+sum_(n>=0)(d_n+c)/(p beta^n)=C_H,

because sum c/(p beta^n)=c when p-q=1. Pad all finite seeds to one
length m, chosen large enough also that beta^(-m)C_H<1/q. The r words
now have the same positive root value beta^(-m)C_H. Their tails have
distinct constant digit offsets, so they are r different expansions.
The proof constructs actual ordinary trajectories, not an inverse-limit
point or a compactness limit of unrelated starting integers.

Finally the ceiling digit is the least residue of -pH=-H moduloq.
Digit0 corresponds to H=0 modq; digits1,...,q-r+1 correspond to residues
q-1,...,r-1. This proves(ii)<=>(iii), with the inclusive endpoints in
S_r as written. For r2 this is all q classes, not a proper subset. For
r>=3 it is a nonempty proper subset of size q-r+2. The formula at r=q
gives S_q={0,q-1}; it is not a singleton. The boundary q2,r2 is valid
and gives S_2={0,1}.

Specializing(3.3) to11/10:

    a real with >=9 expansions exists
      iff some positive ceil(11H/10) orbit stays in{0,8,9} mod10;
    a real with 10 expansions exists
      iff some positive ceil(11H/10) orbit stays in{0,9} mod10. (3.4)

F5A supplies the missing upper bound in the phrase '10 expansions'.
Neither existence nor nonexistence of these ordinary orbits is proved.
The original Dubickas–Mossinghoff proper-residue termination question
applies to these displayed sets as an OPEN question. Its proved
singleton case does not settle either set. Ruling out only tenfold
fibers would still leave the ninefold A/B obstruction possible.

## 4. F5C: an arbitrary expansion of an A/B growth value is a translate

Assume throughout this section an infinite POSITIVE ordinary lift of
(0.1)–(0.2). Every Q_n>=81, and all full steps increase Q. There must
be infinitely many B blocks: an all-A tail gives
100^m | X_j for all m at its fixed positive starting state. Also

    C=lim beta^(-n)Q_n=X_0-R>0,
    R=sum_(j>=0) w_j100^j/121^(j+1),
    0<=R<=1/21.                                   (4.1)

The series in(4.1) is evaluated in the REAL numbers in this paragraph.
It is not identified with the10-adic series below.

### 4.1 Full proof of the bounded integer correction lemma

The coordinator's separate unverified note proposed the following
mechanism. We reconstruct it here, without treating that note as an
accepted theorem. Suppose bounded ordinary integers c_n and digits
0<=d_n<=10 satisfy Z_n=Q_n-c_n and

    10Z_(n+1)=11Z_n+d_n,
    10c_(n+1)=11c_n+h_n-d_n.                       (4.2)

If c_n<=0 at any time, then

    c_(n+1)<=floor((11c_n+1)/10)<=c_n.

It remains nonpositive and nonincreasing. A zero value encounters a
later h=-1, forcing it negative, because B occurs arbitrarily late.
Once c<=-1, every later first step of a block has h<=0 and makes
c_(n+1)<=floor(11c_n/10)<=c_n-1. Between those steps it cannot increase.
This contradicts boundedness. Hence c_n>=1 at EVERY index.

If c_n>=10 at any time, then

    c_(n+1)>=c_n+ceil((c_n+h_n-10)/10)>=c_n.

For the last inequality the worst value at c10 is ceil(-1/10)=0.
A later h=1 forces a value at least11. Once c>=11, every later second
step of a block has h>=0 and adds at least1; at other steps it cannot
decrease. Again boundedness is contradicted. Thus c_n<=9 at EVERY index.

Inside1,...,9 rewrite(4.2) as

    10(c_(n+1)-c_n)=c_n+h_n-d_n in[-10,10].

The value-10 requires(c_n,h_n,d_n)=(1,-1,10), and would give c_(n+1)=0.
The value10 requires(9,1,0), and would give c_(n+1)=10. Both were
excluded. The remaining multiple of10 is zero. Consequently

    c_n=c in{1,...,9} for ALL n,   d_n=h_n+c.      (4.3)

Conversely each of these nine constants gives digits0,...,10 and
satisfies(4.2). There is no causal rule, finite-state hypothesis, or
future independence assumption in this lemma.

### 4.2 Matching every global expansion to a common integer time

Choose one m large enough that the canonical words of Q_0-c, c1,...,9,
all have length<=m and V=beta^(-m)C<1/10. Pad them to length m and append
the tails h_n+c. The integer recurrence proves prefix admissibility.
Each word has value V, since its unscaled value is

    Q_0-c+sum_(n>=0)(h_n+c)/(11 beta^n)=C.

Their tails are different, so there are at least nine expansions.

Now take ANY global admissible expansion of this SAME value V. The
inequality V<1/10 forces all its indices>=0 to be zero. It is therefore
one root word a in W, without a separate radix adjustment. Put

    Z_n=N_(m+n)(a),   d_n=a_(m+n+1).

These are nonnegative ordinary prefix integers with the recurrence in
(4.2). The full tail estimate gives

    Z_n=C beta^n-T_(m+n),    0<=T_(m+n)<10.

The signed Q recurrence has the equally explicit uniform error

    Q_n=C beta^n-U_n,
    U_n=sum_(j>=0) h_(n+j)/(11 beta^j),   |U_n|<=1.

Therefore c_n=Q_n-Z_n=T_(m+n)-U_n is a BOUNDED sequence of ordinary
integers. The lemma applies at every index and gives one fixed
c in1,...,9. Its first length-m prefix has value Q_0-c. Fixed-length
finite uniqueness makes that prefix exactly the chosen padded seed.
Its entire remaining digit tail is h_n+c by(4.3). Thus the arbitrary
expansion was one of the nine already constructed.

It follows that V, and by common index translation also C, has
EXACTLY NINE global admissible expansions. This is a conditional
conclusion about the hypothetical ordinary A/B lift; it does not
assert the existence of any ninefold fiber. It uses the full matching
argument above, not an inference from the coordinator's common-index
carry lemma alone.

Exactly eight of these nine expansions are eventually minimal: c1,...,8
have digits0,...,9, whereas c9 has digit10 at infinitely many h=1
positions. Exactly eight are eventually maximal: c2,...,9 have digits
1,...,10, whereas c1 has digit0 at infinitely many h=-1 positions.
The seven with c2,...,8 always have digits1,...,9 after their seeds,
and hence are unary. The two remaining paths have infinitely many
branching positions and are not eventually unary. The counts are
eventual-tail counts and disregard finite seed or leading-zero choices.

### 4.3 An exact fiber in ordinary initial integers

Define on positive ordinary integers

    G(z)=lim_(n->infinity) beta^(-n) T^n(z),
    T(z)=ceil(11z/10).

The limit exists by its bounded0,...,9 digit series. For the hypothetical
A/B growth coefficient C in(4.1), the ENTIRE positive integer fiber is

    {z>0:G(z)=C}={Q_0-8,Q_0-7,...,Q_0-1}.         (4.4)

Indeed each listed trajectory is Q_n-c for1<=c<=8 and has coefficient C.
For an arbitrary positive ceiling trajectory with coefficient C, its
bounded tail error makes Q_n-T^n(z) bounded, so(4.3) applies. The choice
c9 is impossible because the ceiling alphabet excludes digit10, which
h_n+9 attains infinitely often. Hence c1,...,8 exhaust the fiber.
The map G is nondecreasing because T is nondecreasing, so this is an
exact eight-point constant interval in its ordinary integer domain.
This arithmetic plateau is another necessary condition, not a proved
impossibility. It strengthens no claim to all full-controller paths.

## 5. F5D: real interval image,10-adic separation, ordinary intersection

For an arbitrary binary word w define two DISTINCT evaluations of the
same formal series:

    Psi_R(w)=sum_(j>=0) w_j100^j/121^(j+1) in R,
    Psi_10(w)=sum_(j>=0) w_j100^j/121^(j+1) in Z_10. (5.1)

Both converge in their stated topologies. Put I=[0,1/21]. The real
image of all binary words is EXACTLY I, not a sparse real Cantor set.
Containment in I is its geometric bound. For the reverse containment
use the two contractions f_i(t)=(i+100t)/121, i0,1. Their images are

    f_0(I)=[0,100/(121*21)],
    f_1(I)=[1/121,1/21].

They overlap and their union is I. Given t in I, recursively select
w_j in{0,1} and t_(j+1) in I with t_j=f_(w_j)(t_(j+1)). After N
choices,

    t=sum_(j=0)^(N-1) w_j100^j/121^(j+1)
        +(100/121)^N t_N.

The last term tends to zero, proving real surjectivity onto I. No
admissibility or ordinary integer lift was used in this interval proof.

In Z_10 the map is instead injective with exact two-prime separation.
If w and v first differ at index j, subtract their series and factor:

    Psi_10(w)-Psi_10(v)
      =(100^j/121^(j+1))*(epsilon+100t),
    epsilon in{-1,1},  t in Z_10.

The last factor is a unit at both2 and5. Thus the exact exponents of
2 and5 in the difference are BOTH2j. A fixed binary prefix of length N
determines one class modulo100^N; all its suffixes have that class, and
the2^N different prefixes determine2^N DIFFERENT classes. This is a
statement about a sparse inverse-limit image, not about an equality
of its real evaluation with the embedded ordinary integer.

For clarity the remaining ordinary bridge can be stated as an exact iff:

    Psi_10(w) is an ordinary positive integer X_0
      iff w is the block word of an infinite positive ordinary A/B lift.
                                                               (5.2)

For the forward direction, the series identity gives
121X_0-w_0=100 Psi_10(shift w). Reduction modulo100 makes the left side
divisible by100 as an ordinary integer. Hence
X_1=(121X_0-w_0)/100 is ordinary and equals the next10-adic tail.
Cancellation of100 here is valid because multiplication by100 is
injective in both Z_2 and Z_5, hence in Z_10; no inverse of100 or
field structure on Z_10 is assumed.
It is positive: for X_0>=1 its numerator is at least120. Repeating
this argument gives ordinary positive X_j at all times. The residues
are exactly X_j=0 mod100 when w_j0 and X_j=81 mod100 when w_j1;
therefore the accepted intermediate-step check gives the actual loops.
For the reverse direction iterate(0.1):

    X_0=sum_(j=0)^(N-1) w_j100^j/121^(j+1)
          +(100/121)^N X_N.

The remainder tends to zero in Z_10 because X_N are ordinary integers,
so their2- and5-adic valuations are nonnegative. This proves(5.2).

Every finite prefix has arbitrarily large positive integer representatives
in its prescribed class. Such representatives may change with N. Their
existence is not a positive integer in the intersection of ALL those
classes. The interval image under Psi_R likewise supplies no positive
ordinary point under Psi_10. This packet does not determine whether the
intersection in(5.2) is nonempty.

## 6. F5E: strict necessary fractional parts, with no false converse

An infinite positive ordinary A/B lift also has infinitely many A blocks.
Otherwise on an all-B tail let Y_j=21X_j-1, a positive ordinary integer.
The recurrence gives100Y_(j+1)=121Y_j. It would make a fixed positive
Y_j divisible by100^m for every m, impossible. Along with the all-A
argument in Section4, every binary tail contains both symbols.

Set R_j=Psi_R(shift^j w). The strict consequence is

    0<R_j<1/21,
    gamma^j C=X_j-R_j,
    {gamma^j C}=1-R_j in(20/21,1) for ALL j>=0.    (6.1)

The open lower endpoint follows because an actual ordinary tail cannot
be all ones; the open upper endpoint follows because it cannot be all
zeros. The identity comes either by the real recurrence or by splitting
the real convergent series in(4.1). This necessary fractional-part
condition concerns gamma=121/100, whereas F5A–F5C use the full-time
base11/10; the two time indices are not interchanged.

It would be invalid to reverse(6.1) solely from that interval width.
For arbitrary integral shadow choices X_j with errors R_j in(0,1/21),
the integer discrepancy121X_j-100X_(j+1)=121R_j-100R_(j+1) could be
any integer from-4 through5 at a single transition. It is not forced
to lie in{0,1}. A concrete two-time local witness is

    X_0=62, X_1=75,
    R_1=1/121, R_0=342/14641,
    C_*=62-R_0.

Both errors lie strictly between0 and1/21, and
gamma C_*=75-R_1, but121*62-100*75=2. The identities follow directly
from121R_0-100R_1=2;21*342<14641 checks the upper bound for R_0.
This only refutes that LOCAL inference. It is not a positive infinite
A/B example, not an all-time fractional-part counterexample, and not
a proof that an all-time converse cannot follow from extra hypotheses.

## 7. Precise unresolved arithmetic and source boundary

For base11/10, F5B identifies the ordinary existence question behind
ninefold fibers as a positive ceiling orbit confined to{0,8,9} mod10.
F5C places a hypothetical A/B lift in an exact ninefold fiber and an
exact eight-point integer growth plateau. None of those properties
has been excluded. F5D shows that calling the real binary-series image
a Cantor set cannot itself give the missing arithmetic obstruction;
the sparse object is its10-adic image, and(5.2) requires ONE embedded
positive ordinary integer. F5E gives an interval restriction without
silently identifying it with the binary ordinary lift.

AFS's actual admissible language,1/q weights and full alphabet are used.
Its general multiplicity estimate permits eleven at11/10, and its
at-most-two corollary needs p>=2q-1, which fails. AEV2026 states the
stronger universal at-most-two/normality assertions as conjectural;
its implications do not prove those hypotheses. Original
Dubickas–Mossinghoff Proposition3.2 proves termination for a SINGLE
allowed residue, whereas(3.4) has three or two. Proposition3.1 is a
conditional implication from termination, not a proof of it. No claim
that those papers settle the displayed sets, that no applicable theorem
exists anywhere, or that the elementary deductions here have priority
is made. Actual primary read scopes and URLs are in the source record.

The accepted full-controller complexity obstructions also remain in force:
an arbitrary signed controller does not automatically admit bounded
ceiling carries, and a finite controller does not force automaticity.
Even termination of every A/B path would exclude only that restricted
mechanism, not settle every contest path. No full2022B4(b) answer,
unrestricted no-ninefold theorem, infinite ordinary counterexample,
numerical experiment, or promotion to accepted proof is asserted.
