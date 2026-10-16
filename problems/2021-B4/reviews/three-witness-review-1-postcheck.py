#!/usr/bin/env python3
"""Post-run comparisons and primary-source provenance, without author imports."""
from datetime import datetime, timezone
import gzip
import hashlib
import json
import math
from pathlib import Path

root=Path(__file__).resolve().parents[3]
prefix=Path(__file__).with_name("three-witness-review-1")
comps=root/"problems/2021-B4/computations"
own=json.loads(Path(str(prefix)+"-full-result.json").read_text())
author=json.loads((comps/"coordinator-three-witness-v2-result.json").read_text())
assert own["polynomial_stream_sha256"]==author["polynomial_stream_sha256"]=="aa5cd774ea5d10dcbb52a5bcee0d289d807ec7a364fd5921f29c9b412dda8cad"
assert own["uncompressed_certificate_stream_sha256"]==author["uncompressed_certificate_stream_sha256"]=="4befc080569dbe0d4d978efaef502e51f644163d15ef9bd22ae7112cf1840387"
assert own["chunks"]==author["chunks"]
assert sum(c["rows"] for c in own["chunks"])==1493024
assert own["compressed_bytes"]==9431158
expected={"0":772,"101":1416728,"103":71108,"107":4109,"109":297,"127":9,"131":1}
assert own["certificate_histogram"]==expected
assert {**{k:v for k,v in expected.items() if k not in ("0","131")},"constant_nonzero":772}==author["resolution_histogram"]
for p in (101,103,107,109,127,131):
    assert all(p%d for d in range(2,math.isqrt(p)+1))
assert author["unresolved"]==1 and author["resolved"]==1493023
unresolved=json.loads((comps/"coordinator-three-witness-v2-unresolved.jsonl").read_text())
sentinel=own["sentinel"][0]
assert (unresolved["center_mask"],unresolved["u_mask"],unresolved["P"],unresolved["Q"])==(sentinel["mask"],sentinel["U_mask"],sentinel["P"],sentinel["Q"])
resolution=json.loads((comps/"coordinator-three-witness-v2-resolve-result.json").read_text())
assert resolution["resolved"]==1 and resolution["unresolved"]==0 and len(resolution["cases"])==1
r=resolution["cases"][0]
assert (r["center_mask"],r["u_mask"],r["prime"],r["degrees"],r["leading_residues"],r["gcd_degree"])==(6436,24785,131,[16,20],[8,102],0)
raw_sentinels=[]
for chunk in own["chunks"]:
    with gzip.open(root/chunk["path"],"rt") as stream:
        for line in stream:
            row=json.loads(line)
            if row[2]==-1:
                raw_sentinels.append(row)
assert raw_sentinels==[[6436,24785,-1]]
paths=["AGENTS.md","problems/2021-B4/statement.md",
       "problems/2021-B4/notes/rational-witness-p-plus-one-v1.1.md",
       "problems/2021-B4/notes/padic-rational-newton-obstructions-v1.md",
       "problems/2021-B4/notes/coordinator-newton-degeneration-v1.md",
       ".cache/official/2021-paper_b.pdf",
       ".cache/literature/2021/cited-66c5af6a0f0239f5.pdf",
       ".cache/literature/2021/massri-1806.09561v6.pdf",
       ".cache/literature/2021/draisma-de-jong-newsletter-2011-06-80.pdf",
       ".cache/literature/2021/newton-review-1-stoll-padic-analysis.pdf",
       ".cache/literature/2021/poonen-curves.pdf"]
