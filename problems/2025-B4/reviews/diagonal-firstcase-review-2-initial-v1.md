# Initial independent whole audit R2: finite-range diagonal first case

2026-10-17 UTC. Reviewer /root/review_2022_complexity_r2 did not
construct this candidate. Requested gpt-6.1-sol/max; independent
effective-setting readback unavailable. This full report, per-claim
ledger and source checks are frozen before peer CF1 findings are read.

Target: complete coordinator-diagonal-firstcase-candidate-v1.md,
SHA-256 3a6c0bc793d7e5cf77d440fdb27b3ec139d3a5c61fe773b03310e9b8184a1a03;
complete freeze-v1.json,
59ad3e5d858d4b809195f55453f2af4c09ef519580eca5d5c448a1a0db3c3250.
The appendix-inspection note, earlier literature report and exact
accepted elementary dependencies were also read in their stated status.

**Finding:** CF1 reconstructs with its explicit attributed inputs.
I found no substantive objection or mathematical repair requirement.
The signed substitution, coprimality, relative-class-group rank
interface and exact finite-range contradiction are valid.
This does not newly prove the external class-number theorem or
rerun the published class-group calculation. It does not exclude
the two residual second-case residues, prove the unrestricted
diagonal classification, or establish novelty.
Only the coordinator decides acceptance after both independent audits.

## 1. Official domain and exact import boundary

The [official 2025 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2025_paper_b.pdf),
page2, B4(b), concerns integers x,y,n,q with n,q>=2.
In this packet the term count is m=n+1, and the restricted
diagonal equation is

    G_p(x)=(x^p-1)/(x-1)=y^p,
    p prime, 101<=p<2^31, |x|>=2.

Thus official n=p-1 and q=p. The symbol p in the literature
is neither official n nor an unrestricted composite exponent.
All restricted instances lie in the official open domain.
The preliminary part(a) is not solved or reproduced.

The accepted C1/C2/C4 register has SHA-256
c422139567ee3e2f4eafd852c9a3f5fac73cb6c8e0bfdf9e2c9c5311a9348b0d;
its accepted partial exposition and acceptance were read in this
sustained review session. Only C1 magnitude, C2 signed
odd-prime LTE and the elementary congruence G_p(x)=1 mod x
are needed here. The register's separate conjectural full
solution list is not a premise.

