# Accepted cofactor-dominant-r4: exact coordinator scope

2026-10-18 UTC. **Proved, independently reviewed scoped partial result.**

Accepted scope: **R4A-R4E**, only the stated restricted exponent
family Q=2^s,s>=3, ell=Q-1,q=Q^k,k>=1, with N=ell*q-2,
A=(ell-2)(ell+1),p=ell-1 a POSITIVE ORDINARY INTEGER, not a prime.
The characteristic is2; the official target is coefficientwise
polynomial reducibility in2024 B4(b). All degree and strict size
hypotheses below are retained. This is a scoped partial result.

Using ONLY separately accepted CG1/CG2 and the UNSIMPLIFIED first
line of accepted section6(9), R4A proves EVERY actual proper reduced
factor of degree0<e<=N/2 has e<A whenever q>=2ell+7. It establishes
B=q+1-2ell e/A>0 and T=p(e-e^2/A)>0 BEFORE division. The accepted
reduced-product c-1 correction is necessary; no irreducible genus
formula is applied to a product. Neither CG3 nor cubic R3 is a premise.

If also N>=3A-2, actual grouping and the smaller complementary
degree give a UNIQUE absolute component G with degree>N/2. Its
cofactor H has e<A, including H=1, and degG>N-A. Coefficient
normalization proves G,H are F2-defined and EXACTLY invariant under
the four-form S4 action. Reducibility over F2 and over its algebraic
closure are equivalent in this regime; no such equivalence is asserted
outside it. In the reducible case H is nonconstant and is the ACTUAL
smaller cofactor to which the remaining argument is applied.

At the central point the selected tangent lines form free pairs,
so m is even. At each noncentral diagonal point, the projective
stabilizer gives a six-point orbit, and its TWO independent tangent
translations give local multiplicity divisible by4. Thus24|S and
8|(e-m), using S=3(e-m). Off-diagonal points have nonzero distinct
four-coordinate values, forcing trivial projective stabilizers and
24-point orbits; hence24|V. Multiplicity need only be constant WITHIN
each orbit. Therefore the SAME positive ordinary integer
D=(ell-3)e+2m-V is4-divisible and D>=4. Zero multiplicities and
H missing the central point are retained. D is not assigned to H=1.

The sign-correct comparison T/D-aD/A<=T/4-4a/A and a global REAL
quadratic maximum give the necessary reducibility bound
q<=pA/16+ell-1+4/p. Only its STRICT reverse proves whole absolute
irreducibility; equality and a failed sufficient test are undecided.
The first two size hypotheses hold for EVERY s>=3,k>=2. In particular
Q16 has threshold196+2/7<256 and gives WHOLE absolute irreducibility
for EVERY n=15*16^k+1,k>=2. The Q8 case recovers already accepted FS.
Every s>=3,k>=3 also follows symbolically. General s>=5,k2, k1,
other odd parts and the full annual classification remain unresolved.

Root is sole NEW constructor and is EXCLUDED. A R1 and C R2 are
TWO OTHER initially blind ENTIRE WHOLE audits, ALL48 obligations each.
Their entire reports/ALLledger/issues/source/log/code and ALLmetadata
froze10:00:00.531207 and10:04:34.916077UTC BEFORE corresponding NEW
peer findings/files/hashes/metadata were disclosed. Root read the
ENTIRE11-file author packet, BOTH COMPLETE reports/ALL96 ledger rows,
all issues/sources/logs/code and ALLmetadata and reconciled each
inference with the exact accepted CG authority. Both find zero
substantive defects or required mathematical repairs. A's seven
closed notes and C's no-advisory disposition preserve existing scope.

