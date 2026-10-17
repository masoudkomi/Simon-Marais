# IC1--IC4: complete initially blind WHOLE R2

2026-10-17 UTC. Reviewer `/root/review_2017_coarsening_r1`.
Requested gpt-6.1-sol/max; independently verified effective settings
unavailable. This is a NONCONSTRUCTOR whole initial audit of the NEW
IC packet. I authored OLD accepted CP1--CP3 and reviewed older2024
structural/divisor/NV/KC/CJ/DI material. Those roles are disclosed;
this is not an independent recertification of my own CP theorem.
The separately accepted old inputs retain their two-other-review basis.
I did not construct or contribute any inference to NEW IC1--IC4.
No new IC peer/root report, ledger, source verdict or findings were
read before this COMPLETE initial packet was frozen.

Target main: `notes/reasoning-components-r1-candidate-v1.md`,24588B,
SHA256 `21a23e6dedf5531b23c004e78cc4bf54253e356fa29676d97a9ae6e23d5bee48`.
Target freeze SHA256
`1c2ac7f2322f7e83d62cfbb563c312eca75aa536448e875f849c9b2195ffd5e9`.
The separate authority-hash-only addendum SHA256 is
`3aac70a9a54b40f00087007562de109d9325419190e65aecbea9bae76c9b7133`.
The entire new mathematical packet, all48 obligations, failure/source
records, worklog, metadata schema and addendum were inspected. Accepted
KC/GK bodies and scopes, and the old CP/NV whole-divisor boundary,
were read. No author selfcheck, orbit sample or CAS substitutes for
the reconstruction below.

## Verdict and exact theorem dependence

I found no substantive defect requiring an author repair in the stated
IC1--IC4 scopes. IC1 is self-contained. IC2--IC4 explicitly import
the Janwa--Wilson component theorem J, whose COMPLETE statement and
matching definitions were verified in the primary coauthor source,
including the existing full-page image. Its original1993 proof was
not read or reconstructed. This is an explicit published-theorem
dependency, not a newly proved absolute-factorization claim. The
source's later singular-point/transversality argument is not imported.
IC3 and the full-block clause of IC4 use accepted KC only AFTER
the whole divisor has actually been forced. Neither KC nor CP is
applied directly to one arbitrary factor.

The result gives exact individual-component restrictions and some exact
individual occurrence criteria. It constructs no new qualifying exponent
family and does not classify all factors or solve2024 B4(b). The
q16 proper-block alternatives remain genuinely unresolved in this
argument. Promotion still belongs to the coordinator after the other
fresh whole audit and reconciliation of full reports and source scopes.

## 1. Official domain and quotient boundaries

I read complete actual B4 of the official2024 paper. The parameter is
an odd positive integer n. Congruence is coefficientwise for integer
polynomials and both unknown factors must remain nonconstant modulo2.
Thus actual F2 polynomial reducibility is the target; evaluations on
F2^3, extension-only factors and APN status do not decide it. No
preliminary part(a) construction was investigated or reproduced.

For odd n>=3 let W=X+Y+Z and

    f_n=X^n+Y^n+Z^n+W^n,
    R=(X+Y)(Y+Z)(Z+X),  phi_n=f_n/R,
    psi_n(x,y)=phi_n(x,y,1), G_n=x^n+(x+1)^n.

The accepted quotient is a genuine homogeneous polynomial of degree
n-3. Its numerator is nonzero: the coefficient of X^(n-1)Y is1.
At n=1 the numerator is zero and cannot equal R times two nonzero
nonconstant reductions in the polynomial domain. At n=3 the quotient
is the unit1. These endpoints do not qualify. Component assertions
assume k>=2,q=2^k>=4; q2 has no labels and its base quotient is the
unit phi3. The auxiliary GK r0=n1 is not passed into KC or IC2.

## 2. IC1: numerator squarefreeness and the entire coordinate boundary

Write n-1=Qh with Q=2^s,s>=1 and h odd. In K=Fbar2,

    f_X=(X^h+W^h)^Q,  f_Y=(Y^h+W^h)^Q.

These formulas use n odd and Frobenius exactly. Since h is odd,
X^h+W^h splits into the h distinct forms X+zeta W, zeta^h=1,
and similarly the other polynomial splits into Y+eta W. Their
coefficient vectors are (1+zeta,zeta,zeta) and
(eta,1+eta,eta). Association by a nonzero scalar c would make
zeta=c eta from Z, and1+zeta=c eta from X, an impossibility.
No zero zeta/eta occurs. This covers h1 too: its forms are Y+Z
and X+Z. Hence f_X and f_Y have no common irreducible factor.

