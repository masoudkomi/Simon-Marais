# Accepted composition-Kasami: coordinator status and scope

2026-10-17 UTC. **Proved, independently reviewed scoped partial result.**

CP1 proves, for ALL odd d,n>=3, that the WHOLE homogeneous polynomial phi_d divides phi_n over F2 if and only if g_n=H composed with g_d for some H in F2[T], where x^n+(x+1)^n=g_n(x²+x). Both homogeneous directions, the full-degree dehomogenization, rank-four free-module descent and monic h-adic argument are included. Repeated diagonal factors and d=3/n=3 unit endpoints are retained. This criterion does not classify arbitrary factors of phi_n.

CP2 proves for EVERY q=2^k,k>=1, d=q²−q+1 and N=(q⁵+1)/(q+1) that g_N=g_d^(q²+1)+(g_d+1)^d, by an unrestricted four-term Frobenius identity. CP3 gives actual positive-degree homogeneous F2 factors and coefficientwise integer lifts for k>=2. Its advertised family beyond the attributed q=4,n=205 endpoint uses k>=3; the first is n=3641 with whole divisor phi_57 and factor degrees54 and3584. Every k>=3 member lacks the WHOLE phi13 divisor, by the separately accepted exact criterion and the valuation v2(N−1)=k. This does not exclude its other factors.

Root's whole R1 and the other reviewer's whole R2 were independently frozen before comparison, with23 and38 inference checks respectively. Reviewer2 authored old T1–T4/C7/C11 context but did not construct the new CP1–CP3. Root inspected an unrelated MCM-polynomial literature lead after the independent R1; that lead is no premise, contribution or repair of the CP proof. No substantive objection was found and no author repair was required. The saved q8 computation is finite corroboration only, and neither reviewer reran it. The elementary all-q proof stands without it.

The n=1 zero-polynomial and n=3 unit boundaries do not qualify for the official problem. No full reducibility classification, arbitrary-m extension of the family, absolute-component list, APN classification, or novelty is accepted. The annual 2024 problem remains unresolved. The q=4/205 context and published coordinate methods are attributed, with exact external proof-read limits in the source records.

The complete frozen submission follows as a byte-identical suffix. Its historical unverified labels and conditional statuses record the submission date; this header and the acceptance record state the current scope.

---

# Whole-divisor composition and a generalized Kasami family

2026-10-17 UTC. **Candidate proof - unverified.** Constructor:
`review_2017_coarsening_r1`; requested gpt-6.1-sol/max, verified effective
readback unavailable. Two OTHER fresh initially blind nonconstructor
whole audits are required. This is part(b) only. No novelty or complete
reducibility classification is claimed. Original APN component theorems,
the accepted phi13 criterion, T1--T4 and C7/C11 remain separately attributed.

## Statements and exact scope

Work in F2[X,Y,Z], with coefficientwise polynomial equality. For odd
n>=3 use the already established quotient

    phi_n=(X^n+Y^n+Z^n+(X+Y+Z)^n)/R,
    R=(X+Y)(Y+Z)(Z+X).

For an odd n>=3, define the univariate polynomial g_n over F2 uniquely by

    x^n+(x+1)^n=g_n(x^2+x).                              (1)

Existence, uniqueness and degree are proved below. It is unrelated to
the unspecified factor called g in the official question.

**CP1 (all fixed WHOLE divisors).** For odd d,n>=3,

    phi_d divides phi_n in F2[X,Y,Z]
       iff g_n=H composed with g_d for some H in F2[T].   (2)

In particular d-1 divides n-1 whenever this holds. For d>=5 and n>d,
the composition has degree at least two and gives a genuine proper whole
divisor. This concerns the whole fixed phi_d, not each of its individual
irreducible or absolute factors. It is not an assertion that all factors
of phi_n come from a univariate invariant ring.

**CP2 (unrestricted Frobenius identity).** Let q=2^k, k>=1, and put

    d=q^2-q+1,
    N=(q^5+1)/(q+1)=q^4-q^3+q^2-q+1,
    B_q(T)=T^(q^2+1)+(T+1)^d in F2[T].

Then the exact univariate identity is

    g_N=B_q composed with g_d.                           (3)

Consequently phi_d divides phi_N OVER F2. No absolute Kasami
factorization theorem, factor-field descent from that theorem or APN
classification is a premise of (3).

**CP3 (qualifying family beyond the accepted phi13 progression).**
For every k>=3, the odd positive integer

    N_k=2^(4k)-2^(3k)+2^(2k)-2^k+1                       (4)

satisfies the official part(b), with whole divisor phi_(2^(2k)-2^k+1)
and positive-degree cofactor. Their degrees are

    2^(2k)-2^k-2,          2^(3k)(2^k-1).                (5)

