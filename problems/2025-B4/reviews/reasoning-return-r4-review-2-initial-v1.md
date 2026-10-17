# Independent whole FS1--FS3 audit R2

2026-10-17 UTC. **Initial independent nonconstructor WHOLE audit,
frozen before peer findings.** Reviewer
`/root/review_2021_reasoning_j15_r2`; requested gpt-6.1-sol/max,
verified effective-setting readback unavailable. The constructor is
`/root/review_2017_coarsening_r1`. The root's FS R1 report, later root
inspection and NEW original-weight packet were not read. No substantive
finding was sent before this complete report/ledger/source/integrity
freeze. No candidate, source, shared, historical or Git file was edited.

**Disposition:** no substantive mathematical objection to FS1--FS3 in
their exact algebraic scopes. I recommend scoped acceptance only after
the coordinator reconciles BOTH complete whole audits. FS2 is an
attributed alternative proof of the already stated one-element selection
result. FS3's extra weight does not solve the original-weight selection
or any Diophantine application. No source-proof repair or full annual
result is recommended or claimed.

I reconstructed the entire main argument, all40 constructor obligations,
the complete source audit/worklog/self-check and declared submission.
The companion ledger records50 separate inference/adversarial checks.
Only byte hashes, JSON and old-file preservation use executable code.
No mathematical program, CAS, prime scan, sample, author-code rerun or
certificate replay was used.

## 1. Domain, definitions and independence

The [official B4(b)](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2025_paper_b.pdf),
page2, has integers x,y and n,q>=2. Its degree n becomes term count
m=n+1. The algebraic prime p, Fueter index t and multiplicity k in FS3
are separate parameters. The statements concern cyclotomic group-ring
elements for every written prime and k, without assuming a Diophantine
solution. No part(a) proof is researched.

I previously reviewed the OLD PG and CF1 packets and other years'
results, and authored the unrelated2021 return constructions. I neither
constructed nor supplied a strategy or repair for NEW FS1--FS3. Those old
roles do not make me an independent auditor of my own old constructions;
they are not mathematical premises here. Accepted MS1--MS5 were read
completely, and their used interfaces are rederived below rather than
replaced by an acceptance label.

The explicit definitions are sufficient. G=F_p^*, sigma_a(zeta)=zeta^a,
Z[G] is free over Z on this basis, N is its all-ones vector, and j is
sigma_-1. In DIRECT indices F(theta)=sum n_a a, whereas
M_r(theta)=sum n_a a^(-r). Thus F encodes multiplicative action on zeta;
the Fourier map E(theta)=sum n_a zeta^a is a different additive map.
Left multiplication by sigma_h changes direct index a to ha, giving

    F(sigma_h theta)=h F(theta),
    M_r(sigma_h theta)=h^(-r) M_r(theta).

Consequently M_1 nonzero is a sufficient exact freeness test. Its
vanishing is not a converse. Positivity means nonnegative coefficients,
including zero, as in the primary definitions.

## 2. Module membership, coefficient orientation and moments

With vartheta=(1/p)sum c sigma_c^-1, the coefficient of sigma_c^-1
in sigma_a vartheta is r_a(c)/p, where r_a(c) is the canonical nonzero
residue of ac. This follows by solving a/b=c^-1 for the old index b.
It gives Theta_a=(a-sigma_a)vartheta with coefficient floor(ac/p).
The formula is asserted only for positive a prime to p; no undefined
sigma_0 or source endpoint a=p is used. Subtraction gives
psi_t=(1+sigma_t-sigma_(t+1))vartheta. These integral elements belong
to the explicitly defined intersection I. Multiplication by G preserves I.

For 1<=t<=p-2, both t,t+1 are nonzero. The consecutive floors differ
by0 or1 because 0<c/p<1. The floors at p-c give
nu_c+nu_(p-c)=1, so psi_t+j psi_t=N and its augmentation is(p-1)/2.
This also proves N in I without any basis theorem. N has both F=0 and
M_1=0. Positive sums and G-translates preserve all required memberships;
ker F is G-stable by the direct transformation rule.

I independently reconstructed both power-sum calculations. In
sum(ac-pu_c)^2=sum c^2, reduction modulo p^2 and division by p give

    2a sum c u_c=(a^2-1)/6 mod p,
    M_1(Theta_a)=(a-a^-1)/12.

Here sum c^2/p=(p-1)(2p-1)/6 is integral and congruent to1/6 for
p>=5. Since the coefficients use sigma_c^-1, their DIRECT inverse
index is c, which proves that this is M_1, not F.

Likewise sum c^4/p=(p-1)(2p-1)(3p^2-3p-1)/30 is integral and
congruent to-1/30 for p>=7. All higher terms in the fourth-power
expansion contain p^2. Thus

    4a^3 sum c^3 u_c=(a^4-1)(-1/30),
    M_3(Theta_a)=-(a-a^-3)/120.

