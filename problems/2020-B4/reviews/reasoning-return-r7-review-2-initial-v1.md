# 2020 R7: initially blind whole independent review 2

2026-10-17 UTC. Reviewer `/root/review_2017_coarsening_r1` (C).
Requested `gpt-6.1-sol`, reasoning `max`; effective-setting readback is
unavailable. This is the complete initial nonconstructor WHOLE audit of
`notes/reasoning-return-r7-candidate-v1.md`, 21471 bytes,
SHA256 `4a0866b149aab5beb0dd0b7e76bf6abaf90355085178ea8ea18b2b539e5abe7b`,
and its complete ten-artifact construction packet. The constructor freeze
is 4168 bytes, SHA256
`b83040ef82ae1b4ef8393b4d1c8799fd095ed4d81a52a7ebb03aff8087fb649a`.
All 56 author obligations have separate independent ledger rows.

**Initial verdict:** no substantive mathematical defect or required
repair found in the exact R7A--R7E partial scope. These are an arithmetic
existence equivalence and two obstructions to weaker realization rules;
they do not classify taut integers or give a new forbidden order. This
is one independent audit, not coordinator promotion or a full annual
solution. All new root/peer R7 reports, ledgers, sources, metadata and
findings remained unread through the entire initial freeze. The verdict
and mathematical findings are to be withheld from root until root's own
complete initial R1 has frozen.

I did not construct or contribute a mathematical inference to NEW R7.
I authored the older repaired R3 F1/F2 and accepted R6 packet, and
reviewed earlier R4/R5 work, including the R4 repair. Those separately
accepted inputs have other independent audits. This audit does not count
as a fresh independent recertification of my own old inputs. The new
R7 proof is reconstructed below rather than accepted from the author
checks, old review conclusions or an authority metadata label.

## 1. Official target and actual inputs

The actual official B4 asks which integers n>=2 are taut: there must be
n chosen vertices in a regular (n^2-n+1)-gon with all pairwise distances
different. Only part (b) is under investigation. I read the official B4
text and local statement; the accepted part-(b) dictionary is a named
input, not a new preliminary proof here. For q=n-1>=2, put k=q+1,
v=q^2+q+1 and G=C_v. The dictionary requires an ACTUAL k-element subset
D, every nonzero ordered difference appearing exactly once. The accepted
n=2 boundary is retained separately. An abstract incidence matrix,
integer multiset or algebraic integer alone is not this dictionary.

The complete accepted initial header and linked body, repaired R4,
accepted R5 and R6 bodies and the three current acceptance Markdown
scopes were read. R3's common/individual fixed-subgroup qualification
was rechecked in its header/initial section; its full older proof is
inherited, not claimed freshly reread in full. All exact fingerprints
and metadata preservation references are bound by the review freezer.

The accepted context used here is limited: DD^- = q*1+N_G, the one
sum-zero translation using gcd(k,v)=1, the planar First Multiplier
Theorem, and attributed known Singer existence at prime-power q=16.
R4 saturation is extra. R5's normalizer result needs an ACTUALLY
Desarguesian plane. R6 is necessary actual-set information, not a
realization theorem. Cohen's two literal q=4 exceptions cannot be
applied to a multiset or a tentative tuple. No new R7 proof requires
the detailed Cohen sieve or a classical-plane classification.

## 2. R7A reconstructed: all orders, rational identity, integral recovery

Fix zeta_v and zeta_d=zeta_v^(v/d). Every j!=0 has exactly one expression
j=(v/d)b with d>1 dividing v and b a unit modulo d: d is the order of
the character x -> zeta_v^(jx). Assign F(0)=k and
F((v/d)b)=sigma_b(alpha_d). This prescribes EVERY frequency exactly
once, including nonprimitive frequencies at composite v. The inverse is

    a_x = (k + sum_(d|v,d>1) Tr(alpha_d*zeta_d^(-x)))/v.

The trace equals the sum over all units b of
sigma_b(alpha_d)*zeta_d^(-bx), so its sign and factor 1/v are correct.
Fourier orthogonality then gives A(zeta_v^j)=F(j) and augmentation k.
The trace numerators are integers, hence every a_x is rational. This
requires no nonnegativity assumption. Integer traces follow because
the products in each trace are algebraic integers and rational traces
of algebraic integers are ordinary integers.

