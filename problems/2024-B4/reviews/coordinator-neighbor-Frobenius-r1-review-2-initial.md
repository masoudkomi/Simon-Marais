# Neighbor-Frobenius: complete initially blind WHOLE R2

18 October 2026 UTC. Reviewer B, `/root/review_2022_complexity_r2`.
**Candidate proof - unverified.** This is an independent whole initial,
not coordinator acceptance. I did not construct the NEW NF argument.

I reconstructed NF1--NF3, all36 obligations and the complete seven-file
constructor packet. I found **no substantive defect requiring repair**.
The local calculations in BOTH arithmetic branches exclude shared zeros
off the ordinary point, and the final projective degree contradiction
is valid without an assumption that every component passes that point.
Four retained scope notes are recorded separately. No NEW A NF report,
finding, ledger, source record, manifest or metadata was opened through
the ENTIRE initial freeze. Root is sole NEW constructor and excluded
from the two independent reviewer count.

Exact main: `notes/coordinator-neighbor-Frobenius-r1-candidate-v1.md`,
13799bytes, SHA256
`775501d763a46b8411a6509c7da06d3a7fc3dacb3b27141881b80de2ea37f9d4`.
Exact constructor freeze:2492bytes, SHA256
`f97a4dc9eb21dea3e4e4e94d42ba7f3bdf09ddf3555e2defcab19c4ec5812671`.
Requested gpt-6.1-sol/max; independent effective readback unavailable.

## 1. Domain, independence and precise conclusions

The actual official PaperB page2 asks in(b) about coefficientwise
integer-polynomial congruence modulo2, with BOTH reduced factors
nonconstant. Thus the established quotient phi_n must split into two
positive-degree F2 polynomials. It is not a question about polynomial
functions on eight points. A factorization over the algebraic closure
alone does not suffice, whereas whole absolute irreducibility does
exclude the official factorization. I used the accepted quotient
normalization as context and did not reproduce the preliminary(a).

The new theorem assumes a>=2, q=2^a, ell>=3 odd, n=q ell+1, and either
ell|(q-2) or ell|(2q-1). It asserts absolute irreducibility of the WHOLE
positive-degree quotient, not merely existence of an absolute component.
Here n>=13, N=n-3=q ell-2>0, so zero/unit quotient endpoints do not enter
the assertion. Neither ell1 nor q2 is silently included. For a2 the
first alternative has no eligible ell; that vacuity causes no problem.

Because ell is odd, ell|(q-2) is equivalent to
ell|(2^(a-1)-1); the other condition is literally
ell|(2^(a+1)-1). The coprimality needed later is exact, including
composite ell: any common divisor with q-1 divides either the difference
between q-1 and q-2, or (2q-1)-2(q-1). Both differences are1. A
nontrivial ell-root cannot therefore lie in F_q.

My earlier roles include whole reviews of the accepted structural,
sector3, GK/CP/other local packets and both three-bit submissions. Those
are disclosed context, not a fresh independent recertification of old
own work. Their current acceptance scopes were read. The NEW NF proof
does not use T1, S3B or the three-bit theorem as a mathematical premise;
every special calculation is supplied and reconstructed here. The old
narrower three-bit submission is not upgraded by this audit. I received
no new proof inference from root in this generic assignment.

## 2. Local lemma, squarefreeness and homogeneous factors

For a local series H with first piece c L^m and next homogeneous piece
not divisible by L, suppose H=AB with both constant terms zero. Their
orders s,t are positive and sum to m. Since K[x,y] is a UFD, their
initial forms are scalar multiples of L^s and L^t. The next product
piece is A_s B_(t+1)+A_(s+1)B_t. Both summands have a factor L,
contradicting the given next piece. This proves the required
unit-cofactor conclusion. The conclusion persists under multiplication
by a unit or an invertible local coordinate change. A high total
multiplicity alone would not prove it; the next piece is indispensable.

With W=X+Y+Z, formal differentiation in characteristic2 gives

    f_X=(X^ell+W^ell)^q,   f_Y=(Y^ell+W^ell)^q.

Each base form splits into distinct lines since ell is odd. A line in
the first list has coefficient vector(1+zeta,zeta,zeta), and one in the
second has(eta,1+eta,eta), for nonzero ell-roots zeta,eta. Proportionality
would give from Z that zeta=c eta, and from X that1+zeta=c eta. This
is impossible even at zeta1 or eta1. Thus the partials are coprime.
Every repeated irreducible factor of f divides both derivatives,
including when its exponent is divisible by2 and its own derivative
term vanishes. Hence f is squarefree, and its quotient phi is squarefree.

