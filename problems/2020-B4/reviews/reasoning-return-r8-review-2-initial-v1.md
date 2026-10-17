# 2020 R8: initially blind whole audit R2

2026-10-17 UTC. Reviewer `/root/review_2021_reasoning_j15_r2`.
Requested inherited settings: gpt-6.1-sol/max. Independent effective-setting
readback is unavailable. This is an independent nonconstructor review of
the COMPLETE R8A--R8F argument, not an acceptance or annual solution.

## 1. Target, independence and finding

Target: `notes/reasoning-return-r8-candidate-v1.md`, 25948 bytes, SHA256
`2eb3bbc51c282619a4bf0bf2b34f083c9c65abd7b27822355cd4973f391637d8`.
Constructor freeze: `notes/reasoning-return-r8-freeze-v1.json`, 5346 bytes,
SHA256 `6f7d5060bf093304ec26a0268a8098942bd8021e99e056b1970dec12813d102e`.
All twelve frozen records, including all 54 obligations, were examined.
The mathematical executable count is zero. The author freeze script was
read as administrative source and was not executed or reused.

I found no substantive defect requiring repair in the stated claims. The
recommendation is to accept R8A--R8F only in their precise conditional
domains, after the coordinator reconciles TWO OTHER whole reviews. This
review does not establish a new taut order, an unrestricted classification,
a class-number computation, or a numerical cutoff. There are no open
review issues or requested author changes. The companion ledger gives an
individual disposition for every author obligation.

I did not construct or contribute any new R8 inference. My relevant older
roles were the 2020 R3 whole R2 and targeted F4 repair review, and R5 whole
R2. The R3 review found the distinction between an arbitrary common fixed
group and the individual generated subgroups; that original objection and
the author's repair remain preserved. Those roles do not independently
recertify R3/R5 or any other accepted premise here. The present constructor
authored R4/R5/R7 and reviewed R6. The root's broad assignment is not a new
R8 proof contribution. Every NEW root R8 report, issue log, source record,
manifest and finding remained unread through this ENTIRE initial freeze.
No new peer R8 verdict was received. I have not opened the queued 2017 R6
packet. Earlier own construction and review bytes are immutable inputs.

## 2. Official domain and fixed fields

I checked the official B4 hypotheses and part (b), and read the local
statement in full. The accepted distance/difference dictionary uses
q=n-1, k=q+1 and v=q^2+q+1. It concerns actual distinct vertices and actual
0/1 subsets; it is not a relaxation to signed coefficients. The boundary
n=2, q=1 remains separately accepted. The new claims assume q>=2 and the
EXTRA condition p=v prime. No preliminary construction is reproduced.

Fix any odd T in (Z/pZ)^* containing every prime divisor of q. This choice
is before existence, and need not be the full multiplier group. Since q
is the product of these primes with multiplicity, q is in T. The identity
q^3=1 modulo p and 1<q<p give order exactly 3. In particular T is
nonidentity and p>=7. Odd order excludes -1. Abelianity of the cyclotomic
Galois group makes F=Q(zeta_p)^T stable under conjugation; c is nontrivial
on F. Its fixed field E is totally real, F totally imaginary, and F/E is
cyclic quadratic. Every sigma_t preserves F and commutes with c. It need
not fix E pointwise, a distinction retained in the multiplier argument.

For an actual planar set the accepted prime-divisor multiplier theorem
applies. Since p does not divide k, simultaneous numerical multipliers
fix the same unique sum-zero translate. Negation cannot fix an actual
set of at least three points: the ordered pair (d,e) and its conjugate
pair (-e,-d) would repeat a nonzero difference unless d=-e, and not all
pairs can be opposite. Every even subgroup of the cyclic group contains
negation. Thus the generated prime-divisor subgroup is odd for an actual
set. This explains coverage of actual prime-modulus configurations; it
does not turn existence for an arbitrarily larger T into unrestricted
tautness for that T.

## 3. R8A: every local place, then a FIELD norm

For each rational ell dividing q, ell is not p and its Frobenius is in T.
It splits completely in F and E. Every completion F_w/E_v above ell has
degree one, whose norm is the identity. Hence the positive valuation of q
causes no local obstruction. This is not a claim about norms of units at
ell dividing q.

At a finite place away from p and the divisors of q, the extension is
unramified or trivial and q is a unit. The finite residue-field norm is
onto. Given a residue lift, the correction on successive principal-unit
quotients uses the residue trace:

    N(1+pi^h x) = 1+pi^h Tr(x) modulo pi^(h+1), h>=1.

