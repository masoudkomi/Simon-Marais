# CF1: initially blind whole review R1

2026-10-17 UTC. Reviewer `review_2021_reasoning_j15_r2`.
Requested gpt-6.1-sol/max; effective-setting readback unavailable.
I did not construct or contribute to CF1. This complete report, ledger,
source checks and manifest were frozen before reading any peer CF1
report or findings. This is a review recommendation, not promotion.

I find no substantive defect in CF1 as an explicitly attributed finite-range
corollary of the two stated published inputs. I reconstructed every local
inference and freshly inspected the primary source theorem, its Section3
explanation, and HHO's Introduction/Table2. I do not claim to reconstruct
Mihailescu's entire proof, its Eichler/Washington imports, or HHO's large
published computation. No theorem from the separate second-case/appendix/
binary-Thue material is used or accepted by this review.

## Exact target and domain

The whole target is `notes/coordinator-diagonal-firstcase-candidate-v1.md`,
SHA-256 `3a6c0bc793d7e5cf77d440fdb27b3ec139d3a5c61fe773b03310e9b8184a1a03`.
Its freeze manifest has SHA-256
`59ad3e5d858d4b809195f55453f2af4c09ef519580eca5d5c448a1a0db3c3250`.
The constructor-listed files are integrity-checked, including unused
appendix/cache material whose bytes are not mathematical premises here.

The equation is G_p(x)=y^p with integer x,y, odd prime
101<=p<2^31 and |x|>=2. The term count m is p; the OFFICIAL degree
is n=p-1. This is a restricted diagonal portion of B4(b), not the
official preliminary part (a). C1/C2 are taken from the already accepted
frozen elementary proof/register. Their used signed LTE interface was
also independently checked below. The integer boundary values x=0,±1
are outside this packet; residue classes 0,±1 modulo p are different.

## Elementary valuation and coprimality checks

If x=1 modulo p, then p is odd, p|(x-1), p does not divide x,
the term-count exponent p is positive, and x^p-1 and x-1 are nonzero.
The accepted signed odd-prime LTE yields

    v_p(G_p(x))=v_p(p)=1.

But y is nonzero because G_p(x) is nonzero for |x|>=2, so
v_p(y^p)=p v_p(y) cannot be 1. This excludes residue 1, including
negative integer x in that residue. Negative signs do not change an
integer valuation. This step uses no class-group theorem.

For the remaining first-case residues, set X=x,Y=-1,Z=y. Since p is
odd, Y^p=-1 and X+Y=x-1, so the generalized source quotient is exactly

    (X^p+Y^p)/(X+Y)=(x^p-1)/(x-1)=G_p(x)=Z^p.

The sign Y=-1 is essential to this identity and is correct. Its denominator
does not vanish under |x|>=2. The two pairs involving Y are automatically
coprime. If a prime divided both X=x and Z=y, reducing G_p(x)=y^p
modulo that prime would give 1=0. Thus gcd(x,y)=1 and the three source
integers are pairwise coprime, which is at least the source's coprimality
requirement. No positivity of X or any replacement of x by |x| was used.

Finally,

    XY(X^2-Y^2)=-x(x^2-1).

In F_p this is nonzero precisely when x avoids 0,1,-1. Those are exactly
the residues excluded before applying the source first-case theorem.
No additional residue condition on Z is asserted without derivation.

## Complete first imported theorem interface