The coefficient X^(n-1)Y in f is1, because n is odd. The numerator and
quotient are nonzero. A factorization of a nonzero homogeneous polynomial
has homogeneous factors: minimum and maximum total degrees add in a
domain, so the degree spreads add and must both be zero. Consequently
any absolute splitting yields coprime homogeneous U,V with positive
degrees e,d, e+d=N. Grouping more than two absolute factors causes no
exception, and repeated factors were excluded globally rather than
assumed away at P.

## 3. Every possible projective common point

If U and V vanish at a point, their product phi and all its first
partials vanish there. The product f=R phi then has zero value and zero
first partials even on R0. In the chart Z1 put
lambda=alpha+beta+1. From f_X=f_Y0 and injectivity of qth powers,

    alpha^ell=beta^ell=lambda^ell=u.

Substitution in f0 gives
(alpha+beta+lambda)u^q+1=u^q+1=0. Therefore u=1. All three
quantities alpha,beta,lambda are NONZERO ell-roots.

They split into P=(1,1), the three diagonal cases alpha1, beta1,
alpha=beta, and off-diagonal triples with alpha,beta non1 and distinct.
At a diagonal other than P a coordinate permutation and nonzero
rescaling give(b:1:1), with b a nontrivial ell-root. For the alpha=beta
chart the rescaling can replace b by b^-1; this remains an allowed
nonzero root. No division by a vanishing root or by R is made here.

This is a projective argument. Symmetry of f,R,phi permits any nonzero
coordinate to be chosen as the normalized Z coordinate. If a singular
point had any zero coordinate, one of the other two normalized
coordinates would be zero, contradicting the conclusion above. Thus
there is no singularity with a zero coordinate, including all possible
points at infinity in the original chart. The common-zero set of U,V
has not lost any infinity contribution to Bézout.

## 4. Ordinary P and the complete diagonal calculation

At X=1+x,Y=1+y,Z1 the denominator is exactly xy(x+y). For any root z
with z^ell=1, the beginning of the translated numerator contribution is

    (z+t)^n = z+t+z^(1-q)t^q+z^-q t^(q+1)
              +terms of degree at least2q.

Indeed expand(z+t)(z^q+t^q)^ell, using the odd first binomial
coefficient. At z1 the constant/linear/qth-power pieces cancel in f.
The first remaining term is x^q y+x y^q, of degree q+1. Since
2q>q+1 for q>=4, no omitted term interferes. Division by the cubic
R gives order q-2 at P and cone

    C=(x^(q-1)+y^(q-1))/(x+y)
      = product_(b in F_q minus{0,1})(x+b y).

There are exactly q-2 distinct directions; none is x0, y0 or x+y0.
In phi=UV the two initial cones partition these distinct lines, hence
are coprime. The local intersection is m m', where m=m_P(U),
m'=m_P(V). If one factor misses P, its order and intersection
contribution are zero; this possibility is retained until the final
contradiction.

For a nontrivial diagonal root b let c=b+1, E=b^-q,
B=1+b^(1-q). All are nonzero: B0 would give b in F_q, excluded by
gcd(ell,q-1)1. Translate X=b+x,Y=1+y,Z1. Direct multiplication gives

    R=c²y+c y²+x²y+x y².

The root expansion above yields

    f_q=B y^q,
    f_(q+1)=y[E x^q+E x y^(q-1)+(1+E)y^q].

There are no lower nonzero positive pieces. The order-(q-1) quotient
piece is(B/c²)y^(q-1). Solving the degree-(q+1) product equation,
including R_2 times this preceding piece, gives

    phi_q=(E/c²)x^q+(E/c²)x y^(q-1)
             +[(1+E)/c²+B/c³]y^q.

The B/c³ term cannot be dropped. The nonzero x^q coefficient proves
that this next piece is not divisible by y. The local lemma then
excludes simultaneous vanishing of U,V. Coordinate symmetry covers
all three diagonal lines; P was already treated separately.

## 5. Off-diagonal expansion and first neighbor

Now alpha,beta,lambda,alpha+1,beta+1,alpha+beta are all nonzero.
R is a local unit, so a hypothetical shared zero factors f as(RU)V
with both factors still vanishing. Its two relevant pieces, by the
same root expansion, are

    H_q=A x^q+B y^q,
    A=alpha^(1-q)+lambda^(1-q),
    B=beta^(1-q)+lambda^(1-q),

    H_(q+1)=(alpha^-q+lambda^-q)x^(q+1)
             +(beta^-q+lambda^-q)y^(q+1)
             +lambda^-q(x^q y+x y^q).

