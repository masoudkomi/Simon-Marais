# R7 ENTIRE whole-audit obligations and constructor checks

**Candidate proof — unverified.** These are constructor HAND checks, not
independent reviews or evidence from a mathematical program. Every row
must be reconstructed by TWO OTHER initially blind WHOLE auditors. C is
excluded as constructor. MAIN means the complete candidate-v1.md.

| ID | Inference and exact audit obligation | Constructor disposition / proof location |
|---|---|---|
| R7-01 | Official domain is positive odd n and a coefficientwise F2 product with both degrees positive. | Checked; MAIN0,7; no finite-field-function substitution. |
| R7-02 | Established quotient R and degree ell*q-2 are the same homogeneous polynomial. | Checked; MAIN0; preliminary existence is an attributed input. |
| R7-03 | q is the maximal power of two in n-1. | Checked; ell odd, i>=2. |
| R7-04 | T1's binary-weight hypothesis holds for every parameter. | Checked; wt(n)=wt(ell)+1>=3. |
| R7-05 | m=ord_ell(2) exists and is at least two, even for composite ell. | Checked; ell odd>=3, order1 would force ell divides1. |
| R7-06 | ALL ell-th roots, not just primitive ones, belong to E=F_(2^m). | Checked; ell divides2^m-1; MAIN2. |
| R7-07 | The finite-field intersection equals F2 under gcd(i,m)=1. | Checked by Frobenius/gcd; MAIN2. |
| R7-08 | i1, ell1, n1, n3 and the zero/unit boundaries are excluded explicitly. | Checked; MAIN7; no new claim there. |
| R7-09 | f_n is a nonzero polynomial, not merely a nonzero function. | Checked coefficient X^(n-1)Y=1; MAIN2. |
| R7-10 | All three homogeneous partials are the q-th powers in(1). | Checked by differentiation n odd. |
| R7-11 | W cannot vanish at a common gradient zero; W=1 yields a finite list. | Checked; MAIN2, no affine-only omission. |
| R7-12 | A repeated factor would divide all partials, so f_n and phi_n are reduced. | Checked; infinite curve versus finite common-zero set. |
| R7-13 | An intersection of two factors is singular on phi even when R=0. | Checked product rule, then f=R phi. |
| R7-14 | Affine partial equations give a^ell=b^ell=l^ell. | Checked injectivity of q-Frobenius. |
| R7-15 | f=0 then forces that common value to be one, with nonzero coordinates. | Checked a+b+l=1; MAIN2. |
| R7-16 | All infinity points away from R are smooth using the Z partial. | Checked (X+Y)^(n-1)!=0; MAIN2. |
| R7-17 | All three infinity vertices on R have phi=1. | Checked derivative of f=R phi at each; accepted T1 evaluation. |
| R7-18 | The three remaining affine types exhaust every possible intersection. | Checked: center, noncentral R=0, or R!=0. |
| R7-19 | A noncentral diagonal b lies in E but outside F_q. | Checked by R7-06/07 and b!=0,1. |
| R7-20 | c=b+1 and B0=1+b^(1-q) are nonzero before division. | Checked b!=1 and b not in F_q. |
| R7-21 | Frobenius expansion leaves no positive term below q at a singular point. | Checked exact (a+x)(a^q+x^q)^ell. |
| R7-22 | Both diagonal numerator terms in(4) are correct. | Hand expanded; MAIN3. |
| R7-23 | Diagonal denominator is exactly(5), with all four terms. | Hand multiplied y(c+x+y)(c+x). |
| R7-24 | Quotient's multiplicity is q-1 and initial tangent is y^(q-1). | Checked B0 nonzero and denominator order1. |
| R7-25 | Next quotient term has uncancellable x^q coefficient E0/c^2. | Checked division in(6), including degree2 denominator correction. |
| R7-26 | Pure-power cone plus next-term nondivisibility excludes two vanishing factors. | Proved MAIN1 for arbitrary r,s>=1, not just smooth factors. |
| R7-27 | Diagonal argument covers all three lines by actual coordinate symmetry. | Checked; no unhandled R=0 branch. |
| R7-28 | Off-diagonal a,b,1,l are pairwise distinct, all nonzero. | Checked pair equalities reduce to R=0; MAIN4. |
| R7-29 | A,B are defined uniquely over K, allowing a zero coefficient. | Checked q-Frobenius automorphism; no division by them. |
| R7-30 | Off-diagonal degree-q numerator term is L^q. | Hand expansion; MAIN4(7)-(8). |
| R7-31 | That term is nonzero in the full stated parameter domain. | Checked A=B=0 => ratios and1/l in F_q => center by(3). |
| R7-32 | Degree q+1 numerator term is exactly the second line of(8). | Hand expansion using ell odd and a^ell=b^ell=l^ell=1. |
| R7-33 | (B,A) is a nonzero direction on L=0. | Checked characteristic two and not both A,B zero. |
| R7-34 | First identity(9) has the full denominator a^q b^q l^q. | Checked clearing it without zero divisions. |
| R7-35 | Its coefficient of B simplifies to b+b^q. | Displayed hand chain in MAIN4. |
| R7-36 | Its coefficient of A simplifies to a+a^q. | Same expansion with a,b interchanged. |
| R7-37 | Raising T to q gives the intermediate expression in MAIN4. | Hand expansion of both products in(7). |
| R7-38 | a+b=l+1 reduces it to the exact Kasami four-point expression. | Checked constants cancel in q-powers and a+b+l=1. |
| R7-39 | Published Kasami APN theorem has precisely gcd(i,m)=1 and all m>=1. | Primary Sections1-4 read; imported theorem, not new result. |
| R7-40 | Odd-dimensional operative proof and external Lemma4 read limits are honest. | Complete returned text read; original root-classification proof not newly claimed. |
| R7-41 | Even-dimensional use is the complete FIRST proof with MCM Lemma5. | Read full operative first proof; gcd forces odd exponent parameter. |
| R7-42 | Later incomplete alternative even discussion is not used as a premise. | Explicitly excluded in MAIN0/source record. |
| R7-43 | Reducing i modulo m, if needed, preserves the function even at zero. | Checked nonzero positive residue and positive exponents; MAIN5. |
| R7-44 | Difference c0=a+b=1+l is nonzero. | Checked off-diagonal distinctness. |
| R7-45 | T=0 produces FOUR distinct solutions of the SAME derivative equation. | Listed a,b,1,l in(10); no two unrelated equations. |
| R7-46 | APN therefore forces T!=0 and tangent nondivisibility. | Checked the exact denominator and homogeneous line restriction. |
| R7-47 | Dividing by the unit R changes the next term only by a multiple of L^q. | Exact quotient(11), not an assumed factor Taylor gap. |
| R7-48 | MAIN1 excludes all off-diagonal intersections, not just F2 factors. | Checked over K with actual E-rational singular point. |
| R7-49 | Center numerator has cancelled degree q term and nonzero degree q+1 term. | Hand expansion x^q y+x y^q. |
| R7-50 | Division by xy(x+y) yields multiplicity q-2 and cone(12). | Checked exact degree and nonzero form; q>=4. |
| R7-51 | Cone(12) consists of exactly q-2 distinct lines and no x or y factor. | Checked q-1 odd; remove alpha1 from F_q*. |
| R7-52 | Reduced phi admits a split into two coprime homogeneous positive-degree products. | Checked absolute component partition, MAIN6. |
| R7-53 | Factors missing P are included with multiplicity zero. | Checked MAIN6, no false all-components-through-P premise. |
| R7-54 | Coprime initial cones give exact local intersection r*s, including the unit case. | Fulton3.3 property5 and separate unit case, hypotheses explicit. |
| R7-55 | Every possible intersection outside P, including infinity, has been excluded. | Checked R7-16/17/27/48 jointly. |
| R7-56 | Projective Bezout applies to U,V without a common component and gives(14). | Full operative primary proof read, char2 valid. |
| R7-57 | Multiplicity equals degree only for a binary homogeneous form in P-centered coordinates. | Checked monomial degrees; over K such a form splits into lines. |
| R7-58 | T1 gives strict m<degree for EACH nonconstant divisor, contradicting(14). | Checked also r=0 or s=0, not just irreducible U,V. |
| R7-59 | ord_(2^s-1)(2)=s for every s>=2. | Checked by the strict size of2^t-1 for0<t<s. |
| R7-60 | R7D and i2/odd-s family follow with binary weight>=4 where claimed. | Exact symbolic arithmetic; no enumeration. |
| R7-61 | n13 is excluded by gcd(2,ord_3(2))=2. | Checked; no absolute claim at the known boundary. |
| R7-62 | Whole absolute irreducibility rules out official ordinary F2 products, including nonhomogeneous ones. | Checked polynomial-ring implication, MAIN7. |
| R7-63 | Old three-bit/R6/R4/R5 results are not re-labelled as new or silently widened. | Full operative bodies/current scopes read; only T1/reducedness operative. |
| R7-64 | No converse, whole annual classification, Férard-body read, novel APN theorem or priority is claimed. | Explicit MAIN0,7,8 and source/failure records. |

All64 are constructor checked only. Open status: TWO OTHER WHOLE audits,
all source-hypothesis checks and coordinator reconciliation are pending.
