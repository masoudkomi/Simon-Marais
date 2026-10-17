# 2022 B4(b), R5: initially blind whole review R1

2026-10-17 UTC. Reviewer `/root/review_2021_reasoning_j15_r2`.
Requested gpt-6.1-sol/max; independent effective-setting readback unavailable.

I reconstructed the complete F5A–F5E argument, all 42 constructor obligations,
and the cited sources within the read scopes recorded separately. I found
no substantive defect or required author repair. I recommend acceptance of
these scoped partial results after the coordinator reconciles the two whole
audits. This report does not promote them, prove a no-ninefold theorem,
establish an infinite ordinary A/B lift, or settle the official question.

The reviewed main is 26928 bytes, SHA256
`f08f3e579f9ddeec52746060ab81aec6055f1ecfce24fa2031608eadb7743bef`.
The constructor freeze is SHA256
`29a0ba60beda79572326525a2ab5fe20b23f0aff1c4129fc9645a86b83ff4601`.
The candidate, source audit, sources JSON, full log, failed-route ledger,
all obligations and exact accepted input bodies were read. The final
metadata freeze verifies their declared bytes and preservation of my older
packets. Those administrative checks are not mathematical evidence.

I previously whole-reviewed the separately accepted R3 and R4 packets.
Those roles are disclosed inputs, not independent construction of the NEW
R5 assertions. I did not supply its bounded-correction strategy, proof,
family classification or repair. Root supplied that lead and the other
actor constructed R5; neither is counted as an independent R5 reviewer.
No new peer R5 report, conclusion or later root inspection was read before
the complete initial freeze. No mathematical program, CAS, orbit scan,
certificate replay or constructor rerun was used. Only this assigned review
prefix was written; no candidate, shared file, older record or Git changed.

## Domain and exact accepted inputs

The actual official B4(b) uses positive ordinary integers, simultaneous
updates a'=a+2 floor(b/20), b'=b+3 floor(a/30), and inclusive a0*b0>=600.
No preliminary trapping proof is investigated here. The accepted restricted
A/B loops keep d=1 and return to r=0. Their full-time corrections are
(0,0) or (-1,+1), so with X_j=Q_(2j),

    100 X_(j+1)=121 X_j-w_j,  w_j in {0,1}.

Ordinary block integrality requires X=0 mod100 for A and X=81 mod100 for
B. The intermediate quotients, respectively 11X/10 and (11X-1)/10,
are 0 and 9 mod10. This verifies both controls rather than retaining only
the terminal block equation. An infinite positive lift has every Q>=81,
increasing full steps, and gives the actual contest start
(60X0+1,60X0), of product well above 600 and difference always one.
Zero with the all-A word is excluded. This restricted implication does
not classify every equality-avoiding controller.

The accepted R4 result provides at least nine full-alphabet expansions;
its finite power100 shadow universality does not provide a single ordinary
infinite lift. The new exact-nine inference is checked below. The old
full-controller carry obstructions apply to their original smaller output
alphabet and full input quantifiers. The coordinator carry note is marked
unverified and is re-proved in R5, not imported as accepted authority.

## Finite prefixes and the single global normalization

Write p=q+1, q>=2, beta=p/q, and use digits 0,...,q with the 1/q
valuation convention. For a length-k prefix its integer value N_k obeys
qN_(k+1)=pN_k+a_(k+1). Modified division of a positive ordinary N has
predecessor floor(qN/p)<N and last digit qN modulo p in 0,...,p-1.
It terminates. Conversely successive integral prefix updates are exactly
canonical prefixes with possible leading zeros. At a FIXED length, the
last digit and predecessor are unique; iterating proves injectivity.
This statement does not identify infinite words that temporarily share a
prefix. Zero at fixed length has only the corresponding all-zero word.