Any repeated irreducible factor of f_n divides each partial derivative
by the product rule, also in characteristic2. Therefore f_n is
squarefree over K. R has three distinct linear factors, so f_n=R phi_n
implies both squarefreeness of phi_n and gcd(R,phi_n)=1. This argument
does not apply to the excluded zero numerator at n1 and does not
assert that phi_n is irreducible.

At Y0,Z1 the precise polynomial restriction is

    psi_n(x,0)=(G_n(x)+1)/(x(x+1)).

G_n+1 has degree n-1 and leading coefficient1: the top x^n terms
cancel and the next coefficient is n=1. Both0 and1 are numerator
roots with derivative1, so they are SIMPLE. Cancellation consequently
gives value1 at each, a monic degree n-3 quotient, and value1 at the
projective point at infinity of Y0. All three F2 points on this
projective line are accounted for. For n3 the restriction is1 and
the intersection is empty.

At any remaining boundary root (a,0), put b=a+1. Then ab!=0 and
R(a,0,1)=ab. Differentiating f_n=R phi_n at the root gives

    psi_y(a,0)=b^(n-1)/(ab)!=0.

The y^(n-1) term vanishes because n>=3; the term at b is nonzero.
Thus every such boundary point is smooth. More importantly, if
psi_n=H C with H(a,0)=0, the product rule gives
psi_y(a,0)=H_y(a,0)C(a,0). Both right factors are nonzero. C is
a unit in the local ring at this point. This proves EXACT contact
transfer to H and ensures only one absolute component goes through
the point. A mere divisibility lower bound would not give that fact.

## 3. IC1: exact contact trichotomy, including all low endpoints

Let e be the multiplicity of a in the boundary restriction. Because
the denominator is a unit, it equals ord_a(G_n+1). If its derivative
is nonzero then e1. Otherwise set a^(n-1)=b^(n-1)=t. The root equation
gives t(a+b)+1=t+1=0, so t1. Frobenius injectivity gives
a^h=b^h=1. This rules out h1: it would require both a and b to be1.
Thus in the multiple-root case h>=3 and the terms through Q+1
are within the polynomial degree.

Expanding (a+z)^n=(a+z)(a^Q+z^Q)^h and its b counterpart,
constant and linear coefficients cancel. There are no exponents2
through Q-1. Since h is odd, the next two coefficients are

    z^Q: a^(1-Q)+b^(1-Q),
    z^(Q+1): a^(-Q)+b^(-Q)=(ab)^(-Q)!=0.

Terms arising from the next binomial index have exponent at least2Q,
strictly greater than Q+1, including Q2. Thus no missed term can
cancel the second coefficient. The first vanishes precisely when
a^(Q-1)=b^(Q-1), equivalently a^Q b=b^Q a. Substituting b=a+1
reduces this to a^Q=a. Therefore the complete trichotomy is

    e=1; or e=Q+1 with a in F_Q; or e=Q with a outside F_Q.

The latter two cases also have a^h=b^h=1 as derived. This is exactly
the stated contact formula. For ANY factor through the point, its
cofactor is a unit, so its boundary contact equals e, not merely
at most e. An odd contact greater than1 is therefore Q+1 and
determines s EXACTLY. This eliminates the otherwise possible s>k
case in the later application. No J input entered Sections2--3.

## 4. J: full homogeneous transport and actual F2 factors

The imported coauthor statement gives the complete affine factorization
of psi_d, d=q²-q+1, by absolutely irreducible p_alpha over F_q,
degree q+1, with p_alpha(x,0)=(x+alpha)^(q+1). I verified the
same affine definition psi=phi(x,y,1). The odd-k/extension-degree
conditions of a preceding APN theorem are not attached to this
separate statement. Only this decomposition/normalization is used;
the subsequent theorem at (1,1) is not.

Homogenize each factor to degree q+1. The specialization already
has that full degree, so P_alpha has no Z factor and

    P_alpha(X,0,Z)=(X+alpha Z)^(q+1).

It is normalized by coefficient X^(q+1)=1. Distinct alpha give
nonassociate factors. A factorization of P_alpha would dehomogenize
to a factorization of p_alpha unless a factor became a unit; such
a homogeneous factor would be a Z power, which was excluded.
Hence these homogeneous factors remain absolutely irreducible.
Their total degree is(q-2)(q+1)=d-3, so homogenization gives the
WHOLE equality phi_d=product_alpha P_alpha, without a missing line
or undetermined scalar.

For every odd target n>=3, f_n(X,Y,0) is nonzero, again from its
X^(n-1)Y coefficient. Since R(X,Y,0)=XY(X+Y) is nonzero, phi_n
is not divisible by Z and its Z1 affine degree is still n-3.
Consequently affine division by p_alpha and homogeneous division
by P_alpha are equivalent: degrees add in a polynomial domain and
homogenizing the quotient introduces no extra Z factor.