The [Mihailescu author upload](https://www.researchgate.net/publication/226863681_Class_Number_Conditions_for_the_Diagonal_Case_of_the_Equation_of_Nagell_and_Ljunggren)
identifies version2.0,17September2007 of the2008 chapter.
I read its Theorem1 and the beginning of Section3.
For coprime signed integers X,Y,Z satisfying
(X^p+Y^p)/(X+Y)=Z^p with p not dividing
XY(X^2-Y^2), that input gives r>sqrt(p)-1 for the
relative cyclotomic p-rank. Section3 explicitly discusses
Y=-1 and delegates the adapted proof to Eichler/Washington.
This is an attributed theorem import, not a new reconstruction
of those external proofs.

The [Hart--Harvey--Ong primary paper](https://arxiv.org/html/1605.02398v1),
Introduction items(1)--(3) and Table2, gives a full p-part
isomorphic to (Z/pZ)^(i_p) at the first cyclotomic level
for every odd prime p<2^31, and maximum i_p equal to nine.
The finite calculation is imported as published; it was
not rerun. The table's range is an exhaustive claimed range,
not a sampling assertion or a Poisson heuristic.

## 2. The residue-one branch is excluded by signed LTE

If x=1 mod p, then p|(x-1), p is odd and p does not divide x.
With |x|>=2 the factors x-1 and G_p(x) are nonzero.
The accepted odd-prime signed LTE identity applies with
term count p and gives

    v_p(G_p(x))=v_p(p)=1.

On the right, v_p(y^p)=p v_p(y). C1 gives |y|>1,
so y is a nonzero integer and this valuation is defined.
A nonnegative integer multiple of p cannot equal one.
This excludes the residue one without any class-group input,
and works unchanged when x is negative.

This branch must be removed separately: the imported first-case
condition includes the factor X^2-Y^2 and would not allow
the residue x=1. The candidate does not mistakenly apply it there.

## 3. Exact signed substitution and every coprimality hypothesis

Now suppose x is outside {-1,0,1} modulo p. Set

    X=x,      Y=-1,      Z=y.

Since p>=101 is odd, Y^p=-1, so

    (X^p+Y^p)/(X+Y)=(x^p-1)/(x-1)=G_p(x)=y^p.

The denominator x-1 is nonzero because |x|>=2.
There is no positivity assumption on X. Even for negative
x the substitution produces the same equation with signed
integer variables. C1 ensures |Z|>1; no trivial unit root
or zero value is introduced.

The variable Y=-1 is a unit, so it is coprime to both
X and Z. Also G_p(x)=1 mod x gives gcd(x,y)=1:
if a positive prime ell divided both, reducing the
geometric sum and y^p modulo ell would yield1=0.
Thus X,Y,Z are pairwise coprime. This is stronger than
any interpretation requiring only collective gcd one.

The theorem's excluded factor is exactly

    XY(X^2-Y^2)=-x(x^2-1)=-x(x-1)(x+1).

Over F_p a product is nonzero precisely when all its
factors are nonzero. The three excluded residues are
exactly those needed. In particular p does not divide
X, Y or X+Y; there is no hidden denominator reduction.
As an optional compatibility check, for x!=1 mod p,
Fermat's congruence gives G_p(x)=1 mod p and hence
y^p=y=1 mod p. Thus p does not divide Z either.
No additional obstruction is inferred from that congruence.

Every explicit hypothesis of the imported first-case
statement is therefore met. It yields the claimed
strict lower bound for r. The source's Section3
identifies t=Y/X=-1/x mod p; the restrictions on t
agree exactly with the three forbidden residues on x.
No cyclic permutation or positivity convention is
needed to force the substitution into the theorem.

## 4. Reconstructing the relative/minus p-primary interface

It is important that r be a group rank rather than a
logarithm of a class number or an Iwasawa invariant at
a different cyclotomic level. Write

    K=Q(zeta_p),     Kplus=its maximal real subfield,
    C=Cl(K)[p-infinity],     B=Cl(Kplus)[p-infinity].

Let c act on C by complex conjugation, j:B->C be
extension of ideal classes, and N:C->B the norm.
In additive notation the ideal identities give

    N j=2 on B,          j N=1+c on C.

These hold for fractional ideals and hence ideal classes,
including primes ramified in the quadratic extension:
extension of the norm is the product of the conjugate
ideals, and norm of extension squares the original ideal.

Since p is odd, multiplication by two is an automorphism
of each finite p-group. From N j=2, j is injective and
N is surjective. The endomorphisms

    eplus=(1+c)/2,       eminus=(1-c)/2

are well-defined, complementary idempotents on C.
They give C=Cplus direct-sum Cminus. Moreover

    ker N=Cminus,       j(B)=Cplus.

For the first identity, N(a)=0 implies (1+c)a=jN(a)=0,
so a is in Cminus. Conversely (1+c)a=0 implies
jN(a)=0 and injectivity of j gives N(a)=0.
For the second, j(B) is fixed by c; if ca=a, then
a=j(N(a)/2), using invertibility of two on B.

Consequently the relative group on p-primary parts
can be described either as the norm kernel or as
C/j(B), and both descriptions give Cminus.
Any usual two-primary distinction between full relative
class-group conventions is irrelevant for this odd p.
This reconstructs the minus/direct-summand claim used
in the candidate rather than relying on a class-number
ratio alone.

The p-rank of a finite abelian p-group is the number
of its cyclic p-primary factors, equivalently
dim_Fp(C/pC) or dim_Fp(C[p]). Under the imported
structure C=(Z/pZ)^(i_p), C is already a vector
space of dimension i_p. Its direct summand Cminus
is a subspace, so

    r<=i_p<=9.

Thus the upper bound uses the full p-part, not merely
the index of irregularity without a group-structure
bridge. Vandiver is unnecessary: it would additionally
annihilate B and make Cplus zero, but the inequality
above already suffices. No unrestricted conjecture
is used to identify these groups.

## 5. Exact threshold, finite calculation and contradiction

At p>=101, the exact integer inequality p>100=10^2
implies sqrt(p)>10 and therefore sqrt(p)-1>9.
Together the bounds are

    9>=r>sqrt(p)-1>9,

which is impossible. No floating-point estimate or
prime table is needed for this threshold.
The upper range is strictly p<2^31, exactly the range
covered by the imported finite calculation. Only its
first-level class group is used; the level variable
in the paper's general statement is not official n.

Table2's maximum is a reported actual computed maximum,
not a theoretical upper bound deduced from its comparison
with Poisson probabilities. The candidate correctly
imports the finite computation and does not turn
the statistical discussion into a proof.
Nothing here verifies fresh Bernoulli indices or
class groups, and no computational rerun was needed.

The residue-one branch and the first-case contradiction
exhaust all residues except zero and minus one.
Thus the candidate's necessary condition x=0 or -1
mod p is exactly what follows, conditional on the
stated published inputs.

## 6. Residual cases and source obligations kept separate

If x=0 mod p, the first-case factor -x(x^2-1)
vanishes. If x=-1 mod p it also vanishes. Thus
neither residue can be excluded by the imported
first-case theorem as used here. Both are correctly
retained. The simple congruence G_p(x)=1 mod p
in these cases supplies no contradiction to an
integer y^p; it only allows y=1 mod p.

The chapter's second-case theorem and its analytic
upper-bound/repair interface are explicitly not
premises. No implication from the first-case
class-rank inequality to either residual branch
is asserted. Likewise no parameterized binary-Thue
theorem is applied without its separate hypotheses.

I read the companion appendix-inspection note in
its actual status: a list of research and source
proof-reading obligations. It is not an accepted
objection or theorem refutation. This review does
not resolve its augmented matrix, cancellation or
repair questions; they are absent from the CF1
dependency chain. The earlier broad literature
report is a lead, not a proof of the stronger
second-case finite-range exclusion.

The candidate's finite-range first-case result
does not address p<101, p>=2^31, composite term
counts, off-diagonal exponents or the full signed
integer classification. Its failed priority search
does not establish that the corollary is new.
All these limits are stated accurately.

## 7. Whole-audit disposition and preservation

I checked the signed numerator and denominator,
pairwise gcd, nontrivial magnitude, all three
residue factors, source first-case definition,
ordinary relative/minus p-group conventions,
norm/extension compositions, invertibility of
two, p-rank versus class number and Iwasawa level,
exhaustive finite range versus heuristic,
the exact101 threshold, unused Vandiver and
both residual second-case residues.
No counterexample or substantive gap was found.

The result remains an attributed consequence:
the external theorem proof and the finite
published computation have not been newly
reconstructed. No full solution, source-theorem
refutation, novelty or promotion is claimed.

Only assigned diagonal-firstcase-review-2-*
review records were created. No mathematical
program, enumeration, CAS or new prime/class-group
table ran. No candidate/shared edits, Git,
spawning, charge, outside contact or separately
billed API occurred. Frozen target rows and all
earlier own records are separately fingerprinted.
No peer CF1 findings were read before initial freeze.

Latest authoritative weekly total use at the start
of this audit was26% at2026-10-17 06:35:13UTC,
window10080minutes, reset1792745187. The90%
total ceiling and integration/review reserve apply.
