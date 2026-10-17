# The last even first break is incompatible with the three actual center equations

2026-10-17 UTC. **Candidate proof - unverified.** Constructor:
`/root/review_2021_reasoning_j15_r2`. Requested gpt-6.1-sol/max;
independently verified effective settings unavailable. TWO OTHER fresh,
initially blind WHOLE nonconstructor audits and coordinator reconciliation
are required. Only2021 B4(b) is considered. No full J15, degree20,
annual classification, rational counterexample or novelty is claimed.

The proposed new result removes an ACTUAL remaining first-break branch:
the even ladder at the simple small root cannot reach H12. This excludes
the entire m7 branch, including BOTH R10's t1/depth14 alternative and its
t>=2 alternative, without assuming any ordinary ordering of the roots.
The proof combines the exact accepted R8 fork with two short polynomial
incompatibilities over F19. It does not bound rational height, infer a
sign from a residue, enumerate masks or infer a lift from a finite test.
No mathematical executable, CAS, scan, old certificate or author rerun
was used. Every new arithmetic step is supplied below.

## 0. Official domain, exact branch and accepted inputs

The [official2021 Paper B, page2](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf)
requires f in Q[X] and an ACTUAL RATIONAL common root of f and each
derivative of orders1,...,d-1. The value can depend on the derivative.
The other roots need not be rational or real. The open target is(b),
the degree classification. No preliminary proof is investigated.

Use exactly the accepted normalized degree20/J15/multiplicity-two,
sole-H3 setting WITH an ADDITIONAL actual double small root s:

    f(X)=X^20-20X^19+sum_(j=2)^18 binom(20,j)a_j X^(20-j),
    a_j in Z_(19), a0=1,a1=-1, ord_0(f)=2,
    f(1)=0, J=max{j:v19(a_j)=0}=15,
    H3(f)(1)=0, H2(f)(1)!=0, H4(f)(1)!=0.            (S)

Here H_k=f^(k)/k!, v19(19)=1 and v19(0)=infinity. Every derivative
has its required ACTUAL rational common witness. The separately
accepted J15 dictionary gives

    f=X^2(X-r)(X-s)^2(X-1)g,
    r,s in Q, nu=v19(r)=v19(s)>=1, s/r=2 mod19,
    {rational roots of f}={0,1,r,s},
    H2(f)(r)=H4(f)(r)=0.                              (W)

All four values are distinct; r,1 are simple and0,s double. The
degree14 rational carrier g is Eisenstein at19. Its global exclusion
from derivative roots has its separate accepted proof. The new field
argument needs only the exact RATIONAL root set in(W); it does not
apply a CA theorem to the degree-six quotient or assume all roots real.
In particular an arbitrary Q19 root would not supply a contest witness.

Define over Q BEFORE reduction

    D_j(X)=H_(20-j)(f)(X)/binom(20,j)
          =sum_(ell=0)^j binom(j,ell)a_(j-ell)X^ell,
    beta_j=binom(20,j)/19, 2<=j<=18.                   (N)

For bookkeeping set a19=a20=0. These are monic integral normalized
derivatives, with D_j'=jD_(j-1).
All beta_j are19-units. At an actual small witness w in{0,r,s},

    D_j(w)=a_j mod19.

Consequently, if a_j is a unit, an actual rational common witness of
f,D_j can ONLY be1. More generally, with a bar denoting reduction,

    bar(a_j) * bar(D_j(1))=0.                         (R)

This is a necessary consequence of an actual witness, never a converse
lifting claim. For j15, J15 and(R) give D15(1)=0 ACTUALLY. Thus the
three equations used later are

    f(1)=0, D15(1)=0, D17(1)=0.                       (C)

The last is the stipulated H3 center; D15 is H5, not H15.

The precise accepted theorem inputs are these:

1. PN3, [reviewed-odd-support-exclusion-v1.1.md](../proofs/reviewed-odd-support-exclusion-v1.1.md):
   at least one of the EVEN coefficients a2,a4,...,a18 is a unit in
   this normalized rational-witness/J15/sole-H3/multiplicity-two setting.
   The accepted64-case proof is not rerun or independently recertified.
2. R5D, [reviewed-reasoning-return-r5-v1.1.md](../proofs/reviewed-reasoning-return-r5-v1.1.md):
   H6(r),H8(r),H10(r),H12(r),H14(r) cannot all vanish, under this
   ADDITIONAL actual double-s hypothesis and every actual witness.
