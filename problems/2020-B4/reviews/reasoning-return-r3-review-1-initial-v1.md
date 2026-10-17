# Fresh whole reconstruction R1: fixed subgroups and relative traces

2026-10-17 UTC. Coordinator root, nonconstructor of this new packet.
This initial whole report is completed and frozen before reading any
peer review or findings for the packet. It is a review recommendation,
not acceptance. The accepted older normalization is a dependency, not
a new proof being independently certified here.

Target: `notes/reasoning-return-r3-candidate-v1.md`, SHA-256
`2cb5803b20cdcc96961956773f02a3fe2e00f0ae9a4bee8df56af0ec2cd86796`;
constructor freeze SHA-256
`413351e9d6d6b9e8c463ba6b3ad230f2d4440c5042711df882f879a7b82a02ed`.
I read the entire candidate, source checks, obligations and source
record; the complete accepted original P1–P6 argument, reviewed
register, source clarification and acceptance; and the official
normalization. Only 2020 B4(b) is in scope.

I find no substantive mathematical objection on the explicit domains.
The seven claims below reconstruct completely. The full cyclic prime
power conjecture remains open. The arguments are classical structural
reconstructions and a restricted consequence; novelty is not established.

## 1. Common fixed subgroups and the actual subplane

The accepted common sum-zero translate really makes every numerical
multiplier fix D setwise: summing tD=D+h gives (q+1)h=0, and
gcd(q+1,v)=1. It does not assume pointwise fixedness. The accepted
First Multiplier Theorem supplies every prime divisor of q; it remains
an attributed theorem import with its previously recorded scope.

If z is a nonzero common fixed group element, its unique ordered
representation z=d-e is sent by every chosen multiplier to another
representation of exactly z. Uniqueness fixes d and e individually.
Hence E=D intersect H represents every nonzero element of H exactly
once, and f(f-1)=h-1. No averaging, orbit-stabilizer division or
coprimality with the multiplier-group order is being assumed. For
h=1, f is 0 or 1; for h>1 it is at least 2, and h=m²+m+1 with
m=f-1. This is an actual difference set in H.

For cyclic G, the simultaneous annihilator of the integers t_i-1
has order gcd(v,t_1-1,...,t_s-1), by the elementary description of
subgroups of Z/vZ. A nonidentity multiplier acts nontrivially on G,
so its common fixed subgroup is proper. For m>=2 the incidence
structure on H has lines E+x, x in H: two points of H have their
unique difference pair in E, so the full-plane translate parameter
also lies in H. Conversely the full line intersects H in that
translate of E. Thus this is an embedded proper subplane, with no
quotient occupancy substituted for E.

Here is an independent check of the size bound. Choose an external
point P. Two extended subplane lines through P would meet outside
the subplane, contradicting their already unique subplane intersection.
If one such line goes through P, its m+1 subplane points are accounted
for together, and the other m² subplane points require m² distinct
additional lines through P. Thus q+1>=m²+1. If there is no such
line, all m²+m+1 subplane points need different lines, which is
stronger. For m=1 the displayed q>=1 inequality is automatic,
without invoking a nondegenerate subplane. Consequently
h=m²+m+1<=q+sqrt(q)+1. Prime-order multiplier orbits have lengths
one or ell; counting them gives q-m divisible by ell when h>1.
For h=1 the same single membership decision for 0 is retained.

## 2. The restricted cofactor family

With q=pu, reducing modulo p-1 gives q²+q+1 congruent to
u²+u+1. Therefore F5 is an exact gcd identity. If p is20 modulo57,
p-1 is divisible by19 and not by3; for u=7 the fixed subgroup
has order gcd(p-1,57)=19. The equation f(f-1)=18 has no
integer solution because the consecutive values at f=4,5 are12,20.
This excludes precisely the asserted restricted family.

The one hand prime certificate for761 covers every prime at most
sqrt(761)<28. Independently, the listed remainders for divisors
2,3,5,7,11,13,17,19,23 are respectively1,2,1,5,2,7,13,1,2,
all nonzero. Also761=57*13+20, q=5327, n=5328,
q=3 modulo4 and2 modulo3. The old two congruence tests therefore
do not apply at this example. No independence from all published
tests, new range, infinitude assertion or minimality follows.

## 3. Complete involution fiber count

Because v is odd, (1-t)/2 and (1+t)/2 are complementary
idempotents, with G=A direct-sum B. Set a=|A|, b=|B|.
Since t is nonidentity, a>1. Fibers D_y in A are invariant under
negation. If x,z are distinct and not opposite, the representations
x-z and (-z)-(-x) are different ordered pairs for the same
nonzero difference. Thus fibers have at most two elements; a
singleton must be0, and a double fiber is {x,-x}, x nonzero.

Every nonzero element of A must occur as a difference with B
coordinate zero. Only a double fiber can supply it, and each
supplies exactly two different nonzero differences because A is
odd. Hence2R=a-1. If b=1, D is contained in one fiber of size
at most2, impossible since q+1>=3. Applying the already proved
fixed-set argument to B gives b=s²+s+1 and f=s+1, s>=1.
Counting D gives q+1=f+2R=s+a. Substituting a=q-s+1 into
ab=q²+q+1 gives exactly (q-s)(q-s²)=0.
The root q=s gives a=1 and is excluded. The remaining root
is q=s², with s>=2 because q>=2. This establishes F8 without
the classification of involutory plane collineations.

The factors A0=m²-m+1 and B0=m²+m+1 are odd and coprime:
their gcd divides2m and each is coprime to m. The congruences
m³=-1 modulo A0 and m³=1 modulo B0 follow from their
defining quadratic equations. Cyclicity supplies the unique
subgroups of these orders, so t and multiplication by m³
agree on both factors and hence on G. The full multiplier
order, rather than an order at one prime factor, is what
produces this unique involution. An even-order multiplier
therefore contradicts nonsquare q by its halfway power.

