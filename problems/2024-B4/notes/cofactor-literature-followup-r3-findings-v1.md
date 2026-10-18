# 2024 B4(b): Férard sequel source follow-up

Status: literature-only checkpoint; no new mathematical claim or novelty determination.

Worker C; checked 2026-10-18 UTC. Requested setting: gpt-6.1-sol/max; effective setting readback unavailable. This note is separate from the immutable cofactor-global-r2 whole review and supplies no repair of its proof. The coordinator's message confirming both whole review freezes ended that review's blindness boundary; no corresponding peer review was opened in this follow-up.

## 1. The exact 2017 publication is identified

Éric Férard, “On the irreducibility of the hyperplane sections of Fermat varieties in P³ in characteristic 2. II,” *Cryptography and Communications* **9** (2017), 749–767, DOI [10.1007/s12095-017-0213-1](https://doi.org/10.1007/s12095-017-0213-1). The [primary publisher page](https://link.springer.com/article/10.1007/s12095-017-0213-1) gives publication on 14 February 2017 and the November 2017 issue. The [GAATI institutional list](https://gaati.org/publications/fr/) links this exact DOI to [HAL hal-03417811v1](https://upf.hal.science/hal-03417811v1).

The accessible publisher abstract concerns the whole polynomial φ_t for t ≥ 3, t ≡ 1 (mod 4). It announces sufficient conditions involving the largest odd divisor of t−1: a size condition and exclusion of a particular form. Neither condition is displayed precisely in the accessible abstract. The page explicitly describes itself as subscription preview. This reading does **not** establish an exact threshold, the exceptional form, endpoint hypotheses, or any operative proof.

## 2. HAL is a notice, not a retrieved author manuscript

Two bounded, successful public API requests to `api.archives-ouvertes.fr/search/` identify this same record. The first returns `openAccess_bool: false`, the exact title/DOI and UPF URI, with no `fileMain_s` or `files_s` values. The second additionally returns:

```
docid: 3417811
halId_s: hal-03417811
version_i: 1
submitType_s: notice
docType_s: ART
submittedDate_s: 2021-11-05 22:26:18
producedDate_s: 2017-11
openAccess_bool: false
```

The API responses are preserved as transcribed returned JSON in the companion source record. No public author-manuscript URL was returned. This establishes the metadata-only status of **that HAL record**, not nonexistence of an author copy elsewhere.

HAL landing/document URLs failed in the web tool; the public API nevertheless completed normally through bounded native curl. A missing web-tool response is not itself an access prohibition or a theorem statement.

## 3. Adjacent sources and honest read limits

The [2014 primary AIMS page](https://www.aimsciences.org/article/doi/10.3934/amc.2014.8.497), DOI 10.3934/amc.2014.8.497, was read at landing-page/abstract level only in this pass. Its abstract describes a t ≡ 5 (mod 8) whole-irreducibility criterion, a φ_13 divisibility conclusion in the stated setting, and an infinite reducible family. The actual theorem and proof were **not** newly retrieved here. It cannot be used here to fill the missing 2017 hypotheses or to certify a family outside that stated residue setting.

The GAATI member list contains Férard's name but no linked personal page. A guessed `/ferard/` URL was not readable through the web tool. The exact-title/DOI searches located the institutional listing, publisher page, bibliographic records and a ResearchGate abstract page explicitly reporting no full text. No author was contacted, and no paid or restricted content was obtained. Bibliographic/aggregator hits were discovery aids only.

## 4. Operational interruption and conclusion

A sandboxed curl of the public AIMS HTML failed with DNS error 6. The required escalated retry, still using a 30-second network cap, was then held at the tool/approval layer and returned only `aborted by user after 2610.3s`. It supplied no PID, session identifier, article output or saved file. The 30-second curl cap does not bound an approval wait before execution. This interval was an operational stall, not sustained mathematical work. The source was not retried after recovery. A read-only process inspection was denied by the sandbox; no process cleanup or absence of a background process is claimed. No file output was requested by either AIMS command.

**The 2017 body remains UNREAD.** The exact accessible abstract is relevant enough that novelty or subsumption cannot responsibly be settled from this search. No new irreducibility theorem, comparison theorem, or absence-of-prior-art assertion is made. A legitimate public full manuscript or exact primary theorem context is still needed for a rigorous comparison. All previous constructor/review bytes remain unchanged.
