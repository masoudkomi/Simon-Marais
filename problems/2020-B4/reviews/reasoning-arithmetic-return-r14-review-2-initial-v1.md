# R14 OTHER initially blind whole review 2

18 October 2026 UTC. Reviewer C, `/root/review_2017_coarsening_r1`.
This is an independent reconstruction of **NEW SQ14A–SQ14E**, not
coordinator promotion. The constructor is B. Requested inherited
gpt-6.1-sol/max; independent effective-setting readback unavailable.

The reviewed main is
`problems/2020-B4/notes/reasoning-arithmetic-return-r14-candidate-v1.md`,
16951 bytes, SHA256
`673bcde7cadb391baf6a8362295bc4ba833e40a69dd4836725b5b3de2015df7f`.
The author freeze is 7060 bytes, SHA256
`e10b1b5ed9b573e181846b4403d1dbda20515fab3ff39091ce1c8c51124919d5`.
All twelve constructor files, all 64 obligations, checks, issues,
failed routes, sources MD/JSON, worklog, administrative code and metadata
were read. The new root R14 review, including its metadata and hashes,
was not accessed. The corresponding mathematical findings are embargoed
until explicit confirmation of BOTH entire initially blind freezes.

**Disposition:** all 64 obligations pass within the displayed scope.
I found no substantive defect and request no repair. Eight closed notes
record the boundaries most likely to be lost in a later application.
This verdict does not supply an actual new difference set, a class-group
evaluation, or a full answer to 2020 B4(b).

## Domain, inputs and independence

The official open task is part (b), determining taut integers. This
packet addresses only `q=n-1>=2` with `p=q²+q+1` prime. The q=1/n=2
endpoint and composite polygon moduli are outside its new claims. No
preliminary construction is reproduced. One fixed **odd** subgroup T
of the multiplicative group modulo p must contain every prime divisor
of q. With `s=|T|`, the residue q has order 3: q³=1 modulo p, while
1<q<p and 1<q²<p. Thus 3 divides s. Oddness excludes -1 from T.
Consequently F, the fixed field of T in K=Q(zeta_p), is CM, its real
subfield E has index two, and `[F:Q]=2d=(p-1)/s`. Every prime dividing
q splits completely in F because its Frobenius lies in T. The primes
above it form d distinct conjugate pairs. No odd class-number premise
has been added.

The ordinary class group is C=Cl(F), S is the extension image of Cl(E),
V=C/S, and Gamma=C^c/S is retained. The ordinary minus subgroup
`Cminus=ker(1+c)` is a different object. The accepted TD1–TD5 body and
current MD/JSON authority were read completely, including the same-ideal
generator criterion, field-norm step, canonical offset and the kernel
Gamma. The complete accepted A9 and L13 bodies, their current MD/JSON
authorities, and their source/failure records were also read. L13 is
frontier context; it does not prove the new square argument.

C authored older fixed-subgroup/arithmetic work, including A9 and M10.
Those separately accepted inputs are not newly independently certified
by this review. In particular the nonsquare norm result is an attributed
published input. C did not construct SQ14A–E or supply its deductions.
B's authorship of earlier TD/L13 inputs is likewise not a replacement
for their separate acceptance. Root is the other reviewer of NEW R14.

An actual set enters only when the main explicitly assumes a centered
T-stable set. Enlarging an odd subgroup does not preserve this property
automatically. All other claims are conditional arithmetic restrictions
on the field/subgroup sector just specified.

## 1. The exact integral lift and its two moments

Take an integer a>=1 with p not dividing a, and beta in O_F with
`beta*c(beta)=a²`. Modulo lambda=(1-zeta_p), the residue field is F_p
and conjugation is trivial. The residue therefore squares to a².
Because p is odd and a is nonzero modulo p, precisely one of the two
signs of beta reduces to a. This sign choice is needed before fixing
augmentation; both signs are restored at the conclusion.

O_K=Z[zeta_p] gives a p-coefficient representative in Z[C_p]. The kernel
of evaluation is exactly Z*N, where N is the full group sum. Indeed a
polynomial of degree at most p-1 vanishing at zeta_p is a scalar multiple
of the monic polynomial Phi_p, and its integral coefficients make that
scalar integral. Evaluation modulo lambda agrees with augmentation
modulo p. The uniform integer shift `(a-augmentation)/p` therefore
produces a representative B of exact augmentation a. A second such
representative differs by hN, whose augmentation is hp; hence it is
identical. Negative coefficients cause no difficulty.

