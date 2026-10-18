# R14 complete hand reconstruction of the finite certificates

18 October2026 UTC. **Candidate proof - unverified.** No mathematical
executable, scan, mask table, CAS, test scaffolding or author rerun was
used. The following values were derived by substituting into the main's
affine equations. They are a proof-critical certificate for the stated
finite field implication, not evidence that a residue configuration
lifts to an actual rational polynomial. All arithmetic is in F19.

Each ordered pair in a table gives the values at E=0 and E=E*, in that
order. The eight low prefixes follow directly from the four actual
witness products, not a chosen subset. Their E* values are:

    (A,B,C): (0,0,0),(0,0,3),(0,2,0),(0,2,14),
             (1,0,0),(1,0,16),(1,−1,0),(1,−1,1);
    E*:       4,8,3,9,13,9,4,18.

Put F=F9,G=F10 and K=G−10F. The ACTUAL center values are S9=F+y,
S10=G+10y. Thus y=0 uses zeros of F/G, while y!=0 uses y=−F!=0
and zeros of K. The common witness at D11, which is original H9,
has product z S11=0 with

    z=Z+12U+y, S11=Z+d+6U−y,
    Z=7+14A+15B+8C+4E+8V,
    d=9+17A+13B+7C+6E+6V.

## I. U=0, V=V*!=0

Accepted R12A makes V nonzero in this case. Its exact substituted value
is V*=5−15A−B−15C−6E. The entries with V*=0 do not belong to CaseI;
they are displayed so the exclusion cannot hide a zero case.

    F=13+11A+6C+2E,
    G=15+11A+5B+5C−E,
    K=18+15A+5B+2C−2E.

|A,B,C|E*|V*|F|G|K|
|---|---:|---|---|---|---|
|0,0,0|4|5,0|13,2|15,11|18,10|
|0,0,3|8|17,7|12,9|11,3|5,8|
|0,2,0|3|3,4|13,0|6,3|9,3|
|0,2,14|9|2,5|2,1|0,10|18,0|
|1,0,0|13|9,7|5,12|7,13|14,7|
|1,0,16|9|16,0|6,5|11,2|8,9|
|1,−1,0|4|10,5|5,13|2,17|9,1|
|1,−1,1|18|14,1|11,9|7,8|11,13|

For y=0 the only zeros occur at E3 in prefix(0,2,0), or E0 in
(0,2,14). For y!=0 the only K zero is E9 in(0,2,14), and F=1
there, so y=18. All three have V!=0.

## II. U!=0, V=V*!=0

Here U=−7A−9B−11C−2E and

    F=13+5A+14B+2C+3E,
    G=15−B+4C+4E,
    K=18+7A+11B+3C+12E.

The V* values remain the previous table. Both V* and U must be
nonzero; entries violating either condition are retained in the
table but are not CaseII inputs.

|A,B,C|E*|U|F|G|K|
|---|---:|---|---|---|---|
|0,0,0|4|0,11|13,6|15,12|18,9|
|0,0,3|8|5,8|0,5|8,2|8,9|
|0,2,0|3|1,14|3,12|13,6|2,0|
|0,2,14|9|18,0|12,1|12,10|6,0|
|1,0,0|13|12,5|18,0|15,10|6,10|
|1,0,16|9|7,8|12,1|3,1|16,10|
|1,−1,0|4|2,13|4,16|16,13|14,5|
|1,−1,1|18|10,12|6,3|1,16|17,5|

For y=0 only E0 in(0,0,3) and E13 in(1,0,0) give a zero, both of F.
For y!=0, K=0 at E3 in(0,2,0), where F=12 and y=7. The other
algebraic zero E9 in(0,2,14) has U=0 and is CaseI instead. No G
entry is zero in this case, including any of the excluded entries.

## III. U!=0, V=0

Now U=7−9A+B−13C+E and

    F=17+12A+17B+9C+2E,
    G=2+A+13B+5C+12E,
    K=3+14A+14B+10C+11E.

|A,B,C|E*|U|F|G|K|
|---|---:|---|---|---|---|
|0,0,0|4|7,11|17,6|2,12|3,9|
|0,0,3|8|6,14|6,3|17,18|14,7|
|0,2,0|3|9,12|13,0|9,7|12,7|
|0,2,14|9|17,7|6,5|3,16|0,4|
|1,0,0|13|17,11|10,17|3,7|17,8|
|1,0,16|9|18,8|2,1|7,1|6,10|
|1,−1,0|4|16,1|12,1|9,0|3,9|
|1,−1,1|18|3,2|2,0|14,2|13,2|

For y=0 the zeros are E3 in(0,2,0), E4 in(1,−1,0), E18 in(1,−1,1).
For y!=0, only E0 in(0,2,14) has K=0; F=6, so y=13.

## Witness-product verification for all ten exceptional prefixes

The main lists the complete seven y0 and three y!=0 tuples and their
Z,d,z,S11 values. Their products in that order are

    11,2,13,18,9,6,8; 14,6,12.

Each is NONZERO. For a direct check of a nontrivial unit-U tuple,
CaseII,y7 has (A,B,C,E,V,U)=(0,2,0,3,4,14). Thus Z=5,d=1,
z=5+12·14+7=180=9 and S11=5+1+6·14−7=83=7, giving product6.
In CaseIII,y13, Z=16,d=0,U=17, so z=233=5 and S11=105=10,
giving product12. For y0 CaseII prefix(1,0,0,13,7,5), Z=15,d=13,
z=75=18,S11=58=1, giving18. No coefficient has been divided out
to eliminate the possible z=0 branch; these forced tuples all have
nonzero z and nonzero S11 themselves.

Every entry follows from the displayed field polynomials and the two
allowed E values. No finite test or characteristic-zero lift supplies
an unrestricted inference. The only unrestricted steps are the exact
actual-to-residue implications and the subsequent actual contradiction
spelled out in the mathematical main.