3. R8B and its Euler estimate(E), [reviewed-reasoning-return-r8-v1.1.md](../proofs/reviewed-reasoning-return-r8-v1.1.md):
   if the first broken even equation is H14(r)!=0, then

       v19(D6(r))>=2nu, v19(a6)>=nu,                  (E)

   and at least one of the following holds:

   * EC: some H_k, k in{14,15,16}, has sole common value1 and a
     NONZERO NONUNIT normalized constant a_(20-k), with valuation>=nu;
   * T4: v19(a3)>=nu, v19(a4)>=2nu,
     v19(a5)>=3nu, v19(a6)>=4nu.

   There is NO cubic alternative at m7. These statements allow arbitrary
   nu>=1, zero coefficients in T4, exact s=2r and arbitrary finite
   displacement. The nonzero/nonunit qualifications in EC are retained.
4. For the final corollary only, accepted TA1 in the exact frozen
   [transfer body](reasoning-return-r3-transfer-candidate-v1.md), accepted
   by [reviewed-return-r3-v1.1.md](../proofs/reviewed-return-r3-v1.1.md):
   under the preceding even ladder, a_(19-2m) a unit transfers ANY
   actual rational noncenter H_(2m) witness to the actual r, for3<=m<=8.

The COMPLETE R10 accepted body and failed routes were read first, as
assigned. The proof below does not import its ordinary endpoint geometry,
the odd-run theorem, a bound on nu or a bound on delta=s-2r. The complete
R5, R8, PN and TA1 accepted bodies/scopes were also read. Older authorship
of TA1/R6/R7/R8/R10 and older J15/PN/R5 audits is disclosed; none supplies
an independent review of this NEW submission. The coordinator assigned
the research question and supplied NO new R11 mathematical inference.

## Proposed claims

**R11A, two residual incompatibilities.** In(S),(W), suppose

    a6,a8,a10,a12,a14,a16,a18 are nonunits.             (P)

Neither of these two tuples of residues is possible:

    (bar a2,bar a3,bar a4,bar a5)=(1,0,0,0),
    (bar a2,bar a3,bar a4,bar a5)=(1,0,-3,9).          (I),(II)

The proof uses(C), J15, and the actual common witnesses of H13,H11,H9.
It allows all five remaining odd residues to vanish during the field
calculation; their possible vanishing is not discarded by division.

**R11B, complete exclusion of the m7 first break.** In(S),(W),

    NOT[H6(r)=H8(r)=H10(r)=H12(r)=0].                  (B)

Equivalently the first break has m in{3,4,5,6}, rather than{3,...,7}.
This is an actual branch exclusion, with no ordinary endpoint, selected
word, coefficient-unit, valuation-upper-bound or sign assumption added.

**R11C, four-unit essential-center consequence.** In the same domain,
if a7,a9,a11,a13 are all units, then at least one of H6,H8,H10,H12 has
1 as its SOLE rational common-root value, and its full monic gcd with f
is X-1 by the separately accepted global carrier exclusion. There is
no assumption on a3 or a5. This is the direct TA1 consequence of(B),
not an assertion that the four units always occur.

## 1. A common field reduction and the divided original center equation

Until Section5 work in F19 and write

    A=bar a2, B=bar a3, C=bar a4, E=bar a5,
    x=bar a7, y=bar a9, z=bar a11,
    w=bar a13, u=bar a15.

Under(P), J15 also gives bar a17=0. Constant/linear terms of f vanish
exactly by ord_0 f2. Thus the ONLY possibly nonzero normalized residues
are indices0,1,2,3,4,5,7,9,11,13,15. Do not confuse coefficient index
j with derivative order20-j.

For2<=j<=18, direct rational cancellation BEFORE reduction gives

    beta_j=(20/[j(j-1)]) binom(18,j-2)
           =(-1)^j/[j(j-1)] mod19.                  (1)

Every displayed denominator is a19-unit. The original center equation
must first be divided by19:

    f(1)=-19+19 sum beta_j a_j=0,
    sum beta_j a_j=1 in Z_(19).                      (2)

Reduction of f(1) without this division would give only0=0. Its odd
coefficients in(1), moved to the other side, give

    5x+14y+14z+5w+u=L,
    L=-1+10A+3B+8C-E.                               (3)

For example, the inverses of j(j-1) at j7,9,11,13,15 are5,14,14,5,1.
The even terms beta2=10,beta4=8 and odd beta3=3,beta5=-1 fix the signs.

The two actual derivative center equations in(C) give

    13x+8y+16z+10w+u=R,
    R=-5-10A+B+3C-E;
    11x+9y+7z+5w+3u=S,
    S=-3-3A-15B-5C-13E.                              (4)

For a complete hand certificate of the binomials, rows j15 and j17
at columns7,9,11,13,15 reduce respectively to

    (6435,5005,1365,105,1) mod19=(13,8,16,10,1),
    (19448,24310,12376,2380,136) mod19=(11,9,7,5,3).

