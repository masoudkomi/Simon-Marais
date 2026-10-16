# Blind independent adversarial review R1: exact phi13 criterion v1

Review completed 2026-10-16. This is the initial blind report. I did not
construct the candidate, read another review, read shared issue/research
statuses, or import, inspect, or execute the author's construction or
verification scripts. Reading their bytes to verify frozen hashes was the
only access to those scripts. I reconstructed the whole argument and wrote
an independent exact checker.

**Review finding: no substantive objection found to the stated fixed-factor
criterion or its explicitly partial B4(b) consequence.** I recommend accepting
this as one independent audit. This report does not promote the candidate;
the coordinator must also resolve the second independent audit before any
promotion. No claim about a complete reducibility classification or novelty
is included in this finding.

Requested reviewer settings: `gpt-6.1-sol`, `max` reasoning. These are the
requested settings supplied with the assignment, not independently verified
effective backend settings; no effective-setting readback is available.
Authoritative account-wide usage was checked twice during this review:
weekly total used was 5%, in the 10080-minute window resetting at Unix
1792745187. No separately billed API was used.

## Frozen object and official scope

The exact reviewed candidate is
`notes/zero-automaton-criterion-v1.md`, SHA256
`59e3bb1f9aba8162ea5b79f0ccec5f56b6f2cb0cc7917cfe81f4aff196ff6ab4`.
The input manifest SHA256 is
`41fef0ca55da72d8efc8fb04f3b0180f77fc43edf28b276a87f7bd033b6687f2`.
Every file hash listed in that manifest was independently recomputed and
matched. In particular, the readable certificate hash is
`b384ed3c0b51572e729b1e5486847ebcc5d964f4afa64c43e60a76910ad0ddd3`,
and the raw graph hash is
`ee818f60e68da70ae2f0f7fa84a2c4dec740d10d03908359a271e354a1a0ce4e`.

I opened the [official 2024 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf)
online, read the relevant B4(b) wording and definitions, and visually checked
the relevant material on page 2 of the cached official paper. The cached
PDF SHA256 is
`1401f21218ad4c387c4d537ed8fd7de119b376cba52957ef788c772dc5ab4ddc`.
The original PDF and rendered page remain in ignored `.cache/official/`.
This review did not investigate B1-B3 or solve/reproduce preliminary (a).

The official domain is positive odd integers n, with coefficientwise
congruence of integer polynomials modulo 2 and both additional factors
nonconstant modulo 2. Passing to F2[x,y,z] preserves precisely this
interpretation. For odd n>=3, define

    f_n=x^n+y^n+z^n+(x+y+z)^n,
    R=(x+y)(y+z)(z+x),   phi_n=f_n/R.

The reviewed statement is exactly

    phi_13 | phi_n  in F2[x,y,z]
       iff n=(64*16^m+1)/5 for some integer m>=0,
    for odd n>=3.

It is intentionally a criterion for divisibility by the whole fixed
polynomial phi_13. It asserts neither that all reducible phi_n have that
factor nor that all factors after substitution descend individually. The
case n=13 has cofactor 1 and hence this criterion alone gives no B4(b)
factorization there. The candidate states these limitations correctly.

## Reconstruction of the generating algebra

Put w=x+y+z, Q=x^2+y^2+z^2+xy+yz+zx, D=xyzw. The elementary symmetric
coefficients of x,y,z,w are 0,Q,R,D, so

    E(t)=(1+xt)(1+yt)(1+zt)(1+wt)
        =1+Qt^2+Rt^3+Dt^4.

Over characteristic 2, differentiation gives tE'(t)=Rt^3. Expanding
a*t/(1+a*t) as a geometric formal series for each of the four a's gives

    sum_(n>=1) f_n*t^n=Rt^3/E(t).

All denominators have constant coefficient 1, so these calculations take
place in the ordinary formal power series ring T[[t]], T=F2[x,y,z]. In
particular the series coefficients provide polynomial quotients by R.
Since E^2=1+Q^2*t^4+R^2*t^6+D^2*t^8 has only even exponents, the even
t-section of E/E^2 has numerator 1+Qt^2+Dt^4. With s=t^2 this proves

    sum_(j>=0) phi_(2j+3)*s^j
      =(1+Qs+Ds^2)/(1+Q^2s^2+R^2s^3+D^2s^4).