That trace is surjective, including in residue characteristic 2, because
finite fields are separable and the trace map is nonzero. Completeness
makes the successive corrections converge. No division by the extension
degree or by 2 is used.

At p the relative local extension has degree two, since p is totally
ramified through every cyclotomic subfield. The nonzero residue q^2 is
a root of X^2-q modulo p: q^4=q. Its derivative 2q^2 is a p-unit. Hensel
therefore gives x in Q_p with x^2=q. The image x in E_v has relative norm
x^2=q. This explicitly proves the needed ramified-place norm; general
surjectivity of ramified unit norms is not asserted. All real E-places
become complex, and q>0 is a complex-to-real norm there. These cases
exhaust the places.

The actual Hasse norm theorem applies because F/E is a CYCLIC extension
of number fields, with local solubility at every finite and infinite
place. Its conclusion is z in F^* with z*c(z)=q. It has no integrality
conclusion. I freshly read the complete operative Hasse statements and
their displayed proofs in Kedlaya and Milne, and the unramified norm
proof in Kedlaya. The deeper class-field-theory foundation is attributed,
not claimed freshly reconstructed in full. R8A does not select a balanced
ideal, a generator of such an ideal, or an ordinary integral Fourier lift.

## 4. R8B: the general quadratic obstruction

Let L/B be any quadratic number-field extension. Write A=Cl(L)^c and
let S consist of classes with a c-invariant fractional ideal representative.
S is a subgroup of A; a fixed CLASS is not presumed to have a fixed IDEAL.
For [J] in A choose (b)=J/c(J). Taking norms of ideals shows that b*c(b)
has trivial ideal in L and lies in B. Injectivity of extension on ideals
then shows it is a unit of B. The assignment

    [J] -> N(b) modulo N(U_L)

is a homomorphism to (U_B intersect N(L^*))/N(U_L). A new b for the same
principal ideal differs by a unit. Replacing J by (w)J multiplies b by
w/c(w), up to a unit, and this factor has norm one. These facts prove the
two required choice invariances.

For surjectivity, let N(b) be a B-unit. The principal ideal I=(b) satisfies
I*c(I)=1. A c-fixed prime has exponent zero. On a pair P,c(P) the
exponents are a,-a. Assign max(a,0) to P and max(-a,0) to c(P) in J.
Then I=J/c(J). Its class is ambiguous, and maps to N(b). It is not
assumed strongly ambiguous; the proof is precisely what measures that
distinction.

For the kernel, N(b)=N(u), u a unit, makes t=b/u a norm-one element.
If t!=-1, w=1+t is nonzero and w/c(w)=t. If t=-1, choose alpha outside
B; w=alpha-c(alpha) is nonzero and has c(w)=-w. Thus in both cases
J/(w) is invariant. Conversely an invariant representative J0 with
J=(w)J0 makes b/(w/c(w)) a unit, proving its norm a unit norm. Therefore

    A/S = (U_B intersect N(L^*))/N(U_L).

For [J] in A, the invariant ideal J*c(J) represents 2[J], so the quotient
has exponent at most two. It is finite because Cl(L) is finite. If the
FULL ordinary class group has odd order, its subgroup quotient is both
odd and of exponent at most two, hence zero. The explicit construction
also checks: if odd h annihilates Cl(L), then

    H=(J*c(J))^((h+1)/2), [H]=[J], c(H)=H.

Writing J=(w)H makes u=b*c(w)/w a UNIT with N(u)=N(b). Negative ideal
valuations cause no problem; ideals throughout this argument may be
fractional. This reconstructs the classical exact sequence rather than
assuming an integral Hilbert 90 theorem. Lemmermeyer's original six-page
preprint and operative Proposition 1 were inspected. No class-number
formula is silently imported to discharge any new arithmetic condition.

## 5. R8C: specialize without losing the real unit obstruction

The exact accepted R7B3 says the integral conjugation-norm-one elements
of F are +/-1. Its hypotheses are met, especially nonidentity of T. For
u in U_F, u/c(u) is such an integral unit. At the unique prime P over p,
c acts identically on the residue field F_p and u has nonzero residue.
Thus u/c(u) reduces to 1, excluding -1 since p is odd. Consequently
U_F=U_E and N(U_F)=U_E^2. This is not a statement that every positive
unit is a square or a field norm.

With s=|T|, pi_F=product_(t in T)(1-zeta_p^t) is an integer of F. Each
factor has the unique p-prime of K as its ideal. The product has K-valuation
s, no other support, and F-valuation one because K/F is totally ramified
of degree s there. Hence (pi_F)=P. It is the actual ramified prime ideal
which is principal, not every ideal of F.

