# Reviewer 2 audit assets

Created 2026-10-16 for an independent adversarial audit of `proof.md` v1.0, SHA-256 `5a90732b2696559176d02b6a695e1743fbc4406158a76c0185d9e06c17b06e83`. No review-1 assets or conclusions were read. No author computation code or output was read. The known m=5 preliminary case was excluded from separate computations.

All commands ran from `/Users/uqmkamga/Documents/ChatGPT/Website`.

## Exact computations

Command:

```sh
.venv/bin/python problems/2018-B4/reviews/review-2-assets/review2_exact.py
```

Dependencies: Python 3.12.14 standard library only for the exact script (`collections`, `functools`, `itertools`, `math`, `pathlib`, `time`, `platform`). The provided environment's pypdf 6.10.0 was used only to extract source text. Local Poppler `pdftoppm` version 26.05.0 rendered source pages.

The script saves `review2_exact-output.txt`. It enumerates actual strict columns, with a cap of 500,000 cached states per parameter case; checks the proposed sum separately; exhausts the forward and inverse reflection maps on all small row pairs; and checks leading-coefficient cancellation numerically. All 28 parameter cases completed, and no state cap was reached. No incomplete run is presented as complete. The output is evidence only.

An initial successful script run tested 26 pairs. Adding (9,1) and (10,1) produced the saved final 28-pair run, which also passed. The output file records the final run and its wall time. No failed mathematical or computational approach was discarded.

## Primary documents and hashes

- Cached official `.cache/official/2018-paper_b.pdf`: SHA-256 `fa26d31d056dfcb5f782209c20ee0c59f20717cdc48ef195c2099582037aa704`.
- Fresh `hering-howard-v2.pdf`: SHA-256 `4d03468322f4886c092aa263d88b98c593aacc2106f340049a36ec4b398ab360`; source <https://arxiv.org/pdf/1211.3941v2>; inspected Prop. 3.2, pp. 6-7, and tableau definitions p. 4.
- Fresh `ottaviani.pdf`: SHA-256 `8e6e11d3105670a7b6fa00df0a3e8665770001276e64bd776e10f58f70812cb4`; source <https://seminariomatematico.polito.it/rendiconti/71-1/119.pdf>; inspected Theorem 40 p. 186, Theorem 28 proof p. 173, first page and bibliography p. 192.

Retrieval commands:

```sh
curl -L --fail --silent --show-error https://arxiv.org/pdf/1211.3941v2 -o problems/2018-B4/reviews/review-2-assets/hering-howard-v2.pdf
curl -L --fail --silent --show-error https://seminariomatematico.polito.it/rendiconti/71-1/119.pdf -o problems/2018-B4/reviews/review-2-assets/ottaviani.pdf
shasum -a 256 problems/2018-B4/proof.md
shasum -a 256 .cache/official/2018-paper_b.pdf
```

PDF hashes for downloaded sources were calculated with Python `hashlib.sha256(Path(...).read_bytes()).hexdigest()`.

Rendering commands:

```sh
pdftoppm -f 6 -l 7 -scale-to 1500 -png problems/2018-B4/reviews/review-2-assets/hering-howard-v2.pdf problems/2018-B4/reviews/review-2-assets/hering-howard
pdftoppm -f 68 -l 68 -scale-to 1500 -png -singlefile problems/2018-B4/reviews/review-2-assets/ottaviani.pdf problems/2018-B4/reviews/review-2-assets/ottaviani-theorem-40
pdftoppm -f 2 -l 2 -r 100 -x 40 -y 840 -W 760 -H 330 -png -singlefile .cache/official/2018-paper_b.pdf problems/2018-B4/reviews/review-2-assets/official-b4
```

All four saved page/crop PNGs were visually inspected. Pypdf emitted `Ignoring wrong pointing object ... (offset 0)` warnings for the Ottaviani PDF. Extraction still succeeded; the rendered theorem page was legible and was checked visually. The mathematical statement was not inferred from garbled extraction.

## Online verification and failed retrievals

On 2026-10-16, the web tool opened the official B paper, the two primary full texts, <https://arxiv.org/abs/1211.3941>, <https://webhomes.maths.ed.ac.uk/~mhering/publications.html>, and <https://www.simonmarais.org/20181.html>. ArXiv's version history confirmed v2 dated 2014-01-19. The author's list confirmed the 2014 journal publication. The Ottaviani journal PDF confirms its volume-71 (2013) bibliographic label, and attributes Theorem 40 to Howe, section 5.4.2.3. Howe's original was not read; no independent verification of its contents is claimed.

Web screenshot requests for the Hering-Howard PDF page 6 and Ottaviani PDF page 68 failed with `Cache miss`. The DOI page <https://doi.org/10.1007/s00209-013-1272-4> was inaccessible through the web tool. These failures were resolved for the audit's purposes by the successful fresh downloads and local rendering above. No dependency or security change was made.

The linked official 2018 page currently renders competition results. Bounded `find` checks for `B4`, `correction`, and `open` did not reveal a statement explaining the historical open-label discrepancy. This is not an exhaustive search and does not establish absence of a correction elsewhere.
