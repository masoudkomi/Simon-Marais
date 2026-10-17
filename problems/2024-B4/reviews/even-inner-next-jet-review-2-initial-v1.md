# Initially blind whole NJ-v2 review R2

2026-10-17 UTC. Reviewer `/root/review_2022_complexity_r2`.
Requested model/reasoning: `gpt-6.1-sol` / `max`; independent effective-setting
readback is unavailable. This is a COMPLETE initial nonconstructor review,
frozen before reading any new NJ peer report, ledger or coordinator finding.
Only the coordinator may promote a result after the other whole audit and
reconciliation.

I find no substantive defect in the submitted NJ1-v2 and NJ2-v2 scopes. The
coefficient at order M+1 supplies a contradiction for every larger even
target index, rather than just an obstruction at finitely many indices.
The argument permits arbitrary extension coefficients and inseparable
outer polynomials. The whole-divisor consequence concerns only the fixed-q
GK family and even inner indices. It does not classify the official odd
exponents or the other factors of these polynomials.

## Submission, independence and read scope

The target is the COMPLETE 12232-byte
`notes/coordinator-even-inner-next-jet-return-v2.md`, SHA256
`5197ab6841d0a97356484cf3a08a7163055449fa879bd8010886e28158532ef6`,
and its 2368-byte `notes/coordinator-even-inner-next-jet-manifest-v2.json`,
SHA256 `7aec0a9fd4109910ea8d95e3b8e50860c4e8083bbe82249196617274d95b03a3`.
I read the full main file, including all ten final obligations, failed
routes and scope qualifications. The earlier P2-only v1 is fingerprinted
history: I did not use it as a theorem or assume its proof correct. No
extension-only audit was substituted for reconstructing the complete v2.

Root constructed NJ-v2. I supplied no part of this new proof. My older
2024 roles include whole reviews of structural/divisor/GK packets and a
necessary-valuation review. Those roles concern earlier inputs. I have
now reread the complete accepted GK, CP and CJ mathematical bodies and
their acceptance scopes; the source record distinguishes mathematical
reads from metadata-only checks of historical reviews/certificates.
Prior review of GK is disclosed rather than counted as a new NJ proof
contribution. Root's new NJ conclusions and the other NJ review remain
unread. No peer comparison occurred before this freeze.

## Official domain and exact proposed assertions

The official 2024 Paper B, page2, asks in (b) for all positive odd n whose
specified homogeneous numerator has the prescribed product modulo2 with
two integer polynomials nonconstant modulo2. Congruence is coefficientwise.
No preliminary proof is reproduced here. The n1 zero numerator cannot be
a product with two nonzero nonconstant factors in the polynomial domain;
the n3 quotient is the unit1. Both endpoints remain outside the qualifying
factorizations discussed by the accepted inputs.

Fix an integer k>=2 and q=2^k. Let

    A=T^q+(T+1)^(q-1), B=(T+1)^(q-1),
    P0=1, P1=T,
    P_(i+2)=A^(q^(2i+1))*P_(i+1)+B^(q^(2i+1))*P_i.

The accepted degree is E_i=sum_(a=0)^(i-1) q^(2a), i>=1, and
F=P2=T^(q^2+1)+(T+1)^(q^2-q+1). NJ1 says that, over every
algebraically closed field K of characteristic2, for every even r>=2,
every s>=1 and H in K[T], P_s=H(P_r) occurs exactly at s=r,H=T.
P0 is excluded, since a constant outer polynomial would otherwise give
immediate compositions. Odd inner indices, decompositions through some
other polynomial and arbitrary-factor statements are not assertions.

For d=q^2-q+1 and L_i=(q^(2i+1)+1)/(q+1), NJ2 says that the WHOLE
homogeneous phi_(L_r) divides phi_(L_s) over F2 exactly at s=r in the
same index range. Both parameters are odd and at least3. The claim is
negative for every other s in this family, not for all odd n.

## Reconstruction of the exact accepted inputs

