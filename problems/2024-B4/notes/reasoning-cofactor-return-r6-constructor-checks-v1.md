# R6 constructor hand checks and exact vulnerabilities

18 October 2026 UTC. **Candidate proof — unverified.** This is the NEW
constructor's check record, not an independent review or theorem oracle.
Every one of the48 obligations has a resolution in the separate ledger.
The following checks expose the places most likely to conceal an error.

1. **Use the numerator.** The missing Taylor coefficients belong to f_n.
   They need not belong to phi_n, its complementary factor or its selected
   component. At a selected smooth point the complementary value J(P) is
   nonzero, so restricted polynomial orders, not Taylor coefficients, pass
   to h. No derivative of a quotient is assigned the numerator's gap.
2. **A component must be simple.** The gradient common-zero calculation is
   projective and finite, including infinity. A repeated component would
   force that whole curve into this set. This closes the multiplicity
   issue before choosing a point. Perfectness alone is not a substitute
   for this explicit calculation.
3. **Infinity is accounted for.** At a common gradient zero W cannot be0.
   Scaling W=1 handles projective points wherever Z happens to vanish.
   A nonlinear component is not the line Z=0, so it has infinitely many
   points with Z=1; a finite excluded set cannot occupy that affine part.
4. **One actual point suffices.** The argument does not require every
   point smooth, every tangent generic, a fixed finite coefficient field,
   or an effective way to list P. The algebraic closure is infinite. At
   the chosen point grad f_n!=0, and the factor identity itself forces
   both J(P)!=0 and grad h(P)!=0.
5. **Homogeneous versus affine gradient.** Euler is applied to f_n at
   Z=1, where f_n(P)=0. Thus nonzero homogeneous gradient cannot be
   supported solely in the Z coordinate. This justifies the actual
   affine tangent vector. No division by deg h is used; deg h may be
   even, as it often is in characteristic two.
6. **No line component through P.** If h restricted to the tangent line
   were identically0, h would have a linear factor. If another component
   of f_n were that line, its value at P would be0, contrary to J(P)!=0.
   Consequently the univariate product is nonzero and its finite zero
   order is legitimate.
7. **All zero parameters included.** Formula(4) holds for a=0,c=0 and
   q2. The coefficient interval2<=j<q is empty at q2, correctly leaving
   only the usual constant/linear vanishing and degree>=2. No field
   inverse, root of unity selection or separability condition occurs.
8. **The accepted inequality has the right object.** R4A is stated for
   every ACTUAL proper factor over the algebraic closure, including a
   least-degree absolute component. It is not merely an inequality for
   F2 factors, symmetric factors, or factors through P. Main §5 selects
   exactly an object in its domain and does not use a formal candidate H.
9. **The needed old input is weaker than R4B.** No large-component
   Frobenius descent or S4 normalization is needed. Under reducibility
   the least absolute degree is <=N/2; R4A directly makes it <A. The
   strict gap A<q is sufficient. The optional N>=3A-2 comparison is
   separately displayed, not silently presumed in the main route.
10. **Boundary consistency.** Gold line components are excluded from the
    nonlinear bound. The k1 case has q=Q<A, and also fails R4A's size
    hypothesis; no false Kasami exclusion follows. The theorem starts
    at Q8,k2. General q2 exponents and s<3 are not decided by R6D.
11. **Ordinary versus absolute conclusion.** The main contradiction
    excludes a factorization over K, hence in particular over F2. The
    converse is not assumed globally. Whole irreducibility is not
    inferred from an external theorem giving one F2-defined component.
12. **No new-source hypothesis is hidden.** The final proof can be read
    using only elementary line restrictions and the two exact old
    accepted inputs. Modern Gauss-map sources motivate the viewpoint,
    but their characteristic/dimension and separability assumptions
    are not invoked. Possible publication overlap remains unresolved.

An attempted counterexample must therefore attack the actual Taylor gap,
the existence of a regular component point, the unit transfer, or the
exact universally quantified R4A premise. Merely displaying a symmetric
formal polynomial of low degree is not an actual divisor counterexample.
This list does not assert that no counterexample or missed inference can
exist; the required two OTHER whole audits remain outstanding.
