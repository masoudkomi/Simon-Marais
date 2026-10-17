# Fresh initially blind whole audit R1: GK1–GK3

2026-10-17 UTC. Reviewer `review_2021_reasoning_j15_r2`. Requested
gpt-6.1-sol/max; no verified effective-setting readback is available.
This is an independent whole review of coordinator root's frozen
generalized Kasami packet. It is not a promotion or an author repair.

**Recommendation:** no substantive defect found in the complete scoped
GK1–GK3 argument. The recurrence gives the claimed all-index sufficient
whole-divisor families over F2, with the endpoint and phi13 qualifications
stated. A second fresh whole audit and coordinator reconciliation remain
required. No full official classification or novelty follows.

Main candidate:10290 bytes, SHA256
`f99bae5f5d3877e556a30347a38616daf6b54fde300ae60543f849893a7dc4b8`.
Six-record constructor manifest:2042 bytes, SHA256
`50c3269d28a49327e28e216a857fdb711dae8875cab127645bc4081f2ac9ec65`.
I read the full candidate, source record, worklog,16 obligations and
administrative freeze source, plus the full accepted CP body and exact
phi13 body/acceptance scopes. Input hashes and all older own packets
are preserved in the accompanying freeze.

## Independence and actual premises

I did not construct or contribute the new auxiliary-root construction,
pairing argument, vector relation, recurrence, all-index degree proof
or GK applications. I authored older T1–T4 and C7/C11 context, and was
fresh whole reviewer R2 of the previously accepted CP1–CP3 packet.
That history is disclosed rather than counted as fresh review of my
own older constructions. Old T1–T4/C7/C11 do not supply any GK premise.
The exact accepted CP1 theorem is a stated logical premise; CP2 is
only a consistency comparison. My separately frozen2019 construction
and2017 strict local construction are unrelated to this proof.

I remained blind to peer GK findings and any later root inspection
through completion of this initial report, ledger, source checks and
freeze. No substantive finding was disclosed before the full freeze.
I did not read the future all-D global candidate. No mathematical code,
CAS, certificate rerun or exponent scan was used. Python was used only
for administrative metadata and freezing. Only the assigned review
prefix was written; all candidate/shared/older bytes remain unchanged.

## 1. Official domain and integer indices

I freshly reopened [official2024 Paper B,p.2 B4(b)](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf).
The target is positive odd n and a coefficientwise congruence of
integer polynomials with both extra factors nonconstant modulo2.
Positive-degree F2 factors lift by choosing integer coefficients0/1.
The argument does not use equality of functions on a finite field.
Existing quotient existence and the excluded n1/n3 boundaries are
accepted background; no preliminary-part solution is reconstructed.

For q=2^k,k>=1 and r>=0, the integer identity

    (q+1)L_r=q^(2r+1)+1

holds because the alternating integer sum q^(2r)-q^(2r-1)+...-q+1
multiplies by q+1 to give the numerator. The sum is positive and odd:
q is even, all its positive powers are even, and its constant is1.
At r0 it is1; at r1 it is d=q^2-q+1>=3. For r>=1 the exponent is in
the domain of CP1. L_r is strictly increasing in r for each fixed q,
so r>=2 implies L_r>d. The auxiliary g_1=1 satisfies
a+(a+1)=1 and is used only to initialize the recurrence, not to extend
CP1 to n1. The notation m=r-1 in the sufficient family is consistent.

## 2. Auxiliary roots and root-choice independence

Let a be transcendental over F2, b=a+1, and work in an algebraic
closure of F2(a). Roots A^(q+1)=a and B^(q+1)=b exist by the definition
of algebraic closure; both are nonzero as a,b are nonzero field
elements. No algebraic independence of A,B is assumed. They obey
A^(q+1)+B^(q+1)=1.

For v=(A,B) define v^[j]=(A^(q^j),B^(q^j)). The dot product is the
ordinary bilinear one, with no positivity, conjugation or finite-field
Hermitian assumption. Its q-power is compatible with coordinatewise
Frobenius because characteristic is2 and q is a power of2. In
particular q^2-Frobenius is not declared the identity on this field.

For D_r=v dot v^[2r+1], integer divisibility gives

    D_r=A^((q+1)L_r)+B^((q+1)L_r)
       =a^L_r+b^L_r=g_(L_r)(a^2+a).

This proves root-choice independence of EVERY D_r directly. Although
the two individual coordinates lie in an algebraic extension, the
desired scalars lie in F2[a]. D_0=1 and D_1=c=g_d(a^2+a). The
accepted degree deg g_d=(d-1)/2>=1 makes c nonconstant of degree d-1
in a. Therefore c+1 is nonzero in the function field. This includes
q2,d3, for which c=a^2+a+1 and c+1=a^2+a is nonzero at transcendental
a. The excluded q1 would fail this setup, but is outside k>=1.

