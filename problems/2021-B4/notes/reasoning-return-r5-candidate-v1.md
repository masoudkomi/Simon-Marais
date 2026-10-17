# A positive selector constant, bounded witness depth, and two J15 consequences

2026-10-17 UTC. **Candidate proof - unverified.** Constructor
`review_2017_coarsening_r1`; requested `gpt-6.1-sol` / `max`, verified
effective-setting readback unavailable. Two OTHER fresh initially blind
whole nonconstructor audits are required. Only2021 B4(b) is investigated.
No annual classification, complete degree20 or J15 exclusion, rational
counterexample, finite-mask enlargement, or novelty is claimed.

This checkpoint supplies: R5A, an exact nonzero selector constant and
its valuation divisibility for every allowed selector; R5B, an explicit
degree20 witness-depth bound10 without mask enumeration; R5C, a symbolic
degree-p+1 extension of the previously accepted J15 unrecycled-carrier
argument; R5D, an exclusion of the precisely specified repeated-root
EVEN LADDER by combining accepted RC2 and PN4; and R5E, the resulting
five-odd-unit essential-center condition, dropping a3 from TA2's six
units. These are necessary restrictions and scoped subfamily results.
The remaining actual rational-lifting problem is not solved.

## 0. Exact background and distinctions

The official problem requires f in Q[X] and an actual RATIONAL common
root of f and each nonconstant derivative. It does not assume all roots
of f rational or real. H_k denotes the Hasse derivative f^(k)/k! over Q.
We do not reproduce the already known preliminary part(a).

Use the accepted normalization for d=p+1, p>=5 prime, attributed to
Castryck--Laterveer--Ounaies (CLO), Section3.4 and Lemma17, with the
rational affine change checked in the reviewed project normalization:

    f(X)=X^d-d X^(d-1)
             +sum_(j=2)^(d-2) binom(d,j)a_j X^(d-j),
    a_j in Z_(p), a0=1, a1=-1,
    f(0)=f'(0)=f(1)=0.                              (N)

The center1 is simple. Every other nonzero root has positive p-adic
valuation; every RATIONAL such root consequently has integer valuation
at least1. The other roots can be nonrational and ramified. Put

    D_j(X)=H_(d-j)(f)(X)/binom(d,j)
          =sum_(k=0)^j binom(j,k)a_k X^(j-k),
                1<=j<=d-2.                         (D)

This is the monic integral normalized derivative BEFORE reduction.
Its rational zeros are the same as those of H_(d-j). Each
binom(p+1,j) for2<=j<=p-1 has valuation exactly1; write

    beta_j=binom(d,j)/p in Z.

The complete accepted bodies used are identified in the source packet.
In particular reviewed-return-r3-v1.1.md accepts the exact seven frozen
return texts, including G1/G2, RC2 and TA1. The independently accepted
reviewed-odd-support-exclusion-v1.1.md supplies PN4. Their historical
candidate labels do not erase those acceptance scopes, and their bodies
remain unchanged. This new packet does not rerun their finite certificates.

## 1. R5A: every selector has a nonzero integer collapse constant

For each j=2,...,d-2 choose ANY actual rational common root w_j of
f and D_j. No center-priority convention is needed. Set w_1=1,
as D_1=X-1. Define the selector

    I={1} union {j in{2,...,d-2}:w_j=1}.

This is a set of SELECTED CENTER INDICES. It is NOT necessarily the
support of the normalized coefficients modulo p: selected center
coefficients can be nonunits. All I with1 in I and max I<=d-2 are
covered by the integer identities below, including even indices.
There is no restriction to PN's odd-support class.

Collapse each selected noncenter witness to0 and define ordinary
integers b_j by

    b0=1;
    b_j=0 if j notin I;
    b_j=-sum_(k<j) binom(j,k)b_k if j in I,
                              1<=j<=d-2.           (1)

In particular b1=-1. Put

    F_I(Z)=sum_(j=0)^(d-2) b_j binom(Z,j),
    q_I=-1+sum_(j=2)^(d-2) beta_j b_j.

**R5A.** For EVERY such I,

    p q_I=F_I(d)=(-1)^|I| d(I;d) !=0,             (2)