The denominators6,12 are units at p>=5;30,120 are units at p>=7.
The exact integer identities are divided before reduction. Subtracting
the a=t and t+1 values gives precisely

    M_1(psi_t)=Q(t)/(12t(t+1)), Q(t)=t^2+t+1,
    M_3(psi_t)=-(1+t^-3-(t+1)^-3)/120.

No coefficient or power-sum table is used as evidence.

## 3. Complete FS1 reconstruction and small-prime checks

Off Q(t)=0 the nonzero M_1 formula forces h=1 for a stabilizer element.
On Q(t)=0 and p>=5, t^3=1 and t!=1, hence order(t)=3 and p>=7.
Moreover t+1=-t^2. The integer coefficient identity becomes

    p nu_c=c+r_t(c)+r_(t^2)(c)-p.

Replacing c by r_t(c) cycles these three canonical residues and leaves
the integer sum unchanged. In the INVERSE basis, the coefficient at
sigma_c^-1 of sigma_t psi_t is nu_(r_t(c)), not nu_(r_(t^-1)(c)).
The formula therefore proves literal invariance under sigma_t.

At the same parameter M_3=-1/40 is nonzero. The transformation law
forces every stabilizer element h to satisfy h^3=1. There are at most
three such elements in F_p, and {1,t,t^2} are already in the stabilizer.
Thus that is its EXACT stabilizer. Its invariance and F(sigma_t psi)=tF(psi)
also force F=0; M_1=0 follows separately from Q(t)=0. Moment zero was
not used to infer invariance.

For p=5 there is no order3 subgroup, so the exceptional case cannot
occur and the M_3 formula is never invoked. At p=3 the allowed t=1
gives psi_1=sigma_2, which is free, despite Q(1)=0. Excluding this
prime is necessary. As a hand adversarial check, at p=7,t=2 the direct
support is{3,5,6}, permuted by multiplication by2; its cubic inverse
moment is4=-1/40 mod7. This checks the exceptional case without a scan
or extrapolation. The FS1 proof itself covers every stated prime.

## 4. Complete FS2 reconstruction

First reconstruct F, independently of M_1. The residues r_c=ac-pu_c
permute1,...,p-1. Expanding their PRODUCT modulo p^2 in Z_(p) and
canceling the unit factorial yields

    1=a^(p-1)[1-(p/a)sum u_c/c] mod p^2.

Writing a^(p-1)=1+p q_p(a), dividing the resulting congruence by p
and reducing gives F(Theta_a)=sum u_c/c=a q_p(a). Thus

    f(t)=F(psi_t)=((t+1)^p-t^p-1)/p mod p.

The numerator defines an integer polynomial quotient. Its reduction
has degree p-1 and zeros at0,-1. For j=1,...,5 its coefficient at
X^(p-j) is(-1)^(j-1)/j. These are coefficients of a genuine polynomial;
X^p=X has not been imposed inside the polynomial ring.

If u(t)=f(t)Q(t)/(12t(t+1)) were constant C on the domain deleting
0,-1 and Q-roots, then

    P(X)=Q(X)^2 f(X)-12C X(X+1)Q(X)

would vanish at EVERY field element. The deleted Q-roots are handled
by the outer factor; at0,-1 both terms vanish. Hence X^p-X divides P.
Its degree is p+3, so the quotient has degree3. The high part of such
a product has degrees at least p and the low part degrees at most4.
For p>7, p-1>4, and its coefficient at p-1 is therefore0. Direct
coefficient extraction instead gives

    1-1+1-1/2+1/5=7/10 !=0 in F_p.

The C term has degree4 and cannot contribute. This proves nonconstancy
for EVERY p>7, not merely the existence of examples. Its domain is
nonempty and has two distinct u-values as a consequence of the
contradiction; the claim also handles primes with no Q-root.

Choose s,t with different u-values. Their inverse moments are nonzero.
If one F value is0, twice that Fueter element has F=0, nonzero M_1,
weight p-1 and complement2N. Both F values cannot be0. Otherwise use

    theta=sigma_(f(t)) psi_s+sigma_(-f(s)) psi_t.

Both indices are nonzero; the negative index changes the permutation,
not the sign of an integer coefficient. F cancels and

    M_1(theta)=[f(s)M_1(psi_s)-f(t)M_1(psi_t)]/[f(s)f(t)] !=0.

Membership, positivity, weight, theta+j theta=2N and exact freeness
follow from the previously reconstructed identities. No zero F value
is divided by. p7 is excluded precisely where7/10 vanishes; no
nonexistence claim there is inferred.