These exponents are infinitely many distinct integers. Their valuation
v2(N_k-1)=k>=3 differs from valuation2 for every exponent in the accepted
whole-phi13 progression. Thus the accepted phi13 criterion also says
phi13 does NOT divide any member of (4). That last comparison uses the
accepted criterion; the construction (2)--(5) is independent of it.

The q=4 endpoint is the already published/accepted n=205 mechanism and
is only a compatibility endpoint here. Its old certificate is not rerun.
At q=2 the divisor is phi3=1, so this identity gives no qualifying
two-positive-degree factorization. The new advertised range is k>=3.
The official n=1 zero case and n=3 unit case remain excluded as previously
established; neither is silently an irreducible polynomial in this note.

## 1. Translation invariants, exact degrees and a linear projective change

Set G_n(x)=x^n+(x+1)^n. It is fixed by x->x+1. Let U=x^2+x.
Every element of F2[x] has a unique expression

    A(U)+x B(U),       A,B in F2[U].

Existence follows repeatedly by reducing x^2=x+U. For uniqueness, the
leading degrees of U^a and xU^b are respectively even and odd, so their
largest terms cannot cancel. Translation by one sends A+xB to A+xB+B;
therefore its invariant elements are exactly F2[U]. This proves (1).
For odd n>1 the x^n terms cancel in G_n, and its x^(n-1) coefficient
is n=1 in F2. Thus g_n is monic of degree

    e_n=(n-1)/2.                                         (6)

Define the symmetric difference quotient

    Q_n(U,V)=(g_n(U)+g_n(V))/(U+V) in F2[U,V].            (7)

It is a polynomial, since every T^j+S^j is divisible by T+S in
characteristic two. Its degree is e_n-1: its highest homogeneous part
is (U^e_n+V^e_n)/(U+V), which is nonzero, including when e_n is even.
For n=3 this is the constant1.

Now use the INVERTIBLE LINEAR homogeneous coordinate map

    (X,Y,Z)=(s+u,s,t),     inverse (s,t,u)=(Y,Z,X+Y).

Dehomogenize at u=1, and write Psi_n(s,t)=phi_n(s+1,s,t). The numerator
becomes G_n(s)+G_n(t), while R becomes
(s+t)(s+t+1)=s^2+s+t^2+t. Hence the exact polynomial identity is

    Psi_n(s,t)=Q_n(s^2+s,t^2+t).                         (8)

There is no division by a numeric s,t or a possibly vanishing value.
Equation (8) follows in the polynomial ring from the defining R quotient.
The numerator and denominator cancellation are exact identities in a
domain. This is not equality of functions on a finite set.

Substitution in (8) doubles the highest total degree: distinct highest
monomials U^a V^b give distinct s^(2a)t^(2b). Consequently

    deg Psi_n=2(e_n-1)=n-3.                              (9)

Thus no factor at the dehomogenizing line u=0 was lost. More explicitly,
the homogeneous phi_n(s+u,s,t) is exactly the degree-(n-3)
homogenization of Psi_n; its top affine part is nonzero. If Psi_d divides
Psi_n, the cofactor's total degree is n-d by additivity of total degree
for nonzero products. Homogenizing the equality therefore gives division
of those full homogeneous polynomials with no extra power of u. The
inverse linear map recovers phi_d|phi_n. The other direction is immediate
by substitution/dehomogenization. We have proved

    phi_d|phi_n  iff Psi_d|Psi_n.                         (10)

The n=d and d=3 unit cases obey this same argument; when n<d and d>=5,
both sides correctly fail by degree.

## 2. Whole-polynomial divisibility descends through both quadratic covers

Put S=F2[U,V], A=F2[s,t], with U=s^2+s,V=t^2+t. The embedding of S
is injective: leading monomials U^a V^b have distinct s^(2a)t^(2b).
In fact A is a FREE S-module with basis

    1,s,t,st.                                            (11)

Reduction by the two monic quadratic relations gives existence. To check
independence, products U^a V^b s^epsilon t^delta have distinct leading
exponent pairs (2a+epsilon,2b+delta), for epsilon,delta in{0,1}.
The largest leading monomial of a finite nonzero sum cannot cancel.

Let A0,B0 be nonzero elements of S. If their substituted images satisfy
B0=A0 C in A, expand C uniquely in (11). Since the left side lies in
S, independence forces each coefficient of s,t,st to be annihilated
by A0. S is a domain and A0 is nonzero, so those three coefficients
are zero. The remaining coefficient belongs to S. Therefore

    A0|B0 in A iff A0|B0 in S.                            (12)

