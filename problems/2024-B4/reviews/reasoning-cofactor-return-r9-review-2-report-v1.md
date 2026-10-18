# Independent whole R9 review2: reciprocal and cubic jet criterion

18 October2026 UTC. **Initially blind ENTIRE WHOLE audit, ALL64.**
Reviewer C, `/root/review_2017_coarsening_r1`, did not construct NEW R9
and received no new mathematical inference from root or B. Requested
inherited gpt-6.1-sol/max; verified effective-setting readback unavailable.
The exact author main is20443bytes, SHA
`740e85acc2103aa6ed72ac46ac3089b12cfb29962fc4e0593ccf9e8223af66bf`;
the ENTIRE11 freeze is9271bytes, SHA
`baad7591162df50c28cc4d20794616d165d622ae8c6abc0bb9f699e255d2147d`.

**Disposition: no substantive mathematical defect found in R9A–D's stated
scopes.** ALL64 separate dispositions are in the companion ledger. Nine
adversarial notes are closed below/in the issues record. This is one
independent review, not acceptance: TWO OTHER entire initially blind whole
reviews and coordinator reconciliation remain required. The disposition
and every new peer file/hash/metadata remain embargoed until the explicit
BOTH-entire confirmation. All old bytes stay preserved.

C constructed the OLD accepted R6/R7/R8 and reviewed earlier T1–T4.
Those accepted inputs have their own OTHER audits. This new whole R9
audit is NOT independent recertification of C's own earlier proofs. Fresh
complete current bodies and each authority MD/JSON were read to check the
exact imports. R9's new use of condition(J), zero-initial-jet handling,
congruences and families was constructed by B, without C's contribution.

## 1. Actual question and dependency boundary

I freshly read official PaperB page2 B4 setup/(b), the complete local
statement, AGENTS and all eleven author files, including every obligation,
constructor check, failure/source/log/code record and both generated
metadata files. Only(b) is audited. The question is an identity of
coefficientwise reductions in F2[X,Y,Z], with two nonconstant factors,
and not a polynomial-function identity on a finite field. The established
quotient is homogeneous; whole absolute irreducibility is a sufficient
exclusion of the requested F2 factorization, including nonhomogeneous
integer lifts. A single absolute component defined over F2 would not be
enough.

Set q=2^i, i>=2, ell>=3 odd, n=ell*q+1, delta=q²-q+1, N=ell*q-2.
Oddness of ell makes q the MAXIMAL2-power in n-1. Its binary expansion has
at least two ones; shifting it by i then adding the separate bit0 gives
wt(n)>=3. Thus accepted T1 applies over K=F2bar. Complete general R6B/C,
not merely its special family, applies to EVERY nonlinear absolute
component and supplies degree>=q and reducedness. Those are the only
operative project inputs in R9A/B/D. R6D and R7A are additionally needed
ONLY to combine the full ell15 coverage in(F15). R8's NF4 theorem is NOT
applied when its hypothesis fails.

Condition(J) quantifies over ALL four DISTINCT roots of unity whose sum
is0 and requires their delta-power sum nonzero. It is sufficient, with no
necessity claim. It is weaker than NF4 as a hypothesis: the actual ell15
family below both satisfies(J) and has four-sums. No auxiliary polynomial
function on a field is substituted for phi_n. Endpoints ell1,q2,n1/n3
are outside, and(ell,q)=(3,4),n13 is expressly excluded from R9A.

## 2. Local lemma, reducedness and the complete intersection locus

The local product lemma is valid as stated. Suppose ord(G)=r>=2 and
G_r=cL^r with c!=0. If G=UV with positive orders u,v, then u+v=r.
Unique factorization in K[x,y] forces U_u=aL^u and V_v=bL^v. The
degree r+1 product term is

    aL^u V_(v+1) + bL^v U_(u+1),

which is divisible by L because u,v>=1. Therefore a next homogeneous
term not divisible by L forbids BOTH factors vanishing. Missing next
terms are0 and divisible; none can be used to force a contradiction.
Multiplication by a unit only adds a multiple of L^r to that next term,
so the conclusion is invariant under the actual unit denominators used.
This is no-two-factors at ONE point, not local smoothness/global
irreducibility.

Reducedness can also be reconstructed without a source assumption. With
W=X+Y+Z the three numerator derivatives are(X^ell+W^ell)^q and its Y,Z
versions. Their common projective locus is finite: W0 would force all
coordinates0; with W1, each coordinate is an ellth root. A repeated
irreducible factor of f_n divides all three derivatives, even for even
multiplicity, and its projective curve cannot fit in this finite locus.
The nonzero numerator has coefficient1 at X^(n-1)Y. Thus f_n and phi_n
are absolutely reduced.