The allowed extension digits are the least residue of -pN modulo q and,
only if this residue is zero, the extra digit q. Hence a least digit in
0,...,q-1 always exists and any finite prefix extends infinitely. The
least update is ceil(pN/q). The maximal digit is 1,...,q; the sole
two-choice case is N=0 modq, with choices 0 and q. These facts retain
the full alphabet, including digit10 in base11/10.

A global expansion is an indexed sequence with a finite integer part;
extra leading zeros are not distinct indexed sequences. Translating
every index by -M is a bijection of the entire fiber at V with that at
beta^(-M)V, preserving all prefix words. Choose ONE M for the fixed V
so that 0<beta^(-M)V<1/q. Nonnegative weights then force all indices
>=0 to carry zero in every expansion of that value. All are root words
starting at the same fractional index. This normalization applies to
arbitrary expansions, not only a preselected finite family. Zero has
only its all-zero expansion.

## F5A: the endpoint and finite-fiber argument

The exact root-word identity is beta^k*rho=N_k+T_k, with
T_k=(1/q) sum_(j>=1) a_(k+j)*beta^(-j). It gives 0<=T_k<=q.
Equality would require every future digit q. Then
q(N_(n+1)+q)=p(N_n+q), forcing q^m to divide the fixed positive
ordinary N_k+q for every m, which is impossible since gcd(p,q)=1.
Thus 0<=T_k<q, including k=0 and integral beta^k*rho.

Every prefix integer for a fixed rho lies in the OPEN-left interval
(beta^k*rho-q,beta^k*rho]. This contains exactly q integers, even
when its right endpoint is integral. Select q+1 different words if a
fiber has that many, including if it is infinite, and choose one finite
level after every pair has separated. Fixed-length injectivity supplies
q+1 distinct integers in that interval, a contradiction. The common
global normalization transfers the bound to arbitrary positive real
values. q=2 gives two, zero gives one, and q=1 is not asserted.

I checked the original AFS parameter: k is integral and must exceed
(q-1)/(p-q). The source estimate therefore permits eleven at 11/10;
the separate at-most-two corollary needs p>=2q-1. The proposed ten
bound has the displayed independent endpoint proof and still permits
nine. No priority claim or exclusion of nine follows.

## F5B: full fiber geometry and both directions of the ordinary iff

At one level, children of N have integer values from ceil(pN/q) through
floor((pN+q)/q). Put pN/q=t+j/q with 0<=j<=q-1. The next parent's
first child is t+2, whereas the previous interval ends t+1. This
includes j=0 and j=q-1. Therefore the level labels are exactly
0,...,G_k-1, with G_0=1 and G_(k+1)=ceil(beta G_k). Fixed-length
injectivity ensures one word per such integer.

For two different integer parents, the least possible next numerator
difference is p-q=1. Both quotients are integers, so strict order
persists regardless of future allowed digits. First branching from a
common parent is ordered by the digit. Thus lexicographic order agrees
with level integers, and normalized limits make rho nondecreasing,
not necessarily strictly increasing.

If an intermediate integer prefix lies between prefixes from two words
in one real fiber, any infinite extension of it is lexicographically
between those words. Monotonic rho forces the same real value. This
proves that fiber-prefix integers have no holes. F5A first gives a
finite fiber of size s<=q. One common separation level makes all s
prefixes distinct, and they remain so at every later level. The lower
endpoint beta^n*V-q tends to infinity for V>0, so that level may also
be chosen to make them positive. There is no claim of a uniform level
over all real fibers.

After that level put H_n=max prefix and L_n=H_n-s+1. Constant width
and the two exact updates imply e_n-d_n=s-1 for bottom and top digits.
Consequently 0<=d_n<=q-s+1. For s>=2 this lies in 0,...,q-1, so the
top is an ordinary ceiling orbit. Permanent order labels every path
H_n-c; its digit is d_n+c. The bottom is maximal and the s-2 inner
paths, when present, use only digits 1,...,q-1 and have unary updates.

