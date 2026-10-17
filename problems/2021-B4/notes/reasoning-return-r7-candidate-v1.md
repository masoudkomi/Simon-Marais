# A weighted first-break fork and the two rational double-root frames

2026-10-17 UTC. **Candidate proof - unverified.** Constructor
`/root/review_2021_reasoning_j15_r2`; requested gpt-6.1-sol/max,
independently verified effective settings unavailable. Two OTHER fresh
initially blind nonconstructor WHOLE audits are required. Only2021 B4(b)
is researched. No full repeated-root branch, J15 mask, degree20, annual
classification, rational lift or novelty is claimed.

The new proposed improvement is quantitative: the quadratic argument does
not require its coefficient to be a unit. Its valuation need only be
STRICTLY below the common small-root valuation. At the first broken even
equation this replaces R6's two nonunits by a weighted triple of depths
nu,2nu,3nu. A rational affine involution exchanges the two double roots
and preserves that remaining alternative. The minimal-cover observation
itself was already present in accepted RC3; it is not advertised as new.

## 0. Exact setting and accepted inputs

The [official problem](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf)
requires f in Q[X] with an ACTUAL RATIONAL common root for every derivative
order1,...,19. Its other roots need not be rational or real. No proof or
investigation of preliminary part(a) is supplied.

Use the accepted normalized degree20,J15,multiplicity-two sole-H3 setting:

    f=X^20-20X^19+sum_(j=2)^18 binom(20,j)a_j X^(20-j),
    a_j in Z_(19), a0=1,a1=-1,
    f(0)=f'(0)=f(1)=0, ord_0(f)=2,
    max{j:v_19(a_j)=0}=15,
    H3(f)(1)=0, H2(f)(1)!=0, H4(f)(1)!=0.          (S)

Write v=v_19 with v(19)=1 and v(0)=infinity. H_k is the characteristic-zero
Hasse derivative f^(k)/k!. The center1 is simple. Accepted D1/D3 supply
the ACTUAL rational simple root r sharing H2,H4, with nu=v(r)>=1.
Make the ADDITIONAL ACTUAL-double-root assumption: the two other small
slots coincide at s. T1 then forces s rational. Equality of residues alone
does not imply this extra assumption. The complete rational root set is

    {0,1,r,s}, v(s)=nu, s/r=2 mod19, delta=s-2r.

The fourteen fractional roots have valuation1/14. Actual rational division
gives f=X^2(X-r)(X-s)^2(X-1)g, with g a rational Eisenstein polynomial
of degree14 at19. Accepted G1/R5C excludes its ENTIRE global root set
from every derivative. Thus every derivative common-root value, including
over the algebraic closure, is one of0,1,r,s. No local factor is assumed
rational without this actual division.

Define monic normalized derivatives BEFORE reduction:

    D_j=H_(20-j)(f)/binom(20,j)
       =sum_(k=0)^j binom(j,k)a_k X^(j-k),
    beta_j=binom(20,j)/19, 2<=j<=18.              (N)

All beta_j are19-adic units. An essential center means that1 is the
sole common-root VALUE of f and the derivative. Since1 is simple and the
carrier is excluded, its full monic gcd is then X-1. Essential double
roots0/s, by contrast, can occur with gcd multiplicity one OR two.

Direct accepted inputs, read in full in their recorded scopes:

1. J15 D1/D3, rational normalization, Newton/T1 and G1/R5C as above.
   Normalization is attributed to Castryck--Laterveer--Ounaies (CLO),
   Section3.4/Lemma17, with rational affine descent checked separately
   in the accepted project body. No all-roots-rational theorem is used.
2. R5D: in this full ACTUAL-double branch, H6(r),H8(r),H10(r),H12(r),
   H14(r) cannot ALL vanish. This accepted combination retains its
   separately audited RC2/PN4 dependencies, not rerun here.