Let two actual distinct components intersect. Their coprime component
partition makes the point singular on phi_n; f_n=R phi_n then gives f_n
and its derivatives0 there, ALSO when R0. In the Z1 chart put P=(a:b:1)
and c=a+b+1. The affine derivative equations give
a^ell=b^ell=c^ell=u. The value equation is

    f_n(P)=(a+b+c)u^q+1=u^q+1=0.

Frobenius injectivity gives u1. Thus all a,b,c are nonzero roots in
mu_ell. Off R, the four a,b,1,c are distinct; any repeated pair is
equivalent to a=b,a1 or b1. On R the only remaining cases are the three
noncentral diagonal sets and their common center(1:1:1).

No intersection is hidden at infinity. If Z0,R!=0 then X+Y!=0 and the
HOMOGENEOUS derivative(f_n)_Z=(X+Y)^(n-1) is nonzero. At a quotient
zero this implies a nonzero derivative of phi_n, hence smoothness. The
three R0 infinity vertices are(1:0:0),(0:1:0),(1:1:0). At the first use
the Y derivative of f_n=R phi_n, at the last the X derivative, and use
symmetry for the other: both the selected f and R derivatives are1,
so phi_n=1. They are not curve points. This uses n>1, which holds here.

## 3. Independent off-diagonal expansion, including zero coefficients

At an actual off-diagonal singular point translate X=a+x,Y=b+y,Z=1.
The identity(a+x)^n=(a+x)(a^q+x^q)^ell permits below2q only the
degrees0,1,q,q+1. Constant/linear forms vanish at this point. Because
each base coordinate has ellth power1 and ell is odd, the q and q+1
forms are exactly

    F_q=(Ax+By)^q,
    A^q=a^(1-q)+c^(1-q), B^q=b^(1-q)+c^(1-q),
    F_(q+1)=a^-q x^(q+1)+b^-q y^(q+1)+c^-q(x+y)^(q+1).

Frobenius is bijective on K, so A,B exist uniquely. At this stage A,B
or A+B may be0. I did not assume a root-field intersection or divide
by any of them.

To independently check the crucial cleared identity, write D=a^q b^q
c^q and expand(A+B)^(q+1)=A^q A+A^q B+B^q A+B^q B. Substitution of
the displayed qth powers into D*F_(q+1)(B,A) leaves coefficient of B

    b c^q+b^q c+a b^q+a^q b
      =b(a+c)^q+b^q(a+c)=b+b^q,

since a+c=b+1. The coefficient of A is a+a^q by the same expansion.
Thus D*F_(q+1)(B,A)=T=B(b+b^q)+A(a+a^q), including all zero cases.
Raising this expression to q gives

    T^q=a+b+a^delta+b^delta
           +c^(1-q)[(a+b)^q+(a+b)^(q²)].

With a+b=c+1 the bracket is c^q+c^(q²); multiplying gives c+c^delta.
As a+b+c1, the result is1+a^delta+b^delta+c^delta, exactly the
condition(J) sum on the actual roots a,b,1,c. This proves T!=0 and
also forces(A,B)!=(0,0), closing the potentially zero initial-cone case.

Consequently L=Ax+By is a nonzero line and(B,A) is its nonzero tangent
vector. The cleared evaluation above is nonzero, so L cannot divide
F_(q+1). Since R0!=0, division by the translated unit denominator gives

    phi_q=F_q/R0,
    phi_(q+1)=F_(q+1)/R0 + R1 F_q/R0².

The correction vanishes on L=0, so it cannot cancel the nonzero first
term's restriction. Apply Section2's lemma with r=q. No off-diagonal
point can host two components under(J), though such a point may remain
singular on one component. A simultaneous zero A=B=0 is impossible UNDER
(J), not impossible for every exponent. This distinction is essential.

## 4. All diagonal jets, both cases, and their count

At a noncentral diagonal point use coordinate symmetry to write(b:1:1),
b in mu_ell minus{1}; set c0=b+1,E=b^-q,B0=1+b^(1-q). Translation
gives, by the same binomial/Frobenius identity,

    F_q=B0 y^q,
    F_(q+1)=y[E x^q+E x y^(q-1)+(1+E)y^q],
    R=y(c0+x)(c0+x+y)
     =c0²y+c0y²+x²y+xy².

