# R2 source access and failure record

Checked 2026-10-17 Australia/Brisbane / 2026-10-16 UTC.

## Primary sources and local reads

- Read `AGENTS.md`, frozen candidate, author statement/references/literature audit, and author source manifest. Reconstructed C1-C4 before consulting the author's research log for precise imported restrictions. No other reviewer report or conclusion was read.
- Cached official Paper B page 2: extracted the B4 region. The first extraction started at the prose occurrence of `(b)` and therefore included the preliminary problem statement incidentally; no preliminary solution was read, investigated or reproduced. The final audit uses only the exact B4(b) statement. The official solution extraction selected only the unsolved-part remark on PDF page 20, starting at `Remarks`.
- Extracted primary cached PDFs with bundled Python `pypdf` into ignored `initial-review-2-*.txt` files. Chen-Mihailescu had 24 pages and matched the supplied hash. Other paper counts: Bennett-Levin 17, Bugeaud-Mihailescu 7, Son 5. Wang's actual PDF bytes were not locally obtained.
- Used bundled `pdftoppm` to render Chen-Mihailescu PDF page 2, Son page 4, and Bugeaud-Mihailescu page 2; viewed these images to confirm typography, including the footnote and coefficients. Full papers and page images remain in ignored cache.

## Public web actions

The following original public sources were opened through the normal web tool: official Paper B, Bennett's author-posted published PDF, Son's original journal PDF, the Fudan journal's full 2026 PDF, and Wang's original v1 HTML and PDF download endpoint. The Bugeaud-Mihailescu journal PDF web opener returned an internal error; its already cached primary PDF was read locally instead.

Two limited current-status queries were run:

1. `"Nagell-Ljunggren" "2026" "solutions"`
2. `"Nagell-Ljunggren" "2025" proof conjecture`

Primary results reconfirmed Chen-Mihailescu, Son, and Wang. No verified unrestricted solution was established by this audit. This limited search is not proof of absence. Search hits from nonprimary pages were not used as theorem authority.

## Failed download attempts, preserved without bypass

Command 1:

```text
curl -L --fail --silent --show-error https://www.preprints.org/manuscript/202512.0286/v1 -o .cache/literature/2025/initial-review-2-wang-2025-v1.html
```

Result: exit 56, `curl: (56) The requested URL returned error: 403`. No HTML file was created. This was a server HTTP response, not a sandbox DNS/network failure. No authentication or access-control bypass was attempted.

Command 2, a normal public PDF download endpoint also exposed by the primary site:

```text
curl -L --fail --silent --show-error https://www.preprints.org/manuscript/202512.0286/v1/download -o .cache/literature/2025/initial-review-2-wang-2025-v1.pdf
```

Result: exit 56, same HTTP 403; no PDF file created. The normal web tool independently returned the original PDF text, 9 PDF pages (cover plus eight numbered article pages). Both that text and the original HTML supplied full relevant Theorem 7 and Theorem 8 context.

The web PDF screenshot requests for PDF pages 7 and 8 both returned `Unable to resolve screenshot call because content type is not application/pdf and web screenshot is not enabled`, despite the preceding text opener reporting PDF content. I therefore make no claim to have visually inspected Wang's PDF. The cached `initial-review-2-wang-provider-snapshot.json` is a hashable provider extraction, not original HTML or byte-identical PDF. The formulas were cross-checked between the original HTML and provider PDF text.

## Arithmetic command and child cleanup scope

```text
/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -u problems/2025-B4/reviews/initial-review-2-run.py
```

The launcher uses the same executable with `-u initial-review-2-checks.py`, a 45-second explicit subprocess timeout and flushed per-stage checkpoints. Child PID `36288` completed with exit 0; no terminate or kill action was needed. The PID and exact parameters remain in `initial-review-2-job.json`. The script uses Python's standard library only; no native CAS was started and no unrelated process was touched.

No failed arithmetic attempts occurred. Source and artifact hashes, runtime version and result details are in the reviewer-owned manifest and results JSON. No full third-party source was added to a tracked path.

Dependency readbacks: Python `3.12.14 (main, Aug 25 2026, 13:50:33) [Clang 22.1.3]`; `pypdf 6.10.0`; bundled `pdftoppm 26.05.0`. These were read with `python3` importing `pypdf` and `sys`, and `pdftoppm -v`. Arithmetic itself imports only the Python standard library.
