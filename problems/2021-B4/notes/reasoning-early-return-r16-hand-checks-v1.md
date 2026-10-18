# R16 complete hand coefficient and affine checks

18 October2026 UTC. **Candidate proof - unverified.** These checks
were derived and checked by hand. No mathematical code, table generator,
CAS, author/source replay, sample or larger mask enumeration was run.
The new metadata code cannot verify these mathematical statements.

## Three original-center rows

Under(Q*) the possible residues are at indices

    0,1,2,3,4,5,6,7,8,9,13,15.

The exact rational beta_j are reduced only after dividing by19.
For j2/3/4/5/6/7/8/9/13/15 their reductions are

    10,3,8,-1,7,14,-1,5,14,-1.

Examples:190/19=10,1140/19=60=3,4845/19=255=8,
15504/19=816=-1,38760/19=2040=7,77520/19=4080=14,
125970/19=6630=-1,167960/19=8840=5. Symmetry supplies j13/15.
Thus the original divided equation is EXACTLY

    0=L+14x-U+5y+14w-u,
    L=-1+10A+3B+8C-E+7V.

Adding5x+14y+5w to the solved expression for u gives the first
row of main(1). There is no minus14x error.

For D15, the coefficients at j2/3/4/5/6/7/8/9/13/15 are

    105,455,1365,3003,5005,6435,6435,5005,105,1
    =10,-1,-3,1,8,13,13,8,10,1 mod19.

Its constant at X1 from a0/a1 is1-15=5. This gives R and
13x+8y+10w+u=R+6U, with a11 nonunit contribution0.

For D17 the corresponding coefficients are

    136,680,2380,6188,12376,19448,24310,24310,2380,136
    =3,15,5,13,7,11,9,9,5,3 mod19.

Its constant is1-17=3. Hence
11x+9y+5w+3u=S-9U with the stated S. All other possibly nonunit
even coefficients and a17 contribute0 in this field.

Temporarily retaining z=a11 before setting it0, elimination gives

    2z+5w=K-8x+6y+7U,
    3z+9w=N+4x-5y-6U.

The determinant3 has inverse13. Eliminate w to get
7z=2K+N-12x+7y+8U. Since7 inverse11,

    z=(3K-8N)+x+y+12U.

Back-substitution gives w=(7N-K)-2x-3y+8U. Expanding
K=R-L and N=S-3L gives the main Z/W0 coefficients, including
Z's8V and W0's9V. This uses only fixed field units.

## Low products, prefix completeness and V boundaries

Direct D_j(1) for j2..8 gives

    D2=A-1,
    D3=B-2+3A,
    D4=C-3+6A+4B,
    D5=E-4+10A+10B+5C,
    D6=V-5+15A+B+15C+6E,
    D7=x+13+2A+16B+16C+2E+7V,
    D8=U+12+9A-B+13C-E+9V+8x.

The actual product at j9 is not needed once S9=0 is assumed;
its full value is y-2x+q9+9U. No product at an absent index is
silently used. The eight prefixes from D2/D3/D4 and allowed E*
are exact. Each C choice and E* is distinct from0 here, so all
two-choice comparisons are literal; V* may vanish and is retained.

|A,B,C|E*|V* at E0|V* at E*|
|---|---:|---:|---:|
|0,0,0|4|5|0|
|0,0,3|8|17|7|
|0,2,0|3|3|4|
|0,2,14|9|2|5|
|1,0,0|13|9|7|
|1,0,16|9|16|0|
|1,-1,0|4|10|5|
|1,-1,1|18|14|1|

In particular a V*=0 case is represented by V0 and not deleted.
The proofs evaluate both algebraic formulas even when identical.
No assumption of unit a6, a8 or a9 appears.

## ALL32 affine equations when x is nonzero

S9=0 and z0 give U=(q9-Z)/3-x. Under x=-p7 this is main(7).
For V0 and V* the four affine functions have respective E slopes

    (11,13,7,6), inverses(7,3,11,16).