Their constant parts before moving sides are

    5+10A-B-3C+E,
    3+3A+15B+5C+13E.

These also follow directly from a0=1,a1=-1. No a_j with larger index
is hidden in(3),(4): a16,a17,a18 reduce to zero and a19=a20=0 exactly.

Set K=R-L and N=S-3L. Subtracting(3) from the first of(4), and three
times(3) from the second, gives

    8x+13y+2z+5w=K,
    15x+5y+3z+9w=N.

Their combination2*(second)-3*(first) yields

    3w=2N-3K+13x+10y.

Consequently, with division by the NONZERO field scalars2,3,

    w=(7N-K)+17x+16y,
    z=(3K-8N)+x+y.                                 (5)

This is the entire global compatibility calculation. It uses the
ORIGINAL divided f-center equation and BOTH actual derivative center
equations, rather than an abstract residue polynomial with its own
CA property.

## 2. Actual witnesses impose three polynomial equations

For j7,9,11 the constant contributions of indices0,...,5 at1 are

    p=13+2A+16B+16C+2E,
    q=11+17A+8B+12C+12E,
    d=9+17A+13B+7C+6E.                              (6)

The remaining Pascal residues needed here are

    binom(9,7)=36=-2 mod19,
    binom(11,7)=330=7, binom(11,9)=55=-2 mod19.

Applying(R) to the ACTUAL H13,H11,H9 common witnesses gives

    x(x+p)=0,
    y(y-2x+q)=0,
    z(z+7x-2y+d)=0.                                (7)

Zero x,y,z are explicitly allowed. A nonzero residue excludes every
small rational witness and forces the corresponding actual center
equation; that is the sole reason(7) holds. No center-availability
choice, ordinary ordering, essentialness or coefficient-mask inference
is being smuggled into this reduction.

## 3. Proof of R11A for prefix(I)

For(A,B,C,E)=(1,0,0,0), equations(3),(4) give

    (L,R,S)=(9,4,13), K=14,N=5,
    z=2+x+y, w=2-2x-3y.

Also(p,q,d)=(15,9,7). Thus(7) becomes

    x(x-4)=0,
    y(y-2x+9)=0,
    (x+y+2)(9+8x-y)=0.                              (8)

Expanding the last product gives

    8x^2+7xy+25x+7y+18-y^2.

Substitute x^2=4x and y^2=(2x-9)y from the first two equations.
The expression becomes

    (5x-3)y-1.                                     (9)

If(8) held, (9)=0 would give y!=0. The second of(8) then gives
y=2x-9, so

    1=(5x-3)(2x-9)=10x^2-51x+27=8x+8.

Hence x=11, since8^(-1)=12 in F19. But

    x^2-4x=121-44=77=1 mod19,

contrary to the first of(8). This proves impossibility(I). It is a
polynomial contradiction covering all residues at once, not a table
of selected masks or an extrapolation from tests.

## 4. Proof of R11A for prefix(II)

For(A,B,C,E)=(1,0,-3,9), equations(3),(4) instead give

    (L,R,S)=(14,5,6), K=10,N=2,
    z=14+x+y, w=4-2x-3y.

Here(p,q,d)=(4,5,2), and(7) becomes

    x(x+4)=0,
    y(y-2x+5)=0,
    (x+y+14)(16+8x-y)=0.                            (10)

The last product expands to

    8x^2+7xy+128x+2y+224-y^2.

Substitution of x^2=-4x and y^2=(2x-5)y reduces it to

    x+(5x+7)y+15.                                  (11)

If y=0, equation(11)=0 would force x=4, contradicting x(x+4)=0
since4*8=13 mod19. Thus y!=0. The second of(10) gives y=2x-5,
and substitution in(11), using x^2=-4x, gives

    0=10x^2-10x-20=7x-1.

Hence x=11. This contradicts

    x^2+4x=121+44=165=13 mod19.

Thus(II) is impossible. No division by x,z,w,u, a potentially zero
coefficient, or a root displacement has occurred.

## 5. The last-break prefix, including every EC possibility

Assume, toward proving R11B, that H6(r)=H8(r)=H10(r)=H12(r)=0.
Together with H2(r)=H4(r)=0, R5D forces H14(r)!=0. Thus the first
break is exactly m7 and the precise accepted R8 m7 fork applies.

For j8,10,12,14,16,18 the ACTUAL equations D_j(r)=0 and v19(r)>=nu
give v19(a_j)>=nu by the integral expansion in(N). Estimate(E) gives
the same for a6. Hence(P) holds. PN3 now says

    A!=0 OR C!=0.                                  (12)