3. The accepted R6 Euler estimate, stated precisely next. R6's unit
   quadratic proof is not silently substituted for the weighted proof
   below. The old minimum selected-witness bound10 is not a maximum
   root/displacement bound and is not needed by the new proof.

For 3<=m<=7 put e=2m, j=20-e, h_k=H_k(f)(r), and assume

    H2(r)=H4(r)=...=H_(e-2)(r)=0.                 (L_m)

The even Taylor polynomial has the exact form

    [f(r+T)+f(r-T)]/2=T^e W_m(T^2),
    W_m(Z)=h_e+h_(e+2)Z+...+Z^(10-m).

Every nonleading even h_k is divisible by19; h20=1. The accepted
Euler identity, valid at arbitrary nu, gives

    delta=0: W_m(r^2)=0;
    delta!=0: v(W_m(r^2))>=(2m-1)nu+1;
    v(D_j(r))>=2nu, v(a_j)>=nu.                 (E)

For clarity, its exact mechanism is f=(X-s)^2 U with
U=X^2(X-r)(X-1)g and eta=U'(2r)/U(2r)=2/r+an integral element.
The identity

    2r^(e+1)W_m'(r^2)
      =-delta U(2r)[1+delta(m/r-eta/2)]

has a unit bracket when delta!=0. With v(U(2r))=3nu+1 and
v(W_m'(r^2))>=1 it gives v(delta)>=(2m-2)nu, and then the value
bound(E). At exact delta0 the separate zero identity is used, with no
division by delta. This is accepted earlier work, not a new R7 lemma.

## 1. R7A: a quadratic coefficient of depth below nu suffices

Suppose(L_m) and

    u=a_(j-2)!=0, tau=v(u), 0<=tau<nu.            (Qw)

**R7A.** Then v(H_e(r))=2nu+tau+1 exactly. At least one of H_e,H_(e+1)
has full monic gcd X-1 with f and a NONZERO normalized constant whose
valuation is at least nu. If H_e has any ACTUAL rational noncenter
common root, the adjacent H_(e+1) has that essential center and

    v(a_(j-1))=nu+tau.                            (A)

Thus tau0 recovers the earlier unit case, but positive tau below nu is
also covered. Nothing is assumed about the valuations of later unit
coefficients, and no upper bound on nu or on v(delta) is needed.

### The first nonzero even value

D_(j-2)(r)=u+O(r), with integral coefficients. Since tau<nu, its
valuation is exactly tau and D_(j-2)(r)/u=1 mod19. Consequently

    v(h_(e+2))=tau+1.

The term h_(e+2)r^2 in W_m(r^2) has valuation2nu+tau+1. Every later
nonleading term has valuation at least4nu+1, and the leading term
has valuation j*nu>=6nu. These are STRICTLY higher because
tau<=nu-1. The value W_m(r^2) itself is zero or has valuation at
least5nu+1 by(E). Cancellation therefore forces

    v(h_e)=2nu+tau+1,
    D_j(r)/(u r^2)=-c mod19,
    c=beta_(j-2)/beta_j
      =j(j-1)/[(e+1)(e+2)] in F19^*.              (1)

The exact rational binomial ratio is taken before reduction. In
particular H_e(r) is nonzero. The comparison is of whole weighted
terms; it does not require u to be a unit before scaling.

### Actual noncenter roots and integral scaled coefficients

If H_e has no rational noncenter common root, the full contest
hypothesis supplies1. By(E), v(a_j)>=nu, and a_j cannot be zero
because then0 would be a common root. This gives the first conclusion.

Otherwise an ACTUAL rational common root w is0 or s: it is not r
by(1), and no other root is eligible. In either case v(r-w)=nu.
Expand

    D_j(X)=a_j+j a_(j-1)X+b u X^2+sum_(ell>=3)c_ell X^ell,
    b=j(j-1)/2, c_ell in Z_(19).

The difference quotient at r,w has valuation nu+tau. Its right side is

    j a_(j-1)+b u(r+w)+terms of valuation>=2nu.

The second term has valuation at least nu+tau, and2nu>nu+tau.
A smaller valuation for a_(j-1) would be uniquely minimal, impossible.
Thus v(a_(j-1))>=nu+tau. Evaluating D_j(w)=0 now gives
v(a_j)>=2nu+tau; at w0 one has a_j=0 exactly. This justifies the
integral residues

    ellbar=a_(j-1)/(u r) mod19,
    C=a_j/(u r^2) mod19.

Every term of degree at least3 disappears after X=r*z and division
by u*r^2, since its remaining valuation is at least nu-tau>0.
The reduced polynomial is therefore

    Q(z)=C+j ellbar*z+b z^2,
    Q(1)=-c,
    Q(0)=0 if w0, or Q(2)=0 if ws.                (2)

Solving these two equations gives j ellbar=-b-c for w0 and
j ellbar=c-3b for ws. No rational equality s=2r is imposed.

If H_(e+1) also had an actual rational noncenter witness zeta,
then zeta/r reduces to y in{0,1,2}. In its normalized polynomial
D_(j-1), division by u*r is integral by the bound just proved;
all terms of degree at least2 disappear because2nu>nu+tau.
The equation is

    ellbar+(j-1)y=0.

Combining it with(2) forces

    w0: y=rho_m=1/2+1/[(2m+1)(2m+2)];
    ws: y=2-rho_m.                               (3)

The set{0,1,2} is invariant under y->2-y. For rho_m to belong to
it, the product(2m+1)(2m+2) would have to be17,2 or7 modulo19.
The complete five-case hand check is

| m | product | residue mod19 |
|---|---|---|
|3|7*8=56|18|
|4|9*10=90|14|
|5|11*12=132|18|
|6|13*14=182|11|
|7|15*16=240|12|

None is permitted. Thus H_(e+1) has no rational noncenter common
root and must have sole center1. Moreover rho_m and2-rho_m are
both nonzero. The equations for ellbar make it nonzero, proving
the exact finite valuation(A). G1 and simplicity of1 give the
full gcd X-1. This proves proposed R7A.

## 2. R7B: the first break has a weighted triple alternative

By accepted R5D let m0 be the first m in{3,...,7} with H_(2m)(r)!=0.
Put e=2m0 and j=20-e. The preceding(L_m0) holds.

**R7B.** At this FIRST break at least one of the following holds:

1. Some k in{e,e+1} has monic gcd(f,H_k)=X-1 and
   nu<=v(a_(20-k))<infinity.
2. The three successive normalized coefficients satisfy

       v(a_(j-2))>=nu,
       v(a_(j-1))>=2nu,
       v(a_j)>=3nu.                              (T_j)

These alternatives may overlap. Infinity is allowed in(T_j), so it
does not assert that any of its coefficients is nonzero.

Proof. If H_e has no rational noncenter common root, alternative1
follows from(E), with nonzero a_j. Otherwise choose an actual w.
The first-break condition excludes r, so w is0 or s. If
v(a_(j-2))<nu, R7A gives alternative1. We are left with
v(a_(j-2))>=nu, including a_(j-2)=0.

Then D_(j-2)(r)=a_(j-2)+O(r) has valuation at least nu.
In W_m(r^2), the next even term has valuation at least3nu+1;
later nonleading terms have valuation at least4nu+1 and the
leading term has valuation at least6nu>=3nu+1. Its value(E) has
still higher valuation or is zero. Hence

    v(h_e)>=3nu+1, v(D_j(r))>=3nu.

The quotient[D_j(r)-D_j(w)]/(r-w) has valuation at least2nu.
Its quadratic contribution b*a_(j-2)*(r+w) and every term of
degree at least3 have valuation at least2nu. Since j is a unit,
its linear coefficient must satisfy v(a_(j-1))>=2nu. Finally
D_j(w)=0 gives v(a_j)>=3nu: every term after the constant has
that valuation or higher. If w0, the constant is exactly zero.
This is(T_j), proving the proposed fork.

This sharpens R6B's two merely NONUNIT coefficients. At nu1 it
adds a depth-two requirement for a_(j-1) and depth-three requirement
for a_j. It does not exclude deep nonunits or essential centers.
It does not turn a lower bound on delta into an upper bound.

## 3. R7C: a weaker paired valuation hypothesis forces a nonunit center

Retain(S), the actual double s and the full rational-witness condition.
Assume for EACH odd o in{13,11,9,7,5} that

    v(a_o)<2nu OR v(a_(o-1))<nu.                 (P_w)

**R7C.** Some H_k,6<=k<=15, has full monic gcd X-1 and
nu<=v(a_(20-k))<infinity.

Indeed the first break chooses exactly one of those five pairs.
Hypothesis(P_w) contradicts its(T_j) alternative, so R7B gives
the essential center with nonzero nonunit constant.

Every old R6C paired OR-unit condition implies(P_w), but(P_w)
also allows some pairs with both coefficients nonunit. For example
at nu1 an odd coefficient of valuation1 is below2nu. This describes
the logical weakness of the new hypothesis, not an actual constructed
rational polynomial satisfying all the other hypotheses. Nothing here
proves(P_w) for every surviving rational lift.

## 4. R7D: exchanging the two rational double-root origins

Define the exact rational affine change fixing the center:

    F(Y)=(1-s)^(-20) f(s+(1-s)Y),
    r'=(r-s)/(1-s), s'=-s/(1-s).

The denominator is a19-unit since v(s)>0. The old double root s
becomes0; the old double0 becomes s'; the simple r and1 become
r' and1. Both r',s' have valuation nu, their ratio reduces to2,
and

    s'-2r'=delta/(1-s).

Hasse derivatives transform by the exact nonzero scalar
(1-s)^(k-20), so the same sole-H3 conditions, preceding even ladder
and first-break index hold. The fractional roots keep valuation1/14,
since subtracting s of larger valuation cannot change theirs.

Write the normalized coefficients of F as a'_j. The EXACT transport is

    a'_j=(1-s)^(-j) D_j(s), 0<=j<=18.            (4)

In particular a'_0=1,a'_1=-1 and a'_j=a_j mod19 for every j.
The unit mask and J15 are unchanged. Applying the analogous change
to F at its other double root s' returns f: its translation is zero
and its total scaling is one. Thus this is an involution of the
two choices of double-root origin, not a new symmetry f is assumed
to possess.

**R7D.** For the chosen first-break j, the deep condition(T_j) is
invariant under this involution. To prove one direction expand(4):

    (1-s)^j a'_j
      =a_j+j a_(j-1)s+binom(j,2)a_(j-2)s^2+O(s^3),
    (1-s)^(j-1) a'_(j-1)
      =a_(j-1)+(j-1)a_(j-2)s+O(s^2),
    (1-s)^(j-2) a'_(j-2)=a_(j-2)+O(s).

All omitted coefficients are integral. Under(T_j) the respective
right sides have valuations at least3nu,2nu,nu. Division by the
units preserves these bounds. The involution proves the reverse
implication. Thus applying R7B in both rational frames does not
by itself contradict its remaining weighted alternative.

### The exact minimal-cover consequence, retained as old mechanism

T1 excludes EVERY three-value rational cover, not just a polynomial
with only three rational roots. Here the available set is exactly
{0,1,r,s}. If a value were never the sole common-root value of a
derivative, the other three could cover all orders. Thus each is
essential somewhere. Low supports are

    H1:{0,s}, H2:{r}, H3:{1}, H4:{r}, H5:{1}, H19:{1}.

Therefore0 and s are sole common-root VALUES at two DIFFERENT
orders in6,...,18. In particular there are different indices
j0,js in2,...,14 such that

    a_(j0)=0, D_(j0)(s)!=0;
    D_(js)(s)=0, a_(js)!=0.                      (5)

At either index the derivative's values at r and1 are nonzero as
well. Essential0/s gcd multiplicities are not asserted to be one.
Under the old long ladder the eight-order refinement was already
proved as accepted RC3. Equation(5), without that ladder, is the
same elementary cover mechanism in a larger eligible set and is
not claimed as new progress. Formula(4) exchanges the two coefficient
gap sets. It does not force their gaps to occur at the same index.
Neither(5) nor this coordinate change produces a missing unit in
(T_j), a full rational compatibility contradiction or an actual lift.

## 5. Boundary diagnostic: a cubic initial jet survives

The STRICT tau<nu in R7A is essential to that proof: at tau=nu,
cubic terms need not disappear after quadratic scaling. The following
HAND identity demonstrates a consistent leading jet, not a rational
polynomial or a full local lift.

Take m3,j14 and a unit cubic coefficient a11. Formally scale D14
by a11*r^3, and take residues

    a12/(a11*r)=-1, a13/(a11*r^2)=0,
    a14/(a11*r^3)=0.

The resulting cubic is

    Q(z)=-binom(14,2)z^2+binom(14,3)z^3
        =4z^2+3z^3 over F19.

It has Q(0)=Q'(0)=0 but Q(1)=7!=0. Thus the broken even
equation and adjacent derivative may both use the noncenter0 at
this leading level. The necessary leading even-Taylor cancellation
also holds:

    H2(Q)(1)=4+9=13,
    7+[2/(7*8)]*13=7+17*13=228=0 mod19.          (6)

Here binom(14,2)=91=15, binom(14,3)=364=3 and7*8=18 mod19.
The factor2/(7*8) is the exact ratio from the even Taylor coefficients
after expressing the next term through H2(Q)(1). This does not
certify higher digits, all Euler equations, other derivative witnesses,
an actual double-root polynomial or ordinary rational lifting. It only
blocks extending the SAME quadratic truncation beyond its strict
valuation threshold. R7A–R7D do not rely on this diagnostic for proof.

## 6. Explicit remaining work and provenance

R7 strengthens a local necessary fork and weakens one conditional
essential-center hypothesis. It does NOT exclude either a nonunit
essential center or the deep triple(T_j). The coordinate involution
shows why re-normalizing at the other rational double root leaves
that alternative intact. The minimal-four-root lead alone does not
settle the resulting exact higher coefficient gaps.

No assertion is made that a satisfying leading jet lifts to Q19 or Q,
that every Q19 root is a contest witness, or that all roots are rational.
The global carrier and the degree-six rational residual factor do not
inherit a Casas-Alvero property as their OWN derivatives. CLO's
all-root/unramified theorem therefore remains inapplicable. The2011
prime5 erratum is unchanged; no two-prime shortcut is used. The degree19
critical-value polynomial in old TA2 is still not proved Casas-Alvero.

The accepted R5 minimum selected valuation bound nu<=10 in this equal
valuation branch, retained in R6, is context, not used to truncate the new
proof or bound collision depth. Distinct2R slots, other low-center
patterns, multiplicity3, lower J, remaining masks and all of degree20
remain unresolved. No larger mask search or routine valuation table
was substituted for these inferences.

Published normalization and the support/descent mechanism are attributed
in the source packet. The present constructor authored the OLD seven
return-r3 bodies and R6 and earlier reviewed J15, PN and R5. Their
separately accepted status is not an independent review of NEW R7.
Root suggested examining essential-root coverage; that elementary
mechanism was found already in accepted RC3. Root did not supply the
new weighted comparison or triple bounds. Two other fresh whole audits
are still required; no reviewer eligibility or acceptance is presumed.

The full candidate, explicit failures, source checks, log, obligations
and administrative hash records freeze before any reassignment. No
mathematical program, CAS, enumeration, author rerun, paid API, contact,
access bypass, spawning, shared edit or worker Git action was used.