Every c-invariant fractional ideal extends an E-ideal except possibly an
odd exponent at P. At split primes the two exponents agree; at inert
primes the extension index is one; at P write an arbitrary integer
exponent 2b+r, r=0 or 1. Since P is principal, S=j Cl(E).

To check injectivity of j, suppose b O_F=(gamma) for a fractional E-ideal.
Then c(gamma)/gamma is an integral norm-one unit, hence +/-1. If positive,
gamma is in E and injectivity of ideal extension makes b principal.
If negative, v_P(gamma) is even, including when negative. Divide locally
by the corresponding integer power of a uniformizer of E_v. The result
is an anti-real UNIT w. Because c acts trivially on F_p, reduction gives
nonzero w=-w in odd characteristic, a contradiction. This proves j is
injective with no unstated integrality of the original ideal or generator.

It follows that Gamma=Cl(F)^c/j Cl(E) is the unit quotient in R8C. It is
finite of exponent at most two, and odd h(F) kills it. Neither odd |T|
nor odd h(E) replaces that hypothesis. The field named E in the old q=5
nonprincipal example is an imaginary quadratic field; it is not the
present real field E=F^c. Thus that example cannot be misread as a
counterexample to this j. The classical unit-index/capitulation context
was checked against the actual original Lemmermeyer statements; the
candidate's specialized proof stands independently of any shorthand.

## 6. R8D: the SAME ideal, a correcting UNIT, and actual 0/1 sets

For an integral principal balanced ideal a=(gamma), its generator gamma
is integral. The quotient epsilon=gamma*c(gamma)/q is in E, has trivial
ideal, and is positive at every real embedding, so it is a totally
positive E-unit. R8A supplies z with N(z)=q; gamma/z is allowed to be
fractional, but has norm epsilon. Thus epsilon is specifically a
FIELD-NORM unit, which is stronger than positivity.

Apply the paired-prime construction to (gamma/z)=J/c(J). The coset
o(a)=[J] mod j Cl(E) maps under the proved isomorphism to epsilon
mod U_E^2. Changing gamma changes this square class by a unit norm;
changing z or J leaves it fixed. Injectivity of the isomorphism proves
independence of all choices. Importantly o(a) is the class of an
AUXILIARY ambiguous J, not the original principal class [a]=0.

If o(a)=0, choose a UNIT u with N(u)=epsilon. Then alpha=gamma/u is
integral, generates the SAME a, and has norm q. Conversely any norm-q
generator alpha of a gives the UNIT gamma/alpha of norm epsilon.
The reciprocal convention agrees with the older correction by a unit of
norm epsilon^-1; there is no sign inversion in the argument. Because
U_F=U_E, the needed unit condition is exactly epsilon in U_E^2. It is
not supplied by positivity alone.

At P, alpha has residue +/-k since alpha^2=q=k^2 modulo p. Exactly one
sign has residue k, as p is odd and k is a p-unit. For completeness I
checked the accepted R7B bridge against its full body. O_K=Z[zeta_p],
and the kernel of integral group-ring evaluation is Z times the full
sum N_G. The residue condition makes the adjustment to augmentation k
integral and unique. For that lift A, evaluation gives

    A*A^(-) - q = c0 N_G.

Augmentation gives c0=(k^2-q)/p=1. Its identity coefficient yields
sum a_i^2=k=sum a_i. Each integer a_i(a_i-1) is nonnegative, so every
coefficient is 0 or 1; the full off-identity coefficients give every
nonzero ordered difference once. This recovers an actual set, not just
real values, primitive Fourier data, or signed coefficients.

Fixed F-values and fixed-augmentation injectivity give T-stability.
The sum of the elements is fixed by a nonidentity scalar in T and
therefore zero in F_p. For each realized ideal exactly two norm-q
generators exist, their ratio a norm-one unit +/-1. Only one sign has
augmentation residue k. Conversely every actual T-stable centered set
gives such an ideal and zero obstruction. Different ideals cannot
give the same normalized character or the same actual set. The stated
bijection is exact.

When Gamma=0, and in particular when h(F) is odd, every PRINCIPAL balanced
ideal passes the unit obstruction. At least one such principal ideal is
still necessary and sufficient. Balance itself is easy because the
primes dividing q split, but principality is not inferred from balance.
The accepted q=5 balanced nonprincipal ideal remains nonprincipal and
does not contradict this conditional statement.