Define P_j in the independent polynomial ring S=F2[q,u,d] by the same
rational expression with Q,R^2,D replaced by q,u,d. Direct coefficient
comparison gives

    P_0=1, P_1=q, P_2=q^2+d,
    P_j=q^2*P_(j-2)+u*P_(j-3)+d^2*P_(j-4)  (j>=3),

where negative indices are zero. The recurrence at j=2 includes its
numerator term d. It yields

    P_5=q^5+q*d^2+u*d=A,
    phi_(2j+3)=P_j(Q,R^2,D), phi_13=A(Q,R^2,D).

The independent checker confirms the elementary symmetric identity, P_5,
and the exact finite identity R*A(Q,R^2,D)=f_13 by direct support
arithmetic. These are checks of stated finite algebraic identities; the
general generating-function derivation above is not inferred from samples.

## Localization and saturation audit

The coefficients of A, viewed as a degree-one polynomial in u over
F2[q,d], are d and q^5+q*d^2. Their gcd is 1: a common irreducible would
divide d and hence q^5, which is impossible. Thus A is primitive and is
irreducible over F2(q,d)[u]. Gauss's lemma applies over the UFD F2[q,d],
so A is irreducible in S. Since S is a UFD, A is prime. Its positive
u-degree prevents it from dividing q or d.

In U=S[q^-1,d^-1], A=0 is equivalent to

    u=q^5/d+q*d.

Eliminating u therefore gives precisely F2[q,q^-1,d,d^-1], with no
additional relation. Set b=d/q^2, another invertible independent
coordinate. Then d=q^2*b and u=q^3*(b+b^-1). Substituting s=z/q yields

    F(z,b)=(1+z+b*z^2)/K(z,b),
    K(z,b)=1+z^2+(b+b^-1)*z^3+b^2*z^4.

Its z^j coefficient is the localized image of q^-j*P_j. This coefficient
belongs to Lambda=F2[b,b^-1], whose embedding in
F2[q,q^-1,b,b^-1] is injective. Consequently it is zero exactly when
P_j belongs to A*U. Clearing denominators gives q^a*d^b*P_j in (A),
with a,b>=0. Primality and A not dividing q or d then give P_j in (A).
This proves the two-sided equivalence

    A | P_j in S  iff [z^j]F=0 identically in Lambda.

The localization does not silently discard any additional global
polynomial divisibility cases at q=0 or d=0. Saturation is precisely the
needed argument. No testing of b at finitely many field values is used.

## Laurent formal series and Cartier invariant

Work in Lambda[[z]]. Every coefficient is a finite Laurent polynomial in
b, although its exponent bounds can grow with z-degree. This is enough:
at any fixed z-degree all Cauchy convolutions use finitely many terms,
and K is a unit because K(0,b)=1.

For residues r,t in {0,1}, let C_(r,t) retain terms whose z and b
exponents have those residues and replace (i,h) by
((i-r)/2,(h-t)/2). Negative h causes no ambiguity; parity is its residue
modulo 2. For example, starting from b^-1, the independent checker obtains

    C_(0,0)(b^-1*K)=0,
    C_(0,1)(b^-1*K)=b^-1+z*b^-1+z^2,

in agreement with certificate columns 0 and 529. This checks the negative
exponent convention directly.

Characteristic 2 gives K(z,b)^2=K(z^2,b^2). A series involving only even
z and b exponents can be pulled through C with both arguments halved.
Applying this coefficientwise to

    N/K=N*K/K(z^2,b^2)

proves C_(r,t)(N/K)=C_(r,t)(N*K)/K. This argument is legitimate for
Laurent coefficients, including the inverse denominator; it requires no
uniform lower bound on b-exponents across all z-degrees.

Let V have F2 basis z^i*b^h for 0<=i<=3 and -1<=h<=2. Products N*K
have 0<=i<=7 and -2<=h<=4. Selecting either parity and halving gives
0<=i<=3 and -1<=h<=2 again. Thus the four maps
L_(r,t)(N)=C_(r,t)(N*K) are genuinely endomorphisms of this
16-dimensional F2-vector space. The numerator 1+z+b*z^2 belongs to V.

The zero test needs the conjunction of both b-parities: a Laurent
polynomial h(b) uniquely decomposes as h_0(b^2)+b*h_1(b^2), whose
supports have distinct parity. It is zero iff both h_0 and h_1 are zero.
For a subspace W define

    T_r(W)=span_F2{L_(r,0)(N),L_(r,1)(N):N in W}.