Classical multiplicity/intersection inputs remain attributed and their
characteristic2 limits retained. The recent Frobenius paper's property(A),
separability and strict exponent hypothesis are UNPROVED and UNUSED.
The HM proper-divisor COMPONENT theorem is UNUSED. Férard2017's
operative body remains UNREAD; priority and published overlap are
unestablished. Exact original-source reading limits accompany the
reviews. No mathematical program,CAS,scan,optimizer,certificate or
author/source rerun supplied a proof step. Historical bytes remain
unchanged. Integrity checks are administrative; internal review is
not external validation. No full annual or novelty claim is promoted.

The COMPLETE frozen mathematical submission follows as a byte-identical suffix. Its historical unverified label records submission status; this header and acceptance record state the current exact scope.

---

# A unique large component and the exact S4 cofactor obstruction

18 October 2026 UTC. **Candidate proof - unverified.** Root is sole
NEW constructor and is EXCLUDED from the independent reviewer count.
TWO OTHER initially blind ENTIRE WHOLE audits and complete coordinator
reconciliation are required. All deductions are hand reasoning.

## 0. Exact question, significance and proposed scope

Only official 2024 B4(b), reducibility over F2, is investigated. The
connection with APN power functions explains the existing literature
on an absolutely irreducible component. A component theorem alone
does not decide reducibility of the WHOLE polynomial. Here the proposed
reduction isolates a single large absolute component and a uniformly
bounded cofactor for a restricted infinite exponent family. The
cofactor's actual symmetries, rather than presumed transitivity on all
singular points, then strengthen the intersection obstruction. This
would settle one additional parameter family. It is not the general
annual classification, a new APN theorem, or an established novelty claim.

Let s>=3,k>=1 be integers and put

    Q=2^s, ell=Q-1, q=Q^k, n=ell*q+1,
    N=ell*q-2, A=(ell-2)(ell+1), p=ell-1, a=(ell+2)/p.

The symbol p in this note is the POSITIVE INTEGER ell-1, NOT a prime
or the field characteristic. Work over K=F2bar and set

    W=X+Y+Z, R=(X+Y)(Y+Z)(Z+X),
    f=X^n+Y^n+Z^n+W^n, phi=f/R.

The sole operative accepted input is CG1/CG2, precisely bound by
`../reviews/cofactor-global-r2-acceptance.json` and its accepted main.
The old CG3 quartic threshold, the pending cubic R3 submission and
ANY corresponding NEW cubic review are NOT premises. The e<A argument
is explicitly reconstructed below. Accepted CG1 gives reducedness,
absence of absolute lines, all ordinary cones and exact contacts.
Accepted CG2 applies to ANY proper factor, including a reduced UNION
of components, retaining the classical c-1 correction.

**R4A.** If q>=2ell+7, EVERY proper factor U over K with
0<e=deg(U)<=N/2 satisfies e<A.

**R4B.** If also N>=3A-2, phi has a UNIQUE absolute irreducible
component G of degree>N/2. Its complementary product H has degree
e<A (possibly e=0), so deg(G)>N-A. G and H may both be normalized
over F2 and are EXACTLY invariant under the S4 action on X,Y,Z,W.
In this regime absolute reducibility of phi is equivalent to its
reducibility over F2, because if H is nonconstant, G,H themselves
give the two positive-degree F2 factors.

**R4C.** Under these two hypotheses, if phi is reducible, take its
ACTUAL invariant cofactor H of degree e>0. Let m be its multiplicity
at P=(1:1:1), S the sum of its non-P diagonal multiplicities, and V
the sum of its off-diagonal multiplicities. Then

    m is even, S is divisible by24, t=e-m=S/3 is divisible by8,
    V is divisible by24,
    D=(ell-3)e+2m-V is a POSITIVE integer divisible by4.

In particular D>=4. These are ORDINARY integer multiplicities, not
congruences calculated in the coefficient field. Equal multiplicity
on EVERY off-diagonal point is not asserted or needed.

**R4D.** Consequently, under q>=2ell+7 and N>=3A-2, reducibility
implies the exact necessary bound

    q <= p*A/16 + ell-1 + 4/p.                    (R4-bound)