For t in T, the automorphism permutes the p coefficients and preserves
augmentation. It fixes the **element** beta, so uniqueness forces it to
fix B. Invariance of the principal ideal alone would not justify this
step. The actual coefficient orbits are {0} and 2d nonzero cosets of T,
all the latter of size s. Write their coefficients b0 and c_j.

Evaluation of `BB^--a²*1` is zero, so it is hN. Its augmentation is
exactly a²-a²=0, hence h=0. This is an exact group-ring identity, not
an estimate on nontrivial Fourier characters with an unspecified full
group term. Its identity coefficient and augmentation give

    b0²+s sum c_j²=a²,       b0+s sum c_j=a.

Set `r=sum c_j=(a-b0)/s`. Energy gives |b0|<=a, so r is a nonnegative
integer. Substitution gives

    sum c_j²=r(2a-sr),
    sum c_j(c_j-1)=r(2a-sr-1).

For every integer c, including a negative integer, c(c-1)>=0. If r=0,
the energy equation gives every c_j=0 and b0=a. The chosen beta is a
and the original beta is +/-a. If r>0, division by the positive r gives
`sr<=2a-1`. Thus s>=2a forces rationality. This proves SQ14A without
requiring a minimal-support representative or 0,+/-1 coefficients.

At `s=2a-1`, a>=2, one obtains r=1 and `sum c_j=sum c_j²=1`.
All c_j are then 0 or 1, with exactly one equal to 1, and b0=1-a.
This is only a necessary endpoint shape; the other autocorrelations
have not been checked for an arbitrary such shape. The candidate
does not claim realization. At a=1 the standing s>=3 forces +/-1.
a=0 and p|a are excluded; p does not divide any supported a, and the
small range also implies this exclusion from s<=p-1.

## 2. Principal balanced ideals and the square-unit correction

Suppose an integral ideal I satisfies `I*c(I)=(a)` and is principal,
I=(gamma). Its generator is integral. The element
`epsilon=gamma*c(gamma)/a` lies in E, is totally positive, and has
trivial ideal in F. Both epsilon and its inverse are integral in F
and hence in E, so epsilon is an O_E unit. None of this shows that
epsilon itself is a norm of an F-unit.

Instead use `beta=gamma²/epsilon`. The inverse unit is integral, so
beta is integral, `(beta)=I²`, and direct conjugation gives
`beta*c(beta)=a²`. Under 2a<=s, SQ14A yields beta=+/-a, so the **same**
ideal I² is (a). For each rational prime ell in a, ell!=p and it is
unramified. If ell has rational exponent f in a, every prime above
ell has exponent f in (a). From I²=(a), every f is even and every
valuation of I is f/2. Thus `a=b²` and `I=(b)`. Conversely this
rational ideal is principal and has balance a. a=1 gives O_F.

This proves the exact iff in SQ14B. It removes no unit defect on I
itself outside this range, and it requires neither an odd class number
nor a square root of epsilon. The distinction between the corrected
generator of I² and an arbitrary generator of I is essential.

## 3. Refined and ordinary injections, including repeated primes

For supported positive a, TD1 defines the canonical label rho(I,a)
using an actual field norm and a decomposition of ideals of the form
J/c(J). Its zero is equivalent to an integral exact norm-a generator
of the specified ideal I. This does not follow merely from [I]=0.
The quotient retains Gamma. This accepted criterion is used with a²
as well as a; both are still supported positive integers.

If rho(I,a)=rho(J,a), form the integral product B=I*c(J).
It has balance a² and zero rho by additivity and conjugation. TD1
gives an integral generator of **B**, with conjugation norm a².
SQ14A, using 2a<=s, gives B=(a). Since J*c(J)=(a), ideal cancellation
gives I=J. No fractional quotient was improperly fed into an integral
element theorem.

Write `a=product ell_i^f_i` over distinct rational primes. Complete
splitting and nonnegative valuations show that every balanced ideal
is uniquely

    product_(i,j) P_(i,j)^u_(i,j) c(P_(i,j))^(f_i-u_(i,j)),
    0<=u_(i,j)<=f_i.

There are d pairs above **each** ell_i, so the exact count is
`product_i(f_i+1)^d`. This includes repeated prime powers and has no
support away from a. Injectivity proves the lower bound for |V|.

For completeness, take I0 with every u=0 and choose the same field
norm z as in TD1. If I0/(z)=J0/c(J0), then
`I(u)/(z)=J0*product P^u / c(J0*product P^u)`.
Thus the actual offset is rho(I0,a) and the actual step is `[P]+S`.
There is no division by two, arbitrary choice of a half, or claim that
an abstract compatible label tuple has been realized by a field ideal.