where d(I;n) is the classical number of permutations of n letters
with descent set exactly I, extended polynomially in n. In particular
q_I is a nonzero ordinary integer. If

    nu_w=min {v_p(w_j):2<=j<=d-2, w_j notin{0,1}},

then that set is nonempty and

    p^nu_w divides q_I,
    p^(nu_w+1) divides d(I;d).                      (3)

The valuation minimum concerns selected positive NONCENTER witnesses,
not all roots and not a maximum valuation. Zero is omitted from the
minimum, rather than assigned an illegitimate finite valuation.

### Exact descent identification

The recurrence used is classical, stated with proof in
Diaz-Lopez--Harris--Insko--Omar--Sagan, *Descent polynomials*,
Proposition2.1. For m=max I and I^-=I-minus{m},

    d(I;Z)=binom(Z,m)d(I^-;m)-d(I^-;Z).             (4)

Its hypotheses for actual counts are integer n>m. A combinatorial
verification chooses the m values in a first block with internal
descents I^- and leaves the final block increasing; splitting according
to the comparison across the join gives(4). Polynomial extension then
gives the identity for the variable Z.

When the next selected index m is added to(1), b_m=-F_(I^-)(m), and

    F_I(Z)=F_(I^-)(Z)-F_(I^-)(m)binom(Z,m).          (5)

Starting at F_empty=1, equations(4),(5) give
F_I=(-1)^|I|d(I;Z) by induction. This fixes the exact index orientation;
no complement, reversal or independently selected support is used.
The general Casas-Alvero/MacMahon connection is already attributed in
the accepted PP1 packet and Marashdeh TheoremB; it is not a new method
claimed here.

Since d>max I, d(I;d)>=1. Explicitly, use the ascending runs with
lengths determined by I; assign the largest available values to the
first run, the next largest to the second, and so on, increasing within
each run. Joins are descents and internal comparisons are ascents.
Thus every prescribed I occurs. This is positivity over Z, not a claim
that its reduction modulo p is nonzero.

Now b0+b1*d=1-d=-p and all the other binom(d,j) are p beta_j.
Evaluating F_I at d proves p q_I=F_I(d), and positivity proves the
nonzero assertion in(2).

### Comparing the actual and collapsed coefficients

If no positive noncenter w_j were selected, all w_j would be0 or1.
The exact triangular equation D_j(w_j)=0 would then force a_j=b_j
for all j. But f(1)=0 would give F_I(d)=0, contradicting(2).
Thus nu_w is finite, positive and integral.

Inductively a_j-b_j belongs to p^nu_w Z_(p). It is true at j=0,1.
If w_j=1, subtract its actual triangular equation from(1); all earlier
coefficient differences remain divisible by p^nu_w. If w_j!=1 then
b_j=0, and

    a_j=-sum_(k<j) binom(j,k)a_k w_j^(j-k)

is divisible by p^nu_w because every exponent is positive and all
earlier a_k are p-integral. This includes w_j=0 exactly.

The actual divided center equation is

    -1+sum_(j=2)^(d-2) beta_j a_j=0.

Subtract it from q_I. Every term beta_j(b_j-a_j) is divisible by
p^nu_w, proving(3). q_I is an integer, so this is ordinary integer
divisibility as well as a statement in Z_(p). No denominator is
inverted after reduction.

R5A removes the old qualification "if q0 is nonzero" wherever q0
is exactly this0/1 collapse for a specified selector. It does not
assert a p-adic unit: indeed every actual selector must satisfy the
stronger p² divisibility of its descent count.

## 2. R5B: a uniform finite valuation bound, and nu<=10 at degree20

For an arbitrary n>=2, write n=3s+t with t in{0,1,2}, and define

    U_n=n!/[3^s * 2^[t=2]].                         (6)

Every fixed descent set of a permutation of n letters has at most U_n
realizations. To prove this, partition POSITIONS into s triples and,
if present, a final singleton or pair. In a triple the two prescribed
comparison patterns ++,+-,-+,-- allow respectively

    {123}, {132,231}, {213,312}, {321}

