# Official B4 open-portion audit

Checked directly against the B4 blocks on page 2 of all nine cached official Paper B PDFs on 2026-10-16. `tools/audit_open_scope.py` records each source URL, SHA-256 hash, page number and short designation excerpt in [open-scope-audit.json](open-scope-audit.json). Original download hashes are also recorded in [retrieval.json](retrieval.json).

| Year | Official designation | Authorized target |
|---|---|---|
| [2017 official paper](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-2_1.pdf) | B4 described as open; 2018 separately identifies m=5 as already known | Entire B4: determine both normalized tiling-count limits. |
| [2018 official paper](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2018-paper-b_1.pdf) | B4 described as open; 2018 separately identifies m=5 as already known | General enumeration for arbitrary positive m,n. The already known m=5 preliminary case is excluded as a research target. |
| [2019 official paper](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-paper-b_1.pdf) | Only part (b) described as open | B4(b) only: determine the binary-string exponential liminf and limsup. |
| [2020 official paper](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2020-paper-b_1.pdf) | Only part (b) described as open | B4(b) only: classify all taut integers. |
| [2021 official paper](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf) | Only part (b) described as open | B4(b) only: classify degrees with the stated rational common-root property. |
| [2022 official paper](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2022-paper-b.pdf) | Only part (b) described as open | B4(b) only: decide whether every admissible recurrence orbit reaches equality. |
| [2023 official paper](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2023_paper_b.pdf) | Only part (b) described as open | B4(b) only: classify exponent pairs allowing a real r of either sign. |
| [2024 official paper](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf) | Only part (b) described as open | B4(b) only: classify all odd exponents admitting the stated factorization modulo two. |
| [2025 official paper](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2025_paper_b.pdf) | Only part (b) described as open | B4(b) only: classify integer solutions of the general geometric-sum perfect-power equation. |

## Scope and current status

The user's clarification excludes all preliminary part (a) investigations. Previously solved preliminary facts may be cited as context for the open target, but are not research deliverables. For 2018, the known m=5 case is only a consistency check for a general formula. The statement files have been narrowed to the open targets and required definitions. A1-A4 and B1-B3 are excluded entirely from investigation. 2026 is deferred.

The official labels describe openness **when each paper was issued**. They do not prove that a problem remains unsolved today. Current primary-literature checks are separately recorded by year. A potentially applicable general 2018 formula predating the competition has been located and is being checked for exact statement fidelity; it must be attributed, not presented as new research.

## Reproduce

```sh
python3 tools/fetch_official.py
python3 tools/audit_open_scope.py
```

PDF parsing requires `pypdf==6.10.0` in the inspected bundled runtime. The audit searches only the B4 block for the explicit designation; it is supplemented by direct reading of each full B4 statement. It is a scope check, not proof verification or a literature-status determination.