I directly opened Mihailescu's author-uploaded full chapter, version2.0
dated17 September2007, and read the full Theorem1 statement on printed
page2, the definitions around it and the complete relevant Section3
explanation on printed page12. Its source uses coprime INTEGERS, with
the generalized quotient and nonzero residue product just checked,
and concludes that the relative cyclotomic p-class rank r exceeds
sqrt(p)-1. Section3 expressly uses the substitution of its second
variable by -1 and explains the first-case ratio restriction. There is
no unmentioned positive-base hypothesis. The chapter attributes its
proof to the relevant Eichler/Washington argument; I checked the theorem
interface, not a full reconstruction of those external proofs.
[Primary author upload](https://www.researchgate.net/publication/226863681_Class_Number_Conditions_for_the_Diagonal_Case_of_the_Equation_of_Nagell_and_Ljunggren).

Thus every source hypothesis is matched by the above signed substitution,
and for a putative first-case solution it yields r>sqrt(p)-1.
The first-case theorem and its Section3 explanation do not use the
chapter's later upper-bound/second-case conclusion in this application.

## Relative/minus rank versus the entire p-primary class group

Let L=Q(zeta_p), K=L^+ and C_L,C_K be their finite p-primary ideal class
groups. Let c be complex conjugation, j the extension map and N the ideal
norm. In additive notation the ordinary ideal identities give

    N j=2 on C_K,        j N=1+c on C_L.

Because p is odd, multiplication by2 is an automorphism on both groups.
Consequently j is injective and N is surjective on these p-primary
groups. The endomorphisms e_+=(1+c)/2,e_-=(1-c)/2 are well-defined:
division by2 means the unique half in the finite p-group. They are
complementary idempotents, not an unsupported rational scalar action.

The image of j is exactly C_L^+. It is contained there because ideals
extended from K are conjugation-fixed; conversely for a plus class a,
jN(a)=2a, so a is in im(j). The kernel of N is exactly C_L^-: if N(a)=0,
(1+c)a=0; if c a=-a, then 2N(a)=N(a)+N(ca)=0, whence N(a)=0.
Thus the relative p-primary group, whether represented by this norm
kernel or by the quotient by the extended real part, is isomorphic
to the minus direct summand.

In particular its p-rank cannot exceed the rank of the full C_L.
This comparison does not assume that an arbitrary relative class
number is a rank, that all class groups are elementary abelian, or
that a capitulation kernel has harmless order without proof. The
degree-two norm/extension identities and odd p supply the splitting.

## Complete finite-computation input and the rank contradiction

I freshly read HHO's full Introduction items(1)–(3) and complete Table2
in the primary arXiv v1 text. The stated computation covers EVERY odd
prime p<2^31. In particular item(3) reports class-group structure
(Z/p^n Z)^(i_p) for Q(zeta_(p^n)), n>=1, following the stated computed
invariants. At n=1 this is precisely the entire p-primary C_L needed
here. Table2 is presented as the exact distribution over the complete
range and has categories 0 through9, with a single prime of index9.
Thus its reported maximum is i_p<=9. This bound is read from the
finite calculation, not the adjacent Poisson heuristic.
[Primary HHO text](https://arxiv.org/html/1605.02398v1).

These are explicitly imported published computational results; the
underlying many-prime calculation and its certificates were not rerun
or independently certified here. Taking that stated input gives

    rank_p C_L=i_p<=9,       r<=i_p<=9.

HHO also reports Vandiver in the same finite range, but equality of
the whole p-primary group with its minus part is unnecessary. The
inequality already proved suffices, so no unrestricted Vandiver
conjecture or second-case theorem is substituted.

For p>=101, p>100 implies sqrt(p)>10 and sqrt(p)-1>9. Therefore the
source lower bound r>sqrt(p)-1 contradicts r<=9. This excludes every
residue outside {0,1,-1}. Together with the independent LTE exclusion
of 1, any actual solution in this exact range must have x=0 or -1
modulo p. This proves precisely CF1 with its stated attributed inputs.

## Boundary, source and disposition limits

Residues 0 and -1 remain unresolved by this proof because the imported
first-case nonzero-product hypothesis fails there. These are residue
classes, not excluded integer boundary points. No application of the
chapter's Theorem4, its later upper bounds, any singular-system repair,
the companion appendix note or the binary-Thue theorem is made. Those
files are not needed for the proof and their presence in an integrity
manifest does not promote them.

No statement for smaller primes, primes at or beyond2^31, composite term
counts, different power exponents, the full signed Nagell–Ljunggren
classification or priority follows. The m=n_official+1 translation is
retained throughout. No preliminary part (a) argument was investigated.

No substantive issue or author repair is requested. I recommend acceptance
of CF1 as this explicitly attributed finite-range first-case corollary
after the other fresh audit and coordinator reconciliation. This report
does not independently prove the imported arithmetic theorem or published
finite computation and does not promote a full solution.

No mathematical program, numerical check, prime enumeration or CAS was
run. Only this assigned review prefix was written. The freeze validates
all eight constructor records and all 27 earlier own frozen packets.
Latest account-wide weekly total used is27%, reset1792745187, with the
90%-total cutoff and integration reserve. Requested and effective
settings remain separately recorded.
