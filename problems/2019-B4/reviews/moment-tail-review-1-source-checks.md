# 2019 moment/regular-tail R1: source and dependency audit

2026-10-17 UTC. Independent whole initial review; no new peer moment-tail
report or findings were read before this packet froze.

## Primary official statement

[Official 2019 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-paper-b_1.pdf),
page 2, B4 statement and (b), directly opened in this audit. Checked the
initial string, alternating prescribed bits, addition at either end,
distinct-string counts, and the two exponential limits requested.
Only the open part (b) is investigated. The candidate uses an already
accepted common rate, and supplies new enclosures/convergence control;
it does not claim an evaluated exact answer.

## Accepted second-pass interface

Read in full:

* `proofs/reviewed-secondpass-v1.1.md`;
* `notes/secondpass-canonical-renewal.md`;
* `notes/secondpass-checkpoint-2.md`;
* `reviews/secondpass-acceptance.md`.

The acceptance register expressly covers the unchanged mathematical
texts despite their preserved historical candidate labels. Its relevant
accepted conclusions are the canonical language, factor-free/no-overlap
obstruction set, renewal identity, root identity, finite first moment,
rate equality with official distinct strings, and complete coefficients
through length 24. The new candidate does not inherit an incomplete
length-28 probe or the failed old suffix restriction.

I reconstructed the renewal bijection for an arbitrary subset G in my
report. The accepted finite data are inputs; I do not claim a fresh
exhaustion of the 143 words. The accepted prefix polynomial has coefficients
1,1,2,3,2,4,8,6,20,14,40,42 at degrees
4,12,14,16,17,18,19,20,21,22,23,24 respectively, exactly as used here.

## Accepted third-pass interface

Read in full `proofs/reviewed-thirdpass-v1.1.md` and
`reviews/thirdpass-acceptance.md`. The envelope theorem makes F_D a
subset of the actual intrinsic F, with agreement through 2D+1. The
accepted separation-three expression is unambiguous and gives precisely
z^4+z^12/(1-2z^5-z^8). Those are the properties needed for M1 and M3.
The union therefore adds known actual obstructions without introducing
false forbidden words or silently changing the canonical language.

The old separation-seven upper bound is already accepted. This review
does not rerun its 11,662-row vector certificate or its queue monitor.
Regularity at each cap is not treated as regularity of the full F.

## New mathematical inference: no external theorem gap

M1 and M2 are proved directly using factoriality, finite-coefficient
renewal, nonnegative-series convergence, elementary submultiplicativity,
uniform derivative convergence, and the fundamental theorem of calculus.
The last two use the already accepted finite first moment. No theorem
about analytic continuation, a simple dominant pole, full rationality or
a finite second moment is needed. The candidate cites no additional
external paper as a new premise, so no inaccessible theorem is accepted
by title or analogy.

The official four-move relation stays attributed context inside the
accepted results. This review does not reconstruct preliminary (a).
No full third-party source was downloaded, redistributed or newly cached.

## Independent proof-critical arithmetic

The independently written `moment-tail-review-1-certificate-v1.py` checks
only a fixed rational point. Before reading the author's certificate code
or JSON, I derived the identity

    25W^2 E_G=W^2[25-48z+sum(25-n)u_n z^n]
                +13z^12-36z^17-21z^20,
    W=1-2z^5-z^8,       G=U+z^12/W.

It clears denominators at r=100000000/176522347 using ordinary integers.
It checks the new sign is negative, the old P24 sign positive and W(r)>0.
Its reduced fractions agree exactly with the constructor's values,
which I opened afterward. No bisection, floating-point root, history
enumeration, factor search or automaton calculation enters this check.

The exact command was

    python3 problems/2019-B4/reviews/moment-tail-review-1-run-v1.py

The runner records child PID 89100, an external 10-second timeout,
exit code 0, elapsed time about 0.0284 seconds, reaping and saved stderr.
The complete output retains the full integer and fractional certificate.
Administrative freeze scripts separately record byte sizes and hashes;
they are not mathematical evidence.

## Preservation and budget

The supplied candidate and freeze hashes match the assigned values. All
thirteen constructor/dependency records in that freeze are checked by the
input-validation record. The review's earlier immutable packets are
separately rechecked for preservation. Only the assigned review prefix
is written, and no peer new review is read before this freeze. There are
no Git operations, shared-file edits, spawned agents, charges, external
contacts or separately billed APIs. Authoritative transition telemetry:
24% total weekly used, reset 1792745187; cutoff 90% total with reserve.
