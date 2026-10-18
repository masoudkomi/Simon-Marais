# R18 hand arithmetic and adversarial checks

2026-10-18 UTC. Candidate proof - unverified; author hand checks only.
No mathematical program or author/source certificate rerun occurred.

## Fixed-row elimination check

From the first three center rows, put K=R-L,N=S-3L. Subtracting
gives5w=K-8x+6y+3z-2t+7U and
9w=N+4x+14y+z-3t-6U. Equivalently the un-rearranged second
row is15x+5y+18z+3t+9w=N-6U. Twice this row minus three times
the first difference gives3w=2N-3K-6x-9y-7z+5U.
Their fixed determinant operation gives
t=Z0+x+y+z+12U and w=W0-2x-3y+4z+8U. Setting t into the
actual D11 row yields, together with the D12-12D11 row, the
equations for y/z in main(3). No t, z, x, U, displacement or
possibly zero coefficient was divided out. Only field scalars.

For a quick full check of the resulting linear reduction, substitute
z=10+10A+5B+14C+4E+6V+9x+6U+6y into
t=Z0+x+y+z+12U. Comparing with the D11 equation gives
y=12-4A+10B+10C+4E+2V+8x+8U. Substitution gives the displayed
z,t,w. The x coefficient of z really cancels. The u value is then
u=L-U-5x-14y-4z-14t-5w.

## Affine-zero certificate completeness

The eleven distinct usable-entry groups are exactly:

1. Prefix000,E4: c7/d7, V0, x17,U8.
2. Prefix003,E0: d1, V17, x0,U0.
3. Prefix003,E8: d5, V7, x0,U8.
4. Prefix020,E0: d1, V3, x0,U0.
5. Prefix02,14,E0: d4, V2, x2,U0.
6. Prefix100,E13: d3, V7, x5,U0.
7. Prefix100,E0: d4, V9, x17,U0.
8. Prefix100,E13: d5/d6, V7, x0,U5.
9. Prefix10,16,E9: c2/d2, V0, x0,U0.
10. Prefix1,-1,0,E0: d6, V10, x0,U2.
11. Prefix1,-1,1,E18: c8, V0, x6,U11.

There are no other entries equal to0 or E* in the two full tables.
The three slash pairs are duplicates, not extra omitted tuples.
Only group4 has z*D10=0; its z is0, so no division by z is allowed.
At group4, w=3 and D13=9+24+24=0, so the unused last product
does not contradict the tuple. The original three row values are
83=7,106=11,79=3mod19. This is a survivor, not a contradiction.

## Exact integer coefficient identity

D12-12D11 before eliminating a3/a6 has coefficients

    const109; a2 -594; a3 -1760; a4 -3465;
    a5 -4752; a6 -4620; a7 -3168; a8 -1485;
    a9 -440; a10 -66; a11 0; a12 1.

For example binom(12,5)-12binom(11,5)=792-5544=-4752.
With a3=2-3a2 and a6=-35+45a2-15a4-6a5, the constant and
a2/a4/a5 coefficients are158289,-203214,65835,22968. The
constant is19*8331 with8331=19*438+9. This is the valuation-one
term that excludes nu>=2. It is not an assumed numerical maximum.

## Whole leading increment table reconstruction

At nu1, only q2,q4,q7,q12,q14,q16,q17 may contribute. Exact
triangular center equations give increments modulo19:

    da3=-3q2,
    da6=7q2+4q4,
    da11=18q2+7q4+12q7,
    da13=18q2+7q4+8q7+6q12,
    da15=14q2+17q4+17q12+4q14.

Here da means(a_j-c_j)/19 mod19, not a_j/19 for a unit.
For example the a15 coefficient of q7 is
-13-16*12-10*8=-285=0mod19, whereas its q2 coefficient is
-10+54-56-288-180=-480=14. Its q4 coefficient is-230=17.

The exact baseline is

    c3=2,
    c6=5-20*2=-35,
    c11=10-165*2-462*(-35)=15850,
    c13=12-286*2-1716*(-35)-78*15850=-1176800,
    c15=14-455*2-5005*(-35)-1365*15850-105*(-1176800)
       =102103029.

Useful mod361 representatives are2,-35,-34,60,-45. Thus

    D17 baseline=-16-42*2+102*(-35)+102*(-34)+214*60+136*(-45)
                =-418=304=19*16 mod361,
    divided-f baseline=-1+60*2+235*(-35)+176*(-34)+109*60+94*(-45)
                       =-11780=133=19*7 mod361.

After these substitutions, the full two leading rows have columns
(q2,q4,q7,q12,q14,q16,q17):

    D17:(18,16,2,18,8,17,1), constant16;
    fdiv:(17,0,15,9,3,8,3), constant7.

For D17 the q2 sum is3-45+49+126+90+42=265=18;
the q4 sum is5+28+49+35+51=168=16;
the q7 sum is11+84+40=135=2;
the q12 sum is13+30+51=94=18;
the q14 sum is15+12=27=8. The last two columns are17 and1.

For fdiv the q2 sum is10-9+49+90+252+252=644=17;
the q4 sum is8+28+35+98+306=475=0;
the q7 sum is14+60+112=186=15;
the q12 sum is18+84+306=408=9;
the q14 sum is7+72=79=3. The last two columns are8 and3.

Subtracting3D17 cancels the arbitrary eta=q17 and leaves
(1,9,9,12,17,14,0), constant16. Inserting the ACTUAL leading
witness identities gives16+rho*(2u+4v+w+12). The independent
F12 row gives9+rho*(u+9w+9). Their elimination is exactly
2*(-u+v+w-1)=0, not an ordinary inequality on r.

## Degeneracy and failed overstatements

* All exact-zero coefficients remain allowed in the depth induction.
* Every unit inference is a unit residue, not a nonzero rational number.
* The field lemma does not require t/u nonzero. Its survivor makes them
 4/12 and so supplies that conclusion.
* Delta0 and arbitrary finite delta depths enter only the accepted Euler
 estimate. No division by delta occurs in the new proof.
* Both origin frames have the same field tuple and transform rho/labels
 consistently. This is covariance, not a new symmetry of f.
* Small simple derivative roots may correspond to double roots of f;
 the gcd is nevertheless simple because the derivative root is simple.
* The characteristic19 degree12 example does not satisfy the five
 original center rows. It blocks a shortcut, not the stated field lemma.
* The six leading triples do not supply a rational lift. All three
 oriented frames and the non-adjacent m4/m3 cases remain open.