The already stated one-element selection is correctly attributed to
[Bartolome--Mihailescu, Lemma2.7](https://arxiv.org/pdf/1412.5798v2).
I checked the actual two-moment statement and Appendix5.2's product
route. The candidate supplies its own restricted-prime proof and does
not import that appendix, its small-prime wording or a Diophantine theorem.

## 5. Complete FS3 reconstruction, including arbitrary integer k

FS2 gives integral coefficients n_a in{0,1,2} with n_a+n_-a=2.
They cannot all be1 since M_1(theta)!=0. They therefore have a zero
and a2. If exactly one zero occurred at v, the only2 would be at-v,
and theta=N-sigma_v+sigma_-v would have F=-2v!=0. Thus there are two
distinct zeros v,w. They cannot be opposite because of the complement
identity. Their DIRECT ratio h=v/w differs from1 and-1.

At direct index v, the coefficient of sigma_h theta is n_(h^-1 v)=n_w,
so gamma=theta+sigma_h theta has an ACTUAL common zero. Its complement
is4N, forcing a coefficient4 at-v and extrema0,4. Also
M_1(gamma)=(1+h^-1)M_1(theta)!=0. It is positive in I_f and free.

For k>=2 the displayed A_l=(k-l)theta+lN,0<=l<=k-1, and
B=gamma+(k-2)N are all positive in I_f with the SAME augmentation
k(p-1); they also have complement2kN. Freeness of A_l is an integer
statement: if sigma_g fixes it, multiplication by the nonzero INTEGER
k-l annihilates sigma_g theta-theta in the free abelian group Z[G],
so that difference is0. It remains valid when p divides k-l. B has
the stabilizer of gamma, since its added norm vector is invariant.

A_l has minimum l and maximum2k-l, so its k orbits are distinct.
B has minimum k-2; only A_(k-2) could share its orbit. Here the
integer coefficient Euclidean norm is G-invariant and

    ||gamma||^2=4||theta||^2-||theta-sigma_h theta||^2
               <||2theta||^2.

The strict term is positive because h!=1 and theta is free. Adding
(k-2)N preserves this strict inequality: gamma and2theta have the
same augmentation, so the cross terms of that addition are equal.
It separates B from A_(k-2), proving k+1 pairwise nonconjugate free
elements for every integer k>=2. No reduced-moment nonvanishing is
silently imposed on all A_l.

For E(theta)=sum n_a zeta^a, a kernel polynomial has constant0 and
degree at most p-1. Divisibility by the degree-p-1 cyclotomic polynomial,
whose constant is1, makes that kernel polynomial0. Hence E is
injective. Direct-index multiplication proves equivariance. Stabilizers
therefore coincide, and a cross-orbit equality of Fourier values would
give a conjugacy of the group-ring elements. This proves the full
p-1 entries within each of the k+1 DISJOINT lists.

This Fourier fact does not extend to the reciprocal map. For example,
opposite-index reciprocal terms sum to a value independent of the pair,
so differences of such pairs give a kernel. No such transfer occurs in FS3.

## 6. Application, weight and scope audit

I checked the actual original chapter definitions and full Lemma3,
then the Section4.3 second-case selection passage. Its weight is the
ordinary augmentation p-1. The later paper's relative weight2 means
that SAME augmentation; it is not an extra factor of p-1. FS2 has
this weight but supplies only one proven free orbit. FS3 has weight
k(p-1), k>=2, and cannot replace two original-weight elements without
new estimates. At k1 its extra candidate gamma-N has coefficient-1
at the common zero, so this attempted specialization fails exactly.

The candidate's size warning is correct under its explicit conditional
hypotheses. If beta^p=(x-zeta)^eta, eta+j eta=2kN, G_p(x)=y^p and
y>0, then

    |beta|^(2p)=(x-zeta)^(eta+j eta)
               =G_p(x)^(2k)=y^(2kp),

so |beta|=y^k. No existence or integrality of such beta is asserted by
FS3. Likewise distinct first Fourier coefficients do not prove all
higher coefficients form one common Vandermonde system, simultaneous
interpolation, integral cofactors, every-conjugate cancellation or a
nonzero delta. The source's original and later maps and thresholds
remain distinct. The candidate explicitly withholds all these steps.

The printed original Lemma7 already states the p-squared residue
refinement; the candidate attributes it and makes no new exclusion.
C/PG/CF1/MS and the narrow StrongFC source-objection scopes remain
unchanged. No all-prime Vandiver, extra class-number theorem or signed
Diophantine range is imported.

Thus the remaining problem is stated accurately: two suitable free
orbits at the original weight, or a complete larger-weight application,
has not been supplied by FS. Either would still need the other actual
source hypotheses and proof interfaces. No full external proof is
accepted or refuted by this audit. Source identity/read limits and all
integrity results are in the companion records. Promotion belongs only
to the coordinator after both complete reports are reconciled.
