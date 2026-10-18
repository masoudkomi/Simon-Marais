# R17 hand reconstruction record

2026-10-18 UTC. **Candidate proof - unverified.** These are exact
hand calculations supporting the whole main; no mathematical executable,
CAS, mask scan, author rerun or old certificate replay was used.
Administrative fingerprint/freezer code is not mathematical evidence.

## Three global rows and binomial coefficients

The relevant ORIGINAL divided-center coefficients beta2..beta8 are
10,60,255,816,2040,4080,6630, reducing to10,3,8,-1,7,14,-1.
beta13=4080=14 and beta15=816=-1. Thus its residual equation is
L+14x-U+14w-u=0, equivalently5x+5w+u=L-U.

At D15 the constant and A/B/C/E/V coefficients are

    1-15=5; 105=10;455=-1;1365=-3;3003=1;5005=8.

Its x/U/w/u coefficients are6435=13,6435=13,105=10,1.
At D17 the low coefficients are

    1-17=3;136=3;680=15;2380=5;6188=13;12376=7,

and its x/U/w/u coefficients are19448=11,24310=9,2380=5,136=3.
Moving these low pieces gives exactly R,S in the main.

Writing K=R-L,N=S-3L, the subtractions give
5w=K-8x+7U and9w=N+4x-6U. Their eliminated equation is

    0=9K-5N-92x+93U.

Dividing by fixed unit3 gives Z+x+12U=0, Z=3K-8N.
For W0, note carefully7N-K=7S-20L-R=7S-L-R modulo19;
this gives4-2A+5B+11C+6E+9V. Substituting the Z relation into
the first w equation gives w=W0-2x+8U. No low variable is inverted.

## The actual products and complete low prefixes

D2..D6 have the following constant-free residual values:

    A-1;
    B-2+3A;
    C-3+6A+4B;
    E-4+10A+10B+5C;
    V-5+15A+B+15C+6E.

D7 is x+13+2A+16B+16C+2E+7V.
D8 is U+8x+12+9A-B+13C-E+9V.
D13 is w+6x+14U+7+2A+B+12C+14E+6V.
Here binom(13,7)=1716=6 and binom(13,8)=1287=14.

The successive products give A0/1, B0 or2-3A, C0 or3-6A-4B,
E0 or4-10A-10B-5C. The eight ordered triples and E* are:

    (0,0,0):4; (0,0,3):8; (0,2,0):3; (0,2,14):9;
    (1,0,0):13; (1,0,16):9; (1,-1,0):4; (1,-1,1):18.

All E* are nonzero. The index6 product allows V0/V*, including
V*=0 and its harmless overlap. No division by V* is justified or used.

## Every U-nonzero table entry

The cancellation Z-12T has coefficients
(-4,1,8,4,-3,-5) at(1,A,B,C,E,V). Substituting V* makes it
9+13B+3C+8E. The two E zeros are therefore exactly
13(A+8B+4C-4) and15B+2C+6.

For all eight prefixes, the following are the UNREDUCED integers
obtained from those formulas, followed by their residues. These are
the entire16 affine zeros, independently checked against E0/E*.

|prefix order|V0 integer|V0 residue|V* integer|V* residue|
|---|---:|---:|---:|---:|
|1|-52|5|6|6|
|2|104|9|12|12|
|3|156|4|36|17|
|4|884|10|64|7|
|5|-39|18|6|6|
|6|793|14|38|0|
|7|-143|9|-9|10|
|8|-91|4|-7|12|

Only row6 E0 hits. It has V*=5-15-240=-250=16.
Direct substitutions give Z277=11,T373=12,p7=383=3,
W0=322=18,c13=297=12. Then x0/16 yields U7/12 and w17/6.
At x0, D13=17+98+12=127=13, product221=12.
At x16, D13=6+96+168+12=282=16, product96=1.
Both contradict the actual H7-type product.

## Every U-zero table entry

For U0, x=-Z and x(x+p7)=0 gives Z0 or Z=p7.
The E coefficients4,13,2,-4 have fixed inverses5,3,10,14.
Solving the four equations yields

    c1=3+6A+B+17C, c2=11+14A+17B+13C,
    c3=3+13A+10B+4C, c4=14+4A+9B+18C.

ALL32 UNREDUCED integer evaluations are:

|prefix order|c1|c2|c3|c4|
|---|---:|---:|---:|---:|
|1|3|11|3|14|
|2|54|50|15|68|
|3|5|45|23|32|
|4|243|227|79|284|
|5|9|25|16|18|
|6|281|233|80|306|
|7|8|8|6|9|
|8|25|21|10|27|

Their residues are exactly the32 entries in main Section3. For each
row, every residue differs from0 and its corresponding E*. This
comparison is exhaustive because each equation has a NONZERO FIXED
E coefficient; it is not a sample or a valuation/witness search.

## Actual application and endpoints rechecked

Under actual Q*, R16A supplies v(a9)>=nu, while J15 supplies a17
nonunit. The three rows and every product then really follow from f;
there is no unproved rational lift. At e6 the Euler estimate applies
only if H6(r)!=0; otherwise direct D14(r)=0 gives its nonunit constant.
Both cases make a14 nonunit. This is why the forced unit assertion
is global in(S),(W), not just a guessed m4 support.

At m4, the exact difference quotient for a hypothetical H8 witness
w0/s has a unit12a11 when a11 is unit, while all terms of degrees
at least2 have valuation>=nu. The exact valuation of r-w is nu in
BOTH cases, including exact s=2r. The result violates v(D12(r))>=2nu.
This forces an actual nonzero a12 and EC8, not merely an available
center. Irreducible carrier degree14>12/11/10 and simple1 justify
the full gcd assertions. If a11 nonunit and a10 unit, R8A's strict
bound holds with tau0 even when a9=0. Its EC conclusion is NONUNIT.

All derivative multiplicities at1 use identities over Q. A repeated
root of D12 or D11 is not a repeated root of f. In the other double-
origin frame,1-s is a unit, D_j(s)=a_j modulo19, and actual derivative
transport is by a NONZERO rational scalar. Thus coefficient unit
statuses and the actual first break are unchanged. Root order, finite
displacement, exact s=2r and every coefficient0 remain covered.