result={"verified_at_utc":datetime.now(timezone.utc).isoformat(),
        "all_polynomial_and_certificate_stream_hashes_match":True,
        "all_25_chunk_hashes_and_counts_match":True,
        "certificate_prime_primality_checked_by_trial_division":True,
        "initial_and_final_resolution_histograms_match":True,
        "sentinel_row_and_both_integer_polynomials_match_exactly":True,
        "separate_mod131_resolver_agrees_with_independent_regeneration":True,
        "raw_sentinel_rows":raw_sentinels,
        "source_hashes":{p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in paths},
        "primary_source_reading":{
          "CLO":{"url":"https://arxiv.org/abs/1208.5404","pdf_pages_one_based":[2,3,4,5,7,12,13,14,15],
                 "used":"Section 3.4 equations (9)-(10), Lemma 17; recycled-root definition; Proposition 10; Hasse definition and good-prime lists"},
          "Massri_v6":{"url":"https://arxiv.org/abs/1806.09561v6","pdf_pages_one_based":[12,13,14],
                       "used":"Remark 7.4 and Theorem 7.10 attribution checked only; not a mathematical dependency"},
          "Draisma_de_Jong":{"url":"https://www.ems-ph.org/journals/newsletter/pdf/2011-06-80.pdf","pdf_pages_one_based":[33,34],
                             "used":"Proposition 6 and its proof; separate later corrected degree-family assertion not used"},
          "Stoll":{"url":"https://mathe2.uni-bayreuth.de/stoll/teaching/pAdicAnalysis-WS2015/Skript-pAdicAnalysis-pub-print.pdf",
                   "pdf_pages_one_based":[15,16],"used":"Theorem 3.6 explicitly counts roots with multiplicity"},
          "Poonen":{"url":"https://math.mit.edu/~poonen/papers/curves.pdf","pdf_pages_one_based":[68],
                    "used":"Section 4.2.1 supporting-line convention and theorem; Stoll used for explicit multiplicities"},
          "official_2021_B4":{"url":"https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf",
                              "pdf_pages_one_based":[2],"used":"Only B4(b) scope checked; no preliminary case solved"}},
        "source_access_failure_preserved":"Web screenshot requests for Massri v6 PDF pages 13 and 14 failed with Cache miss; complete cached primary pages were read successfully via pypdf. No mathematical input was inferred from the failed screenshots.",
        "telemetry":{"observed_used_percent_start":9,"observed_used_percent_after_full_run":9,
                     "weekly_window_minutes":10080,"reset_unix_seconds":1792745187,"stop_at_total_used_percent":90},
        "requested_model":"gpt-6.1-sol","requested_reasoning_effort":"max",
        "verified_effective_model_or_effort":None}
Path(str(prefix)+"-postcheck-result.json").write_text(json.dumps(result,indent=2)+"\n")
candidate_manifest=root/"problems/2021-B4/notes/coordinator-three-rational-witnesses-v1-manifest.json"
frozen=json.loads(candidate_manifest.read_text())
for artifact in frozen["artifacts"]:
    path=root/artifact["path"]
    assert path.stat().st_size==artifact["bytes"]
    assert hashlib.sha256(path.read_bytes()).hexdigest()==artifact["sha256"]
manifest_path=Path(str(prefix)+"-manifest.json")
artifacts=[]
for path in sorted(prefix.parent.glob(prefix.name+"*")):
    if path.is_file() and path!=manifest_path:
        artifacts.append({"path":str(path.relative_to(root)),"bytes":path.stat().st_size,
                          "sha256":hashlib.sha256(path.read_bytes()).hexdigest()})
manifest={"completed_at_utc":datetime.now(timezone.utc).isoformat(),
          "review":"R1 complete independent adversarial audit; no unresolved substantive objections",
          "candidate_sha256":"be91345a8511338d55f30b140ee2555698c21d0e341efe29fe2536bca4fffbda",
          "candidate_manifest_sha256":hashlib.sha256(candidate_manifest.read_bytes()).hexdigest(),
          "candidate_artifacts_checked_before_and_after":len(frozen["artifacts"]),
          "candidate_artifacts_unchanged":True,
          "claims":{"T1":"accepted subject to frozen dependencies and coordinator promotion gate",
                    "T2":"accepted conditional on T1 and frozen normalization/Newton inputs",
                    "T3":"accepted conditional on T1 and frozen normalization/Newton inputs"},
          "full_families_independently_regenerated_and_verified":1493024,
          "open_substantive_issues":0,"author_repairs_requested":0,
          "peer_reports_or_conclusions_read":False,"constructor_modules_imported_or_executed":False,
          "independent_core_written_and_run_before_raw_certificates":True,
          "independent_core_sha256_before_and_after":"ed98ed514ac6dffa20e3c5779d7851437003326992f0619018f1837147386464",
          "full_child_pid":34054,"external_timeout_seconds":420,"full_child_exit_code":0,
          "full_child_reaped":True,"full_job_elapsed_seconds":127.62004133299342,
          "source_provenance_file":str(Path(str(prefix)+"-postcheck-result.json").relative_to(root)),
          "requested_model":"gpt-6.1-sol","requested_reasoning_effort":"max",
          "verified_effective_model_or_effort":None,"artifacts":artifacts}
manifest_path.write_text(json.dumps(manifest,indent=2)+"\n")
print(json.dumps({k:v for k,v in result.items() if k.endswith("match") or k.endswith("matches") or k.endswith("checked_by_trial_division") or k.endswith("regeneration")}))
print(json.dumps({"review_manifest":str(manifest_path.relative_to(root)),"artifacts":len(artifacts),
                  "candidate_artifacts_unchanged":True}))