The actual common witnesses of H18,H17,H16,H15, via(R), give

    A(A-1)=0,
    B(B-2+3A)=0,
    C(C-3+6A+4B)=0,
    E(E-4+10A+10B+5C)=0.                            (13)

In particular A is0 or1; B is0 or2-3A. Thus the only(A,B) pairs
are(0,0),(0,2),(1,0),(1,-1). This four-pair identity is derived from
the first two actual witness equations, not supplied by a mask search.
All statements in the rest of this section are in F19.

### 5.1 The T4 side is impossible

T4 gives B=C=E=0. By(12), A!=0; by(13), A=1. This is precisely
prefix(I), contrary to R11A. All arbitrary deeper coefficient depths,
including infinity, are covered by this single reduction.

### 5.2 An EC at H16 is impossible

Its nonunit constant gives C=0, and its actual center equation gives

    -3+6A+4B=0.

For A0 and B0/2 the value6A+4B is0/8; for A1 and B0/-1 it is6/2.
None is3. Therefore no such H16 EC is possible.

### 5.3 An EC at H15 is impossible

Its nonunit constant gives E=0, and its center equation gives

    -4+10A+10B+5C=0.                               (14)

If C=0, this requires A+B=8. But A+B belongs to{0,1,2} from(13).
If C!=0, (13) gives C=3-6A-4B; substitution in(14) requires
2A+B=3. Again2A+B belongs to{0,1,2}. Both cases are impossible.
The nonzero/nonunit EC constant was not replaced by a unit-center
statement; its zero residue is used exactly as required.

### 5.4 An EC at H14 forces precisely prefix(II)

Here a6 already has zero residue by(P). Its actual center equation is

    -5+15A+B+15C+6E=0.                             (15)

First E cannot be zero. If E=C=0, equation(15) requires15A+B=5,
whereas the four pairs in(13) give0,2,15,14. If E=0,C!=0, then
C=3-6A-4B and(15) reduces to A-2B=17; its four possible values
are0,-4,1,3. None is17 in F19.

Thus E!=0, and(13) gives

    E=4-10A-10B-5C.

Substitution into(15) reduces it to

    6A-B+2C=0.                                    (16)

If C=0, (12) forces A=1. Equation(16) would then require B=6,
but(13) permits only0 or-1. Hence C!=0. Now substitute
C=3-6A-4B into(16); the result is

    2A+3B=2.

If A0, the possible left sides are0 or6. If A1, they are2 or-1,
so only A1,B0 remains. It gives C=-3 and E=9. This is exactly
prefix(II), already excluded by R11A.

Every alternative of the accepted m7 fork has now been contradicted.
This proves R11B. The field reasoning never divides by a6, a root,
delta, nu or a normalized constant. In particular it covers delta0,
all finite displacement depths, every integer nu>=1, zero coefficients,
both double-origin frames and every ordinary ordering of0,1,r,s.

## 6. Consequences and exact remaining scope

For R11C assume a7,a9,a11,a13 are units. If every one of H6,H8,H10,H12
had an actual rational noncenter common root, apply accepted TA1 at
m3,4,5,6. Its respective unit coefficients are a13,a11,a9,a7. Starting
from H2(r)=H4(r)=0, it successively forces the four actual equations
excluded by R11B. Thus at least one of those even derivatives has NO
rational noncenter common root. Its required common value is1.
The accepted global carrier exclusion and simple1 then give full
monic gcd X-1. This proves R11C with no assumption on a3 or a5.

R10's complete domain includes the m7 ladder. R11B therefore excludes
that ENTIRE actual domain, for t1, t>=2 and every permitted local depth.
No sign/height contradiction with P(r/19) is alleged: the congruences
themselves still admit negative integer representatives. What fails is
simultaneous compatibility with the actual THREE center equations and
the remaining actual witnesses. The old R10 statements and failed-route
bytes are preserved; their necessary-condition conclusions are not
silently rewritten as if their historical proofs had this new step.

This does NOT exclude earlier first breaks m3,m4,m5,m6, whose nonunit
center, four-depth or cubic alternatives have different coefficient
indices. Nor does it cover distinct2R slots, different low centers,
multiplicity3, lower J, every degree20 branch or the annual degree
classification. The four-unit premise in R11C is not proved automatic.
No arbitrary-Q factor, ramified carrier or all-roots-real theorem closes
the missing cases. No maximum valuation, rational height bound, rational
or local lift, counterexample, external validation or novelty is claimed.

The general normalized-center reduction and beta formula are attributed
to CLO Sections3.4--3.5, rather than claimed as a new method. The new
contribution proposed here is the explicit pair of polynomial field
contradictions and their combination with the exact accepted m7 fork.
Primary read limits, abandoned routes, all obligations and immutable
input/output records accompany this complete constructor checkpoint.