Here c0,E!=0. B0!=0 iff b notin F_q. In that case divide degree q by
the first denominator term to get phi_(q-1)=B0/c0²*y^(q-1). Subtract
the product of that form with c0 y² before the next comparison. This
gives

    phi_q=E/c0²*x^q+E/c0²*x y^(q-1)
                 +[(1+E)/c0²+B0/c0³]y^q.

The nonzero x^q coefficient E/c0² means the sole tangent y does not
divide the next form. The local lemma has r=q-1>=3 and excludes a
component intersection. It does not incorrectly call the point smooth.

If b in F_q*, B0=0 and E=b^-1. The first quotient form is instead

    b^-1/c0² * [x^q+x y^(q-1)+c0 y^q].

Its exact order is q. At y1 the slope polynomial x^q+x+c0 has derivative1,
and its leading x^q coefficient is nonzero. Hence it has q distinct
finite tangents and no extra y0 tangent. All factor cones partition
these distinct directions. The number of b in mu_ell intersect F_q*
is d0=gcd(ell,q-1), as common roots of two odd-exponent unity equations.
Removing b1 and taking three disjoint diagonal sets gives EXACTLY
3(d0-1) ordinary noncentral points. None is dropped when d0>1.

At the center translate(1+x,1+y,1). Degree q cancels, degree q+1 of
the numerator is x^q y+x y^q, and R=xy(x+y). Thus the first quotient
form has order q-2 and equals

    (x^(q-1)+y^(q-1))/(x+y)
      =product_(alpha in F_q minus F2)(x+alpha y).

Odd q-1 makes the q-2 surviving directions distinct. A factor missing
any particular point has local order0 and contributes0 to that point's
intersection; it is not required to pass through the center.

## 5. Global actual-factor contradiction and small exception

Assume reducibility over K, select an actual least-degree absolute
component U and let V be its actual full complement. Reducedness gives
gcd(U,V)=1 even if V is reducible. T1 and general R6B/C give
q<=e=deg U<=N/2. Also N-2q=(ell-2)q-2>=2. Consequently

    e(N-e)-q(N-q)=(e-q)(N-e-q)>=0,
    e(N-e)>=(ell-1)q²-2q.

At every ordinary point the disjoint cone subsets of U,V have coprime
tangents; local intersection equals the product of their orders. This
also holds with both sides0 if either is a unit. The center contributes
at most(q-2)²/4 and EACH of the3(d0-1) other ordinary points contributes
at most q²/4. Sections2–4 have excluded every other possible intersection.
Projective Bezout for coprime actual curves, valid for this reducible V
in characteristic2, therefore yields

    e(N-e)<=[(q-2)²+3(d0-1)q²]/4.

Subtracting the right upper from the lower gives exactly

    [(4ell-3d0-2)q²-4q-4]/4
      >=[(ell-2)q²-4q-4]/4.

For ell>=5 and q>=4, the last numerator is at least3q²-4q-4>=28;
for ell3,q>=8 it is at least q²-4q-4>=28. Monotonicity for these
positive q ranges follows from q(3q-4)-4 and q(q-4)-4. The ONLY remaining
power-of-two pair is ell3,q4. Here d0=3, lower24 and upper25 provide
no contradiction. The exception is correctly retained. The argument
therefore proves the WHOLE R9A conclusion, rather than only a component.

The classical geometry was checked in the primary Fulton copy: complete
operative Sections3.3 and5.3, plus AppendixA. Its local-algebra/graded-ring
arguments used here do not require characteristic0 or irreducibility of
V. We use no genus formula for V and no Gauss-map hypothesis. Exact fresh
read ranges and limits are in the source companion.

## 6. The two arithmetic tests are valid sufficient tests

For four distinct nonzero a,b,c,d with equal sum0 put s=a+b=c+d!=0.
If the reciprocal sum also vanished, s/(ab)=s/(cd), hence ab=cd.
The unordered pairs would then solve the same quadratic T²+sT+ab and
coincide, contradicting four distinct entries. This uses NONZERO roots,
and is not APN-ness of the inverse function on an entire even-degree
field including0.

The cube expansion is directly

    a³+b³+c³+(a+b+c)³=(a+b)(a+c)(b+c)!=0.

On mu_ell, either delta=-2^t or delta=3*2^t modulo ell changes the
delta sum into respectively a Frobenius power of the inverse sum or
of the cube sum. Injective Frobenius, including the identity t0, gives
(J). Negative exponents are evaluated only at nonzero roots. Neither
test is called necessary, and their failure is not made a factorization.

