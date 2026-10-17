# Fresh initially blind whole audit R2: CP1–CP3

2026-10-17 UTC. Reviewer `review_2021_reasoning_j15_r2`. This is an
independent whole review of the new frozen composition/family packet,
not an author repair or a promotion. Requested settings are
gpt-6.1-sol/max; no independent effective-setting readback is available.

**Recommendation:** no substantive defect found in the complete stated
CP1–CP3 argument. The proof gives an unrestricted whole-divisor criterion
and the stated infinite qualifying family; it does not classify all
reducible exponents. The coordinator must reconcile two independent
audits before any promotion.

The audited main file has 15010 bytes and SHA256
`cff70e9b104a48613712d0f2920157f29a5c20b56fb26055de829984e11fb021`.
The constructor's 15-artifact freeze has SHA256
`e2c1b451f486db75597fbd6b99c970f85a7ed70528bebd032e2d7168fbcf7741`.
The whole main proof, obligations, source audit, research log, failed
routes, source metadata and finite corroboration records were read.
Input and older-file checks are separately frozen with this report.

## Independence and precise premises

I did not construct or contribute the new invariant-ring/composition
criterion, Frobenius identity, infinite family, target computation or
their repair. I authored the older T1–T4 and C7/C11 packets. Those older
results are contextual here, and I do not count this review as a fresh
review of my own earlier work. Neither old packet is needed for the
CP1–CP2 proof or the qualifying-factor construction in CP3. The already
accepted exact whole-phi13 theorem is used only for CP3's exclusion of
that particular divisor; I read its full accepted statement/proof and
acceptance scope without rerunning its finite machinery. Accepted
existence of the ordinary quotient phi_n is background, not a new
preliminary-part argument.

No peer CP review, conclusions or proposed repairs were read before this
complete initial freeze. No substantive finding was sent to the author
or coordinator before it. Only the assigned review prefix was written.
I used no mathematical program, CAS, factor scan, author-code rerun or
new native network download. The only Python execution in this audit is
the administrative hashing/freeze script. My separately frozen 2017
construction is unrelated and supplies no premise.

## 1. Official domain and boundary

I checked B4(b) against the [official 2024 Paper B, p.2](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf).
The target concerns positive odd n and coefficientwise congruence for
integer polynomials, with both additional factors nonconstant modulo 2.
Thus genuine positive-degree factors in F2[X,Y,Z] suffice by choosing
integer coefficients 0 or 1. Equality of functions on F2 cubed would not
suffice and is never used.

At n=1 the numerator is zero. Both qualifying factors would be nonzero,
and their product with nonzero R cannot vanish in this domain. At n=3
the established quotient is the unit. These endpoints are excluded,
rather than called irreducible. CP1 itself explicitly starts at odd
d,n>=3 and permits its unit divisor. No preliminary-part proof is
reproduced.

## 2. Reconstruction of the invariant and homogeneous reductions

Write U=x^2+x and G_n(x)=x^n+(x+1)^n. Reduction using x^2=x+U
expresses every polynomial as A(U)+xB(U). If nonzero, the two summands
have even and odd leading x-degrees, respectively; hence this expression
is unique. Translation x to x+1 preserves U and sends it to
A(U)+xB(U)+B(U). Its invariants are therefore exactly F2[U]. This gives
the unique g_n with G_n=g_n(U), without division by the group order.

For odd n>=3 the top x^n terms cancel in G_n and its coefficient of
x^(n-1) is n=1 in F2. Consequently g_n is monic of degree
e_n=(n-1)/2, and g_n(0)=G_n(0)=1. In particular it is nonconstant even
at n=3. The quotient

    Q_n(U,V)=(g_n(U)+g_n(V))/(U+V)

is a polynomial. Its highest homogeneous part is
(U^e_n+V^e_n)/(U+V), which is nonzero of degree e_n-1. This remains
true when e_n is even or a power of two: a repeated diagonal factor is
not the zero polynomial. For n=3, Q_3=1.

