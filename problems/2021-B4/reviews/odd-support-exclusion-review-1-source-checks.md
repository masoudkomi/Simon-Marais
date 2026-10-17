# PN1–PN4 R1: source, independence and method record

Checked 2026-10-17 UTC. Requested gpt-6.1-sol/max; effective setting unknown.
Whole initial report, ledger and this source record were completed before
any peer PN review or findings were read.

## Exact targets and local dependencies

Read the entire new candidate and constructor freeze manifest. The target
candidate SHA-256 is
`a7845441df7725edc5d30e28f7b8f28c529b0b710168ad4b068d279582c1857c`;
freeze SHA-256
`337a43225bd6637d666bc992738a49afab8e7b569f526281add45564ab17b592`.
The one-time review freeze verifies all 13 listed local artifacts, including
the unchanged accepted dependencies. Constructor program and output files
are hashed as bytes only, and were not read or executed to perform this
review. Their saved arithmetic is not a premise of my reconstruction.

Read the entire accepted parity PP1/PP2 text, its PB1 diagnostic, the accepted
return register and acceptance Markdown/JSON. Also read the parity source
record and official statement normalization. PP1/PP2 have exact frozen SHA
`6506e371c2a3eb8506f75c55ef3d80be9933ecbcd187be21fe5bd18932fe8789`;
the accepted register SHA is
`9cda0a35c42e7a3098418ec052180f4868ca995feee47b503971b8fc2cb6d4b4`.
The accepted statement still leaves joint endpoint nonvanishing unproved;
the new packet proposes to resolve that finite target and has not yet
been promoted. No acceptance was silently borrowed for the new lemma.

I authored PP1/PP2 and PB1 in the older accepted packets. Those dependencies
received two independent audits by other actors. I did not author the new
finite classification, operator expansion, 8x8 table or PN applications.
This report does not count as a new independent review of my own old work.

## Official annual statement

[Official 2021 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf),
PDF page 2, B4(b), read directly through the primary web PDF extraction.
The ambient polynomial has rational coefficients and an actual rational
common root for each nonconstant derivative, with the witness allowed to
depend on derivative order. PN3/PN4 retain that hypothesis. Only part (b)
was researched; the preliminary assertion was not solved or reproduced.

## Classical descent recurrence

A. Diaz-Lopez, P. E. Harris, E. Insko, M. Omar, B. E. Sagan,
*Descent polynomials*, arXiv1710.11033v2, header 15 November 2017;
published Discrete Mathematics 342(6) (2019), 1674–1686,
DOI 10.1016/j.disc.2019.01.034.
[Primary full text](https://arxiv.org/pdf/1710.11033v2).

Freshly read the definitions and full Proposition 2.1 with its proof.
For a nonempty finite set I of positive descent positions, m=max I,
the recurrence removes the largest descent position and uses an initial
m-letter block. Its polynomial identity has exactly the sign/orientation
retained by F_I=(-1)^|I|d(I;Z). This identity extends from the defining
integer range to the polynomial variable; no root-bound theorem or
positivity over the reals is used for the mod19 obstruction.

The new PN1/PN2 proof can in fact be verified directly from its integer
binomial recursion without invoking this external recurrence. The source
check supports attribution and PN3's accepted descent-polynomial interface,
not a new source theorem claiming joint endpoint nonvanishing.

## One-recycled-root attribution boundary

M. F. Marashdeh, *A descent-set obstruction for the Casas–Alvero conjecture*,
arXiv2608.14726v1, 2026.
[Primary full text](https://arxiv.org/pdf/2608.14726).

Freshly inspected the complete Theorem B statement and surrounding scenario
restrictions on PDF pages 3–4. Its single nonzero recycled-root setting
identifies the triangular recursion with descent counts, retaining the
nonvanishing coefficient requirement. The text expressly leaves scenarios
with multiple recycled roots untreated by that one-root conclusion.
PN1–PN4 neither import a multi-root classification from it nor use it as
an external finite nonvanishing theorem. No assertion of novelty is made.

Only these precise source interfaces were audited here, not entire external
paper proofs. No erratum-based prime5 shortcut, global rational-factor
claim or 19-adic-to-rational witness substitution is used by the new packet.

## Reproducible hand certificate and exact tool scope

The full report contains the independent eight prefix coefficient triples,
15 ordinary binomial values with residues for those prefixes, 10 ordinary
binomial values for the final operators, a separate eight-column linear
reduction, its complete auxiliary table and all 64 resulting residues.
These were reconstructed by hand, followed by the direct derivative and
Taylor arguments. This is the explicitly requested proof-critical finite
certificate; there was no larger mask/support enumeration or author-code
rerun. The PB1 diagnostic did not replace checking the other 63 cases.

Read-only commands used `cat` on the exact named files and `rg --files`
to locate the specified frozen dependencies. Web calls directly opened the
three primary PDFs above and located the indicated complete statements.
No new paper was downloaded or redistributed. The only executed Python for
this review is its own metadata-only one-time integrity freeze. No CAS,
mathematical script, subprocess search or separately billed API was used.

Account-wide usage at the transition was 26% total of the weekly
10080-minute window, reset 1792745187. Stop at or below 90% total with
integration reserve. No Git/shared edits, spawning, contact, charges or
access bypass occurred. All prior candidate and review bytes are retained.
