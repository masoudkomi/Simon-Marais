# NJ1-v2/NJ2-v2: initially blind independent whole R1 audit

2026-10-17 UTC. Reviewer `/root/review_2021_reasoning_j15_r2`.
Requested gpt-6.1-sol/max; independently verified effective settings unknown.
Target12232B, SHA256
`5197ab6841d0a97356484cf3a08a7163055449fa879bd8010886e28158532ef6`.
Constructor manifest2368B, SHA256
`7aec0a9fd4109910ea8d95e3b8e50860c4e8083bbe82249196617274d95b03a3`.

I reconstructed the COMPLETE v2 proof, both claims and all ten whole-audit
obligations. No substantive defect or required author repair was found.
I recommend only the exact every-even-inner-index composition criterion
and its fixed-family WHOLE-divisor consequence after the other complete
independent audit and coordinator reconciliation. No reviewer promotion,
arbitrary-factor irreducibility or complete annual classification is made.

I authored older T1–T4/C7/C11 and whole-reviewed CP, GK, KC, CJ and DI.
Those roles did not construct NEW NJ, contribute its next-coefficient
argument or extend it to every even inner index. I do not count this
as independent recertification of my older authored work. Root constructed
NJ and is excluded as an independent reviewer. The earlier P2-only v1
is preserved history, not an assumed theorem or a partial audit here.
The entire2019 R7 construction was frozen before the first NJ target
read. No new NJ peer report, conclusion or later root inspection was
read before this complete initial freeze. The queued2020 target is unread.

## Exact domains, degrees and all immediate cases

Fix q=2^k>=4 and the exact accepted F2 polynomials A,B,P_i. The
complete accepted GK and CP bodies and acceptance scopes were reread,
as was accepted CJ for context. Only GK recurrence/degrees/identity
and CP1 for the final homogeneous consequence are needed as theorem
inputs. Every new local step is reconstructed; neither CJ's old
necessary modulus nor the unverified DI criterion fills an inference.

For nonconstant polynomials over any field, composition degrees multiply,
including inseparable polynomials. P_s is nonconstant for every s>=1.
Thus a hypothetical H is nonconstant with E_s=(deg H)E_r. The E_i
are strictly increasing, so s<r fails. At s=r a degree-one H satisfies
H(P_r)=P_r only when H=T, by injectivity of substitution by a
nonconstant polynomial. The auxiliary P0=1 is correctly outside s>=1.

Modulo the positive integer q^2+1, the terms in E_i alternate1,-1.
Consequently E_r is divisible by q^2+1 for every EVEN r, whereas
E_s is1 modulo it for every ODD s. E_r|E_s would then be impossible
for odd s. This is a necessary degree argument, not an assumed full
classification of when E_r divides E_s. The remaining range is exactly
even s>r>=2. All extensions of the coefficient field are allowed in
this argument; no restriction on H's derivative was imposed.

## The critical constants and derivative recurrences

The identity(T+1)A=T^(q+1)+1 is exact. The numerator has q+1 distinct
nonzero roots because its derivative is T^q. Dividing removes only
the simple root1; A(1)=1. Hence A has exactly q simple roots alpha,
all nonzero and different from1. Each is in F_(q^2) and satisfies
alpha^q=alpha^-1. These facts hold inside any algebraically closed
characteristic-two K. Frobenius periodicity is used on these finite
constants, not on the indeterminate or all of K.

For u=alpha+1!=0, u^q=u/alpha and u^(q^2)=u, so B(alpha)=alpha^-1.
Every odd iterate of q-Frobenius raises that value to alpha. The
displayed F=P2 has F(alpha)=alpha^2+alpha*u=alpha. The derivatives
A'(alpha)=B'(alpha)=u^(q-2)=a are nonzero; the derivative of T^q
is zero and the coefficient q-1 of B' is1 in the field.

At alpha each recurrence therefore reduces to P_(i+2)(alpha)=
alpha P_i(alpha), giving P_(2h)(alpha)=alpha^h and
P_(2h+1)(alpha)=alpha^(h+1), including h0 with the stated bases.
Differentiate BEFORE evaluation: every recurrence coefficient has a
positive power-of-two exponent and derivative zero. This gives
P_(i+2)'(alpha)=alpha P_i'(alpha), whose bases0,1 yield

    P_(2h)'(alpha)=0,
    P_(2h+1)'(alpha)=alpha^h.

The latter is always nonzero, even if h is a multiple of q+1 or an
even integer. One must not differentiate the evaluated expression
alpha^h as if alpha remained a variable; the submission does not.
For example beta=alpha^h may equal1 and is permitted to repeat.
No distinct-critical-value property of P_r is needed.

## Exact order q at every even inner index

Let Z=T-alpha. From the explicit formula F'=A^q, its linear coefficient
at alpha is zero. The binary support of q^2+1 is{0,2k}, and that of
q^2-q+1 is{0,k,...,2k-1}. Frobenius binomial products consequently
contain no exponent2 through q-1. The Z^q coefficient comes only
from the second summand and is u^(q^2-2q+1), nonzero. Thus
ord_Z(F(alpha+Z)-alpha)=q EXACTLY. Derivative multiplicity q was
not incorrectly converted into local order q+1.

