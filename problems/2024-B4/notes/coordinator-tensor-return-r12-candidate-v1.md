# Exact tensor counts for two root groups and the exponent6721

19 October2026, Brisbane. **Candidate proof - unverified.** Root is the
NEW constructor and is EXCLUDED from the TWO required OTHER initially
blind ENTIRE WHOLE audits. C's unverified FR11 translation perspective
was the conceptual trigger; conservatively C is also excluded from
these two audits. A/B are the intended OTHER reviewers after their
separate FR11 initials. Neither has supplied a NEW tensor inference.
Requested inherited gpt-6.1-sol/max; independent effective readback
unavailable. This concerns **2024 B4(b) only**, not preliminary(a).

The root quadruples in the accepted intersection budget have additional
algebraic structure when the root group is a product of two coprime-degree
subfield groups. Their additive structure is the elementary matrix-rank
geometry underlying the classical bilinear-forms association scheme.
Counting rank-one and rank-two decompositions gives exact values where a
size-only estimate loses most information. The proposed consequence is
whole absolute irreducibility in an explicit infinite family including
n6721. No general annual classification, priority or new-method claim.

## 0. Exact domain, definitions and operative accepted input

Let K be an algebraic closure of F2. For odd s let H_s=mu_s in K and
let M_s count ordered pairs (x,y) such that x,y,z=1+x+y,1 are FOUR
DISTINCT elements of H_s. This is EXACTLY the normalized off-diagonal
point count in accepted FR10, not a count modulo permutations/scalings
or an unnormalized quadruple count.

Use the established polynomial quotient

    phi_n=(X^n+Y^n+Z^n+(X+Y+Z)^n)/[(X+Y)(Y+Z)(Z+X)].

Its existence is an accepted preliminary fact, not reproduced. The sole
operative geometric import is COMPLETE accepted FR10,27940 bytes SHA256
ce9a3c9e00ce931716fe00d6ea0a605167ddf58a29779d459a62cbc9dd04d173,
and EACH current acceptance MDJSON. All were freshly read in full.
One combined display clipped the first attempt; the COMPLETE accepted
body was separately re-read before using it. Root was one of FR10's
OTHER whole auditors; that old role is not a fresh independent
self-certification of its geometric inputs.

In the domain n=ell*q+1,ell>=3 odd,q=2^i,i>=2,d=gcd(ell,q-1),
N=ell*q-2, FR10 gives reducedness and EVERY-component degree at leastq.
If the WHOLE phi_n were absolutely reducible, its ACTUAL least component
and FULL actual coprime complementary product would satisfy

    q(N-q) <= e(N-e)
       <= (q-2)^2/4+3(d-1)q^2/4
                            +q*M_ell+q(q-2)*M_d/4.        (I)

The SAME pair is used throughout. Every central, diagonal, ordinary,
nonordinary and infinity contribution is already included in (I).
No common-center, equal-degree, F2-definition, formal grouping or
irreducible-complement hypothesis is added. Both count coefficients
are nonnegative. The NEW contribution below is the exact finite count
inserted into this ACCEPTED actual budget.

FR11 remains unverified and is NOT a proof premise. Its elementary
translation view suggested retaining the actual root count. The new
finite-field tensor isomorphism, rank decomposition counts, exact
M21/M105 and q64 inclusion are constructed here by root. For maximum
review independence both root and C are excluded from the two NEW audits.
No FR11 NEW peer report/finding/actual inventory/open/hash/meta was read.

## Proposed TR12A--TR12D

**TR12A.** Let a,b>=2 be coprime INTEGERS, r=2^a-1,s=2^b-1 and
ell=rs. Then H_ell is additively identified with the set of nonzero
rank-one tensors in F_(2^a) tensor_(F2) F_(2^b). Put A=r+s-2.
For every nonzero rank-one tensor t, the number of x in H_ell with
x+t in H_ell is EXACTLY A. For every rank-two t it is EXACTLY6.
These counts are of elements x, equivalently ORDERED decompositions
t=x+(x+t), not unordered decompositions.

**TR12B.** In that domain the normalized quadruple count is EXACTLY

    M_ell=A(A-2)+4(ell-1-A)
          =r^2+s^2+6rs-10r-10s+12.                    (1)

