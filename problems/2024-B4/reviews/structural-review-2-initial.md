# Independent whole structural review 2: T1--T4

2026-10-16 UTC. This is a blind initial review of the entire structural candidate. The reviewed file remains **candidate proof - unverified** pending the coordinator's two-review reconciliation. This reviewer makes no promotion and no novelty claim.

## Independence, settings, and initial disposition

I did not construct the candidate. Before freezing this report, its issue ledger, and its source-check record, I did not read a peer structural review or receive its conclusions. The earlier 2021 and 2022 review artifacts are preserved and their peer findings remain unread.

Requested settings remain gpt-6.1-sol / max, from the coordinator assignment and AGENTS.md. An independent effective-setting readback is unavailable; the request is not reported as verified execution settings.

Frozen candidate: notes/structural-reasoning-r2-candidate-v1.md, SHA-256 0c451d5f9410573625725bc6be35af91fe938deee4dc1d92910572374dc69f52, 16027 bytes. The candidate and all six records in its manifest match their recorded fingerprints.

**No blocking or substantive mathematical defect found in T1--T4.** I reconstructed every substantive step, including the point-free cubic count, treatment of individual base-field factors, and the coordinate-action contradiction in T4. No mathematical author repair is requested. One minor terminology advisory is recorded separately: Section 3 concerns ternary homogeneous cubics, despite its heading saying binary cubics. This does not affect any argument.

I recommend acceptance only of the four stated partial structural results after reconciliation with the second independent whole audit. They do not classify all admissible exponents, force reducibility for a general exponent, or show that all global factors pass through P.

## 1. Official domain, homogeneity, and boundary conditions

The [official 2024 Paper B, page 2](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf) specifies odd positive n and a coefficientwise polynomial congruence modulo 2 with two integer polynomials that are nonconstant modulo 2. The candidate correctly studies factorization over \(\mathbb F_2\), rather than polynomial functions on a finite set or factorization solely over an extension field. An \(\mathbb F_2\) factorization can be lifted coefficientwise to integer polynomials.

The packet deliberately restricts to odd n of binary weight at least three; in particular \(n\ge7\). Thus it does not apply its line obstruction to the excluded binary-weight-two family, or its tangent notation to \(n=1\), where \(v_2(n-1)\) would not be a finite integer. The elementary unit/zero boundary cases are outside its four theorems. T4 additionally has \(n=8\ell+1\), with \(\ell\ge3\) odd, so \(v_2(n-1)=3\) exactly and the binary-weight condition automatically holds. The case \(\ell=1\) is excluded and no degree bound from T1 is applied to it.

The quotient setup \(f_n=R\phi_n\) is accepted context for part (b). In this packet \(\phi_n\) is a nonzero homogeneous polynomial of degree \(n-3\). Nonzeroness also follows directly from the diagonal derivative checked in T1 below.

Nonhomogeneous factors cause no omitted cases. If a nonzero homogeneous polynomial equals \(A B\) in a polynomial ring over a field, the least total degrees of nonzero homogeneous pieces add, and the greatest total degrees add. The product has only one degree, so the degree ranges of both A and B have length zero. Therefore both factors are homogeneous, up to scalar units. This applies over \(\mathbb F_2\) and its algebraic closure. Consequently a proof excluding homogeneous lines also excludes nonhomogeneous degree-one divisors, and the homogeneity of H in T2 is justified.

Repeated factors away from P are not excluded by the packet and are not needed to be excluded. Repetition through P will be ruled out by the squarefree local cone, not by an unsupported global squarefreeness claim.

## 2. Whole reconstruction of T1: every algebraic-closure line

Let \(k=\overline{\mathbb F}_2\). Any homogeneous line has a nonzero coefficient; after permuting the symmetric coordinates and scaling, it has equation \(X+aY+bZ=0\). Substitution into \(f_n\) gives

\[
(aY+bZ)^n+Y^n+Z^n+((a+1)Y+(b+1)Z)^n=0.
\]

For \(0<j<n\) with odd binomial coefficient, coefficient comparison yields

\[
a^j b^{n-j}+(a+1)^j(b+1)^{n-j}=0.
\tag{L1}
\]

Because n is odd, \(j=1\) and \(j=n-1\) are eligible. If \(a=0\), the first equation forces \(b=1\); if \(a=1\), it forces \(b=0\). The second equation gives the same alternatives if \(b=0\) or \(b=1\). The exponent \(n-1\) is positive throughout this domain, so none of these deductions uses a zero-th power. These alternatives are prescribed diagonal lines after undoing the coordinate permutation.

For all other cases, \(a,b,a+1,b+1\) are nonzero. Define

\[
A=\frac a{a+1},\quad B=\frac b{b+1},\quad T=A/B.
\]

