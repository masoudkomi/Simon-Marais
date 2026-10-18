# A prospective two-parameter tensor family

18 October2026UTC. **Candidate reasoning — UNVERIFIED, not an accepted
corollary.** Root sole constructor of this NEW exploration. The tensor
count in the separate frozen TR12 candidate is under TWO OTHER blind
audits and is NOT yet an accepted mathematical premise. This note
records a further hand deduction to preserve it during those audits;
it cannot be promoted together with TR12 without its own full review.
C's earlier FR11 served as a conceptual trigger; conservatively exclude
root/C from future OTHER audits of the tensor extension. No NEW TR12
peer findings/files/actual inventories/hashes/metadata were accessed.

## Why pursue this family?

The 2024 factorization question connects finite-field additive quadruples
to local curve intersections. TR12 proposes an exact count by identifying
the root group with nonzero rank-one tensors from linearly disjoint
binary finite fields. Instead of applying that count only at105 and21,
one can choose two consecutive field degrees so BOTH groups in the same
actual intersection budget have tensor descriptions. This may extend
the irreducibility result while preserving its precise geometric input.
No annual classification, converse or publication priority follows.

## Hand deduction, conditional on the fully stated TR12 count

Let a>=3 be ODD and t>=0. Write

    r=2^a-1, s=2^(a+1)-1=2r+1,
    ell=r*s, i=a*((a+1)*t+2), q=2^i, n=ell*q+1.

The gcd of the consecutive degrees a,a+1 is1, so r,s are coprime.
Since a is odd, gcd(i,a+1)=gcd(2a,a+1)=2, while a divides i.
The elementary Euclidean identity

    gcd(2^u-1,2^v-1)=2^gcd(u,v)-1

then yields

    d=gcd(ell,q-1)=r*3.

For completeness, the identity follows by reducing2^u-1 modulo2^v-1
to2^(u mod v)-1 and iterating Euclid on the exponents. The product
formula for d is valid because r and s are COPRIME. Also r is1mod3
when a is odd, so the two factors3,r of d are coprime. No primality
of r or s is assumed. Both root groups admit linearly disjoint
tensor descriptions: degrees(a,a+1) for ell, and(2,a) for d.

The precise proposed TR12 lemma, not yet accepted, states that for
coprime field degrees u,v>=2 and R=2^u-1,S=2^v-1,

    M_(RS)=R²+S²+6RS-10R-10S+12,

where M counts ORDERED pairs (x,y) with1,x,y,1+x+y four DISTINCT
members of mu_(RS) in the algebraic closure of F2. It is not a count
of unordered sets or arbitrary tensors of every rank. Its proof and
field-embedding hypotheses are in the COMPLETE frozen TR12 submission,
which is undergoing independent reconstruction.

Substituting the two valid coprime degree pairs gives, conditionally,

    M_ell=17r²-20r+3,
    M_d=r²+8r-9.

These expansions are by hand: with S=2r+1 the square/cross terms total
17r²+10r+1, then the linear subtraction gives-30r-10 and constant12.
With R3 the terms become9+r²+18r-30-10r+12.

Accepted FR10 supplies the actual least-component/full-complement
inequality for ell>=3 odd,q>=4, including reducedness, EVERY-component
degree>=q and all center/diagonal/off-diagonal/infinity costs:

    q((ell-1)q-2) <= e(ell*q-2-e)
        <= (q-2)²/4+3(d-1)q²/4+q*M_ell+q(q-2)*M_d/4.

Do not substitute the numerical counts into a merely formal component
assignment. They strengthen this SAME ACTUAL pair's upper bound.
Multiplying the resulting gap by4 gives

    P_T=(7r²-13r+7)q²-(66r²-96r+34)q-4.       (1)

Indeed4ell-3d-2-M_d=8r²+4r-9r-2-r²-8r+9,
and4+4M_ell-2M_d=4+68r²-80r+12-2r²-16r+18.
No mathematical program generated these coefficients.

For r>=7 define A=7r²-13r+7 and B=66r²-96r+34.
A>0 (for example7r²-13r>=r(49-13)>0). Moreover

    16A-B=46r²-112r+78
          =46r(r-3)+26r+78 >0  for r>=7.

Thus for EVERY q>=16,

    Aq-B >=16A-B >=46*7*4+26*7+78=1548,
    P_T=q(Aq-B)-4 >=16*1548-4>0.

The actual family has i>=2a>=6, so q>=64. Conditional on the exact
tensor count, the accepted same-pair FR10 interface would therefore
prove WHOLE absolute irreducibility for every a>=3 odd,t>=0.
The official coefficientwise product is excluded by canceling the
nonzero prescribed R in the polynomial integral domain, as in FR10.

For comparison, the old crude-count positive test has leading coefficient

    4ell-d²+d-5=-r²+7r-5 <0  for r>=7.

Its subtracted q coefficient is

    C=4(ell-2)²-2(3r-1)(3r-3)>0.

A transparent bound uses ell-2=2r²+r-2>=2r² and
2(3r-1)(3r-3)<18r², giving C>16r4-18r²>0.
Thus the old P is strictly negative at every family member. This is
only a comparison with that EXACT test, not all prior papers. At a3,
r7,ell105,i12t+6,(1) becomes259q²-2596q-4, recovering the already
submitted TR12 family including q64/n6721. For a>=5 it proposes further
odd parts; no sample, search or extrapolation establishes the theorem.

## Limits and required next work

This exploration depends on the UNVERIFIED general tensor count. It must
remain unverified until TR12 is accepted in that exact scope, followed
by an independently frozen complete NEW statement/proof/obligation/source
packet and TWO OTHER initially blind WHOLE reviews of this extension.
Do not amend frozen TR12 to insert it. No peer review of this extension
has occurred and no conclusion is yet promoted or included in a status
count as a solved case.

Searches18Oct2026UTC for Férard2017, Jedlicka/105/6721 and literal APN6721
returned the2014 publisher abstract and unrelated parcel identifiers.
Those unrelated results were discarded. The2014 primary abstract concerns
t5mod8, whereas this proposed family is1mod64, but its full operative
body and original2017/Jedlicka proofs remain unread here. No absence,
nonoverlap, novelty or source theorem is inferred from these searches.
Primary discovery URL: https://www.aimsciences.org/article/doi/10.3934/amc.2014.8.497 .

No mathematical Python/CAS, finite-field enumeration, factor scan,
routine test, paid source, contact, bypass, download or third-party
redistribution occurred. Literature overlap and the full annual target
remain open. Root continues its separate initially blind RC10 whole2
audit without accessing the corresponding NEW peer materials.