This direct free-module argument supplies coefficient-field descent over
F2 and retains every specialization U=0,V=0. It is not a claim that
individual factors of B0 after substitution must themselves be in S.
Applying it to the WHOLE Q_d,Q_n and using (8),(10) gives

    phi_d|phi_n iff Q_d|Q_n in F2[U,V].                   (13)

## 3. Difference-quotient division is exactly composition

We prove the elementary polynomial statement needed for (13). Let
h,p in F2[T], with h monic of degree e>=1. Repeated division by h
gives a unique expansion

    p(U)=sum_(j=0)^(e-1) U^j C_j(h(U)),  C_j in F2[T].   (14)

Existence is division with remainder iterated on each quotient. For
uniqueness, the leading degrees of U^j C_j(h(U)) are distinct modulo
e for different j, so the largest one cannot cancel.

Divide p(U)+p(V) by the monic degree-e polynomial h(U)+h(V) in
F2[V][U]. Modulo this divisor, h(U) equals h(V), so its remainder is

    sum_(j=0)^(e-1) U^j C_j(h(V)) + p(V).                 (15)

If h(U)+h(V) divides p(U)+p(V), (15) vanishes. For every j>=1 this
forces C_j(h(V))=0. Composition with the nonconstant h(V) is injective
on F2[T] by leading degree, so C_j=0. Hence p=C_0 composed with h.
Conversely p=H composed with h gives
h(U)+h(V) dividing p(U)+p(V), by the universal identity
H(A)+H(B) divisible by A+B. The recovered H is in F2[T], not merely
an extension field.

Since g_d(U)+g_d(V)=(U+V)Q_d and likewise for n, cancellation of the
SAME nonzero U+V factor shows

    Q_d|Q_n iff g_n=H composed with g_d, H in F2[T].       (16)

No coprimality of Q_d and U+V is required for this cancellation. In
particular possible repeated diagonal factors of a difference quotient
are not discarded. Combining (13),(16) proves CP1 completely. Equation
(6) then gives (n-1)/(d-1)=deg H, proving the divisibility obstruction.
For n=d, monicity and g_n(0)=g_d(0)=1 give H(T)=T. For d=3,
g_3(T)=T+1 has degree one, so every g_n is a composition with it,
consistent with the unit phi3.

## 4. The all-q Frobenius identity, with every cross term exposed

Let q=2^k, k>=1, d=q^2-q+1 and N=q^4-q^3+q^2-q+1. In F2[x]
write

    a=x, b=x+1, a+b=1,
    c=a^d+b^d=G_d(x),
    p=a^(q-1)+b^(q-1), w=ab.

Only that q and its powers are Frobenius powers is used. First,

    w p^(q+1)
      = a^(q^2)b + a^d b^q + a^q b^d + ab^(q^2).        (17)

This follows by expanding
ab(a^(q(q-1))+b^(q(q-1)))(a^(q-1)+b^(q-1)). Adding c to
the middle two terms in (17) gives

    a^d(1+b^q)+b^d(1+a^q)
      = a^(d+q)+b^(d+q)
      = a^(q^2+1)+b^(q^2+1),

because 1+b^q=a^q and 1+a^q=b^q. Adding the first and last terms
of (17) to this expression gives

    a^(q^2)(a+b)+b^(q^2)(a+b)
      = a^(q^2)+b^(q^2)=1.

Therefore the exact identity is

    c+1=w p^(q+1).                                       (18)

For the next expansion use the INTEGER exponent equalities

    d(q^2+1)=N+q^2,
    q^2-d=q-1,
    N-d=q^3(q-1),
    d(q^2-1)=(q^3+1)(q-1),
    d(q+1)=q^3+1.                                       (19)

Expanding c^(q^2+1) and adding G_N(x)=a^N+b^N, then using
1+a^(q^2)=b^(q^2), gives

    c^(q^2+1)+G_N
      = a^N b^(q^2)+b^N a^(q^2)
          +a^(d q^2)b^d+b^(d q^2)a^d
      = w^d [a^(q^3(q-1))b^(q-1)
               +b^(q^3(q-1))a^(q-1)
               +a^((q^3+1)(q-1))+b^((q^3+1)(q-1))]
      = w^d (a^(q-1)+b^(q-1))^(q^3+1)
      = (w p^(q+1))^d
      = (c+1)^d.                                        (20)

The third line is exactly the four-term expansion of p^(q^3+1);
q^3 is another Frobenius power. The fourth uses the last equality
in (19); the last uses (18). All exponents in these factorizations
are nonnegative for q>=2. This is an identity of polynomials, with
no division by a,b,w,p or any field-valued point.

Thus

    G_N(x)=G_d(x)^(q^2+1)+(G_d(x)+1)^d.                  (21)