as relative orders. Thus there are at most2 of the6 relative orders,
a fraction1/3. A prescribed comparison in a final pair allows1 of2.
Choose values for all blocks, then arrange inside each block. Relative
orders in disjoint blocks vary independently. Ignoring comparisons
BETWEEN blocks only enlarges the count. Consequently the allowed number
is at most n! times (1/3)^s and, for t=2, another1/2. This proves(6)
without any independence assumption on overlapping comparisons.

Let K_p=max{e>=0:p^e<=U_(p+1)}. R5A now gives for every selector

    nu_w<=v_p(q_I)<=K_p-1.                          (7)

This is a uniform quantitative obstruction at every fixed degree p+1.
It bounds the least valuation in every selected positive-witness set,
not every rational root or every selected witness individually.

For p=19,d=20, six triples and one pair give EXACTLY the bound

    U_20=20!/(2*3^6)=1668657070080000,
    19^12=2213314919066161 > U_20.

A positive count divisible by19^(nu_w+1) cannot have nu_w+1>=12.
Therefore

    1<=nu_w<=10.                                   (8)

The integer arithmetic is hand-reconstructible: 20!=2432902008176640000,
and dividing by1458 gives the displayed U_20. No mask enumeration,
Euler-number table, p-adic digit search or native mathematical program
is used. The known sharper maximal-descent-count theorem is unnecessary.

**Degree20 consequences.** In ANY full rational-witness counterexample
in normalization(N), regardless of J, at least one selected actual
positive noncenter rational witness has valuation at most10; every chosen
witness selector has one. In particular a rational witness cover using
only0,1 and roots in19^11 Z_(19) is impossible. This is not a bound on
global rational heights or on valuations of unused roots.

In an equal-valuation J15 branch (including each single-low-center
pattern), all nonzero small roots have the same integer nu, and the
fractional cluster is unavailable to rational witnesses. R5A guarantees
that some selected positive witness exists, so nu_w=nu and

    nu<=10.                                        (9)

For unequal valuations only the minimum among ACTUALLY selected positive
witnesses is bounded; no bound on every deeper small slot is inferred.
For the old D3 q0, it is always nonzero and the sharper selector-specific
nu<=v_19(q0) remains available. Equations(8),(9) exclude a uniform
high-valuation subfamily, not all69 J15 masks or all684 surviving masks.

## 3. R5C: the long Eisenstein carrier is unrecycled for symbolic p+1

This extends the accepted J15-multiplicity-two G1 mechanism; its method
is attributed to that packet and no new-method claim is made.

In normalization(N), put

    J=max{j in{2,...,d-2}:v_p(a_j)=0},
    h=d-J, e=J-1,

and assume J>=d/2. J exists by the divided center equation. The accepted
Newton theorem gives exactly e roots of valuation1/e. Here e>=2 and
2<=h<p. Let g be their product factor, monic of degree e over Q_p.

**R5C.** There is ONE monic irreducible factor Q in Q[X] containing all
these e roots, and

    gcd(Q,H_k(f))=1 for EVERY 1<=k<=d-1.             (10)

In particular, for R=f/Q, every gcd(f,H_k(f)) divides R, and
deg R<=h+1. This does not make R a Casas-Alvero polynomial and does
not by itself rule out a rational witness cover of R's roots.

### Local factor and exact low-derivative valuations

Write f=sum c_l X^l. Then v(c_h)=1, c_p=-d is a unit,
every middle c_l has valuation>=1, and c_l for2<=l<h has valuation>=2
or vanishes. Constant and linear terms vanish. The supporting line
from(h,1) to(p,0) has ordinate (p-l)/e. For2<=l<h its value is at
most(p-2)/e<2, using J>=d/2; for h<l<p it is<1. At l=d its value
is negative. Hence ONLY exponents h,p are on that Newton edge.

The valuation cluster is stable under Gal(Q_pbar/Q_p), so its monic
product g has coefficients in Q_p. Each nonleading coefficient is a
symmetric sum with strictly positive valuation and lies in Q_p;
it therefore has valuation at least1. The constant coefficient has
valuation exactly e/e=1. Thus g is Eisenstein of degree e and is
irreducible. Multiplicity conventions in the accepted Newton theorem
are retained; irreducibility in characteristic0 also gives separability.

