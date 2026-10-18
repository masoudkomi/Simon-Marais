# Proper norm factors and the limits of the easy class-group tests

2026-10-18 UTC. **Candidate proof - unverified.** Constructor C,
`/root/review_2017_coarsening_r1`. Requested inherited gpt-6.1-sol/max;
effective-setting readback unavailable. TWO OTHER fresh initially blind
WHOLE audits and coordinator reconciliation are required. No new taut
order, excluded numerical order, unrestricted prime-power classification,
classicality theorem, numerical cutoff or novelty is claimed.

The principal consequence is exact: in the prime-modulus, odd-class-number
domain of accepted R8, BOTH of its easy sufficient tests can hold only
at prime-power q. Thus those tests cannot certify a non-prime-power
counterexample to the cyclic prime-power conjecture. The full interval
criterion is not eliminated; at squarefree composite q, any actual
solution must instead involve a minimal zero-sum sequence of NONZERO
minus ideal classes. This is an arithmetic obstruction, not a replacement
of classes by formal configurations or a solution of that remaining
mixed cancellation problem.

The small-Weil-norm threshold used here is PUBLISHED. Leung--Schmidt,
*Nonexistence Results on Generalized Bent Functions...*, JCTA163(2019),
Theorem23 in the [author version](https://personal.ntu.edu.sg/bernhard/Publications/pub/BentFunctions.pdf),
proves it for prime-power conductor. Section1 reconstructs the needed
prime-conductor case by an elementary coefficient argument. Its bound,
Cassels' coefficient-energy method and the Hasse norm theorem are not
claimed as new. The source ledger distinguishes their actual operative
reads, complete accepted imports and this packet's deductions.

## 0. Exact official sector and accepted authority

Only2020 B4(b) is investigated. The official open question asks which
integers n>=2 are taut. Use the separately accepted difference-set
dictionary, without reproducing the preliminary construction. Set

    q=n-1>=2, k=q+1, p=q^2+q+1, and ASSUME p PRIME.       (0)

An actual planar set D in Z/pZ has k distinct members and represents
every nonzero ordered difference once. The accepted q=1,n=2 boundary
and all composite moduli are outside the new claims. The conjecture
that every taut q>=2 is a prime power remains open here.

Fix an ODD subgroup T of F_p^* containing EVERY rational prime ell
dividing q, and put

    K=Q(zeta_p), F=K^T, c=complex conjugation on F,
    E=F^c, C=Cl(F), C^-={x in C:c(x)=-x}.                (1)

C is the ORDINARY ideal class group, written additively. Except for
the standalone small-norm theorem and Section6, the additional
assumption is

    h(F)=|C| is ODD.                                    (2)

Fields and T are fixed before any actual D is assumed. Since q is a
product of the indicated prime residues, q belongs to T and has exact
order3 modulo p. Thus T is nonidentity and F/E is CM quadratic. Every
ell|q splits completely in F, and conjugation pairs its primes without
fixed primes. These are the exact accepted R8 field hypotheses.

The COMPLETE accepted R8 body/header is
`proofs/reviewed-reasoning-return-r8-v1.1.md`,29871B,
SHA2569003af18926d1fe49d3f997b40ed070ceefa37e42f73c5a98c32bbe7a2f3bfcb.
It is imported only in its accepted scope. In particular:

* its standalone quadratic norm-unit lemma says that, if the ORDINARY
  class number of a quadratic extension is odd, every base UNIT which
  is a FIELD norm is the norm of a UNIT;
* the prime-modulus integral relative-norm-to-ACTUAL-set equivalence
  and exact augmentation sign are separately accepted R7 inputs;
* for actual centered D, numerical multipliers fix D, every prime
  divisor of q is one by the attributed First Multiplier Theorem, and
  the full numerical group M is odd, with |M|<=q+1;
* balance, principality and a correcting unit remain distinct before
  the odd-class-number argument is applied.

Complete accepted R7,R6,R5 and repaired R4 bodies/scopes were read.
C authored OLD repaired R3 and R6 and reviewed OLD R4/R5/R7; those
accepted inputs are not independently self-certified by this new
construction. Root supplied the broad research assignment but no new
proof inference. Neither S0 saturation nor Desarguesian structure is
assumed. The q4, q5 and q16 old examples and all old repairs are intact.

Primality in(0) implies q is NOT a square: q=b^2 would give

    p=(b^2+b+1)(b^2-b+1), b>=2.                        (3)

This also follows from the accepted perfect-power restriction. It is
not a preliminary existence argument.

## 1. A9A: the published small-norm barrier, with full prime-case proof

**Known theorem, needed special case.** If a>=2 is a nonsquare integer,
p is an odd prime and alpha in Z[zeta_p] satisfies

    alpha*c(alpha)=a,

then

    p<=a^2+a+1.                                         (4)

Here c is ordinary complex conjugation; the identity implies the same
positive modulus at EVERY embedding. No mere absolute-field-norm
assertion is substituted. Theorem23 of Leung--Schmidt is stronger in
allowing conductor p^b. The following is a complete reconstruction
for b=1, not a new-method claim.

Write alpha=sum_(i=0)^(p-1) c_i zeta^i with integer coefficients.
Tracing alpha*c(alpha)=a, using Tr(1)=p-1 and Tr(zeta^u)=-1 for
nonzero u, gives the coefficient-energy identity

    a(p-1)=p sum_i c_i^2-(sum_i c_i)^2
          =sum_(i<j)(c_i-c_j)^2.                       (5)

This is the prime case of the classical Cassels M-function identity;
the displayed trace computation proves precisely what is used.

Suppose, towards contradiction, p>a^2+a+1. Then p>4a: for a>=3,
a^2+a+1>=4a+1; for a=2, the next possible prime after7 is at least11.
Let t be the largest multiplicity of a coefficient value, and let the
multiplicities of all coefficient values be t_1,t_2,... . Unequal
integer coefficients differ in squared value by at least1. Moreover
sum_j t_j^2<=t sum_j t_j=t p. Thus(5) implies

    a(p-1)>=(p^2-sum_j t_j^2)/2>=p(p-t)/2,
    t>=p-2a(p-1)/p>p-2a>p/2.                          (6)

Subtract this most frequent integer value from ALL coefficients. This
does not change alpha because sum_i zeta^i=0. The resulting vector b
has support size u=p-t<2a<p/2. Each of its u nonzero coefficients
differs from each zero by at least1; hence

    a(p-1)>=u(p-u).                                    (7)

The function x(p-x) is increasing on[0,p/2]. If u>=a+1, then

    u(p-u)>=(a+1)(p-a-1)
             =a(p-1)+p-a^2-a-1>a(p-1),

contradiction. Therefore u<=a.

Let B=sum_i b_i X^i in Z[C_p]. Evaluation at zeta has kernel exactly
Z*N, where N=sum_(i=0)^(p-1) X^i: the only polynomial relation of
degree<=p-1 is a constant multiple of Phi_p, and integral coefficients
make that constant integral. Consequently

    B B^-=a*1+lambda N, lambda in Z.                    (8)

If lambda=0, augmentation of(8) makes a the square of the integer
sum_i b_i, impossible. If lambda!=0, every one of the p-1 nonzero
residues must occur as a difference of two distinct support indices
of B. There are at most u(u-1)<=a(a-1) such ordered pairs, whereas
p-1>a(a-1). This is also impossible. This proves(4), including
negative coefficients, arbitrary integer augmentation and the a2
endpoint. No enumeration or factor table has been used.

### 1.1 Actual consequences at the planar prime

At p=q^2+q+1, strict monotonicity of x^2+x+1 for x>=0 makes(4) say:

    NO integral cyclotomic number has relative norm a
    for ANY nonsquare integer2<=a<q.                   (9)

This is unconditional on existence of D, on T and on class numbers.
Thus every actual norm-q character is multiplicatively indecomposable
in the semigroup of integral Weil numbers of INTEGER norms>1. Indeed
if alpha=beta gamma with beta*c(beta)=a>1 and gamma*c(gamma)=b>1,
then ab=q; because q is nonsquare, at least one of a,b is nonsquare
and is smaller than q, contrary to(9).

This is NOT ordinary ring-theoretic irreducibility: arbitrary integral
factors need not have rational constant conjugation norm. Nor does
Weil indecomposability force q prime. At the attributed known order
q8,p73, an actual Singer character has norm8 and cannot have integral
Weil factors of norms2 and4. This existing prime-power example already
prevents that false conclusion; no preliminary construction is repeated.

## 2. A9B: norm/unit correction for EVERY supported positive integer

Let a>=1 be ANY positive integer all of whose rational prime divisors
divide q. Its exponents need not be bounded by those of q. We claim:

1. a is a FIELD norm from F to E;
2. under(2), every integral balanced ideal B with
   B*c(B)=(a) has a generator of exact relative norm a IF B is principal.

The converse in2 is immediate. No integrality is inferred from1 alone.

For1, apply the classical Hasse norm theorem ONLY to the CYCLIC
quadratic number-field extension F/E, checking ALL places. At a prime
over ell|a, ell belongs to T and splits completely in F, so each local
relative degree is1 and its norm is the identity. Away from p and a,
the local extension is unramified or trivial and a is a unit; norms
on units in an unramified local extension are surjective, including
residue characteristic2. The residue norm and successive trace
corrections prove this standard local fact without dividing by2.

At the unique prime over p, write s=|T|, which is odd. The residue
of a is in T. Thus r=a^((s+1)/2) modulo p satisfies r^2=a modulo p.
It is nonzero, so Hensel's lemma lifts it to x in Q_p with x^2=a;
the derivative2r is a unit as p>=7. In the local real subfield E_v
this x is fixed by c, and its relative norm is x^2=a. Every real
place of E becomes complex in F and a>0, so it is a norm there too.
There are no other places. The Hasse theorem gives z in F^* with
z*c(z)=a. This z may have denominators; it has not generated B.

For2, let B=(gamma) be integral and balanced. Then gamma is integral
and epsilon=gamma*c(gamma)/a is a totally positive UNIT of E.
Because z exists, epsilon=N_(F/E)(gamma/z) is a FIELD-norm unit.
The EXACT accepted standalone R8B norm-unit lemma, using the ODD
ordinary class number h(F), supplies a UNIT u in F with
u*c(u)=epsilon. Then

    alpha=gamma/u in O_F, (alpha)=B,
    alpha*c(alpha)=a.                                  (10)

This proves the complete partial-factor extension of the needed R8
correction. Positivity, the norm-one kernel and a formal ideal pattern
were not used as substitutes for a correcting unit. At even h(F) the
conclusion is NOT asserted; the original finite2-primary obstruction
can remain.

Combining(9),(10), under(2) EVERY integral balanced ideal of supported
nonsquare norm a<q is NONPRINCIPAL. Thus it is not merely an occasional
poor choice of a balanced ideal that obstructs such a proper factor.

## 3. A9C: compulsory minus-class orders and the class-number-one limit

For ell|q, choose ANY integral balanced ideal B_ell with

    B_ell*c(B_ell)=(ell).                               (11)

Such ideals exist: ell splits completely in F, and putting exponent1
on one prime of each conjugate pair and0 on the other gives(11).
Let r be the order of its class in C. That class is in C^- because
its sum with its conjugate is zero. Under(2), r is odd.

The ideal B_ell^r is principal and balanced of norm ell^r. Section2
therefore gives an integral relative-norm-ell^r generator. Since r
is odd, ell^r is a nonsquare. Apply(4) and compare with p in(0):

    ell^r>=q, for EVERY balanced B_ell.                 (12)

If q is not a power of ell, equality is impossible, so ell^r>q.
In particular, writing e_ell=v_ell(q), for non-prime-power q,

    r>log_ell(q)>e_ell,
    exp(C^-)>e_ell for EVERY ell|q.                    (13)

Here the logarithmic inequality means an exact integer comparison;
no logarithm has been numerically approximated. The exponent of C^-
is at least r because r divides it. These restrictions apply to the
actual arithmetic field even before any planar D exists.

If h(F)=1 and q is composite, choose a prime ell<q dividing q.
Then r=1 contradicts(12). Hence

    h(F)=1 in the stated prime/T domain FORCES q PRIME. (14)

This is not a converse: prime q need not make h(F)=1. It does not
claim that every relevant field has odd class number. Instead it
shows exactly why the class-number-one clause of R8 cannot furnish
a new composite, and in particular non-prime-power, taut order.

## 4. A9D: BOTH easy R8 existence tests force prime powers

Keep(0)--(2). Write q=product_ell ell^(e_ell). For the primes over
each ell choose one P_i from each conjugate pair. Put

    delta_i=[P_i]-[c(P_i)], m_i=ord(delta_i),
    m=exp C.                                          (15)

All these orders are odd, with order1 allowed. The two accepted R8E
sufficient hypotheses are EXACTLY:

    (L) e_ell>=m_i-1 for EVERY pair over ell;
    (X) m divides e_ell for EVERY ell|q.                (16)

They remain sufficient in their original domain. The new conclusion
is that each can hold only when q is a prime power.

### 4.1 The long-interval test

If q is not a prime power, it has at least two distinct prime factors.
Since q is not a square by(3), choose ell with e=e_ell ODD. Then

    a=ell^e is a supported NONSQUARE with2<=a<q.         (17)

Restrict(L) to the conjugate pairs over this ONE ell, and let
b0=[product_i c(P_i)^e]. It is the class of a balanced norm-a ideal.
The factorization of(ell) gives the exact class relation

    2b0=-e sum_i delta_i.                              (18)

For each i choose a_i in0,...,m_i-1 with2a_i=e modulo m_i. This is
possible since m_i is odd, including m_i1 where a_i0. Hypothesis(L)
puts a_i inside0,...,e. Thus

    B=product_i P_i^(a_i)c(P_i)^(e-a_i)

is an INTEGRAL balanced norm-a ideal. Its class x=b0+sum_i a_i delta_i
satisfies2x=0 by(18); since C has odd order, x=0. It is principal.
Section2 then gives an integral relative norm a, contradicting(9),(17).

Therefore(L) forces q to be a prime power. This is a contradiction
to a proposed easy CERTIFICATE at composite non-prime-power q, not
a nonexistence proof for every actual D there: an actual norm-q ideal
can involve mixed class cancellation without satisfying(L).

### 4.2 The exponent-divisibility test, including its exact endpoint

Condition(X) implies(L), since each m_i divides m and a positive
multiple e_ell of m is at least m_i. It therefore forces q=ell^e.
There is a sharper conclusion. Since m is odd, B_ell^m is principal
balanced of nonsquare norm ell^m. Sections1--2 give ell^m>=q=ell^e,
so m>=e. But(X) says m|e, hence

    q=ell^e and exp Cl(F)=e.                            (19)

Conversely(19) immediately implies(X). Thus within(0)--(2) condition(X)
is EQUIVALENT to(19); it is not an unexamined route to a new non-prime-
power order. The accepted perfect-power prime-value lemma further
forces e to be a power of3, including e1. This uses no classicality
assumption about an actual plane. It does not assert that fields with
(19) exist for every such prime-power q, or that(X) is necessary for
actual tautness.

## 5. A9E: an actual squarefree order requires mixed nonzero classes

Assume IN ADDITION that q is squarefree and that an ACTUAL T-stable
centered planar D exists. Let alpha be its accepted norm-q character
and A=(alpha) in F. At every prime pair above ell|q, balance forces
the two exponents to be0 and1. Thus the ell-primary part B_ell of A
is balanced of norm ell, and

    A=product_(ell|q) B_ell,
    sum_(ell|q) [B_ell]=0 in C^-.                      (20)

Every nonempty proper subproduct has supported nonsquare norm
a=product_(ell in S)ell<q. By Sections1--2 its ideal is NOT principal.
Consequently no nonempty proper subsequence of the classes in(20)
sums to zero. They form a MINIMAL zero-sum sequence in the ACTUAL
minus class group. At composite q every individual class is nonzero.

For clarity, this gives the elementary bound

    omega(q)<=D(C^-)<=|C^-|,                            (21)

where D denotes the maximum length of a minimal zero-sum sequence.
The second inequality needs no uninspected zero-sum theorem: for an
ordered minimal sequence x1,...,xt, its partial sums0,x1,...,
x1+...+x_(t-1) are all distinct; any equality would give a nonempty
proper zero-sum subsequence. Hence t<=|C^-|.

Under(2), accepted R8C also identifies C^c=j Cl(E), with j injective.
Multiplication by2 is invertible on C, so x=(x+c x)/2+(x-c x)/2
decomposes C into its plus and minus groups. Therefore

    |C^-|=h(F)/h(E),

if a relative-class-number formulation is desired. The group C^-,
not an uncomputed collection of abstract labels, is essential.

Nothing here reverses(20)--(21). A minimal zero-sum sequence in a
class group does not supply balanced ideals at the specified primes,
an integral generator, or the complete actual character. The full
R8 interval criterion at q is still the unresolved actual arithmetic
problem. General nonsquare q with repeated prime factors need not
give a minimal sequence of all individual layers: a proper layer
product can have SQUARE norm, outside the obstruction(9).

## 6. A9F: an independent sharp small-multiplier gap

This elementary clause does NOT require(2) or an integral norm element.
Let p=q^2+q+1 be prime and let T<=F_p^* contain q and a prime ell|q.
Put s=|T| and d=s/3; q has order3, so d is an integer. If q is NOT
a power of ell, then

    ell^d>=p+1,
    s>=3 ceil(log_ell(p+1))>6 log_ell(q).               (22)

Indeed ell^d has cube1 modulo p, so its residue belongs to the THREE
distinct roots1,q,q^2 of X^3-1. If1<ell^d<p, it must equal one of
these three ordinary integers. It cannot equal1; equality with q or
q^2 would make q a power of ell by unique prime factorization.
Equality ell^d=p is also impossible since ell<p is a different prime.
Thus ell^d>=p+1, proving both inequalities. No factor scan is used.

In particular, for an ACTUAL prime-modulus planar set with full
numerical multiplier group M and least prime ell|q,

    |M|<=6 log_ell(q) IMPLIES q is a power of ell.       (23)

At q=ell^e, the order of ell modulo p is exactly3e: it divides3e;
any proper divisor u of3e is at most3e/2<2e, making
0<ell^u-1<ell^(2e)+ell^e+1=p, contradiction. The actual group M is
odd and contains ell, so if the bound in(23) holds, |M| is an odd
multiple of3e at most6e; hence |M|=3e and M=<ell>.

This is a restricted small-multiplier prime-power theorem. It does
NOT prove that every actual M satisfies its added upper bound, does
not make an arbitrary cyclic plane Desarguesian, and does not resolve
the large nonsaturated or saturated branches. The same inequality
(22) may be applied to the known subgroup generated by prime divisors
of q, without identifying that subgroup with the full M. All such
applications retain prime p; no composite-factor substitution is made.

## 7. What is genuinely settled by this candidate, and the exact gap

The known small-norm theorem is used on PROPER factors rather than
only on q itself. In the stated odd-class-number arithmetic domain it
forces every proper supported nonsquare balanced ideal to be nonprincipal,
gives compulsory minus-class orders, and proves that the two easy R8
sufficient tests certify only prime-power orders. The class-number-one
specialization similarly forces q prime. These are exact restrictions
on proposed arithmetic certificates, not assertions that those easy
tests were necessary for actual difference sets.

At squarefree non-prime-power q, actual existence would require mixed
nonzero ideal classes whose full sum vanishes and whose proper sums
do not. No theorem here prevents such cancellation. For repeated
prime factors, square-norm partial products require additional work;
an assertion that all integral Weil numbers factor by rational prime
norms is false already for the existing norm8 example. Even h(F)
retains the old unit-norm obstruction. Composite v retains the full
joint Fourier-gluing obstruction. None is erased by the field norm
being soluble.

No new numerical q is tested, no mathematical code/CAS/large table
or old certificate is run, and no original source theorem is inferred
from an abstract. No full solution, new cutoff or priority claim follows.
TWO OTHER initially blind WHOLE audits must reconstruct ALL these
steps, the published hypotheses and the exact original
official domain before any coordinator promotion.