## 7. Complete infinite-family and boundary reconstruction

For ell15,i=4k+2, q4mod15 and delta13=-2mod15. The reciprocal test
uses t1, proving EVERY k>=0 and avoiding the excluded ell3 corner.
The binary weight is exactly5: four shifted bits of15 plus bit0.
To witness genuine NF4 failure, mu15=F16*. An element beta outside
F4 gives the additive coset beta+F4, whose four distinct nonzero members
beta,beta+1,beta+omega,beta+omega² sum0. Scaling by one member's
inverse preserves mu15, distinctness and the sum and makes one root1.
Writing the others a,b,c gives c=a+b+1. These roots satisfy the numerator
value/gradient equations; R!=0. Hence an ACTUAL off-diagonal singularity
does occur, but Section3 forbids a component intersection there.

The literal old hypotheses indeed fail on this branch. ord15(2)=4
because2^4=1 while2 and4 are not1, so gcd(i,4)=2. Also q-2=2 and
2q-1=7mod15; neither neighbor congruence holds. R6D at ell15 uses
q=16^k, never i2mod4. These are comparisons of sufficient assumptions,
not a literature-novelty conclusion.

For(F15), odd i>=3 meet accepted R7A's gcd(i,4)=1. The new proof covers
i2mod4. Multiples of4 with i>=8 have q=16^(i/4), and accepted R6D uses
Q16,k=i/4>=2. Thus all i>=2 except i4 are covered. n241 at i4 equals
16²-16+1; no new conclusion there is needed or asserted.

For R9D, delta is odd, delta>=13, and2^t is positive even for t>=1.
Thus ell=delta+2^t is odd>=15, delta=-2^tmod ell, and the R9A exception
cannot occur. The n formula is ell*q+1=q³-q²+q+2^t q+1; t1 gives
q³-q²+3q+1. No fixed odd-part or root-field condition was smuggled in.

At n57, ell7,q8, delta1mod7. The powers of2 form an order3 subgroup,
so -1 is absent; the cubic alternative would require5 in it, but
5³=-1mod7. At n205, ell51,q4, delta13. The reciprocal test would require
2^t=-13: modulo3 gives t odd, whereas modulo17 it gives2^t4 and t2mod8
since2^4=-1,2^8=1. Impossible. The cubic test fails modulo3 immediately.
These are exact consistency checks, not scans or re-factorizations of old
examples. n13 remains expressly outside the absolute criterion.

## 8. Scope, source honesty, preservation and final disposition

Every new inference needed for R9A–D has been reconstructed above. The
main's claim is a sufficient whole ABSOLUTE irreducibility theorem, hence
an official nonfactorization for its stated parameters; it is not the
complete ordinary-F2 classification. When both congruences fail, nothing
here decides(J). When(J) fails, no convenient intersection cost or actual
cofactor is supplied. The unrestricted annual question and priority stay
open.

Fresh complete T1–T4/R6/R7/R8 bodies and authority MDJSON, R6 failure and
R8 failure/source records were read. The new proof does not invoke a
published APN theorem; only accepted R7A's scoped odd-i conclusion is
used in combined(F15). The original CKM operative proofs were historically
read in C's OLD R7 construction; no fresh reread or independent old-proof
audit is claimed here. Original joint journal/JW1993/Ferard2017 bodies
were NOT freshly read. The author correctly distinguishes a fresh thesis
record visit from its older visual thesis reading. No priority or complete
published-overlap audit follows, and no unrestricted5mod8 theorem is
accepted or refuted from a search remark.

No mathematical program, scan, CAS, factor table, sample test, source/
author/old-certificate replay or optimizer was used. The new admin only
checks bytes/JSON/64 labels and preservation. It verifies the ENTIRE11
author, its compact31-record baseline, four exact current accepted bodies
and authorities, and this reviewer's immediate immutable SQ15v1.1
ENTIRE16 parent. Historical inventories remain compactly parent-bound.
All writes are exclusively in the assigned NEW review2 prefix; no old,
shared, Git or cache byte is changed. No pending call or native child.

The nine closed notes and ALL64 ledger constitute the whole initial.
Final full-model readback of EVERY payload and manifest, then SEPARATE
verification, precedes identity-only handoff. No corresponding NEW root
R9 finding/file/hash/metadata has been accessed. One whole pass does not
promote the candidate; BOTH whole initials and root reconciliation are
still required before acceptance.