Choose pi with pi^e=p. The supporting-line check gives an integral
polynomial

    P(T)=pi^(-p) f(pi T),
    Pbar(T)=-T^p+lambda T^h,
    lambda=c_h/p mod p !=0.                        (11)

For any cluster root alpha, T0=alpha/pi is a unit and
T0bar^e=lambda. For1<=k<=h, Hasse scaling and reduction give

    H_k(f)(alpha)=pi^(p-k) H_k(P)(T0),
    H_k(Pbar)(T0bar)=lambda binom(h,k) T0bar^(h-k)!=0.

Both h<p and k<=h matter: binom(p,k)=0 modulo p, while binom(h,k)
is a unit. Therefore the exact valuation is

    v_p(H_k(f)(alpha))=(p-k)/e, 1<=k<=h.           (12)

### Global carrier and the borderline derivative

Let Q be alpha's monic minimal polynomial over Q and M=deg Q.
It divides f. Since g is alpha's irreducible polynomial over Q_p,
g divides Q over Q_p and M>=e. In particular every cluster root
belongs to this SAME global rational irreducible factor.

For k<=h, equation(12) rules out Q dividing H_k(f). For k>=h+1,
deg H_k(f)=d-k<=e. If M>e, degree already rules it out. If M=e,
then Q=g as monic polynomials over Q_p. At k=h+1 the only remaining
degree equality would force

    Q=D_e=X^e-e X^(e-1)+... .

But g's X^(e-1) coefficient is divisible by p, while -e is a unit
because2<=e<=p-2. This is impossible. Larger k have strictly smaller
derivative degree. Thus(10) holds. A rational irreducible factor shares
one derivative root exactly when it divides that derivative, so all
global conjugates are excluded, not merely the local fractional roots.

The quotient R is over Q, and coprimality with Q gives the claimed
gcd containment. No Galois-group classification, all-roots-rational
hypothesis, or unramified-field variant of CLO Proposition19 is used.

For J15,d20 the accepted m=2 G2 gives the degree14/15 global dichotomy.
R5C also applies directly to m=3: accepted T3 makes all remaining slots
rational after removing the degree14 Eisenstein factor, so ALL derivative
common-root values are rational in that triple-zero branch as well.
This is a support statement, not its exclusion.

## 4. R5D: the full repeated2R branch cannot have the long even ladder

Now specialize to the EXACT accepted D3 setting:

    d=20,p=19,J=15,ord_0 f=2,
    H3(f)(1)=0, H2(f)(1)!=0, H4(f)(1)!=0.

There is a rational simple r with nu=v_19(r)>=1 sharing H2,H4.
The other two nonzero small slots reduce to2R, R=r/19^nu mod19.
Assume those TWO SLOTS COINCIDE at a double root d0. Accepted T1
forces d0 rational. The rational roots are exactly{0,1,r,d0}, and
d0/r=2 mod19. Neither d0=2r nor a particular collision depth is assumed.

**R5D.** Under the full rational-witness hypothesis, it is impossible
that all five equations

    H6(f)(r)=H8(f)(r)=H10(f)(r)
                  =H12(f)(r)=H14(f)(r)=0            (L)

hold. Consequently at least one of these actual values is nonzero.

Proof. The accepted RC2 theorem, with exactly this normalization,
sole-H3 assumption, repeated2R root and extra ladder(L), states in
particular that H18 cannot use the center1. Its proof treats arbitrary
nu and both exact/finite displacement; its depth conclusions are not
assumed here from sample lifts. Therefore the contest's actual rational
H18 witness is noncenter. The independently accepted PN4 forbids the
conjunction of precisely this repeated-root setting, (L), and an actual
rational noncenter H18 witness. This is a contradiction. End proof.

This is a NEW COMBINATION of two accepted partial inputs, not a new
finite certificate and not an assertion that either historical packet
already stated the combination. The formerly retained depths15,16 under
(L) therefore cannot furnish a FULL rational-witness polynomial once
PN4 is also imposed. Neither packet's original frozen statement is
edited. Cases missing (L), distinct2R slots, other low-center patterns,
multiplicity3 and lower J are outside R5D.

