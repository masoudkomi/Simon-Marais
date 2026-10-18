# R12: complete hand checks and adversarial reconstruction

18 October 2026 UTC. **Candidate proof - unverified.** These are the
constructor's self-checks, NOT an independent audit. Two OTHER entire
initially blind whole audits remain mandatory. No mathematical
executable, field scan, old certificate, CAS or author-program rerun
was used. Every numeric table in the main is an exact finite algebraic
certificate derived from the equations there, not empirical evidence.

## 1. Index, scalar and original-center checks

The coefficient index j corresponds to derivative order20-j:
indices6,7,8,9,11,13,15,17 mean H14,H13,H12,H11,H9,H7,H5,H3.
This was checked separately from the first-break notation e=2m,j=20-e.
At m6, j8 and the TA1 linear coefficient is a7, not a9 or a5.

The binomial factors for orders used are valuation1 at19; beta_j is
formed over Q before reduction. The original center is divided by19,
using f(1)=1-20+19 sum beta_j a_j. Its constant is-1 after division,
not0. The beta6 check is exact:

    binom(20,6)=38760, 38760/19=2040=7 mod19.

The low row constants for D15,D17 are
5+10A-B-3C+E+8V and3+3A+15B+5C+13E+7V.
For j15, binomial indices6,7,9,11,13,15 reduce to8,13,8,16,10,1;
for j17 they reduce to7,11,9,7,5,3. These were checked by direct
integer remainders of the displayed binomials. No denominator19 was
inverted in F19.

As a separate linear check of the NEW V contribution, changing V by1
changes(L,R,S) by(7,-8,-7). It changes K=R-L by4 and N=S-3L by10.
Hence it changes Z=3K-8N by3*4-8*10=-68=8, and W=7N-K by66=9.
This verifies the two coefficients that cannot be borrowed from R11's
V0 calculation.

## 2. Odd-row and root-set checks

The normalized witness products at indices7,9,11,13 retain EVERY low
contribution. In particular:

    binom(9,6)=84=8;
    binom(11,6)=462=6;
    binom(13,5)=1287=14;
    binom(13,6)=binom(13,7)=1716=6.

After z=Z+x+y, its product becomes

    (Z+x+y)(Z+8x+d11-y)=0.

Thus the y roots are exactly -Z-x or Z+8x+d11, irrespective of
whether z itself vanishes. The y product gives roots0 or2x-q9.
This independently checks the signs in both sets(7). No root is
assumed to be nonzero in forming the sets, and a double set entry is
retained as the same possible value.

## 3. The first certificate, in an alternative arithmetic form

For V=x=0 the main certificate can be reconstructed from the following
triples(Z,q9,d11). Each pair lists E0 first and E* second:

|A,B,C|E*|Triple at E0|Triple at E*|
|---|---:|---|---|
|0,0,3|8|12,9,11|6,10,2|
|0,2,14|9|16,5,0|14,18,16|
|1,0,0|13|2,9,7|16,13,9|
|1,0,16|9|16,11,5|14,5,2|
|1,-1,0|4|6,1,13|3,11,18|
|1,-1,1|18|14,13,1|10,1,14|

This is the same finite proof written as coefficients rather than root
sets; it is a self-check, not a second reviewer. For example, in row2
at E9, the values come from

    Z=7+15*2+8*14+4*9=185=14,
    q9=11+8*2+12*14+12*9=303=18,
    d11=9+13*2+7*14+6*9=187=16.

The required roots are then{0,1} and{5,11}, disjoint. Every other
entry is obtained by the same displayed linear expressions, with no
search or missing residue choice. For the last prefix at E18,
Z=10,q9=1,d11=14 give{0,18} versus{9,5}, also disjoint.

The two actual survivors of the middle equations were substituted in
the FINAL w product, rather than assumed impossible because of an
unsupported nonzero residue:

* A1,B0,C0,E13,x0,y6 gives Z16,W4,z3,w5,c13=1.
  D13(1)=5+72+6+1=84=8. Its w product is nonzero.
* A1,B-1,C0,E0,x0,y0 gives Z6,W16,z6,w16,c13=8.
  D13(1)=16+12+8=36=17. Its w product is nonzero.

All variable divisions are avoided in this certificate. PN3 is used
only to remove A=C=0 when V0; it is not applied in the later V-unit
certificate.