Their four CONSTANTS and UNIQUE E ZEROS are all shown. Thus each
entry is reproducible as minus its constant times its stated inverse.

|A,B,C|four constants|four unique E zeros|allowed E*|
|---|---|---|---:|
|0,0,0|(8,11,5,1)|(1,5,2,3)|4|
|0,0,3|(3,3,8,7)|(17,10,7,2)|8|
|0,2,0|(10,2,12,15)|(6,13,1,7)|3|
|0,2,14|(12,9,7,5)|(11,11,18,15)|9|
|1,0,0|(11,7,17,8)|(18,17,3,5)|13|
|1,0,16|(16,15,14,2)|(2,12,17,6)|9|
|1,-1,0|(10,2,4,1)|(6,13,13,3)|4|
|1,-1,1|(2,12,5,3)|(5,2,2,9)|18|

Examples fixing the sign convention: in prefix1 U at V0 is8+11E,
whose zero is-8*7=1; its second V0 factor is11+13E, zero-33=5.
In prefix4 the V* U function is7+7E, whose zero is-77=18.
In prefix8 the V* second factor is3+6E, whose zero is-48=9.
None of the32 zeros is0 or the associated E*. Both factors in
U times its second factor are therefore nonzero for every permissible
input. The x!=0 supposition cannot survive. Allowing a computed
x0 in this superset does not discard a genuine x!=0 possibility.

## ALL24 affine equations when x is zero

Now U=(q9-Z)/3, so the three functions of E have slopes

    (9,8,11), inverses(17,12,7).

The zero formulas are equivalently(2K,7J,12H), where K,J,H are
their constants. These are convenient checks avoiding negative signs.

|A,B,C|three constants|three unique E zeros|allowed E*|
|---|---|---|---:|
|0,0,0|(14,7,14)|(9,11,16)|4|
|0,0,3|(18,12,13)|(17,8,4)|8|
|0,2,0|(3,13,2)|(6,15,5)|3|
|0,2,14|(9,11,10)|(18,1,6)|9|
|1,0,0|(15,17,3)|(11,5,17)|13|
|1,0,16|(11,12,4)|(3,8,10)|9|
|1,-1,0|(11,14,9)|(3,3,13)|4|
|1,-1,1|(6,3,15)|(12,2,9)|18|

ONLY prefix2 E8 makes any factor zero; it is the second factor at
V0. V* at that E is7, so the V* formula correctly does not vanish.
Direct check of the surviving tuple:

    Z=7+8*3+4*8=63=6,
    q9=11+12*3+12*8=143=10,
    W0=4+11*3+6*8=85=9,
    U=14+14*3+9*8=128=14,
    y=-q9-9U=-136=16,
    w=W0-3y+8U=73=16.

At this tuple S9=16+10+9*14=152=0 and
z=6+16+12*14=190=0, as required by the temporary assumption.
The index8 second factor is0 as well, so this is not being removed
by an earlier equation it actually satisfies. The first global row
gives u=1; J15 is not used to discard it either.

Instead its actual index13 product fails. Binom(13,7)=6,
binom(13,8)=14,binom(13,9)=12 and the low coefficient expression
c13 equals7+12*3+14*8=155=3. Thus S13=407=8 and wS13=128=14.
This explicit final violation covers the sole affine exception.

## Actual valuation and both cubic frames

The proof makes S9 a FIELD unit, not merely an unavailable exact
zero. Since H11=binom(20,9)D9 and the scalar has valuation1,
v(H11(1))=1. An actual H11 witness is therefore in{0,r,s}; all
nonconstant terms of integral D9 there have valuation>=nu.
No leading coefficient is cancelled to deduce v(a9)>=nu.

