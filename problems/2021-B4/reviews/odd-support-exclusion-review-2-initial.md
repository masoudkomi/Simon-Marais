# Whole initial independent audit R2: the odd-support obstruction

2026-10-17 UTC. Reviewer `review_2017_coarsening_r1`; requested
gpt-6.1-sol/max, effective readback unavailable. I did not construct
PN1-PN4 or the accepted parity packet. This whole initial report,
ledger and source/integrity record freeze before any peer PN findings
are read. No candidate, old review or shared file is modified.

Target main SHA256
a7845441df7725edc5d30e28f7b8f28c529b0b710168ad4b068d279582c1857c;
target freeze SHA256
337a43225bd6637d666bc992738a49afab8e7b569f526281add45564ab17b592.
I read the whole candidate and exact accepted PP1/PP2/PB1 scopes, and
reconstruct all64 possibilities below by hand. I did not run the
constructor's code, inspect its output as a proof, enlarge the support
class, or use a native CAS. Administrative hashing is the only code.

**Disposition:** no substantive defect found. PN1 and PN2 have the
stated complete finite proof; PN3 and PN4 are valid within the exact
accepted rational-witness hypotheses. I recommend scoped acceptance
after the other independent audit and coordinator reconciliation.
No degree20, all-mask, general repeated-root or annual classification
is established by this report.

## 1. Exact finite domain and the operator

There are precisely2^6=64 supports:1 and15 are compulsory, and each
of3,5,7,9,11,13 is independently optional. b0=1 and off-support
b_j=0 are ordinary integers. When j is added after all smaller
indices, the existing polynomial has degree<j and evaluates at j
as sum_(k<j)binom(j,k)b_k. Appending b_j binom(Z,j) with its
negative evaluation gives exactly T_j F=F-F(j)binom(Z,j).
Terms at future indices vanish at every earlier nonnegative index.
Thus all selected exact roots are retained, particularly F_I(1)=0
from b1=-1. Every binomial denominator divides15!, a19-unit.
Reduction and ordinary differentiation therefore take place in Z_(19).

PN1 classifies this finite support class without assuming every selected
b_j remains nonzero mod19. The actual support condition from PP1 is
an additional later check, correctly retained for the second survivor.

## 2. Independent prefix reconstruction

Starting at1-Z, the possible residual coefficients(b3,b5,b7) are:

|3,5,7|b3|b5|b7|
|---|---:|---:|---:|
|000|0|0|0|
|001|0|0|6|
|010|0|4|0|
|011|0|4|17|
|100|2|0|0|
|101|2|0|12|
|110|2|3|0|
|111|2|3|6|

Indeed b3=2 when selected; b5=4 without3 and-16=3 with3;
b7=6-35b3-21b5 when selected. These give6,-78,-64,272
in the four applicable cases, or6,17,12,6 modulo19.

Here is the independent Pascal evaluation table, whose columns are
the base1-z and binom(z,3),binom(z,5),binom(z,7) modulo19:

|z|1-z|C(z,3)|C(z,5)|C(z,7)|
|---|---:|---:|---:|---:|
|9|11|8|12|17|
|11|9|13|6|7|
|13|7|1|14|6|
|15|5|18|1|13|
|17|3|15|13|11|

Multiplying these three coefficient columns and adding the base gives
all eight f=(f9,f11,f13,f15,f17), respectively

    000: (11,9,7,5,3)      001: (18,13,5,7,12)
    010: (2,14,6,9,17)     011: (6,0,13,2,14)
    100: (8,16,9,3,14)     101: (3,5,5,7,13)
    110: (6,15,13,6,15)    111: (13,0,11,8,5).

This checks every prefix vector in the candidate rather than infer them
from its claimed64-case output.

## 3. Operator expansion and all64 endpoint values

Let a,b,c indicate9,11,13. The necessary binomial residues are
C(11,9)=17; C(13,9)=12,C(13,11)=2;
C(15,9)=8,C(15,11)=16,C(15,13)=10;
and at17 the values for9,11,13,15 are9,7,5,3.