## 4. The V0, x-unit center check

Substituting x=-p7 into S8 gives
3+12A+4B-C+2E. The C0 case has A1 and B0/-1, forcing E2/4;
only the second is allowed by the actual E product. For C!=0,
C=C* gives E=10A-4B. If E0, only A=B0 satisfies that among the
four pairs. If E!=0, comparing E*=8+A+10B gives9A+5B=8,
whose four left sides0,10,9,4 fail. Thus only the TWO prefixes in
the main survive. Their actual x values and root sets were recomputed
from(7), not from the x0 table:

    (A,B,C,E,x)=(0,0,3,0,15):
      2x-q9=2, -Z-x=11, Z+8x+d11=10;
    (A,B,C,E,x)=(1,-1,0,4,12):
      2x-q9=13, -Z-x=4, Z+8x+d11=3.

Each is a genuine contradiction of the actual witness products.

## 5. The V-unit certificate and all remaining center cases

V!=0 forces actual D6(1)=0 by the small-root residue test. Substituting
V=5-15A-B-15C-6E independently gives

    p7=10+11A+9B+6C-2E,
    T=S8-8x=7A+9B+11C+2E.

For example:

* A0,B0,C0,E4 gives V=5-24=0, which is outside this case.
  It is NOT discarded from the entire proof: Section3 already covers V0.
* A1,B0,C16,E9 gives V=9-240-54=-285=0, also already covered.
* A0,B2,C14 has E*=9. Its E0 values are V2,p7=17,T1;
  its E9 values are V5,p7=18,T0. Thus it contributes the second
  possible T0 prefix, with no accidental reduction of a nonzero entry.
* A1,B-1,C1 has E*=18. Its E0 values are V14,p7=18,T9;
  at E18 they are V1,p7=1,T7. No zero p7 is hidden here.

The eight main rows follow from the four actual(A,B) pairs and both
C choices. Every p7 entry is nonzero. Exactly the two stated T0
entries survive V!=0. Their middle witness equations fail:

    all low A,B,C,E0,V5,x0 gives Z9,q9=13,d11=1,
    so y is0/6 by one equation and10 by the other;

    A0,B2,C14,E9,V5,x0 gives Z16,q9=1,d11=8,
    so y is0/18 by one equation and3/5 by the other.

For x!=0, a hypothetical S8=0 gives E=15-5A-6B+C. At C0 the four
required E values are15,3,10,16, while the allowed nonzero alternatives
are4,3,13,4; only A0,B2,E3 survives. At C=C*, E becomes-1+8A+9B.
Its E0 comparison has left sides0,18,8,18 for8A+9B, never1.
Its E* comparison has left sides0,17,7,8 for7A-B, never9.

The sole C0 survivor gives V4,p7=3,x16. Direct substitution yields
Z5,q9=0,d11=1. Its roots are{0,13} and{17,1}, disjoint.
This closes every V/x zero/nonzero case without assuming an odd unit.

## 6. Actual m6 bridge, corollary and important nonclaims

Under the assumed H6/H8/H10 ladder, R11B makes H12(r) nonzero.
The earlier actual equations and accepted Euler estimate supply(Q6).
The NEW field obstruction gives an unavailable H12 center. An actual
noncenter witness then exists; TA1 makes a7 unit impossible. Only now
are a6 and D7(1) FORCED units. The R8 fork needs a nonunit EC at12/13/14,
or a nonunit a6 in its other two alternatives. Every one is contradicted.
The EC14 exclusion is specifically its NONUNIT constant requirement:
an ordinary unit-center H14 equation by itself is not inconsistent.

The corollary's coefficients are a13,a11,a9 at m3,m4,m5. No a7 unit
is needed or assumed there. Simple1 and the separately accepted
GLOBAL carrier exclusion justify the full gcd, including its accepted
equal-degree boundary; no local carrier is silently made rational.

The proof does not bound nu, delta=s-2r, heights, ordinary root order,
or all witness valuations. It makes no sign inference from a residue.
It does not produce an actual lift from any displayed tuple. Earlier
m3–m5 can retain additional even residues absent from(Q6); they are not
silently covered. A second constructor pass found no arithmetic gap,
but this is still only an unverified proposed proof awaiting TWO OTHER
whole audits.
