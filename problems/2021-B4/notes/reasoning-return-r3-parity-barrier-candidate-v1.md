# A degree17 residue barrier: the second descent endpoint is essential

2026-10-17 UTC. **Candidate proof - unverified.** Constructor:
review_2021_reasoning_j15_r2. Requested gpt-6.1-sol/max; independent
effective readback unavailable. Two fresh independent nonconstructor
audits are required. No novelty, rational lift, original branch
realization or characteristic-zero counterexample is claimed.
All calculations below are exact hand calculations in F19.
No mathematical program, CAS or support enumeration was used.

## Exact finite-field certificate PB1

Set normalized residues

    a0=1,a1=-1,a3=2,a5=3,a7=6,a15=11,
    all other a_j=0, 2<=j<=17.

Write D_j(X)=sum_(k=0)^j binom(j,k)a_k X^(j-k) over F19.
Then

    P(X):=D17(X)
      =X17+2X16+11X14+X12+9X10+14X2

is a nontrivial Hasse-CA polynomial of degree17 over F19.
Its derivatives have a cover using only the two roots0 and1.
Its normalized unit index set is exactly

    I={1,3,5,7,15}.

The associated descent polynomial satisfies

    d(I;17)=0 mod19,
    d(I;20)/19=1 mod19.

The second quotient is an integer since19|d(I;20).
In particular 19^2 does NOT divide d(I;20).

Thus the first residual-CA/descent equation in the preceding
parity candidate is actually realizable. Claiming that no
such residual degree17 polynomial exists would be false.
The simultaneous second endpoint remains essential.

## Verification of every finite-field condition

The displayed expansion of P follows from the reduced coefficients

    binom(17,1)=17,
    binom(17,3)=15, binom(17,5)=13,
    binom(17,7)=11, binom(17,15)=3 mod19.

Hence the coefficients are respectively2,11,1,9,14.
P(0)=0 and P(1)=1+2+11+1+9+14=38=0 mod19.
Since its X2 coefficient14 is nonzero,0 has multiplicity exactly2.

For1<=j<=16,

    H_(17-j)(P)=binom(17,j)D_j,

and every displayed binomial scalar is a19-unit.
If j notin I, D_j(0)=a_j=0. For the five indices in I the
actual D_j(1) checks are the following exact congruence calculations,
using integer representatives:

    D1(1)=0,
    D3(1)=1-3+2=0,
    D5(1)=1-5+10*2+3=19,
    D7(1)=1-7+35*2+21*3+6=133=7*19,
    D15(1)=-14+18*2+1*3+13*6+11=114=6*19 mod19.

The last line uses the listed binomial residues at degree15;
it is an exact congruence calculation. Thus every derivative
order1,...,16 has a common root0 or1 with P.
The remaining center identity D17(1) can also be checked directly:

    -16+15*2+13*3+11*6+3*11=152=8*19.

No characteristic-zero derivative theorem is used here.

## Why the original divided center endpoint fails

For completeness take the exact integer support model b_j:
b0=1,b1=-1, b_j=0 off I, and for j in I,

    b_j=-sum_(k<j) binom(j,k)b_k.

Its residues are exactly the a_j above. Put
F_I(Z)=sum_(j=0)^15 b_j binom(Z,j).
The published descent recurrence gives
F_I=(-1)^|I|d(I;Z)=-d(I;Z).

Since F_I(1)=0 exactly and its coefficient denominators divide15!,

    F_I(20)/19=F'_I(1) mod19.

At odd indices j>=3 the derivative of binom(Z,j) at1 is
-1/[j(j-1)]. The four contributions are

    a3/6=13, a5/20=3, a7/42=11, a15/210=11 mod19.

Their sum38 is0. Therefore

    F'_I(1)=-1,
    F_I(20)/19=-1,
    d(I;20)/19=1 mod19.

Meanwhile F_I(17)=D17(1)=0 mod19 proves the first endpoint.
This establishes both claims of PB1 without calculating a
large integer descent count or enumerating other supports.

The general recurrence and the Casas-Alvero/MacMahon connection
are published; their precise attribution is in the source log.
This is a scoped explicit residue certificate and a diagnostic
for an invalid shortcut, with no novelty asserted.

## What this certificate does not show

It is a degree17 polynomial in characteristic19, not a rational
degree20 polynomial. It fails even the original divided center
root congruence, so it cannot serve as a first-level model of
all hypotheses of the earlier parity PP1 statement. It neither
constructs a CA polynomial over Q nor supplies actual rational
witnesses or a lift for the remaining collision depths15,16.

It does not refute the joint-endpoint criterion or SD1: its support
has five indices, and its second endpoint fails. It does refute
discarding the second endpoint or trying to use a general
two-recycled-root impossibility theorem in positive characteristic.

All earlier frozen packets remain unchanged and unpromoted.
Only root may promote a scoped conclusion after the required audits.