Since coefficient extraction divided by K is F2-linear, requiring
vanishing for each image generator is equivalent to requiring vanishing
for every vector of this span. This proves, for every a>=0,

    [z^(2a+r)](N/K)=0 for every N in W
      iff [z^a](M/K)=0 for every M in T_r(W).

Inducting from W_start=span(1+z+b*z^2) gives exactly the candidate's
invariant after least-significant-first bits r_0,...,r_(k-1):

    [z^(2^k*a+ell)]F=0
      iff [z^a](N/K)=0 for every N in reached W,
    ell=sum_(h<k) r_h*2^h.

At a=0, K(0,b)=1 makes acceptance equivalent to zero bottom four
numerator coordinates on every basis vector. Thus the conjunction,
acceptance rule, and bit order are all justified. Leading zeros append
zero bits on the reading side and preserve the represented coefficient.

## Independent finite certificate and accepted language

My checker derives every map by multiplying finite Laurent supports and
selecting parities. It builds reachable subspaces from their COMPLETE
sets of vectors, using support symmetric difference, without Gaussian
elimination. The raw certificate is read only after this construction for
comparison. The independently obtained graph has exactly 48 distinct
states, all 96 outgoing transitions closed, six accepting states, and
maximum full subspace size 64. Dimension multiplicities are

    dimension: 1  2  3   4   5  6
    count:     1  3  9  17  12  6.

All 64 operator columns, all subspaces, every transition, every output,
and both tables in the readable certificate match. I additionally check
the claimed reduced-basis conditions and the exact eight quotient classes,
including every listed class member. Independent refinement also yields
these eight classes; minimality is not needed for the proof.

The quotient forces the initial path S--1-->A--0-->B--1-->C. After
reaching C, any sequence with a future 1 must traverse

    C--0-->D--0-->E--1-->B--1-->C,

or it enters the rejecting sink. Any final sequence of zero bits stays
accepting from C through D,E,Z. Hence all finite accepted words, in reading
order, are exactly

    101(0011)*0*.

To challenge both language inclusions independently, my checker constructs
an epsilon NFA directly from that regex and exhaustively checks the closed
reachable product with the independently built 48-state machine. All
reachable product outputs agree. This is an all-word finite equivalence
check, not a scan up to a chosen word length. The literal regex subset
machine has nine states because its initial-prefix B and repeated-block B
are equivalent but distinct before minimization; its product has 48
reachable states. This is consistent with the eight-state minimal quotient.

A positive integer's canonical least-significant-first word ends in 1, so
the final zero suffix must be empty. The accepted indices are therefore

    j=5+sum_(h=0 to m-1) 12*2^(3+4h)
     =(32*16^m-7)/5,  m>=0.

The empty word j=0 is rejected. No canonical zero word can match the
language's initial 1. The initial block is 101=5 and each repeated block
is 0011, with local value 12; these checks rule out reversed digit order.

It follows for ALL j>=0 that

    A | P_j in S  iff j=(32*16^m-7)/5, m>=0.

The independent direct Laurent recurrence also agrees with the machine
for 0<=j<=65535, where the only zero coefficients occur at
5,101,1637,26213. This finite scan is supplementary evidence only.

## Reverse divisibility: full descent audit

This is an essential logical step, and I find its hypotheses satisfied.
Let iota:S->T map (q,u,d) to (Q,R^2,D). In lexicographic order x>y>z,
the leading monomials are

    x^2, x^4*y^2, x^2*y*z.

The independent finite support calculation confirms them. More directly,
the image of q^a*u^b*d^c has leading exponent vector

    (2a+4b+2c, 2b+c, c).

Equality of two such INTEGER vectors first forces equality of c, then b,
then a. Thus distinct monomials of S have distinct image leading
monomials. In a nonzero polynomial image the largest such monomial cannot
be canceled by any term from a summand with smaller leading monomial.
This proves injectivity. The exponent determinant is 4 over the integers;
reducing it modulo characteristic 2 would be inappropriate. The argument
requires no separability or nonzero Jacobian.

For each a=x,y,z, the four-root polynomial gives

    a^4+Q*a^2+R*a+D=0,
    a^8+Q^2*a^4+R^2*a^2+D^2=0.