If the reverse STRICT inequality holds, phi is absolutely irreducible.
The weaker universal cofactor conclusion in R4B still applies without
this last numerical inequality.

**R4E.** The first two hypotheses hold for EVERY s>=3,k>=2. In
particular the last inequality proves whole absolute irreducibility
for s=4 and EVERY k>=2, that is

    n=15*16^k+1, k>=2.

For s=3,k>=2 it recovers a family already accepted by the special FS
argument; that recovery is not a new result. It also implies all k>=3
in the general family, but supplies no blanket irreducibility theorem
for s>=5,k2. Smaller k, other odd parts, and the full annual problem
remain unresolved here. Priority and possible published overlap remain
unestablished, especially because Férard2017's operative body is unread.

## 1. Exact accepted inequalities and the small-factor step

For ANY actual proper factor U with 0<e<=N/2, CG2 supplies an ordinary
integer D>=1 and

    P(e)=e^2-N*e+(A/4)(q+1)^2 >=0,               (1)
    D*B <= T-a*D^2/A,                           (2)
    B=q+1-2ell*e/A, T=p*(e-e^2/A).

The full first inequality and the UNSIMPLIFIED second inequality are
used. They hold for reduced products because CG2 retained the c-1
term in its multiplicity bound. No assumption that U passes through
P or is F2-defined enters these two premises.

Set e0=(ell-2)q/2. Since N/2-e0=q-1>0, e0<N/2. Substitution gives

    P(e0)=(ell-2)/4 *[-q^2+2(ell+3)q+ell+1].     (3)

At q0=2ell+7 the bracket is -ell-6<0; its derivative is negative
for all real q>=q0. Moreover P is decreasing on e<=N/2. Thus (1)
excludes every e in [e0,N/2], giving e<e0. It follows that

    B > q/(ell+1)+1 >0.                         (4)

Now D*B>0 in (2), so T>0 BEFORE any division by D. Since e>0 and
p,A>0, T=p*e*(1-e/A)>0 implies e<A. This proves R4A for EVERY
smaller factor, not merely for a least-degree absolute component.
The proof has not imported the pending cubic R3 theorem or its reviews.

## 2. A quantitative dominant component by a proper grouping argument

Assume N>=3A-2. Suppose first that no absolute component has degree
>N/2. Since phi is reduced, each component is a proper factor and
R4A gives its integer degree <=A-1. Accumulate distinct components
until their sum d first reaches A. Such a sum exists since total N>=A.
The preceding sum was <=A-1, and the last component has degree<=A-1,
so

    A<=d<=2A-2,       N-d>=A.                   (5)

The two complementary products are nonconstant proper factors, and
the smaller of their degrees lies in [A,N/2], contradicting R4A.
Thus an absolute component G of degree>N/2 exists. It is unique since
two such degrees cannot sum to at most N. Its complementary reduced
product H has degree e<N/2. If e>0, R4A gives e<A; if e=0 this same
strict bound is immediate. Therefore deg(G)=N-e>N-A.

This grouping uses the NEW e<A bound on EVERY proper union; it does
not reuse the invalid irreducible genus inequality on a product.
The weaker N>=4A argument in the unfinished seed is strengthened here
by taking the smaller complementary degree in (5). No conclusion is
made below N>=3A-2 from this particular grouping argument.

## 3. Descent and the exact four-letter symmetry

Coefficient Frobenius sigma:c->c^2 preserves phi, so it permutes its
absolute irreducible divisor components and preserves their degrees.
Uniqueness forces sigma(G)=cG for some c!=0. Normalize one nonzero
monomial coefficient of G to1. Its corresponding coefficient in
sigma(G) is also1, forcing c=1. Every coefficient of G is fixed by
squaring, so G has coefficients in F2. Write H=phi/G over K. Applying
sigma to this identity and cancelling G gives sigma(H)=H, hence H
also has coefficients in F2. The irreducible case H=1 is included.

