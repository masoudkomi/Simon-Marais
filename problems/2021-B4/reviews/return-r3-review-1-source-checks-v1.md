# Source and dependency checks for return audit R1

2026-10-17 UTC. Initially blind nonconstructor review of all seven
reasoning-return-r3 candidates. No peer review findings were read.
The companion report supplies the independent mathematical reconstruction;
this record distinguishes theorem inputs from attribution and context.
Requested gpt-6.1-sol/max; effective-setting readback unavailable.

## Official domain

[Official 2021 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf),
page 2, B4 statement and part (b), directly opened in this audit.
The polynomial and each common witness belong to Q, the derivative
orders are 1 through d-1, the witness may depend on the order, and the
open question ranges over d>=2. No preliminary proof or other problem
was investigated. The local statement.md agrees.

## Primary published sources

1. Castryck--Laterveer--Ounaies,
   [Constraints on counterexamples to the Casas-Alvero conjecture, and a verification in degree 12](https://arxiv.org/pdf/1208.5404).
   Read the relevant normalization in section 3.4, Lemma 17, and the whole
   Proposition 19 proof and following remark in section 3.7
   (PDF pages 15--16). Proposition 19 requires all roots rational;
   the following extension needs an ambient number field unramified at p.
   Rational derivative witnesses do not supply either hypothesis.
   The new packets use the accepted normalization/local interface and
   do not invoke this stronger exclusion.

2. Draisma--de Jong,
   [original erratum/addition](https://math-unibe.ch/jdraisma/publications/erratumcasasalvero.pdf),
   one page, dated August 2011. Read in full. It adds 5 to the excluded
   primes for base degree 4 and retracts the stated degree-20 consequence.
   The characteristic-5 residue in the new packet is consistent with
   this correction. No corrected family theorem is used as a shortcut.

3. Diaz-Lopez--Harris--Insko--Omar--Sagan,
   [Descent polynomials, arXiv:1710.11033v2](https://arxiv.org/pdf/1710.11033v2).
   Checked the exact descent-set definition and all of Proposition 2.1
   and its proof, with the nearby polynomial-extension statement.
   The recurrence uses the specified descent set itself. Its polynomial
   identity permits negative length evaluation; no root-bound theorem
   is applied here. Version v2 was submitted 13 November 2017;
   its PDF title page is dated 15 November.

4. Marashdeh,
   [A descent-set obstruction for the Casas-Alvero conjecture, arXiv:2608.14726v1](https://arxiv.org/pdf/2608.14726v1).
   The abstract record confirms v1 on 12 August 2026.
   Read Theorems A--E in the introduction, the setting and proofs of
   Theorems 4.1/4.4 and Corollary 4.3, the one-nonzero-root boundary,
   Theorem 5.9 and Remark 5.10. The one-root descent/MacMahon connection
   is prior work. The two-element coefficient-support result is not
   a four-rational-witness result. This paper is attribution/context,
   not an imported exclusion or lifting theorem.

5. Cima--Gasull--Manosas,
   [Around some extensions of Casas-Alvero conjecture for non-polynomial functions](https://ddd.uab.cat/pub/artpub/2020/237526/CimGasMan2019e.pdf).
   Read the introduction's precise all-roots-real setting. That condition
   is stronger than rational shared witnesses. No theorem from this
   source is a new proof premise. Its historical first-open-degree
   sentence is not used as current status evidence.

The Descent polynomials journal citation in the author record gives
Discrete Mathematics 342(6), 2019, 1674--1686,
doi:10.1016/j.disc.2019.01.034. Direct DOI resolution returned an
internal browser error during this audit; that publisher metadata was
not needed for any mathematical inference. The exact arXiv v2 identity
and proof were successfully read.

No quotes or full source copies were added to tracked files.
No paper was newly downloaded. Existing ignored primary caches were
fingerprinted independently:

| Existing cache | SHA-256 |
| --- | --- |
| .cache/literature/2021/cited-66c5af6a0f0239f5.pdf | d818747102d32060f43ae5f015f27065aadf38699b272a2367749db8b33fedbf |
| .cache/literature/deep-literature-r1/2021-draisma-dejong-erratum-2011.pdf | 9414998fc302643b7cf261e4adec1333034dc732e8a3a493a1a0ff7418d8f262 |

I do not claim byte identity between these existing caches and
browser-rendered source responses. Browser source URLs and cache
fingerprints are different provenance records.

## Accepted project interfaces

I read the relevant accepted statements and mathematical bodies:

- rational-witness-p-plus-one-reviewed-v1.2.md: rational affine
  normalization and the witness/all-root distinction.
- padic-rational-newton-reviewed-v1.1.md: the accepted long edge,
  multiplicity conventions and its scoped register.
- coordinator-three-rational-witnesses-reviewed-v1.1.md and the
  full frozen coordinator-three-rational-witnesses-v1.md: T1,
  exact finite-family coverage and certificate mechanism. The
  separate prior exhaustive certificates are accepted dependencies;
  no rerun or fresh validation of them is represented here.
- proofs/reviewed-reasoning-J15-v1.1.md: full D1--D5 scope,
  local Q_19 splitting, sole-H3 actual root, coefficients and
  retained low-order rational family.
- reasoning-J15-acceptance.json and three-witness-acceptance.json:
  promotion scope and fingerprints, without importing any review
  of the seven new return candidates.

The accepted sole-H2/sole-H4 registers and other historical files
listed by the constructor were fingerprinted as declared inputs.
They are not additional theorem premises of the new sole-H3
arguments, and I do not present their metadata checks as fresh
mathematical audits.

The audit reconstructs the global carrier, reflection, witness
splits, parity recursion, endpoint arithmetic and transfer directly.
It never treats one new unreviewed candidate as an accepted
dependency of another.

## Executed actions and preservation

Only read commands, public primary-source browsing and metadata hashing
were used before writing the assigned reviewer records. The metadata
checker parsed each of the seven manifests, their JSON records and
embedded input-validation entries, and compared file lengths and SHA-256
digests. The first complete pass checked 826 recorded rows, representing
147 distinct paths, with no mismatch. The freeze rechecks those records.
These are artifact-integrity checks, not mathematical tests.

The earlier reviewer/construction chain ending in the 2022 supplement
freeze is checked separately for preservation. No earlier review was
edited. Only problems/2021-B4/reviews/return-r3-review-1-* is written.
No Git, shared or candidate edit, process search, native CAS, support
enumeration, finite-family rerun, external contact, charge or separately
billed API occurred. Latest root-authoritative weekly use is 24%,
reset 1792745187, cutoff 90% total with review/integration reserve.