Complex conjugation commutes with every sigma_b. Thus F(-j)=bar(F(j))
and F(j)F(-j)=q for every j!=0. The principal value is k^2=q+v.
Characters separate Q[G], so these are exactly the character values
of AA^-=q*1+N_G. At coefficient zero and at augmentation this gives

    sum_x a_x^2=k,       sum_x a_x=k.

If every trace numerator is 0 modulo v, all a_x are integers. For ANY
integer a, a(a-1)>=0, including a<0. The displayed two sums force
sum a_x(a_x-1)=0; hence each coefficient is 0 or 1. Augmentation gives
precisely k distinct points, and the nonzero coefficients of AA^- give
the required ordered-difference property. Conversely, an actual set
with the specified order-d values has this inverse by uniqueness and
so satisfies every divisibility congruence. This proves the advertised
iff, not just a necessary test.

For T invariance, F(tj)=F(j) holds for every t in T because the action
at order d is the image of t modulo d. Fourier inversion gives
a_(tx)=a_x. If these coefficients are integral, the resulting actual
D is T-stable. S=sum_(x in D)x is fixed by EVERY t in T; it belongs
to the COMMON fixed subgroup G^T. Since gcd(k,v)=1, c=-k^(-1)S is in
that same subgroup and D+c has sum zero while remaining T-stable.
Each new phase is alpha_d*zeta_d^c, fixed because (t-1)c=0 modulo v.
No element's individual fixed subgroup is substituted for G^T.

This exact equivalence does not solve the simultaneous congruences.
Its sufficiency uses complete coherent character data and joint
integrality; the primitive component alone is insufficient in general.

## 3. R7B reconstructed: why prime modulus changes the lift

Let p=v be prime. Then p>=7, k is nonzero modulo p and q=k^2 modulo p.
For K=Q(zeta_p), the attributed integral basis is O_K=Z[zeta_p].
Modulo lambda=1-zeta_p, O_K/(lambda)=F_p and conjugation is the
identity. Therefore beta*bar(beta)=q implies beta^2=k^2 modulo lambda.
The two roots k,-k are distinct, so exactly one sign alpha=+/-beta has
residue k. This is a RELATIVE conjugation-norm equation as a field
identity, not an absolute norm condition.

Represent alpha with integral coefficients in degrees 0 through p-2,
append coefficient zero in degree p-1, and call their sum s. The
residue condition is s=k modulo p. Adding the same integer (k-s)/p
to all p coefficients changes evaluation by a multiple of Phi_p(zeta_p)
=0 and changes augmentation to k. This constructs the integral lift.

An integral polynomial of degree at most p-1 vanishing at zeta_p is an
integer multiple of Phi_p: divisibility over Q and equal degrees give
a rational scalar, whose leading coefficient is integral. Thus the
kernel Z[C_p] -> O_K is exactly Z*N_G. In particular, the lift with
given augmentation is unique. AA^- -q*1 lies in that kernel; writing
it c*N_G, augmentation gives cp=k^2-q=p, so c=1. The same integer
coefficient argument from section 2 makes A binary. Necessity is
evaluation of an actual difference set. No saturation or numerical
multiplier size is needed for this equivalence.

For F=K^T, O_F=O_K intersect F. The sign choice stays in F. If beta
is in O_F, then for t in T the integral group-ring elements A and tA
have the same evaluation and augmentation, so the fixed-augmentation
kernel argument makes them equal. Conversely, a T-stable D evaluates
in O_F. If T is nonidentity, G^T=0 since a nonidentity element of F_p^*
fixes no nonzero additive residue; the resulting D already has sum zero.

For ANY actual D put in the common sum-zero frame, a numerical multiplier
tD=D+c has kc=0, hence c=0. Therefore M is exactly the Galois stabilizer
of alpha=D(zeta_p), namely Gal(K/Q(alpha)). This is not an identification
of M with the full plane automorphism group, and a specified T need not
equal M.

The auxiliary norm-one proof works for EVERY odd prime p, including p=3.
For u*bar(u)=1 choose the sign of residue 1, lift with augmentation 1,
and use the kernel to obtain UU^-=1: the multiple c*N_G has augmentation
cp=0. Then the integral squared coefficient sum is 1 and coefficient sum
is 1, forcing one positive coefficient 1. Thus u=+/-zeta_p^c. If T is
nonidentity and u is fixed, (t-1)c=0 forces c=0, so u=+/-1. This says
nothing about surjectivity of norms on all totally positive units.

## 4. R7C reconstructed: three genuinely separate arithmetic conditions