Every permutation of X,Y,Z,W induces an invertible linear map on
the three-dimensional space X+Y+Z+W=0: any three of these four linear
forms are independent, and the inverse comes from the inverse
permutation. The action is faithful: the four displayed linear forms
are distinct, so a permutation fixing each form is the identity.
These maps have F2 coefficients. They fix f. The three
linear factors of R correspond to the three pair partitions, since
X+Y=Z+W and similarly for the other two pairs. Each permutation
therefore permutes the THREE displayed factors of R, and fixes R
exactly. As f=R*phi in a polynomial domain, phi too is fixed exactly.

Every such map preserves the unique large component as a divisor.
Thus G(MX)=c_M G(X). Both polynomials have F2 coefficients. Comparing
the monomial at which G was normalized to1 gives c_M in F2*. Hence
c_M=1. Cancellation in phi=G*H then gives H(MX)=H(X) exactly as
well. There is no nontrivial scalar character left to assume away.
If H is nonconstant, G and H are the two positive-degree F2 factors
asked for in the official open question. Conversely an F2 factorization
is an absolute factorization, proving the equivalence in R4B.

## 4. Multiplicity divisibility on the ACTUAL invariant cofactor

Assume reducibility and use this H with e>0. Its tangent cone at any
listed ordinary point is a product of a subset of the DISTINCT tangent
lines of phi. This is an accepted CG1 consequence of reducedness.
The group stabilizer of the point preserves this subset. We need
only exact orbit sizes, not transitivity on the full singularity set.

### 4.1 The central point

At P put X=1+x,Y=1+y,Z=1. The transposition X<->Y acts on the
tangent plane by (x,y)->(y,x). Its sole fixed projective direction
in characteristic2 is x=y, one of the three prescribed diagonals.
That direction is NOT a tangent of phi by CG1. The selected tangent
lines of H therefore split into free pairs under this involution.
Consequently m is even. This reasoning does not require H to pass P;
m=0 is permitted.

### 4.2 Non-P diagonal points

Each can be permuted to P_b=(b:1:1), b in F_Q*, b!=1. Its four
coordinate values are (b,1,1,b). A projective permutation fixing P_b
must multiply this multiset by some c. Either c fixes both b and1,
giving c=1, or it swaps them, requiring c=b and b^2=1. In char2
the second case would force b=1, excluded. Thus the stabilizer consists
of the two independent swaps of the equal pairs, and has order4.
Its S4 orbit therefore has size6. Invariance of H makes its
multiplicity constant on this six-point orbit.

There is a stronger LOCAL constraint at P_b. With X=b+x,Y=1+y,Z=1,
the swaps (X W) and (Y Z) have first-order actions

    (x,y)->(x+y,y),       (x,y)->(x+b*y,y),        (6)

respectively. The second follows directly by normalizing Z'=1:
x'=(x+b*y)/(1+y), y'=y/(1+y). The diagonal y=0 is not a tangent
by CG1. On the remaining tangent directions u=x/y, (6) acts by
u->u+1 and u->u+b. Since b!=0,1, these generate the additive group
{0,1,b,1+b} of order4, acting freely on finite u. The selected
tangent lines of H are an invariant subset, so their number r_b is
divisible by4. Each six-point orbit consequently contributes a
multiple of24 to S. Therefore 24 divides S and, by the accepted exact
diagonal identity S=3(e-m), 8 divides t=e-m.

### 4.3 Off-diagonal points

At such a point the four nonzero coordinate values are pairwise
distinct; equality of any pair is exactly one prescribed diagonal
because X+Y+Z+W=0. If a permutation fixes the projective point, some
nonzero scalar c permutes this four-element set. The cyclic action
of multiplication by c is free on every nonzero element: each orbit
has length equal to the multiplicative order d of c. Thus d divides4.
In characteristic2, c^4=1 implies (c+1)^4=0 and c=1. Distinctness
then forces the permutation itself to be the identity. Each S4 orbit
has size24. H has constant multiplicity on each such orbit, giving
24 divides V. No assertion that DIFFERENT orbits have equal
multiplicity enters this argument.