Division in (L1) gives \(B^nT^j=1\). Choose a set bit \(h=2^s>1\) of n. A third set bit exists, so \(1+h<n\), and both \(j=1\) and \(j=1+h\) have odd binomial coefficients. The product identity for \((1+t)^n\) in characteristic two verifies this without a parity-table assumption. The ratio of the two equations gives \(T^h=1\). Since \(T^h-1=(T-1)^h\) in characteristic two and k is a field, \(T=1\).

Thus \(A=B\), whence \(a=b\) by cross multiplication, and \(B^n=1\). The coefficient of \(Y^n\) in the original substituted polynomial is then

\[
a^n+(a+1)^n+1=1,
\]

because \(B^n=1\) gives \(a^n=(a+1)^n\). This contradiction rules out every additional line, including lines defined only over an extension field.

Finally the prescribed diagonals have multiplicity exactly one in \(f_n\). Modulo \(X+Y\),

\[
\frac{\partial f_n}{\partial X}=Y^{n-1}+Z^{n-1}\ne0.
\]

If \((X+Y)^2\) divided \(f_n\), its derivative would vanish modulo \(X+Y\), including in characteristic two. Symmetry gives the other diagonals. Dividing by their product R removes all lines and proves T1 for \(\phi_n\). This is a coefficient identity over k, not an evaluation argument on \(k\)-points.

## 3. Rational points and the exact ordinary cone

At \((1:0:0)\), both \(\partial_Y f_n\) and \(\partial_Y R\) are 1. At \((1:1:0)\), both \(\partial_X f_n\) and \(\partial_X R\) are 1. In each case \(R=0\), so differentiating \(f_n=R\phi_n\) gives \(\phi_n=1\). Their coordinate-permutation orbits exhaust the six \(\mathbb F_2\)-projective points other than \(P=(1:1:1)\).

Write \(n=q\ell+1\), \(q=2^i\), \(\ell\) odd, for \(n>1\). The calculation also makes sense at \(i=1\). In the chart \(X=1+U,Y=1+V,Z=1\),

\[
R=UV(U+V),\qquad
(1+T)^n=1+T+T^q+T^{q+1}+\text{terms of degree at least }2q.
\]

The constants, linear terms, and q-th powers cancel from the four numerator terms. The first nonzero term is \(U^qV+UV^q\), of degree \(q+1\). Hence the initial form of \(\phi_n\) is exactly

\[
C_i(U,V)=\frac{U^{q-1}+V^{q-1}}{U+V}
=\prod_{\alpha\in\mathbb F_q\setminus\mathbb F_2}(U+\alpha V).
\tag{C}
\]

For \(i=1\), this is 1, so P is not on the curve. For \(i\ge2\), it has degree \(q-2\), consists of distinct lines, and contains no direction over \(\mathbb F_2\), including the infinite direction. The identity follows from the distinct nonzero \((q-1)\)-st roots of unity and removal of the root 1. Thus the candidate's projective point pattern is correct: no rational point when \(n\equiv3\pmod4\), and exactly P when \(n\equiv1\pmod4\).

For a factorization of \(\phi_n\), the initial forms of the factors vanishing at P multiply, while factors avoiding P are local units. Equation (C) therefore assigns disjoint subsets of its tangent lines to all absolute components through P. A repeated component or shared tangent through P would give a repeated line in (C), impossible. A base-field factor smooth at P would have a single \(\mathbb F_2\)-defined tangent, also impossible.

## 4. Whole reconstruction of the point-free cubic lemma

This lemma concerns homogeneous cubics in three variables. Point-free means nonzero at each of the seven points of \(\mathbb P^2(\mathbb F_2)\).

The three pure-cube coefficients must equal 1. At each point supported on two coordinates, the sum of its two corresponding mixed-cube coefficients must equal 1. There are three independent binary choices. At \((1:1:1)\), the sum of the pure and paired coefficients is \(3+3=0\), so the coefficient of XYZ must equal 1. These conditions are necessary and sufficient, leaving exactly eight cubics.

Let \(a,b,c\) be an ordered \(\mathbb F_2\)-basis of \(\mathbb F_8\), and \(L=aX+bY+cZ\). Its norm form

\[
N(L)=L\,\sigma(L)\,\sigma^2(L)
\]

has coefficients fixed by Frobenius and therefore in \(\mathbb F_2\). For every nonzero binary vector v, \(L(v)\ne0\), hence \(N(L)(v)=L(v)^7=1\). It is a point-free cubic split into conjugate lines.

There are \(7\cdot6\cdot4=168\) ordered bases. The three conjugate lines are pairwise nonassociate. Indeed an equality \(\sigma^j(L)=sL\), \(j=1\) or 2, would force \(b/a,c/a\) to be fixed by \(x\mapsto x^{2^j}\) in \(\mathbb F_8\), hence to lie in \(\mathbb F_2\). The coefficients would then be linearly dependent.