In particular M21=96 and M105=696. Both equalities hold in the algebraic
closure root group, independently of the later Frobenius parameter q.

**TR12C.** For EVERY integer t>=0, the WHOLE polynomial phi_n is
absolutely irreducible for

    q=2^(12t+6), ell=105, n=105q+1.                    (2)

The endpoint t0 is n6721. These are sufficient exclusions of the official
two nonconstant coefficientwise factors. No function-value substitution
or one-distinguished-component conclusion is used.

**TR12D, limitation.** The exact same actual-budget substitution at
ell21,q=2^(6t),t>=1 has negative gap; it still decides neither outcome
there. No converse for a failed intersection-budget test, unrestricted
classification or earlier-publication nonoverlap is asserted.

## 1. Coprime subfields give an actual additive tensor model

Write E=F_(2^a),F=F_(2^b) inside K. Recall the elementary finite-field
description: F_(2^m) is the set of roots of X^(2^m)-X; it has2^m
distinct elements and is a field. Frobenius squaring permutes it.
The intersection E intersect F is F2 because an element fixed by both
Frobenius powers a,b is fixed by their gcd1. Indeed use integer Bezout
on the two automorphisms, including their inverses on the finite field
generated by the element. Thus E* intersect F*={1}.

For completeness the multiplication map

    E tensor_(F2) F -> EF, u tensor v -> uv              (3)

is injective as well as surjective, not merely multiplicatively
injective on pairs. Choose alpha generating E over F2. Such an element
can for example generate the cyclic multiplicative group E*: a finite
subgroup of a field's multiplicative group is cyclic, by the elementary
root-count argument given below. Its minimal polynomial has Frobenius
orbit alpha,alpha²,...,alpha^(2^(a-1)), of length a. Over F the Frobenius
power is2^b, and its orbit has length a because a divides bk exactly
when a divides k. Therefore alpha still has degree a over F. Hence
1,alpha,...,alpha^(a-1) are F-linearly independent and span F(alpha).
The tensor multiplication map in these bases is an isomorphism of
F-vector spaces. Its target has2^(ab) elements. This proves (3) directly;
no coprime-degree assertion is applied to a noncoprime case.

Here the cyclic-group fact needs no unproved generator assumption.
For a finite subgroup G of a field*, let e be the least common multiple
of element orders. In an abelian group, commuting primary-order parts
of suitable elements give an element of order e: for each prime-power
in e take the corresponding maximal primary part, then multiply them.
Every element of G is a root of X^e-1, so |G|<=e. Conversely all
element orders divide |G| by Lagrange, so e<=|G|. Thus e=|G| and
the constructed element generates G. The ordinary field root-count
bound is valid here; all multiplicative group orders are odd.

Euclidean reduction of exponents gives gcd(2^a-1,2^b-1)=2^gcd(a,b)-1=1.
For example, subtract multiples using
2^u-1 = 2^(u-v)(2^v-1)+(2^(u-v)-1) when u>=v;
iteration is the integer Euclidean algorithm. Therefore E*F* is a
subgroup of K* of size rs=ell, with unique expression uv. Every such
product has ell-th power1. Since ell is odd, X^ell-1 has ell distinct
roots, so E*F*=H_ell. Under (3) this group is exactly the set of
nonzero decomposable, or rank-one, tensors. Over F2 a nonzero rank-one
tensor has a UNIQUE pair of nonzero factors: the only nonzero scalar
available for rescaling is1. This agrees with the multiplicative
uniqueness, but the ADDITIVE isomorphism (3) was separately essential.

## 2. The two exact rank counts

For finite-dimensional F2-spaces U,V of dimensions a,b, identify
U tensor V with linear maps V*->U. Tensor rank here is ordinary MATRIX
rank, independent of chosen bases. Let H be the nonzero rank-one
tensors. They number (2^a-1)(2^b-1)=ell. Define

    rho(t)=#{x in H:x+t in H}.

Fix a nonzero rank-one t=u tensor v. If x=u tensor w with
w!=0,v, then x+t=u tensor(w+v) is nonzero rank1. This gives
2^b-2=s-1 choices. If x=w tensor v with w!=0,u, this gives
2^a-2=r-1 choices. These two sets are DISJOINT: sharing BOTH factors
would give x=t and x+t=0, which is excluded.