Let sigma square coefficients. Unique factorization and normalization
give sigma(P_alpha)=P_(alpha²), by their boundary restrictions.
If alpha has exact field degree t, this is an orbit of length t.
The coefficient of X^q Z in the restriction is alpha, since
(X+alpha Z)^(q+1)=X^(q+1)+alpha X^qZ+alpha^q XZ^q+
alpha^(q+1)Z^(q+1). Thus the MINIMAL coefficient field is exactly
F2(alpha)=F_(2^t), not necessarily all F_q.

Each Frobenius orbit product Q_O is fixed by sigma, hence is over
F2. A proper nonconstant F2 divisor would select a proper nonempty
sigma-invariant subset of that single absolute-factor orbit, impossible.
Thus Q_O is F2-irreducible of degree |O|(q+1), and these exhaust the
ordinary F2 factors of phi_d. For any F2 target, containment of one
P_alpha forces its entire orbit product. The quotient descends to F2
because applying sigma fixes numerator and divisor and uniqueness
of the quotient fixes it. Absolute versus F2 containment is therefore
handled explicitly, rather than inferred from APN statements.

## 5. IC2: a single component fixes the valuation and mixed-base gcds

If P_alpha divides phi_n, its boundary root alpha has contact q+1,
which is odd and greater than1. The cofactor-unit assertion of IC1
forces this to equal the TOTAL contact of the target. The trichotomy
therefore gives q+1=Q+1, hence s=k, and also

    alpha^(n-1)=(alpha+1)^(n-1)=1.

Equivalently, with m_alpha the lcm of the two multiplicative orders,
q*m_alpha divides n-1 and its quotient is odd. Both orders are odd.
There is no assumption alpha is primitive and no unjustified replacement
of m_alpha by q-1 when alpha lies in a proper subfield. These are
necessary conditions only.

If v2(n-1)!=k, any nonconstant gcd over K with the WHOLE phi_d
would select one of J's actual absolute primes P_alpha, contradicting
the individual implication. Thus the gcd is1 over K and over F2,
not merely a failed whole-divisor test. This is where having an
individual contact theorem genuinely strengthens old whole NV.

For t=2^ell,ell>=1 and r>=1, the integer identity

    L_(t,r)-1=t*(t^(2r)-1)/(t+1)

has an odd integer quotient: t+1 divides t^(2r)-1 and both are
odd. Hence its valuation is ell exactly. Distinct k and ell give
the entire mixed-q coprimality claim at EVERY index. The t2,r1
case has target n3/unit and remains valid. No absolute factorization
of the higher member is assumed. Conversely same valuation is not
asserted sufficient and non-base components of higher members are
outside this argument. Global squarefreeness proves every occurrence
is simple and, under the accepted same-q whole division, the quotient
is coprime to phi_d. At r1 that quotient is1, as explicitly stated.

## 6. Actual symmetries and the full semilinear label action

The two linear maps S:(X,Y,Z)->(Z,Y,X) and
T:(X,Y,Z)->(X+Y+Z,Y,Z) are invertible involutions. S permutes
X,Z; T exchanges X,W. Thus each fixes f_n. They also fix R;
for T its three factors become X+Z,Y+Z,X+Y. Cancellation in the
polynomial domain shows each fixes phi_n as a POLYNOMIAL for
every n, not merely as a finite-field function.

Applying these substitutions to one normalized P_alpha and using
its restriction gives

    P_alpha composed with S=alpha^(q+1) P_(1/alpha),
    P_alpha composed with T=P_(alpha+1).

Unique factorization of the fixed phi_d supplies actual components;
the restriction identifies their labels and the scalar. The first
nonzero scalar is necessary for the polynomial identity and harmless
for divisibility. Frobenius plus these coordinate changes propagate
containment in phi_n along the stated semilinear orbit.

The label group H consists of the six explicit PGL2(F2) functions
a,a+1,1/a,1/(a+1),a/(a+1),(a+1)/a. Their poles are excluded by
a!=0,1. Each rational map and its inverse have F2 coefficients,
so they preserve F2(a) exactly and commute with squaring. Squaring
also preserves the exact field degree. Checking fixed-point equations,
the involutions have no admissible fixed point; the order3 maps fix
precisely the roots of a²+a+1. Hence H-orbits have size2 on
F4 minus F2 and size6 elsewhere. No orbit enumeration is needed.

## 7. IC3: exactly three transitive fields and both iff directions

At k2, the two labels form one H-orbit. At k3, no label is in
F4 because F8 intersect F4=F2; the six labels form one free
H-orbit. At k5 all30 labels have exact degree5 and H acts freely.
If h sigma^j fixes one, its fifth power makes h^5 fix the label.
Freeness gives h^5=id, and the possible orders1,2,3 force h=id.
Exact degree5 then forces j0mod5. The commuting H times C5
action is free, giving an orbit of30, the whole label set.