For 2<=r<=q, an actual fiber of size s>=r therefore gives an ALL-time
positive ordinary ceiling orbit with digits at most q-r+1 after its
allowed finite prefix discard. The converse is substantive and valid:
given such an ordinary orbit H_n, go forward until H_0>r-1, then use
positive integers H_n-c for 0<=c<=r-1. Their digits d_n+c lie in the
full alphabet. Canonical finite seeds followed by these digits are
prefix-admissible. Their common real growth coefficient follows from
sum_(n>=0) c/(p*beta^n)=c, using p-q=1. Pad all seeds to ONE length
m and choose beta^(-m)C_H<1/q. Their different digit offsets give r
different expansions of that same root value. They are not merely
finite representatives or index copies.

The ceiling digit is -H modulo q in 0,...,q-1. The allowed residue
set is exactly S_r={0,r-1,...,q-1}, of size q-r+2. At r=2 this is
ALL classes; no proper-set termination theorem may be applied. At r=q
it is two classes {0,q-1}, including q=2,r=2. At 11/10 the ninefold
existence set is {0,8,9}; exactly-ten existence uses {0,9} together
with F5A's upper bound. The source singleton theorem settles neither.
No ordinary all-time orbit in these sets is constructed or excluded.

## F5C: rigidity, arbitrary-expansion matching and the full growth fiber

Assume an actual positive ordinary infinite A/B lift. Infinitely many B
blocks are necessary: an eventual A tail would force every 100-power
to divide a fixed positive X. The REAL coefficient is
C=X0-sum w_j*100^j/121^(j+1)>=81-1/21>0. This expression is not
identified with the evaluation of that formal series in Z10.

For arbitrary bounded integer c_n with Z_n=Q_n-c_n and full digits
d_n in 0,...,10, the exact carry equation is

    10 c_(n+1)=11 c_n+h_n-d_n.

If c<=0, integrality gives cnext<=floor((11c+1)/10)<=c. A later
h=-1 leaves zero, and at each subsequent first block step h<=0 makes
a negative carry decrease by at least one. Between such steps it
cannot increase, contradicting boundedness. Thus every c>=1. If
c>=10, the dual bound is cnext>=c+ceil((c+h-10)/10)>=c; at c=10,
h=-1 the ceiling is zero, not -1. A later h=+1 leaves ten upwards.
For c>=11 every subsequent second block step h>=0 increases it by
at least one. Thus every c<=9.

Inside that interval, 10(cnext-c)=c+h-d lies in [-10,10]. The two
nonzero multiples require (c,h,d)=(1,-1,10) or (9,1,0), which would
exit to zero or ten. Only zero remains. Every bounded integer carry
is therefore a constant c=1,...,9, with d=h+c. Conversely all nine
constants work. The argument allows arbitrary future-aware bounded
initialization, arbitrary memory and the ENTIRE output alphabet.

Choose a single m padding the nine ordinary positive seeds Q0-c and
making V=beta^(-m)C<1/10. They generate nine root words of value V,
because the digit-series correction cancels the constant c. Now take
ANY global expansion of this V. Nonnegative digits and V<1/10 force
it into the same root indexing, with actual integer Z_n=N_(m+n).
Its tail gives Z_n=beta^n*C-T_(m+n), 0<=T<10. The signed recurrence
gives Q_n=beta^n*C-U_n, where |U_n|<=1. Hence their difference is
a bounded ordinary integer carry. The just-proved lemma forces one
constant c=1,...,9. Fixed-length injectivity recovers the complete
length-m seed of value Q0-c, and d=h+c recovers all later digits.
Thus every expansion is one of the nine; there is no unmatched
integer part, different prefix length or seed ambiguity. One common
index translation gives the same exact count for C itself.

