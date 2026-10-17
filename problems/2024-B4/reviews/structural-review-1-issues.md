# Structural review1 initial issue ledger

2026-10-16--17 UTC. Candidate SHA-256:
`0c451d5f9410573625725bc6be35af91fe938deee4dc1d92910572374dc69f52`.
Initial whole audit completed without peer structural reports/conclusions.

| ID | Adversarial issue examined | Resolution | Status |
| --- | --- | --- | --- |
| 24-SR1-01 | Polynomial functions might replace coefficientwise congruence | Official definition checked; all identities and divisibility occur in polynomial rings. Norm counting explicitly counts distinct polynomials by UFD. | Closed, no defect |
| 24-SR1-02 | Domain could accidentally include weight2, n1 or n3 | T1/T2 assume weight>=3 and n>=7. T3 adds i>=2. T4 has exact v2=3, ell>=3 odd, excluding n9. Boundary exclusions checked separately. | Closed, no defect |
| 24-SR1-03 | A line over the algebraic closure might escape normalization | Homogeneous factors and coordinate permutation put every line in X+aY+bZ form; a,b remain arbitrary closure elements. | Closed, no defect |
| 24-SR1-04 | Zero denominators or a missing supported binomial index | a,b in{0,1} disposed of with j1,n-1. Three set bits ensure1+h<n. Frobenius ratio argument uses units only. | Closed, no defect |
| 24-SR1-05 | Diagonal lines might survive in the quotient with multiplicity | Nonzero derivative modulo each diagonal excludes a square divisor; R removes every line exactly once. | Closed, no defect |
| 24-SR1-06 | Rational point calculations might divide zero by zero | Values at six points obtained by differentiating f=R*phi, where the selected derivative of R is1. P handled by formal local expansion. | Closed, no defect |
| 24-SR1-07 | Tangent cone or its squarefreeness might fail for some odd ell | Low-degree expansion coefficient is1 because ell odd; q+1<2q. C_i has exactly the distinct Fq minus F2 directions. | Closed, no defect |
| 24-SR1-08 | Cubic norm argument might count only some point-free cubics | Seven coefficient constraints give exactly8 cubics. 168 bases modulo21 distinct norm equivalences produce8 different polynomials, proving completeness. | Closed, no defect |
| 24-SR1-09 | Norm conjugates or equivalence classes might repeat | An associate relation forces all coefficient ratios into F2, contradicting basis independence. UFD then gives exactly21 representatives per norm. | Closed, no defect |
| 24-SR1-10 | T2 cubic restriction might lose infinity or leave a residual root at P | Homogeneous binary restriction is projective and has exact multiplicity2 at P since its F2 direction is not tangent; residual linear zero is a different rational point. | Closed, no defect |
| 24-SR1-11 | F2 irreducibility might be confused with absolute irreducibility | T2 excludes F2 low factors using absolute-line contradiction; T3 assumes only individual H irreducible over F2 and proves its absolute orbit properties. | Closed, no defect |
| 24-SR1-12 | Singular-point field descent might use a nonsingular-point theorem improperly | Unique tangent assignment follows from the squarefree full cone, giving sigma^d(G)=G directly. No missing resolution/nonsingularity hypothesis. | Closed, no defect |
| 24-SR1-13 | Some conjugates of an individual H might avoid P | Rationality of P plus transitivity forces all its absolute conjugates through P, with equal multiplicity; unrelated global factors may avoid P. | Closed, no defect |
| 24-SR1-14 | Orbit length might give only a field bound, not minimal field | Normalized polynomial stabilizer under Frobenius is exactly the coefficient-field stabilizer. r is minimal, and r divides every tangent degree. | Closed, no defect |
| 24-SR1-15 | S3 action could fail to commute or its local formula be projectively wrong | Coordinate maps are F2-defined. Actual affine chart map has linear part(U+V,U). Centralizer and A3 argument checked on component classes. | Closed, no defect |
| 24-SR1-16 | One-factor r3 case might have fixed tangent directions | Fixed directions lie in F4 minus F2, disjoint from F8; all six tangent orbits have length3, incompatible with multiplicity2 per component. | Closed, no defect |
| 24-SR1-17 | Two-factor case could mix an absolute factor with a norm factor | Coordinate transposition exchanges actual F2 components and preserves geometric splitting/minimal field. Both r values coincide. | Closed, no defect |
| 24-SR1-18 | Degree or smoothness bounds might overstate local data | Degree=m would force lines; T1/T2 give stated bounds. Multiplicity1 implies smoothness at P only; candidate makes that local claim. | Closed, no defect |
| 24-SR1-19 | Hidden third component, repeated factor or all-components-through-P assumption | Tangent cone has two irreducible F2 cubic factors and is squarefree. Only1 or2 F2 components pass P; the rest are expressly allowed away from P. | Closed, no defect |
| 24-SR1-20 | Literature background might supply unproved premises or novelty | T1--T4 reconstructed self-contained. Thesis hypotheses, HM component theorem and Delgado--Janwa parity issue checked; inaccessible sources remain unused and novelty unclaimed. | Closed, no defect |

Unresolved substantive objections:0. Requested author repairs:0.
Recommendation: accept T1--T4 only in their stated partial scope after
the second independent whole audit and coordinator reconciliation.
