# Initially blind whole reconstruction R1: CP1–CP3

2026-10-17 UTC. Reviewer coordinator root, nonconstructor of this packet.
The COMPLETE initial report, inference ledger and source checks are frozen
before reading any fresh CP peer report or receiving its findings. Root
requested a complete checkpoint and audits but supplied no mathematical
step of CP1–CP3 to its constructor. The earlier coarsening/strict strategy
contribution concerns a different year's tiling program. A later MCM
literature lead read by root is not a premise or repair of this proof.

**Finding: no substantive objection to CP1–CP3 in their precise partial
scope.** This is one whole audit only, not coordinator promotion. The
second whole audit, full reconciliation and integrity checks remain
necessary. No complete reducibility classification or novelty claim.
No mathematical computation, certificate rerun, enumeration or CAS was
used in this review. Administrative hashes do not prove the theorem.

## Official target and the dependency boundary

I directly reopened official2024PaperB p2 B4(b): n is a positive odd
integer, equality is coefficientwise modulo2, and both integer factors
must be nonconstant modulo2. The new construction concerns a specified
infinite subset and a whole-fixed-divisor equivalence. It neither solves
the preliminary(a) question as a substituted target nor claims the
subset is all admissible exponents. The F2 domain has no zero divisors.
The established quotient phi_n=f_n/R is used for odd n>=3. The accepted
whole-phi13 theorem is used ONLY for the final nonoverlap comparison.
All new mathematical steps are supplied explicitly in the main packet.
No HM exceptional-component theorem, original Janwa–Wilson factor theorem,
Férard theorem or MCM monodromy theorem is imported to make them work.

## 1. Translation invariants and the actual homogeneous polynomial

Write U=s²+s. Repeated use of s²=U+s expresses each polynomial uniquely
as A(U)+sB(U). The leading degrees of the two nonzero summands have
opposite parity, so independence follows. Replacing s by s+1 adds B(U);
therefore an invariant polynomial lies exactly in F2[U]. For odd n>1,
G_n=s^n+(s+1)^n is invariant, nonzero, and its leading term is s^(n−1).
Thus g_n is uniquely defined, monic, and has degree e_n=(n−1)/2. This is
an identity of polynomials, not functions evaluated on a finite field.

The change(X,Y,Z)=(s+u,s,t) has explicit inverse(Y,Z,X+Y), so it is a
linear homogeneous automorphism. At u=1 its numerator is G_n(s)+G_n(t),
and its prescribed denominator is(s+t)(s+t+1)=U+V, with V=t²+t.
Consequently Psi_n=Q_n(U,V), Q_n=(g_n(U)+g_n(V))/(U+V), exactly in the
polynomial ring. Each power-sum difference is divisible by U+V, and the
top homogeneous difference quotient is nonzero even when e_n is even.
Hence deg Q_n=e_n−1. The quadratic substitution doubles the top total
degree without cancellation: distinct top exponent pairs give distinct
s^(2a)t^(2b). Thus deg Psi_n=n−3, the FULL homogeneous degree.

It follows that phi_n(s+u,s,t) is precisely this full-degree
homogenization; there is no lost u factor. If Psi_n=Psi_d C, total
degree is additive for a nonzero product over a domain, so deg C=n−d.
Homogenizing at those exact degrees gives phi_n=phi_d times the
homogenized cofactor after reversing the linear map. Conversely a
homogeneous division dehomogenizes. For n<d,d>=5 the degree obstruction
correctly prevents division. For d=3 the divisor is the unit and no
positive-degree claim about it follows.

## 2. Whole descent is stronger than a statement about individual factors

F2[s,t] is free over F2[U,V] with basis1,s,t,st. Reduction by the two
monic quadratics gives spanning. For independence, expand in monomials
U^aV^b s^epsilon t^delta; leading exponent pairs(2a+epsilon,2b+delta)
are distinct. The largest such pair in a monomial order cannot cancel,
including terms on coordinate axes. Thus the embedding and basis hold.

If two nonzero base-ring elements satisfy B=A C in the larger ring,
expand C in this basis. The three nonconstant-basis coefficients are
annihilated by A and therefore vanish in the base domain. This puts C
back in F2[U,V]. In particular WHOLE Q_d divisibility descends. This
argument asserts no descent for arbitrary factors of Q_n after the
quadratic substitution; such a stronger assertion would be false in
general and is not needed.

## 3. Exact composition from monic division, without separability

For monic h of degree e>=1, successive Euclidean divisions give
p(U)=sum_(j<e) U^j C_j(h(U)). Nonzero summands have leading degrees
distinct modulo e; uniqueness follows. In the ring F2[V][U], divide
p(U)+p(V) by the MONIC polynomial h(U)+h(V). Its remainder has degree
less than e in U and equals sum_(j<e) U^j C_j(h(V))+p(V).
Divisibility forces each coefficient C_j(h(V)),j>=1,to vanish.
Composition with nonconstant h(V) is injective by degree, so these
C_j are zero and p=C_0∘h, over F2 itself. Conversely composition
implies difference divisibility by the universal A+B factor identity.
No nonzero-derivative or separability assumption is necessary.

