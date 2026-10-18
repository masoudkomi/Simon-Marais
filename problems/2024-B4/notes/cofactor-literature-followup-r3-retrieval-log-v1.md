# Retrieval and operation log

Date: 2026-10-18 UTC. Scope: public literature discovery only; no mathematical program, CAS, factorization, enumeration, author rerun, Git operation or peer-review access.

1. Searched the exact DOI, exact HAL ID, exact title and author, and GAATI publication links. Read the GAATI institutional publication entry for the 2017 sequel, the primary Springer landing page/abstract/reference list, and the primary AIMS 2014 landing page/abstract. Search results and bibliographic metadata do not substitute for a full theorem read.
2. Web opens of `https://hal.science/hal-03417811`, the DOI redirect, the UPF HAL landing page and `/document` did not return a manuscript. Their errors are recorded as tool retrieval failures, not assertions about a mathematical theorem.
3. Successful native public metadata command (no file output):

```sh
curl -L --fail --silent --show-error --connect-timeout 10 --max-time 30 'https://api.archives-ouvertes.fr/search/?q=halId_s%3Ahal-03417811&fl=title_s%2Curi_s%2CfileMain_s%2Cfiles_s%2CopenAccess_bool%2Cabstract_s%2CdoiId_s&wt=json'
```

The initial tool returned session 28140; its bounded poll completed with exit 0 and the JSON transcribed in the source record. No paper was downloaded.

4. A second successful command, also exit 0 without a file output, requested `docid,halId_s,version_i,submitType_s,fileMain_s,files_s,linkExtUrl_s,arxivId_s,authFullName_s,docType_s,licence_s,keyword_s,abstract_s,openAccess_bool,producedDate_s,submittedDate_s` from the same public search endpoint. It identified a notice and supplied no manuscript field. Its JSON is transcribed separately in the source record.
5. Read the GAATI member page; Férard was listed without a personal-page link. The guessed `https://gaati.org/ferard/` was not accessible through the web tool. No directory crawl or access bypass was attempted.
6. Exact failed AIMS source-discovery command:

```sh
curl -L --fail --silent --show-error --connect-timeout 10 --max-time 30 'https://www.aimsciences.org/article/doi/10.3934/amc.2014.8.497' | rg -o '.{0,100}(pdf|PDF|download).{0,180}'
```

The sandboxed invocation returned `curl: (6) Could not resolve host: www.aimsciences.org`, overall exit 1 from the pipeline. The escalated retry was submitted with the same bounded command and an explicit public-source justification. It returned only `aborted by user after 2610.3s`; there was no successful source output, PID, session identifier or download. The parent then interrupted this logical turn for recovery. The exact source retrieval was **not** reissued.
7. Recovery at approximately 09:29 UTC: reported the operational stall to the coordinator, re-read AGENTS.md, confirmed this new literature prefix was unused, and checked the declared parent fingerprints. `ps -axo pid,ppid,etime,args` returned `operation not permitted`; it was not escalated because no PID-specific cleanup was needed or possible. No global kill was attempted. This is not evidence that every possible process has stopped.
8. Froze a literature-only note and source/read-limit record. The 2017 full body, exact theorem thresholds/exceptional forms and operative proofs remain unread. The 2014 body was not newly retrieved. No source PDF was saved or hashed in this pass; the freeze hashes bind only the worker's new records and explicitly named immutable parents.

Budget: coordinator reported authoritative 21% total weekly use at 09:27:42 UTC, reset 1792874445, ceiling 90% total with integration reserve. No automatic later-window authorization is inferred. Requested gpt-6.1-sol/max is recorded separately from unavailable effective readback. No charges, author contact or access bypass.