If instead the ordinary classes of I,J agree, B=I*c(J) is ordinary
principal and has balance a². To use SQ14B here requires the stronger
`2a²<=s`. At that balance SQ14B gives B=(a), so again I=J. All [I]
lie in Cminus because I*c(I) is principal. The ordinary image size
must not be identified with |V| when even class groups are allowed.
At a=1 both boxes have the single ideal O_F and the bound is 1.

## 4. Orders of actual balanced prime ideals

A balanced norm-ell ideal J chooses one prime in each conjugate pair.
For every u>0, the paired valuations of J^u are u and 0. A rational
ideal has equal conjugate valuations, so no J^u is rational.

Let R be the finite ordinary order of [J]. Then J^R is principal
with balance ell^R. If `s>=2ell^R`, SQ14B would force it to be rational.
Consequently `s<=2ell^R-1`. The proof permits R=1 in the definition
and excludes it only where the inequality requires exclusion.

Let r be the order of rho(J,ell). TD1 gives an integral exact generator
of the same ideal J^r, with norm ell^r. For odd r the accepted published
nonsquare bound applies; it yields `ell^r>=q`. For mixed q equality
would make q a power of ell, so the inequality is strict. For even r,
put a=ell^(r/2). Its generator cannot be +/-a because J^r is not
rational. SQ14A gives `s<=2ell^(r/2)-1`.

Under 2ell<=s, SQ14B makes [J] nonzero. A refined label of order 1
would principalize J. A label of order 2 would give a norm-ell²
generator of J² and SQ14A would make J² rational. Thus these specified
labels lie outside V[2]. This is not a proof that Gamma is zero or
that arbitrary two-torsion classes cannot occur elsewhere in V.

## 5. Mixed least-prime application and the actual-set boundary

Suppose q has at least two distinct prime factors and ell is its least
prime factor. The other factor is larger than ell, so q>ell². Since
ell lies in T, `ell^(s/3)` is a cube root of 1 modulo p. The three
distinct roots are 1,q,q², since p is prime. If its positive integer
value is less than p, it cannot be 1 and must equal q or q². Either
would make q a power of ell. Equality to p is impossible because
ell!=p. Therefore

    ell^(s/3)>=p+1>q²>ell^4.

It follows that s/3>4. This quotient is an odd integer, hence s>=15.
When ell<=7, s>2ell. Complete splitting supplies actual balanced
norm-ell ideals, so the preceding statements imply that all their
ordinary classes are nonzero, all their refined labels lie outside
V[2], V is not of exponent at most 2, and |V|>=2^d. These are field
restrictions even without a difference set.

Only now assume an actual centered T-stable set D of size q+1. It
has a nonzero point, and every nonzero orbit has exactly s points;
hence s<=q+1. It follows that `2d=q(q+1)/s>=q`, and the integer d is
at least ceil(q/2). This proves the stronger necessary lower bound
`|V|>=2^ceil(q/2)` with its actual-set hypothesis intact. For ell=2,
R<=2 would give `2ell^R<=8<s`, contradicting the ordinary order bound,
so every such R is at least 3. No class group is evaluated here.

## 6. Sources, failures, checks and remaining gap

The operative published nonsquare theorem and proof were checked; its
use is confined to odd r. Exact source/read limits are in the companion.
No unread weighing-matrix or unique-difference proof is imported.

I tested the possible loss of augmentation, a residual full-group
defect, negative coefficient signs, ideal-only fixation, a hidden unit
norm assumption, fractional rather than integral collisions, a factor
two in the refined steps, unequal ordinary/refined thresholds, repeated
prime powers, r or R equal to 1, and actual stabilization of an enlarged
subgroup. Each is handled by an explicit hypothesis or the derivation
above. These are hand deductions, not computational tests or searches.

The low range 2a<=s does not generally reach a=q, because an actual
set only supplies s<=q+1. An actual norm-q ideal can contain no small
principal balanced divisor and still survive all statements here.
The lower bound for |V| may be satisfied by a larger unknown class
group. No parameter is shown to violate it. No unrestricted existence,
nonexistence, prime-power classification, annual solution or novelty
claim has been established by this packet or review.

Administrative Python is confined to labels, JSON, byte fingerprints
and preservation. No mathematical program, native child, class/order
scan, CAS, source-author run or old freezer/certificate replay was used.
No pending source call or approval is left. Only the assigned new
review prefix is written. Promotion remains solely the coordinator's
decision after both complete independent reviews and reconciliation.