Infinitely many B blocks yield infinitely many h=-1 and h=+1. Thus
c=1,...,8 are eventually minimal, whereas c=9 uses digit10 infinitely
often. Similarly c=2,...,9 are eventually maximal, and c=1 uses zero
infinitely often. Exactly c=2,...,8 are eventually unary; the two
endpoint paths branch infinitely often. These are eventual-tail counts,
not extra copies from seed padding.

For the ordinary ceiling growth map G(z)=lim beta^(-n)T^n(z), every
z=Q0-c, 1<=c<=8, has growth C. Conversely ANY positive ordinary
z with G(z)=C has a uniformly bounded ceiling tail error. Comparing
its orbit to Q_n again produces a bounded integer carry, hence c in
1,...,9. c=9 is excluded by its infinitely many digit10 occurrences,
since ceiling digits stop at nine. Therefore the ENTIRE positive
integer growth fiber is {Q0-8,...,Q0-1}. Monotonicity of T gives
nondecreasing G. An eight-point plateau is a necessary conditional
property, not a contradiction or a no-ninefold proof.

## F5D and F5E: real image, two-prime image and strict endpoints

For arbitrary binary words the REAL image of the shadow series is
I=[0,1/21]. The maps f_i(t)=(i+100t)/121 send I to overlapping
intervals [0,100/(121*21)] and [1/121,1/21] whose union is I.
Recursively choose a preimage in I and iterate. The remainder after N
steps is bounded by (100/121)^N/21 and tends to zero, proving full
surjectivity. This uses no admissibility or ordinary lift.

In Z10, a first difference at j factors as
100^j/121^(j+1)*(epsilon+100t), with epsilon=+/-1 and t in Z10.
The last factor is a unit at BOTH 2 and 5. Both valuations are exactly
2j. Consequently the 2^N binary prefixes give distinct classes modulo
100^N, independent of suffixes. No field structure on Z10 is used.

The positive ORDINARY membership iff is valid in both directions.
If Psi10(w)=X0 is a positive integer, the series identity makes the
ordinary integer 121X0-w0 divisible by100. Its ordinary quotient is
positive and equals the next tail, because multiplication by100 is
injective in Z2 and Z5. Inductively all X_j are ordinary positive,
with the exact 0/81 congruences and both intermediate controls checked
above. Conversely iterate the ordinary recurrence: its remaining term
(100/121)^N X_N tends to zero in both completions, since each X_N
is an integer and has nonnegative valuations. Varying finite positive
representatives of the prefix classes do not give one ordinary point
in their infinite intersection. Real surjectivity supplies no such point.

An eventual all-B tail is also impossible: Y=21X-1 is a positive
ordinary integer satisfying 100Ynext=121Y, forcing all 100-powers to
divide a fixed positive Y. Hence every binary tail contains both
symbols. Its real value R_j is strictly between zero and 1/21, and
gamma^j*C=X_j-R_j gives fractional parts strictly in (20/21,1).
These are block-time powers gamma=121/100, not full-time beta powers.

The interval alone does not force a single transition's discrepancy to
be binary: 121R-100R' lies in (-100/21,121/21), whose possible
integers are -4,...,5. The displayed witness X0=62, X1=75,
R1=1/121, R0=342/14641 gives discrepancy 2 by direct hand algebra;
both errors lie strictly in (0,1/21). It refutes only the LOCAL
implication. No infinite all-time interval counterexample or ordinary
A/B lift is claimed from it.

## Disposition and retained gaps

All five claims are supported in their stated scopes; the separate
ledger records 60 inference checks covering every one of the 42
obligations. No substantive issue or author repair is requested.
The original two/three-residue termination problems, no-ninefold
assertion, positive ordinary membership of the infinite binary image,
and universal contest conclusion remain open in this packet. The full
controller is not silently replaced by A/B, its finite states do not
force low complexity, and no source conjecture is promoted. This is
a complete initially blind whole audit rather than acceptance of
isolated local lemmas. Promotion and reconciliation belong to root.
