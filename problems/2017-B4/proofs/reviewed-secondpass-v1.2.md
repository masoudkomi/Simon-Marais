# Reviewed counting and gluing partial results

**Proved, independently reviewed (partial results)**, 2026-10-16 UTC.
The complete accepted mathematical arguments are the unchanged full
author-repaired v1.1 packets:

- [MacMahon inequality and hierarchy](../notes/author-repair-macmahon-candidate-v1.1.md), M1-M3.
- [Fixed-boundary fibers and gluing](../notes/author-repair-boundary-fiber-candidate-v1.1.md), F1-F3.
- [Four-direction entropy and construction](../notes/author-repair-periodic-grid-candidate-v1.1.md), G1-G2.

Their candidate labels record the earlier frozen status. The
[acceptance record](../reviews/secondpass-acceptance.md) and hashes seal
the later decision. Two initially blind full reconstructions, an author
repair and both independent targeted re-audits are complete.

M1 proves for positive integer a,b,c, with S=ab+bc+ca and MacMahon's
product M(a,b,c), the sharp finite inequality

    M(a,b,c)^2 * 16^S <= 27^S.

M2 bounds the output of the specifically defined adaptive full ternary
gluing model by 2^(c0*n^2+O(n log n)), c0=(3/4)*log2(3)-1. Singleton
full-ternary leaf trees require odd n. This model does not cover all
arrangements and supplies no upper bound on the whole C(n). M3 is a
conditional floor-robust recurrence lemma; its geometric injection is
a hypothesis, not supplied automatically by the recurrence.

F1 identifies a fixed labelled boundary-patch count with a fiber of
complete marked arrangement signs. Its converse uses the full exterior
rotation system, a transferred facial walk, and a regular neighborhood
to obtain a genuine Jordan disk even with bridges or empty slots. F2
factors constraints through the specified four-packet incidence
components. F3 gives injective replacement under proper distinct
transverse-port hypotheses; the empty patch contributes one.

G1 establishes a finite joint entropy limit for four fixed directions,
using separate superadditivity and nonnegative remainders. It does not
establish the limit requested for the growing-direction C(n).
G2 supplies the reproducible lower certificate

    liminf log2(C(n))/n^2 >=
    (1+log2(4419734746)/9)/24 = 0.1900060770448... .

The repaired proof resolves every uncounted multicrossing by one fixed
local wiring in simultaneously disjoint disks before simple-partial
tail completion. Those fixed choices preserve all counted choices and
the exponent. The exact finite Q(3,3) input was independently reproduced
by both initial reviewers; no incomplete side-4 run is used.

The current located published lower bound 0.2721 is stronger. Thus no
frontier improvement, exact rate, official entropy-limit existence, or
novelty is claimed. The primary tiling/arrangement dictionary, MacMahon
product, signotope theorem and private-tail completion are attributed
to the sources specified and checked in the full packets and audits.
