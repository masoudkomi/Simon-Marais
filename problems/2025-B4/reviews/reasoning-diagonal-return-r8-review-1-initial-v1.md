# DR8 OTHER initially blind ENTIRE WHOLE review1

2026-10-18 UTC. Reviewer B, `/root/review_2022_complexity_r2`.
Requested inherited gpt-6.1-sol/max; independent effective-setting
readback unavailable. A is sole NEW constructor and excluded. Root
supplied the assignment, not a new proof inference. This initial report,
ALL64 ledger, issues, source MDJSON, worklog and ALL administrative files
are completed without corresponding NEW review2 findings, files, hashes,
metadata, filename inventory or commentary. Findings remain embargoed
until the coordinator explicitly confirms BOTH ENTIRE checkpoints.

## Whole disposition

I reconstructed the ENTIRE DR8A--DR8C proof and ALL64 obligations. No
substantive defect, counterexample in the stated domain or required
author repair was found. Eight closed scope notes are retained in the
issue ledger. This is one independent audit of an UNVERIFIED candidate,
not coordinator promotion or a complete annual solution.

Exact main: `problems/2025-B4/notes/reasoning-diagonal-return-r8-candidate-v1.md`,
15008bytes, SHA256
`2e793eb556b4a3063dbdde1cf0b16b7f9f53eec4e36469adf31693b022b19a47`.
Exact author freeze: `reasoning-diagonal-return-r8-freeze-v1.json`,
3635bytes, SHA256
`53ce3848114979fe2f882c7ef22ac3d97e4f79880a1abec92ddfcda4964d4323`.
Read ENTIRE14 author files, including ALL64 obligations, checks,
failures/issues, sources, worklog, code record, administrative source,
baseline, input validation, metadata and freeze. No author program or
old freezer was executed. The immutable parent for my own older packets
is the complete AU12-file freeze, separately bound in this review.

I previously constructed other2025 partials, including RD, and performed
the whole DR7 review2. These accepted older roles are disclosed, not
counted as new independent self-recertification. I did not construct
DR8 or supply an inference to its author. Freshly read the COMPLETE
accepted DR7 body/current MDJSON and its source/failure records. DR6/RD
current authorities and the complete PG body/acceptance were checked as
comparison only; no new full foundational Jacobi/Runge audit is claimed.

## 1. Official domain and the exact imported interface

The original2025 PaperB page2 setup/(b) agrees with the local statement.
The official degree is p-1 here, the term count and perfect-power
exponent are p. The candidate assumes p>=37 prime, ordinary |X|>=2,
Phi_p(X)=Y^p and ADDITIONALLY p|X(X+1). This does not cover every
official or diagonal solution. Boundary X0,+/-1 and small p are outside
its stated scope. I did not investigate preliminary(a).

Since p is odd, Phi_p(X)>1 for either signed base, so Y is positive
and >1. The imported DR7A supplies Y<|X|, depth s=h+1>=2,
v_p(Y-1)=h, and the actual full-prime-power partition c=g b. DR7D
supplies b>1. These are precisely the accepted p>=37 ordinary sector,
not an assumption about arbitrary p-adic representatives or the support
of a chosen formal cofactor. A prime congruent1modp can belong to g;
its ACTUAL order on Y, not its congruence class alone, defines b.

For the unique a0 in{0,-1}, set N=|X-a0|=c p^s=p b Q, Q=g p^h.
The other distance M is p-free and coprime to N. Writing U=|X|,
the four possibilities for (N,M) are

    X=N:       (U,U+1);       X=-N:     (U,U-1);
    X=N-1:     (U+1,U);       X=-N-1:   (U-1,U).

Thus M>=U-1 in every case. Since 1<Y<U are integers, U>=3 and
Y-1<=U-2, so M>Y-1 strictly. This is the key signed endpoint check.

## 2. Entire DR8A reconstruction: full powers and the other distance

Let K=(p-1)/2. Direct finite polynomial algebra gives

    (Y-1)Phi_p(Y)=Y^p-1=Phi_p(X)-1
       =X(X+1)H,    H=sum_(j=0)^(K-1)X^(2j)>0.

The right side equals |X(X+1)|H, including X<=-2. At the two selected
residues H is1 or K modulo p, hence p not dividing H. In the usual
cyclotomic factorization this is exactly

    H=product_(d|p-1,d>2)Phi_d(X).

For every non-p prime ell dividing the right side, Y is a unit with
Y^p=1 mod ell; the order is1 or p. In the order1 case Phi_p(Y)=p
mod ell is a unit, so ALL source ell-powers lie in Y-1. In the
order-p case Y-1 is a unit and ALL source powers lie in Phi_p(Y).
Prime2 necessarily belongs to the first case. This partitions full
powers of M into d0=gcd(M,Y-1) and e=M/d0, which are coprime.

Any order-p prime is odd and at least2p+1. If it divides X, H=1
mod ell; if it divides X+1, H=K mod ell and K<ell. In either
case its entire valuation in Phi_p(Y) is exactly its valuation in
the corresponding adjacent distance. Consequently b,e have disjoint
support and their whole powers can be divided out of Phi_p(Y).

At p, put z=Y-1 with v_p(z)>=1. The expansion

    Phi_p(1+z)=sum_(j=1)^p binom(p,j) z^(j-1)

has constant p. Its nonconstant intermediate coefficients contribute
at least p², and its final z^(p-1) also contributes p². Thus its
p-order is exactly1. Hence R=Phi_p(Y)/(p b e) is a positive p-free
integer. Since d0 is coprime to Q, Qd0 divides Y-1 and
T=(Y-1)/(Qd0) is a positive integer. Cancelling the exact identity
NM=p b Q d0 e yields H=T R.