## 3. All six pairings and the full vector relation

I independently computed the relevant exponent sums. From
A^(q+1)+B^(q+1)=1 and c=A^(q^3+1)+B^(q^3+1), one gets

    v dot v^[1]       =1;
    v^[2] dot v^[1]   =1^q=1;
    v dot v^[3]       =c;
    v^[2] dot v^[3]   =1^(q^2)=1;
    v^[4] dot v^[1]   =c^q;
    v^[4] dot v^[3]   =1^(q^3)=1.

For example q^4+q=q(q^3+1) gives the penultimate equality; the last
uses q^4+q^3=q^3(q+1). Every pairing follows from an explicit
Frobenius power of a displayed identity, not from periodicity.

The two functionals dot v^[1], dot v^[3] evaluated on the ordered
columns v^[2],v give

    [1 1; 1 c],  determinant c+1 !=0.

Over a field, invertibility of this pairing matrix implies both that
the two columns are a basis and that the two functionals are
independent. Thus a coefficient solution of the two scalar equations
does determine a full vector identity; it is not merely a necessary
projection onto a one-dimensional image.

Write v^[4]=alpha v^[2]+beta v. The last two pairings give exactly

    alpha+beta=c^q,  alpha+c beta=1.

Adding them yields (c+1)beta=c^q+1=(c+1)^q. Division by the nonzero
field element c+1 gives

    beta=(c+1)^(q-1),
    alpha=c^q+(c+1)^(q-1).

These coefficients are actual polynomials in c over F2. Their equality
to the field coefficients was established where division is valid;
the denominator has disappeared. Matrix invertibility verifies the
full vector relation with these polynomials. No uninspected
factorization, monodromy or group-order theorem enters this step.

## 4. Frobenius propagation and polynomial descent for every r

Raise the complete vector relation to q^(2r+1), for arbitrary integer
r>=0. It becomes

    v^[2r+5]=alpha^(q^(2r+1)) v^[2r+3]
                    +beta^(q^(2r+1)) v^[2r+1].

The index shifts are addition of Frobenius iteration indices, so4
becomes2r+5 and2 becomes2r+3. Now take the dot product with the
ORIGINAL unraised v. The three pairings are exactly D_(r+2),
D_(r+1),D_r, respectively. Raising that other v as well would change
the statement; the actual proof correctly does not do so.

With alpha=A_q(c),beta=B_q(c), the scalars therefore obey the stated
P recurrence. Initial values1,c and ordinary induction give
D_r=P_r(c) for ALL r>=0. Each P_r belongs to F2[T], since the
recurrence starts there and uses only polynomial powers and sums.

We have proved equality of
g_(L_r)(a^2+a) and P_r(g_d(a^2+a)) in the algebraic closure. Both
expressions are polynomials in a, so this is already an equality in
F2[a], not merely of rational functions with unequal domains. Since
a is transcendental, it is a polynomial identity. The injection
F2[U] into F2[a], U->a^2+a, follows by doubled leading degree.
Consequently it descends to the actual identity

    g_(L_r)(U)=P_r(g_d(U)) in F2[U]

for every r. This is the full GK1 claim.

No finite specialization is used to prove it. In particular zeros of
c+1 are allowed in the final polynomial statement, even though the
auxiliary basis calculation there would be singular. For example its
polynomial coefficients specialize at c1 to A_q(1)=1,B_q(1)=0, so
there is no remaining denominator. A singular auxiliary matrix at a
finite point does not invalidate a polynomial identity already
proved at the transcendental parameter.

## 5. All-index monicity, degrees and r2 comparison

A_q(T) is monic of degree q: the other summand has degree q-1.
B_q(T) is monic of degree q-1. E_0=0,E_1=1 agree with P_0=1,P_1=T.
Assuming the two preceding degrees, the first recurrence summand has
degree q*q^(2r+1)+E_(r+1)=q^(2r+2)+E_(r+1)=E_(r+2).
The other has degree (q-1)q^(2r+1)+E_r. Their difference is

    q^(2r+2)-(q-1)q^(2r+1)+(E_(r+1)-E_r)
       =q^(2r+1)+q^(2r)=q^(2r)(q+1)>0.

Thus the higher leading monomial cannot cancel in characteristic2;
P_(r+2) remains monic of degree E_(r+2). This proves the assertion
at every index, not by extrapolation from a finite pattern. Also

    (L_r-1)/(d-1)
      =[q(q^(2r)-1)/(q+1)]/[q(q-1)]
      =(q^(2r)-1)/(q^2-1)=E_r,