At m4, H2/H4/H6(r)=0 gives a18/a16/a14 nonunit. BOTH R8 cubic
rows have a10/a11/a12 depths at least nu+sigma/2nu+sigma/3nu+sigma.
All six Q* hypotheses therefore hold even if sigma0, positive sigma,
one of these coefficients0, delta0 or delta arbitrarily deep. The
contradiction sigma<nu versus sigma>=nu does not select an origin.
The exact gaps in the two R8 cubic rows are not needed for this step.

## Quartic scaling, correct functional and ALL nine affine node pairs

Under the explicitly extra a8 unit and T4 hypotheses, P's degree
0/1/2/3 coefficient valuations are nonnegative after division by
a8 r^4. Its degree4 coefficient is495; every degree>=5 coefficient
has valuation at least nu. Differentiation over Q before reduction
gives main(12); no derivative of the reduced high-degree terms is
used in place of that justified identity.

The actual Euler value has excess>=3nu after division by
19 beta12 a8 r^4, or it is0. Its later even terms have strictly
positive excess2nu,4nu,6nu,8nu-1 as lower bounds. Exactly q,H2(q),
H4(q) remain. In F19,

    beta12=beta8=18, beta10=15,
    binom(12,2)=66=9, binom(12,4)=495=1,
    15/(18*9)=15/10=11, 18/(18*1)=1.

For w0 the monic quartic has the C0/B0 formulas in the main. Its
functional is

    q(1)+11H2(q)(1)+1 = 68-136v+12C0+B0
                    =11-3v+12C0+B0 mod19.

All nine(coefficient,constant) pairs in the affine equation for v,
and their solutions, are:

|u,t|coefficient|constant|solution v|
|---|---:|---:|---|
|0,0|16|11|10|
|0,1|8|15|10|
|0,2|0|8|impossible|
|1,0|9|7|14|
|1,1|15|4|1|
|1,2|2|14|12|
|2,0|7|17|3|
|2,1|8|7|11|
|2,2|9|15|11|

Only1 at u=t1 is a permitted v. The coefficient-zero cell is
treated by its nonzero constant, not by inversion. Coalescing nodes
are retained; indeed the one surviving case coalesces all three.
Reflection takes w2 to w0 and preserves all even derivative values
at1; q=(z-1)^4-1 is itself invariant, so it covers both roots.

Direct diagnostic: q(0)=q(2)=0,q(1)=-1,
q'=4(z-1)^3,H2(q)=6(z-1)^2,H3(q)=4(z-1),H4(q)=1.
The correct functional equals-1+0+1=0. The m5 functional with final3
would instead give2 and cannot be borrowed at m4.

Only the node1 can witness the three derivative conditions. The
three actual small rational values have DISTINCT residues0,1,2;
this is the direction ACTUAL ZERO => residue node => identified
ACTUAL value, with no assertion that an arbitrary residue lifts.

Coefficient comparison gives

    11*(a9/(a8r))=-4 => ratio10,
    9*(a10/(a8r^2))=6 => ratio7,
    12*(a11/(a8r^3))=-4 => ratio6,
    a12/(a8r^4)=0 mod19.

The first three ratios are nonzero, so the depths are exact. The last
has at least one extra integral valuation, including infinity. Unit a8
also gives D8(r) unit and H12(r) nonzero, while its actual rational
witness is center1. D12-D12(r) has first three derivatives0 and fourth
derivative12*11*10*9 D8(r)!=0. This proves EXACT order4 contact,
without asserting any repeated root of f or D12.

## Domains and open endpoints

All divisions use19 in Q before reduction, a proved unit a8 only in
R16C, nonzero r, fixed binomial scalars or displayed nonzero field
slopes. None divides by displacement, a possibly zero low coefficient,
or a node. Nu>=1 is arbitrary; no selected-minimum upper bound10,
height or ordinary sign is invoked. No all-real-root theorem or new
prime5 argument is used. Global degree comparisons are used for the
explicit full-gcd conclusions and stated no-(EC) application. Every
other new assertion uses actual
rational witnesses and their necessary products directly. R15 remains
unverified and unused. The four-depth/nonunit-essential-center branch
and m3 remain OPEN.