Successively subtracting the relevant evaluation times that binomial
column gives

    g11=f11+2a f9,
    g13=f13-2b f11-a(12+4b)f9,
    g15=f15-10c f13+b(3+c)f11
                    +a(11+6b+6c+2bc)f9.

Substitute these into f17-9a f9-7b g11-5c g13-3g15.
The coefficients reduce to

    u+6c f13+b(3+7c)f11
              +a(15+6b+4c+14bc)f9,
    u=f17-3f15.                                         (A)

I used the following compressed complete certificate, with no code.
For c=0 its four(a,b) cases are u, u+3f11, u+15f9,
u+3f11+21f9. For c=1, the a coefficient simplifies because
15+4=0 and6+14=1 modulo19. Hence there are three values:
U=u+6f13 when b=0 (for BOTH values of a), U+10f11 for(a,b)=(0,1),
and U+10f11+f9 for(a,b)=(1,1). The table is:

|3,5,7|c0:a0b0|c0:a0b1|c0:a1b0|c0:a1b1|c1:b0, either a|c1:a0b1|c1:a1b1|
|---|---:|---:|---:|---:|---:|---:|---:|
|000|7|15|1|18|11|6|17|
|001|10|11|14|9|2|18|17|
|010|9|13|1|17|7|14|16|
|011|8|8|3|1|10|10|16|
|100|5|15|11|12|2|10|18|
|101|11|7|18|13|3|15|18|
|110|16|4|11|16|18|16|3|
|111|0|0|5|7|9|9|3|

Each row covers4+2+1+1=8 distinct(a,b,c) choices, including the
explicitly duplicated b=0,c=1 value; all8*8=64 cases are therefore
accounted for. To compare with the candidate's columns000,...,111,
the mapping is, in order, columns1,5,2,6,3,5,4,7 of this table.
It reproduces EVERY entry of that64-case table, not only its zeros.
Only prefix111 with a=c=0 and b=0 or1 vanishes.

Those supports are exactly{1,3,5,7,15} and{1,3,5,7,11,15}.
For either, the prefix coefficients are b3=2,b5=3,b7=6;
b9=b13=0. Adding11, if present, has b11=-f11=0 modulo19.
The last evaluation is g15=f15=8, so b15=-8=11. The entire
residue vector is therefore exactly the displayed PN1 vector.
The optional b11 is a zero residue; it need not be the zero integer.
It cannot be in the actual unit support of PP1. This proves PN1
with its precise nonvanishing qualification.

## 4. The divided second endpoint

For j>=3 the derivative of binom(Z,j) at1 is
(-1)^(j-2)/[j(j-1)], by differentiating its single factor Z-1.
For odd j this is negative. For both surviving vectors the derivative
modulo19 is consequently

    -1-(2/6+3/20+6/42+11/210).

The four fractions are13,3,11,11 modulo19 and sum to0, so the
derivative is-1. The b11 term, if selected, contributes0 modulo19.
All displayed denominators are units and F_I(1)=0 exactly. Taylor
over Z_(19) gives F_I(20)=19 F'_I(1) modulo19². Thus it is
-19=342 modulo361, and is not0. This treats both possible supports,
even though only one has the actual nonzero support. PN2 therefore
needs no extra unit hypothesis and follows exactly as stated.

This uses the ordinary derivative in the length variable Z. It does
not replace any characteristic-zero Casas--Alvero derivative by a
finite-field derivative or assume the degree17 residue lifts.

## 5. PN3: every accepted PP1 hypothesis is retained

The accepted register and frozen PP1 body concern the normalized
degree20 J15 multiplicity-two setting at prime19, with an actual
rational common root for EVERY nonconstant derivative. Coefficients
a_j are19-integral, a0=1,a1=-1, ord0 f=2 and the largest unit
index is15. Accepted root reduction says every rational f-root other
than1 reduces to0. Neither all roots being rational nor arbitrary
algebraic/local roots is substituted.

Assume additionally H3(f)(1)=0 and that every even a_j,2<=j<=18,
is a nonunit. The actual unit index set I is odd, contains1,15,
and has no indices beyond15. At a unit index j a rational D_j
witness cannot reduce to0, since the reduction has nonzero constant
a_j. It must be the actual root1. Thus D_j(1)=0 gives precisely
the triangular recurrence modulo19; induction identifies a_j=b_j
mod19, retaining b_j!=0 for selected j. This supplies a SINGLE
support, not separately chosen supports at the two endpoints.

