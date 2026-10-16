# Source and notation clarifications after both audits

2026-10-16 UTC. This addendum resolves the editorial issues without
changing frozen proof, reference, source, or review files.

Gordon's [small-lambda arXiv preprint v1](https://arxiv.org/pdf/2007.07292v1)
numbers the orbit inequality as Theorem 3 and the cyclic multiplier
bound as Theorem 4. These are the numbers used by the existing
references and computation notes. In the publisher version
([DOI record](https://doi.org/10.1007/s10801-020-00992-x)), the
corresponding numbers are Theorems 2 and 3; its Theorem 4 is a
contracted-multiplier extension. Read old theorem-number references
as explicitly referring to arXiv v1. R1 checked the publisher's indexed
text, rather than claiming a newly retrieved publisher PDF. The
mathematical statements applied here agree across these locators.

The orbit inequality counts a≥0 nontrivial orbits and b≥0 singleton
orbits. A literal reading of the source's word “positive” would
discard legitimate b=0 cases. Both independent reviewers reconstructed
the necessary counting argument with nonnegative counts, and the
existing code already implements that formulation. For example the
saved order-8, sum-zero set
{1,2,4,8,16,32,37,55,64} modulo 73 is fixed by multiplication by 2
and contains no singleton orbit. This is a source-wording issue,
not an error in the implemented test or a theorem about sufficiency.

The plane correspondence always requires the point action to be by
collineations. P2's final paragraph supplies this hypothesis; the
accepted register makes it immediate rather than relying on that
later clarification.

Gordon (1994), Theorems 2, 6 and 8, supplies the checked published
statements for the divisor multipliers, square descent and the
3-divisibility restriction. Both reviewers downloaded and inspected
the relevant pages of the [full paper](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v1i1r6/pdf/).
Original Jungnickel–Vedder and Wilbrink full PDFs returned HTTP 403;
primary publisher abstracts and Gordon's explicit restatements were
checked. No access restriction was bypassed. The original imported
proofs remain unaudited, a disclosed dependency rather than a new proof.

The published bound q<2×10¹⁰ translates conservatively to
3≤n≤2×10¹⁰, with n=2 separately retained. The project has not rerun
that large computation, and the two audits do not establish that this
is the latest possible verification bound.