The elementary identity gcd(Y-1,Phi_p(Y))=p, together with p not
dividing H, proves gcd(T,R)=1. If a prime of R also divided either
adjacent distance, it would be an order-p prime whose FULL valuation
was already consumed in b or e, since H is a unit there. This proves
gcd(R,X(X+1))=1. It does not assert that T is coprime to both distances.

The ordinary inequalities are also complete. From Qd0|Y-1,

    e=M/d0>=Q M/(Y-1)>Q.

For positive X=U, coefficient comparison gives
Phi_p(U)<(U+1)^(p-1); with alpha=(p-1)/p the strict increment
(U+1)^alpha-U^alpha<1 gives Y-1<U^alpha. For X=-U,
Phi_p(-U)=(U^p+1)/(U+1)<U^(p-1), giving the same strict bound.
No fractional real power of a negative number is used. Substitution
proves the sharper e bound. Finally

    b e=T |X(X+1)|/[p(Y-1)]
       >(U-1)U^(1/p)/p,

using T>=1 and |X(X+1)|>=U(U-1). The first inequality for e may
be equality; the subsequent ordinary bounds are strict as claimed.

## 3. Entire DR8B reconstruction: EVERY cyclotomic component

For d>2, primitive d-th roots are nonreal and occur in conjugate pairs.
Their factors at real X give Phi_d(X)>0. Each |X-zeta| is strictly
greater than U-1; equality in the reverse triangle inequality would
require zeta=+/-1 of the appropriate real sign. Those are not primitive
for d>2. Therefore

    Phi_d(X)>(U-1)^phi(d)>U>Y-1,

where phi(d)>=2 and (U-1)²>U for U>=3. This is an all-index argument,
not a list of small cyclotomic polynomials. It retains negative X.

At any order1 prime, the exponent of Y-1 in the full product identity
is at least that in EACH component. At an order-p prime it is zero.
Since p is absent from H, gcd(Phi_d(X),Y-1) therefore extracts the
ENTIRE order1 part of that component. Its quotient R_d is the entire
order-p part. Repeated primes shared by different unfiltered components
are handled by adding their valuations in the product. Thus
product T_d=T and product R_d=R. The strict component size forces
R_d>1 for EVERY d, even if T_d=1 or an unfiltered prime repeats.

If ell|R_d, its order on Y is p, so ell>=2p+1>p>d. It is a
unit on X because Phi_d(0)=1. Its X-order k divides d. Modulo ell,
Z^d-1 is separable because ell not dividing d; in its product over
Phi_j, j|d, the reduced factors have disjoint root sets. The root X
also belongs to Z^k-1, so one of its factors Phi_j with j|k must
be Phi_d. Hence d|k and k=d. This explicitly rules out small
index-prime anomalies, without Zsigmondy/BHV or a primitive-divisor
exception list.

Different d cannot share an R_d prime because a single residue X has
one exact multiplicative order. Also p not dividing H, and the order-p
primes of b,e were already proved H-units. Thus p,b,e,ALL R_d are
pairwise coprime. This is NOT asserted for the T_d or the full
cyclotomic values. Finally p,d,2 divide ell-1 with gcd(p,d)=1,
so p*lcm(2,d) divides ell-1. Positive full prime powers preserve
the residue1, giving the claimed congruence and lower bound for R_d.

## 4. Entire DR8C reconstruction and limitations

The index set has exactly tau(p-1)-2 elements: p-1 is even and
precisely1,2 were removed. Accepted b>1, proved e>Q>=p and every
R_d>1 supply tau(p-1) nontrivial pairwise-coprime factors of
Phi_p(Y)/p. Prime p occurs exactly once in Phi_p(Y), supplying the
additional prime. These are primes of Phi_p(Y), NOT primes of Y.
No claimed upper support bound can be inferred.

For each d, T_d<=Y-1<U^alpha and the root-distance lower bound give
R_d>(U-1)^phi(d)/U^alpha. The exact product of the T_d is the
SINGLE budget (Y-1)/(Qd0). Allowing every component an independent
full Y-1 budget would be weaker and not the stated exact identity.
Both adjacent distances contain different actual order-p primes because
b,e>1 and the distances are coprime. The excluded families are exactly
those contradicting these necessary conditions. Formal factors satisfying
them are neither claimed realized nor a counterexample to an actual
Diophantine obstruction. Large actual support remains unresolved.

## 5. Adversarial and source checks

I challenged the whole-power gcds, common unfiltered index primes,
the prime2 branch, p's exact valuation, both signs at both centres,
the U2 boundary, strict versus weak inequalities, every d at once,
root separability and the count target. These close on the frozen
text as detailed above and in ALL64 separate ledger entries. I found
no need for a reviewer repair, numerical testcase, scan or CAS.

Fresh original BMR introduction/Theorem1(H) and its immediate order
argument have positive x,y hypotheses. Fresh signed Bennett--Levin
Equation(1)/Proposition1/Theorem1 context retain their exceptions and
term-count convention. Fresh BBM2011 few-digit statements retain
their positive-base/common-divisor restrictions; its complete Lemma8
proof matches the elementary p-depth mechanism. These sources provide
attribution/context only here. No complete external computational,
Runge, logarithmic or Jacobi theorem proof is newly certified/imported.
The source record gives precise passages and retrieval limits.

The sole operative accepted theorem import is DR7A/DR7D in its exact
ordinary p>=37 sector. Source-led or old mathematical comparisons do
not silently add another premise. No annual classification, numerical
prime exclusion, priority or external validation follows from this audit.
Only the coordinator, after BOTH whole reports are released and fully
reconciled, can promote the exact scoped result.
