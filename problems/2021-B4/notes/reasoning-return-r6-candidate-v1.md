# A quadratic jet forces an earlier nonunit essential center

2026-10-17 UTC. **Candidate proof - unverified.** Constructor:
`review_2021_reasoning_j15_r2`; requested `gpt-6.1-sol` / `max`, verified
effective-setting readback unavailable. Two OTHER fresh initially blind
nonconstructor whole audits are required. Only 2021 B4(b) is researched.
The official degree classification and degree20 remain unresolved.
No full J15 or repeated-root exclusion, rational lift, counterexample,
larger mask search, priority or novelty is claimed.

The new proposed inference is a quadratic normalized-derivative
obstruction, R6A. With a preceding even ladder and a unit next even
coefficient, two adjacent derivative orders cannot both have rational
noncenter common roots. The resulting essential center has a NONUNIT
normalized constant. R6B gives a coefficient-free fork at the first
broken even equation. R6C replaces R5E's five odd units by five paired
OR conditions, at the cost of allowing an adjacent odd order in the
conclusion. Its nonunit-constant conclusion is essential: merely obtaining
some center from a unit coefficient would give no new restriction.

## 0. Exact setting and accepted inputs

The [official problem](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf),
page2, requires rational coefficients and an ACTUAL RATIONAL common root
with every nonconstant derivative. The other polynomial roots need not
be rational or real. No preliminary part(a) argument is investigated.

Use the separately accepted rational affine normalization and J15,
multiplicity-two, sole-H3 setting:

    f(X)=X^20-20 X^19
           +sum_(j=2)^18 binom(20,j) a_j X^(20-j),
    a_j in Z_(19), a0=1, a1=-1,
    f(0)=f'(0)=f(1)=0,
    J=max{j:v_19(a_j)=0}=15, ord_0(f)=2,
    H3(f)(1)=0, H2(f)(1)!=0, H4(f)(1)!=0.           (S)

Here H_k=f^(k)/k! over Q and v=v_19, with v(19)=1 and v(0)=infinity.
Throughout, f satisfies ALL official rational-witness conditions.

Accepted D1/D3 give a simple rational root r, with nu=v(r)>=1,
sharing H2 and H4. The other two nonzero small slots have the same
valuation nu and reduce to twice the residue of r. This packet makes
the ADDITIONAL hypothesis that these two slots ACTUALLY COINCIDE at
a double root s. Equality of residues alone does not imply this.

Accepted T1 requires four distinct rational witness values. The fourteen
fractional-valuation slots cannot be rational. If s were not rational,
only 0,1,r would be rational roots, contradicting T1. Thus s is rational,
the rational root set is exactly {0,1,r,s}, and

    f=X^2(X-r)(X-s)^2 B(X), B=(X-1)g,
    nu=v(r)=v(s)>=1, s/r=2 mod19, delta=s-2r.

The actual rational division makes g a polynomial in Q[X]. Its degree
is14 and its local coefficients are Eisenstein at19. In particular B
has constant valuation1, coefficients of X through X^13 divisible19,
coefficient of X^14 congruent to -1, and leading coefficient1.
If delta!=0, Delta=v(delta)>nu. The exact case delta=0 is allowed.

Define the MONIC normalized derivative before reduction:

    D_j(X)=H_(20-j)(f)(X)/binom(20,j)
          =sum_(k=0)^j binom(j,k)a_k X^(j-k),
    beta_j=binom(20,j)/19, 2<=j<=18.               (N)

Every beta_j is a 19-adic unit. A coefficient a_j is called a unit
exactly when v(a_j)=0; nonunit includes zero. A derivative has an
essential center here if its sole rational common-root VALUE with f
is1, even if other derivatives use1 too.

The accepted project inputs are used only in these exact scopes:

1. Normalization, Newton/T1, and J15 D1/D3, as above. The published
   normalization is attributed to Castryck--Laterveer--Ounaies (CLO),
   Section3.4 and Lemma17; the project separately checks rationality of
   the affine change. No all-roots-rational theorem is imported.
2. Accepted TA1: for 3<=m<=8, if H2,H4,...,H_(2m-2) vanish at r,
   a_(19-2m) is a unit, and H_(2m) has an actual rational noncenter
   common root, that root must be the actual r. In particular H_(2m)(r)=0.
3. Accepted R5D: in the full setting(S) with this actual double s,
   the five equations H6(r)=H8(r)=H10(r)=H12(r)=H14(r)=0 cannot all hold.
   Its accepted proof combines EXACT RC2 and PN4; these old finite
   certificates are not rerun or independently recertified here.
