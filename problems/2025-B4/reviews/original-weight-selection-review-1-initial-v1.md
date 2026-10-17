# Initially blind whole R1 audit: original-weight orbit selection

2026-10-17 UTC. Independent reviewer /root/review_2017_coarsening_r1.
Requested gpt-6.1-sol/max; effective-setting readback unavailable.
Root constructed this NEW OW1–OW3 argument. I did not construct it.

**Verdict:** all18 author obligations reconstruct in the precise
conditional scopes stated. No substantive objection or required repair
was found. OW1 needs a positive half-weight element already in I_f
with nonzero inverse moment. OW2/OW3 need their actual0/1/2 coefficients,
opposite-pair identity and strict ratio-set inequality. No universal
existence hypothesis, Nagell–Ljunggren exclusion or later source-proof
repair follows.

I authored the OLDER, separately frozen FS1–FS3 candidate. This whole
audit is independent reconstruction of NEW OW, not an independent
re-audit of that older theorem. In particular neither the unverified
universal FS2 nor any new FS review conclusion is a premise here.
The accepted MS algebra is a separately reviewed input. Root's older
MS authorship and my older MS whole R2 role remain distinct from
construction of this new argument.

## Scope, target and actual reads

Read the entire6934B OW candidate, all18 obligations, its complete
source/failed-route record and manifest, official local(b) statement,
complete accepted MS1–MS5 body and its exact acceptance scope.
Target main SHA256:
ef41445567edb53e53980b9edfbba2739cb1879f048e19b9e64f48e2e684ad3e.
Target manifest SHA256:
f73e2c9152c196f1b39b360fa7c6fb4ba6d53dcf64a4abb7385c78ced8fc91a3.

The primary Bartolomé–Mihailescu1412.5798v2 definitions of I,
inverse-index Fuchsian/Fueter coefficients and the direct action
functional were directly reopened. No original-weight universal
selection theorem is imported. No new OW peer report/findings were
read before this complete report, issue ledger, source checks and
integrity freeze. No mathematical program, scan, CAS, finite table,
certificate replay or author rerun was used.

The official2025 target remains(b) only, all integer(x,y,n,q) with
n,q>=2, and term count m=n+1. This is algebraic partial progress at
an odd prime p>=5; it does not cover all signed/exponent branches.

## 1. Exact module, indices, norm element and freeness

Use DIRECT indices sigma_a(zeta)=zeta^a. Then

    F(theta)=sum n_a a, M(theta)=sum n_a a^(-1) in F_p.

For multiplication by sigma_h, reindexing yields

    F(sigma_h theta)=hF(theta),
    M(sigma_h theta)=h^(-1)M(theta).

Thus sigma_h theta=theta with M(theta)!=0 forces h=1. Nonzero
inverse moment is sufficient for a free orbit; no converse or
positive-weight shortcut is used.

The group is abelian. Hence I=(vartheta Z[G]) intersect Z[G] is
additive and G-stable directly from its definition, even though
vartheta is initially rational. In the INVERSE coefficient basis,

    vartheta=(1/p)sum_(c=1)^(p-1)c sigma_c^(-1),
    (2-sigma2)vartheta
       =sum_c floor(2c/p) sigma_c^(-1).

Indeed the sigma2-translated coefficient at sigma_c^(-1) is
[2c]_p/p. The resulting coefficients are integral0/1. The
coefficients at c and p-c are complementary, since p is odd and
2c/p is nonintegral. Thus psi1+jpsi1=N belongs to I. Both F(N)
and M(N) vanish because the nonzero field residues and their
inverses each sum to zero. Positivity always means actual integer
coefficients, not residues represented by a positive lift.

## 2. Reconstruct OW1, including the Fueter application

Assume precisely a positive u in I_f with weight(p-1)/2 and
M(u)!=0. For h outside{1,-1}, available since |G|=p-1>=4,

    theta1=2u, theta2=u+sigma_h u

belong to I_f, are positive and both have weight p-1. The moments
are2M(u) and(1+h^(-1))M(u). The first is nonzero because p is odd;
the second because h!=-1. Therefore both orbits are free.

G acts by coefficient permutations, preserving the INTEGER
Euclidean norm. Since u is free and h!=1, u-sigma_h u is a
nonzero integer vector. Its squared norm is strictly positive.
Writing v=sigma_h u with ||v||=||u|| gives

    ||u+v||²=4||u||²-||u-v||²<4||u||²=||2u||².

Conjugate vectors have the same norm, so these two elements are
not conjugate. The proof does not use binary coefficients of u.

For the advertised application put psi_t=Theta_(t+1)-Theta_t,
including t1 where Theta1=0. For1<=t<=p-2, its inverse-index
coefficient at c is

    floor((t+1)c/p)-floor(tc/p) in{0,1}.

It is integral and belongs to I. Replacing c by p-c gives the
complementary coefficient, since neither t nor t+1 is divisible
by p. Thus its weight is(p-1)/2 throughout this full t range,
including beyond the usual displayed generating half-range.
The accepted MS square-sum identity, or its elementary subtraction,
gives

    M(psi_t)=(t²+t+1)/(12t(t+1)).