For composite k>=4, choose a proper divisor1<e<k. The subfield
F_(2^e) supplies an element of degree e, whereas F_q supplies
one of degree k; primitive multiplicative elements give explicit
existence by the elementary cyclicity of finite-field units. Degree
is preserved by all actions, so they cannot be transitive. The
cyclicity justification in the candidate is sound: combine prime
power orders to obtain the exponent as an actual element order,
then compare the roots of X^m-1 with the group size. For prime
k>=7, an orbit has at most6k elements while2^k-2>6k; the inequality
starts at7 and its gap increases. All k>=2 are exhausted.

In k2,3,5, any one component's containment consequently forces
ALL distinct J factors, i.e. the whole phi_d divides phi_n over
K. Quotient uniqueness descends this division to F2. Only NOW
may accepted KC be invoked in its actual k>=2,odd n>=3 domain:
n=(q^(2r+1)+1)/(q+1),r>=1. The reverse implication is the accepted
GK/KC whole containment, which supplies every component. This
proves both directions of the individual iff without applying a
whole-composition theorem directly to one factor.

For q8 the six labels have Frobenius orbit length3, giving two
degree27 F2-irreducibles. For q32 the thirty labels have orbit
length5, giving six degree165 F2-irreducibles. Each has the exact
unrestricted target test. Their total degrees54 and990 agree with
phi57 and phi993, so they are proper at those self exponents.
At q4 the single F2 orbit factor is the whole phi13; equality at
n13 has a unit cofactor and alone does not qualify for the official
question. For r>=2 accepted positive-degree arguments apply. No
new existence of the published base factors is claimed here.

## 8. IC4: the complete q16 two-block conclusion and no converse

F16 minus F2 consists of two degree2 labels and twelve degree4
labels. The former pair is one H-orbit. On the latter H acts freely,
so there are precisely two H-orbits of size6. Squaring permutes them.
If it preserved either one, sigma(a)=h(a) for some h in H. As
sigma^4=id and the actions commute, h^4 fixes a; freeness gives
h^4=id. Thus h has order1 or2, and sigma²(a)=h²(a)=a would put
a in F4, a contradiction. Therefore squaring exchanges the two
H-orbits and all twelve labels form one combined orbit.

Under Frobenius alone the small block has one orbit of length2;
the large block has three orbits of length4. Accordingly A is
an irreducible F2 polynomial of degree34 and B is a product of
three distinct degree68 F2-irreducibles, total204. Their product
has degree238=241-3. Every common factor with an F2 target must
be a union of whole saturation blocks; squarefreeness excludes
powers. Thus its F2 gcd is exactly among1,A,B,AB.

Any nontrivial case has valuation4 by IC2. A contains the two
order3 F4 labels, so requires3|(n-1). B contains a primitive
F16 label, so requires15|(n-1); this does not assert the original
chosen degree4 label was primitive. AB is whole phi241, whose
containment has exactly the accepted q16 KC progression. No
proper A-only or B-only occurrence is constructed or excluded.
The fact that these two invariant blocks exist proves only the
limit of this symmetry propagation, not that a proper possibility
is realized. This limitation is accurately retained.

## 9. Attribution, failure boundaries and complete audit disposition

The actual primary2012 Delgado--Janwa Lemma1(b) already states
coprimality of distinct PURE Kasami bases, with the displayed absolute
factor degrees giving its proof. That r1 subcase is correctly
attributed. IC2 adds the arbitrary odd-target/different-valuation
scope and every later mixed-q member; no literature-priority claim
is warranted or made. The1993 proof remains unread, and this audit
does not independently prove J's absolute irreducibility. Its exact
coauthor statement and coefficient normalization are the imported
published theorem, with no adjacent APN/odd-k restrictions attached.

I specifically challenged these invalid shortcuts: transferring a
whole NV/KC exclusion directly to one component; inferring s=k from
contact only bounded below; treating any subfield label as primitive;
assuming all k are transitive; inferring actual partial containment
from nontransitivity; omitting the reciprocal scalar; inferring
ordinary F2 reducibility solely from absolute splitting; and using
the later singular-point parity theorem. The candidate uses none
of them. Its local unit, exact coefficient expansion, actual
coordinate action and orbit quotient descent supply the needed
steps. Each of the48 obligations has an explicit inference row
in the companion ledger.

No same-valuation criterion for general k, q16 proper-block realization,
classification of non-base higher-family components, all-factor theorem,
annual solution or novelty is inferred. No mathematical program, CAS,
orbit/sample/exponent scan, old certificate or constructor rerun was
used. Primary pages and existing cache images were read only; no
cache mutation/download/redistribution or external contact occurred.
The full review/source/identity packet freezes before any peer finding.
There are0 open substantive issues and0 required author repairs within
the stated published-input scope; root alone may reconcile/promote.