If \(N(L')=N(L)\), unique factorization forces \(L'=s\sigma^j(L)\) for some j. Comparing any nonzero coefficient places \(s\) in \(\mathbb F_8^\times\); conversely every such s has norm \(s^7=1\) and preserves the norm form. The 21 choices of \((s,j)\) are distinct because of nonassociation. They preserve the ordered-basis condition. Thus exactly \(168/21=8\) different norm cubics occur, exhausting all eight point-free cubics. No case was dropped through coincident lines, and no enumeration program is needed.

The quadratic observation is also correct. A point-free homogeneous quadratic would have three square coefficients 1 and, by the two-coordinate points, three mixed coefficients 1. Its value at P would then be 0, a contradiction.

## 5. Whole reconstruction of T2

Let H be a base-field irreducible factor of degree two or three. It is homogeneous by Section 1. If H has no \(\mathbb F_2\) point, the quadratic observation is a contradiction, or the cubic lemma gives an absolute line factor of H and hence of \(\phi_n\), contradicting T1.

Thus H has a rational point; the point pattern makes it P and forces \(i\ge2\). Since its tangent cone cannot contain a base-field line, \(m_P(H)\ge2\). If \(m_P(H)=\deg H\), its affine expansion at P has only its top homogeneous part. That binary homogeneous form splits into lines over k. Homogenizing after the rational coordinate translation gives actual projective line factors of H and of \(\phi_n\), forbidden by T1. This excludes degree two and the multiplicity-three cubic.

The remaining case is a cubic of multiplicity two at P. Its quadratic tangent form has no rational projective zero. Choose any rational projective line through P. T1 ensures that this line is not a component, so the restriction of H is a nonzero homogeneous binary cubic. Its local order at P is exactly two because the tangent form is nonzero on that rational direction. Removing the double linear factor for P leaves a base-field linear factor not vanishing at P. Its other projective root is rational, even if it occurs at infinity in a chosen affine coordinate, and gives a second rational point of \(\phi_n\). This contradicts the point pattern.

Degree one was already excluded absolutely. Therefore every base-field irreducible factor has degree at least four, and every base-field positive-degree divisor has degree at least four. The proof does not confuse extension factors with factors relevant to the official target.

## 6. Whole reconstruction of T3: individual-factor descent

Let H be a homogeneous \(\mathbb F_2\)-irreducible factor with H(P)=0 and \(i\ge2\). Normalize each absolute factor with one fixed monomial order and leading coefficient 1. Its coefficients lie in a finite extension of \(\mathbb F_2\). Frobenius permutes these normalized factors.

The action is transitive: the product of the factors in a proper orbit would be a nonconstant proper base-field divisor of H. At least one absolute factor passes through P, and because P is rational, all its conjugates do. Thus every absolute factor of H passes through P. A repeated absolute factor would contradict the squarefree cone (C), so H is a product of r distinct conjugates of an absolute factor G.

The orbit length r is exactly the degree of G's minimal coefficient field, with this normalization: \(\sigma^rG=G\) means all coefficients lie in \(\mathbb F_{2^r}\), and a smaller coefficient field would give a smaller period. Both degree and local order are invariant under Frobenius, yielding

\[
\deg H=r\deg G,\qquad m_P(H)=r\mu,\quad\mu=m_P(G)\ge1.
\tag{D}
\]

Take a tangent \(U+\alpha V\) of G and let d be the exact degree of \(\alpha\) over \(\mathbb F_2\). From (C), \(\alpha\in\mathbb F_{2^i}\), so \(d\mid i\). Frobenius to the d-th power fixes this normalized line and sends G to another absolute factor of H carrying the same tangent. Two different absolute components through P cannot share a tangent by squarefreeness of (C). Therefore \(\sigma^dG=G\) and \(r\mid d\).

The same argument works for every tangent of every absolute factor of H. With (D), it gives exactly

\[
r\mid\gcd(i,\deg H,m_P(H))
\]

and the additional divisibility by every tangent-field degree in H. The proof applies to one irreducible base-field factor, not to the whole polynomial without its irreducibility hypothesis. It does not assume that factors avoiding P are absent.

## 7. Whole reconstruction of T4: \(v_2(n-1)=3\)

Here \(q=8\) and the cone has degree six:

\[
C_3=(U^3+U^2V+V^3)(U^3+UV^2+V^3)=A B.
\]

Expansion gives all seven degree-six monomials from \(U^6\) through \(V^6\), as required by (C). Each binary cubic takes value 1 at the three binary projective points, so each is irreducible of degree three over \(\mathbb F_2\). Their roots have exact degree three and lie in \(\mathbb F_8\setminus\mathbb F_2\). The two cubics are different and the six tangent lines are distinct.

The tangent form of any base-field irreducible factor through P is a nonempty base-field divisor of AB. Thus it is A, B, or AB. Squarefreeness implies exactly one or two such factors, each occurring only once in \(\phi_n\). Swapping X,Y acts by \(U\leftrightarrow V\) and exchanges A,B.

### 7.1 Exactly one base-field factor through P

Call it H. Every coordinate permutation preserves H because \(\phi_n\) and P are invariant and there is no other base-field irreducible factor through P. On its absolute factors, coordinate permutations commute with Frobenius. The Frobenius action is an r-cycle, so its centralizer is the cyclic group generated by that cycle. Hence the image of \(S_3\) is abelian and its commutator subgroup \(A_3\) fixes every absolute factor.

This uses the abstract permutation group and its abelianization. It does not confuse permutation parity with the determinant scalar in characteristic two.

T3 gives \(r\mid3\), hence \(r=1\) or 3, since every tangent has exact field degree three. A cyclic coordinate permutation acts near P with linear part

\[
(U,V)\longmapsto(U+V,U).
\]

For example, cycling coordinates and renormalizing the new third coordinate gives this derivative; the nonlinear denominator is a unit and does not affect tangent directions. Pullback sends the line parameter \(\alpha\) to \(1/(1+\alpha)\). Its fixed lines satisfy \(\alpha^2+\alpha+1=0\), which are in \(\mathbb F_4\) and not in \(\mathbb F_8\). Thus every orbit on the six tangent lines has size three.

Every absolute factor of H is stable under that 3-cycle, so its finite tangent set is a union of size-three orbits. If \(r=3\), (D) gives \(\mu=6/3=2\), whereas the squarefree cone makes that tangent set have exactly two elements. This is impossible. Therefore \(r=1\), H is absolutely irreducible over \(\mathbb F_2\), and \(m_P(H)=6\).

Its degree is at least six. Equality would make its translated affine equation a homogeneous binary form of degree six and hence a product of lines after homogenization, contradicting T1. Consequently \(\deg H\ge7\), proving alternative 1.

### 7.2 Exactly two base-field factors through P

They have tangent forms A and B and local multiplicities three. The coordinate swap exchanges those tangent forms and therefore the two actual factors. It follows that their degrees, numbers of absolute components, and minimal absolute coefficient fields agree.

The action on this two-element set is a homomorphism \(S_3\to S_2\). One transposition acts nontrivially, and conjugacy of the transpositions shows that all transpositions do; hence the action is the abstract sign homomorphism. Every odd coordinate permutation exchanges the factors.

Again T3 permits only \(r=1\) or 3. If \(r=1\), both factors are absolutely irreducible and T2 gives degree at least four, which is alternative 2. If \(r=3\), (D) gives local multiplicity one for every absolute factor. Each is therefore smooth at P, has minimal field exactly \(\mathbb F_8\), and has degree at least two by T1. The two base-field factors consequently have equal degree, a multiple of three and at least six, which is alternative 3.

A mixed pair cannot occur: an \(\mathbb F_2\)-defined coordinate permutation exchanging the factors preserves their absolute factorization and coefficient-field orbit lengths. The one-factor case, two-factor absolute case, and two-factor three-conjugate case are mutually exclusive and exhaustive. Other global factors may avoid P and are untouched by this argument.

## 8. Source hypotheses, attribution, and limitations

I read the supplied source audit and research log, checked their hashes, and directly checked the specified primary source passages. The details are in the separate source record.

McGuire's Proposition 9 explicitly assumes base-field irreducibility; that assumption is correctly retained when T3 applies the classical orbit argument to H. The new proof reconstructs its stronger tangent-by-tangent information without importing a singular-point descent assertion for a reducible whole polynomial. The Kasami example \(n=57\) is consistent with the thesis's two degree-27 base-field factors and six degree-nine \(\mathbb F_8\) absolute factors, but is context rather than a premise of T1--T4.

The supplied source audit correctly isolates the later symmetric-product parity inference. In \(\mathbb F_2\), \(t_A t_B+t_A+t_B=1\) also when \((t_A,t_B)=(1,0)\) or \((0,1)\). Its explicit example \(A=1+X+Y,\ B=1+XY\) has

\[
AB=1+X+Y+XY+X^2Y+XY^2,
\]

so an odd nonconstant equal-degree-term count for the product does not force that count for both factors. This challenges that proof inference, not the separately attributed Kasami decomposition, and none of T1--T4 depends on it.

Hernando--McGuire's known component theorem and whole-irreducibility assumption are correctly separated from the official reducibility target. The unread original 1993 proof and unread full Ferard theorem are not hidden premises. No claim that the packet is new, or that a bounded search proves no classification exists, is made here.

No broad enumeration, CAS, factorization program, height bound, or numerical experiment was used for this review. The finite coefficient counts and group arguments above are analytic proofs. No conclusion about a general exponent outside the packet's stated hypotheses follows from the audit.