For every even i>=2, the recurrence exponent q^(2i+1) is at least
q^5. Its A term vanishes to that order, and its B coefficient differs
from alpha to at least that order by Frobenius. It follows that
P_(i+2)=alpha P_i modulo Z^(q^5). Induction gives

    P_(2h)(alpha+Z)=alpha^(h-1)F(alpha+Z) mod Z^(q^5).

For h1 this is exact equality and no erroneous initial recurrence is
needed. For every h>=1 its constant is alpha^h and its leading
nonconstant coefficient is alpha^(h-1)u^(q^2-2q+1), nonzero. The
error threshold exceeds q. Therefore V=P_r(alpha+Z)-beta has exact
order q for EVERY even r=2h>=2, including repeated beta-values.

## The first later recurrence and the nonzero M+1 coefficient

Set M=q^(2r+1), which is at least q^5 and greater than1. The exact
next recurrence gives

    P_(r+2)-alpha P_r=A^M P_(r+1)+(B^M-alpha)P_r.

Both coefficient polynomials on the right have no exponent below M
in their local nonconstant part. A^M has no constant term; its
coefficient at Z^M is a^M. The constant of B^M is alpha, so the
same is true of B^M-alpha. Their subsequent possible exponents are
at least2M, greater than M+1. The whole difference has order at least M.

At M+1 the first summand contributes exactly a^M P_(r+1)'(alpha),
which is a^M alpha^h!=0. The second summand contributes
a^M P_r'(alpha)=0. No smaller constant or higher Frobenius term
can contribute at M+1. This checks BOTH summands and the exact sign
convention in characteristic two. The proof needs no assertion about
the coefficient at order M itself.

Each subsequent even recurrence has exponent at least q^(2r+5),
strictly greater than M+1 and hence at least M+2. Modulo Z^(M+2)
it therefore only multiplies the earlier even polynomial by alpha.
For every even s>=r+2, iteration gives the exact retained jet

    P_s=alpha^((s-r-2)/2)P_(r+2) mod Z^(M+2).

Subtract cP_r, c=alpha^((s-r)/2). The difference has order at least M
and coefficient at M+1 equal to
alpha^((s-r-2)/2)*a^M*alpha^h, which is nonzero. At s=r+2 the
first multiplier is1; at arbitrarily large s it is still a unit.
There is no repeated sum of a common coefficient whose step count
could vanish modulo2: later errors begin above M+1. Thus the
next-coefficient fact is uniform over ALL even later target indices.

## Composition forbids precisely that exponent

Suppose P_s=H(P_r) in the remaining range. Put K_beta(Y)=H(Y)-cY.
If this polynomial is zero, the just-computed nonzero coefficient
already contradicts the zero composition. Otherwise let m>=0 be its
EXACT local order at beta and factor

    K_beta(Y)=(Y-beta)^m W(Y), W(beta)!=0.

Substitution at P_r has order exactly qm, because V has order q
and the substituted W has nonzero constant W(beta). This retains
inseparable H and any vanishing first derivatives. The lower order
bound M forces m>=M/q=q^(2r).

Expanding at beta thus has NO powers below J=q^(2r); it may have a
zero coefficient at J as well. Its first allowed term b_J V^J has
only exponents divisible by J, since J is itself a power of2.
M+1=qJ+1 is not divisible by J>1. Every later allowed term has
order at least q(J+1)=M+q>M+1. Therefore the entire composition
has ZERO coefficient at M+1, regardless of whether b_J vanishes.
This contradicts the retained jet and excludes every even s>r.
Together with the earlier smaller/odd/equality cases, NJ1 follows
over every algebraically closed K in the exact stated range.

## NJ2: whole homogeneous divisor, not an arbitrary factor theorem

For fixed q>=4, all L_i for i>=1 are positive odd integers at least
d=q^2-q+1>=13. Thus they meet the full CP1 domain, and g_d is
nonconstant of degree(d-1)/2. CP1 applied to a WHOLE divisor gives
g_(L_s)=H(g_(L_r)) with H in F2[T]. The full accepted GK identity
then gives P_s(g_d)=H(P_r(g_d)). A nonzero univariate polynomial
composed with nonconstant g_d cannot vanish, by leading degree.
Hence P_s=H(P_r) as POLYNOMIALS, not just as field functions.
Apply NJ1 in an algebraic closure of F2 to obtain s=r,H=T.
Conversely s=r gives equality and therefore division. This proves
both directions of NJ2 without an absolute-component or descent guess.

CP1's complete accepted body includes the homogeneous/affine degree
check, both quadratic-cover free-module descent and repeated diagonal
factor cancellation. Its exact WHOLE criterion is what is used here.
No extension-field factor is promoted to an F2 factor. L0=1/P0 are
auxiliary cases explicitly excluded; equality has a unit cofactor and
does not supply two positive-degree official factors. The smaller
whole phi_d factors from GK are unaffected. No odd inner index>1,
other composition factor, component or general exponent is classified.

The official statement and exact accepted scopes were checked in full.
No mathematical program, CAS, scan, sample or author rerun supplies any
step. The ten obligations are covered by the separate per-inference
ledger, with a complete source/integrity record. Candidate, old v1,
all older own bytes and shared files remain unchanged. Reconciliation
and promotion belong only to the coordinator after both whole audits.