Now Delta g_d=(U+V)Q_d and Delta g_n=(U+V)Q_n. Cancelling the SAME
nonzero element U+V converts divisibility in either direction, without
assuming it is coprime to Q_d. Repeated diagonal factors are retained.
Combining this with the two previous sections proves the whole CP1 iff.
The nonconstant H degree is e_n/e_d, proving d−1 divides n−1. At d=n,
H has degree1, leading coefficient1 and constant determined by g(0)=1,
so it is T. At d=3,g_3=T+1 and composition always exists. At n=3 and
d>3 it cannot exist by degree. These edge cases agree with phi3=1.

## 4. Independent reconstruction of the unrestricted q identity

Let a=s,b=s+1, w=ab, p=a^(q−1)+b^(q−1), c=a^d+b^d,
q=2^k>=2,d=q²−q+1. Expanding w p^(q+1) gives the four monomials

    a^(q²)b, a^d b^q, a^q b^d, a b^(q²).

Add c. Group a^d(1+b^q)=a^(d+q) and its b counterpart, using
1+b^q=a^q. Since d+q=q²+1, the remaining two pairs are
 a^(q²)(a+b)+b^(q²)(a+b)=a^(q²)+b^(q²)=1.
Thus c+1=w p^(q+1), with no division or excluded point.

For N=q4−q3+q²−q+1, direct integer multiplication gives
 d(q²+1)=N+q², q²−d=q−1, N−d=q³(q−1),
 d(q²−1)=(q³+1)(q−1), d(q+1)=q³+1.
Expand c^(q²+1)+a^N+b^N, using Frobenius at q². Its four terms are
 a^N b^(q²), b^N a^(q²), a^(dq²)b^d, b^(dq²)a^d.
Factor w^d from these, leaving respectively
 a^(q³(q−1))b^(q−1), b^(q³(q−1))a^(q−1),
 a^((q³+1)(q−1)), b^((q³+1)(q−1)).
Their sum is exactly p^(q³+1), since q³ is a Frobenius power. Hence
 c^(q²+1)+G_N=w^d p^(q³+1)=(w p^(q+1))^d=(c+1)^d.
All exponents are nonnegative at q=2 and larger; all identities are
in F2[s]. Injectivity of U=s²+s then yields CP2 in F2[U]. CP1 gives
the FULL homogeneous divisor over F2, independently of absolute factors.

## 5. Proper factors and the infinite nonoverlap comparison

For odd n>1 the mixed coefficient X^(n−1)Y of f_n is1, so the quotient
is nonzero homogeneous of degree n−3. CP2 therefore supplies a nonzero
cofactor of degree N−d=q³(q−1). The divisor has degree d−3=q²−q−2.
Both are positive for q>=4, and lifting coefficients to0/1integers gives
the exact requested congruence. Neither factor needs to be irreducible.
At q=2,d3 the divisor is1: this is no qualifying factorization. At
q=4,d13,N205 the result is attributed prior context, not a novel example.
The advertised range k>=3 has first d57,N3641 and degrees54,3584.

Finally N−1=q(q−1)(q²+1), giving v2(N−1)=k. Distinct k therefore give
distinct exponents. The accepted phi13 theorem's sequence has
 n_m−1=4(16^(m+1)−1)/5 of valuation2 for all m>=0.
Thus the new advertised k>=3 sequence lies outside it. Applying that
EXACT accepted criterion also excludes whole phi13 at those new n.
The family proof itself is independent of that comparison theorem.
No conclusion about other factors or all irreducible exponents follows.

## Source, finite evidence and disposition

I read the entire main, source/obligation/failed-route/worklog packet,
source JSON and exact author freeze, and reread the full accepted
phi13 exposition and its precise acceptance scope. The primary official
part(b), HM Section2.3 and Section6 were directly reopened. HM's known
205 example is retained as attribution; its universal component result
and its long proof are not imported. The constructor's original-source
access gaps remain explicit. No claim of a full original Janwa–Wilson,
Férard or MCM proof read is made here.

I inspected the saved q8 job/completion/certificate metadata and the
constructor's stated exact symbolic role. Its extraction is not a
premise: every q is proved above, so neither an author rerun nor a second
mathematical finite check is needed for this review. The finite case
cannot imply an unrestricted theorem, an all-m extension or a complete
classification. The initial report finds no substantive issue under
the exact scope. Another fresh whole audit and root reconciliation
remain necessary. No peer CP findings were read before this freeze.