## 4. Coherence of local 2-parts

Any abelian2-group with a unique involution is cyclic. One
can prove this by induction on its size: doubling has a
kernel of order2, and its proper image again has at most
one involution. A generator of the cyclic image lifts to
an element of full group order. The order2 base case is
immediate. Thus the stated multiplier Sylow restriction
is justified, using commutativity.

For a global order 2^a s, s odd, a local order has the
form2^b d with d|s and b<=a. Raising x to2^(a-1)s
gives the local identity if b<a and the local involution
if b=a. At an odd prime power the only nonidentity
involution is-1: the relatively prime odd parts of
z-1 and z+1 cannot both contain that prime. Comparison
with m³ proves all of F10. Inconsistency between two
known multipliers can exclude an order, but passing the
test does not establish that a unit is a multiplier.

## 5. Exact relative trace and the remaining lift

First check the sum-uniqueness step, including repeated
summands. If d1+d2=d3+d4 and d1!=d3, then
d1-d3=d4-d2 is nonzero, so uniqueness forces
d1=d4 and d3=d2. If d1=d3, then d2=d4 directly.
Thus unordered pairs, with repetitions, are uniquely
determined by their sum. Multiplication by two is
invertible throughout.

Projection P=beta_*(D) counts a nonfixed pair twice
at its average, and an element e of E once at e.
The convolution (E/2)*(E/2) counts repeated pairs
once at e and distinct unordered E pairs twice at
their average. Sum uniqueness makes these supports
disjoint except for the repeated E pairs, which
appear once in each expression. Every nonzero
coefficient of their sum is therefore2. Its total
augmentation is m²+1+(m+1)²=2(m²+m+1)=2|B|.
There are exactly |B| available positions, proving
P+(E/2)*(E/2)=2U_B coefficient by coefficient.

This gives P=1 on E,0 on the distinct-pair averages,
and2 on the remaining m(m-1)/2 positions. Applying
a nonprincipal character gives chi(P)=-chi(E/2)².
The half-map is an automorphism of B, so E/2 is
also a planar difference set of order m and its
nonprincipal character magnitude squared is m.
Thus the claimed phase equation and norm q both
follow; the norm alone omits the phase information.

If a nonzero A coordinate appeared in two different
fibers, the corresponding difference in B would
have a nonfixed representation, contradicting F1.
Each nonfixed fiber is already a sign pair. Counting
now shows the R positions are bijective with the
(|A|-1)/2 nonzero sign pairs. This proves F13/F14,
but does not make an arbitrary bijection sufficient.

For the exact sufficiency interface, take the proposed
L_b, all symmetric under inversion in A. The B
coefficient delta of DD^(-1) is precisely
sum_b L_b L_(b-delta). At delta0 it equals
(m+1+2|R|)*1+sum_(sign pairs){X^(2f)+X^(-2f)}
=q*1+U_A, because doubling permutes the nonzero
sign pairs. For nonzero delta it must equal U_A.
These equations are exactly the full difference-set
identity on every coefficient of A direct-sum B,
and are sufficient as well as necessary. Taking
augmentation of the identity for P only checks
their coefficient sums, not those individual
coefficients. No hidden lifting theorem remains
inside the iff statement F15.

## 6. The relaxation barrier and the integral boundary

For r=sqrt(q), k=q+1, b=(k-r)/v, both b and
r are positive and the augmentation of A=r*1+bU
is k. Its product has identity term q and U
coefficient2rb+vb²=(k²-q)/v=1. Every unit
multiplier fixes both1 and U. The identity
coefficient of A is r+b>1 while its other
coefficients are positive. Thus this is a real
nonnegative norm solution but never a subset.
It refutes only the expressly relaxed inference.

Conversely if an integral C has the complete
original norm identity and augmentation k,
the identity coefficient yields sum c_g²=q+1=k.
Subtracting sum c_g=k gives sum c_g(c_g-1)=0.
Every summand is a nonnegative integer, even
for negative c_g, hence all c_g are0 or1.
Different augmentation, conductor or norm
premises cannot be silently substituted.

## 7. Source audit, adversarial scope and disposition

Independently opened the original BBB author PDF
https://aeb.win.tue.nl/preprints/hermitian1.pdf,
dated7March1990, six pages. Read all applicable
Section2 setup, involution argument and Lemmas1–2
with proofs on pages1–2. These assume an abelian
planar difference set with a multiplier-fixed
translate and an involution, without a prime-power
order hypothesis. The later Desarguesian code
theorem is not used. F3 is correctly attributed
to the original Lemma2; F2 replaces the source's
geometric classification with the full fiber
argument checked above. The Mann original is
not a new proof premise. Neither its unavailable
bytes nor the missing BBB byte hash is fabricated.

The audits covered h=1, h=3, empty common fixed
intersection, nonidentity versus identity T,
proper versus improper subplanes, composite v,
nonpointwise multiplier stability, singletons
containing0, b=1, q=s, repeated sums, convolution
versus inversion, quotient versus intersection,
all local2-parts, real versus integral norms,
and the exact lift coefficient equations.
No substantive gap was found. A second initially
blind fresh whole audit and coordinator comparison
are still required. No general prime-power or
annual classification, published-range improvement,
source theorem refutation or originality is claimed.

No mathematical program, enumeration, CAS or
large calculation ran. Commands read named
records; administrative hashing freezes this
review. No peer2020 findings were read before
this initial freeze. Account use was26%, with
the90%-total ceiling and integration reserve.
