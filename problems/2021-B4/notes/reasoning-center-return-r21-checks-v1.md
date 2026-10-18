# Hand checks for R21

Candidate proof - unverified. These are constructor checks, not OTHER
review. No mathematical program or certificate replay was used.

1. The degree index is j in D_j=H_(20-j)/binom(20,j). Thus the r rows
   H13/H6/H4/H2 are D7/D14/D16/D18. The seven center degrees are
   3,6,11,12,13,15,17, not the same derivative orders.
2. D3(1)=-2+3a2+a3 and a2=0 gives a3=2. D6(1)=-5+20a3+6a5+a6,
   with a2=a4=0, gives a6=-35-6a5. D5 and D7 then give the main's
   exact formulas without deleting a5.
3. At2 all A_j are integral by their actual monic witness equations.
   Scaling the center gives A3=2h^3 and A6=-35h^6-6hA5, hence the
   residues b3=0,b6=hbar. Neither rational19-integrality alone nor
   an arbitrary dyadic unit supplied this induction.
4. Binary20 permits0,4,16,20; a4=a20=0 leaves Z20+b16Z4. F(1)=0
   fixes b16=1. D16(R)=0 then forces Rbar=1. Binary18 permits
   0,2,16,18; a2=0 gives b18=0 at Rbar=1.
5. If h,S both reduce0 the exact six linear factors force at least
   five zero factors after reduction, while Z4(Z-1)16 has only four.
   The degree14 carrier is integral by monic division, so its factors
   cannot remove a zero factor by a denominator.
6. In the chosen formal branch h=R=1,S=0, support(L) contains exactly
   10 indices, of which b0,b1 and b16,b17 are required by normalization
   and the top/lower rows. This is ONE manually specified vector.
7. For degrees1,...,10 the permitted binary coefficient indices are:
   1:{0,1};2:{0,2};3:{0,1,2,3};4:{0,4};5:{0,1,4,5};
   6:{0,2,4,6};7:{0,...,7};8:{0,8};9:{0,1,8,9};
   10:{0,2,8,10}. Their intersection with(L) gives each displayed E_j.
8. For11,...,20 they are:
   11:{0,1,2,3,8,9,10,11};12:{0,4,8,12};
   13:{0,1,4,5,8,9,12,13};14:{0,2,4,6,8,10,12,14};
   15:{0,...,15};16:{0,16};17:{0,1,16,17};
   18:{0,2,16,18};19:{0,1,2,3,16,17,18,19};
   20:{0,4,16,20}. Again intersection gives every displayed row.
9. Each chosen0 row has no constant term. Every chosen1 row has an
   even number of terms; counts are2,2,2,4,2,2,4,4,8,2,4,2 for
   j1,3,6,7,11,12,13,14,15,16,17,18 respectively.
10. E19=Z2(Z+1)(Z16+1). At S=0 it vanishes; E20 has multiplicities
    4/16 at0/1. The reduced rational linear factors give Z4(Z-1)2,
    leaving (Z-1)14, degree14. No global splitting assertion follows.
11. The main's identity(N) has odd coefficients only at its constant,
    a8 and a12. It becomes1+b8+b12=0, satisfied by0/1. The
    first-break H8 nonzero condition has no demand for a nonzero
    residue at2; E12(R)=0 is not a counterexample to that condition.
12. For the exact D5 fork, q(r),q(s) are19-units because q has
    constant20. Both r+s and r-s have19-depth1 as s/r=2mod19.
    The difference quotient's three homogeneous parts have depths1,
    at least3 and at least4, so its first term cannot cancel.
13. If a5=0 then D5=X2q with q0=20, so the gcd with the actual
    double origin is X2. If the witness is r/s then D5'=5D4;
    D4(w)=8w-4w3+w4 has depth1, making the witness simple.
    The carrier degree14 exceeds5, excluding any other common factor.
14. In residue branch h=R=1,S=0, G0 is a unit and the coefficient
    of Z2 is exactly R h S2 G0, with positive sign. Its valuation
    gives v2(A18)=2v2(S)-1. b18=0 allows this; it does not contradict it.

The checks establish only the exact limited assertions described in the
candidate. The actual system(A)--(E),(T) is unresolved. No actual CA
polynomial, no lift, no sign bound and no new annual result is checked.
