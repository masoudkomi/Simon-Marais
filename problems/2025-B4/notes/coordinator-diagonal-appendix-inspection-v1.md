# Diagonal appendix: source inspection and unresolved repair interfaces

2026-10-17 UTC. **Research note, not a theorem refutation or accepted
source objection.** The unrestricted diagonal theorem is neither
proved nor disproved by this note. No mathematical counterexample
to a claimed Diophantine conclusion has been constructed.

Source: Bartolome--Mihailescu, [arXiv1412.5798v2](https://arxiv.org/pdf/1412.5798v2),
internal version1.13 dated2021-11-02. The root read Appendix5.1
and its application on printed pp15--16, and inspected both entire
rendered pages to distinguish actual formulas from extraction loss.
The cached primary PDF SHA is recorded in the companion freeze.
No full source PDF or page image is redistributed to GitHub.

The bouquet-dimension statement itself has a short correct proof:
if multiplication by a vector with distinct coordinates preserved
a proper subspace containing a vector with no zero coordinates,
all its Hadamard powers times that vector would lie in the subspace.
Their Vandermonde matrix is invertible, a contradiction. The printed
bound on the first escaping index needs care, but is not needed by
this direct invariant-subspace proof. This observation alone says
nothing about the later Diophantine estimate.

The application introduces a singular m-by-m matrix A of rank r,
its first r independent rows, and a new independent bouquet row.
It forms an augmented square minor S. The printed linear equations
are labelled with A, including A*lambda=d for d=e_(r+1).
Taken literally with the defined A this is incompatible with the
preceding first-r-row homogeneous conditions: the first r rows
span the row space, so annihilating them annihilates ALL rows of A.
The augmented S system can prescribe the new row to equal1;
the original A system cannot. This looks like a matrix-label error,
not a counterexample to the intended augmented construction.

Before using the second-case theorem as a project premise, resolve
the intended augmented equations, why the selected bouquet vector's
coordinates satisfy Lemma5.1's distinctness assumption, how the
resulting cancellation propagates to every conjugate, and the
delta=0 branch. The latter is written with a leading term that
must be reconciled with the preceding cancellation. These are
specific proof-reading obligations, not assertions that repair
is impossible or that the final theorem is false.

A tempting objection to the cofactor bounds was discarded on
inspection: replacing a column by the last standard basis vector
removes the new weighted row from the nonzero cofactor. Thus
large coordinates in the appended row do not alone contradict
the asserted bounds on those cofactors. This failed objection
is preserved rather than presented as a defect.

The elementary PG1--PG3 packet and the separate first-case CF1
candidate do not depend on this appendix, its upper bounds, or
the second-case theorem. A later whole source audit must inspect
the original2008 context and exact mathematical edition; no
stronger range exclusion is accepted on the basis of this note.