All denominators are invertible at p>=5. Under the stated
t²+t+1!=0 and F(psi_t)=0, OW1 applies. Nothing in this reasoning
supplies such an action-zero t for every p. A zero inverse
moment at an exceptional cubic root does not meet the hypothesis.
This also keeps F and M, and direct/inverse source indices,
separate.

## 3. Reconstruct OW2 and its strict ratio-set threshold

Assume theta in I_f has n_a in{0,1,2},
theta+jtheta=2N and M(theta)!=0. The coefficient identity is
n_a+n_(-a)=2. Therefore Z={a:n_a=0} and -Z are disjoint; the
2-support is exactly -Z and all remaining coefficients are1.
Summing the identity gives weight p-1.

If Z were empty, no coefficient2 could occur either, so theta=N.
That contradicts M(theta)!=0. Thus z=|Z|>=1. Define delta=theta-N.
It is -1 on Z,+1 on -Z, zero elsewhere, has augmentation0 and
jdelta=-delta. Its support S=Z union(-Z) is nonempty.

For nonzero supports the exact multiplicative ratio identity is

    S/S=(Z/Z) union(-(Z/Z)).

The diagonal ratios of Z/Z all equal1; there are at most z(z-1)
other ordered ratios. Hence |S/S|<=2[z(z-1)+1]. Under the STRICT
displayed inequality this upper bound is less than |G|, so an
h outside S/S exists. Both1,-1 lie in S/S, so h is neither.
Moreover hS intersect S is empty: an intersection would give
h=s/s' with s,s' in S.

Consequently

    theta'=N+delta+sigma_h delta=theta+sigma_h theta-N

has actual coefficients only0,1,2: at most one defect vector is
nonzero at each position. The zero set is exactly the disjoint
union Z and hZ, of size2z. The -1 and+1 defects are never added
at the same position, so there is neither a negative coefficient
nor a hidden cancellation in this coefficient check.

Additivity/G-stability of I and N in I put theta' in I. Direct
moment reindexing gives F(theta')=0, and augmentation gives the
same original weight p-1. The oddness of both defect vectors
preserves theta'+jtheta'=2N. Finally

    M(theta')=(1+h^(-1))M(theta)!=0.

This proves the preserved hypotheses and freeness. Different
zero-counts already imply nonconjugacy. Independently the defect
augmentation makes delta orthogonal to N, and its shifted support
is disjoint. Therefore

    ||theta'||²=(p-1)+2||delta||²
               >(p-1)+||delta||²=||theta||²,

since ||delta||²=2z>0. This is a positive INTEGER norm difference,
not a field-norm inequality or a modular calculation. An explicit
algebraic subtraction of N is harmless only because this actual
coefficient proof has been supplied.

## 4. Reconstruct OW3, endpoints and Fourier consequences

At each step use the CURRENT defect support and a newly chosen
h outside its ratio set. OW2 preserves all hypotheses, doubles
the current zero-count and leaves weight p-1 unchanged.
The integer function f(x)=2x(x-1)+2 is strictly increasing for
x>=1, since f(x+1)-f(x)=4x>0. Thus the stated inequality at the
largest input2^(r-1)z implies every earlier needed inequality.
Induction supplies exactly the claimed r+1 pairwise
nonconjugate free elements with zero-counts z,...,2^r z.
The statement does not assume that one fixed h works repeatedly.

The endpoint r1 is exactly OW2. Equality at the threshold does
not guarantee a complement to S/S and is correctly excluded.
No assertion is made for p3, z0 or a failed threshold. The
existence of disjoint supports itself bounds their size; there
is no use of an impossible repeated doubling after the hypothesis
fails. Small p5/p7 cause no division-by-zero or missing h issue
in the conditional OW1 statement; no satisfying starting element
is asserted merely because those primes are in its domain.

For Fourier evaluation E(theta)=sum n_a zeta^a, a vanishing
polynomial of degree<=p-1 with constant0 is a constant rational
multiple of Phi_p only if that multiple is zero. Irreducibility
follows from Eisenstein applied to Phi_p(X+1). Thus E is faithful
on all integer coefficient vectors and is G-equivariant.
A free theta gives p-1 distinct Fourier values. If values from
the two lists agreed, faithfulness would identify translates of
the original vectors, contradicting nonconjugacy. No reciprocal
map is involved and no Fourier injectivity is transferred to it.

## 5. Whole verdict and precise remaining obligations

OW1–OW3 are correct as scoped conditional algebraic statements.
Every original-weight construction, positivity argument, free
stabilizer test and conjugacy separation is present. The
18-row companion ledger records each inference and source scope.

The remaining universal starting hypotheses are NOT proved:
a suitable half-weight kernel u, or a weight-p-1 theta satisfying
the sparse0/1/2 regime and threshold. This report does not accept
my older FS2 by self-review, turn its candidates into such sparse
inputs, grant solution-specific Jacobi integrality/existence,
higher-jet rank, cancellation through every conjugate, nonzero
delta, a class-number strengthening, a height bound or an
unrestricted signed Diophantine exclusion.

Recommend acceptance only in the written OW scopes after the
other fresh whole audit and coordinator reconciliation. No old
candidate or review bytes were altered, and no novelty or complete
annual solution is claimed.

