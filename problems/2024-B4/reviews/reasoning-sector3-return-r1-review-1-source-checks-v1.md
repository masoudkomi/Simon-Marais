# Sector3 R1: exact source and premise checks

2026-10-17 UTC. Fresh initially blind nonconstructor audit. Requested
gpt-6.1-sol/max; effective setting independently unreadable. No new
sector3 peer report or conclusion was read. Source inspection is not
an additional independent reviewer, and C/root remain contributors.

## Original operative theorem and proof

Gary M. McGuire, *Absolutely irreducible curves with applications to
combinatorics and coding theory*, Caltech thesis1995,
[original-author PDF](https://thesis.caltech.edu/4053/01/McGuire_gm_1995.pdf),
[DOI10.7907/1CZ2-6S05](https://doi.org/10.7907/1CZ2-6S05).
I used the existing scan at
`.cache/literature/deep-literature-r2/2024-mcguire-thesis-1995.pdf`,
2610589bytes, SHA256
d8e8e62d873c5ec69e2fd40473a9aee257bb8d4994cb5ffc1a42cb70f8bcbd24.
The normal web PDF opening returned an internal/inaccessible error.
No download, access bypass or byte modification was used to overcome it.

I applied the PDF skill read-only and visually read the complete existing
images for PDF pages7,11,12,13,14,15,18,20,21,22,23,24,25. These are
printed2,6--10,13,15--20. Exact page/image hashes are recorded in the
source JSON and final validation. The thirteenth image, PDF11, was
additionally read to check the ambient field and multiplicity definition;
the constructor's47 input records already bind the other twelve images.
The extra old PDF11 fingerprint is checked against its original
deep-literature source declaration. No rendering command or cache write
was required.

The definitions on printed6--7 work over a field k with points over its
algebraic closure, expand into homogeneous local pieces, and define
multiplicity as the first nonzero degree. Printed7--8 gives projective
Bezout for curves with no common component, with sum of intersection
multiplicities equal to the positive degree product. That hypothesis
is retained in the candidate; its shared-component case is handled
separately. The printed9--10 Proposition A and its entire proof require
both a unique tangent and coprime consecutive initial pieces. The
candidate's local argument is the precise polynomial consequence, with
its own proof, and does not require an undefined intersection number
for two factors with a common component.

Printed15--17 identifies the same quotient, its homogeneous and affine
forms, and the general n=2^i ell+1 expansion. Printed18--19 explains
the denominator correction when transferring numerator terms to the
quotient. The complete Theorem2.1' statement and proof are on
printed19--20/PDF24--25. It states WHOLE absolute irreducibility of
g_t(X,Y) for t>3,t=3mod4. No primality, cyclic-code minimum-distance
assumption or additional restriction on the odd ell occurs in that
theorem. I checked the actual proof, including evaluation of the cubic
on the double tangent, not just a title or abstract.

The candidate independently redoes the expansions and strengthens the
exposition of TypeII, denominator corrections, projective coverage and
shared components. I reconstructed each, as recorded in the full report
and36-row ledger. The original source's infinity remark is not used as
a substitute for that coverage, and no source defect is claimed. The
partial_Z derivative at infinity agrees with the remark. The new
all-index diagonal isolation is proved in the candidate and is not
claimed to be a literal theorem in this thesis.

Printed2/PDF7 directly links Theorem2.1 and the specified section2.4
results to the joint paper with Janwa and Wilson. The journal article
is *Double-error-correcting cyclic codes and absolutely irreducible
polynomials over GF(2)*, J.Algebra178(2)(1995)665--676,
[DOI10.1006/jabr.1995.1372](https://doi.org/10.1006/jabr.1995.1372).
The later primary paper's reference[5] confirms that bibliography.
The publisher opening was unsuccessful in this audit. I do NOT claim
to have read the journal PDF or even a successful publisher abstract
in this task. The original coauthor's actual thesis proof is the
operative source. The author's own broader abstract-reading history
is distinguished from my present read scope.

## Later primary context, not replacement proof inputs

[Hernando--McGuire0903.2016v4](https://arxiv.org/pdf/0903.2016v4):
I read the matching quotient definitions, conjecture/component
distinction, i1 attribution table, exact Theorem15/16 statements with
nearby proof context, section6's reported counterexample and the
references. Theorem15 assumes ordinary F2 irreducibility; Theorem16
in its ell-divisibility case gives an F2-defined absolutely irreducible
factor. Neither is imported as a general whole theorem. I did not
independently audit their complete global proof or rerun the reported
factorization. The v4 header is18Sep2009; its rendered later footer
does not change that version identification. No new PDF bytes were
saved or a hash invented for web-parser text.

[Delgado--Janwa1207.5528v1](https://arxiv.org/pdf/1207.5528v1):
I read the matching definitions and the complete Lemma1 statement
and proof passage on PDF4--5, plus the diagonal restriction discussion
on PDF9--10. They discuss selected exceptional-family coprimalities.
They are context only; no arbitrary-target theorem is attributed to
that lemma. No complete-paper proof audit or priority claim follows.

The original Janwa--Wilson1993 chapter remains unread and is not a
premise of S3A--S3D. Gold/Kasami decompositions, APN conclusions,
general factor-descent theorems and automatic-set results are not used
in the new argument. Old source limitations remain explicit.

## Official open target and exact accepted project scopes

I freshly read [official2024 PaperB](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf),
page2 B4(b), and the local statement. The domain is odd positive n;
the congruence is coefficientwise and both integer polynomials have
nonconstant reductions. The accepted quotient normalization is used
without investigating or reproducing the preliminary construction.
The n1 zero and n3 unit deductions, positive-degree requirement and
integer lift equivalence are explicit in the audit.

I read the following accepted copies only to the fresh scopes stated
here, together with each complete acceptance Markdown/JSON and its
integrity metadata. Their declared body fingerprints are checked,
while the growing historical inventories are bound by immutable
metadata rather than copied or mistaken for fresh mathematical review.

| Accepted copy | Current fresh read scope and role |
|---|---|
| reviewed-structural-v1.1.md, SHA082dc054ce2cdaea80eee009f4c97c877c6968afb54b5a8f3141b7354031dd3f | Lines1--155: status/scope, official normalization, T1--T4 statements and initial boundary discussion. Not a dependency of the new whole-sector proof; no extension of its binary-weight restrictions. |
| reviewed-divisor-criteria-v1.1.md, SHA3afbf3eda795ecfcf6989ef6ec855e5c7e795f26f5a84effe8c4bd73ffeb4ed3 | Lines1--185: accepted C7/C11 scopes, published attribution and normalization/descent context. New S3C rederives those singletons in a wider sector. Old coefficient certificate and scripts were not rerun. |
| reviewed-reasoning-components-r1-v1.1.md, SHA43f095a4286919a32db16298ae6ddde016f9ee10de9394c45584c69ca186fe36 | Lines1--145 and147--249: exact accepted IC scopes and complete source-free IC1 squarefreeness/smooth coordinate-boundary/contact argument. I specifically verified that its Y0 theorem does not apply without computation to Y=Z. J/IC2--4 are not new proof premises. |
| reviewed-component-saturation-v1.1.md, SHA84770c4555e611c7206292d892c1b0364ebe97a8c26db6667a26e4502cd27466 | Lines1--110: accepted all-k saturation scope and initial setup. CS's body is not imported or freshly re-certified; absolute irreducibility already makes the entire base the shared component in S3C. |

This task's mathematical proof is self-contained after the established
quotient normalization, the original attributed sector method and
classical projective Bezout. Earlier own review roles do not generate
an extra independent audit. Exact current constructor companions were
all read; source/read-history assertions in their log are reported as
constructor history unless separately verified above.

## Immutable preservation and commands

The initial baseline rechecked the constructor's9 artifacts plus freeze,
all47 declared input/source records, the relevant accepted authorities,
and my prior own11-file R8 packet. Its immutable manifest and validation
bind the earlier365 own paths, giving376 transitively preserved paths.
The baseline itself is6602bytes, SHA256
1146ff0f7421921db81b7b31e1955f7166fe7658d9b44f2ce0af915ff1c28988.
The final helper repeats necessary checks and records counts/digests;
it does not copy or replay the entire historical inventory. Metadata
reading has no implication of rereading unrelated old mathematics.

Read-only inspection used cat/sed/rg, view_image and the public web tool.
The PDF skill was read from the installed runtime and applied read-only.
The only executable Python in this audit hashes/validates metadata and
exclusively creates this fresh review prefix. No mathematical code,
CAS, exponent table, native job/PID, old author-script run, source
download, cache/shared/Git mutation, spawning, contact, charge or bypass
occurred. The exact final command and immutable outputs are in the
freeze helper/manifest. All new peer sector3 records remain unread
through the entire initial freeze.