The homogeneous map (X,Y,Z)=(s+u,s,t) is linear and invertible, with
inverse (s,t,u)=(Y,Z,X+Y). At u=1 its numerator is G_n(s)+G_n(t).
Its denominator R is (s+t)(s+t+1), equal to U+V after
U=s^2+s,V=t^2+t. Cancelling the defining polynomial identity in a
domain proves

    Psi_n(s,t)=phi_n(s+1,s,t)=Q_n(s^2+s,t^2+t).

This uses no division by the value of s, t, s+t or s+t+1. Zero values
and the diagonal are not discarded.

Distinct top-degree monomials U^a V^b have distinct top pullbacks
s^(2a)t^(2b); lower-degree monomials cannot reach their doubled degree.
Hence deg Psi_n=2(e_n-1)=n-3, the full homogeneous degree. If
Phi_n(s,t,u)=phi_n(s+u,s,t), then Phi_n is exactly the degree-(n-3)
homogenization of Psi_n and u does not divide it. No component on u=0
is missing.

If Psi_n=Psi_d C, nonzero products have additive total degrees, so
deg C=n-d. Homogenizing this equality gives Phi_n=Phi_d C^hom with
exact matching degrees. The inverse linear map gives phi_d|phi_n.
The forward implication follows by substituting into a polynomial
factorization. Thus BOTH divisibility directions hold, including the
unit and equality cases; n<d with d>=5 fails by degree.

## 3. Rank-four descent applies to whole polynomials

Let S=F2[U,V] embedded in A=F2[s,t] through the same substitution.
Monic quadratic reductions give the spanning set 1,s,t,st. For
independence, the leading exponent pair of
U^a V^b s^epsilon t^delta is (2a+epsilon,2b+delta). These are distinct
as the four integers vary with epsilon,delta in {0,1}. Choosing the
largest leading monomial in a finite purported relation rules out
cancellation. This also verifies injectivity S into A.

Accordingly A is free, and faithfully free, of rank four over S. If
nonzero A0,B0 in S satisfy B0=A0 C in A, expand
C=C00+sC10+tC01+stC11. Uniqueness forces A0 C10=A0 C01=A0 C11=0.
The domain S and A0 nonzero force all three coefficients to vanish;
therefore C is in S. The converse divisibility direction is immediate.
This proves contraction of the whole principal divisibility relation.
It does not say that every factor after a quadratic substitution lies
in S, nor that one may descend an individual absolute factor.

Applied to Q_d,Q_n, both nonzero, it proves

    phi_d|phi_n  iff Q_d|Q_n in F2[U,V].

No averaging, finite-point test, separability, normality assertion or
specialization away from U=0,V=0 is required.

## 4. The h-adic equivalence, including inseparable cases

For monic h of degree e>=1, repeated monic division gives

    p(U)=sum_(0<=j<e) U^j C_j(h(U)), C_j in F2[T].

This is finite because the successive quotient degrees drop. The
leading degrees e*deg(C_j)+j for distinct nonzero summands are distinct
modulo e, so the expansion is unique.

Over F2[V], divide p(U)+p(V) by the monic polynomial h(U)+h(V) in U.
The remainder is exactly

    sum_(0<=j<e) U^j C_j(h(V)) + p(V),

whose U-degree is less than e. A zero remainder forces
C_j(h(V))=0 for j>=1. Since h is nonconstant, composition with it is
injective by leading degree. Therefore C_j=0 for j>=1 and
p=C_0 composed with h. Conversely p=H composed with h gives
divisibility by h(U)+h(V) using the elementary difference-of-powers
identity. The coefficient field stays F2. Constant p, e=1 and a
vanishing derivative of h cause no exception to this argument.

For h=g_d,p=g_n, multiply Q_d,Q_n by the SAME nonzero U+V. A quotient
of the two differences is a quotient of Q_n by Q_d after cancellation
in the domain, and conversely. No claim that U+V is coprime to Q_d is
made or needed. Combining this with sections 2–3 gives the exact CP1
equivalence for all odd d,n>=3.

Because g_n is nonconstant, its outer H is nonconstant. Degree
multiplication gives deg H=(n-1)/(d-1) and the claimed necessary
integer divisibility. If n=d, leading degree and constants give H=T.
If d=3, g_3=T+1, so every g_n equals H(g_3) with
H(T)=g_n(T+1), in agreement with phi_3=1. For n=3,d>3 the degree
obstruction prohibits composition and divisibility. For d>=5,n>d,
the degree ratio is at least two and both homogeneous factor degrees
are positive. This is a whole-divisor classification, not a
classification of every irreducible factor of phi_n.