H3(f)(1)=0 is an exact characteristic-zero equality. Although
H3=1140D17 has a19-divisible scalar, dividing an exact zero over Q
is valid, so D17(1)=0 and F_I(17)=0 modulo19. For the other
endpoint f(1)=0 becomes-19+sum_(j=2)^18 C(20,j)a_j=0.
Each C(20,j) in that range has valuation1. Replacing a_j by b_j
for j<=15 changes this only modulo19², and j>=16 terms vanish
modulo19² because their a_j are nonunits. Hence F_I(20)=0
modulo19². This does not assert the integer model equals f or has
its characteristic-zero roots.

PN2 contradicts those two necessary congruences. Therefore under
H3(f)(1)=0 at least one even normalized coefficient is a19-unit,
exactly PN3. It does not exclude every J15 multiplicity-two polynomial
without that extra center equality. This application agrees with the
accepted PP1 endpoint statement and does not need a new CA theorem.

## 6. PN4 and the exact PP2 scope

The candidate explicitly invokes the repeated2R-root setting OF PP2,
not an arbitrary repeated-root branch. Its accepted assumptions include
the normalized rational-witness J15 setup, the accepted sole-H3
configuration, the two2R slots forming a double root d, the exact
equations H6(r),H8(r),...,H14(r)=0, and an actual rational
noncenter common H18 witness. The earlier return/valuation restrictions
are accepted only with those hypotheses. A local root of H18 alone
or a center equation alone is insufficient.

I read the complete PP2 derivation as well as its accepted register.
For the five ladder indices the corresponding D_j(r)=0 reduces to
a_j=0 modulo19 because r has positive valuation. A noncenter rational
H18 witness z in{0,r,d} gives a2=2z-z², hence a2 nonunit;
D2(r)=(r-z)(r+z-2) also gives the stated h18 valuation. The
accepted repeated-root Taylor/Euler bound gives the e0 and h16 bounds,
including delta=0 separately. With h18 nonzero its valuation is at
least nu+1; h16 then has valuation at least min(3nu+1,4nu).
Since4845 has valuation1, the exact displayed formula for a4 makes
it nonunit as well. The already accepted J15 reduction handles a16,a18.
Thus this exact PP2 setting implies all the even nonunit conditions
and its sole-H3 premise supplies H3(f)(1)=0.

PN3 rules out that conjunction. No use is made of a tied-minimum
Taylor case outside PP2, an unspecified2R root, a different mask,
or a general degree20 exclusion. PN4 is therefore a valid scoped
application of the accepted theorem and the new finite obstruction.

## 7. Source attribution, PB1 and final limits

The primary *Descent polynomials* source, arXiv1710.11033v2,
Proposition2.1 and its whole applicable proof were directly read.
It assumes a finite nonempty positive descent set I with maximum m
and gives d(I;Z)=C(Z,m)d(I-minus{m};m)-d(I-minus{m};Z), initially
for integer lengths beyond m and hence as a polynomial identity.
The same recurrence and base1 imply F_I=(-1)^|I|d(I;Z).
No complement, peak-set admissibility or real-root theorem is imported.
The sign is a unit for both endpoint divisibilities. The broader
MacMahon/one-recycled-root connection remains attributed; the finite
proof needs no unverified new theorem from that connection.

The accepted PB1 polynomial has exactly the valid first survivor's
residue vector and derivative residue-1, in agreement with this whole
reconstruction. It is a characteristic19 degree17 certificate failing
the second endpoint, not a rational degree20 counterexample. Thus PN1
does not contradict PB1, and PN2 does not discard an actual valid
two-endpoint support found there.

The official quantifier requires rational common root values allowed
to depend on derivative order. This is retained throughout the scoped
applications. No preliminary(a) proof, new support search, remaining
mask enumeration, rational lift, full degree20 theorem or annual
classification is supplied. No mathematical code or CAS was needed:
the complete finite certificate above is hand-reconstructible. Both
initial reviews and coordinator reconciliation are still required.