Finally ell-3=Q-4 is divisible by4, m is even and V is divisible
by24. Hence

    D=(ell-3)e+2m-V is divisible by4.            (7)

CG2 already guarantees the SAME ordinary integer D>=1 for this H,
so D>=4. This completes R4C without a generic invariant-ring theorem,
Frobenius orbit assumption or an off-diagonal uniformity shortcut.

## 5. The strengthened threshold and its exact endpoints

Use the SAME B,T of Section1 for H. We already have B>0,T>0.
Divide (2) by D>0 and use D>=4, retaining both signs:

    B <= T/D-a*D/A <= T/4-4a/A.

Thus

    q+1 <= (p/4+2ell/A)e - (p/(4A))e^2 -4a/A
         <= (p*A+8ell)^2/(16p*A)-4a/A
          = p*A/16+ell+4/p.                     (8)

The second line is a global REAL quadratic maximum, not an assertion
that its vertex is an attainable factor degree. For the last identity
use ell^2-ell-2=A and a=(ell+2)/p. Subtract1 to obtain (R4-bound).
Its strict reverse contradicts an actual cofactor H and proves whole
absolute irreducibility. Equality is NOT excluded by this argument.

For EVERY Q>=8,k>=2,

    q>=Q^2>2Q+5=2ell+7,
    N-(3A-2)>=(Q-1)Q^2-3Q(Q-3)
              =Q*(Q^2-4Q+9)>0.                (9)

At Q=16, ell=15,p=14,A=208. The bound is

    p*A/16+ell-1+4/p = 182+14+2/7 = 196+2/7,

whereas q>=256. This proves the proposed family s4,k>=2. For Q8,
the bound is 15+6+2/3=21+2/3 and q>=64, recovering the already
accepted FS family. For general Q>=8,k>=3, the threshold is

    (Q-2)(Q-3)Q/16+Q-2+4/(Q-2)
       < Q^3/16+Q < Q^3 <= q,

because -2+4/(Q-2)<0 and Q>=8. No small-field scan, symbolic
optimizer, factor table or numeric interpolation supplies these steps.

For s>=5,k2 this bound may fail; failure of a sufficient exclusion
does not imply reducibility. The unique-component/small-cofactor
reduction still applies by (9). General k1 is not covered by (9),
nor by this theorem's necessary-threshold conclusion without separately
checking BOTH hypotheses. Other exponent families are untouched.

## 6. Source and proof boundaries

The complete accepted CG1/CG2 main was reread. Its exact full
unsimplified inequality, reduced-product c-1 correction, absence of
absolute lines, ordinary tangent cones and diagonal identity are the
only operative mathematical imports. Its historical proof status
is controlled by the exact accepted authority, not by a free-standing
copy of the old constructor label. CG3 and pending R3 are unused.

The global geometric method is classical and attributed in CG's source
audit. The fresh S4 argument is completely written above. Hernando–
McGuire's proper-divisor COMPONENT theorem is not a premise, and is
not a whole-polynomial assertion at k1. Férard2017's exact paper is
identified, but its operative body and exceptional forms remain UNREAD;
no absence-of-prior-art or priority conclusion follows. The separate
Frobenius/Gauss note checks a failed interface only; none of its
unverified hypotheses is imported. Full third-party papers remain local.

The accompanying constructor obligations, rejected routes, source
limits, worklog and ALL compact preservation metadata are part of this
ENTIRE submission. No OTHER agent supplied a NEW mathematical inference.
Root's accepted-CG authorship and pending-cubic authorship are disclosed.
Neither can count as an OTHER independent audit of this new packet.
Promotion requires TWO OTHER initially blind WHOLE audits, EACH
finished with ALL companions and metadata before corresponding new
peer findings/files/hashes/metadata are revealed, then full reconciliation.