## 5. Independent all-q reconstruction of CP2

Let q=2^k with k>=1, d=q^2-q+1 and
N=q^4-q^3+q^2-q+1. Multiplying N by q+1 gives q^5+1 over the
integers, so the displayed quotient is an integer. Both d and N are
odd. Put a=x,b=x+1, so a+b=1, and write
c=a^d+b^d, p=a^(q-1)+b^(q-1), w=ab.

The four terms of wp^(q+1), obtained using the q-th Frobenius, are

    a^(q^2)b, a^d b^q, a^q b^d, a b^(q^2).

Upon adding c, the two middle terms pair with a^d,b^d to give
a^d(1+b^q)+b^d(1+a^q)=a^(q^2+1)+b^(q^2+1).
The remaining two terms then group with these to give
a^(q^2)(a+b)+b^(q^2)(a+b)=1. Hence

    c+1=wp^(q+1).

I checked each needed integer exponent identity independently:

    d(q^2+1)=q^4-q^3+2q^2-q+1=N+q^2;
    q^2-d=q-1;
    N-d=q^4-q^3=q^3(q-1);
    d(q^2-1)=q^4-q^3+q-1=(q^3+1)(q-1);
    d(q+1)=q^3+1.

The q^2-th Frobenius expands c^(q^2+1) into four terms. The pure
powers a^(d(q^2+1)),b^(d(q^2+1)) combine with a^N,b^N to become
a^N b^(q^2),b^N a^(q^2), since 1+a^(q^2)=b^(q^2). The two remaining
cross terms are a^(dq^2)b^d and b^(dq^2)a^d. Factoring w^d leaves
exactly

    a^(q^3(q-1)) b^(q-1) + b^(q^3(q-1)) a^(q-1)
       +a^((q^3+1)(q-1))+b^((q^3+1)(q-1)).

These are the four terms of p^(q^3+1); q^3 is again a Frobenius
power. The result is

    c^(q^2+1)+G_N=w^d p^(q^3+1)
                     =(wp^(q+1))^d=(c+1)^d.

Every exponent factored off is nonnegative for q>=2. This proof
never divides by a, b, w, p or their evaluations. Consequently it
holds as a polynomial identity at their zeros as well.

The injection F2[U] into F2[x] now gives

    g_N(U)=g_d(U)^(q^2+1)+(g_d(U)+1)^d=B_q(g_d(U)).

B_q is monic of degree q^2+1, since d<q^2+1. This degree agrees with
(N-1)/(d-1). CP1 gives the whole homogeneous F2 divisor phi_d. No
assertion about the absolute Kasami factors or their orbit lengths
has been used. This completes an unrestricted proof for every k>=1.

## 6. CP3, coefficient lifts and the two q endpoints

For odd n>1 the mixed numerator coefficient X^(n-1)Y is n=1 in F2,
so the numerator and its established quotient are nonzero. The latter
is homogeneous of degree n-3. CP1–CP2 therefore give a nonzero
cofactor of degree N-d=q^3(q-1), while the divisor has degree
d-3=q^2-q-2. Both are positive for q>=4. Homogenization constructs
actual polynomials and loses no u factor. Their coefficientwise 0/1
integer lifts satisfy the exact official congruence. Neither needs
to be irreducible over F2 or absolutely.

At q=2 the identity has d=3,N=11 and a unit whole divisor. The
construction explicitly withholds a qualifying factorization there.
At q=4 it has d=13,N=205, with the published reducibility example
attributed to Hernando–McGuire and the accepted whole-phi13 result
retained as context. The old205 certificate is not rerun. The family
advertised beyond that endpoint starts at k=3: d=57,N=3641, factor
degrees 54 and 3584. These values follow from the symbolic proof.

For every k>=3,

    N_k-1=q(q-1)(q^2+1),  q=2^k,