4. Accepted G1, also supplied by R5C in this setting: the degree14
   rational carrier shares NO root with ANY derivative. Thus every
   derivative common root belongs to {0,1,r,s}, also over an algebraic
   closure. Since1 is simple, an essential center has monic gcd X-1.

The complete accepted R5 body was read, including its descent constant,
minimum witness valuation <=10, global carrier and the exact R5D/E
scopes. The bound10 is not a bound on Delta or on every witness depth.
The new local proof below needs no upper bound on nu or Delta.

The constructor authored the seven OLD accepted return-r3 bodies and
previously reviewed J15, PN and R5. Their acceptance by OTHER reviewers
is recorded separately. This construction does not count those earlier
roles as either of the required fresh reviews of R6.

## 1. Reconstructed accepted Euler estimate

This subsection reproduces the valuation estimate underlying accepted
TA1/RC1; it is an input mechanism, not a newly claimed theorem.

For 3<=m<=8 suppose

    H2(r)=H4(r)=...=H_(2m-2)(r)=0.                 (L_m)

Put h_e=H_e(f)(r), and set

    E(T)=[f(r+T)+f(r-T)]/2=T^(2m) A_m(T^2),
    A_m(Z)=h_(2m)+h_(2m+2)Z+...+Z^(10-m).          (1)

The constant Taylor term is zero because f(r)=0. Every even h_e with
e<=18 belongs to19 Z_19 by(N), while h20=1. Put

    U=X^2(X-r)B, f=(X-s)^2 U,
    U(2r)=4r^3 B(2r), v(U(2r))=3nu+1,
    eta=U'(2r)/U(2r)=2/r+B'(2r)/B(2r).            (2)

The last logarithmic-derivative term is integral. Indeed v(B(2r))=1
and B'(2r) is divisible19, including the high-degree terms. In
particular U(2r) is nonzero and every division in(2) is legitimate.
Using f(0)=f'(0)=0 and the double-root factor gives EXACTLY

    E(r)=delta^2 U(2r)/2,
    E'(r)=delta^2 U'(2r)/2-delta U(2r),
    2r^(2m+1) A_m'(r^2)
       =-delta U(2r)[1+delta(m/r-eta/2)].           (3)

