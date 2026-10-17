# Structural review 2: sources, fingerprints, and verification boundary

2026-10-16 UTC. Blind initial whole review. Requested gpt-6.1-sol / max; independent effective-setting readback unavailable. No peer structural report or conclusion was read before this artifact and the joint freeze were completed.

## Direct source inspection

Opened the [official 2024 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf), page 2. Checked odd positive n, coefficientwise congruence, integer polynomials, and both factors nonconstant modulo 2. The review does not reproduce the preliminary construction.

Used the PDF skill in read-only mode to inspect existing page renderings from [McGuire's thesis](https://thesis.caltech.edu/4053/). Visually checked printed pp.10--11,29,35--37. Proposition B distinguishes its nonsingular case from assertions requiring base-field irreducibility; Proposition 9 explicitly assumes that irreducibility. The n=57 discussion records six degree-nine absolute factors over \(\mathbb F_8\), two degree-27 irreducible factors over \(\mathbb F_2\), and multiplicity three for each at P. These are context, not proof premises for T1--T4.

Read [Delgado--Janwa v1](https://arxiv.org/pdf/1612.05997v1), Section 3, equations (5)--(6), and Lemma 1's parity argument on PDF pp.8--9; also visually checked the existing full rendering of PDF p.7. The supplied audit correctly distinguishes the attributed decomposition from its later intersection argument. The displayed parity implication fails for input parities (1,0) and (0,1); the audit's small symmetric-polynomial example checks exactly. No conclusion about the truth of the later intersection theorem is inferred from that proof objection.

Read [Hernando--McGuire](https://arxiv.org/pdf/0903.2016), Sections 2.1--2.3 and the statements of Theorems 15--16. The definitions match this quotient. The known conclusion is existence of a base-field absolutely irreducible component outside the exceptional exponent families; whole-polynomial irreducibility is separately assumed in Theorem 15. These facts are correctly separated in the candidate and do not replace the official factorization question.

The original 1993 Janwa--Wilson proof and full Ferard theorem were not independently obtained or read in this review. The constructor's records describe those access limits; T1--T4 do not depend on either missing text. I did not repeat access attempts, contact authors, log in, or infer theorem hypotheses from metadata. No new full paper or page rendering was written.

## Reviewed packet fingerprints

| Path | SHA-256 |
|---|---|
| AGENTS.md | 28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff |
| problems/2024-B4/statement.md | 60244f7752634772adb434efbdb41a63fb02029dc3be4238f3718c6e5ec84e5f |
| problems/2024-B4/notes/structural-reasoning-r2-candidate-v1.md | 0c451d5f9410573625725bc6be35af91fe938deee4dc1d92910572374dc69f52 |
| problems/2024-B4/notes/structural-reasoning-r2-manifest-v1.json | 55a13b078de0f0e2b404e294dc4015442c66cd103a8397079f1c1ab1d8704200 |
| problems/2024-B4/notes/structural-reasoning-r2-source-audit-v1.md | 8c18686381299e2e2a4b81c4728820a4ca5e52241df62a4b802fe1f4df4f4687 |
| problems/2024-B4/notes/structural-reasoning-r2-research-log-v1.md | ceeab21a0ff6b1f7e4515c6fd5e4e3919f5ba6f411a338f37ecb37eaf94af70b |
| problems/2024-B4/notes/structural-reasoning-r2-sources-v1.json | 4c71233c20137e1964869e55b33cd52f80bedaf8ab47c1518b8d20e97bc35d68 |
| problems/2024-B4/notes/structural-reasoning-r2-freeze-v1.py | 87bb430f34092f79da92b2848a25ff079d1a7b130f09b7cb0fd0afdd5475562e |
| problems/2024-B4/notes/structural-reasoning-r2-freeze-output-v1.json | 5e6395b554069ba10ca5355a9846deb6b08606235c46cc02c7e2208a18082bf6 |

All six packet records match the manifest. The freeze script was hashed but not executed or used as a mathematical premise. Its historical output is provenance, not an experiment repeated by this reviewer.

Existing ignored full-paper hashes were checked read-only:

| Existing cache | SHA-256 |
|---|---|
| .cache/official/2024-paper_b.pdf | 1401f21218ad4c387c4d537ed8fd7de119b376cba52957ef788c772dc5ab4ddc |
| .cache/literature/deep-literature-r2/2024-mcguire-thesis-1995.pdf | d8e8e62d873c5ec69e2fd40473a9aee257bb8d4994cb5ffc1a42cb70f8bcbd24 |
| .cache/literature/deep-literature-r2/2024-delgado-janwa-1612.05997v1.pdf | 9704f18d5acbec194e89ab26eed3c0a39d944a3de0c73896e4a05269c18528d9 |
| .cache/literature/2024/cited-3e7f3cb84c20c6b1.pdf | bc9389858756658a7a2769a74ebb40b4df05523ddfe24a4639cd7d79ef31df16 |

These identify existing cache bytes; a fresh comparison of the web viewer's raw retrieval bytes is not claimed. Existing renderings used: McGuire suffixes 15,16,34,40,41,42 (printed pp.10,11,29,35,36,37) and structural-reasoning-r2-delgado-janwa-page7.png.

## Operations and budget

Read commands used cat, rg --files, nl -ba, and shasum -a 256. Primary web inspection used open and find. Existing PNGs were inspected through view_image under the PDF skill. No source files, candidate files, shared status, or Git metadata were edited. Only the assigned structural-review-2 review artifacts were written.

All mathematical reconstruction was exact reasoning, including the finite coefficient count and finite group arguments. No broad enumeration, CAS, polynomial factorization command, numerical approximation, native long-running child, separately billed API, or new agent was used. Python is used only for output hashes, manifest creation, and preservation checks of earlier review bytes.

Fresh authoritative account-wide telemetry was read at approximately 2026-10-16 23:55--23:56 UTC: 18% total weekly used, 10080-minute window, reset 1792745187. This matches the coordinator's prior window; the 90%-total ceiling with reserve remains in force. No account identifiers or authentication data are copied into these artifacts.