No lower positive piece survives. We must prove that H_q is nonzero
with ONE distinct tangent and that the whole next piece misses it.
Neither an absence-of-off-diagonal-points claim nor a count of such
points is needed.

For ell|(q-2), the qth-power map agrees with squaring on the roots
alpha,beta,lambda and therefore on the finite field F they generate.
This field extension step is valid for sums, products and inverses;
it is not an inference about an arbitrary point of K. Write
u=alpha+1,v=beta+1. Then

    A=v/(alpha lambda), B=u/(beta lambda),
    D=A/B=beta*v/(alpha*u).

All displayed denominators and A,B,D are nonzero. The inverse of the
q-Frobenius automorphism on F supplies a t in F with t^q=D. Injectivity
of qth powers in K makes it the unique such root there too. Since
t belongs to F, t^q=t², so t²=D. Hence H_q=B(y+t x)^q. Because
B and A are nonzero, its sole tangent is represented by(1,t); no
vertical tangent is omitted.

Let h=H_(q+1)(1,t). On F, inverse qth powers are inverse squares, and
t^(q+1)=t³. Consequently

    lambda² h=v²/alpha²+(u²/beta²)t³+t+t²
       =v²/alpha²+D+t[uv/(alpha beta)+1].

The exact identity uv+alpha beta=lambda gives the t coefficient
lambda/(alpha beta). For the constant, placing v²/alpha²+D over
alpha²u gives v(uv+alpha beta)/(alpha²u)
=v lambda/(alpha²u). Thus

    lambda² h=lambda*[v/(alpha²u)+t/(alpha beta)].

If h0, cancellation of nonzero lambda,alpha,beta,u gives t=D=t².
The only roots of t²+t are0 and1. D nonzero rules out0. At t1,
beta(beta+1)=alpha(alpha+1), so with s=alpha+beta one has s²+s0.
s0 contradicts distinct alpha,beta; s1 makes lambda0. Both are
impossible. Therefore h is nonzero. The next piece is not divisible
by the unique tangent, and the local lemma eliminates this shared zero.

This is symbolic for every eligible composite or prime ell. When an
off-diagonal triple does not exist, its elimination statement is simply
vacuous. No field table or primitive-root assumption is used.

## 6. Second neighbor, keeping its Frobenius order separate

For ell|(2q-1), alpha^(2q)=alpha and likewise beta,lambda. This is a
different identity from t^q=t²; I do not substitute the first-branch
identity into this branch. Squaring the coefficients gives

    A²=alpha^(2-2q)+lambda^(2-2q)=alpha+lambda=v,
    B²=u.

Also(v^q)²=v and(u^q)²=u. Square injectivity therefore gives the
EXACT coefficients A=v^q,B=u^q, and H_q=(v x+u y)^q. Its single
tangent has t=v/u at x1, with u,v nonzero. Every rational expression
in alpha,beta,lambda belongs to their finite field fixed by the
2q-Frobenius. In particular t^(2q)=t; no square-root ambiguity or
extra scalar in the tangent is hidden.

Square the FULL next piece at(1,t), not only its pure terms. The
pure-y exponent becomes t^(2q+2)=t³, while the mixed terms become
t²+t^(2q)=t²+t. Since alpha^-2q=alpha^-1 and analogously for beta,
lambda, one obtains

    lambda h²=v/alpha+(u/beta)t³+t²+t
       =(v/u²)[u²/alpha+v²/beta+v+u].

Now u²/alpha=alpha+alpha^-1,
v²/beta=beta+beta^-1 and u+v=alpha+beta, so the bracket is
(alpha+beta)/(alpha beta). It follows that

    h²=v*(alpha+beta)/(lambda*u²*alpha*beta) !=0.

Every factor used to claim nonzero was explicitly excluded from zero
in the off-diagonal list. Thus h is nonzero. This branch too satisfies
the local lemma and excludes a shared factor zero, without a point
count or an unsupported conclusion from multiplicity q alone.

## 7. Whole Bézout contradiction, all degrees and omissions

Every projective common zero of coprime homogeneous positive-degree
U,V is now confined to P. Over the algebraically closed K, classical
projective Bézout applies, and disjoint cones at P give

    ed=sum_Q I_Q(U,V)=m m'.