For every T the field F=K^T is stable under conjugation because the
cyclotomic Galois group is abelian. The existence of alpha in O_F with
alpha*bar(alpha)=q is equivalent to existence of an integral ideal a
such that a*bar(a)=(q), a=(gamma), and the unit equation

    u*bar(u)=(gamma*bar(gamma)/q)^(-1)

has a solution u in O_F^*. Necessity uses a=(alpha), gamma=alpha, u=1.
For sufficiency alpha=u*gamma is integral and has the required norm.
The direction of the inverse on the right is correct. From ideal balance
and principality, epsilon=gamma*bar(gamma)/q has trivial principal ideal,
so is a unit. It is fixed by conjugation, and every real embedding of
the fixed real field sends it to |sigma(gamma)|^2/q>0. Positivity alone
does not solve the unit equation, even if F is real.

Changing gamma to w*gamma changes epsilon to w*bar(w)*epsilon; the
existence of the correcting unit is unchanged. Two norm-q generators
for the SAME ideal have ratio a unit of conjugation norm one. For
nonidentity T the preceding lemma restricts that ratio to +/-1. This
does not count different ideals or all difference sets.

For ell|q, ell!=p and is unramified in the cyclotomic field and F.
Valuations of ideal balance give a_P+a_bar(P)=v_ell(q), including the
case P=bar(P), where this is twice a_P. Thus a self-conjugate prime
requires even valuation. If T contains the Hall multiplier ell, its
Frobenius restricts trivially to F, so ell splits completely there.
For odd T, -1 is not in T, conjugation on F is nonidentity, and its
free action on the completely split primes pairs distinct primes.
Neither splitting nor parity proves principality or the unit equation.
The argument also covers the T={1}, T containing conjugation and
F=Q cases without a hidden nontrivial-CM hypothesis.

## 5. R7D reconstructed: balanced nonprincipal ideal in the actual field

At q=5, p=31, T=<5> has order 3 and F=K^T has degree 10. This is a
specified known subgroup; no equality T=M or saturation is assumed.
The square subgroup R has order 15 and contains T, so E=K^R is a
quadratic subfield of F and [F:E]=5.

For the quadratic character chi, tau=sum_(x!=0)chi(x)zeta_31^x has
sigma_a(tau)=chi(a)tau by substitution. As chi(-1)=-1, bar(tau)=-tau.
In tau*bar(tau), put x=ty. The inner sum over y!=0 is 30 for t=1
and -1 otherwise. Its value is 30-sum_(t!=0,1)chi(t)=31. Consequently
tau^2=-31. It is nonrational and fixed by R, identifying E with
Q(sqrt(-31)); this is not a guessed quadratic subfield.

For an integral (a+b*sqrt(-31))/2, trace gives integer a and norm
gives a^2+31b^2 in 4Z. If b=m/n is reduced, n^2 divides 31, hence n=1.
Reduction modulo 4 makes a and b have the same parity. Conversely
omega=(1+sqrt(-31))/2 satisfies X^2-X+8, so O_E=Z[omega]. This checks
possible rational denominators instead of assuming an integral basis.

The maps omega -> 2,4 modulo 5 have distinct norm-five kernels P,Q.
Conjugation sends omega to 1-omega, so Q=bar(P). They are comaximal
since P+Q contains 2 and 5. The reduction of the monic polynomial is
(X-2)(X-4), proving (5)=P*Q, also by norms and the two residue maps.

For gamma=4omega-3=-1+2sqrt(-31), the norm is 125. Its residue is 0
at P and 3 at Q, so unique prime ideal factorization gives (gamma)=P^3.
If P were principal its generator would have norm 5; the established
basis would give integers a,b with a^2+31b^2=20. Nonzero b is already
too large and no integer square equals 20. Thus [P] has exact order 3.
No class-number table or claim that the whole class group has order 3
is used.

Extending to a=P*O_F gives a*bar(a)=(5)*O_F. Milne's ideal-norm
identities apply to this finite separable degree-five extension of
number fields: N_(F/E)(P*O_F)=P^5 and the norm of a principal ideal is
principal. If a were principal, P^5 would be principal; together with
P^3 principal and gcd(3,5)=1 this would make P principal, a contradiction.
This is the exact obstruction; there is no assertion that ideal classes
never capitulate in general.

The example disproves the rule that EVERY balanced ideal in the
multiplier fixed field has a norm-q generator. It leaves other balanced
ideals and known q=5 difference sets untouched. Its input is the
relevant specified F, not a fictitious ideal arising from a claimed set.

## 6. R7E reconstructed: primitive obstruction survives actual quotients