Each side lies in F2[x^2+x]. The substitution F2[U]->F2[x] is
injective by leading degree. Consequently (21) is precisely (3):

    g_N(U)=g_d(U)^(q^2+1)+(g_d(U)+1)^d.

CP1 now proves the WHOLE homogeneous divisibility phi_d|phi_N over
F2. No counting of absolute components or assumption of their coefficient
fields has entered this proof.

## 5. Genuine factor degrees, integer lifts and both small-q endpoints

For every odd n>1, f_n has the mixed coefficient X^(n-1)Y equal to
one. It is nonzero; hence phi_n is nonzero homogeneous of degree n-3.
The universal composition quotient

    (B_q(A)+B_q(B))/(A+B) in F2[A,B]

is a polynomial. Substituting A=g_d(U),B=g_d(V), then the two quadratic
covers, and finally homogenizing through the invertible linear map
constructs an actual F2 cofactor of phi_d in phi_N. Section1 already
proved that no denominator or homogenizing-line factor is lost. As
the product is nonzero, the cofactor is nonzero homogeneous of degree

    (N-3)-(d-3)=N-d=q^3(q-1).                            (22)

The divisor has degree d-3=q^2-q-2. For q>=4 both are positive.
Lift the two F2 polynomials coefficientwise to integer polynomials by
choosing coefficients0 or1. These are neither constant modulo2 and
satisfy the exact coefficientwise congruence in the official part(b).
We do not assert that either factor is irreducible over F2 or absolutely.

At q=2, d=3,N=11. Equations(17)--(21) still hold, but phi3=1 and
its degree d-3 is zero. Thus no qualifying factorization of phi11 is
deduced. This agrees with the accepted irreducibility/exclusion context;
the unit endpoint is not an exception hidden in a degree claim.

At q=4, d=13,N=205. This is the previously published Hernando--McGuire
example and the accepted whole-phi13 factor. The present identity is
compatible with it, without reproducing its preliminary/exploratory
multivariate certificate or using it as a premise. The advertised new
family is q=2^k with k>=3. Its first member is N=3641,d=57, with
factor degrees54 and3584. That numerical instance is a corollary of
the unrestricted symbolic proof, not an extrapolation from its check.

Finally

    N_k-1=2^k(2^k-1)(2^(2k)+1),

so v2(N_k-1)=k. These valuations distinguish the infinitely many k.
Every accepted phi13-progression exponent n_m=(64*16^m+1)/5 has

    n_m-1=4(16^(m+1)-1)/5,

with an odd integer parenthesis quotient, hence valuation2. No N_k
with k>=3 equals an n_m. The accepted exact whole-phi13 criterion,
and ONLY that criterion for this comparison, excludes phi13 as a
divisor of every member of the new advertised family. CP3 follows.

## Attribution, finite corroboration and remaining gap

The coordinate change relating the original homogeneous quotient to
the affine APN collision quotient is classical; Hernando--McGuire
Section2.3 gives the equivalent birational formulation. The elementary
two-cover/free-module and polynomial-composition arguments are fully
proved above; no priority is asserted. The q-family proof uses only
the displayed characteristic-two identities. It does not import the
unread original Janwa--Wilson Kasami proof, the reproduced K1
factorization, Férard's inaccessible full theorem, or an exceptional-APN
classification. The accepted phi13 criterion is used only to state
disjointness from that known fixed-divisor progression. Published q4
attribution is explicitly retained.

One targeted univariate computation was used for intuition: q8,d57,
N3641 ONLY. It found an outer polynomial with support
0,1,8,9,16,17,24,25,32,33,40,41,48,49,56,57,65,
which is exactly T65+(T+1)^57 by Frobenius expansion. This suggested
(3), which was then proved for every q in (17)--(21). The saved child
also independently checks both G exponents by direct substitution in
x, not by finite-field point tests. PID95340 was externally capped at
10seconds, completed with return code0 in about0.024seconds including
launch, and reaped. Complete supports, job, output and completion are
saved under this prefix. They are finite corroboration and are NOT a
premise of CP1--CP3. No multivariate factorization, n205 rerun, routine
factor table or broad exponent scan was performed.

No full list of reducible phi_n is supplied. CP1 concerns whole fixed
divisors and does not imply every factor is another phi_d. The broader
family (q^(2m+3)+1)/(q+1) at arbitrary m is not proved here beyond
the accepted q4 progression and the all-q m1 identity. A separate
Artin--Schreier/S4 collision-curve analysis remains a later packet,
not a dependency or claim of this checkpoint. All old frozen bytes
remain unchanged. Obtain two other fresh WHOLE audits before any
coordinator promotion.