The accepted GK proof is an unrestricted polynomial argument. In an
auxiliary algebraic closure of F2(a), with a transcendental, choose
v=(u,v0) satisfying u^(q+1)=a, v0^(q+1)=a+1. Put
D_i=v dot v^[2i+1] and c=D1=g_d(a^2+a). The four pairings of v,v^[2]
against v^[1],v^[3] form the matrix with columns (1,1) and (1,c).
Its determinant c+1 is nonzero because g_d is nonconstant. Hence both
the vectors and the functionals are bases. Solving for v^[4] gives the
FULL vector equality

    v^[4]=A(c)v^[2]+B(c)v,

with B(c)=(c+1)^(q-1) and A(c)=c^q+B(c). Raising to q^(2i+1) and
pairing with the original v gives the exact recurrence above, initial
values D0=1,D1=c, and D_i=P_i(c). Substitution at the transcendental
a and then injectivity of U->a^2+a establish g_(L_i)=P_i(g_d) as a
polynomial identity. No finite specializations or zeros of the canceled
temporary denominator are excluded. A and B are monic of degrees q and
q-1. The two recurrence summand degrees differ by q^(2i)(q+1)>0,
which proves the monic degree formula without cancellation. These are
the GK facts actually needed here. Its phi13 comparison is not an NJ
premise, and its old automaton certificate is not rerun.

The complete accepted CP1 argument also retains the needed scope. The
translation invariant ring in one variable is F2[x^2+x]: every polynomial
has a unique expression U-part plus x times another U-part. Thus the
odd-n invariant g_n exists uniquely, monic of degree (n-1)/2. Set
Q_n(U,V)=(g_n(U)+g_n(V))/(U+V). The invertible homogeneous coordinate
change (X,Y,Z)=(s+u,s,t), followed by u=1, gives

    phi_n(s+1,s,t)=Q_n(s^2+s,t^2+t).

Its degree is exactly n-3: distinct top terms double to distinct top
exponent pairs. Homogenization therefore loses no component on u=0.
The quadratic-cover ring F2[s,t] is free over F2[U,V] with basis
1,s,t,st, so division of a WHOLE element descends to F2[U,V]. For a
monic nonconstant h, the unique h-adic expansion
p(U)=sum_(j<deg h) U^j C_j(h(U)) shows by division that
h(U)+h(V) divides p(U)+p(V) exactly when p=H(h) over F2. Canceling
the same nonzero factor U+V then proves

    phi_a|phi_b iff g_b=H(g_a), H in F2[T],

for all odd a,b>=3. It does not require the diagonal factor to be
coprime to Q_a and does not discard multiplicities. CP2/CP3's old
finite q8 corroboration is not an input to this reconstruction. The
complete CJ body was read as context, but all local calculations used
below are reconstructed directly; its necessary congruence alone would
not prove the new conclusion.

## 1. Degree reductions include every smaller or odd target

E_i increases strictly for i>=1, so P_s is nonconstant and any H in an
equality must be nonconstant with E_s=(deg H)E_r. Thus s<r is impossible.
At s=r, H has degree1. Its leading coefficient must be1, and subtracting
P_r forces its constant term to vanish; H=T, also in characteristic2.
Substitution by a nonconstant polynomial is injective by leading degree.

Modulo the integer q^2+1, E_i is the alternating sum of i copies of1.
It is0 for even i and1 for odd i. Since even r makes q^2+1 divide E_r,
degree divisibility excludes every odd s. This uses integer degrees,
not a characteristic-two reduction of the degree itself. Consequently
only even s>=r+2 remains, without needing r|s or any stronger integer
divisibility classification.

## 2. A genuine finite critical point and all-index recurrences

The exact polynomial identity (T+1)A=T^(q+1)+1 gives q simple roots of
A in K, all nonzero, all different from1. Indeed the numerator has
q+1 distinct roots because its derivative T^q has no common root with
it, and the root1 removed by T+1 is simple. Choose any alpha among
the remaining roots. Then alpha^(q+1)=1, alpha^q=alpha^-1, and
alpha^(q^2)=alpha. These facts are used only at this finite constant.

