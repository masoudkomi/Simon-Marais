# 2022 return-r3 R1: primary-source and dependency checks

2026-10-17 UTC. Whole independent initial review. No new peer return-r3
report or finding was read before freezing this source check. All links
below were opened directly during this audit. No new full paper was
downloaded or copied into a tracked directory. Existing ignored PDFs
were only checked against the constructor's hashes.

## Official problem

[Official 2022 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2022-paper-b.pdf),
page 2, B4 statement and part (b). Verified positive integers, product
>=600, simultaneous old-coordinate updates, and a nonnegative equality time.
No preliminary trapping proof is reproduced. The local statement normalization
matches the source.

## Accepted local dependencies

Read the entire `proofs/reviewed-partials-v1.md` and
`proofs/reviewed-arithmetic-complexity-v1.1.md`, including attribution,
plus `reviews/acceptance.md` and
`reviews/arithmetic-complexity-acceptance.md`. The new proof uses the
accepted closed strip, finite-control lifting bijection, rational Z10
fixed-denominator property, and the complexity result only for comparison.
I reconstructed the quotient interface and fixed-denominator inference in
the whole report. I did not use another new return-r3 review as a dependency.
The finite-lift, ordinary-lift, bounded-rational and high-complexity boundaries
in these accepted expositions are preserved by the new packet.

## Dubickas 2009: attribution rather than an inapplicable scalar theorem

[Original publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C40C0C07FEC20797475BB2899C436C9A/S0017089508004655a.pdf/on_integer_sequences_generated_by_linear_maps.pdf),
Theorem 3, journal page 245; entire Section 4 proof, page 249.
The theorem assumes a positive integer ceiling orbit with coprime p>q>1.
Its proof compares divisibility after repeated correction blocks with real
orbit growth. The candidate credits this method and supplies its own signed
loop proof. It does not treat the full controller as that scalar map.

## Dubickas–Mossinghoff: the actual proper-subset question

[Author-uploaded full paper body](https://www.researchgate.net/publication/220576840_Lower_bounds_for_Z-numbers),
Section 1, equation (1.1), and complete Proposition 3.2 proof in Section 3.
The original question requires a nonempty proper residue subset and positive
starts. Proposition 3.2 treats one residue only. The candidate's set has two
residues, so no unconditional termination conclusion follows from it. I used
the paper body, not the generated webpage abstract. No access restriction was
bypassed; no claim about an unseen publisher PDF is made in this review.

## Andrieu–Eliahou–Vivion v2: conditional residue escape

[Primary arXiv full text, version 2](https://arxiv.org/html/2510.11723v2),
dated 7 April 2026. Read the introduction's conjectural status and weaker
zero-letter discussion, plus full Section 3.3 through Question 3.12,
Proposition 3.13 and its proof, and Remark 3.14. Their implication uses
conjectural normality/equidistribution; it is not an unconditional residue
theorem. Question 3.12's proper-subset convention is made explicit in the
older source above. This supports the candidate's stated conditional boundary,
not a claim that all literature has been exhausted.

## Akiyama–Frougny–Sakarovitch: exact alphabet and boundary

[Original author PDF](https://perso.telecom-paristech.fr/jsaka/PUB/Files/RBNS-rev.pdf),
Section 3.3, complete Proposition 13 proof, pages 12-13 of the PDF; also
Proposition 37 and Corollary 38 with proof, pages 22-23. The converter uses
digits {0,...,p-1}, reads from the right, and has a terminal output/acceptance
condition. Its proof addresses positive numerical values; negative terminal
states are not final. Thus the p=11 alphabet includes 10. Corollary 38's
two-expansion condition p>=2q-1 fails for both ratios under discussion.
These qualifications are sufficient to check the claimed source boundary.

## Integrity, method, and access record

The constructor's three original artifacts, thirteen frozen inputs,
supplement, base-freeze link and two existing cached primary PDFs were
compared with their recorded bytes and SHA-256 values: 20 checks, all
unchanged. The input-validation file preserves the detailed list. The
supplement-freeze file itself is also fingerprinted in the review manifest.
No mathematical assertion was accepted from a truncated display: the complete
candidate, supplement, accepted expositions, log and source packet were read
in separate adequate displays where needed.

The web reads used the official statement, author/publisher originals and
the author-uploaded original paper body. No review, search snippet or
secondary summary supplies a mathematical premise. All mathematical
reconstruction was by hand. Administrative Python only hashes and records
files. There was no enumeration, CAS, paid access, contact or separately
billed API. Latest account-wide weekly telemetry was 23% total used,
reset 1792745187; cutoff 90% total with integration reserve.
