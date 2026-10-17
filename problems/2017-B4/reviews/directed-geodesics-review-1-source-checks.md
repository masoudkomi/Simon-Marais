# Directed-geodesics whole audit 1: source and procedure checks

Checked 2026-10-17 UTC, before peer review comparison. Requested
gpt-6.1-sol / max; independent effective-setting readback unavailable.

## Original arc-path source

Alan Arroyo, Dan McQuillan, R. Bruce Richter and Gelasio Salazar,
*Levi's Lemma, pseudolinear drawings of K_n, and empty triangles*, author
preprint, dated 2015-11-20.

- Original author URL:
  https://www.ifisica.uaslp.mx/~gsalazar/RESEARCH/levi.pdf
- Read scope: all Section 2 definitions preceding Lemma 2.2 and its entire
  proof, printed pp. 4--5. The adjacent enlargement theorem was also
  distinguished from the actual lemma used.
- Verified applicability: finite plane arcs, each separating the plane,
  distinct pairs disjoint or meeting once in a crossing; the lemma produces
  a dual path crossing each arc at most once. Parallel pairs are permitted.
- Application check: the candidate constructs proper piecewise-linear lines
  satisfying these requirements. The source itself does not state DG2 or
  claim a disk-to-plane identification for this tiling.
- Streamed original PDF SHA-256:
  0d90b6ddbef318b2a859f576b59896d01919bc1752bf34a27f925c0234c3f471.
  No new full-paper file was saved or redistributed by this reviewer.

The web tool returned readable PDF text for the complete relevant definition,
statement and proof. Its page-screenshot requests for zero-based pages 3 and 4
failed with a cache-miss response, so visual page rendering is not represented
as a successful check. The statements and proof used here contain no necessary
figure.

Exact retrieval/hash command, successful with authorized network escalation:

    /bin/zsh -o pipefail -c 'curl -L --fail --silent --show-error https://www.ifisica.uaslp.mx/~gsalazar/RESEARCH/levi.pdf | shasum -a 256'

Output:

    0d90b6ddbef318b2a859f576b59896d01919bc1752bf34a27f925c0234c3f471  -

The initial sandboxed curl attempt failed to resolve the host. Its downstream
hash command printed the hash of an empty stream; that value was discarded and
is not a PDF hash. The repeated command used pipefail and completed with exit
code 0. Public access was already authorized; there was no purchase, charge,
subscription, access bypass or third-party contact.

## Official domain and attribution boundary

- Official 2017 Paper B, p. 2, B4:
  https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-2_1.pdf
- Official 2017 notes, p. 12, B4 comments:
  https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-solutions-preliminary_1.pdf
- Rechecked the exact \(n\geq2\) domain, regular \(2n\)-gon, side length 1,
  equal-side quadrilateral tilings and both limiting exponents. The notes'
  small values and arrangement dictionary fix the marked orientation
  convention. No other problem was investigated.
- Existing official cache hashes were already recorded in the research
  packet and are used only for source integrity:
  Paper B 69d7cf84128c2464d962136ed613808b6c7a7b07122cfba9c06b5adf775e2a68;
  notes c272a72239ef4c2ccd54df0702140179e0a9b85f5a9028c87d485841eb1a2c12.
- DG1 is an application of the attributed published arc-path mechanism with
  a separately audited finite-disk construction. DG2 is a local estimate
  conditional on DG1 and a strictly positive affine direction. No novelty
  assertion, closed-annulus theorem, exponent value or universal recovery
  theorem is supported or claimed by this source check.

## Local input integrity

- AGENTS.md:
  28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff.
- problems/2017-B4/statement.md:
  e459750064b4e25e3eaa71f25f236c046548147e415b06d8bd097839020228f3.
- Candidate and constructor freeze hashes are recorded in the report and
  machine-readable manifest. Their initial hashes matched the assignment.
- No peer directed-geodesics report, issue ledger or conclusion was read.
  No other frozen initial review was edited.
- All mathematics was checked by exact topological, combinatorial and
  inequality reasoning. No enumeration, CAS, statistical test or numerical
  certificate was run.

## Budget and settings record

At 2026-10-17 00:32:46 UTC, the authoritative account-wide weekly telemetry
reported 20% used in the 10080-minute window, resetting at Unix timestamp
1792745187. The 90% total-used cutoff and integration reserve remain applicable.
No separately billed API was used. Requested settings and unverified effective
settings remain distinct.