With u=alpha+1, the constant identities are

    u^q=u/alpha, u^(q^2)=u, B(alpha)=alpha^-1,
    B(alpha)^(q^(2i+1))=alpha,
    F(alpha)=alpha^2+alpha*u=alpha,
    A'(alpha)=B'(alpha)=u^(q-2)=a!=0.

Here q-1 is odd and the derivative of T^q is zero. The recurrence
evaluated at alpha is P_(i+2)(alpha)=alpha P_i(alpha). Starting from
1,alpha proves for every h>=0

    P_(2h)(alpha)=alpha^h,
    P_(2h+1)(alpha)=alpha^(h+1).

Every recurrence coefficient has formal derivative zero because its
exponent q^(2i+1) is a positive power of2. Differentiating before
evaluating gives the same two-step recurrence for derivatives, with
initial0,1. Therefore

    P_(2h)'(alpha)=0, P_(2h+1)'(alpha)=alpha^h.

In particular the later odd derivative is nonzero for arbitrarily large
h. There is no periodicity assertion about Frobenius on T or on all K.

## 3. Exact order q at every even inner index

Put Z=T-alpha. F'=A^q, so F has no linear term in its local difference.
The characteristic-two binary expansion shows no exponent between2
and q-1 in either summand of F: the support bits of q^2+1 are0,2k;
those of q^2-q+1 are0,k,k+1,...,2k-1. At exponent q only the second
summand contributes, with coefficient u^(q^2-2q+1)!=0. Consequently

    ord_Z(F(alpha+Z)-alpha)=q.

This proves exact ramification order directly; the vanishing derivative
alone would not do so. For every even i>=2, N=q^(2i+1)>=q^5 and
Frobenius give A(alpha+Z)^N=0 modulo Z^N and
B(alpha+Z)^N=alpha modulo Z^N. Hence

    P_(i+2)(alpha+Z)=alpha P_i(alpha+Z) mod Z^(q^5).

Iteration yields P_(2h)=alpha^(h-1)F modulo Z^(q^5), h>=1. At r=2h,
beta=P_r(alpha)=alpha^h and

    V(Z)=P_r(alpha+Z)-beta
        =alpha^(h-1)u^(q^2-2q+1)Z^q+ higher terms.

Since q^5>q, its order is exactly q. It causes no problem if beta is1
or repeats for several choices of h, or if several critical points share
a critical value. Only one alpha and the exact order are required.

## 4. The next recurrence supplies an uncancelled M+1 coefficient

Fix even r=2h>=2 and M=q^(2r+1)>=q^5. The exact next recurrence gives

    R(Z):=P_(r+2)(alpha+Z)-alpha P_r(alpha+Z)
        =A(alpha+Z)^M P_(r+1)(alpha+Z)
           +(B(alpha+Z)^M-alpha)P_r(alpha+Z).

Both coefficients on the right have zero constant term and support only
at positive multiples of M; their first coefficients are a^M at Z^M.
Thus ord R>=M. Since 2M>M+1, the only contribution of the first
summand to Z^(M+1) is a^M times P_(r+1)'(alpha)=alpha^h. The second
would require P_r'(alpha), which is zero. It follows that

    [Z^(M+1)]R=a^M alpha^h!=0.

There is no unnoticed term of A^M at M+1 and no omitted constant term
from B^M-alpha. The coefficient at M is not needed, so no assumption
about its cancellation enters the proof.

For every later even recurrence the exponent is at least
q^(2r+5)>M+1. Thus, in K[Z]/(Z^(M+2)), it merely multiplies the prior
even polynomial by alpha. For even s>=r+2, set t=(s-r-2)/2>=0 and
c=alpha^(t+1). Then

    P_s(alpha+Z)=alpha^t P_(r+2)(alpha+Z) mod Z^(M+2),
    ord_Z(P_s(alpha+Z)-cP_r(alpha+Z))>=M,
    [Z^(M+1)](P_s-cP_r)=alpha^t a^M alpha^h!=0.