## 5. R5E: five odd units already force a sole higher center

Retain R5D's full repeated-root setting, but DO NOT assume (L).
Assume only the following FIVE odd normalized coefficients are units:

    a5,a7,a9,a11,a13 in Z_(19)^*.                   (U)

No hypothesis on a3 is made.

**R5E.** At least one H_k with k in{6,8,10,12,14} has1 as its SOLE
RATIONAL common-root value with f. In fact its monic gcd with f is
exactly X-1, also over the algebraic closure.

Proof. Suppose every one of those five derivatives had an actual
rational noncenter common root. Starting with accepted H2(r)=H4(r)=0,
apply accepted TA1 successively at m=3,4,5,6,7. Its unit linear
coefficients are respectively a13,a11,a9,a7,a5, exactly(U). At each
step the earlier even equations have been established, and the actual
noncenter witness hypothesis is the one assumed. TA1 forces that
witness to be the ACTUAL r and its derivative value to vanish. Thus
the complete ladder(L) follows, contrary to R5D. At least one of the
five derivatives has no rational noncenter common root. The contest
supplies a rational common root, so its only possible value is1.

Here d0 is rational and all three small slots are rational. Dividing
f by X²(X-1)(X-r)(X-d0)² gives the rational degree14 Eisenstein
carrier. The accepted G1, or R5C just proved, excludes every root of
that carrier from every derivative. Thus all possible common-root
values lie in{0,1,r,d0}. Since1 is simple, the monic gcd for the
selected derivative is exactly X-1. Scalar extension adds no common
root to coprime rational factors. This proves the final assertion.

Compared with accepted TA2, a3 has been dropped because R5D now
contradicts the ladder directly; no three-value-cover construction
for H16/H18 is required at this step. This does not establish(U) in
every remaining pattern or rule out such a higher essential center.

## 6. Exact remaining obstruction and failed shortcuts

R5A--R5B show that a rational witness cover cannot be arbitrarily deep
at19, and remove a zero-constant loophole in the selector argument.
They do NOT make q_I a unit, eliminate all divisibilities modulo19²,
bound global rational heights, or prove that every remaining actual
selector lifts. Positive integers can have the required finite prime
power divisibility. The numerical bound10 leaves valuations1,...,10.

R5C removes the global irreducible carrier, not its rational residual
factor. R=f/Q does not inherit the derivative equations of f as its
OWN derivatives; applying a smaller-degree Casas-Alvero theorem to R
would be invalid. A large Galois group for Q supplies no contradiction.

R5D removes a precisely specified ladder subfamily. It does not prove
that any higher even witness must be r without the relevant TA1 unit
hypothesis, and cannot be applied to two distinct roots sharing residue2R.
R5E requires all FIVE units in(U). If a needed odd unit is absent,
the unit-linear injectivity mechanism can fail. Even when(U) holds,
the resulting actual sole center is a necessary compatibility condition,
not a contradiction. The known prime-degree result cannot be applied
to the odd degree19 critical-value polynomial from the old return
packet: no Casas-Alvero property for that polynomial has been proved.

The old prime5 bad quartic residue and the2011 correction remain valid.
No first-residue or CRT shortcut closes degree20. Rational witnesses
still do not imply all roots rational or real, so CLO Proposition19
and all-real-root interpolation cannot be imported under weaker hypotheses.

A useful next target is the first higher even derivative that fails
to vanish at r in R5D. With its preceding TA1 linear coefficient a
unit, that failure forces a sole center; without that unit, its small
normalized derivative has a higher-multiplicity initial root. A proof
controlling these successive nonunit initial forms, while keeping
actual rational witnesses, could strengthen R5E. No such general
transfer theorem is established here. No larger mask scan is proposed
as a substitute for that missing inference.

All arguments above are exact hand reasoning. There is no mathematical
program, CAS, enumeration, enlarged finite table or source-certificate
rerun. Only administrative source/hash verification is executable in
the freeze. All earlier frozen bytes are preserved; author-owned repairs
and two other fresh whole audits are required before coordinator promotion.