matching the necessary composition degree for r>=1.

At recurrence index r0 one obtains

    P_2=T^(q^2+1)+(T+1)^(q(q-1))T+(T+1)^(q(q-1))
       =T^(q^2+1)+(T+1)^(q^2-q+1).

This agrees with accepted CP2 by direct algebra. CP2 is not used to
infer the vector relation or the induction. No q8 check, n233017
calculation or author certificate is a premise or was rerun.

## 6. Whole homogeneous factors and official integer lifts

The accepted CP1 theorem is an iff for ALL odd d,n>=3 over the
actual polynomial rings. I read its entire accepted body, including
full-degree homogenization, rank-four free-module contraction and
monic h-adic difference quotient argument. It retains repeated
diagonal factors and unit endpoints. The accepted copy is an exact
byte suffix copy of the frozen CP candidate after its scope header.

GK1 supplies an F2 polynomial composition with the fixed g_d. For
r>=1, d>=3 and L_r>=d are odd, so every CP1 hypothesis holds and its
conclusion is the WHOLE homogeneous phi_d dividing phi_(L_r) over
F2[X,Y,Z]. There is no descent from one absolute factor and no
unmentioned localization. The full cofactor exists over F2.

For q>=4 and r>=2 its divisor degree is q^2-q-2>0, and its cofactor
degree is L_r-d>0. Both are nonzero by the accepted nonzero degree
theorem for odd n>=3. Coefficientwise0/1 integer lifts of these actual
F2 polynomials therefore give precisely the official congruence and
nonconstant residues. Irreducibility of either factor is unnecessary
and unclaimed.

For each fixed k>=2, strict increase of L_r gives an infinite family
as r>=2 varies, with the same whole divisor and growing cofactor.
With m=r-1, its exponent is (q^(2m+3)+1)/(q+1), m>=1. For q8,m1
this is32769/9=3641, and m2 gives2097153/9=233017. These integer
identities are hand substitutions, not finite evidence for the
unrestricted theorem.

## 7. Exact phi13 necessity and all endpoint cases

For r>=1, (q^(2r)-1)/(q+1) is an odd integer: q=-1 modulo q+1 and
the exponent is even; numerator and denominator are odd. Therefore

    L_r-1=q*(q^(2r)-1)/(q+1),  v2(L_r-1)=k.

The accepted exact phi13 criterion concerns all odd n>=3 and says
precisely n=(64*16^j+1)/5,j>=0. Every such exponent has
n-1=4*(16^(j+1)-1)/5, with odd integer quotient, hence valuation2.
Thus for k>=3 and every r>=1, L_r is not in the accepted iff
progression, and its WHOLE phi13 divisor is absent. This uses exact
necessity; merely knowing a sufficient old progression would not
justify it. It excludes only that whole divisor and says nothing
about any one of its absolute components.

At q4,

    L_r=(4*16^r+1)/5=(64*16^(r-1)+1)/5,

so the qualifying r>=2 range is exactly the already accepted
progression with index m=r-1>=1. Its known205 endpoint and published
context retain attribution; no new necessity or priority is asserted.

At q2 the divisor is phi3=1, even for r>=2; no genuine official
factorization follows from that unit. At r1, L_1=d and P_1=T, so
the divisibility is equality with a unit cofactor for every q. At
r0, L_0=1 and g_1=1 are auxiliary only, outside CP1; no valuation
claim or official factorization is made there. The ordinary n1 zero
and n3 unit exclusions are retained. Thus the domains and boundaries
match across all three GK claims.

## 8. Adversarial conclusion and source limitations

I tested the logical failure modes of treating the pairing as a
Hermitian form, imposing q^2=id, changing both vectors during the
Frobenius propagation, passing from two scalar equations to a vector
without independent functionals, overlooking a denominator at finite
zeros, canceling equal leading degrees, applying CP1 at n1, and
using a merely sufficient phi13 progression. The explicit arguments
above resolve each within the actual domains. I found no counterexample
or remaining substantive gap in the frozen proof.

The source note separates MCM/Dickson inspiration from theorem
premises. No proof of an external splitting-field, factor-field,
monodromy, Janwa–Wilson or APN theorem is reconstructed or imported.
The new argument is elementary algebra; its accepted dependencies
are CP1/degree and the phi13 iff only for GK3. Actual reading and
raw-byte preservation are distinguished in the source record.

There is no full exponent classification, necessity for arbitrary q,
general individual-factor assertion, irreducibility consequence from
a failed whole-divisor test, or novelty. The per-inference ledger
covers every one of the16 constructor obligations; no author repair
is requested by this initial audit. Only the coordinator may promote
the scoped result after the second independent whole review.
