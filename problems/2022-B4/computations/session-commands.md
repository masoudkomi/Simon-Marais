# 2026-10-16 command record

All commands used the repository root as working directory. Primary search
queries and URLs are in ../references.md; the main computations and their
exact invocations are in README.md. No shell command changed shared files.

The read-only environment/source checks included:

```sh
command -v pdftotext
ls -l .cache/official/2022-paper_b.pdf .cache/official/2022-solutions.pdf .venv/bin/python
.venv/bin/python -c 'import sys; print(sys.version); import pypdf; r=pypdf.PdfReader(".cache/official/2022-paper_b.pdf"); s=r.pages[1].extract_text(); print(s[s.find("B4."):])'
cat requirements-research.txt
git diff --check -- problems/2022-B4
git status --short -- problems/2022-B4
```

The source extraction was used only to verify B4(b)'s statement and scope.
No preliminary proof or other problem was researched. `pdftotext` returned
exit 1 (unavailable); the pypdf command succeeded with Python 3.12.14.

Before the reusable continuation script was written, this exact ad hoc
command produced the preserved `random-256-continued.json`:

```sh
.venv/bin/python -c 'import json; from pathlib import Path; from importlib.machinery import SourceFileLoader; m=SourceFileLoader("s","problems/2022-B4/computations/exact_search.py").load_module(); p=Path("problems/2022-B4/computations/random-256.json"); j=json.loads(p.read_text()); out=[]; [(out.append({"a0":r["a0"],"b0":r["b0"],"result":m.iterate(r["a0"],r["b0"],20000,8192)})) for r in j["records"] if "status" in r]; Path("problems/2022-B4/computations/random-256-continued.json").write_text(json.dumps({"step_cap":20000,"bit_cap":8192,"evidence_only":True,"results":out},indent=2)+"\n"); print(out); print("mean first hit",sum(int(k)*v for k,v in j["histogram"].items())/j["counts"]["hit"])'
```

It returned a hit at 5,119; the mean first hit among the initial 9,999
completed random runs was 1769.4557455745576. The reusable script later
reproduced the exact continuation and added boundary checks.

The first residue graph output checked r=0,...,18 in the delay family
(2,280 triples). The final script broadened this to r=0,...,19 (2,400
triples), added reverse BFS and the analytic-policy evidence, and was
rerun. No failed/incomplete mathematical search is hidden: the only
individual capped orbit was explicitly continued, and all four parameter
enumerations completed inside their time cap. All outputs are finite
evidence; all partial proofs retain unverified status.