For q=16, v=273=3*7*13, k=17, the primitive element alpha=4 is integral,
has conjugation norm 16 and is fixed by every Galois action. CRT on units
factors Tr(zeta_273^x) into the three nonzero-residue sums. Each is ell-1
if ell|x and -1 otherwise, establishing the written Ramanujan product.

At x=0 the value is 144. At x!=0 a positive product must have exactly
two nondividing prime factors: zero nondividing factors would mean x=0.
The largest possible positive product is at most 144/(2*6)=12. All
negative values satisfy the same upper bound. Thus a 17-element SET
B has trace at most 144+16*12=336 if it contains 0, and at most 17*12
otherwise. But Tr(4)=576. The contradiction uses distinct points only;
no difference property or multiplier bound is hidden in it.

The diagnostic A=4X^0+N_H for H=21Z/273Z has augmentation 17, all-unit
invariance and weighted sum 21(0+...+12)=1638=6v. Its coefficient at
zero is 5 and its primitive evaluation is 4, since a primitive character
sums to zero on H. An order-three character is trivial on H, giving
17 and the wrong norm. It is correctly called a multiset, not an actual
difference set or an input to Cohen/full-multiplier bounds.

For the stronger example, choose ONE attributed actual Singer D0 at
q=16 and put it in the common sum-zero frame. The planar First Multiplier
Theorem applies to 2|q, 2>lambda=1, 2 not dividing v, so D0 is stable
under T=<2>. The order is 12: 2^12=4096=1 modulo 273, while 2^6=64
and 2^4=16 are not 1; every proper divisor of 12 divides 6 or 4.

Retain D0's principal value and every proper-order component and replace
only the order-273 component by 4. All components are integral of norm
16 and fixed by the correct image of T. Their Galois conjugates within
each order give a coherent full Fourier prescription. For each proper
d|273, ALL quotient characters have orders dividing d<273, so they
are unchanged. Inverse Fourier uniqueness on C_d proves that the
ENTIRE quotient coefficient vector is exactly the actual image of D0.
These images may have multiplicities; they are not called difference
subsets in the smaller quotients. All proper quotient data are jointly
from the SAME actual D0, not just separately satisfiable.

Any actual full lift would nevertheless have primitive evaluation 4,
contradicting the trace bound. R7A therefore forces at least one full
inverse coefficient to be nonintegral. Correct T invariance and a common
normalization cannot repair this arithmetic gluing failure. It gives no
nonexistence assertion for q=16. Nor is weighted group sum for a rational
inverse silently treated as a sum of an actual subset.

## 7. Adversarial boundaries, source limits and conclusion

The proof survives the relevant degeneracies: q=1 is outside the new
claims; prime v has p>=7; the auxiliary norm-one lemma alone allows
p=3; k never vanishes modulo prime v; T may be trivial or contain
conjugation; common and individual fixed groups are not interchanged;
proper quotient images may be multisets. Negative integral inverse
coefficients are explicitly ruled out by the integer quadratic argument,
not by an assumed positivity hypothesis. At composite v, failure of
primitive sufficiency is proved without treating tentative components
as an actual set.

Primary contexts actually read and exact hypotheses are documented in
the separate source record. Turyn's complete-character/cyclotomic facts
are used in their stated range, and the reconstruction proofs are
written here. Milne's finite-separable-extension norm statements and
Conrad's Dedekind ideal/norm facts apply to the specific number fields.
The First Multiplier Theorem has its lambda/divisibility qualifications.
No garbled Schmidt PDF, inaccessible Hayashi text, Cohen extension to
multisets, general capitulation assertion or unrestricted cyclic-plane
classification is a missing premise. The methods are classical and
attributed; no novelty or new published computational cutoff is inferred.

The constructor's full failures, check list, worklog, source JSON and
freeze script were read. The script was not rerun. No mathematical code,
CAS, enumeration, old certificate replay or new native mathematical job
was used in this audit. Only source reading and a new review-prefix
administrative fingerprint/JSON freeze were performed. Historical
preservation is bound compactly to immutable parents and verified by
their reproduction references, not copied into another growing list.

The complete ledger has 56 independent rows and zero open substantive
issues. No author repair is required for the stated partial claims.
Prime-modulus norm existence, ideal principality, unit norms and the
general joint congruences remain actual arithmetic tasks. The annual
taut classification, prime-power converse, incidence realization and
any new excluded order remain unresolved. Root alone may promote the
precise result after BOTH full blind audits and reconciliation.
