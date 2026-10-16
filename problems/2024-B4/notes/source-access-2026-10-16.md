# Focused-family literature access record, 2026-10-16

This is a bounded source search for 2024 B4(b), particularly the family
n=(64*16^m+1)/5. No novelty or complete-literature claim is made.

## Original-source findings

- Éric Férard, *On the irreducibility of the hyperplane sections of
  Fermat varieties in P^3 in characteristic 2*, Advances in Mathematics
  of Communications 8 (2014), no. 4, 497-509,
  DOI [10.3934/amc.2014.8.497](https://doi.org/10.3934/amc.2014.8.497).
  The [publisher's original abstract](https://www.aimsciences.org/article/doi/10.3934/amc.2014.8.497)
  announces a phi_13 divisibility criterion and an infinite family for
  t=5 modulo 8. The exact family and full theorem hypotheses remain
  unread. This paper is a prior-attribution lead, not a theorem relied
  on by the self-contained v1 candidate.
- The primary [GAATI publications list](https://gaati.org/publications/fr/)
  lists the paper with HAL identifier hal-01779804. Its public metadata
  API returned one record with openAccess_bool=true and the URI
  `https://hal.science/hal-01779804v1`, but no fileMain_s field.
- The existing Hernando--McGuire reference and n205 factor attribution
  were rechecked at [arXiv:0903.2016](https://arxiv.org/pdf/0903.2016),
  Section 6. No new theorem from that article is needed for the Cartier
  proof. Delgado--Janwa's [arXiv:1612.05997](https://arxiv.org/pdf/1612.05997)
  led to the Férard citation; its discussion is not substituted for
  reading Férard's original theorem.

## Access attempts and outcomes

The normal publisher article page was downloaded with curl. The first
sandboxed attempt failed with `curl: (6) Could not resolve host`; the
same authorized read was rerun through the required escalated interface
and succeeded. Relevant commands, all from the repository root:

```sh
curl -L --fail --silent --show-error 'https://www.aimsciences.org/article/doi/10.3934/amc.2014.8.497' -o /private/tmp/2024-B4-ferard-publisher.html
curl -L --fail --silent --show-error 'https://www.aimsciences.org/data/article/export-pdf?id=35639722-1f4a-4d82-b06d-fb1493ba278d' -o problems/2024-B4/.cache/ferard-2014.pdf
curl -L --fail --silent --show-error --connect-timeout 10 --max-time 45 'https://data.aimsciences.org/aimsmath-upload/AMC/2014/4/PDF/1930-5346_2014_4_497.pdf' -o problems/2024-B4/.cache/ferard-2014-direct.pdf
curl -L --fail --silent --show-error --connect-timeout 10 --max-time 35 'https://hal.science/hal-01779804/document' -o problems/2024-B4/.cache/ferard-2014-hal.pdf
curl -L --fail --silent --show-error --connect-timeout 10 --max-time 25 -X POST 'https://www.aimsciences.org/data/article/check-article-pdf?id=35639722-1f4a-4d82-b06d-fb1493ba278d' -o problems/2024-B4/.cache/ferard-pdf-availability.json
curl -L --fail --silent --show-error --connect-timeout 10 --max-time 20 'https://api.archives-ouvertes.fr/search/?q=halId_s%3Ahal-01779804&fl=title_s,fileMain_s,uri_s,openAccess_bool&wt=json' -o problems/2024-B4/.cache/ferard-hal-metadata.json
```

The publisher's export endpoint returned success status to curl but an
empty file. This is a failed full-text retrieval, not a downloaded paper.
The commented legacy direct-PDF link in the publisher HTML and HAL's
document link both returned HTTP 404 (`curl: (56) The requested URL
returned error: 404`). HAL's record page returned a bot/access-denial
page in the browser research tool. No access restriction was bypassed.

The publisher page's standard public download-handler JavaScript was
read to identify its normal PDF-availability check. That check returned
exactly

```json
{"result":"success","title":null,"message":"login","data":null,"count":null,"type":null}
```

No further publisher full-text attempt was made after this explicit
login requirement. There was no purchase, subscription, login attempt,
message to an author, or paid API use. The HAL API was used only for
public bibliographic metadata; it supplied no PDF. Reading a full
paper's theorem remains a task for a later authorized source check.

An attempted local `pdftotext` path from an earlier computation record
was unavailable; no extraction is claimed for an empty PDF. The actual
bundled executable was subsequently located under
`dependencies/native/poppler/poppler/bin/pdftotext`, but no paper had
been retrieved to extract.

## Retained local source hashes

All the files below are in the ignored `problems/2024-B4/.cache/`.
No full third-party paper is being added to Git. Licence terms have not
been verified for the unavailable full paper.

| File | Bytes | SHA256 |
|---|---:|---|
| ferard-publisher-2026-10-16.html | 98520 | 77e31e056d2501e7f6cb7c3f0de9c7778e90cf2bfebc7fd5beacb62e1ca89b20 |
| ferard-pdf-availability.json | 88 | bb4a403ad0249d94207003f80b15d8797e79d39d693bc804f262a391e18632e0 |
| ferard-hal-metadata.json | 325 | 91bd38967f7dc0d3336682975d2582a739b5b897c78129d520f65473c4102f9d |
| ferard-2014.pdf (empty failed retrieval) | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |

## Bounded search queries

The web research tool was used for these query groups; only original
publisher/author/institutional material is used as evidence in the notes.
Unrelated numeric or topic matches were discarded.

- `"205" "3277" polynomial APN factor`
- `"phi_13" "205" polynomial factor`
- `"4" "5" "infinite" "Hernando" "McGuire" reducible`
- `"On the Decomposition of Generalized Fermat Varieties"`
- `"phi" "3277" APN`
- `"205" "13" "divides" "APN"`
- `"205" "factor" "4^" McGuire`
- `"generalized Fermat" "205"`
- `Férard phi polynomial "205" "infinite"`
- `Ferard "absolutely irreducible" "5" "8" polynomial`
- `"Férard" "497" "pdf" Fermat`
- `"Ferard" "205" "13" polynomial`
- `"hyperplane sections of Fermat" pdf ferard`
- `"Férard" "irreducibility" "hyperplane" filetype:pdf`
- `"Ferard" "hyperplane" "hal"`
- `"phi_{13}" "Férard"`
- `"Férard" "205" "3277"`
- `Eric Ferard publications site:gaati.org`
- `"On the irreducibility" "Fermat" "pdf" "2014"`
- `"amc.2014.8.497" pdf download`
- `"hal-01779804"`
- `"ferard" "fermat" "205" polynomial`
- `"phi13" "Fermat" "2014"`
- `"Férard" "4^" irreducibility`

No exact prior-family formula was verified by these queries. The absence
of a located formula is not evidence of novelty.