The smallest target s=r+2 has t=0 and multiplier1. Later iterations
produce a multiplicative power of a nonzero field constant, not a sum
of identical terms; characteristic2 cannot annul it by counting steps.

## 5. The forbidden exponent argument includes every outer polynomial

Assume P_s=H(P_r), and let K_beta(Y)=H(Y)-cY. If it is the zero
polynomial, then P_s-cP_r is zero, contradicting the displayed nonzero
coefficient. Otherwise factor it at beta exactly as

    K_beta(Y)=(Y-beta)^m W(Y), W(beta)!=0, m>=0.

By the exact order of V, substitution has order qm, since W(P_r) is
a unit in K[[Z]]. The order bound above forces

    m>=N=M/q=q^(2r).

This is an integer lower bound even if H has zero derivative or the
initial coefficients vanish. The expansion at beta therefore is

    K_beta(beta+Y)=b_N Y^N+sum_(j>=N+1)b_jY^j,

where b_N is allowed to be zero. N is a positive power of2 greater
than1. Frobenius makes every exponent of V(Z)^N divisible by N,
regardless of its coefficients in K. But M+1=qN+1 is1 modulo N,
so this first term contributes zero there. Every later term has order
at least q(N+1)=M+q>M+1. The whole composition therefore has zero
coefficient at M+1, in contradiction with the previous section.

This proves the exclusion for every larger even s. It is an exact
polynomial/local-order proof, not extrapolation from a finite jet scan.
No separability, nonzero H'(beta), distinct critical values or outer
coefficient-field descent is assumed. Together with the degree
reductions it proves NJ1 in its complete stated domain.

## 6. Whole-divisor transport and application limits

For i>=1 the integer L_i is odd, at least d>=13, and the exact GK
identity is g_(L_i)=P_i(g_d). CP1 is applicable to a=L_r,b=L_s.
A hypothetical whole phi_(L_r)|phi_(L_s) therefore supplies H in
F2[T] with

    P_s(g_d)=H(P_r(g_d)).

The nonconstant g_d has degree (d-1)/2, so substitution by it is
injective on F2[T]. We recover P_s=H(P_r), now a special case of
NJ1 over an algebraic closure. It forces s=r,H=T. Conversely s=r
is polynomial equality and hence divisibility. No factor-field
assumption or tests at finite points enter this direction.

The equality case has a unit cofactor, so NJ2 by itself supplies no
qualifying two-positive-degree official factorization. For s>=2 the
accepted smaller whole divisor phi_d still supplies the GK examples;
NJ2 does not make phi_(L_s) irreducible. It excludes neither a proper
component of phi_(L_r), an odd-index whole divisor, another univariate
inner polynomial nor an exponent outside this fixed-q family. The
unverified DI packet is not a premise. L0=1 is not passed through CP1.
No new APN, monodromy, Ritt or decomposition theorem is imported.

## Adversarial result and required handoff

The complete 36-check ledger covers all ten author obligations and the
exact accepted premise bridges. I challenged the root/simple-order
step, repeated critical values, the possible second-summand cancellation,
large even targets, zero comparison polynomial, strictly larger local
order, arbitrary coefficients, inseparable H, small parameter endpoints
and homogeneous descent. Each is resolved by the calculations above.
No author repair is requested by this initial review. This finding is
not an acceptance or an assertion that no overlooked error is possible.

All earlier own frozen packets are preserved. The new integrity record
hashes the target, exact accepted bodies/acceptances, their declared
metadata, public cache references and the prior own freeze chain. Such
hashes attest integrity, not mathematics. No mathematical program, CAS,
scan, certificate replay, author rerun or candidate/shared/Git edit was
performed. The latest direct account-wide reading used here was44%
TOTAL weekly at2026-10-17 14:21:40UTC, reset1792745187, below the90%
total ceiling with reserve. Source read limits and old-role disclosures
are in the separate source check; no whole external proof is claimed.