There are no other choices. If x=u' tensor v' shares neither factor
with t, then u,u' are independent and v,v' are independent over F2.
Applying linear functionals that distinguish v,v' shows that x+t has
image span{u,u'} and rank2, not rank1. Conversely, rank at most1 of
their sum forces one of those two dependencies; over F2 dependency
of nonzero vectors means equality. Thus

    rho(t)=(s-1)+(r-1)=A.                              (4)

Now suppose t has rank2. If t=x+y with x,y nonzero rank1, their image
vectors u1,u2 must be independent and span Im(t), a two-dimensional
space; their two covectors must also be independent. Choose ANY ordered
basis (u1,u2) of Im(t). There are (4-1)(4-2)=6 such bases. Expanding
the map t uniquely in that basis gives covectors v1,v2 with
t=u1 tensor v1+u2 tensor v2. Rank2 makes v1,v2 nonzero/independent,
so this is a valid ordered pair of rank-one tensors. Conversely every
ordered decomposition gives exactly this ordered basis, since factors
are unique over F2. Therefore

    rho(t)=6 when rank(t)=2.                           (5)

No division by two or orbit-size factor is inserted. If rank(t)>2,
there is no such two-summand representation, but that case is not
needed for t=1+x with x rank1. Equations(4)--(5) are the elementary
small-rank intersection numbers in the classical bilinear-forms scheme;
they are proved here in full rather than imported from an unread paper.

## 3. Recover the EXACT normalized root quadruple count

Under (3), the field element1 is the rank-one tensor1 tensor1. For
each x in H except1, t=1+x is nonzero of rank1 or2. Exactly A such
x give rank1, by (4) with t=1. The other ell-1-A give rank2.

For this fixed x, the possible y,z=t+y in H number rho(t). Exactly
two violate distinctness of x,y,z,1: y1 and y=x. In characteristic2,
y=z would force t0, which cannot happen. Also z1 is equivalent to
y=x, and z=x to y1. Thus no other collision is omitted. The count
of VALID y is rho(t)-2. Summing over the two ranks yields

    M_ell=A(A-2)+(ell-1-A)(6-2).

This proves(1), counting ordered x,y once each; z is determined and
the fourth entry is FIXED1. The remaining count ell-1-A=(r-1)(s-1)
is nonnegative. At a,b>=2,r,s>=3 all displayed term counts are valid.
The expanded formula follows by ordinary integer algebra; counts are
not field elements and no inequality divides inside K.

For (a,b)=(2,3), (r,s)=(3,7),ell21,A8:

    M21=8*6+(21-1-8)*4=48+48=96.

For (a,b)=(3,4), (r,s)=(7,15),ell105,A20:

    M105=20*18+(105-1-20)*4=360+336=696.

Both pairs of degrees are coprime, so all tensor hypotheses really hold.
These are exact counts in H21 subset F64 and H105 subset F4096,
respectively. The ambient field for counting H105 need NOT be the later
F_q used to locate ordinary points. The ordinary count uses H_d;
FR10's normalized fixed-field argument already establishes that domain.

## 4. Insert EXACT counts in the SAME actual component budget

Take q=2^(12t+6),ell105,t integer>=0. The orders of2 modulo3,5,7
are2,4,3 respectively. The exponent is divisible by6 and congruent2
mod4, so 3 and7 divide q-1, while5 does not. Since105=3*5*7,
d=gcd(105,q-1)=21 EXACTLY, and q>=64. The number n=105q+1 is odd;
q is the maximal two-power in n-1 because105 is odd. The binary
weight of n is five, so all accepted FR10 geometric hypotheses hold.

Put M_ell=696 and M_d=96 into(I). Its actual upper expression is

    B=(q-2)^2/4+60q^2/4+696q+96q(q-2)/4
      =(157/4)q^2+647q+1.                              (6)

The least-component lower expression is
q(N-q)=104q^2-2q. Subtracting gives

    4[q(N-q)-B]=259q^2-2596q-4.                       (7)

For every real q>=16, 259q-2596>=1548>0, so(7) is at least
16*1548-4=24764>0. In particular this holds for ALL the actual q>=64
in(2). Inequality(I) is impossible. Reducedness also excludes a power
of only one absolute component. Consequently the WHOLE phi_n is
absolutely irreducible. This proves TR12C including t0,n6721.

The first endpoint can be checked entirely by hand within this proof:
q64,N6718,q(N-q)=425856 and B202177. The gap is223679, whose fourfold
value894716 agrees with(7). These integer substitutions are illustrative
arithmetic, not a CAS factorization, scan or finite-certificate premise
for the infinite statement. The uniform positivity argument already
covers every t.

An official product would reduce coefficientwise to phi_n=gbar*hbar
in F2[X,Y,Z], by cancellation of the nonzero prescribed linear product
in this integral domain. Both reductions have positive degree. Whole
absolute irreducibility rules this out even for nonhomogeneous initial
gbar,hbar. Merely finding one F2-defined absolute component or comparing
polynomial functions on F2^3 would not prove this conclusion.

For comparison only, the OLD accepted FR10 size-bound gap on the SAME
parameters is -5q²-41716q-4<0 for every q. The unverified FR11 author
test is31q²-40972q-4; at q64 it is126976-2622208-4<0 and its claimed
family begins at t1. These are literal comparisons of displayed
sufficient tests, not a declaration that no older theorem or paper
could decide n6721. FR11 is not needed as a proof premise or accepted
because it was consulted as an idea source. Its author bytes and both
NEW peer-review embargoes are preserved.

## 5. Limitation and failed directions

At ell21,q=2^(6t),t>=1, d21 and M_ell=M_d=96. Applying exactly the
same budget algebra gives

    (84-63-2-96)q²-[4+4*96-2*96]q-4
       =-77q²-196q-4<0.                               (8)

This proves only that this sufficient contradiction is unavailable.
It proves neither reducibility nor irreducibility and supplies no
unrestricted converse. It establishes TR12D in its negative scope.

Other failed routes must not be silently used:

* Multiplicative uniqueness of uv alone does not make the field product
  an ADDITIVE tensor isomorphism. Coprime field degrees and the orbit
  argument in Section1 are indispensable.
* If gcd(a,b)>1, the F2 tensor multiplication has a nontrivial kernel
  and the subfield factors can rescale by a larger intersection field.
  The displayed rank-one counts cannot simply be reused. No theorem
  for that domain is asserted.
* Over a larger base field, nonzero factors have extra scalar
  representations. The exact6 is specific to F2. No q-ary count is
  inferred by replacing2 with a variable.
* The normalized fourth point is1. Unnormalized zero-sum quadruples or
  unordered four-sets have different multiplicities; none is inserted
  into the actual intersection budget.
* Replacing a WHOLE irreducibility conclusion by the general published
  exceptional-APN component theorem would leave the official inference
  unproved. The actual least-component contradiction is retained.

## 6. ALL48 constructor obligations and hand checks

These are constructor dispositions, NOT independent review. TWO OTHER
ENTIRE whole auditors must reconstruct EVERY row and all companion data.

| ID | Required inference and constructor hand check |
|---|---|
| TR12-O01 | Exact official positive odd n/coefficientwise target and only open(b); checked primary57--74/local statement. |
| TR12-O02 | Quotient and actual least-component budget imported only from complete accepted FR10/current MDJSON. |
| TR12-O03 | Old root FR10 role and C conceptual trigger disclosed; both excluded from NEW audit count. |
| TR12-O04 | FR11 remains unverified/context, no theorem from it is a proof premise or peer review accessed. |
| TR12-O05 | a,b integers>=2 and gcd1 are explicit; r,s,ell positive odd with no hidden endpoint. |
| TR12-O06 | Finite subfields in K and their intersection F2 derived via Frobenius/gcd. |
| TR12-O07 | Cyclicity needed to choose alpha is justified by elementary exponent/root counting, not a generator assumption. |
| TR12-O08 | Alpha's Frobenius2^b orbit has full length a because gcd(a,b)=1. |
| TR12-O09 | Degree a over F gives the actual ADDITIVE tensor multiplication isomorphism. |
| TR12-O10 | Gcd(2^a-1,2^b-1)=1 established by integer exponent Euclidean reduction. |
| TR12-O11 | E*F* has sizeell, is a subgroup and equals the complete odd root groupmu_ell. |
| TR12-O12 | Under the isomorphism, H is exactly all nonzero rank-one tensors, not a subset. |
| TR12-O13 | Rank-one factorization is unique over F2, excluding scalar multiplicity errors. |
| TR12-O14 | Tensor rank is ordinary matrix rank as a map V*->U, basis independent. |
| TR12-O15 | For rank-one t, same-left choices total2^b-2=s-1 and remain nonzero. |
| TR12-O16 | Same-right choices total2^a-2=r-1 and remain nonzero. |
| TR12-O17 | The two valid rank-one choice sets are disjoint; their putative overlap would give x=t,y0. |
| TR12-O18 | Two independent factor pairs force rank2 by separating functionals; no other rank-one sums occur. |
| TR12-O19 | Exact rank-one translation count is A=r+s-2, counting elements/ordered decompositions. |
| TR12-O20 | For rank2 t every two-rank-one decomposition has image factors a basis of Im(t). |
| TR12-O21 | Every ordered image basis determines a UNIQUE pair of covectors/decomposition. |
| TR12-O22 | Covectors are nonzero and independent because t has rank2, so all6 decompositions are valid. |
| TR12-O23 | A2-dimensional F2 image has(4-1)(4-2)=6 ordered bases; no unordered division. |
| TR12-O24 | Fourth root1 corresponds to rank-one tensor1 tensor1 under the same additive map. |
| TR12-O25 | For xH except1, t1+x is nonzero rank1/2; exactly A have rank1. |
| TR12-O26 | Remainingell-1-A=(r-1)(s-1) choices have rank2, with no higher rank. |
| TR12-O27 | For each x, exactly y1,x violate four-distinctness; all z collisions enumerated, y=z impossible. |
| TR12-O28 | Summing rho(t)-2 gives EXACT M with fixed fourth1 and ordered x,y, no orbit factor. |
| TR12-O29 | Expanded polynomial formula follows by ordinary integer algebra. |
| TR12-O30 | Degree pair2,3 is coprime and gives r3,s7,A8,M21=96 by hand. |
| TR12-O31 | Degree pair3,4 is coprime and gives r7,s15,A20,M105=696 by hand. |
| TR12-O32 | Counts belong to full root groups in K, not a falsely restricted later F_q model. |
| TR12-O33 | Orders of2 modulo3,5,7 give exactly d21 for every exponent12t+6,t>=0. |
| TR12-O34 | q>=64,maximal two-part,ell105odd,binaryweight5 check every FR10 domain hypothesis. |
| TR12-O35 | SAME actual least component/FULL complement retains degree product lower bound. |
| TR12-O36 | Substitution preserves every center/diagonal/ordinary/nonordinary/infinity term of accepted(I). |
| TR12-O37 | Exact B=(157/4)q²+647q+1 obtained with M105696/M2196, signs correct. |
| TR12-O38 | Fourfold actual gap is259q²-2596q-4, with lower term104q²-2q. |
| TR12-O39 | Uniform positivity at every realq>=16 covers ALL actualq>=64, not a finite test. |
| TR12-O40 | Reducedness plus impossible actual coprime split gives WHOLE absolute irreducibility, not one component. |
| TR12-O41 | Endpointt0 hasq64,n6721,N6718 and illustrative exact positive gap223679. |
| TR12-O42 | Official integer product reduces/cancels to two positive-degree polynomial factors, even if nonhomogeneous. |
| TR12-O43 | Old FR10 gap is strictly negative on this family; comparison is only between stated sufficient tests. |
| TR12-O44 | Unverified FR11 q64 test negative/claimedt>=1 scope comparison supplies no proof premise or novelty claim. |
| TR12-O45 | ell21 surviving sector gives exact negativegap-77q²-196q-4 and decides neither outcome. |
| TR12-O46 | Noncoprime degrees/larger base/unnormalized counts are excluded, and all failure directions preserved. |
| TR12-O47 | Literal primary read limits, inaccessible originals/overlap and classical rank-metric attribution retained. |
| TR12-O48 | Complete issues/sources/worklog/code/ALLmetadata and TWO OTHER whole-audit boundary; no mathcode/annual/priority claim. |

## 7. Issue ledger, source limits and worklog

Known issues at this checkpoint:

1. OPEN independent audit: all four claims and ALL48 steps require TWO
   OTHER whole reviews. Root cannot accept its own construction merely
   because earlier geometric inputs were reviewed.
2. OPEN annual target: neither this family nor the failed ell21 budget
   decides arbitrary n or every remaining component configuration.
3. OPEN publication overlap: rank-one/rank-two matrix geometry is
   classical. The exact root-group application and n6721 may have earlier
   formulations. A failed exact-name search is not evidence of novelty.
4. Closed before freeze: a first exploratory norm-torus derivation for
   M21 was superseded by one unified tensor argument proving BOTH counts.
   No incomplete norm-torus claim is used as a premise or claimed audited.
5. Closed by scope: C's FR11 supplied the conceptual translation trigger;
   no unverified FR11 theorem is imported. C and root are both excluded
   conservatively from the two new audit slots.

Literal fresh mathematical/local reads: COMPLETE accepted FR10 body
27940B and EACH complete current authority MDJSON; complete2024 local
statement. Earlier root complete FR10 author/BOTH-review reconciliation
and R6/R9/Fulton operative proofs are historical, not fresh full source
replays for this packet. The present new proof imports the exact reviewed
FR10 actual-budget theorem, not an abstract or an unread local theorem.
FR11 UNVERIFIED author main14297B/freeze3460B were read as idea/context
only; its companions were not all freshly read or required as premises.
No corresponding NEW FR11 peer finding or actual file was accessed.

Fresh official public2024 PaperB p2, setup57--63/(b)68--74:
<https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf>.
The earlier guessed paper URL was inaccessible; the actual local
statement's verified URL was then opened. Preliminary(a) not investigated.

Primary background: Ph.Delsarte, Bilinear forms over a finite field,
with applications to coding theory, JCTA25(3)(1978),226--241,
<https://doi.org/10.1016/0097-3165(78)90015-8>.
The primary publisher SEARCH result supplied bibliographic data and
abstract describing the rank-difference association scheme. A direct
open returned403; the operative article body was NOT read and no
intersection-number theorem from it is imported. Section2 supplies
all needed small-rank counts directly. A guessed author graph page was
also inaccessible. This is classical-context attribution, not a claim
to have audited Delsarte's whole proof or established first publication.

Fresh primary Hernando--McGuire arXiv0903.2016 landing/version4 metadata
and abstract were read, <https://arxiv.org/abs/0903.2016>. Earlier
operative local/count excerpts are historical, retained through FR10.
No new whole HM proof audit or general WHOLE-irreducibility inference
from its exceptional-APN classification is claimed. Original Jedlicka/
Ferard operative bodies remain unread; overlap remains open. Searches
for literal6721/APN/irreducible and root-count terms yielded no usable
direct exclusion source; some unrestricted matches concerned unrelated
property identifiers and were discarded. No absence/priority conclusion.

Worklog: after AR/CI12 integration, root read the frozen FR11 author
main. The translation count suggested viewing products of independent
subfields as rank-one tensors. Root first derived M21 by a prospective
norm argument, then replaced that route with the complete unified
rank argument, deriving M21=96,M105=696 and the strictly positive q64
actual budget by hand. All hypotheses, ordered multiplicities and the
ordinary H_d/total H_ell distinction were checked. Primary/context
searches and exact accepted/official reads above were completed. A narrow
new-prefix check returned unused. This COMPLETE main embeds significance,
proof, ALL48 constructor checks, issues, failed routes, source MD and
worklog; source JSON plus documentary admin/baseline/freeze complete
the compact ENTIRE5 author packet. Every final payload and generated
metadata must receive FULL model readback before freeze, then the full
manifest must be read and a SEPARATE read-only verification passed.
Actual completion identities are supplied later, never invented here.

No mathematical program, factor scan, CAS, routine test, source/author
routine, old certificate/freezer replay or native mathematical child
was used. All arithmetic and rank reasoning above is by hand. The NEW
documentary checker only preserves byte identities/JSON/literal labels.
No paper binary was downloaded or uploaded this pass; no purchase,
contact, access bypass, default merge or unrelated mutation. Root owns
integration and will save the explicitly UNVERIFIED packet to GitHub.
The latest observed weekly quota is63%TOTAL/reset1792874445,90%TOTAL
ceiling with review/integration reserve; effective model settings remain
unreadable. Research continues on all unresolved annual targets.