The second relation is monic over iota(S), including its R^2 coefficient.
It proves x,y,z integral over S. These exact identities also passed the
independent support check. Because T=S[x,y,z], reducing each exponent by
these monic degree-eight relations shows that T is generated over S by
the 512 monomials x^a*y^b*z^c with 0<=a,b,c<8. They need not form a
basis. A finite algebra generated by integral elements is integral, or the
determinant trick on this spanning set proves every element of T integral.
All required finiteness hypotheses therefore hold.

S is a polynomial ring over a field and hence a UFD and integrally closed
in Frac(S). For clarity, the latter implication uses no geometric
smoothness assertion: if a reduced fraction p/q satisfies a monic
equation, multiplying by q^k implies q divides p^k, so coprimality in the
UFD makes q a unit.

Now suppose phi_13 divides phi_(2j+3) in T and write the quotient H in T.
By the generating identities and injectivity, this same element in Frac(T)
is P_j/A in the embedded subfield Frac(S). Since H is in T it is integral
over S, and since it is in Frac(S), integral closedness forces H in S.
Thus P_j=A*H in S. Conversely a formal divisibility in S substitutes to
the required divisibility in T. This establishes both directions with no
unmentioned invariant-ring assertion:

    phi_13 | phi_(2j+3) in T iff A | P_j in S.

In particular it is enough that S is this normal polynomial subring and
T is integral over it; S need not be identified with a full invariant
ring. Possible splitting of A after extension to T does not invalidate
descent of the quotient by the WHOLE A. No specializations of x,y,z are
used.

Combining descent with the accepted indices gives

    n=2j+3=(64*16^m+1)/5, m>=0.

These are odd integers: 16^m=1 modulo 5 gives divisibility by 5 of the
odd numerator. All are at least 13. This completes my reconstruction of
the criterion, including its necessary direction.

## Boundary and consequence checks

- n=1 is outside the theorem. Indeed f_1=0, so extending the fixed-factor
  criterion to it would be false because every polynomial divides zero.
  In the official B4(b) question n=1 is excluded because R is nonzero and
  the reductions of nonconstant g,h are nonzero in the domain T.
- n=3 has phi_3=1 and j=0, correctly rejected.
- n=13 is the first accepted exponent, with quotient 1. The note explicitly
  does not claim this is a factorization into two nonconstant factors.
- For every odd n>1, the coefficient of x^(n-1)*y in f_n is 1; no other
  pure-power summand contributes to it. Thus f_n and phi_n are nonzero.
  Homogeneity gives degree(phi_n)=n-3 and degree(phi_13)=10. At the
  accepted n with m>=1 the quotient has positive degree n-13 and therefore
  gives two nonconstant F2 factors. Coefficientwise integer lifts meet
  the official congruence condition.
- Rejection by this automaton excludes only divisibility by the whole
  phi_13. It does not establish irreducibility, exclude other factors, or
  solve the full open classification. The candidate keeps this distinction.

The reference to published work is explicitly contextual and the candidate
claims no novelty. No external automaton theorem, APN classification,
uninspected fixed-factor theorem, or earlier family audit is needed in
the reconstructed argument. I have not audited those literature claims
for priority or attempted a priority comparison.

## Reproduction and checker-development record

From the repository root, run

```sh
.venv/bin/python -u problems/2024-B4/reviews/criterion-review-1-check.py
```

The default harness launches its own identified child, gives it 45 seconds,
records the PID before waiting, and writes incremental checkpoints. It
terminates only that child if necessary. The final job used Python 3.12.14
and the standard library only; PID 16829 completed with exit 0 in
0.4935338750074152 seconds including launch and was reaped. The child
reported 0.4523919159837533 seconds of work. Exact command, timestamps,
parameters, hashes, output and stderr are saved in the accompanying files.
No cap or timeout was reached and no job remains running.

The first checker attempt wrongly asserted that the unminimized literal
regex subset machine had eight states. All preceding algebra, 48-state
graph, quotient, and product-output agreement checks had passed; the
assertion failed because the literal NFA retains two equivalent B states.
I corrected this reviewer-code assumption, kept output agreement on every
reachable product state as the language-equivalence test, and reran the
whole checker successfully. The failed script, job, output, and traceback
are preserved as `criterion-review-1-attempt-1-*`. This was a checker
development error, not a substantive objection to the candidate.

No author file, existing review, shared issue log, source inventory, or
research status was edited. Review artifacts alone were created, plus the
ignored rendered official page. No Git commit or push was made. The own
issue log records all challenged points as resolved, with no substantive
candidate issue remaining from this audit.
