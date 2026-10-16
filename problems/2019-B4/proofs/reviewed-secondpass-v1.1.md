# 2019 B4(b): reviewed renewal and obstruction results

**Proved, independently reviewed (partial results)**, 2026-10-16 UTC.
This acceptance register covers the three frozen mathematical texts below
and the complete length-24 certificate in checkpoint 2. Their original
candidate labels remain as historical version information; this register
and `reviews/secondpass-acceptance.md` record the subsequent acceptance.
No mathematical body was changed after either initial blind review.

The growth constant of the original distinct-string sequence exists, and

    1.76521 < lambda < 1.83516197.

Its exact value remains undetermined. These results are partial progress
on B4(b); no claim of novelty or complete solution is made.

Accepted mathematical texts, identified by their immutable hashes in the
acceptance JSON:

1. [Canonical obstructions and renewal](../notes/secondpass-canonical-renewal.md):
   minimal noncanonical factors are factor-free and cross-bifix-free;
   `C(z)=1/(1-2z+F(z))`; at `R=1/lambda`, `F(R)=2R-1` and
   `sum n*f_n*R^(n-1)<=2`; exact-prefix tail enclosures.
2. [Rigid collisions](../notes/secondpass-rigidity-obstructions.md):
   an infinite two-parameter family with exactly two histories and unique
   proper factors; no finite sound equation presentation on the fixed
   history generators; fixed-window scheduling obstructions.
3. [Staircases and finite approximations](../notes/secondpass-staircases-and-pumping.md):
   arbitrarily long bounded-run rigid minimal factors; finitely many bases
   under only even run inflation cannot suffice; every finite minimal-factor
   avoidance upper approximation has growth strictly greater than lambda.
4. [Length-24 checkpoint](../notes/secondpass-checkpoint-2.md): the 143 factors
   through 24 and rational sign certificates give the displayed enclosure.

Both fresh initially blind reviewers reconstructed the full chains and
independently wrote exact enumeration/certificate checkers. Their reports
are [R1](../reviews/secondpass-review-1.md) and
[R2](../reviews/secondpass-review-2.md). Neither found an unresolved
substantive objection. The coordinator read both reports and verified
frozen input and review hashes before acceptance.

The older accepted existence, marked-context injections and finite
converging-enclosure arguments remain in [proof.md](../proof.md). The
official four-move relation remains attributed to the official solution
notes; preliminary part (a) is not reproduced as a research target.

Outside acceptance: the unrestricted run-compression conjecture,
1791-state parity experiment, all claimed regularity/algebraicity of the
full canonical language, and a formula enumerating every minimal factor.
The length-28 coordinator probe timed out and supplied no saved extension
word list; it plays no role in these accepted results.