and the last two factors are odd. Thus v2(N_k-1)=k; different k give
different N_k. The accepted exact whole-phi13 criterion says precisely
that its odd exponents >=3 are n_m=(64*16^m+1)/5 for m>=0. Since

    n_m-1=4*(16^(m+1)-1)/5,

and the indicated integer quotient is odd, each has valuation 2.
Every advertised N_k is outside that progression. Exact necessity in
the accepted theorem therefore gives phi13 not dividing phi_(N_k).
A merely sufficient old progression would not justify this last step;
the actual imported theorem is the accepted iff. This comparison
alone uses it, and excludes only that whole divisor.

## 7. The one q8 corroboration and adversarial probes

I read the exact checker, harness, full saved certificate and the
job/completion/stdout records. I did not execute either author script.
Their recursive power-sum identities have a separate hand derivation:
for roots a+b=1,ab=U, put P_n=a^n+b^n. Then P_0=0,P_1=1,
P_(2m)=P_m^2 and P_(2m+1)=P_m P_(m+1)+U^m; the cross terms of
the product sum to U^m(a+b). This matches the returned adjacent pair
in `dickson_pair`. XOR multiplication and squaring encode exact
polynomials, not function values. The saved direct check substitutes
U=X^2+X and compares full polynomial supports with (X+1)^n+X^n.

As a hand check independent of leading-term extraction, the binary
expansion 57=32+16+8+1 gives

    (T+1)^57=(1+T^32)(1+T^16)(1+T^8)(1+T),

whose support is {8j,8j+1:0<=j<=7}. Adding T^65 gives exactly the
17 outer terms in the record. The recursion also gives

    P_14 support {0,2,6}; P_15 support {0,1,3,7};
    P_28 support {0,4,12};
    P_29 support {0,1,2,5,6,13,14};
    P_57 support {0,1,2,4,9,10,12,25,26,28},

matching the recorded inner polynomial. The direct X support at
3641 is obtained from
3641=2048+1024+512+32+16+8+1: it consists of the subsets of those
seven powers, with the top exponent removed. It is the eight blocks
512j+{0,1,8,9,...,56,57}, 0<=j<=7, minus 3641, matching the listed
127 terms. I do not claim to have independently rerun every large
bit-product in the certificate.

The saved harness records PID95340, parent95339, an external10-second
timeout, return0, no timeout, explicit reap, empty stderr and about
0.02443 seconds total. Its output hashes match the saved files. These
are preserved historical records, not a live process observation by
this reviewer. The targeted q8 certificate and its extraction support
are finite corroboration only; the proof in section5 stands without
them. There was no broader scan in the reviewed checker.

I specifically challenged the most plausible failure points: a
missing dehomogenizing-line factor; cancellations in the rank-four
basis; failure of quotient descent; inseparable/repeated diagonal
differences; use of an extension-field H; negative exponents at q=2;
division at the zeros of w or p; a unit divisor advertised as genuine;
and exclusion by a sufficient rather than exact phi13 criterion.
The complete arguments above address each. I found no counterexample
or unresolved inference within the stated scope.

## 8. Source boundary, outcome and preservation

The classical coordinate context is attributed to
[Hernando–McGuire, §2.3](https://arxiv.org/pdf/0903.2016v4).
Their absolute-component conclusions do not decide whole-polynomial
F2 reducibility. This new proof supplies its own invertible linear
coordinates, free-module descent and all-q algebra. No uninspected
original Janwa–Wilson proof, Férard full theorem or monodromy
classification is a premise. Detailed actual passage checks and cache
fingerprints are in the source record.

No arbitrary-m extension, complete classification, absolute-factor
list, novelty or full official solution is established. Failure of
all whole-divisor tests would not prove irreducibility. These limits
are correctly explicit in the candidate and failed-route record.

The per-inference ledger addresses all 16 constructor obligations.
There is no required author repair in this initial audit. The freeze
verifies all 15 current constructor artifacts, declared older author
records and all 33 prior own packets, including the immediately prior
G4 audit, without changing any. Latest direct authoritative telemetry
is 30% total weekly use, reset1792745187, with a90%-total ceiling and
integration reserve. Only the coordinator may promote the scoped
results after the other independent whole audit is reconciled.