## 7. R8E: finite arithmetic criterion and both sufficiency tests

At every ell dividing q all primes of F split into distinct conjugate
pairs. With e_i=v_ell(q), every integral balanced ideal is exactly

    product_i P_i^a_i c(P_i)^(e_i-a_i), 0<=a_i<=e_i.

Outside q balance and nonnegative valuations force zero support, including
at p; no extra prime is omitted. Its class is c0+sum a_i delta_i, with
c0=sum e_i[c(P_i)] and delta_i=[P_i]-[c(P_i)]. Under odd h(F), the vanishing
of some such class is equivalent to actual T-stable existence by R8D.
Thus the finite interval test is BOTH necessary and sufficient with that
hypothesis. It is not an evaluated class-group computation here.

Since product_i(P_i*c(P_i))^e_i=(q), one has
2c0=-sum e_i delta_i. Let m_i be the order of delta_i. The full C is
odd, so each m_i is odd and 2 is invertible modulo m_i. Under
e_i>=m_i-1, its unique half-residue a_i in [0,m_i-1] lies in the allowed
interval. Then twice the chosen class is zero. Oddness of the FULL C,
not just of the individual m_i or of T, forces the class itself zero.
The case m_i=1 gives a_i=0 and is included. Reversing a pair replaces
a_i by e_i-a_i and leaves the ideal test unchanged.

If exp(C) divides every e_ell, the SINGLE extreme choice all a_i=0
has c0=0. Hence a principal balanced ideal exists. Intermediate a_i
need not be multiples of the exponent and are not declared principal.
Class-number one is included. These are sufficient conditions, not
necessity claims, verified new q, or a newly established infinite family.

## 8. R8F and preserved obstructions

For an actual set let alpha be the normalized character and a=(alpha).
Every sigma_t preserves F, commutes with c, and fixes rational q, so it
preserves the relative norm q even though it may move E pointwise.
If it fixes the EXACT ideal a, sigma_t(alpha)/alpha is an integral unit
of norm one. It is +/-1. Both character values reduce to k at the unique
p-prime, so its residue is 1, excluding -1. Thus the character is fixed
and unique fixed-augmentation lifting gives tD=D.

Conversely, a numerical multiplier gives tD=D+b. In the common zero-sum
frame, k*b=0 modulo p and k is invertible, so b=0. Evaluation fixes alpha,
and hence its exact ideal. This proves the FULL numerical multiplier
group identity, without an odd-class-number hypothesis once D exists.
It is not a description of all collineations. Replacing a by [a] would
give all G0 because [a]=0; the attributed actual classical q=5 example
has |M|=3 and |G0|=30, so the distinction matters.

I also challenged the proof by dropping hypotheses. If T were trivial,
zeta_p itself would be a nontrivial norm-one unit, breaking uniqueness;
the actual domain forbids this. A field norm may have opposite valuations
at conjugate primes, so it does not prove integrality. A positive unit
need not be a square; the Gamma quotient retains that obstruction when
not discharged. The q=5 nonprincipal ideal still prevents a universal
principality inference. At composite v, the old q=16 proper-quotient
gluing failure and full integral Fourier conditions remain outside R8.
The individual/common-subgroup repair, automatic final R4 moment,
saturation and classicality qualifications, and Cohen exceptions remain
unchanged. None is silently strengthened by this packet.

## 9. Sources, preservation and completion

The companion source record gives actual original theorem passages read,
fresh read limits, and unimported literature. No native primary-paper
download or invented byte hash was produced. A direct Milne URL returned
an internal web error promptly; the ordinary public author-page link
resolved the PDF in the next bounded retrieval. There was no native
retrieval wait or access bypass.

Input hashes are reverified administratively and compactly bound in the
input-validation record. This is preservation evidence, not mathematical
proof. Older metadata parents are bound by exact path/bytes/SHA and
occurrence/deduplicated summaries, rather than recopying the historical
inventory. No old mathematics is claimed freshly reread merely because
its hash was checked. The whole review and all 54 ledger dispositions
precede the immutable manifest and any peer comparison.

The last consistent direct weekly reading was 65% at 20:39:15 UTC,
reset 1792745187. A later same-account tool reading changed to 0% and
reset 1792874445 at 20:43:51 UTC, matching the root's reported anomaly.
It is NOT treated as a fresh allowance or permission to spend into a new
window. Per the root's instruction, this already-underway full freeze
uses integration reserve; no next research/audit task starts until the
budget continuation question is resolved. Nothing in this administrative
constraint abbreviated the whole mathematical reconstruction.