If delta!=0, the bracket is a unit, since Delta>nu. Also A_m has
degree10-m>=2, and A_m'(r^2) is divisible19: every nonleading
differentiated coefficient has that factor, and the leading term
contains r^2. Thus finite delta implies A_m'(r^2)!=0 and

    Delta=(2m-2)nu-1+v(A_m'(r^2)) >=(2m-2)nu,
    v(A_m(r^2))=2Delta+(3-2m)nu+1
                      >=(2m-1)nu+1.              (4)

If delta=0, equation(3)'s first equality instead gives A_m(r^2)=0
exactly. No division by delta is used in that case.

Every nonconstant nonleading term of A_m(r^2) has valuation at least
2nu+1; its leading term has valuation2(10-m)nu>=4nu>=2nu+1.
Subtracting these terms, and using(4) or A_m(r^2)=0, gives

    v(h_(2m))>=2nu+1,
    v(D_(20-2m)(r))>=2nu,
    v(a_(20-2m))>=nu.                            (5)

For the last inequality expand D_j(r)=a_j+j a_(j-1)r+O(r^2), with
integral coefficients. Both terms on the right after a_j have
valuation at least nu. In particular the normalized constant for
the current even order is nonunit, even before imposing a quadratic
unit hypothesis.

## 2. R6A: a unit quadratic coefficient obstructs adjacent witnesses

Let 3<=m<=7, set e=2m and j=20-e, assume(L_m), and suppose

    u=a_(j-2)=a_(18-2m) is a unit.                (Q_m)

**R6A.** Then v(H_e(r))=2nu+1 exactly. At least one of H_e,H_(e+1)
has1 as its sole common-root value with f, with a NONZERO NONUNIT
normalized constant a_(20-k) satisfying v(a_(20-k))>=nu. Its monic
gcd with f is X-1, also over the algebraic closure.

More precisely, if H_e has any actual rational noncenter common root,
that root is0 or s; then H_(e+1) has sole common root1 and

    v(a_(j-1))=nu.                               (6)

### Exact leading even value

The next even Taylor coefficient satisfies

    h_(e+2)/19 = beta_(j-2) u mod19.

In A_m(r^2), every term after h_(e+2)r^2 has valuation STRICTLY greater
than2nu+1. For a later nonleading term this follows from4nu+1>2nu+1;
the top term has valuation j nu>=6nu>2nu+1 for m<=7. Equation(4)
or its exact-zero version is higher as well. Therefore

    v(h_e)=2nu+1,
    D_j(r)/(u r^2)=-c mod19,
    c=beta_(j-2)/beta_j
     =j(j-1)/[(2m+1)(2m+2)] in F_19^*.            (7)

In particular H_e(r)!=0. This is cancellation of the first two even
Taylor terms, not an assumption that either term alone is the minimum.
The binomial ratio in(7) is taken as an exact rational ratio before
reduction; all its displayed denominators are19-units.

### A scaled quadratic if the even order has a noncenter witness

If H_e has no rational noncenter common root, the full contest
hypothesis supplies1. Its normalized constant a_j has valuation
at least nu by(5), and cannot be zero, since a_j=0 would make0 a
common root. This already proves the required conclusion for k=e.

Otherwise choose an ACTUAL rational noncenter common root w of H_e.
By(7), w!=r. Thus w is0 or s, and v(r-w)=nu. Write

    D_j(X)=a_j+j a_(j-1)X+b u X^2
                      +sum_(ell>=3) c_ell X^ell,
    b=j(j-1)/2, c_ell in Z_19.                    (8)

The difference quotient [D_j(r)-D_j(w)]/(r-w) has valuation nu by(7).
Its right side from(8) is

    j a_(j-1)+b u(r+w)+terms of valuation>=2nu.

The second term has valuation at least nu. A value v(a_(j-1))<nu
would therefore be the unique smaller valuation, a contradiction.
Hence v(a_(j-1))>=nu. Using D_j(w)=0 in(8) also gives v(a_j)>=2nu;
when w=0 the equation gives a_j=0 exactly. Define integral residues

    ellbar=a_(j-1)/(u r) mod19,
    C=a_j/(u r^2) mod19.

After X=r z and division by u r^2, the reduced polynomial is

    Q(z)=C+j ellbar z+b z^2,
    Q(1)=-c,
    Q(0)=0 if w=0, or Q(2)=0 if w=s.              (9)

All higher terms disappear because their scaled valuations are at
least(ell-2)nu>0. The possibility w=s uses only s/r=2 mod19, not
s=2r. Solving the two scalar equations in(9) gives

    w=0: j ellbar=-b-c;
    w=s: j ellbar=c-3b.                           (10)

### The adjacent odd order cannot have a noncenter witness

Suppose H_(e+1) had an actual rational noncenter common root zeta.
It belongs to {0,r,s}, so y=zeta/r mod19 belongs to {0,1,2}.
Its monic normalized derivative is D_(j-1). Division by u r is
integral at zeta, by the just-proved bound on a_(j-1), and reduces to

    0=ellbar+(j-1)y.                             (11)

Combining(10),(11) gives

    w=0: y=rho_m=1/2+1/[(2m+1)(2m+2)];
    w=s: y=2-rho_m.                              (12)

The set{0,1,2} is stable under y -> 2-y. Thus either equation could
be compatible with a noncenter witness only if

    rho_m in{0,1,2}, equivalently
    (2m+1)(2m+2) in{-2,2,2/3}={17,2,7} mod19.     (13)

For ALL five possible m the exact products are

| m | (2m+1)(2m+2) | residue modulo19 |
|---|---|---|
| 3 | 7*8=56 | 18 |
| 4 | 9*10=90 | 14 |
| 5 | 11*12=132 | 18 |
| 6 | 13*14=182 | 11 |
| 7 | 15*16=240 | 12 |

None is17,2 or7. This five-product hand certificate proves the
contradiction. No pattern search or mathematical program is needed.
Consequently H_(e+1) has no rational noncenter common root. The
contest supplies1, its sole rational common-root value.

Moreover both rho_m and 2-rho_m are nonzero, because rho_m is neither
0 nor2. Equations(10) imply ellbar!=0, proving(6). The coefficient
for this essential odd center is a_(j-1), and has positive finite
valuation nu. In both cases G1 and simplicity of1 give the full
monic gcd X-1. This completes R6A.

There is also an AUTOMATIC essential center at order e+2 under(Q_m),
since its normalized constant u is a unit. R6A forces a DISTINCT earlier
essential center whose normalized constant is nonunit. It is this latter
assertion that is proposed as new progress.

## 3. R6B: a first-break fork without coefficient unit hypotheses

Accepted R5D supplies some first broken even equation: let m0 be the
smallest m in{3,4,5,6,7} such that H_(2m)(r)!=0. Put

    e=2m0, j=20-e.

Then(L_m0) holds and v(a_j)>=nu by(5).

**R6B.** At this FIRST break either a derivative H_k with
k in{e,e+1} has sole common root1 and a NONZERO normalized constant
with valuation at least nu, or BOTH

    a_(j-1), a_(j-2) are nonunits.                 (14)

The alternatives may overlap; no uniqueness is asserted.

Proof. If H_e has no rational noncenter common root, it has sole
common root1. By(5), a_j has valuation>=nu, and it is nonzero because
otherwise0 would be a common root. This is the first alternative.
Otherwise H_e has an actual rational noncenter common root. If
a_(j-1) were a unit, accepted TA1 would force H_e(r)=0, contrary to
the definition of the break. Hence a_(j-1) is nonunit. If a_(j-2) is
also nonunit, we have(14). If it is a unit, R6A forces H_(e+1) to
have sole common root1 and v(a_(j-1))=nu. This is again the first
alternative. The full-gcd refinement is inherited from G1. End proof.

This fork is unrestricted in the normalized coefficients of the stated
ACTUALLY repeated-root branch. It does not eliminate the double-nonunit
alternative, the essential-center alternative, or the whole branch.

## 4. R6C: five paired OR conditions force a nonunit essential center

Retain the full setting(S) and actual double s. Assume

    at least one coefficient in EACH pair is a unit:
    (a13,a12), (a11,a10), (a9,a8), (a7,a6), (a5,a4).       (P)

**R6C.** Some H_k with 6<=k<=15 has monic gcd(f,H_k)=X-1 and

    nu <= v(a_(20-k)) < infinity.                 (15)

Thus there is an essential center with a NONZERO NONUNIT normalized
constant among those ten orders.

Proof. Take the first break from R5D. Its pair(a_(j-1),a_(j-2)) is
one of the five pairs in(P), so the second alternative of R6B cannot
hold. The first gives exactly(15), with k=e or e+1. End proof.

Condition(P) is weaker than requiring all of a5,a7,a9,a11,a13 to be
units. The conclusion allows odd orders; R5E retains its stronger
EVEN-order conclusion under the old all-odd-unit hypothesis. R6C does
not claim that this weaker hypothesis implies R5E's even-only conclusion.
Unlike the automatic center implied by any individual unit constant,
the selected coefficient in(15) is nonunit. Nothing here proves(P)
for every surviving center pattern or rational lift.

## 5. Endpoints, failed shortcuts, and remaining work

The residue step has a real local endpoint. At m=8, j=4, the product
17*18 is2 modulo19. Formally c=4*3/2=6 and b=6, and the reduced
equations admit

    Q(z)=6z(z-2), ellbar=-3,
    ellbar+(j-1)y=3(y-1).

The even equation can use0 or2 while the adjacent odd equation uses1.
This is only a consistent pair of LOCAL residue equations, not a lifted
polynomial or a full contest witness cover. R5D already forbids the
full preceding ladder through H14 under the full contest hypotheses.
This example explains why the NEW residue calculation is not extended
past m7 by an unsupported uniform statement.

Two discarded shortcuts are recorded explicitly. First, merely concluding
that one of H6,...,H15 uses the center under(P) is immediate from some
unit constants and is not substantive. The proof keeps the nonunit
constant and exact essential-center conclusion in(15). Second, the
old Euler lower bound and the finite-displacement lower bound are
already accepted TA1/RC1 mechanisms; they are rederived for clarity
and not presented as new contributions.

No minimum-selected-witness bound is promoted to a maximum collision
depth bound. Exact delta=0 and arbitrary finite Delta>nu are both
covered. A Q_19 root is never selected merely because it exists;
every common witness used in the proof is an actual rational root.
The rational carrier g is obtained by actual rational division only
after s has been forced rational. Its residual factor is not claimed
to inherit the Casas--Alvero property. The critical-value polynomial
from the old transfer packet is still not shown Casas--Alvero.

CLO Proposition19 requires all roots rational (or its stated unramified
field condition), which fails for the fractional carrier here. The
2011 prime5 erratum and the accepted source-objection register remain
unchanged; neither a good-prime shortcut nor an unresolved universal
proof is used. Marashdeh's one-nonzero-recycled-root descent criterion
is attributed context, not a multi-root theorem for this four-rational
value setting. No novelty claim follows from the source inspection.

Remaining gaps are precise. The first-break fork still allows either
an essential center with nonunit constant or a pair of consecutive
normalized coefficients both nonunit. No contradiction for either
alternative, global rational compatibility theorem, or lift criterion
has been established. Distinct2R slots, other low-center patterns,
multiplicity3, lower J, all remaining masks and degree20 stay outside
the new conclusion. Higher initial forms may be a future direction,
but no larger routine scan is proposed in place of that missing proof.

All mathematical arguments and the five-product certificate are hand
reasoning. The companion executable checks only byte hashes, JSON and
preservation of earlier packets. The candidate and complete sources,
research log, obligations and integrity manifest freeze before review;
only the coordinator may promote after two other independent audits.
