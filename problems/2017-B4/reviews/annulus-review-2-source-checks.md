# Annulus A1--A5: initial source and procedure checks 2

Checked 2026-10-17 UTC, before reading peer annulus findings.

## Official scope

The official 2017 Paper B, p. 2, B4 asks for both limiting exponents
of the number of equal-side quadrilateral tilings of a regular
\(2n\)-gon of side length one, for integer \(n\geq2\).

- https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-2_1.pdf
- Official B4 comments, p. 12:
  https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-solutions-preliminary_1.pdf

The comments' marked values and arrangement dictionary fix the intended
orientation convention. These sources were checked directly in this
session and in the already frozen initial fixedD source audit. Neither
the local frame count in A5 nor the \(D=4\) integer geometry is equated
with the unrestricted official count.

Local normalized statement SHA-256:
e459750064b4e25e3eaa71f25f236c046548147e415b06d8bd097839020228f3.
AGENTS.md SHA-256:
28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff.

## Named primary lead and its precise use

Arroyo, McQuillan, Richter and Salazar, *Levi's Lemma,
pseudolinear drawings of K_n, and empty triangles*, author preprint,
2015-11-20:

https://www.ifisica.uaslp.mx/~gsalazar/RESEARCH/levi.pdf

Read and rechecked the full Section 2 arc definition and Lemma 2.2 proof,
printed pp. 4--5. It concerns a finite plane arrangement of separating
arcs, with distinct pairs disjoint or crossing once. It provides a dual
path crossing each arc at most once. It is not a finite-disk confinement
or annulus statement. The projective enlargement theorem has different
hypotheses and is not used here.

The annulus packet uses this paper only as a lead for its expressly
unproved cut-window interface. A1--A5 are not inferred from it. No
unreviewed DG disk adaptation is imported. The exact source hash,
streamed earlier in this session, is
0d90b6ddbef318b2a859f576b59896d01919bc1752bf34a27f925c0234c3f471.
No new full-paper file was saved by this reviewer for this audit.

The candidate's other substantive steps were reconstructed directly:
finite-word inversion order, ideal prefixes, planar positive shellings,
winding invariance under a point-avoiding homotopy, exact digital
threshold order, bounded integer-origin counts and the block-gluing
liminf/supremum argument. None depends on an SFT filling theorem,
unproved periodic entropy theorem, general annulus theorem, profile
convexity or the false height-only consequence challenged as FD2-01.

## Complete assigned packet and independence

The following four assigned files were read:

- annulus-reasoning-r1-candidate-v1.md:
  020d3f6408f9423b83ac2d5633d3e508a7468a16ebe6db673879fca2af1ff610.
- annulus-reasoning-r1-worklog-v1.md:
  f99a0f7342060bd5dcaea5ad09a97963e9a99d732e8d29ccd52c89e75a22e701.
- annulus-reasoning-r1-sources-v1.json:
  6ec82a9ffcffcc87cd0291246f660db27af841387f9623aa8692ce0290e481ff.
- annulus-reasoning-r1-freeze-v1.json:
  958640fdb6a6f30b17306b3ba01014431e26fc544a26ab06f186f4e2a4f8e6cc.

The initial large tool response truncated a small part of A5; the
complete lines 300--410 were then separately read, including the full
limit argument, obstruction and remaining-interface section. No
unread omitted passage is represented as audited.

The source and freeze files contain metadata hashes of other earlier
reviews, which were read as metadata. No peer annulus report, ledger
or conclusion was opened. The constructor's worklog and repair-ledger
description of its own approach are candidate inputs, not peer audit
findings or accepted proofs. The complete earlier FD2-01 targeted
report was separately frozen before this whole annulus audit began.

All earlier twenty-four files frozen by this reviewer are preserved and
verified by their recorded hashes, including the separate FD2-01
reaudit. No review, candidate, source record or shared file was edited
outside the assigned annulus-review-2 prefix.

## Mathematical and administrative operations

No routine tests, enumeration, CAS, random search, numerical certificate,
Git operation or subagent spawn was used. Exact computations in the
report are hand identities supporting the proof audit, including the
two-color continuous gap, kernel-vector identity and weighted area.

Administrative commands read the full assigned texts, obtained line
numbers, checked SHA-256 values and byte counts, verified earlier
manifests, and wrote this report's own freeze manifest. No full PDF
redistribution, charge, subscription, access bypass or third-party
contact occurred. The packet claims no novelty, and this review does
not add such a claim.

Requested model/reasoning: gpt-6.1-sol / max. Independent effective
readback: unavailable. Authoritative account-wide weekly telemetry
at 2026-10-17 00:38:56 UTC reported 20% total used, 10080-minute
window, reset 1792745187. Cutoff: 90% total used with review and
integration reserve; no separately billed API.