If m or m' is zero, the right side is zero while ed>0. If both are
positive, the elementary local bounds m<=e and m'<=d imply
(m/e)(m'/d)=1 with both ratios at most1. Hence m=e and m'=d.
Multiplicities of a product add, so

    q ell-2=e+d=m+m'=q-2.

This contradicts ell>=3. Unequal factor degrees, products of many
absolute factors, components avoiding P and repeated-factor attempts
have all been covered. The proof does not need the old no-line theorem
or the stronger claim that every component must pass P. NF2 is this
conditional shared-point localization inside an impossible splitting;
it is not a classification of the individual singularities/components.
NF1 follows as WHOLE absolute irreducibility, and therefore as exclusion
from the official F2 factorization set.

The two general imports retain their ordinary hypotheses: projective
plane curves over K with no common component, and local intersection
equality for coprime tangent cones. Hernando--McGuire's actual
Section3.2/Corollary8 supplies those statements. Its component-existence
theorem and its theorem conditional on ordinary irreducibility are not
used. I also opened the author-posted Fulton book endpoint; the direct
PDF fetch failed, so I do not advertise a complete original-book proof
read. This bounded source failure does not replace the successfully
read operative statements by an unread theorem.

## 8. Four-bit corollary, source attribution and honest limits

For ell7 the order of2 modulo7 is3. If a1mod3 then q2mod7, meeting
the first condition; if a2mod3 then q4mod7, meeting the second. If
a0mod3 then q1mod7, meeting neither. Thus NF3 is exactly the asserted
a>=2,3 not dividing a subfamily. The integer7*2^a+1 has ones at
positions0,a,a+1,a+2, distinct because a>=2, hence binary weight4.

The excluded parameter branch cannot be added for free. At a0mod3,
q-Frobenius is the identity on F8, so at the off-diagonal F8 triples
both coefficients of H_q vanish. The single-tangent premise fails;
the degree-(q+1) term is the next candidate and requires another
argument. The familiar n57 is therefore outside NF3, consistently
with the Kasami context. NF does not classify all four-bit exponents,
all other ell or the official annual factorization set.

I freshly read the COMPLETE existing images of McGuire's thesis
printed24--26 (image files29--31), including Theorem8 and its entire
printed proof. Its displayed family ell=2^(a+1)-1 is a special case
of the second neighbor; n29 is already there. The local method and
the concluding degree/multiplicity mechanism are attributed. This
does not certify priority for the more general parameter criterion.
The preceding Theorem7 proof tail is visible but was not treated as
a fully reread theorem premise. The Caltech primary record confirms
the actual thesis title, rather than inheriting an older miscitation.

The current companion source record's unread Jedlicka PDF and partial
2026 lead are unimported literature context. I did not rerun those
failed fetches, claim their hypotheses, or infer novelty from an unread
source. No APN classification is substituted for ordinary F2
reducibility, and no preliminary positive-family construction is made.

## 9. Adversarial boundaries, preservation and checkpoint

The attempted failure points included repeated factors in
characteristic2; affine-only singularity lists; singular points with
zero coordinates; a factor missing P; repeated tangents versus true
unit cofactors; the diagonal quotient correction; a nonzero vertical
tangent; a qth root leaving F; using the wrong Frobenius identity in
the second neighbor; composite ell; unequal degrees and many
components; small q4/vacuous first branch; and the q1mod7 branch where
the next-term argument actually ceases to apply. The reconstructed
proof survives these within its stated domain. Four scope notes are
preserved; no substantive repair request is recorded.

All mathematics was hand reasoning. No mathematical executable, CAS,
mask/field/factor scan, finite-test extrapolation, original-source
algorithm execution, count/certificate replay or constructor program
ran. Metadata checks bind bytes/JSON/ledger tags only. Existing cached
papers/images were read-only, never rewritten or redistributed.

The compact baseline binds7 constructor files,14 declared current
context fingerprints and9 immediately preceding own frozen files:
30occurrences/30paths, canonical summary
`09330fbcfe393fca6cdcbd718d35f2315bf55bc3dab34ae7a57aa9805d935c5f`.
The immutable own parent binds457 older own paths transitively; its
nine files were reverified without expanding or recopying that history.
No old/shared/Git/cache bytes were edited. No spawning, contact, charge,
separately billed API, access bypass or automatic-reset spending occurred.

This new weekly window was explicitly authorized by the user to90%
TOTAL with integration reserve. Direct primary/legacy host telemetry
at00:23:55UTC on2026-10-18 showed3% used, reset1792874445,
ordinary usage allowed. The freeze records the later transition check
separately. Requested settings remain distinct from unknown effective
readback. The entire report, all36 ledger rows, issues, actual source
scopes and immutable integrity records freeze before ANY new peer NF
file/finding/metadata is opened. Root alone may reconcile and promote
after BOTH independent whole audits. The queued2025R9 packet remained
unopened through this complete checkpoint.
